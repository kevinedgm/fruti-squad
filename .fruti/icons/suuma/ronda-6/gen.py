import os,sys,math
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import uharfbuzz as hb
S=sys.argv[1]; INK='#1F1D1A'; BG='#FAF7F2'
src=S+'/fuentes/Manrope[wght].ttf'; inst='/tmp/suuma-manrope700.ttf'
if not os.path.exists(inst): instancer.instantiateVariableFont(TTFont(src),{'wght':700}).save(inst)
FONT=TTFont(inst); UPM=FONT['head'].unitsPerEm; XH=FONT['OS/2'].sxHeight; GS=FONT.getGlyphSet()
bp=BoundsPen(GS); GS['l'].draw(bp); STEM=bp.bounds[2]-bp.bounds[0]
bp=BoundsPen(GS); GS['u'].draw(bp); UW=bp.bounds[2]-bp.bounds[0]
def palabra(s,size,x0,y0,track=0):
    hf=hb.Font(hb.Face(hb.Blob.from_file_path(inst))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    order=FONT.getGlyphOrder(); k=size/UPM; x=x0; d=''
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        g=GS[order[i.codepoint]]; pen=SVGPathPen(GS); g.draw(TransformPen(pen,(k,0,0,-k,x,y0))); d+=pen.getCommands(); x+=ps.x_advance*k+track
    return d,x
SIZE=120; Y=110; k=SIZE/UPM; xh=XH*k; st=STEM*k; uw=UW*k; r=uw/2-st/2  # radio del cuenco (línea central)
def U(x,depth=None,spur=True,top=None,w=None):
    """u como trazo de línea central, grosor st, cuenco redondo"""
    w=w or uw; rr=w/2-st/2; top=Y-xh+st/2 if top is None else top; yb=(depth or Y)-st/2
    x0=x+st/2; x1=x+w-st/2
    d=f'M{x0:.1f} {top:.1f} V{yb-rr:.1f} A{rr:.1f} {rr:.1f} 0 0 0 {x1:.1f} {yb-rr:.1f} V{top:.1f}'
    if spur: d+=f' M{x1:.1f} {top:.1f} V{yb:.1f}'
    return d
def stroked(d,w=None,c=None): return f'<path d="{d}" fill="none" stroke="{c or INK}" stroke-width="{w or st:.1f}" stroke-linecap="butt" stroke-linejoin="round"/>'
I=lambda d,f=None:f'<path d="{d}" fill="{f or INK}"/>'
gap=st*0.9  # espacio entre letras


exec(open('../ronda-3/gen.py').read().split('def stroke(')[0].split('import random')[0].replace("INK='#1F1D1A'; BG='#FAF7F2'",''))
P=lambda x,y,r=6,f=None:f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{f or INK}"/>'
C={}; SYM={}
def outer(x,W=1.35): return stroked(U(x,w=uw*W,spur=False)),uw*W
def arc(cx,cy,rx,ry,a0,a1,n=40):
    pts=[(cx+rx*math.cos(math.radians(a0+(a1-a0)*i/n)),cy+ry*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    return pts
def S1(x):  # sonrisa de línea: arco ancho y poco profundo, extremos afinados (pincel)
    s,bw=outer(x); cx=x+bw/2; cy=Y-xh*0.66; pts=arc(cx,cy,bw*0.27,xh*0.24,20,160)
    return s+I(brush(pts,lambda t:st*0.42*(0.35+0.65*math.sin(math.pi*t)**0.7),n=90)),x+bw
def S2(x):  # sonrisa maciza: media luna (B4 hecha sonrisa)
    s,bw=outer(x); cx=x+bw/2; cy=Y-xh*0.66; rx=bw*0.27
    d='M'+' L'.join(f'{px:.1f} {py:.1f}' for px,py in arc(cx,cy,rx,xh*0.26,10,170))+' '+' L'.join(f'{px:.1f} {py:.1f}' for px,py in arc(cx,cy,rx,xh*0.06,170,10))+'Z'
    return s+I(d),x+bw
def S3(x):  # sonrisa de línea + dos puntos: la carita completa (límite)
    s,bw=outer(x); cx=x+bw/2; cy=Y-xh*0.62; pts=arc(cx,cy,bw*0.24,xh*0.20,20,160)
    return s+I(brush(pts,lambda t:st*0.40*(0.4+0.6*math.sin(math.pi*t)**0.7),n=90))+P(cx-bw*0.17,Y-xh*0.78,st*0.30)+P(cx+bw*0.17,Y-xh*0.78,st*0.30),x+bw
def S4(x):  # sonrisa como u chica con comisuras: la u interior de B1 con los extremos abiertos hacia fuera
    s,bw=outer(x); cx=x+bw/2; cy=Y-xh*0.70; pts=[(cx-bw*0.28,cy-xh*0.06),(cx-bw*0.24,cy+xh*0.14),(cx,cy+xh*0.24),(cx+bw*0.24,cy+xh*0.14),(cx+bw*0.28,cy-xh*0.06)]
    return s+I(brush(pts,lambda t:st*0.40*(0.5+0.5*math.sin(math.pi*t)**0.6),n=120)),x+bw
def S5(x):  # sonrisa maciza asimétrica: media luna más gruesa a la derecha (gesto, no icono)
    s,bw=outer(x); cx=x+bw/2; cy=Y-xh*0.66; rx=bw*0.27
    up=arc(cx,cy,rx,xh*0.26,10,170); lo=arc(cx,cy,rx,xh*0.06,170,10)
    lo=[(px,py-xh*0.07*math.sin(math.radians(170-(160*i/len(lo))))*(1 if px>cx else 0)) for i,(px,py) in enumerate(lo)]
    d='M'+' L'.join(f'{px:.1f} {py:.1f}' for px,py in up)+' '+' L'.join(f'{px:.1f} {py:.1f}' for px,py in lo)+'Z'
    return s+I(d),x+bw
def build(key,name,desc,fn):
    d_s,x=palabra('s',SIZE,0,Y); x+=gap*0.3
    uu,x2=fn(x)
    d_ma,x3=palabra('ma',SIZE,x2+gap*0.3,Y)
    C[key]=(name,I(d_s)+uu+I(d_ma),desc,x3); SYM[key]=fn(0)
build('S1','Línea','Sonrisa de línea con extremos afinados, como un trazo de pincel. La B1 hecha sonrisa.',S1)
build('S2','Maciza','Media luna llena: la B4 hecha sonrisa. La más sólida a 16 px.',S2)
build('S3','Con ojos','La misma sonrisa con dos puntos: carita completa. Es el límite que el brief pide evitar; la muestro para decidir con ella a la vista.',S3)
build('S4','Comisuras','Una u chica que abre las puntas hacia fuera: sonríe sin dejar de ser u.',S4)
build('S5','Asimétrica','Media luna más gruesa de un lado: un gesto, no un emoji.',S5)
W=max(v[3] for v in C.values())+8
def svg(body,w=None,h=None): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 20 {W:.0f} 130" width="{w or W:.0f}" height="{h or 130}">{body}</svg>'
def sym(key,size):
    b,w=SYM[key]; pad=12; vb=f'{-pad} {Y-xh-pad} {w+2*pad:.0f} {xh+2*pad:.0f}'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{size}" height="{size}" preserveAspectRatio="xMidYMid meet">{b}</svg>'
def app(key,size):
    b,w=SYM[key]; b=b.replace(INK,'@@').replace(BG,INK).replace('@@',BG); pad=w*0.22; side=w+2*pad; y0=Y-xh-pad-(w-xh)/2
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {y0} {side:.0f} {side:.0f}" width="{size}" height="{size}"><rect x="{-pad}" y="{y0}" width="{side:.0f}" height="{side:.0f}" rx="{side*0.22:.0f}" fill="{INK}"/>{b}</svg>'
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:{BG};color:{INK};font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 20px;color:#5B5750}}
.c{{display:grid;grid-template-columns:440px 1fr;gap:6px 36px;align-items:center;padding:16px 0;border-top:1px solid #E6E1D8}}
.big svg{{width:440px;height:auto;display:block}}.sm{{display:flex;gap:18px;align-items:flex-end;flex-wrap:wrap}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5B5750}}
.c h2{{font:600 16px sans-serif;margin:0}}.c p{{margin:0;color:#5B5750;font-size:13px}}
</style></head><body><h1>SUUMA · ronda 6 · la u interior como sonrisa</h1><p class="i">Cinco sonrisas dentro de la u. A la derecha: el símbolo solo a 16, 32 y 64 px y como icono de app.</p>"""+''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="sm"><span>{svg(b,80,int(80*130/W))}80 px</span><span>{sym(k,16)}16</span><span>{sym(k,32)}32</span><span>{sym(k,64)}64</span><span>{app(k,64)}app</span></div><h2>{k} · {n}</h2><p>{t}</p></div>' for k,(n,b,t,_) in C.items())+'</body></html>')
for k,(n,b,t,_) in C.items(): open(f'{k}.svg','w').write(svg(b)); open(f'{k}-simbolo.svg','w').write(sym(k,128))
print('ok')
