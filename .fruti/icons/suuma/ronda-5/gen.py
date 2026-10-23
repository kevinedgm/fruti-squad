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

C={}; SYM={}
def nested(x,W=1.35,iw=0.62,itop=0.62,idepth=1.25,isw=0.78,dx=0,fill=False,outer_sw=1.0):
    bw=uw*W; big=U(x,w=bw,spur=False); inner_w=uw*iw; ix=x+(bw-inner_w)/2+dx
    small=U(ix,top=Y-xh*itop+st/2,depth=Y-st*idepth,spur=False,w=inner_w)
    s=stroked(big,w=st*outer_sw)
    if fill:
        rr=inner_w/2; yb=Y-st*idepth; top=Y-xh*itop
        s+=I(f'M{ix:.1f} {top:.1f} H{ix+inner_w:.1f} V{yb-rr:.1f} A{rr:.1f} {rr:.1f} 0 0 1 {ix:.1f} {yb-rr:.1f}Z')
    else: s+=stroked(small,w=st*isw)
    return s,x+bw
def build(key,name,desc,**kw):
    d_s,x=palabra('s',SIZE,0,Y); x+=gap*0.3
    uu,x2=nested(x,**kw)
    d_ma,x3=palabra('ma',SIZE,x2+gap*0.3,Y)
    C[key]=(name,I(d_s)+uu+I(d_ma),desc,x3); SYM[key]=(nested(0,**kw)[0],nested(0,**kw)[1])
build('B1','Centrada','La de la ronda 4: u interior más fina, centrada.')
build('B2','Mismo peso','La u interior con el mismo grosor y más chica, apoyada en el cuenco.',iw=0.5,itop=0.5,idepth=1.15,isw=1.0)
build('B3','Descentrada','La u interior se corre a la derecha: cada quien en su sitio, no en el centro.',dx=st*0.9,iw=0.55,itop=0.58,isw=0.85)
build('B4','Llena','La u interior es maciza: una pieza que ocupa su lugar dentro de la red.',iw=0.42,itop=0.46,idepth=1.3,isw=1.0,fill=True)
build('B5','Cuenco ancho','La u exterior se abre más: contenedor claro, interior normal.',W=1.6,iw=0.62,itop=0.62,idepth=1.25,isw=0.85)
W=max(v[3] for v in C.values())+8
def svg(body,w=None,h=None): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 20 {W:.0f} 130" width="{w or W:.0f}" height="{h or 130}">{body}</svg>'
def sym(key,size,inv=False):
    b,w=SYM[key]; pad=12; vb=f'{-pad} {Y-xh-pad} {w+2*pad:.0f} {xh+2*pad:.0f}'
    if inv: b=b.replace(INK,'@@').replace(BG,INK).replace('@@',BG)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{size}" height="{size}" preserveAspectRatio="xMidYMid meet">{b}</svg>'
def app(key,size):
    b,w=SYM[key]; b=b.replace(INK,'@@').replace(BG,INK).replace('@@',BG); pad=w*0.22; vb=f'{-pad} {Y-xh-pad-(w-xh)/2 if w>xh else Y-xh-pad} {w+2*pad:.0f} {w+2*pad:.0f}'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{size}" height="{size}"><rect x="{-pad}" y="{Y-xh-pad-(w-xh)/2}" width="{w+2*pad:.0f}" height="{w+2*pad:.0f}" rx="{(w+2*pad)*0.22:.0f}" fill="{INK}"/>{b}</svg>'
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:{BG};color:{INK};font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 20px;color:#5B5750}}
.c{{display:grid;grid-template-columns:440px 1fr;gap:6px 36px;align-items:center;padding:16px 0;border-top:1px solid #E6E1D8}}
.big svg{{width:440px;height:auto;display:block}}.sm{{display:flex;gap:18px;align-items:flex-end;flex-wrap:wrap}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5B5750}}
.c h2{{font:600 16px sans-serif;margin:0}}.c p{{margin:0;color:#5B5750;font-size:13px}}
</style></head><body><h1>SUUMA · ronda 5 · desarrollo de B (Anidada)</h1><p class="i">Cinco variaciones del encaje. A la derecha: la «uu» sola como símbolo a 16, 32 y 64 px, y como icono de app.</p>"""+''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="sm"><span>{svg(b,80,int(80*130/W))}80 px</span><span>{sym(k,16)}16</span><span>{sym(k,32)}32</span><span>{sym(k,64)}64</span><span>{app(k,64)}app</span></div><h2>{k} · {n}</h2><p>{t}</p></div>' for k,(n,b,t,_) in C.items())+'</body></html>')
for k,(n,b,t,_) in C.items(): open(f'{k}.svg','w').write(svg(b)); open(f'{k}-simbolo.svg','w').write(sym(k,128))
print('ok')
