# 01 — Game Design Overview

## Vision
A calm, satisfying cultivation fantasy you can carry in your pocket. Each time you open the game, your cultivator has grown stronger. Each decision about where to spend your Qi, stones, and herbs pushes you toward the next realm.

## Design Pillars
1. **Always progressing.** The player never sees a dead screen. Some bar is always filling and some upgrade is always close.
2. **Meaningful choices.** Resources are shared between systems. Spending spirit stones on forging means waiting longer on alchemy. Choices about allocation are the strategy layer.
3. **Long-term goals.** The realm ladder spans months, and every major realm visibly changes your character, unlocks systems, and opens maps.
4. **Respectful idling.** Offline gains are generous, there are no punishing timers, ads are never forced, and there is no FOMO beyond light dailies.

## Target Audience
- **Primary:** 18–35 mobile players who read or watch xianxia (*cultivation*) stories, and fans of idle games like *Melvor Idle*, *Idle Slayer*, *Legend of Mushroom*, and *Immortal Taoists*.
- **Secondary:** casual players who want low-pressure progression in short sessions.
- **Play pattern:** 3–6 short check-ins per day, plus one optional 5–10 minute active session.

## Core Loops

### Moment-to-moment (seconds)
Qi bar fills → tap **Level Up** → stats rise. Auto-combat ticks, and loot pops into the bag.

### Core loop (minutes to hours)
```
Cultivate Qi  ─┐
               ├──► Level up / Breakthrough ──► stronger stats
Temper Body  ──┘                                     │
       ▲                                              ▼
Pills, baths, gear ◄── Craft / Upgrade ◄── Fight on maps (loot, stones, beast blood)
```
Two cultivation tracks run in parallel: **Qi** (ATK, Max Qi, realms) and **Body** (Max HP, DEF, body stages). Each one helps the other: a strong body raises breakthrough chance and survives tribulations.

**The Vessel Model** ([02-Systems §0](02-Systems.md)): Qi and HP are pools.
- Training refills them, and max only grows while they're full.
- Every level-up spends the pool, and trying without enough fails with an injury.
- Combat drains the **same** pools.
- The cultivator does **one activity at a time**: **Battle** (loot), **Meditate** (Qi), or **Train** (Body). Nothing grows in battle. **Routines** automate the cycle for idle and offline play.
- Moment to moment, the player decides: fight now or grow now? Push a hard zone or farm an easy one? Use a potion or wait?

### Meta loop (hours to days)
Gathering life skills (mining, woodcutting, fishing, farming) produce raw materials. Processing skills (alchemy, cooking, forging) turn them into pills, food buffs, and gear. Those boost cultivation and combat.

### Long loop (days to months)
Major realm gates need **Qi + breakthrough materials + a Heavenly Tribulation boss**. Clearing a gate unlocks new maps, a dungeon tier, a system, and a visible character transformation.

### Rebirth loop (weeks)
When progress slows, the player can **reincarnate**: the soul keeps a permanent Qi multiplier (and later Karma perks), while realm and body start over. Each life climbs faster and goes deeper than the last. Deciding *when* to rebirth is a key strategic choice.

## Session Design
| Session | Length | What the player does |
|---|---|---|
| Check-in | ~30 s | Collect offline gains (optionally watch an ad for 2×), level up, queue life-skill jobs |
| Management | 2–5 min | Equip gear, craft pills, plant fields, spend stones |
| Active | 5–10 min | Push a new map, run dungeon entries, attempt a breakthrough |

## Progression Feel
**Fast start, steady later (decided).**
- **First hour:** a level-up every 30–60 s, three realms (Meridian Opening → Qi Sea) in about 50 minutes, the first sword drop and the first Cultivation Ground. Foundation Establishment around the 1–2 h mark. Hooks the player.
- **Day 1:** Golden Core and the first Heavenly Tribulation. Rebirth unlocks.
- **Day ~5:** Nascent Soul. The first Rebirth is worthwhile (Golden Core peak or later). Spirit Fields are running.
- **Week 3:** Soul Formation. Pets, dungeons, all life skills. The body is at Silver Marrow or Jade Flesh.
- **Month 1+:** deeper realms and rebirth loops. Each new life replays the fast early game at a higher multiplier.

