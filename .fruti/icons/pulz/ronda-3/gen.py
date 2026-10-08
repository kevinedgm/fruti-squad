# PULZ · ronda 3: la Z del trasiego. Uso: python gen.py <Archivo[wdth,wght].ttf>
import sys, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
SRC=sys.argv[1]
C='var(--pulz-color,#b4582f)'; INK='currentColor'
def marca(uid,anim=False):
    # tanque de arriba (vacío al final), trasiego en diagonal, tanque de abajo con el lote ya llegado
    diag='38,21 56,21 26,43 8,43'
    b=(f'<rect x="8" y="9" width="48" height="12" rx="3" fill="{INK}"/>'
       f'<rect x="8" y="43" width="48" height="12" rx="3" fill="{INK}"/>')
    if not anim:
        b+=f'<polygon points="{diag}" fill="{C}"/><rect x="11.5" y="46.5" width="41" height="5" rx="2.5" fill="{C}"/>'
        return b
    b+=(f'<rect class="pz-arriba" x="11.5" y="12.5" width="41" height="5" rx="2.5" fill="{C}"/>'
        f'<clipPath id="d{uid}"><polygon points="{diag}"/></clipPath>'
        f'<path class="pz-trasiego" clip-path="url(#d{uid})" d="M50 19.5 14 44.5" pathLength="1" stroke="{C}" stroke-width="30" fill="none"/>'
        f'<rect class="pz-abajo" x="11.5" y="46.5" width="41" height="5" rx="2.5" fill="{C}"/>')
    return b
CSS=('<style>.pz-arriba,.pz-abajo{transform-box:fill-box}.pz-arriba{transform-origin:right center;animation:pz-vacia 700ms cubic-bezier(.5,0,.75,0) 500ms both}'
     '.pz-trasiego{stroke-dasharray:1 1.1;animation:pz-corre 700ms cubic-bezier(.4,0,.2,1) 900ms both}'
     '.pz-abajo{transform-origin:left center;animation:pz-llena 800ms cubic-bezier(.2,.8,.3,1) 1400ms both}'
     '@keyframes pz-vacia{from{transform:scaleX(1)}to{transform:scaleX(0)}}@keyframes pz-corre{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}@keyframes pz-llena{from{transform:scaleX(0)}to{transform:scaleX(1)}}'
     '@media (prefers-reduced-motion:reduce){.pz-arriba{animation:none;transform:scaleX(0)}.pz-trasiego,.pz-abajo{animation:none}}</style>')
def svg(w,h,body,oscuro=False,label='PULZ',style=''):
    col='#f4efe6' if oscuro else '#2a211c'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" role="img" aria-label="{label}" style="color:{col}">{style}{body}</svg>\n'
