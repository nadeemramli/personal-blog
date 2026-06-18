# -*- coding: utf-8 -*-
"""Generate the 'Signal and Noise' poster — Cognitive Enhancement Part 1.1.
Locked 'Neural Signal Schematic' style, landscape live signal-tuning bench."""
import math, random

INK   = "#0B0F14"
INK2  = "#11161D"
CYAN  = "#2DD4BF"
CYAN_D= "#1C8C80"
AMBER = "#E8A23D"
AMBER_D="#8A6526"
RED   = "#FF5C5C"
WHITE = "#E6E8EE"
GREY  = "#4A525C"
GREY_L= "#6B7480"
HAIR  = "#1E2730"

MONO = "'JetBrains Mono','SF Mono',ui-monospace,'DejaVu Sans Mono',Consolas,monospace"
SANS = "'Inter','Segoe UI',system-ui,'DejaVu Sans',Arial,sans-serif"

W, H = 1500, 1200
out = []
def add(s): out.append(s)

add('<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" font-family="%s">' % (W,H,MONO))
add('<defs>')
add('<pattern id="clip" width="11" height="11" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
    '<rect width="11" height="11" fill="none"/>'
    '<line x1="0" y1="0" x2="0" y2="11" stroke="%s" stroke-width="1.4" opacity="0.55"/></pattern>' % AMBER)
add('<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">'
    '<circle cx="1" cy="1" r="1" fill="%s"/></pattern>' % HAIR)
add('<filter id="glow" x="-40%" y="-40%" width="180%" height="180%">'
    '<feGaussianBlur stdDeviation="3.2" result="b"/>'
    '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
add('</defs>')

add('<rect width="%d" height="%d" fill="%s"/>' % (W,H,INK))
add('<rect width="%d" height="%d" fill="url(#grid)" opacity="0.5"/>' % (W,H))
add('<rect x="20" y="20" width="%d" height="%d" fill="none" stroke="%s" stroke-width="1.5"/>' % (W-40,H-40,HAIR))
for (cx,cy) in [(20,20),(W-20,20),(20,H-20),(W-20,H-20)]:
    add('<path d="M%d,%d h24 M%d,%d v24" stroke="%s" stroke-width="1" opacity="0.6"/>' % (cx-12,cy,cx,cy-12,GREY))

def text(x,y,s,size=12,fill=WHITE,anchor="start",weight="600",ff=MONO,ls="0.5",op=1.0):
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s" font-weight="%s" '
            'font-family="%s" letter-spacing="%s" opacity="%s">%s</text>' %
            (x,y,size,fill,anchor,weight,ff,ls,op,s))

# HEADER
add(text(48,70,"COGNITIVE ENHANCEMENT &#183; PART 1.1",14,CYAN,ls="3"))
add(text(48,104,"SIGNAL AND NOISE",30,WHITE,ff=SANS,weight="700",ls="1"))
add(text(48,130,"&#8212; you're turning the wrong knob.",15,AMBER,ls="1"))
add('<rect x="980" y="44" width="478" height="58" rx="6" fill="none" stroke="%s" stroke-width="1.4"/>' % CYAN_D)
add(text(1219,70,"PERFORMANCE = SIGNAL &#247; NOISE",17,CYAN,anchor="middle",ls="1"))
add(text(1219,92,"NOT SIGNAL ALONE",12.5,GREY_L,anchor="middle",ls="3"))
add('<line x1="48" y1="150" x2="1452" y2="150" stroke="%s" stroke-width="1.5"/>' % HAIR)
add(text(1452,144,"NEURAL SIGNAL SCHEMATIC &#183; LIVE BENCH",10.5,GREY,anchor="end",ls="2"))

add(text(48,178,"SIGNAL CHAIN  &#8594;  trace the path",11,GREY_L,ls="2"))

