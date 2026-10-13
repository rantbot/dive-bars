# The American Dive Bar

A five-minute lightning talk in the style of a prestige nature documentary, about the American dive bar. It runs in the browser, with ambient sound for each scene that crossfades as the slides advance.

## Presenting

1. Open the site and click anywhere on the dark screen. Your notes window opens and the sound turns on. The title stays hidden until the narration starts, so the room sees it fade in. The presentation stays in a normal window. To go full screen, press **Full screen** in the notes window or press **F** in the presentation window. In the notes window, press **Next** once to play the narrator over the title card, and again to bring up slide 1. If your browser blocks it, allow pop-ups for the site and press **P**.
2. In your video call, share only the presentation tab. It shows no controls, just the slides.
3. Run everything from the notes window: Back and Next, sound on or off, volume and the talk timer. Arrow keys and clickers work in either window, and the two stay in sync.

Refreshing a tab keeps you on the same slide. Opening the site fresh starts at the title card.

## The film

**film.html** is the standalone version for people to watch on their own. It plays like a film: one narrator tells the whole story, the slides reveal on cue with the voice, and captions run underneath. Viewers can pause, skip between the twenty chapters, turn captions off and go full screen. It is built from the lightning talk with four scenes from the full version added back (the Working-Class Dive, the Currency Ceiling, the Late-Night Dive and Local Adaptations).

- `narration/clips.json` holds every line of narration, in order. Edit a line there and record that clip again. `[*]` marks the word where something on the slide appears.
- `narration/recording-script.md` is the same script laid out for recording, with direction and pronunciation.
- `narration/generate.py` records every clip with ElevenLabs into `snd/film/`. See the top of that file.

At the end, a field journal asks viewers for a favorite dive bar and a protocol of their own. To switch it on, create a free Supabase project, run `supabase/field_notes.sql` in its SQL editor, and put the project URL and its public anon key into `FIELD_NOTES` near the top of the film script. Viewers can only add notes, never read them. You read them in Supabase's Table editor.

Until a clip is recorded, the film shows its line as a caption and moves on after about as long as it would take to say it, so the film can be watched from start to finish at any point.

## What's in here

- `index.html` holds the slides, styles, and the sound engine. Most ambience is synthesized live with the Web Audio API.
- `snd/` holds the field recordings: neighborhood chatter, a bar room loop, and a biker bar late at night.
- `img/` holds the photographs and illustrations. Most photos are low-resolution stand-ins to be replaced with real field photos.

Fonts load from Google Fonts. The audio files load with `fetch`, so open the page through a web server (GitHub Pages works) rather than straight from disk.

## Two versions

- **index.html** is the five-minute lightning talk (16 slides).
- **full.html** is the full twelve-minute version with every slide, kept for the website.
