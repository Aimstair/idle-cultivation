G,P,EFF,SP,CF,PK=1.15,1.10,0.25,0.8,0.76,1.6
realms=["MO","QC","QS","FE","GC","NS","SF","VB","MA","GA"]
BASE=[15,50,250,12000,4e5,9e6,None,None,None,None]
RR=[0.6,1,2,5,25,125,625,3125,15625,78125]
ground=[1,1.1,1.1,1.25,1.4,1.65,2.05,2.3,2.85,3.6]
tal=[1,1.05,1.06,1.17,1.31,1.40,1.57,1.70,1.85,2.0]
meth=[1,1,1,1.2,1.35,1.5,1.7,2.0,2.3,2.6]
achf=[0,0,0.003,0.01,0.02,0.04,0.1,0.2,0.33,0.6]
elem=[1,1,1,1.1,1.1,1.1,1.1,1.1,1.1,1.1]
EXT=[ground[i]*tal[i]*meth[i]*(1+3*achf[i])*elem[i] for i in range(10)]
def realm_hours(i,base):
    t=0;prev=None
    for L in range(1,10):
        rate=RR[i]*P**(L-1)*EXT[i]
        cap= CF*base*G**(L-1) if L<9 else PK*CF*base*G**7
        if L==1: sm=cap/G; refill=sm
        else: sm=prev; refill=SP*prev
        t+= refill/rate + (cap-sm)/(EFF*rate); prev=cap
    return t/3600
mh=4.8
cum=0
targets_reach={"QC":None,"FE":1/4.8*0+None if False else None}
for i,r in enumerate(realms):
    if BASE[i] is None: continue
    h=realm_hours(i,BASE[i]); cum+=h
    print(r, "EXT %.2f"%EXT[i], "realm h %.2f"%h, "cum h %.2f"%cum, "done day %.1f"%(cum/mh))
# tune SF..GA: target completion (reach next) days: SF->VB 40, VB->MA 65, MA->GA 110, GA->Asc 180
tgt={6:40,7:65,8:110,9:180}
for i in range(6,10):
    need=tgt[i]*mh-cum
    unit=realm_hours(i,1.0)
    b=need/unit; BASE[i]=b; cum+=need
    print(realms[i],"EXT %.2f"%EXT[i],"BASE %.3g"%b, "ratio to prev %.1f"%(b/BASE[i-1]))
