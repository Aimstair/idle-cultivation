# 14 — UI, Onboarding, Notifications & Settings

Portrait, one-handed. The main actions sit in the bottom half of the screen. There's **no navigation bar**: the Cultivate hub has side rails of icon medallions, and every other screen has a round back button (see below).

---

## 0. Wireframes
High-fidelity wireframes of 12 key screens: https://claude.ai/artifact/6uwPXJEDkExMrk9tvCgooG (Cultivate Qi, Cultivate Body, Realm Breakthrough, Offline return, Battle, Routine, Equipment, Rebirth, Heavenly Tribulation, World map, Region map with map sheet, Region map with the Meditate filter and a site sheet, Stage map, the boss-defeat unlock storyboard, Alchemy furnace, Spirit Fields, Forge (Enhance), Quests, Shop, Breakthrough success, Breakthrough failure (Qi Deviation), Character creation, and the opening cutscene storyboard).

**Opening order:** cutscene frames 1–2 (past life, betrayal) → frame 3 (waking as a mortal) → **Character creation** ("Your new body") → frame 4 (title card, "Hold to open your meridians") → tutorial. Skippable; plays once.

**Patterns added in the second batch:**
- **Crafting screens share one layout:** an illustrated station (furnace, anvil, terraced fields) on top, an icon grid of recipes or tools, one selected-item card (ingredients as icons with owned/needed counts, success %, quality odds as a 4-color bar), and one big round action (brew, strike, harvest) with small round helpers (quantity, queue, repeat, plant all).
- **Missing ingredients say where to get them** ("Need 1 more Spirit Crystal: Mining 25 or Old Sect Ruins"), and the action button greys out instead of failing.
- **Quests:** icon tabs (Daily, Weekly, Path, Achievements), a daily Merit track with jade chests, and per-quest round buttons: ✓ claim, or › go there.
- **Shop:** one hero offer (Monthly Jade Card as a ticket banner), then a 2×2 grid. Price is always the button. Restore purchases sits at the bottom.
- **Failure screens teach, they don't punish:** they show had vs needed on a bar, the injury with its exact effect and timer, "your level is safe", and three icon fixes (cure pill, meditate, recovery pill).
- **Success screens reward:** a realm seal, the stat jumps, new paths as icons, the Memory Fragment line for the story, and the consolidation bar. The standalone grounds picker was removed: grounds live on the map.

**Cultivation-world motifs used across the UI** (keep them consistent as more screens are designed):
| Motif | Where | Meaning |
|---|---|---|
| **Seal stamps** (vermilion square with brush hanzi: 金丹, 铁骨, 天劫, 轮回 …) | Screen headers, realm and body stage, modals | "This is an official cultivation milestone" |
| **Ink-wash mountains + xiangyun clouds** | Meditation scene, modals' backdrops | The world outside your seclusion |
| **Meridian chart** (acupuncture-diagram style) | Body tab | Tempered parts glow; meridians show the Tempering flow |
| **Hanging scroll** (wooden rods, paper body) | Realm Breakthrough modal, quest banner | Formal, important decision |
| **Bagua dial** (trigram ticks around a ring) | Breakthrough success chance | Heaven's roll |
| **Incense stick timeline** | Offline return | How the time "burned": Battle / Train / Meditate bands |
| **Jade treasure box** | Offline return | The reward reveal |
| **Wheel of samsara** | Rebirth | Reincarnation |
| **Storm-eye + lightning count** | Tribulation | The six strikes, with a survival estimate from current HP |
| **Rarity knots + element glyph badges** | Every item and site card | Double-encoded meaning ([08-Art-Bible §4](../08-Art-Bible.md)) |

**UX patterns the wireframes add:**
- The **Break Through** button carries its destination ("→ GC 5"). The vessel bar shows the cost marker (80%) so players see affordability before tapping.
- **Grounds show the effective rate** after element match (×1.20 → ×1.32), so a weaker-looking site can win. Locked cards say exactly which boss to defeat, with **Go to map**.
- The **Tribulation** screen gives a **survival estimate** and a one-tap **Postpone & refill** that starts a Train → Meditate Routine.
- The **Rebirth** screen shows the projected time to regain the current realm ("7 days, this life took 14"), which is the main reason to say yes. Confirm is **hold-to-reincarnate** with a visible fill.
- **Accessory cards** show each rolled stat with a bar for where it landed in its rarity range.

