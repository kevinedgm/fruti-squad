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

def stroke(pts,w,n=70,p=0.8,lo=0.1,hi=0.9): return brush(pts,lambda t:w*math.sin(math.pi*(lo+(hi-lo)*t))**p,n=n)
def polar(cx,cy,ang,r): a=math.radians(ang); return (cx+r*math.cos(a),cy+r*math.sin(a))
def ray(cx,cy,ang,r0,r1,w,curve=0,n=60,lo=0.15,hi=1.0,p=0.9):
    a=math.radians(ang); ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux; m=(r0+r1)/2
    pts=[(cx+ux*r0,cy+uy*r0),(cx+ux*m+px*curve,cy+uy*m+py*curve),(cx+ux*r1,cy+uy*r1)]
    return brush(pts,lambda t:w*(0.35+0.65*math.sin(math.pi*(lo+(hi-lo)*t))**p),n=n)
I=lambda d:f'<path d="{d}" fill="{INK}"/>'
P=lambda x,y,r=6:f'<circle cx="{x}" cy="{y}" r="{r}" fill="{INK}"/>'
C={}
# ---- E · Aleteo
C['E1']=('E1 · Aleteo', ''.join(I(stroke([(x0,y0),(x0+dx*.5+c,y0+dy*.5),(x0+dx,y0+dy)],w)) for x0,y0,dx,dy,w,c in [(40,100,26,-84,6.5,6),(58,104,30,-66,5.5,5),(78,106,26,-44,4.5,4)])+P(30,110),'La de la ronda 2: tres trazos desiguales y el punto abajo.')
C['E2']=('E2 · Abanico', ''.join(I(ray(34,104,a,16,L,w,curve=c,lo=0.05)) for a,L,w,c in [(-72,92,7,6),(-50,78,6,5),(-28,58,5,4)])+P(34,104,6.5),'Los tres trazos nacen del mismo punto: el pivote del vuelo.')
C['E3']=('E3 · Suelto', I(stroke([(44,104),(50,60),(66,18)],7,n=80,lo=0.06,hi=0.96))+I(stroke([(64,100),(76,66),(94,34)],5.5,lo=0.06,hi=0.96))+I(stroke([(88,106),(98,84),(112,66)],4.2,lo=0.1,hi=0.95))+P(32,60,6),'Trazos rectos y limpios; el punto flota a un lado, no abajo.')
C['E4']=('E4 · Cuatro alas', ''.join(I(ray(28,110,a,14,L,w,curve=c,lo=0.05)) for a,L,w,c in [(-78,96,6.5,5),(-60,70,5.5,4),(-44,84,5,5),(-26,52,4.5,3)])+P(28,110,6.5),'Cuatro trazos, dos largos y dos cortos, como las cuatro alas. Más denso.')
# ---- B · Cuatro vientos
C['B1']=('B1 · Cuatro vientos', ''.join(I(ray(64,64,a,12,12+L,w,curve=c)) for a,L,w,c in [(-100,48,6.5,5),(-10,34,5,-4),(80,40,5.5,6),(176,26,4.5,-3)]),'La de la ronda 2: cuatro trazos desiguales desde un vacío.')
C['B2']=('B2 · Giro', ''.join(I(ray(64,64,a,13,13+L,w,curve=c)) for a,L,w,c in [(-100,48,6.5,9),(-10,38,5.5,8),(80,44,6,9),(170,30,5,7)]),'Los cuatro trazos giran en el mismo sentido: el aire que mueve al quedarse quieta.')
C['B3']=('B3 · Punto', ''.join(I(ray(66,62,a,18,18+L,w,curve=c)) for a,L,w,c in [(-100,44,6.5,5),(-12,32,5,-4),(78,38,5.5,6),(174,24,4.5,-3)])+P(66,62,5.5),'El vacío se vuelve punto: el foco de la interfaz vive en el centro.')
C['B4']=('B4 · Tres y uno', ''.join(I(ray(64,66,a,12,12+L,w,curve=c)) for a,L,w,c in [(-96,50,7,6),(-4,36,5,-3),(84,46,6,6)])+P(polar(64,66,178,30)[0],polar(64,66,178,30)[1],5.5),'Tres trazos y, en el cuarto rumbo, el punto: donde se detiene.')
cols=4
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:{BG};color:{INK};font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 24px;color:#57534E}}
.g{{display:grid;grid-template-columns:repeat(4,1fr);gap:28px 24px}}.c{{display:grid;gap:10px;justify-items:center;text-align:center}}
.big svg{{width:180px;height:180px;display:block}}.sm{{display:flex;gap:14px;align-items:flex-end}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#57534E}}
.inv{{background:{INK};border-radius:12px;padding:10px}}.inv svg path,.inv svg circle{{fill:{BG}}}
.c h2{{font:600 15px sans-serif;margin:6px 0 0}}.c p{{margin:0;color:#57534E;font-size:13px;max-width:220px}}
</style></head><body><h1>Libela · ronda 3 · desarrollo de E (Aleteo) y B (Cuatro vientos)</h1><p class="i">Cuatro variaciones de cada una. A 180, 32 y 16 px y en negativo.</p><div class="g">"""+''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="sm"><span>{svg(b,16)}16</span><span>{svg(b,32)}32</span><span class="inv">{svg(b,48)}</span></div><h2>{n}</h2><p>{t}</p></div>' for k,(n,b,t) in C.items())+'</div></body></html>')
for k,(n,b,t) in C.items(): open(f'{k}.svg','w').write(svg(b))
print('ok')
