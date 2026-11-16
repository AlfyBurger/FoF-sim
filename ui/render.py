#!/usr/bin/env python3
"""Render a Fields of Fire board from a game-state JSON using the Vassal module art.

Usage: python3 ui/render.py <state.json> <out.jpg> [--images DIR] [--catalog catalog.json]
Images come from assets/, filled by tools/extract_assets.py from the Vassal module (art is not in the repo).

state.json (minimal):
{
  "title": "...", "turn": 1, "visibility": "Daylight", "activity": "No Contact",
  "map": {"R3": [card, card, card], "R2": [...], "R1": [...], "S": [...]},   # card = {"img": "N17 Woods.jpg", "under": "N01 Hill.jpg"} or {"back": "Card Back - Normandy.jpg"}
  "units": {"1/1": "R1C1", ...},          # unit name -> card id (R<row>C<col>, S<col> for staging)
  "exposed": ["1/1", ...], "pinned": [...],
  "commands": {"1st PLT HQ": {"available": 0, "saved": 0, "status": "..."}},
  "notes": ["free text lines for the side panel"]
}
catalog.json: {"units": {"1/1": "2nd_1-1.png", ...}, "markers": {...}, "commands": {"1st PLT HQ": "Commands_1st PLT.png"}}
"""
import json, sys, argparse, os
from PIL import Image, ImageDraw, ImageFont

CW, CH = 220, 308          # terrain card size on the board
CS = 62                    # counter size
GAP = 26                   # gap between cards (room for markers between cards)
PANEL = 300
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load(images, name, size=None):
    im = Image.open(os.path.join(images, name)).convert("RGBA")
    return im.resize(size, Image.LANCZOS) if size else im


def counter(images, cat, unit, state):
    im = load(images, cat["units"][unit], (CS, CS))
    if unit in state.get("pinned", []):
        lay = load(images, cat["markers"]["pinned_layer"])
        lay = lay.resize((CS, int(CS * lay.height / lay.width)))
        im.alpha_composite(lay, (0, CS - lay.height))
    elif unit in state.get("exposed", []):
        lay = load(images, cat["markers"]["exposed_layer"])
        lay = lay.resize((CS, int(CS * lay.height / lay.width)))
        im.alpha_composite(lay, (0, CS - lay.height))
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("state"); ap.add_argument("out")
    ap.add_argument("--images", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"),
                    help="folder of component images (see tools/extract_assets.py)")
    ap.add_argument("--catalog", default=os.path.join(os.path.dirname(__file__), "catalog.json"))
    a = ap.parse_args()
    st = json.load(open(a.state)); cat = json.load(open(a.catalog)); images = a.images

    rows = [r for r in st["map"] if r != "S"]
    rows.sort(key=lambda r: -int(r[1:]))                       # highest row at the top
    order = rows + (["S"] if "S" in st["map"] else [])
    ncol = max(len(v) for v in st["map"].values())
    W = GAP + ncol * (CW + GAP) + PANEL
    H = 40 + len(order) * (CH + GAP) + GAP
    img = Image.new("RGBA", (W, H), (58, 66, 52, 255))
    d = ImageDraw.Draw(img)
    f_big, f_lab, f_txt = ImageFont.truetype(FONT, 22), ImageFont.truetype(FONT, 15), ImageFont.truetype(FONT_R, 14)
    d.text((GAP, 8), st.get("title", ""), font=f_big, fill="white")

    # which units sit on which card
    on = {}
    for u, cid in st["units"].items():
        on.setdefault(cid, []).append(u)

    for ri, r in enumerate(order):
        y = 40 + ri * (CH + GAP)
        for ci, card in enumerate(st["map"][r]):
            x = GAP + ci * (CW + GAP)
            cid = f"S{ci+1}" if r == "S" else f"{r}C{ci+1}"
            if card.get("under"):                               # hill underneath, offset
                img.alpha_composite(load(images, card["under"], (CW, CH)), (x + 16, y - 14))
            face = card.get("img") or card.get("back")
            c = load(images, face, (CW, CH))
            if r == "S":                                        # dim the staging cards
                c = Image.blend(c, Image.new("RGBA", c.size, (40, 40, 40, 255)), 0.45)
            img.alpha_composite(c, (x, y))
            # card label
            lab = cid + ("  Staging" if r == "S" else "")
            tw = d.textlength(lab, font=f_lab)
            d.rounded_rectangle((x + 4, y + CH - 24, x + 12 + tw, y + CH - 4), 4, fill=(0, 0, 0, 170))
            d.text((x + 8, y + CH - 23), lab, font=f_lab, fill="white")
            # counters: grid of 3 per row starting a bit below the card header
            units = on.get(cid, [])
            for k, u in enumerate(units):
                cx = x + 8 + (k % 3) * (CS + 6)
                cy = y + (24 if r == "S" else 92) + (k // 3) * (CS + 6)
                sh = Image.new("RGBA", (CS, CS), (0, 0, 0, 120))
                img.alpha_composite(sh, (cx + 3, cy + 3))
                img.alpha_composite(counter(images, cat, u, st), (cx, cy))

    # side panel
    px = GAP + ncol * (CW + GAP) + 6
    d.rounded_rectangle((px, 40, W - 14, H - GAP), 10, fill=(30, 34, 28, 255))
    yy = 52
    d.text((px + 12, yy), f"Turn {st.get('turn', '?')}", font=f_big, fill="white"); yy += 34
    if st.get("phase"):
        for line in wrap(d, st["phase"], f_txt, PANEL - 40):
            d.text((px + 12, yy), line, font=f_txt, fill=(220, 220, 200)); yy += 18
        yy += 6
    mk = [cat["markers"].get(st.get("visibility")), cat["markers"].get(st.get("activity"))]
    mx = px + 12
    for m in mk:
        if m:
            img.alpha_composite(load(images, m, (70, 70)), (mx, yy)); mx += 80
    yy += 84
    for hq, c in st.get("commands", {}).items():
        icon = cat.get("commands", {}).get(hq)
        if icon:
            img.alpha_composite(load(images, icon, (48, 48)), (px + 12, yy))
        d.text((px + 68, yy + 2), hq, font=f_lab, fill="white")
        d.text((px + 68, yy + 22), f"available {c.get('available', 0)} · saved {c.get('saved', 0)}", font=f_txt, fill=(220, 220, 200))
        yy += 58
    yy += 6
    for n in st.get("notes", []):
        for line in wrap(d, n, f_txt, PANEL - 40):
            d.text((px + 12, yy), line, font=f_txt, fill=(220, 220, 200)); yy += 18
        yy += 4
    img.convert("RGB").save(a.out, quality=85)


def wrap(d, text, font, width):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) > width and cur:
            out.append(cur); cur = w
        else:
            cur = t
    if cur: out.append(cur)
    return out


if __name__ == "__main__":
    main()