## 1. Global Layout
### Top bar (always visible)
| Element | Behavior |
|---|---|
| Avatar + realm/level ("GC 4") | Tap → Character tab |
| Spirit Stones, Jade | Tap Jade → Shop |
| Qi/s mini-readout | Long-press → rate breakdown (base, realm, technique, Talisman ×, pills, rebirth ×, etc.) |
| Mini pool bars (HP red, Qi blue) | Thin current/max bars, visible on every tab, since combat and cultivation share them |
| Activity chip | Current activity and place: **Battle** ⚔ (map) / **Meditate** 🧘 (site) / **Train** 💪 (ground), plus a ⟳ icon when a Routine is running. Tap → activity switcher (below) |
| Buff icons | Active pills, meals, baths, ad boosts with timers |
| Injury badges | **Qi Deviation** (cracked blue orb) and **Internal Injury** (cracked red heart), each with a **stack count** ("×3") and the time until the next stack expires. Tap → list of every stack with its own 5-min timer, the combined effect ("Qi rate ×0.51, ATK −15%"), and **Use Meridian Mending Pill** (clears all stacks) |
| Mail / notifications bell | Rewards, Sect messages |

### No navigation bar: the hub and its side rails
The **Cultivate screen is the hub**. There's no bottom tab bar; everything is reached from **round medallion icons** on the hub's edges (a pattern familiar from top mobile games), and every other screen has a round **back** button (top-left) that returns toward the hub. **Exception:** the **Body** and **Battle** screens have no back button, because their bottom activity tiles (Battle / Meditate / Train) already move between the three activity screens and the hub. On Battle, the map-name pill at the top opens the stage map.

| Rail | Icons (top → bottom) | Notes |
|---|---|---|
| **Left: your journey** | Adventure (map scroll) · Skills & crafting (cauldron) · Character (robe) · Pets (paw) | Badge dot = something to do; a small pill shows counts ("3/3" workers busy) |
| **Right: the world** | Quests (scroll + seal) · Shop (jade disc) · Events (lantern, with countdown "1d 13h") · Rebirth (samsara wheel, gold ring when worthwhile) | Mail and Menu are small square icons in the top-right corner |

**Icon-first rule:** buttons are **icons, not words**, wherever the icon is unambiguous (back, close, add to Routine ⟳, battle ⚔, meditate lotus, train stone, collect ✓, watch ad 📺 with a "+10%" / "×2" tag). Every icon has an accessible label and a long-press tooltip, and the tutorial introduces each rail icon the first time it lights up. **Text stays only for the one hero action per screen** (Break Through, Face the Heavens, Hold to Reincarnate) and for numbers.

**Hub layout:** top bar (avatar, realm + progress bar, Spirit Stones, Jade with +), a status pill (current activity), the two rails, the meditating cultivator **flanked by two vertical gauges** (HP left, opens Body; Qi right, glows gold when ready), a site pill (element glyph, Qi/s, ×), the **Break Through** hero button, and the **activity tiles** row (Battle / Meditate / Train as big icon tiles + the Routine loop icon).

### Activity switcher (the main control)
A row of three large **icon tiles** at the bottom of the hub, Body, and Battle screens (no text labels, just the icon and its multiplier or zone), plus a ⟳ Routine tile; reachable from the status pill everywhere else:
```
[ ⚔ Battle ]  [ 🧘 Meditate ]  [ 💪 Train ]      ⟳ Routine: Grind & Grow ▸
   Bamboo Grove Z2   Moonlit Lake Pavilion ×1.2   Pass Fort Drill Yard ×1.1
```
- One activity at a time ([02-Systems §0b](../02-Systems.md)). Under each button: **where** it happens (combat map / Meditation Site / Training Ground) and what it's doing right now ("Qi 62% → refilling").
- **Location:** tapping the place name under Meditate or Train opens the **Region map with the Meditate or Train filter on** (§2.8). It defaults to your best usable site/ground (unlocked and at or above its minimum realm).
- **Battle** drains HP/Qi and grows nothing; pools only base-regenerate there (10% rate). A small hint under the switch says so the first few times.
- Tapping a button manually **pauses the active Routine** ("Routine paused — Resume?").
- The ⟳ Routine link opens the Routine editor (§2.6). Locked until FE 1 ("Unlocks at Foundation Establishment").

