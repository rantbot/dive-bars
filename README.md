# The American Dive Bar

A five-minute lightning talk in the style of a prestige nature documentary, about the American dive bar. It runs in the browser, with ambient sound for each scene that crossfades as the slides advance.

## Presenting

Open `index.html` (or the GitHub Pages site), click **Begin · Sound on**, then advance with the arrow keys or a presentation clicker.

| Key | Action |
| --- | --- |
| → / Space / Page Down | Next slide or build |
| ← / Page Up | Previous |
| P | Presenter view (opens a private window with your notes, the next slide and a timer) |
| N | Speaker notes on the main screen |
| M | Mute |
| F | Full screen |

## Presenting while screen sharing

1. Open the site and click **Begin · Sound on**.
2. Press **P**. A presenter window opens with your notes, a preview of the next slide and a timer.
3. In your video call, share only the first tab. Keep the presenter window to yourself.
4. Advance from either window. They stay in sync.

Refreshing a tab keeps you on the same slide. Opening the site fresh starts at the title card.

## What's in here

- `index.html` holds the slides, styles, and the sound engine. Most ambience is synthesized live with the Web Audio API.
- `snd/` holds the field recordings: neighborhood chatter, a bar room loop, and a biker bar late at night.
- `img/` holds the photographs and illustrations. Most photos are low-resolution stand-ins to be replaced with real field photos.

Fonts load from Google Fonts. The audio files load with `fetch`, so open the page through a web server (GitHub Pages works) rather than straight from disk.
