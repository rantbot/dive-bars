#!/usr/bin/env python3
"""Record the film's narration with ElevenLabs.

Run it from the dive-bars folder in Terminal:

    ELEVEN_API_KEY=your-key ELEVEN_VOICE_ID=your-voice-id python3 narration/generate.py

It reads narration/clips.json and writes one MP3 per clip into snd/film/.
Clips that already exist are skipped, so you can run it again after a hiccup.

    --only anatomy        record just one scene (use the scene id from clips.json)
    --force               record again even if the file exists
    --dry-run             show what would be recorded, without calling ElevenLabs

Your API key never gets saved anywhere. It only lives in that one Terminal command.
"""
import json, os, sys, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = sys.argv[1:]
only = args[args.index('--only') + 1] if '--only' in args else None
force, dry = '--force' in args, '--dry-run' in args

data = json.load(open(os.path.join(ROOT, 'narration', 'clips.json'), encoding='utf-8'))
key, voice = os.environ.get('ELEVEN_API_KEY'), os.environ.get('ELEVEN_VOICE_ID')
if not dry and not (key and voice):
    sys.exit('Set ELEVEN_API_KEY and ELEVEN_VOICE_ID first. See the top of this file.')

settings = dict(data['voiceSettings'])
model = settings.pop('model_id')

def spoken(text):
    text = text.replace('[*]', '')
    for written, said in data.get('say', {}).items():
        text = text.replace(written, said)
    return ' '.join(text.split())

def record(text, prev_text, next_text, path):
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
            open(path, 'wb').write(audio)
            return
        except urllib.error.HTTPError as e:
            msg = e.read().decode('utf-8', 'replace')[:300]
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(4 * (attempt + 1)); continue
            sys.exit('ElevenLabs said %s: %s' % (e.code, msg))

done = skipped = 0
for scene in data['scenes']:
    if only and scene['id'] != only:
        continue
    texts = [spoken(c['text']) for c in scene['clips']]
    for k, clip in enumerate(scene['clips']):
        path = os.path.join(ROOT, clip['file'])
        if os.path.exists(path) and not force:
            skipped += 1; continue
        print('Recording', clip['file'], '·', texts[k][:60] + ('…' if len(texts[k]) > 60 else ''))
        if not dry:
            record(texts[k], ' '.join(texts[:k])[-500:], ' '.join(texts[k + 1:])[:500], path)
        done += 1
print('Done. %d recorded, %d already there.' % (done, skipped))
