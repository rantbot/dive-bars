# The American Dive Bar · narration

The film plays one narrator over the whole story, the same voice as the opening (`snd/intro.mp3`). Every line below is one clip. Each clip becomes one MP3 in `snd/film/`, named exactly as shown. The film page finds them on its own, and until a clip exists it shows that line as a caption instead.

## The quick way

Record everything with one command in Terminal, from the dive-bars folder. You need your ElevenLabs API key (Profile, API keys) and the voice ID of the opening narrator (Voices, the voice's menu, Copy voice ID).

```
ELEVEN_API_KEY=your-key ELEVEN_VOICE_ID=your-voice-id python3 narration/generate.py
```

It skips clips that already exist, so you can rerun it. To redo one scene, add `--only anatomy --force` with the scene name from the headings below. The key stays in that one command and is never saved.

## By hand in ElevenLabs

Use the same voice as the opening, the Multilingual v2 model, and these settings everywhere so the clips match.

- Stability 50, Similarity 75, Style 20, Speaker boost on
- Paste the **Say** line exactly. Where it differs from the caption, it is spelled the way it should sound.
- Download as MP3 and save it with the file name shown, into `snd/film/`.

## Pronunciation

If ElevenLabs gets one of these wrong, add it to the `say` list in `narration/clips.json` with a respelling (for example `"Malört": "MAHL-urt"`) and record that clip again.

- Diveus (DYE-vee-us), americanus, laboriosus, motorcyclus, nocturnus, artificialis
- Guayaquil (gwy-ah-KEEL)
- pulquería (pool-keh-REE-ah), pulque (POOL-keh)
- boteco (boo-TEH-koo), Comida di Buteco (koh-MEE-dah jee boo-TEH-koo)
- Malört (MAHL-urt)
- Oldenburg, Schlitz, McSorley's

## The clips

### 01 · Habitat (`cover`)

*Warm and unhurried. The first line after the title. A hint of a smile on the last sentence.*

**`01-cover-1.mp3`**

> Since the late 1900s, our researcher has conducted extensive field research into this fragile habitat. Most of it at night. All of it involving beer.

### 02 · Range (`range`)

*Matter-of-fact, like reading from a field log.*

**`02-range-1.mp3`**

> Sixty-eight cities explored, with many dives documented in each, from Vancouver to Guayaquil, spanning both American continents, yet the survey continues to this day.

**`02-range-2.mp3`**

> The U.S. government counts drinking places. However, it has no category for a dive. Diveus americanus remains today, unrecognized by science.

**`02-range-3.mp3`**

> The word itself was never a compliment. By the late 1860s, American newspapers were calling a disreputable drinking den a "dive," possibly because so many of them sat a flight below the street.

### 03 · Anatomy (`anatomy`)

*An anatomy lecture. Each organ is its own short clip, so give each one a small beat of weight.*

**`03-anatomy-1.mp3`**

> Let us examine a specimen up close. Every healthy dive shares eight organs.

**`03-anatomy-2.mp3`**

> An old neon sign.

**`03-anatomy-3.mp3`**

> Light dim enough to forgive you, and what you might've seen.

**`03-anatomy-4.mp3`**

> Beer at exactly one temperature.

**`03-anatomy-5.mp3`**

> A stool that belongs to someone, even when they're not sitting on it.

**`03-anatomy-6.mp3`**

> The beer clock. After Prohibition, Congress barred brewers from giving bar owners anything of value... unless it carried the brewer's name on it. A free clock would be a bribe. A free clock with a beer's name on it... is marketing.

**`03-anatomy-7.mp3`**

> Then hanging on the wall, there is also the thing nobody can explain, there are personal objects left behind as gifts from patrons, and of course, an analog jukebox to create the unique soundtrack found only in this dive.

**`03-anatomy-8.mp3`**

> A real dive is not decorated. It accumulates.

### 04 · Ancestors (`lineage`)

*Slower and straight. This is the one place where the history carries more weight than the joke.*

**`04-lineage-1.mp3`**

> Every known species has ancestors.

**`04-lineage-2.mp3`**

> For the dive bar, it may be the juke joint. In the Jim Crow South, Black workers were shut out of white establishments, so they built their own. An unassuming shack at a crossroads. Music, food, and dancing after a long week.

**`04-lineage-3.mp3`**

> Some historians call this the first private space Black Americans had in this country. The blues grew up there. When record machines came to bars, they took its name. The jukebox.

**`04-lineage-4.mp3`**

> Out west, the honky-tonk was born. Country music is said to have gone electric partly so it could be heard over the rowdy noise.

### 05 · The Neighborhood Dive (`sp1`)

*Affectionate. Dry on "Others, the keg."*

**`05-sp1-1.mp3`**

> Our research has identified five remaining species today.

**`05-sp1-2.mp3`**

> The most widespread is the Neighborhood Dive. Its defining trait is community. The bartender may even start pouring before your order is complete. Some regulars have been observed changing the music. Others, the keg.

### 06 · McSorley's (`mcsorleys`)

*Respectful. Let the last line land quietly.*

**`06-mcsorleys-1.mp3`**

> Here is the Neighborhood Dive in its oldest form. McSorley's Old Ale House in New York's East Village. It claims a birth in 1854 and historic patrons, Abraham Lincoln, Ulysses S. Grant, Teddy Roosevelt, and William Jefferson Clinton.

**`06-mcsorleys-2.mp3`**

> It served men only until 1970, when two lawyers sued and won.

**`06-mcsorleys-3.mp3`**

> Above the bar hang wishbones, said to have been left by soldiers heading to the First World War. The ones still hanging are said to belong to those who never came back.

### 07 · The Working-Class Dive (`sp2`)

*Plain and steady, like the routine it describes. Deadpan on the last line.*

**`07-sp2-1.mp3`**

> In older industrial towns, we find a hardier relative. The Working-Class Dive. Diveus laboriosus.

**`07-sp2-2.mp3`**

> Its defining trait is routine. Activity peaks at shift change. Same people. Same stools. Same drinks. Same time.

**`07-sp2-3.mp3`**

> Researchers have observed individual specimens occupying the same stool for decades. Removing the stool could result in severe ecological disruption.

### 08 · The Destination Dive (`sp3`)

*A memory. Warm, a little wistful.*

**`08-sp3-1.mp3`**

> The Destination Dive. Found on back roads, coastlines, and generally, at the ends of things.

**`08-sp3-2.mp3`**

> This is Jimbo's Place, tucked behind a water treatment plant on Virginia Key in Miami. When our researcher first encountered Jimbo's over two decades ago, they kept no bartender, only a caretaker who occasionally surfaced to restore the habitat, and an old fisherman grilling fresh oysters for guests over a burning barrel. You paid in cash through a slot in a lockbox and pulled your own beer from the cooler.

**`08-sp3-3.mp3`**

> That's not a business. That's a community.

### 09 · The Currency Ceiling (`dollars`)

*Curious, a little conspiratorial. Land the dollar figure clearly.*

**`09-dollars-1.mp3`**

> Some habitats are papered in dollar bills. Why money? Scientists remain divided.

**`09-dollars-2.mp3`**

> In California's Gold Country, regulars tell of miners who signed a bill and tacked it to the ceiling, so they would never come back too broke for a first drink. On the Florida coast, the story involves fishermen, betting a dollar on the day's catch.

**`09-dollars-3.mp3`**

> Aviators had a cousin of the custom. Signed bills called short snorters. Fail to produce yours, and you bought the round.

**`09-dollars-4.mp3`**

> The true origin may be unrecoverable. The money is not. In 2019, staff at the Siesta Key Oyster Bar pulled every bill off the walls. Thirteen thousand, nine hundred and sixty-one dollars. All of it sent to hurricane relief in the Bahamas.

### 10 · The Biker Bar (`biker`)

*Respectful distance. The last line is a firm, friendly warning.*

**`10-biker-1.mp3`**

> The Biker Bar. Identified by the precise row of motorcycles out front.

**`10-biker-2.mp3`**

> Despite its reputation, Diveus motorcyclus is among the most courteous habitats on the continent.

**`10-biker-3.mp3`**

> Researchers are advised to admire the bikes. Never touch the bikes.

### 11 · The Late-Night Dive (`sp4`)

*Nature documentary migration voice. Build through the list, then drop to deadpan for Boston.*

**`11-sp4-1.mp3`**

> Our final species is rarely seen in daylight. The Late-Night Dive. Diveus nocturnus.

**`11-sp4-2.mp3`**

> As midnight approaches, scattered populations begin their nightly migration toward a common watering hole. Restaurant staff, finished with their shifts. Concertgoers. Wedding guests. Patrons of lesser bars that have already closed.

**`11-sp4-3.mp3`**

> By 1:17 a.m., they converge. Here, together, they will make increasingly questionable decisions.

Say: By one seventeen a.m., they converge. Here, together, they will make increasingly questionable decisions.

**`11-sp4-4.mp3`**

> The migration has an earlier phase. Happy hour. The term began among sailors aboard the USS Arkansas in 1913, and caught on during Prohibition. In Massachusetts, it has been illegal since 1984.

**`11-sp4-5.mp3`**

> Boston simply has hours.

### 12 · Fauna (`fauna`)

*Field guide. One beat per species. The last one is the joke.*

**`12-fauna-1.mp3`**

> Every habitat supports its fauna.

**`12-fauna-2.mp3`**

> The Regular. Territorial.

**`12-fauna-3.mp3`**

> The Bartender, the apex species, controlling access to all resources.

**`12-fauna-4.mp3`**

> The Tourist, identified by looking around too much.

**`12-fauna-5.mp3`**

> And the Bachelorette Party. Native species are known to retreat until the disturbance has passed.

### 13 · Local Adaptations (`local`)

*Lively, a travel guide with an inside joke.*

**`13-local-1.mp3`**

> Every population adapts to its environment.

**`13-local-2.mp3`**

> In Chicago, before Prohibition, brewers built saloons of their own. Between 1897 and 1905, Schlitz alone built fifty-seven here. Beer on the ground floor. Upstairs, often, the family who ran the place. Many still stand.

**`13-local-3.mp3`**

> The local ritual is the Chicago Handshake. A shot of Malört, which tastes like a punishment, and an Old Style to recover.

**`13-local-4.mp3`**

> In Wisconsin, the dice cup lives on the bar. Shake of the Day. Beat the bartender, and the next one's free. When three Milwaukee bars tried to ban the dice in 2016, the ban lasted two days.

### 14 · Related Populations (`abroad`)

*Admiring. Say the Spanish and Portuguese words with care.*

**`14-abroad-1.mp3`**

> The genus doesn't stop at the United States border.

**`14-abroad-2.mp3`**

> In Mexico, the pulquería, serving the fermented agave drink the Aztecs held sacred long before the invention of tequila and mezcal. Mexico City once counted about 1,100 pulquerías. Until beer companies and the government spent decades disparaging pulque as unclean and a poor man's drink. Today, only 80 pulquerías remain.

Say: In Mexico, the pulquería, serving the fermented agave drink the Aztecs held sacred long before the invention of tequila and mezcal. Mexico City once counted about eleven hundred pulquerías. Until beer companies and the government spent decades disparaging pulque as unclean and a poor man's drink. Today, only eighty pulquerías remain.

**`14-abroad-3.mp3`**

> In Brazil, the boteco, where bars in 25 cities compete every year in the Comida di Buteco, to name Brazil's best snack and coldest beer.

### 15 · Third Places (`third`)

*Thoughtful. Let the two numbers contrast.*

**`15-third-1.mp3`**

> Sociologist Ray Oldenburg defines these as third places. Home is the first. Work is the second.

**`15-third-2.mp3`**

> In a national survey, Americans who identified with a regular spot were far more likely to talk with someone they don't know well. Forty-eight percent.

**`15-third-3.mp3`**

> Versus only twenty-eight percent for those with no regular third place at all.

### 16 · The False Dive (`falsedive`)

*A warning about an impostor. Dry.*

**`16-falsedive-1.mp3`**

> In your explorations, beware Diveus artificialis, the False Dive. Its camouflage can be quickly identified by its Edison bulbs, its custom neon signs with clever phrases. And of course, a signature $17 cocktail.

Say: In your explorations, beware Diveus artificialis, the False Dive. Its camouflage can be quickly identified by its Edison bulbs, its custom neon signs with clever phrases. And of course, a signature seventeen-dollar cocktail.

**`16-falsedive-2.mp3`**

> While attempts have been made to breed the false dive in captivity, they have largely failed.

### 17 · The Diagnostic (`test`)

*Quiet. Ask the two questions slowly. Silence follows.*

**`17-test-1.mp3`**

> Today, there is one simple diagnostic for a dive bar.

**`17-test-2.mp3`**

> Did this accumulate? Or was it purchased?

### 18 · Field Protocol (`protocol`)

*Practical advice from a seasoned guide. Each rule is its own clip.*

**`18-protocol-1.mp3`**

> If your curiosity takes over and you decide to explore a dive bar for yourself, here are a few protocols to observe.

**`18-protocol-2.mp3`**

> Arrive with no more than three other people.

**`18-protocol-3.mp3`**

> A beer, a shot, or a drink with two ingredients. Never order a fancy cocktail.

**`18-protocol-4.mp3`**

> Read the room before you touch the jukebox.

**`18-protocol-5.mp3`**

> Watch how seriously they play pool. Mimic accordingly.

**`18-protocol-6.mp3`**

> The restroom is only for number one. Number two means it's time to go home.

**`18-protocol-7.mp3`**

> And finally, always bring cash. If they don't take cards, be delighted. You have just encountered one of the last remaining American dive bars.

### 19 · Conservation (`conservation`)

*Sincere. The stool line is gentle, almost a whisper.*

**`19-conservation-1.mp3`**

> No one has ever counted all of America's dive bars, while many have tried. But the pressures today are real. Rising rents. Redevelopment. Fewer drinkers.

**`19-conservation-2.mp3`**

> You can open a bar tomorrow. But you cannot open a seventy-year-old bar tomorrow.

**`19-conservation-3.mp3`**

> Do you see that stool over there? That's Gary's seat. It took him decades to earn it.

### 20 · Respect the Habitat (`closing`)

*The sign-off. Build to "And whatever you do...", hold, then deliver the last line deadpan.*

**`20-closing-1.mp3`**

> A great dive bar isn't designed. It evolves.

**`20-closing-2.mp3`**

> So if you find one in the wild, approach it respectfully. Order something simple.

**`20-closing-3.mp3`**

> And whatever you do...

**`20-closing-4.mp3`**

> Respect the habitat. Don't sit in Gary's seat.
