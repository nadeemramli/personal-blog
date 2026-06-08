#!/usr/bin/env python3
"""Idempotency QC for product notes.
Usage: python3 os_qc_ids.py "<path to '2. Catalog' folder>"

Rules enforced (one note per product_id = compound+spec+vendor):
 1. every product note has product_id, compound, vendor
 2. product_id is unique across Stock + Wishlist
 3. product_id == slug(filename)  (rename-drift detection)
 4. status 'planned' only in Wishlist/; everything else only in Stock/
 5. same compound may appear multiple times ONLY with different vendors/specs
 6. frontmatter must start with --- and contain no invalid \| YAML escapes
"""
import os, re, sys

CAT = sys.argv[1] if len(sys.argv) > 1 else "2. Catalog"
PROD = os.path.join(CAT, "Products")

def fm_get(txt, key):
    m = re.search(rf'^{key}:\s*"?([^"\n]*)"?\s*$', txt, re.M)
    return (m.group(1).strip() if m else "")

def slug(s):
    s = s.lower().replace("×", "x").replace("—", "-").replace("+", "plus").replace("%", "pct")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")

ids, problems, compounds = {}, [], {}
for root, dirs, files in os.walk(PROD):
    for fn in sorted(files):
        if not fn.endswith(".md") or fn.startswith("0. "):
            continue
        fp = os.path.join(root, fn)
        txt = open(fp, encoding="utf-8", errors="surrogateescape").read()
        if fm_get(txt, "type") != "product":
            continue
        rel = os.path.relpath(fp, PROD)
        if not txt.startswith("---"):
            problems.append("BROKEN FRONTMATTER (missing opening ---): " + rel)
        fm_m = re.match(r'^---\n(.*?)\n---', txt, re.S)
        if fm_m and "\\|" in fm_m.group(1):
            problems.append("INVALID YAML (\\| escape in frontmatter): " + rel)
        if txt.count("[[") != txt.count("]]"):
            problems.append("UNBALANCED WIKILINKS: " + rel)
        pid, comp, ven, st = (fm_get(txt, k) for k in ("product_id", "compound", "vendor", "status"))
        for k, v in (("product_id", pid), ("compound", comp), ("vendor", ven)):
            if not v:
                problems.append("MISSING " + k + ": " + rel)
        if pid:
            if pid in ids:
                problems.append("DUPLICATE product_id '" + pid + "': " + rel + "  <-> " + ids[pid])
            ids[pid] = rel
            if pid != slug(fn[:-3]):
                problems.append("ID/FILENAME DRIFT: " + rel + " (id=" + pid + ", expected " + slug(fn[:-3]) + ")")
        in_wishlist = rel.startswith("Wishlist")
        if st == "planned" and not in_wishlist:
            problems.append("PLANNED OUTSIDE WISHLIST: " + rel)
        if st not in ("planned", "") and in_wishlist:
            problems.append("NON-PLANNED IN WISHLIST: " + rel + " (status=" + st + ")")
        if comp:
            compounds.setdefault(comp, []).append(rel)

print("product notes: " + str(len(ids)))
multi = {c: v for c, v in compounds.items() if len(v) > 1}
if multi:
    print("\ncompounds with multiple offers (OK if vendors/specs differ):")
    for c, v in multi.items():
        print("  " + c + ":")
        for r in v:
            print("    - " + r)
if problems:
    print("\nPROBLEMS:")
    for p in problems:
        print("  " + p)
    sys.exit(1)
print("\nOK - all product notes idempotent.")
