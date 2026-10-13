# The American Dive Bar

A five-minute lightning talk in the style of a prestige nature documentary, about the American dive bar. It runs in the browser, with ambient sound for each scene that crossfades as the slides advance.

## Presenting

1. Open the talk at `/dive-bars/lightning/` and click anywhere on the dark screen. Your notes window opens and the sound turns on. The title stays hidden until the narration starts, so the room sees it fade in. The presentation stays in a normal window. To go full screen, press **Full screen** in the notes window or press **F** in the presentation window. In the notes window, press **Next** once to play the narrator over the title card, and again to bring up slide 1. If your browser blocks it, allow pop-ups for the site and press **P**.
2. In your video call, share only the presentation tab. It shows no controls, just the slides.
3. Run everything from the notes window: Back and Next, sound on or off, volume and the talk timer. Arrow keys and clickers work in either window, and the two stay in sync.

Refreshing a tab keeps you on the same slide. Opening the site fresh starts at the title card.

## The film

**The site's home page (`index.html`)** is the film, the standalone version for people to watch on their own. It plays like a film: one narrator tells the whole story, the slides reveal on cue with the voice, and captions run underneath. Viewers can pause, skip between the twenty chapters, turn captions off and go full screen. It is built from the lightning talk with four scenes from the full version added back (the Working-Class Dive, the Currency Ceiling, the Late-Night Dive and Local Adaptations).

- `narration/clips.json` holds every line of narration, in order. Edit a line there and record that clip again. `[*]` marks the word where something on the slide appears.
- `narration/recording-script.md` has the voice direction and pronunciation guide. The words in `clips.json` win if the two differ.
- `narration/generate.py` records the narration with ElevenLabs into `snd/film/`. It only records lines whose words changed, reuses lines that only moved, and removes recordings the script no longer uses. `narration/recorded.json` keeps track. A new line can leave out `file` and gets a name automatically.

**Regenerating the voice after a script change.** Edit the words in `narration/clips.json`, then either:

1. Double-click **Record narration.command** in the dive-bars folder. The first time, it asks for your ElevenLabs API key (kept on your Mac in `narration/.elevenlabs.json`, never committed) and the narrator's voice ID (saved in `clips.json`). Then commit and push in GitHub Desktop.
2. Or just commit and push. The **Record narration** GitHub Action records the changed lines and commits them back. It needs the API key once, in the repo's Settings, Secrets and variables, Actions, as a secret named `ELEVEN_API_KEY`, and the voice ID filled in at the top of `clips.json`. Pull in GitHub Desktop afterwards to get the new recordings.

At the end, a field journal asks viewers for a favorite dive bar and a protocol of their own. Their notes go up on the bathroom wall, a pan-and-zoom page that opens after someone logs a note, from Read the wall on the end card, or at `/dive-bars/#wall`. The notes live in a free Supabase project. Run `supabase/field_notes.sql` in its SQL editor (it's safe to run again after changes). To take a note off the wall, tick `hidden` on its row in the Table editor.

Until a clip is recorded, the film shows its line as a caption and moves on after about as long as it would take to say it, so the film can be watched from start to finish at any point.

## What's in here

- `lightning/index.html` holds the talk's slides, styles, and the sound engine. The film is built from it, so the two share the same slides. Most ambience is synthesized live with the Web Audio API.
- `snd/` holds the field recordings: neighborhood chatter, a bar room loop, and a biker bar late at night.
- `img/` holds the photographs and illustrations. Most photos are low-resolution stand-ins to be replaced with real field photos.

Fonts load from Google Fonts. The audio files load with `fetch`, so open the page through a web server (GitHub Pages works) rather than straight from disk.

## Two versions

- **lightning/index.html** is the five-minute lightning talk (16 slides), at `/dive-bars/lightning/`.
- **lightning/full.html** is the full twelve-minute talk with every slide.
- **film.html** only forwards old links to the film.
