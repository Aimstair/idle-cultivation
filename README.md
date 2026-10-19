# Idle Cultivation — Design Docs

> **Status:** Planning complete for design, story, art style, and tech stack. No code yet. **Next: resolve the small open questions, then pre-production (balancing spreadsheet, art bible, wireframes).**

## Pitch
**Cultivation Idle** is a casual incremental idle game with a xianxia cultivation theme. You start as a mortal just opening their meridians and climb the realms through automatic training, breakthroughs, map exploration, and dungeon challenges. Defeat monsters for loot (equipment, techniques, materials, pills, spirit stones, pets), tend spirit fields, and level life skills: fishing, woodcutting, mining, farming, alchemy, cooking, and forging. Every system keeps producing resources, so cultivation, combat, collection, and management feed a single progression loop. Your character keeps cultivating while you're away.

**Audience:** fans of cultivation novels and anime, idle/incremental players, and players who like collecting, managing resources, and chasing long-term goals.

## Documents
| # | Doc | What's in it |
|---|---|---|
| 1 | [Game Design Overview](01-GDD.md) | Vision, pillars, audience, core loops, session design, tone |
| 2 | [Systems](02-Systems.md) | Every system: purpose, mechanics, unlock point, UI screen |
| 3 | [Economy & Balancing](03-Economy.md) | Currencies, formulas, pacing table, offline math |
| 4 | [Content](content/00-Registry.md) | **Folder `content/`**: registry + 14 files covering every realm, map, monster, dungeon, item, technique, pill, recipe, pet, quest, event, and screen |
| 5 | [Monetization](05-Monetization.md) | Rewarded ads, IAP, guardrails, LiveOps |
| 6 | [Tech](06-Tech.md) | Flutter + Flame + Supabase, architecture, saves, AI workflow |
| 7 | [Roadmap](07-Roadmap.md) | Milestones M0 → M3, checklists, KPIs |
| 9 | [Master Sheets](09-Master-Sheets.md) | Prompt pack for the first approved art: hero, monsters + boss, 12 icons |
| 10 | [Character Prompt Pack](10-Character-Prompt-Pack.md) | Every monster, boss and pet for v1.0 (195 rows) with copy-paste prompts in the official GPT style; checklist in `art/character_manifest.csv` |
| 11 | [Audio Plan](11-Audio.md) | Music (8 loops + 10 stingers), 8 ambience beds, ~75 SFX: direction, prompts, tools and licences, mixing rules, file specs |
| — | `tools/inbox.py` | Drop-folder tool for character art: `next` builds art/_review/next.html, `process` cleans and stages everything saved into art/_inbox/, `approve` / `redo` update the checklist |
| — | [Screens (canvas)](https://claude.ai/artifact/6uwPXJEDkExMrk9tvCgooG) | 10 high-fidelity wireframes of the key screens |
| 8 | [Art Bible](08-Art-Bible.md) | Chibi style rules, color system, layered characters, AI prompt templates, asset list |
| — | [Balancing.xlsx](Balancing.xlsx) | Working balancing model: pacing, multipliers, rebirth, economy, checks |

## Decisions so far
- **Platform:** mobile (iOS + Android), portrait, one-handed play.
- **Monetization:** rewarded ads + light IAP. No pay-to-skip realm gates.
- **First release = v1.0** (no public soft launch): Mortal Plane realms 1–8 (Meridian Opening → Void Breaking), all 7 life skills, pets, Spirit Fields, Karma perk tree, 3 dungeons + Trial Tower, quests and achievements, cloud save, 5 languages. It's built in two internal steps: M1 Alpha, then M2 v1.0. A private closed beta runs before launch.
- **Rebirth:** yes. Reincarnate for a permanent Qi multiplier. Stacking Qi and Body multipliers plus Karma. Unlocks at Golden Core.
- **Realms:** the Mortal Plane (10 realms, Meridian Opening → Great Ascension) at launch. 9 more Planes (Immortal → Primordial) come as expansions, reached through **Ascension**.
- **Body Cultivation:** yes. A second track (body stages and training exercises) for HP, DEF, and regen.
- **Name:** *Idle Cultivation*.
- **Art style:** chibi 2D, AI-generated layered art animated in code.
- **Story:** the strongest cultivator of a past life, reincarnated as a mortal, climbing back to the top (see [01-GDD § Story](01-GDD.md)).
- **Online:** cloud save and **leaderboards at launch**. A **player marketplace** comes in a future update.
- **Tech stack:** **Flutter + Flame + Supabase**. Solo developer, AI-assisted for code and art (see [06-Tech](06-Tech.md)).

## Open questions
**78 former open questions are now decided: [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).**

Still open: story details (S1–S3 in that file: the past-life title, the betrayer, and a rival).

## Working on another machine
1. `git clone https://github.com/Aimstair/idle-cultivation.git` and open the folder in Claude Code. `CLAUDE.md` carries the rules, decisions and current state.
2. Install **Python 3** and Pillow (`pip install pillow`), plus Chrome or Edge (the drop-folder tool uses it to render battle scenes; set `CHROME_PATH` if it isn't found).
3. Run `python tools/inbox.py next` to rebuild the "Next up" page, then carry on generating.
4. The design canvas stays at https://claude.ai/artifact/6uwPXJEDkExMrk9tvCgooG (sign in with the same claude.ai account). Board sources are mirrored in `design/canvas/`.
