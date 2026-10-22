import math,random,json,sys
# ---- motivos en la línea de la flor de Laranda (caja 128) ----
LOBOS=['M60 46 C54 30 40 26 34 36 C28 46 38 56 50 56','M68 44 C72 30 88 26 94 36 C100 46 90 56 78 58','M80 66 C96 64 104 76 98 86 C92 94 78 92 72 80','M66 86 C70 100 60 110 50 104 C42 98 46 88 56 84','M48 76 C34 82 22 74 26 62 C30 52 44 54 52 62']
LOB_OFF=[(0,0),(4,-4),(0,0),(0,0),(0,0)]
MANCHA='M62 36 C50 26 36 34 40 50 C28 54 24 70 34 78 C42 86 54 84 60 76 C62 92 78 100 88 90 C96 82 92 70 84 64 C98 58 100 42 88 36 C80 30 70 32 62 36Z'
LOBULO='M70 20 C78 14 92 18 96 30 C98 40 90 48 80 46 C72 44 66 32 70 20Z'
def wob(d,r,amp=1.6):
    # variación orgánica sutil: desplaza cada número del path ±amp (determinista)
    out=[];
    for tok in d.replace(',',' ').split():
        try: v=float(tok); out.append(f'{v+r.uniform(-amp,amp):.1f}')
        except ValueError: out.append(tok)
    return ' '.join(out)
def flor(r,acc=None):
    s=''
    if acc=='brand': s+=f'<path d="{MANCHA}" fill="{{BRAND}}" transform="translate(8 7)"/>'
    if acc=='accent': s+=f'<path d="{LOBULO}" fill="{{ACCENT}}" transform="translate(9 6)"/>'
    for d,(dx,dy) in zip(LOBOS,LOB_OFF): s+=f'<path d="{wob(d,r)}" transform="translate({dx} {dy})"/>'
    s+=f'<circle cx="64" cy="68" r="4.5"/>'
    return s,56
def capullo(r):
    s=''.join(f'<path d="{wob(d,r)}"/>' for d in (LOBOS[0],LOBOS[1],LOBOS[4]))
    s+=f'<path d="{wob("M64 62 C62 80 66 96 60 118",r)}"/>'
    return s,50
def petalo(r):
    s=f'<path d="{wob("M44 92 C36 66 50 40 78 32 C84 58 72 82 44 92",r)}"/><path d="{wob("M50 84 C56 66 64 52 74 42",r,1.0)}"/>'
    return s,30
def ramita(r):
    s=f'<path d="{wob("M20 110 C40 90 60 70 100 24",r)}"/>'
    for t,(x,y,a) in enumerate([(40,88,-30),(56,70,40),(72,54,-30),(86,40,40)]):
        s+=f'<path d="{wob("M0 0 C2 -12 14 -20 26 -18 C24 -6 14 2 0 0Z",r,1.2)}" transform="translate({x} {y}) rotate({a})"/>'
    return s,56
def puntos(r):
    s=''.join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="currentColor" stroke="none"/>' for x,y in [(40,80),(60,60),(84,48)])
    return s,30
def trazo(r):
    s=f'<path d="{wob("M30 70 C50 50 70 70 96 52",r)}"/>'
    return s,30
KINDS=[('flor',flor,1.0),('capullo',capullo,1.2),('petalo',petalo,2.2),('ramita',ramita,1.3),('puntos',puntos,1.6),('trazo',trazo,0.5)]
def pick(r):
    tot=sum(w for _,_,w in KINDS); x=r.uniform(0,tot)
    for n,f,w in KINDS:
        x-=w
        if x<=0: return n,f
    return KINDS[-1][:2]
def build(W,H,seed,n_target,sw,torus=False,center_free=0,accents=(3,1),scale_rng=(0.9,1.6)):
    r=random.Random(seed); placed=[]; items=[]; kinds=[]; acc=list(accents); tries=0
    def dist(a,b):
        dx=abs(a[0]-b[0]); dy=abs(a[1]-b[1])
        if torus: dx=min(dx,W-dx); dy=min(dy,H-dy)
        return math.hypot(dx,dy)
    grid=None
    if torus:
        k=int(round(n_target**0.5)); cw,ch=W/k,H/k
        grid=[(i*cw+r.uniform(0.15,0.85)*cw,j*ch+r.uniform(0.15,0.85)*ch) for i in range(k) for j in range(k)]
        r.shuffle(grid)
    while len(items)<n_target and tries<20000:
        tries+=1
        if grid:
            if not grid: break
            x,y=grid[0]
        else:
            x=r.uniform(0,W); y=r.uniform(0,H)
        if center_free:
            # densidad hacia los lados: rechaza el centro con probabilidad según distancia al eje
            d=abs(x-W/2)/(W/2)
            if d<center_free/W: continue
            if r.random()>d**0.8: continue
        name,fn=pick(r)
        sc=r.uniform(*scale_rng)*(1.35 if name=='flor' else 1.0)
        rad=(56 if name in('flor','ramita') else 40)*sc*0.9
        if any(dist((x,y),p)<rad+pr+10 for p,pr in placed):
            if grid: grid.pop(0)
            continue
        if grid: grid.pop(0)
        a=None
        if name=='flor' and acc[0]>0 and r.random()<0.5: a='brand'; acc[0]-=1
        elif name=='flor' and acc[1]>0 and r.random()<0.5: a='accent'; acc[1]-=1
        rr=random.Random(r.random())
        body,_=fn(rr,a) if name=='flor' else fn(rr)
        rot=r.uniform(-35,35)
        items.append((x,y,sc,rot,body)); placed.append(((x,y),rad)); kinds.append(name)
    g=''
    offs=[(0,0)] if not torus else [(i*W,j*H) for i in (-1,0,1) for j in (-1,0,1)]
    for x,y,sc,rot,body in items:
        for ox,oy in offs:
            g+=f'<g transform="translate({x+ox:.1f} {y+oy:.1f}) rotate({rot:.1f}) scale({sc:.3f}) translate(-64 -64)">{body}</g>'
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><style>path,circle{{vector-effect:non-scaling-stroke}}</style><g fill="none" stroke="{{INK}}" color="{{INK}}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke">{g}</g></svg>'
    return svg,kinds
COL={'hueso':{'INK':'#F6F4EF','BRAND':'#C4B5F0','ACCENT':'#F2A074'},'tinta':{'INK':'#111013','BRAND':'#5B3BB5','ACCENT':'#E0611A'}}
def write(name,svg):
    for v,c in COL.items():
        s=svg
        for k,val in c.items(): s=s.replace('{'+k+'}',val)
        open(f'{name}-{v}.svg','w').write(s)
seed=int(sys.argv[1]) if len(sys.argv)>1 else 7
seed_t=int(sys.argv[2]) if len(sys.argv)>2 else 15
# grande: trazo 3.5 px en 2560; el stroke se escala con el motivo, así que doy sw por motivo ≈ 3.5/scale medio
g,n1=build(2560,1440,seed,n_target=95,sw=3.5,center_free=1000,accents=(3,1),scale_rng=(1.0,1.9))
write('doodle-hero',g)
t,n2=build(600,600,seed_t,n_target=16,sw=4,torus=True,accents=(1,0),scale_rng=(0.75,1.2))
write('doodle-mosaico',t)
print(len(n1),len(n2),sorted(n2))