# 1. GAS KNOB
gx,gy=150,320
add(text(48,210,"[ INPUT STAGE ]",11,AMBER,ls="2"))
add(text(150,234,"STIMULATION / AROUSAL",13.5,WHITE,anchor="middle",ls="1"))
add(text(150,252,"dopamine &#183; norepinephrine &#183; caffeine",10,GREY_L,anchor="middle",ls="0.5"))
R=78
def polar(cx,cy,r,deg):
    a=math.radians(deg); return cx+r*math.cos(a), cy-r*math.sin(a)
ax0,ay0=polar(gx,gy,R,200); ax1,ay1=polar(gx,gy,R,-20)
add('<path d="M%.1f,%.1f A%d,%d 0 1 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2"/>' % (ax0,ay0,R,R,ax1,ay1,GREY))
for deg,col in [(200,GREY_L),(90,CYAN),(-20,AMBER)]:
    tx,ty=polar(gx,gy,R,deg); ix,iy=polar(gx,gy,R-12,deg)
    add('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.4"/>' % (ix,iy,tx,ty,col))
add(text(gx-86,gy+8,"TOO",9.5,GREY_L,anchor="middle"))
add(text(gx-86,gy+20,"LITTLE",9.5,GREY_L,anchor="middle"))
add(text(gx,gy-R-12,"PEAK",10,CYAN,anchor="middle",ls="1"))
add(text(gx+88,gy+8,"TOO",9.5,AMBER,anchor="middle"))
add(text(gx+88,gy+20,"MUCH",9.5,AMBER,anchor="middle"))
add('<circle cx="%d" cy="%d" r="46" fill="%s" stroke="%s" stroke-width="2.5"/>' % (gx,gy,INK2,CYAN))
add('<circle cx="%d" cy="%d" r="46" fill="none" stroke="%s" stroke-width="6" opacity="0.18"/>' % (gx,gy,CYAN))
pdeg=55; pxe,pye=polar(gx,gy,40,pdeg)
add('<line x1="%d" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3.5" filter="url(#glow)"/>' % (gx,gy,pxe,pye,CYAN))
add('<circle cx="%d" cy="%d" r="6" fill="%s"/>' % (gx,gy,CYAN))
cdx,cdy=polar(gx,gy,R,pdeg)
add('<circle cx="%.1f" cy="%.1f" r="5.5" fill="%s" filter="url(#glow)"/>' % (cdx,cdy,CYAN))
add('<rect x="44" y="392" width="212" height="40" rx="5" fill="%s" stroke="%s" stroke-width="1.2"/>' % (INK2,AMBER_D))
add(text(150,410,"&#9650; this knob raises",10.5,AMBER,anchor="middle"))
add(text(150,425,"SIGNAL and NOISE",11,AMBER,anchor="middle",ls="1",weight="700"))
add('<path d="M250,320 h46" stroke="%s" stroke-width="2"/>' % CYAN_D)
add('<path d="M292,314 l10,6 l-10,6" fill="none" stroke="%s" stroke-width="2"/>' % CYAN_D)

# 2. HERO CURVE
bx0,bx1=320,760; btop,bbase=230,700
add(text(bx0,206,"[ TRANSFER CURVE &#183; the operating curve has a WRONG SIDE ]",11,CYAN,ls="1"))
add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5"/>' % (bx0,bbase,bx1+6,bbase,GREY))
add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5"/>' % (bx0,btop-6,bx0,bbase,GREY))
add(text(bx0-6,btop+6,"OUTPUT",9.5,GREY_L,anchor="end",ls="1"))
add(text(bx1+4,bbase+16,"AROUSAL &#8594;",9.5,GREY_L,anchor="end",ls="1"))
peak_x,peak_y=500,268
main=('M%d,%d C390,%d 440,330 %d,%d C560,330 600,470 %d,%d' %
      (bx0,bbase-30,bbase-40,peak_x,peak_y,bx1,bbase-10))
