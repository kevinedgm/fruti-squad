# Conectti · ronda 2: direcciones más modernas y con forma propia. Colores del DS (cobalto #1D52BB, fuerte #0439A1, verde azulado #057F7D).
# Uso: python gen.py <carpeta de fuentes con IBMPlexSans.ttf>
import sys,os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import uharfbuzz as hb
S=sys.argv[1]; INK='#111820'; BG='#F4F7FA'; COB='#1D52BB'; COBS='#0439A1'; TEAL='#057F7D'; WHITE='#FFFFFF'
src=S+'/fuentes/IBMPlexSans.ttf'; inst='/tmp/conectti-plex600.ttf'
if not os.path.exists(inst): instancer.instantiateVariableFont(TTFont(src),{'wght':600,'wdth':100}).save(inst)
FONT=TTFont(inst); UPM=FONT['head'].unitsPerEm
def palabra(s,size,x0,y0):
    hf=hb.Font(hb.Face(hb.Blob.from_file_path(inst))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    gs=FONT.getGlyphSet(); order=FONT.getGlyphOrder(); k=size/UPM; x=x0; d=''
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        g=gs[order[i.codepoint]]; pen=SVGPathPen(gs); g.draw(TransformPen(pen,(k,0,0,-k,x,y0))); d+=pen.getCommands(); x+=ps.x_advance*k
    return d,x
GRAD=f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{COB}"/><stop offset="1" stop-color="{TEAL}"/></linearGradient></defs>'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
# A · gota de barrido: una gota (agua, bebida, muestra) hecha solo de líneas horizontales de distinto largo; la línea más larga, en acento, es la lectura.
def gota(c=True):
    b=''; filas=[(14,3),(18,6),(22,9),(26,12),(30,15),(34,17),(38,18),(42,18),(46,16),(50,12),(54,6)]
    for i,(y,r) in enumerate(filas):
        col=(TEAL if i==7 else COB) if c else INK
        b+=f'<path d="M{32-r} {y} H{32+r}" stroke="{col}" stroke-width="2.6"/>'
    return svg(b)
# B · pico en negativo: bloque cobalto con el pico de una medición recortado en blanco; el vértice lleva el punto de acento.
def pico(c=True):
    k=COB if c else INK; a=TEAL if c else WHITE
    return svg(f'<rect x="6" y="6" width="52" height="52" rx="14" fill="{k}"/><path d="M14 42 H24 L32 22 L40 42 H50" stroke="{WHITE}" stroke-width="5"/><circle cx="32" cy="22" r="4" fill="{a}"/>')
# D · lente: una vesica (dos medidas que coinciden) en degradado cobalto→verde azulado con una ranura de calibración blanca.
def lente(c=True):
    f='url(#g)' if c else INK
    return svg(f'{GRAD}<path d="M32 6 C50 18 50 46 32 58 C14 46 14 18 32 6 Z" fill="{f}"/><path d="M32 24 V40" stroke="{WHITE}" stroke-width="5"/>')
# C · logotipo con la tt como ligadura: "conec" y "i" de IBM Plex Sans 600; las dos t dibujadas a mano comparten una sola barra que se extiende como marca de calibración; el punto de la i es de acento.
def wordmark(c=True, size=40):
    k=COB if c else INK; a=TEAL if c else INK; y0=size*1.05; u=size/UPM
    d1,x=palabra('conec',size,4,y0)
    dt1,x1=palabra('t',size,x,y0); dt2,x2=palabra('t',size,x1,y0); di,x3=palabra('ı',size,x2,y0)
    # barra compartida: cubre las dos barras reales (y 421–522 en unidades) y sobresale a la derecha como marca de calibración
    bx=x+25*u; bw=(x2+90*u)-bx; by=y0-522*u; bh=101*u
    bar=f'<rect x="{bx:.2f}" y="{by:.2f}" width="{bw:.2f}" height="{bh:.2f}" rx="{bh/2:.2f}" fill="{a}"/>'
    dot=f'<circle cx="{x2+138*u:.2f}" cy="{y0-690*u:.2f}" r="{60*u:.2f}" fill="{a}"/>'
    return svg(f'<path d="{d1}{dt1}{dt2}{di}" fill="{k}"/>{bar}{dot}', f'0 0 {x3+6:.0f} {size*1.35:.0f}')
# versión símbolo de C: solo la tt
def tt(c=True):
    k=COB if c else INK; a=TEAL if c else INK
    return svg(f'<path d="M22 12 V42 a9 9 0 0 0 9 9 H34" stroke="{k}" stroke-width="7.5"/><path d="M42 12 V42 a9 9 0 0 0 9 9 H54" stroke="{k}" stroke-width="7.5"/><path d="M14 27 H60" stroke="{a}" stroke-width="6"/>')
C={'A · gota de barrido':gota,'B · pico en negativo':pico,'C · la ligadura tt':tt,'D · la lente':lente}
css=f'''@font-face{{font-family:Plex;src:url("file://{src}");font-weight:100 700}}
body{{margin:0;padding:28px;background:{BG};color:{INK};font:14px/1.4 Plex,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:600 18px Plex;margin:0 0 6px}} .sub{{color:#4A515C;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-bottom:26px}}
.celda{{display:grid;gap:10px;align-content:start;background:{WHITE};padding:16px;border-radius:11px;border:1px solid #DCE2EA}} .celda svg{{display:block}} .big svg{{width:120px;height:120px}}
.s{{display:flex;gap:14px;align-items:center}} .s svg{{width:24px;height:24px}} .s .x svg{{width:16px;height:16px}}
.inv{{background:{COBS};padding:10px;border-radius:8px;display:inline-flex;gap:10px}}
.lock{{display:flex;align-items:center;gap:10px}} .lock svg{{width:40px;height:40px}} .lock b{{font:600 30px Plex;letter-spacing:-.01em;color:{INK}}}
.wm{{grid-column:1/-1;background:{WHITE};padding:20px;border-radius:11px;border:1px solid #DCE2EA;display:grid;gap:14px}} .wm svg{{height:64px;display:block}} .wm .inv2{{background:{COBS};padding:16px;border-radius:8px}} .wm .mini svg{{height:22px}}
.tag{{font:400 12px Plex;color:#646B75}}'''
def inv(s): return s.replace(f'fill="{WHITE}"','fill="@W@"').replace(f'stroke="{WHITE}"','stroke="@S@"').replace('url(#g)',WHITE).replace(COB,WHITE).replace(TEAL,'#5FD6CF').replace(INK,WHITE).replace('@W@',COBS).replace('@S@',COBS)
cells=''
for name,fn in C.items():
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big">{fn(True)}</div><div class="s">{fn(True)}<span class="x">{fn(True)}</span><span class="inv">{inv(fn(True))}{inv(fn(False))}</span></div><div class="big" style="opacity:.9">{fn(False)}</div><div class="lock">{fn(True)}<b>Conectti</b></div></div>'
wm=f'<div class="wm"><h2>C · el logotipo completo: conectti con la tt ligada (IBM Plex Sans 600 + tt dibujada)</h2>{wordmark(True)}<div class="inv2">{inv(wordmark(True))}</div><div class="mini">{wordmark(True)}</div><span class="tag">la barra de acento une las dos t y sobresale como marca de calibración; el punto de la i repite el acento</span></div>'
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Conectti · ronda 2 · cuatro direcciones con forma propia: gota de barrido, pico en negativo, ligadura tt, lente en degradado. Colores del DS.</p><div class="fila">{cells}{wm}</div>')
print('ok')
