#!/usr/bin/env python3
"""Make the room sound and music under each chapter with ElevenLabs.

Edit narration/soundscapes.json and run this (the GitHub Action runs it on every push that changes it).
Only beds whose prompt, length or kind changed are made again. snd/scenes/made.json keeps track.
A bed that fails is reported and skipped, so it never holds up the narration.

Options:  --only lineage   --force   --dry-run
"""
import hashlib, json, os, sys, time, urllib.request, urllib.error
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, 'narration', 'soundscapes.json')
LEDGER = os.path.join(ROOT, 'snd', 'scenes', 'made.json')
SECRETS = os.path.join(ROOT, 'narration', '.elevenlabs.json')
args = sys.argv[1:]
only = args[args.index('--only') + 1] if '--only' in args else None
force, dry = '--force' in args, '--dry-run' in args

def warn(msg):
    if os.environ.get('GITHUB_ACTIONS'): print('::warning title=Room sound::' + msg.replace('\n', ' '))
    else: print('Warning:', msg)

spec = json.load(open(SPEC, encoding='utf-8'))
ledger = json.load(open(LEDGER)) if os.path.exists(LEDGER) else {}
saved = json.load(open(SECRETS)) if os.path.exists(SECRETS) else {}
key = os.environ.get('ELEVEN_API_KEY') or saved.get('apiKey')
if not key and not dry: sys.exit('Missing the ElevenLabs API key (repository secret ELEVEN_API_KEY).')

def fingerprint(b): return hashlib.sha1(json.dumps({k: b.get(k) for k in ('kind', 'prompt', 'seconds')}, sort_keys=True).encode()).hexdigest()[:16]

def call(url, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method='POST',
                                 headers={'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=300) as r: return r.read()
        except urllib.error.HTTPError as e:
            msg = e.read().decode('utf-8', 'replace')[:300]
            if e.code in (429, 500, 502, 503) and attempt < 3: time.sleep(5 * (attempt + 1)); continue
            raise RuntimeError('ElevenLabs said %s: %s' % (e.code, msg))
        except urllib.error.URLError as e:
            if attempt < 3: time.sleep(5 * (attempt + 1)); continue
            raise RuntimeError('Could not reach ElevenLabs: %s' % e.reason)

def make(b):
    if b['kind'] == 'music':
        return call('https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128',
                    {'prompt': b['prompt'], 'music_length_ms': int(b.get('seconds', 45) * 1000), 'model_id': 'music_v1'})
    return call('https://api.elevenlabs.io/v1/sound-generation?output_format=mp3_44100_128',
                {'text': b['prompt'], 'duration_seconds': min(30, b.get('seconds', 22)), 'prompt_influence': 0.45,
                 'loop': True, 'model_id': 'eleven_text_to_sound_v2'})

made = skipped = failed = 0
wanted = set()
for scene, beds in spec['beds'].items():
    for b in beds:
        f = b['file']; wanted.add(f); fp = fingerprint(b); path = os.path.join(ROOT, f)
        if only and scene != only: continue
        if not force and os.path.exists(path) and ledger.get(f) == fp: skipped += 1; continue
        print('Making', f, '(%s, %ss)' % (b['kind'], b.get('seconds')))
        if dry: made += 1; continue
        try:
            audio = make(b)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path + '.part', 'wb').write(audio); os.replace(path + '.part', path)
            ledger[f] = fp; made += 1
            json.dump(dict(sorted(ledger.items())), open(LEDGER, 'w'), indent=2)
        except Exception as e:
            failed += 1; warn('%s was not made. %s' % (f, e))
if not dry and not only:
    for f in list(ledger):
        if f not in wanted:
            ledger.pop(f)
            if os.path.exists(os.path.join(ROOT, f)): os.remove(os.path.join(ROOT, f)); print('Removing', f)
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    json.dump(dict(sorted(ledger.items())), open(LEDGER, 'w'), indent=2)
print('Room sound: %d made, %d unchanged, %d failed.' % (made, skipped, failed))
