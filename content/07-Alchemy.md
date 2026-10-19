# 07 — Alchemy

Alchemy turns herbs, ores, and monster materials into **pills** (cultivation, breakthroughs, combat, pets) and **Medicinal Baths** (body). It runs as a **worker-slot job**, like the other processing skills (see [08-Life-Skills](08-Life-Skills.md)), and continues offline.

- **Unlock:** QC 5. The first big recipe is the Foundation Pill (needed for the QS → FE gate). **Milestone:** M1 (pills up to the GC→NS gate), M2 (to the SF→VB gate), M3 (the rest).
- **Skill:** levels 1–99, XP curve `xpToNext(L) = 50 × 1.10^L` (shared with all life skills).

---

## Mechanics

### Success rate
```
success = recipe base % + 1% × (Alchemy lvl − recipe lvl) + furnace bonus + fuel bonus
cap: 95% (100% for pills of Mid quality or lower at 30+ levels over the recipe)
```
- **Failure** consumes the ingredients and grants 50% XP, plus **Pill Residue** (1 per failed pill, ×2 for gate pills). Rare boss drops are always returned on failure.
- **Pill Residue** is a by-product used as **Spirit Field fertilizer** ([10-Spirit-Fields](10-Spirit-Fields.md)), so failures still feed another system.

### Pill quality
Each successful craft rolls a quality grade:

| Grade | Effect multiplier | Base odds | Gate-pill bonus to breakthrough chance |
|---|---|---|---|
| Low | ×0.8 | 30% | +0% |
| Mid | ×1.0 | 50% | +5% |
| High | ×1.2 | 17% | +10% |
| Perfect | ×1.5 (gold "pill cloud" effect) | 3% | +15% |

- Each Alchemy level above the recipe shifts 1% from Low toward High/Perfect (Perfect is capped at 20%).
- The furnace and fuel shift odds further (see below).
- Pills of different grades stack separately in the inventory.

### Furnaces (permanent upgrades)
| Furnace | Alchemy lvl | Cost | Success | Quality shift | Craft time | Batch |
|---|---|---|---|---|---|---|
| Clay Furnace | 1 | Starter | +0% | — | ×1.0 | 1 |
| Bronze Furnace | 15 | 5,000 Spirit Stones, Copper Ore ×50, Iron Ore ×20 | +5% | +2% | ×0.9 | 1 |
| Spirit Furnace | 35 | 300,000 SS, Spirit Crystal ×30, Thunder Crystal ×10 | +8% | +4% | ×0.8 | 2 |
| Earth-Fire Furnace | 55 | 20M SS, Starsilver ×50, Salamander Heart ×1 | +10% | +6% | ×0.7 | 3 |
| Heavenly Cauldron | 80 | 2B SS, Dragon-Vein Jade ×50, Phoenix Blood ×1 | +12% | +8% | ×0.6 | 5 |

"Batch" = pills produced per craft from one set of ingredients × batch. The player can choose a batch size of 1 up to the furnace maximum.

### Fuel (optional)
- Fuel is **never required**, so Alchemy works before Woodcutting unlocks.
- Adding fuel for a craft costs 3 wood. The wood's tier gives a bonus: **+2% success and +1% quality shift per wood tier, up to the recipe's tier**. (For example, Ironwood (T2) on a T3 recipe gives +4% / +2%.)
- Auto-fuel toggle: keep using the best wood in stock.

