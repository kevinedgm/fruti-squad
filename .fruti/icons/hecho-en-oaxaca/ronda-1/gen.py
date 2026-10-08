# Sello «Hecho en Oaxaca»: tres conceptos inspirados en las marmotas de las calendas. Texto convertido a trazados (Bricolage Grotesque).
import sys, math, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
SRC=sys.argv[1]
TINTA='#2a1a12'; MANTA='#fffaf0'; MADERA='#b0773a'
PICADO=['#e4007c','#00a3a3','#f2b200','#f26419','#7b3fb3']   # rosa mexicano, turquesa, amarillo, naranja, morado
_c={}
def font(wght,wdth,opsz):
    k=(wght,wdth,opsz)
    if k not in _c:
        f=TTFont(SRC); instantiateVariableFont(f,{'wght':wght,'wdth':wdth,'opsz':opsz},inplace=True); p=f'/tmp/bg-{wght}-{wdth}-{opsz}.ttf'; f.save(p); _c[k]=(TTFont(p),p)
    return _c[k]
def shape(s,wght,wdth,opsz):
    f,p=font(wght,wdth,opsz); hf=hb.Font(hb.Face(hb.Blob.from_file_path(p))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    return f,[(f.getGlyphOrder()[i.codepoint],p_.x_advance) for i,p_ in zip(b.glyph_infos,b.glyph_positions)]
def texto(s,size,x0,y0,wght=760,wdth=85,opsz=24,track=0,anchor='start'):
    f,gl=shape(s,wght,wdth,opsz); upm=f['head'].unitsPerEm; k=size/upm; gs=f.getGlyphSet()
    W=sum(a for _,a in gl)*k+track*(len(gl)-1)
    x=x0-(W/2 if anchor=='middle' else 0); d=''
    for g,a in gl:
        pen=SVGPathPen(gs); gs[g].draw(TransformPen(pen,(k,0,0,-k,x,y0))); d+=pen.getCommands(); x+=a*k+track
    return d,W
def arco(s,size,cx,cy,r,centro_ang,wght=760,wdth=85,opsz=24,track=0,abajo=False):
    # texto sobre un círculo: arriba se lee en sentido horario; abajo, antihorario (para que no quede de cabeza)
    f,gl=shape(s,wght,wdth,opsz); upm=f['head'].unitsPerEm; k=size/upm; gs=f.getGlyphSet()
    W=sum(a for _,a in gl)*k+track*(len(gl)-1); ang_total=W/r
    a0=math.radians(centro_ang)-(ang_total/2 if not abajo else -ang_total/2); d=''; pos=0
    for g,a in gl:
        w=a*k; mid=pos+w/2
        th=a0+(mid/r if not abajo else -mid/r)
        x=cx+r*math.cos(th); y=cy+r*math.sin(th)
        rot=th+math.pi/2 if not abajo else th-math.pi/2
        c,s_=math.cos(rot),math.sin(rot)
        # glifo centrado en su avance, línea base sobre el círculo
        m=(k*c, k*s_, k*s_, -k*c, x - (w/2)*c, y - (w/2)*s_)
        pen=SVGPathPen(gs); gs[g].draw(TransformPen(pen,m)); d+=pen.getCommands(); pos+=w+track
    return d
def marmota(cx,cy,r,sw,banda=None,triangulos=True,discos=True,poste=0,tri_n=7):
    # esfera de manta con costillas (meridianos), banda opcional, papel picado arriba, discos y mástil
    out=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{MANTA}"/>'
    if triangulos:
        for i in range(tri_n):
            ang=math.radians(-150+i*(120/(tri_n-1))); rr=r*.62
            x=cx+rr*math.cos(ang); y=cy+rr*math.sin(ang)*.9-r*.05; t=r*.17
            out+=f'<path d="M{x-t:.2f} {y-t*.55:.2f}H{x+t:.2f}L{x:.2f} {y+t*.75:.2f}Z" fill="{PICADO[i%5]}"/>'
    rib=''.join(f'<ellipse cx="{cx}" cy="{cy}" rx="{r*f:.2f}" ry="{r}"/>' for f in (.38,.74))+f'<path d="M{cx} {cy-r}V{cy+r}"/>'
    out+=f'<g fill="none" stroke="{TINTA}" stroke-width="{sw*.55:.2f}" opacity=".55">{rib}</g>'
    if banda:
        y0,h,d=banda
        out+=f'<clipPath id="bc{cx}{cy}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath><rect clip-path="url(#bc{cx}{cy})" x="{cx-r}" y="{y0}" width="{2*r}" height="{h}" fill="{TINTA}"/><path fill="{MANTA}" d="{d}"/>'
    out+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{TINTA}" stroke-width="{sw}"/>'
    if discos:
        for yy in (cy-r, cy+r):
            out+=f'<ellipse cx="{cx}" cy="{yy}" rx="{r*.22:.2f}" ry="{r*.07:.2f}" fill="{MADERA}" stroke="{TINTA}" stroke-width="{sw*.6:.2f}"/>'
    if poste:
        out+=f'<path d="M{cx} {cy+r+r*.07}V{cy+r+poste}" stroke="{MADERA}" stroke-width="{sw*1.6:.2f}" stroke-linecap="round"/><path d="M{cx} {cy+r+r*.07}V{cy+r+poste}" stroke="{TINTA}" stroke-width="{sw*.5:.2f}" stroke-linecap="round" opacity=".35"/>'
    return out
def svg(w,h,body,label='Hecho en Oaxaca'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">{body}</svg>\n'
OUT={}
# A · marmota con banda: el texto va en la banda de la marmota, como en la calenda
d,_=texto('HECHO EN OAXACA',10.2,60,84.8,780,78,18,0.3,'middle')
d2,_=texto('MADE IN OAXACA',6.2,60,140,600,90,14,0.6,'middle')
OUT['a-banda']=svg(120,150,marmota(60,70,44,3.2,banda=(73.5,15,d),poste=0,tri_n=7)+f'<path d="M60 117V132" stroke="{MADERA}" stroke-width="5" stroke-linecap="round"/><path fill="{TINTA}" d="{d2}"/>')
# B · sello circular: texto alrededor, marmota pequeña al centro
ring=f'<circle cx="80" cy="80" r="76" fill="{MANTA}" stroke="{TINTA}" stroke-width="3.5"/><circle cx="80" cy="80" r="52" fill="none" stroke="{TINTA}" stroke-width="1.6"/>'
top=arco('HECHO EN OAXACA',15,80,80,59,-90,800,80,18,0.8)
bot=arco('MADE IN OAXACA',11,80,80,67,90,650,90,14,1.2,abajo=True)
dots=''.join(f'<circle cx="{80+63*math.cos(math.radians(a)):.2f}" cy="{80+63*math.sin(math.radians(a)):.2f}" r="2.6" fill="{PICADO[i]}"/>' for i,a in enumerate((180,0)))
OUT['b-sello']=svg(160,160,ring+f'<path fill="{TINTA}" d="{top}"/><path fill="{TINTA}" d="{bot}"/>'+dots+marmota(80,74,30,2.6,tri_n=5,poste=18))
# C · marca mínima + nombre: marmota reducida a lo esencial, legible a 16 px
mini=(f'<circle cx="20" cy="18" r="14" fill="{MANTA}" stroke="{TINTA}" stroke-width="2.6"/>'
      f'<ellipse cx="20" cy="18" rx="6" ry="14" fill="none" stroke="{TINTA}" stroke-width="1.6"/>'
      f'<path d="M14.5 10H25.5L20 17Z" fill="{PICADO[0]}"/>'
      f'<path d="M20 32.6V44" stroke="{MADERA}" stroke-width="4" stroke-linecap="round"/>')
dh,wh=texto('Hecho en',13,44,20,600,90,18,0)
do,wo=texto('Oaxaca',24,43,42,800,80,24,-0.2)
OUT['c-marca']=svg(46+max(wh,wo)+4,48,mini+f'<path fill="{TINTA}" d="{dh}"/><path fill="{TINTA}" d="{do}"/>')
OUT['c-icono']=svg(40,48,mini)
for k,s in OUT.items(): open(f'{k}.svg','w').write(s)
def r(f,h,style=''): return f'<span style="display:inline-flex;{style}">'+open(f).read().replace('<svg ',f'<svg height="{h}" ',1)+'</span>'
rows=''
for k,hs in (('a-banda',(150,90,48)),('b-sello',(160,96,48)),('c-marca',(96,48,28)),('c-icono',(48,32,20))):
    rows+=f'<section style="display:flex;gap:26px;align-items:flex-end;padding:16px 20px;border-bottom:1px solid #eadfce"><b style="width:80px;font:600 12px sans-serif;color:#7a6650">{k}</b>'+''.join(r(k+'.svg',h) for h in hs)+r(k+'.svg',hs[1],'padding:10px;background:#f26419;border-radius:10px')+r(k+'.svg',hs[1],'padding:10px;background:#1b1210;border-radius:10px')+'</section>'
open('banco.html','w').write(f'<html><body style="margin:0;background:#fbf5ea">{rows}</body></html>')
print('ok')
