import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
from openpyxl.formatting.rule import CellIsRule, FormulaRule
OUT=sys.argv[1]
G,P,EFF,SP,CF,PK=1.15,1.10,0.25,0.8,0.76,1.6
F_="Arial"
BLUE=Font(name=F_,color="0000FF"); BLACK=Font(name=F_); GREEN=Font(name=F_,color="008000")
BOLD=Font(name=F_,bold=True); TITLE=Font(name=F_,bold=True,size=14); HDR=Font(name=F_,bold=True,color="FFFFFF")
HFILL=PatternFill("solid",fgColor="4B3B7A"); YEL=PatternFill("solid",fgColor="FFFF00"); SEC=PatternFill("solid",fgColor="E8E2F4")
OKF=PatternFill("solid",fgColor="C6EFCE"); BADF=PatternFill("solid",fgColor="FFC7CE")
thin=Side(style="thin",color="BBBBBB")
def hdr(ws,row,labels,col=1):
    for i,l in enumerate(labels):
        c=ws.cell(row=row,column=col+i,value=l); c.font=HDR; c.fill=HFILL; c.alignment=Alignment(wrap_text=True,vertical="center")
def put(ws,ref,val,font=BLACK,fmt=None,fill=None,note=None):
    c=ws[ref]; c.value=val; c.font=font
    if fmt: c.number_format=fmt
    if fill: c.fill=fill
    if note: c.comment=Comment(note,"Design docs")
    return c
def widths(ws,w):
    for k,v in w.items(): ws.column_dimensions[k].width=v

# ---------- data ----------
realms=[("Meridian Opening","MO","T1",15,0.6,0,0,0),("Qi Condensation","QC","T1",50,1,0.02,0,0),("Qi Sea","QS","T1",250,2,0.06,0,0),
("Foundation Establishment","FE","T2",12000,5,0.2,0,0),("Golden Core","GC","T3",4e5,25,1,0.5,2),("Nascent Soul","NS","T4",None,125,5,1,3),
("Soul Formation","SF","T5",None,625,21,2,4),("Void Breaking","VB","T6",None,3125,40,4,5),("Mahayana","MA","T7",None,15625,65,8,6),("Great Ascension","GA","T8–T9",None,78125,110,16,7)]
ext_in=[(1,1,1,0,1),(1.1,1.05,1,0,1),(1.1,1.06,1,0.003,1),(1.25,1.17,1.2,0.01,1.1),(1.4,1.31,1.35,0.02,1.1),(1.65,1.40,1.5,0.04,1.1),
(2.05,1.57,1.7,0.1,1.1),(2.3,1.70,2.0,0.2,1.1),(2.85,1.85,2.3,0.33,1.1),(3.6,2.0,2.6,0.6,1.1)]
doc_ext=[1,1,1,1.5,2.5,4,None,None,None,None]
EXT=[a*b*c*(1+3*d)*e for a,b,c,d,e in ext_in]
def realm_h(rate_mult,ext,base,step_rate):
    t=0;prev=None
    for L in range(1,10):
        rate=step_rate*P**(L-1)*ext
        cap=CF*base*G**(L-1) if L<9 else PK*CF*base*G**7
        if L==1: sm=cap/G; ref=sm
        else: sm=prev; ref=SP*prev
        t+=ref/rate+(cap-sm)/(EFF*rate); prev=cap
    return t/3600
# tune SF..GA to target reach days (meditation 4.8 h/day)
mh=12*0.4; cum=0
bases=[r[3] for r in realms]
for i in range(5): cum+=realm_h(0,EXT[i],bases[i],realms[i][4])
targets_next={5:21,6:40,7:65,8:110,9:180}
for i in range(5,10):
    need=targets_next[i]*mh-cum; b=need/realm_h(0,EXT[i],1.0,realms[i][4]); b=float(f"{b:.2g}"); bases[i]=b
    cum+=realm_h(0,EXT[i],b,realms[i][4])
# body
stages=[("Copper Skin",400,1,0.4,0,0),("Iron Bone",12500,1.5,2.5,0.5,1),("Silver Marrow",3e5,2.5,11,1,2),("Jade Flesh",4.7e6,4,30,2,3),
("Golden Body",None,6,72,4,4),("Diamond Vajra Body",None,9,155,8,5),("Immortal Body",None,13,250,16,6)]
bbase=[s[1] for s in stages]; th=12*0.3; cum=0
for i in range(4): cum+=realm_h(0,stages[i][2],bbase[i],4**i)
for i in range(4,7):
    need=stages[i][3]*th-cum; b=need/realm_h(0,stages[i][2],1.0,4**i); b=float(f"{b:.2g}"); bbase[i]=b; cum+=realm_h(0,stages[i][2],b,4**i)

