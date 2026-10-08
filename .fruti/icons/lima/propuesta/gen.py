# Lima · variantes (E2) + medición de separaciones (A6) y márgenes (A2)
import math
SW=2
def hexpts(R,cx=12,cy=12): return [(cx+R*math.sin(math.radians(a)), cy-R*math.cos(math.radians(a))) for a in range(0,360,60)]
def segdist(p,a,b):
    ax,ay=a; bx,by=b; px,py=p; dx,dy=bx-ax,by-ay; t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy)))
    return math.hypot(px-ax-t*dx,py-ay-t*dy)
def sample(a,b,n=40): return [(a[0]+(b[0]-a[0])*i/n, a[1]+(b[1]-a[1])*i/n) for i in range(n+1)]
def gap(lines,poly):
    edges=list(zip(poly,poly[1:]+poly[:1]))
    return min(segdist(p,a,b) for l in lines for p in sample(*l) for a,b in edges)-SW
def rr_poly(x0,y0,x1,y1,r,n=8):
    pts=[]
    for cx,cy,a0 in ((x1-r,y0+r,-90),(x1-r,y1-r,0),(x0+r,y1-r,90),(x0+r,y0+r,180)):
        pts+= [(cx+r*math.cos(math.radians(a0+90*i/n)), cy+r*math.sin(math.radians(a0+90*i/n))) for i in range(n+1)]
    return pts
def svg(id_,cont,lines):
    body=''.join(f'  <path class="uva-{id_}__{n}" d="M{a[0]:g} {a[1]:g}{"V"+format(b[1],"g") if a[0]==b[0] else "H"+format(b[0],"g")}"/>\n' for n,(a,b) in lines)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="uva-icon uva-{id_}" aria-hidden="true">\n'
            f'  <style>.uva-{id_}{{stroke-width:var(--uva-stroke,2)}}</style>\n  {cont}\n{body}</svg>\n')
H=hexpts(9)
hexd='M'+' L'.join('%.2f %.2f'%p for p in H)+'Z'
V={}
# V1 hexágono + I (entrada, eje, salida) — la referencia del brief
L1=[('entrada',((9.75,9),(14.25,9))),('eje',((12,9),(12,15))),('salida',((9.75,15),(14.25,15)))]
V['v1-hexagono']=(f'<path class="uva-v1-hexagono__contenedor" d="{hexd}"/>',L1,H)
# V2 squircle vertical + I
sq=rr_poly(5,3,19,21,5.5)
V['v2-squircle']=('<rect class="uva-v2-squircle__contenedor" x="5" y="3" width="14" height="18" rx="5.5"/>',[('entrada',((9.25,8.5),(14.75,8.5))),('eje',((12,8.5),(12,15.5))),('salida',((9.25,15.5),(14.75,15.5)))],sq)
# V3 hexágono + eje de vértice a vértice + dos compuertas que lo cruzan
L3=[('eje',((12,3),(12,21))),('entrada',((9.5,9.5),(14.5,9.5))),('salida',((9.5,14.5),(14.5,14.5)))]
V['v3-compuertas']=(f'<path class="uva-v3-compuertas__contenedor" d="{hexd}"/>',L3,H)
for k,(cont,lines,poly) in V.items():
    open(f'{k}.svg','w').write(svg(k,cont,lines))
    inner=[l for n,l in lines if not (k=='v3-compuertas' and n=='eje')]
    xs=[p[0] for p in poly]; ys=[p[1] for p in poly]
    print(f'{k}: hueco barra–contenedor {gap(inner,poly):.2f} (≥2) · margen {min(min(xs),24-max(xs),min(ys),24-max(ys))-SW/2:.2f} (≥2)')
