# 06 — Tech

> **✅ DECIDED: Flutter + Flame + Supabase.** Solo developer, AI-assisted for code and art. **No code until the plan is approved.**

## Requirements from the design
- **Real mobile app** (iOS + Android) with **chibi 2D art** and lots of effects: auras, lightning tribulations, sword light, "pill cloud".
- **A backend at launch:** accounts, cloud save, server-validated saves, **leaderboards**. Later, a **player marketplace** (server-authoritative trades) and Sects.
- **Big numbers** (Planes go far beyond 1e300), offline simulation, Routines, and data-driven content (hundreds of items, 26+ maps).
- **Rewarded ads + IAP**, 5 languages, remote config for tuning.
- **AI-friendly workflow:** everything is code or data, with no visual-editor-only setup. The game can run on desktop for fast AI test loops (run, screenshot, check).

## The Stack
| Layer | Choice | Notes |
|---|---|---|
| Language / app | **Flutter (Dart)** | Compiles to true native iOS/Android. Hot reload. Runs on macOS desktop or web during development for quick AI-driven testing |
| UI (menus, bars, modals: most of the game) | Flutter widgets + built-in animations | Flutter's main strength: smooth 60/120 fps UI animation with little code |
| Game scenes (battle view, character, effects) | **Flame** (Flutter 2D engine) | Sprites, particles, tweens. Embedded in Flutter screens with `GameWidget` |
| Chibi animation | **Parts-based sprites animated in code** | AI-generated chibi art split into layers (head, body, arms, weapon, aura) and animated with code tweens (idle bob, breathing, attack swing, squash and stretch). No manual rigging. Rive can come later for hero moments if wanted |
| State management | Riverpod (or Bloc) | The UI reads game state; the game core stays pure Dart |
| Backend | **Supabase** (Postgres, Auth, Edge Functions) | Official Flutter SDK. Cloud save, leaderboards, and later marketplace transactions in SQL |
| Ads | `google_mobile_ads` (official Google plugin) | Rewarded ads only (see [05-Monetization](05-Monetization.md)) |
| IAP | RevenueCat (`purchases_flutter`) | Cross-platform purchases, subscriptions (Monthly Card), receipt validation |
| Analytics / Remote Config / Crashes | Firebase (Analytics, Remote Config, Crashlytics) | Official FlutterFire plugins |
| Notifications | `flutter_local_notifications` | Offline cap reached, fields ready, Routine stopped |
| Localization | Flutter `intl` / ARB files | 5 languages at v1.0 |
| Local save | JSON in app storage (or SQLite via `drift`) | Versioned, with rotating backups |

## Architecture
```
┌────────────────────────────────────────────┐
│ Flutter UI (screens, widgets, animations)  │  reads state, sends actions
│   └ Flame scenes (battle, character, FX)   │
├────────────────────────────────────────────┤
│ Game core (pure Dart, deterministic)       │  tick(state, dt) → state
│  ├ Vessel/Cultivation ├ Body   ├ Combat    │  applyAction(state, action)
│  ├ Activities/Routines├ Skills ├ Crafting  │
│  ├ Inventory/Gear     ├ Rebirth├ Offline   │
├────────────────────────────────────────────┤
│ Data tables (realms, maps, items, recipes) │  JSON exported from the balancing spreadsheet
├────────────────────────────────────────────┤
│ Services: Save · Supabase · Ads · IAP ·    │
│ Analytics · Remote Config · Notifications  │
└────────────────────────────────────────────┘
```

### Key principles
1. **Simulation separated from presentation.** The game core is plain Dart with no Flutter imports, so it can be unit-tested, run headless for balancing, and reused for offline progress.
2. **Fixed tick.** The core advances in fixed steps (for example, 100 ms in the foreground). Offline progress runs the **same** systems in large analytic chunks (expected-value math, not per-tick replay), so returning after 8 h is instant.
3. **Data-driven content.** Every number in [03-Economy](03-Economy.md) and [content/](content/00-Registry.md) lives in data files. Remote Config can override key constants for live tuning.
4. **Big numbers from day 1.** A custom mantissa + exponent `BigNum` type (like break_infinity) for Qi, HP pools, stones, and multipliers.
5. **Seeded RNG.** Store the RNG seed in the save so loot rolls are reproducible for debugging.
6. **Split state.** Three layers: **current life** (reset by Rebirth), **plane** (reset by Ascension), and **eternal** (Karma, Dao Marks, mastery, items, purchases). Rebirth and Ascension are then simple, testable resets.

## Save, Cloud & Anti-Cheat
- **Local save:** a single serialized state with a `version` field. Autosave every 30 s, on app background, and on key actions. Keep 2 rotating backups.
- **Migrations:** each version bump has a migration step. Never break old saves.
- **Cloud save (v1.0):** Supabase Auth (Apple / Google sign-in, or guest upgraded later). Saves are uploaded periodically. On conflict, a "choose save" prompt.
- **Server validation:**
  - **Leaderboard** submissions go through an Edge Function. It checks progression against the server clock and the maximum possible rates, and rejects impossible growth.
  - Offline time is validated against server time when online.
- **Marketplace (future):** trades are Postgres transactions with row-level security. Traded items live server-side.

## AI-Assisted Workflow (solo)
- **Code:** AI writes Dart and Flutter. The game runs on macOS desktop or web during development, so changes can be run and screenshotted quickly. Unit tests on the game core catch balance and logic regressions.
- **Art:**
  - First an **art bible**: one chibi style reference, a fixed prompt template, a palette, and character proportions.
  - Characters are generated as **separate layers** for code animation.
  - Icons (items, pills, materials) come from a consistent template.
  - Check the image tool's **commercial-use license**.
- **Data:** the balancing spreadsheet is the source of truth. It's exported to JSON, which the game loads.

## Analytics Events (initial list)
| Event | Key params |
|---|---|
| `session_start` / `session_end` | duration, offline_seconds |
| `level_up` | realm, level, time_since_install |
| `breakthrough_attempt` | realm, chance, success, pool_ok, used_ad, used_pill |
| `tribulation_result` | realm, win, attempts, body_stage |
| `body_stage_up` | stage, qi_realm, time_since_install |
| `activity_time` | battle / meditate / train shares per session |
| `rebirth` | rebirth_count, realm_at_rebirth, level, qi_gain, body_gain, karma, life_duration |
| `map_boss_kill` | map_id, power |
| `life_skill_level` | skill, level |
| `ad_watched` | placement, reward |
| `iap_purchase` | product_id, price |
| `tutorial_step` | step_id (funnel) |
| `churn_point` (derived) | last realm/level before 7 days inactive |

## Testing Strategy
- Unit tests on the game core: formulas, the Vessel Model, offline math, rebirth resets, save migrations.
- Headless simulation: a "bot" player runs 30–60 simulated days, compared against the pacing table in 03-Economy.
- Debug menu: time acceleration (×10, ×100), grant resources, jump to realm.

## Decisions
- **Guest play first.** Prompt to link Apple/Google after the first breakthrough.
- **Local save:** JSON for v1.0. Switch to SQLite (`drift`) only if large inventories get slow.
- **Leaderboards:** global plus a friends filter at launch. Regional seasons later if needed.
- **Daily reset:** a fixed server time per region.