add('<path d="M%d,%d C400,%d 470,360 540,300 C600,355 640,490 %d,%d" fill="none" stroke="%s" stroke-width="1.6" opacity="0.55" stroke-dasharray="2 5"/>' % (bx0,bbase-15,bbase-30,bx1,bbase+5,GREY))
add('<path d="M%d,%d C380,%d 410,300 460,250 C520,300 560,450 %d,%d" fill="none" stroke="%s" stroke-width="1.6" opacity="0.45" stroke-dasharray="2 5"/>' % (bx0,bbase-45,bbase-55,bx1-30,bbase-25,GREY))
clipx=600
add('<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="url(#clip)" opacity="0.5"/>' % (clipx,btop-10,bx1+6,btop-10,bx1+6,bbase,clipx,bbase))
add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.3" stroke-dasharray="4 4" opacity="0.7"/>' % (clipx,btop-10,clipx,bbase,AMBER))
add(text(685,btop+18,"CLIP /",12,AMBER,anchor="middle",ls="1",weight="700"))
add(text(685,btop+34,"DISTORTION",12,AMBER,anchor="middle",ls="1",weight="700"))
add('<path d="%s" fill="none" stroke="%s" stroke-width="3.4" filter="url(#glow)"/>' % (main,CYAN))
add('<path d="M%d,%d C560,330 600,470 %d,%d" fill="none" stroke="%s" stroke-width="3.4" opacity="0.85"/>' % (peak_x,peak_y,bx1,bbase-10,AMBER))
add(text(360,560,"every input",10,CYAN))
add(text(360,574,"here is a GAIN",10,CYAN,weight="700"))
add('<circle cx="%d" cy="%d" r="9" fill="%s" stroke="%s" stroke-width="2.5" stroke-dasharray="3 3"/>' % (peak_x,peak_y,INK,CYAN))
add('<circle cx="%d" cy="%d" r="4" fill="%s" filter="url(#glow)"/>' % (peak_x,peak_y,CYAN))
add(text(peak_x,peak_y-20,"OPTIMAL AROUSAL",11,CYAN,anchor="middle",ls="1",weight="700"))
add(text(peak_x,peak_y-34,"&#8226; movable: shifts by task &amp; person &#8226;",8.5,GREY_L,anchor="middle"))
gcx,gcy=560,312
add('<circle cx="%d" cy="%d" r="6.5" fill="%s" filter="url(#glow)"/>' % (gcx,gcy,CYAN))
add('<path d="M%d,%d l30,18" stroke="%s" stroke-width="1.4" stroke-dasharray="2 3"/>' % (gcx,gcy,CYAN))
add(text(640,500,"feels like needing more",10.5,AMBER,anchor="middle",weight="700"))
add(text(640,514,"&#8212; is the trap snapping shut",9.5,AMBER,anchor="middle"))
# ONE RED OBJECT
rkx,rky=700,628
add('<circle cx="%d" cy="%d" r="22" fill="%s" stroke="%s" stroke-width="2.2"/>' % (rkx,rky,INK2,RED))
add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.6"/>' % (rkx,rky,rkx+15,rky-12,RED))
add('<path d="M%d,%d A26,26 0 0 1 %d,%d" fill="none" stroke="%s" stroke-width="2.2"/>' % (rkx+24,rky-14,rkx+30,rky+8,RED))
add('<path d="M%d,%d l-7,-2 l3,7" fill="%s"/>' % (rkx+30,rky+8,RED))
add('<path d="M%d,%d q-4,-16 8,-18 q2,-10 9,-7 q3,-8 9,-4 q4,-6 9,-1 l3,18 q2,12 -10,16 z" fill="none" stroke="%s" stroke-width="1.8" opacity="0.9"/>' % (rkx-30,rky+26,RED))
add('<circle cx="%d" cy="%d" r="8" fill="%s" filter="url(#glow)"/>' % (rkx+58,rky-2,RED))
add(text(rkx+72,rky-6,"WIRED &amp; STUCK",11,RED,weight="700"))
add(text(rkx+72,rky+9,"adding gas here makes it worse",9.5,RED))
add('<path d="M770,360 h30" stroke="%s" stroke-width="2"/>' % CYAN_D)
add('<path d="M796,354 l10,6 l-10,6" fill="none" stroke="%s" stroke-width="2"/>' % CYAN_D)

