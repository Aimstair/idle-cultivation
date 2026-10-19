# 08 — Art Bible

The style guide for every visual in *Idle Cultivation*. Art is **AI-generated, chibi 2D, layered, and animated in code** (Flutter + Flame, see [06-Tech](06-Tech.md)). This doc keeps hundreds of AI images, every screen, and every effect looking like **one game**.

Palette page: https://claude.ai/artifact/SshqLjkBDbaetDvBYRwfQQ

---

## 1. Style Pillars
1. **Cute body, epic power.** Chibi characters, with cultivation effects (auras, lightning, sword light) that feel genuinely powerful. The contrast *is* the style.
2. **Readable at thumb size.** Clear silhouettes, thick outlines, few details. Every icon must read at 48 px, and every character must pass the silhouette test (§2).
3. **Soft and warm, never muddy.** Pastel bases, clean 2-tone cel shading, one soft highlight. No gritty textures, no photo-real lighting.
4. **Xianxia, not generic fantasy.** Hanfu robes, jade, talismans, flying swords, misty mountains, lotus, seals, calligraphy, Wu Xing.
5. **Every meaning has two signals.** Rarity, element, realm, and body stage are each shown by **color and shape**, so they work for colorblind players and at a glance (§4).

## 2. Readability Rules (value & hierarchy)
The screen has four depth bands. Each band has a fixed contrast budget, so the eye always lands on the right thing:

| Band | Saturation | Value contrast | Outline |
|---|---|---|---|
| **Backgrounds** (far → near) | Low (−30 to −50%) | Low; far layers lighter and bluer (atmospheric perspective) | None (far), soft (near) |
| **Characters, monsters, pets** | Medium | High: dark outline, clear shadow side | Full |
| **VFX, loot, numbers** | Highest | Brightest values on screen (white-hot cores) | None (glow instead) |
| **UI** | Medium, flat | High for text; panels separated by outline + paper texture | UI outline |

- **Silhouette test:** fill a character or monster solid black. It must still read as *that* creature and its action. No thin limbs, and the weapon is visible.
- **Squint test:** blur the full screen. The player, the current enemy, and the main button must still be the three strongest shapes.
- **Never put bright, saturated detail in backgrounds.** That's reserved for things the player should look at.

## 3. Proportions & Line
**Official character style (decided 2026-10-19): the ChatGPT (GPT Image) set** in `art/masters/hero_official/` and `art/masters/monsters/` is the style reference. Gemini was tested (`art/masters/gemini_candidates/`): bolder and cleaner but plainer, and it dropped the story motifs. Attach the official masters to every character, monster, boss and pet prompt.

| Rule | Spec |
|---|---|
| Height | **~3 heads tall** (head ≈ 33% of height). Still chibi, but with room for a detailed martial costume |
| Eyes | Large and **sharp**: heavy upper lash line, straight serious brows, gradient iris (deep → bright at the bottom), 2 highlights. Heroes look confident, not cute |
| Hands / feet | Defined fingers; fingerless gloves, bracers and boots are the default martial kit |
| Costume detail | **Murim RPG level of detail**: layered hanfu (2–3 visible layers), fur trim on collar/cuffs, cloud-scroll embroidery on hems, greek-key (回纹) cuff bands, sash with a medallion buckle and tassels, a hair crown (guan). Detail lives on the costume; the silhouette stays simple |
| Outline color | **Cool dark indigo `#24263A`** on characters (reads crisper, more "RPG"); UI uses rosewood `#2A1008`. Never pure black |
| Outline weight | **0.6% of character height** on the outer silhouette (≈ 5 px on the 900 px source, ≈ 3 px at 512 px display), **0.35%** for interior lines |
| Shading | Soft **gradient cel**: base + shadow ~15% darker, hue-shifted toward violet/blue, plus a rim light on the side away from the key light and glossy highlights on hair and metal |
| Light source | Top-left, always |
| Robes | Flowing hanfu silhouettes. Sleeves and sashes are the main "motion" shapes |
| Monsters | Same chibi rules: big heads, round shapes. Bosses are 1.5–2.5× the player's size, with one extra level of detail |

