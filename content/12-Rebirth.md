# Content 12 — Rebirth & Past-Life Perks

System overview: [02-Systems §2c](../02-Systems.md). Formulas: [03-Economy → Rebirth](../03-Economy.md#rebirth).

## Unlock
- New lives start with the **starting pools full** (Meridian Opening 1 Max Qi and the Mortal Body Max HP), so growth begins immediately.
- The first time you reach **Golden Core**, a short story beat plays: an old hermit says, "Some cultivators walk the path more than once…" A **Rebirth** button appears on the Cultivate screen.
- **Milestone:** M1 (Qi + Body multipliers), M2 (Karma + perk tree).
- **Rebirth vs Ascension:** Rebirth restarts the current Plane at its first realm (Mortal Plane: Meridian Opening). **Ascension** ([16-Planes-Ascension](16-Planes-Ascension.md)) is the bigger, one-way layer above it: it converts the Qi and Body multipliers into permanent Dao Marks and moves you to the next Plane. Karma and perks survive both.

## Rebirth Flow
### 1. Preview screen
| Section | Contents |
|---|---|
| Header | "Reincarnate?" plus the current realm/level and life number ("Life 3") |
| **You will gain** | Qi multiplier: current ×2.50 → **×3.56** (+1.06, Nascent Soul 1). Body multiplier: ×1.50 → **×2.00** (+0.50, Iron Bone peak). Karma: +5 (M2) |
| **You will keep** | Icons: life skills, mastery, gear and inventory, techniques, pets, fields, Jade, purchases, achievements, 10% of Spirit Stones (+ perks) |
| **You will lose** | Qi and HP pools (current and max), realm, body stage, 90% of Spirit Stones, map/boss progress, active pill buffs |
| **Cleared** | Active injuries (Qi Deviation, Internal Injury): a new body starts healthy |
| **Projection** | "You'll be back to Golden Core · Peak in ~21 h (was ~31 h)." Uses the headless sim with the new multiplier |
| **Advice tag** | *Too early* (gain under 15% of current multiplier) / *Good time* / *Great time* (time to next level > 4 h and gain ≥ 25%) |
| Next tier tease | "Reach Nascent Soul to gain +1.06× instead." |

### 2. Confirmation
- Hold-to-confirm button (2 s) with the text "Begin the next life." No accidental taps.
- If a breakthrough is **pending** or there are **unclaimed** rewards (quests, offline gains), a warning shows first.

### 3. Animation beats (~6 s, skippable after the first time)
1. The character sits in meditation. The aura flares and then fades.
2. The body dissolves into motes of light. A soul orb rises.
3. The orb crosses a starry river (reincarnation). The multiplier number counts up on screen.
4. A newborn glow lands. The character re-forms as a mortal at Meridian Opening. Text: "Life 4 begins."
5. Return to the home screen with a toast showing the new multiplier.

## Reset / Keep
| Resets | Kept |
|---|---|
| Qi pool (current and Max Qi), realm, level, Insight stacks | Qi and Body multipliers, Karma, perks |
| HP pool (current and Max HP), body stage, layers | Exercise mastery |
| Injuries (Qi Deviation, Internal Injury), cleared | Retreat/resume points, Qi floor, saved Routines (current activity resets to Meditate) |
| 90% of Spirit Stones | Life-skill levels, recipes, worker slots |
| Map and boss progress (first-kill rewards don't repeat), and the **Cultivation Grounds** those boss clears unlocked (they re-unlock as you re-clear bosses; Humble Hut and Village Courtyard are always available) | Gear and inventory (realm requirements still apply) |
| Dungeon tier progress | Techniques and comprehension, pets, Spirit Field plots and crops |
| Active pill and bath buffs, pending breakthrough | Achievements, titles, Jade, cosmetics, IAP perks |
| Trial Tower floor for the current week | Lifetime stats ("deepest realm ever") |

## Multipliers (Qi and Body, both stacking)
Both stack by realm/stage: every realm or stage passed through adds its full gain, and the current one adds a partial gain. Lives add together. Formulas in [03-Economy](../03-Economy.md#rebirth).
```
qiGain   = Σ REALM_GAIN of realms passed + REALM_GAIN[R] × (0.5 + 0.5 × L / 9)
bodyGain = Σ STAGE_GAIN of stages passed + STAGE_GAIN[S] × (0.5 + 0.5 × layer / 9)
```
**Body** uses the same numbers, shifted: Iron Bone = Golden Core's row, Silver Marrow = Nascent Soul's row, and so on.

| Highest realm reached | REALM_GAIN | Qi gain, level 1 (stacked) | Level 5 | Level 9 (peak) | Karma, stacked (M2) |
|---|---|---|---|---|---|
| Golden Core | 0.5 | +0.28× | +0.39× | +0.50× | 2 |
| Nascent Soul | 1 | +1.06× | +1.28× | +1.50× | 5 (2+3) |
| Soul Formation | 2 | +2.61× | +3.06× | +3.50× | 9 (+4) |
| Void Breaking | 4 | +5.72× | +6.61× | +7.50× | 14 (+5) |
| Mahayana | 8 | +11.9× | +13.7× | +15.5× | 20 (+6) |
| Great Ascension | 16 | +24.4× | +27.9× | +31.5× | 27 (+7) |

The opening realms (MO, QC, QS) and Foundation Establishment give no rebirth gain. Rebirth unlocks at Golden Core.

**Karma stacks:** each realm reached adds its own Karma on top of the ones before it (GC 2, then +3, +4, …). Pushing one realm deeper is always worth noticeably more than rebirthing early.

**Body Karma (stacks the same way):**

| Body stage reached | Iron Bone | Silver Marrow | Jade Flesh | Golden Body | Diamond Vajra Body | Immortal Body |
|---|---|---|---|---|---|---|
| Body Karma | 1 | 3 | 6 | 10 | 15 | 21 |

Total Karma per rebirth = Qi Karma + Body Karma. A typical life-1 rebirth (Golden Core peak, body in Silver Marrow) gives **2 + 3 = 5**.

## Past-Life Perk Tree (M2)
Three branches. A perk needs its prerequisite. Karma costs are per rank.

### Dao (cultivation)
| Perk | Effect per rank | Max | Cost | Prerequisite |
|---|---|---|---|---|
| Lingering Qi | +5% Qi rate | 5 | 1 | — |
| Old Habits | Auto level-up (levels 1–8, Qi and body layers). It **only attempts when the pool covers the 80% spend**, so it never triggers a failure or injury. It never auto-attempts realm/stage gates | 1 | 3 | — |
| Still Waters | Refill is faster: +15% Qi rate and Tempering while the pool is **below** max (growth is unaffected) | 3 | 2 | Lingering Qi 1 |
| Dao Heart | +5% Qi breakthrough chance | 3 | 4 | Lingering Qi 3 |
| Reincarnated Prodigy | Start new lives at Qi Sea 9 (skips the opening realms), with **full pools** | 1 | 5 | Old Habits |
| Tribulation Scar | −10% tribulation damage | 2 | 6 | Dao Heart 1 |
| Born at the Foundation | Start new lives at FE 1 (replaces Prodigy), with **full pools** | 1 | 12 | Reincarnated Prodigy |
| Heaven's Favor | +10% to future rebirth gains | 3 | 8 | Born at the Foundation |

### Body (body and combat)
| Perk | Effect per rank | Max | Cost | Prerequisite |
|---|---|---|---|---|
| Muscle Memory+ | +5% mastery XP | 5 | 2 | — |
| Iron Will | +5% Tempering | 5 | 2 | — |
| Battle Instinct | +5% ATK and DEF in combat | 3 | 3 | — |
| Quick Recovery | Each injury stack lasts 1 min less (5 → 4 → 3 min) | 2 | 2 | Iron Will 1 |
| Bloodline Awakening | Beast Blood bursts +50% | 1 | 6 | Iron Will 2 |
| Second Training Slot | Run 2 exercises at once | 1 | 10 | Iron Will 3 |
| Reborn Body | Start new lives with Copper Skin complete (at Iron Bone layer 1, HP pool full) | 1 | 12 | Iron Will 5 |

### Fortune (economy and convenience)
| Perk | Effect per rank | Max | Cost | Prerequisite |
|---|---|---|---|---|
| Merchant's Memory | Keep +5% more Spirit Stones on rebirth (10% → max 35%) | 5 | 1 | — |
| Disciplined Routine | +1 Routine step (3 → 4 → 5) and unlocks timer/HP/Qi conditions on every step | 2 | 4 | Merchant's Memory 1 |
| Lucky Star | +3% rare drop chance | 5 | 3 | — |
| Map Memory | Map unlocks **and their Meditation Sites / Training Grounds** persist through rebirth (bosses don't need re-killing to travel, meditate, or train there). Each ground still needs its **minimum realm**, so old grounds become usable again as you climb. Upkeep still applies | 1 | 10 | — |
| Long Meditation | +2 h offline cap | 1 | 5 | Merchant's Memory 2 |
| Dungeon Sweeper | Dungeon tiers cleared in past lives can be swept immediately | 1 | 6 | Map Memory |
| Bonded Weapon | Equipped weapon ignores realm requirement | 1 | 8 | Lucky Star 2 |
| Extra Hands | +1 worker slot | 1 | 10 | Long Meditation |
| Bigger Queue | Life-skill job queue grows to 5 | 1 | 4 | Merchant's Memory 1 |
| Prepared Mind | Your loadout switches automatically when the activity changes (Battle / Meditate / Train) | 1 | 6 | Disciplined Routine 1 |

**Totals:** Dao 82 Karma · Body 63 · Fortune 78 · **all perks ~223 Karma**. That's a long-term (several-month) goal. A typical player earns about 2–4 Karma per rebirth early on and 5–8 later.

### Karma timeline (typical player, 40/30/30 split, stacked Karma)
| Life | Rebirth at | Qi multiplier during this life | Approx. length | Karma earned | Total Karma | Calendar |
|---|---|---|---|---|---|---|
| 1 | Golden Core peak | ×1.0 | ~5 days | 2 | 2 | ~Day 5 |
| 2 | Nascent Soul peak | ×1.5 | ~14 days | 5 | 7 | ~Day 19 |
| 3 | Nascent Soul peak | ×3.0 | ~7 days | 5 | **12** | **~Day 26** |
| 4 | Soul Formation | ×4.5 | ~7 days | 9 | 21 | ~Day 33 |

- *Days from Balancing.xlsx (Rebirth sheet). The table above counts Qi Karma only.* Body Karma typically adds +3 in early lives and +6–10 later, so **10 Karma arrives around week 3 (2 lives)**.
- **(Qi only:) 10 Karma arrives around week 4 (3 lives).** Map Memory (10) is realistically a week 5–7 purchase once early cheap perks are bought.
- Deep lives pay a lot: a Void Breaking rebirth gives 14 and a Mahayana rebirth gives 20, so the full tree (~213) is a roughly 3–4 month goal.
- These are optimistic. The Qi multiplier doesn't speed up body training, material farming, or tribulations, so real lives run somewhat longer.

**Respec:** free once. After that, 200 Jade or a Rebirth Token (event reward). This is the only Jade touchpoint, and it never buys Karma.

## Recommended Strategy (what the advice tag nudges)
| Phase | Recommendation |
|---|---|
| Life 1 | Push to **Golden Core Peak** (~23 h of meditation, around day 5 with a 40/30/30 split). Rebirth there or early in Nascent Soul. Buy Old Habits plus Lingering Qi (Disciplined Routine if idling a lot) |
| Lives 2–3 | Go at least one realm deeper each life. Rebirth at **Nascent Soul Late/Peak** (+1.3–1.5× Qi). Take Reincarnated Prodigy and Iron Will |
| Lives 4–6 | Aim for **Soul Formation** (+2.6–3.5× Qi), and push the body to Silver Marrow or Jade Flesh for the Body multiplier. Rebirth when level-ups take more than ~6 h. Get Second Training Slot and Map Memory |
| Lives 7+ | Each life aims for a new deepest realm. Deep rebirths (VB+) dwarf early ones, so spamming shallow rebirths is inefficient by design |
| Endgame | Once Great Ascension and Diamond Vajra Body are in reach, do one last strong life and **Ascend**. Dao Marks scale with √(Qi × Body multiplier), so the final rebirths still pay off |
| Rule of thumb | Rebirth when **gain ≥ 25% of your current total multiplier** and the next level takes more than 4 h |

## Decisions
- **Heaven's Favor:** stays at +10% per rank, 3 ranks (max +30%).
- **Shallow rebirths:** keep giving Karma. Stacking already makes them inefficient.
- **Prodigy / Foundation starts:** full pools.
- New Fortune perks: **Bigger Queue** (5-slot job queue) and **Prepared Mind** (auto-swap loadout by activity).