# 3. SCOPE A/B
sx0=820; scope_w=300
add(text(sx0,206,"[ OUTPUT SCOPE &#183; same task, two settings ]",11,CYAN,ls="1"))
def scope(x,y,h,label,sub,signal_col,noise_amp,sig_amp,clipped,verdict,vcol,vsub,seed):
    add('<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="%s" stroke="%s" stroke-width="1.4"/>' % (x,y,scope_w,h,INK2,GREY))
    midy=y+h/2
    for gyl in range(1,4):
        yy=y+h*gyl/4
        add('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>' % (x,yy,x+scope_w,yy,HAIR))
    for gxl in range(1,6):
        xx=x+scope_w*gxl/6
        add('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1"/>' % (xx,y,xx,y+h,HAIR))
    add(text(x+10,y+20,label,12,signal_col,weight="700",ls="1"))
    add(text(x+scope_w-10,y+20,sub,9,GREY_L,anchor="end"))
    nf_top=midy-noise_amp; nf_bot=midy+noise_amp
    if noise_amp>4:
        add('<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="%s" opacity="0.12"/>' % (x+8,nf_top,scope_w-16,nf_bot-nf_top,AMBER))
        random.seed(seed); pts=[]; n=80
        for i in range(n+1):
            xx=x+8+(scope_w-16)*i/n; yy=midy+random.uniform(-1,1)*noise_amp
            pts.append("%.1f,%.1f"%(xx,yy))
        add('<polyline points="%s" fill="none" stroke="%s" stroke-width="1" opacity="0.55"/>' % (" ".join(pts),AMBER))
        add(text(x+12,nf_bot+13,"NOISE FLOOR",8.5,AMBER,ls="1"))
    else:
        add('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1" stroke-dasharray="3 4" opacity="0.6"/>' % (x+8,midy,x+scope_w-8,midy,CYAN_D))
        add(text(x+12,midy+15,"noise floor &#8595; gated",8.5,CYAN_D,ls="0.5"))
    pts=[]; n=160
    for i in range(n+1):
        xx=x+10+(scope_w-20)*i/n; v=math.sin(i/n*math.pi*4); yy=midy-v*sig_amp
        if clipped:
            lim=sig_amp*0.62; yy=midy-max(-lim,min(lim,v*sig_amp))
        pts.append("%.1f,%.1f"%(xx,yy))
    add('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4" filter="url(#glow)"/>' % (" ".join(pts),signal_col))
    add('<rect x="%d" y="%d" width="%d" height="26" rx="4" fill="none" stroke="%s" stroke-width="1.4"/>' % (x+8,y+h-34,scope_w-16,vcol))
    add(text(x+scope_w/2,y+h-21,verdict,11.5,vcol,anchor="middle",weight="700",ls="1"))
    add(text(x+scope_w/2,y+h-9,vsub,8,GREY_L,anchor="middle"))
