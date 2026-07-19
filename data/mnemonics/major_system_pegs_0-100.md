# Major System Pegs 0–100

Master peg dictionary. Object pegs and character pegs.

## Encoding

| Digit | Sounds |
|---|---|
| 0 | S, Z (soft C) |
| 1 | T, D |
| 2 | N |
| 3 | M |
| 4 | R |
| 5 | L |
| 6 | J, SH, CH, soft G |
| 7 | K, hard G |
| 8 | F, V |
| 9 | P, B |

Vowels, W, H and Y are silent — ignore them when checking a word's code.

## Rules

- **Phonetics, not spelling — always.** The spoken sound is the sole criterion, everywhere in the system, for both object and character pegs. Never the written letter, never the alphabet letter-name. Say the word aloud and encode what you hear. (The only exceptions are the object pegs explicitly marked as letter-identity cheats — M&Ms, J&J, FF.)
- **Nouns only** — concrete, physical, pointable. No verbs, adjectives, or abstract nouns.
- **Object pegs** are exact matches unless marked *(rlx)* for relaxed. Four relaxations are allowed, all valid only for fixed lookup, never for decoding arbitrary digit strings:
  1. trailing sounds dropped — Emerald, Gold, Laurel
  2. leading S dropped — Snail, Screw, Snare, Staff
  3. letter-identity via a word's own name — M&Ms, J&J, FF
  4. letter-identity via a person's or character's initials — George Foreman, FB
- **Character pegs:** pure two-initials method. Two separate names (first + last, or a famous pair), each contributing one digit. Single-name word-phonetic entries are rejected.
  - **Silent-initial rule:** where a name begins with a silent or unassigned letter (vowels, H, W, Y), skip it and take the **first consonant sound**. Harry Kane = R,K = 47. Wayne Rooney = N,R = 24. Ossie Ardiles = S,R = 04. This supersedes the earlier "vowel-initial names are invalid" rule, which was wrong — Elmer Fudd is a perfectly good 58 (L,F).
  - **Spelling traps.** Say it aloud; the page will mislead you. Chalk → **CH,K** = 67 (the L is silent). Phillips → **F** (PH), not P. Hughes → **Z** (H and Y silent). Wright → **R**. Chris → **K** but Charlton → **CH**. Geoff → **J** — and note Geoff and Phillips are the same trap in reverse. Cole → **K**. Gascoigne → hard **G**. Gervais → soft **G**. Thierry → **T**. Cameron → **K**, never S.
- **Birth/death placement:** birth objects and actions above the waist or in front (creating, planting, picking, lighting, inflating, catching, lifting). Death objects and actions below the waist or behind (dropping, extinguishing, smashing, deflating, crushing).

## Status key

🟢 locked · 🟡 working draft, mechanics fine but not final · 🔴 unresolved gap

---

## Visual pegs

