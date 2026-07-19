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
| **Role** | writer, poet, playwright, composer, artist, philosopher, mathematician, astronomer, physicist, chemist, naturalist, physician, nurse, engineer, architect, inventor, historian, statistician, economist, lawyer, clergyman, politician, statesman, ruler, king-emperor, queen, empress, general, admiral, revolutionary, activist, explorer, businessman | many |
| **Field** | science, arts, music, literature, power, military, exploration, philosophy | many |
| **Era** | ancient, medieval, renaissance, early-modern, enlightenment, industrial, modern | one |
| **Region** | british, french, italian, german, austrian, american, dutch, polish, serbian, egyptian, roman, greek, macedonian, mongol, genoese, indian, south-african, chinese, russian, portuguese, norwegian, spanish, turkish, carthaginian, persian, swiss | one |
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


**Facts:** Wolfgang Amadeus Mozart was a freak of nature — a child prodigy playing the keyboard blindfolded and composing at five, paraded around the courts of Europe by his ambitious father Leopold like a performing miracle. He grew into perhaps the most naturally gifted composer who ever lived, able to write out whole works already finished in his head, with barely a correction.

Yet fame and money slipped through his fingers. He chafed against his stingy Salzburg employers, went freelance in Vienna, and swung between triumph and debt, firing off begging letters to friends. He died at just thirty-five while writing his Requiem, and was buried in a common grave — the cause (rheumatic fever, kidney failure, or something else) still argued over two centuries later.

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


**Facts:** Isaac Newton was a solitary, secretive and famously prickly genius who, sent home from Cambridge during a plague year, used the isolation to invent calculus, split white light into the spectrum, and begin working out universal gravitation — the falling apple, literal or not, belongs to this period. His Principia Mathematica set out the laws of motion and gravity that ruled physics for two centuries.

He was also a man of strange obsessions, spending as much time on alchemy and biblical prophecy as on physics, and feuding venomously with rivals like Hooke and Leibniz. As Master of the Royal Mint he personally hunted down counterfeiters and sent them to the gallows. He died unmarried and rich in 1727, and was buried in Westminster Abbey.

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


**Facts:** William Shakespeare is the most famous writer in the English language, yet we know maddeningly little about him — a glover's son from Stratford-upon-Avon who married at eighteen, surfaced in London as an actor and playwright, and produced some 38 plays and 154 sonnets that have never left the stage since. He gave English roughly 1,700 new words and phrases still in daily use.

He wrote for the Globe, a round open-air playhouse packed with rowdy 'groundlings', ran his company as a profit-sharing shareholder, and grew wealthy enough to retire to the second-grandest house in Stratford. He died at 52 on (by tradition) his own birthday; the cause is unknown, and a curse carved on his gravestone still warns anyone against moving his bones.

---

## 4. Genghis Khan 🟢 (1162–1227)

- Birth peg: **62 → Chains**
- Death peg: **27 → Nike**
- Role: ruler, general
- Field: power, military
- Era: medieval
- Region: mongol
- End: uncertain
- Scene: Boy Temüjin is wrapped in **chains** — his early captivity — then bursts free as he rises to power. At the end he sweats, shakes with fever and keels over, the **Nikes** on his feet represent victory as he crashes to the ground — conquest won, felled by an uncertain illness.
- Position: Chains wrapped high and broken free, in front — birth; carries 62. He keels over, the Nikes on his feet hitting the ground — death action, low; carries 27.
- Red-fix: pegs unchanged (Chains 62 / Nike 27). The redness was only the open death-cause; the fever/collapse imagery stays compatible without committing.

**Facts:** Temüjin was born into a fractured, feuding steppe world — his father poisoned when he was a boy, his family cast out to near-starvation. From that he clawed his way up to unite the warring Mongol tribes and forge, through terrifying discipline and mobility, the largest contiguous land empire in history, from the Pacific almost to the gates of Europe.

He was both a genocidal conqueror who razed cities that resisted and a surprising moderniser — instituting written law, religious tolerance, a horse-relay postal system and protected Silk Road trade. He died on campaign in 1227; the cause is genuinely uncertain (illness, or injuries from a fall), and his burial place was hidden so completely that it has never been found.

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


**Facts:** Albert Einstein was an obscure patent clerk in Bern, turned down for academic posts, when in his 'miracle year' of 1905 he published four papers that overturned physics — including special relativity and E=mc². A decade later general relativity reimagined gravity as the bending of space and time itself, confirmed when starlight was seen to bend around the sun during the 1919 eclipse, making him the world's first scientific superstar.

A lifelong pacifist and, from 1933, a refugee from Nazi Germany, he settled at Princeton and reluctantly signed the letter that spurred the atomic bomb — a step he later regretted. He spent his last decades chasing a unified theory he never found, declined the presidency of Israel, and died in 1955 of an aortic aneurysm, refusing surgery.

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


**Facts:** Elizabeth I survived a perilous youth — her mother Anne Boleyn beheaded when she was two, herself imprisoned in the Tower under her half-sister Mary — to become one of England's greatest monarchs. The 'Virgin Queen' never married, dangling rival suitors and powers against one another for forty-five years while insisting she was wedded only to her country.