wb=Workbook()
# ---------- Guide ----------
ws=wb.active; ws.title="Guide"
lines=[("Idle Cultivation: Balancing Model",TITLE),("",None),
("What this is",BOLD),("A working model of the progression math from 03-Economy.md, 02-Systems.md (Vessel Model) and content/*.md. Change the inputs and every sheet recalculates.",BLACK),("",None),
("Color legend",BOLD),("Blue text = input you can change · Black = formula · Green = pulled from another sheet · Yellow fill = key assumption",BLACK),("",None),
("Sheets",BOLD),
("Inputs: global constants, realm table (BASE, REALM_RATE, targets, rebirth gains, Karma), body-stage table.",BLACK),
("EXT_Budget: builds each realm's Qi multiplier (EXT) from grounds × Talisman × method × achievements × element match, and compares it with the old doc assumption.",BLACK),
("Qi_Pacing: level-by-level Vessel Model for all 10 Mortal realms (refill + growth time), cumulative meditation hours and calendar days.",BLACK),
("Body_Pacing: the same for the 7 body stages, using Train time.",BLACK),
("Rebirth: stacked Qi/Body gains, Karma, and a 6-life planner (edit the blue 'reached' cells) with Dao Marks if you ascend.",BLACK),
("Grounds_Economy: Spirit Stone income per tier vs Cultivation Ground upkeep, with recommended upkeep.",BLACK),
("Checks: model vs target days, suggested BASE values to hit targets, EXT sanity, upkeep, and Karma milestones.",BLACK),("",None),
("How to tune",BOLD),
("1. Look at Checks. Any 'Retune' row has a 'Suggested BASE' that would hit its target.",BLACK),
("2. Copy the suggestion into Inputs (blue cell), and the sheet recalculates. Later realms shift too, so tune top to bottom.",BLACK),
("3. If a realm feels too fast because of multipliers, adjust EXT_Budget inputs (for example, achievement share) instead of BASE.",BLACK),("",None),
("Model simplifications",BOLD),
("· Times are pure Meditate (Qi) or Train (Body) time, converted to calendar days with the activity split on Inputs. Battle drain and pills aren't modelled.",BLACK),
("· Breakthrough materials, success rolls, and tribulations add time on top (expect +20–40%).",BLACK),
("· Rebirth life lengths are approximated as first-life hours ÷ the Qi multiplier for that life.",BLACK),
("· SF–GA BASE values and Golden Body+ BODY_BASE values were tuned by this model to hit the registry targets; they are new numbers, not from the docs.",BLACK)]
for i,(t,f) in enumerate(lines,1):
    c=ws.cell(row=i,column=1,value=t)
    if f: c.font=f
    c.alignment=Alignment(wrap_text=True)
widths(ws,{"A":120})

# ---------- Inputs ----------
wi=wb.create_sheet("Inputs")
put(wi,"A1","Inputs",TITLE)
put(wi,"A3","Global constants",BOLD,fill=SEC); put(wi,"B3","Value",BOLD,fill=SEC); put(wi,"C3","Note / source",BOLD,fill=SEC)
glob=[("Cost growth per level (G)",1.15,"0.00","03-Economy: work × 1.15 per level"),
("Rate growth per level (P)",1.10,"0.00","03-Economy: rate × 1.10 per level"),
("Expansion efficiency",0.25,"0%","Vessel Model: 4 points → +1 max while full"),
("Level spend (% of cap)",0.8,"0%","Breakthrough spends 80% of cap (gates 100%)"),
("Cap factor (cap = factor × work)",0.76,"0.00","03-Economy cap(R,L) = 0.76 × work"),
("Peak cap multiplier (level 9)",1.6,"0.0","cap(R,9) = 1.6 × cap(R,8)"),
("Effective hours per day",12,"0","Online + offline within the 8 h cap, 3–6 check-ins"),
("Meditate share",0.4,"0%","Activity split assumption (03-Economy)"),
("Train share",0.3,"0%","Activity split assumption"),
("Battle share","=1-B11-B12","0%","Remainder"),
("Base regen (% of full rate)",0.1,"0%","Always on; refills only, never grows max"),
("Offline combat efficiency",0.8,"0%","Decision #8"),
("Body stage rate step",4,"0","Tempering rate × 4 per body stage"),
("Achievement Qi bonus at 100%",3.0,"0%","Decision #62: +300% total"),
("Stone income growth per tier (T5+)",7,"0","03-Economy: ×7 per tier from SF"),
("Target upkeep share of income",0.12,"0%","15-Cultivation-Grounds: about 10–15%")]
for i,(l,v,fmt,n) in enumerate(glob):
    r=4+i; put(wi,f"A{r}",l); c=put(wi,f"B{r}",v,BLUE if not str(v).startswith("=") else BLACK,fmt); put(wi,f"C{r}",n)
