# Idle Cultivation — UI asset style spec (for SVG drawing)

Game: chibi xianxia / murim idle RPG for phones. The UI should feel like a premium mobile gacha RPG menu (think Disgaea RPG / Genshin-era mobile UI), but in **Chinese martial-sect materials**. Every asset must look like it belongs to ONE set.

## Hard rules (every file)
1. **Self-contained SVG**: `xmlns="http://www.w3.org/2000/svg"`, all gradients/filters in `<defs>`, no external refs, no `<image>`, no CSS, no animation, no `<text>` (the game renders all text and calligraphy on top — **never bake words or hanzi into an asset**).
2. **Unique ids**: prefix every id with the file's base name, e.g. `alchemy-gold`, `alchemy-disc` (the files may end up on one page).
3. **Exact canvas**: use the width/height/viewBox given for each file. Transparent background.
4. **Outline**: rosewood `#2A1008`, round joins and caps. ~2.5 units on outer silhouettes at a 64-unit viewBox (scale proportionally for bigger canvases), 1–1.8 inside.
5. **Light**: from the top-left. One clear white/cream highlight per major form. Soft cast shadow allowed.
6. **Readability at 48 px** (icons): at most 3 levels of detail; no detail thinner than 1 unit or smaller than ~3 units at 64-viewBox; the object must be recognisable as a silhouette.
7. **Polish target**: painted-game-icon feel (bevels, gradients, glints), not flat line art.

## Materials & palette
| Material | Gradient / colours |
|---|---|
| Gold (rims, hero, currency) | `#FFF6C8 → #FFD45A → #D69A2A → #9A5E14` (top → bottom); bright edge `#FFE7A0` |
| Rosewood (dark frames, plates) | `#5A2A16 → #3A190C → #1A0804` |
| Red lacquer (hero action, alerts) | `#FF6A44 → #C21E10 → #5A0A04` (radial, bright at top) |
| Jade (active, nature, Qi) | `#C8FFE6 → #3FC79A → #0E6A50` |
| Royal blue (water, hero costume) | `#B8E4FF → #3B7FE0 → #1A2A6E` |
| Spirit crystal | `#FFFFFF → #8FDCFF → #2E7FD0` |
| Silver | `#FFFFFF → #CFD6E4 → #7E8698` |
| Parchment | `#FFF8E4 → #E9CF98` |
| Wood | `#6A3414 / #C07A3E` |
| Stone | `#E4DEEC → #A69EB8 → #6E6684` |
| Fire | `#FFF2A0 → #FFA020 → #E8301A` (bright at the base) |
| Lotus pink | `#FFFFFF → #FFC4D8 → #E0607E` |
| Purple (rebirth, karma) | `#EAD8FF → #9A6AE8 → #3A1E7A` |

Gold is reserved for rims, the hero action and currency. Don't make everything gold.

## Rail icon recipe (64 × 64 viewBox, written as width=256 height=256)
- **Backing disc**: circle centre (32,33), r = 22, radial gradient from a light tint at the top-left to the given disc colour to a darker shade, outline 2.5 `#2A1008`, plus an inner ring r ≈ 19.8, stroke `#FFE7A0` at 80% opacity, width 1.2.
- **The object is larger than the disc and breaks out of it** (top and sides overflow, roughly 4–60 units). It is the hero of the icon: a full-colour painted object, not a glyph.
- Leave the **top-right corner (x > 46, y < 14)** fairly clear: the game puts a red notification badge there.
- Leave the bottom 6 units clear-ish: a text label sits under the icon.

## Reference: quality bar & current layout
- Quality bar (a good result): `/private/tmp/claude-501/-Users-eric/a79f814e-3f5f-45b3-a165-ae9275a85a62/scratchpad/svgtest/fable_cauldron.svg` (except that it forgot the disc).
- Current (weaker) versions of all hub assets, for subject and layout: `/private/tmp/claude-501/-Users-eric/a79f814e-3f5f-45b3-a165-ae9275a85a62/scratchpad/hub_ui.html`.
- The hub art direction: dawn sky (lavender → pink → peach), ink-wash mountains, a meditating swordsman in white and royal blue with fur trim and a crescent-moon motif.

## Self-check before you finish
Render each file with headless Chrome and look at it at 256 px AND 48 px:
`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files --screenshot=OUT.png --window-size=W,H "file://PAGE.html"`
(make a small HTML page that shows your files on a `#3E3456` background and on a `#F3E2C8` background). Fix anything that is unclear at 48 px, overflows the canvas, or breaks a hard rule. Delete your temporary preview files when done.

## Additions for the full UI kit (batch 2)

### Stretchable frames (9-slice)
Panels, cards, buttons and bars are stretched by the game engine with **9-slice scaling**: the four corners stay fixed, the edges repeat or stretch along one axis, and the centre stretches both ways. So for every file marked *9-slice*:
- All ornament (filigree, gems, cloud scrolls) lives **inside the corner squares** (size given per file) or is centred on an edge **only if the brief says so** (an edge-centre ornament breaks when stretched, so avoid it unless asked).
- Edges between the corners must be **uniform along their length** (straight bands, gradients across the band only, no motifs).
- The centre fill must be plain or a smooth gradient that still looks right when stretched.
- Write the corner size into the file as an XML comment on line 2: `<!-- 9slice: 24 -->`.

### Buttons and states
Every button keeps the same shape across states. Pressed and hover are done in code (move down 4 px, shrink the base). Disabled has its own file. Leave the centre calm for the text label.

