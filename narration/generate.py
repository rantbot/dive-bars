#!/usr/bin/env python3
"""Record the film's narration with ElevenLabs, and keep it in step with the script.

Edit the lines in narration/clips.json, then run this. It records only the clips whose words
changed (or that are new), reuses recordings that only moved, and removes ones the script no
longer uses. narration/recorded.json remembers what each MP3 says, so nothing is recorded twice.

Three ways to run it:
  - Double-click "Record narration.command" in the dive-bars folder.
  - In Terminal, from the dive-bars folder:  python3 narration/generate.py
  - Push a change to narration/clips.json. The GitHub Action records it for you (see README).

The first time on your Mac it asks for your ElevenLabs API key and keeps it in
narration/.elevenlabs.json, which never leaves your computer (it is in .gitignore).

Options:
  --only anatomy   record just one scene, by its id in clips.json
  --force          record again even if nothing changed
  --dry-run        show what would happen without calling ElevenLabs
  --keep           leave recordings the script no longer uses
"""
import hashlib, json, os, shutil, sys, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIPS = os.path.join(ROOT, 'narration', 'clips.json')
LEDGER = os.path.join(ROOT, 'narration', 'recorded.json')
SECRETS = os.path.join(ROOT, 'narration', '.elevenlabs.json')
FOLDER = os.path.join(ROOT, 'snd', 'film')

args = sys.argv[1:]
only = args[args.index('--only') + 1] if '--only' in args else None
force, dry, keep = '--force' in args, '--dry-run' in args, '--keep' in args

data = json.load(open(CLIPS, encoding='utf-8'))
ledger = json.load(open(LEDGER, encoding='utf-8')) if os.path.exists(LEDGER) else {}
settings = dict(data['voiceSettings'])
model = settings.pop('model_id')

def credentials():
    saved = json.load(open(SECRETS)) if os.path.exists(SECRETS) else {}
    key = os.environ.get('ELEVEN_API_KEY') or saved.get('apiKey')
    voice = os.environ.get('ELEVEN_VOICE_ID') or data.get('voiceId') or saved.get('voiceId')
    if dry: return key, voice
    if not key and sys.stdin.isatty():
        import getpass
        print('Your ElevenLabs API key is under Profile, API keys in ElevenLabs. It stays on this computer.')
        key = getpass.getpass('API key: ').strip()
        saved['apiKey'] = key; json.dump(saved, open(SECRETS, 'w'), indent=2)
    if not voice and sys.stdin.isatty():
        print("The narrator's voice ID is in ElevenLabs under Voices, the voice's menu, Copy voice ID.")
        voice = input('Voice ID: ').strip()
        data['voiceId'] = voice
        open(CLIPS, 'w', encoding='utf-8').write(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    if not (key and voice):
        sys.exit('Missing the ElevenLabs API key or voice ID. See the top of narration/generate.py.')
    return key, voice

def spoken(text):
    text = text.replace('[*]', '')
    for written, said in data.get('say', {}).items():
        text = text.replace(written, said)
    return ' '.join(text.split())

key, voice = credentials()

def fingerprint(text):
    # What makes a recording: the words, the voice, the model and its settings.
    raw = json.dumps({'text': text, 'voice': voice, 'model': model, 'settings': settings}, sort_keys=True)
    return hashlib.sha1(raw.encode('utf-8')).hexdigest()[:16]

def record(text, prev_text, next_text, path):
    if os.environ.get('NARRATION_FAKE'):   # for testing the bookkeeping without calling ElevenLabs
        os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(text); return
    body = json.dumps({'text': text, 'model_id': model, 'voice_settings': settings,
                       'previous_text': prev_text or None, 'next_text': next_text or None}).encode()
    url = 'https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=mp3_44100_128' % voice
    req = urllib.request.Request(url, data=body, method='POST',
                                 headers={'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                audio = r.read()
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path + '.part', 'wb').write(audio); os.replace(path + '.part', path)
            return
        except urllib.error.HTTPError as e:
            msg = e.read().decode('utf-8', 'replace')[:300]
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(4 * (attempt + 1)); continue
            sys.exit('ElevenLabs said %s: %s' % (e.code, msg))

# A new line in clips.json can leave out "file". It gets a name here, saved back into clips.json.
named = False
for n, scene in enumerate(data['scenes'], 1):
    taken = {c.get('file') for c in scene['clips']}
    for clip in scene['clips']:
        if not clip.get('file'):
            k = 1
            while 'snd/film/%02d-%s-%d.mp3' % (n, scene['id'], k) in taken: k += 1
            clip['file'] = 'snd/film/%02d-%s-%d.mp3' % (n, scene['id'], k); taken.add(clip['file']); named = True
if named and not dry:
    open(CLIPS, 'w', encoding='utf-8').write(json.dumps(data, indent=2, ensure_ascii=False) + '\n')

# Recordings we already have, by what they say, so a line that only moved is copied, not re-recorded.
have = {v: f for f, v in ledger.items() if os.path.exists(os.path.join(ROOT, f))}
wanted, recorded, reused, same = {}, 0, 0, 0
for scene in data['scenes']:
    texts = [spoken(c['text']) for c in scene['clips']]
    for k, clip in enumerate(scene['clips']):
        f, fp = clip['file'], fingerprint(texts[k])
        wanted[f] = fp
        if only and scene['id'] != only:
            continue
        path = os.path.join(ROOT, f)
        if not force and os.path.exists(path) and ledger.get(f) == fp:
            same += 1; continue
        if not force and fp in have and have[fp] != f:
            print('Reusing ', f, '(same words as', have[fp] + ')')
            if not dry: shutil.copyfile(os.path.join(ROOT, have[fp]), path)
            reused += 1; continue
        print('Recording', f, '·', texts[k][:60] + ('…' if len(texts[k]) > 60 else ''))
        if not dry: record(texts[k], ' '.join(texts[:k])[-500:], ' '.join(texts[k + 1:])[:500], path)
        recorded += 1
        if not dry: ledger[f] = fp; json.dump(dict(sorted(ledger.items())), open(LEDGER, 'w'), indent=2)

removed = 0
if not keep and not only and os.path.isdir(FOLDER):
    for name in sorted(os.listdir(FOLDER)):
        f = 'snd/film/' + name
        if name.endswith('.mp3') and f not in wanted:
            print('Removing ', f, '(no longer in the script)')
            if not dry: os.remove(os.path.join(FOLDER, name))
            removed += 1
if not dry:
    for f in list(ledger):
        if f not in wanted or not os.path.exists(os.path.join(ROOT, f)): ledger.pop(f)
    for f, fp in wanted.items():
        if os.path.exists(os.path.join(ROOT, f)) and f not in ledger: ledger[f] = fp
    json.dump(dict(sorted(ledger.items())), open(LEDGER, 'w'), indent=2)
print('Done. %d recorded, %d reused, %d unchanged, %d removed.' % (recorded, reused, same, removed))
