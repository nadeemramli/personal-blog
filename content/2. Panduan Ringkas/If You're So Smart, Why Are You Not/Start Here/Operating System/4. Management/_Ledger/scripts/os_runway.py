#!/usr/bin/env python3
"""Overall stock runway v3 — functional stacks (freq-ordered) + cut-aligned seasonal."""
import os, glob, re, yaml, datetime, html, sys
PROD = sys.argv[1] if len(sys.argv)>1 else "2. Catalog/Products"
OUT  = sys.argv[2] if len(sys.argv)>2 else "4. Management/_Ledger/charts/overall_runway.svg"
TODAY=datetime.date(2026,6,14); HEND=datetime.date(2027,12,31)
CUTS=[(datetime.date(2026,7,14),84),(datetime.date(2027,6,1),84)]
DPW={"ED":7.0,"EOD":3.5,"ITD":4.0,"OCC":4.0,"TD":6.0,"5x":5.0,"1-2x":1.5,"E3D":2.33,"E4D":1.75}
FREQ={"ED":"daily","EOD":"EOD","ITD":"intra-WO","OCC":"occ","TD":"training","5x":"5×/wk","1-2x":"1–2×/wk","E3D":"e3d","E4D":"e4d"}
FRANK={"ED":0,"EOD":1,"5x":1,"ITD":2,"TD":3,"E4D":4,"E3D":4,"OCC":5,"1-2x":5}
PED_CAL={"Etho Testosterone 450":(350,52),"Oxandrolone (Anavar)":(240,16),"MK-677":(140,24),
 "Trenbolone Acetate":(70,8),"Proviron":(175,8),"Levothyroxine (T4)":(700,16),
 "Cytolin (Cytomel / T3)":(175,16),"Cardarine (GW-501516)":(105,8)}
PED_ALIAS={"Acro Trenbolone 100":"Trenbolone Acetate"}
SHORT={"Methylene Blue (USP pharma grade)":"Methylene Blue","Metformin+Empagliflozin FDC":"Metformin+Empagliflozin",
 "TB-500 (Thymosin Beta-4)":"TB-500","Cytolin (Cytomel / T3)":"Cytolin (T3)","Nicorette Gum (nicotine)":"Nicorette Gum",
 "P5P (Pyridoxal-5-Phosphate)":"P5P","Uridine Monophosphate":"Uridine","Cardarine (GW-501516)":"Cardarine",
 "Oral Minoxidil 5mg":"Oral Minoxidil","Zinc Picolinate":"Zinc","Vidalista 10mg":"Tadalafil","Zetiheal 10mg":"Ezetimibe",
 "Nebiheal 5mg":"Nebivolol","Momenta 5mg":"Memantine","Etho Testosterone 450":"Test Enanthate 450",
 "Acro Trenbolone 100":"Trenbolone Acetate"}
GROUPS=[
 ("Daily Cognitive","C","#3E7BC2",["Uridine Monophosphate","CDP-Choline","Bacopa Monnieri","Saffron","Fish Oil (Omega-3)"]),
 ("Daily Antioxidant / CV","C","#1D9E75",["Taurine","Vitamin C","Aged Garlic Extract","Methyl B Complex","TMG (Betaine)","NAC"]),
 ("Daily Protection / Ancillary","C","#7F77DD",["Aspirin","Irbesartan","Zetiheal 10mg","Rosuvastatin","Oral Minoxidil 5mg","Nebiheal 5mg","Vidalista 10mg","GHK-Cu","KPV"]),
 ("Nutrient Partitioning","C","#639922",["Retatrutide","Metformin+Empagliflozin FDC"]),
 ("Every-Other-Day Cognitive","C","#6FA3D6",["L-Theanine","L-Tyrosine","Caffeine","Acetyl L-Carnitine","Nicorette Gum (nicotine)","Ginkgo Biloba","Huperzine-A"]),
 ("Every-Other-Day Androgen Support","C","#D69A3A",["Copper (Bisglycinate)","Selenium","Zinc Picolinate","Boron","DIM"]),
 ("Every-Other-Day Mitochondria Support","C","#0F6E56",["CoQ10","Nicotinamide Riboside","Vitamin D3/K2"]),
 ("Sleep / Recovery","C","#D4537E",["Magnesium Glycinate","Apigenin","Melatonin"]),
 ("Training-Day Performance","C","#D85A30",["Pre-Workout","Intra-Workout","Alpha-GPC","Creatine Monohydrate"]),
 ("TRT Base","C","#5F5E5A",["Etho Testosterone 450"]),
 ("Cut / Seasonal (Cycle-Gated)","S","#D6493F",["MK-677","Oxandrolone (Anavar)","Proviron","Cardarine (GW-501516)","Acro Trenbolone 100","Cytolin (Cytomel / T3)","Levothyroxine (T4)","Mirabegron","Clenbuterol","Ketotifen","Methylene Blue (USP pharma grade)","Momenta 5mg","BHB Salts","C8 MCT Powder","P5P (Pyridoxal-5-Phosphate)"]),
 ("Situational (As-Needed)","X","#9A968F",["Ashwagandha","Modaheal 200mg","Trazodone","Acarbose","BPC-157","TB-500 (Thymosin Beta-4)","TUDCA","Astragalus Root","Calcium D-Glucarate"]),
]
SEASONAL_ORDER=["Trenbolone Acetate","Oxandrolone (Anavar)","Proviron","P5P","Memantine","MK-677","Levothyroxine (T4)","Cytolin (T3)","Mirabegron","Clenbuterol","Ketotifen","Methylene Blue","Cardarine","C8 MCT Powder","BHB Salts"]
GMAP={}
for gi,(gn,gm,gc,members) in enumerate(GROUPS):
    for nm in members: GMAP[nm]=gi
