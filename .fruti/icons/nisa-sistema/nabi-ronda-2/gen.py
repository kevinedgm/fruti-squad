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

C={}
R=lambda x,y,w,h,rx=0,f=None:f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f or INK}"/>'
# A · Placa: placa de 4×4 pocillos; los llenos dibujan la N; uno en pera
cells=''
fill={(0,0),(0,1),(0,2),(0,3),(1,1),(2,2),(3,0),(3,1),(3,2),(3,3)}
for c in range(4):
    for r in range(4):
        x=25+c*26; y=25+r*26
        if (c,r)==(3,0): cells+=P(x,y,10.5)
        elif (c,r) in fill: cells+=f'<circle cx="{x}" cy="{y}" r="10.5" fill="{INK}"/>'
        else: cells+=f'<circle cx="{x}" cy="{y}" r="9" fill="none" stroke="{INK}" stroke-width="2.5"/>'
C['A']=('Placa',cells,'Una placa de pocillos, el instrumento de cualquier laboratorio. Los llenos dibujan la N; el pera es la muestra que se está procesando. Es un sistema: la placa puede cambiar de estado.')
# B · Etiqueta: la etiqueta de muestra con código de barras y el punto pera
bars=''.join(R(30+x,44,w,40) for x,w in [(0,5),(9,2.5),(15,7),(26,2.5),(32,4),(40,2.5),(46,6)])
C['B']=('Etiqueta',f'<rect x="12" y="28" width="104" height="72" rx="14" fill="none" stroke="{INK}" stroke-width="7"/>'+bars+P(96,64,9),'La etiqueta de una muestra: código de barras y un punto pera. Es lo que el sistema imprime y lee todos los días.')
# C · Gradilla: cuatro tubos con niveles crecientes; tapa pera en el último
tubes=''
for i,lv in enumerate([0.32,0.5,0.7,0.9]):
    x=16+i*26; top=18; h=84; liq=h*lv
    tubes+=f'<path d="M{x} {top} V{top+h-9} a9 9 0 0 0 18 0 V{top}" fill="none" stroke="{INK}" stroke-width="4.5"/>'
    tubes+=f'<path d="M{x+4} {top+h-liq} H{x+14} V{top+h-9} a5 5 0 0 1 -10 0Z" fill="{INK}"/>'
tubes+=R(92,8,22,9,3,PERA)
C['C']=('Gradilla',tubes,'Cuatro tubos, uno por letra de «nabi», con niveles que suben: el lote avanza. La tapa pera marca el que ya está listo.')
# D · b con giro: la b gruesa con el ojo lleno de pera; en el lockup, la b de la palabra lleva el mismo ojo
bb=f'<path d="M30 12 V112" stroke="{INK}" stroke-width="18" stroke-linecap="round"/><circle cx="66" cy="80" r="30" fill="none" stroke="{INK}" stroke-width="18"/><circle cx="66" cy="80" r="14" fill="{PERA}"/>'
C['D']=('b con ojo',bb,'La b de nabi con el ojo lleno de pera, como una muestra dentro del sistema. El giro vive en la letra, no en un dibujo aparte.')
# E · Esténcil: N cortada en tres piezas, la diagonal en pera
E=f'<path d="M16 112 V16 H39 V112Z" fill="{INK}"/><path d="M47 16 H64 L81 112 H64Z" fill="{PERA}"/><path d="M89 16 H112 V112 H89Z" fill="{INK}"/>'
C['E']=('Esténcil',E,'Una N de esténcil, como las letras pintadas en equipo y en cajas de laboratorio. Las piezas no se tocan; la del centro es pera.')
def svg(b,size=128): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}">{b}</svg>'
def inv(b): return b.replace(f'"{INK}"','"#FFFFFF"')
def app(b,size=72): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20 -20 168 168" width="{size}" height="{size}"><rect x="-20" y="-20" width="168" height="168" rx="38" fill="{INK}"/>{inv(b)}</svg>'
def lockup(k,b):
    d,x=palabra('nabi',92,150,100,track=-1); extra=''
    if k=='D':
        dn,xn=palabra('na',92,150,100,track=-1); db,xb=palabra('b',92,xn,100)
        extra=f'<circle cx="{xn+(xb-xn)*0.58:.1f}" cy="{100-92*0.27:.1f}" r="{92*0.11:.1f}" fill="{PERA}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {x+10:.0f} 128" height="64">{b}<path d="{d}" fill="{INK}"/>{extra}</svg>'
rows=''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="side"><div class="lk">{lockup(k,b)}</div><div class="sm"><span>{svg(b,16)}16</span><span>{svg(b,32)}32</span><span>{app(b)}app</span></div><h2>{k} · {n}</h2><p>{t}</p></div></div>' for k,(n,b,t) in C.items())
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#fff;color:#1B1F2B;font:14px/1.45 sans-serif;padding:32px}}h1{{font:700 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 16px;color:#5A6070;max-width:900px}}
.c{{display:grid;grid-template-columns:180px 1fr;gap:28px;align-items:center;padding:18px 0;border-top:1px solid #E2E5EC}}.big svg{{width:180px;height:180px;display:block}}
.side{{display:grid;gap:10px}}.lk svg{{display:block;height:64px;width:auto}}.sm{{display:flex;gap:16px;align-items:flex-end}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5A6070}}
.side h2{{font:600 15px sans-serif;margin:0}}.side p{{margin:0;color:#5A6070;font-size:13px;max-width:640px}}
</style></head><body><h1>Nabi · ronda 2 · fuera de la onda y el matraz</h1><p class="i">Nada derivado del logo madre: el símbolo sale de los objetos y la operación diaria de un laboratorio. Mantengo azul y pera para que siga siendo familia.</p>{rows}</body></html>""")
for k,(n,b,t) in C.items(): open(f'{k}.svg','w').write(svg(b))
print('ok')
