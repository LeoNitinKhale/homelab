# Mnemonic Instances

Historical figures encoded with the pegs in `major_system_pegs_0-100.md`. Last two digits of birth and death year.

## Scene rules

- **Object pegs carry the numbers.** They are the load-bearing part of every scene.
- **Birth** — object above the waist or in front, via a birth action: creating, planting, picking, lighting, inflating, catching, lifting.
- **Death** — object below the waist or behind, via the inverse: dropping, extinguishing, smashing, deflating, crushing.
- Scenes connect to the figure's actual life or legacy. Mechanically valid but arbitrary scenes are amber, not green.
- **Characters play two roles, neither numeric by default:**
  - *Century marker* — a character peg keyed to the birth century's prefix digits (key in `major_system_pegs_0-100.md`). Used selectively, only where the century is genuinely ambiguous.
  - *Emotional trigger* — a character present to motivate the action and make it stick (Patton jailing Churchill; Mozart's father on the other end of the leash). Carries no number and isn't meant to.

## Status tags

- 🟢 **Green** — locked: numbers verified, action/position consistent (or a consciously accepted exception), nothing open
- 🟡 **Amber** — numbers and mechanics check out, visual not yet strong enough to call final
- 🔴 **Red** — a real gap remains

## Fields

Every entry carries five metadata fields, each on its own line, so the set can be filtered for practice (all writers, all ancient, all assassinated). Separate fields rather than encoded tag strings — this imports straight into a database or a Dataview query with no parsing convention.

| Field | Values | Cardinality |
|---|---|---|
| **Role** | writer, poet, playwright, composer, artist, philosopher, mathematician, astronomer, physicist, chemist, naturalist, physician, engineer, architect, inventor, historian, lawyer, clergyman, politician, statesman, ruler, king-emperor, queen, general, revolutionary, explorer, businessman | many |
| **Field** | science, arts, music, literature, power, military, exploration, philosophy | many |
| **Era** | ancient, medieval, renaissance, early-modern, enlightenment, industrial, modern | one |
| **Region** | british, french, italian, german, austrian, american, dutch, polish, serbian, egyptian, roman, mongol, genoese | one |
| **End** | natural, illness, assassinated, executed, suicide, battle, uncertain | one |

**Two rules that keep the set usable:**

- **End** is the manner of death, and the year pegs are now **Birth peg** / **Death peg**. Distinct names for distinct things — "death" previously meant two.
- **Role is the most specific term; Field is the broad bucket.** Never tag a specialism and its parent together. Newton is `Role: mathematician, physicist, astronomer` + `Field: science` — there is no role "scientist", because "all the scientists" is `Field: science`. Same on the arts side: `Role: composer` + `Field: music`, never "musician".

## Template

```
## N. Name 🔴 (birth–death)

- Birth peg: **BB → Word**
- Death peg: **DD → Word**
- Century: **CC → Character**
- Role:
- Field:
- Era:
- Region:
- End:
- Scene:
- Position:
```

---

## 1. Mozart 🟢 (1756–1791)

- Birth peg: **56 → Leash**
- Death peg: **91 → Pad / Bat** (both encode 91 — deliberate reinforcement)
- Century: **17 → Tom Kerridge**
- Role: composer
- Field: music
- Era: enlightenment
- Region: austrian
- End: illness
- Scene: A leash around Mozart's neck, his overbearing father on the other end, controlling him. He wears cricket pads on his legs and holds a bat down at his side.
- Position: leash at the neck, above waist, front. Pads and bat both below waist — death position. Clean.
- The father is an emotional trigger, not a number-carrier.

---

## 2. Newton 🟢 (1642–1727)

- Birth peg: **42 → Orange** (R,N,J — trailing J dropped)
- Death peg: **27 → Ink**
- Century: **16 → Tom & Jerry**
- Role: mathematician, physicist, astronomer
- Field: science
- Era: early-modern
- Region: british
- End: natural
- Scene: An orange falls on Newton's head; the juice drips down as orange ink into an inkwell. A book, "PrINKipia Mathematica," sits by his feet.
- Position: ink dripping down to the well, book at his feet — death action, death position, death number. The orange *falls* (a death-type action) while sitting on his head (birth position) carrying the birth number. **Accepted exception**: the falling-fruit/gravity tie is worth the mismatch.
- Ink is shared with Genghis (4).

---

## 3. Shakespeare 🟢 (1564–1616)

- Birth peg: **64 → Cherry**
- Death peg: **16 → Dish**
- Century: **15 → David Lynch**
- Role: playwright, poet, writer
- Field: literature
- Era: renaissance
- Region: british
- End: uncertain
- Scene: Plucks a cherry from a tree hung with oversize cherries and scrolls, inking his fingers. Writes on an unravelled scroll, lays it on a dish, kneels and presents it low: "a fine dish for her majesty."
- Position: plucking from a tree — birth action, birth position. The dish presented low from a kneel — death position. Clean.
- The spoken line fixes the word as *dish*. "Plate" is P,L,T = 951.

---

## 4. Genghis Khan 🔴 (1162–1227)

- Birth peg: **62 → Chains**
- Death peg: **27 → Nike**
- Century: **11 → Tony Tiger**
- Role: ruler, general
- Field: power, military
- Era: medieval
- Region: mongol
- End: uncertain
- Scene: Wrapped in chains — early-life struggle. Breaks free. Sweats uncontrollably and keels over saying 'Just screw it!' Feet have Nikes on represent his historical victory/conquest.
- Position: chains/breaking free reads birth-consistent, above/front. Keeling over and the Nikes on his feet — death position, below waist. Clean.
- 🔴 Cause of death open. The record is genuinely uncertain — illness or fever, possibly plague, following a fall from his horse the year before. The nosebleed story belongs to Attila. The sweating/collapse imagery is compatible with the fever reading without committing to it.
- Nike (27) replaces Ink, clearing the duplicate with Newton (2). "Just screw it" is a spoken cue, not a peg — Screw is 74.

---

## 5. Einstein 🟢 (1879–1955)

- Birth peg: **79 → Cap**
- Death peg: **55 → Lily**
- Century: **18 → Tim Vine** (optional)
- Role: physicist
- Field: science
- Era: modern
- Region: german
- End: illness
- Scene: Wearing a cap with "E=MC²" on it. Looks down and touches water with lilies floating on it; ripples radiate out like spacetime ripples.
- Position: cap on his head — birth position, front. Looking down to the water — death position. "Touches" isn't a listed death verb; mild looseness, not a conflict.

---

## 6. Elizabeth I 🟢 (1533–1603)

- Birth peg: **33 → M&Ms** (letter cheat)
- Death peg: **03 → Sum** (Seam is the strict-noun alternative, same phonetics)
- Century: **15 → David Lynch** (shared with Shakespeare)
- Role: queen, ruler
- Field: power
- Era: renaissance
- Region: british
- End: natural
- Scene: Eating M&Ms, which contrast against her famously white face. They fall to the floor, where she tries to sum them to balance the country's finances.
- Position: eating near her face — birth. Falling to the floor — death action and position. Clean.
- Sum is abstract, retained as an accepted exception for the finance pun.

---

## 7. Napoleon Bonaparte 🟢 (1769–1821)

- Birth peg: **69 → Chip**
- Death peg: **21 → Net**
- Century: **17 → Toby Keith** (optional; Tom Kerridge is Mozart's)
- Role: king-emperor, general, ruler
- Field: power, military
- Era: early-modern
- Region: french
- End: illness
- Scene: A physical chip on his shoulder falls down into a net — a fryer basket, but a net — full of other chips. It all fizzles and dissolves.
- Position: chip on the shoulder — birth position, front. Falling into the net below — death action and position. Clean.

---

## 8. Charles Darwin 🟢 (1809–1882)

- Birth peg: **09 → Ape**
- Death peg: **82 → Fan**
- Century: **18 → Tim Vine** (optional)
- Role: naturalist
- Field: science
- Era: industrial
- Region: british
- End: illness
- Scene: Inflating an inflatable ape — evolution. A giant fan blows it away — the controversy and pushback.
- Position: inflating — birth action, above/front. The fan blowing it away — dispersal, death-consistent.
- **Accepted exception**: Ape is a single-sound word (P), so it doesn't carry the tens-place zero the 00–09 range otherwise requires. Since you only ever peg isolated two-digit year-endings in context, never freeform digit strings, there's no reading of Ape other than 09.

---

## 9. Abraham Lincoln 🟡 (1809–1865)

- Birth peg: **09 → Ape** (same accepted exception as Darwin)
- Death peg: **65 → Shell**
- Century: **18 → David Frost** (optional)
- Role: statesman, politician, lawyer
- Field: power
- Era: industrial
- Region: american
- End: assassinated
- Scene: An ape in a stovepipe hat, inflated by a young Lincoln. He's shot at the theatre; the balloon pops, and a shell bearing the American flag closes around him — the Union preserved.
- Position: inflating — birth action, above/front. The pop-to-shell is a single continuous beat rather than two, matching the pattern elsewhere (orange-to-ink, cherry-to-dish, M&Ms-to-sum).
- 🟡 Visual not strong enough. Open.
- Shares the birth peg with Darwin (8) — same birth year, in fact the same day, 12 Feb 1809. A linked pair of scenes is an option if the separate ones stay thin.

---

## 10. Henry VIII 🟡 (1491–1547)

- Birth peg: **91 → Boat**
- Death peg: **47 → Rock**
- Century: **14 → Daniel Radcliffe** (optional)
- Role: king-emperor, ruler
- Field: power
- Era: renaissance
- Region: british
- End: illness
- Scene: Henry on a small boat crowded with his six wives, casting off. A monk hurls a rock that smashes into the boat as it sinks.
- Position: casting off — birth action, above waterline, front. The rock smashing the boat — listed death action, correct position. Clean.
- The monk is an emotional trigger and carries the Reformation, so the death image has historical weight.
- 🟡 Sitting with the visual before calling it final.

---

## 11. Leonardo da Vinci 🟢 (1452–1519)

- Birth peg: **52 → Lion**
- Death peg: **19 → Tuba**
- Century: **14 → Tim Roth** (Henry VIII takes Daniel Radcliffe — both 1400s births)
- Role: artist, engineer, inventor
- Field: arts, science
- Era: renaissance
- Region: italian
- End: natural
- Scene: Baby Leonardo born in a lion's den. He grabs the lion's tail like a paintbrush and starts painting. Later his head sticks out of a tuba, King Francis I supporting him almost like cradling his neck.
- Position: born in the den, painting — creating, above/front. Head-in-tuba with the king's embrace reads reclining/low — death-consistent.
- "Leonardo" → "Leo" → lion is a personal hook, and the tail-as-paintbrush ties the number-carrier into the action rather than leaving it a static prop.
- **Historical flag**: the Francis I deathbed scene is legend, not fact. Royal records place Francis at Saint-Germain-en-Laye on the day Leonardo died (2 May 1519), not at Amboise. The story comes from Vasari, writing 30 years later. Kept because the image is strong.

---

## 12. Christopher Columbus 🟢 (1451–1506)

- Birth peg: **51 → Lady / Light** (both encode 51)
- Death peg: **06 → Sash**
- Century: **14 → Daniel Radcliffe** (optional)
- Role: explorer
- Field: exploration
- Era: renaissance
- Region: genoese
- End: illness
- Scene: The Statue of Liberty — the lady in the light — rises into view and lights up in the distance. Columbus falls, lies down, a red/white/blue sash draped over him.
- Position: rising and lighting up — both listed birth actions, high and in front. Falling, lying down, sash draped over the body — death action, death position. Clean.
- The number is carried by *lady* and *light*. "Liberty" is L,B,R,T = 5941.

---

## 13. Cleopatra 🟢 (69 BC – 30 BC)

- Birth peg: **69 → Shop**
- Death peg: **30 → Mice**
- Role: queen, ruler
- Field: power
- Era: ancient
- Region: egyptian
- End: suicide
- Scene: Cleopatra opens a shop, window packed with sacks of grain and gold, "open for business". Mice run in, drawn by the grain; a snake follows the mice and bites her.
- Position: opening the shop — creating, front. Mice at floor level, snake striking low — death position. Clean.
- **BC caution**: the numbers run backwards — birth 69 is the larger, death 30 the smaller. The only entry where birth > death. Worth a fixed BC cue in the scene so you know to flip.
- The asp is Plutarch's account and is disputed; poison is the alternative reading.

---

## 14. Marie Curie 🟢 (1867–1934)

- Birth peg: **67 → Chalk** (CH,K — the L is silent)
- Death peg: **34 → Myrrh**
- Century: **18 → Tim Vine** (optional)
- Role: physicist, chemist
- Field: science
- Era: modern
- Region: polish
- End: illness
- Scene: A radioactive glowing baby immediately grabs the chalk and scribbles physics equations on a blackboard. Later, three gift boxes — "gifts for the wise woman," echoing the three wise men — she opens the third, myrrh, and the fumes overcome her.
- Position: grabbing chalk, writing on the board — birth action, above waist, front. The myrrh box is the weak point: *opening* is a birth-type action, and nothing places it low or behind. **Fix**: put the box on the floor, drop the lid, have the fumes rise from below her.
- She died of aplastic anaemia from radiation exposure, not from inhaling anything — the fumes are a number-carrier, not history.

---

## 15. Winston Churchill 🟢 (1874–1965)

- Birth peg: **74 → Car**
- Death peg: **65 → Jail**
- Century: **18 → David Frost** (optional; Frost interviewed him, which is a free tie)
- Role: statesman, politician, writer, general
- Field: power, military
- Era: modern
- Region: british
- End: natural
- Scene: Baby Churchill, bulldog-faced, cigar in mouth, driven up in a car. Later, General Patton leads him into a jail cell, bars closing behind him.
- Position: arriving in the car, cigar at the mouth — birth position, front. Bars closing *behind* him — death position. Clean.
- The peg is *jail* (J,L = 65). "Cell" is S,L = 05 — the more natural word for the image, so say jail.
- Patton is an emotional trigger, carrying no number: he's there to motivate the jailing.

---

## 16. Nikola Tesla 🟡 (1856–1943)

- Birth peg: **56 → Leash**
- Death peg: **43 → Arm**
- Century: **18 → Tim Vine** (optional)
- Role: inventor, engineer, physicist
- Field: science
- Era: modern
- Region: serbian
- End: natural
- Scene: Baby Tesla on an electrified leash, crackling with sparks. Later, he raises his arm and blasts through the hotel window into the clouds for one last lightning storm, then falls back and dies.
- Position: leash on the baby, above waist — birth, clean. **The arm breaks the rule**: raising it is a lifting action, held high and in front — every signal says birth, but it carries the death number.
- **Fix options**: (a) the arm *falls* — the storm passes, the arm drops limp at his side and stays there, so the last image is low and dropping; (b) swap to Ram, Room or Rim.
- Leash is shared with Mozart (1). Lash or Leech would clear it.
- 🟡 Open on the arm position.
- He died 7 Jan 1943, alone in the Hotel New Yorker — the hotel window is real.

---

## 17. Vincent van Gogh 🟢 (1853–1890)

- Birth peg: **53 → Lemon / Lime**
- Death peg: **90 → Bees**
- Century: **18 → Tim Vine** (optional)
- Role: artist
- Field: arts
- Era: industrial
- Region: dutch
- End: suicide
- Scene: Born in a basket of lemons and limes; he squeezes the lemons to make yellow ink and paints sunflowers. In a wheat field, a swarm of buzzing bees pours out of the sunflowers — speech bubble: "I can't 'ear them" (dropped H, and the missing ear).
- Position: born in the basket, squeezing, painting — creating, above/front. Clean. The bees *pour out* and swarm at head height, which reads as emergence rather than a death action. **Fix**: have them pour downward and settle behind/below him as he falls in the field.
- The "I can't 'ear them" pun refers to cutting off his ear.
- He shot himself in a wheat field at Auvers (29 July 1890, dying two days later), so the field is right. The bees carry the number but have no historical hook — the weakest part of an otherwise strong scene.

---

## 18. Ben Jonson 🟢 (1572–1637)

- Birth peg: **72 → Coin**
- Death peg: **37 → Mug**
- Century: **15 → David Lynch** (optional)
- Role: playwright, poet, writer
- Field: literature
- Era: renaissance
- Region: british
- End: illness
- Scene: Ben Jonson with **Ben Johnson the sprinter's face** — memory hook, not history. He crawls onstage chasing coins, scrabbling after them: his satires on greed (*Volpone*, *The Alchemist*). Later he grabs a mug, drinks heavily, drops it and dies.
- Position: chasing the coins, reaching forward — front, birth-consistent. The mug is dropped — listed death action, falls below. Clean.
- The sprinter's face is an emotional trigger, carrying no number. It brings the doping association free, which is on-theme for a satirist of fraud.

---

## 19. Voltaire 🟢 (1694–1778)

- Birth peg: **94 → Boar**
- Death peg: **78 → Cuff / Cove**
- Century: **16 → Tom & Jerry** (optional)
- Role: philosopher, writer
- Field: philosophy, literature
- Era: enlightenment
- Region: french
- End: illness
- Scene: A boar carries him in on its back; he quips "I've never been a *bore*." Later the devil leads him away by the cuffs, down into Devil's Cove.
- Position: carried in, up on the boar's back — birth position, front. Led away and down into the cove — death position, behind. Clean.
- The Bastille imprisonment is real (twice). The deathbed line "this is no time to make new enemies" is almost certainly apocryphal — good imagery, not history.

---

## 20. John Milton 🟢 (1608–1674)

- Birth peg: **08 → Sieve** (S,V — same slot as Safe and Sofa)
- Death peg: **74 → Car**
- Century: **16 → Tom & Jerry** (optional)
- Role: poet, writer
- Field: literature
- Era: early-modern
- Region: british
- End: illness
- Scene: Young Milton shakes a sieve above two or three baby girls below him, only scraps getting through — his daughters read aloud to him in languages he never taught them to understand. Later, blind Milton crashes a car, shouting "Where's Paradise? I'm lost!"
- Position: sieve held up and shaken, above the waist — birth action, birth position. The car crashes — smashing, a listed death action. Clean.
- The daughters detail is true: they read to him in Latin and Greek without being taught the meaning.
- **Sieve** is new to the 08 slot — added to `major_system_pegs_0-100.md`.

---

## 21. Blaise Pascal 🟡 (1623–1662)

- Birth peg: **23 → Number** (N,M)
- Death peg: **62 → Chain** *(corrected — see flag)*
- Century: **16 → Tom & Jerry** (optional)
- Role: mathematician, physicist, philosopher
- Field: science, philosophy
- Era: early-modern
- Region: french
- End: illness
- Scene: Baby Pascal in a **number** 23 jersey, floating digits forming the number around him — the boy prodigy. Later a chain is pulled tight through his stomach, doubling him over: "here's one problem I couldn't solve." The tumour that killed him.
- Position: jersey on his chest, digits above and around him — birth position, front. The chain drags down and back through his gut — death position. Clean.
- The peg is the word **number** (N,M = 23), not the digits themselves. The floating 23 is reinforcement on top of a proper peg, not a substitute for one — the jersey and the digits are decoration, the *word* carries it.
- 🔴 **Death peg was mis-encoded.** Notch, niche and gnash are all N·CH = **26**, not 62. 62 is CH·N — Chin, Chain, Genie. Chain keeps the constriction and the gut pain; Genie bursting from the stomach is the stranger option.
- Cause of death is disputed — stomach cancer and tuberculosis are both argued. The imagery survives either way.

---

## 22. Michelangelo 🟢 (1475–1564)

- Birth peg: **75 → Coal**
- Death peg: **64 → Chair**
- Century: **14 → Daniel Radcliffe** (optional)
- Role: artist, poet
- Field: arts
- Era: renaissance
- Region: italian
- End: natural
- Scene: Born by being hewn out of a seam of coal, he cries "Coalazzo!" Later he falls from the Sistine "Chair-pel" ceiling and slumps, dead, onto a chair.
- Position: hewn from the coal seam — created, above/front, birth. Falling and slumping onto the chair — death action, below. Clean.
- **Invented death.** He didn't fall from the ceiling — he painted it 1508–1512 and died of a fever at 88, decades later. Hook only, like Leonardo's deathbed legend.

---

## 23. Robert Hooke 🟢 (1635–1703)

- Birth peg: **35 → Mill**
- Death peg: **03 → Trident** *(visual peg: 3 prongs = 3; the leading 0 is supplied by context, same exception as Ape/09)*
- Century: **17 → Toby Keith** (optional)
- Role: physicist, naturalist, architect
- Field: science
- Era: early-modern
- Region: british
- End: illness
- Scene: Hooke, hook-handed, hangs from the sail of a windmill and is carried round with it; the cord on his hook stretches and contracts as he swings — Hooke's Law. Later, Newton stabs him with a trident: "Here's the 3 laws of de-motion!"
- Position: hanging from the mill sail, carried up and round — birth, above/front. The trident thrust down into him — death action, low. Clean.
- The stretch-and-contract of the hook cord *is* Hooke's Law (elasticity), so the birth object carries the physics, not just the number. Newton is the emotional trigger — their real, bitter feud — and "demotion" puns his three laws of motion.

---

## 24. Augustus (Octavian) 🟢 (63 BC – 14 AD)

- Birth peg: **63 → Jam**
- Death peg: **14 → Door**
- Century: —
- Role: king-emperor, ruler, statesman
- Field: power
- Era: ancient
- Region: roman
- End: natural
- Scene: Young Octavian jams severed body parts into a jam jar, red jam smeared everywhere — the brutality of his rise. Old Augustus walks out through a door: "Did I play my part well? Then let me make my exit."
- Position: jamming into the jar, held up and in front — birth. Exiting through the door, turning away — death, behind. Clean.
- The jam/brutality hook is anchored: the proscriptions of the Second Triumvirate killed thousands, Cicero among them. The exit line is Suetonius's account of his actual deathbed — he asked whether he'd played his part in the comedy of life, then quoted the Greek tag about applause.
- **BC/AD crossing.** This is the first entry that straddles the boundary — birth is 63 *BC*, death 14 *AD*. The pegs (63, 14) are unaffected, but unlike the pure-BC figures the numbers don't simply run backwards; you have to hold that birth sits before the line and death after it.

---

## 25. Charles Dickens 🟢 (1812–1870)

- Birth peg: **12 → Ton** (*Tan* boot polish is reinforcement — T,N = 12 as well, so both words in the image carry the same number)
- Death peg: **70 → Goose**
- Century: **18 → Tim Vine** (optional)
- Role: writer
- Field: literature
- Era: industrial
- Region: british
- End: illness
- Scene: Baby Dickens, tan boot polish smudged on his cheeks, boots scattered around him, straining to hoist a giant weight overhead labelled "ONE TON" — the debt that sent his father to debtors' prison, and his own child labour in the blacking factory. Later he collapses at his writing desk mid-sentence on *Edwin Drood*; Scrooge appears with a goose: "your goose is cooked."
- Position: hoisting the weight overhead — lifting, a listed birth action, above the waist. **The goose is the weak point**: Scrooge *holds* it, which is neither a death action nor a death position. **Fix**: Scrooge drops the goose on the floor beside the collapsed body, so the last image is low and falling.
- *Edwin Drood* was genuinely unfinished — he died the day after working on it. The goose is the Cratchit Christmas dinner from *A Christmas Carol*.

---

## 26. Michael Faraday 🔴 (1791–1867)

- Birth peg: **91 → Pot** *(proposed — see flag)*
- Death peg: **67 → Cheque** (Jag is the alternate, same slot)
- Century: **17 → Toby Keith** (optional)
- Role: physicist, chemist
- Field: science
- Era: industrial
- Region: british
- End: natural
- Scene: Baby Faraday surrounded by leather-bound books — he started as a bookbinder's apprentice. A bookbinder's glue **pot** is yanked upward off the bench by an invisible magnet, foreshadowing electromagnetic induction. Later, the dying Faraday is offered a cheque (the knighthood he refused) and pushes it away: "what a cheek." Layered alternate: a **Jag** pulls up to deliver the offer instead of a person.
- Position: the pot pulled up and off the bench — lifting, birth action, above the waist. The cheque pushed away — moving behind him, death position. Clean.
- He really did refuse a knighthood and burial in Westminster Abbey, insisting on staying plain Mr Faraday. The refusal is the historical anchor, so the death peg earns its place.
- 🔴 **Birth peg was mis-encoded.** *Pin* and *pan* are both P·N = **92**, not 91 — 92 is the Bone/Pin/Pen/Bun slot. 91 is P/B·T/D: Boat, Bat, Bud, **Pot**, Pad. The safety-pin image, as built, encodes the wrong year. **Pot** is proposed above because a bookbinder's glue pot keeps both the apprenticeship hook and the magnet-yank, so only the object swaps — the scene survives intact. Confirm the swap, or pick another 91 word and rebuild.

---

## 27. Florence Nightingale 🟢 (1820–1910)

- Birth peg: **20 → Nissan** *(rlx — trailing N dropped, same relaxation as Emerald/Gold)*
- Death peg: **10 → Dice**
- Century: **18 → David Frost** (optional)
- Role: nurse, statistician
- Field: science
- Era: industrial
- Region: british
- End: natural
- Scene: Baby Nightingale rides in a plush carriage — her family was wealthy — badged **Nissan** where the luxury marque should be, furry dice swinging inside. She says "look at my *Nurse-san*." Later those same dice reappear: she throws them down — "this was all preventable, look at my disease dice."
- Position: the badge and the hanging dice at eye level in the carriage — birth position, front. The dice thrown down — dropping, a listed death action, low. Clean.
- **The badge must read *Nissan*, not "Nurse-san".** *Nurse* is N,R,S = 240 (it already sits at 24), so a badge reading "Nurse-san" encodes the wrong number. Same discipline as Churchill's jail/cell: the pun is spoken, the peg is written.
- The recurring dice are a deliberate thread linking her two scenes — the only entry that reuses one object across birth and death.
- The statistics hook is real: her polar-area "coxcomb" diagrams showed disease, not wounds, killed most soldiers in the Crimea.

---

## 28. Alan Turing 🟢 (1912–1954)

- Birth peg: **12 → Tin** (Tintin is the visual dress-up, carrying no number — see note)
- Death peg: **54 → Lyre**
- Century: **19 → David Beckham** (optional)
- Role: mathematician
- Field: science
- Era: modern
- Region: british
- End: suicide
- Scene: Young Turing drawn as Tintin — quiff and all, Snowy at his side — holding up a magnifying glass over roses, whose thorny stems twist into the shape of a **lyre** as he watches. Puzzled: "what are these strange things growing out of the roses?" Later he collapses beside the poisoned apple, the broken lyre lying behind him, grown from those same thorns: "lion-eyed poisoning — I failed a Turing test."
- Position: magnifying glass and roses held up in front — birth position, examining and picking. The lyre broken and lying behind the body — smashing, death action, low and behind. Clean.
- **Tintin carries no number.** *Tintin* is T,N,T,N = **1212**, so it fails the exact-match rule as a peg and fails the two-initials rule as a character peg. It works as an emotional trigger and visual hook — the same role as Ben Jonson's sprinter face — while the word **Tin** does the encoding. Conveniently, "Tintin" is literally *tin* twice, so the hook reinforces the peg instead of fighting it.
- Shares the birth peg with Dickens (25) — same birth-year ending, different words and images (Tin/Tintin vs Ton/tan boot), so they stay distinct.
- Officially suicide by cyanide, and that's what the inquest found — but accidental inhalation from his home electroplating setup is seriously argued, and his mother maintained it. The apple was never tested.

---

## 29. Mark Antony 🟢 (83 BC – 30 BC)

- Birth peg: **83 → Foam**
- Death peg: **30 → Mice** (shared with Cleopatra 13 — deliberate)
- Century: —
- Role: general, statesman, ruler
- Field: military, power
- Era: ancient
- Region: roman
- End: suicide
- Scene: Young party-boy Antony lounges in a bath overflowing with champagne **foam**, women around him — his reputation for drink and scandal before Caesar. Arm raised, triumphant: "fame — I'm gonna live forever." Later the same **mice** from Cleopatra's scene run in low around him as he falls on his sword.
- Position: foam heaped up around his chest and raised arm — birth position, front. Mice at floor level as he falls — death position. Clean.
- **Deliberate shared peg.** Antony and Cleopatra died in the same year (30 BC), both by suicide after Actium, so the mice are the same mice. This is the one duplicate in the set that carries meaning rather than costing anything.
- **BC caution**: numbers run backwards — birth 83 is larger than death 30, same trap as Cleopatra (13).
- Dramatic irony in the birth line: the fame outlived him, the power didn't.

---

## Open items

- **Faraday (26)** — birth peg mis-encoded (pin/pan = 92, not 91); Pot proposed, needs confirming.
- **Genghis (4)** — cause of death unresolved.
- **Lincoln (9)** — visual not strong enough.
- **Tesla (16)** — arm is in birth position but carries the death number.
- **Curie (14), Van Gogh (17)** — death objects not clearly low or behind.
- **Pascal (21)** — death peg was mis-encoded (notch/niche/gnash = 26, not 62), provisionally corrected to Chain. Confirm or pick Chin/Genie.
- **Dickens (25)** — goose is held, not dropped; needs the low/falling fix.
- **Nightingale (27)** — Role uses `nurse` and `statistician`, neither of which is in the Fields table yet. Add them or remap.
- **Duplicate object pegs across scenes**: Ink (Newton 2 / Genghis 4), Ape (Darwin 8 / Lincoln 9 — same year, so defensible), Leash (Mozart 1 / Tesla 16), Tin/Ton (Dickens 25 / Turing 28 — same year-ending, distinct words), Mice (Cleopatra 13 / Mark Antony 29 — same death year, deliberate).
- **Century marker crowding**: six figures sit in the 1800s and the key offers only Tim Vine and David Frost for 18. Markers are selective — drop them where the century is obvious.

## Backlog

Dates and candidate peg words; no scenes yet. Word lists are options to pick from, not decisions. Facts line is there to spark the hook — the strongest scenes come from something the figure actually did.

**René Descartes** — 1596 / 1650
Birth **96**: Beach, Peach, Bush, Badge, Bosch · Death **50**: Lace, Lice, Lasso, Listerine
*Cogito ergo sum. Claimed his philosophy came from three dreams in a stove-heated room. Died in Sweden, killed by Queen Christina's 5am tutorials in the cold. Mind–body dualism; Cartesian coordinates.*


**Gottfried Leibniz** — 1646 / 1716
Birth **46**: Roach, Ridge · Death **16**: Dish, Dash, Ditch
*Invented calculus independently of Newton, and the priority dispute poisoned both their lives. Binary arithmetic. "The best of all possible worlds" — the line Voltaire mocked in Candide. Both slots are thin.*
🟡 **Raja (46) flagged for geographic mismatch** — his Eastern link was the Chinese *I Ching*, which he read as confirmation of his binary arithmetic, not anything Indian. Left in place for now; a Chinese-flavoured 46 would be better but the slot has only Roach and Ridge to work with.

**Nicolaus Copernicus** — 1473 / 1543
Birth **73**: Comb, Gum, Camel, Camel *(cigs)* · Death **43**: Ram, Arm, Rum, Room, Rim, Rimmel
*Put the sun at the centre and sat on it for decades — De revolutionibus was published the year he died, the first copy reportedly reaching him on his deathbed. Canon of Frombork cathedral; astronomy was the side project. Raised by his bishop uncle after his father died, which is the strongest unused birth-scene angle.*
🔴 Neither slot locked. Note: **Game and Camo are not available for 73** — Game was struck from the dictionary as a non-noun (see major_system_pegs_0-100.md audit), and Camo is abstract. Comb and Gum are the live options.

**Alexander the Great** — see Backlog entry above
🔴 Dates identified (356 BC / 323 BC → 56 / 23), no scene started. **Collision watch**: 56 is Tesla's birth peg (Leash) and 23 is Pascal's (Number). Leech, Lash or Lush clear the first; Gnome or Anemone clear the second.

**Julius Caesar** — 100 BC / 44 BC
Birth **00**: Sauce · Death **44**: Rear, Aurora, Warrior
*Crossed the Rubicon. Stabbed 23 times in the Senate on the Ides of March. Julian calendar. BC — the numbers run backwards, same trap as Cleopatra.*

**Socrates** — 470 BC / 399 BC
Birth **70**: Case, Goose, Gauze, Casio · Death **99**: Baby, Poppy, Pipe, Puppy, Pepsi
*Executed by hemlock for "corrupting the youth". Wrote nothing — everything comes via Plato. The Socratic method. BC.*

**Alexander the Great** — 356 BC / 323 BC
Birth **56**: Leash, Leech, Lash, Lush · Death **23**: Gnome, Number, Anemone
*Tutored by Aristotle. Tamed Bucephalus as a boy. Never lost a battle; dead at 32, possibly typhoid or poison. BC.*

**Galileo Galilei** — 1564 / 1642
Birth **64**: Chair, Shore, Cherry · Death **42**: Rhino, Wren, Rain, Orange, Renault
*Improved the telescope, found Jupiter's moons. Tried by the Inquisition, forced to recant heliocentrism, spent his last years under house arrest, blind. Shares a birth year with Shakespeare (3) and a death year with Newton's birth.*

**J.S. Bach** — 1685 / 1750
Birth **85**: Foil, File, Volvo · Death **50**: Lace, Lice, Lasso, Listerine
*Twenty children. Walked 250 miles to hear an organist play. Jailed for a month for trying to leave a job. Died after botched eye surgery by the same quack who blinded Handel.*

**Beethoven** — 1770 / 1827
Birth **70**: Case, Goose, Gauze, Casio · Death **27**: Neck, Nag, Nook, Ink, Nike
*Went deaf and kept composing — conducted the Ninth without hearing the ovation and had to be turned round to see it. Sawed the legs off his piano to feel the vibrations through the floor.*

**Jane Austen** — 1775 / 1817
Birth **75**: Coal, Coil, Eagle, Gold, Colgate · Death **17**: Tack, Duck, Dog, Deck, Tag, TK Maxx
*Published anonymously — "By a Lady". Wrote at a small table in a room with a creaking door she refused to have fixed, so it would warn her to hide her papers. Died at 41, cause still argued.*

**Queen Victoria** — 1819 / 1901
Birth **19**: Tub, Tape, Tip, Tuba, Toblerone · Death **01**: Seed, Suit
*Sixty-three years on the throne. Wore black for 40 years after Albert died. Survived eight assassination attempts. Empress of India; never visited it.*

**Karl Marx** — 1818 / 1883
Birth **18**: Dove, Toffee, Diva, Staff, Tefal · Death **83**: Foam, Femur, Vomit, Famous Grouse
*Wrote Das Kapital in the British Museum reading room. Bankrolled for decades by Engels. Buried in Highgate. Died stateless.*

**Ada Lovelace** — 1815 / 1852
Birth **15**: Tail, Dial, Doll, Tile, Towel, Tilda · Death **52**: Lion, Lawn, Lane, Loon, Alien, Lenor
*Byron's daughter. Wrote the first published algorithm, for Babbage's unbuilt Analytical Engine, and saw that it could do more than numbers. Died at 36, same age as her father.*

**Sigmund Freud** — 1856 / 1939
Birth **56**: Leash, Leech, Lash, Lush · Death **39**: Map, Mop, Amp
*The couch. Cocaine enthusiast early on. Fled the Nazis to London in 1938; 33 operations for jaw cancer from cigars; died by assisted morphine.*

**Mahatma Gandhi** — 1869 / 1948
Birth **69**: Ship, Shop, Sheep, Chip, Chop, Jeep · Death **48**: Roof, Reef, Roofer, Ryvita
*Salt March. Spun his own cloth. Assassinated by Nathuram Godse. Nominated for the Nobel Peace Prize five times, never awarded it.*

**Nelson Mandela** — 1918 / 2013
Birth **18**: Dove, Toffee, Diva, Staff, Tefal · Death **13**: Tomb, Dime, Dam, Team, Time, Timberland
*Twenty-seven years in prison, eighteen of them on Robben Island breaking rocks in a lime quarry, which ruined his eyes. Walked out and negotiated with his jailers' government. Only entry here with a 20th-century death — note the century marker.*

**Joan of Arc** — 1412 / 1431
Birth **12**: Tin, Den, Dawn, Ton, Down, Tango · Death **31**: Mat, Meat, Mud, Moat, Mattel
*Illiterate teenage peasant who talked her way into command. Lifted the siege of Orléans. Burned at the stake at 19; her heart reportedly wouldn't burn. Retried and exonerated 25 years later.*

**Captain James Cook** — 1728 / 1779
Birth **28**: Knife, Nephew, Navy, Nivea · Death **79**: Cap, Cub, Cop, Cab, Cape
*Charted New Zealand and eastern Australia. Beat scurvy with sauerkraut. Killed in the surf at Kealakekua Bay, Hawaii, in a scuffle over a stolen boat.*

**Rembrandt** — 1606 / 1669
Birth **06**: Sash · Death **69**: Ship, Shop, Sheep, Chip, Chop, Jeep
*Around 80 self-portraits, tracking his own face from cocky youth to ruin. Bankrupt in 1656; his possessions auctioned. Buried in an unmarked pauper's grave. 06 is a one-word slot.*

**Marie Antoinette** — 1755 / 1793
Birth **55**: Lily, Lolly, Lilac, Lyle's · Death **93**: Bomb, Beam, Puma, Pom, BMW
*Never said "let them eat cake". Played at being a shepherdess in a fake hamlet at Versailles. Guillotined nine months after her husband; apologised to the executioner for treading on his foot.*

**Ludwig Wittgenstein** — 1889 / 1951
Birth **89**: Fob, Fop, Fibre-optic, Fab · Death **51**: Light, Lad, Lady, Ladder, Lidl
*Gave away a vast family fortune. Worked as a village schoolteacher, a gardener, and a hospital porter. Wrote one book in his lifetime, then spent it arguing against himself. Last words: "Tell them I've had a wonderful life."*

**Emmeline Pankhurst** — 1858 / 1928
Birth **58**: Leaf, Elf, Olive, Loaf, Levi's · Death **28**: Knife, Nephew, Navy, Nivea
*Led the militant suffragettes. Arrested repeatedly; hunger strikes and force-feeding; released and re-arrested under the "Cat and Mouse" Act. Died weeks before women got the vote on equal terms.*