Her reign became a golden age: the defeat of the Spanish Armada in 1588, the flowering of Shakespeare and Marlowe, and the first stirrings of English sea power. Vain, shrewd and formidably educated, she died in 1603 as the last of the Tudors, having steered a Protestant England through decades of religious and dynastic danger.

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


**Facts:** Napoleon Bonaparte was a minor Corsican noble who rose on the chaos of the French Revolution to become, by his mid-thirties, Emperor of the French and master of most of Europe. A military genius who reshaped the art of war, he also left a deeper civilian legacy in the Napoleonic Code, still the backbone of law in much of the world.

His ambition finally overreached in the frozen catastrophe of the 1812 invasion of Russia; after a brief comeback he was crushed at Waterloo in 1815. Exiled to the remote Atlantic island of St Helena, he died there in 1821 — officially of stomach cancer, though arsenic poisoning has been rumoured ever since.

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


**Facts:** Charles Darwin was a comfortably-off young naturalist, all but destined to become a country parson, when a five-year voyage aboard HMS Beagle changed everything. Studying the finches and giant tortoises of the Galápagos and fossils across South America, he slowly assembled the theory of evolution by natural selection — then sat on it, terrified of the uproar, for some twenty years.

He finally published On the Origin of Species in 1859, prompted only when a rival, Alfred Russel Wallace, hit on the same idea. It transformed biology and set off a culture war that still smoulders. A gentle, chronically ill family man, he died in 1882 and — despite his lost faith — was buried in Westminster Abbey near Newton.

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


**Facts:** Abraham Lincoln rose from a one-room Kentucky log cabin and almost no formal schooling to become, largely self-taught, a lawyer, congressman and the sixteenth President of the United States. His election triggered the secession of the southern slave states and plunged the nation into the Civil War, which he was determined to fight to preserve the Union.

He issued the Emancipation Proclamation freeing the enslaved, and distilled the war's higher purpose into the few immortal sentences of the Gettysburg Address. Just days after the war ended in Union victory, he was shot in the head by the actor John Wilkes Booth at Ford's Theatre, and died the next morning — the first American president to be assassinated.

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


**Facts:** Henry VIII began as a golden Renaissance prince — athletic, musical, learned — and curdled into one of England's most fearsome kings. His obsessive hunt for a male heir, and for Anne Boleyn, led him to break with the Pope, declare himself Supreme Head of the Church of England, and dissolve the monasteries, reshaping the country's religion forever.

He married six times — 'divorced, beheaded, died; divorced, beheaded, survived' — executing two wives and a string of former friends and ministers along the way. Grown vast, gout-ridden and paranoid from a festering jousting wound, he died in 1547, leaving a contested succession and a transformed nation.

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


**Facts:** Leonardo da Vinci was the archetypal 'Renaissance man' — painter, anatomist, engineer, inventor and insatiable observer of everything. The illegitimate son of a Tuscan notary, he painted the two most famous pictures in the world, the Mona Lisa and The Last Supper, while filling thousands of mirror-written notebook pages with flying machines, war engines, dissections and studies of water and light.

He left much unfinished, forever chasing the next question, and carried the Mona Lisa around with him for years. He spent his final years in France under the patronage of King Francis I, and died there in 1519 — the famous deathbed scene of him cradled in the king's arms is a lovely legend rather than fact.

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


**Facts:** Christopher Columbus was a Genoese weaver's son and self-taught mariner who spent years hawking a wildly optimistic — and geographically mistaken — plan to reach Asia by sailing west. When Spain's monarchs finally backed him, he crossed the Atlantic in 1492 and made landfall in the Caribbean, convinced to his dying day that he had reached the Indies.

His voyages opened the Americas to European colonisation and its catastrophic consequences for indigenous peoples, whom he enslaved and brutalised — even his own patrons once had him arrested for misrule. He died in 1506 in Valladolid, wealthy but embittered, still insisting he had found a new route to the East rather than an entire new world.

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


**Facts:** Cleopatra VII was the last pharaoh of Egypt, a Greek-descended Ptolemy who — unlike her forebears — actually learned Egyptian and presented herself as the living goddess Isis. Brilliant, multilingual and politically ruthless, she secured her throne and her country's independence by allying herself with, and bearing children to, the two most powerful Romans of the age: Julius Caesar and then Mark Antony.

When she and Antony lost the sea battle of Actium to Octavian in 31 BC, their cause collapsed. Rather than be paraded through Rome as a trophy, she took her own life the next year — famously, though disputedly, by the bite of an asp — and Egypt was swallowed into the Roman Empire.

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


**Facts:** Marie Curie, born Maria Skłodowska in Russian-occupied Poland, studied in a clandestine 'flying university' before escaping to Paris, where she often worked hungry and freezing in a garret. With her husband Pierre she discovered the elements polonium (named for her homeland) and radium, and coined the very word 'radioactivity'.

She became the first woman to win a Nobel Prize, the first person to win two, and the only person ever to win in two different sciences — physics and chemistry. She carried tubes of glowing radium in her pockets, unaware of the danger; the radiation she pioneered eventually killed her in 1934, and her notebooks remain so radioactive they are kept in lead-lined boxes.

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