scope(sx0,232,200,"A &#183; GAS ONLY","drive maxed, no brake",AMBER,34,62,True,"RIGID &#183; TUNNEL VISION",AMBER,"locked hard, can't ask if it's right",51)
scope(sx0,472,200,"B &#183; GAS + BRAKE","drive balanced with calm",CYAN,3,58,False,"FLEXIBLE &#183; AIMABLE",CYAN,"hold the task AND step back from it",7)
rmx=sx0+scope_w+16
add('<rect x="%d" y="300" width="56" height="300" rx="5" fill="%s" stroke="%s" stroke-width="1.3"/>' % (rmx,INK2,GREY))
add(text(rmx+28,290,"S/N",10,GREY_L,anchor="middle",ls="1"))
add('<rect x="%d" y="540" width="36" height="48" fill="%s" opacity="0.8"/>' % (rmx+10,AMBER))
add(text(rmx+28,600,"&#8776;1:1",9,AMBER,anchor="middle"))
add('<rect x="%d" y="320" width="36" height="120" fill="%s" opacity="0.9" filter="url(#glow)"/>' % (rmx+10,CYAN))
add(text(rmx+28,314,"HIGH",8.5,CYAN,anchor="middle"))
add('<path d="M%d,535 L%d,445" stroke="%s" stroke-width="2" stroke-dasharray="3 3"/>' % (rmx+28,rmx+28,CYAN))
add('<path d="M%d,452 l6,-10 l6,10" fill="%s"/>' % (rmx+22,CYAN))

# 4. BRAKE KNOB
bkx,bky=1290,360
add(text(1186,206,"[ THE CONTROL THAT PRODUCES B ]",11,CYAN,ls="1"))
add(text(bkx,234,"CALM / INHIBITION",13.5,CYAN,anchor="middle",ls="1"))
add(text(bkx,252,"GABA &#183; serotonin",10,GREY_L,anchor="middle"))
add(text(bkx,268,"&#8212; the lever you skipped &#8212;",9.5,AMBER,anchor="middle"))
add('<circle cx="%d" cy="%d" r="38" fill="%s" stroke="%s" stroke-width="2.5"/>' % (bkx,bky,INK2,CYAN))
add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (bkx-26,bky+2,bkx+26,bky+2,CYAN))
add('<path d="M%d,%d l0,12 M%d,%d l5,5 l5,-5" stroke="%s" stroke-width="2" fill="none"/>' % (bkx-10,bky-16,bkx-15,bky-9,CYAN))
add('<path d="M%d,%d l0,12 M%d,%d l5,5 l5,-5" stroke="%s" stroke-width="2" fill="none"/>' % (bkx+10,bky-16,bkx+5,bky-9,CYAN))
add(text(bkx,bky+24,"gate &#8595;",8.5,CYAN,anchor="middle"))
add('<rect x="1196" y="416" width="188" height="30" rx="5" fill="%s" stroke="%s" stroke-width="1.2"/>' % (INK2,CYAN_D))
add(text(bkx,435,"CALM &#8595; lowers NOISE only",10.5,CYAN,anchor="middle"))
add('<rect x="1196" y="456" width="188" height="34" rx="5" fill="none" stroke="%s" stroke-width="1.1"/>' % AMBER_D)
add(text(bkx,471,"prevents emotional capture",9.5,AMBER,anchor="middle"))
add(text(bkx,484,"(rides through the spike)",8,GREY_L,anchor="middle"))
add('<rect x="1196" y="496" width="188" height="34" rx="5" fill="none" stroke="%s" stroke-width="1.1"/>' % AMBER_D)
add(text(bkx,511,"releases hyper-fixation",9.5,AMBER,anchor="middle"))
add(text(bkx,524,"(frees headroom to pivot)",8,GREY_L,anchor="middle"))
add('<rect x="1196" y="542" width="188" height="50" rx="6" fill="%s" stroke="%s" stroke-width="1.6"/>' % (INK2,CYAN))
add(text(bkx,562,"the brake doesn't kill drive.",10,WHITE,anchor="middle"))
add(text(bkx,580,"it AIMS it.",13,CYAN,anchor="middle",weight="700",ls="1"))

# Flexibility plate
add('<rect x="320" y="724" width="600" height="40" rx="6" fill="none" stroke="%s" stroke-width="1.4"/>' % CYAN_D)
add(text(620,742,"FLEXIBILITY IS NOT A KIND OF STIMULATION.",12.5,WHITE,anchor="middle",ls="0.5"))
add(text(620,757,"IT'S THE ABSENCE OF NOISE.",12.5,CYAN,anchor="middle",weight="700",ls="1"))

