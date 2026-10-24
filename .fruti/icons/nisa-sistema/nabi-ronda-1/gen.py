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
# A · Onda: una sola onda del laboratorio hace la «n»; el punto pera es la i
W=[(14,104),(20,64),(34,36),(50,34),(64,62),(78,92),(94,96),(106,74),(112,44)]
C['A']=('Onda',I(stroke(W,9.5,lo=0.04,hi=0.96))+P(114,22,8),'Una sola de las dos ondas del laboratorio: Nisa Nabani son dos, Nabi es una. El punto pera es la i.')
# B · Matraz: el matraz del logo, simplificado, con la onda como superficie del líquido
flask='M48 14 H80 M54 14 V46 L24 104 Q20 114 32 114 H96 Q108 114 104 104 L74 46 V14'
liq='M36 82 C46 74 56 74 64 82 C72 90 82 90 92 82 L102 104 Q106 112 96 112 H32 Q22 112 26 104Z'
C['B']=('Matraz',I(liq,PERA)+O(flask,7),'El matraz del logo madre, reducido a contorno, con la onda como superficie del líquido.')
# C · Ligadura nb: la pierna derecha de la n es el asta de la b
nb='M22 110 V54 M22 70 C22 52 58 48 62 66 V110 M62 16 V110 M62 76 C64 56 104 54 104 82 C104 110 64 112 62 92'
C['C']=('Ligadura nb',O(nb,11)+P(110,24,8),'La pierna de la n es el asta de la b: «na-bi» en una pieza. El punto pera es la i.')
# D · Muestras: la onda lleva tres muestras que crecen; el lote avanza
pts=catmull(W,n=140)
C['D']=('Muestras',I(even(W,5.5))+P(*pts[18],7)+P(*pts[70],9.5)+P(*pts[128],12),'La onda como línea de proceso y tres muestras que crecen a lo largo de ella: del lote al certificado.')
# E · Hija: la onda grande en azul y una menor en pera que nace dentro de ella
W2=[(46,108),(52,86),(62,74),(72,78),(80,94),(90,104),(100,98),(106,84)]
C['E']=('Hija',I(stroke(W,9,lo=0.04,hi=0.96))+I(stroke(W2,6,lo=0.05,hi=0.95),PERA),'La onda azul del laboratorio y una pequeña en pera que nace en su cuenco: la familia, sin repetir el logo.')
def svg(b,size=128): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}">{b}</svg>'
def inv(b): return b.replace(f'"{INK}"','"@@"').replace('"@@"','"#FFFFFF"')
def app(b,size=72): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20 -20 168 168" width="{size}" height="{size}"><rect x="-20" y="-20" width="168" height="168" rx="38" fill="{INK}"/>{inv(b)}</svg>'
def lockup(b):
    d,x=palabra('nabi',92,150,100,track=-1)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {x+10:.0f} 128" height="64">{b}<path d="{d}" fill="{INK}"/></svg>'
rows=''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="side"><div class="lk">{lockup(b)}</div><div class="sm"><span>{svg(b,16)}16</span><span>{svg(b,32)}32</span><span>{app(b)}app</span></div><h2>{k} · {n}</h2><p>{t}</p></div></div>' for k,(n,b,t) in C.items())
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#fff;color:#1B1F2B;font:14px/1.45 sans-serif;padding:32px}}h1{{font:700 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 16px;color:#5A6070;max-width:900px}}
.c{{display:grid;grid-template-columns:180px 1fr;gap:28px;align-items:center;padding:18px 0;border-top:1px solid #E2E5EC}}.big svg{{width:180px;height:180px;display:block}}
.side{{display:grid;gap:10px}}.lk svg{{display:block;height:64px;width:auto}}.sm{{display:flex;gap:16px;align-items:flex-end}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5A6070}}
.side h2{{font:600 15px sans-serif;margin:0}}.side p{{margin:0;color:#5A6070;font-size:13px;max-width:640px}}
</style></head><body><h1>Nabi · ronda 1 · símbolo</h1><p class="i">Marca de familia de Nisa Nabani: azul real y pera del laboratorio, wordmark «nabi» en grotesca ancha como la del logo madre. Cada idea con su lockup, a 32 y 16 px y como icono de app.</p>{rows}</body></html>""")
for k,(n,b,t) in C.items(): open(f'{k}.svg','w').write(svg(b))
print('ok')
