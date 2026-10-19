# World, Region & Stage maps brief (Adventure screens)

Read first: `../UI-STYLE-SPEC.md` (whole file, especially "Backgrounds (batch 4)"). Quality and detail bar: the approved battle backgrounds in `battle/` (e.g. `map03_*`, `map12_*`) and Cultivation Grounds in `grounds/`. **Make everything as detailed and beautiful as possible** (the user's request): depth, texture, light, small story props, statically drawn particles, all in the same ink-wash vector language.

## How these screens work (from the UI spec)
- **World map**: the Mortal Plane as a tall cultivation **scroll you climb upward**: 8 regions linked by a path from Mortal Valley (bottom) to Heaven's Stair (top).
- **Region map**: one region's combat maps, dungeon and Trial Tower drawn as **floating islands** on the scroll, linked by the path. Cultivation Grounds appear as UI pins next to their map's island.
- **Stage map**: one per combat map, an illustrated **climb up that place**: gate at the bottom → Zone 1 → Zone 2 → Zone 3 → **boss lair at the summit**, with the map's Cultivation Ground beside the lair and a cloud-hidden teaser of the next land at the top.
- **The game draws on top** (already exist as UI kit SVGs, do NOT paint them): the dotted path beads, zone nodes, boss medallion, red seals, pins, lock badges, fog puffs, labels. Your paintings provide the scenery, and **a soft painted trail** (a worn track or steps, no beads) that passes through the anchor points so the UI path sits naturally on it.
- No text, no characters, no monsters (a boss lair is a place; no creature in it).

## Common format
Tall scroll paintings: viewBox `0 0 390 1688` (two phone screens tall; the screen scrolls vertically), width 780, height 1688×2 = 3376. Opaque. Ids prefixed with the file's base name. Keep the left/right 20 units calm (screen edge), and the top 90 units calmer (header bar). Size: up to ~250 KB per file is fine; avoid pathological blur.
Render checks at 390×1688 (one long screenshot), look, fix, re-render once. Use a temp folder, delete it at the end.

## 1. World map: `world_mortal_plane.svg`
A grand painted scroll of the whole Mortal Plane, bottom to top, with a soft painted trail winding up through the **8 region vignettes** at these centres (the UI puts a medallion/pin on each):
| Region | Centre (x, y) | Vignette |
|---|---|---|
| 1 Mortal Valley | (200, 1540) | village, rice terraces, bamboo, a river |
| 2 Azure Lake Province | (120, 1330) | a moonlit lake with a pavilion, willows |
| 3 Thunder Spine Mountains | (270, 1120) | jagged storm peaks, lightning, a tall pagoda (Trial Tower) |
| 4 Ghost Mist Wilds | (110, 910) | misty dead forest, ghost lanterns, a tomb |
| 5 Sky Bridge Heights | (280, 700) | floating peaks joined by a sky bridge, cloud sea |
| 6 Shattered Void Expanse | (120, 490) | broken floating rock, violet space cracks |
| 7 Sword Tomb Abyss | (270, 300) | swords planted in a chasm. **Veiled in heavy cloud** (post-launch), silhouette only |
| 8 Heaven's Stair | (195, 130) | a golden gate at the top of endless stairs. **Veiled in heavy cloud**, golden glow seeping through |
Atmosphere climbs from earthy and warm at the bottom to celestial at the top (sky colour shifts upward). Scroll-paper feel at the edges (subtle paper texture, rolled-scroll ends at the very top and bottom are optional but lovely).

## 2. Region maps (6): `region1_mortal_valley.svg` … `region6_shattered_void.svg`
Each is the **backdrop** for that region: its sky, distant scenery and mood, with **open space at the island slots** (islands are separate files placed by the game, about 180×160 each). Paint a soft trail/cloud-bridge linking the slots in order.
Island slots (centres), bottom to top: S1 (110, 1480), S2 (280, 1250), S3 (110, 1020), S4 (280, 790), S5 (110, 560), S6 (280, 330). Unused slots should still look natural (clouds, distant scenery).
| File | Region · realm band | Islands it hosts (slot order) | Mood |
|---|---|---|---|
| `region1_mortal_valley.svg` | Mortal Valley · MO–QS | Map 1, Map 2 | Fresh green valley, village roofs far below, spring morning |
| `region2_azure_lake.svg` | Azure Lake Province · FE | Map 3, D1, Map 4, Map 5 | Lakes and rivers below, moonlit-to-dawn blues, lotus |
| `region3_thunder_spine.svg` | Thunder Spine Mountains · GC | Map 6, D2, Map 7, Trial Tower, Map 8 | Storm-violet peaks, lightning, cold heights |
| `region4_ghost_mist.svg` | Ghost Mist Wilds · NS | Map 9, D3, Map 10, Map 11 | Teal ghost mist, dead forest below, pale moon, desert edge |
| `region5_sky_bridge.svg` | Sky Bridge Heights · SF | Map 12, D4, Map 13, Map 14 | Bright cloud sea, floating karst peaks, sunlight (keep the slots mid-value so islands read) |
| `region6_shattered_void.svg` | Shattered Void Expanse · VB | Map 15, D5, Map 16, Map 17 | Violet void, star fields, broken space, demon-red glow at the top edge |

## 3. Floating islands (23): `island_map01.svg` … `island_map17.svg`, `island_dun01.svg` … `island_dun05.svg`, `island_tower.svg`
viewBox `0 0 200 180`, width/height ×2, **transparent**. A floating chunk of land: **one shared rocky underside** (design it on the first island and reuse the exact underside geometry on all, tinted per element: Wood green-moss, Fire red-ochre, Water blue-grey, Metal steel-grey, Earth ochre-brown; dangling roots and small falling rock bits), and a **unique top**: a miniature diorama of that place's landmark (use the battle backgrounds `battle/mapNN_mid.svg` / `dunNN_mid.svg` / `tower_mid.svg` as reference). Top surface roughly y 40–100, underside y 90–175. Soft drop glow underneath, no hard outline except soft linework. Must read at 120 px wide.

## 4. Stage maps (17): `stage_map01.svg` … `stage_map17.svg`
A tall climb through that combat map, using **its battle background's palette, landmark and props** (open `battle/mapNN_far.svg`, `_mid.svg`, `_near.svg` for reference). Painted trail passing through these **fixed anchors** (identical on every stage map so the UI nodes line up):
| Anchor | (x, y) | What the painting shows there |
|---|---|---|
| Gate | (195, 1600) | the entrance to the place: a gate, archway, cave mouth or trailhead |
| Zone 1 | (120, 1310) | a clearing / landing on the trail |
| Zone 2 | (270, 1020) | a second landing, deeper in |
| Zone 3 | (130, 730) | a third landing near the heights |
| Boss lair | (195, 380) | the summit lair: a dramatic arena or den for that map's boss (no creature), framed by the landmark |
| Cultivation Ground | (305, 470) | a small calm spot beside the lair (sealed until the boss falls; the UI adds the pin) |
| Next-land teaser | top band y 0–200 | the next map's world peeking through heavy clouds (e.g. Map 6 shows a hint of poison marsh). Map 17 shows a red-gold glow (Sword Tomb Abyss beyond) |
Keep a calm ~60-unit circle around each anchor (no busy detail right under a node); detail and drama everywhere else. The climb should feel like ascending: base of the place at the bottom, its heart in the middle, its summit or sanctum at the top.