## 4. Color & Meaning System

### 4.1 UI palette
| Token | Hex | Use |
|---|---|---|
| Parchment | `#FBF6EC` | Main background |
| Paper | `#FFFFFF` | Cards, panels |
| Ink | `#2E2A3A` | Primary text |
| Ink soft | `#6B6478` | Secondary text |
| Jade | `#3FA58C` | Qi UI fills, positive states |
| Jade deep | `#277864` | Buttons and text version of Jade (white text 5.3:1) |
| Vermilion | `#E0533D` | HP fills, damage, danger |
| Vermilion deep | `#B83E2B` | Buttons and text version (white text 5.6:1) |
| Lavender | `#8C7BD9` | Body / Tempering UI fills |
| Lavender deep | `#6E5DC0` | Buttons and text version (white text 5.3:1) |
| Gold | `#E8B54A` | **Currency and rewards only** (fills and badges with Ink text, 7.4:1) |
| Mist | `#E8E2F4` | Section backgrounds, disabled |
| Outline | `#24263A` (characters) · `#2A1008` (UI rosewood) | Linework |

**Contrast rule:** the base Jade, Vermilion, and Lavender only pass for large bold text with white on top (3.0–3.8:1). Use the **deep** shades for buttons and small text. **Gold is never text on Parchment** (1.75:1).

**One theme, by choice.** The game commits to the parchment-day look. The art is painted for it, so there's no in-game dark mode. A "dim" option lowers background brightness by 15% for night play without changing any meaning colors.

**Bars:** HP = Vermilion. Qi = Jade → cyan `#3FA58C → #5FD3E0`. Tempering = Lavender. Each Vessel bar shows three layers: current (solid), max (pale), and a **cap marker** (outline tick).

### 4.2 Meaning channels: one hue family each, plus a shape
Each meaning owns a channel. Where hues unavoidably overlap (gold appears in several places), the **shape** carries the meaning.

