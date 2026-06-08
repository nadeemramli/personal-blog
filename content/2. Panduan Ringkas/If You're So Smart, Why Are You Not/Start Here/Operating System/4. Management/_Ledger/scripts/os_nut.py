#!/usr/bin/env python3
"""Order Operating System — recompute engine.
Usage: python3 os_nut.py "<path to Operating System folder>"
Reads product + overhead notes, prints Monthly Nut (E/F/X), stock run-out + restock,
and the freedom buckets. Edit CONFIG for income / PED calendar / overhead classing.
Formulas: dose monthly = daily_dose*(dpw/7)*(cost/mass)*30.44*(weeks_per_year/52);
shelf-life = cost/shelf_life_months; PEDs = weekly*weeks_per_year*cost_per_mg/12."""
import os,re,glob,sys,yaml,math
OS=sys.argv[1] if len(sys.argv)>1 else "."
DPW={"ED":7.0,"EOD":3.5,"ITD":4.0,"OCC":4.0,"TD":6.0}

# ---------------- CONFIG (edit at each review) ----------------
INCOME={"net_salary":4569.92,"study_allowance":1200.0,"indexa":1200.0}  # study ends 2030
CASH_SAVINGS=0.0
EPF={"age":26,"balance":34500,"monthly_contrib":1152,"rate":0.06}
# PED rotating calendar: name -> (weekly mg, weeks/year). Bloodwork-provisional.
PED_CAL={"Testosterone Enanthate/Cypionate":(311,52),"Boldenone Undecanoate":(350,20),
 "Oxandrolone (Anavar)":(240,16),"MK-677":(140,16),"Trenbolone Acetate":(110,8),
 "Proviron":(175,8),"Levothyroxine (T4)":(350,16),"Cardarine (GW-501516)":(105,8)}
OVH_F={"Gym","Diagnostics","Grooming"}; OVH_E={"Living","Insurance"}  # else -> X
OVH_F_NAMES={"MacroFactor (app)"}  # software but foundational
# --------------------------------------------------------------

def fm(p):
    t=open(p,encoding="utf-8").read();m=re.match(r'^---\n(.*?)\n---',t,re.S)
    try: return yaml.safe_load(m.group(1)) or {}
    except: return {}
def n(v):
    try: return float(v)
    except: return None

prod={}
for f in glob.glob(os.path.join(OS,"Products","**","*.md"),recursive=True):
    d=fm(f)
    if d.get("type")=="product": prod[d.get("name")]=d
def cpmass(d): return n(d["cost_per_bottle"])/(n(d["package_size"])*n(d["base_dose"]))

# ---- product burn ----
stacks={}; ped_mo=0; lines=[]
for name,(wk,wks) in PED_CAL.items():
    if name not in prod: continue
    mo=wk*wks*cpmass(prod[name])/12; ped_mo+=mo; stacks["PEDs"]=stacks.get("PEDs",0)+mo
    lines.append((name,"PEDs",round(mo,2)))
for name,d in prod.items():
    s=d.get("stack","")
    if s in("PEDs","Peptides"): continue
    if d.get("status") in("paused","planned","retired"): continue
    if d.get("count_in_total",True) is False or d.get("active",False) is False: continue
    cb=n(d.get("cost_per_bottle")); shelf=n(d.get("shelf_life_months")); wpy=n(d.get("weeks_per_year")) or 52
    if shelf and cb: mo=cb/shelf
    else:
        pkg=n(d.get("package_size"));base=n(d.get("base_dose"));daily=n(d.get("daily_dose"))
        du=str(d.get("dose_unit")or"");su=str(d.get("size_unit")or"");dpw=DPW.get(str(d.get("dosing")or""))
        if None in(cb,pkg,base,daily) or dpw is None or base==0: continue
        mass=pkg if(su==du and su) else pkg*base
        mo=daily*(dpw/7)*(cb/mass)*30.44*(wpy/52.0)
    stacks[s]=stacks.get(s,0)+mo; lines.append((name,s,round(mo,2)))
prod_total=sum(stacks.values())

# ---- overheads E/F/X ----
E=F=X=0; F+=0
for f in glob.glob(os.path.join(OS,"Overheads","*.md")):
    d=fm(f); 
    if d.get("type")!="overhead": continue
    eff=n(d.get("eff_monthly")) or 0; cat=d.get("category",""); nm=d.get("name","")
    if cat in OVH_E: E+=eff
    elif cat in OVH_F or nm in OVH_F_NAMES: F+=eff
    else: X+=eff
F+=prod_total
NUT=E+F+X; EF=E+F

print("="*60); print("MONTHLY NUT"); print("="*60)
for s,m in sorted(stacks.items(),key=lambda x:-x[1]): print(f"  {s:26} RM{m:8.2f}")
print(f"  {'PRODUCT TOTAL':26} RM{prod_total:8.2f}")
print(f"\n  E (Essential)  RM{E:8.2f}\n  F (Foundational) RM{F:8.2f}\n  X (Executional) RM{X:8.2f}")
print(f"  >> E+F FLOOR = RM{EF:.2f}   MONTHLY NUT = RM{NUT:.2f}")

# ---- stock / restock ----
print("\n"+"="*60); print("STOCK — run-out soonest (dose items w/ stock)"); print("="*60)
soon=[]
for name,d in prod.items():
    if d.get("status")!="active" or not d.get("active") or d.get("count_in_total",True) is False: continue
    st=n(d.get("stock_on_hand")); daily=n(d.get("daily_dose")); dpw=DPW.get(str(d.get("dosing")or""))
    if st is None or daily is None or dpw is None: continue
    eff=daily*dpw/7
    if eff<=0: continue
    soon.append((name,round(st/eff)))
for name,days in sorted(soon,key=lambda x:x[1])[:12]:
    flag="BUY NOW" if days<35 else ("buy this month" if days<60 else "ok")
    print(f"  {name[:34]:34} ~{days:>4}d  {flag}")

# ---- freedom ----
inc=sum(INCOME.values()); surplus=inc-NUT
emerg6=EF*6; free24=EF*24*1.06; opt=10000; full=emerg6+opt+free24
print("\n"+"="*60); print("FREEDOM NUMBERS"); print("="*60)
print(f"  6-mo emergency = RM{emerg6:,.0f}   24-mo freedom = RM{free24:,.0f}   optionality = RM{opt:,.0f}")
print(f"  Full target (B1+B2+B3) = RM{full:,.0f}")
print(f"  Take-home RM{inc:,.0f} - nut RM{NUT:,.0f} = surplus RM{surplus:,.0f}/mo")
if surplus>0:
    months=(full-CASH_SAVINGS)/surplus
    print(f"  Months to full freedom (from cash RM{CASH_SAVINGS:,.0f}) = {months:.1f} (~{months/12:.1f} yr)")
# EPF
g=(1+EPF["rate"])**(60-EPF["age"]); ann=(g-1)/EPF["rate"]
fv=EPF["balance"]*g+EPF["monthly_contrib"]*12*ann
print(f"  EPF trajectory by 60 ~ RM{fv:,.0f}  (Enhanced tier RM1.3M: {'ON TRACK' if fv>=1.3e6 else 'below'})")
