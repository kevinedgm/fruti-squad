import math
INK='#1C1917'; BG='#FAF8F5'
def catmull(pts,n=160):
    P=[pts[0]]+list(pts)+[pts[-1]]; out=[]
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        for k in range(n//(len(P)-3)):
            t=k/(n//(len(P)-3)); t2=t*t; t3=t2*t
            x=0.5*((2*p1[0])+(-p0[0]+p2[0])*t+(2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2+(-p0[0]+3*p1[0]-3*p2[0]+p3[0])*t3)
            y=0.5*((2*p1[1])+(-p0[1]+p2[1])*t+(2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2+(-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)
            out.append((x,y))
    out.append(pts[-1]); return out
def brush(pts,prof,n=160):
    """trazo de pincel: línea central Catmull-Rom por pts, ancho según prof(t) (0..1)."""
    c=catmull(pts,n); L=[];R=[]
    for i,(x,y) in enumerate(c):
        a=c[max(i-1,0)]; b=c[min(i+1,len(c)-1)]; dx,dy=b[0]-a[0],b[1]-a[1]; d=math.hypot(dx,dy) or 1
        nx,ny=-dy/d,dx/d; w=prof(i/(len(c)-1))
        L.append((x+nx*w,y+ny*w)); R.append((x-nx*w,y-ny*w))
    pts2=L+R[::-1]
    return 'M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts2)+'Z'
taper=lambda a,b,p=1.0: (lambda t: a+(b-a)*math.sin(math.pi*t)**p)
def svg(body,size=128): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}">{body}</svg>'
C={}
# A · Pausa: un gesto que baja, hace un rizo (se detiene en el aire) y sale; el punto es donde acierta
A=brush([(14,30),(44,22),(76,40),(86,72),(66,88),(46,72),(60,50),(92,52),(112,76),(114,104)],lambda t:1.2+7.5*math.sin(math.pi*t)**0.8)
C['A']=('Pausa',f'<path d="{A}" fill="{INK}"/><circle cx="26" cy="58" r="5.5" fill="{INK}"/>','Un gesto que baja, se detiene en un rizo y sale; el punto es donde acierta.')
# B · Cuatro vientos: cuatro trazos desiguales que nacen de un vacío (vuela en cuatro direcciones)
def rad(ang,L,w,curve):
    a=math.radians(ang); ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux
    pts=[(64+ux*12+px*0,64+uy*12),(64+ux*(12+L*.5)+px*curve,64+uy*(12+L*.5)+py*curve),(64+ux*(12+L),64+uy*(12+L))]
    return brush(pts,lambda t:w*(0.35+0.65*math.sin(math.pi*(0.15+0.85*t))**0.9),n=60)
B=''.join(f'<path d="{rad(a,L,w,c)}" fill="{INK}"/>' for a,L,w,c in [(-100,48,6.5,5),(-10,34,5,-4),(80,40,5.5,6),(176,26,4.5,-3)])
C['B']=('Cuatro vientos',B,'Cuatro trazos desiguales desde un vacío: vuela en cuatro direcciones, mira 360°.')
# C · Posarse: un solo trazo de pincel que baja, dobla y se afina; la L nace del gesto, no de la letra
Cc=brush([(70,10),(52,34),(42,64),(44,92),(62,104),(90,104),(116,98)],lambda t:2+9*math.sin(math.pi*(0.1+0.9*t))**0.7)
C['C']=('Posarse',f'<path d="{Cc}" fill="{INK}"/><circle cx="60" cy="80" r="6" fill="{BG}"/>','Un solo trazo que baja, dobla y se afina. El hueco queda dentro de la curva.')
# D · Mirada: arco casi cerrado de ancho variable (ver 360°) y un punto descentrado que lo rompe
D=brush([(84,20),(50,22),(26,52),(34,92),(72,110),(104,96),(112,70)],lambda t:1.5+7*math.sin(math.pi*(0.08+0.92*t))**0.8)
C['D']=('Mirada',f'<path d="{D}" fill="{INK}"/><circle cx="76" cy="62" r="7" fill="{INK}"/>','Un arco abierto de ancho variable y un punto fuera del centro: calcula y acierta.')
# E · Aleteo: tres trazos paralelos de largo distinto, vibración de alas; el punto los ancla
E=''.join(f'<path d="{brush([(x0,y0),(x0+dx*.5+c,y0+dy*.5),(x0+dx,y0+dy)],lambda t,w=w:w*math.sin(math.pi*(0.1+0.8*t))**0.8,n=60)}" fill="{INK}"/>' for x0,y0,dx,dy,w,c in [(40,100,26,-84,6.5,6),(58,104,30,-66,5.5,5),(78,106,26,-44,4.5,4)])
C['E']=('Aleteo',f'{E}<circle cx="30" cy="110" r="6" fill="{INK}"/>','Tres trazos desiguales, la vibración de un ala; el punto los ancla abajo.')
open('banco.html','w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:{BG};color:{INK};font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 24px;color:#57534E}}
.g{{display:grid;grid-template-columns:repeat(5,1fr);gap:24px}}.c{{display:grid;gap:10px;justify-items:center;text-align:center}}
.big svg{{width:200px;height:200px;display:block}}.sm{{display:flex;gap:14px;align-items:flex-end}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#57534E}}
.inv{{background:{INK};border-radius:12px;padding:10px}}.inv svg path,.inv svg circle{{fill:{BG}}}.inv svg circle[fill="{BG}"]{{fill:{INK}}}
.c h2{{font:600 16px sans-serif;margin:6px 0 0}}.c p{{margin:0;color:#57534E;font-size:13px;max-width:220px}}
</style></head><body><h1>Libela · ronda 2 · gesto abstracto, trazo orgánico</h1><p class="i">Nada de alas ni insecto: un trazo de pincel que cuenta «calcula, se detiene, acierta». A 200, 32 y 16 px y en negativo.</p><div class="g">'''+''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="sm"><span>{svg(b,16)}16</span><span>{svg(b,32)}32</span><span class="inv">{svg(b,48)}</span></div><h2>{k} · {n}</h2><p>{t}</p></div>' for k,(n,b,t) in C.items())+'</div></body></html>')
for k,(n,b,t) in C.items(): open(f'{k}.svg','w').write(svg(b))
print('ok')
