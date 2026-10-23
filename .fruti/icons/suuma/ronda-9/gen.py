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

def arc(cx,cy,rx,ry,a0,a1,n=40):
    return [(cx+rx*math.cos(math.radians(a0+(a1-a0)*i/n)),cy+ry*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]; c=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in c]; return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def cr(a,b): la,lb=lum(a),lum(b); return round((max(la,lb)+0.05)/(min(la,lb)+0.05),1)
# S3 afinada: sonrisa un poco más ancha, ojos algo más separados
def S3(x,ink,eye,smile,bgc):
    bw=uw*1.35; s=stroked(U(x,w=bw,spur=False),c=ink); inner_w=uw*0.62; ix=x+(bw-inner_w)/2
    s+=stroked(U(ix,top=Y-xh*0.62+st/2,depth=Y-st*1.25,spur=False,w=inner_w),w=st*0.78,c=smile)
    return s,x+bw
def word(ink,eye,smile,bgc):
    d_s,x=palabra('s',SIZE,0,Y); x+=gap*0.3; uu,x2=S3(x,ink,eye,smile,bgc); d_ma,x3=palabra('ma',SIZE,x2+gap*0.3,Y)
    return I(d_s,ink)+uu+I(d_ma,ink),x3
PAL={
 'Q1':('Esmeralda y mandarina',dict(verde='#0F8A5F',tierra='#121212',neutro='#FFFFFF',contraste='#FF6A2B',tinta='#121212',oscuro='#121212')),
 'Q2':('Cobalto y mandarina',dict(verde='#1F3BE0',tierra='#121212',neutro='#FFFFFF',contraste='#FF6A2B',tinta='#121212',oscuro='#121212')),
 'Q3':('Ciruela y coral',dict(verde='#5A2A86',tierra='#121212',neutro='#FFFFFF',contraste='#FF5A4E',tinta='#121212',oscuro='#121212')),
 'Q4':('Petróleo y ámbar',dict(verde='#0E6E7A',tierra='#121212',neutro='#FFFFFF',contraste='#F5A623',tinta='#121212',oscuro='#121212')),
}
rows=''
for k,(name,c) in PAL.items():
    wm,x3=word(c['tinta'],c['verde'],c['verde'],c['neutro']); W=x3+8
    svgw=lambda body,bg,w=300: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 20 {W:.0f} 130" width="{w}" style="background:{bg};border-radius:10px;padding:14px 18px;box-sizing:content-box">{body}</svg>'
    wm_d,_=word(c['neutro'],c['verde'] if cr(c['verde'],c['oscuro'])>=3 else c['contraste'],c['contraste'],c['oscuro'])
    def app(bg,glyph,eye,smile,size=96):
        b,w=S3(0,glyph,eye,smile,bg); pad=w*0.22; side=w+2*pad; y0=Y-xh-pad-(w-xh)/2
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {y0} {side:.0f} {side:.0f}" width="{size}" height="{size}"><rect x="{-pad}" y="{y0}" width="{side:.0f}" height="{side:.0f}" rx="{side*0.22:.0f}" fill="{bg}"/>{b}</svg>'
    sw=''.join(f'<i style="background:{v}" title="{n} {v}"></i>' for n,v in c.items())
    checks=f"tinta/neutro {cr(c['tinta'],c['neutro'])} · verde/neutro {cr(c['verde'],c['neutro'])} · contraste/neutro {cr(c['contraste'],c['neutro'])} · neutro/verde {cr(c['neutro'],c['verde'])} · contraste/verde {cr(c['contraste'],c['verde'])} · neutro/tinta {cr(c['neutro'],c['tinta'])} · contraste/tinta {cr(c['contraste'],c['tinta'])}"
    rows+=f'<div class="c"><h2>{k} · {name}</h2><div class="sw">{sw}</div><div class="row">{svgw(wm,c["neutro"])}{svgw(wm_d,c["oscuro"])}{app(c["verde"],c["neutro"],c["neutro"],c["contraste"])}{app(c["neutro"],c["tinta"],c["verde"],c["contraste"])}{app(c["tierra"],c["neutro"],c["neutro"],c["contraste"])}</div><p>{checks}</p></div>'
    open(f'{k}.svg','w').write(svgw(wm,c['neutro'],W))
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#FFFFFF;color:#1F1D1A;font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 20px;color:#5B5750}}
.c{{padding:18px 0;border-top:1px solid #E6E1D8;display:grid;gap:10px}}.c h2{{font:600 16px sans-serif;margin:0}}.sw{{display:flex;gap:6px}}.sw i{{display:block;width:40px;height:22px;border-radius:5px;border:1px solid rgba(0,0,0,.08)}}
.row{{display:flex;gap:18px;align-items:center;flex-wrap:wrap}}.c p{{margin:0;color:#5B5750;font-size:12px}}
</style></head><body><h1>SUUMA · ronda 9 · B1 en color vivo y editorial</h1><p class="i">Blanco y tinta como base editorial; un cromático intenso (marca, acciones) y un acento en la u interior. Por fila: wordmark en claro y oscuro; icono sobre el cromático, sobre blanco y sobre tinta. Debajo, contrastes WCAG (texto 4.5, componentes 3).</p>{rows}</body></html>""")
print('ok')