### Pool bar (used for both Qi and HP)
A **two-layer bar** that teaches the Vessel Model at a glance:
```
[██████████████░░░░░░│      ]   1,240 / 1,600 Max  ·  Cap 2,000
 └ current (bright) ─┘└ empty part of max (dim) ┘│ └ room to grow to cap (outline) ┘
```
- **Bright fill:** current pool. **Dim segment:** max not yet refilled. **Outline beyond max:** growth still available up to the level's **cap marker** (a vertical tick).
- **Regen readout** on every pool bar: "+12 Qi/s" while Meditating/Training, "+1.2 Qi/s (base)" in any other activity, so players see why the matching activity refills 10× faster.
- State label under the bar: **Refilling…** (current < max), **Growing…** (full, max < cap), **Ready to break through** (max = cap), **Injured** (icon).
- The bar pulses gold when ready to break through. A small spend marker shows where 80% (or 100% at gates) of the cap falls, so the player can see whether they'd have enough.

---

## 2. Screens

### 2.1 Cultivate tab (Home)
Sub-tabs: **Qi** | **Body**. The **Rebirth** button appears from GC 1. From GA 5, an **Ascension** preview card appears beside it (requirements checklist: GA peak, Ascension Pill, Diamond Vajra Body, Final Tribulation).

**Qi sub-tab**
| Element | Action |
|---|---|
| Character on meditation mat, realm aura | Visual only. The aura changes with each major realm |
| **Qi pool bar** (current / Max Qi / cap, see above), Qi/s, state label | — |
| **Break Through** (big button) | Enabled when Max Qi = cap. Spends 80% of the cap. If current Qi < spend: the button turns red with "Not enough Qi". Tapping shows a **warning confirm** ("This attempt will fail: Qi drained + 1 Qi Deviation stack. Refill first?" → **Meditate to refill** / **Use Qi Recovery Pill** / **Try anyway**). At level 9 it becomes **Realm Breakthrough** → Breakthrough modal |
| Activity hint | If the activity isn't Meditate: "Qi only grows while Meditating" + **Meditate now** button |
| Meditation Site card | Current site, its × Qi, element match (✓ +10% if it matches your method), upkeep/h if any. Tap → map with the Meditate filter (§2.8) |
| **Focus** (hold, while Meditating) | +50% Qi for 30 s, then a cooldown ring |
| Cultivation method card | Tap → technique picker |
| Active buffs strip | Tap → use a pill from the bag |
| Main quest banner ("Path of Cultivation: Defeat Flame Ape") | Tap → jumps to the relevant screen |

**Body sub-tab**
| Element | Action |
|---|---|
| Body silhouette with tempered areas glowing (by stage) | Visual |
| Stage + layer ("Iron Bone 6"), **HP pool bar** (current / Max HP / cap), Tempering/s, state label | — |
| **Temper Through** (layer breakthrough). At layer 9: **Stage Breakthrough** with a material checklist | Spends 80% of the cap in HP (100% at a stage). Disabled until materials are owned. If HP is short, the same red warning + confirm as Qi ("HP to 1 + Internal Injury"), with shortcuts **Train to refill** / **Healing Pill** / **Try anyway** |
| Activity hint | If the activity isn't Train: "Your body only grows while Training" + **Train now** button |
| Training Ground card | Current ground, its × Tempering, focus exercise (+50% mastery XP; highlighted if it matches your exercise), upkeep/h if any. Tap → map with the Train filter (§2.8) |
| **Push** (hold, while Training) | +50% Tempering for 30 s, then a cooldown ring |
| Exercise picker (cards with mastery level and stat) | Switch the active exercise (used whenever the activity is Train). A ★ marks exercises that get a focus bonus at an unlocked ground |
| Bath slot | Use a Medicinal Bath. Shows the remaining time |
| Beast Blood button | Instant Tempering burst (heals first, then grows) |
| Tempering sources card | Total × Tempering with sources (Training Ground, Ring stats if rolled, baths, stage, rebirth Body multiplier, injuries). Tap → Equipment |