for r in (10,11,12): wi[f"B{r}"].fill=YEL
# realm table
put(wi,"A21","Mortal Plane realms",BOLD,fill=SEC)
hdr(wi,22,["Idx","Realm","Abbrev","Tier","BASE (L1 work)","REALM_RATE","Target reach day","REALM_GAIN","Qi Karma add","EXT override (blank = use EXT_Budget)"])
for i,(name,ab,tier,base,rr,tday,gain,karma) in enumerate(realms):
    r=23+i
    put(wi,f"A{r}",i+1); put(wi,f"B{r}",name); put(wi,f"C{r}",ab); put(wi,f"D{r}",tier)
    note=None if realms[i][3] is not None else "Tuned by this model to hit the target days (new value, not in the docs yet)."
    put(wi,f"E{r}",bases[i],BLUE,"#,##0" if bases[i]<1e7 else "0.00E+00",YEL if note else None,note)
    put(wi,f"F{r}",rr,BLUE,"#,##0.0"); put(wi,f"G{r}",tday,BLUE,"0.00"); put(wi,f"H{r}",gain,BLUE,"0.0"); put(wi,f"I{r}",karma,BLUE,"0")
    put(wi,f"J{r}",None,BLUE,"0.00")
put(wi,"B33","Ascension (GA complete)"); put(wi,"C33","ASC"); put(wi,"G33",180,BLUE,"0")
put(wi,"A34","Target days: content/00-Registry.md (first life, 40/30/30 split). REALM_GAIN and Karma: 03-Economy / content/12-Rebirth.")
# body table
put(wi,"A36","Body stages",BOLD,fill=SEC)
hdr(wi,37,["Idx","Stage","BODY_BASE (L1 work)","EXT_body","Target completion day","STAGE_GAIN","Body Karma add"])
for i,(name,bb,ex,tday,gain,k) in enumerate(stages):
    r=38+i; note=None if stages[i][1] is not None else "Tuned by this model to hit the target day (new value)."
    put(wi,f"A{r}",i+1); put(wi,f"B{r}",name)
    put(wi,f"C{r}",bbase[i],BLUE,"#,##0" if bbase[i]<1e7 else "0.00E+00",YEL if note else None,note)
    put(wi,f"D{r}",ex,BLUE,"0.0"); put(wi,f"E{r}",tday,BLUE,"0"); put(wi,f"F{r}",gain,BLUE,"0.0"); put(wi,f"G{r}",k,BLUE,"0")
put(wi,"A45","Targets: content/02-Body.md. EXT_body = baths, Ring, Training Ground, mastery (assumed).")
widths(wi,{"A":34,"B":26,"C":16,"D":10,"E":16,"F":12,"G":16,"H":12,"I":12,"J":22})
wi.freeze_panes="A4"

# ---------- EXT_Budget ----------
we=wb.create_sheet("EXT_Budget")
put(we,"A1","EXT budget: what actually multiplies Qi rate in each realm",TITLE)
hdr(we,3,["Realm","Best Meditation ground ×","Typical Talisman Qi ×","Cultivation method ×","Achievements earned (share of total)","Element match ×","Achievement ×","Computed EXT","Old doc EXT","Computed ÷ doc","EXT used in pacing"])
for i,(a,b,c,d,e) in enumerate(ext_in):
    r=4+i
    put(we,f"A{r}",f"=Inputs!C{23+i}",GREEN)
    put(we,f"B{r}",a,BLUE,"0.00"); put(we,f"C{r}",b,BLUE,"0.00"); put(we,f"D{r}",c,BLUE,"0.00"); put(we,f"E{r}",d,BLUE,"0.0%"); put(we,f"F{r}",e,BLUE,"0.00")
    put(we,f"G{r}",f"=1+E{r}*Inputs!$B$17",fmt="0.00")
    put(we,f"H{r}",f"=B{r}*C{r}*D{r}*G{r}*F{r}",fmt="0.00")
    put(we,f"I{r}",doc_ext[i],BLUE,"0.00")
    put(we,f"J{r}",f'=IF(I{r}="","",H{r}/I{r})',fmt="0.00")
    put(we,f"K{r}",f'=IF(Inputs!J{23+i}="",H{r},Inputs!J{23+i})',fmt="0.00")