| Meaning | Color signal | Shape signal (always present) |
|---|---|---|
| **Rarity** | Frame color | **Frame ornament**: Mortal plain · Spirit 1 corner knot · Earth 2 corner knots · Heaven 4 knots + top gem · Immortal full cloud-pattern frame + animated shimmer |
| **Element** | Tint + accent | **Glyph badge** 金 木 水 火 土 in a small circle, plus element-shaped VFX (§9) |
| **Realm** | Aura hue | **Aura form** (each realm's shape is unique, see 4.4). Shape matters more than hue |
| **Body stage** | Skin sheen | **Rim-light pattern** (none → crack lines → full rim → diamond facets) |
| **Currency** | Gold | Coin/stone silhouette, always with an icon, never color alone |

### 4.3 Rarity
| Rarity | Hex | Frame ornament | Drop feedback |
|---|---|---|---|
| Mortal | `#9AA0A6` | Plain | Small pop |
| Spirit | `#4CAF7A` | 1 corner knot | Soft glow + chime |
| Earth | `#4A8FE7` | 2 corner knots | Glow + sparkle |
| Heaven | `#A066E0` | 4 knots + top gem | Pulsing glow, light beam on drop |
| Immortal | `#F2B53A` | Full cloud-pattern frame | Animated shimmer, beam, screen shake, slow-mo 150 ms |

### 4.4 Elements (Wu Xing)
| Element | Hex | Glyph | Motif |
|---|---|---|---|
| Metal | `#D8DDE6` | 金 | Sword glints, sharp straight lines, triangles |
| Wood | `#5DBB63` | 木 | Leaves, vines, spirals |
| Water | `#3FA7D6` | 水 | Ripples, droplets, arcs |
| Fire | `#F2643B` | 火 | Flames, embers, upward teardrops |
| Earth | `#C9954C` | 土 | Rocks, dust, hexagons, squares |

### 4.5 Realm auras (shape first)
| Realm | Hue | **Form (the main signal)** |
|---|---|---|
| Meridian Opening | Pale white `#F4F7FF` | Faint shimmer outline only |
| Qi Condensation | Soft cyan `#9FE6F0` | Small orbiting motes |
| Qi Sea | Deep blue `#3E7FD9` | Wave ring at the feet |
| Foundation Establishment | Jade `#3FA58C` | Steady glow + rising motes |
| Golden Core | Gold `#F2C14E` | **Glowing core in the chest** + halo ring |
| Nascent Soul | Violet `#8C6BE0` | A faint mini-spirit silhouette behind the player |
| Soul Formation | Lavender-pink `#E6A3E0` | Petals + double halo |
| Void Breaking | Starry indigo `#2C2A6B` | Cracked-space shards with stars |
| Mahayana | Crimson-gold `#C8463A → #F2C14E` | Lotus platform beneath |
| Great Ascension | Prismatic white-gold | Light pillar from above |

### 4.6 Body-stage sheen
Copper `#C47A4A` · Iron `#8C949C` · Silver `#D9DEE5` · Jade `#6CC4A1` · Golden `#F5C542` · Diamond `#E8F7FF` · Immortal `#FFF3D6`. Applied as a 10–20% tint plus a **rim-light pattern** on the skin layers only: Copper/Iron = flat rim, Silver/Jade = rim + faint crack-lines, Golden = full glowing rim, Diamond = faceted highlights, Immortal = soft radiant bloom.

## 5. Typography (multilingual)
Launch languages: English, Simplified Chinese, Vietnamese, Indonesian, Spanish.

| Role | Latin + Vietnamese | Simplified Chinese |
|---|---|---|
| UI and body | **Nunito** (has Vietnamese) | **Noto Sans SC** |
| Headings, numbers, buttons | **Baloo 2** (chunky, rounded, has Vietnamese) | **ZCOOL KuaiLe** (cute, rounded) |
| Calligraphy (decorative) | — | **Ma Shan Zheng** |

- **Calligraphy is decoration, not text.** Realm banners show a large brush-drawn hanzi seal (金丹, 元婴, …) as artwork in every language, with the **localized realm name** set in the heading font beneath. No translation of artwork is needed.
- **Numbers:** Baloo 2 with tabular figures, short suffixes (1.24M, 3.5B, then aa/ab), and never more than 4 significant digits on screen.
- **Type scale (pt):** 12 caption · 14 body · 16 emphasis · 20 button · 24 heading · 32 big numbers · 48 breakthrough banner. Minimum body size 14 pt.
- All fonts are OFL (free for commercial use). Bundle them in the app; don't load them from the web.

## 6. UI Language
| Element | Rule |
|---|---|
| Material language | **Murim RPG materials, not flat app UI.** Carved **rosewood** (#5A2A16 → #2A1008) panels, **red lacquer** (#E8402A → #6A0E06) for hero actions, **carved jade** tablets for activities, **bronze-gold** (#FFE7A0 / #D6A443 / #8A5A1E) bevelled rims, paper scrolls for labels |
| Frame recipe | Every frame = dark rosewood keyline → gold bevel ring → dark keyline → fill with a top sheen. Gold filigree corner pieces on large panels; hanging red tassels on the top plaque and the hero button |
| Shapes | **Octagonal (bagua) badges** for rail icons; **temple plaques** (clipped corners) for the hero button; **carved tablets** (radius 10) for activity tiles; ribbon banners for status; scroll labels with wooden rollers |
| Buttons | Chunky, with a 7 px dark base below. **Pressed** = moves down 4 px and the base shrinks. **Disabled** = desaturated stone with a dulled rim |
| Primary vs secondary | One hero action per screen = **red-lacquer temple plaque with a gold 突破-style brush character** + English label. Secondary = rosewood. Active choice = glowing jade |
| Activity symbols | Battle = crossed jian over a flame crest · Cultivate = glowing lotus with a golden core · **Train = wooden wing-chun training dummy** (木人桩). Not a stone-lock weight: it reads as a padlock, which means "locked" in UI |
| Icons | **Illustrated objects, not line glyphs.** Each button is a full-colour painted object (cauldron, lantern, map scroll, spirit fox, samsara wheel…) that **breaks out of** a small round coloured backing disc. Thick rosewood outline, top-left light, one white highlight, sparkles on valuable items. Label underneath in **white text with a thick dark outline** (Baloo 2, 13 pt). Status = glossy red number badge (top-right), ribbon tags ("Best Value!", "FREE"), or a timer chip. Idle micro-motion: smoke puffs, lantern sway, wheel spin, gem twinkle |
| Banners | Ribbon banners with folded tails (location), speech-bubble goal cards with a red header ribbon and a **Go!** button, gold plaques with a flaming pearl crest for the hero action. Headline text is gold-gradient or white with a thick dark stroke |
| Ornament | Cloud-scroll corners, wave carving, seal stamps, tassels. Rich, but always framing the character, never covering them |
| Touch | Minimum 48 × 48 pt targets. Primary actions sit in the bottom third, for one-handed play |
| Haptics | Light tap on buttons, medium on breakthrough, heavy + long on realm breakthrough and Immortal drops |

### Motion language
| Moment | Duration | Easing |
|---|---|---|
| Button press | 80 ms down / 120 ms up | ease-out |
| Panel / modal open | 220 ms | ease-out-back (slight overshoot) |
| Number tick-up | 400–900 ms (scaled to size) | ease-out-expo |
| Loot pop | 300 ms arc + 150 ms settle | ease-out-back |
| Breakthrough | 1.2 s total: 0.4 s build, 0.1 s flash, 0.7 s release | custom |
| Realm breakthrough | 3–4 s cinematic, skippable after first viewing | custom |

**Reduce Motion** setting: no screen shake, no slow-mo, cross-fades instead of flashes.

## 7. The Layered Character (code animation)
Characters are generated as full images, then **split into parts** that the game animates in code. There's no skeletal rigging.

### Parts (back → front)
| # | Layer | Pivot |
|---|---|---|
| 1 | `aura_back` | center |
| 2 | `hair_back` | top of head |
| 3 | `robe_back` (cape, sleeves behind) | shoulders |
| 4 | `arm_back` | shoulder |
| 5 | `legs` | hips |
| 6 | `torso` (robe front) | hips |
| 7 | `weapon` (sword) | grip point |
| 8 | `head` (face base) | neck |
| 9 | `eyes` (open, closed, focused, hurt, happy, shocked) | — |
| 10 | `mouth` (matching set) | — |
| 11 | `hair_front` | top of head |
| 12 | `arm_front` | shoulder |
| 13 | `headpiece` | top of head |
| 14 | `aura_front` | center |

**Overlap rule:** each part extends **8–12% past its joint** under the neighbouring part, so rotations never show gaps.

### Poses (separate art sets)
- **Stand / battle stance:** Battle and Train.
- **Meditate:** cross-legged, floating. Its own `legs` + `torso`; the other parts are reused.

### Code animation (12 principles applied)
| Animation | How | Principle |
|---|---|---|
| Idle | Bob 2 px on a 2 s sine. Breathing scale-Y 1.00↔1.02 from the hips. Blink every 3–6 s. Hair and sleeves lag the body by 120 ms | Follow-through, secondary action |
| Meditate | Float ±4 px, aura pulse, eyes closed, motes rise | Slow in / slow out |
| Train | Arm swing loop + a prop per exercise (stone, waterfall splash, iron sand) | Arcs |
| Attack | 80 ms wind-up (lean back −15°), 0.12 s swing (−60° → +40°), 1-frame smear, squash on impact, 0.2 s recovery | Anticipation, squash & stretch, exaggeration |
| Cast | Raise arm, glow builds, element VFX releases | Staging |
| Hit | White flash 60 ms, knockback 6 px, **hit-stop 50 ms** | Timing |
| Dodge | Slide back + 2 fading afterimages | — |
| Breakthrough | Rise, glow builds, burst + screen flash, new aura fades in | Anticipation → payoff |
| Retreat / faint | Tip over + fade | — |

### Customization (decision #70: presets)
2 body bases × 6 hair styles × 4 face presets × hair and robe colors (palette-swapped in code). Robes change per realm (8 robe sets at launch).

## 8. Environments
- **Battle stage:** side view, player on the left third, enemy on the right third, ground line at 72% of the stage height. Stage safe area 1290 × 1300 pt-equivalent; UI never covers the fighters.
- **Parallax:** 3 layers (far 0.2×, mid 0.5×, near 1×). Far = sky and mountains (light, cool), mid = landmarks (the map's identity), near = ground and props (warmest, most contrast).
- **Map identity:** one landmark per map that reads in silhouette (bamboo arch, bandit watchtower, moon over the lake, …), plus the map's element accent at low saturation.
- **Cultivation Grounds:** framed vignette paintings (seal-stamp border), calm, with one ambient animation (waterfall, drifting petals, lightning flicker).

## 9. VFX Language
- **Three phases for every effect:** anticipation (gather, 20%) → impact (flash, 10%) → dissipation (particles, smoke, 70%).
- **Color ramp:** white-hot core → element color → darker element edge → transparent. Never a flat single color.
- **Shape language per element:** Metal = straight slashes, triangle shards. Wood = curving leaves and spirals. Water = arcs and droplets. Fire = upward teardrops and embers. Earth = chunky hexagon debris and dust.
- **Scale by importance:** normal hit < crit (1.5× size, +shake) < combat art (unique sprite) < tribulation lightning (full-screen) < breakthrough (full-screen + slow-mo).
- **Screen shake tiers:** none (normal hit) · 2 px (crit) · 4 px (boss skill) · 8 px (tribulation strike, Immortal drop). Always respects Reduce Motion.
- **Budget:** at most 60 live particles on screen on low-end phones; additive blending only for cores and glows.
- **Boss defeat unlock:** seal slam (ink splatter + 8 px shake) → golden Qi trail along the path → cloud burst and rising island → scroll reveal. Gold and vermilion are the only colors added, so it reads as "victory" in every region.
- **Damage numbers:** Baloo 2 with an Outline stroke. White = normal, gold-tinted = crit (larger, with a pop), element-tinted = element advantage, Vermilion = damage taken.

## 10. Asset List (v1.0 launch scope)
| Category | Count (approx.) | Notes |
|---|---|---|
| Player character parts | 2 bases × 2 poses + 6 hair + 4 faces × 6 expressions | Layered |
| Robes (per realm) | 8 sets | Layered torso/sleeves |
| Auras | 8 | Mostly code particles + 1 sprite each |
| Monsters | ~30 base designs | **Palette-swapped** by element and tier to cover ~100 map monsters |
| Bosses | 17 map + 3 dungeon + 4 tribulation visuals | Unique designs |
| Pets | 5 × 3 evolution stages = 15 | |
| Map backgrounds | 17 maps × 3 parallax layers | |
| Cultivation Grounds | 19 + 2 starter vignettes | |
| Gear icons | 7 slots × 6 tiers (T1–T6) = 42 | Rarity shown by frame, not new art |
| Swords | 4 launch types × 6 tiers + ≤ 6 legendaries | |
| Materials | ~60 | |
| Pills & baths | ~40 | One pill base shape, recolored + symbol |
| Realm calligraphy seals | 10 | Brush hanzi artwork |
| World & region maps | 1 scroll frame + 8 region vignettes + ~21 floating islands for launch (17 maps, 3 dungeons, Trial Tower), plus **17 tall stage-map illustrations** (one per combat map: the climb from gate to boss lair; reuses the map's background palette and landmark) | Islands share one rocky-underside base, with a unique top per map. The path, beads, seals, and fog are UI elements |
| UI kit | Frames, rarity ornaments, buttons, bars, tab icons, currency icons, element glyph badges | Vector where possible |
| VFX sprites | ~30 | Per element + tribulation + breakthrough |

## 11. Image Tool & Pipeline

### Recommendation
| Stage | Tool | Why |
|---|---|---|
| **Primary: masters, characters, bosses, everything at first** | **OpenAI GPT Image** (in ChatGPT for exploring, through the **API** for batches) | Very good at following detailed prompts and **reference images** (keeps a character consistent while changing robe, pose, expression). It can output **transparent PNGs**. The API lets AI tools batch-generate whole categories from a prompt list, which suits your AI-driven workflow |
| **Scale-up (optional), when icons and monsters run into the hundreds** | **Scenario** (scenario.com), a game-asset platform | Trains a **custom style model on your approved master sheets**, then generates new assets in exactly that style, with an API and commercial use. Add it only if consistency drifts at volume |
| **Background removal / cleanup** | Built into GPT Image (transparent output), otherwise any remove-background tool | — |
| **UI kit and vector icons** (buttons, banners, frames, rail and activity icons, badges, tags, simple item icons) | **Claude Fable 5.1**, hand-writing SVG; Claude Opus sets the rules and checks every result rendered at real size (48 px, missing parts, consistency) | Tested 2026-10-17: Fable's SVG icon beat Opus's on detail and polish. Vector stays crisp at any screen density and costs no image-generation budget. **Not for characters:** a Fable SVG hero test came out stiff and paper-doll-like, so painted characters stay in GPT Image |
| **Backgrounds and Cultivation Grounds** (battle stages as 3 seamless parallax layers; grounds as full portrait hub backgrounds) | **Claude Opus**, SVG in the vector "ink-wash" style of the approved hub world (Fable stays on icons) | Decided 2026-10-18. Fable drew the two approved pilots (Map 1, Bamboo Grove Hermitage) that set the standard |
| **Splitting characters into layers** | **Krita** (free) or **Photopea** (free, in the browser), with their AI selection tools | Cut parts and paint small fills under the joints |

**Not recommended as the main tool:** Midjourney. It's beautiful for exploring a style, but it has no official public API for batch work, and its transparent-background and precise-edit support are weaker for game assets. It's fine for mood boards.

Before committing, check each tool's **current pricing and commercial-use terms**. These change often.

### Pipeline
1. **Mood board** (Midjourney or GPT Image): 10–15 images to agree on the look.
2. **Master sheets** in GPT Image, approved by you: (a) the hero, front + meditate, (b) 3 monsters + 1 boss, (c) 12 icons across rarities and elements.
3. **Batch production** through the API: one prompt list per category (all ores, all pills, …). Every call attaches the master sheet as a reference + the style anchor.
3b. **UI kit:** Fable draws every UI element as SVG from the shared UI style spec; Opus renders each at 1× and 48 px, checks it against the spec, and puts it on the canvas for approval.
3c. **SVG → game export:** the UI kit lives in `art/ui/` as SVG (source of truth). Fable's files use blur filters for soft shadows and glows (21 files) and one mask (`burst_levelup`), which Flutter's SVG renderer may not support. **Default plan:** rasterise every SVG to PNG at 1×/2×/3× at build time (headless Chrome or resvg) and load PNGs in the game; 9-slice pieces carry their corner size in a `<!-- 9slice: N -->` comment for Flame's nine-tile boxes. Test flutter_svg directly only for assets that must scale at runtime.
4. **Post-process:** check transparency, unify the outline color, check against the palette, trim, center, export.
5. **Characters:** split into layers in Krita/Photopea (~30–60 min per base). Everything after that is code.
6. If drift appears at volume: train a Scenario style model on all approved assets and switch batch production to it.

## 12. Prompt Templates
**Style anchor (append to every prompt):**
> chibi murim xianxia RPG game art, about 3 heads tall, sharp detailed anime eyes, highly detailed layered costume with fine embroidery, rich saturated palette, glossy highlights, **bold dark outer outline**, slightly simplified shading so it reads at small size, light from top-left, full body, no floating effects or debris around the character, mobile game asset, **real transparent background (no checkerboard pattern)**, no text, no watermark

**Negative (where the tool supports it):**
> realistic, photorealistic, 3D render, gritty, dark, complex background, text, letters, watermark, signature, extra limbs, extra fingers, blurry, noisy, cropped, black outlines

| Asset | Template |
|---|---|
| Player character | `full body front view of a young [male/female] cultivator, [hair style] [hair color] hair, wearing [realm] hanfu robes in [colors], [expression], standing, arms slightly away from the body so they can be separated` + anchor |
| Meditate pose | `same character (see reference), sitting cross-legged meditating, floating slightly, eyes closed, hands resting on knees` + anchor |
| Monster | `chibi [creature] monster, [element] element accents, cute but menacing, round shapes, strong silhouette, full body, 3/4 side view facing left` + anchor |
| Boss | `chibi boss monster, [description], large and imposing but cute, [element] accents, strong silhouette, full body 3/4 view facing left, dramatic pose` + anchor |
| Pet | `chibi spirit beast pet, [creature], [element] element, adorable, evolution stage [1 baby / 2 young / 3 majestic]` + anchor |
| Item icon | `game item icon of a single [item], centered, 3/4 view, thick outline, fills 80% of a square canvas` + anchor |
| Pill | `game icon of a round cultivation pill, [color] glossy surface with a [symbol] pattern, small glow, centered` + anchor |
| Sword | `game icon of a [Jian/Saber/Greatsword/Twin swords], [material/tier description], diagonal from bottom-left to top-right, centered` + anchor |
| Map background | `2D side-view mobile game background, [map] with [landmark] as the clear focal silhouette, xianxia scenery, soft painterly pastel, low saturation, [far/mid/near] parallax layer only, wide` (no character anchor; keep the palette words) |
| VFX | `game VFX sprite of [effect], white-hot core fading to [element color], [element shape language], on pure black background, centered` |
| Realm seal | `brush calligraphy of the Chinese characters [hanzi] inside a round seal stamp, ink and gold, centered` |

## 13. Export & Naming
| Type | Source size | Format |
|---|---|---|
| Character parts | 1024 px tall canvas (character ~900 px) | PNG-32, transparent |
| Monsters / bosses | 1024 / 2048 px | PNG-32 |
| Icons | **512 × 512** (shown at 48–96 pt, so 3× screens never upscale) | PNG-32 |
| Backgrounds | **1440 × 1600** per battle-stage layer (far layer 2× wide for parallax) | PNG (near), WebP (far, mid) |
| VFX | 512 × 512 frames | PNG-32 |

Ship in **sprite atlases** per screen or category, downscaled at build time to @1x/@2x/@3x.

**Naming:** `category_subject_variant_state.png`. Examples: `char_base_f_head.png` · `char_eyes_closed.png` · `robe_gc_torso.png` · `mon_viper_wood_t1.png` · `boss_bamboo_viper_king.png` · `icon_pill_foundation.png` · `icon_sword_jian_t3.png` · `bg_map01_far.webp` · `fx_lightning_strike_01.png` · `seal_golden_core.png`

## 14. Licensing & Safety
- Use tools whose terms **allow commercial use**, and save a copy of the terms at the time of generation.
- **Don't name living artists, studios, or existing games or IPs** in prompts.
- Review outputs for look-alikes of famous characters or logos.
- The App Store and Google Play allow AI-generated art. Keep the prompt log (prompt, reference, seed, tool version, date) with each final file.

## 15. QA Checklist (every asset)
- [ ] Passes the silhouette test (characters, monsters) or reads at 48 px (icons)
- [ ] Outline color and weight match the masters
- [ ] Meaning colors used only for their meaning, and the shape signal is present
- [ ] Light from the top-left, violet-shifted shadows
- [ ] Sits in the right depth band (backgrounds quiet, VFX brightest)
- [ ] Transparent, trimmed, centered, correct size and name
- [ ] Prompt logged

## Decisions
- **Chibi 2D, AI-generated, layered, code-animated** (no skeletal rigging).
- **Every meaning is double-encoded** (color + shape) for accessibility and readability.
- **One art-directed parchment theme** in-game, plus a "dim" option.
- **Multilingual font stacks;** calligraphy is artwork, not text.
- **GPT Image** is the primary generator, with API batching. **Scenario** is the optional scale-up for style-locked volume. **Krita/Photopea** split the layers.