### 2.2 Adventure tab
| Sub-screen | Elements |
|---|---|
| **World map** (Adventure opens here) | The current Plane as a tall **cultivation scroll** you climb upward: 8 regions linked by a dashed path from Mortal Valley (bottom) to Heaven's Stair (top). A red pin with your face marks your region. The next region is visible but locked ("reach Nascent Soul"). Later regions are hidden in clouds. A Plane switcher at the top (Mortal / Immortal 🔒). Regions in [00-Registry §3b](00-Registry.md) |
| **Region map** | The region's combat maps, dungeon, and Trial Tower drawn as **floating islands** on the scroll, linked by the path. Each map island shows its element glyph, **3 jade beads** (zones cleared), and a **red seal** once the boss is defeated. Locked islands show the condition ("Defeat Thunder Hawk"). Far islands sit under fog |
| **Island preview** (tap an island) | A small card: name, element, realm range, zone beads, the boss, and what its defeat unlocks (next map + Cultivation Ground). **Enter ›** opens the stage map. Dungeon and ground islands open their own sheets |
| **Stage map** (one per combat map) | Its own illustrated map: a climb up that place (for Thunder Peak, a storm mountain). Path from the **gate** at the bottom through **Zone 1 → 2 → 3** (jade-disc nodes with brush numerals 一 二 三; cleared nodes carry a red 击败 seal; your pin marks the current zone) to the **boss lair at the summit** (large portrait medallion, red ring, "BOSS" tag, "Clear Zone 3 to challenge"). The map's **Cultivation Ground** sits beside the lair, sealed until the boss falls. A cloud-hidden teaser at the top edge shows the next land ("Poison Marsh lies beyond"). Tapping a node opens a compact card: monsters, drops, kills/min, **Battle here**, **+ Routine** |
| **Boss defeat unlock** (animation, ~3 s) | 1 **The seal falls** (0–0.8 s): the boss portrait cracks, a giant red 击败 seal slams down, 8 px shake, gong, heavy haptic. 2 **The path ignites** (0.8–1.8 s): golden Qi runs from the lair along the path into the clouds; the sealed ground breaks open ("Ground unlocked"); the last jade bead fills. 3 **The clouds part** (1.8–3.0 s): pull back to the region map; clouds blow apart; the next island rises with dust and its lock shatters. 4 **New land revealed** (3.0 s+): a scroll with the new map, the ground unlocked and first-clear loot; **Travel there** / **Keep farming**. A region's **last** boss also plays it on the World map (the scroll unrolls upward and the next region's clouds blow away). Skippable after the first time; Reduce Motion uses cross-fades |
| **Battle view** | Player vs monster sprites, HP bars, damage numbers, kills/min, loot feed. Zone selector (1–3) + **Challenge Boss** button (the boss card shows which site/ground its first clear unlocks). **Start Battle** sets the activity to Battle. Status line: **Fighting / Retreated (HP 28% — below your retreat point) / Not battling (Meditating)**. A small "Est. time until retreat: ~14 min" shows for the selected zone, using current HP, damage taken, and healer pet/pill healing |
| **Combat settings** (gear icon in Battle view) | **Retreat point** slider (10–90% HP, default 30%), with the plain-language line: *"Retreat point: the HP % where your cultivator stops fighting to avoid dying."* **Resume point** slider (default **100%**, must be above the retreat point): *"Resume point: with a Routine, your cultivator Trains back up to this HP before fighting again."* **Qi floor** slider (0–100%, default 0%): *"Combat arts stop below this Qi. Set to 100% to never spend Qi in battle."* **Healing Pill auto-use at** slider. Healer pet indicator: "Pet heals ~X HP/min" |
| **Dungeons** | List with entries left (3/3), tier selector, **Enter** / **Sweep**, an ad button for +1 entry |
| **Trial Tower** | Current floor, next-floor preview, **Challenge**, weekly reward track, leaderboard link |

### 2.3 Skills tab
| Sub-screen | Elements |
|---|---|
| **Workers overview** | Worker slots (1–4), each with skill icon, current job, progress, output/h. Tap to reassign |
| **Skill detail (×7)** | Skill level + XP bar, list of nodes/recipes (locked ones show the required level), queue, mastery bonuses |
| **Alchemy furnace** | Recipe list, ingredients owned/needed, success %, craft ×1 / ×max |
| **Forge** | Tabs: Craft / Enhance / Reforge / Salvage |
| **Spirit Fields** | Grid of plots (2–9). Each plot: seed, growth timer, **Harvest**. **Plant all** button |

