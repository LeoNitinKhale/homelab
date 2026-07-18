Leo is building a personal Major System memory palace system for memorising historical dates. The system encodes the last two digits of birth and death years as concrete visual nouns using phonetic consonant-to-digit mappings (S/Z=0, T/D=1, N=2, M=3, R=4, L=5, J/SH/CH=6, K/G=7, F/V=8, P/B=9). Birth-year objects are placed above the waist or in front of the body; death-year objects below the waist or behind.
Three interconnected reference files are being built:

major_system_pegs_0-100.md — master peg word dictionary
character_pegs_0-100.md — character and real-person initials reference (two-initials method)
mnemonic_implementations.md — completed historical figure scenes

UK figures and references are actively preferred throughout.

The goal is to:
* move everything into a database 
* have a portal frontend to browse this for search, spaced repetition testing and addition of actual images
* connection to an issue tracker (e.g. YouTrack) with a ticket per famous person, and allow Claude to work on creating birth-death images for them autonomously, eventually using e.g. a Hermes agent if needed

Current state
Historical figures with completed or in-progress scenes: Mozart, Newton, Shakespeare, Elizabeth I, Einstein, Genghis Khan (red/unresolved), Napoleon Bonaparte, Charles Darwin, Abraham Lincoln, Henry VIII, Leonardo da Vinci.
A traffic-light status system is in use: green = fully locked scenes, amber = mechanically sound but visually unsatisfying, red = genuinely unresolved gaps. Genghis Khan is currently red.
Some entries were discussed verbally during a driving session and flagged for later filing — these may still need to be formally added to the relevant files.
Key learnings & principles
Core encoding rules:

Actual phonetic pronunciation governs all encoding — not letter names. Hard C = K sound (7), not "cee" (0). H is always unassigned.
Concrete nouns only — no adjectives, verbs, or abstract nouns.
Strong, vivid imagery is prioritised; scenes should connect meaningfully to the figure's actual life or legacy.

Negotiated rule relaxations (documented):

Trailing sounds may be dropped (Emerald = 34, Gold = 75)
Leading S may be dropped since S=0 leaves a free slot (Snail = 25, Screw = 74)
Longer words including brand names are valid pegs when the first two consonant sounds match

Character pegs method:

Pure two-initials only: every entry must be two separate names (first + last, or a famous pair), each contributing one digit via the actual spoken sound of that name
Single-name word-phonetic entries are explicitly rejected

Error patterns to watch for (Claude has made these mistakes previously):

Using letter names instead of phonetic sounds for initials
Misattributing comments or corrections to the wrong figure
Incorrectly placing entries in the character pegs file
Conflating historical anecdotes across figures (e.g., the nosebleed story belongs to Attila the Hun, not Genghis Khan)

Tools & resources

Three markdown files: major_system_pegs_0-100.md, character_pegs_0-100.md, mnemonic_implementations.md
Major System phonetic encoding standard as the underlying framework
UK cultural references actively drawn upon for character pegs (e.g., Rory the Racing Car, Bob the Builder, Chuckle Brothers, Jools Holland, Keith Richards, Freddie Mercury)


Birth-death system

Birth action is creating/planting/picking/lighting/inflating/catching/lifting
Death action is the opposite of each, dropping/extinguishing/smashing/deflating/crushing,etc.
Birth objects generally above waist/in front, death below/behind

Add any used pegs to pegs.md