**A separate system from everything below.** These encode by *shape*, not by sound — a trident is 3 because it has three prongs, not because of its consonants (T,R,T,N,T would be 41214). Never mix the two in one lookup, and flag any instance entry that uses a visual peg so it isn't read phonetically. Currently used by Hooke's death peg (instances #23).

Candidate visual pegs for 0–20 below — **suggestions / alternatives to pick from**, not
locked. Shape is the encoding basis; **Swan (2)** and **Trident (3)** are the ones
currently in use. The extra columns collect parallel association aids the same numbers can
hang off — a body-part list and a colour/design scheme.

| # | Shape / object suggestions | Body part | Colour / design |
|---|---|---|---|
| 0 | Noose, floatie, donut, football, ring, plate, letter "O", severed head | Anus | black & white circle |
| 1 | Candle, flute, tall horn, unicorn, staff/stick, numeral "1", arrow, bat | Finger | pale green (dollar) |
| 2 | **Swan** *(in use)*, socks, bicycle, hook, two heads, spiral shell, yin-yang | Feet | — |
| 3 | **Trident** / fork *(in use — 3 prongs)*, traffic lights, pyramid, triceratops/trike, triangle, handcuffs | Buttocks | azure & white (clouds) |
| 4 | Four-leaf clover, swastika, car, quad bike, square, diamond | Head (pointy) | diamond |
| 5 | Five-point star, hand, Olympic rings, beehive, white glove, pentagon, "V" | Hand | yellow & black stripes |
| 6 | Six-pack, Star of David, ants/anthill, Rubik's cube, artic truck, hexagon, snowflake | Abdomen | — |
| 7 | Rainbow, bow tie (007), calendar, wax-seal rosette, hockey stick, seal (seven seals), boomerang | Nose (upside-down) | rainbow |
| 8 | Octopus/spider, cobweb, handcuffs, round glasses, crawler bot | Eyes | red & deep blue |
| 9 | Cat, fireman/police helmet, baton, Moses' staff, police car, balloon, monocle | Ear | Belgian flag (black/yellow/red) |
| 10 | Toes, Ravana (ten heads), hen, oversized keeper gloves, stone tablet, letter "X" | Toes | blue & silver (pharaoh) |
| 11 | Skis, toy rocket (Apollo 11), chopsticks, stilts, giant legs, numeral "11" | Legs | silver |
| 12 | Calendar, Indian headdress, buffalo, dozen yellow crocuses | Ribs | — |
| 13 | Witch's hat, devil horns, broken mirror, black cat | — | fiery red & orange |
| 14 | Bouquet of red roses, crystal carriage, heart | — | pink |
| 15 | Gold bar, umpire's chair (15-1), 3-step podium, strawberries & cream / tennis racquet | — | green & purple |
| 16 | Cake, sweets, Latymer badge/tie, big red bus | — | blue & black stripes |
| 17 | Magazine / lip gloss, wand, wizard hat, Zac Efron (17 Again) | — | — |
| 18 | Golf club, bunker & flag, plus-fours, golf buggy | — | — |
| 19 | Machine gun, helicopter, dog tags / soldier's hat | — | military green & yellow |
| 20 | Dartboard, giant pint, dart-shaped car | — | red & black segmented circle |

**Symbolic / number-association pegs** — not shape or sound, but a pure cultural
association tied to a number. Flag any instance using one so it isn't read phonetically.

| # | Symbol | Association |
|---|--------|-------------|
| 23 | Goat | GOAT — "greatest of all time"; Michael Jordan's number 23 |


---

## Object pegs

| # | Sounds | Words | Brands |
|---|--------|-------|--------|
| 0 | S/Z | Saw, Zoo, Ice, Hose | — |
| 1 | T/D | Tie, Tea, Doe, Hut, Head | — |
| 2 | N | Hen, Knee, Inn, Honey, Wine | — |
| 3 | M | Ma, May, Ham, Emu, Ammo | — |
| 4 | R | Rye, Roe, Ear, Hair, Oar | — |
| 5 | L | Owl, Ale, Hall, Eel, Wool | — |
| 6 | J/SH/CH | Shoe, Jay, Ash, Jaw, Chai | — |
| 7 | K/G | Cow, Key, Oak, Egg, Hawk, Sock *(rlx)* | — |
| 8 | F/V | Ivy, Hoof, Hive, Oaf, Wave | — |
| 9 | P/B | Pie, Bee, Ape, Hoop, Hub, Soap *(rlx)* | — |
| 10 | TS | Toes, Dice, Oats, Ties, Dose | Tesco |
| 11 | TT/TD/DD | Toad, Tot, Date, Dot, Dad | Tide |
| 12 | TN | Tin, Den, Dawn, Ton, Down, Tan, Tuna | Tango |
| 13 | TM | Tomb, Dime, Dam, Team, Time | Timberland |
| 14 | TR | Tire, Deer, Door, Tar, Tower | Terry's Chocolate Orange |
| 15 | TL | Tail, Dial, Doll, Tile, Towel | Tilda |
| 16 | TSH/TCH | Dish, Dash, Ditch, Dutch | — |
| 17 | TK | Tack, Duck, Dog, Deck, Tag | TK Maxx |
| 18 | TF | Dove, Toffee, Diva, Staff *(rlx)* | Tefal |
| 19 | TP | Tub, Tape, Tip, Tuba *(rlx)*, Tap | Toblerone |
| 20 | NS | Nose, Noose, Ounce, Niece | Nescafé, Nissan *(rlx)* |
| 21 | NT | Knot, Net, Note, Aunt | Nutella |
| 22 | NN | Nun, Onion, Neon, Nanny, Naan | — |
| 23 | NM | Gnome, Number, Anemone *(rlx)* | — |
| 24 | NR | Nurse *(rlx)*, Snare *(rlx)* | — |
| 25 | NL | Nail, Nile *(proper)*, Noel *(proper)*, Snail *(rlx)* | — |
| 26 | NJ/NSH/NCH | Nacho, Notch | — |
| 27 | NK | Neck, Nag, Hank, Nook, Ink | Nike |
| 28 | NF | Knife, Nephew, Navy | Nivea |
| 29 | NP | Knob, Nib, Nappy | — |
| 30 | MS | Mouse, Mice, Moose, Maze | Maserati |
| 31 | MT | Mat, Meat, Mud, Moat | Mattel |
| 32 | MN | Moon, Money, Mine, Mane | Monopoly |
| 33 | MM | Mummy, Mime, Mama, Mum, Mammoth | M&Ms *(letter cheat)* |
| 34 | MR | Mower, Mirror, Mare, Moor, Mayor, Myrrh, Hammer, Emerald *(rlx)* | Marmite |
| 35 | ML | Mail, Mule, Mole, Mall, Mill | Milky Way |
| 36 | MJ/MSH/MCH | Mash, Match, Mesh, Mush | Michelin |
| 37 | MK | Mug, Mic, Mac, Mocha | McDonald's |
| 38 | MF | Muff, Muffin *(rlx)* | — |
| 39 | MP | Map, Mop, Amp | — |
| 40 | RS | Rose, Rice | Rice Krispies |
| 41 | RT | Root, Rat, Rod | Ritz |
| 42 | RN | Rhino, Wren, Rain, Orange *(rlx)* | Renault |
| 43 | RM | Ram, Arm, Rum, Room, Rim, Roman *(rlx)*, Rambo *(rlx)* | Rimmel |
| 44 | RR | Rear, Aurora, Warrior | — |
| 45 | RL | Reel, Rail, Roll, Aerial | Rolex, Rolls-Royce |
| 46 | RJ/RSH/RCH | Roach, Ridge, Raja | — |
| 47 | RK | Rock, Rack, Rake, Rag, Rug | Ricola |
| 48 | RF | Roof, Reef, Ref, Ruff, RAF, Roofer *(rlx)*, Rifle *(rlx)*, Raft *(rlx)*, Rover *(rlx)*, Refugee *(rlx)*, Reverend *(rlx)*, Ravioli *(rlx)* | Ryvita, Revlon, Revels |
| 49 | RP | Rope, Robe, Rib, Ruby | Reebok, Ribena |
| 50 | LS | Lace, Lice, Lasso | Listerine |
| 51 | LT | Light, Lad, Lady, Ladder *(rlx)*, Lute, Ladle *(rlx)*, LED, Loot | Lidl |
| 52 | LN | Lion, Lawn, Lane, Loon, Alien, Lung | Lenor |
| 53 | LM | Lamb, Lime, Lemon, Llama, Loom, Elm, Lima *(proper)*, Lemur *(rlx)* | Lamborghini |
| 54 | LR | Lyre, Lure, Liar, Lorry, Laurel *(rlx)* | L'Oréal |
| 55 | LL | Lily, Lolly, Lilac *(rlx)* | Lyle's Golden Syrup |
| 56 | LJ/LSH/LCH | Leash, Leech, Lash | Lush |
| 57 | LK | Lock, Lake, Log, Leg | LEGO, Lucozade |
| 58 | LF | Leaf, Elf, Olive, Loaf | Levi's |
| 59 | LP | Lobe, Lip, Lab, Loop | Lipton |
| 60 | SHS/CHS | Shoes, Chess, Juice, Cheese | — |
| 61 | SHT/CHT | Sheet, Jet, Shuttle *(rlx)* | — |
| 62 | SHN/CHN | Chin, Chain, Genie | Chanel |
| 63 | SHM/CHM | Chime, Gem, Chum, Jam, Chimney *(rlx)* | — |
| 64 | SHR/CHR | Chair, Shore, Cherry | — |
| 65 | SHL/CHL | Shell, Jail, Shawl, Jewel, Jelly | Shell |
| 66 | JJ | Judge, Jujube | Johnson & Johnson (J&J) |
| 67 | SHK/CHK | Chalk *(L is silent — CH,K)*, Cheque, Shack, Jockey, Jug, Jag | Jaguar *(rlx — trailing R dropped)* |
| 68 | SHF/CHF | Chef, Chief, George Foreman *(rlx)* | — |
| 69 | SHP/CHP | Ship, Shop, Sheep, Chip, Chop, Jeep | Chupa Chups |
| 70 | KS/GS | Case, Goose, Gauze | Casio |
| 71 | KT/GT | Cat, Coat, Kite, Goat, Kid | Kit Kat |
| 72 | KN/GN | Cane, Coin, Gun, Can, Queen, Canoe | Canon |
| 73 | KM/GM | Comb, Gum, Camel *(rlx)* | Camel *(cigarettes)* |
| 74 | KR/GR | Car, Core, Gear, Choir, Screw *(rlx)* | Corona, Carlsberg |
| 75 | KL/GL | Coal, Coil, Eagle, Gold *(rlx)* | Colgate, Kellogg's |
| 76 | KJ/KSH/KCH | Cash, Coach, Couch, Cage | Gucci |
| 77 | KK | Cook, Kayak, Cake, Cog | Coke, Coca-Cola |
| 78 | KF/GF | Cave, Coffee, Cuff, Cove | KFC |
| 79 | KP/GP | Cap, Cub, Cop, Cab, Cape | — |
| 80 | FS | Vase, Fuse, Face, Fez | Fisher-Price |
| 81 | FT | Foot, Vet, Vat | Fiat, Fitbit |
| 82 | FN | Van, Fan, Phone | Fanta |
| 83 | FM | Foam, Femur *(rlx)*, Vomit *(rlx)* | Famous Grouse |
| 84 | FR | Fire, Fur, Ferry | Ferrari |
| 85 | FL | Foil, File | Volvo |
| 86 | FSH/FCH | Fish, Fisherman *(rlx)* | Fisherman's Friend |
| 87 | FK | Fig, Fog | Facebook |
| 88 | FF | Fife, Fiver *(rlx)*, FF *(rlx)* | FIFA |
| 89 | FP | Fob, Fop, Fibre-optic *(rlx)*, FB *(rlx)* | Fab |
| 90 | BS/PS | Bus, Bees, Bass, Boss | Bose |
| 91 | BT/PT | Boat, Bat, Bud, Pot, Pad, Boot, Bed, Butt, Booty | Budweiser, BT |
| 92 | BN/PN | Bone, Pin, Pen, Bun, Pony | Bounty |
| 93 | BM/PM | Bomb, Beam, Puma, Pom | BMW |
| 94 | BR/PR | Bear, Pear, Boar, Beer | Burger King |
| 95 | BL/PL | Ball, Bell, Pal, Pill | PlayStation |
| 96 | BSH/PSH/BCH/PCH | Beach, Peach, Bush, Badge | Bosch |
| 97 | BK/PK | Book, Pig, Bike, Pack, Peak | Bacardi |
| 98 | BF/PF | Beef, Puffin *(rlx)*, Beaver *(rlx)*, Pavarotti *(rlx)* | Beefeater |
| 99 | BB/PB/PP | Baby, Poppy, Pipe, Puppy | Pepsi |
| 100 | DSS/TSS | Daisies, Tissues | — |

---

## Year-ending 00–09

Only for years whose last two digits are 00–09, where the tens-place zero must be phonetically present (S/Z sound). Not needed for freestanding digits 0–9 — see the top of the table above.

| # | Sounds | Words | Brands |
|---|--------|-------|--------|
| 00 | SS/SZ | Sauce | — |
| 01 | ST/SD | Seed, Suit | — |
| 02 | SN | Sun | Snickers |
| 03 | SM | Seam, Sum *(accepted exception — abstract, kept for the finance pun)* | Samsung |
| 04 | SR | Sewer, Sari | — |
| 05 | SL | Seal, Sail | Solero |
| 06 | SSH/SCH | Sash | — |
| 07 | SK/SG | Sack, Sock | Skoda |
| 08 | SF/SV | Safe, Sofa, Sieve | — |
| 09 | SP/SB | Soap, Ape *(accepted exception — single sound, missing the tens-zero; year-ending pegs only, see instances #8)* | Subway |

---

## Century markers (prefix 10–20) 🟢

Canonical. Used selectively in scenes — only when the century itself needs reinforcing, not by default. Pure initials, both names required, checked against actual pronunciation rather than the alphabet letter-name.

| Prefix | Option 1 | Check | Option 2 | Check |
|---|---|---|---|---|
| 10 | Tom Sawyer | T,S = 1,0 | Tony Soprano *(adult tone)* | T,S = 1,0 |
| 11 | Tony Tiger | T,T = 1,1 | Donald Duck | D,D = 1,1 |
| 12 | Tom Nook | T,N = 1,2 | — | — |
| 13 | Tim Minchin | T,M = 1,3 | David Mitchell | D,M = 1,3 |
| 14 | Daniel Radcliffe | D,R = 1,4 | Tim Roth / The Rock *(TH treated as T — convention choice, not standard across Major System variants)* | T,R = 1,4 |
| 15 | David Lynch | D,L = 1,5 | Tom Lehrer *(niche)* | T,L = 1,5 |
| 16 | Tom & Jerry | T,J = 1,6 | — | — |
| 17 | Tom Kerridge *(UK chef, moderate fame)* | T,K = 1,7 | Toby Keith | T,K = 1,7 |
| 18 | Tim Vine | T,V = 1,8 | David Frost | D,F = 1,8 |
| 19 | David Beckham | D,B = 1,9 | Tony Blair | T,B = 1,9 |
| 20 | Nigel Slater | N,S = 2,0 | Nancy Sinatra | N,S = 2,0 |

"Tom" alone and "Tony" alone are not used anywhere as standalone word-phonetic entries — every pick requires both names. All eleven rows check out phonetically.

---

## Character pegs 00–99

Two-initials method. **Bold** = confirmed/in use. Footballers added as extra options, not replacements — the point is collision-proofing, so more per slot is better.

**No primary.** Every name in a slot is equally usable — pick whichever suits the scene. Characters are currently used lightly, as century markers and emotional triggers in `mnemonic_implementations.md`, and carry no number in the emotional-trigger role. More options per slot is the point.

No actions are assigned here. If PAO with actions is ever adopted, that layer lives in `pao.md` and would need a designated person per number; until then this table stands alone and is the source of truth for characters.

There is no separate `character_pegs_0-100.md`.

| # | Options |
|---|---|
| 00 | Steven Spielberg, Zinedine Zidane |
| 01 | Steve Davis |
| 02 | Sam Neill, Sid & Nancy *(pair — fine as a static peg, but won't carry a single action if PAO is added later)* |
| 03 | Sarah Millican, Stanley Matthews, Sadio Mané |
| 04 | Salman Rushdie, Ossie Ardiles |
| 05 | Stan Laurel |
| 06 | Sid James |
| 07 | Simon Cowell, Sergio Agüero, Sol Campbell |
| 08 | Sam Fox |
| 09 | Syd Barrett |
| 10 | **Tom Sawyer**, Tony Soprano, David Seaman |
| 11 | **Tony Tiger**, Donald Duck, Didier Drogba, Tony Adams |
| 12 | **Tom Nook**, Thierry Henry |
| 13 | **Tim Minchin**, David Mitchell, Diego Maradona |
| 14 | **Daniel Radcliffe**, Tim Roth, Declan Rice |
| 15 | **David Lynch**, Tom Lehrer, Denis Law, Dele Alli |
| 16 | **Tom & Jerry**, Teddy Sheringham |
| 17 | **Tom Kerridge**, Toby Keith, Diego Costa |
| 18 | **Tim Vine**, David Frost |
| 19 | **David Beckham**, Tony Blair, Dennis Bergkamp, Trevor Brooking |
| 20 | **Nigel Slater**, Nancy Sinatra, Nina Simone, Nobby Stiles |
| 21 | Neil Diamond, Norman Whiteside |
| 22 | Nick Nolte, Andrés Iniesta |
| 23 | Nicki Minaj |
| 24 | Nick Robinson, Wayne Rooney, Ian Wright, Ian Rush |
| 25 | Nick Leeson, Nat Lofthouse |
| 26 | Nathan Jones |
| 27 | Noel Gallagher, Andy Cole |
| 28 | Nick Faldo, Nemanja Vidić |
| 29 | Nigel Benn |
| 30 | Mo Salah, Emile Heskey |
| 31 | Matt Damon |
| 32 | Martina Navratilova, Michael Owen |
| 33 | Mickey Mouse |
| 34 | Marcus Rashford |
| 35 | Mark Lawrenson, Matt Le Tissier |
| 36 | Michael Jackson |
| 37 | Mel Gibson |
| 38 | Michael Fish |
| 39 | Michael Palin, Michael Ballack |
| 40 | Rick Stein, Raheem Sterling |
| 41 | Ricky Tomlinson |
| 42 | Rafael Nadal, Arsène Wenger |
| 43 | Ricky Martin |
| 44 | **Rory the Racing Car**, Aaron Ramsey |
| 45 | Rob Lowe, Erling Haaland |
| 46 | Ricky Gervais |
| 47 | Ronnie Corbett, Roy Keane, Ryan Giggs, Harry Kane, Eric Cantona |
| 48 | Rio Ferdinand, Robbie Fowler |
| 49 | Rob Brydon |
| 50 | Lisa Simpson |
| 51 | Leonardo DiCaprio |
| 52 | Liam Neeson, Alan Hansen |
| 53 | Lee Mack, Lionel Messi, Luka Modrić |
| 54 | Lisa Riley, Alf Ramsey |
| 55 | Lois Lane |
| 56 | Lily James, Alan Shearer |
| 57 | Lorraine Kelly |
| 58 | Luther Vandross, Les Ferdinand, Alex Ferguson, Elmer Fudd |
| 59 | Lorraine Bracco, Alan Ball |
| 60 | Jason Statham |
| 61 | James Dean, John Terry |
| 62 | Jack Nicholson, Chuck Norris | 
| 63 | John Major |
| 64 | Johnny Rotten, Geoff Hurst |
| 65 | Jude Law |
| 66 | James Joyce |
| 67 | Jeremy Clarkson, Jack Grealish, Jimmy Greaves, Ashley Cole |
| 68 | **George Foreman** |
| 69 | Jack Black, Jude Bellingham, Jordan Pickford |
| 70 | Kevin Spacey, Graeme Souness, Gareth Southgate, Chris Sutton |
| 71 | Kirk Douglas, Kenny Dalglish, Kevin De Bruyne, Glenn Hoddle, Chris Waddle |
| 72 | Kate Nash, Gary Neville |
| 73 | Kylie Minogue, Kylian Mbappé |
| 74 | **Keith Richards**, Cristiano Ronaldo |
| 75 | Karl Lagerfeld, Gary Lineker |
| 76 | Kim Jong-un, Kasper Schmeichel |
| 77 | Clark Kent, Kevin Keegan |
| 78 | **Kevin Phillips** (Phillips = PH = F, not P) |
| 79 | Kate Bush, Cole Palmer, Gordon Banks |
| 80 | Frank Sinatra |
| 81 | Fred Dibnah |
| 82 | Florence Nightingale |
| 83 | **Freddie Mercury** |
| 84 | Francis Rossi |
| 85 | Frank Lampard |
| 86 | Fred Jones, Vinnie Jones |
| 87 | Freddy Krueger |
| 88 | Freddie Flintoff, Phil Foden, Virgil van Dijk |
| 89 | Frank Bruno |
| 90 | Bart Simpson, Bukayo Saka, Paul Scholes |
| 91 | Bob Dylan |
| 92 | Bill Nighy |
| 93 | Bob Marley, Bobby Moore |
| 94 | Bill Roache, Bobby Robson, Billy Wright |
| 95 | Bruce Lee |
| 96 | Boy George, Bobby Charlton, Peter Shilton |
| 97 | Ben Kingsley, Paul Gascoigne, Peter Crouch, Pep Guardiola |
| 98 | Bruce Forsyth, Patrick Vieira, Bruno Fernandes |
| 99 | **Bob the Builder**, Peter Beardsley |

---

## Audit notes

### Phonetic errors found and fixed

- **Suds (was at 0).** S·D·S = 010, not 0. Removed. Same class of error as the "Hay" catch.
- **Nib (was listed at 19).** N·B = 29, not 19. Removed from 19; it was already correctly at 29.

### Not nouns — removed

- **Nine (22), Five (88)** — numerals.
- **Name, Enemy, Anime (23)** — abstract. This collapsed 23 to a single word (Gnome), so Anemone was added.
- Verbs and abstract nouns cleared: Touch, Stuff, Dab, Muse, Meal, Movie, Mafia, Mob, Army, Race, Rays, Rot, Ruin, Rush, Rave, Rip, Lot, Leak, Lap, Kiss, Game, Comma, Curl, Vote, Fine, Fizz, Fuel, Fall, Fume, Fair, Puff, Pop, Base, Pair, Shot, Sham, Char, Niche, Nap, Nova, Jism, Shit.
- **Navy (28)** kept under protest — collective abstract, but the slot is thin. Knife does the work.

### Rule correction — silent initials

The recorded rule "vowel-initial names are invalid" was wrong. Skipping silent letters to the first consonant sound is deterministic, so those names encode cleanly and roughly double the candidate pool. Elmer Fudd (58) was rejected on this basis and is now rei