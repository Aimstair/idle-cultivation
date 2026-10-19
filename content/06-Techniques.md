# 06 — Techniques

Two kinds of technique: **Cultivation Methods** (passive, boost Qi gain and stats) and **Combat Arts** (active, auto-cast in battle). Names follow [00-Registry](00-Registry.md). Status effects (Burn, Poison, Bleed, Freeze, Stun, Root, Shield, Taunt) are defined in [03-Combat-Maps](03-Combat-Maps.md).

## Slots
| Slot | Unlock | Notes |
|---|---|---|
| Cultivation method 1 | MO 1 (Basic Breathing Method equipped) | Full effect |
| Cultivation method 2 | VB 1 | **50% effect** (Qi bonus and stat bias). Its element doesn't change your attack element |
| Combat art 1 | MO 5 (with combat) | — |
| Combat art 2 | FE 1 | — |
| Combat art 3 | SF 1 | — |

- Techniques can be swapped freely outside combat. Swapping during a fight takes effect next fight.
- **Element:** your primary method's element is your **attack element** for basic attacks (Wu Xing advantage). Combat arts use their own element.
- **Auto-cast:** arts fire in slot order when off cooldown and enough Qi is available (the shared cultivation pool, above your **Qi floor** setting). Players can reorder slots to set priority.
- **Kept through Rebirth:** all learned techniques and comprehension levels.

## Cultivation Methods (15)
| Method | Tier | Element | Qi bonus | Stat bias | Source | Milestone |
|---|---|---|---|---|---|---|
| Basic Breathing Method | T1 | None | +0% | — | Start | M0 |
| Verdant Spring Art | T1 | Wood | +10% | +5% HP | Bamboo Viper King (Map 1) | M1 |
| Azure Cloud Sutra | T2 | Water | +20% | +5% SPD | Lake Serpent (Map 3) | M1 |
| Golden Bell Scripture | T2 | Metal | +25% | +15% DEF | Fallen Elder (Map 5) | M1 |
| Nine Suns Scripture | T2 | Fire | +35% | +10% ATK | Flame Ape (Map 4) / D1 | M1 |
| Thunder Sovereign Canon | T3 | Metal | +45% | +4% Crit | Thunder Hawk (Map 6) / D2 | M1 |
| Yellow Springs Yin Art | T4 | Earth | +60% | +15% HP | Corpse King (Map 10) | M2 |
| Endless Sea Sutra | T4 | Water | +60% | +20% Max Qi | Kraken Matriarch (Map 11) / D3 | M2 |
| Golden Roc Wing Art | T5 | Metal | +80% | +10% SPD | Golden Roc (Map 12) | M2 |
| Ten-Thousand Beast Scripture | T5 | Wood | +80% | +20% pet stats | Ancient Ape Sovereign (Map 14) | M2 |
| Void Heart Sutra | T6 | Earth | +110% | +4% Dodge | Void Golem (Map 15) / D5 | M2 |
| Sword Dao Canon | T7 | Metal | +150% | +25% Crit Dmg | Sword Wraith Emperor (Map 18) / D2 (top tier) | M3 |
| Primordial Dragon Scripture | T7 | Water | +150% | +10% HP and ATK | Abyss Dragon (Map 20) / D6 | M3 |
| Vermilion Bird Rebirth Art | T8 | Fire | +200% | Revive once per fight at 30% HP | Vermilion Phoenix (Map 22) | M3 |
| Heavenly Dao Scripture | T9 | All (matches enemy weakness) | +300% | +10% all stats | Heavenly Dao Avatar (Map 26) | M3 |

Method Qi bonuses **multiply** with the Talisman's × Qi rate ([05-Equipment](05-Equipment.md#accessories)): for example, Nine Suns (+35%) with a Spirit Talisman (×1.20) gives ×1.62. Together they make up most of the `EXT` assumption in [03-Economy](../03-Economy.md) (1.0 / 1.5 / 2.5 / 4.0 for realms 1–4). Keep the two in sync when tuning.

## Combat Arts (26)
Qi cost is **3–10% of Max Qi**, paid from your **shared cultivation pool** ([02-Systems §0](../02-Systems.md)). Every cast means more Meditate time later before Max Qi can grow, so arts set to Auto trade cultivation time for kill speed. A **Qi floor** of 100% turns them all off ([03-Combat-Maps A5](03-Combat-Maps.md)). Damage is a % of ATK.

### Metal
| Art | Tier | Effect | Qi | CD | Source | Milestone |
|---|---|---|---|---|---|---|
| Flying Sword | T1 | 150% ATK, single target. **+30% damage with a Flying Sword-type sword equipped** | 3% | 4 s | Bandit Chief Zhao (Map 2) | M1 |
| Golden Bell Guard | T2 | +40% DEF for 6 s | 4% | 14 s | Fallen Elder (Map 5) | M1 |
| Lightning Spear | T3 | 220% ATK, 20% chance to Stun 1 s | 4% | 6 s | Thunder Hawk (Map 6) | M1 |
| Thousand Blades | T3 | 80% ATK × 3, all enemies | 5% | 8 s | D2 | M2 |
| Sword Domain | T7 | 5 s field: all enemies take 60% ATK/s | 8% | 18 s | Sword Wraith Emperor (Map 18) / D2 | M3 |
| Heavenly Judgement | T9 | 600% ATK, executes targets below 20% HP | 10% | 20 s | Heavenly General (Map 24) | M3 |

