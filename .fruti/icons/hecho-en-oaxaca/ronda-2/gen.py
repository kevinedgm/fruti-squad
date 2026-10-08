# Hecho en Oaxaca · ronda 2: abstracciones de la marmota (giro, la O, papel picado).
import sys, math, random
sys.path.insert(0,'../ronda-1'); sys.argv=[sys.argv[0],sys.argv[1]]
import importlib.util
spec=importlib.util.spec_from_file_location('r1','../ronda-1/gen.py')
SRC=sys.argv[1]
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
TINTA='#1a1210'; MANTA='#fff8ee'; ROSA='#e4007c'
PICADO=['#e4007c','#00a3a3','#f2b200','#f26419','#7b3fb3']
_c={}
def fnt(w,wd,op):
    k=(w,wd,op)
    if k not in _c:
        f=TTFont(SRC); instantiateVariableFont(f,{'wght':w,'wdth':wd,'opsz':op},inplace=True); p=f'/tmp/bg2-{w}-{wd}-{op}.ttf'; f.save(p); _c[k]=(TTFont(p),p)
    return _c[k]
def texto(s,size,x0,y0,w=800,wd=78,op=48,track=0):
    f,p=fnt(w,wd,op); hf=hb.Font(hb.Face(hb.Blob.from_file_path(p))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    gs=f.getGlyphSet(); order=f.getGlyphOrder(); k=size/f['head'].unitsPerEm; x=x0; d=''
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        pen=SVGPathPen(gs); gs[order[i.codepoint]].draw(TransformPen(pen,(k,0,0,-k,x,y0))); d+=pen.getCommands(); x+=ps.x_advance*k+track
    return d,x-x0-track
def metr(w=800,wd=78,op=48):
    f,_=fnt(w,wd,op); upm=f['head'].unitsPerEm; return f['OS/2'].sCapHeight/upm, f['OS/2'].sxHeight/upm
def svg(w,h,body,extra='',label='Hecho en Oaxaca'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" role="img" aria-label="{label}">{extra}{body}</svg>\n'
OUT={}
# ---------- K · esfera cinética: husos entre meridianos (12 costillas) que giran
def gajos(cx,cy,R,rot_deg,colores,id_='k'):
    out=''
    for k in range(-1,13):
        a=math.radians(k*15+rot_deg-90); b=math.radians((k+1)*15+rot_deg-90)
        a=max(a,-math.pi/2); b=min(b,math.pi/2)
        if b<=a: continue
        xa,xb=R*math.sin(a),R*math.sin(b)
        sa=1 if xa>=0 else 0; sb=0 if xb>=0 else 1
        d=(f'M{cx} {cy-R}A{abs(xa):.3f} {R} 0 0 {sa} {cx} {cy+R}'
           f'A{abs(xb):.3f} {R} 0 0 {sb} {cx} {cy-R}Z')
        out+=f'<path d="{d}" fill="{colores[(k)%len(colores)]}"/>'
    return out
K_COL=[ROSA,MANTA,'#00a3a3',MANTA,'#f2b200',MANTA,'#7b3fb3',MANTA,'#f26419',MANTA,ROSA,MANTA]
def kinetica(cx,cy,R,anim=False):
    frames=''
    body=f'<clipPath id="kc"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath><g clip-path="url(#kc)">'
    if anim:
        # giro continuo: 30° (dos husos) por ciclo, en bucle; con reduce, quieto
        n=12
        for i in range(n):
            body+=f'<g class="f" style="animation-delay:{-i*1400/n:.0f}ms">{gajos(cx,cy,R,i*30/n,K_COL)}</g>'
    else:
        body+=gajos(cx,cy,R,7.5,K_COL)
    body+='</g>'
    body+=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{TINTA}" stroke-width="{R*.06:.2f}"/>'
    body+=f'<path d="M{cx} {cy+R}V{cy+R*1.55:.2f}" stroke="{TINTA}" stroke-width="{R*.11:.2f}" stroke-linecap="round"/>'
    return body
dh,wh=texto('HECHO EN',22,128,58,800,78,48,1.2); do,wo=texto('OAXACA',46,126,104,850,75,48,0.5)
OUT['k-cinetica']=svg(132+max(wh,wo),130,kinetica(54,56,44)+f'<path fill="{TINTA}" d="{dh}"/><path fill="{ROSA}" d="{do}"/>')
css='<style>.f{opacity:0;animation:fr 1400ms steps(1,end) infinite}@keyframes fr{0%{opacity:1}8.333%{opacity:0}100%{opacity:0}}@media (prefers-reduced-motion:reduce){.f{animation:none}.f:first-child{opacity:1}}</style>'
OUT['k-cinetica-animada']=svg(108,112,kinetica(54,48,44,anim=True),css)
OUT['k-icono']=svg(108,112,kinetica(54,48,44))
# ---------- O · la O de Oaxaca es la marmota
cap,xh=metr(850,75,48); size=96
d1,w1=texto('axaca',size,0,0,850,75,48,0.5)
f,_=fnt(850,75,48); bp=BoundsPen(f.getGlyphSet()); f.getGlyphSet()['l'].draw(bp); stem=(bp.bounds[2]-bp.bounds[0])*size/f['head'].unitsPerEm if bp.bounds else size*.12
H=cap*size; R=H/2; sw=max(stem*.95,size*.11)
x0=12; cxo=x0+R; base=120
o=(f'<circle cx="{cxo:.2f}" cy="{base-R:.2f}" r="{R-sw/2:.2f}" fill="none" stroke="{TINTA}" stroke-width="{sw:.2f}"/>'
   f'<ellipse cx="{cxo:.2f}" cy="{base-R:.2f}" rx="{(R-sw/2)*.42:.2f}" ry="{R-sw/2:.2f}" fill="none" stroke="{ROSA}" stroke-width="{sw*.42:.2f}"/>'
   f'<path d="M{cxo:.2f} {base-sw*.2:.2f}V{base+size*.24:.2f}" stroke="{TINTA}" stroke-width="{sw*.7:.2f}" stroke-linecap="round"/>')
d1,w1=texto('axaca',size,cxo+R+2,base,850,75,48,0.5)
dh,wh=texto('HECHO EN',24,x0+2,base-H-14,800,78,48,1.6)
OUT['o-marmota']=svg(cxo+R+2+w1+10,base+size*.24+12,o+f'<path fill="{TINTA}" d="{d1}"/><path fill="{ROSA}" d="{dh}"/>')
OUT['o-icono']=svg(2*R+20,base+size*.24+12-(base-H-14)+4,o.replace(f'{cxo:.2f}',f'{R+10:.2f}'),'') if False else None
# icono O suelto
ox=R+8; oy=R+8
OUT['o-icono']=svg(2*R+16,2*R+16+size*.24,(f'<circle cx="{ox:.2f}" cy="{oy:.2f}" r="{R-sw/2:.2f}" fill="none" stroke="{TINTA}" stroke-width="{sw:.2f}"/>'
   f'<ellipse cx="{ox:.2f}" cy="{oy:.2f}" rx="{(R-sw/2)*.42:.2f}" ry="{R-sw/2:.2f}" fill="none" stroke="{ROSA}" stroke-width="{sw*.42:.2f}"/>'
   f'<path d="M{ox:.2f} {oy+R-sw*.2:.2f}V{oy+R+size*.24:.2f}" stroke="{TINTA}" stroke-width="{sw*.7:.2f}" stroke-linecap="round"/>'))
# ---------- T · papel picado: círculo hecho solo de triángulos recortados
def picado(cx,cy,R,s,gap,seed=7):
    random.seed(seed); h=s*math.sqrt(3)/2; out=f'<clipPath id="tc"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath><g clip-path="url(#tc)">'
    rows=int(2*R/h)+3; cols=int(2*R/s)+3
    for j in range(-1,rows):
        for i in range(-1,cols*2):
            x=cx-R-s+i*s/2; y=cy-R-h+j*h; up=(i+j)%2==0
            pts=[(x,y+h),(x+s/2,y),(x+s,y+h)] if up else [(x,y),(x+s,y),(x+s/2,y+h)]
            gx=sum(p[0] for p in pts)/3; gy=sum(p[1] for p in pts)/3
            if math.hypot(gx-cx,gy-cy)>R+s*.2: continue
            k=1-gap/s*1.7; pts=[(gx+(p[0]-gx)*k,gy+(p[1]-gy)*k) for p in pts]
            c=random.choice(PICADO+[MANTA,MANTA])
            out+=f'<path d="M'+'L'.join('%.2f %.2f'%p for p in pts)+f'Z" fill="{c}"/>'
    return out+'</g>'
T=picado(54,50,44,15,1.6)+f'<path d="M54 94V118" stroke="{TINTA}" stroke-width="5" stroke-linecap="round"/>'
dh,wh=texto('HECHO EN',22,124,58,800,78,48,1.2); do,wo=texto('OAXACA',46,122,104,850,75,48,0.5)
OUT['t-picado']=svg(128+max(wh,wo),124,f'<rect width="100%" height="100%" fill="{TINTA}"/>'+T+f'<path d="M54 94V118" stroke="{MANTA}" stroke-width="5" stroke-linecap="round"/><path fill="{MANTA}" d="{dh}"/><path fill="{PICADO[2]}" d="{do}"/>')
OUT['t-icono']=svg(108,124,T)
for k,s in OUT.items():
    if s: open(f'{k}.svg','w').write(s)
def r(f,h,style=''): return f'<span style="display:inline-flex;{style}">'+open(f).read().replace('<svg ',f'<svg height="{h}" ',1)+'</span>'
rows=''
for k,ic in (('k-cinetica','k-icono'),('o-marmota','o-icono'),('t-picado','t-icono')):
    rows+=(f'<section style="display:flex;gap:24px;align-items:center;padding:16px 20px;border-bottom:1px solid #eadfce;flex-wrap:wrap"><b style="width:90px;font:600 12px sans-serif;color:#7a6650">{k}</b>'
           +r(k+'.svg',110)+r(k+'.svg',48)+r(ic+'.svg',64)+r(ic+'.svg',32)+r(ic+'.svg',20)+'</section>')
open('banco.html','w').write(f'<html><body style="margin:0;background:#fbf5ea">{rows}</body></html>')
print('ok')
