# 13 — Sect, Events, Leaderboards & Battle Pass

Online features. They need a backend (an open question in [06-Tech](../06-Tech.md), parked). All of them are **M3** unless tagged otherwise.

---

## 1. Sect (Guild)
**Unlock:** SF 1 (per [00-Registry](00-Registry.md)). **Size:** 30 members (raised to 50 via the Sect tech tree).

### Joining & creating
| Action | Rules |
|---|---|
| Browse / search | List of Sects with name, level, member count, language, minimum realm |
| Join | Instant if "Open". Request if "Approval". Hidden if "Invite only" |
| Create | Requires SF 1 + Spirit Stones (large sink) **or** 500 Jade. Choose name, emblem, and motto |
| Leave | 24 h cooldown before joining another Sect. Personal Sect Merit is kept |
| Inactive members | Leaders can kick members inactive for 7+ days. Leadership passes automatically after 14 days of leader inactivity |

### Ranks
| Rank | Count | Permissions |
|---|---|---|
| Sect Master | 1 | Everything, disband, transfer |
| Elder | Up to 3 | Accept/kick, start Sect Boss, choose tech research |
| Inner Disciple | — | Full participation |
| Outer Disciple | — | New members (first 3 days): can contribute, reduced shop access |

### Contributions (earn **Sect Merit** personally + **Sect EXP** for the Sect)
| Activity | Frequency | Merit | Sect EXP |
|---|---|---|---|
| Daily sign-in | 1/day | 20 | 10 |
| Donate Spirit Stones | 3/day | 30 each | 20 each |
| Donate materials (current tier) | 3/day | 40 each | 25 each |
| Sect Boss attack | 3/day | By damage dealt | By damage dealt |
| Sect mission (shared task: "members defeat 50,000 monsters this week") | Weekly | 300 | 500 |

### Sect Shop (spend Sect Merit)
| Item | Cost | Limit |
|---|---|---|
| Manual Fragment ×5 | 200 | Weekly ×3 |
| Dao Pattern Stone | 500 | Weekly ×2 |
| Spirit Beast Egg (current tier) | 1,500 | Weekly ×1 |
| Gate pill materials (current realm) | 300 | Weekly ×2 |
| Sect cosmetic robe, emblem frame | 3,000 | One-time |
| Insight ×3 | 250 | Weekly ×1 |
| **Heaven-rarity sword** (Jian or Saber of your tier, random affixes) | 4,000 | Monthly ×1 (Sect level 10+) |

Shop tiers unlock with the **Sect level** (1–20).

### Co-op Sect Boss
- **Weekly world boss** for the Sect, rotating among the map bosses at elevated tiers (for example, Frost Qilin ×50 HP).
- Each member has **3 attacks per day**. Each attack is a 30-second simulated fight using their stats, and damage dealt is recorded.
- Shared HP bar. Damage milestones (25 / 50 / 75 / 100%) unlock a Sect-wide chest for everyone who attacked at least once.
- Personal reward is scaled by personal damage rank within the Sect.
- If the boss is killed, the next week's boss is +1 tier.

### Sect Tech Tree (researched with Sect EXP; Elders choose)
| Branch | Nodes (examples) | Max effect |
|---|---|---|
| Cultivation Hall | +Qi rate, +breakthrough chance | +10% Qi, +3% chance |
| Body Hall | +Tempering, +bath duration | +10% Tempering |
| Martial Hall | +ATK, +HP, +Sect Boss damage | +5% ATK/HP |
| Hall of Crafts | +life-skill speed, +pill success | +10% speed |
| Administration | Member cap 30 → 50, shop tiers | — |

Tech bonuses apply only **while you're a member**.

### Sect Grounds (with Sects, M3)
- Each Sect can build a **Sect-owned Meditation Site / Training Ground** shared by all members (see [15-Cultivation-Grounds](15-Cultivation-Grounds.md)). Its multiplier is upgraded with Sect EXP. Upkeep is paid from the Sect treasury, not by members.

### Friends (with Sects, M3)
- A simple **Friends list** (unlocks GC 1) arrives with the Sect update: send and receive daily gifts (small Spirit Stones or Qi pill), and a friends filter on leaderboards. At v1.0, social play is leaderboards only.

## 2. Events
All events are **opt-in**, with no exclusive *power*. Exclusive *cosmetics* and titles are fine. Unused Event Tokens convert to Spirit Stones at the end.

### Weekly (Milestone: M2)
| Day | Event | Mechanic |
|---|---|---|
| Mon–Thu | — | Normal play |
| Fri–Sun | **Secret Realm Weekend** | +1 free dungeon entry per day |
| Sat | **Abundant Harvest** | +50% life-skill output |
| Sun | **Heavenly Alignment** | +10% breakthrough chance |