put(we,"A15","Sources: grounds from content/15-Cultivation-Grounds (best site usable mid-realm); Talisman = typical rarity for the realm from 02-Systems §4 accessory ranges; method = 06-Techniques progression (assumed); achievements = assumed share of the +300% total earned by that realm; element match +10% from FE.")
we["A15"].alignment=Alignment(wrap_text=True); we.merge_cells("A15:K16"); we.row_dimensions[15].height=30
widths(we,{"A":10,"B":14,"C":14,"D":14,"E":16,"F":12,"G":13,"H":13,"I":11,"J":12,"K":14}); we.freeze_panes="B4"

# ---------- pacing sheet builder ----------
def pacing(name,title,count,labelref,baseref,raterow_formula,extref,share_cell,keyfmt):
    ws=wb.create_sheet(name); put(ws,"A1",title,TITLE)
    hdr(ws,3,["Key","Idx","Level","Rate /s","Work","Cap (max at level end)","Start max","Refill amount","Refill h","Growth h","Level h","Cumulative h","Day (end of level)","Day (level reached)"])
    r=4
    for idx in range(1,count+1):
        for L in range(1,10):
            put(ws,f"A{r}",keyfmt(idx,L),GREEN)
            put(ws,f"B{r}",idx); put(ws,f"C{r}",L)
            put(ws,f"D{r}",raterow_formula(idx,r),fmt="#,##0.00")
            put(ws,f"E{r}",f"=INDEX({baseref},B{r})*Inputs!$B$4^(C{r}-1)",fmt="0.00E+00")
            put(ws,f"F{r}",f"=IF(C{r}<9,Inputs!$B$8*E{r},Inputs!$B$9*Inputs!$B$8*INDEX({baseref},B{r})*Inputs!$B$4^7)",fmt="0.00E+00")
            put(ws,f"G{r}",f"=IF(C{r}=1,F{r}/Inputs!$B$4,F{r-1})" if r>4 else f"=F{r}/Inputs!$B$4",fmt="0.00E+00")
            put(ws,f"H{r}",f"=IF(C{r}=1,G{r},Inputs!$B$7*F{r-1})" if r>4 else f"=G{r}",fmt="0.00E+00")
            put(ws,f"I{r}",f"=H{r}/D{r}/3600",fmt="0.000")
            put(ws,f"J{r}",f"=(F{r}-G{r})/(Inputs!$B$6*D{r})/3600",fmt="0.000")
            put(ws,f"K{r}",f"=I{r}+J{r}",fmt="0.000")
            put(ws,f"L{r}",f"=L{r-1}+K{r}" if r>4 else f"=K{r}",fmt="#,##0.00")
            put(ws,f"M{r}",f"=L{r}/(Inputs!$B$10*{share_cell})",fmt="0.0")
            put(ws,f"N{r}",f"=(L{r}-K{r})/(Inputs!$B$10*{share_cell})",fmt="0.00")
            r+=1
    widths(ws,{"A":22,"B":6,"C":7,"D":14,"E":12,"F":14,"G":12,"H":13,"I":10,"J":10,"K":10,"L":13,"M":12,"N":13}); ws.freeze_panes="D4"
    return r-1
qlast=pacing("Qi_Pacing","Qi pacing (Vessel Model, Meditate time)",10,None,"Inputs!$E$23:$E$32",
    lambda idx,r: f"=INDEX(Inputs!$F$23:$F$32,B{r})*Inputs!$B$5^(C{r}-1)*INDEX(EXT_Budget!$K$4:$K$13,B{r})",None,"Inputs!$B$11",
    lambda idx,L: f'=Inputs!$C${22+idx}&" {L}"')