### 2.4 Character tab
| Sub-screen | Elements |
|---|---|
| **Overview** | Stats panel (current/Max HP, current/Max Qi, ATK, DEF, SPD, Crit, Dodge, element), multipliers panel (Qi ×, Tempering ×, Damage ×, Spirit Stones ×, Life-skill ×, with sources including the current site/ground), combat power, title selector |
| **Loadouts** | 3 slots above the Equipment screen (for example, Meditate / Battle / Tribulation). Each saves sword, armor, accessories, and pill pouch. **One tap** to switch, long-press to rename or overwrite. With the *Prepared Mind* perk, they auto-switch by activity |
| **Equipment** | **Sword** slot (shows its Damage × in large text, type icon, and trait) plus Robe, Bracers, Boots around the character. An **accessory row** below: **Talisman**, **Ring**, **Pendant**. There's no main stat: each accessory card lists its **1–3 rolled stats**, one per line, with the value and a small bar showing where it landed in its rarity's range (for example "× Qi rate 1.42 ▮▮▮▮▯"). Compare popup lists stat-by-stat deltas, including stats gained or lost. **Auto-equip best** asks which to prioritise (Qi / Body / Damage / Stones) because accessories mix stats |
| **Techniques** | Method slot(s), combat art slots (2–3), manual library, Comprehension levels |
| **Pets** | Active pet + 3 passive slots, pet list, feed, evolve |
| **Bag** | Grid with filter (gear / materials / pills / eggs), sort, auto-salvage rules |
| **Cosmetics** | Robes, auras, pet skins |

### 2.5 More tab
Shop · **Sword Pavilion** (from MO 5) · Quests (daily / weekly / main / achievements) · Sect (from SF) · Events · Leaderboards · Mail · Settings · Help/FAQ · Support.

### 2.6 Routine editor (unlocks FE 1)
Opened from the ⟳ link on the activity switcher.
| Element | Action |
|---|---|
| Routine name + preset picker | Presets: **Grind & Grow** (Battle until HP < retreat point → Train until HP full → Meditate 1 h), **Body Focus** (Battle → Train to full → Train 2 h), **Pure Cultivation** (Meditate until Qi full → Train until HP full, no Battle) |
| **Steps 1–3** (4–5 with the Karma perk *Disciplined Routine*) | Each step: activity (Battle / Meditate / Train) + **location** (combat map & zone, Meditation Site, or Training Ground; defaults to the best usable) + an **until** condition: *HP below X%*, *HP full*, *Qi full*, *pool at cap* (ready to break through), or *for X min/h* |
| Loop toggle | Repeat from step 1 (default on) |
| Preview line | Plain text: "Fight in Ember Hills Z2 until HP < 30%, then train at Ember Hot Springs until HP is full, then meditate at Moonlit Lake Pavilion for 1 h. Repeat." Upkeep per loop is shown if any step uses a paid ground |
| Safety notes | Routines never break through, never start tribulations, and never return to Battle right after a breakthrough until HP reaches the resume point |
| **Start** / **Pause** | Also shown on the activity switcher |

### 2.7 Sword Pavilion (shop, unlocks MO 5)
| Element | Action |
|---|---|
| **Always in stock** | Mortal Iron Jian at your current tier (Spirit Stones) |
| **Rotating stock (3)** | Spirit or Earth swords of mixed types (Jian, Saber, Greatsword). Each card: type icon, rarity color, Damage ×, trait, affixes, price |
| Refresh timer | Every 6 h. **Refresh now** with Jade |
| Compare | Same compare popup as Equipment (Damage × delta first) |
| Info line | "Twin Swords, Flying Swords and legendary blades can't be bought: defeat bosses and clear dungeons to find them." |

