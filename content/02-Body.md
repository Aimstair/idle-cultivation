# Content 02 — Body Cultivation

System overview: [02-Systems §2b](../02-Systems.md). Formulas: [03-Economy → Body Cultivation Pacing](../03-Economy.md). Names: [00-Registry](00-Registry.md).

## How Stages Work
- Characters start as **Mortal Body** (no layers). When Body Cultivation unlocks at **QC 1**, you begin **Copper Skin, Layer 1**.
- Each stage has **9 layers**. Body uses the **Vessel Model** ([02-Systems §0](../02-Systems.md)) with **HP as the pool**. This is the same HP used in combat and tribulations.
- **Full Tempering only runs while the activity is Train** ([02-Systems §0b](../02-Systems.md)). During any other activity (Battle, Meditate), HP **base-regenerates at 10% of the Tempering rate**. Base regen refills HP but **never grows Max HP**.
  1. **Tempering refills current HP first.** Healing Pills, Beast Blood, and healer pets (in battle) add bursts on top of base regen.
  2. **Only at full HP** does Tempering raise **Max HP** (at 25% efficiency), up to the layer's **cap**.
  3. **Layer breakthrough (1→8):** spends **80% of the cap** in HP. There's no roll: with enough HP, it always succeeds.
  4. **Stage breakthrough (layer 9 → next stage):** needs **100% HP** (a full pool; the peak cap is ×1.6 a normal cap) **plus the breakthrough materials**. There's no random roll.
  5. **Not enough HP** for either kind of breakthrough: the attempt **fails**, HP drops to **1**, and the cultivator gets an **Internal Injury** stack (×0.8 Tempering rate, −5% DEF, 5 min per stack, stacks are unlimited). Materials are kept. The UI warns "Not enough HP — this attempt will fail" and asks for confirmation.
- Completing a stage applies its DEF multiplier and bonuses. Max HP jumps to the next stage's base, with a near-empty pool, so a **consolidation refill** follows before the body grows again.
- **Combat interaction:** damage taken in Battle comes out of this pool. During Battle, HP only base-regenerates (10% rate), which slows the drain but rarely outpaces it. After fighting, you **Train** to refill HP at the full rate before the body can grow again. A Routine like *Battle until HP < 30% → Train until HP full → Train 1 h more → repeat* automates this. To push a body breakthrough, stay on Train until the pool is full.

## Body Stages
| # | Stage | BODY_BASE (Tempering work) | Stage time* | Done at (cumulative)* | On completion | Breakthrough materials | Milestone |
|---|---|---|---|---|---|---|---|
| 0 | Mortal Body | — | — | — | Starting state | — | M1 |
| 1 | Copper Skin | 400 | ~1.5 h | ~1.6 h | DEF ×1.4 | Copper Ore ×20, Viper Blood ×3 | M1 |
| 2 | Iron Bone | 12,500 | ~8 h | ~9.5 h | DEF ×1.4 | Iron Ore ×40, Flame Ape Blood ×3 | M1 |
| 3 | Silver Marrow | 300,000 | ~28 h | ~38 h | DEF ×1.4, Tempering +10% (faster HP regen) | Spirit Crystal ×20, Thunder Hawk Blood ×3, Marrow Pill ×1 | M1 |
| 4 | Jade Flesh | 4,700,000 | ~70 h | ~108 h | DEF ×1.4, +10% Physical ATK, Tempering +10% | Ice Jade ×10, Qilin Blood ×1, Wyrm Blood ×2 | M2 |
| 5 | Golden Body | ~80,000,000 | ~150 h | ~260 h | DEF ×1.4, +15% element resist, Tempering +10% | Starsilver ×30, Roc Blood ×3, Salamander Heart ×2 | M2 |
| 6 | Diamond Vajra Body | ~1.5B | ~300 h | ~560 h | DEF ×1.6, +20% tribulation resist, Tempering +10% | Void Stone ×40, Leviathan Blood ×3, Thunder Essence ×10 | M3 |
| 7 | Immortal Body | ~30B | ~600 h | ~1,160 h | DEF ×1.8, all stats +10%, Tempering +20% | Dragon-Vein Jade ×50, Dragon Blood ×3, Phoenix Blood ×3, Kirin Blood ×1 | M3 |

*Hours of **Train** activity, first life, typical bonuses, excluding material farming and the refill after battles. With the 40/30/30 Meditate/Train/Battle split (~3.6 h of training per day), these come to roughly: Copper Skin done in the first session (day ~0.4), Iron Bone by day ~2.5 (fast start), Silver Marrow by day ~11, Jade Flesh by day ~30, Golden Body by day ~72, Diamond Vajra Body by day ~155. Stages 5–7 BODY_BASE values were tuned in [Balancing.xlsx](../Balancing.xlsx).

