#!/usr/bin/env python3
"""Order OS — Financial report generator.
Regenerates the monthly cash-flow Sankey + PED stock-runway SVGs into _Ledger/charts/,
and (re)writes _Ledger/Financial Snapshot.md embedding them. Obsidian-safe (hardcoded
palette + background, no CSS vars). Usage: python3 os_reports.py "<path to OS folder>"."""
import os,re,glob,sys,yaml
from datetime import date,timedelta
OS=sys.argv[1] if len(sys.argv)>1 else "."
TODAY=date.today()
# ---------------- CONFIG (sync with os_nut.py at each review) ----------------
def _load_inputs():
    import os as _o,re as _r,yaml as _y
    p=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),"..","FOS 0 — Financial Inputs.md")
    try:
        t=open(p,encoding="utf-8").read()
        return _y.safe_load(_r.match(r"^---\n(.*?)\n---",t,_r.S).group(1)) or {}
    except Exception:
        return {}
_IN=_load_inputs()
INCOME=[("2X net salary",_IN.get("income_2x_net",4569.92),"blue"),("ACCA allowance",_IN.get("income_study_allowance",1200.0),"green"),("INDEXA (net)",_IN.get("income_indexa_net",1200.0),"amber")]
SAVING_RATE=_IN.get("saving_rate_monthly",2090.98)
CC_BALANCE=_IN.get("cc_balance",10653.04)
DPW={"ED":7.0,"EOD":3.5,"ITD":4.0,"OCC":4.0,"TD":6.0,"5x":5.0,"1-2x":1.5}
PED_CAL={"Etho Testosterone 450":(350,52),"Boldenone Undecanoate":(350,20),"Oxandrolone (Anavar)":(240,16),
 "MK-677":(140,24),"Trenbolone Acetate":(70,8),"Proviron":(175,8),"Levothyroxine (T4)":(700,16),
 "Cytolin (Cytomel / T3)":(175,16),"Cardarine (GW-501516)":(105,8)}
# palette (works on light & dark Obsidian — SVG carries its own light card bg)
BG="#FCFCFB";INK="#2F2D2A";MUTE="#6B6862";GRID="#E6E4E0";WHITE="#FFFFFF"
C={"blue":"#3E7BC2","green":"#3DA56B","amber":"#D69A3A","red":"#D6493F","grey":"#9A968F"}
# ----------------------------------------------------------------------------
def fm(p):
    t=open(p,encoding="utf-8").read();m=re.match(r'^---\n(.*?)\n---',t,re.S)
    try:return yaml.safe_load(m.group(1)) or {}
    except:return {}
def num(v):
    try:return float(v)
    except:return None

# ---- read overheads (Living vs other) ----
living=0.0; overhead=0.0
for f in glob.glob(os.path.join(OS,"2. Catalog","Overheads","*.md")):
    d=fm(f)
    if d.get("type")!="overhead":continue
    eff=num(d.get("eff_monthly")) or 0
    if d.get("category")=="Living": living+=eff
    else: overhead+=eff
# ---- read products: foundation burn + PED runway ----
prod={}
for f in glob.glob(os.path.join(OS,"2. Catalog","Products","**","*.md"),recursive=True):
    d=fm(f)
    if d.get("type")=="product": prod[d.get("name")]=d
def cpmass(d):
    cb=num(d.get("cost_per_bottle"));pkg=num(d.get("package_size"));base=num(d.get("base_dose"))
    return cb/(pkg*base) if (cb and pkg and base) else None
foundation=0.0
for name,(wk,wks) in PED_CAL.items():
    d=prod.get(name); cm=cpmass(d) if d else None
    if cm: foundation+=wk*wks*cm/12
for name,d in prod.items():
    s=d.get("stack","")
    if s in("PEDs","Peptides"):continue
    if s=="" or d.get("status") in("paused","planned","retired"):continue
    if d.get("count_in_total",True) is False or d.get("active",False) is False:continue
    cb=num(d.get("cost_per_bottle"));shelf=num(d.get("shelf_life_months"));wpy=num(d.get("weeks_per_year")) or 52
    if shelf and cb: foundation+=cb/shelf;continue
    pkg=num(d.get("package_size"));base=num(d.get("base_dose"));daily=num(d.get("daily_dose"))
    du=str(d.get("dose_unit")or"");su=str(d.get("size_unit")or"");dpw=DPW.get(str(d.get("dosing")or""))
    if None in(cb,pkg,base,daily) or dpw is None or base==0:continue
    mass=pkg if(su==du and su) else pkg*base
    foundation+=daily*(dpw/7)*(cb/mass)*30.44*(wpy/52.0)

