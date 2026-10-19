# Battle backgrounds brief (combat maps 2–17)

Read first: `../UI-STYLE-SPEC.md` — the whole file, and especially **"Backgrounds (batch 4)"** and its **seamless-tile technique** note.
The approved baseline is Map 1: `battle/map01_far.svg`, `battle/map01_mid.svg`, `battle/map01_near.svg`. Open all three and study how they are built. Then **go further in detail** than Map 1. The user asked for these to be **as detailed as possible**.

## Technical rules (same as Map 1, non-negotiable)
- Three files per map: `mapNN_far.svg`, `mapNN_mid.svg`, `mapNN_near.svg`. Each has viewBox `0 0 780 560`, width 1560, height 1120, and ids prefixed `mapNN_far-` and so on.
- Each file is two screens wide and **tiles seamlessly**. Build the content in one 780-wide tile group and instance it at x = −780, 0 and +780. Full-width shapes span exactly 0..780. Semi-transparent full-width bands use horizontally uniform gradient rects.
- `far` is opaque. `mid` and `near` are transparent above their silhouettes.
- **Ground line at y ≈ 403** in `near`, fairly level. **Fighting lanes stay clear** (x 60–160 and 230–330, plus the same +390): only ground texture there, plus low details under 12 units tall. Tall props go only at x 0–50, 170–220 and 340–440 (and +390), never in the lanes.
- The bottom 120 units get darker, because the UI sits there.
- No characters and no monsters. No text or readable characters (abstract marks only). No dark outlines, except soft thin linework on near props.
- **Saturation and contrast stay below the painted characters'** (white-and-blue hero, colourful monsters). Detail must not compete with the fighters, so keep values grouped: busy detail in the far and mid layers sits in a narrow value range.

## "As detailed as possible": what that means here
Aim for the richness of a premium mobile RPG backdrop while keeping the ink-wash language:
- **Depth:** 3–5 sub-depths inside each layer (for example the `far` layer has sky, cloud bank, two or three mountain ranges, mist between them). Atmospheric perspective at every step.
- **Texture:** rock strata and cracks, bark lines, leaf clusters, roof tiles, plank grain, water ripples and reflections, cloth folds on banners. Use `<use>` instancing with varied transforms (scale, rotation, flip) so repeats don't look stamped.
- **Light:** a clear key light per map, rim light on silhouettes, god rays or glow where it fits, local light sources (lanterns, lava, crystals) with soft radial glows.
- **Life:** small story props (broken carts, shrines, bones, banners, tools) and environmental particles drawn statically (falling leaves, embers, snow, spores, fireflies) at varied sizes and opacity.
- **Identity:** each map's landmark is big, readable in silhouette, and shown once per 780 tile in the `mid` layer, away from the lane centres.
- **Size:** detail is welcome. The game converts these to PNG, so up to ~250 KB per layer is fine. Avoid pathological blur (a few large `feGaussianBlur` filters only).

## Workflow (keep it efficient: Map 1 lost two hours to repeated heavy renders)
For each map: write the three layers (hand-written SVG; a small helper script in your temp folder is fine for instancing or scattering, delete it afterwards). Render once **stacked at 390×560** (one screen) and once as **two tiles side by side** (seam check). Fix, re-render once, move on. Check file sizes. Use a temp folder for previews and delete it at the end.

