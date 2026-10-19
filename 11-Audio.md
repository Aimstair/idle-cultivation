# 11 — Audio Plan (music, ambience, SFX)

Everything you hear in *Idle Cultivation* for **v1.0**: what to make, how it should sound, the tools, copy-paste prompts, and the technical specs the game needs. Companion to the [Art Bible](08-Art-Bible.md) (the visual moments here have matching sounds) and [06-Tech](06-Tech.md).

## 1. Direction

**Pillars**
1. **Calm you can live in.** An idle game is left running for hours. The hub music must never tire the ear: slow, sparse, no sharp highs, no busy drums, no vocals.
2. **Rewards ring.** The few big moments (breakthrough, rare drop, boss defeat, rebirth) get bright, satisfying stingers. Everything else stays soft so these stand out. Same rule as gold in the UI: reserve the sparkle.
3. **A place has a sound.** Each Cultivation Ground and map family has an ambience bed (wind in bamboo, night lake, storm), so moving to a new ground *sounds* like travelling.
4. **Element = timbre.** Metal rings and slices, Wood rustles and creaks, Water splashes and chimes, Fire crackles and whooshes, Earth thuds and rumbles. A player should hear what element just hit.

**Instrument palette (Chinese wuxia / xianxia):** guqin and guzheng (calm, plucked), dizi and xiao flutes (air, freedom), erhu (emotion, tension), pipa (fast, martial), yangqin (sparkle), temple bells, singing bowls, wooden fish, gong, Chinese drums and taiko (battle only), soft string pads and choir "ah" (celestial moments only). No vocals with words.

**Don'ts:** no rock or EDM drums, no modern synth leads, no lyrics, no copyrighted melodies or "in the style of" a named composer or game.

## 2. Music (8 loops + 10 stingers)

Loops are 2–3 minutes, instrumental, and loop seamlessly (I trim and crossfade the loop points; see §7).

| id | Track | Where | Mood | Length |
|---|---|---|---|---|
| `mus_title` | Main theme | Title screen, opening cutscene | Hopeful, a reborn master's quiet confidence; the one memorable melody (dizi lead) | 1:30–2:00 |
| `mus_hub_day` | Cultivation · Day | Hub (Meditate/Train) at most grounds | Serene, slow guqin and guzheng, soft xiao, gentle pad. **The most-heard track: make it the least tiring** | 2:30–3:00 |
| `mus_hub_night` | Cultivation · Night | Hub at night-time grounds (Moonlit Lake, Yin Altar, Observatory) | Moonlit, sparse, singing bowls, distant flute | 2:30–3:00 |
| `mus_battle` | Battle | Combat maps (zones 1–3) | Light martial energy: pipa rhythm, light drums, dizi; **steady, not frantic** (it runs for hours) | 2:00 |
| `mus_boss` | Boss | Map and dungeon bosses | Urgent: taiko, erhu, fast pipa, tension | 1:30 |
| `mus_dungeon` | Secret Realm | Dungeons, Trial Tower | Mysterious, low drones, sparse percussion, echoing bells | 2:00 |
| `mus_tribulation` | Heavenly Tribulation | Tribulation fights | Epic and ominous: big drums, thunder, choir, rising erhu | 1:30 |
| `mus_map` | Journey | World, region and stage maps | Adventurous, open, dizi melody over guzheng | 1:30 |

| id | Stinger | When | Length |
|---|---|---|---|
| `stg_breakthrough` | Minor breakthrough success | Each level-up gate | 2–3 s |
| `stg_realm` | Realm breakthrough fanfare | New realm (e.g. Golden Core) | 6–8 s |
| `stg_fail` | Breakthrough failed / Qi deviation | Failed breakthrough | 2–3 s |
| `stg_boss_win` | Boss defeated | Boss kill, before the unlock sequence | 3–4 s |
| `stg_unlock` | New land unlocked | Map/ground unlock animation (seal slam → clouds part) | 4–5 s |
| `stg_rare_drop` | Rare drop | Heaven or Immortal rarity drop | 2–3 s |
| `stg_offline` | Welcome back | Offline-return chest reveal | 3 s |
| `stg_rebirth` | Rebirth | Rebirth jackpot animation | 5–6 s |
| `stg_trib_win` | Tribulation passed | | 4–5 s |
| `stg_trib_lose` | Tribulation failed | | 3 s |

### Music prompts (Suno, Instrumental ON)
Paste the style line, then the track line. Generate 2–4 versions, pick the best, and save as `<id>.mp3`.

> **Style line (all tracks):** instrumental, traditional Chinese xianxia game soundtrack, guzheng, guqin, dizi, erhu, soft strings, warm mix, cinematic but gentle, no vocals, no lyrics

