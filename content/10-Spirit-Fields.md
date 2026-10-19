# 10 — Spirit Fields (Farming)

Spirit Fields are the **Farming** skill. The player plants herb seeds in plots that grow in real time. Farming XP comes from planting and harvesting. Fields **don't use a worker slot**.

- **Unlock:** **GC 1** (moved earlier, so herbs for the Nascent Soul gate don't depend only on drops). **Milestone:** M2.
- Before GC, every herb comes from map and dungeon drops (see [00-Registry](00-Registry.md)). Fields make herbs reliable and unlock the rarest ones.
- **Skill:** Farming, levels 1–99, same XP curve as other life skills.

---

## Plots
| Plot | Requirement | Cost (Spirit Stones) |
|---|---|---|
| 1–2 | GC 1 (free) | — |
| 3 | Farming 5 | 60,000 |
| 4 | Farming 15 | 250,000 |
| 5 | Farming 25 | 2,000,000 |
| 6 | Farming 40 | 6,000,000 |
| 7 | Farming 55 | 20,000,000 |
| 8 | Farming 70 | 60,000,000 |
| 9 | Farming 85 | 200,000,000 |

Plots are laid out in a 3×3 grid. Adjacency matters for cross-pollination (below).

## Soil Quality (per plot)
| Soil | Farming lvl | Upgrade cost | Yield | Grow time | Cross-pollination |
|---|---|---|---|---|---|
| Common | — | — | ×1.0 | ×1.0 | 3% |
| Fertile | 20 | 500,000 SS, Beast Core (T4) ×10 | ×1.2 | ×1.0 | 4% |
| Spirit | 45 | 15M SS, Beast Core (T5) ×20, Spirit Crystal ×50 | ×1.4 | ×0.9 | 5% |
| Immortal | 80 | 1B SS, Beast Core (T7) ×30, Dragon-Vein Jade ×20 | ×1.75 | ×0.8 | 7% |

## Seeds & Herbs
| Farming lvl | Herb | Grow time | Yield per harvest | Plant XP | Harvest XP | Seed sources |
|---|---|---|---|---|---|---|
| 1 | Spirit Grass | 30 min | 4–6 | 5 | 20 | Starter ×5, maps 1–3, harvest |
| 5 | Spirit Rice | 1 h | 6–8 | 8 | 35 | Starter ×5, map 2, harvest |
| 15 | Fire Lotus | 2 h | 2–3 | 20 | 90 | Map 4, D4, harvest |
| 30 | Purple Cloud Grass | 3 h | 2–3 | 45 | 200 | Maps 5 and 7, D4, harvest |
| 45 | Snow Lotus | 4 h | 2 | 90 | 400 | Map 8, D4, harvest |
| 55 | Soul Lotus | 6 h | 1–2 | 150 | 700 | Map 10, D4, harvest |
| 60 | Blood Ginseng | 8 h | 1–2 | 220 | 1,000 | Map 13, D4, harvest |
| 75 | Star Orchid | 10 h | 1 | 450 | 2,000 | Map 16, D4, harvest |
| 90 | Nine-Leaf Immortal Grass | 12 h | 1 (25% chance of 2) | 1,000 | 5,000 | D4 (rare), map 22, cross-pollination only otherwise |

- **Seed return:** every harvest returns 1 seed, plus a 20% chance of a 2nd. A player who keeps planting never runs out.
- Seeds for higher herbs also drop (at low rates) from the maps listed, and from **D4 Herb King's Garden**. They also appear in the Sect and Event shops (see [13-Sect-Events](13-Sect-Events.md)).

## Cross-Pollination (rare yields)
- When a plot is harvested, each **adjacent plot growing a different herb** gives a chance (by soil, table above) to also drop **1 seed of the next-higher herb** in the list, if the player's Farming level allows planting it.
- This is the main way to get Nine-Leaf Immortal Grass seeds outside D4, and it gives the 3×3 layout a puzzle element.

## Tending & Fertilizer (optional)
- **Tend (water):** once per growth cycle, tap the plot (or "Tend All") for **−10% remaining grow time**. Online only, never required.
- **Fertilizer:** bury Beast Cores in a plot when planting. A core of tier ≥ the herb's tier gives **+25% yield** for that cycle (1 core per plot).
- **Pill Residue** (from failed alchemy crafts, [07-Alchemy](07-Alchemy.md)) also works as fertilizer: **+15% yield and −10% grow time** for that cycle, any herb tier (1 Residue per plot). It can stack with a Beast Core.
- **Speed-ups:** rewarded ad or Jade, −30 min per use (caps per [05-Monetization](../05-Monetization.md)).
- **Pet bonus:** Jade Rabbit +10% Farming speed (see [09-Pets](09-Pets.md)).

## Offline Growth
- Fields grow on **real time**, so they keep going while the app is closed. The offline cap doesn't apply to fields.
- Ready crops **never wither**. They wait until harvested.
- Local notification when all plots are ready ("Your spirit fields are ripe").
- With the Farming 50 perk, harvests and replanting happen automatically, even offline (if seeds are in stock).

## Mastery Perks
| Lvl | Perk |
|---|---|
| 25 | 10% chance of +1 yield |
| 50 | **Auto-harvest & replant** (same seed, if in stock) |
| 75 | −15% grow time |
| 99 | Title **Herb King**, cross-pollination chance ×2 |

## UI
- **Skills tab → Spirit Fields:** 3×3 grid, each plot shows its herb sprite, growth ring, and soil color. Tap a plot to plant, harvest, fertilize, or upgrade soil. "Harvest All", "Replant All", and "Tend All" buttons sit at the top.

---

## Decisions
- Spirit Fields and Farming unlock at **GC 1** (was NS 1). Plot 3–4 prices were lowered to fit Golden Core income.
- Plot prices are a **fixed table**, tuned in the balancing spreadsheet.
- **Event-only herbs and seeds** come with events (post-launch).
- Pill Residue from failed alchemy works as fertilizer.
