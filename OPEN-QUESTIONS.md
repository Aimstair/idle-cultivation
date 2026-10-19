# Design Decisions (formerly Open Questions)

**✅ All decided.** The user approved the recommendations, with the changes noted below (#62, #63). These answers are written into the design docs.

⭐ = worth a real look (affects feel or scope). The rest are tuning or polish defaults.

## Core gameplay
| # | Question | Recommendation |
|---|---|---|
| 1 | Cultivation "paths" (Sword / Body / Alchemy specialization)? | **Not at launch.** Revisit post-launch, possibly as an Immortal Plane feature |
| 2 | Should the character's look reflect the body stage? | **Yes.** Subtle skin sheen per body stage (copper, iron, silver, jade, gold), plus the Qi realm aura. Cheap with layered chibi art |
| 3 | ⭐ Fully auto combat, or optional manual skill timing? | **Fully auto at launch.** Idle-first. Revisit if players ask |
| 4 | Limited or unlimited bag? | **Limited but generous** (grows to 140 slots) with auto-salvage filters |
| 5 | Rebirth: full body-stage reset or drop one stage? | **Full reset** (current). The Body multiplier compensates |
| 6 | Rebirth: keep gear? | **Keep** (current). Realm requirements still apply |
| 7 | Qi overflow after a breakthrough? | **Resolved by the Vessel Model:** whatever's left in the pool after the spend stays |
| 8 | Offline combat efficiency 70%: too stingy? | **Raise to 80%.** Growth already only happens during Meditate/Train |
| 9 | Can free players earn Jade meaningfully? | **Yes:** about 1 cosmetic per month from dailies, achievements, and events |
| 10 | Minimum rebirth point: Golden Core or Nascent Soul? | **Golden Core** (current). Stacking already rewards going deeper |

## Monetization & tech
| # | Question | Recommendation |
|---|---|---|
| 11 | Remove Ads gives +5% Qi? | **No power bonus** (no pay-for-power). It auto-claims ad rewards instead (current) |
| 12 | Monthly Card or one-time VIP? | **Monthly Card** (current). Immortal Cave already acts as a one-time "VIP" purchase |
| 13 | Guest play or required sign-in? | **Guest first.** Prompt to link Apple/Google after the first breakthrough |
| 14 | Save format: JSON or SQLite? | **JSON for v1.0.** Switch only if large inventories get slow |

## Realms & tribulations
| # | Question | Recommendation |
|---|---|---|
| 15 | Can a tribulation be postponed forever? | **Yes, unlimited** (idle-friendly), with a gentle reminder |
| 16 | Heart Demon mirror at 90% of your stats? | **Yes, 90%** |
| 17 | Tribulations count as Battle (only base regen + pills)? | **Confirm yes** |
| 18 | Suggest a "refill" Routine when postponing a tribulation? | **Yes**, one tap: Train to full → Meditate to full |
| 19 | ⭐ Qi Sea unlocks nothing new. Add something? | **Yes:** Qi Sea 1 unlocks the **Pendant slot** and the Sword Pavilion's **rotating stock** |

## Body
| # | Question | Recommendation |
|---|---|---|
| 20 | Golden Bell Cover's 30% damage-reduction cap also applies in tribulations? | **Yes** |
| 21 | 60-min cap on blood bursts too generous? | **Keep.** Check in the balancing spreadsheet |
| 22 | Warm-up penalty when switching exercises? | **No.** Unneeded friction |
| 23 | Blood bursts usable mid-Battle? | **Yes** (current) |

## Combat & maps
| # | Question | Recommendation |
|---|---|---|
| 24 | ⭐ Default retreat 30% / resume 90%, or resume at 100%? | **Retreat 30% / Resume 100%.** Each Battle step starts full, and the Train step can grow max once full |
| 25 | Healing Pills auto-use outside combat? | **No.** In battle only; tap to use manually otherwise |
| 26 | Boss respawn every 10 min: too generous? | **Keep.** Tune in the balancing spreadsheet |
| 27 | Bad-luck protection on boss signature drops? | **Yes:** guaranteed by kill ≈ 2 ÷ drop rate |
| 28 | Manual "interrupt" button for bosses? | **No** at launch |
| 29 | Pet capture from zone monsters? | **No**, bosses only |

## Dungeons
| # | Question | Recommendation |
|---|---|---|
| 30 | Entries per dungeon or a shared pool? | **Per dungeon** (current, simpler) |
| 31 | Sweep needs ★★★ or ★? | **★ (one clear)**, more idle-friendly |
| 32 | Void Labyrinth paths: auto-pick by default? | **Yes**, with a setting to choose manually |
| 33 | Trial Tower offline auto-climb? | **No.** It's the competitive leaderboard, so it stays active play |
| 34 | Rebirth: keep dungeon tiers and stars? | **Reset** (current). The *Dungeon Sweeper* perk keeps sweeping |

## Equipment
| # | Question | Recommendation |
|---|---|---|
| 35 | Enhancement Transfer free or 20% cost? | **20% cost** (stone sink) |
| 36 | ⭐ Loadouts (one-tap gear sets)? | **Yes, 3 loadouts at v1.0.** Each saves sword, armor, accessories, and pill pouch, swapped with one tap |
| 37 | Named legendaries for other slots? | **Swords only** at launch |
| 38 | Gathering gear set? | **No.** The Pendant's life-skill stat covers it |
| 39 | ⭐ Should higher rarity favor more accessory stats? | **Yes, lightly:** Mortal 1–2, Spirit 1–2, Earth 1–3, Heaven 2–3, Immortal 3 (each still random within its range) |
| 40 | Auto-swap loadouts by activity? | **Yes, as a Karma perk** ("Prepared Mind") |

## Techniques
| # | Question | Recommendation |
|---|---|---|
| 41 | Element "schools" bonus? | **Yes, simple:** +10% if your method and all equipped arts share an element |
| 42 | 2nd method slot at 50%? | **Keep 50%** |
| 43 | Combat art cost: % of Max Qi or flat? | **Keep %** (scales automatically) |
| 44 | Healing arts balanced vs meditation time? | **Keep.** Tune in the closed beta |

## Alchemy
| # | Question | Recommendation |
|---|---|---|
| 45 | Pill toxicity meter? | **No.** The existing limits (1 Qi pill, 2 chance pills) are enough |
| 46 | Failure: 50% ingredient refund or "Pill Residue"? | **Pill Residue**, usable as Spirit Field fertilizer |
| 47 | Gift a Foundation Pill once by quest? | **Yes**, as a safety net |
| 48 | Ascension Pill at Alchemy 99 too steep? | **Lower to 95** |
| 49 | Daily ad for instant full HP/Qi? | **No.** It would undercut restoration pills |

## Life skills, pets, fields
| # | Question | Recommendation |
|---|---|---|
| 50 | Bigger job queue (5)? | **Karma perk only** |
| 51 | Cooking uses fuel? | **No**, fuel-free |
| 52 | Level 99 grind (~260 h on one node) too long? | **Target ~120–150 h.** Tune XP in the spreadsheet |
| 53 | Gathering "focus" toggle (main vs rare yield)? | **Yes**, simple toggle |
| 54 | Pet equipment? | **No** |
| 55 | Pet element uses Wu Xing advantage? | **Yes, +10%** |
| 56 | Pet expeditions? | **Post-launch** |
| 57 | ⭐ Unlock Spirit Fields earlier (Golden Core 1)? | **Yes.** Helps the herbs needed for the Nascent Soul gate |
| 58 | Field plot prices: scaling or fixed? | **Fixed table**, tuned in the spreadsheet |
| 59 | Event-only herbs? | **Yes**, with events (post-launch) |

## Quests, rebirth, social
| # | Question | Recommendation |
|---|---|---|
| 60 | Daily reset: local midnight or fixed server time? | **Fixed server time per region** |
| 61 | ⭐ "Watch an ad" daily quest OK? | **Remove it** to keep the "ads are always your choice" promise |
| 62 | Achievements give ~+40% Qi total: too much? | **Raise to +300% Qi total** (user decision). A long-term chase; the balancing spreadsheet must account for it inside `EXT` |
| 63 | Heaven's Favor (+30% future gains) too strong? | **Keep +10% per rank, 3 ranks (max +30%)** (user decision) |
| 64 | Stop Karma from shallow rebirths later? | **No.** Stacking already makes shallow rebirths inefficient |
| 65 | Prodigy / Foundation start: full or empty pools? | **Full pools** |
| 66 | Sect at Soul Formation too late socially? | **Keep.** Social at v1.0 = leaderboards. Friends list + gifts arrive with Sects post-launch |
| 67 | Sect boss: real-time or async? | **Async** (current) |
| 68 | Leaderboards: global, regional, or per server? | **Global + friends filter** at launch. Regional seasons later if needed |
| 69 | Battle pass at launch? | **Post-launch** |

## UI & tutorial
| # | Question | Recommendation |
|---|---|---|
| 70 | Character customization depth? | **Presets:** gender, hair, face, colors (easy with layered art) |
| 71 | Disclose the tutorial's ×3 Qi speed-up? | **Invisible** |
| 72 | 5 bottom tabs too many? | **Keep 5** |
| 73 | Tablet landscape? | **Not at launch** |
| 74 | Activity switcher on every tab? | **A tappable top-bar chip on every tab**; the full switcher on Cultivate/Adventure |
| 75 | Scripted safe failure at 4:00 too early? | **Move it** to the first natural "not enough" moment |
| 76 | Mini HP/Qi bars always on? | **Always on.** The pools are shared |

## Grounds & Planes
| # | Question | Recommendation |
|---|---|---|
| 77 | Sect-owned shared site? | **Yes, when Sects arrive** |
| 78 | Which Immortal Plane realm does the Fire & Wind Calamity gate? | **Earth Immortal → Heaven Immortal** |

## Already resolved (will be removed from the docs)
- Prestige layer (Rebirth is in) · body breakthrough failure (HP check, no roll) · a second Training slot (Karma perk) · healer pets (allowed) · Master Smith bonus · Qi overflow (#7) · Planes 5–10 length (shorter, with deep systems) · post-breakthrough retreat loop (Consolidating).

## Story details (decide anytime before main-quest writing)
- S1. The protagonist's past-life title (for example, "Sword Sovereign", "Heavenly Venerable").
- S2. Who ended the past life, and when it's revealed (a suggested Plane: Immortal).
- S3. A named rival in the present life? (Recommended: yes. A recurring chibi rival boss fits idle combat well.)