blast=pacing("Body_Pacing","Body pacing (Vessel Model, Train time)",7,None,"Inputs!$C$38:$C$44",
    lambda idx,r: f"=Inputs!$B$16^(B{r}-1)*Inputs!$B$5^(C{r}-1)*INDEX(Inputs!$D$38:$D$44,B{r})",None,"Inputs!$B$12",
    lambda idx,L: f'=Inputs!$B${37+idx}&" {L}"')

# ---------- Rebirth ----------
wr=wb.create_sheet("Rebirth"); put(wr,"A1","Rebirth: stacked gains, Karma, life planner",TITLE)
put(wr,"A3","Qi realm gains (stacked)",BOLD,fill=SEC)
hdr(wr,4,["Realm","REALM_GAIN","Cumulative before","Gain at level 1","Gain at peak","Qi Karma (stacked)"])
for i in range(10):
    r=5+i
    put(wr,f"A{r}",f"=Inputs!C{23+i}",GREEN); put(wr,f"B{r}",f"=Inputs!H{23+i}",GREEN,"0.00")
    put(wr,f"C{r}",f"=C{r-1}+B{r-1}" if i else 0,fmt="0.00")
    put(wr,f"D{r}",f"=IF(B{r}=0,0,C{r}+B{r}*(0.5+0.5*1/9))",fmt="0.00"); put(wr,f"E{r}",f"=C{r}+B{r}",fmt="0.00")
    put(wr,f"F{r}",f"=F{r-1}+Inputs!I{23+i}" if i else f"=Inputs!I23",fmt="0")
put(wr,"A17","Body stage gains (stacked)",BOLD,fill=SEC)
hdr(wr,18,["Stage","STAGE_GAIN","Cumulative before","Gain at layer 1","Gain at peak","Body Karma (stacked)"])
for i in range(7):
    r=19+i
    put(wr,f"A{r}",f"=Inputs!B{38+i}",GREEN); put(wr,f"B{r}",f"=Inputs!F{38+i}",GREEN,"0.00")
    put(wr,f"C{r}",f"=C{r-1}+B{r-1}" if i else 0,fmt="0.00")
    put(wr,f"D{r}",f"=IF(B{r}=0,0,C{r}+B{r}*(0.5+0.5*1/9))",fmt="0.00"); put(wr,f"E{r}",f"=C{r}+B{r}",fmt="0.00")
    put(wr,f"F{r}",f"=F{r-1}+Inputs!G{38+i}" if i else f"=Inputs!G38",fmt="0")
put(wr,"A28","Life planner (edit the blue cells: where each life rebirths)",BOLD,fill=SEC)
hdr(wr,29,["Life","Qi realm reached","Level","Body stage reached","Layer","Qi × during life","Body × during life","Meditation h to reach (life 1 basis)","Life length (days)","Cumulative day","Qi gain","Body gain","Qi Karma","Body Karma","Karma this rebirth","Karma total","Qi × after","Body × after","Dao Marks if ascending now"])
plan=[("GC",9,"Silver Marrow",3),("NS",9,"Jade Flesh",1),("NS",9,"Jade Flesh",5),("SF",5,"Jade Flesh",9),("VB",5,"Golden Body",3),("MA",5,"Golden Body",9)]
for i,(rq,lq,st,ly) in enumerate(plan):
    r=30+i
    put(wr,f"A{r}",i+1); put(wr,f"B{r}",rq,BLUE); put(wr,f"C{r}",lq,BLUE); put(wr,f"D{r}",st,BLUE); put(wr,f"E{r}",ly,BLUE)
    put(wr,f"F{r}",f"=F{r-1}+K{r-1}" if i else 1,fmt="0.00"); put(wr,f"G{r}",f"=G{r-1}+L{r-1}" if i else 1,fmt="0.00")
    put(wr,f"H{r}",f'=INDEX(Qi_Pacing!$L$4:$L${qlast},MATCH(B{r}&" "&C{r},Qi_Pacing!$A$4:$A${qlast},0))',fmt="#,##0.0")
    put(wr,f"I{r}",f"=H{r}/F{r}/(Inputs!$B$10*Inputs!$B$11)",fmt="0.0")
    put(wr,f"J{r}",f"=J{r-1}+I{r}" if i else f"=I{r}",fmt="0.0")
    put(wr,f"K{r}",f"=INDEX($C$5:$C$14,MATCH(B{r},$A$5:$A$14,0))+INDEX($B$5:$B$14,MATCH(B{r},$A$5:$A$14,0))*(0.5+0.5*C{r}/9)",fmt="0.00")
    put(wr,f"L{r}",f"=INDEX($C$19:$C$25,MATCH(D{r},$A$19:$A$25,0))+INDEX($B$19:$B$25,MATCH(D{r},$A$19:$A$25,0))*(0.5+0.5*E{r}/9)",fmt="0.00")
    put(wr,f"M{r}",f"=INDEX($F$5:$F$14,MATCH(B{r},$A$5:$A$14,0))",fmt="0")
    put(wr,f"N{r}",f"=INDEX($F$19:$F$25,MATCH(D{r},$A$19:$A$25,0))",fmt="0")
    put(wr,f"O{r}",f"=M{r}+N{r}",fmt="0"); put(wr,f"P{r}",f"=P{r-1}+O{r}" if i else f"=O{r}",fmt="0")
    put(wr,f"Q{r}",f"=F{r}+K{r}",fmt="0.00"); put(wr,f"R{r}",f"=G{r}+L{r}",fmt="0.00")
    put(wr,f"S{r}",f"=FLOOR(10*SQRT(Q{r}*R{r}),1)",fmt="0")
