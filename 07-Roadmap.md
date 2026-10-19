# 07 — Roadmap

Durations assume **one solo developer using AI for code and art**, on Flutter + Flame + Supabase. Total to launch: about **6–9 months**.

## M-1: Pre-production (now, 1–2 weeks)
- [ ] Review and sign off on design docs 01–06
- [x] Tech stack: **Flutter + Flame + Supabase** (see [06-Tech](06-Tech.md))
- [x] Art bible written ([08-Art-Bible](08-Art-Bible.md))
- [ ] Generate and approve the 3 master sheets (hero, monsters + boss, 12 icons)
- [x] Art direction: **chibi**. Make 1 mood board and 1 mock home screen
- [ ] Build the balancing spreadsheet from [03-Economy](03-Economy.md)
- [ ] Wireframe all 5 main tabs
- [x] Name: **Idle Cultivation**. Check app-store availability and the name's uniqueness (consider a subtitle)

## M0: Prototype (2–3 weeks)
**Goal:** prove the core loop is satisfying with placeholder art.
- [ ] Cultivation: Qi bar, level up, meditation boost
- [ ] Realms 1–4 (Meridian Opening → Foundation Establishment) + breakthrough (success chance, pity)
- [ ] 1 map with auto-combat, 3 zones, boss, loot drops
- [ ] Basic inventory + equip
- [ ] Save/load + offline gains + return screen
- [ ] Debug menu (time acceleration, grants)
- **Exit criteria:** testers voluntarily keep playing for 30+ min, and offline return feels rewarding.

## M1: Alpha (internal, 6–8 weeks)
**Goal:** a complete core loop, playable end to end by the team and a small group of testers. **Not released publicly.**
- [ ] Realms 1–5 (through Golden Core), Tribulation I boss
- [ ] 8 maps, 1 dungeon (Spirit Vein Cave)
- [ ] Gear: Sword + 3 armor slots + 3 accessories (1–3 random stats), rarities, affixes, forging/enhance, salvage
- [ ] Vessel Model: Qi/HP pools shared with combat, breakthrough spend, stacking 5-min injuries, retreat point
- [ ] Activities (Battle / Meditate / Train) + Routines
- [ ] Swords: Jian, Saber, Greatsword, Twin Swords (Flying Swords and legendaries come with later dungeons/bosses), Sword Pavilion shop
- [ ] Cultivation Grounds: 2 starter grounds + 8 from maps 1–8 (Meditation Sites / Training Grounds, min realms)
- [ ] Techniques: 1 method + 2 combat arts
- [ ] Body Cultivation: Copper Skin → Silver Marrow, 3 exercises + mastery, Medicinal Bath + Purple Cloud Bath
- [ ] Rebirth: stacking Qi + Body multipliers, preview screen, current-life/eternal save split
- [ ] Life skills: **Mining + Alchemy**, worker slots
- [ ] Tutorial (first 10 min) and unlock tips
- [ ] **Game feel pass:** breakthrough flashes, loot bursts by rarity, number tick-ups, the offline chest reveal, the rebirth jackpot animation (see 01-GDD § Reward Cadence)
- [ ] Rewarded ads (all placements) + IAP (Remove Ads, Starter Pack, Monthly Card, Jade packs)
- [ ] Analytics, crash reporting, Remote Config
- [ ] Local notifications
- [ ] Final art for the MVP scope, SFX + music
- [ ] Internal playtests with time acceleration. Tune pacing against [03-Economy](03-Economy.md)
- **Exit criteria:** testers enjoy the first week of play (accelerated), no progression blockers, crash-free ≥ 99%.

## M2: v1.0 Launch, the first public release (8–12 weeks after M1)
**Everything in M1 plus the list below ships together as the first launch.**
- [ ] Realms 6–8 (Nascent Soul → Void Breaking), Tribulations II–IV
- [ ] Pets (5+), Spirit Fields
- [ ] Body stages Jade Flesh → Golden Body, Shadow Footwork, Lightning Tempering
- [ ] Karma and Past-Life perk tree
- [ ] All 7 life skills (Fishing, Woodcutting, Farming, Cooking added)
- [ ] Dungeons 2–3, Sweep
- [ ] Daily quests, weekly chest, achievements
- [ ] Cloud save + backend (accounts, server-validated saves)
- [ ] **Leaderboards:** realm, power, Trial Tower (server-validated, see content/13-Sect-Events)
- [ ] Story: opening cutscene, Memory Fragments journal, main-quest story text (realms 1–8)
- [ ] Cosmetics shop
- [ ] Loadouts (3 one-tap gear sets)
- [ ] Character appearance presets
- [ ] Localization (5 languages)
- [ ] Store page, trailer, ASO
- [ ] **Closed beta (2–4 weeks before launch):** the full v1.0 build via TestFlight / Play internal testing, about 100–500 players. Checks retention, the economy, and crashes, then a final tuning pass. It's private, not a public soft launch
- [ ] Worldwide launch on iOS + Android
- **Beta KPI gates to proceed to launch:** D1 ≥ 40%, D7 ≥ 15%, crash-free ≥ 99.5%.
- **Launch KPI targets:** D1 45%, D7 18%, D30 7%, ARPDAU ≥ $0.08.
- **Content at launch:** realms 1–8 (Meridian Opening → Void Breaking) are about 6 weeks of first-life play, plus rebirth loops and the Karma tree. That's comfortably past the D30 target.

## M3: Post-launch (ongoing, ~6-week update cadence)
- [ ] Sects (guilds): sect shop, co-op boss (async), Friends list + gifts, Sect-owned Meditation Site
- [ ] Pet expeditions, event-only herbs
- [ ] Tablet landscape support (later)
- [ ] Monthly events and a seasonal battle pass
- [ ] Realms 9–10 (Mahayana, Great Ascension), Tribulations V–VI, then **Ascension** to the Immortal Plane (first expansion). Later Planes: one per major expansion (see content/16-Planes-Ascension)
- [ ] **Player Marketplace** (future): trade materials and gear for Spirit Stones (see content/13-Sect-Events §5)
- [ ] Optional: cultivation paths (Sword / Body / Alchemy specialization)

## Risks
| Risk | Mitigation |
|---|---|
| Crowded genre (many cultivation idlers) | Lean into 7-skill depth, polish, and respectful monetization. Pick a distinctive art style |
| Pacing too fast or slow | Data-driven constants, Remote Config, headless sim, and telemetry vs the pacing table |
| Scope creep (7 skills + pets + fields…) | Strict MVP = core loop only. All skills share one framework |
| Rebirth feels like losing progress | Clear preview of gains and what's kept, projected "back to current realm in X h," celebratory animation |
| Body track feels like a chore next to Qi | No luck roll on body breakthroughs (full HP + materials), offline training, Training Grounds, Body rebirth multiplier, mastery that persists forever |
| Save corruption or loss | Versioned migrations, rotating backups, cloud save by M2 |
| Ad revenue below target | Tune placements and caps via Remote Config before adding any new ad types |

## Next Steps (for you)
1. Read docs 01–05 and `content/`, and mark anything you disagree with.
2. Answer the open questions, especially **art direction**, then pick the **tech stack**.
3. Once you say go, we start M-1 tasks (spreadsheet, wireframes) and then the M0 prototype.