def fm(p):
    t=open(p,encoding="utf-8",errors="surrogateescape").read(); m=re.match(r'^---\n(.*?)\n---',t,re.S)
    try: return yaml.safe_load(m.group(1)) or {}
    except Exception: return {}
def num(v):
    try: return float(v)
    except: return None
def adddays(d,n): return d+datetime.timedelta(days=int(round(n)))
prod={}
for f in glob.glob(os.path.join(PROD,"Stock","**","*.md"),recursive=True):
    d=fm(f)
    if d.get("type")=="product" and d.get("status")=="active" and d.get("name"): prod[d["name"]]=d
items=[]; unsorted=[]
for nm,d in prod.items():
    soh=num(d.get("stock_on_hand"))
    if soh is None: continue
    dosing=str(d.get("dosing") or ""); daily=num(d.get("daily_dose")); wpy=num(d.get("weeks_per_year")) or 52
    du=re.split(r'[ (]',str(d.get("dose_unit") or "mg"))[0] or "mg"
    pkey=PED_ALIAS.get(nm,nm); ped=pkey in PED_CAL
    if ped: wk,w=PED_CAL[pkey]; wpy=w; ann=wk*(w/52.0)/7.0; incut=wk/7.0
    else:
        dpw=DPW.get(dosing); ann=daily*(dpw/7.0)*(wpy/52.0) if (daily and dpw) else None
        incut=daily*(dpw/7.0) if (daily and dpw) else None
    if not ann or ann<=0: continue
    gi=GMAP.get(nm)
    if gi is None: gi=len(GROUPS); unsorted.append(nm)
    mode=GROUPS[gi][1] if gi<len(GROUPS) else "C"
    if mode=="S" and incut:
        rem=soh; ro=None
        for cs,clen in CUTS:
            dosed=clen
            if rem<=incut*dosed: ro=adddays(cs,rem/incut); break
            rem-=incut*dosed
        rdate=ro
    else:
        rdate=adddays(TODAY,soh/ann)
    items.append(dict(nm=SHORT.get(nm,nm),soh=soh,du=du,gi=gi,mode=mode,rdate=rdate,
        freq=FREQ.get(dosing,dosing.lower() or "—"),frank=FRANK.get(dosing,9),incut=incut,wpy=wpy))
W=900; X0=300; X1=872; span=(HEND-TODAY).days; ppd=(X1-X0)/span
def X(dt): return max(X0,min(X1,X0+(dt-TODAY).days*ppd))
def urg(rdate):
    if rdate is None: return "green"
    if rdate<=adddays(TODAY,56): return "red"
    if rdate<=datetime.date(2026,12,31): return "amber"
    if rdate<=HEND: return "blue"
    return "green"
ULAB={"red":"#2F2D2A","amber":"#2F2D2A","blue":"#2F2D2A","green":"#2F2D2A"}
rowH=18; top=96
order=list(range(len(GROUPS)))+([len(GROUPS)] if unsorted else [])
grp_items={gi:[] for gi in order}
for it in items: grp_items[it["gi"]].append(it)
def sortkey(it):
    if it["mode"]=="S":
        try: return (0, SEASONAL_ORDER.index(it["nm"]))
        except ValueError: return (0, 999)
    return (it["frank"], it["rdate"] or datetime.date(2099,1,1))