put(wr,"A37","Life length = first-life meditation hours to reach that point ÷ the Qi multiplier during the life (approximation; body and gates not included).")
widths(wr,{"A":14,"B":14,"C":12,"D":18,"E":12,"F":12,"G":12,"H":16,"I":12,"J":12,"K":10,"L":10,"M":10,"N":10,"O":12,"P":12,"Q":10,"R":10,"S":14})
wr.freeze_panes="A5"

# ---------- Grounds_Economy ----------
wg=wb.create_sheet("Grounds_Economy"); put(wg,"A1","Spirit Stone income vs Cultivation Ground upkeep",TITLE)
hdr(wg,3,["Tier","Realms","Stones per hour (income)"])
tiers=[("T1","MO–QS",200),("T2","FE",2000),("T3","GC",15000),("T4","NS",100000),("T5","SF",None),("T6","VB",None),("T7","MA",None),("T8","GA 1–4",None),("T9","GA 5–9",None)]
for i,(t,rl,v) in enumerate(tiers):
    r=4+i; put(wg,f"A{r}",i+1,fmt='"T"0'); put(wg,f"B{r}",rl)
    put(wg,f"C{r}",v if v is not None else f"=C{r-1}*Inputs!$B$18",BLUE if v is not None else BLACK,"#,##0")
put(wg,"A13","T1–T4 income from 03-Economy (Spirit Stone Flow); T5+ extrapolated ×7 per tier.")
grounds=[("—","Humble Hut","Meditation",1.0,"MO 1",1,0),("—","Village Courtyard","Training",1.0,"QC 1",1,0)]
raw="""1|Bamboo Grove Hermitage|Meditation|1.10|MO 5|1|0
2|Pass Fort Drill Yard|Training|1.10|QC 7|1|0
3|Moonlit Lake Pavilion|Meditation|1.20|FE 1|2|0
4|Ember Hot Springs|Training|1.25|FE 4|2|0
5|Ruined Meditation Hall|Meditation|1.30|FE 8|2|0
6|Thunderstruck Summit|Training|1.35|GC 2|3|0
7|Venom-Steeped Pools|Training|1.45|GC 5|3|0
8|Glacial Cave of Stillness|Meditation|1.50|GC 8|3|0
9|Sunscorch Dunes|Training|1.60|NS 1|4|0
10|Yin Spirit Altar|Meditation|1.65|NS 4|4|0
11|Tidal Reef Platform|Training|1.75|NS 7|4|0
12|Cloud Sea Peak|Meditation|1.90|SF 1|5|70000
13|Volcano Crater Forge|Training|1.95|SF 4|5|84000
14|Primal Spirit Spring|Meditation|2.05|SF 7|5|98000
15|Void Rift Edge|Training|2.20|VB 1|6|500000
16|Starlight Observatory|Meditation|2.30|VB 4|6|590000
17|Demon-Slaying Wall|Training|2.45|VB 7|6|690000
18|Sword Intent Cliff|Meditation|2.60|MA 1|7|3500000
19|World Tree Roots|Training|2.70|MA 4|7|4100000
20|Dragon's Breath Chasm|Meditation|2.85|MA 7|7|4800000
21|Celestial Palace Courtyard|Training|3.00|GA 1|8|25000000
22|Phoenix Flame Altar|Meditation|3.20|GA 2|8|29000000
23|Tribulation Lightning Field|Training|3.35|GA 4|8|34000000
24|Nine Heavens Terrace|Meditation|3.60|GA 5|9|170000000
25|Chaos Crucible|Training|3.80|GA 6|9|200000000
26|Summit of Heaven|Both|4.50|GA 8|9|250000000"""
for line in raw.split("\n"):
    a=line.split("|"); grounds.append((a[0],a[1],a[2],float(a[3]),a[4],int(a[5]),int(a[6])))
