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

import random
def polar(cx,cy,ang,r): a=math.radians(ang); return (cx+r*math.cos(a),cy+r*math.sin(a))
def blob(cx,cy,r,seed,k=0.16,n=56):
    rr=random.Random(seed); ph=[rr.random()*6.28 for _ in range(3)]; pts=[]
    for i in range(n):
        a=2*math.pi*i/n; rad=r*(1+k*math.sin(2*a+ph[0])+k*0.5*math.sin(3*a+ph[1])+k*0.3*math.sin(5*a+ph[2]))
        pts.append((cx+rad*math.cos(a),cy+rad*math.sin(a)))
    return 'M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)+'Z'
I=lambda d,f=None:f'<path d="{d}" fill="{f or INK}"/>'
S=lambda d,w,c=None:f'<path d="{d}" fill="none" stroke="{c or INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'

def stroke(pts,w,n=120,p=0.8,lo=0.1,hi=0.9): return brush(pts,lambda t:w*math.sin(math.pi*(lo+(hi-lo)*t))**p,n=n)
def line(pts,n=120): return 'M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in catmull(pts,n))
P=lambda x,y,r=6,f=None:f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f or INK}"/>'
C={}
# A · Senda: un camino grueso que se abre en dos y vuelve a juntarse; el punto es el inicio
A=I(stroke([(16,96),(30,78),(46,62),(62,54),(78,40),(96,30),(112,22)],8,lo=0.25,hi=0.95))+I(stroke([(46,62),(60,78),(80,70),(96,46),(104,34)],6,lo=0.2,hi=0.9))+P(14,100,6.5)
C['A']=('Senda',A,'Un camino que se abre en dos y vuelve a juntarse. Colaborar es compartir tramo sin perder el tuyo.')
# B · Une los puntos: puntos de distinto tamaño y una línea fina que los recorre sin cerrar
dots=[(22,88,5),(44,38,7),(72,66,4.5),(98,30,6),(108,84,8),(66,108,5.5)]
order=[0,1,2,3,4,5]
B=S(line([(dots[i][0],dots[i][1]) for i in order],n=160),2.6)+''.join(P(x,y,r) for x,y,r in dots)
C['B']=('Une los puntos',B,'Personas de distinto tamaño y una línea fina que pasa por todas sin cerrar el circuito.')
# C · Cuencos: una U dentro de otra, la interior desplazada; sumar es contener sin igualar
C1=stroke([(20,22),(22,70),(48,100),(80,102),(104,76),(108,24)],8.5,lo=0.06,hi=0.94)
C2=stroke([(50,46),(50,72),(64,84),(80,84),(90,70),(92,46)],6,lo=0.06,hi=0.94)
C['C']=('Cuencos',I(C1)+I(C2),'Una U dentro de otra, descentrada. Sumar es contener sin igualar: cada quien con su forma.')
# D · Trenza: dos hebras de grosor distinto que se cruzan una vez y siguen
D1=stroke([(14,34),(40,42),(64,64),(88,86),(114,96)],8,lo=0.08,hi=0.92)
D2=stroke([(18,96),(40,86),(64,64),(90,42),(112,30)],5.5,lo=0.08,hi=0.92)
C['D']=('Trenza',I(D1)+I(D2)+P(64,64,9,BG)+P(64,64,4.5),'Dos hebras de grosor distinto se cruzan una vez y siguen. El punto marca el cruce.')
# E · Eco: anillos irregulares abiertos por un lado alrededor de un punto descentrado
E=''.join(S(line([(polar(56,66,a,r)) for a in range(-150,151,30)],n=120),w) for r,w in [(18,4),(34,3.2),(50,2.6)])
C['E']=('Eco',E+P(56,66,7),'Anillos abiertos alrededor de un punto: lo que haces se propaga y vuelve. Cerca de ti.')
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:{BG};color:{INK};font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 24px;color:#5B5750}}
.g{{display:grid;grid-template-columns:repeat(5,1fr);gap:24px}}.c{{display:grid;gap:10px;justify-items:center;text-align:center}}
.big svg{{width:200px;height:200px;display:block}}.sm{{display:flex;gap:14px;align-items:flex-end}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5B5750}}
.c h2{{font:600 16px sans-serif;margin:6px 0 0}}.c p{{margin:0;color:#5B5750;font-size:13px;max-width:220px}}
</style></head><body><h1>SUUMA · ronda 3 · ideas desde la narrativa</h1><p class="i">Senda, unir puntos, contener, trenzar, propagarse. A 200, 64, 32 y 16 px.</p><div class="g">"""+''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="sm"><span>{svg(b,16)}16</span><span>{svg(b,32)}32</span><span>{svg(b,64)}64</span></div><h2>{k} · {n}</h2><p>{t}</p></div>' for k,(n,b,t) in C.items())+'</div></body></html>')
for k,(n,b,t) in C.items(): open(f'{k}.svg','w').write(svg(b))
print('ok')
