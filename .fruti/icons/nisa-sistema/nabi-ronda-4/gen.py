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

from fontTools.pens.boundsPen import BoundsPen
N=[(0,3),(0,2),(0,1),(0,0),(1,1),(2,2),(3,3),(3,2),(3,1),(3,0)]   # orden del trazo de la N
NS=set(N); ACT=(3,0)
def cell(shape,x,y,f,r=11,cls=''):
    c=f' class="{cls}"' if cls else ''
    if shape=='R': return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}"{c}/>'
    return f'<rect x="{x-r}" y="{y-r}" width="{2*r}" height="{2*r}" rx="{r*0.62:.1f}" fill="{f}"{c}/>'
def empty(shape,x,y):
    if shape=='R': return f'<circle cx="{x}" cy="{y}" r="3.2" fill="{INK}"/>'
    return f'<rect x="{x-3.4}" y="{y-3.4}" width="6.8" height="6.8" rx="1.8" fill="{INK}"/>'
def sym(shape,ink=INK,acc=ACT,empties=True,anim=False):
    s=''
    for c in range(4):
        for r in range(4):
            x=25+c*26; y=25+r*26
            if (c,r) in NS:
                if anim: s+=cell(shape,x,y,ink,cls=f'w w{N.index((c,r))}')
                else: s+=cell(shape,x,y,PERA if (c,r)==acc else ink)
            elif empties: s+=empty(shape,x,y).replace(INK,ink)
    if anim:
        css='.w{animation:nb 2s linear infinite}'+''.join(f'.w{i}{{animation-delay:{i*0.2:.1f}s}}' for i in range(10))
        css+=f'@keyframes nb{{0%,9%{{fill:{PERA}}}10%,100%{{fill:{ink}}}}}@media (prefers-reduced-motion:reduce){{.w{{animation:none}}.w9{{fill:{PERA}}}}}'
        s=f'<style>{css}</style>'+s
    return s
def fav(shape,ink=INK):  # 16 px: solo la N, pocillos más grandes, sin vacíos
    s=''
    for (c,r) in N:
        x=22+c*28; y=22+r*28
        s+=cell(shape,x,y,PERA if (c,r)==ACT else ink,r=13.5)
    return s
def svg(b,size=128,vb='0 0 128 128'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{size}" height="{size}">{b}</svg>'
def app(shape,dark=True,size=88):
    bg=INK if dark else '#FFFFFF'; ink='#FFFFFF' if dark else INK; brd='' if dark else f' stroke="#E2E5EC" stroke-width="2"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-22 -22 172 172" width="{size}" height="{size}"><rect x="-22" y="-22" width="172" height="172" rx="38" fill="{bg}"{brd}/>{sym(shape,ink)}</svg>'
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

def lockup(shape,ink=INK):
    w,x=wordmark()
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {x+10:.0f} 128" height="64">{sym(shape,ink)}{w.replace(INK,ink)}</svg>'
V={'R':('Pocillo redondo','La N de A2: pocillos redondos y vacíos como puntos. Más laboratorio: así se ve una placa real.'),
   'Q':('Pocillo cuadrado','La misma N en cuadrado redondeado (A4). Más software: se alinea con la retícula de la interfaz.')}
rows=''
for k,(n,t) in V.items():
    strip=''.join(f'<span>{svg(sym(k,acc=N[i]),36)}</span>' for i in range(0,10,2))
    rows+=f"""<div class="c"><div class="big">{svg(sym(k))}</div><div class="side"><h2>{n}</h2><p>{t}</p>
<div class="row"><div class="lk">{lockup(k)}</div><div class="lk dk">{lockup(k,'#FFFFFF')}</div></div>
<div class="row"><span class="m">{app(k)}app</span><span class="m">{app(k,False)}app claro</span><span class="m">{svg(fav(k),32,'0 0 128 128')}favicon 32</span><span class="m">{svg(fav(k),16,'0 0 128 128')}favicon 16</span><span class="m">{svg(sym(k),24)}24</span></div>
<div class="row"><span class="m an">{svg(sym(k,anim=True),64)}carga (animado)</span><span class="strip">{strip}</span></div></div></div>"""
    for nm,b in [(f'simbolo-{k}',sym(k)),(f'favicon-{k}',fav(k)),(f'carga-{k}',sym(k,anim=True))]: open(nm+'.svg','w').write(svg(b))
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#fff;color:#1B1F2B;font:14px/1.45 sans-serif;padding:32px}}h1{{font:700 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 16px;color:#5A6070;max-width:900px}}
.c{{display:grid;grid-template-columns:200px 1fr;gap:32px;align-items:start;padding:22px 0;border-top:1px solid #E2E5EC}}.big svg{{width:200px;height:200px;display:block}}
.side{{display:grid;gap:14px}}.side h2{{font:600 16px sans-serif;margin:0}}.side p{{margin:0;color:#5A6070;font-size:13px;max-width:640px}}
.row{{display:flex;gap:18px;align-items:flex-end;flex-wrap:wrap}}.lk{{padding:10px 14px;border-radius:10px}}.lk svg{{display:block;height:56px;width:auto}}.dk{{background:{INK}}}
.m{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5A6070}}.strip{{display:flex;gap:6px;padding-left:16px;border-left:1px solid #E2E5EC}}
</style></head><body><h1>Nabi · ronda 4 · A2 + A4 + A5</h1><p class="i">La N de pocillos con la muestra pera, en dos formas de pocillo. El favicon pierde los vacíos y agranda los pocillos para leerse a 16 px. La carga es la muestra recorriendo la N; con «reducir movimiento» queda fija.</p>{rows}</body></html>""")
print('ok')