**Body and the realm ladder:**
- Body Cultivation unlocks at Qi Condensation 1 (about 6 min in).
- **Ascension** from Great Ascension needs **Diamond Vajra Body or higher** ([16-Planes-Ascension](16-Planes-Ascension.md)). The day ~155 Diamond target sits just before the day ~180 first-Ascension target.
- Immortal Body (~1,160 h of training) is mostly reached with rebirth Body multipliers.

- **Max HP** is the pool. Its size per layer is `cap = 0.76 × work` (Vessel Model, [03-Economy](../03-Economy.md)). Each stage starts Max HP at the next stage's base, which is the big HP jump players feel on a stage breakthrough. (The old fixed "HP ×1.6 per stage" is replaced by the cap ladder. Tune the stage bases so the jump still feels about that size.)
- **DEF:** ×1.06 per layer, plus the stage multiplier above.
- **HP regen = Tempering rate** while HP isn't full. The stage bonuses "Tempering +10%" make both regen and growth faster.
- **Design intent:** with a typical split, the body trails the Qi realm by about one step (Copper Skin done during FE, Iron Bone during GC, Silver Marrow during NS, Jade Flesh during SF…). Players who train more than they meditate can flip this.

### Visual per stage
| Stage | Look |
|---|---|
| Copper Skin | Faint bronze sheen on arms |
| Iron Bone | Darker, matte steel tint. Heavier stance |
| Silver Marrow | Silver veins glow faintly when training |
| Jade Flesh | Translucent green-white skin highlight |
| Golden Body | Golden skin glow, gold particles |
| Diamond Vajra Body | Crystalline refraction, rainbow edge light |
| Immortal Body | Soft white radiance, a light silhouette |

## Training Exercises
While the activity is **Train**, one exercise is active. The Karma perk *Second Training Slot* lets two exercises run together while Training: both earn mastery XP, and Tempering uses the faster of the two rates.

| Exercise | Unlock | Tempering rate | Mastery bonus (per level, max 99) | Milestone |
|---|---|---|---|---|
| Stone Lifting | Mortal Body | 1.0× | +1% DEF | M1 |
| Waterfall Endurance | Mortal Body | 1.0× | +1% Max HP | M1 |
| Iron Sand Palm | Copper Skin | 1.1× | +1% Physical ATK | M1 |
| Shadow Footwork | Iron Bone | 1.1× | +0.5 SPD, +0.2% Dodge | M2 |
| Golden Bell Cover | Jade Flesh | 1.2× | +0.5% DEF, +0.5% damage reduction (cap 30%) | M2 |
| Lightning Tempering | Golden Body | 1.3× | +1% lightning resist | M2 |
| Dragon-Elephant Stance | Diamond Vajra Body | 1.4× | +0.5% HP, +0.5% ATK | M3 |

- **Mastery XP** comes from time spent Training on the exercise: 1 XP/s × Muscle Memory bonuses. Uses the life-skill curve `xpToNext(L) = 50 × 1.10^L`.
- Mastery is **kept through rebirth**.
- **Switching** exercise is free and instant. Tempering is stage-wide, not per exercise.
- Every exercise produces Tempering, so every exercise also heals. Mastery XP is earned whether Tempering is refilling HP or growing Max HP.

### Tempering multipliers
| Source | Effect |
|---|---|
| **× Tempering stat on accessories** | Can roll on a **Ring** (one of its 1–3 random stats). Range by rarity: Mortal ×1.03–1.10 · Spirit ×1.08–1.20 · Earth ×1.15–1.35 · Heaven ×1.30–1.60 · Immortal ×1.50–2.00, shifted up by tier and enhancement ([02-Systems §4](../02-Systems.md)) |
| **Training Ground** | ×1.00 (Village Courtyard) up to ×3.80 (×4.50 at Summit of Heaven), and +50% mastery XP for its focus exercise ([15-Cultivation-Grounds](15-Cultivation-Grounds.md)) |
| Exercise rate | ×1.0–1.4 (table above) |
| Baths | ×3–×5 while active |
| Stage bonuses | +10% per stage from Silver Marrow |
| Body multiplier (rebirth) | 1 + Σ stacked body gains (see [12-Rebirth](12-Rebirth.md)) |
| Internal Injury | ×0.8 per stack while active |

