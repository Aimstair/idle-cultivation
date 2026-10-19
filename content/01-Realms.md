# Content 01 — Realms & Tribulations

Uses names from [00-Registry](00-Registry.md). Formulas: [03-Economy](../03-Economy.md). Systems: [02-Systems §1–2](../02-Systems.md).

These are the 10 realms of the **Mortal Plane**, the launch ladder. Later Planes (Immortal → Primordial, 55 more realms) are reached through **Ascension**: see [16-Planes-Ascension](16-Planes-Ascension.md).

## Level Structure (all realms)
| Levels | Stage name | Display example |
|---|---|---|
| 1–3 | Early | "Golden Core · Early · Layer 2" |
| 4–6 | Middle | "Golden Core · Middle · Layer 5" |
| 7–8 | Late | "Golden Core · Late · Layer 8" |
| 9 | Peak (the breakthrough attempt) | "Golden Core · Peak — Breakthrough ready" |

All levels follow the **Vessel Model** ([02-Systems §0](../02-Systems.md)):
- Qi refills at the full rate and grows **only while Meditating** ([02-Systems §0b](../02-Systems.md)).
- During any other activity, Qi still **base-regenerates at 10% of the normal rate**, but base regen never grows Max Qi.
- Where you meditate matters. Each **Meditation Site** multiplies the Qi rate: ×1.00 at the Humble Hut, up to ×3.60, and ×4.50 at Summit of Heaven. New sites unlock from combat-map boss clears ([15-Cultivation-Grounds](15-Cultivation-Grounds.md)).
- Qi refills the pool first. Max Qi grows only while the pool is full, and growth stops at the level's **cap**.

**Breaking through:**
- **Levels 1→8:** breaking through **spends 80% of the cap** in Qi. There's no success roll: with enough Qi, it always succeeds. With too little, it fails, Qi is drained, and the cultivator gets **Qi Deviation** ([02-Systems §1b](../02-Systems.md)).
- **Level 9 → next realm** is the **Breakthrough**. It needs **100% of the peak cap** (a full pool; the peak cap is ×1.6 a normal cap).
  - From QS → FE onward, it also needs a gate pill and passes a success roll.
  - From GC onward, it's followed by a **Heavenly Tribulation**.
  - The two opening gates (MO → QC, QC → QS) are tutorial gates: full Qi only, with no pill and no roll.
- After entering a new realm, Max Qi jumps to the new realm's base with a near-empty pool. The **consolidation refill** that follows is a long refill period before growth resumes.

## Realm Overview
| # | Realm | Qi rate × (REALM_RATE) | ATK × | Base BT chance | Reach (typical) | Milestone |
|---|---|---|---|---|---|---|
| 1 | Meridian Opening | 0.6 | 1 | — | Start | M0 |
| 2 | Qi Condensation | 1 | 1.35 | — (no roll) | First session, ~6 min of meditation | M0 |
| 3 | Qi Sea | 2 | 1.85 | — (no roll) | First session, ~17 min of meditation | M0 |
| 4 | Foundation Establishment | 5 | 2.5 | 80% | Day 1, ~46 min of meditation (~2 h of play) | M0 |
| 5 | Golden Core | 25 | 6.25 | 65% | Day 1 (~4.5 h of meditation) | M1 |
| 6 | Nascent Soul | 125 | 15.6 | 55% | Day ~5 | M2 |
| 7 | Soul Formation | 625 | 39 | 50% | Day ~21 | M2 |
| 8 | Void Breaking | 3,125 | 98 | 45% | Day ~40 | M2 |
| 9 | Mahayana | 15,625 | 244 | 40% | Day ~65 | M3 |
| 10 | Great Ascension | 78,125 | 610 | 35% | Day ~110 | M3 |
| → | **Ascension** (Immortal Plane) | new Plane ladder | — | 30% | Day ~180 | M3+ |

