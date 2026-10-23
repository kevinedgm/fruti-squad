import math
INK='#1F1D1A'; BG='#FAF7F2'
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

def stroke(pts,w,n=90,p=0.8,lo=0.1,hi=0.9): return brush(pts,lambda t:w*math.sin(math.pi*(lo+(hi-lo)*t))**p,n=n)
I=lambda d,f=None:f'<path d="{d}" fill="{f or INK}"/>'
P=lambda x,y,r=6,f=None:f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f or INK}"/>'
C={}
# A · Doble U: dos U de pincel, una delante de otra, desfasadas; comparten el valle
U1=stroke([(30,30),(28,70),(50,98),(76,90),(86,56)],8,lo=0.08,hi=0.92)
U2=stroke([(66,46),(66,82),(86,106),(110,96),(116,66)],6,lo=0.08,hi=0.92)
C['A']=('Doble U',I(U1)+I(U2),'Dos U de pincel, desfasadas: el nombre hecho gesto. Donde se cruzan, suman.')
# B · Nodos: tres formas orgánicas distintas que se tocan y forman una sola silueta
def blob(cx,cy,r,seed,k=0.18,n=48):
    import random; rr=random.Random(seed); ph=[rr.random()*6.28 for _ in range(3)]
    pts=[]
    for i in range(n):
        a=2*math.pi*i/n; rad=r*(1+k*math.sin(2*a+ph[0])+k*0.5*math.sin(3*a+ph[1]))
        pts.append((cx+rad*math.cos(a),cy+rad*math.sin(a)))
    return 'M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)+'Z'
C['B']=('Nodos',I(blob(46,50,24,1))+I(blob(82,46,17,2))+I(blob(70,84,21,3))+P(104,86,7),'Tres formas distintas que se tocan y hacen una silueta; cada una conserva la suya. Un punto se acerca.')
# C · Onda: un solo trazo que dibuja uu como una ola: dos valles, un gesto
W=stroke([(14,34),(18,78),(44,98),(66,78),(70,58),(78,76),(100,88),(116,66),(118,46)],7.5,lo=0.05,hi=0.95,n=140)
C['C']=('Onda',I(W),'Un solo trazo que escribe «uu» como una ola. Dos valles, un gesto: sumar sin cortar.')
# D · Fila: puntos que crecen a lo largo de una curva: la fila que avanza
pts=catmull([(14,96),(40,88),(62,70),(86,48),(108,26)],n=100)
D=''.join(P(pts[int(i)][0],pts[int(i)][1],r) for i,r in [(2,3.2),(22,4.4),(44,5.8),(68,7.4),(96,9.4)])
C['D']=('Fila',D,'Puntos que crecen a lo largo de una trayectoria: la fila que avanza y cada uno llega más lejos.')
# E · Encuentro: dos trazos que vienen de lados distintos y se funden en uno más grueso
E1=stroke([(18,22),(28,52),(62,70)],6,lo=0.3,hi=1.0,n=60)
E2=stroke([(110,30),(98,58),(62,70)],5,lo=0.3,hi=1.0,n=60)
E3=stroke([(62,70),(56,92),(66,112)],9,lo=0.0,hi=0.85,n=60)
C['E']=('Encuentro',I(E1)+I(E2)+I(E3)+P(62,70,8,BG)+P(62,70,4.5),'Dos trazos de lados distintos se funden en uno más grueso. El punto es el encuentro.')
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:{BG};color:{INK};font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 24px;color:#5B5750}}
.g{{display:grid;grid-template-columns:repeat(5,1fr);gap:24px}}.c{{display:grid;gap:10px;justify-items:center;text-align:center}}
.big svg{{width:200px;height:200px;display:block}}.sm{{display:flex;gap:14px;align-items:flex-end}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5B5750}}
.inv{{background:{INK};border-radius:12px;padding:10px}}.inv svg path,.inv svg circle{{fill:{BG}}}.inv svg circle[fill="{BG}"]{{fill:{INK}}}
.c h2{{font:600 16px sans-serif;margin:6px 0 0}}.c p{{margin:0;color:#5B5750;font-size:13px;max-width:220px}}
</style></head><body><h1>SUUMA · ronda 1 · símbolo en blanco y negro</h1><p class="i">Abstracto y orgánico: la doble U y «individuos que forman una figura común». A 200, 32 y 16 px y en negativo.</p><div class="g">"""+''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="sm"><span>{svg(b,16)}16</span><span>{svg(b,32)}32</span><span class="inv">{svg(b,48)}</span></div><h2>{k} · {n}</h2><p>{t}</p></div>' for k,(n,b,t) in C.items())+'</div></body></html>')
for k,(n,b,t) in C.items(): open(f'{k}.svg','w').write(svg(b))
print('ok')