# FOOT DEVICES
add('<line x1="48" y1="788" x2="1452" y2="788" stroke="%s" stroke-width="1.5"/>' % HAIR)
add(text(48,812,"WORKED DEVICES &#8212; what to actually do",11,GREY_L,ls="2"))
def card(x,y,w,h,title):
    add('<rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="%s" stroke="%s" stroke-width="1.4"/>' % (x,y,w,h,INK2,GREY))
    add(text(x+16,y+26,title,12,CYAN,weight="700",ls="1"))
cy0=828; ch=252
# TEACUP
tx=48; tw=430
card(tx,cy0,tw,ch,"THE TEACUP")
add(text(tx+16,cy0+44,"the whole principle in one afternoon",9.5,GREY_L))
cux,cuy=tx+80,cy0+150
add('<path d="M%d,%d h88 v44 a44,34 0 0 1 -88,0 z" fill="none" stroke="%s" stroke-width="2"/>' % (cux-44,cuy-40,WHITE))
add('<path d="M%d,%d a22,20 0 0 1 0,40" fill="none" stroke="%s" stroke-width="2"/>' % (cux+44,cuy-30,WHITE))
add('<path d="M%d,%d q6,-8 0,-16 M%d,%d q6,-8 0,-16" fill="none" stroke="%s" stroke-width="1.4"/>' % (cux-14,cuy-52,cux+12,cuy-52,GREY_L))
add(text(cux,cuy+40,"caffeine + L-theanine",11,CYAN,anchor="middle",weight="700"))
add(text(cux,cuy+56,"&#8776; 2:1",14,CYAN,anchor="middle",weight="700",ls="2"))
add(text(tx+250,cy0+86,"a little GAS",10,CYAN))
add(text(tx+250,cy0+104,"+ a little BRAKE",10,CYAN))
add('<path d="M%d,%d h150" stroke="%s" stroke-width="1" stroke-dasharray="3 3"/>' % (tx+248,cy0+120,GREY))
mwx,mwy=tx+250,cy0+160; ptsm=[]
for i in range(61):
    xx=mwx+150*i/60; yy=mwy-18*math.sin(i/60*math.pi*4); ptsm.append("%.1f,%.1f"%(xx,yy))
add('<polyline points="%s" fill="none" stroke="%s" stroke-width="2" filter="url(#glow)"/>' % (" ".join(ptsm),CYAN))
add(text(tx+250,cy0+200,"&#8594; waveform B (clean)",10,CYAN))
add(text(tx+250,cy0+222,"the inverted-U you can",9,GREY_L))
add(text(tx+250,cy0+234,"feel in one afternoon.",9,GREY_L))
# FADER BANK
fx=500; fw=470
card(fx,cy0,fw,ch,"LOW-DOSE SYNERGY")
add(text(fx+16,cy0+44,"modest amounts of several &#62; a max dose of one",9.5,GREY_L))
sweet_y=cy0+118; track_top=cy0+78; track_bot=cy0+200
add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.7"/>' % (fx+30,sweet_y,fx+300,sweet_y,CYAN))
add(text(fx+24,sweet_y+4,"sweet",8,CYAN,anchor="end"))
random.seed(7)
for fxx in [fx+60,fx+105,fx+150,fx+195,fx+240]:
    add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (fxx,track_top,fxx,track_bot,GREY))
    capy=sweet_y+random.uniform(-8,8)
    add('<rect x="%d" y="%.1f" width="18" height="10" rx="2" fill="%s"/>' % (fxx-9,capy-5,CYAN))