| id | Track line |
|---|---|
| `mus_title` | hopeful main theme, memorable dizi melody over flowing guzheng arpeggios, slow build to a warm full section, then settles, 80 bpm |
| `mus_hub_day` | serene meditation music, slow guqin and guzheng, soft xiao flute phrases, airy string pad, very calm, sparse, no drums, seamless loop, 60 bpm |
| `mus_hub_night` | moonlit night meditation, singing bowls, distant xiao flute, soft guzheng harmonics, gentle drone, very sparse, no drums, seamless loop, 55 bpm |
| `mus_battle` | light martial adventure, driving pipa rhythm, light Chinese drums, dizi melody, energetic but not intense, steady loop, 110 bpm |
| `mus_boss` | intense boss battle, powerful taiko and Chinese war drums, urgent erhu, fast pipa tremolo, rising tension, 140 bpm |
| `mus_dungeon` | mysterious ancient tomb exploration, low drones, echoing temple bells, sparse percussion, distant guqin, eerie but calm, 70 bpm |
| `mus_tribulation` | epic heavenly tribulation, thunder, huge drums, wordless choir, rising erhu, ominous and grand, 120 bpm |
| `mus_map` | open adventure journey, soaring dizi melody over guzheng, light hand percussion, bright and hopeful, 95 bpm |
| stingers | *(style line)* + short victory fanfare / short sad failure motif / short sparkling treasure jingle … *(one line per stinger, add "short 3-second musical sting, ends cleanly")* |

## 3. Ambience beds (8 loops, ~60 s each)
Played quietly under the hub music at a Cultivation Ground (and under battle on matching maps).

| id | Bed | Used at |
|---|---|---|
| `amb_bamboo` | Wind through bamboo, birds, distant stream | Bamboo Grove Hermitage, Primal Spirit Spring, Map 1, Map 14 |
| `amb_village` | Village morning: distant chickens, wind chimes | Humble Hut, Village Courtyard |
| `amb_lake_night` | Night lake, crickets, gentle water lapping | Moonlit Lake Pavilion, Starlight Observatory |
| `amb_fire` | Crackling heat, distant lava rumble, steam hiss | Ember Hot Springs, Volcano Crater Forge |
| `amb_storm` | Wind on a peak, distant thunder | Thunderstruck Summit, Cloud Sea Peak |
| `amb_marsh` | Frogs, bubbling, insects | Venom-Steeped Pools |
| `amb_ice` | Cold wind, creaking ice, faint chimes | Glacial Cave of Stillness |
| `amb_eerie` | Low hum, whispers-like wind (no words), distant bells | Ruined Hall, Yin Spirit Altar, Void Rift Edge |

## 4. Sound effects (~75)

Short, punchy, mono. ElevenLabs prompts: describe the sound plainly, say the length. Generate 3–4, keep the best. Element hits are the most-heard SFX in the game: make them pleasant at 6–12 per minute.

### UI (14)
`ui_tap` soft wooden tap · `ui_back` lighter tap · `ui_open` paper scroll unrolling, short · `ui_close` scroll rolling shut · `ui_tab` soft jade click · `ui_toggle` small bamboo click · `ui_error` low muted wooden knock · `ui_claim` bright jade chime · `ui_coin` spirit stones clinking (for number tick-ups, very short) · `ui_jade` glassy jade chime · `ui_purchase` coins plus soft bell · `ui_badge` tiny bell ding · `ui_equip` cloth rustle and metal click · `ui_levelup_small` rising pluck

### Progression (10)
`prg_qi_full` soft shimmer swell (pool full) · `prg_level` rising guzheng glissando, short · `prg_bt_charge` Qi gathering whoosh building (loopable, 1 s) · `prg_bt_flash` bright crystalline burst · `prg_bt_release` deep resonant boom with shimmer tail · `prg_fail_crack` glassy crack and low thud · `prg_injury` muted heartbeat thump · `prg_meditate_start` singing bowl strike · `prg_train_start` wooden dummy strike thud · `prg_rebirth_whoosh` reverse whoosh into big chime

### Combat (30)
- **Hits by element (5):** `hit_metal` sharp sword slice with ring · `hit_wood` leafy whip snap · `hit_water` heavy splash impact · `hit_fire` burst of flame whoosh · `hit_earth` heavy rock thud
- **Basic (5):** `atk_light` quick sword swish · `atk_heavy` heavy swing whoosh · `hit_crit` sharp impact with bright ring · `miss` air whiff · `dodge` quick cloth whoosh
- **Defence and status (8):** `shield_up` glassy barrier hum · `shield_break` glass shatter · `heal` warm soft chime swell · `st_burn` sizzle · `st_poison` bubbling drip · `st_freeze` ice crackle · `st_stun` dizzy ringing · `st_bleed` wet slash
- **Combat arts, casts (5, one per element):** `cast_metal` blades unsheathing, rising ring · `cast_wood` vines surging, creak · `cast_water` wave surge · `cast_fire` roaring flame build · `cast_earth` ground rumble rising
- **Enemies (7):** `enemy_death` soft poof with sparkle · `swarm_death` small multiple poofs · `boss_roar_beast` big creature roar · `boss_roar_human` war cry (no words) · `boss_phase2` deep power-up swell · `boss_death` big impact and crumble · `enemy_spawn` soft whoosh in

