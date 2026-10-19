# 05 — Monetization

**Model:** free-to-play, with **rewarded ads + light IAP**. Our promise to players: *ads are always your choice, and money never buys realms.*

## Rewarded Ads (opt-in only)
| Placement | Reward | Daily cap | Unlock |
|---|---|---|---|
| Offline return | 2× offline collection | 3 | After the first offline return |
| Breakthrough | +10% success chance | 1 per attempt | First breakthrough |
| Dungeon | +1 entry | 2 | Dungeon 1 |
| Qi Surge | 2× Qi rate for 2 h (stacks duration, max 6 h) | 3 | Day 1 |
| Field / job speed-up | −30 min on one timer | 5 | Spirit Fields / life skills |
| Daily chest | Bonus stones and materials | 1 | Day 2 |

There are **no "watch an ad" daily quests**, keeping the "ads are always your choice" promise.

**Targets:** 3–6 ads per DAU among engaged players. Placements are surfaced with a calm button, never a pop-up.

## Interstitial / Banner Ads
**None.** They conflict with Pillar 4 (respectful idling) and hurt retention in this genre. We may revisit only if ARPDAU from rewarded ads is far below target.

## In-App Purchases
| Product | Price (USD) | Contents | Notes |
|---|---|---|---|
| **Remove Ads** | $4.99 | All rewarded-ad rewards granted instantly (no watching) | Best-value first purchase in the genre |
| **Starter Pack** | $0.99 | Spirit gear set, 3 Qi Gathering Pills, 300 Jade | One-time, shown after day 1 |
| **Monthly Jade Card** | $4.99 / 30 days | 100 Jade per day on login + 10% Qi | Main recurring revenue |
| **Immortal Cave** | $9.99 | Offline cap 8 h → 12 h, +1 worker slot | Permanent, high-value |
| **Jade packs** | $0.99–$49.99 | 60 → 3,600 Jade | Standard ladder |
| **Cosmetics** | Jade | Robes, auras, pet skins | Pure cosmetic |
| **Battle Pass (M3)** | $4.99 / season | Seasonal cosmetics + materials track | Post-launch |

### What Jade buys
Cosmetics, extra dungeon entries (max 2 per day), field and job speed-ups, shop refresh, and extra bag space.
**Never:** Qi, Tempering, levels, breakthrough success, Karma, rebirth multipliers, or exclusive power gear.

### Rebirth & Body
- The Rebirth multiplier and Karma are **earned only**. Nothing paid touches the prestige layer.
- IAP perks (Remove Ads, Immortal Cave, Monthly Card) **persist through rebirth**. Say so on the rebirth screen so buyers never feel they lost anything.
- Possible rewarded ad: "+1 free Medicinal Bath" (cap 2/day).

## Guardrails
- No interstitials, no forced ads, and no ads in the first 10 minutes.
- No "limited offer" pop-up more than once per day. None during the first 3 days except the Starter Pack.
- Every paid boost is also obtainable free (by ad or by play), just slower.
- Show prices clearly, no loot boxes with paid currency (avoids regulatory risk in BE/NL and app-store disclosure requirements).

## Revenue Targets (closed beta and launch benchmarks)
| Metric | Target |
|---|---|
| Ad ARPDAU | $0.03–0.06 |
| IAP conversion (D30) | 2–4% |
| Total ARPDAU | $0.06–0.12 |
| Remove Ads share of IAP | ~30% |

## LiveOps (M2+)
- **Weekly:** dungeon bonus weekend (+1 entry).
- **Monthly:** themed event map with a cosmetic reward track (for example, Lantern Festival, Mid-Autumn Moon).
- **Each major update:** a new realm + 2 maps + 1 dungeon + a pet.

## Decisions
- **Remove Ads** gives no power bonus. It auto-claims ad rewards instead.
- **Monthly Card** (subscription) stays the recurring product. *Immortal Cave* acts as the one-time "VIP" purchase.
- **Free Jade:** about 1 cosmetic per month from play.
- **Battle pass:** post-launch (M3).