- "Base BT chance" is the chance of breaking **into** that realm.
- ATK multipliers are cumulative. Each opening-realm breakthrough gives ×1.35; from FE onward, each major breakthrough gives ×2.5.
- "Reach" assumes a first life with a 40/30/30 Meditate/Train/Battle split (see [00-Registry](00-Registry.md)). Rebirths shorten it.
- **Max Qi** is the Qi pool, so it isn't listed as a multiplier. Its size per level comes from `cap(R, L)` in [03-Economy](../03-Economy.md).
- **Max HP** comes only from Body Cultivation ([02-Body](02-Body.md)).
- Max Qi is also the combat Qi pool: combat arts spend it.

### Breakthrough chance modifiers
| Source | Bonus |
|---|---|
| Gate pill (required) | Included in base |
| Insight stacks (from failures) | +5% each |
| Insight Pill | +15% |
| Rewarded ad | +10% (1 per attempt) |
| Each completed body stage | +2% |
| Karma perk *Dao Heart* | +5% per rank |
| Accessory affix *+Breakthrough chance* | +1–3% |
| Cap | 100% |

### Breakthrough attempt, step by step
| Step | Check | If it fails |
|---|---|---|
| 1. Pool check | Current Qi = 100% of the peak cap (full pool) | **Fail:** Qi drops to 0 and the cultivator gets **Qi Deviation** (one stack: ×0.8 Qi rate, −5% ATK, 5 min; stacks are unlimited). The gate pill is **kept**. The modal first warns "Not enough Qi — this attempt will fail" and asks for confirmation |
| 2. Success roll (from QS → FE) | Base chance + modifiers above | **Fail:** 50% of the cost is spent, the gate pill is kept, **no injury**, +1 Insight stack. Refill and retry |
| 3. Success | — | The gate pill is consumed and the Qi is spent. From GC onward a **Heavenly Tribulation** follows. Max Qi jumps to the new realm's base only after the tribulation is cleared (or right away before GC) |

Normal levels (1→8) use only step 1, at 80% of the cap. The two tutorial gates (MO → QC, QC → QS) use only step 1, at 100%.

---

## Realm Details

### 1. Meridian Opening (开脉)
*"Heaven-and-earth Qi forces its way into meridians that have never carried it before."*
- **Unlocks:**
  - L1: Qi Cultivation, Meditation boost, Mining, Inventory, and the Battle and Meditate activities.
  - L5: Combat & Maps, Equipment, Sword Pavilion.
- **Gate out:** full Qi only (tutorial gate). No pill, no roll, no tribulation.
- **Visual:** a mortal in plain clothes. Faint white threads trace the meridians while meditating.
- **Pacing:** about 30–50 s per level. The realm takes ~6 min of meditation. All times are **meditation time**. Battle adds none and drains the pool (see [03-Economy](../03-Economy.md)).

### 2. Qi Condensation (凝气)
*"The threads thicken into droplets. Qi begins to gather instead of slipping away."*
- **Unlocks:**
  - L1: Body Cultivation and the **Train** activity.
  - L5: Alchemy (first big recipe: the Foundation Pill).
- **Gate out:** full Qi only (tutorial gate).
- **Visual:** grey disciple robe. White wisps swirl around the body.
- **Pacing:** ~1 min per level, ~11 min total.

### 3. Qi Sea (气海)
*"Droplets become a lake within your dantian. For the first time, it is deep enough to drown in."*
- **Unlocks:** the **Pendant** accessory slot and the Sword Pavilion's **rotating stock**. The rest of the realm is spent preparing the Foundation Pill (Mining, Map 2 Bandit Pass, Alchemy).
- **Gate out:** Foundation Pill (Alchemy 5). No tribulation.
- **Visual:** a soft blue swirl at the dantian while meditating.
- **Pacing:** 2–4 min per level, ~29 min total.

### 4. Foundation Establishment (筑基)
*"Your Qi condenses into a liquid sea. Your dao foundation is laid."*
- **Unlocks:** Routines, Forging, Woodcutting, 2nd worker slot, Dungeon 1 (Spirit Vein Cave), Daily Quests, combat art slot 2.
- **Gate out:** Golden Core Pill (Alchemy 20) → **Tribulation I**.
- **Visual:** pale blue aura, outer-disciple robe, a sword appears on the back.
- **Pacing:** levels take 27–36 min each (level 1 includes the consolidation refill), and the peak ~1.9 h. Realm total ~6 h of meditation.