### 2.8 Cultivation Grounds on the map (no separate screen)
Meditation Sites and Training Grounds are **places on the Region map**, like dungeons. Each one sits next to the combat map whose boss unlocks it ([15-Cultivation-Grounds](15-Cultivation-Grounds.md)).
| Element | Behavior |
|---|---|
| **Ground markers** | A rounded pavilion pin: **jade + lotus** for Meditation Sites, **lavender + stone** for Training Grounds. They show the effective multiplier ("×1.32"), and **★** marks your best usable one. Locked grounds have a dashed outline + lock badge; too-low-realm grounds are greyed with "Requires NS 7" |
| **Filter chips** (top of the map) | **All · Battle · Meditate · Train**. A filter dims everything else and highlights the matching places with their effective rate, so the best spot stands out |
| **Ground sheet** (tap a marker) | Same bottom sheet as a combat map: a vignette, the unlocking boss, minimum realm, upkeep ("Free" or stones/h + "you can afford ~X h"), then **Base ×**, **element match** (sites) or **focus exercise** (grounds), and the **Effective ×**. A line compares it with your next best. Actions: **Meditate here / Train here** and **Add to Routine** |
| Shortcuts | The site/ground name under Meditate or Train, the cards on the Cultivate tab, and a Routine step's location all **open the map with the matching filter on**, centered on your best usable ground |
| Default | When you switch to Meditate or Train without choosing, the game uses your **best usable** site or ground automatically |
| Locked | The sheet says "Defeat *Boss* in *Map* to unlock" with **Go to map** |
| Upkeep | When stones run out, you move to your best free ground (toast + note on the offline return screen) |

---

## 3. Modals
| Modal | Contents | Actions |
|---|---|---|
| **Offline return** | "While you were away for 6h 12m…", time spent per activity and place ("Battle 2h 10m · Train 1h 40m at Ember Hot Springs · Meditate 2h 22m at Moonlit Lake Pavilion"), the Routine used, upkeep paid (and any switch to a free ground when stones ran out), gains list (Max Qi / Max HP grown, pools refilled, loot summary, life-skill output, time spent retreated), "Ready to break through ×1", injuries that healed, note when the cap is hit | **Collect** · **Collect 2× (ad)** |
| **Breakthrough (Qi realm)** | **Step 1 pool check** (✓ full / ✗ "Qi 82% — attempt will fail"), success chance breakdown (base, pills, Insight, body stage, accessory affix, ad), gate pill check, failure consequences for both cases | **Attempt** · **+10% (ad)** · Use pill · **Refill first** (Qi Recovery Pill / Meditate) |
| **Breakthrough result** | Success: realm-change animation, stat gains, unlocks list, "Consolidating…" (pool refill begins). Roll failure: 50% of the cost lost, +Insight, no injury. Pool failure: Qi drained, **Qi Deviation** card with cure options | Continue |
| **Not-enough confirm** (Qi or HP) | Red warning: what will be lost, +1 injury stack (name, effect, 5 min) and the stacks you already have, current vs required pool | **Meditate / Train to refill** · **Use pill** · **Try anyway** |
| **Tribulation** | Pre-fight screen: lightning strike count, recommended HP / lightning resist vs yours, **current HP / Max HP and current Qi** (the fight uses current pools), survival estimate based on current HP. The fight is a short auto-sim with strikes visualized. Loss → Internal Injury | **Face the Heavens** · **Postpone & refill** (offers a one-tap Routine: Train to full → Meditate to full) |
| **Body stage breakthrough** | HP pool check (needs 100%), material checklist, stat preview | **Temper** · Healing Pill · Train to refill |
| **Rebirth** | Multiplier gain preview, keep/lose lists, projected "time to regain current realm", Karma gained (M2), typed or hold-to-confirm | **Reincarnate** · Cancel |
| **Ascension** (M3+) | Shown at Great Ascension peak once all requirements are met. Dao Marks preview (√(Qi × Body multiplier) × 10), the Plane left behind vs kept lists, a first look at the Immortal Plane's first realm (Loose Immortal), a hold-to-confirm with an extra "This cannot be undone" line. See [16-Planes-Ascension](16-Planes-Ascension.md) | **Ascend** · Not yet |
| **Unlock** | New system card with 1-line explanation | Go there · Later |
| **Ground unlocked** (toast + card) | After a boss's first clear: "Bamboo Grove Hermitage unlocked — Meditate ×1.10 (Wood)". Shows how it compares to your current site/ground | **Use now** · Later |
| **Level-up toast** | Non-blocking banner | — |
| **Shop offer** | Max once per day (see guardrails) | Buy · Close |

## 4. Shop Screen
Tabs: **Featured** (Starter Pack, Monthly Jade Card, Immortal Cave) · **Jade** (packs) · **Remove Ads** · **Cosmetics** · **Jade Shop** (convenience items) · **Event Shop** · **Sect Shop** (when in a Sect). Prices are shown in local currency, with **Restore Purchases** at the bottom.

