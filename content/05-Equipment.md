# 05 — Equipment

Names, tiers, and materials follow [00-Registry](00-Registry.md). Stats feed the formulas in [03-Economy](../03-Economy.md#stats).

## Slots
| Slot | Main stat | Secondary (fixed) | Affix restrictions |
|---|---|---|---|
| **Sword** (weapon) | **× Damage** multiplier | Type trait | Gear affix pool |
| Robe | HP | DEF | — |
| Bracers | ATK | Crit % | — |
| Boots | SPD | Dodge % | — |
| **Talisman** (accessory) | **None** (1–3 random stats) | — | Talisman pool only |
| **Ring** (accessory) | **None** (1–3 random stats) | — | Ring pool only |
| **Pendant** (accessory) | **None** (1–3 random stats) | — | Pendant pool only |

- **7 slots:** the Sword, 3 armor pieces (Robe, Bracers, Boots), and 3 **accessories**.
- The **Sword** multiplies all damage dealt (see [Swords](#swords)).
- Armor gives flat combat stats and random affixes.
- Accessories have no main stat. Each one rolls 1–3 random stats from its slot's pool (see [Accessories](#accessories)).
- Flat ATK now comes from Qi levels and Bracers. The sword is a multiplier on top.
- **Milestone:** all 7 slots in M1.

## Swords
Every weapon is a sword ([02-Systems §4](../02-Systems.md)). Main stat: **× Damage** (all damage dealt, including combat arts), rolled from the rarity range, plus **+0.05 per tier above T1**.

| Rarity | × Damage (T1) | Typical sources |
|---|---|---|
| Mortal | ×1.05–1.15 | Sword Pavilion, Forging |
| Spirit | ×1.15–1.30 | Sword Pavilion (rotating), Forging, map monsters |
| Earth | ×1.30–1.50 | Forging (high level), map bosses, dungeons |
| Heaven | ×1.50–1.80 | Dungeon bosses, Sect shop, rare map-boss drops |
| Immortal | ×1.80–2.50 | D8, named legendaries, events |

### Types
| Type | Trait | Craftable? | Main sources |
|---|---|---|---|
| **Jian** (balanced) | +1 affix slot (max 5) | Yes | Sword Pavilion, Forging, map monsters |
| **Saber (Dao)** | +20% Crit Dmg (+5% per tier) | Yes | Forging, map monsters |
| **Greatsword** | +15% Damage, −10% SPD | Yes (needs a boss material) | Forging only |
| **Twin Swords** | 25% chance of an extra hit for 50% damage, +5% SPD | No | **Map bosses** (each boss has its own pair) |
| **Flying Sword** | Each hit adds 2% of Max Qi as bonus damage. The *Flying Sword* combat art deals +30% | No | **Dungeons** (D2 especially, also D5, D7, D8) |
| **Legendary** (named) | Unique effect (see below) | No | Specific bosses (rare), tribulation first clears, events |

### Sword list by tier
| Tier | Jian | Saber | Greatsword (forge material) | Twin Swords (boss) | Flying Sword (dungeon) |
|---|---|---|---|---|---|
| T1 | Iron Jian | Bamboo-Cutter Saber | Copper Greatsword (Viper Fang ×2) | Viper Twin Fangs (Bamboo Viper King) | — |
| T1–T2 | — | — | — | Bandit Twin Hooks (Bandit Chief Zhao) | — |
| T2 | Spirit Steel Jian | Moonlit Saber | Ember Greatsword (Flame Ape Blood ×1) | Serpent Twin Blades (Lake Serpent) | — |
| T3 | Thunder Crystal Jian | Frostbite Saber | Thunder Hawk Greatsword (Thunder Hawk Blood ×1) | Toad-Venom Twins (Thousand-Year Toad) | Sword Saint's Flying Sword (D2 I–II) |
| T4 | Ice Jade Jian | Desert Wind Saber | Wyrm-Bone Greatsword (Wyrm Blood ×1) | Kraken Twin Fangs (Kraken Matriarch) | Ghost-Light Flying Sword (D2 III) |
| T5 | Starsilver Jian | Roc-Wing Saber | Salamander Greatsword (Salamander Heart ×1) | Sovereign Twin Blades (Ancient Ape Sovereign) | Starfall Flying Sword (D2 IV) |
| T6 | Void Stone Jian | Starsea Saber | Void Golem Greatsword (Void Core ×1) | Leviathan Twin Fins (Star-Eater Leviathan) | Void Weaver's Needle (D5) |
| T7 | Dragon-Vein Jian | Abyss Tide Saber | Abyss Dragon Greatsword (Dragon Blood ×1) | Sword Wraith Twin Edges (Sword Wraith Emperor) | Ascendant Flying Sword (D2 V) |
| T8 | Celestial Jian (Celestial Feather ×1) | Phoenix Flame Saber (Phoenix Blood ×1) | Kirin Thunder Greatsword (Kirin Blood ×1) | Phoenix Twin Wings (Vermilion Phoenix) | Tribulation Thunder Flying Sword (D7) |
| T9 | Heavenly General Jian (General's Seal ×1) | Chaos Saber (Chaos Essence ×1) | Heaven's Gate Greatsword (Dao Fragment ×1) | Taotie Twin Maws (Taotie the Devourer) | Immortal Ancestor Flying Sword (D8) |

- Craftable recipes (ore, wood, Beast Core, boss material) are in [08-Life-Skills](08-Life-Skills.md#forging).
- **Twin Swords:** 15% of a boss's gear drops are its Twin Swords, at any rarity (boss weights apply).
- **Flying Swords:** 20% of the weapon drops in the listed dungeon tiers.
- Map monsters drop Jian and Saber of the map's tier.

### Legendary swords
Always **Immortal** rarity, at the tier of their source. Each source has a **pity counter** (guaranteed at the listed kill count).

| Sword | Tier | Source | Drop / pity | Unique effect | Milestone |
|---|---|---|---|---|---|
| Thunder Hawk's Talon | T3 | Thunder Hawk (Map 6) | 0.3% / 400 kills | Crits chain lightning to 2 more enemies for 60% damage | M1 |
| Frost Qilin Horn Blade | T3 | Frost Qilin (Map 8) | 0.3% / 400 | Hits have a 10% chance to Freeze. +20% damage to frozen enemies | M1 |
| Sword Saint's Last Intent | T3–T7 (scales with D2 tier) | Sword Saint's Shade (D2) | 0.5% per clear / 150 clears | Every combat art cast also fires a sword strike for 100% ATK | M2 |
| Thunder-Tempered Blade | T5 | First clear of Tribulation III (Nine-Strike) | Guaranteed, once per life | +25% damage during tribulations. +10% lightning resist | M2 |
| Dragon King's Tide | T7 | Abyss Dragon (Map 20) | 0.3% / 400 | Each kill heals 3% Max HP. This is the only on-kill heal, which makes it valuable since battle only has slow base regen | M3 |
| Sword Wraith Emperor's Edge | T7 | Sword Wraith Emperor (Map 18) | 0.3% / 400 | Ten Thousand Swords: every 5th attack hits 5 times for 40% each | M3 |
| Vermilion Feather | T8 | Vermilion Phoenix (Map 22) | 0.3% / 400 | Burn stacks up to 6 (normally 3). Burning enemies take +15% damage | M3 |
| Heaven's Wrath | T8 | First clear of Tribulation VI (Nine Heavens Thunder) | Guaranteed, once per life | Every 10 s, a lightning bolt deals 300% ATK | M3 |
| Taotie's Hunger | T9 | Taotie the Devourer (Map 25) | 0.3% / 400 | Lifesteal 5% of damage dealt | M3 |
| Heavenly Dao Sword | T9 | Heavenly Dao Avatar (Map 26) | 0.2% / 600 | +3% damage per realm reached (+30% at GA) | M3 |
| Moonlight Lantern Sword | Your tier | Lantern Festival event track | Event reward | +20% damage at night (device clock, 18:00–06:00) | M3 |
| Riverdragon Jian | Your tier | Dragon Boat event track | Event reward | +15% SPD. Its first hit each fight deals ×2 | M3 |

- Legendaries **scale with tier** like other swords, so an early one isn't automatically best in slot later. Event legendaries drop at the player's current tier.
- Pity counters and "guaranteed once per life" clears **reset on Rebirth**. Swords you own are kept.

### Sword Pavilion (shop)
- **Unlock:** MO 5. Pays in **Spirit Stones only**.
- **Stock:** Mortal Jian, Saber, and Greatsword of your current tier, always available. Plus **3 rotating slots**: Spirit (80%) or Earth (20%) Jian or Saber of your current tier, with random affixes shown before buying.
- **Refresh:** every 6 h, or with Jade (20 Jade, max 3 per day).
- **Prices (T1, ×7^(tier − 1)):** Mortal 50 · Spirit 300 · Earth 1,500 Spirit Stones.
- **Milestone:** M1.

## Rarity
| Rarity | Color | Affixes | Main-stat roll (× base) | Affix roll | Drop weight |
|---|---|---|---|---|---|
| Mortal | Grey | 0 | 0.8–1.0 | — | 60% |
| Spirit | Green | 1 | 1.0–1.2 | Full range | 28% |
| Earth | Blue | 2 | 1.2–1.5 | Full range | 10% |
| Heaven | Purple | 3 | 1.5–1.9 | Top 50% of range | 1.9% |
| Immortal | Gold | 4 | 2.0–2.5 | Top 25% of range | 0.1% (bosses, dungeons, D8 only) |

Boss kills roll rarity with weights ×3 for Earth and above. Dungeon final chests roll at least Spirit.

## Item Tier, Level & Requirements
- **Item tier (T1–T9)** = the tier of the map or dungeon that dropped it (see the registry's map table). It sets the **required realm**: T1 MO, T2 FE, T3 GC, T4 NS, T5 SF, T6 VB, T7 MA, T8 GA 1, T9 GA 5.
- **Item level within a tier (1–4):** zone 1 → 1, zone 2 → 2, zone 3 → 3, boss/dungeon → 4. Each item level adds +10% main stat.
- **Main stat** = slot base × 2.5^(tier − 1) × (1 + 0.1 × (itemLevel − 1)) × rarity roll. The ×2.5 matches the realm stat multiplier, so on-tier gear stays at about +40–60% of base stats.

| Slot | T1 base main stat | T1 base secondary |
|---|---|---|
| Robe | 60 HP | 6 DEF |
| Bracers | 5 ATK | 1% Crit |
| Boots | 3 SPD | 1% Dodge |
(Secondary % stats don't scale with tier. Flat ones do. The Sword's main stat is a multiplier (see [Swords](#swords)). Accessories have no main stat (see [Accessories](#accessories)).)

## Accessories
**No main stat.** Each accessory rolls **1–3 random stats** from its **slot's pool**. Higher rarity favors more stats:

| Rarity | Stat count |
|---|---|
| Mortal | 1–2 |
| Spirit | 1–2 |
| Earth | 1–3 |
| Heaven | 2–3 |
| Immortal | 3 |

The count is random within that range. Each stat's value is rolled from a range set by **rarity** ([02-Systems §4](../02-Systems.md)). The same stat can't roll twice on one item.

| Slot | Stat pool |
|---|---|
| **Talisman** | × Qi rate · +Max Qi % · +Breakthrough chance · +Crit % · −Combat art Qi cost % · −Injury duration % |
| **Ring** | × Tempering rate · +Max HP % · +DEF % · +Dodge % · +Healing received % · −Injury duration % |
| **Pendant** | × Spirit Stones · × Damage · +Drop rarity % · × Life-skill speed · +Crit Dmg % · −Injury duration % |

| Rarity | × stats (Qi, Tempering, Stones, Damage, Life-skill) | % stats (Max HP/Qi, DEF, Healing received, Crit Dmg, −Qi cost, −Injury duration) | Small % stats (Crit, Dodge, Breakthrough, Drop rarity) |
|---|---|---|---|
| Mortal | ×1.03–1.10 | +2–5% | +0.5–1% |
| Spirit | ×1.08–1.20 | +4–8% | +1–2% |
| Earth | ×1.15–1.35 | +7–12% | +2–3% |
| Heaven | ×1.30–1.60 | +10–18% | +3–4% |
| Immortal | ×1.50–2.00 | +15–25% | +4–6% |

- **Tier shift:** × stats +0.03 per tier above T1. % stats +5% of the value per tier above T1 (a T5 Earth Ring's +10% Max HP becomes +12%).
- **Enhancement:** each level adds +2% to every stat's bonus (+30% at +15). For example, ×1.40 Qi at +15 becomes ×1.52. Costs and success rates are the same as gear.
- **Reforge:** reroll one stat (type and value) and keep the others (see [Reforging](#reforging)).
- **Examples:** a Heaven Talisman with ×1.42 Qi and +3% Breakthrough. An Earth Ring with only ×1.31 Tempering. A Spirit Pendant with ×1.12 Spirit Stones, ×1.09 Damage, and +6% Crit Dmg.
- × stats from all sources **multiply** (Talisman × cultivation method × pills × rebirth). A good Qi Talisman and Tempering Ring are the biggest single pieces of `EXT` in [03-Economy](../03-Economy.md).
- An accessory's realm requirement follows its tier, like gear. A high-rarity, low-tier accessory with a strong × stat stays useful for a long time.

## Affixes
**Gear affixes** (Sword, Robe, Bracers, Boots). Each affix can appear at most once per item. Values by item tier (interpolate the tiers in between). Qi rate % doesn't roll on gear: it comes from Talisman stats.

| Affix | T1 | T3 | T5 | T7 | T9 | Cap (total) |
|---|---|---|---|---|---|---|
| +ATK % | 2–4 | 4–7 | 6–10 | 8–13 | 10–16 | — |
| +HP % | 2–4 | 4–7 | 6–10 | 8–13 | 10–16 | — |
| +DEF % | 2–4 | 4–7 | 6–10 | 8–13 | 10–16 | — |
| +SPD (flat) | 1–3 | 4–8 | 10–18 | 22–40 | 50–90 | — |
| +Crit % | 1–2 | 2–3 | 3–4 | 4–5 | 5–6 | 75% |
| +Crit Dmg % | 5–10 | 10–16 | 15–24 | 20–32 | 25–40 | — |
| +Dodge % | 1–2 | 2–3 | 3–4 | 4–5 | 5–6 | 40% |
| +Element Dmg % (one element) | 3–6 | 6–10 | 9–14 | 12–19 | 15–25 | — |
| Armor Pierce % | 2–4 | 4–7 | 6–10 | 9–14 | 12–18 | 60% |
| +Tempering Rate % (Robe only) | 2–4 | 4–6 | 6–9 | 8–12 | 10–15 | — |
| Lightning Resist % (D7 and Tribulation set only) | — | — | — | 8–14 | 12–20 | 70% |

## Gear Sets
Set pieces exist for all 7 slots. A set Sword keeps its type and × Damage roll, and a set accessory keeps its 1–3 random stats. Bonuses top out at 6 pieces, so one slot is always free, usually for a Twin, Flying, or Legendary sword, which are never set pieces. They drop as **Earth rarity or better** from the listed sources (about 15% of Earth+ drops there are set pieces, 30% from that tier's bosses). Set pieces keep normal random affixes.

| Set | Tier | Source | Element | 2 pieces | 4 pieces | 6 pieces | Milestone |
|---|---|---|---|---|---|---|---|
| Bamboo Wanderer | T1 | Maps 1–2 | Wood | +5% SPD | +8% ATK | +15% Wood dmg. Combat arts cost 20% less Qi | M1 |
| Ember Monk | T2 | Maps 3–5 | Fire | +8% HP | +10% ATK | Basic attacks apply Burn (3% ATK/s, 3 s) | M1 |
| Thunder Hawk Regalia | T3 | Maps 6–8 | Metal | +3% Crit | +20% Crit Dmg | Crits call down lightning for 50% ATK | M1 |
| Sword Saint's Legacy | T3–T7 (scales with D2 tier) | D2 | Metal | +10% combat art dmg | −15% combat art cooldowns | Every 3rd combat art casts twice | M2 |
| Desert Wyrm Scale | T4 | Maps 9–11 | Earth | +10% DEF | +12% HP | Reflect 15% of damage taken | M2 |
| Golden Roc Plumage | T5 | Maps 12–14 | Metal | +6% SPD | +5% Dodge | After a dodge, next attack +100% dmg | M2 |
| Void Walker | T6 | Maps 15–17 | Earth | +6% Armor Pierce | +12% ATK | 10% chance for an attack to ignore all DEF | M2 |
| Abyssal Dragon | T7 | Maps 18–20 | Water | +12% HP | +15% Water dmg | Below 30% HP: shield for 25% HP (once per fight). Delays the retreat point | M3 |
| Vermilion Phoenix | T8 | Maps 21–23 | Fire | +15% ATK | +20% Fire dmg | Revive once per fight at 40% HP | M3 |
| Tribulation Thunder Robes | T8 | D7 | Metal | +15% Lightning Resist | +10% HP | +30% all stats during Heavenly Tribulations | M3 |
| Heavenly General | T9 | Maps 24–26 | Metal | +10% HP and DEF | +15% ATK | +25% dmg vs bosses, +10% Lightning Resist | M3 |
| Immortal Ancestor | T9 | D8 (Immortal rarity only) | All | +10% Qi rate | +15% all stats | +20% all dmg. Cast one free combat art at fight start | M3 |

Rule: sets from different tiers can mix (2 + 2 + 2). Only the highest bonus of each set counts.

## Enhancement (+1 … +15)
Done at the Forge. Spirit Stone cost below is for a **T1 item**. Multiply by **7^(tier − 1)** for higher tiers. Refining Stone cost is multiplied by the item tier.

| Lvl | Spirit Stones (T1) | Refining Stones (× tier) | Success | Main stat bonus (cumulative) | Realm cap |
|---|---|---|---|---|---|
| +1 | 25 | 1 | 100% | +4% | FE |
| +2 | 40 | 1 | 100% | +8% | FE |
| +3 | 60 | 2 | 100% | +12% | FE |
| +4 | 90 | 2 | 100% | +16% | FE |
| +5 | 130 | 3 | 100% | +20% | FE |
| +6 | 200 | 4 | 90% | +26% | GC |
| +7 | 300 | 5 | 80% | +32% | GC |
| +8 | 450 | 6 | 70% | +38% | GC |
| +9 | 650 | 8 | 60% | +44% | GC |
| +10 | 950 | 10 | 50% | +50% | GC |
| +11 | 1,400 | 12 | 45% | +58% | NS |
| +12 | 2,000 | 15 | 40% | +66% | NS |
| +13 | 2,900 | 18 | 35% | +74% | NS |
| +14 | 4,250 | 22 | 30% | +82% | NS |
| +15 | 6,000 | 26 | 25% | +90% + sword/robe glow (cosmetic) | NS |

- **Swords and accessories:** the "main stat bonus" column applies to armor only. On a **Sword**, each level adds +2% to the × Damage bonus (+30% at +15: ×1.40 → ×1.52). On an **accessory**, each level adds +2% to every stat's bonus. Costs and success rates are the same.

- **Non-destructive:** a failure never lowers the level or destroys the item. It consumes the Refining Stones, and **50% of the Spirit Stones are refunded**.
- **Pity:** +10% success per consecutive failure on that item. Resets on success.
- **Enhancement Transfer:** when you equip a new item in the same slot, you can move the old item's enhancement level to it for 20% of the total original Spirit Stone cost (at the new item's tier). The old item drops to +0. This keeps investment from feeling wasted as you move up tiers.
- Caps (+5 / +10 / +15) unlock with realms, matching the Spirit Stone flow in [03-Economy](../03-Economy.md).
- **Milestone:** +1…+10 in M1, +11…+15 in M2.

## Reforging
| Tier | Unlock | Action | Cost |
|---|---|---|---|
| Reforge I | FE (with Forging) | Reroll the **value** of one affix/accessory stat within its range, or reroll its **type** (random new one from the slot's pool) | 1 Dao Pattern Stone + Spirit Stones (= +5 enhance cost at that tier) |
| Reforge II | VB 1 | **Lock** up to 2 affixes and reroll the rest, **or** pick one affix to replace from 3 offered options | 3 Dao Pattern Stones (+2 per locked affix) + Spirit Stones |

- Dao Pattern Stones: ~5% chance from any boss kill (from FE onward), and a main drop of D5.
- Reforging never changes rarity, set, main stat, sword type, or the **number** of accessory stats. A legendary sword's unique effect can't be reforged.
- **Milestone:** Reforge I in M1, Reforge II in M2.

## Salvage
Spirit Stone values below are for T1. Multiply by **7^(tier − 1)**.

| Rarity | Spirit Stones | Refining Stones | Extra |
|---|---|---|---|
| Mortal | 10 | 30% chance of 1 | — |
| Spirit | 30 | 1 | — |
| Earth | 100 | 3 | 1 ore of the item's tier (Mining table) |
| Heaven | 400 | 8 | 10% chance of a Dao Pattern Stone |
| Immortal | 2,000 | 25 | 1 Dao Pattern Stone |

Enhanced items also return **50% of the Refining Stones** spent on enhancing them.

### Auto-salvage
- **Unlock:** achievement "Hoarder's Regret" (salvage 200 items manually). See [11-Quests-Achievements](11-Quests-Achievements.md).
- **Filters (combinable):** rarity at or below X · tier below current realm · not a set piece / any · keep if it has affix Y (whitelist) · keep if main stat is higher than equipped.
- **Locked** items are never salvaged. Equipped items are always locked.

## Inventory (Gear Bag)
- **Gear bag:** 50 slots at start, +10 per major realm reached (140 at GA), and +10 per Jade expansion (50 → 100 → 150… Jade, max +100). Bag size is kept through Rebirth.
- **Materials** go into a separate **unlimited, stacking** material storage. They never take bag slots.
- **Full bag:** new gear drops are **auto-salvaged** instead of lost, and the return screen says "23 items auto-salvaged (bag full)." Nothing is ever silently destroyed.
- Sort: by tier, rarity, slot, power. Filter: slot, set, element. A "compare to equipped" arrow is shown on every item.
- **Milestone:** M1.

## Loadouts
- **3 loadout slots at launch (v1.0).** Each saves the Sword, armor, all 3 accessories, and the pill pouch.
- **Swap with one tap** from the Character screen or the top-bar chip. Example sets: Meditate (best Qi stats), Battle (damage, crit, healing pills), Tribulation (lightning resist, Max HP).
- An item can be in several loadouts. Swapping never moves enhancement levels.
- **Auto-swap by activity** is a Karma perk (*Prepared Mind*, [12-Rebirth](12-Rebirth.md)): Meditate, Train, and Battle each use their assigned loadout automatically, including during Routines and offline.

## Sources Summary
| Source | Gear |
|---|---|
| Map monsters | Tier of the map, Mortal → Heaven. Swords: Jian and Saber |
| Map bosses | Tier of the map, rarity weights ×3, set pieces 30%, the boss's own **Twin Swords** 15%, legendary swords (listed bosses) |
| Dungeons | Dungeon set pieces, at least Spirit. **Flying Swords** (D2, D5, D7, D8). D8 gives Immortal |
| Forging | Choose the slot, at least Spirit. Swords: Jian, Saber, Greatsword. Recipes and the rarity chance from Forging level are in [08-Life-Skills](08-Life-Skills.md) |
| Sword Pavilion | Mortal swords always. Spirit/Earth Jian and Saber rotating (Spirit Stones) |
| Sect shop | Heaven-rarity swords (Sect Merit), see [13-Sect-Events](13-Sect-Events.md) |
| Events | Event legendary swords |
| Tribulations | Thunder-Tempered Blade, Heaven's Wrath (first clears) |

## Decisions
- Enhancement Transfer costs **20%** (a stone sink).
- **3 loadouts** at v1.0 (see [Loadouts](#loadouts)). Auto-swap by activity is a Karma perk.
- Named legendaries are **swords only** at launch.
- No gathering gear set; the Pendant's life-skill stat covers it.
- Accessory stat count is weighted by rarity (Mortal 1–2 … Immortal 3).
