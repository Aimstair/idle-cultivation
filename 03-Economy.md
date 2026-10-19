# 03 — Economy & Balancing

## Currencies & Resources
| Resource | Type | Source | Sink |
|---|---|---|---|
| **Qi** | Soft, primary | Cultivation per second | Levels, breakthroughs |
| **Spirit Stones** | Soft, main currency | Combat, salvage, dailies, selling | Forging/enhancing, shop, field plots, worker upgrades |
| **Jade** | Premium | IAP, dailies, achievements, events (free players earn about 1 cosmetic's worth per month) | Cosmetics, convenience (extra dungeon entry, field speed-up), shop refresh |
| **Materials** | Crafting | Life skills, combat, dungeons | Forging, alchemy, cooking, breakthroughs |
| **Insight** | Pity counter | Failed breakthroughs | Consumed on next attempt (+5% each) |
| **Comprehension** | Technique XP | Duplicate manuals | Technique levels |
| **Tempering** | Soft, body | Active training exercise | Body layers |
| **Beast Blood** | Material | Map and dungeon bosses | Body stage breakthroughs, Tempering burst |
| **Karma** (M2) | Prestige | Rebirth | Past-Life perk tree |

Rule: **Jade must never buy Qi or realm progress directly.** It only buys convenience, cosmetics, and time on non-core timers.

## Core Formulas

### Qi per level: the Vessel Model (see [02-Systems §0](02-Systems.md))
Each level's time is **refill + growth**:
```
work(R, L)  = BASE[R] × 1.15^(L−1)            L = 1…8   (Qi produced to clear the level)
work(R, 9)  ≈ 3 × work(R, 8)                            (realm gate)

cap(R, L)   = 0.76 × work(R, L)                L = 1…8   (Max Qi ceiling of the level)
cap(R, 9)   = 1.6 × cap(R, 8)                            (peak level)

growth time = (cap(L) − cap(L−1)) / (0.25 × rate)       (expansion at 25% efficiency, only while full)
refill time = spend / rate                              (spend = 0.8 × cap for levels, 1.0 × cap for the gate)
```
Check for a normal level: growth (0.13 cap ÷ 0.25 = 0.52 cap) + refill (0.80 cap) = 1.32 × cap ≈ work. The pacing table below stays valid as **time per level**, now read as the Qi you must *produce*, not a price you pay.
At the gate: growth (0.6 × cap8 ÷ 0.25 = 2.4 × cap8) + refill (1.6 × cap8) = 4.0 × cap8 ≈ 3 × work(8). ✓
After a realm breakthrough, Max Qi starts the new realm at `cap(R+1, 1) / 1.15` with an empty pool. That's the **consolidation** refill.

**Body uses identical formulas** with `BODY_BASE` and the Tempering rate (below).

**Times in the table are Meditation time only.** Battle drains the pools and grows nothing, so any HP/Qi spent in battle adds refill time later. See the activity split under "Resulting milestones."

`BASE` (tuned per realm, not a single multiplier, so each realm can be paced on its own):

| Realm (Mortal Plane) | BASE (Lvl 1 work) | REALM_RATE |
|---|---|---|
| Meridian Opening | 15 | ×0.6 |
| Qi Condensation | 50 | ×1 |
| Qi Sea | 250 | ×2 |
| Foundation Establishment | 12,000 | ×5 |
| Golden Core | 400,000 | ×25 |
| Nascent Soul | 13,000,000 | ×125 |
| Soul Formation | 130,000,000 | ×625 |
| Void Breaking | 1.6 × 10⁹ | ×3,125 |
| Mahayana | 2.7 × 10¹⁰ | ×15,625 |
| Great Ascension | 4.6 × 10¹¹ | ×78,125 |
*NS–GA values were tuned in [Balancing.xlsx](Balancing.xlsx) to hit the registry target days under the **fast start, steady later** pacing (below). The per-level table further down is illustrative and was computed with the older model; **the spreadsheet is the source of truth.***
Later Planes restart their own BASE/REALM_RATE ladders ([content/16-Planes-Ascension](content/16-Planes-Ascension.md)).

### Qi rate
```
rate(R, L) = 1.0 × REALM_RATE[R] × 1.10^(L−1) × EXT
```
- `REALM_RATE[R]`: realm multiplier from the table above. The three short opening realms ramp up to the old ×5-per-realm curve from Foundation Establishment on.
- `1.10^(L−1)`: per-level growth. This is deliberately **below** cost growth (1.15), so each level takes a bit longer than the last, and a breakthrough feels like a big release.
- `EXT`: product of all bonuses (technique, pills, pets, fields, achievements). The pacing table assumes a typical player at **1.0 / 1.5 / 2.5 / 4.0** in realms 1–4.
- `EXT` now includes the **Cultivation Ground** multiplier (best unlocked Meditation Site or Training Ground: about ×1.1 / ×1.3 / ×1.5 / ×1.65 in realms 1–4). Together with accessory stats and techniques, this makes up the 1.0 / 1.5 / 2.5 / 4.0 assumption. Re-check this in the balancing spreadsheet, since all three stack multiplicatively.
- `EXT` also includes **achievement bonuses: up to +300% Qi** (×4) at full completion. It's a long-term chase that ramps slowly, so the early-realm assumption barely changes, but the spreadsheet must model achievement progress over time.
- The **Rebirth multiplier** is applied on top of `EXT`. The pacing table below is for the **first life** (multiplier ×1).

### Stats
Two tracks feed stats, so neither can be skipped:

| Stat | From Qi cultivation | From Body cultivation |
|---|---|---|
| ATK | ×1.12 per level | Iron Sand Palm mastery only |
| Max Qi (pool, also spent by combat arts) | = the Qi pool (Vessel Model) | — |
| Max HP (pool, also combat HP) | — | = the HP pool (Vessel Model) |
| DEF | — | ×1.06 per layer |
| HP regen | — | = Tempering rate while HP isn't full. Potions add bursts |

- A major **Qi** breakthrough multiplies ATK by **×2.5** from Foundation Establishment on. The three short opening-realm gates (MO→QC, QC→QS, QS→FE) give **×1.35** each ([content/01-Realms](content/01-Realms.md)).
- A **Body** stage breakthrough multiplies DEF by **×1.4** (exceptions: Diamond Vajra Body ×1.6, Immortal Body ×1.8, per [content/02-Body](content/02-Body.md)). Max HP jumps to the new stage's base.
- **Combat arts cost a % of Max Qi** (3–10%), and monster damage is tuned as a % of the intended Max HP, so the shared pools scale naturally.
- **Exercise mastery** (levels 1–99): +1% of its stat per level, so a maxed exercise gives about +99%, permanently (kept through rebirth).
- Gear adds about 40–60% on top of base at the intended map tier. This makes gear matter without overriding realms.

### Combat difficulty
- Monster HP/ATK in a zone = `zoneTier × 1.18^zoneIndex`, tuned so a player at the **intended realm/level** clears zone 1 at ~95% win rate and the boss at ~60%.

## Pacing Table (Qi only, realms 1–4)
"Effective time" counts time online **plus** offline time (within the cap). A typical player gets about **12 effective hours per day** (3–6 check-ins with an 8 h offline cap).

| Realm | Lvl | Qi work | Qi/s | Time | Cumulative (effective)* |
|---|---|---|---|---|---|
| Meridian Opening | 1–9 (realm total) | 15 → … | 0.6 → 1.3 | ~6 min | 6 min |
| Qi Condensation | 1–9 (realm total) | 50 → … | 1.0 → 2.1 | ~11 min | 17 min |
| Qi Sea | 1–9 → BT (realm total) | 250 → … | 2.0 → 4.3 | ~29 min | 46 min |
| Foundation Est. | 1 | 12,000 | 7.5 | 27 min | 40 min |
| Foundation Est. | 2 | 13,800 | 8.2 | 28 min | 1.1 h |
| Foundation Est. | 3 | 15,870 | 9.1 | 29 min | 1.6 h |
| Foundation Est. | 4 | 18,250 | 10.0 | 30 min | 2.1 h |
| Foundation Est. | 5 | 20,988 | 11.0 | 32 min | 2.7 h |
| Foundation Est. | 6 | 24,136 | 12.1 | 33 min | 3.2 h |
| Foundation Est. | 7 | 27,757 | 13.3 | 35 min | 3.8 h |
| Foundation Est. | 8 | 31,920 | 14.6 | 36 min | 4.4 h |
| Foundation Est. | 9 → BT | 110,125 | 16.1 | 1.9 h | 6.3 h |
| Golden Core | 1 | 400,000 | 62.5 | 1.8 h | 8.1 h |
| Golden Core | 2 | 460,000 | 68.8 | 1.9 h | 9.9 h |
| Golden Core | 3 | 529,000 | 75.6 | 1.9 h | 11.9 h |
| Golden Core | 4 | 608,350 | 83.2 | 2.0 h | 13.9 h |
| Golden Core | 5 | 699,602 | 91.5 | 2.1 h | 16.0 h |
| Golden Core | 6 | 804,543 | 100.7 | 2.2 h | 18.3 h |
| Golden Core | 7 | 925,224 | 110.7 | 2.3 h | 20.6 h |
| Golden Core | 8 | 1,064,008 | 121.8 | 2.4 h | 23.0 h |
| Golden Core | 9 → BT | 3,670,827 | 134.0 | 7.6 h | 30.6 h |
| Nascent Soul | 1 | 9,000,000 | 500.0 | 5.0 h | 35.6 h |
| Nascent Soul | 2 | 10,350,000 | 550.0 | 5.2 h | 40.8 h |
| Nascent Soul | 3 | 11,902,500 | 605.0 | 5.5 h | 46.3 h |
| Nascent Soul | 4 | 13,687,875 | 665.5 | 5.7 h | 52 h |
| Nascent Soul | 5 | 15,741,056 | 732.1 | 6.0 h | 58 h |
| Nascent Soul | 6 | 18,102,215 | 805.3 | 6.2 h | 64 h |
| Nascent Soul | 7 | 20,817,547 | 885.8 | 6.5 h | 71 h |
| Nascent Soul | 8 | 23,940,179 | 974.4 | 6.8 h | 78 h |
| Nascent Soul | 9 → BT | 82,593,617 | 1,071.8 | 21.4 h | 99 h |

*From Foundation Establishment on, the cumulative column was computed for the old single opening realm (14 min). Add about **+32 min** for the three new opening realms (46 min total). Per-level times are unchanged.

### Resulting milestones
"Effective time" in the table above is **time spent Meditating**. Activities are exclusive ([02-Systems §0b](02-Systems.md)), so assume a typical split of **40% Meditate / 30% Train / 30% Battle**. Of ~12 effective h/day, that's about **4.8 h/day of meditation**.

| Milestone | Meditation time | Calendar (first life) |
|---|---|---|
| First level-up | <1 min | First session |
| Reach Qi Condensation | 6 min | First session |
| Reach Qi Sea | 17 min | First session |
| Reach Foundation Establishment | ~46 min | Day 1 (~2 h of play) |
| Reach Golden Core | ~4.5 h | **Day 1** |
| Reach Nascent Soul | ~23 h | **Day ~5** |
| Reach Soul Formation | ~100 h + gates | **Day ~21** |

*(Values from Balancing.xlsx with realistic multipliers: grounds, Talisman, method, achievements.)*

### Pacing philosophy: fast start, steady later (decided)
| Phase | Pace | Where the rush comes from |
|---|---|---|
| First hour | Very fast | A level-up every 30–60 s, 3 realms in ~50 min, first sword drop, first ground unlock |
| Days 1–5 | Fast | Golden Core on day 1, Nascent Soul around day 5. Breakthroughs every few hours |
| Day 5+ | Steady | Realms take days, but every session has small wins: drops, crafts, perks, harvests |
| Rebirths | Spikes | Each new life replays the fast early realms at ×1.5 → ×3 → ×4.5+ speed |

Why not fast overall: v1.0 would be finished in 3–4 weeks, long before post-launch updates. The rush comes from **reward frequency and feedback**, not from burning through realms ([01-GDD § Reward Cadence](01-GDD.md)).

**Notes:**
- The table covers **Qi only**. Real progress will be slower because breakthroughs also need materials, a success roll, and (from Golden Core) a tribulation boss that may need better gear. Expect a further +20–40%.
- Breakthrough-attempt rows (BT) show one successful attempt. A failed attempt adds a partial repeat.
- The activity split is the biggest pacing lever. Measure the real split in playtests and retune `BASE` if it differs much from 40/30/30.

## Body Cultivation Pacing
Same shape as Qi (Vessel Model: `cost` below = **work**, cap = 0.76 × work, HP is the pool), with its own constants:
```
cost(S, L)  = BODY_BASE[S] × 1.15^(L−1)       (layer 9 = ×3, then the material gate)
temper(S,L) = 1.0 × 4^S × 1.10^(L−1) × EXT_body × BodyMultiplier   (rebirth, see below)
```
`S` = 0 for Copper Skin. `EXT_body` assumes exercise and bath bonuses of 1.0 / 1.5 / 2.5 / 4.0, matching Qi.

| Stage | BODY_BASE | Stage duration | Done at (cumulative, effective) | Qi realm at that time |
|---|---|---|---|---|
| Copper Skin | 400 | ~1.5 h | ~1.6 h | Foundation Est. |
| Iron Bone | 12,500 | ~8 h | ~9.5 h | Golden Core |
| Silver Marrow | 300,000 | ~28 h | ~38 h | Nascent Soul |
| Jade Flesh | 4,700,000 | ~70 h | ~108 h | Soul Formation |
| Golden Body | 77,000,000 | | target: done ~day 72 | |
| Diamond Vajra Body | 840,000,000 | | target: done ~day 155 | |
| Immortal Body | 5.5 × 10⁹ | | target: done ~day 250 | |

**Design intent:** the body stage trails the Qi realm by about one step, so the player always feels "my body needs to catch up" before a tribulation. Durations exclude the time spent farming breakthrough materials.

## Rebirth
### Multipliers gained: Qi and Body, both stacking
Rebirth gives **two** permanent multipliers: **Qi rate** (from the Qi realm reached) and **Tempering rate** (from the body stage reached). Both **stack by realm/stage**:
- every realm or stage you **passed through** adds its full gain;
- the one you're **in** adds a partial gain based on level;
- gains from all past rebirths then add together.
```
qiGain   = Σ REALM_GAIN[r] for each realm passed  +  REALM_GAIN[R] × (0.5 + 0.5 × L / 9)
bodyGain = Σ STAGE_GAIN[s] for each stage passed  +  STAGE_GAIN[S] × (0.5 + 0.5 × layer / 9)
Qi multiplier   = 1 + Σ qiGain   over all past rebirths
Body multiplier = 1 + Σ bodyGain over all past rebirths      (replaces the old flat +10% "Body Memory")
```
REALM_GAIN starts at Golden Core, and STAGE_GAIN starts at Iron Bone (body runs about one stage behind Qi). Both double per step.

| Qi realm reached | REALM_GAIN | Qi gain at level 1 | Qi gain at peak | Body stage reached | STAGE_GAIN | Body gain at layer 1 | Body gain at peak |
|---|---|---|---|---|---|---|---|
| Golden Core | 0.5 | +0.28× | +0.50× | Iron Bone | 0.5 | +0.28× | +0.50× |
| Nascent Soul | 1 | +1.06× | +1.50× | Silver Marrow | 1 | +1.06× | +1.50× |
| Soul Formation | 2 | +2.61× | +3.50× | Jade Flesh | 2 | +2.61× | +3.50× |
| Void Breaking | 4 | +5.72× | +7.50× | Golden Body | 4 | +5.72× | +7.50× |
| Mahayana | 8 | +11.9× | +15.5× | Diamond Vajra Body | 8 | +11.9× | +15.5× |
| Great Ascension | 16 | +24.4× | +31.5× | Immortal Body | 16 | +24.4× | +31.5× |

- Lives still **add** together (they don't multiply each other), so quick rebirths can't snowball. Within one life, stacking makes every extra realm/stage worth more than everything before it combined, so going deeper always wins.
- **Body is now rewarded:** a player who rebirths at Nascent Soul peak with an Iron Bone body gets +1.5× Qi but only +0.28–0.5× Body. Training the body before rebirthing pays off.
- **Example:** first life to Golden Core peak (~31 h of meditation). Rebirth gives ×1.5 Qi. Second life reaches the same point in about 21 h, then pushes on. A Nascent Soul peak rebirth then adds +1.5 (total ×3.0).
- **Balance watch:** stacking makes later lives much faster than the old rule did (for example, ×4.5 Qi after three early lives). Check the realm targets in [content/00-Registry](content/00-Registry.md) in the balancing spreadsheet, and lower `REALM_GAIN` if lives 4+ fly by.
- **Break-even check:** rebirthing at the Golden Core peak vs pushing through Nascent Soul is roughly equal in time (~65 h vs ~68 h to finish Nascent Soul). That's intentional: the first rebirth is a meaningful choice, not a no-brainer.

### Karma (M2)
**Karma stacks by realm reached.** Each realm you reach before rebirthing adds its own Karma on top of the realms before it:
`Karma = 2 for Golden Core, then +3, +4, +5, … for each further realm reached`

**Body stages add Karma too, also stacking:** Iron Bone 1, Silver Marrow +2 (3), Jade Flesh +3 (6), Golden Body +4 (10), Diamond Vajra Body +5 (15), Immortal Body +6 (21). Total Karma per rebirth = Qi Karma + Body Karma.
so Golden Core gives 2, Nascent Soul 2+3 = **5**, Soul Formation **9**, Void Breaking **14**, Mahayana **20**, Great Ascension **27**. Spent in a perk tree. Example costs: auto level-up (3), start new lives at Qi Sea 9 (5), +2 h offline cap (5), Bonded Weapon: your weapon ignores its realm requirement (8). Full tree in [content/12-Rebirth](content/12-Rebirth.md).

## Spirit Stone Flow (per hour, intended)
| Realm | Income (combat + salvage) | Main sinks |
|---|---|---|
| MO–QS | ~200 | Starter gear, worker slot |
| Foundation Est. | ~2,000 | Enhance +1…+5, Mining nodes |
| Golden Core | ~15,000 | Enhance +6…+10, alchemy furnace upgrades |
| Nascent Soul | ~100,000 | Enhance +11…+15, reforging, field plots |

Target: the player can afford **roughly 1 meaningful stone purchase per check-in**.
From SF onward, extrapolate at about **×7 per tier**. Per-kill values are in [content/03-Combat-Maps](content/03-Combat-Maps.md), tuned so about 360 kills/h reproduces this table.
**Known pressure point:** fully enhancing six T2 items to +5 costs about 14.5k stones, against about 12k earned during FE. Enhancement Transfer ([content/05-Equipment](content/05-Equipment.md)) softens this. Verify it in the balancing spreadsheet.

## Offline Gains
```
offlineSeconds = min(now − lastSave, cap)          cap = 8 h (12 h with IAP)
Qi         = rate_at_logout × offlineSeconds × 1.0
Tempering  = temper_at_logout × offlineSeconds × 1.0   (mastery XP too)
Combat     = expectedKillsPerSec(currentZone) × offlineSeconds × uptime × 0.8  → batch-roll loot
             uptime = share of time spent fighting vs retreating/recovering (Vessel Model; see content/03-Combat-Maps)
Growth     = only during Meditate/Train steps, after the pool is full
LifeSkills = jobs completed = floor(offlineSeconds / jobDuration) × 1.0
```
- Levels are **not** auto-purchased offline (the player enjoys spending on return). The return screen shows "Ready to level up ×4".
- Offline time is checked against a trusted time source when online (see [06-Tech](06-Tech.md)) to discourage clock cheating.

## Number Formatting
Numbers grow large past Soul Formation. Use suffixes K, M, B, T, then aa, ab… (or scientific notation as an option). The game will need a big-number type from realm 6 onward.

## Balancing Process
**The working model is [Balancing.xlsx](Balancing.xlsx)** (Inputs → EXT_Budget → Qi/Body pacing → Rebirth → Grounds economy → Checks).

1. Keep all constants in data tables (spreadsheet → exported data), never hard-coded.
2. Build a balancing spreadsheet that reproduces the formulas above, including EXT assumptions per system.
3. Playtest with a time-acceleration debug flag (×10, ×100).
4. Track the telemetry "time to realm X" against this table during the closed beta and after launch.

## Decisions
- **Qi overflow:** resolved by the Vessel Model. Whatever's left in the pool after a breakthrough spend stays.
- **Offline combat efficiency:** 80%.
- **Free Jade:** yes, about 1 cosmetic per month from dailies, achievements, and events.
- **Minimum rebirth point:** Golden Core.
- **Achievements:** up to +300% Qi in total (counted in `EXT`).
- **Heaven's Favor:** +10% per rank, 3 ranks.