## Reward Cadence (the "rush")
The rush comes from **how often** something good happens, not from racing through realms.

| Every… | Something rewarding |
|---|---|
| ~30 s (early) to a few minutes (later) | A level or layer breakthrough, with a flash, sound, and numbers jumping |
| Every fight | Loot bursts, with a rarity glow and sound that scale with rarity (gold = screen shake) |
| Every session | The offline return screen as a **treasure chest reveal**, plus a daily quest or achievement pop |
| Every few hours to days | Realm breakthroughs and tribulations, with a full-screen cinematic moment and a new aura |
| Every boss first-clear | A new Cultivation Ground unlock and a guaranteed manual |
| Every rebirth | A **jackpot moment**: an animated multiplier jump, then blazing through early realms |

**Always visible:** the "next unlock" teaser, progress bars close to filling, and Qi/s numbers that keep climbing.

(Exact numbers are in [03-Economy.md](03-Economy.md).)

## Tone & Presentation
- **Tone:** serene but aspirational, with a confident, slightly cheeky protagonist who *remembers being the strongest*. Flavor text reads like a cultivation novel ("Your dantian trembles as the Qi sea expands… just like it did a lifetime ago.").
- **Art direction: chibi (decided).** Cute, big-head 2D characters with expressive animations (meditating, training, fighting), bright cultivation effects (auras, lightning, sword light), and a clean pastel UI. Monsters and bosses are chibi too: menacing, but cute. Skeletal 2D animation (for example, Spine) keeps one character rig reusable across robes, swords, and realm auras.
- **Audio:** guqin and flute ambience, gong on breakthrough, thunder on tribulation.
- **Character:** visible aura and robe changes per major realm, plus a subtle **skin sheen per body stage** (copper, iron, silver, jade, gold). This is the main "power fantasy" payoff. Appearance **presets** at the start: gender, hair, face, colors.

## Story
**Premise:** in a past life, you were the strongest cultivator under heaven. Then something (or someone) ended that life, and you were **reincarnated** as a weak mortal in a cultivation world. You still have fragments of your memories. Now you start the journey to become the strongest again, and to find out what happened.

**How the story shows up (light narrative, never blocking play):**
- **Opening (tutorial):** a short cutscene of your past self's final battle, then waking up as a mortal. Your memories explain why you know how to open your meridians so fast (the quick opening realms).
- **Memory Fragments:** each realm breakthrough unlocks a short memory of your past life (a few lines of text plus an illustration). They're collectible in a "Past Life" journal.
- **The Main Quest ("Path of Cultivation")** follows the story: reclaiming your old techniques, meeting people who knew your past self, and hints about who betrayed you.
- **Rebirth fits the lore:** you've reincarnated before, so each rebirth deepens your past-life memories. That's why the perk tree is called *Past-Life* perks and the currency is Karma.
- **Long arc (Planes):** each Plane reveals more of your past life. Reaching **Primordial** in the Origin Plane means finally surpassing your past self, the true ending.

**Open story questions:** the protagonist's past-life title (for example, "Sword Sovereign"), the betrayer's identity and when they're revealed, and whether there's a named rival in the present life.

## Unique Selling Points
1. Seven interlocking life skills plus twin Qi/Body cultivation, so the game is deeper than a single-bar idler.
2. Heavenly Tribulation boss fights as dramatic realm gates.
3. Honest, generous offline progress and ads that never interrupt.

## Decisions
- **Cultivation paths** (Sword / Body / Alchemy specialization): not at launch. Revisit post-launch, possibly as an Immortal Plane feature.
- **Prestige:** Rebirth (inside a Plane) plus Ascension (between Planes).
- **Character look** reflects both the body stage (skin sheen) and the Qi realm (aura, robes).
- **Combat** is fully automatic.
- Story details (past-life title, the betrayer, a rival) are still open. See § Story.