### Effect sprites
Generic particles (glow, spark, ring, smoke, slash, swirl) are drawn **in white / light grey only**, so the game can tint them per element. Use opacity gradients for softness. No outlines on effect sprites. Element-specific sprites (ember, leaf, droplet, rock shard, lightning, petal, ink splash) keep their colours, still without outlines.

### Housekeeping
Write your files only into the folder named in your brief. Make temporary preview files inside a temp folder of your own (for example `<your folder>/_tmp_<yourname>/`) and delete it when finished.

## Item icons (batch 3)
Item icons appear inside the rarity frames (`kit2/rarity/rarity_*.svg`, a 72-unit slot with a dark well) in inventory grids at **40–64 px**, and on their own in reward pop-ups.
- **Canvas:** viewBox `0 0 64 64`, width/height 256. Transparent. **No backing disc, no frame, no rarity colour** (rarity is the frame's job, so the same icon works at every rarity).
- **Fill:** the object sits inside x/y 6–58 (about 80% of the canvas), centred, with a small soft contact shadow at most.
- **Weapons and tools:** always on the same diagonal: grip/handle at the bottom-left, tip at the top-right (45°).
- **Tier ladders:** items of the same kind across tiers (e.g. Iron Jian → Spirit Steel Jian → Thunder Crystal Jian, or the three Robe tiers) keep **one silhouette family**; higher tiers gain richer materials, glow and ornament, **never a bigger size**.
- **Readability:** must read at 40 px on the dark slot well (#1A0804-ish) and on parchment. Max 3 levels of detail; one clear highlight; bold silhouette.
- **Outline / light / palette:** same as the rest of the kit (rosewood outline ~2.2–2.5, light from top-left, spec palette, plus the item's own natural colours).
- Check your icons inside a real slot: render them on top of `/private/tmp/claude-501/-Users-eric/a79f814e-3f5f-45b3-a165-ae9275a85a62/scratchpad/ui/kit2/rarity/rarity_spirit.svg` at 72 px and at 40 px.

## Backgrounds (batch 4): battle stages & Cultivation Grounds
**Style reference (the user loved this):** the painted vector world in `/private/tmp/claude-501/-Users-eric/a79f814e-3f5f-45b3-a165-ae9275a85a62/scratchpad/screens/project/HubFinal.dc.html` — the first big `<svg>` (sky gradient, sun glow, three ink-wash mountain layers with mist bands, pagoda, cranes, floating peaks with a waterfall, framing cliffs, cherry branch, stone bagua platform). A full-screen render of the hub is at `/private/tmp/claude-501/-Users-eric/a79f814e-3f5f-45b3-a165-ae9275a85a62/scratchpad/preview_hub.png`. Match its language: soft gradients, atmospheric perspective (far = light, cool, low contrast; near = warmer, darker, more contrast), mist bands between layers, ink-wash silhouettes, a few crisp accents. **Backgrounds have NO dark outlines** except thin, soft linework on near-layer props; saturation stays below the characters' so the painted hero always pops.
Backgrounds are big: keep files lean (reuse shapes with `<use>`, avoid thousands of tiny paths; aim < 120 KB per file). No text, no characters, no monsters.

### Battle stage (per combat map) — 3 parallax layers
- Each layer: viewBox `0 0 780 560`, width/height ×2 (1560×1120). It is TWO screens wide and must **tile seamlessly horizontally** (the right edge continues exactly into the left edge) because the game scrolls it endlessly. Verify by rendering two copies side by side.
- `far` (scrolls 0.2×): opaque. Sky + distant mountains/landmark silhouettes + mist. 
- `mid` (0.5×): transparent above its silhouette. The map's **identity landmark** (one per map) + mid hills/trees + mist band at its base.
- `near` (1×): transparent above the ground. The **ground surface top edge is at y ≈ 403 (72%)** and stays fairly level; ground fills to the bottom. Props (rocks, grass tufts, roots, small shrubs) only LOW (< 40 units above the ground line) except at the far left/right ends; keep the fighting lanes (x 60–160 and x 230–330, and the same +390 for the second screen) clear and readable. The bottom 120 units get darker (UI sits there).
- Make a composite preview of all three layers stacked to judge the whole scene, then delete it.

### Cultivation Ground (hub background, one per ground)
- viewBox `0 0 390 844`, width/height 780×1688. Opaque, full screen portrait.
- **Hero zone:** x 80–310, y 170–560 — calm, lighter value, soft backlight/glow so the meditating hero (in white and royal blue) pops. Provide a natural **seat/stage** for the hero centred at x 195, top surface around y 520–545 (a flat rock, a carved platform, a pavilion floor, a training floor…).
- **UI zones (keep low-contrast, no focal details):** top 0–80 (header plates), side strips x 0–78 and 312–390 for y 80–560 (icon rails), bottom y 560–844 (location ribbon, Break Through plaque, activity buttons) — the bottom can be a darker foreground (water, ground, cliff edge) that the game further darkens.
- One clear **identity** for the place (described per ground) and one area that could carry a gentle ambient animation later (falling water, drifting mist, leaves) — just draw it; the game animates separately.
- **Seamless-tile technique (learned on Map 1):** build all layer content inside one 780-wide tile group and instance it at x = −780 / 0 / +780; every full-width shape must span exactly 0..780 (overshooting makes the neighbour copy paint a stripe); semi-transparent full-width bands must be horizontally uniform (gradient rects, not blurred paths).
