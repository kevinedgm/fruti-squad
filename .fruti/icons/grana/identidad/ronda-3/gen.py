# Grana · ronda 3: wordmark con Instrument Sans (texto convertido a trazados) + símbolo A5.
import sys, re, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
SRC=sys.argv[1]
COLOR='var(--g-color-brand,#a3123a)'
_cache={}
def inst(wght,wdth):
    k=(wght,wdth)
    if k not in _cache:
        f=TTFont(SRC); instantiateVariableFont(f,{'wght':wght,'wdth':wdth},inplace=True); p=f'is-{wght}-{wdth}.ttf'; f.save(p); _cache[k]=(TTFont(p),p)
    return _cache[k]
def texto(s,size,x0,y0,wght=600,wdth=100,track=0):
    f,p=inst(wght,wdth); upm=f['head'].unitsPerEm
    font=hb.Font(hb.Face(hb.Blob.from_file_path(p))); buf=hb.Buffer(); buf.add_str(s); buf.guess_segment_properties(); hb.shape(font,buf,{'kern':True})
    gs=f.getGlyphSet(); order=f.getGlyphOrder(); k=size/upm; x=0; d=''
    for info,pos in zip(buf.glyph_infos,buf.glyph_positions):
        pen=SVGPathPen(gs); gs[order[info.codepoint]].draw(TransformPen(pen,(k,0,0,-k,x0+x*k,y0))); d+=pen.getCommands(); x+=pos.x_advance+track*upm
    return d, x*k-track*upm*k
def capheight(wght,wdth):
    f,_=inst(wght,wdth); return f['OS/2'].sCapHeight/f['head'].unitsPerEm, f['OS/2'].sxHeight/f['head'].unitsPerEm
sym=open('../ronda-2/a5-color.svg').read()
sym_inner=re.search(r'-->\n(.*)</svg>',sym,re.S).group(1)
def simbolo(x,y,s):  # s = lado en unidades
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({s/48:.4f})">{sym_inner}</g>'
def svg(w,h,body,label='Grana'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" role="img" aria-label="{label}">\n{body}\n</svg>\n'
OUT={}
# W1 · limpio: símbolo + «grana» seminegrita, ligero ajuste de espaciado
size=64; ch,xh=capheight(600,100)
d,w=texto('grana',size,72,52,600,100,-0.01)
OUT['w1-limpio']=svg(72+w+4,72,simbolo(0,4,64)+f'<path fill="currentColor" d="{d}"/>')
# W2 · fuera de registro: la palabra en tinta con su tinte desplazado detrás (la firma del símbolo llevada al nombre)
d,w=texto('grana',size,72,52,700,100,-0.015)
OUT['w2-registro']=svg(72+w+6,72,simbolo(0,4,64)+f'<path fill="{COLOR}" transform="translate(2.4 2.4)" d="{d}"/><path fill="currentColor" d="{d}"/>')
# W3 · semicondensado + lema: más compacto y técnico, con el lema debajo
d,w=texto('grana',size,72,46,650,85,-0.01)
dl,wl=texto("The only bug you'll want in your UI.",13.5,73,66,500,100,0)
OUT['w3-lema']=svg(72+max(w,wl)+4,72,simbolo(0,4,64)+f'<path fill="currentColor" d="{d}"/><path fill="currentColor" opacity=".72" d="{dl}"/>')
for k,s in OUT.items(): open(f'{k}.svg','w').write(s)
# banco
TEMAS=['#a3123a','#2563eb','#0f8a5f']
def r(f,h,style=''): return f'<span style="display:inline-flex;{style}">'+open(f).read().replace('<svg ',f'<svg height="{h}" ',1)+'</span>'
rows=''
for k in OUT:
    rows+=(f'<section style="padding:14px 18px;border-bottom:1px solid #e8e8e8"><b style="font:600 13px sans-serif;color:#555">{k}</b>'
           f'<div style="display:flex;gap:28px;align-items:center;margin-top:10px;color:#141414">{r(k+".svg",72)}{r(k+".svg",32)}{r(k+".svg",20)}</div>'
           f'<div style="display:flex;gap:12px;align-items:center;margin-top:12px">'
           + ''.join(r(k+'.svg',36,f'padding:10px 14px;background:#fff;border:1px solid #eee;border-radius:10px;color:#141414;--g-color-brand:{c}') for c in TEMAS)
           + r(k+'.svg',36,'padding:10px 14px;background:#141414;color:#f5f5f5;border-radius:10px;--g-color-brand:#ff4d7a') + '</div></section>')
open('banco.html','w').write(f'<html><body style="margin:0;background:#fafaf9">{rows}</body></html>')
