# 15 — Cultivation Grounds (Meditation Sites & Training Grounds)

There are three kinds of map, one per activity ([02-Systems §0b](../02-Systems.md)):

| Map kind | Activity | What it gives |
|---|---|---|
| **Combat Maps** (26, see [03-Combat-Maps](03-Combat-Maps.md)) | Battle | Loot, stones, materials |
| **Meditation Sites** | Meditate | **× Qi rate** while meditating there |
| **Training Grounds** | Train | **× Tempering rate** while training there, plus a mastery XP bonus for one exercise |

## Rules
- **Unlocking:** the **first clear of each combat map's boss** unlocks that map's Meditation Site or Training Ground. Progressing through combat is how you get better places to cultivate.
- **Starting grounds** are always available:
  - **Humble Hut** (Meditate ×1.0)
  - **Village Courtyard** (Train ×1.0)
- **Choosing:** when you pick Meditate or Train (or set a Routine step), you also pick the site. The game defaults to your best unlocked one.
- **Element affinity (Meditation Sites):** +10% more if the site's element matches your equipped cultivation method's element ([06-Techniques](06-Techniques.md)). A slightly weaker site of your element can beat a stronger one of another element.
- **Exercise focus (Training Grounds):** each ground gives **+50% mastery XP** to one exercise ([02-Body](02-Body.md)), so the best ground depends on which exercise you're levelling.
- **Upkeep (from SF):** high-tier grounds cost **Spirit Stones per hour** while in use, including offline. If you can't pay, you're moved to your best free ground. This is a stone sink that scales with the economy.
- **Minimum realm:** each ground can only be used once you reach the realm and level where its combat map starts (column below). This matters most after a rebirth with Map Memory: your old grounds stay unlocked but become usable again as you climb.
- **No upgrades** for now. Sites are fixed.
- **Stacking:** the site multiplier multiplies with everything else (Talisman/Ring stats, technique, rebirth). It's part of `EXT` in [03-Economy](../03-Economy.md).
- **Rebirth:** grounds re-lock with map progress and re-unlock as you re-clear bosses. The **Map Memory** Karma perk ([12-Rebirth](12-Rebirth.md)) keeps them.
- **Milestone:** M1 (grounds from maps 1–8), M2 (9–17), M3 (18–26).

## Grounds by Map
| Map (boss first clear) | Unlocks | Kind | Multiplier | Element / Exercise focus | Min realm | Upkeep (stones/h) |
|---|---|---|---|---|---|---|
| — (start) | Humble Hut | Meditation | ×1.00 | — | MO 1 | — |
| — (start) | Village Courtyard | Training | ×1.00 | — | QC 1 | — |
| 1 Misty Bamboo Grove | Bamboo Grove Hermitage | Meditation | ×1.10 | Wood | MO 5 | — |
| 2 Bandit Pass | Pass Fort Drill Yard | Training | ×1.10 | Stone Lifting | QC 7 | — |
| 3 Moonlit Lake | Moonlit Lake Pavilion | Meditation | ×1.20 | Water | FE 1 | — |
| 4 Ember Hills | Ember Hot Springs | Training | ×1.25 | Waterfall Endurance | FE 4 | — |
| 5 Old Sect Ruins | Ruined Meditation Hall | Meditation | ×1.30 | Earth | FE 8 | — |
| 6 Thunder Peak | Thunderstruck Summit | Training | ×1.35 | Iron Sand Palm | GC 2 | — |
| 7 Poison Marsh | Venom-Steeped Pools | Training | ×1.45 | Waterfall Endurance | GC 5 | — |
| 8 Frozen Abyss | Glacial Cave of Stillness | Meditation | ×1.50 | Water | GC 8 | — |
| 9 Crimson Desert | Sunscorch Dunes | Training | ×1.60 | Shadow Footwork | NS 1 | — |
| 10 Ghost Mist Forest | Yin Spirit Altar | Meditation | ×1.65 | Earth | NS 4 | — |
| 11 Azure Sea Isles | Tidal Reef Platform | Training | ×1.75 | Stone Lifting | NS 7 | — |
| 12 Sky Bridge Peaks | Cloud Sea Peak | Meditation | ×1.90 | Metal | SF 1 | 70,000 |
| 13 Scorched Volcano | Volcano Crater Forge | Training | ×1.95 | Iron Sand Palm | SF 4 | 84,000 |
| 14 Spirit Beast Plains | Primal Spirit Spring | Meditation | ×2.05 | Wood | SF 7 | 98,000 |
| 15 Shattered Realm | Void Rift Edge | Training | ×2.20 | Shadow Footwork | VB 1 | 500,000 |
| 16 Star Sea Ruins | Starlight Observatory | Meditation | ×2.30 | Water | VB 4 | 590,000 |
| 17 Demon Border | Demon-Slaying Wall | Training | ×2.45 | Golden Bell Cover | VB 7 | 690,000 |
| 18 Heavenly Sword Tomb | Sword Intent Cliff | Meditation | ×2.60 | Metal | MA 1 | 3,500,000 |
| 19 Primordial Jungle | World Tree Roots | Training | ×2.70 | Waterfall Endurance | MA 4 | 4,100,000 |
| 20 Abyssal Rift | Dragon's Breath Chasm | Meditation | ×2.85 | Water | MA 7 | 4,800,000 |
| 21 Celestial Ruins | Celestial Palace Courtyard | Training | ×3.00 | Dragon-Elephant Stance | GA 1 | 25,000,000 |
| 22 Phoenix Nest | Phoenix Flame Altar | Meditation | ×3.20 | Fire | GA 2 | 29,000,000 |
| 23 Thunder Sea | Tribulation Lightning Field | Training | ×3.35 | Lightning Tempering | GA 4 | 34,000,000 |
| 24 Nine Heavens Stair | Nine Heavens Terrace | Meditation | ×3.60 | Metal | GA 5 | 170,000,000 |
| 25 Chaos Wastes | Chaos Crucible | Training | ×3.80 | Dragon-Elephant Stance | GA 6 | 200,000,000 |
| 26 Heaven's Gate | Summit of Heaven | **Both** | ×4.50 | All elements / all exercises +25% | GA 8 | 250,000,000 |

**Balance notes:**
- Every realm band has at least one site of each kind. Fire-element meditators get no Fire site until Phoenix Flame Altar. That's deliberate (Fire methods are combat-strong), but it's an open question.
- Upkeep is set to **10% / 12% / 14–15%** of the hourly stone income at that tier (1st / 2nd / 3rd ground of the tier), checked in [Balancing.xlsx](../Balancing.xlsx) ([03-Economy](../03-Economy.md)).

## Decisions
- **Sect-owned site:** yes, shared by Sect members, arriving with Sects (post-launch).
- **Site upgrades:** none for now. **Minimum realms:** yes (column above).