**Facts:** Winston Churchill packed several lifetimes into one — cavalry officer, war correspondent who escaped a Boer prison camp, painter, bricklayer, Nobel-winning historian, and a politician written off as finished more than once. Then, in 1940, at sixty-five, he became Prime Minister at Britain's darkest hour and, through sheer defiance and thunderous oratory, rallied the country to fight on alone against Nazi Germany.

Bulldog-stubborn, cigar-chomping and prone to the black moods he called his 'black dog', he was voted out almost as soon as the war was won, returned as PM in the 1950s, and lived to be given a state funeral in 1965. His reputation is shadowed by his diehard imperialism, but his wartime leadership remains legendary.

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
- Scene: Baby Tesla on an electrified leash, crackling with sparks. Later, sitting up in bed, he drops his arm from beside his head down to horizontal and blasts through the hotel window into the clouds for one last lightning storm, then falls back and dies.
- Position: leash on the baby, above the waist — birth, clean. Sitting up in bed, he drops his arm from beside his head down to horizontal — a dropping, death-type action — then blasts out through the window and falls back dead; the arm carries 43 in the death position.
- He died 7 Jan 1943, alone in the Hotel New Yorker — the hotel window is real.


**Facts:** Nikola Tesla was a Serbian-American inventor of dazzling, eccentric genius who pioneered the alternating-current (AC) system that powers the modern world, winning the 'War of the Currents' against Thomas Edison's direct current. He claimed to see his inventions fully formed in vivid flashes, and demonstrated wireless power, radio and remote control decades ahead of their time.

Brilliant but hopeless at business, he was repeatedly out-manoeuvred and died alone and broke in a New York hotel in 1943, obsessed in his final years with pigeons and with schemes for transmitting free energy through the air. Long overshadowed by rivals, he has since become a cult hero, and the unit of magnetic flux density — the tesla — bears his name.

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


**Facts:** Vincent van Gogh came to painting late and sold, famously, almost nothing in his lifetime — kept afloat financially and emotionally by his devoted brother Theo, to whom he poured out his soul in hundreds of letters. In barely a decade he produced some 2,000 works of blazing colour and feeling, from the Sunflowers to The Starry Night, all but inventing the language of modern expressive painting.

He was tormented by mental illness, most notoriously cutting off part of his own ear during a breakdown in Arles. In 1890, at thirty-seven, he shot himself in a wheat field and died two days later. His fame — and astronomical prices — came only after his death, making him the archetype of the misunderstood genius.

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


**Facts:** Ben Jonson was Shakespeare's great friend, rival and drinking companion — a bricklayer's stepson who became the leading playwright and poet of his age, a brawler who killed a man in a duel and escaped hanging by pleading 'benefit of clergy'. His satirical comedies such as Volpone and The Alchemist mercilessly skewered human greed and folly.

Learned, combative and hugely self-confident, he became in effect England's first Poet Laureate and gathered a circle of younger admirers, the 'Tribe of Ben'. He fell into poverty and ill health late in life, and died in 1637; he is buried upright in Westminster Abbey under the terse epitaph 'O Rare Ben Jonson'.

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


**Facts:** Voltaire — pen name of François-Marie Arouet — was the sharpest wit and fiercest campaigner of the French Enlightenment: playwright, historian and philosopher who wielded satire as a weapon against tyranny, religious intolerance and injustice. His scorching little novel Candide demolished blind optimism, ending with the advice that we must simply 'cultivate our garden'.

His pen made him rich and famous but also landed him in the Bastille twice and in years of exile. A tireless defender of free speech and of victims of injustice, he grew into the revered sage of Europe, and died in Paris in 1778 at 83, shortly after a rapturous return to the city that had once banished him.

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


**Facts:** John Milton was a prodigiously learned Puritan poet and pamphleteer who threw himself into the English Civil War on Parliament's side, serving Cromwell's government and defending both the execution of Charles I and the freedom of the press (in Areopagitica). The relentless work helped ruin his eyesight, and by his early forties he was completely blind.

Blind and out of favour after the monarchy was restored, he composed his masterpiece Paradise Lost — the vast epic of Satan's rebellion and the Fall of Man — entirely in his head, dictating it to his daughters and assistants. He died in 1674, having built the grandest poem in the English language without being able to see a word of it.

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


**Facts:** Blaise Pascal was a French child prodigy who, to help his tax-collector father, built one of the first mechanical calculators at nineteen. He went on to found the theory of probability (with Fermat), prove key results about vacuums and air pressure — the unit of pressure, the pascal, is named for him — and pioneer the hydraulic press.

Then a profound mystical experience turned him from science to God. He devoted his last years to theology and the unfinished Pensées, home of 'Pascal's Wager', and to defending the Jansenists. Chronically ill and increasingly ascetic, he died in agony at just thirty-nine, probably of stomach cancer or tuberculosis.

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


**Facts:** Michelangelo Buonarroti was the towering genius of the High Renaissance, supreme as both sculptor and painter — a difficult, driven perfectionist who considered himself first and foremost a sculptor, 'freeing' figures already trapped in the marble. From single blocks he carved the David and the Pietà; on his back for four years he painted the ceiling of the Sistine Chapel.

