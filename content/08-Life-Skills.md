# 08 — Life Skills

Covers **Mining, Woodcutting, Fishing** (gathering) and **Cooking, Forging** (processing). Alchemy is in [07-Alchemy](07-Alchemy.md). Farming is in [10-Spirit-Fields](10-Spirit-Fields.md).

---

## Shared Framework

### Levels & XP
- Levels **1–99** per skill. `xpToNext(L) = 50 × 1.10^L`.
- Cumulative XP: Lvl 15 ≈ 1,600 · Lvl 25 ≈ 4,400 · Lvl 50 ≈ 58,000 · Lvl 75 ≈ 630,000 · Lvl 99 ≈ 6.3M.
- XP per second rises with each tier of node or recipe, so moving to new content always feels faster.
- **Target: ~120–150 h of one slot's time from Lvl 1 to 99** (about 13 XP/s on average). Top-tier nodes and recipes give enough XP that 75 → 99 takes roughly 60 h, not the ~260 h a flat curve would give. Exact per-node XP is set in the balancing spreadsheet.

### Worker slots
| Source | Slots |
|---|---|
| Start | 1 |
| FE 1 | +1 (2) |
| NS 1 | +1 (3) |
| MA 1 | +1 (4) |
| IAP "Immortal Cave" | +1 |
| Karma perk (see [12-Rebirth](12-Rebirth.md)) | +1 |

- Each slot runs **one job continuously**: a gathering node, or a processing recipe repeated until its ingredients run out.
- Farming (Spirit Fields) and body Training don't use worker slots.

### Job queue
- Each slot has a queue of up to **3 jobs** (M1: 1 job, no queue). A Karma perk raises it to **5** (not sold as IAP). Example: "Craft 20 Foundation Pills → then mine Iron Ore forever."
- A processing job ends when ingredients run out or the target count is reached, then the next queued job starts. If the queue is empty, the slot goes idle and a local notification fires ("Your alchemist is idle").
- Gathering jobs have no end unless a target count is set.

### Gathering focus
- Each gathering job has a **Focus** toggle: **Main yield** (default) or **Rare yield** (for example, pearls instead of fish, crystals instead of ore). Rare focus gives ×2 rare-drop chance at −40% main yield.
- **Cooking is fuel-free.** Only Alchemy uses (optional) wood fuel.

### Offline
Jobs run at **100% efficiency** offline, within the offline cap (8 h, or 12 h with IAP). The simulation is the same as online, done in bulk.

### Tools
Gathering speed tools, forged by Forging (see the Forging section). Each tier: **−8% action time** (cumulative over the tier ladder, not stacking between tools).

| Tool tier | Forging lvl | Pickaxe / Axe / Rod recipe |
|---|---|---|
| Copper (starter, gifted) | — | — |
| Iron | 15 | Iron Ore ×20, Ironwood ×10 |
| Spirit Crystal | 30 | Spirit Crystal ×20, Phoenix Parasol Wood ×10 |
| Ice Jade | 45 | Ice Jade ×20, Moon Cassia Wood ×10 |
| Starsilver | 60 | Starsilver ×20, Thunderstruck Peach Wood ×10 |
| Void Stone | 75 | Void Stone ×20, Void Willow ×10 |
| Dragon-Vein Jade | 90 | Dragon-Vein Jade ×20, World Tree Branch ×10 |

Tools never gate a node. They only speed it up.

---

## Mining
**Unlock:** MO 1. **Milestone:** M1.

| Lvl | Node | Action time | XP | Yield | Rare drop (chance) |
|---|---|---|---|---|---|
| 1 | Copper Vein | 10 s | 8 | Copper Ore ×1 | Spirit Stones ×5 (2%) |
| 15 | Iron Vein | 15 s | 20 | Iron Ore ×1 | Spirit Stones ×20 (2%) |
| 25 | Spirit Crystal Vein | 20 s | 35 | Spirit Crystal ×1 | Refining Stone (1%) |
| 40 | Thunder Rock | 30 s | 75 | Thunder Crystal ×1 | Refining Stone (1.5%) |
| 50 | Glacial Vein | 35 s | 120 | Ice Jade ×1 | Refining Stone (2%) |
| 60 | Starsilver Lode | 45 s | 220 | Starsilver ×1 | Dao Pattern Stone (0.2%) |
| 75 | Void Fissure | 60 s | 420 | Void Stone ×1 | Dao Pattern Stone (0.3%) |
| 90 | Dragon Vein | 75 s | 750 | Dragon-Vein Jade ×1 | Dao Pattern Stone (0.5%) |