## 5. Onboarding: First 30 Minutes (Milestone: M1)
| Time | Beat | Teaches |
|---|---|---|
| 0:00 | Short story card: "A mortal youth senses Qi…" (skippable). Name your cultivator and choose an appearance **preset** (gender, hair, face, colors) | — |
| 0:20 | The activity switcher shows **Meditate** selected at the **Humble Hut**. The pool starts full. The bar shows "Growing…" and Max Qi creeps toward the cap tick. Tip: "Your dantian expands only when full, and only while you Meditate." (Tutorial levels run at ×3 speed) | Meditate, grow-when-full |
| 0:40 | Meridian Opening 1 → 2. Hand pointer on **Break Through** when max hits the cap. The bar drops to 20%. Tip: "Breaking through spends Qi. Refill, then grow again." | Spend → refill → grow |
| 1:30 | Hold **Focus** prompt (faster refill while Meditating) | Active boost |
| 2:00 | **Mining** unlocks. Assign the worker to Copper Vein. Tip: "Workers keep going whatever you're doing." | Workers run in parallel |
| 3:00 | MO 5: **Battle** unlocks. Pointer on the **Battle** button of the switcher; auto-battle starts in Misty Bamboo Grove. The first sword (Mortal Iron Jian) drops (guaranteed). Tip on the mini bars: "In battle, HP and Qi drain much faster than they slowly regenerate, and nothing grows while fighting." | Battle activity, shared pools |
| 5:00 | Equip prompt, compare popup. Tip: "The Sword Pavilion sells basic swords for Spirit Stones." | Gear, swords |
| 6:00 | Combat settings tip: the **retreat point** ("the HP % where your cultivator stops fighting to avoid dying") and **Qi floor** | Retreat point |
| 6:30 | MO 9 → **Qi Condensation**: the first realm gate. A tutorial gate needs only a full Qi pool, with no pill or roll. Short celebration, and the realm name changes on the avatar | Realm gates |
| 7:00 | QC 1: **Train** unlocks at the **Village Courtyard**. Pick Stone Lifting. The HP bar shows "Refilling…" (HP is low from fights) and the regen readout jumps 10×: "Training refills 10× faster than base regen. Only a full body grows stronger, and only while you Train" | Train activity, refill-first |
| 8:00 | QC 5: **Alchemy** unlocks. Quest: craft Foundation Pill. The worker is shared, so prompt switching Mining → Alchemy | Resource choices |
| 10:00 | Challenge Bamboo Viper King (tuned to win). Drops Viper Fang. The player is given 2 Healing Pills afterward. **Ground unlocked** card: "Bamboo Grove Hermitage — Meditate ×1.10 (Wood)". Pointer on **Use now**, then the map opens with the Meditate filter on, showing the new site's ★ and multiplier | Boss, potions, **Cultivation Grounds** |
| 11:00 | Tip: "Switch to **Meditate** (now at the Hermitage) to fill your Qi for the breakthrough. Switch to **Train** first if your HP is low." | Choosing activities |
| 11:30 | QC 9 → **Qi Sea** (tutorial gate, full Qi only). Tip: "The next gate needs a Foundation Pill and a success roll." | Gate preview |
| 13:00 | QS 9 → **Breakthrough** modal with the Foundation Pill. The pool check is shown ✓ (the tutorial tops it up if needed). The first pill-gate attempt is guaranteed 100% | Pill gate breakthrough |
| 15:00 | Foundation Establishment reached: celebration. The bar shows the big empty new pool: "Consolidating…". **Routines unlock**: guided setup of the first Routine, the **Grind & Grow** preset (*Battle until HP < 30% → Train until HP full → Meditate 1 h*), with the location for each step pre-filled with the best unlocked one. Then Forging, Dungeon 1, and the 2nd worker unlock (one tip at a time, queued) | Routines, consolidation, unlock rhythm |
| 16:00 | Dungeon 1 first clear (guided). The Routine pauses for the run and resumes after | Dungeons |
| 20:00 | "Close the app, your Routine keeps running" message + offline cap explained. Ask for notification permission **here**, not at launch | Offline gains |
| 30:00 | Main quest takes over. Remaining tips are contextual | — |

**Rules:** at most 1 forced tap sequence at a time. Every tip is skippable. No ads or shop offers in the first 10 minutes (per [05-Monetization](../05-Monetization.md)).

