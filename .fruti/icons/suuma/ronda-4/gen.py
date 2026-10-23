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
C={}
def build(uu_fn,name,desc,key):
    d_s,x=palabra('s',SIZE,0,Y); x+=gap*0.3
    uu,x2=uu_fn(x)
    d_ma,x3=palabra('ma',SIZE,x2+gap*0.3,Y)
    body=I(d_s)+uu+I(d_ma); C[key]=(name,body,desc,x3)
# A · Ligadura: las dos u comparten el tallo central, que cuelga y no llega al cuenco
def A(x):
    u1=U(x,spur=False); u2=U(x+uw-st)   # la segunda u arranca donde termina el tallo de la primera: se tocan
    return stroked(u1)+stroked(u2),x+2*uw-st
build(A,'Pegadas','Las dos u se tocan y forman una sola pieza sin fundirse: juntas, cada una entera.','A')
# B · Anidada: la segunda u, más chica, dentro del cuenco de la primera
def B(x):
    big=U(x,w=uw*1.35,spur=False); inner_w=uw*0.62; ix=x+(uw*1.35-inner_w)/2
    small=U(ix,top=Y-xh*0.62+st/2,depth=Y-st*1.25,spur=False,w=inner_w)
    return stroked(big)+stroked(small,w=st*0.78),x+uw*1.35
build(B,'Anidada','Una u dentro de la otra: la red contiene sin igualar. La palabra se acorta.','B')
# C · Hueca: la segunda u es contorno; la primera, maciza
def Cf(x):
    u1=U(x); u2=U(x+uw+gap*0.6)
    return stroked(u1)+f'<path d="{u2}" fill="none" stroke="{INK}" stroke-width="{st:.1f}" stroke-linecap="butt" stroke-linejoin="round"/>'.replace(f'stroke-width="{st:.1f}"',f'stroke-width="{st:.1f}" ') and (stroked(u1)+stroked(u2)+stroked(u2,w=st-2*2.6,c=BG)), x+2*uw+gap*0.6
build(Cf,'Hueca','Una u maciza y una u vaciada: el profesional y el lugar que le hace la plataforma.','C')
# D · Desnivel: la segunda u baja por debajo de la línea base
def D(x):
    u1=U(x); u2=U(x+uw+gap*0.6,depth=Y+xh*0.32)
    return stroked(u1)+stroked(u2),x+2*uw+gap*0.6
build(D,'Desnivel','La segunda u baja de la línea base: dos iguales a distinta altura, ninguna igual a la otra.','D')
# E · Gesto: las dos u son un trazo de pincel entre letras geométricas
sys.path.insert(0,'../ronda-3'); 
exec(open('../ronda-3/gen.py').read().split("def stroke(")[0].split("import random")[0].replace("INK='#1F1D1A'; BG='#FAF7F2'",""))
def E(x):
    top=Y-xh; w=uw*0.98
    def hu(x,seed):
        import random; rr=random.Random(seed); j=lambda a:a+rr.uniform(-1.6,1.6)
        pts=[(j(x+st*0.5),j(top+st*0.2)),(j(x+st*0.5),j(Y-r*1.2)),(j(x+w*0.5),j(Y+st*0.25)),(j(x+w-st*0.5),j(Y-r*1.2)),(j(x+w-st*0.5),j(top+st*0.1)),(j(x+w-st*0.45),j(Y-st*0.1))]
        return I(brush(pts,lambda t:st*0.5*(0.6+0.4*math.sin(math.pi*(0.1+0.8*t))**0.6),n=200))
    return hu(x,4)+hu(x+w+gap*0.5,9),x+2*w+gap*0.5
build(E,'Gesto','Las dos u van a pincel, cada una con su mano, entre letras geométricas: la persona dentro del sistema.','E')
W=max(v[3] for v in C.values())+8
def svg(body,w=None,h=None): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 20 {W:.0f} 130" width="{w or W:.0f}" height="{h or 130}">{body}</svg>'
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:{BG};color:{INK};font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 20px;color:#5B5750}}
.g{{display:grid;grid-template-columns:1fr 1fr;gap:18px 40px}}.c{{display:grid;grid-template-columns:1fr auto;gap:6px 24px;align-items:center;padding:14px 0;border-top:1px solid #E6E1D8}}
.big svg{{width:420px;height:auto;display:block}}.sm{{display:flex;gap:18px;align-items:flex-end}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5B5750}}
.c h2{{font:600 16px sans-serif;margin:0}}.c p{{margin:0;color:#5B5750;font-size:13px;grid-column:1/-1}}
</style></head><body><h1>SUUMA · ronda 4 · tipográfico con giro</h1><p class="i">Manrope 700 para s, m, a; la doble U construida a mano y es la que hace el truco. Cada una a 420 px y a 80 px de ancho.</p><div class="g">"""+''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="sm"><span>{svg(b,80,int(80*130/W))}80 px</span><span>{svg(b,140,int(140*130/W))}140</span></div><h2>{k} · {n}</h2><p>{t}</p></div>' for k,(n,b,t,_) in C.items())+'</div></body></html>')
for k,(n,b,t,_) in C.items(): open(f'{k}.svg','w').write(svg(b))
print('ok',round(xh,1),round(st,1),round(uw,1))