| Mastery | Perk |
|---|---|
| 25 | 10% chance of double ore |
| 50 | 1% chance per action for bonus Spirit Stones (10× the node's rare drop) |
| 75 | −15% action time |
| 99 | Title **Earth Vein Master**, +1 ore per action |

## Woodcutting
**Unlock:** FE 1. **Milestone:** M2. (In M1, Spirit Wood isn't needed, since alchemy fuel is optional.)

| Lvl | Tree | Action time | XP | Yield | Rare drop (chance) |
|---|---|---|---|---|---|
| 1 | Spirit Pine | 10 s | 8 | Spirit Wood ×1 | Spirit Grass ×2 (3%) |
| 15 | Ironwood Tree | 15 s | 20 | Ironwood ×1 | Spirit Rice ×2 (3%) |
| 30 | Phoenix Parasol Tree | 22 s | 45 | Phoenix Parasol Wood ×1 | Fire Lotus ×1 (2%) |
| 45 | Moon Cassia Tree | 30 s | 100 | Moon Cassia Wood ×1 | Snow Lotus ×1 (1.5%) |
| 60 | Thunderstruck Peach Tree | 45 s | 220 | Thunderstruck Peach Wood ×1 | Thunder Essence ×1 (0.5%) |
| 75 | Void Willow | 60 s | 420 | Void Willow ×1 | Star Orchid ×1 (0.5%) |
| 90 | World Tree Sapling | 75 s | 750 | World Tree Branch ×1 | Nine-Leaf Immortal Grass ×1 (0.2%) |

| Mastery | Perk |
|---|---|
| 25 | 10% chance of double logs |
| 50 | **Seasoned Wood:** wood you cut gives +1% extra success when burned as alchemy fuel |
| 75 | −15% action time |
| 99 | Title **Forest Sage**, +1 log per action |

## Fishing
**Unlock:** GC 1. **Milestone:** M2.

| Lvl | Spot | Action time | XP | Catch | Rare catch |
|---|---|---|---|---|---|
| 1 | Village Pond | 12 s | 10 | Silver Carp ×1 | Spirit Pearl (1%) |
| 15 | Misty River | 18 s | 25 | Spirit Eel ×1 | Spirit Pearl (2%) |
| 30 | Jade Lake | 25 s | 55 | Jade Koi ×1 | Moon Pearl (1.5%) |
| 45 | Magma Pool | 32 s | 110 | Lava Crab ×1 | Moon Pearl (2.5%) |
| 60 | Starfall Bay | 45 s | 230 | Star Shrimp ×1 | Star Pearl (1.5%) |
| 75 | Void Abyss Pool | 60 s | 430 | Void Angler ×1 | Star Pearl (2.5%) |
| 90 | Dragon Gate Falls | 75 s | 760 | Dragon Carp ×1 | Dragon Pearl (1%) |

| Mastery | Perk |
|---|---|
| 25 | +50% pearl chance |
| 50 | 10% chance of a double catch |
| 75 | −15% action time |
| 99 | Title **Dragon Gate Angler**, pearl chance ×2 |

---

## Cooking
**Unlock:** GC 1. **Milestone:** M2.

- Produces **meals** (timed buffs, **one meal active at a time**) and **pet food**.
- **Burn chance:** 20% at recipe level, −1% per level above it, 0% at +20 levels. Burnt food gives 50% XP.
- Meal buffs stack with pills (different buff category).

### Meals
| Lvl | Meal | Ingredients | Cook time | XP | Buff |
|---|---|---|---|---|---|
| 1 | Grilled Silver Carp | Silver Carp ×2 | 15 s | 12 | +10% Max HP, 1 h |
| 5 | Spirit Rice Porridge | Spirit Rice ×3 | 20 s | 18 | +5% Qi rate, 2 h |
| 15 | Eel Soup | Spirit Eel ×2, Spirit Grass ×2 | 30 s | 35 | +15% ATK, 1 h |
| 20 | Fire Lotus Tea | Fire Lotus ×1, Spirit Grass ×2 | 30 s | 45 | +10% gathering speed, 2 h |
| 30 | Steamed Jade Koi | Jade Koi ×2, Spirit Rice ×2 | 45 s | 80 | +20% DEF, 2 h |
| 45 | Lava Crab Hotpot | Lava Crab ×2, Fire Lotus ×2 | 1 min | 150 | +20% ATK, +10% Fire damage, 2 h |
| 60 | Star Shrimp Dumplings | Star Shrimp ×3, Spirit Rice ×3 | 1.5 min | 320 | +15% all stats, 2 h |
| 75 | Void Angler Sashimi | Void Angler ×2, Snow Lotus ×1 | 2 min | 600 | +25% Crit Dmg, +10% SPD, 3 h |
| 90 | Dragon Carp Feast | Dragon Carp ×1, Blood Ginseng ×2, Spirit Rice ×5 | 3 min | 1,100 | +25% all stats, +10% Qi rate, 4 h |

### Pet food
| Lvl | Food | Ingredients | Cook time | XP | Pet XP |
|---|---|---|---|---|---|
| 1 | Beast Chow | Beast Core (T1) ×2, Silver Carp ×1 | 15 s | 10 | 100 |
| 30 | Spirit Beast Feast | Beast Core (T3) ×2, Jade Koi ×1 | 45 s | 80 | 1,000 |
| 60 | Star-Grade Beast Feast | Beast Core (T5) ×2, Star Shrimp ×1 | 1.5 min | 320 | 8,000 |
| 75 | Dragon-Grade Beast Feast | Beast Core (T6) ×2, Void Angler ×1 | 2 min | 600 | 20,000 |

| Mastery | Perk |
|---|---|
| 25 | 10% chance to cook 2 |
| 50 | Meal duration +25% |
| 75 | −20% cook time |
| 99 | Title **Imperial Chef**, meals +10% effect |

---

## Forging
**Unlock:** FE 1. **Milestone:** M1 (T1–T3), M2 (T4–T6), M3 (T7–T9).

Forging covers **crafting gear and tools**, **enhancing**, **reforging**, and **salvage**. The enhance, reforge, and salvage rules (costs, odds) live in [05-Equipment](05-Equipment.md). Forging only defines the XP they give and the level they require.

### Gear recipes (per tier)
Item level = tier. Every recipe also costs Spirit Stones (scaling by tier).

| Tier | Forging lvl | Ore | Wood | Other |
|---|---|---|---|---|
| T1 | 1 | Copper Ore | Spirit Wood | Beast Core (T1) |
| T2 | 15 | Iron Ore | Ironwood | Beast Core (T2) |
| T3 | 30 | Spirit Crystal / Thunder Crystal (weapons) | Phoenix Parasol Wood | Beast Core (T3) |
| T4 | 45 | Ice Jade | Moon Cassia Wood | Beast Core (T4) |
| T5 | 55 | Starsilver | Thunderstruck Peach Wood | Beast Core (T5) |
| T6 | 65 | Void Stone | Void Willow | Beast Core (T6) |
| T7 | 75 | Dragon-Vein Jade | World Tree Branch | Beast Core (T7) |
| T8 | 85 | Dragon-Vein Jade | World Tree Branch | Beast Core (T8), Celestial Feather |
| T9 | 95 | Dragon-Vein Jade | World Tree Branch | Beast Core (T9), Chaos Essence |

### Slot recipe shapes (quantities at T1, scale ×1.5 per tier)
| Slot | Shape |
|---|---|
| Sword: **Jian** | Ore ×10, Wood ×4, Beast Core ×3 |
| Sword: **Saber** | Ore ×12, Wood ×2, Beast Core ×3 |
| Sword: **Greatsword** | Ore ×16, Wood ×4, Beast Core ×4, **1 boss material** for that tier (T1 Viper Fang ×2 · T2 Flame Ape Blood · T3 Thunder Hawk Blood · T4 Wyrm Blood · T5 Salamander Heart · T6 Void Core · T7 Dragon Blood · T8 Kirin Blood · T9 Dao Fragment) |
| Robe | Beast Core ×6, Ore ×2, **1 boss signature drop of that tier** (any) |
| Bracers | Ore ×6, Beast Core ×3 |
| Boots | Ore ×4, Wood ×4, Beast Core ×3 |
| Talisman | Wood ×6, Ore ×2, Pearl ×1 (Spirit Pearl T1–T2, Moon Pearl T3–T4, Star Pearl T5–T6, Dragon Pearl T7+) |
| Ring | Ore ×6, Pearl ×1 |
| Pendant | Ore ×3, Beast Core ×2, Pearl ×1 |

Until Fishing unlocks (GC 1), Talismans, Rings, and Pendants at T1–T2 use Spirit Stones in place of pearls.

- **Swords:** only **Jian, Saber, and Greatsword** can be forged. Twin Swords (boss drops), Flying Swords (dungeon drops), and legendary swords can't be crafted. Names per tier are in [05-Equipment](05-Equipment.md#swords). A crafted sword rolls its × Damage within its rarity's range.
- **Accessories** roll 1–3 random stats from their slot pool when crafted, like drops ([05-Equipment](05-Equipment.md#accessories)).
- T8–T9 Jian and Saber also need that tier's extra material from the recipe table (Celestial Feather / Chaos Essence). Sword names reference other boss materials only for flavor.

### Craft time & XP
| Tier | Craft time | XP per craft |
|---|---|---|
| T1 | 30 s | 20 |
| T2 | 1 min | 60 |
| T3 | 2 min | 180 |
| T4 | 4 min | 500 |
| T5 | 6 min | 1,200 |
| T6 | 10 min | 3,000 |
| T7 | 15 min | 7,000 |
| T8 | 20 min | 15,000 |
| T9 | 30 min | 35,000 |

### Crafted rarity odds
| Rarity | Base odds | Per Forging level above recipe |
|---|---|---|
| Mortal | 50% | −1% |
| Spirit | 35% | +0.5% |
| Earth | 13% | +0.35% |
| Heaven | 2% | +0.15% |
| Immortal | Not craftable (D8 and bosses only) | — |

Other XP: enhancing gives 10 × item tier, reforging gives 50 × item tier, salvaging gives 2 × item tier.

| Mastery | Perk |
|---|---|
| 25 | +5% chance to upgrade a crafted item's rarity by one step |
| 50 | Salvage returns +25% |
| 75 | −20% enhancement Spirit Stone cost |
| 99 | Title **Divine Smith**, 10% chance for crafted gear to roll +1 affix |

---

## Decisions
- Job queue grows from 3 to **5 via a Karma perk** only.
- Cooking stays **fuel-free**.
- Level 99 target: **~120–150 h** per skill (tune XP in the spreadsheet).
- Gathering nodes get a **Focus** toggle (main vs rare yield).
