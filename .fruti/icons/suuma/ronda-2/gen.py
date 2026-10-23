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
def blob(cx,cy,r,seed,k=0.16,n=56):
    rr=random.Random(seed); ph=[rr.random()*6.28 for _ in range(3)]; pts=[]
    for i in range(n):
        a=2*math.pi*i/n; rad=r*(1+k*math.sin(2*a+ph[0])+k*0.5*math.sin(3*a+ph[1])+k*0.3*math.sin(5*a+ph[2]))
        pts.append((cx+rad*math.cos(a),cy+rad*math.sin(a)))
    return 'M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)+'Z'
I=lambda d,f=None:f'<path d="{d}" fill="{f or INK}"/>'
S=lambda d,w,c=None:f'<path d="{d}" fill="none" stroke="{c or INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
C={}
# A · Hueco: una masa orgánica de tinta con una U vaciada; la marca es lo que falta
A_mass=blob(64,64,56,11,k=0.09)
A_u='M42 30 C40 60 44 86 64 88 C84 86 88 60 86 30'
C['A']=('Hueco',I(A_mass)+S(A_u,15,BG),'Una masa de tinta con la U vaciada. La marca es el hueco: el lugar que ocupa cada quien.')
# B · Enjambre: nueve formas distintas empacadas; falta una: tu lugar. La regla admite N piezas
pos=[(40,34),(68,30),(96,38),(30,62),(58,60),(88,66),(44,92),(72,94),(102,92)]
B=''.join(I(blob(x+random.Random(i).uniform(-2,2),y+random.Random(i+9).uniform(-2,2),13.5,i*7+3,k=0.2)) for i,(x,y) in enumerate(pos) if i!=5)
C['B']=('Enjambre',B,'Nueve lugares, ocho formas distintas: falta una. Es un sistema: crece con cada perfil.')
# C · Suma: dos formas en U se superponen; la intersección es una tercera forma, la real
U1=blob(50,62,30,21,k=0.12); U2=blob(80,68,30,22,k=0.12)
C['C']=('Suma',f'<defs><pattern id="h" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="{INK}"/><rect width="2.4" height="6" fill="{BG}"/></pattern><clipPath id="k"><path d="{U1}"/></clipPath></defs>'+I(U1)+S(U2,4.5)+f'<path d="{U2}" fill="url(#h)" clip-path="url(#k)"/>','Dos formas se superponen y la intersección es una tercera. Uno más uno hace algo nuevo.')
# D · Bloque: un bloque sólido con dos U mordidas de distinta profundidad; monolítico, de app
D_block='M14 22 C14 12 22 8 34 8 L94 8 C108 8 116 14 116 26 L116 100 C116 114 106 120 92 120 L34 120 C20 120 12 112 12 98Z'
C['D']=('Bloque',I(D_block)+S('M34 0 C32 36 36 58 48 60 C60 58 64 36 62 0',11,BG)+S('M76 0 C74 24 78 42 90 44 C102 42 106 24 104 0',11,BG),'Un bloque con dos U mordidas, una más honda. Lee como sello y como icono de app.')
# E · Fragmentos: una U hecha de piezas desiguales que no se tocan; muchos hacen uno
path=catmull([(26,22),(24,70),(44,100),(70,104),(94,86),(102,46),(104,22)],n=200)
segs=[(0,22,7),(30,58,9),(66,96,6),(104,134,10),(142,166,7),(174,199,8)]
E=''
for a,b,w in segs:
    pts=path[a:b+1]; L=[];R=[]
    for i,(x,y) in enumerate(pts):
        p0=pts[max(i-1,0)]; p1=pts[min(i+1,len(pts)-1)]; dx,dy=p1[0]-p0[0],p1[1]-p0[1]; d=math.hypot(dx,dy) or 1
        nx,ny=-dy/d,dx/d; t=i/(len(pts)-1); ww=w*(0.55+0.45*math.sin(math.pi*t))
        L.append((x+nx*ww,y+ny*ww)); R.append((x-nx*ww,y-ny*ww))
    E+=I('M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in L+R[::-1])+'Z')
C['E']=('Fragmentos',E,'Una U hecha de piezas desiguales que no se tocan. Muchos hacen uno sin fundirse.')
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:{BG};color:{INK};font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 24px;color:#5B5750}}
.g{{display:grid;grid-template-columns:repeat(5,1fr);gap:24px}}.c{{display:grid;gap:10px;justify-items:center;text-align:center}}
.big svg{{width:200px;height:200px;display:block}}.sm{{display:flex;gap:14px;align-items:flex-end}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5B5750}}
.c h2{{font:600 16px sans-serif;margin:6px 0 0}}.c p{{margin:0;color:#5B5750;font-size:13px;max-width:220px}}
</style></head><body><h1>SUUMA · ronda 2 · cambiar el mecanismo, no solo el trazo</h1><p class="i">Vacío, sistema, superposición, bloque y fragmentos. A 200, 32 y 16 px.</p><div class="g">"""+''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="sm"><span>{svg(b,16)}16</span><span>{svg(b,32)}32</span><span>{svg(b,64)}64</span></div><h2>{k} · {n}</h2><p>{t}</p></div>' for k,(n,b,t) in C.items())+'</div></body></html>')
for k,(n,b,t) in C.items(): open(f'{k}.svg','w').write(svg(b))
print('ok')
