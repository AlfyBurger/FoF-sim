#!/usr/bin/env python3
"""Extract the component images the renderer needs from the official Vassal module.

The art is GMT's and is not kept in this repository. Run this once per machine/session:

    python3 tools/extract_assets.py /path/to/FoF_All_Volumes_v5_0_2.vmod

It copies into assets/ (git-ignored):
  - every image named in ui/catalog.json,
  - every image named in any games/*/state.json map,
  - the Normandy terrain deck (N01-N55), card backs, and the action cards (A01-A50).
Use --all to extract every image of the module instead.
"""
import argparse, glob, json, os, re, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def wanted_names():
    names = set()
    cat = json.load(open(os.path.join(ROOT, "ui", "catalog.json")))
    for group in cat.values():
        names.update(v for v in group.values() if isinstance(v, str))
    for st in glob.glob(os.path.join(ROOT, "games", "*", "state.json")):
        s = json.load(open(st))
        for row in s.get("map", {}).values():
            for card in row:
                names.update(v for k, v in card.items() if k in ("img", "under", "back"))
    return names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vmod")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out", default=os.path.join(ROOT, "assets"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    want = wanted_names()
    pat = re.compile(r"^(N\d\d .+\.jpg|A\d\d\.jpg|Card Back - .+|Reshuffle Card\.png)$")
    n = 0
    with zipfile.ZipFile(a.vmod) as z:
        for info in z.infolist():
            if not info.filename.startswith("images/") or info.is_dir():
                continue
            base = info.filename[len("images/"):]
            if "/" in base:
                continue
            if a.all or base in want or pat.match(base):
                with z.open(info) as src, open(os.path.join(a.out, base), "wb") as dst:
                    dst.write(src.read())
                n += 1
    missing = sorted(w for w in want if not os.path.exists(os.path.join(a.out, w)))
    print(f"extracted {n} images to {a.out}")
    if missing:
        print("MISSING:", missing)


if __name__ == "__main__":
    main()