### Monthly (one rotating 7-day event)
| Event | Mechanic | Rewards |
|---|---|---|
| **Beast Tide** | Special event map with waves of beasts. Kills give Event Tokens | Pet skin, Spirit Beast Egg |
| **Alchemy Contest** | Craft pills to score points. Rare pills score more | Alchemy title, furnace cosmetic |
| **Tower Rush** | Trial Tower floors give double tokens | Tower Lord frame |
| **Great Fishing Festival** | Fishing ranks by rarest catch | Fishing rod cosmetic, Pearls |
| **Demon Invasion** | Sect-wide: defeat the Demon General's army (map 17 monsters at your tier) | Sect cosmetic, Sect Merit |

### Seasonal Festivals (2–3 weeks each)
| Festival | Timing | Mechanic | Exclusive rewards |
|---|---|---|---|
| **Lantern Festival** | Lunar New Year | Light lanterns (log in, defeat bosses) → token shop | "Lantern Bearer" title, red robe, legendary **Moonlight Lantern Sword** (token track) |
| **Qingming Spirit Walk** | April | Ghost Mist Forest themed map, Yin Soul Jade drops at your tier | Ghost-fire aura |
| **Dragon Boat** | June | Race event: mini-ranking by kills per hour | Dragon-boat pet skin, legendary **Riverdragon Jian** (event kill-count milestone, not ranking) |
| **Mid-Autumn Moon** | Sep–Oct | Mooncake cooking recipes, Moon Pearl fishing boost | "Moon Gazer" title, Jade Rabbit skin |
| **Winter Solstice Tribulation** | December | Special tribulation challenge (survive N lightning strikes) | Thunder aura |

## 3. Leaderboards (Milestone: M2, live at launch)
| Board | Metric | Reset | Rewards |
|---|---|---|---|
| Realm | Highest realm + level in the current life, tie-break by time | Never (all-time) + seasonal | Title frame for Top 100 |
| Power | Combat power score | Seasonal (6 weeks) | Jade, title |
| Trial Tower | Highest floor | Weekly | Jade, Tower Lord title (Top 100) |
| Sect | Sect level + Sect Boss damage | Weekly | Sect chest |
| Rebirths | Total Qi multiplier | All-time | Cosmetic only |

**Anti-cheat:**
- Leaderboard submissions only come from a **cloud-validated save**. The server checks time progression against its own clock and rejects impossible growth (for example, more Qi than the max rate × elapsed time).
- Trial Tower and Sect Boss fights are **re-simulated on the server** from the seeded RNG and stats (deterministic sim; see [06-Tech](../06-Tech.md)).
- Suspicious accounts are shadow-banned from boards. Their single-player game is unaffected.

**Scope at launch:** **global** boards with a friends filter (once friends exist). Regional seasonal boards come later, only if the global ones feel too crowded.

## 5. Player Marketplace (future, post-launch)
**Outline only.** Full spec when it's scheduled.
- **What:** an auction-house-style market where players list items for others to buy.
- **Currency:** **Spirit Stones only.** Jade can't be used, which avoids pay-to-win and real-money trading.
- **Tradeable:** materials (ores, herbs, bloods, Beast Cores), unbound gear and swords, Spirit Beast Eggs, seeds.
- **Not tradeable (bound):** anything bought with Jade or real money, legendary swords, quest and achievement rewards, pets once hatched.
- **Rules:**
  - A 5–10% listing tax (a Spirit Stone sink).
  - Unlocks at Golden Core (blocks throwaway bot accounts).
  - A daily listing cap.
  - Price bands per item tier, to stop "gift" trades that shift wealth between accounts.
- **Needs:** server-authoritative inventory for traded items, plus anti-bot and anti-fraud checks. The backend built for cloud save and leaderboards is the foundation.
- **Open questions:** cross-server or regional markets? Should Sect members get a private Sect market?

## 4. Battle Pass: "Path of the Season" (Milestone: M3)
- **Season length:** 6 weeks. **50 tiers.** XP comes from daily quests, events, and Trial Tower floors (not from spending).
- **Free track:** Spirit Stones, materials, Refining Stones, Jade ×300 total, 1 cosmetic.
- **Paid track ($4.99):** seasonal cosmetics (robe, aura, pet skin, title), extra materials and Jade (≈ 1,000). It must **not** include exclusive power gear, Karma, or Qi.
- The theme rotates with the current seasonal festival.
- Tier skips are purchasable with Jade (max 10 per season).

## Decisions
- The Sect stays at **SF 1**. At v1.0, social play is leaderboards. A Friends list + gifts arrive with Sects post-launch.
- Sect Bosses are **async** (attack on your own schedule).
- Leaderboards are **global** at launch (friends filter later). Regional seasons only if needed.
- Battle pass is **post-launch** (M3).
- A **Sect-owned shared ground** comes with Sects.
