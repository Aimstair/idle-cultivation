import json
R=json.load(open('rows.json'))
ANCHOR='chibi murim xianxia RPG game art, cute but menacing enemy, big expressive eyes, rich saturated palette, glossy highlights, bold dark outer outline, slightly simplified shading so it reads at small size, light from top-left, 3/4 view facing left, full body, mobile game asset, real transparent background (no checkerboard pattern), no text, no watermark'
PET_ANCHOR=ANCHOR.replace('cute but menacing enemy','adorable friendly pet creature, never menacing')
POSE={'Swift':'lean and agile, low crouch ready to pounce, dynamic','Brute':'big and heavy, wide stance, attacking with raw strength','Tank':'wide, low and armoured, braced defensively','Caster':'floating or holding a focus, glowing magic swirling around it','Swarm':'a group of THREE identical small creatures in one tight cluster','Boss':'about twice the visual weight of a normal monster, ornate, crowned or decorated, dramatic rearing pose, one extra level of detail','Mini-boss':'about one and a half times a normal monster, an extra armour or ornament detail, imposing pose','Pet S1':'small, round, sitting or hopping happily','Pet S2':'standing proud, grown but still cute','Pet S3':'majestic heroic pose with a soft aura'}
EL={'Wood':'Wood accents: greens, leaves, curving spirals','Fire':'Fire accents: orange-red, upward flame teardrops, embers','Water':'Water accents: blues, arcs, droplets, ripples','Metal':'Metal accents: silver-steel, straight slashes, triangle shards, lightning','Earth':'Earth accents: ochre-brown, chunky stone, hexagon debris'}
names={r[0]:r[1] for r in R}
def prompt(r):
    rid,name,where,arch,el,ms,method,base,core=r
    if method in('DONE','CODE'): return None
    anc=PET_ANCHOR if arch.startswith('Pet') else ANCHOR
    acc=(', '+EL[el]) if el in EL else ''
    if method=='NEW':
        att=''
        if base: att=f'Attach `{base}` ({names.get(base,base)}) as a family reference. '
        return f'{att}{core}. Pose: {POSE[arch]}{acc}. {anc}'
    return f'Attach `{base}` ({names.get(base,base)}). The same design family and exactly the same art style, line weight, shading and colour quality as the attached image, but: {core}. Pose: {POSE[arch]}{acc}. {anc}'
SECTIONS=[('Maps 1–8 · M1 (v1.0 alpha content)',lambda r:r[2].startswith('Map') and int(r[2].split()[1])<=8),
('Dungeon D1 · M1',lambda r:r[2].startswith('D1')),
('Maps 9–17 · M2',lambda r:r[2].startswith('Map') and int(r[2].split()[1])>=9),
('Dungeons D2–D5 · M2',lambda r:r[2][:2] in('D2','D3','D4','D5')),
('Tribulation',lambda r:r[2]=='Tribulation'),
('Pets (15 × 3 stages) · M2',lambda r:r[2]=='Pet')]
out=[]
out.append('''# 10 — Character Prompt Pack (monsters, bosses, pets)

Everything painted that is still to generate for **v1.0** (maps 1–17, dungeons D1–D5, pets T1–T6), in the **official GPT style** ([08-Art-Bible §3](08-Art-Bible.md)). A matching checklist you can tick off lives in [`art/character_manifest.csv`](art/character_manifest.csv).

## How to use
1. **Generate bases first.** Rows marked **NEW** are fresh designs. Rows marked **EDIT** are made *from* another image: attach the base image named in the prompt and paste the prompt. Editing from a base keeps whole families consistent (all golems, all bandits, all wolves) and is faster than new designs.
2. **Always attach two style references** as well: the approved hero (`art/masters/hero_official/m_stand_original.png`) and one approved monster (`art/masters/monsters/b2_ember_wolf.png`).
3. **Paste the prompt exactly.** The style text is already appended.
4. **Pick 1 of 4.** Generate 4 variations, keep the best. Reject any with: a checkerboard or solid background, text, a second creature (except Swarm rows), cropped limbs, or a creature facing right.
5. **Save** as `art/monsters/<id>.png` (pets: `art/pets/<id>.png`), using the id in the list. Tick the row in the CSV.
6. **Send me batches.** I check each one in its battle scene for facing, scale, readability and style, and key out any fake background.

**Totals:** 195 rows · 4 done · **78 NEW** · **112 EDIT** · 1 handled in code. At ~4 tries per keeper, about 760 generations.

## Size classes (in-game height on the battle stage)
| Class | Height | Notes |
|---|---|---|
| Swarm | 90 px (group) | One image with three identical small creatures |
| Swift | 95 px | |
| Caster | 100 px | Floating ones hover ~10 px above the ground |
| Tank | 110 px | |
| Brute | 120 px | |
| Mini-boss | 150 px | Dungeon wave 10 |
| Boss | 190 px | Map and dungeon bosses |
| Pets | 70 / 85 / 100 px | Stage 1 / 2 / 3, beside the hero |

Phase 2 of a boss (shed skin, enraged, flying) is done with code effects (tint, aura, particles), **not** new art.

## Recommended order
1. **Family bases (M1):** Bandit Thug, Lake Frog, Charcoal Golem, Fire Imp Swarm, Red Ape, Stone Guardian, Water Wraith, Skeleton Disciple, Puppet Sentinel, Bog Lizard, Marsh Troll, Icicle Bats, Glacier Bear, Frost Witch, Static Wisp, Silver Heron, Ruin Crow.
2. **The rest of maps 1–8 and D1**, map by map, so each map can be checked as a set.
3. **M1 bosses:** Bandit Chief Zhao, Lake Serpent, Flame Ape, Fallen Elder, Thunder Hawk, Thousand-Year Toad, Frost Qilin, Crystal Vein Wyrm.
4. **Pets stage 1 for T1–T3**, then their stages 2 and 3.
5. **Maps 9–17, D2–D5 and the rest of the pets** (M2).
''')
for title,f in SECTIONS:
    rows=[r for r in R if f(r)]
    out.append(f'\n## {title} ({len(rows)})\n')
    for r in rows:
        rid,name,where,arch,el,ms,method,base,core=r
        tag={'DONE':'✅ DONE','NEW':'🆕 NEW','EDIT':f'✏️ EDIT of `{base}`','CODE':'⚙️ CODE'}[method]
        out.append(f'**`{rid}` · {name}** — {where} · {arch} · {el} · {tag}  ')
        p=prompt(r)
        out.append(('> '+p) if p else ('> '+core if method=='CODE' else '> Approved. Master in `art/masters/monsters/`.'))
        out.append('')
open('/Users/eric/Documents/Apps/Mobile/Idle Cultivation/10-Character-Prompt-Pack.md','w').write('\n'.join(out))
print(sum(len(x) for x in out)//1024,'KB')
