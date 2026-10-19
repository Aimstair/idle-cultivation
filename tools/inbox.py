#!/usr/bin/env python3
"""Character art drop-folder tool.

Workflow: generate in ChatGPT -> save into art/_inbox/ -> run `process`.

  python3 tools/inbox.py next [--n 25]          build the "Next up" page (art/_review/next.html)
  python3 tools/inbox.py process                match, clean, stage and queue everything in art/_inbox/
  python3 tools/inbox.py approve ID [ID ...]    mark rows done (or --all to approve every row in review)
  python3 tools/inbox.py redo ID --note "why"   send a row back to the queue
  python3 tools/inbox.py status                 counts per status

Files in the inbox are matched to checklist rows by name (the file name contains the row id,
e.g. m01_boar.png). Files without an id are matched in save-time order to the rows on the
current "Next up" page and flagged so you can confirm the match on the review page.
"""
import argparse, base64, csv, html, io, json, os, shutil, subprocess, sys, time
from collections import deque
from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "art"
MANIFEST = ART / "character_manifest.csv"
INBOX = ART / "_inbox"
REVIEW = ART / "_review"
BG_CACHE = REVIEW / "_bg"
NEXT_JSON = REVIEW / "next.json"
def find_chrome():
    """Chrome/Edge for rendering battle backgrounds. Override with the CHROME_PATH environment variable."""
    cands = [os.environ.get("CHROME_PATH", ""),
             "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
             r"C:\Program Files\Google\Chrome\Application\chrome.exe",
             r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
             os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
             r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
             r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"]
    cands += [shutil.which(n) or "" for n in ("google-chrome", "chromium", "chrome", "msedge")]
    return next((c for c in cands if c and os.path.exists(c)), None)


CHROME = find_chrome()
HERO = ART / "masters" / "hero_official" / "m_battle_cutout.png"
HERO_STAND = ART / "masters" / "hero_official" / "m_stand_original.png"
WOLF_REF = ART / "masters" / "monsters" / "b2_ember_wolf.png"
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}

# on-stage height in px (battle stage is 390x560, ground line at y=406)
HEIGHT = {"Swarm": 90, "Swift": 95, "Caster": 100, "Tank": 110, "Brute": 120,
          "Mini-boss": 150, "Boss": 190, "Pet S1": 70, "Pet S2": 85, "Pet S3": 100}
FLOAT = {"Caster": 10}  # casters hover a little


# ---------------------------------------------------------------- manifest