total_inc=sum(v for _,v,_ in INCOME)
cc=SAVING_RATE; buffer=total_inc-living-overhead-foundation-cc
ALLOC=[("Living + Ayra",living,"grey"),("Overheads",overhead,"grey"),
       ("Foundation (protocol)",foundation,"blue"),("CC payoff (redirect)",cc,"red"),
       ("Buffer (can speed CC)",buffer,"green")]

# ================= SANKEY =================
def sankey():
    top=66;H=360;sc=H/total_inc;xS=150;wS=15;xH=372;wH=20;xD=600;wD=15;gap=9
    def rib(x0,y0,x1,y1,h,col):
        xm=(x0+x1)/2
        return (f'<path d="M{x0:.1f},{y0:.1f} C{xm:.1f},{y0:.1f} {xm:.1f},{y1:.1f} {x1:.1f},{y1:.1f} '
                f'L{x1:.1f},{y1+h:.1f} C{xm:.1f},{y1+h:.1f} {xm:.1f},{y0+h:.1f} {x0:.1f},{y0+h:.1f} Z" fill="{col}" fill-opacity="0.20"/>')
    s=[f'<svg viewBox="0 0 760 500" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">',
       f'<rect x="0" y="0" width="760" height="500" rx="10" fill="{BG}"/>',
       f'<text x="20" y="34" font-size="18" font-weight="600" fill="{INK}">Monthly cash flow — CC-payoff phase</text>',
       f'<text x="20" y="54" font-size="13" fill="{MUTE}">Take-home RM{total_inc:,.0f} -&gt; maintenance burn + redirect surplus to kill the credit card · {TODAY}</text>']
    ys=top;hub=top
    for nm,v,k in INCOME:
        h=v*sc;col=C[k]
        s.append(f'<rect x="{xS}" y="{ys:.1f}" width="{wS}" height="{h:.1f}" rx="2" fill="{col}"/>')
        s.append(f'<text x="{xS-6}" y="{ys+h/2:.1f}" font-size="12" text-anchor="end" fill="{INK}">{nm}</text>')
        s.append(f'<text x="{xS-6}" y="{ys+h/2+15:.1f}" font-size="11" text-anchor="end" fill="{MUTE}">RM{v:,.0f}</text>')
        s.append(rib(xS+wS,ys,xH,hub,h,col));ys+=h+gap;hub+=h
    s.append(f'<rect x="{xH}" y="{top}" width="{wH}" height="{H:.1f}" rx="2" fill="{INK}"/>')
    s.append(f'<text x="{xH+wH/2:.0f}" y="{top-8}" font-size="12" text-anchor="middle" fill="{INK}">Take-home RM{total_inc:,.0f}</text>')
    yd=top;hub=top
    for nm,v,k in ALLOC:
        h=v*sc;col=C[k]
        s.append(rib(xH+wH,hub,xD,yd,h,col))
        s.append(f'<rect x="{xD}" y="{yd:.1f}" width="{wD}" height="{h:.1f}" rx="2" fill="{col}"/>')
        s.append(f'<text x="{xD+wD+6}" y="{yd+h/2:.1f}" font-size="12" fill="{INK}">{nm}</text>')
        s.append(f'<text x="{xD+wD+6}" y="{yd+h/2+15:.1f}" font-size="11" fill="{MUTE}">RM{v:,.0f}</text>')
        yd+=h+gap;hub+=h
    s.append('</svg>');return "".join(s)

