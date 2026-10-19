# 02 — Systems

Each system lists: **Purpose · Mechanics · Unlock · UI · Milestone** (M0 prototype, M1 internal Alpha, M2 v1.0 launch, M3 post-launch; **M1 + M2 both ship in the first public release**; see [07-Roadmap](07-Roadmap.md)).

---

## 0. The Vessel Model (core rule for Qi and Body)
Qi and HP are both **pools**: a current amount and a max. The same five rules apply to both tracks.

| # | Rule | Qi track | Body track |
|---|---|---|---|
| 0 | **Base regen, always on.** Both pools refill slowly at **10% of their normal rate**, during any activity, including Battle. Base regen never grows max. | Qi | HP |
| 1 | **Training refills faster.** While doing the matching activity (§0b), the full rate refills the current pool up to max. | Qi rate (**Meditate**) | Tempering rate (**Train**) |
| 2 | **Growth only when full.** At a full pool, the rate **expands max** instead, at 25% efficiency (4 points → +1 max). | Max Qi grows | Max HP grows |
| 3 | **Each level has a cap.** Max stops growing at the cap, and the player can break through. | 9 levels per realm | 9 layers per stage |
| 4 | **Breaking through spends the pool.** Cost is **80% of the cap** for a level/layer, and **100%** for a new realm/stage. | Spends Qi | Spends HP |
| 5 | **Not enough means failure.** If the current pool is below the cost, the attempt fails: the pool is **drained** and the cultivator is **injured** (§1b). The UI warns first, but lets the player try. | Qi Deviation | Internal Injury |

**Why it matters:** the pools are **shared with combat** (§3). Taking damage costs HP, and combat arts cost Qi. **In battle, the pools only get slow base regen and never grow.** Every hour spent fighting is an hour not growing, so the player chooses when to fight, when to meditate, when to train, and when to use potions.

**After any breakthrough (consolidating):** the pool is low, so Routines (§0b) won't switch to Battle until the pool is back to the Resume % (§3). This prevents an instant retreat or death loop right after a 100% spend.

**Max HP % / Max Qi % bonuses** (Waterfall Endurance mastery, accessory affixes) scale the **whole ladder**: cap, max, and spend together. They give a bigger combat buffer, not cheaper breakthroughs.

**Rhythm of one level:** *refill → grow to cap → break through (spend) → refill again*. Potions skip the refill. Bigger multipliers (accessories, techniques, rebirth) speed up both refilling and growth.

## 0b. Activities & Routines
The cultivator does **one activity at a time**:

| Activity | What it does | Pools |
|---|---|---|
| **Battle** | Auto-combat on the selected map: loot, stones, materials | Damage and combat arts drain HP and Qi. Both get only **base regen** (10%). **No growth.** Potions and healer pets heal faster |
| **Meditate** | Qi cultivation | Qi refills at the full rate, then Max Qi grows. HP gets base regen |
| **Train** | Body exercise (the chosen one gains mastery XP) | HP refills at the full rate, then Max HP grows. Qi gets base regen |