## The maps
| # | Map | Element | Mood · time · palette | Landmark (mid layer) | Near-layer ground & props |
|---|---|---|---|---|---|
| 02 | Bandit Pass | Metal | Dusty late afternoon, steel-grey cliffs, warm ochre light | A wooden **bandit watchtower** and a spiked palisade gate wedged between cliffs, tattered red banners | Rocky dirt road with wheel ruts, scattered arrows, a broken cart wheel, dry grass, stones |
| 03 | Moonlit Lake | Water | Night, silver-blue, huge full moon, cool mist | A **lakeside pavilion** on stilts with lanterns, willows, the moon's long reflection on the water | Wooden boardwalk / lakeshore planks, lotus pads and buds at the edge, reeds, small paper lanterns |
| 04 | Ember Hills | Fire | Blazing sunset, orange-red sky, smoke | Red **volcanic hills with steaming vents** and a carved **fire-ape totem rock** | Cracked red earth with glowing ember seams, charred stumps, smoking rocks, drifting embers |
| 05 | Old Sect Ruins | Earth | Golden autumn, nostalgic, dust motes | A broken stone **sect gateway (paifang)** and grand stairs to a ruined hall, toppled guardian statues | Cracked flagstones with moss, fallen roof tiles, a broken incense burner, autumn leaves |
| 06 | Thunder Peak | Metal | Storm, violet-grey clouds, rain streaks, lightning | A **lightning-struck mountain peak** with an iron-chain walkway and a small storm shrine | Wet granite ledge, puddles reflecting lightning, iron chains bolted to rock, wind-bent grass |
| 07 | Poison Marsh | Wood | Eerie dusk, luminous green-purple, fog | Twisted **mangrove giants** and a huge moss-covered **toad statue**, glowing toxic pools | Boggy ground with roots, luminous fungi, bubbling puddles, fireflies, hanging moss at the edges |
| 08 | Frozen Abyss | Water | Polar twilight, aurora, ice blue and white | A **glacier chasm** with towering ice pillars and a frozen **qilin ice statue** | Snowy ice shelf with cracks, icicles, frozen grass, drifting snow |
| 09 | Crimson Desert | Fire | Scorching noon, red dunes, heat haze | Colossal **wyrm skeleton ribs** half-buried in dunes, a sand-swallowed temple top | Rippled red sand, bleached bones, cracked pottery, dry thornbushes, wind-blown sand |
| 10 | Ghost Mist Forest | Earth | Night, cold teal-grey mist, ghost fires | Dead black trees hung with **paper talismans and lanterns**, a decrepit **ancestral tomb** | Dark soil with coffins half-sunk at the edges, gnarled roots, blue ghost-fire wisps, spirit paper scraps |
| 11 | Azure Sea Isles | Water | Bright tropical day, turquoise sea | Rock **sea arches** with palm-topped isles and distant **kraken tentacle silhouettes** | White sand beach with shells, coral chunks, tide pools, driftwood, small waves at the edge |
| 12 | Sky Bridge Peaks | Metal | Clear high altitude, cloud sea below, crisp light | Floating stone peaks linked by a long **stone-and-rope sky bridge**, a giant **roc** silhouette far away | Stone cliff-top with carved railings at the ends, wind-swept pines, prayer flags, cloud wisps below the edge |
| 13 | Scorched Volcano | Fire | Hellish night, lava light, ash fall | An **erupting volcano** with lava rivers and obsidian cliffs, a salamander-shaped lava flow | Obsidian ground with glowing lava cracks, pumice, sulphur crystals, falling ash and embers |
| 14 | Spirit Beast Plains | Wood | Sunrise, golden-green, vast and open | Giant **ancient spirit trees** on rolling grassland, distant herds of spirit beasts as tiny silhouettes | Lush grass with wildflowers, a beast trail, a few large paw prints, boulders with moss |
| 15 | Shattered Realm | Earth | Otherworldly, violet void sky with stars | **Floating rock shards** and broken mountains torn by **glowing space cracks** | Fractured stone floor with violet crack glow, floating pebbles, crystal growths |
| 16 | Star Sea Ruins | Water | Deep night, starry sky reflected in shallow water | **Submerged star-temple ruins** with columns and a huge **leviathan skeleton** arch | Shallow starlit water over stone tiles, glowing coral, starfish, ripples |
| 17 | Demon Border | Fire | Blood-red sky, war-torn, dramatic | A great **border wall fortress** with burning watchtowers and demon banners beyond | Scorched battlefield earth, broken spears and shields, a toppled siege ballista at the ends, embers |

## Dungeons & Trial Tower (same technical rules as the maps above)
Dungeon runs are 10 waves + a boss inside one enclosed place, so these scenes are mostly **interiors** (caves, tombs, gardens, mazes). Interiors still need depth: the `far` layer is the deep back wall/vault/distance, the `mid` layer the structural landmark, the `near` layer the floor. Keep the same ground line (y≈403), clear lanes, darker bottom, seamless tiling and hero contrast (the white-and-blue hero must read against the area behind the lanes, y 200–400).
Files: `dunNN_far.svg`, `dunNN_mid.svg`, `dunNN_near.svg` (ids `dunNN_far-` …) and `tower_far.svg`, `tower_mid.svg`, `tower_near.svg` (ids `tower_far-` …).

| # | Dungeon | Element | Mood · light · palette | Landmark (mid) | Near-layer floor & props |
|---|---|---|---|---|---|
| dun01 | Spirit Vein Cave | Earth/Metal | An abandoned spirit-stone mine overrun by ore spirits: dark rock, glowing blue spirit-crystal veins as the main light, warm lantern accents | Timber mine supports and an old ore-cart rail bridge across a glowing crystal cavern, a huge crystal cluster | Rocky mine floor with rail tracks, a tipped ore cart at the end zones, pickaxes, scattered glowing crystal shards |
| dun02 | Ancient Tomb of Sword Saints | Metal | A vast underground tomb of sword cultivators: cold grey stone, shafts of pale light, faint sword-intent glow | Rows of **ancient swords planted in stone** and towering sword-saint statues holding blades, a sealed tomb gate with bronze rings | Worn tomb flagstones with sword-scratch marks, broken puppet parts, fallen blades, incense urns at the ends |
| dun03 | Beast Valley | Wood/Earth | A hidden, lush valley where spirit beasts nest: dappled green-gold light, waterfalls, mist | Cliff walls with huge **beast dens and nests** in the rock, a great waterfall, claw-marked boulders, a giant beast skull shrine | Grassy trail with paw prints, gnawed bones, feathers, ferns and berries, mossy logs at the ends |
| dun04 | Herb King's Garden | Wood | The overgrown garden of an ancient alchemist: lush, slightly sinister, spore-filled golden light | An overgrown **alchemist's pavilion and greenhouse** swallowed by giant flowers and vines, a cracked pill furnace on a terrace | Garden path of broken tiles with roots, giant flower buds, glowing herbs, a toppled planter at the ends, drifting spores |
| dun05 | Void Labyrinth | Earth/Water | A shifting maze between spaces: violet-blue void, impossible geometry, floating light | **Maze walls and staircases at impossible angles** floating in the void, portals, gravity-defying archways | Floating stone floor tiles with glowing seams over a void gap, floating debris, small runic floor marks (abstract) |
| tower | Trial Tower (endless) | — | Inside a tall sacred pagoda floor high in the sky: warm red lacquer and gold, lantern light, open windows showing clouds far below | A circular **arena hall**: lacquered pillars, a ring of banners, a central spiral stair leading up, round windows with sky and cloud sea outside | Polished wooden arena floor with a painted ring, weapon racks and drums at the ends, lanterns |