# ================= PED RUNWAY =================
def runway():
    items=[]
    for name,(wk,wks) in PED_CAL.items():
        d=prod.get(name)
        if not d:continue
        soh=num(d.get("stock_on_hand"));unit=d.get("dose_unit","")
        eff=wk*wks/364.0; due=(soh/eff) if (soh and eff) else (0 if (soh==0) else None)
        items.append((name,soh,unit,due))
    items.sort(key=lambda x:(x[3] is None,x[3] if x[3] is not None else 9e9))
    AXIS=560;x0=205;x1=748;W=x1-x0
    def X(dd):return x0+min(dd,AXIS)/AXIS*W
    top=86;rh=33;ccday=CC_BALANCE/ (SAVING_RATE/30.44)  # days to clear CC at saving rate
    def urg(dd):
        if dd is None or dd<=0 or dd<90:return C["red"]
        if dd<185:return C["amber"]
        if dd<=AXIS:return C["blue"]
        return C["green"]
    n=len(items);ybot=top+n*rh
    s=[f'<svg viewBox="0 0 770 {ybot+60} " xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">',
       f'<rect x="0" y="0" width="770" height="{ybot+60}" rx="10" fill="{BG}"/>',
       f'<text x="20" y="32" font-size="18" font-weight="600" fill="{INK}">PED stock runway — when each runs out</text>',
       f'<text x="20" y="52" font-size="13" fill="{MUTE}">Bars = current hold · red = at zero/buy now · CC-clear line shows the collision · {TODAY}</text>']
    months=[("Jul",20),("Sep",82),("Nov",143),("Jan27",204),("Mar",263),("May",324),("Jul",385),("Sep",447),("Nov",508)]
    for lab,dd in months:
        x=X(dd)
        s.append(f'<line x1="{x:.1f}" y1="{top-6}" x2="{x:.1f}" y2="{ybot:.1f}" stroke="{GRID}" stroke-width="1"/>')
        s.append(f'<text x="{x:.1f}" y="{top-12}" font-size="10" text-anchor="middle" fill="{MUTE}">{lab}</text>')
    xcc=X(ccday)
    s.append(f'<line x1="{xcc:.1f}" y1="{top-6}" x2="{xcc:.1f}" y2="{ybot+6:.1f}" stroke="{C["red"]}" stroke-width="1.3" stroke-dasharray="5 3"/>')
    s.append(f'<text x="{xcc:.1f}" y="{ybot+24:.1f}" font-size="11" text-anchor="middle" fill="{C["red"]}">CC cleared ~{(TODAY+timedelta(days=ccday)).strftime("%b")} (if all surplus -&gt; CC)</text>')
    y=top
    for name,soh,unit,due in items:
        col=urg(due)
        s.append(f'<text x="200" y="{y+rh/2+1:.1f}" font-size="12" text-anchor="end" fill="{INK}">{name[:24]}</text>')
        s.append(f'<text x="200" y="{y+rh/2+14:.1f}" font-size="10" text-anchor="end" fill="{MUTE}">{(("%.0f"%soh)+" "+unit) if soh is not None else "?"}</text>')
        if due is None or due<=0:
            s.append(f'<circle cx="{x0+5:.1f}" cy="{y+rh/2:.1f}" r="6" fill="{C["red"]}"/>')
            s.append(f'<text x="{x0+18:.1f}" y="{y+rh/2+4:.1f}" font-size="11" fill="{C["red"]}">at zero — buy for cut</text>')
        else:
            xe=X(due);covered=due>AXIS
            s.append(f'<rect x="{x0}" y="{y+6:.1f}" width="{xe-x0:.1f}" height="{rh-14}" rx="4" fill="{col}" fill-opacity="0.9"/>')
            if covered:
                s.append(f'<text x="{xe-6:.1f}" y="{y+rh/2+4:.1f}" font-size="10" text-anchor="end" fill="{WHITE}">covered &gt; horizon</text>')
            else:
                s.append(f'<text x="{xe+6:.1f}" y="{y+rh/2+4:.1f}" font-size="11" fill="{INK}">{(TODAY+timedelta(days=due)).strftime("%d %b %Y")}</text>')
        y+=rh
    s.append('</svg>');return "".join(s)

cdir=os.path.join(OS,"4. Management","_Ledger","charts")
os.makedirs(cdir,exist_ok=True)
open(os.path.join(cdir,"cashflow_sankey.svg"),"w",encoding="utf-8").write(sankey())
open(os.path.join(cdir,"ped_runway.svg"),"w",encoding="utf-8").write(runway())

nut=living+overhead+foundation; surplus=total_inc-nut
rep=f"""---
title: Financial Snapshot
draft: true
tags: [operating-system, ledger, financial-os, report]
date: {TODAY}
---
> [!abstract] Auto-generated by `_Ledger/scripts/os_reports.py` from live data. Re-run to refresh. See [[Financial Reports — Generation Policy]].

## Monthly cash flow
![[charts/cashflow_sankey.svg]]

| | RM |
|---|---:|
| Take-home income | {total_inc:,.2f} |
| − Living + Ayra | {living:,.2f} |
| − Overheads | {overhead:,.2f} |
| − Foundation (protocol) | {foundation:,.2f} |
| **= Maintenance nut** | **{nut:,.2f}** |
| Surplus (pre-allocation) | {surplus:,.2f} |
| Routed to CC payoff | {cc:,.2f} |
| Buffer (PED buys / speed CC) | {buffer:,.2f} |

CC RM{CC_BALANCE:,.0f} ÷ RM{SAVING_RATE:,.0f}/mo ≈ **{CC_BALANCE/SAVING_RATE:.1f} months** to clear.

## PED stock runway
![[charts/ped_runway.svg]]

## Links
- [[FOS 1 — Income Layer]] · [[FOS 2 — Min-Monthly Layer]] · [[FOS 3 — Debt & Credit Recovery]] · [[Foundation Funding Plan]] · [[Stock Cost Audit]]
"""
open(os.path.join(OS,"4. Management","_Ledger","Financial Snapshot.md"),"w",encoding="utf-8").write(rep)
print(f"OK  income={total_inc:.2f} nut={nut:.2f} surplus={surplus:.2f} foundation={foundation:.2f} buffer={buffer:.2f}")
print(f"CC clears in {CC_BALANCE/SAVING_RATE:.1f} months")