- **Life skills, Spirit Fields, and Alchemy run in parallel** on worker slots, whatever the activity.
- **Offline:** the current activity (or Routine) continues while you're away.
- **Routine (unlocks FE 1):** a simple loop of up to 3 steps that the game follows automatically, online and offline. Example: *Battle until HP < 30% → Train until HP full → Meditate for 1 h → repeat*. More steps and conditions come from Karma perks. This is the main tool for idle play.
- **Default Routine (before FE):** Battle → Train when HP is low → back to Battle at the resume point. The tutorial teaches switching to Meditate by hand.
- **Where you do it matters (Cultivation Grounds):**
  - **Battle** happens on **Combat Maps**.
  - **Meditate** at a **Meditation Site** (× Qi rate).
  - **Train** at a **Training Ground** (× Tempering rate, plus a bonus to one exercise's mastery).
  - Each combat map's **first boss clear unlocks** one site or ground, so pushing combat unlocks better places to cultivate. Each also has a **minimum realm** to use it.
  - Sites can't be upgraded (for now).
  - Starting grounds: Humble Hut and Village Courtyard (×1.0). The best reach about ×3.5–4.5.
  - Grounds are **places on the Region map** (like dungeons), next to the map that unlocks them. Map filters (Battle / Meditate / Train) highlight the best spot. Full list in [content/15-Cultivation-Grounds](content/15-Cultivation-Grounds.md).
- **Meditation focus (active boost):** while Meditating, holding the focus button gives +50% Qi rate for 30 s, with a cooldown. Training has a matching "Push" button.
- **Milestone:** M0 (three activities), M1 (Routines).

## 1. Cultivation (Qi)
- **Purpose:** the central progress bar and the main source of offensive stats.
- **Mechanics:**
  - Qi rate per second: base rate × realm multiplier × level multiplier × bonuses (technique, Talisman, pills, pets, fields, rebirth).
  - Follows the **Vessel Model** (§0): refill, grow Max Qi while full, break through at the cap by spending Qi.
  - Each realm has **9 levels** (Early 1–3, Middle 4–6, Late 7–9). Each level-up raises **ATK** and the Max Qi base. Most HP and DEF come from **Body Cultivation** (§2b).
  - Qi only refills and grows while **Meditating** (§0b).
  - **Max Qi is also the combat Qi pool:** combat arts spend it, so after a fight you must meditate to refill it before Max Qi can grow again (§3).
- **Unlock:** start of game. **UI:** Home screen (character, two-layer Qi bar showing current/max and cap, Break Through button). **Milestone:** M0.

## 1b. Injuries
| Injury | Caused by | Effect | Duration | Cure |
|---|---|---|---|---|
| **Qi Deviation** | A Qi breakthrough attempted without enough Qi | Per stack: −20% Qi rate, −5% ATK | **5 min per stack** | Meridian Mending Pill (clears all stacks), or wait |
| **Internal Injury** | A body breakthrough attempted without enough HP, **or HP reaching 0 in battle** | Per stack: −20% Tempering rate, −5% DEF | **5 min per stack** | Meridian Mending Pill (clears all stacks), or wait |

- **Stacks are unlimited.** Each failure adds one stack with its own 5-minute timer.
- Effects multiply per stack (×0.8 rate each), so they get harsh but never reach zero: 3 stacks ≈ −49% rate, 5 stacks ≈ −67%.
- Injury timers run offline.
- While injured, the pool still refills at the reduced rate, so growth is possible but slower.
- **Milestone:** M0 (Qi Deviation), M1 (Internal Injury).

## 2. Realms & Breakthroughs
- **Purpose:** long-term goals and soft prestige.
- **Ladder (Mortal Plane, launch):** Meridian Opening → Qi Condensation → Qi Sea → Foundation Establishment → Golden Core → Nascent Soul → Soul Formation → Void Breaking → Mahayana → Great Ascension.
- **Beyond:** 9 more Planes (Immortal → Primordial, 55 realms), released as expansions. Finishing a Plane triggers **Ascension**, a second prestige above Rebirth. See [content/16-Planes-Ascension](content/16-Planes-Ascension.md).
- The first three realms are short tutorial realms: their breakthroughs need a full Qi pool but no pill and no success roll.
- **Breakthrough (level 9 → next realm):**
  - Needs **100% of the peak cap in Qi** (a completely full pool) **plus** breakthrough materials (for example, Foundation Pill). The peak level's cap is ×1.6 a normal level's, so the gate takes about 3× as long as a normal level.
  - **Step 1, the pool check:** if Qi is not full, the attempt fails, Qi is drained, and the cultivator gets **Qi Deviation** (§1b).
  - **Step 2, the success roll** (for example, 60%): pills, techniques, body stage, and an optional rewarded ad (+10%) raise it. A failed roll spends 50% of the cost, **never levels**, causes **no injury**, and grants "Insight" stacks (+5% per stack) for the next attempt (pity system).
  - On success, the realm is reached. From Golden Core onward, the realm is **pending** until the Heavenly Tribulation is cleared. Max Qi then jumps to the new realm's base. The pool is mostly empty, so a long **consolidation** refill follows.
  - Normal levels (1→2 … 8→9) have **no success roll**. With enough Qi, they always succeed.
  - From Golden Core onward, each major breakthrough triggers a **Heavenly Tribulation**: a scripted boss fight (lightning waves). It counts as **Battle**: you enter with your current pools, and only base regen and pills apply. Losing just means retrying later. Lightning damage is reduced by your **body stage**, so a weak body is a reason to go train it.
- **Rewards:** a big stat multiplier, a new map region, a system unlock, and a visual transformation.
- **UI:** Breakthrough modal with chance breakdown. **Milestone:** M0 (realms 1–2), M1 (realms 1–3 + tribulation).

## 2b. Body Cultivation (Body Tempering)
- **Purpose:** a second progression track that runs alongside Qi. It's the main source of **Max HP, DEF, and physical damage**. Qi makes you powerful; your body lets you survive.
- **Mechanics:**
  - **Body stages:** Mortal Body → Copper Skin → Iron Bone → Silver Marrow → Jade Flesh → Golden Body → Diamond Vajra Body → Immortal Body. Each stage has **9 layers**, like Qi realms.
  - **Tempering** is the body's training rate. It only runs while the cultivator's activity is **Train** (§0b), using the exercise you've chosen. Training runs offline at 100%.
  - Follows the **Vessel Model** (§0) with **HP as the pool**:
    - Training first **regenerates current HP** at the full rate. Outside training, HP only gets base regen (10%), plus potions and healer pets.
    - Once HP is full, Tempering **raises Max HP**.
    - Reaching a layer's cap lets you break through, which spends 80% of the cap in HP.
  - This is the **same HP used in battle**. After fighting, you must Train to heal before your body can grow.
  - Each **exercise** has its own **mastery level** (1–99) that gives a permanent stat bonus, so the choice of exercise matters:

    | Exercise | Mastery bonus |
    |---|---|
    | Stone Lifting | +DEF |
    | Waterfall Endurance | +Max HP |
    | Iron Sand Palm | +Physical ATK |
    | Shadow Footwork | +SPD, +Dodge |
    | Lightning Tempering (late) | +Tribulation / lightning resist |

  - **Boosts:** **Medicinal Baths** (made by Alchemy from herbs) give ×3 Tempering for 30 min. **Beast Blood** (boss drops) gives an instant Tempering burst. **Healing Pills** restore HP instantly.
  - **Stage breakthrough (layer 9 → next stage):** needs **100% HP** (a full pool) **plus materials**: beast blood, ores, and herbs from combat, mining, and alchemy.
    - **No random roll:** with full HP and the materials, it always succeeds.
    - Without enough HP, it fails, HP drops to 1, and you get **Internal Injury** (§1b).
    - This deliberately contrasts with Qi: Qi has a luck roll, the body is a grind.
  - **Synergy:** each completed body stage gives +2% Qi breakthrough chance ("a sturdier vessel holds more Qi") and reduces tribulation lightning damage.
- **Unlock:** Qi Condensation 1 (about 6 min in). This adds the **Train** activity, so the player now chooses between Meditate, Train, and Battle early on.
- **UI:** a **Body** sub-tab on the Cultivate screen: body silhouette with glowing tempered areas, exercise picker, stage progress.
- **Milestone:** M1 (Copper Skin → Silver Marrow, 3 exercises + Medicinal Bath), M2 (to Golden Body, all exercises), M3 (Diamond, Immortal).

## 2c. Rebirth (Reincarnation)
- **Purpose:** a prestige layer. It gives long-term players a reason to replay faster and stronger, and gives a way past walls when progress slows.
- **Lore:** your cultivator dies and reincarnates. The **soul** carries over (Qi multiplier, memories). The **body and cultivation** start over.
- **Mechanics:**
  - **Unlock:** first reach **Golden Core**. The Rebirth button appears with a preview: "Reincarnate now: +0.42× Qi permanently."
  - **Reward:** a permanent, cumulative **Qi gain multiplier** (from the Qi realm reached). The longer you go before reincarnating, the bigger the gain (formula in [03-Economy](03-Economy.md#rebirth)).
  - **Body multiplier:** a permanent Tempering multiplier, based on the deepest **body stage** reached.
  - **Karma comes from both tracks:** Qi realms and body stages each add stacking Karma.
  - **Both multipliers and Karma stack by realm/stage:** every realm or stage passed through adds its full reward, so going deeper is always worth more (formulas in [03-Economy](03-Economy.md#rebirth)).
  - **Karma (M2):** each rebirth also gives Karma points for a **Past-Life perk tree** (for example, auto level-up, start at Qi Sea 9, Bonded Weapon, +1 worker slot, extra offline hours). Full tree in [content/12-Rebirth](content/12-Rebirth.md).
- **What resets vs what's kept:**

  | Resets (new life) | Kept (soul and possessions) |
  |---|---|
  | Qi, realm and level | Qi and Body multipliers, Karma perks |
  | Body stage, layers, Tempering | Exercise mastery levels (muscle memory) |
  | Spirit Stones (keep 10%) | Life-skill levels, recipes, worker slots |
  | Map/boss progress (bosses must be re-killed; the first-kill reward doesn't repeat) | Inventory and gear (but gear has realm requirements, so you grow back into it) |
  | Active pill buffs | Techniques, pets, Spirit Field plots, achievements, Jade, cosmetics, IAP perks |
  | Dungeon tier progress, this week's Trial Tower floor | Lifetime stats ("deepest realm ever") |
  | "Once per life" tribulation sword rewards (can be earned again) | Legendary sword pity counters (the soul remembers) |

- **When to rebirth:** the intended answer is "when progress slows to a crawl." Rebirthing at the Golden Core peak is roughly break-even against pushing on. Rebirthing deeper gives much more (see the economy doc). That choice is part of the strategy.
- **UI:** a Rebirth screen with a preview of the multiplier gain, a list of what you keep and lose, a projected "time to reach your current realm again," and a big confirmation with an animation.
- **Milestone:** M1 (Qi + Body multipliers), M2 (Karma perk tree).

## 3. Combat & Maps
- **Purpose:** source of loot, spirit stones, and materials, and the check on your power.
- **Mechanics:**
  - Auto-battle runs continuously on the selected map. Stats: HP, ATK, DEF, SPD, Crit %, Crit Dmg, Dodge, and element (Metal/Wood/Water/Fire/Earth, using the Wu Xing cycle: +25% vs the element you counter).
  - Combat happens only during the **Battle** activity (§0b), and is **fully automatic**.
  - **Shared pools (Vessel Model §0):**
    - HP and Qi carry over between fights. Damage lowers your HP, and combat arts spend your Qi.
    - **In battle, only base regen** (10% of the normal Train/Meditate rate) works. For real healing, use Healing Pills (consumable slot, auto-use below a set HP %) and **healer pets**.
  - **Retreat point:** the HP % (default 30%) at which the cultivator automatically stops battling so they don't die.
    - With a Routine, they switch to Train to heal, then return to Battle at the **resume point** (default **100%**, so every Battle step starts at full HP and the Train step can grow Max HP once full). Without a Routine, they just stop and wait.
    - Both points are adjustable.
    - If HP still hits 0 (for example, from one big hit), the cultivator gets an **Internal Injury** stack and retreats.
  - **Qi floor:** combat arts stop when Qi drops below a set % (default 0%). Set it to 100% to never spend Qi in battle, which saves meditation time later.
  - **Healer pets matter:** they're the main way to extend a battle session, so they're a strong pet choice for loot-focused players.
  - Each map has 3 zones with increasing difficulty, and a **boss**. The first kill gives a one-time reward plus a guaranteed technique manual, and unlocks the next map. After that, the boss **respawns every 10 min** while you farm zone 3, so bloods and pet captures can be farmed. Signature drops have **bad-luck protection** (guaranteed by kill ≈ 2 ÷ drop rate). Pet capture is boss-only.
  - **Farming:** after the boss is cleared, the player can idle on any zone. Kills/min and drop table depend on the zone.
  - Combat is simulated in ticks. The UI only plays a light representation (sprites, damage numbers).
- **Unlock:** Meridian Opening 5. **UI:** Adventure screen (map list → battle view). **Milestone:** M0 (1 map), M1 (8 maps).

## 4. Equipment & Forging
- **Slots (7):** **Sword** (weapon), Robe, Bracers, Boots, plus 3 **accessories** (Talisman, Ring, Pendant).

### Swords (weapon slot)
Every weapon is a sword. Its **main stat is a Damage multiplier** (all damage dealt), plus a type trait and normal affixes.

| Sword type | Trait | How you get it |
|---|---|---|
| **Iron Jian** (balanced) | — | **Bought** from the Sword Pavilion shop (Spirit Stones), or **crafted** (Forging) |
| **Saber (Dao)** | +Crit Dmg | **Crafted** (Forging), or dropped by map monsters |
| **Greatsword** | +Damage, −SPD | **Crafted** (Forging, needs boss materials) |
| **Twin Swords** | Extra hit, +SPD | **Dropped** by map bosses |
| **Flying Sword** | Damage scales partly with Max Qi | **Dropped** in dungeons (D2 Sword Saints' Tomb especially) |
| **Named legendary swords** (for example, "Sword Wraith Emperor's Edge") | Unique effect | **Defeating** specific bosses (rare), tribulations, events |

| Rarity | Damage multiplier | Where this rarity comes from |
|---|---|---|
| Mortal | ×1.05–1.15 | Shop, Forging |
| Spirit | ×1.15–1.30 | Shop (rotating stock), Forging, map monsters |
| Earth | ×1.30–1.50 | Forging (high level), map bosses, dungeons |
| Heaven | ×1.50–1.80 | Dungeon bosses, Sect shop, rare map-boss drops |
| Immortal | ×1.80–2.50 | D8 Immortal Cave Ruins, named legendaries, events |

- **Tier bonus:** +0.05 Damage per tier above T1.
- **Enhancement:** each level increases the sword's damage bonus by +2% (up to +30% at +15).
- **Sword Pavilion (shop, unlocks MO 5):** sells Mortal swords at all times, plus 3 rotating Spirit or Earth swords (rotating stock unlocks at Qi Sea 1). The stock refreshes every 6 h, or with Jade. Spirit Stones only.

### Accessories (Talisman, Ring, Pendant)
Talisman and Ring slots are available from the start of equipment. The **Pendant slot unlocks at Qi Sea 1**.
**No main stat.** Each accessory rolls **1–3 random stats** when you get it. Each stat's value is rolled from a range set by the item's **rarity**. The slot decides which stats can roll:

| Slot | Stat pool |
|---|---|
| **Talisman** | × Qi rate, +Max Qi %, +Breakthrough chance, +Crit %, −Combat art Qi cost % |
| **Ring** | × Tempering rate, +Max HP %, +DEF %, +Dodge %, +Healing received % |
| **Pendant** | × Spirit Stones, × Damage, +Drop rarity %, × Life-skill speed, +Crit Dmg % |
| All slots | −Injury duration % |

| Rarity | × stats (Qi, Tempering, Stones, Damage, Life-skill) | % stats (Max HP/Qi, DEF, healing) | Small % stats (Crit, Dodge, Breakthrough, drop rarity) |
|---|---|---|---|
| Mortal | ×1.03–1.10 | +2–5% | +0.5–1% |
| Spirit | ×1.08–1.20 | +4–8% | +1–2% |
| Earth | ×1.15–1.35 | +7–12% | +2–3% |
| Heaven | ×1.30–1.60 | +10–18% | +3–4% |
| Immortal | ×1.50–2.00 | +15–25% | +4–6% |

- **Stat count** is random, lightly weighted by rarity: Mortal 1–2, Spirit 1–2, Earth 1–3, Heaven 2–3, Immortal 3. The same stat can't roll twice on one item.
- **Tier bonus:** ranges shift up by +0.03 per tier for × stats, and +5% of the value per tier for % stats.
- **Enhancement:** each level adds +2% to every stat's bonus (up to +30% at +15).
- **Reforge** (Dao Pattern Stone): reroll one stat (type and value) and keep the others.
- **Examples:** a Heaven Talisman with ×1.42 Qi and +3% Breakthrough. An Earth Ring with only ×1.31 Tempering. A Spirit Pendant with ×1.12 Spirit Stones, ×1.09 Damage, and +1% Crit Dmg.
- × stats count toward `EXT` in [03-Economy](03-Economy.md). Finding a good Qi Talisman or Tempering Ring is the main reason EXT climbs over the realms.
### Loadouts (v1.0)
- **3 loadout slots.** Each saves the sword, armor, 3 accessories, and pill pouch. Switch with **one tap** (for example, a Meditate set, a Battle set, and a Tribulation set).
- Karma perk **Prepared Mind** switches the loadout automatically when the activity changes ([content/12-Rebirth](content/12-Rebirth.md)).

- **Rarity:** Mortal (grey) → Spirit (green) → Earth (blue) → Heaven (purple) → Immortal (gold). Higher rarity gives more affixes (0–4).
- **Item level:** set by the map tier. The main stat scales with item level.
- **Forging (life skill):** craft gear from ore and wood, **enhance** +1…+15 with stones and ore (failure is never destructive), **reforge** one affix with a rare material.
- **Salvage:** unwanted gear becomes ore and stones. An auto-salvage filter is unlocked by an IAP-free achievement.
- **Unlock:** drops from the start, forging at Foundation Establishment. **Milestone:** M1.

## 5. Techniques (Skills)
- **Cultivation methods (passive):** one equipped. Each boosts Qi rate and gives a stat bias (for example, *Azure Cloud Sutra*: +20% Qi, +SPD). They level up with "comprehension" points from duplicate manuals.
- **Combat arts (active):** up to 3 equipped, auto-cast on cooldown (for example, *Flying Sword*, *Flame Palm*).
- **Source:** manual drops from bosses and dungeons, and the sect shop.
- **Element school bonus:** +10% if your method and all equipped arts share one element.
- **Milestone:** M1 (1 method slot, 2 combat slots), M2 (full).

## 6. Dungeons (Secret Realms)
- **Purpose:** concentrated rewards and unique materials. Gives active players something to do.
- **Mechanics:** 3 free entries per day per dungeon. Extra entries: rewarded ads (max 2 per day across all dungeons) and Jade (max 2 per day). Wave-based (10 waves + boss), with difficulty tiers unlocked per realm. Once a tier is cleared, **Sweep** completes it instantly.
- **Sweep** after one clear (★). Void Labyrinth path choices auto-pick by default (setting to choose manually). Dungeon progress resets on Rebirth; the *Dungeon Sweeper* perk keeps sweeping.
- **Rewards:** breakthrough materials, technique manuals, pet eggs (M2).
- **Milestone:** M1 (1 dungeon), M2 (3+).

## 7. Pets (Spirit Beasts)
- **Mechanics:** hatched from eggs (dungeon or boss drops) or captured from map bosses at low odds. One **active** pet assists in combat. Up to 3 **passive** pets give bonuses (for example, +Qi rate, +gather speed). Pets level with food from cooking.
- **Rarity and evolution:** 3 evolution stages that change the sprite.
- The active pet's element uses the **Wu Xing** advantage (+10% if it counters the enemy). No pet equipment. Pet expeditions come post-launch.
- **Milestone:** M2.

## 8. Spirit Fields
- **Mechanics:** plots (start with 2, expandable to 9) grow herbs in real time (30 min–12 h). Higher-tier seeds come from dungeons. Planting is manual; harvesting can be automated later. Field level comes from the Farming skill.
- **Output:** alchemy herbs and cooking ingredients.
- **Unlock:** **Golden Core 1**, so herbs for the Nascent Soul gate aren't drop-only. Plot prices are a fixed table (tuned in the spreadsheet). Alchemy's **Pill Residue** (from failed crafts) works as fertilizer. Event-only herbs come with events.
- **Milestone:** M2.

## 9. Life Skills
All life skills share one framework: **Skill level (1–99) · Recipes/nodes unlocked by level · Job queue · Worker slot.**
- The player has **1 worker slot** at first (+1 at Foundation Establishment, +1 at Nascent Soul, +1 via IAP or achievement). Each slot runs one life-skill job continuously, including offline.

| Skill | Type | Input → Output | Feeds |
|---|---|---|---|
| Mining | Gathering | → ore, spirit crystals | Forging |
| Woodcutting | Gathering | → spirit wood | Forging, Alchemy (furnace fuel) |
| Fishing | Gathering | → fish, rare pearls | Cooking, pet food |
| Farming | Gathering (via Spirit Fields, **no worker slot**) | → herbs, grain | Alchemy, Cooking |
| Alchemy | Processing | herbs + fuel → pills | Cultivation, Breakthrough |
| Cooking | Processing | fish/grain → meals (timed buffs) | Combat, Pets |
| Forging | Processing | ore + wood → gear, enhance | Equipment |

- **MVP (M1):** Mining + Alchemy, chosen because they cover a gear chain and a pill chain. Herbs in M1 drop from combat until Farming arrives.
- **Unlocks:** Mining at MO 1, Alchemy at QC 5 (so the Foundation Pill can be crafted before the first breakthrough), Woodcutting at FE, Fishing, Cooking, and Farming/Spirit Fields at GC. The full schedule is in [content/00-Registry](content/00-Registry.md).
- **Milestone:** M1 (2 skills), M2 (all 7).

## 10. Offline Progress
- On return, the game simulates time away (cap **8 h**, extendable to 12 h via IAP) for Qi, combat loot on the current map, and life-skill jobs.
- **Efficiency:** Qi 100%, combat **80%**, life skills 100%. Combat is computed from expected kills/min, and loot is rolled in batch.
- **Vessel Model offline:** the sim runs the current activity or Routine (§0b).
  - **Meditate / Train:** refill, then grow.
  - **Battle:** fight until the retreat point. With a Routine, it cycles through its steps. Growth only happens during the Meditate and Train steps, once the pool is full.
  - **Breakthroughs never happen automatically offline.** The return screen says "Ready to break through ×1".
- **Return screen:** a summary card ("While you meditated for 6h 12m…") with **Collect** or **Collect 2× (ad)**.
- **Milestone:** M0.

## 11. Supporting Systems
| System | Notes | Milestone |
|---|---|---|
| Tutorial | Guided first 10 min, contextual tips when systems unlock | M1 |
| Daily quests | 5 small tasks → Jade + stones. Weekly chest. **No ad-watching quests.** Resets at a fixed server time per region | M2 |
| Achievements | Permanent tasks that give permanent bonuses, up to **+300% Qi** in total at full completion (a long-term chase) | M2 |
| Inventory | Bag with size cap, sort/filter, auto-salvage rules | M1 |
| Settings | Sound, notifications, number format (1.2K vs 1.2e3), language | M1 |
| Notifications | "Offline cap reached", "Fields ready", "Dungeon entries refreshed" | M1 |
| Sect (guild) | Join a player sect, sect shop, cooperative boss | M3 |
| Events | Limited-time maps or festivals | M3 |
| Leaderboard | Realm / power ranking | M3 |

## Screen Map (navigation)
**No navigation bar.** The Cultivate screen is the hub, with side rails of icon medallions. Left: Adventure, Skills, Character, Pets. Right: Quests, Shop, Events, Rebirth. Mail and Menu sit top-right. Other screens use a back button. Details in [content/14-UI-Tutorial](content/14-UI-Tutorial.md).

## Decisions
- **Combat:** fully automatic.
- **Bag:** limited but generous (grows to 140 slots) with auto-salvage filters.
- **Breakthrough failure:** Qi breakthroughs can fail (pool check, then a success roll with pity). Body breakthroughs have no roll (full HP + materials).
- **Rebirth:** the body stage resets fully (the Body multiplier compensates). Gear is kept (realm requirements still apply).
- **Second Training slot:** a Karma perk (*Second Training Slot*).
- **Retreat / resume defaults:** 30% / 100%. **Offline combat efficiency:** 80%.
- **Loadouts:** 3 one-tap slots at v1.0, with auto-swap by activity as a Karma perk.
- **Spirit Fields + Farming** unlock at Golden Core 1. **Pendant slot + Sword Pavilion rotating stock** unlock at Qi Sea 1.
- Full decision list: [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).