He worked for a succession of demanding popes, feuded with rivals like Raphael and Leonardo, wrote fine poetry, and in old age designed the dome of St Peter's. Fiercely religious and often miserable, he worked almost to the end, dying in Rome in 1564 at the age of 88.

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


**Facts:** Robert Hooke was one of the most inventive and versatile scientists of the seventeenth century — the Royal Society's paid 'Curator of Experiments', expected to devise several new demonstrations a week. He formulated the law of elasticity that bears his name, coined the biological term 'cell' after peering at cork through a microscope, and helped Wren rebuild London after the Great Fire.

Cantankerous and territorial, he feuded bitterly with Isaac Newton over credit for gravity — a quarrel so venomous that, by legend, Newton later saw to it that no portrait of Hooke survived. He died in 1703, brilliant but embittered and largely written out of history until modern times.

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


**Facts:** Augustus — born Octavian — was the teenage great-nephew and heir of Julius Caesar who, after Caesar's assassination, out-manoeuvred and outlasted every rival, including Mark Antony and Cleopatra, to become the first Roman emperor. He ended a century of civil wars and ushered in the Pax Romana, two centuries of relative peace.

A masterful politician, he kept the outward forms of the Republic while holding absolute power, boasting that he had 'found Rome a city of brick and left it a city of marble'. He ruled for over forty years and died in AD 14; on his deathbed he reportedly asked whether he had played his part well in the comedy of life.

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


**Facts:** Charles Dickens was the most popular novelist of the Victorian age and, in effect, its first literary celebrity — a whirlwind of energy who wrote in monthly instalments that left readers on both sides of the Atlantic desperate for the next episode. His own childhood scarred him: at twelve, his father was thrown into debtors' prison and Dickens was sent to labour in a blacking factory, feeding a lifelong crusade against poverty.

From Oliver Twist and A Christmas Carol to Great Expectations, he filled English with unforgettable characters and helped reshape attitudes to the poor. A restless showman who exhausted himself with dramatic public readings, he died suddenly of a stroke in 1870, leaving The Mystery of Edwin Drood forever unfinished.

---

## 26. Michael Faraday 🟢 (1791–1867)

- Birth peg: **91 → Pad**
- Death peg: **67 → Cheque**
- Role: physicist, chemist
- Field: science
- Era: industrial
- Region: british
- End: natural
- Scene: Baby Faraday, surrounded by the leather-bound books of his apprenticeship, has lots of A4 **pads** in which he writes with metal ring binders which he appreciates as a book-binder. They are yanked straight up off the bench by an unseen magnet — electromagnetic induction. Dying, he is offered a **cheque** (the knighthood he refused) and a **Jaguar** and pushes them away — 'what a **cheek**' — as it slides behind him.
- Position: The A4 pads pulled up off the bench by the unseen magnet — lifting, birth action, above the waist; carries 91. The cheque pushed away and behind him — death position; carries 67.
- Death Cheque (67 = CH,K); Jag is the brand-ish alt.
- Historically anchored: apprenticed as a bookbinder; refused a knighthood, insisting on staying plain Mr Faraday.

**Facts:** Michael Faraday rose from a poor London family and a bookbinding apprenticeship — with almost no formal education — to become one of the greatest experimental scientists in history. Largely self-taught, he discovered electromagnetic induction, built the first electric motor and generator, and effectively laid the foundations of the electrical age.

Modest and devout, he refused a knighthood and declined burial in Westminster Abbey, insisting on remaining plain 'Mr Faraday'. A gifted populariser, he founded the Royal Institution's Christmas Lectures for children, which run to this day. He died in 1867; the unit of electrical capacitance, the farad, honours him.

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


**Facts:** Florence Nightingale was a wealthy, well-connected young woman who scandalised her family by refusing marriage and insisting on a career in nursing. During the Crimean War she led a team of nurses into the filthy, overcrowded British military hospital at Scutari, where far more men were dying of disease than of wounds, and transformed it through sanitation and relentless organisation — the 'Lady with the Lamp' on her night rounds.

A pioneering statistician, she used vivid 'coxcomb' diagrams to prove that hygiene saved lives, then founded the first professional nursing school and reformed hospital design worldwide. Bedridden for much of her long later life, she kept campaigning from her sickbed, and died in 1910 aged 90.

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


**Facts:** Alan Turing was the brilliant, unconventional mathematician who, before the war, conceived the theoretical 'Turing machine' that underpins all modern computing. At Bletchley Park during the Second World War he was a driving force behind cracking the German Enigma code — work later credited with shortening the war by years and saving countless lives.

Afterwards he pioneered ideas of artificial intelligence, including the 'Turing test'. In 1952 he was prosecuted for homosexuality, then a crime in Britain, and forced to undergo chemical castration. He died in 1954 of cyanide poisoning, ruled a suicide (a half-eaten apple beside him), though accidental poisoning is also argued. He received an official royal pardon only in 2013.

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