### Loot & rewards (6)
`loot_common` small clink · `loot_spirit` brighter clink · `loot_earth` chime · `loot_heaven` sparkling chime with shimmer · `loot_immortal` golden choir-like shimmer (pairs with `stg_rare_drop`) · `chest_open` wooden lid creak and sparkle

### Crafting & life skills (12)
`alc_bubble` cauldron bubbling (loop) · `alc_success` puff and bright chime · `alc_fail` muffled puff and fizzle · `forge_hammer` hammer on anvil · `forge_success` ringing anvil and shimmer · `forge_fail` dull clank · `mine_pick` pickaxe on rock · `wood_chop` axe chop · `fish_cast` line whip and plop · `fish_reel` reel clicking · `harvest` plants rustle and pluck · `cook_sizzle` wok sizzle

### World & special (6)
`map_seal_slam` huge seal stamp slam with ink splash and gong · `map_gong` temple gong · `trib_thunder_small` lightning crack · `trib_thunder_big` massive thunderclap · `pet_cute` small happy chirp · `pet_evolve` rising sparkle swell

## 5. Tools & cost
| Need | Tool | Commercial use | Cost |
|---|---|---|---|
| Music + stingers + ambience | **Suno** (Pro, Instrumental mode) | Third-party reviews say the **free plan has no commercial rights** and paid plans do. Terms changed after Suno's Warner Music deal | ~$8–10 for one month |
| SFX | **ElevenLabs Sound Effects** (Starter) | Reviews say the **free tier requires attribution and is not for commercial use**; paid plans cover games | ~$5 for one month |
| Free top-up for UI clicks | **Kenney** audio packs (CC0, no attribution) and **Freesound** filtered to CC0 | Free, commercial OK under CC0 | $0 |

Total: about **$15** if everything is generated within one month. **Before paying, read each tool's current terms page**: the reviews disagree in places, and the rules change. Generate everything **while the paid plan is active**, and keep a screenshot of your plan and the date as proof of licence. Avoid Udio for now: reviews disagree on its commercial rights and report its downloads were suspended.

## 6. Mixing & behaviour in the game
| Rule | Value |
|---|---|
| Buses | Music · Ambience · SFX · UI, each with its own volume slider; plus master mute |
| Default levels | Music 60%, Ambience 40%, SFX 80%, UI 60% |
| Loudness targets | Music −18 LUFS integrated, ambience −26 LUFS, SFX peaks ≤ −1 dBTP; all files normalised so nothing jumps |
| Ducking | Music dips 40% under stingers and big moments (breakthrough, boss win, rare drop) |
| Repetition | Each hit SFX plays with ±5% random pitch and ±2 dB volume so 10 kills a minute don't sound identical; max 4 simultaneous SFX |
| Idle / background | Battle and hub SFX mute while the app is in the background; nothing plays during offline time |
| Phone settings | iOS "ambient" audio session: respects the silent switch and lets the player's own music keep playing (then game music auto-mutes) |
| Haptics | Paired with the same moments as the Art Bible (§6): light tap on buttons, medium on breakthrough, heavy on realm breakthrough and Immortal drops |
| Accessibility | All key info is also visual; sound is never required |

## 7. File specs & pipeline
- **Music, stingers, ambience:** generate as MP3, then I convert to **AAC `.m4a`, 44.1 kHz, 128 kbps stereo**, cut seamless loop points, normalise loudness, trim silence. *(Works on both iOS and Android; to be confirmed in the M0 prototype.)*
- **SFX:** **`.wav` 16-bit 44.1 kHz mono**, trimmed to the sound, under 1.5 s (ambience loops excepted), normalised. Converted to `.m4a` at build time if the bundle gets large.
- **Names:** exactly the ids above (`hit_fire.wav`, `mus_hub_day.m4a`). Save into `audio/_inbox/`; I'll extend the drop-folder tool to sort, convert, normalise and check them.
- **Budget:** ~8 MB music + ~3 MB SFX + ~4 MB ambience in the app download.

## 8. Order
1. **For the M0 prototype:** `mus_hub_day`, `mus_battle`, `stg_breakthrough`, `prg_level`, `ui_tap`, `ui_claim`, the 5 element hits, `enemy_death`, `loot_common`, `loot_heaven`.
2. **For M1 alpha:** everything else in §2–§4 for maps 1–8 (all music loops, all stingers, `amb_bamboo`, `amb_village`, `amb_lake_night`, `amb_fire`, `amb_storm`, `amb_marsh`, `amb_ice`, `amb_eerie`, all SFX).
3. **Later:** event and seasonal music, sect sounds, M3 realm themes.

**Totals:** 8 music loops, 10 stingers, 8 ambience beds, about 75 SFX.
