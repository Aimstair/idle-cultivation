# 09 — Master Sheets (prompt pack)

**Status (2026-10-19):** Sheet A hero approved (GPT style): stand, meditate, battle, expressions, Golden Core robes for male and female. Still to generate: training pose (M+F) and the plain Mortal starting robe (M+F). Sheet B: B1–B4 approved.

The first art you make. These three sheets become the **style references** for every later asset ([08-Art-Bible §11](08-Art-Bible.md)), so take time here and approve them before anything else.

**Tool:** GPT Image (in ChatGPT for this stage). **Rounds:** generate 4 variations of each prompt, pick the best, then refine it with follow-up edits ("keep everything, but…"). Save every approved image and its prompt in `art/masters/`.

**Style anchor** (official GPT style, 2026-10-19): paste at the end of every prompt below, and attach the official masters (`art/masters/hero_official/`, `art/masters/monsters/`) as references:
> chibi murim xianxia RPG game art, about 3 heads tall, sharp detailed anime eyes, highly detailed layered costume with fine embroidery, rich saturated palette, glossy highlights, **bold dark outer outline**, slightly simplified shading so it reads at small size, light from top-left, full body, no floating effects or debris around the character, mobile game asset, **real transparent background (no checkerboard pattern)**, no text, no watermark
> Female hero only: add "softer, more feminine face and eye shape". Monsters: add "3/4 view facing left".

---

## Sheet A: The Hero (the reincarnated cultivator)
The face of the game. The story beat to capture: **a weak mortal body with the eyes of someone who was once the strongest**. Calm, a little smug, quietly confident.