**Facts:** Mark Antony was Julius Caesar's loyal lieutenant, a hard-drinking, charismatic soldier who, after Caesar's murder, turned the Roman mob against the assassins with a famous funeral oration. He then carved up the Roman world with Octavian and Lepidus, taking the wealthy East for himself.

There he fell in love with Cleopatra of Egypt — a liaison Octavian's propaganda spun into proof that Antony had 'gone native' and betrayed Rome. Defeated at the sea battle of Actium in 31 BC and falsely told Cleopatra was already dead, Antony fell on his own sword; she followed him shortly after, and their deaths handed Octavian undisputed mastery of Rome.

---

## 30. René Descartes 🟢 (1596–1650)

- Birth peg: **96 → Badge / Beach**
- Death peg: **50 → Lasso**
- Role: philosopher, mathematician
- Field: philosophy, science
- Era: early-modern
- Region: french
- End: illness
- Scene: On a warm beach, standing up from a recliner. A bright red-orange **badge** on his chest shows the sun and the words "Cogito ergo *Sun*"; he says "I'm pink therefore I am" — red and tanned. Queen Christina appears as the Snow Queen from Narnia and catches him with a huge white **lasso**, dragging him to the floor and into the cold.
- Position: the sun **badge** on his chest — above the waist, front — carries 96, worn as he rises from the recliner on the warm beach (a birth-type action). The white lasso drags him down to the floor and into the cold — pulling down, death action, low position; carries 50. Clean.
- Badge and Beach both encode 96 (Badge = B·J; Beach = B·CH); the chest badge is the number-carrier, the beach is the setting.
- The puns ("sun"; "I'm pink therefore I am") are spoken cues, not pegs. Christina-as-Snow-Queen is an emotional trigger, carrying no number.
- Historically anchored: Descartes died in Stockholm of pneumonia in February 1650, blamed on the cold and Queen Christina's 5am tutorials.


**Facts:** René Descartes was a French soldier-turned-philosopher and mathematician, often called the father of modern philosophy. Seeking absolute certainty, he doubted everything he possibly could until he reached one unshakeable truth — 'I think, therefore I am' (Cogito, ergo sum) — and rebuilt his whole system from there. He also invented analytic geometry and the Cartesian coordinate system that unites algebra and geometry.

A famous late riser who claimed to do his best thinking in bed, he was lured to the freezing Swedish court of Queen Christina, who demanded philosophy lessons at five in the morning. The cold and the punishing schedule broke his health, and he died of pneumonia in Stockholm in 1650.

---

## 33. Julius Caesar 🟢 (100 BC–44 BC)