def load():
    with open(MANIFEST, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(rows):
    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def art_dir(row):
    return ART / ("pets" if row["where"] == "Pet" else "monsters")


def clean_path(row):
    return art_dir(row) / f"{row['id']}.png"


def scene_for(row):
    w = row["where"]
    if w.startswith("Map"):
        return f"map{int(w.split()[1]):02d}"
    if w[:1] == "D" and w[1:2].isdigit():
        return f"dun{int(w[1]):02d}"
    if w == "Pet":
        return "map01"
    return "map01"


# ---------------------------------------------------------------- next up

def ordered_queue(rows):
    """Rows that can be generated now: todo/redo whose base (if any) is approved."""
    by_id = {r["id"]: r for r in rows}
    is_base = {r["attach_base"] for r in rows if r["attach_base"]}

    def ready(r):
        b = r["attach_base"]
        return not b or b == "hero" or (b in by_id and by_id[b]["status"] == "done")

    q = [r for r in rows if r["status"] in ("todo", "redo") and ready(r)]
    order = {r["id"]: i for i, r in enumerate(rows)}
    q.sort(key=lambda r: (r["status"] != "redo", r["milestone"], r["id"] not in is_base, order[r["id"]]))
    return q


HUMAN_NEW = {"m02_thug", "m02_zhao", "m05_elder", "m08_witch", "m16_knight", "m17_vanguard", "m17_general", "d2_shade"}


def root_id(row, by_id):
    seen = 0
    while row["attach_base"] in by_id and seen < 10:
        row = by_id[row["attach_base"]]
        seen += 1
    return row["id"]


def attach_files(row, by_id):
    """EDIT rows: only the approved base. NEW rows: style references (hero only for human enemies)."""
    b = row["attach_base"]
    if row["method"] == "EDIT" and b in by_id:
        files = [clean_path(by_id[b])]
    else:
        human = row["id"] in HUMAN_NEW or root_id(row, by_id) in ("m02_thug", "m08_witch")
        files = ([HERO_STAND] if human else []) + [WOLF_REF]
        if b in by_id:  # new design with a family reference (e.g. a boss attached to its minion)
            files.insert(0, clean_path(by_id[b]))
    return [f for f in files if f.exists()]


def data_uri(path, cache={}):
    """Embed an attach image in the page (max 1024 px) so it can be copied to the clipboard."""
    if path not in cache:
        im = Image.open(path).convert("RGBA")
        im.thumbnail((1024, 1024), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "PNG", optimize=True)
        cache[path] = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
    return cache[path]


def cmd_next(n):
    rows = load()
    by_id = {r["id"]: r for r in rows}
    q = ordered_queue(rows)[:n]
    NEXT_JSON.write_text(json.dumps([r["id"] for r in q]), encoding="utf-8")
    attach_root = REVIEW / "attach"
    shutil.rmtree(attach_root, ignore_errors=True)
    images, cards = {}, []
    for i, r in enumerate(q, 1):
        files = attach_files(r, by_id)
        folder = attach_root / r["id"]
        folder.mkdir(parents=True, exist_ok=True)
        figs = []
        for f in files:
            shutil.copy(f, folder / f.name)
            key = f"i{len(images)}" if str(f) not in images else images[str(f)][0]
            images.setdefault(str(f), (key, data_uri(f)))
            figs.append(f'<figure><img data-k="{key}" alt="{html.escape(f.name)}"><figcaption>{html.escape(f.name)}</figcaption>'
                        f'<button class="ci" onclick="ci(\'{key}\',this)">Copy image</button></figure>')
        note = f'<p class="redo">Redo: {html.escape(r["notes"])}</p>' if r["status"] == "redo" and r["notes"] else ""
        cards.append(f'''<section class="card"><div class="hd"><span class="n">{i}</span>
<b>{html.escape(r["name"])}</b><span class="tag">{html.escape(r["where"])} · {r["archetype"]} · {r["element"]} · {r["method"]}</span></div>
{note}<div class="fn">Save as <code>{r["id"]}.png</code> into <code>art/_inbox/</code></div>
<div class="att">{"".join(figs)}</div>
<div class="fb">Copy not working? The same images are in <code>art/_review/attach/{r["id"]}/</code>: drag them from Finder.</div>
<textarea readonly id="p{i}">{html.escape(r["prompt"])}</textarea>
<button onclick="cp('p{i}',this)">Copy prompt</button></section>''')
    img_js = json.dumps({k: uri for k, uri in images.values()})
    page = f'''<!doctype html><html><head><meta charset="utf-8"><title>Next up</title>
<style>body{{font:14px -apple-system,system-ui,sans-serif;background:#1E1A2A;color:#EDE6F7;margin:0;padding:20px}}
h1{{margin:0 0 4px}} .sub{{color:#A79CC4;margin:0 0 16px}}
.card{{background:#2A2340;border:1px solid #3A3350;border-radius:12px;padding:14px;margin:0 0 14px;max-width:980px}}
.hd{{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}} .n{{background:#FFE7A0;color:#2A1008;border-radius:999px;padding:0 9px;font-weight:800}}
b{{font-size:17px}} .tag{{color:#A79CC4}} .fn{{margin:6px 0}} code{{background:#120E1C;padding:1px 6px;border-radius:4px;color:#9AF6FF}}
.redo{{color:#FF9A80;margin:6px 0}} .att{{display:flex;gap:10px;margin:8px 0}} figure{{margin:0;text-align:center}}
.att img{{height:120px;background:#E7A9B8;border-radius:8px;display:block}} figcaption{{font-size:11px;color:#8E84A8}}
.ci{{margin-top:4px;padding:4px 10px;font-size:12px;background:#4A3F7A}} .fb{{font-size:12px;color:#8E84A8;margin:2px 0 8px}}
textarea{{width:100%;height:96px;background:#120E1C;color:#EDE6F7;border:1px solid #3A3350;border-radius:8px;padding:8px;font:12px ui-monospace,Menlo,monospace}}
button{{margin-top:6px;background:#1F8F6E;color:#fff;border:0;border-radius:8px;padding:7px 14px;font-weight:700;cursor:pointer}}</style></head>
<body><h1>Next up · {len(q)} images</h1>
<p class="sub">For each card: click <b>Copy image</b> and paste it into ChatGPT with ⌘V (repeat for each image), then <b>Copy prompt</b> and paste. Pick the best variation and save it as the file name shown into <code>art/_inbox/</code>. Then ask Claude to "check inbox" (or run <code>python3 tools/inbox.py process</code>).</p>
{"".join(cards) or "<p>Nothing ready: approve the images in review first.</p>"}
<script>const IMG={img_js};
document.querySelectorAll('img[data-k]').forEach(i=>i.src=IMG[i.dataset.k]);
function flash(b,t,o){{b.textContent=t;setTimeout(()=>b.textContent=o,1400)}}
function ci(k,b){{try{{const item=new ClipboardItem({{'image/png':fetch(IMG[k]).then(r=>r.blob())}});
navigator.clipboard.write([item]).then(()=>flash(b,'Copied: paste with ⌘V','Copy image'),()=>flash(b,'Blocked: use the Finder folder','Copy image'))}}
catch(e){{flash(b,'Blocked: use the Finder folder','Copy image')}}}}
function cp(id,b){{const t=document.getElementById(id);t.select();
(navigator.clipboard?navigator.clipboard.writeText(t.value):Promise.reject()).catch(()=>document.execCommand('copy')).finally(()=>flash(b,'Copied','Copy prompt'))}}</script></body></html>'''
    (REVIEW / "next.html").write_text(page, encoding="utf-8")
    print(f"Next up: {len(q)} rows -> {REVIEW / 'next.html'}")


# ---------------------------------------------------------------- cleaning

def classify_background(im):
    """'alpha' (real transparency), 'light' (white or fake checkerboard), 'dark' (solid black) or 'unknown'."""
    a = im.getchannel("A")
    if a.getextrema()[0] < 10 and sum(a.histogram()[:10]) > 0.05 * im.width * im.height:
        return "alpha"
    rgb = im.convert("RGB")
    w, h = rgb.size
    border = [rgb.getpixel((x, y)) for x in range(0, w, 8) for y in (0, h - 1)] + \
             [rgb.getpixel((x, y)) for y in range(0, h, 8) for x in (0, w - 1)]
    light = sum(1 for c in border if min(c) >= 212 and max(c) - min(c) <= 14)
    dark = sum(1 for c in border if max(c) <= 12)
    if light > 0.8 * len(border):
        return "light"
    if dark > 0.8 * len(border):
        return "dark"
    return "unknown"


def key_out(im, mode):
    rgb = im.convert("RGB")
    w, h = rgb.size
    px = rgb.load()
    isbg = (lambda c: min(c) >= 212 and max(c) - min(c) <= 14) if mode == "light" else (lambda c: max(c) <= 12)
    bg = bytearray(w * h)
    q = deque([(x, y) for x in range(w) for y in (0, h - 1)] + [(x, y) for y in range(h) for x in (0, w - 1)])
    while q:
        x, y = q.popleft()
        i = y * w + x
        if bg[i] or not isbg(px[x, y]):
            continue
        bg[i] = 1
        if x > 0: q.append((x - 1, y))
        if x < w - 1: q.append((x + 1, y))
        if y > 0: q.append((x, y - 1))
        if y < h - 1: q.append((x, y + 1))
    alpha = Image.frombytes("L", (w, h), bytes(0 if b else 255 for b in bg))
    alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    out = rgb.convert("RGBA")
    out.putalpha(alpha)
    return out


def clean(src):
    """Returns (clean RGBA image trimmed to content, list of flags)."""
    im = Image.open(src).convert("RGBA")
    flags = []
    if min(im.size) < 1000:
        flags.append(f"low resolution {im.width}x{im.height} (want 1024+)")
    kind = classify_background(im)
    if kind in ("light", "dark"):
        im = key_out(im, kind)
        flags.append({"light": "white/checkerboard background keyed out",
                      "dark": "black background keyed out"}[kind])
    elif kind == "unknown":
        flags.append("background not recognised: check the cutout")
    a = im.getchannel("A").point(lambda v: 255 if v > 20 else 0)
    bb = a.getbbox()
    if not bb:
        return None, flags + ["image is empty after cutout"]
    edge = 3
    if bb[0] <= edge or bb[1] <= edge or bb[2] >= im.width - edge or bb[3] >= im.height - edge:
        flags.append("touches the image edge: may be cropped")
    return im.crop(bb), flags


# ---------------------------------------------------------------- staging

def bg_image(scene):
    BG_CACHE.mkdir(parents=True, exist_ok=True)
    out = BG_CACHE / f"{scene}.png"
    if out.exists():
        return Image.open(out).convert("RGB")
    layers = "".join(
        f'<img src="{(ART / "bg" / "battle" / f"{scene}_{l}.svg").as_uri()}" style="position:absolute;left:0;top:0;width:780px;height:560px">'
        for l in ("far", "mid", "near"))
    page = BG_CACHE / f"{scene}.html"
    page.write_text(f'<!doctype html><html><body style="margin:0"><div style="position:relative;width:390px;height:560px;overflow:hidden">{layers}</div></body></html>', encoding="utf-8")
    if not CHROME:
        sys.exit("Chrome or Edge not found: install Chrome or set the CHROME_PATH environment variable.")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                    "--force-device-scale-factor=1", f"--screenshot={out}", "--window-size=390,560", page.as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    return Image.open(out).convert("RGB")


_hero = None


def hero():
    global _hero
    if _hero is None:
        im = Image.open(HERO).convert("RGBA")
        _hero = im.crop(im.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox())
    return _hero


def fit(im, h):
    return im.resize((max(1, round(h * im.width / im.height)), h), Image.LANCZOS)


def stage(row, sprite):
    stage_img = bg_image(scene_for(row)).convert("RGBA")
    ground = 406
    hh = fit(hero(), 170)
    stage_img.alpha_composite(hh, (110 - hh.width // 2, ground - hh.height))
    h = HEIGHT.get(row["archetype"], 100)
    sp = fit(sprite, h)
    if row["where"] == "Pet":
        x = 185 - sp.width // 2
    else:
        x = min(388 - sp.width, max(200, 285 - sp.width // 2))
    stage_img.alpha_composite(sp, (x, ground - FLOAT.get(row["archetype"], 0) - sp.height))
    return stage_img.convert("RGB")


# ---------------------------------------------------------------- process

def cmd_process():
    rows = load()
    by_id = {r["id"]: r for r in rows}
    ids_by_len = sorted(by_id, key=len, reverse=True)
    files = sorted([p for p in INBOX.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXT],
                   key=lambda p: p.stat().st_mtime)
    if not files:
        print("Inbox is empty.")
        return
    queue = json.loads(NEXT_JSON.read_text(encoding="utf-8")) if NEXT_JSON.exists() else []
    named = {}
    unnamed = []
    for p in files:
        hit = next((i for i in ids_by_len if i.lower() in p.stem.lower()), None)
        (named.__setitem__(p, hit) if hit else unnamed.append(p))
    taken = set(named.values())
    open_slots = [i for i in queue if i not in taken and by_id[i]["status"] in ("todo", "redo")]
    matches = [(p, i, False) for p, i in named.items()]
    for p in unnamed:
        if open_slots:
            matches.append((p, open_slots.pop(0), True))
        else:
            print(f"  ! {p.name}: no id in the name and no open slot on the Next up page; left in the inbox")
    stamp = time.strftime("%Y%m%d-%H%M%S")
    done = []
    for p, rid, by_order in matches:
        row = by_id[rid]
        sprite, flags = clean(p)
        if by_order:
            flags.insert(0, f"matched by save order from '{p.name}': confirm it is the right row")
        if sprite is None:
            print(f"  x {p.name}: {flags[-1]}")
            continue
        d = art_dir(row)
        (d / "_originals").mkdir(parents=True, exist_ok=True)
        shutil.copy(p, d / "_originals" / f"{rid}{p.suffix.lower()}")
        sprite.save(clean_path(row))
        stage(row, sprite).save(REVIEW / f"{rid}.jpg", quality=88)
        row["status"] = "review"
        row["notes"] = "; ".join(flags)
        (INBOX / "processed").mkdir(exist_ok=True)
        shutil.move(str(p), INBOX / "processed" / f"{stamp}_{p.name}")
        done.append(rid)
        print(f"  ✓ {rid:<22} {row['name']}" + (f"  [{row['notes']}]" if flags else ""))
    save(rows)
    build_review(rows)
    print(f"Processed {len(done)} image(s). Review page: {REVIEW / 'index.html'}")


def build_review(rows):
    rv = [r for r in rows if r["status"] == "review"]
    cards = "".join(
        f'''<figure><img src="{r['id']}.jpg" width="390" height="560"><figcaption><b>{html.escape(r['name'])}</b>
<code>{r['id']}</code><br>{html.escape(r['where'])} · {r['archetype']} · {r['element']}
{('<p class="fl">' + html.escape(r['notes']) + '</p>') if r['notes'] else ''}</figcaption></figure>'''
        for r in rv)
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    summary = " · ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
    (REVIEW / "index.html").write_text(f'''<!doctype html><html><head><meta charset="utf-8"><title>Review</title>
<style>body{{font:14px -apple-system,system-ui,sans-serif;background:#1E1A2A;color:#EDE6F7;margin:0;padding:20px}}
.sub{{color:#A79CC4}} .g{{display:flex;flex-wrap:wrap;gap:18px}} figure{{margin:0;width:390px}} img{{border-radius:10px;display:block}}
figcaption{{margin-top:6px;line-height:1.4}} code{{color:#9AF6FF;margin-left:6px}} .fl{{color:#FF9A80;margin:4px 0}}</style></head>
<body><h1>Review · {len(rv)} waiting</h1><p class="sub">{summary}. Approve with <code>python3 tools/inbox.py approve ID ...</code> or <code>--all</code>; send back with <code>redo ID --note "why"</code>. Or just tell Claude.</p>
<div class="g">{cards or "<p>Nothing waiting for review.</p>"}</div></body></html>''', encoding="utf-8")


# ---------------------------------------------------------------- approve / redo / status

def cmd_approve(ids, all_review):
    rows = load()
    n = 0
    for r in rows:
        if (all_review and r["status"] == "review") or r["id"] in ids:
            if r["status"] != "review" and not clean_path(r).exists():
                print(f"  ! {r['id']}: no image yet, skipped")
                continue
            r["status"] = "done"
            n += 1
    save(rows)
    build_review(rows)
    print(f"Approved {n}.")
    cmd_next(25)


def cmd_redo(ids, note):
    rows = load()
    for r in rows:
        if r["id"] in ids:
            r["status"] = "redo"
            r["notes"] = note or r["notes"]
    save(rows)
    build_review(rows)
    print(f"Sent back {len(ids)}.")
    cmd_next(25)


def cmd_status():
    rows = load()
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(" · ".join(f"{k}: {v}" for k, v in sorted(counts.items())), f"(total {len(rows)})")
    print(f"Ready to generate now: {len(ordered_queue(rows))}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # Windows consoles default to a legacy code page
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("next"); n.add_argument("--n", type=int, default=25)
    sub.add_parser("process")
    a = sub.add_parser("approve"); a.add_argument("ids", nargs="*"); a.add_argument("--all", action="store_true")
    r = sub.add_parser("redo"); r.add_argument("ids", nargs="+"); r.add_argument("--note", default="")
    sub.add_parser("status")
    args = ap.parse_args()
    REVIEW.mkdir(parents=True, exist_ok=True)
    INBOX.mkdir(parents=True, exist_ok=True)
    if args.cmd == "next": cmd_next(args.n)
    elif args.cmd == "process": cmd_process()
    elif args.cmd == "approve": cmd_approve(set(args.ids), args.all)
    elif args.cmd == "redo": cmd_redo(set(args.ids), args.note)
    elif args.cmd == "status": cmd_status()


if __name__ == "__main__":
    main()
