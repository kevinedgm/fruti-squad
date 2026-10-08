# Variantes de Coco, Bruno (builder), Mora y Fruti Squad 24 px + medición de huecos (A6) y márgenes (A2)
import math
SW=2
def circ(cx,cy,r,n=72): return [(cx+r*math.cos(2*math.pi*i/n), cy+r*math.sin(2*math.pi*i/n)) for i in range(n)]
def seg(a,b,n=30): return [(a[0]+(b[0]-a[0])*i/n, a[1]+(b[1]-a[1])*i/n) for i in range(n+1)]
def rrect(x0,y0,x1,y1,r,n=10):
    P=[]
    for cx,cy,a in ((x1-r,y0+r,-90),(x1-r,y1-r,0),(x0+r,y1-r,90),(x0+r,y0+r,180)):
        P+=[(cx+r*math.cos(math.radians(a+90*i/n)),cy+r*math.sin(math.radians(a+90*i/n))) for i in range(n+1)]
    out=[]
    for a,b in zip(P,P[1:]+P[:1]): out+=seg(a,b,4)
    return out
UNIDOS=set()
def gap(pieces):
    g=99
    for i in range(len(pieces)):
        for j in range(i+1,len(pieces)):
            if (i,j) in UNIDOS: continue
            (pa,ea),(pb,eb)=pieces[i],pieces[j]
            g=min(g,min(math.dist(p,q) for p in pa for q in pb)-ea-eb)
    return g
def margen(pieces): return min(min(min(x,24-x,y,24-y) for x,y in p)-e for p,e in pieces)
def svg(id_,body,sw=2):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" class="uva-icon uva-{id_}" aria-hidden="true">\n'
            f'  <style>.uva-{id_}{{stroke-width:var(--uva-stroke,{sw})}}</style>\n{body}</svg>\n')
def dot(id_,cls,x,y,r=0):  # r=0: punto (trazo de longitud cero) · r>0: círculo relleno
    if r==0: return f'  <path class="uva-{id_}__{cls}" d="M{x:g} {y:g}h0"/>\n', (([(x,y)],SW/2))
    return f'  <circle class="uva-{id_}__{cls}" cx="{x:g}" cy="{y:g}" r="{r:g}" fill="currentColor"/>\n', (([(x,y)],r+SW/2))
OUT={}
def add(id_,parts,sw=2):
    body=''.join(p[0] for p in parts); pcs=[p[1] for p in parts]
    OUT[id_]=(svg(id_,body,sw),gap(pcs),margen(pcs))
# ---------- COCO
def ring(id_,r=9): return (f'  <circle class="uva-{id_}__circulo" cx="12" cy="12" r="{r}"/>\n',(circ(12,12,r),SW/2))
add('coco-v1-fila',[ring('coco-v1-fila'),dot('coco-v1-fila','nodo',7,12),dot('coco-v1-fila','foco',12,12,.5),dot('coco-v1-fila','nodo',17,12)])
# diagonal ascendente que crece: el foco se acerca (inspección)
add('coco-v2-lupa',[ring('coco-v2-lupa'),dot('coco-v2-lupa','nodo',8,15),dot('coco-v2-lupa','nodo',11,12),dot('coco-v2-lupa','foco',14.5,8.5,.6)])
# triángulo de composición, foco arriba
add('coco-v3-composicion',[ring('coco-v3-composicion'),dot('coco-v3-composicion','foco',12,8,.75),dot('coco-v3-composicion','nodo',8.5,14.5),dot('coco-v3-composicion','nodo',15.5,14.5)])
# ---------- BRUNO (builder)
def modulo(id_,x0,y0,x1,y1,r): return (f'  <rect class="uva-{id_}__modulo" x="{x0:g}" y="{y0:g}" width="{x1-x0:g}" height="{y1-y0:g}" rx="{r:g}"/>\n',(rrect(x0,y0,x1,y1,r),SW/2))
def linea(id_,cls,a,b): return (f'  <path class="uva-{id_}__{cls}" d="M{a[0]:g} {a[1]:g}L{b[0]:g} {b[1]:g}"/>\n',(seg(a,b),SW/2))
UNIDOS={(0,1),(0,2)}
i='bruno-builder-v1-pines'
add(i,[modulo(i,4,3,20,15,4.5),linea(i,'entrada',(9,15),(9,21)),linea(i,'salida',(15,15),(15,21))])
i='bruno-builder-v2-estado'
add(i,[modulo(i,4,3,20,15,4.5),linea(i,'entrada',(9,15),(9,21)),linea(i,'salida',(15,15),(15,21)),dot(i,'estado',12,9,.75)])
i='bruno-builder-v3-flujo'   # props entra por la izquierda, events sale por la derecha
add(i,[modulo(i,7,5,17,19,4),linea(i,'entrada',(3,12),(7,12)),linea(i,'salida',(17,12),(21,12))])
UNIDOS=set()
# ---------- MORA
def anillo(id_,cls,x,y,r): return (f'  <circle class="uva-{id_}__{cls}" cx="{x:g}" cy="{y:g}" r="{r:g}"/>\n',(circ(x,y,r),SW/2))
i='mora-v1-racimo'; r=2.75; s=9.6; h=s*math.sqrt(3)/2; y0=12-h/3*1.0-0.4
add(i,[anillo(i,'documento',12-s/2,y0,r),anillo(i,'evidencia',12+s/2,y0,r),anillo(i,'registro',12,y0+h,r)])
i='mora-v2-base'; r=2.5
add(i,[anillo(i,'documento',7.5,13.75,r),anillo(i,'evidencia',16.5,13.75,r),anillo(i,'registro',12,5.95,r),linea(i,'base',(4.5,20.5),(19.5,20.5))])
i='mora-v3-capsulas'   # tres cápsulas en ritmo escalonado (fichas de un catálogo)
add(i,[linea(i,'documento',(5,7),(14,7)),linea(i,'evidencia',(8,12),(19,12)),linea(i,'registro',(5,17),(16,17))],sw=3)
# ---------- FRUTI SQUAD 24 (espiral sin núcleo: el centro es espacio negativo)
def brazo(k,r0,r1,span):
    pts=[(12+(r0+(r1-r0)*t/12)*math.cos(math.radians(-90+k*72+span*t/12)),12+(r0+(r1-r0)*t/12)*math.sin(math.radians(-90+k*72+span*t/12))) for t in range(13)]
    return pts
def squad(i,r0,r1,span,sw):
    parts=[]
    for k,n in enumerate(['kiwi','lima','coco','bruno','mora']):
        p=brazo(k,r0,r1,span); d='M'+' '.join('%.2f %.2f'%q for q in p)
        parts.append((f'  <path class="uva-{i}__{n}" d="{d}"/>\n',(p,sw/2)))
    OUT[i]=(svg(i,''.join(x[0] for x in parts),sw),gap([x[1] for x in parts]),margen([x[1] for x in parts]))
squad('fruti-squad-24-v1',4.2,8.4,46,2.75)
if __name__=='__main__':
    for k,(s,g,m) in OUT.items():
        open(k+'.svg','w').write(s); print(f'{k:28s} hueco mínimo {g:5.2f} · margen {m:4.2f}')