hdr(wg,15,["Map #","Ground","Kind","Multiplier","Min realm","Tier","Upkeep/h (docs)","Income/h at tier","Upkeep share","Recommended upkeep/h","Check"])
for i,(m,n,k,mu,mr,t,up) in enumerate(grounds):
    r=16+i
    put(wg,f"A{r}",m); put(wg,f"B{r}",n); put(wg,f"C{r}",k); put(wg,f"D{r}",mu,BLUE,"0.00"); put(wg,f"E{r}",mr); put(wg,f"F{r}",t,BLUE,'"T"0')
    put(wg,f"G{r}",up,BLUE,"#,##0"); put(wg,f"H{r}",f"=INDEX($C$4:$C$12,F{r})",fmt="#,##0")
    put(wg,f"I{r}",f"=IFERROR(G{r}/H{r},0)",fmt="0.00%")
    put(wg,f"J{r}",f"=IF(G{r}>0,ROUND(H{r}*Inputs!$B$19,-2),0)",fmt="#,##0")
    put(wg,f"K{r}",f'=IF(G{r}=0,"—",IF(AND(I{r}>=0.1,I{r}<=0.15),"OK","Retune"))')
glast=16+len(grounds)-1
put(wg,f"A{glast+2}","Upkeep (docs) is from content/15-Cultivation-Grounds, set to 10% / 12% / 14–15% of tier income for the 1st/2nd/3rd ground of each tier. Tier is mapped from the ground's minimum realm.")
widths(wg,{"A":8,"B":28,"C":12,"D":11,"E":11,"F":7,"G":15,"H":16,"I":12,"J":18,"K":9}); wg.freeze_panes="C16"

# ---------- Checks ----------
wc=wb.create_sheet("Checks"); put(wc,"A1","Checks",TITLE)
put(wc,"A3","1. Qi realm pacing vs registry targets (first life)",BOLD,fill=SEC)
hdr(wc,4,["Realm","Target reach day","Model reach day","Model ÷ target − 1","Status","Target realm length (days)","Model realm length (days)","Suggested BASE to hit target"])
for i in range(10):
    r=5+i
    put(wc,f"A{r}",f"=Inputs!C{23+i}",GREEN)
    put(wc,f"B{r}",f"=Inputs!G{23+i}",GREEN,"0.00")
    put(wc,f"C{r}",f'=INDEX(Qi_Pacing!$N$4:$N${qlast},MATCH(A{r}&" 1",Qi_Pacing!$A$4:$A${qlast},0))',fmt="0.00")
    put(wc,f"D{r}",f'=IF(B{r}<0.5,"",C{r}/B{r}-1)',fmt="0%")
    put(wc,f"E{r}",f'=IF(B{r}<0.5,"(tutorial)",IF(ABS(D{r})<=0.2,"OK","Retune"))')
    put(wc,f"F{r}",f"=B{r+1}-B{r}",fmt="0.00")
    put(wc,f"G{r}",f"=C{r+1}-C{r}",fmt="0.00")
    put(wc,f"H{r}",f'=IF(G{r}<=0,"",Inputs!E{23+i}*F{r}/G{r})',fmt="0.00E+00")