### Wood
| Art | Tier | Effect | Qi | CD | Source | Milestone |
|---|---|---|---|---|---|---|
| Vine Bind | T1 | 100% ATK, 25% chance to Root | 3% | 6 s | Bamboo Viper King (Map 1) | M1 |
| Verdant Heal | T2 | Heal 20% max HP | 4% | 12 s | Manual Fragments (Maps 1–3) | M1 |
| Poison Mist | T3 | Poison all enemies: 4% ATK/s for 6 s | 4% | 10 s | Thousand-Year Toad (Map 7) | M1 |
| Thorn Storm | T5 | 130% ATK × 2 to all, applies Bleed | 6% | 10 s | Ancient Ape Sovereign (Map 14) | M2 |
| World Tree Blessing | T7 | Heal 30% HP + regen 3% HP/s for 6 s | 8% | 20 s | Elder Treant (Map 19) | M3 |

### Water
| Art | Tier | Effect | Qi | CD | Source | Milestone |
|---|---|---|---|---|---|---|
| Water Mirror Shield | T2 | Shield 20% max HP | 3% | 10 s | Lake Serpent (Map 3) | M1 |
| Frost Needle | T3 | 180% ATK, 30% chance to Freeze 1.5 s | 4% | 7 s | Frost Qilin (Map 8) | M1 |
| Tidal Wave | T4 | 200% ATK to all, pushes back enemy action bars 20% | 6% | 10 s | Kraken Matriarch (Map 11) | M2 |
| Star Sea Torrent | T6 | 70% ATK × 6 hits, refunds 3% Max Qi | 6% | 12 s | Star-Eater Leviathan (Map 16) | M2 |
| Abyssal Dragon Roar | T7 | 350% ATK to all, enemies −20% ATK for 5 s | 9% | 16 s | Abyss Dragon (Map 20) / D6 | M3 |

### Fire
| Art | Tier | Effect | Qi | CD | Source | Milestone |
|---|---|---|---|---|---|---|
| Flame Palm | T2 | 120% ATK + Burn | 3% | 5 s | Flame Ape (Map 4) | M1 |
| Fire Crow Strike | T4 | 3 crows × 110% ATK, each 30% chance to Burn | 4% | 7 s | Sand Wyrm (Map 9) | M2 |
| Lava Eruption | T5 | 280% ATK to all + Burn | 7% | 12 s | Lava Salamander Lord (Map 13) | M2 |
| Demon Flame | T6 | 400% ATK single target, also costs 10% of current HP | 6% | 10 s | Demon General (Map 17) | M2 |
| Vermilion Phoenix Dive | T8 | 500% ATK to all + heal 15% HP | 10% | 18 s | Vermilion Phoenix (Map 22) | M3 |

### Earth
| Art | Tier | Effect | Qi | CD | Source | Milestone |
|---|---|---|---|---|---|---|
| Mountain Fist | T2 | 200% ATK, 15% chance to Stun 1 s | 4% | 7 s | Fallen Elder (Map 5) | M1 |
| Earth Wall | T4 | Shield 35% HP + Taunt (protects your pet) | 5% | 14 s | Corpse King (Map 10) | M2 |
| Void Collapse | T6 | 300% ATK to all, ignores 50% DEF | 8% | 12 s | Void Golem (Map 15) / D5 | M2 |
| Celestial Mountain Seal | T8 | 450% ATK + guaranteed Stun 2 s | 9% | 16 s | Fallen Celestial (Map 21) | M3 |
| Chaos Devour | T9 | 500% ATK, heals for 50% of damage dealt | 10% | 18 s | Taotie the Devourer (Map 25) | M3 |

## Comprehension (levels 1–10)
- Every technique starts at **level 1** when learned.
- A **duplicate manual** of a technique you already know turns into **10 Comprehension** for that technique.
- Levels cost Comprehension + Spirit Stones (stones scale with the technique's tier, ×7 per tier, like enhancement):

| To level | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| Comprehension | 10 | 10 | 20 | 20 | 30 | 30 | 40 | 50 | 60 | 270 (27 duplicates) |
| Spirit Stones (T1) | 50 | 100 | 200 | 400 | 700 | 1,100 | 1,600 | 2,300 | 3,200 | 9,650 |

- **Per level:** methods get +10% of their base Qi bonus and stat bias (so level 10 = ×1.9). Combat arts get +8% damage or effect strength.
- **Level 5:** combat arts −15% cooldown. Methods +2% Qi breakthrough chance.
- **Level 10, "Awakened":** combat arts get an element upgrade. Methods get +5% Qi breakthrough chance and an aura cosmetic.

| Element | Awakened bonus (arts) |
|---|---|
| Metal | +15% Crit chance on this art |
| Wood | Heal, Poison, and Bleed durations ×1.5 |
| Water | Shields +50%, Freeze chance +15% |
| Fire | Burn damage ×2 |
| Earth | Stun chance +15%, Stun duration +0.5 s |

## Element Schools
- **School bonus:** if your main cultivation method and **all** equipped combat arts share one element, you get **+10% damage and +10% Qi rate** for that element's school (for example, an all-Metal "Sword school").
- The second method slot (50% effect) doesn't count toward or against the school.

## Sources
| Source | What drops | Rate |
|---|---|---|
| Map boss, **first kill** | Guaranteed: that boss's combat art manual (the method if it has no art) | 100% once |
| Map boss, repeat kills | Any manual from that boss | 3% |
| D2 Ancient Tomb of Sword Saints | Random manuals (Metal-weighted), Manual Fragments | Main source |
| Manual Fragments | All bosses (5%), D2. **10 fragments → 1 random manual** of your current realm's tier or lower | — |
| Sect shop (M3) | T1–T5 manuals for Sect Merit, rotating weekly | — |
| Events (M3) | Event-only cosmetic variants (same stats) | — |

## Decisions
- Element schools: +10% when the method and all arts share an element (see [Element Schools](#element-schools)).
- The second method slot stays at **50% effect**.
- Combat art Qi cost stays as a **% of Max Qi**.
- Healing arts are kept as-is. Tune in the closed beta.