## Baths (Tempering boosts)
Brewed by Alchemy (recipes in [07-Alchemy](07-Alchemy.md)). One bath is active at a time. A new bath replaces the old one. Baths multiply Tempering, so they speed up **both** HP refill and Max HP growth. A bath right after a breakthrough shortens the consolidation refill. A bath's timer runs in real time, but it only boosts Tempering while you're **Training**, so start one when you switch to Train.

| Bath | Unlock | Effect | Main ingredients | Milestone |
|---|---|---|---|---|
| Medicinal Bath | Copper Skin | ×3 Tempering, 30 min | Spirit Grass ×5, Fire Lotus ×1 | M1 |
| Purple Cloud Bath | Silver Marrow | ×3 Tempering + ×2 mastery XP, 45 min | Purple Cloud Grass ×5, Spirit Crystal ×1 | M1 |
| Snow Lotus Cold Bath | Jade Flesh | ×4 Tempering, 60 min | Snow Lotus ×4, Ice Jade ×1 | M2 |
| Blood Ginseng Bath | Golden Body | ×4 Tempering + ×2 mastery XP, 60 min | Blood Ginseng ×3, Roc Blood ×1 | M2 |
| Thunder Pool Bath | Diamond Vajra Body | ×5 Tempering, 60 min, Lightning Tempering mastery ×3 | Thunder Essence ×2, Star Orchid ×2 | M3 |

Rewarded ad: +1 free Medicinal Bath (cap 2/day), per [05-Monetization](../05-Monetization.md).

## Beast Blood Bursts
Any boss blood can be **consumed** for instant Tempering instead of being saved for a breakthrough. Like all Tempering, the burst first refills current HP, and any remainder grows Max HP (at 25% efficiency). That makes blood an emergency full-heal as well as a growth boost. Unlike normal Tempering, a blood burst works during **any** activity, including mid-Battle.

```
burst = current Tempering/sec × 20 min × (blood tier ÷ current stage tier), capped at 60 min
```
| Blood | Tier | Burst at matching stage |
|---|---|---|
| Viper Blood | T1 | 20 min of Tempering |
| Flame Ape Blood | T2 | 20 min |
| Thunder Hawk Blood | T3 | 20 min |
| Qilin Blood / Wyrm Blood | T4 | 20 min |
| Roc Blood / Sovereign Blood | T5 | 20 min |
| Leviathan Blood | T6 | 20 min |
| Dragon Blood | T7 | 20 min |
| Phoenix Blood / Kirin Blood | T8 | 20 min |

A higher-tier blood used at a lower stage gives more (up to 60 min). Karma perk *Bloodline Awakening* adds +50%. The UI warns when you try to consume a blood still needed for your next breakthrough.

## Body Multiplier (Rebirth)
- Each rebirth adds a permanent **Tempering multiplier** based on the deepest body stage reached. It **stacks by stage**: every stage passed through adds its full gain (Iron Bone +0.5, Silver Marrow +1, Jade Flesh +2, Golden Body +4 …), and the current stage adds a partial gain. Peak values: Iron Bone +0.5×, Silver Marrow +1.5×, Jade Flesh +3.5×, Golden Body +7.5×. Full table in [03-Economy](../03-Economy.md#rebirth).
- The body stage resets to Mortal Body. Max HP and current HP reset to the starting pool. Injuries are cleared. Exercise mastery is kept.
- Karma perk *Reborn Body* starts new lives with Copper Skin already complete.

## Body ↔ Tribulation & Qi Links
| Link | Effect |
|---|---|
| Completed body stage → Qi breakthrough | +2% success chance per stage |
| Completed body stage → Tribulation | −5% lightning damage per stage |
| Lightning Tempering mastery | +1% lightning resist per level |
| Diamond Vajra Body | +20% tribulation resist |
| Tribulation pre-fight screen | Shows "Body is weak for this tribulation" if the stage is 2+ behind the realm, and "HP not full" if current HP < Max HP |
| Shared HP pool | Tribulations are fought with your **current** HP, so a body breakthrough right before a tribulation (which spends HP) is a trap. Refill first |
| Qi realm breakthrough | Spends Qi, not HP, so the two tracks can be pushed back to back. Their failure injuries are separate (Qi Deviation vs Internal Injury) |

## Decisions
- **Golden Bell Cover:** its 30% damage-reduction cap also applies in tribulations.
- **Blood burst 60-min cap:** keep, and check in the balancing spreadsheet.
- **Switching exercises:** no warm-up penalty.
- **Blood bursts mid-Battle:** allowed.
- After a breakthrough, Routines won't return to Battle until HP is back at the resume point (default 100%). Max HP % bonuses scale the whole ladder (cap, max, and spend).