**First failure (not scripted):** the first time the player taps **Try anyway** on a red Break Through button, or HP first hits 0 in battle, a one-time tutorial override applies. The injury lasts 60 s, a card explains stacks and the cure, and a free Meridian Mending Pill is given and used.

## 6. Contextual Unlock Tips
One card, shown the first time each system unlocks (per the [00-Registry](00-Registry.md) unlock schedule): Combat, Sword Pavilion, Body (Train), first Cultivation Ground, Alchemy, Routines, Forging, Woodcutting, Dungeon, Daily Quests, Rebirth ("Not yet. Rebirth when progress slows"), Tribulation, Trial Tower, Fishing, Cooking, Achievements, Pets, Spirit Fields, Sect, Reforge tier 2, the 2nd method slot. Later tips:
- "Your body is behind your realm, train before your tribulation."
- "Bag nearly full, set up auto-salvage."
- "You've been retreating a lot. Try an easier zone, a healer pet, or Healing Pills."
- "You haven't Meditated today. Qi only grows while Meditating."
- "A better Meditation Site / Training Ground is unlocked, switch?" (when the current one isn't your best)
- "HP not full, postpone the tribulation and refill."
- First Talisman, Ring, or Pendant drop: "Accessories roll 1–3 random stats. Check each one."

## 7. Notifications (local push unless noted)
| Notification | Trigger | Default |
|---|---|---|
| Offline cap reached | 8 h (or 12 h) after leaving | On |
| Spirit Field ready | All plots harvestable | On |
| Dungeon entries refreshed | Daily reset, if entries were used yesterday | On |
| Breakthrough ready | Max Qi reached the level 9 cap **and** the pool is full, while offline | On |
| Body stage ready | Materials owned + layer 9 at cap + HP full | Off |
| Injuries healed | All injury stacks ended while offline (only if 3+ stacks) | Off |
| Routine stopped | Upkeep couldn't be paid and the Routine moved to a free ground, or a Routine step can't run | On |
| Pill/meal buff expired | Long buff ends | Off |
| Event started | Remote push | On |
| Sect Boss spawned | Remote push | On (Sect members) |

Rules: max **2 notifications per day**, quiet hours 22:00–08:00, every type can be toggled.

## 8. Settings
- Sound: music, SFX, ambient volume.
- Notifications: per type, plus quiet hours.
- Number format: suffix (1.2M, 1.2aa) / scientific (1.2e6) / engineering.
- Language.
- Graphics: low-power mode (reduced animations, 30 fps), damage numbers on/off.
- Battery: dim screen during idle on/off.
- Account: cloud save link / unlink, export save code, restore purchases, delete account.
- Confirmations: rebirth confirm style, salvage rarity confirm, "not enough Qi/HP" breakthrough warning (on by default; it can't be fully disabled for realm/stage gates).
- Combat defaults: retreat point, resume point, Qi floor, and Healing Pill auto-use % (also in the Battle view).
- Cultivation Grounds: always use the best unlocked site/ground (on by default), or remember my choice.
- Support: FAQ, contact, privacy policy, terms, credits.

## 9. Accessibility
| Area | Support |
|---|---|
| Numbers | Formats above, thousands separators by locale |
| Text size | Small / Normal / Large / XL, layouts tested at XL |
| Colorblind | Rarity shown by color **and** border shape/icon; element icons have unique shapes; 3 colorblind palettes |
| One-handed | All primary actions (including the activity switcher) in the bottom 60% of the screen; a toggle alternative for the hold Focus/Push buttons |
| Motion | Reduce-motion toggle (no screen shake, no flashing on tribulation lightning) |
| Screen readers | Labels on all buttons and resource values (iOS VoiceOver, Android TalkBack) |
| Haptics | On/off |

## Decisions
- **Character customization:** presets (gender, hair, face, colors).
- **Tutorial ×3 Qi speed-up:** invisible.
- **Bottom tabs:** keep 5.
- **Tablet landscape:** not at launch.
- **Activity switcher:** a tappable top-bar chip on every tab. The full switcher sits on Cultivate and Adventure.
- **First failure:** taught at the first natural "not enough" moment, not scripted at 4:00.
- **Mini HP/Qi bars:** always on.
- **Retreat / resume defaults:** 30% / 100%.
- **Loadouts:** 3 one-tap slots.
