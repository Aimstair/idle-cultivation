# Idle Cultivation — working notes for Claude

Mobile idle cultivation (xianxia / murim) RPG. Solo developer using AI for code and art. Stack decided: **Flutter + Flame + Supabase** (RevenueCat, google_mobile_ads, Firebase). Start with `README.md`, which indexes every planning doc.

## Standing rules
- **No game code yet.** The user said: "don't write any code until I say so, we need to plan everything first." Planning docs, spreadsheets, design boards and SVG art are fine. **Ask before writing any code**, including tooling scripts (the existing `tools/` scripts were approved).
- The user wants top-tier game, UI/UX, visual and VFX design work. Check art in context (rendered at real size, on its real background, with the hero) before calling it done.
- Keep docs consistent: names, tiers and unlocks come from `content/00-Registry.md`.

## Art pipeline (decided)
| What | Who / how |
|---|---|
| Characters, monsters, bosses, pets | The user generates them in **ChatGPT (GPT Image)**. **Official style = the GPT set** (chosen over Gemini). Masters: `art/masters/hero_official/`, `art/masters/monsters/` |
| UI kit, item icons, effect sprites (vector) | Drawn as hand-written SVG by **Fable** subagents (`model: "fable"`) from `art/ui/UI-STYLE-SPEC.md`. Opus sets rules and reviews at real size. Run at most ~3–4 agents at once (usage limits) |
| Battle backgrounds, Cultivation Grounds, world/region/stage maps | Hand-written SVG by **Opus** subagents, ink-wash vector style. Briefs: `art/bg/MAPS-BRIEF.md`, `art/bg/GROUNDS-BRIEF.md`, `art/bg/MAPSCREENS-BRIEF.md` |
| Audio | User generates (Suno for music, ElevenLabs for SFX); plan in `11-Audio.md` |

Character prompt rules (already baked into `10-Character-Prompt-Pack.md` and `art/character_manifest.csv`):
- NEW monsters attach **only the Ember Wolf** as a style reference; NEW human enemies attach the hero stand + Ember Wolf; EDIT rows attach **only their base**. Never attach the hero to a monster prompt.
- Element details on the body only; **no floating rocks, shards, sparks or lightning** around the creature (effects are added in code).
- Ask for a **real transparent background**: GPT often bakes in a fake checkerboard or solid white/black. `tools/inbox.py` keys these out.

## Drop-folder workflow (characters)
- `python tools/inbox.py next` builds `art/_review/next.html` (cards with Copy image / Copy prompt).
- The user saves picks into `art/_inbox/` and says **"check inbox"** → run `python tools/inbox.py process`, then look at `art/_review/index.html` (each image staged in its battle scene with the hero) and approve/redo with the user: `approve ID ...` / `redo ID --note "why"`.
- State lives in `art/character_manifest.csv` (status: todo / review / done / redo / code). 195 rows; 4 done at handoff.
- Needs Python 3 + Pillow (`pip install pillow`) and Chrome or Edge (set `CHROME_PATH` if not found).

## Design canvas
All screen boards live on the claude.ai canvas artifact: https://claude.ai/artifact/6uwPXJEDkExMrk9tvCgooG (private to the user's account). The board sources are mirrored in `design/canvas/` (`*.dc.html` + `canvas.json`); images on the boards are artifact assets (`/_blob/...`), so edit and republish through the Artifact tool, reading the artifact first.

Key boards: ★ Hub · visual target (live hub with the official hero), Hero master sheet, UI kit + item icons, Background pilots, Battle backgrounds (17 maps, D1–D5, Trial Tower), Cultivation Grounds (19), World/region/stage maps, Hero art · Gemini vs GPT, Cast · official GPT style.

## State at handoff (2026-10-19)
- **Done:** all planning docs; Balancing.xlsx; wireframes; UI kit (154 SVG) + 230 item icons (M1+M2); 23 battle scenes (69 layers); 19 Cultivation Grounds; world map, 6 region maps, 23 islands, 17 stage maps; official hero set (M/F); 4 monsters; prompt pack; drop-folder tool; audio plan.
- **In progress (user):** generating the 190 remaining characters in ChatGPT (M1 first: 58 images). Two made, waiting for cleanup: Wild Boar, Bandit Thug (had floating debris; user to remove via a ChatGPT edit).
- **Still to make:** hero training pose + plain Mortal robe (M/F); ~19 combat-art signature sprites (Fable) + VFX recipes; audio; SVG→PNG export pipeline (1×/2×/3×; SVGs use blur filters Flutter may not support).
- **Open decisions:** appearance presets (recommend male/female + robe dyes only); zone-clear rule (recommend "20 wins clears a zone", boss unlocks after zone 3); how far to split the hero into layers (recommend whole-sprite tweens + separate sword for combat).
- **Next milestone:** M0 prototype (see `07-Roadmap.md`), only when the user says to start coding. Accounts the user must create: Apple Developer, Google Play, Supabase, Firebase, AdMob, RevenueCat.
