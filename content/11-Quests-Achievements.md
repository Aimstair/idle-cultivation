# 11 — Quests, Achievements, Titles & Login Rewards

Names follow [00-Registry](00-Registry.md). Rewards use registry currencies and materials only.

---

## 1. Daily Quests (unlock: FE 1 · Milestone: M2)
- Each day at the **fixed server reset time for your region**, **5 quests** are drawn from the pool below. Only quests whose system is unlocked can be drawn.
- **Reward scaling:** Spirit Stone rewards scale with the player's realm (`× realm tier`). Material rewards use the player's current tier (T#).
- Completing all 5 also gives **+20 Jade** and **1 Weekly Chest point**.
- **Reroll:** 1 free reroll per day. A rewarded ad gives +1 more (counts toward the ad caps in [05-Monetization](../05-Monetization.md)).

| # | Quest | Requires | Reward |
|---|---|---|---|
| 1 | Break through 3 Qi levels | — | Spirit Stones ×S, Qi Gathering Pill ×1 |
| 2 | Use Meditation boost 5 times | — | Spirit Stones ×S |
| 3 | Defeat 200 monsters | Combat | Spirit Stones ×S, Beast Core (T#) ×5 |
| 4 | Defeat any map boss 3 times | Combat | Refining Stone ×3 |
| 5 | Collect offline gains once | — | Jade ×5 |
| 6 | Mine 50 ore | Mining | Ore (T#) ×10 |
| 7 | Craft 3 pills | Alchemy | Spirit Grass ×10 |
| 8 | Break through 1 body layer **or** gain 2 exercise mastery levels | Body | Medicinal Bath ×1 |
| 9 | Use 1 Medicinal Bath | Body | Tempering burst (10 min of training) |
| 10 | Enhance gear 3 times | Forging | Refining Stone ×3 |
| 11 | Salvage 10 items | Forging | Spirit Stones ×S |
| 12 | Cut 50 wood | Woodcutting | Wood (T#) ×10 |
| 13 | Run 2 dungeon entries | Dungeon 1 | Refining Stone ×5 |
| 14 | Catch 30 fish | Fishing | Fish (T#) ×5 |
| 15 | Cook 3 meals | Cooking | Spirit Rice ×10 |
| 16 | Climb 3 Trial Tower floors (or attempt 3 times) | Trial Tower | Spirit Stones ×2S |
| 17 | Feed your pet 3 times | Pets | Beast Core (T#) ×5 |
| 18 | Harvest 3 Spirit Field plots | Spirit Fields | 1 random herb seed (≤ your Farming level) |
| 19 | Attempt a Qi breakthrough **or** Tribulation | Level 9 reached | Insight ×1 |
| 20 | Contribute to your Sect once | Sect | Sect Merit ×50 |
| 21 | Use 2 restoration pills (Healing / Qi Recovery) | Alchemy | Meridian Mending Pill ×1 |

`S` = 500 × realm tier Spirit Stones (tune in balancing sheet).

## 2. Weekly Chest (Milestone: M2)
- Earn **1 point per day** when all 5 dailies are done (max 7).

| Points | Reward |
|---|---|
| 2 | Spirit Stones ×10S, Refining Stone ×10 |
| 4 | Manual Fragment ×3, Jade ×30 |
| 6 | Spirit Beast Egg (T#) ×1 **or** Dao Pattern Stone ×1 (from VB) |
| 7 | Jade ×50, a random gear piece of **Earth** rarity or better at the current tier |

## 3. Main Quest Line: "Path of Cultivation" (Milestone: M1 for MO–GC steps, M2+ for later realms)
A permanent guided chain, always shown on the Home screen as **one** next objective. It doubles as the tutorial after the first 10 minutes. Rewards are generous early to smooth onboarding.

| Chapter | Steps (examples) | Chapter reward |
|---|---|---|
| **1. The Lowly Disciple** (MO–QS) | Reach MO 5 · Defeat 10 monsters in Misty Bamboo Grove · Buy or equip a sword · Reach QC 1 · Start Stone Lifting · Mine 20 Copper Ore · Defeat Bamboo Viper King · Reach QS 9 (**gift: 1 Foundation Pill**, a safety net) · Craft your first Foundation Pill | Spirit gear Weapon, Jade ×50 |
| **2. Laying the Foundation** (FE) | Break through to FE · Clear Bandit Pass · Forge an item · Clear Spirit Vein Cave once · Complete Copper Skin · Defeat Flame Ape · Craft a Golden Core Pill | Earth Talisman, Medicinal Bath ×3 |
| **3. Forming the Core** (GC) | Survive Tribulation I · Reach Mining 40 · Complete Iron Bone · Defeat Thunder Hawk · Clear Trial Tower floor 10 · **View the Rebirth screen** (no need to rebirth) · Craft a Nascent Pill | Jade ×100, Insight ×3 |
| **4. Birth of the Nascent Soul** (NS) | Survive Tribulation II · Hatch your first pet · Plant a Spirit Field · Defeat Corpse King · Complete Silver Marrow | Spirit Beast Egg (T4), Jade ×100 |
| **5. Forging the Soul** (SF) | Survive Tribulation III · Join a Sect · Defeat Golden Roc · Equip 3 combat arts | Heaven-rarity item (random slot) |
| **6–9.** Void Breaking → Great Ascension (VB, MA, GA early, GA late) | Same pattern: survive tribulation, clear the realm's 3 maps and dungeon, a body milestone, craft the next gate pill | Jade, gear, Karma ×1 per chapter |
| **10. Ascension** (M3+) | Survive Heavenly Dao Judgement | Title "Immortal", ascension cosmetic |

- **Rebirth behavior:** the main quest **does not reset** on rebirth. Completed chapters stay completed, and each new life instead shows the "Reincarnation Journey" side line: reach your previous highest realm → +Karma ×1 (M2).

## 4. Achievements (unlock: GC 1 · Milestone: M2)
Permanent goals with small **permanent bonuses** that persist through rebirth (they're stored in "eternal" data). Bonuses are additive and add up to **+300% Qi in total** (×4 Qi with every achievement), a long-term chase. Individual Qi bonuses range from +3% to +33%. The balancing spreadsheet counts the expected achievement bonus at each realm inside `EXT`.

### Cultivation (Qi)
| Achievement | Goal | Bonus |
|---|---|---|
| First Breath | Reach QC | +3% Qi |
| Boundless Sea | Reach QS | +3% Qi |
| Foundation Laid | Reach FE | +6% Qi |
| Golden Core | Reach GC | +13% Qi |
| Nascent Soul | Reach NS | +13% Qi |
| Soul Forged | Reach SF | +20% Qi |
| Beyond the Void | Reach VB | +20% Qi |
| Mahayana | Reach MA | +20% Qi |
| On the Brink | Reach GA | +25% Qi |
| Stubborn Heart | Fail 10 breakthroughs | +2% breakthrough chance |
| Heaven-Defying | Succeed at a breakthrough under 30% chance | +1% breakthrough chance |
| Endless Meditation | Use Meditation 1,000 times | +5% Meditation strength |
| Bitter Lesson | Survive your first injury (Qi Deviation or Internal Injury) | +10% injury recovery speed |
| Razor's Edge | Break through with **exactly enough** (≤1% of the cost to spare) | +6% Qi |
| Brimming Vessel | Break through 50 times with a completely full pool | +2% Max Qi |
| Closed-Door Hermit | Spend 24 h total Meditating | +13% Qi rate |
| Iron Discipline | Spend 24 h total Training | +2% Tempering |

### Body
| Achievement | Goal | Bonus |
|---|---|---|
| Copper Skin | Complete Copper Skin | +1% HP |
| Iron Bone | Complete Iron Bone | +1% DEF |
| Silver Marrow | Complete Silver Marrow | +2% HP |
| Jade Flesh | Complete Jade Flesh | +2% DEF |
| Golden Body | Complete Golden Body | +3% HP |
| Diamond Vajra | Complete Diamond Vajra Body | +3% DEF |
| Well-Rounded | All exercises to mastery 25 | +3% Tempering |
| Grandmaster of the Body | Any exercise to mastery 99 | +5% that exercise's stat |
| Bath Lover | Use 100 Medicinal Baths | +10% bath duration |
| Unbroken Body | Farm 1 h straight without an auto-retreat | +2% Max HP |
| Perfect Routine | Run a 3-step Routine for 8 h straight without an injury | +5% base regen |

### Rebirth
| Achievement | Goal | Bonus |
|---|---|---|
| A New Life | Rebirth once | +1% Tempering |
| Old Soul | Rebirth 5 times | +13% Qi |
| Eternal Wanderer | Rebirth 20 times | +20% Qi |
| Prodigy Reborn | Reach your previous highest realm within 50% of your previous life's time | +13% Qi |
| Deep Root | Rebirth from VB or later | Karma ×2 (one-time) |

### Combat
| Achievement | Goal | Bonus |
|---|---|---|
| First Blood | Defeat 100 monsters | +1% ATK |
| Slayer | Defeat 10,000 monsters | +2% ATK |
| Calamity | Defeat 1,000,000 monsters | +3% ATK |
| Boss Hunter | Defeat every boss on maps 1–8 | +2% boss damage |
| Bane of Beasts | Defeat every boss on maps 9–17 | +3% boss damage |
| Heaven's Executioner | Defeat every boss on maps 18–26 | +5% boss damage |
| Viper's Bane | Defeat Bamboo Viper King 100 times | +1% Wood resist |
| Five Phases | Clear one map of each element | +2% element damage |
| Untouchable | Win a boss fight without taking damage | +1% Dodge |
| Thunder Walker | Win 3 tribulations on the first try | +3% lightning resist |
| Tower Climber | Trial Tower floor 50 | +2% all stats |
| Tower Master | Trial Tower floor 200 | +3% all stats |

### Equipment & Dungeons
| Achievement | Goal | Bonus |
|---|---|---|
| Lucky Find | Obtain a Heaven item | +1% drop rarity |
| Immortal's Favor | Obtain an Immortal item | +2% drop rarity |
| Master Smith | Enhance an item to +15 | +5% enhance success (failures are non-destructive, see [05-Equipment](05-Equipment.md)) |
| Hoarder's Regret | Salvage 200 items manually | Unlocks auto-salvage filters (see [05-Equipment](05-Equipment.md)) |
| Recycler | Salvage 1,000 items | +5% salvage yield |
| Dungeon Diver | Clear 100 dungeon runs | +1 dungeon entry stored (cap) |
| Secret Realm Conqueror | Clear D1–D5 at max tier | +2% all stats |

### Life Skills (one per skill per threshold: 25 / 50 / 75 / 99)
| Achievement | Goal | Bonus |
|---|---|---|
| Miner I–IV | Mining 25 / 50 / 75 / 99 | +2/3/4/5% Mining speed |
| Woodcutter I–IV | Woodcutting 25 / 50 / 75 / 99 | +2/3/4/5% Woodcutting speed |
| Angler I–IV | Fishing 25 / 50 / 75 / 99 | +2/3/4/5% Fishing speed, +rare-catch chance at IV |
| Farmer I–IV | Farming 25 / 50 / 75 / 99 | +2/3/4/5% growth speed |
| Alchemist I–IV | Alchemy 25 / 50 / 75 / 99 | +2/3/4/5% pill success |
| Chef I–IV | Cooking 25 / 50 / 75 / 99 | +5/10/15/20% meal duration |
| Smith I–IV | Forging 25 / 50 / 75 / 99 | +2/3/4/5% forge quality |
| Jack of All Trades | All 7 life skills to 50 | +1 worker slot |

### Collection
| Achievement | Goal | Bonus |
|---|---|---|
| Beast Tamer | Own 5 pets | +2% pet stats |
| Menagerie | Own every pet | +5% pet stats |
| Scholar | Learn 10 techniques | +2% Comprehension gain |
| Library of the Dao | Learn every technique | +33% Qi |
| Pill Encyclopedia | Craft every pill once | +3% pill effect |
| Gourmet | Cook every meal once | +5% meal effect |
| Sword Collector | Own one sword of each type (Jian, Saber, Greatsword, Twin, Flying) | +2% Damage |
| Hundred Blades | Own 30 different named swords (any tier) | +3% Damage |
| Legend Bearer | Own a legendary sword | +3% Crit Dmg |
| Sword Saint's Armory | Own every legendary sword | +5% Damage, title "Sword Saint" |
| Wanderer of Grounds | Unlock 5 Cultivation Grounds | +13% Qi and Tempering |
| Master of Grounds | Unlock 13 Cultivation Grounds | +20% Qi and Tempering |
| Heaven and Earth Are My Home | Unlock every Cultivation Ground | +33% Qi and Tempering |
| In Harmony | Meditate 1 h at a Meditation Site matching your cultivation method's element | +13% Qi |

### Social & Misc
| Achievement | Goal | Bonus |
|---|---|---|
| Sect Disciple | Join a Sect | +1% Sect Merit |
| Pillar of the Sect | Contribute 10,000 Sect Merit | +3% Sect Merit |
| Faithful | 30 login days (not consecutive) | Jade ×200 |
| Patient Cultivator | Collect 8 h of offline gains in one return | +1% offline efficiency (combat) |

Count: 9 + 3 + 9 + 5 + 12 + 6 + 29 (7 skills × 4 + Jack) + 6 + 4 ≈ **83 achievements** (≈60 with bonuses besides the tiered life-skill ones).

## 5. Titles (Milestone: M2)
- One title equipped at a time. It shows above the character and on leaderboards.
- Each title gives a **small stat bonus** (≤ +3%). Cosmetic-only titles are sold for Jade or come from events.

| Title | Source | Bonus |
|---|---|---|
| Outer Disciple | Start | — |
| Inner Disciple | Reach FE | +1% Qi |
| Core Disciple | Reach GC | +1% Qi, +1% HP |
| Elder | Reach NS | +2% Qi |
| Grand Elder | Reach SF | +2% Qi, +2% HP |
| Sect Master | Reach VB (or lead a Sect for 30 days) | +3% Qi |
| Thunder-Tempered | Win 7 tribulations | +3% lightning resist |
| Diamond Body | Complete Diamond Vajra Body | +3% DEF |
| Thousand-Life Wanderer | Rebirth 20 times | +3% Tempering |
| Tower Lord | Top 100 Trial Tower (season) | +2% all stats (season only) |
| Master Alchemist | Alchemy 99 | +3% pill success |
| Immortal | Ascension | +3% all stats |
| Lantern Bearer, Moon Gazer… | Events (see [13-Sect-Events](13-Sect-Events.md)) | Cosmetic |

## 6. Login Rewards (Milestone: M1 for 7-day, M2 for 28-day)

### Newcomer 7-day calendar (one-time, for new players)
| Day | Reward |
|---|---|
| 1 | Spirit Stones ×1,000, Qi Gathering Pill ×3 |
| 2 | Medicinal Bath ×2 |
| 3 | Jade ×50 |
| 4 | Refining Stone ×10 |
| 5 | Spirit gear set piece (Boots) |
| 6 | Insight ×3 |
| 7 | **Earth-rarity Jian** + Jade ×100 |

### Monthly 28-day calendar (repeating)
- Missing a day doesn't reset progress. The calendar just advances by login count (respectful idling).
- Days 7, 14, 21, and 28 are bigger rewards. Day 28 is a choice of Spirit Beast Egg (current tier) or a cosmetic robe for that month.
- Rewards: Spirit Stones, Jade (≈300 total per cycle), pills, Refining Stones, Manual Fragments.

## Decisions
- Daily quests reset at a **fixed server time per region** (works for Sects and events).
- The "watch an ad" daily quest is **removed**, keeping the "ads are always your choice" promise.
- Achievement Qi bonuses total **+300%** (rescaled above).
- Master Smith: enhancement can fail (non-destructively) per [05-Equipment](05-Equipment.md), so +5% success is meaningful.