add(text(fx+150,track_bot+18,"several rails near peak",9,CYAN,anchor="middle"))
lfx=fx+360
add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (lfx,track_top,lfx,track_bot,GREY))
add('<rect x="%d" y="%d" width="18" height="10" rx="2" fill="%s"/>' % (lfx-9,track_top-2,GREY_L))
add(text(lfx,track_top-8,"MAX",8.5,AMBER,anchor="middle",weight="700"))
clx,cly=lfx-40,track_bot+30; ptsc=[]
for i in range(41):
    xx=clx+80*i/40; v=math.sin(i/40*math.pi*4); lim=0.55; yy=cly-14*max(-lim,min(lim,v)); ptsc.append("%.1f,%.1f"%(xx,yy))
add('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (" ".join(ptsc),AMBER))
add(text(lfx,cly+24,"over the cliff",8.5,AMBER,anchor="middle"))
add(text(lfx,cly+36,"&#8212; clips",8.5,AMBER,anchor="middle"))
add('<rect x="%d" y="%d" width="220" height="28" rx="5" fill="none" stroke="%s" stroke-width="1.4"/>' % (fx+16,cy0+212,CYAN))
add(text(fx+126,cy0+230,"NEVER MAX A SINGLE LEVER",10.5,CYAN,anchor="middle",weight="700"))
# DUTY-CYCLE
dx=992; dw=460
card(dx,cy0,dw,ch,"DAILY DUTY-CYCLE")
add(text(dx+16,cy0+44,"gain up to produce / squelch up to recover",9.5,GREY_L))
rail_y=cy0+92; rx0=dx+30; rx1=dx+dw-30
add('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (rx0,rail_y,rx1,rail_y,GREY))
for hh,lab in [(0,"6a"),(0.33,"12p"),(0.66,"6p"),(1,"12a")]:
    xx=rx0+(rx1-rx0)*hh
    add('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.4"/>' % (xx,rail_y-4,xx,rail_y+4,GREY_L))
    add(text(xx,rail_y+18,lab,8.5,GREY_L,anchor="middle"))
gex=[]
for i in range(61):
    t=i/60; xx=rx0+(rx1-rx0)*t; env=math.exp(-((t-0.28)**2)/0.045); yy=rail_y-40-env*34; gex.append("%.1f,%.1f"%(xx,yy))
add('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.2" filter="url(#glow)"/>' % (" ".join(gex),CYAN))
add(text(rx0+90,cy0+70,"GAIN &#8593; produce",9.5,CYAN,anchor="middle"))
sqx=[]
for i in range(61):
    t=i/60; xx=rx0+(rx1-rx0)*t; env=math.exp(-((t-0.82)**2)/0.05); yy=rail_y+40+env*30; sqx.append("%.1f,%.1f"%(xx,yy))
add('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.2"/>' % (" ".join(sqx),AMBER))
add(text(rx1-90,cy0+205,"SQUELCH &#8593; recover &amp; sleep",9.5,AMBER,anchor="middle"))
add('<rect x="%d" y="%d" width="%d" height="26" rx="5" fill="none" stroke="%s" stroke-width="1.1"/>' % (dx+16,cy0+216,dw-32,AMBER_D))
add(text(dx+dw/2,cy0+233,"stuck flat-out all day = burnout &#183; the peak slides lower each block",9.5,AMBER,anchor="middle"))

# FOOT BANNER
add('<rect x="48" y="1100" width="1404" height="60" rx="8" fill="%s" stroke="%s" stroke-width="2"/>' % (INK2,CYAN))
add(text(750,1130,"WIRED BUT STUCK?  ADD BRAKE, NOT GAS.",24,CYAN,anchor="middle",ff=SANS,weight="700",ls="1.5"))
add(text(750,1150,"the knob you keep turning is the wrong one",11,GREY_L,anchor="middle",ls="1"))

add('</svg>')
svg="\n".join(out)
import io
p="/sessions/laughing-friendly-davinci/mnt/blog viz daily - temporary/_poster_out.svg"
with open(p,"w",encoding="utf-8") as f: f.write(svg)
print("SVG bytes:",len(svg))