- Birth peg: **00 → Sauce**
- Death peg: **44 → Warrior**
- Role: ruler, general, statesman
- Field: power, military
- Era: ancient
- Region: roman
- End: assassinated
- Scene: Young Caesar wades across the Rubicon, but the river runs as thick red **sauce**; he ladles and pours yet more red sauce ahead of him — 'the die is cast', ambition and blood. Later, on the Ides of March, a ring of **warriors** closes in and stabs him twenty-three times; he sinks to the Senate floor. Says 'I should have **worried** about the Ides'. His jaw is spun (your dad is 44, I'm gonna spin his jaw).
- Position: The red sauce poured out ahead and around him, in front — birth-type (pouring/creating) action; carries 00. The warriors close in and he falls to the floor — death action, low; they carry 44.
- Sauce (00) — S,S; Warrior (44) — R,R. The warriors carry the number and do the killing.
- BC — the last two digits peg as normal (100 BC → 00, 44 BC → 44). Historically anchored: crossed the Rubicon (49 BC); stabbed 23 times on the Ides of March, 44 BC.

**Facts:** Julius Caesar was the general, politician and writer who did more than anyone to turn the Roman Republic into an empire. A brilliant, ruthless commander, he conquered Gaul, invaded Britain, and — when ordered to disband his army — instead crossed the Rubicon river with it in 49 BC, plunging Rome into civil war with the words 'the die is cast'.

Victorious, he made himself dictator, reformed the calendar (the Julian calendar, and the month of July, carry his name), and was honoured almost as a king — which proved his undoing. On the Ides of March, 44 BC, a conspiracy of senators including his protégé Brutus stabbed him twenty-three times at the foot of Pompey's statue.

---

## 34. Socrates 🟢 (470 BC–399 BC)

- Birth peg: **70 → Case**
- Death peg: **99 → Pepsi**
- Role: philosopher
- Field: philosophy
- Era: ancient
- Region: greek
- End: executed
- Scene: Young Socrates stands in the agora building his **case** which he literally opens — cross-examining everyone, turning each answer into another question (the Socratic method; the charge of 'corrupting the youth' grows from exactly this). Condemned, he calmly drinks down a can of **Pepsi** that is really the hemlock saying 'The taste of (corrupting) the Next Generation'; the can drops from his hand and he sinks to the floor.
- Position: The case argued and held up in front — birth-type action; carries 70. He drinks the Pepsi-hemlock and sinks, the can dropping low — death action; carries 99.
- Case (70) — K,S, tied to his trial/defence (the Apology). Pepsi (99) is a brand peg — P,P(,S) — a drink for a death by drinking poison.
- BC. Historically anchored: executed by hemlock (399 BC) for 'corrupting the youth'; wrote nothing himself — all via Plato.

**Facts:** Socrates left no writings of his own; almost everything we know comes through his devoted pupil Plato. A stonemason's son with a famously ugly face, he shuffled around the Athenian marketplace barefoot, buttonholing the powerful and dismantling their certainties with relentless questions — the 'Socratic method' still used in classrooms and courtrooms today.

He claimed only to know that he knew nothing, and made many enemies by exposing the ignorance of others. Charged with impiety and 'corrupting the youth' of Athens, he was condemned to death and calmly drank a cup of hemlock in 399 BC, choosing death over exile or silence — the founding martyr of Western philosophy.

---

## 35. Alexander the Great 🟢 (356 BC–323 BC)

- Birth peg: **56 → Leash**
- Death peg: **23 → Anemone**
- Role: king-emperor, general, ruler
- Field: power, military
- Era: ancient
- Region: macedonian
- End: uncertain
- Scene: Boy Alexander tames the wild horse Bucephalus, slipping a **leash** over it and leading it in triumph — the feat that first marked him out, watched by his tutor Aristotle. Years later, never once beaten in battle, he collapses wearing **Michael Jordan 23** shirt into the marshes of Babylon and sinks among sea-**anemones** that close over him — the fever that killed him at 32. Says 'I'm Alexander the GOAT'.
- Position: The leash slipped on and the horse led, up and in front — birth action; carries 56. He sinks into the anemone-filled marsh, low and closing over him — death action; carries 23.
- Leash (56) — L,SH (brand alternative: Lush). Anemone (23) — first two sounds N,M. Aristotle and Bucephalus are hooks.
- BC and reversed: birth 56 is larger than death 23 (356 BC → 56, 323 BC → 23). Cause of death uncertain — typhoid or poison; the marsh reading leaves it open.

**Facts:** Alexander III of Macedon was tutored as a boy by Aristotle and, legend says, tamed the unrideable warhorse Bucephalus before he was even a teenager. Taking the throne at twenty after his father's murder, he launched one of history's greatest military campaigns, never losing a battle as he shattered the mighty Persian Empire and drove his army all the way to India.

By thirty he ruled from Greece to the Punjab, founding some twenty cities named Alexandria and spreading Greek culture across the known world. Then, at just thirty-two, he died suddenly in Babylon — of fever, typhoid, or perhaps poison — and his vast empire was promptly torn apart by his squabbling generals.

---

## 38. Beethoven 🟢 (1770–1827)

- Birth peg: **70 → Casio**
- Death peg: **27 → Neck**
- Role: composer
- Field: music
- Era: enlightenment
- Region: german
- End: illness
- Scene: Deaf Beethoven leans over a **Casio** keyboard, composing furiously — pressing close to feel the vibrations of music he can no longer hear (he really did saw the legs off his piano for this). At the premiere of the Ninth a hand gently turns his **neck** around so he can see the ovation he cannot hear; then, on his deathbed, the head drops and the neck goes limp as he dies.
- Position: The Casio played and composed on, in front — birth (creating) action; carries 70. The neck turned to the ovation, then dropping limp in death — death action, low; carries 27.
- Casio (70) — K,S, an apt keyboard for a composer; Neck (27) — N,K, the famous turning-to-see-the-ovation moment.
- Historically anchored: went deaf yet conducted the Ninth and had to be turned to see the applause; sawed the legs off his piano to feel vibrations.

**Facts:** Ludwig van Beethoven bridged the Classical and Romantic eras and transformed what music could express. A volcanic, untidy, short-tempered genius, he arrived in Vienna as a brilliant young pianist — and then, in his late twenties, began to go deaf, the cruellest fate imaginable for a musician.

Rather than give up, he composed some of his greatest works in near-total silence, 'hearing' them only in his mind, and famously had to be turned around at the premiere of his Ninth Symphony to see an ovation he could not hear. He sawed the legs off his piano to feel its vibrations through the floor. He died in 1827, and some ten thousand people are said to have joined his funeral procession.

---

## 46. Joan of Arc 🟢 (1412–1431)

- Birth peg: **12 → Tin**
- Death peg: **31 → Meat**
- Role: general
- Field: military
- Era: medieval
- Region: french
- End: executed
- Scene: A teenage peasant girl buckles on a **tin** suit of armour and lifts the siege of Orléans. Captured, she is burned at the stake — her body consumed like **meat** on the fire, but her heart, they said, would not burn.
- Position: The tin armour buckled on, worn up and in front — birth position; carries 12. Burned low at the stake, consumed like meat — death, low; carries 31.
- The heart-that-wouldn't-burn is the vivid hook on the death peg.
- Historically anchored: illiterate teenage peasant who lifted the siege of Orléans; burned at the stake at 19; exonerated 25 years later.

**Facts:** Joan of Arc was an illiterate teenage peasant girl who, convinced she heard the voices of saints, talked her way into the presence of the French heir during the Hundred Years' War and persuaded him to let her lead an army. Clad in white armour, she inspired the French to lift the siege of Orléans and turned the tide of the war, seeing him crowned king.

Captured by the English and their allies, she was tried for heresy and witchcraft and burned at the stake in 1431, aged only nineteen; witnesses claimed her heart would not burn. Twenty-five years later a retrial cleared her name, and centuries afterwards the Church declared her a saint — France's warrior-martyr and patron.

---

## 48. Rembrandt 🟢 (1606–1669)

- Birth peg: **06 → Sash**
- Death peg: **69 → Shop**
- Role: artist
- Field: arts
- Era: early-modern
- Region: dutch
- End: natural
- Scene: Baby Rembrandt Has a **Rubiks cube** (visual peg) but throws it saying "I'm a portrait artist not a cubist". Puts on a bright **sash** across his chest and paints himself again and again in rich costume — the \~80 self-portraits. Bankrupt, everything is dragged into a pawn **shop** which says '**Cheap Shop**' and auctioned off, and he sinks into an unmarked pauper's grave. He says 'my whole life was charioscuro'.
- Position: The Rubiks Cube thrown in the air; sash worn across the chest as he paints himself, in front — birth position; carries 06. His goods hauled off to the shop/auction as he sinks — death, low; carries 69.
- Historically anchored: \~80 self-portraits; bankrupt in 1656, possessions auctioned; buried in an unmarked pauper's grave.

**Facts:** Rembrandt van Rijn was the greatest painter of the Dutch Golden Age, a miller's son who became famous and wealthy in Amsterdam for his dramatic play of light and shadow and his uncanny gift for capturing the inner life of his subjects. He painted around eighty searching self-portraits across his life, an unmatched visual autobiography from cocky youth to ruined old age.

He lived beyond his means, and after the death of his wife Saskia his fortunes collapsed; declared insolvent in 1656, he watched his house and possessions auctioned off. He kept painting masterpieces to the end, but died poor in 1669 and was buried in an unmarked pauper's grave.

---

## 96. Hannibal 🟢 (247 BC–183 BC)

- Birth peg: **47 → Rock**
- Death peg: **83 → Foam**
- Role: general
- Field: military
- Era: ancient
- Region: carthaginian
- End: suicide
- Scene: Hannibal drives his war-elephants up over the jagged **rock**s of the snowbound Alps to fall on Rome from the north — the boldest march of the ancient world. He is calling out "(Ag)**Ricola**!" like the advert in the mountains, challenging the Romans. Cornered decades later, rather than be handed to Rome he drains a cup of poison **vomit**s (Hannibal Puka) and dies with **foam** on his lips. Says "I was poisoned like the snakes I used on the boats. *The foam of Rome*"
- Position: The rocks of the Alps scaled and crossed, high and ahead — birth (lifting) action; carries 47. The poison foam low on his lips as he dies; carries 83.
- Crossed the Alps with elephants to invade Italy; won crushing victories but never took Rome; took poison to avoid capture.

**Facts:** Hannibal Barca of Carthage was Rome's most feared enemy, a general who as a boy reputedly swore an eternal oath of hostility to Rome. In 218 BC he did the unthinkable, leading an army — complete with war elephants — across the Pyrenees and the snowbound Alps to strike at Italy from the north, catching the Romans completely off guard.

For fifteen years he rampaged almost unbeaten through Italy, annihilating a vast Roman army at Cannae in one of the most studied battles in history. Yet he could never take Rome itself, was recalled to defend Carthage, and lost at Zama, spending his last years as a hunted exile advising Rome's other enemies. Rather than be captured and paraded through the streets of the city he had sworn to destroy, he took poison, around 183 BC.

---

## 97. Mary Shelley 🟢 (1797–1851)

- Birth peg: **97 → Book**
- Death peg: **51 → Light**
- Role: writer
- Field: literature
- Era: industrial
- Region: british
- End: illness
- Scene: Eighteen-year-old Mary, in a ghost-story contest at a stormy Swiss villa, dreams up a **book** like no other — Frankenstein, the scientist who steals the spark of life. She stands up and opens it and the monster steps out with a glowing heart. People say "Looks like he was bought at **Lidl**!". She turns into the **lady** monster he never had and that same reanimating **light** finally gutters and goes out as, widowed and ill, she collapses and dies alongside the monster as his consort.
- Position: The book of Frankenstein conceived and written, held up in front — birth (creating) action; carries 97. The spark-light extinguished as she dies, low; carries 51.
- Wrote Frankenstein at 18 after a ghost-story challenge at the Villa Diodati; daughter of Mary Wollstonecraft.

**Facts:** Mary Shelley was the daughter of two radical thinkers — the pioneering feminist Mary Wollstonecraft, who died giving birth to her, and the philosopher William Godwin. At sixteen she eloped with the married poet Percy Bysshe Shelley, and two years later, during a wet, gloomy summer at Lord Byron's Villa Diodati on Lake Geneva, the group challenged one another to write ghost stories.

From a waking nightmare, the teenage Mary produced Frankenstein — the tale of a scientist who assembles and reanimates a creature, then recoils in horror from it — often called the first true science-fiction novel and a profound meditation on ambition and responsibility. Her later life was marked by tragedy: the drowning of Percy and the deaths of three of her four children. She kept writing, guarded her husband's legacy, and died of a brain tumour in 1851.

---

## Open items

- **Faraday (26)** — birth peg mis-encoded (pin/pan = 92, not 91); Pot proposed, needs confirming.
- **Genghis (4)** — cause of death unresolved.
- **Lincoln (9)** — visual not strong enough.
- **Tesla (16)** — arm is in birth position but carries the death number.
- **Curie (14), Van Gogh (17)** — death objects not clearly low or behind.
- **Pascal (21)** — death peg was mis-encoded (notch/niche/gnash = 26, not 62), provisionally corrected to Chain. Confirm or pick Chin/Genie.
- **Dickens (25)** — goose is held, not dropped; needs the low/falling fix.
- **Nightingale (27)** — Role uses `nurse` and `statistician`; both now added to the Role vocabulary.
- **Duplicate object pegs across scenes**: Ink (Newton 2 / Genghis 4), Ape (Darwin 8 / Lincoln 9 — same year, so defensible), Leash (Mozart 1 / Tesla 16), Tin/Ton (Dickens 25 / Turing 28 — same year-ending, distinct words), Mice (Cleopatra 13 / Mark Antony 29 — same death year, deliberate).
- **Century marker crowding**: six figures sit in the 1800s and the key offers only Tim Vine and David Frost for 18. Markers are selective — drop them where the century is obvious.

## Backlog

Dates and candidate peg words; no scenes yet. Word lists are options to pick from, not decisions. Facts line is there to spark the hook — the strongest scenes come from something the figure actually did.

**Gottfried Leibniz** — 1646 / 1716
Birth **46**: Roach, Ridge · Death **16**: Dish, Dash, Ditch
*Invented calculus independently of Newton, and the priority dispute poisoned both their lives. Binary arithmetic. "The best of all possible worlds" — the line Voltaire mocked in Candide. Both slots are thin.*
🟡 **Raja (46) flagged for geographic mismatch** — his Eastern link was the Chinese *I Ching*, which he read as confirmation of his binary arithmetic, not anything Indian. Left in place for now; a Chinese-flavoured 46 would be better but the slot has only Roach and Ridge to work with.

**Nicolaus Copernicus** — 1473 / 1543
Birth **73**: Comb, Gum, Camel, Camel *(cigs)* · Death **43**: Ram, Arm, Rum, Room, Rim, Rimmel
*Put the sun at the centre and sat on it for decades — De revolutionibus was published the year he died, the first copy reportedly reaching him on his deathbed. Canon of Frombork cathedral; astronomy was the side project. Raised by his bishop uncle after his father died, which is the strongest unused birth-scene angle.*
🔴 Neither slot locked. Note: **Game and Camo are not available for 73** — Game was struck from the dictionary as a non-noun (see major_system_pegs_0-100.md audit), and Camo is abstract. Comb and Gum are the live options.


**Galileo Galilei** — 1564 / 1642
Birth **64**: Chair, Shore, Cherry · Death **42**: Rhino, Wren, Rain, Orange, Renault
*Improved the telescope, found Jupiter's moons. Tried by the Inquisition, forced to recant heliocentrism, spent his last years under house arrest, blind. Shares a birth year with Shakespeare (3) and a death year with Newton's birth.*

**J.S. Bach** — 1685 / 1750
Birth **85**: Foil, File, Volvo · Death **50**: Lace, Lice, Lasso, Listerine
*Twenty children. Walked 250 miles to hear an organist play. Jailed for a month for trying to leave a job. Died after botched eye surgery by the same quack who blinded Handel.*


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


**Captain James Cook** — 1728 / 1779
Birth **28**: Knife, Nephew, Navy, Nivea · Death **79**: Cap, Cub, Cop, Cab, Cape
*Charted New Zealand and eastern Australia. Beat scurvy with sauerkraut. Killed in the surf at Kealakekua Bay, Hawaii, in a scuffle over a stolen boat.*


**Marie Antoinette** — 1755 / 1793
Birth **55**: Lily, Lolly, Lilac, Lyle's · Death **93**: Bomb, Beam, Puma, Pom, BMW
*Never said "let them eat cake". Played at being a shepherdess in a fake hamlet at Versailles. Guillotined nine months after her husband; apologised to the executioner for treading on his foot.*

**Ludwig Wittgenstein** — 1889 / 1951
Birth **89**: Fob, Fop, Fibre-optic, Fab · Death **51**: Light, Lad, Lady, Ladder, Lidl
*Gave away a vast family fortune. Worked as a village schoolteacher, a gardener, and a hospital porter. Wrote one book in his lifetime, then spent it arguing against himself. Last words: "Tell them I've had a wonderful life."*

**Emmeline Pankhurst** — 1858 / 1928
Birth **58**: Leaf, Elf, Olive, Loaf, Levi's · Death **28**: Knife, Nephew, Navy, Nivea
*Led the militant suffragettes. Arrested repeatedly; hunger strikes and force-feeding; released and re-arrested under the "Cat and Mouse" Act. Died weeks before women got the vote on equal terms.*