| # | Prompt (+ anchor) | Approve when |
|---|---|---|
| A1 | `Full body front view of a young male swordsman cultivator, long glossy black hair in a high ponytail with an ornate silver crown, side strands framing the face, sharp bright blue eyes, serious confident expression, white and royal-blue layered hanfu with white fur-trimmed collar and cuffs, blue cloud-scroll embroidery on the hem, greek-key pattern cuff bands, dark fingerless gloves with blue bands, dark sash with an ornate silver medallion buckle and light-blue tassels, white boots with blue bands, a long sword with gold fittings at the hip, standing relaxed, arms slightly away from the body so each arm is clearly separated from the torso, legs slightly apart` | Matches the approved reference (Image #6 direction). Silhouette reads instantly. Arms and legs don't overlap the body (needed for layer splitting). Outline is dark indigo |
| A1-F | Same as A1, but `young female swordsman cultivator` with the same costume family | Same face shape and style family as A1 |
| A2 | Attach A1 as reference: `The exact same character, sitting cross-legged in meditation on a small round lotus cushion, floating slightly, eyes closed, serene, hands resting on knees in a mudra, sleeves draping` | Same face, hair, and robe as A1. The cushion is a separate, clear shape |
| A3 | Attach A1: `The exact same character, dynamic battle stance in 3/4 view facing right, coat tails flowing, holding the long sword forward in the right hand, left hand in a sword-finger gesture, determined expression, robe and sash flowing` | Faces right (the player stands on the left in battle). The sword is fully visible and separate |
| A4 | Attach A1: `Expression sheet of the exact same character's head only, 6 heads in a 3×2 grid on white: neutral, eyes closed meditating, focused determined, hurt wincing, happy grin, shocked` | All 6 match A1. These become the swappable `eyes` and `mouth` layers |
| A5 | Attach A1: `The exact same character wearing Golden Core realm robes: white, royal-blue and gold layered hanfu, gold cloud embroidery, a gold-trimmed fur collar, a more ornate crown, a small glowing golden orb visible at the chest` | Shows how robes upgrade per realm without changing the character |

**Then:** split A1 (stand) and A2 (meditate) into the 14 layers ([08-Art-Bible §7](08-Art-Bible.md)).

## Sheet B: Monsters & a Boss
Three monsters from different elements and archetypes, plus the first boss. They prove the "cute but menacing" range.

| # | Prompt (+ anchor) | Approve when |
|---|---|---|
| B1 | `Chibi Green Bamboo Snake monster, Wood element, bright bamboo-green scales with darker segment rings like bamboo nodes, a small leaf on its head, coiled ready to strike, cute but menacing, round shapes, strong silhouette, 3/4 side view facing left` | Reads as a snake *and* bamboo at 48 px. Faces left (enemies stand on the right) |
| B2 | `Chibi Ember Wolf monster, Fire element, charcoal-grey fur with glowing orange ember cracks, flame-tipped tail and ears, low prowling pose, cute but menacing, strong silhouette, 3/4 side view facing left` | Fire reads through shape (upward flame tips), not color alone |
| B3 | `Chibi Shell Crab monster, Water element, round pale-blue shell with wave-pattern ridges, one oversized claw raised defensively, cute but menacing, chunky tank shape, 3/4 side view facing left` | Reads as a tank (wide, low, heavy) |
| B4 | `Chibi boss monster Bamboo Viper King, a huge coiled serpent made of living jade-green bamboo, a crown of bamboo shoots and a golden leaf crest, glowing amber eyes, mouth slightly open showing two fangs, large and imposing but cute, Wood element accents, full body 3/4 view facing left, dramatic rearing pose` | Clearly a boss version of B1's style family. About twice the visual weight, with one extra level of detail |

**Palette-swap test:** recolor B2 to Water (blue fur, white crest) in an editor. If it still looks good, the monster style supports palette-swapped variants.

## Sheet C: 12 Icons
Covers every icon family, all rarities, and all five elements. Each icon is generated separately, then shown together in a 4×3 grid for review.

| # | Item | Prompt core (+ "game item icon of a single …, centered, 3/4 view, thick outline, fills 80% of a square canvas" + anchor) |
|---|---|---|
| C1 | Iron Jian (Mortal sword) | `plain iron straight sword with a simple brown leather grip, diagonal from bottom-left to top-right` |
| C2 | Thunder Crystal Jian (T3 sword) | `straight sword with a pale crystal blade crackling with small silver lightning, gold guard` |
| C3 | Foundation Pill | `round glossy jade-green pill with a faint swirl pattern and a soft glow` |
| C4 | Qi Gathering Pill | `round glossy pale-cyan pill with a cloud symbol, tiny sparkles` |
| C5 | Copper Ore | `chunk of raw copper ore with orange-brown metallic facets` |
| C6 | Spirit Grass | `small bundle of luminous pale-green grass blades tied with a red string` |
| C7 | Flame Ape Blood | `small corked glass vial of glowing crimson blood with an ember inside` |
| C8 | Spirit Stone (currency) | `hexagonal pale-blue spirit crystal, glowing softly` |
| C9 | Jade (premium currency) | `round green jade bi disc with a hole in the center and a carved cloud pattern` |
| C10 | Talisman (accessory) | `vertical yellow paper talisman with red ink calligraphy strokes and a small tassel` |
| C11 | Spirit Ring (accessory) | `silver ring set with a small jade stone` |
| C12 | Element glyph badges ×5 | `five round badges in a row, each a brush-calligraphy character: 金 silver, 木 green, 水 blue, 火 orange-red, 土 ochre, each on a light disc with a brown outline` |

**Approve when:** all 12 sit together as one family (same outline weight, light direction, and level of detail); each reads at 48 px. Put C2 in a Heaven rarity frame and C1 in a Mortal frame to check the rarity system.

---

## Sheet D: Hub screen concept (key art for the whole UI)
A single painted mock of the home screen. It sets the target for UI materials, lighting, and mood. Use it after Sheets A–C are approved, and attach the hero (A2) as a reference.

**Prompt (+ anchor, but allow the background):**
> Mobile game home screen mockup, portrait 9:19.5, chibi xianxia cultivation idle game. Center: the chibi cultivator from the reference meditating on a pink lotus cushion on a round carved stone platform with a bagua ring, eyes closed, a glowing golden core in the chest, a golden halo ring behind the head, cyan and gold Qi streams rising, floating light motes. Background: a dawn sky from lavender to peach to cream, layered ink-wash mountains in soft violet with drifting mist bands, a distant pagoda on a peak, floating islands with a small waterfall, flying cranes, a cherry blossom branch top-right with drifting petals. Center character: sharp blue eyes open, a flying sword with a gold guard hovering beside them leaving a blue Qi trail. UI in rich murim RPG materials: a carved rosewood top plaque with a bevelled gold rim, gold filigree corners and hanging red tassels, a round gold portrait frame, the red calligraphy 金丹 next to "Golden Core 4", a gold progress bar, currency chips (blue spirit crystal, green jade disc with a + button). Left and right edges: four octagonal bagua badges each, bevelled bronze-gold rims around coloured enamel cores with cream-gold glyphs (map scroll, cauldron, robe, paw print; quest scroll, jade coin, lantern, samsara wheel), small red notification dots. Two carved pillars with gold cloud caps flanking the cultivator (red HP liquid left, glowing cyan Qi liquid right). Below: a paper scroll label with wooden rollers reading "+96 Qi/s ×1.32" and a large red-lacquer temple plaque "Break Through" button with a bevelled gold frame, big gold brush calligraphy 突破, red tassels and a warm glow. Bottom: three carved tablets with gold bevel frames (sword in deep red, lotus in glowing jade = active, wooden wing-chun training dummy in violet) and a small loop icon tile. Soft gradient cel shading, dark indigo outlines on the character, high polish, readable, no extra text.

**Approve when:** the scene reads as calm and powerful; the UI frames the cultivator without covering them; gold is used only for the hero action, rims, and currency; and the screen still reads when blurred (squint test: cultivator, Break Through, active tile).
Vector reference with live effects: the "★ Hub · visual target" board on the screens canvas.

## Review checklist (all sheets)
- [ ] Outline color is dark indigo on characters, and the weight matches across sheets
- [ ] Light from the top-left; shadows violet-shifted
- [ ] Silhouette test passes (fill solid black, still readable)
- [ ] No text, logos, or watermarks
- [ ] Transparent background (or plain white, removed in post)
- [ ] Prompt, reference image, and date saved next to each file

When all three sheets are approved, they're attached as references to every batch prompt from then on.