### Pill rules
- **One Qi buff pill** is active at a time. A stronger one replaces a weaker one; the same one extends its duration.
- **Breakthrough-chance pills:** up to **2** can be used per attempt (the gate pill doesn't count toward this limit).
- Combat pills auto-use when their condition triggers (for example, Healing Pill below 40% HP). The player picks which pills are in the "pill pouch" (3 slots).
- **Vessel Model ([02-Systems §0](../02-Systems.md)):** HP and Qi are shared pools for combat, training, and breakthroughs. **Restoration pills refill the real pool**, in or out of combat. They're the main way to skip a refill and get back to growing, and to **top up before a breakthrough** (which needs 80% of the cap, or 100% at a gate). Pills never raise Max HP or Max Qi directly; only growth does.

### XP
XP per craft is listed per recipe. Failure gives 50%. Batch crafts give XP × batch size.

### Mastery perks
| Lvl | Perk |
|---|---|
| 25 | +5% quality shift on all recipes |
| 50 | 10% chance to produce +1 extra pill |
| 75 | −20% craft time |
| 99 | Title **Pill Sage**, +3% Perfect odds, cosmetic furnace flame |

---

## Realm Gate Pills
All ingredients are obtainable **before** the gate they unlock (realm ranges per [00-Registry](00-Registry.md)). The two tutorial gates (MO → QC, QC → QS) need no pill.

| Pill | Gate | Ingredients | Alch lvl | Craft time | Base success | XP |
|---|---|---|---|---|---|---|
| Foundation Pill | QS → FE | Spirit Grass ×10, Copper Ore ×5, Viper Fang ×2 | 5 | 5 min | 70% | 60 |
| Golden Core Pill | FE → GC | Spirit Grass ×20, Fire Lotus ×5, Spirit Crystal ×3, Serpent Scale ×1 | 20 | 20 min | 60% | 400 |
| Nascent Pill | GC → NS | Purple Cloud Grass ×10, Thunder Crystal ×3, Frost Qilin Horn ×1 | 35 | 40 min | 55% | 1,500 |
| Soul Nurturing Pill | NS → SF | Snow Lotus ×5, Soul Lotus ×1, Wyrm Blood ×2, Yin Soul Jade ×1 | 50 | 1 h | 50% | 5,000 |
| Void Pill | SF → VB | Blood Ginseng ×5, Starsilver ×5, Roc Feather ×2, Salamander Heart ×1 | 60 | 2 h | 45% | 12,000 |
| Mahayana Pill | VB → MA | Star Orchid ×5, Void Stone ×5, Void Core ×2, Leviathan Blood ×1 | 70 | 3 h | 40% | 30,000 |
| Great Ascension Pill | MA → GA | Dragon-Vein Jade ×3, Sword Intent Shard ×3, Treant Heartwood ×2, Dragon Blood ×1 | 85 | 5 h | 33% | 100,000 |
| Ascension Pill | GA peak → Ascension (Immortal Plane) | Nine-Leaf Immortal Grass ×9, Chaos Essence ×5, Dao Fragment ×3, General's Seal ×1, Dragon Pearl ×1 | 95 | 12 h | 25% | 400,000 |

- **Tutorial safety net:** the first Foundation Pill attempt is guaranteed to succeed (Mid quality), so new players can't get stuck at the first gate. As a second net, the main quest **gifts one Foundation Pill** when you reach Qi Sea 9 ([11-Quests-Achievements](11-Quests-Achievements.md)).
- The NS → SF gate also needs **Soul Lotus ×3** as a raw item, on top of the pill (per the registry).
- **Ingredient sources, checked against the new map ranges:**
  - Foundation Pill: Viper Fang from map 1 (MO 5 – QC 9).
  - Golden Core Pill: Serpent Scale from map 3, Fire Lotus from map 4 (both FE).
  - Nascent Pill: Thunder Crystal and Purple Cloud Grass from maps 6–7, Frost Qilin Horn from map 8 (GC 8 – NS 2).
  - Mahayana Pill: Void Core and Leviathan Blood from maps 15–16 (VB).
  - Great Ascension Pill: Sword Intent Shard, Treant Heartwood, and Dragon Blood from maps 18–20 (MA; map 20 starts at MA 7).
  - Ascension Pill: General's Seal, Chaos Essence, and Dao Fragment from maps 24–26 (GA 5–9).
- **Removed with the realm ladder change:** Body Integration Pill (its recipe is now the Mahayana Pill) and Tribulation Pill (Great Ascension takes its place).

## Breakthrough & Tribulation Pills
| Pill | Ingredients | Alch lvl | Craft time | Base success | Effect | XP |
|---|---|---|---|---|---|---|
| Clear Mind Pill | Spirit Grass ×5, Serpent Scale ×1 | 12 | 3 min | 75% | +5% Qi breakthrough chance | 120 |
| Heart-Calming Pill | Purple Cloud Grass ×3, Spirit Crystal ×2 | 28 | 10 min | 65% | +10% breakthrough chance | 700 |
| Insight Pill | Ice Jade ×1, Purple Cloud Grass ×3 | 40 | 15 min | 60% | +15% breakthrough chance | 2,000 |
| Dao Heart Pill | Star Orchid ×2, Yin Soul Jade ×1, Spirit Pearl ×2 | 65 | 1 h | 50% | +20% breakthrough chance | 18,000 |
| Lightning Ward Pill | Thunder Crystal ×2, Snow Lotus ×2 | 38 | 20 min | 60% | −20% lightning damage in the next tribulation | 1,800 |
| Heart Demon Ward Pill | Blood Ginseng ×2, Yin Soul Jade ×1 | 58 | 45 min | 50% | Heart Demon Trial (Tribulation IV) enemies −25% HP | 9,000 |

## Qi Buff Pills (one active at a time)
| Pill | Ingredients | Alch lvl | Craft time | Base success | Effect | XP |
|---|---|---|---|---|---|---|
| Qi Gathering Pill | Spirit Grass ×3 | 1 | 30 s | 90% | +50% Qi rate, 30 min | 15 |
| Greater Qi Gathering Pill | Spirit Grass ×5, Fire Lotus ×2 | 22 | 5 min | 75% | +75% Qi rate, 1 h | 450 |
| Profound Qi Pill | Snow Lotus ×2, Ice Jade ×1 | 45 | 15 min | 65% | +100% Qi rate, 1 h | 3,000 |
| Heaven-Earth Qi Pill | Star Orchid ×1, Blood Ginseng ×2 | 70 | 30 min | 55% | +150% Qi rate, 2 h | 25,000 |
| Immortal Qi Pill | Nine-Leaf Immortal Grass ×1, Star Pearl ×2 | 90 | 1 h | 45% | +200% Qi rate, 2 h | 120,000 |

## Combat Pills (pill pouch, auto-use)
| Pill | Ingredients | Alch lvl | Craft time | Base success | Effect | XP |
|---|---|---|---|---|---|---|
| Healing Pill | Spirit Grass ×2 | 5 | 1 min | 85% | Restore 30% Max HP (auto below 40% HP, or tap anytime) | 30 |
| Strength Pill | Fire Lotus ×2, Iron Ore ×2 | 15 | 4 min | 75% | +15% ATK, 1 h | 250 |
| Iron Skin Pill | Iron Ore ×3, Spirit Rice ×3 | 18 | 4 min | 75% | +15% DEF, 1 h | 300 |
| Swift Wind Pill | Serpent Scale ×1, Spirit Grass ×4 | 20 | 5 min | 70% | +10% SPD, 1 h | 380 |
| Qi Recovery Pill | Spirit Crystal ×1, Purple Cloud Grass ×2 | 30 | 8 min | 65% | Restore 50% Max Qi (auto below 30% Qi, or tap anytime) | 900 |
| Greater Healing Pill | Snow Lotus ×1, Purple Cloud Grass ×2 | 42 | 10 min | 65% | Restore 60% Max HP (auto below 40% HP, or tap anytime) | 2,400 |
| Five Elements Ward Pill | Fire Lotus ×2, Snow Lotus ×2, Thunder Crystal ×1 | 48 | 20 min | 60% | +20% all element resist, 1 h | 4,500 |
| Berserker Blood Pill | Wyrm Blood ×1, Blood Ginseng ×1 | 62 | 30 min | 55% | +30% ATK, −10% DEF, 1 h | 14,000 |
| Revival Pill | Phoenix Blood ×1, Nine-Leaf Immortal Grass ×1 | 88 | 2 h | 40% | Revive once at 50% HP (per fight) | 100,000 |

## Restoration & Injury Pills (Vessel Model)
Usable anytime: in battle, during a Train or Meditate step, or right before a breakthrough. In battle they are the main heal besides healer pets. Base regen (10% of the Meditate/Train rate) is too slow to rely on. Can sit in the pill pouch for auto-use. Restores are capped at Max.

| Pill | Ingredients | Alch lvl | Craft time | Base success | Effect | XP |
|---|---|---|---|---|---|---|
| Minor Qi Recovery Pill | Spirit Grass ×2, Copper Ore ×1 | 3 | 45 s | 90% | Restore 25% Max Qi | 20 |
| Healing Pill | *(see Combat Pills)* | 5 | | | Restore 30% Max HP | |
| **Meridian Mending Pill** | Spirit Grass ×4, Spirit Rice ×2 | 12 | 3 min | 80% | **Cures Qi Deviation and Internal Injury: clears all stacks at once** (each stack lasts 5 min, unlimited stacks; [02-Systems §1b](../02-Systems.md)) | 150 |
| Qi Recovery Pill | *(see Combat Pills)* | 30 | | | Restore 50% Max Qi | |
| Greater Healing Pill | *(see Combat Pills)* | 42 | | | Restore 60% Max HP | |
| Greater Qi Recovery Pill | Soul Lotus ×1, Ice Jade ×1 | 55 | 15 min | 60% | Restore 75% Max Qi | 6,000 |
| Supreme Healing Pill | Blood Ginseng ×3, Roc Feather ×1 | 66 | 30 min | 55% | Restore 100% Max HP | 18,000 |
| Supreme Qi Recovery Pill | Star Orchid ×1, Starsilver ×2 | 80 | 45 min | 50% | Restore 100% Max Qi | 60,000 |

- **Tier coverage:** MO–QS (Minor Qi, Healing, Mending) → GC (Qi Recovery) → NS (Greater Healing) → SF (Greater Qi) → VB+ (Supreme). Higher realms rely on the % values, so old pills stay useful at reduced convenience.
- **Milestone:** Minor Qi Recovery, Healing, and Meridian Mending in M0/M1 (they're needed for the core Vessel loop). Others follow their tier.
- Rewarded ad option (if wanted): "Instant full recovery" once per day. See Open Questions.

## Body Cultivation Pills & Medicinal Baths
| Item | Ingredients | Alch lvl | Craft time | Base success | Effect | XP |
|---|---|---|---|---|---|---|
| Medicinal Bath | Spirit Grass ×5, Fire Lotus ×1 | 8 | 2 min | 85% | ×3 Tempering, 30 min | 80 |
| Purple Cloud Bath | Purple Cloud Grass ×5, Spirit Crystal ×1 | 26 | 8 min | 75% | ×3 Tempering + ×2 mastery XP, 45 min | 650 |
| Snow Lotus Cold Bath | Snow Lotus ×4, Ice Jade ×1 | 46 | 20 min | 65% | ×4 Tempering, 60 min | 3,500 |
| Blood Ginseng Bath | Blood Ginseng ×3, Roc Blood ×1 | 64 | 40 min | 55% | ×4 Tempering + ×2 mastery XP, 60 min | 16,000 |
| Thunder Pool Bath | Thunder Essence ×2, Star Orchid ×2 | 82 | 1 h | 45% | ×5 Tempering + Lightning Tempering mastery ×3, 60 min | 80,000 |
| Marrow Pill | Spirit Crystal ×2, Purple Cloud Grass ×3 | 25 | 10 min | 70% | Required for the Silver Marrow body breakthrough | 600 |

Only one bath can be active at a time. Bath names, unlocks, and effects match [02-Body](02-Body.md). The Marrow Pill is the only body-breakthrough pill. All other body stages are gated by raw materials.

## Pet Pills
| Pill | Ingredients | Alch lvl | Craft time | Base success | Effect | XP |
|---|---|---|---|---|---|---|
| Beast Taming Pill | Beast Core (T4) ×5, Snow Lotus ×1 | 45 | 15 min | 65% | +5% capture chance on the next boss kill | 3,000 |
| Beast Growth Pill | Beast Core (T3) ×3, Spirit Rice ×5 | 32 | 5 min | 70% | +2,000 pet XP | 1,000 |
| Greater Beast Growth Pill | Beast Core (T6) ×3, Blood Ginseng ×1 | 66 | 20 min | 55% | +30,000 pet XP | 15,000 |

Pet evolution requirements are defined in [09-Pets](09-Pets.md).

---

## Decisions
- **No pill toxicity meter.** The "one Qi pill at a time" and "2 chance pills per attempt" rules are enough.
- Failure gives **Pill Residue** (Spirit Field fertilizer) instead of an ingredient refund.
- One Foundation Pill is **gifted by the main quest** at Qi Sea 9, on top of the guaranteed first craft.
- The Ascension Pill needs **Alchemy 95** (was 99).
- No rewarded ad for instant full HP/Qi recovery. Restoration pills keep that role.