put(wc,"A15","=Inputs!C33",GREEN); put(wc,"B15","=Inputs!G33",GREEN,"0")
put(wc,"C15",f'=INDEX(Qi_Pacing!$M$4:$M${qlast},MATCH("GA 9",Qi_Pacing!$A$4:$A${qlast},0))',fmt="0.00")
put(wc,"D15","=C15/B15-1",fmt="0%"); put(wc,"E15",'=IF(ABS(D15)<=0.2,"OK","Retune")')
put(wc,"A16","Suggested BASE scales a realm's length to its target (realm time is proportional to BASE). Apply top-down: changing one realm shifts every later reach day.")
put(wc,"A18","2. Body stage pacing vs targets (content/02-Body)",BOLD,fill=SEC)
hdr(wc,19,["Stage","Target completion day","Model completion day","Model ÷ target − 1","Status","Suggested BODY_BASE"])
for i in range(7):
    r=20+i
    put(wc,f"A{r}",f"=Inputs!B{38+i}",GREEN); put(wc,f"B{r}",f"=Inputs!E{38+i}",GREEN,"0")
    put(wc,f"C{r}",f'=INDEX(Body_Pacing!$M$4:$M${blast},MATCH(A{r}&" 9",Body_Pacing!$A$4:$A${blast},0))',fmt="0.0")
    put(wc,f"D{r}",f"=C{r}/B{r}-1",fmt="0%"); put(wc,f"E{r}",f'=IF(ABS(D{r})<=0.2,"OK","Retune")')
    prevB="0" if i==0 else f"B{r-1}"; prevC="0" if i==0 else f"C{r-1}"
    put(wc,f"F{r}",f"=IFERROR(Inputs!C{38+i}*(B{r}-{prevB})/(C{r}-{prevC}),\"\")",fmt="0.00E+00")
put(wc,"A28","3. EXT sanity (computed multipliers vs old doc assumption, MO–NS)",BOLD,fill=SEC)
hdr(wc,29,["Realm","Old doc EXT","Computed EXT","Ratio","Status"])
for i in range(6):
    r=30+i
    put(wc,f"A{r}",f"=EXT_Budget!A{4+i}",GREEN); put(wc,f"B{r}",f"=EXT_Budget!I{4+i}",GREEN,"0.00"); put(wc,f"C{r}",f"=EXT_Budget!H{4+i}",GREEN,"0.00")
    put(wc,f"D{r}",f"=C{r}/B{r}",fmt="0.00"); put(wc,f"E{r}",f'=IF(AND(D{r}>=0.8,D{r}<=1.25),"OK","Check")')
put(wc,"A37","4. Other checks",BOLD,fill=SEC)
hdr(wc,38,["Check","Value","Target","Status"])
other=[("Meditation hours to reach FE",f'=INDEX(Qi_Pacing!$L$4:$L${qlast},MATCH("QS 9",Qi_Pacing!$A$4:$A${qlast},0))',"≤ 1.0 h",'=IF(B39<=1,"OK","Retune")',"0.00"),
("Grounds with upkeep outside 10–15% of income",f'=COUNTIF(Grounds_Economy!$K$16:$K${glast},"Retune")',"0",'=IF(B40=0,"OK","Retune")',"0"),
("Karma total after life 2 (Rebirth planner)","=Rebirth!P31","≥ 10",'=IF(B41>=10,"OK","Check")',"0"),
("Dao Marks if ascending after life 6","=Rebirth!S35","info","info","0"),
("Achievement Qi × at full completion","=1+Inputs!B17","info (decision #62)","info","0.00")]
for i,(l,f,t,s,fmt) in enumerate(other):
    r=39+i; put(wc,f"A{r}",l); put(wc,f"B{r}",f,fmt=fmt); put(wc,f"C{r}",t); put(wc,f"D{r}",s)
widths(wc,{"A":44,"B":16,"C":16,"D":16,"E":12,"F":18,"G":18,"H":22})
# conditional formatting on status cells
for ws_,rng in [(wc,"E5:E15"),(wc,"E20:E26"),(wc,"E30:E35"),(wc,"D39:D43"),(wg,f"K16:K{glast}")]:
    ws_.conditional_formatting.add(rng,FormulaRule(formula=[f'ISNUMBER(SEARCH("OK",{rng.split(":")[0]}))'],fill=OKF))
    ws_.conditional_formatting.add(rng,FormulaRule(formula=[f'OR(ISNUMBER(SEARCH("Retune",{rng.split(":")[0]})),ISNUMBER(SEARCH("Check",{rng.split(":")[0]})))'],fill=BADF))
# fonts default Arial for untouched cells
for s in wb.worksheets:
    for row in s.iter_rows():
        for c in row:
            if c.value is not None and (c.font is None or c.font.name!="Arial"):
                c.font=Font(name="Arial",bold=c.font.bold if c.font else False,color=c.font.color if c.font else None)
wb.calculation.fullCalcOnLoad=True
wb.save(OUT); print("saved",OUT)