_c={}
def texto(s,size,x0,y0,w=820,wd=112,track=0):
    k=(w,wd)
    if k not in _c:
        f=TTFont(SRC); instantiateVariableFont(f,{'wght':w,'wdth':wd},inplace=True); p=f'/tmp/ar-{w}-{wd}.ttf'; f.save(p); _c[k]=(TTFont(p),p)
    f,p=_c[k]; hf=hb.Font(hb.Face(hb.Blob.from_file_path(p))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    gs=f.getGlyphSet(); order=f.getGlyphOrder(); kk=size/f['head'].unitsPerEm; x=x0; d=''
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        pen=SVGPathPen(gs); gs[order[i.codepoint]].draw(TransformPen(pen,(kk,0,0,-kk,x,y0))); d+=pen.getCommands(); x+=ps.x_advance*kk+track
    return d,x-x0-track, f['OS/2'].sCapHeight*kk
OUT={}
OUT['simbolo']=svg(64,64,marca('s')); OUT['simbolo-oscuro']=svg(64,64,marca('s'),True)
OUT['simbolo-animado']=svg(64,64,marca('a',True),style=CSS)
# wordmark: PUL + la Z-marca a la altura de las mayúsculas
d,w,cap=texto('PUL',64,0,64,820,112,1.5)
esc=cap/46
import re as _re
_n=[float(v) for v in _re.findall(r'-?\d+\.?\d*',d)]
_f,_p=_c[(820,112)]
from fontTools.pens.boundsPen import BoundsPen as _BP
_bp=_BP(_f.getGlyphSet()); _kk=64/_f['head'].unitsPerEm
_x=0
_hf=hb.Font(hb.Face(hb.Blob.from_file_path(_p))); _b=hb.Buffer(); _b.add_str('PUL'); _b.guess_segment_properties(); hb.shape(_hf,_b,{'kern':True})
for _i,_ps in zip(_b.glyph_infos,_b.glyph_positions):
    _f.getGlyphSet()[_f.getGlyphOrder()[_i.codepoint]].draw(TransformPen(_bp,(_kk,0,0,-_kk,_x,64))); _x+=_ps.x_advance*_kk+1.5
zx=_bp.bounds[2]+cap*0.24-8*esc

WM=lambda anim: f'<path fill="{INK}" d="{d}"/><g transform="translate({zx:.2f} {64-cap-9*esc:.2f}) scale({esc:.4f})">{marca("w"+str(anim),anim)}</g>'
W=zx+48*esc+2
OUT['wordmark']=svg(W,72,WM(False)); OUT['wordmark-oscuro']=svg(W,72,WM(False),True); OUT['wordmark-animado']=svg(W,72,WM(True),style=CSS)
for k,s in OUT.items(): open(f'{k}.svg','w').write(s)
def img(f,h,style=''): return f'<span style="display:inline-flex;{style}"><img src="{f}" style="height:{h}px"></span>'
def tile(f,h,bg): return f'<span style="display:inline-flex;width:{h}px;height:{h}px;border-radius:{h*.22}px;background:{bg};align-items:center;justify-content:center"><img src="{f}" style="height:{h*.64}px"></span>'
TEMAS=[('cobre (PULZ)','#b4582f'),('palenque azul','#2b5ea8'),('palenque verde','#2f7a4f'),('palenque vino','#8a2142')]
def inl(f,h,c): return f'<span style="display:inline-flex;--pulz-color:{c};color:#2a211c">'+open(f).read().replace('<svg ',f'<svg height="{h}" ',1)+'</span>'
rows=(f'<section style="display:flex;gap:18px;align-items:center;padding:14px 18px;border-bottom:1px solid #e3dccf">{img("simbolo.svg",112)}{img("simbolo.svg",48)}{img("simbolo.svg",24)}{img("simbolo.svg",16)}{tile("simbolo.svg",72,"#fff")}{tile("simbolo-oscuro.svg",72,"#2a211c")}</section>'
      f'<section style="display:flex;gap:26px;align-items:center;padding:16px 18px;border-bottom:1px solid #e3dccf">{img("wordmark.svg",64)}{img("wordmark.svg",28)}<span style="display:inline-flex;padding:12px 16px;background:#2a211c;border-radius:12px">{img("wordmark-oscuro.svg",40)}</span></section>'
      f'<section style="display:flex;gap:14px;align-items:center;padding:16px 18px;flex-wrap:wrap"><b style="font:600 12px sans-serif;color:#6b5d50;width:120px">color de cada palenque</b>'
      + ''.join(f'<span style="display:inline-flex;flex-direction:column;gap:6px;align-items:center;font:11px sans-serif;color:#6b5d50">{inl("simbolo.svg",56,c)}<span style="display:inline-flex;gap:6px;align-items:center;font:600 12px sans-serif;color:#2a211c;border:1px solid #e3dccf;border-radius:999px;padding:3px 9px 3px 5px;background:#fff;--pulz-color:{c}">{inl("simbolo.svg",16,c)}hecho con PULZ</span>{n}</span>' for n,c in TEMAS) + '</section>')
open('banco.html','w').write(f'<html><body style="margin:0;background:#f4efe6">{rows}</body></html>')
print('ok')
