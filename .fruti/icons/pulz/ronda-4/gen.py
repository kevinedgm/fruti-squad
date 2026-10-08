# PULZ · ronda 4: misma Z del trasiego; 3 paletas × 3 tipografías.
import sys, re, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
FD=sys.argv[1]
FUENTES={'unbounded':('Unbounded[wght].ttf',800),'syne':('Syne[wght].ttf',800),'space':('SpaceGrotesk[wght].ttf',700)}
PALETAS={'noche-agave':dict(ink='#0e1a1c',acc='#1fbf95',bg='#eef4f1',ink_n='#eef4f1',acc_n='#33d3a6',bg_n='#0e1a1c'),
         'brasa':dict(ink='#17161a',acc='#e8501a',bg='#f6f2ee',ink_n='#f6f2ee',acc_n='#ff6a33',bg_n='#17161a'),
         'anil':dict(ink='#121217',acc='#3346e0',bg='#f2f2f6',ink_n='#f2f2f6',acc_n='#7d8bff',bg_n='#121217')}
def L(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]; c=[v/12.92 if v<=.03928 else ((v+.055)/1.055)**2.4 for v in c]; return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b): x,y=sorted([L(a),L(b)]); return (y+.05)/(x+.05)
def marca(acc,ink):
    return (f'<rect x="8" y="9" width="48" height="12" rx="3" fill="{ink}"/><rect x="8" y="43" width="48" height="12" rx="3" fill="{ink}"/>'
            f'<polygon points="38,21 56,21 26,43 8,43" fill="{acc}"/><rect x="11.5" y="46.5" width="41" height="5" rx="2.5" fill="{acc}"/>')
_c={}
def fuente(k):
    if k not in _c:
        fn,w=FUENTES[k]; f=TTFont(FD+'/'+fn); instantiateVariableFont(f,{'wght':w},inplace=True); p=f'/tmp/pz-{k}.ttf'; f.save(p); _c[k]=(TTFont(p),p)
    return _c[k]
def palabra(k,size,y0,ink):
    f,p=fuente(k); hf=hb.Font(hb.Face(hb.Blob.from_file_path(p))); b=hb.Buffer(); b.add_str('PUL'); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    gs=f.getGlyphSet(); order=f.getGlyphOrder(); kk=size/f['head'].unitsPerEm; x=0; d=''; bp=BoundsPen(gs)
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        g=gs[order[i.codepoint]]; pen=SVGPathPen(gs); m=(kk,0,0,-kk,x,y0); g.draw(TransformPen(pen,m)); g.draw(TransformPen(bp,m)); d+=pen.getCommands(); x+=ps.x_advance*kk
    cap=f['OS/2'].sCapHeight*kk
    return d,bp.bounds,cap
def wordmark(k,pal,oscuro=False):
    P=PALETAS[pal]; ink=P['ink_n'] if oscuro else P['ink']; acc=P['acc_n'] if oscuro else P['acc']
    d,bb,cap=palabra(k,64,64,ink); esc=cap/46; zx=bb[2]+cap*.24-8*esc
    W=zx+56*esc+2
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} 72" role="img" aria-label="PULZ"><path fill="{ink}" d="{d}"/><g transform="translate({zx:.2f} {64-cap-9*esc:.2f}) scale({esc:.4f})">{marca(acc,ink)}</g></svg>'
def appicon(P):
    # icono de app: tile en el acento, barras en el fondo claro, trasiego y lote en tinta
    m=(f'<rect x="8" y="9" width="48" height="12" rx="3" fill="{P["bg"]}"/><rect x="8" y="43" width="48" height="12" rx="3" fill="{P["bg"]}"/>'
       f'<polygon points="38,21 56,21 26,43 8,43" fill="{P["ink"]}"/><rect x="11.5" y="46.5" width="41" height="5" rx="2.5" fill="{P["ink"]}"/>')
    return f'<svg viewBox="0 0 64 64" height="40"><rect width="64" height="64" rx="14" fill="{P["acc"]}"/><g transform="translate(10 10) scale(.6875)">{m}</g></svg>'
cells=''
for pal,P in PALETAS.items():
    info=f'acento {cr(P["acc"],P["bg"]):.2f}:1 claro · {cr(P["acc_n"],P["bg_n"]):.2f}:1 oscuro'
    cells+=f'<h3 style="margin:18px 18px 6px;font:600 13px sans-serif;color:#555">{pal} <small style="font-weight:400;color:#888">{info}</small></h3><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:0 18px">'
    for k in FUENTES:
        claro=wordmark(k,pal).replace('<svg ','<svg height="48" ',1)
        oscuro=wordmark(k,pal,True).replace('<svg ','<svg height="30" ',1)
        cells+=(f'<div style="display:grid;gap:6px"><div style="background:{P["bg"]};border-radius:12px;padding:16px;display:flex;align-items:center;justify-content:center">{claro}</div>'
                f'<div style="background:{P["bg_n"]};border-radius:12px;padding:12px;display:flex;gap:14px;align-items:center;justify-content:center">{oscuro}{appicon(P)}</div>'
                f'<small style="font:11px sans-serif;color:#777;text-align:center">{k}</small></div>')
    cells+='</div>'
open('banco.html','w').write(f'<html><body style="margin:0;background:#fff;padding-bottom:16px">{cells}</body></html>')