nrows=sum(len(v) for v in grp_items.values()); ngrp=sum(1 for gi in order if grp_items[gi])
modehead={"C":"CONTINUOUS — year-round","S":"SEASONAL — cut-gated (depletes only in cuts)","X":"SITUATIONAL — as-needed"}
h=top+nrows*rowH+ngrp*22+3*16+70
s=[]
s.append(f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif" role="img">')
s.append(f'<title>Stock runway by functional stack</title><desc>Days of supply per product grouped into functional stacks, ordered by dosing frequency, with cut-aligned seasonal depletion.</desc>')
s.append(f'<rect x="0" y="0" width="{W}" height="{h}" rx="10" fill="#FCFCFB"/>')
s.append(f'<text x="20" y="32" font-size="18" font-weight="600" fill="#2F2D2A">Stock runway — by functional stack</text>')
s.append(f'<text x="20" y="51" font-size="12" fill="#6B6862">Colour = stack · grey shaded columns = cut windows · seasonal bars burn only inside cuts · date red=buy now, amber=this year, green=covered · 2026-06-14 → 2027-12-31</text>')
for cs,clen in CUTS:
    ce=adddays(cs,clen)
    s.append(f'<rect x="{X(cs):.1f}" y="{top-4}" width="{X(ce)-X(cs):.1f}" height="{h-top-46}" fill="#D6493F" fill-opacity="0.06"/>')
    s.append(f'<text x="{(X(cs)+X(ce))/2:.1f}" y="{top-14}" font-size="9.5" text-anchor="middle" fill="#CC0066" fill-opacity="0.85">{cs.year} cut</text>')
d=datetime.date(2026,7,1)
while d<=HEND:
    x=X(d); lab=d.strftime("%b") if d.month!=1 else d.strftime("%b ’%y")
    s.append(f'<line x1="{x:.1f}" y1="{top-2}" x2="{x:.1f}" y2="{h-48}" stroke="#ECEAE6" stroke-width="1"/>')
    s.append(f'<text x="{x:.1f}" y="{top-4}" font-size="9" text-anchor="middle" fill="#9A968F">{lab}</text>')
    mm=d.month+2; yy=d.year+(mm-1)//12; mm=(mm-1)%12+1; d=datetime.date(yy,mm,1)
y=top+12; lastmode=None
for gi in order:
    g=grp_items[gi]
    if not g: continue
    gn,gm,gc = (GROUPS[gi][0],GROUPS[gi][1],GROUPS[gi][2]) if gi<len(GROUPS) else ("Other (Unsorted)","C","#9A968F")
    if gm!=lastmode:
        s.append(f'<text x="20" y="{y+1}" font-size="11" font-weight="600" fill="#8A8782" letter-spacing="0.5">{modehead[gm]}</text>')
        y+=15; lastmode=gm
    s.append(f'<rect x="20" y="{y-11}" width="{W-40}" height="18" rx="4" fill="{gc}" fill-opacity="0.12"/>')
    s.append(f'<circle cx="29" cy="{y-2}" r="4" fill="{gc}"/>')
    s.append(f'<text x="40" y="{y+2}" font-size="11.5" font-weight="600" fill="#2F2D2A">{html.escape(gn)}</text>')
    y+=22
    for it in sorted(g,key=sortkey):
        c=gc; lbl=html.escape(it["nm"][:26]); sub=f'{it["soh"]:g}{it["du"]}'; u=urg(it["rdate"])
        s.append(f'<text x="244" y="{y+3}" font-size="10.5" text-anchor="end" fill="#2F2D2A">{lbl}</text>')
        s.append(f'<text x="250" y="{y+3}" font-size="9" fill="#A8A49C">{it["freq"]}</text>')
        if it["mode"]=="S":
            end=X(it["rdate"]) if it["rdate"] else X1
            s.append(f'<line x1="{X0}" y1="{y-0.5}" x2="{end:.1f}" y2="{y-0.5}" stroke="{c}" stroke-width="1.4" stroke-opacity="0.30"/>')
            rem=it["soh"]; done=False
            for cs,clen in CUTS:
                if done: break
                dseg=clen
                if rem<=it["incut"]*dseg:
                    dout=rem/it["incut"]; x1=X(cs); x2=X(adddays(cs,dout)); xdef=X(adddays(cs,dseg))
                    s.append(f'<rect x="{x1:.1f}" y="{y-5}" width="{max(x2-x1,2):.1f}" height="10" rx="2" fill="{c}" fill-opacity="0.9"/>'); done=True
                    if xdef>x2+2: s.append(f'<line x1="{x2:.1f}" y1="{y}" x2="{xdef:.1f}" y2="{y}" stroke="#D6493F" stroke-width="3" stroke-opacity="0.4" stroke-dasharray="2 2"/>')
                else:
                    x1=X(cs); x2=X(adddays(cs,dseg))
                    s.append(f'<rect x="{x1:.1f}" y="{y-5}" width="{max(x2-x1,2):.1f}" height="10" rx="2" fill="{c}" fill-opacity="0.55"/>'); rem-=it["incut"]*dseg
            if it["rdate"]:
                if end>X1-96: s.append(f'<text x="{end-4:.1f}" y="{y+3}" font-size="9" text-anchor="end" fill="#FFFFFF">out {it["rdate"].strftime("%d %b %y")} · {sub}</text>')
                else: s.append(f'<text x="{end+5:.1f}" y="{y+3}" font-size="9" fill="{ULAB[u]}">out {it["rdate"].strftime("%d %b %y")} · {sub}</text>')
            else:
                s.append(f'<text x="{X1-4:.1f}" y="{y+3}" font-size="9" text-anchor="end" fill="#FFFFFF">covered ≥2 cuts · {sub}</text>')
        elif it["mode"]=="X":
            end=X(it["rdate"]) if it["rdate"] else X1
            s.append(f'<rect x="{X0}" y="{y-5}" width="{min(end-X0,X1-X0):.1f}" height="10" rx="2" fill="{c}" fill-opacity="0.30"/>')
            if end>X1-96: s.append(f'<text x="{X1-4:.1f}" y="{y+3}" font-size="9" text-anchor="end" fill="#5F5E5A">~{it["rdate"].strftime("%d %b %y")} · {sub}</text>')
            else: s.append(f'<text x="{end+5:.1f}" y="{y+3}" font-size="9" fill="#7A766E">~{it["rdate"].strftime("%d %b %y")} · {sub}</text>')
        else:
            if it["rdate"]<=TODAY:
                s.append(f'<circle cx="{X0+5}" cy="{y}" r="5" fill="#D6493F"/>')
                s.append(f'<text x="{X0+14}" y="{y+3}" font-size="9.5" fill="#D6493F">at zero — buy now · {sub}</text>')
            elif it["rdate"]>HEND:
                s.append(f'<rect x="{X0}" y="{y-5}" width="{X1-X0:.1f}" height="10" rx="2" fill="{c}" fill-opacity="0.9"/>')
                s.append(f'<text x="{X1-4:.1f}" y="{y+3}" font-size="9" text-anchor="end" fill="#FFFFFF">covered &gt; horizon · {sub}</text>')
            else:
                xr=X(it["rdate"]); s.append(f'<rect x="{X0}" y="{y-5}" width="{xr-X0:.1f}" height="10" rx="2" fill="{c}" fill-opacity="0.9"/>')
                if xr>X1-96: s.append(f'<text x="{xr-4:.1f}" y="{y+3}" font-size="9" text-anchor="end" fill="#FFFFFF">{it["rdate"].strftime("%d %b %y")} · {sub}</text>')
                else: s.append(f'<text x="{xr+5:.1f}" y="{y+3}" font-size="9" fill="{ULAB[u]}">{it["rdate"].strftime("%d %b %y")} · {sub}</text>')
        y+=rowH
    y+=4
s.append(f'<text x="20" y="{h-14}" font-size="9.5" fill="#9A968F">Groups ordered daily → every-other-day → training. Seasonal = in-cut rate, depletes only in shaded cut columns. Source: os_runway.py</text>')
s.append('</svg>')
with open(OUT,"w",encoding="utf-8") as fh: fh.write("\n".join(s)); fh.flush(); os.fsync(fh.fileno())
print("wrote",len(items),"items · H",h,"· unsorted:",unsorted)
for gi in order:
    g=grp_items[gi]
    if not g: continue
    print(f"\n[{GROUPS[gi][0] if gi<len(GROUPS) else 'Other'}]")
    for it in sorted(g,key=sortkey):
        print(f"   {it['nm'][:22]:23} {str(it['rdate']) if it['rdate'] else 'covered':10} {it['freq']:9} {it['soh']:g}{it['du']}")
