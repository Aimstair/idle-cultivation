# 03 — Combat & Maps

Names follow [00-Registry](00-Registry.md). Archetypes and rarity weights follow [04-Content](../04-Content.md). Economy targets follow [03-Economy](../03-Economy.md).

---

# Part A — Combat Rules

## A1. Turn Order (Action Gauge)
- Every combatant has an **action gauge** (0 → 1,000). Each combat tick (100 ms) adds `SPD` to the gauge.
- When the gauge reaches 1,000, the unit acts and 1,000 is subtracted (overflow carries over, so very fast units occasionally act twice).
- Ties: the player acts first, then the pet, then enemies in spawn order.
- **Stun / Freeze** pause the gauge. **Slow** halves gauge gain.

## A2. Damage
```
raw      = ATK × skillMult
mitig    = ATK / (ATK + DEF × (1 − armorPierce))
damage   = raw × mitig × elementMod × critMult × variance(0.95–1.05)
```
- Basic attack `skillMult` = 1.0. Combat arts list their own (for example, Flying Sword 1.5).
- The `ATK/(ATK+DEF)` mitigation means equal ATK and DEF gives 50% damage. DEF never fully blocks damage.
- **Minimum damage:** 1.
- **Physical vs Qi damage:** basic attacks and Iron Sand Palm bonuses are *physical*. Combat arts are *Qi* damage. Body-stage resists apply to physical, element resists to Qi. (Both use the same formula. The split only matters for which bonuses apply.)

## A3. Crit, Dodge, Pierce
| Stat | Base | Cap | Notes |
|---|---|---|---|
| Crit % | 5% | 75% | |
| Crit Dmg | 150% | none | |
| Dodge % | 0% | 60% | Checked before damage. Bosses ignore 50% of your Dodge |
| Armor Pierce | 0% | 80% | Ignores that share of DEF |
| HP regen in battle | **Base regen** = 10% of your Train (Tempering) rate | — | Always on, in every activity, but slow. It never grows Max HP. The main in-battle healing is Healing Pills, healing arts, healer pets, lifesteal, and Dragon King's Tide (on-kill) |

## A4. Wu Xing (Five Elements)
**Overcoming cycle** (damage): Wood → Earth → Water → Fire → Metal → Wood
(Wood overcomes Earth, Earth overcomes Water, Water overcomes Fire, Fire overcomes Metal, Metal overcomes Wood.)

| Situation | Damage modifier |
|---|---|
| Your element overcomes the target's | **×1.25** |
| Target's element overcomes yours | **×0.80** |
| Same element or unrelated | ×1.00 |

**Generating cycle** (synergy): Wood → Fire → Earth → Metal → Water → Wood
- If your **active pet's** or **cultivation method's** element *generates* your combat art's element: **+10% damage** on that art.
- If your method and all equipped arts share one element ("Pure Path"): **+5% all stats**.

**Player element** = the element of the equipped cultivation method. Each combat art has its own element and uses it for its hits. Neutral (no element) is allowed for basic attacks.

