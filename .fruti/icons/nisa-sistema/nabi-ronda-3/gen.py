import sys
import math
INK='#052A76'; BG='#FFFFFF'; PERA='#C2D225'
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

import os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
S=sys.argv[1] if len(sys.argv)>1 else ''
inst='/tmp/nabi-archivo.ttf'
if not os.path.exists(inst): instancer.instantiateVariableFont(TTFont(S+'/fuentes/ArchivoVar.ttf'),{'wght':700,'wdth':125}).save(inst)
FONT=TTFont(inst); UPM=FONT['head'].unitsPerEm; GS=FONT.getGlyphSet()
def palabra(s,size,x0,y0,track=0):
    hf=hb.Font(hb.Face(hb.Blob.from_file_path(inst))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    order=FONT.getGlyphOrder(); k=size/UPM; x=x0; d=''
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        g=GS[order[i.codepoint]]; pen=SVGPathPen(GS); g.draw(TransformPen(pen,(k,0,0,-k,x,y0))); d+=pen.getCommands(); x+=ps.x_advance*k+track
    return d,x
def stroke(pts,w,n=140,p=0.8,lo=0.08,hi=0.92): return brush(pts,lambda t:w*math.sin(math.pi*(lo+(hi-lo)*t))**p,n=n)
def even(pts,w,n=140): return brush(pts,lambda t:w,n=n)
I=lambda d,f=None:f'<path d="{d}" fill="{f or INK}"/>'
O=lambda d,w,c=None:f'<path d="{d}" fill="none" stroke="{c or INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
P=lambda x,y,r,f=None:f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f or PERA}"/>'

from fontTools.pens.boundsPen import BoundsPen
C={}
N={(0,0),(0,1),(0,2),(0,3),(1,1),(2,2),(3,0),(3,1),(3,2),(3,3)}
ACT=(3,0)
def grid(cell,empty,acc=ACT,step=26,off=25,rows=4,cols=4,fill=N):
    s=''
    for c in range(cols):
        for r in range(rows):
            x=off+c*step; y=off+r*step
            if (c,r)==acc: s+=cell(x,y,PERA,True)
            elif (c,r) in fill: s+=cell(x,y,INK,True)
            else: s+=empty(x,y)
    return s
circ=lambda R: (lambda x,y,f,full:f'<circle cx="{x}" cy="{y}" r="{R}" fill="{f}"/>')
ring=lambda x,y:f'<circle cx="{x}" cy="{y}" r="9" fill="none" stroke="{INK}" stroke-width="2.5"/>'
pin=lambda x,y:f'<circle cx="{x}" cy="{y}" r="3.2" fill="{INK}"/>'
sq=lambda x,y,f,full:f'<rect x="{x-11}" y="{y-11}" width="22" height="22" rx="7" fill="{f}"/>'
sqe=lambda x,y:f'<rect x="{x-3.5}" y="{y-3.5}" width="7" height="7" rx="2" fill="{INK}"/>'
C['A1']=('Placa','Original: pocillos llenos que dibujan la N y vacíos en anillo.',grid(circ(10.5),ring))
C['A2']=('Solo la N','Los vacíos se reducen a puntos: la N se lee primero y la placa después. Mejor a 16 px.',grid(circ(11),pin))
plate=f'<path d="M14 6 H114 Q122 6 122 14 V114 Q122 122 114 122 H24 L6 104 V14 Q6 6 14 6Z" fill="none" stroke="{INK}" stroke-width="5"/>'
C['A3']=('Con placa','El cuerpo de la microplaca con su esquina cortada, el detalle real que marca el pocillo A1.',plate+grid(circ(9.5),pin,step=24,off=28))
C['A4']=('Pocillos cuadrados','Pocillos en cuadrado redondeado: se siente más interfaz, como píxeles de un sistema.',grid(sq,sqe))
# A5: la muestra pera viaja por la N
order=[(0,3),(0,2),(0,1),(0,0),(1,1),(2,2),(3,3),(3,2),(3,1),(3,0)]
C['A5']=('En proceso','La muestra pera recorre la N: el mismo símbolo sirve de indicador de carga y de estado.',grid(circ(11),pin,acc=(2,2)))
def svg(b,size=128): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}">{b}</svg>'
def inv(b): return b.replace(f'"{INK}"','"#FFFFFF"')
def app(b,size=72): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-22 -22 172 172" width="{size}" height="{size}"><rect x="-22" y="-22" width="172" height="172" rx="38" fill="{INK}"/>{inv(b)}</svg>'
# wordmark con i sin punto + pocillo pera
k=92/UPM
bp=BoundsPen(GS); GS['dotlessi'].draw(bp); ib=bp.bounds
def wordmark(x0=150,y0=100,size=92):
    d,xn=palabra('nab',size,x0,y0,track=-1); kk=size/UPM
    pen=SVGPathPen(GS); GS['dotlessi'].draw(TransformPen(pen,(kk,0,0,-kk,xn,y0))); d+=pen.getCommands()
    cx=xn+(ib[0]+ib[2])/2*kk; w=(ib[2]-ib[0])*kk; cy=y0-ib[3]*kk-w*0.95
    return f'<path d="{d}" fill="{INK}"/><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{w*0.62:.1f}" fill="{PERA}"/>', xn+GS['dotlessi'].width*kk
def lockup(b):
    wm,x=wordmark()
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {x+10:.0f} 128" height="64">{b}{wm}</svg>'
frames=''.join(f'<span>{svg(grid(circ(11),pin,acc=o),40)}</span>' for o in order[::3])
rows=''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="side"><div class="lk">{lockup(b)}</div><div class="sm"><span>{svg(b,16)}16</span><span>{svg(b,24)}24</span><span>{svg(b,32)}32</span><span>{app(b)}app</span>{"<span class=fr>"+frames+"</span>" if k_=="A5" else ""}</div><h2>{k_} · {n}</h2><p>{t}</p></div></div>' for k_,(n,t,b) in C.items())
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#fff;color:#1B1F2B;font:14px/1.45 sans-serif;padding:32px}}h1{{font:700 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 16px;color:#5A6070;max-width:900px}}
.c{{display:grid;grid-template-columns:180px 1fr;gap:28px;align-items:center;padding:18px 0;border-top:1px solid #E2E5EC}}.big svg{{width:180px;height:180px;display:block}}
.side{{display:grid;gap:10px}}.lk svg{{display:block;height:64px;width:auto}}.sm{{display:flex;gap:16px;align-items:flex-end}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5A6070}}.sm .fr{{display:flex;gap:6px;margin-left:12px;padding-left:16px;border-left:1px solid #E2E5EC}}
.side h2{{font:600 15px sans-serif;margin:0}}.side p{{margin:0;color:#5A6070;font-size:13px;max-width:640px}}
</style></head><body><h1>Nabi · ronda 3 · la placa</h1><p class="i">Cinco variaciones de la placa de pocillos. En el wordmark, el punto de la i es un pocillo pera. Cada una a 32, 24 y 16 px y como icono de app.</p>{rows}</body></html>""")
for k_,(n,t,b) in C.items(): open(f'{k_}.svg','w').write(svg(b))
print('ok')