### 5. Golden Core (金丹)
*"The Qi sea compresses into a golden core that hums within your dantian."*
- **Unlocks:** Rebirth, Heavenly Tribulations, Trial Tower, Fishing, Cooking, Spirit Fields + Farming, Dungeon 2, Achievements.
- **Gate out:** Nascent Pill (Alchemy 35) → **Tribulation II**.
- **Visual:** a golden orb glows at the dantian. Inner-disciple robe, and the aura turns gold.
- **Pacing:** ~2 h per level, ~24 h of meditation total.

### 6. Nascent Soul (元婴)
*"A tiny infant of light opens its eyes inside your core: your soul made flesh."*
- **Unlocks:** Pets, 3rd worker slot, Dungeon 3.
- **Gate out:** Soul Nurturing Pill (Alchemy 50) + Soul Lotus ×3 → **Tribulation III**.
- **Visual:** a translucent miniature of the character floats above the head while meditating. Elder robe.
- **Pacing:** 5–7 h per level, ~68 h of meditation total (first life).

### 7. Soul Formation (化神)
*"Your soul expands beyond your body. You sense everything within a hundred li."*
- **Unlocks:** Sect, combat art slot 3, Dungeon 4.
- **Gate out:** Void Pill (Alchemy 60) → **Tribulation IV**.
- **Visual:** a soul-sense ripple ring pulses around the character. Eyes glow.

### 8. Void Breaking (破虚)
*"You strike, and space itself cracks. The void is no longer a wall but a door."*
- **Unlocks:** Reforge tier 2, 2nd cultivation-method slot, Dungeon 5.
- **Gate out:** Mahayana Pill (Alchemy 70) → **Tribulation V**.
- **Visual:** cracks of starry void flicker around the silhouette.

### 9. Mahayana (大乘)
*"Soul, flesh, and dao fuse into one. Heaven itself begins to notice you."*
- **Unlocks:** Dungeon 6, 4th worker slot.
- **Gate out:** Great Ascension Pill (Alchemy 85) → **Tribulation VI**.
- **Visual:** a dharma wheel halo and sage robes. The body-stage sheen (see [02-Body](02-Body.md)) and the Qi aura merge into one dual-colored glow.

### 10. Great Ascension (大飞升)
*"Heaven's punishment gathers. Survive it, and you are no longer mortal."*
- **Unlocks:** Dungeon 7 (L1), Dungeon 8 + Ascension preview (L5).
- **Gate out (M3+):** Ascension Pill (Alchemy 95) + body at Diamond Vajra Body or higher → **Final Tribulation** → **Ascension** to the Immortal Plane.
- **Visual:** permanent storm clouds over the home scene. Robes shimmer with thunder runes. A pillar of light appears at peak.

### → Ascension
*"You ascend. The mortal world becomes a memory."*
- A one-way move to the **Immortal Plane** (Loose Immortal → Dao Immortal). It's the second prestige layer above Rebirth:
  - Rebirth multipliers convert into permanent **Dao Marks**.
  - The Mortal realm, maps, and grounds are left behind.
  - Karma, perks, life skills, pets, and items are kept.
- Full rules and the other 9 Planes: [16-Planes-Ascension](16-Planes-Ascension.md).

---

## Heavenly Tribulations
### Shared rules
- A tribulation starts automatically after a successful breakthrough roll. You can **postpone** it: your state is saved as "Breakthrough pending", and the gate pill and Qi are already spent. Postponing is **unlimited** (idle-friendly), with a gentle reminder, and the game offers a one-tap **refill Routine** (Train to full → Meditate to full).
  - While pending, Max Qi stays at the peak cap. The pools still refill, but don't grow.
  - Postponing is the normal way to **refill HP and Qi before the fight**.
- It's a scripted fight: **N lightning strikes (waves)**, each dealing damage scaled to the realm. Some tribulations add a special mechanic. You survive by not dropping to 0 HP before the last strike.
- **It uses your current pools** (Vessel Model):
  - You enter with whatever HP you have right now, so **entering with low HP is risky**. Coming straight from Battle or a body breakthrough is a bad idea. Switch to **Train** first.
  - Combat arts spend your current Qi, which is low right after the breakthrough spend unless you postponed and refilled.
  - Damage taken stays after the fight, win or lose.