The **"All"** element (Heaven's Gate) rotates every 20 s through the five elements, shown with an aura color.

## A5. Qi & Combat Arts (shared pool)
- Combat arts spend **your cultivation Qi**: the same pool shown on the Cultivate screen ([02-Systems §0](../02-Systems.md)). "Qi Pool" in older text means **Max Qi**.
- In battle, Qi only gets **base regen** (10% of the Meditate rate, [02-Systems §0](../02-Systems.md)). Qi carries over between fights. It refills properly only while **Meditating** (or with Qi Recovery Pills). Any Qi spent here means meditation time later before Max Qi can grow again.
- Combat arts auto-cast in **slot priority order** when they are off cooldown **and** affordable. Otherwise the unit does a basic attack.
- Cost: **3–10% of Max Qi** per cast ([06-Techniques](06-Techniques.md)). Cooldowns are 4–15 s.
- Players can set each slot to **Auto / Hold for Boss / Off**.
- **Qi floor (setting, default 0%):** arts set to Auto stop casting below this % of Max Qi. Set it to 100% to never spend Qi in battle, which saves meditation time later but lowers kill speed ([02-Systems §3](../02-Systems.md)).

## A6. Status Effects
| Effect | Behavior | Stacks | Typical duration |
|---|---|---|---|
| Burn | 3% max HP per second | Up to 3 | 4 s |
| Poison | 2% max HP per second, −30% healing received | Up to 5 | 6 s |
| Bleed | 4% of attacker's ATK per second, physical | Up to 5 | 5 s |
| Freeze | Gauge paused. Next hit taken +20% | No | 1.5 s |
| Stun | Gauge paused | No | 1 s (bosses: 0.5 s, then 5 s immunity) |
| Slow | Gauge gain halved | No | 3 s |
| Shield | Absorbs damage equal to X% max HP | Refreshes | 8 s |
| Root | Can't dodge. Gauge gain −25% | No | 3 s |
| Taunt | Enemies must target the taunter (pets, tanks) | No | 4 s |
| Weaken | −20% ATK | No | 4 s |
| Armor Break | −30% DEF | No | 4 s |
| Enrage (bosses) | +50% ATK, +30% SPD | — | Until death |

The element of a status follows its source: Fire → Burn, Wood → Poison, Water → Freeze/Slow, Metal → Bleed/Armor Break, Earth → Stun/Shield/Taunt, Wood → Poison/Root.

## A7. HP Between Fights (shared pool)
- **Maps:** **no heal between fights.** HP carries over from fight to fight, and it's the **same HP** as your Body pool. 1 s respawn delay. Statuses clear between fights.
- **Only base regen in battle** ([02-Systems §0b](../02-Systems.md)): 10% of the Train/Meditate rate, always on, never grows max. The real in-battle healing is Healing Pills (auto-used from the pouch at the set threshold), healing arts, **healer pets**, lifesteal, and on-kill effects. Full recovery happens in **Train** (HP) and **Meditate** (Qi).
- **Easy zones last longer:** in a zone you over-power, base regen and pets can nearly cover the damage you take, so you get many more fights before the retreat point. Nothing grows during battle, though.
- **Dungeons and Trial Tower:** you **enter with your current HP and Qi** and they stay depleted afterwards ([04-Dungeons](04-Dungeons.md)). Statuses also carry between waves.
- **Bosses:** a 60 s soft timer, then **Enrage**. 120 s hard timer, then the fight counts as a loss.

## A8. Defeat & Retreat
- **Retreat point:** when HP drops below **Retreat %** (default 30%), the cultivator stops battling so they don't die. With a **Routine** ([02-Systems §0b](../02-Systems.md)), the next step runs (usually **Train** to heal), and Battle resumes at the **resume point** (default **100%**, so every Battle step starts at full HP and the Train step can grow Max HP once full). Without a Routine, the cultivator just stops and waits. Both points are adjustable on the map screen.
- **HP reaches 0:** one **Internal Injury** stack ([02-Systems §1b](../02-Systems.md): −20% Tempering, −5% DEF per stack, 5 min each, unlimited stacks), then a forced retreat. No item or currency loss.
- **Maps:** after **3 consecutive losses** in a zone, the player auto-retreats to the previous zone (or zone 1 of the previous map), and the notice "Your cultivation is insufficient" appears.
- **Boss attempts:** unlimited, with a 10 s cooldown. The boss UI shows a **Power Check** (green/yellow/red) based on simulated win rate.
- **Dungeons:** a loss ends the run. Waves cleared still pay **50%** of their rewards. The entry is consumed.

## A9. Battle Activity, Auto-Advance & Farm Mode
- Combat runs only while the activity is **Battle** (directly or as a Routine step). Meditate and Train happen at Cultivation Grounds ([15-Cultivation-Grounds](15-Cultivation-Grounds.md)), not on combat maps.

| Mode | Behavior |
|---|---|
| **Auto-Advance** (default) | After 20 fights in a zone with ≥90% win rate, move to the next zone. At zone 3, attempt the boss when the Power Check is green |
| **Farm** | Stay in the chosen zone forever (for a specific drop) |
| **Boss Farm** (after first clear) | Zone 3 + the boss respawns every 10 min and is auto-fought (see A10) |

## A10. Boss Respawn
- After the first clear, each map boss **respawns every 10 minutes** while you battle in that map's zone 3, and is fought automatically, including offline (only during Battle steps).
- This is the main repeatable source of **signature drops** (bloods for Body breakthroughs, and so on).
- **Bad-luck protection:** each boss has a hidden counter per signature drop. If it hasn't dropped by kill ≈ **2 ÷ drop rate** (for example, the 7th kill at 30%), it's guaranteed, and the counter resets.
- **Healing Pills auto-use in battle only.** Outside battle they're used by tapping.
- **No manual interrupt button.** Interrupts (for example, Frost Qilin's Absolute Zero) come from auto-cast Stuns. Fights stay fully automatic.
- **Pet capture is boss-only.** Zone monsters never drop pets.
- Offline boss kills = `floor(battleSeconds / 600) × bossWinRate × 0.7`, where `battleSeconds` = time spent in Battle steps (see A11).

## A11. Kills/min Estimation (offline & UI)
```
TTK          = enemyHP / playerDPS            (DPS from simulated average, incl. arts & crits)
fightTime    = max(TTK, 2 s) + 1 s respawn
dmgPerFight  = simulated average HP lost per fight, minus in-battle healing (pills, healer pet, lifesteal)
               − baseRegen × fightTime          (baseRegen = 10% of temperRate; slightly extends uptime)

Routine cycle (e.g. Battle → Train → repeat):
  fightsPerCycle = (Resume% − Retreat%) × MaxHP / dmgPerFight      (dmgPerFight ≤ 0 → never retreats)
  battleTime     = fightsPerCycle × fightTime
  recoverTime    = (Resume% − Retreat%) × MaxHP / temperRate      (time in the Train step)
  + any Meditate step's fixed duration, plus Qi refill if arts were used
  uptime         = battleTime / cycleTime

killsPerMin  = 60 / fightTime × winRate × uptime
```
- **Qi:** arts spend Qi (minus Qi base regen) until the Qi floor, then stop. That lowers DPS for the rest of the Battle step. A Meditate step later refills it before Max Qi can grow.
- **Growth** only happens in **Train/Meditate** steps, after the pool is full. Battle steps never grow anything.
- **Healer pets** reduce `dmgPerFight`, so they are the main way to lengthen Battle steps and raise uptime.
- **No Routine:** the cultivator battles until the retreat point, then stops. The offline sim stops counting kills from that moment, and the return screen says "Retreated after 1h 12m".
- Normal monsters at the intended realm: **TTK 3–8 s**, so roughly **6–12 kills/min**.
- The game re-simulates `playerDPS` and `winRate` (100 headless fights) on gear/technique change and at logout. Offline uses that snapshot × 0.7 (economy doc).
- The UI shows **kills/min, stones/hr, and drops/hr** on the map screen.

## A12. Drop Rules (all maps)
| Drop | Chance per normal kill |
|---|---|
| Spirit Stones | 100% (amount below) |
| Beast Core (map tier) | 20% |
| Gear (map tier, rarity per 04-Content weights) | 5% |
| Map material (ore/herb, per map table) | 15% |
| Refining Stone | 2% |
| Manual Fragment | 0.5% (maps 5+) |
| Spirit Beast Egg (map tier) | 0.05% (bosses: 2%), from NS on |

**Spirit Stones per kill by tier** (≈ 360 kills/hr gives the economy-doc income):

| Tier | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|---|---|---|---|---|---|---|---|---|---|
| Stones/kill | 0.5 | 5 | 40 | 280 | 2K | 14K | 100K | 700K | 5M |

Zones 2 and 3 pay ×1.25 and ×1.5. Bosses pay ×20.

**Swords** ([05-Equipment](05-Equipment.md#swords)):
- About 1 in 6 gear drops from normal monsters is a sword: the map tier's **Jian** or **Saber**.
- Boss gear drops are the boss's own **Twin Swords** 15% of the time.
- Listed bosses (Thunder Hawk, Frost Qilin, Sword Wraith Emperor, Abyss Dragon, Vermilion Phoenix, Taotie, Heavenly Dao Avatar) also roll their **legendary sword** (0.2–0.3%, with a pity counter).

**Monster stats:** `zoneTier × 1.18^zoneIndex` (economy doc). Zone 3 is the tightest check. The boss is tuned to ~60% win rate at the map's intended entry realm/level.

---

# Part B — Maps

**Legend:** Archetypes = Brute, Swift, Caster, Tank, Swarm (04-Content). Element in brackets. **Sig.** = signature drop rate per boss kill. **First clear** rewards are one-time (they don't repeat after Rebirth; see 02-Systems §2c).

## Meridian Opening · Qi Condensation · Qi Sea (T1) · M1

### 1. Misty Bamboo Grove [Wood] · MO 5 – QC 9
| Zone | Monsters |
|---|---|
| 1 Bamboo Edge | Green Bamboo Snake (Swift, Wood), Wild Boar (Brute, Earth) |
| 2 Deep Thicket | Bamboo Rat Swarm (Swarm, Wood), Mist Fox (Swift, Water) |
| 3 Viper Hollow | Venom Viper (Caster, Wood), Stone-Shell Tortoise (Tank, Earth) |

- **Boss: Bamboo Viper King** (Wood, Swift). Applies Poison on every 3rd hit. **Phase 2 (50%):** sheds its skin and gains a Shield of 15% HP plus +30% SPD.
- **Drops:** Gear T1 · Beast Core T1 · Spirit Grass, Spirit Wood, Copper Ore · 0.5 stones/kill
- **Sig.:** Viper Fang 60%, Viper Blood 30%
- **First clear:** 50 Jade, 100 stones, Spirit-rarity Iron Jian. Unlocks map 2 and the **Bamboo Grove Hermitage** (Meditation Site, see [15-Cultivation-Grounds](15-Cultivation-Grounds.md). Each ground can be used once you reach the minimum realm listed there).

### 2. Bandit Pass [Metal] · QC 7 – FE 3
| Zone | Monsters |
|---|---|
| 1 Toll Road | Bandit Thug (Brute, Metal), Rogue Archer (Swift, Metal) |
| 2 Hidden Camp | Bandit Swordsman (Brute, Metal), Hedge Cultivator (Caster, Fire) |
| 3 Chief's Fort | Bandit Guard (Tank, Metal), Bandit Rabble (Swarm, Metal) |

- **Boss: Bandit Chief Zhao** (Metal, Brute). Armor Break on his opening strike. **Phase 2:** calls 2 Bandit Guards (Tank) to shield him. Kill the adds to remove his 50% damage reduction.
- **Drops:** Gear T1–T2 · Beast Core T1 · Spirit Grass, Spirit Rice, Copper Ore · 0.5–5 stones/kill
- **Sig.:** Bandit Treasure Map 40% (opens for 50× map stone value)
- **First clear:** 50 Jade, 300 stones, Qi Gathering Pill ×3. Unlocks map 3 and the **Pass Fort Drill Yard** (Training Ground).

## Foundation Establishment (T2) · M1

### 3. Moonlit Lake [Water] · FE 1–5
| Zone | Monsters |
|---|---|
| 1 Reed Shore | Lake Frog (Swarm, Water), Silver Heron (Swift, Metal) |
| 2 Moon Pier | Water Wraith (Caster, Water), Shell Crab (Tank, Water) |
| 3 Serpent Depths | Fang Eel (Swift, Water), Drowned Cultivator (Caster, Water) |

- **Boss: Lake Serpent** (Water, Caster). Every 10 s, Tidal Wave hits for 200% ATK and applies Slow. **Phase 2:** submerges for 3 s (untargetable), then emerges with Freeze.
- **Drops:** Gear T2 · Beast Core T2 · Spirit Grass, Iron Ore, Spirit Pearl (1%) · 5 stones/kill
- **Sig.:** Serpent Scale 50%
- **First clear:** 80 Jade, technique manual *Water Mirror Shield*. Unlocks map 4 and the **Moonlit Lake Pavilion** (Meditation Site).

### 4. Ember Hills [Fire] · FE 4–9
| Zone | Monsters |
|---|---|
| 1 Ashen Slopes | Ember Wolf (Swift, Fire), Charcoal Golem (Tank, Earth) |
| 2 Lava Vents | Fire Imp Swarm (Swarm, Fire), Flame Shaman (Caster, Fire) |
| 3 Ape Ridge | Red Ape (Brute, Fire), Magma Toad (Tank, Fire) |

- **Boss: Flame Ape** (Fire, Brute). Ground Slam: 250% ATK and Stun, every 12 s. **Phase 2:** Enrage early (at 50%) and applies Burn on every hit.
- **Drops:** Gear T2 · Beast Core T2 · Fire Lotus, Iron Ore, Ironwood · 5 stones/kill
- **Sig.:** Flame Ape Blood 30%
- **First clear:** 80 Jade, technique manual *Flame Palm*. Unlocks map 5 and the **Ember Hot Springs** (Training Ground).

### 5. Old Sect Ruins [Earth] · FE 8 – GC 3
| Zone | Monsters |
|---|---|
| 1 Broken Gate | Stone Guardian (Tank, Earth), Ruin Crow (Swift, Metal) |
| 2 Library Ash | Ink Spirit (Caster, Water), Skeleton Disciple (Swarm, Earth) |
| 3 Elder Hall | Puppet Sentinel (Tank, Metal), Grave Cultivator (Caster, Earth) |

- **Boss: Fallen Elder** (Earth, Caster, undead). Summons 3 Skeleton Disciples every 15 s. **Phase 2:** Life Drain (heals 50% of the damage dealt) until all summons are dead.
- **Drops:** Gear T2–T3 · Beast Core T2 · Purple Cloud Grass, Spirit Crystal, Manual Fragment 0.5% · 5–40 stones/kill
- **Sig.:** Elder's Manual Fragment 25% (counts as ×3 Manual Fragment)
- **First clear:** 100 Jade, manual *Azure Cloud Sutra*. Unlocks map 6 and the **Ruined Meditation Hall** (Meditation Site).

## Golden Core (T3) · M1

### 6. Thunder Peak [Metal] · GC 2–6
| Zone | Monsters |
|---|---|
| 1 Storm Steps | Thunder Goat (Brute, Metal), Static Wisp (Caster, Metal) |
| 2 Cloud Nest | Hawk Fledgling Flock (Swarm, Metal), Storm Mantis (Swift, Metal) |
| 3 Lightning Crown | Iron Thunderbird (Swift, Metal), Bronze Sentinel (Tank, Metal) |

- **Boss: Thunder Hawk** (Metal, Swift). Very high SPD and 30% Dodge. Dive: 180% ATK and Bleed. **Phase 2:** Lightning Storm deals 5% max HP per second to all for 6 s. Body stage reduces this (tribulation resist applies).
- **Drops:** Gear T3 · Beast Core T3 · Thunder Crystal, Spirit Crystal · 40 stones/kill
- **Sig.:** Thunder Hawk Blood 30%
- **First clear:** 120 Jade, manual *Flying Sword* (if not owned, otherwise 5 Manual Fragments). Unlocks map 7 and the **Thunderstruck Summit** (Training Ground).

### 7. Poison Marsh [Wood] · GC 5–9
| Zone | Monsters |
|---|---|
| 1 Rotting Banks | Swamp Leech Swarm (Swarm, Wood), Bog Lizard (Swift, Water) |
| 2 Miasma Fen | Spore Shaman (Caster, Wood), Mud Golem (Tank, Earth) |
| 3 Toad Throne | Venom Frog (Caster, Wood), Marsh Troll (Brute, Wood) |

- **Boss: Thousand-Year Toad** (Wood, Tank). A Poison aura stacks every 2 s. Tongue Lash pulls you in and Stuns. **Phase 2:** inflates (+50% DEF) and bursts at 25% HP for big Poison. Burst it fast or cleanse.
- **Drops:** Gear T3 · Beast Core T3 · Purple Cloud Grass, Phoenix Parasol Wood · 40 stones/kill
- **Sig.:** Toad Venom Sac 40%
- **First clear:** 120 Jade, 10 Refining Stones. Unlocks map 8 and the **Venom-Steeped Pools** (Training Ground).

### 8. Frozen Abyss [Water] · GC 8 – NS 2
| Zone | Monsters |
|---|---|
| 1 Ice Shelf | Frost Wolf (Swift, Water), Ice Golem (Tank, Water) |
| 2 Blizzard Rift | Snow Wraith (Caster, Water), Icicle Bats (Swarm, Water) |
| 3 Qilin's Rest | Glacier Bear (Brute, Water), Frost Witch (Caster, Water) |

- **Boss: Frost Qilin** (Water, Caster). Every hit stacks Chill. At 3 stacks: Freeze. **Phase 2:** Absolute Zero channels for 5 s. Interrupt it with a Stun or take 400% ATK.
- **Drops:** Gear T3–T4 (Heaven rarity ×2 weight) · Beast Core T3 · Snow Lotus, Ice Jade · 40–280 stones/kill
- **Sig.:** Qilin Blood 25%, Frost Qilin Horn 20%
- **First clear:** 150 Jade, Earth-rarity Talisman. Unlocks map 9 (M2) and the **Glacial Cave of Stillness** (Meditation Site).

## Nascent Soul (T4) · M2

| # | Map [Elem] · Range | Zone 1 | Zone 2 | Zone 3 |
|---|---|---|---|---|
| 9 | Crimson Desert [Fire] · NS 1–5 | Sand Scorpion (Swift, Fire), Dune Beetle (Tank, Earth) | Mirage Djinn (Caster, Fire), Sandfly Swarm (Swarm, Fire) | Desert Raider (Brute, Metal), Sunfire Lizard (Caster, Fire) |
| 10 | Ghost Mist Forest [Earth] · NS 4–9 | Wandering Ghost (Caster, Water), Hopping Corpse (Brute, Earth) | Ghost Lantern Swarm (Swarm, Fire), Tomb Golem (Tank, Earth) | Yin Puppet (Swift, Earth), Bone Priest (Caster, Earth) |
| 11 | Azure Sea Isles [Water] · NS 7 – SF 2 | Reef Shark (Swift, Water), Coral Golem (Tank, Earth) | Siren (Caster, Water), Jellyfish Bloom (Swarm, Water) | Pirate Cultivator (Brute, Metal), Tide Priest (Caster, Water) |

| # | Boss | Mechanics | Map materials | Sig. | First clear |
|---|---|---|---|---|---|
| 9 | Sand Wyrm (Fire, Brute) | Burrows (untargetable 3 s) every 15 s, emerges with an AoE Stun. P2: sandstorm, −30% your accuracy (Dodge vs you +30%) | Blood Ginseng (1%), Ice Jade, Moon Cassia Wood | Wyrm Blood 30% | 150 Jade, Spirit Beast Egg T4, unlocks **Sunscorch Dunes (Training)** |
| 10 | Corpse King (Earth, Tank) | Revives once at 30% HP. Poison claws. P2: raises 2 Hopping Corpses every 10 s | Soul Lotus, Ice Jade, Manual Fragment 1% | Yin Soul Jade 30% | 150 Jade, Earth Robe, unlocks **Yin Spirit Altar (Meditation)** |
| 11 | Kraken Matriarch (Water, Caster) | 4 tentacles (adds) each block 25% of the damage taken. Ink cloud Slow. P2: Whirlpool deals 3% HP/s | Lava Crab, Moon Pearl (2%), Spirit Crystal | Kraken Ink 40% | 200 Jade, manual fragment ×10, unlocks **Tidal Reef Platform (Training)** |

Drops (all NS maps): Gear T4 · Beast Core T4 · 280 stones/kill (×1.25/×1.5 zones 2/3).

## Soul Formation (T5) · M2

| # | Map [Elem] · Range | Zone 1 | Zone 2 | Zone 3 |
|---|---|---|---|---|
| 12 | Sky Bridge Peaks [Metal] · SF 1–5 | Cloud Crane (Swift, Metal), Peak Guardian (Tank, Earth) | Wind Blade Spirit (Caster, Metal), Eagle Flock (Swarm, Metal) | Golden Griffin (Brute, Metal), Sky Monk (Caster, Metal) |
| 13 | Scorched Volcano [Fire] · SF 4–9 | Magma Hound (Swift, Fire), Obsidian Golem (Tank, Earth) | Ember Sprites (Swarm, Fire), Fire Witch (Caster, Fire) | Lava Giant (Brute, Fire), Salamander Guard (Tank, Fire) |
| 14 | Spirit Beast Plains [Wood] · SF 7 – VB 2 | Thunderhoof Bison (Brute, Wood), Grass Serpent (Swift, Wood) | Wolf Pack (Swarm, Wood), Elder Stag (Caster, Wood) | Ironhide Rhino (Tank, Earth), Ape Warrior (Brute, Wood) |

| # | Boss | Mechanics | Map materials | Sig. | First clear |
|---|---|---|---|---|---|
| 12 | Golden Roc (Metal, Swift) | 40% Dodge. Feather Storm: 6 hits of 50% ATK with Bleed. P2: flies (only Qi arts can hit it for 5 s) | Starsilver, Thunderstruck Peach Wood, Star Shrimp | Roc Feather 40%, Roc Blood 25% | 200 Jade, Heaven Boots, unlocks **Cloud Sea Peak (Meditation)** |
| 13 | Lava Salamander Lord (Fire, Tank) | A Burn aura stacks. Molten Shell: Shield 20% HP every 20 s. P2: the lava floor rises, 2% HP/s until killed | Blood Ginseng, Starsilver | Salamander Heart 30% | 200 Jade, manual fragment ×10, unlocks **Volcano Crater Forge (Training)** |
| 14 | Ancient Ape Sovereign (Wood, Brute) | Chest Beat: buffs self +20% ATK per stack (max 5). P2: summons Ape Warriors. Kill them to remove stacks | Blood Ginseng, Thunderstruck Peach Wood | Sovereign Blood 30% | 250 Jade, Spirit Beast Egg T5, unlocks **Primal Spirit Spring (Meditation)** |

Drops: Gear T5 · Beast Core T5 · 2K stones/kill.

## Void Breaking (T6) · M2

| # | Map [Elem] · Range | Zone 1 | Zone 2 | Zone 3 |
|---|---|---|---|---|
| 15 | Shattered Realm [Earth] · VB 1–5 | Rift Crawler (Swift, Earth), Floating Rock Golem (Tank, Earth) | Void Moth Swarm (Swarm, Water), Space Tearer (Caster, Metal) | Gravity Beast (Brute, Earth), Void Sentinel (Tank, Earth) |
| 16 | Star Sea Ruins [Water] · VB 4–9 | Starfish Swarm (Swarm, Water), Astral Ray (Swift, Water) | Sunken Star Priest (Caster, Water), Ruin Colossus (Tank, Earth) | Comet Shark (Swift, Water), Abyssal Knight (Brute, Metal) |
| 17 | Demon Border [Fire] · VB 7 – MA 2 | Imp Horde (Swarm, Fire), Hellhound (Swift, Fire) | Demon Cultivator (Caster, Fire), Bone Fiend (Brute, Earth) | Demon Vanguard (Tank, Metal), Blood Witch (Caster, Fire) |

| # | Boss | Mechanics | Map materials | Sig. | First clear |
|---|---|---|---|---|---|
| 15 | Void Golem (Earth, Tank) | Very high DEF (Armor Pierce matters). Gravity Well Stuns every 15 s. P2: splits into 2 half-HP golems | Void Stone, Void Willow | Void Core 30% | 250 Jade, Dao Pattern Stone ×3, unlocks **Void Rift Edge (Training)** |
| 16 | Star-Eater Leviathan (Water, Brute) | Devour: 300% ATK, heals 20%. Starfall AoE. P2: swallows your pet for 6 s (no pet assist) | Star Orchid, Void Angler, Star Pearl (2%) | Leviathan Blood 25% | 250 Jade, Heaven Ring, unlocks **Starlight Observatory (Meditation)** |
| 17 | Demon General (Fire, Brute) | Demonic Aura: −20% your healing. Cleave + Burn. P2: Blood Pact, ATK grows +10% every 10 s (DPS race) | Star Orchid, Void Stone | Demon Seal 30% | 300 Jade, manual fragment ×15, unlocks **Demon-Slaying Wall (Training)** |

Drops: Gear T6 · Beast Core T6 · 14K stones/kill.

## Mahayana (T7) · M3

| # | Map [Elem] · Range | Zone 1 | Zone 2 | Zone 3 |
|---|---|---|---|---|
| 18 | Heavenly Sword Tomb [Metal] · MA 1–5 | Flying Sword Spirit (Swift, Metal), Sword Puppet (Tank, Metal) | Broken Blade Swarm (Swarm, Metal), Sword Ghost (Caster, Metal) | Sword Saint Remnant (Brute, Metal), Blade Sentinel (Tank, Metal) |
| 19 | Primordial Jungle [Wood] · MA 4–9 | Thorn Panther (Swift, Wood), Moss Titan (Tank, Earth) | Spore Bloom (Swarm, Wood), Vine Witch (Caster, Wood) | Primeval Tyrant Lizard (Brute, Wood), Ancient Beetle (Tank, Wood) |
| 20 | Abyssal Rift [Water] · MA 7 – GA 1 | Abyss Eel (Swift, Water), Pressure Golem (Tank, Water) | Drowned Legion (Swarm, Water), Deep Oracle (Caster, Water) | Dragonspawn (Brute, Water), Dragon Guard (Tank, Metal) |

| # | Boss | Mechanics | Map materials | Sig. | First clear |
|---|---|---|---|---|---|
| 18 | Sword Wraith Emperor (Metal, Swift) | Ten Thousand Swords: hits = your equipped combat arts × 3. Reflects 20% of Qi damage. P2: copies your strongest art | Dragon-Vein Jade, World Tree Branch | Sword Intent Shard 30% | 300 Jade, Heaven-rarity Sword Wraith Twin Edges (5% chance: Immortal), unlocks **Sword Intent Cliff (Meditation)** |
| 19 | Elder Treant (Wood, Tank) | Regenerates 2% HP/s (Burn stops the regen). Root: Stun. P2: spawns saplings that heal it | World Tree Branch, Nine-Leaf Immortal Grass (0.5%) | Treant Heartwood 30% | 300 Jade, Spirit Beast Egg T7, unlocks **World Tree Roots (Training)** |
| 20 | Abyss Dragon (Water, Brute) | Dragon Breath: 350% ATK and Freeze. Scales: −50% physical damage. P2: Tidal Dragon Form, +SPD | Dragon-Vein Jade, Dragon Carp, Dragon Pearl (1%) | Dragon Blood 25% | 400 Jade, Heaven Robe, unlocks **Dragon's Breath Chasm (Meditation)** |

Drops: Gear T7 · Beast Core T7 · 100K stones/kill.

## Great Ascension, early (GA 1–4, T8) · M3

| # | Map [Elem] · Range | Zone 1 | Zone 2 | Zone 3 |
|---|---|---|---|---|
| 21 | Celestial Ruins [Earth] · GA 1–3 | Fallen Guardian (Tank, Earth), Celestial Hound (Swift, Metal) | Star Fragment Swarm (Swarm, Earth), Ruin Sage (Caster, Earth) | Titan Statue (Brute, Earth), Heaven Soldier (Tank, Metal) |
| 22 | Phoenix Nest [Fire] · GA 2–5 | Sun Crow (Swift, Fire), Ember Golem (Tank, Fire) | Phoenix Chick Flock (Swarm, Fire), Flame Priestess (Caster, Fire) | Rebirth Flame Beast (Brute, Fire), Nest Warden (Tank, Earth) |
| 23 | Thunder Sea [Metal] · GA 4–6 | Storm Eel (Swift, Water), Thunder Turtle (Tank, Metal) | Lightning Jelly Swarm (Swarm, Metal), Storm Caller (Caster, Metal) | Thunder Ox (Brute, Metal), Kirin Guard (Tank, Metal) |

| # | Boss | Mechanics | Map materials | Sig. | First clear |
|---|---|---|---|---|---|
| 21 | Fallen Celestial (Earth, Caster) | Heavenly Seal: silences combat arts for 4 s. P2: summons Heaven Soldiers, judgement beam 400% | Dragon-Vein Jade, Nine-Leaf Immortal Grass (0.5%) | Celestial Feather 30% | 400 Jade, Dao Pattern Stone ×10, unlocks **Celestial Palace Courtyard (Training)** |
| 22 | Vermilion Phoenix (Fire, Caster) | Burn on every hit. **Rebirths once** at full HP unless killed within 10 s of P2 starting. P2: wing storm | Nine-Leaf Immortal Grass (1%), World Tree Branch | Phoenix Blood 25% | 400 Jade, Spirit Beast Egg T8, unlocks **Phoenix Flame Altar (Meditation)** |
| 23 | Thunder Kirin (Metal, Swift) | Chain Lightning, Stun. Tribulation resist applies to all its damage. P2: Thunder Domain, 4% HP/s | Dragon-Vein Jade, Dragon Pearl (1%) | Kirin Blood 25% | 500 Jade, Thunder Essence ×5, unlocks **Tribulation Lightning Field (Training)** |

Drops: Gear T8 · Beast Core T8 · 700K stones/kill.

## Great Ascension, late (GA 5–9, T9) · M3

| # | Map [Elem] · Range | Zone 1 | Zone 2 | Zone 3 |
|---|---|---|---|---|
| 24 | Nine Heavens Stair [Metal] · GA 5–7 | Heavenly Soldier (Tank, Metal), Cloud Rider (Swift, Metal) | Heaven Archer Squad (Swarm, Metal), Thunder Sage (Caster, Metal) | Golden Armored Giant (Brute, Metal), Gate Warden (Tank, Earth) |
| 25 | Chaos Wastes [Earth] · GA 6–9 | Chaos Spawn Horde (Swarm, Earth), Warped Beast (Swift, Fire) | Chaos Sorcerer (Caster, Water), Primordial Golem (Tank, Earth) | Devourer Spawn (Brute, Earth), Chaos Knight (Tank, Metal) |
| 26 | Heaven's Gate [All] · GA 8–9 | Dao Guardian (Tank, rotating), Fate Weaver (Caster, rotating) | Karma Wraiths (Swarm, rotating), Heavenly Blade (Swift, Metal) | Celestial Executor (Brute, rotating), Gate Lion (Tank, Earth) |

| # | Boss | Mechanics | Map materials | Sig. | First clear |
|---|---|---|---|---|---|
| 24 | Heavenly General (Metal, Brute) | Commands: adds buff him +10% each. Armor Break. P2: Heaven's Decree, −30% all your stats for 8 s | Dragon-Vein Jade, Nine-Leaf Immortal Grass (1%) | General's Seal 30% | 500 Jade, Immortal-rarity roll (10%), unlocks **Nine Heavens Terrace (Meditation)** |
| 25 | Taotie the Devourer (Earth, Tank) | Devours your buffs and Shields (heals from them). P2: Endless Hunger, grows +5% stats every 10 s | Dragon-Vein Jade, World Tree Branch | Chaos Essence 25% | 500 Jade, Dao Pattern Stone ×20, unlocks **Chaos Crucible (Training)** |
| 26 | Heavenly Dao Avatar (All, Caster) | Element rotates every 20 s. Mirrors the strongest stat of yours. P2: Judgement, damage scales with your rebirth count (small) | Nine-Leaf Immortal Grass (2%) | Dao Fragment 20% | 1,000 Jade, title "Gatecrasher of Heaven", unlocks **Summit of Heaven (Meditation + Training)** |

Drops: Gear T9 · Beast Core T9 · 5M stones/kill.

---

## Decisions
- Combat is **fully automatic** (no manual skill timing).
- Retreat point 30% / resume point **100%** by default.
- Healing Pills auto-use in battle only.
- Boss respawn stays at 10 min (tune in the balancing spreadsheet).
- Signature drops have bad-luck protection (guaranteed by kill ≈ 2 ÷ rate).
- No manual interrupt button at launch.
- Pet capture is boss-only.
