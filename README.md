# The American Dive Bar

A five-minute lightning talk in the style of a prestige nature documentary, about the American dive bar. It runs in the browser, with ambient sound for each scene that crossfades as the slides advance.

## Presenting

1. Open the site and click **Begin · Sound on**. Your notes window opens at the same moment. If your browser blocks it, allow pop-ups for the site and press **P**.
2. In your video call, share only the presentation tab. It shows no controls, just the slides.
3. Run everything from the notes window: Back and Next, sound on or off, volume and the talk timer. Arrow keys and clickers work in either window, and the two stay in sync.

Refreshing a tab keeps you on the same slide. Opening the site fresh starts at the title card.

## What's in here

- `index.html` holds the slides, styles, and the sound engine. Most ambience is synthesized live with the Web Audio API.
- `snd/` holds the field recordings: neighborhood chatter, a bar room loop, and a biker bar late at night.
- `img/` holds the photographs and illustrations. Most photos are low-resolution stand-ins to be replaced with real field photos.

Fonts load from Google Fonts. The audio files load with `fetch`, so open the page through a web server (GitHub Pages works) rather than straight from disk.