- **Damage taken** = strike power × (1 − body-stage reduction − lightning resist) × DEF mitigation.
  - Each completed body stage: −5% lightning damage.
  - Lightning Tempering mastery: +1% lightning resist per level.
  - Karma perk *Tribulation Scar*: −10% per rank.
- Healing Pills and food buffs work during tribulations. Pets do not take part (heaven judges you alone).
- **On loss:**
  - Your HP hits 0 and you get **Internal Injury** ([02-Systems §1b](../02-Systems.md)), as in any combat. Nothing else is lost.
  - You stay at Peak with "Breakthrough pending". You can retry after a **10-minute** cooldown, or immediately once per day via rewarded ad. Realistically, you must heal (Train or Healing Pills) before retrying.
  - Routines never auto-start a tribulation.
- **On win:** you enter the new realm. Max Qi jumps to the new base and the consolidation refill begins. HP stays at whatever the strikes left.
- **Rewards (first clear):** realm entry, Thunder Essence, a title, Jade.
- **Pre-fight screen:**
  - Shows recommended HP and DEF, and your **current HP / Max HP and current Qi**.
  - Gives a survival estimate (Low / Fair / Good / Certain) based on current HP, not max.
  - When the estimate is Low, offers a "Heal first" shortcut (Healing Pills, or postpone).

### Tribulation list
| # | Name | Gate | Strikes | Special mechanic | Mainly checks | First-clear rewards |
|---|---|---|---|---|---|---|
| I | Three-Strike Lightning | FE → GC | 3 | None. Teaches the system | HP | Thunder Essence ×3, 50 Jade, title *Thunder-Touched* |
| II | Six-Strike Lightning | GC → NS | 6 | Strike 6 deals ×2 damage | HP, DEF | Thunder Essence ×6, 80 Jade |
| III | Nine-Strike Lightning | NS → SF | 9 | Strikes 4–9 leave **Paralysis**: −20% healing until the end | HP, DEF, healing (pills, base regen) | Thunder Essence ×10, 100 Jade, title *Nine-Strike Survivor* |
| IV | Heart Demon Trial | SF → VB | 3 phases | You fight a **mirror copy** of yourself at **90% of your stats** (same gear, skills, and **same current HP/Qi** you enter with). No lightning | Balanced ATK/HP, combat arts | Thunder Essence ×12, 120 Jade, title *Heart Unshaken* |
| V | Purple Divine Thunder | VB → MA | 9 | Each strike reduces SPD by 10% (stacking). A slow build gets hit more | HP, DEF, SPD | Thunder Essence ×15, 150 Jade |
| VI | Nine Heavens Thunder | MA → GA | 9 + guardian | After strike 9, a **Heavenly Guardian** boss appears that you must defeat | Everything | Thunder Essence ×30, 250 Jade, title *Calamity Walker* |
| Final | Heavenly Dao Judgement | GA peak → Ascension | 3 phases | Phase 1: lightning. Phase 2: heart demon. Phase 3: Heavenly Dao Avatar fight | Everything | Immortal title, **Ascension** (M3+) |

*The Fire & Wind Calamity (Fire waves apply Burn, Wind waves remove buffs) has moved to the Immortal Plane ([16-Planes-Ascension](16-Planes-Ascension.md)).*

### Tribulation presentation
- The screen darkens and clouds gather. Each strike: a white flash, screen shake, damage number, HP bar.
- Surviving the final strike: light pours down, a gong sounds, and the character transforms into the new realm's look.
- Haptics on each strike (respects the vibration setting).

## Decisions
- **Postponing a tribulation:** unlimited, with a gentle reminder.
- **Heart Demon mirror:** 90% of your stats.
- **Tribulations count as Battle:** only base regen plus pills heal during the fight (confirmed).
- **Refill Routine:** offered with one tap when postponing.
- **Qi Sea** unlocks the Pendant slot and the Sword Pavilion's rotating stock.
