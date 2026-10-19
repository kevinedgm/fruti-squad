# Xila · ronda 1: cuatro conceptos desde el brocado oaxaqueño (rombos, grecas, puntada en zigzag, franja), con la anatomía de la propia librería
import sys,glob
S=sys.argv[1]; INK='#15171f'; PAPEL='#f7f5f0'; COB='#1f4bd8'; COB_D='#7a9bff'
def svg(body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
# A · la X del telar: dos hilos cruzados forman el rombo; el cruce es la X de Xila y el rombo, el dato
def xtelar(c=True):
    a=COB if c else INK
    return svg(f'<path d="M10 14 L32 36 L54 14" stroke="{INK}" stroke-width="4"/><path d="M10 50 L32 28 L54 50" stroke="{INK}" stroke-width="4"/><path d="M24 32 L32 24 L40 32 L32 40 Z" fill="{a}"/>')
# B · la greca que es gráfica: una línea de 2 px escalonada (greca de Mitla) con su último valor marcado con punto y anillo
def greca(c=True):
    a=COB if c else INK
    return svg(f'<path d="M8 46 H20 V34 H32 V22 H44 V14 H52" stroke="{INK}" stroke-width="4"/><circle cx="52" cy="14" r="6" fill="{a}" stroke="{PAPEL}" stroke-width="3"/>')
# C · la franja: una banda de brocado hecha de barras con extremo redondeado y hueco entre vecinas (la anatomía de Xila), con silueta de rombo
def franja(c=True):
    a=COB if c else INK; b=''
    alt=[14,24,34,42,34,24,14]
    for i,h in enumerate(alt):
        x=8+i*7; b+=f'<rect x="{x}" y="{32-h/2}" width="5" height="{h}" rx="2.5" fill="{a if i==3 else INK}"/>'
    return svg(b)
# D · la puntada: el zigzag de la costura es una serie de tiempo de 2 px; el pico en color es el hallazgo (titlePlugin)
def puntada(c=True):
    a=COB if c else INK
    return svg(f'<path d="M6 40 L16 28 L26 38 L36 20 L46 32 L58 16" stroke="{INK}" stroke-width="4"/><circle cx="58" cy="16" r="6" fill="{a}" stroke="{PAPEL}" stroke-width="3"/><path d="M6 52 H58" stroke="{INK}" stroke-width="2" stroke-dasharray="2 5"/>')
C={'A · la X del telar':xtelar,'B · la greca que es gráfica':greca,'C · la franja de barras':franja,'D · la puntada':puntada}
sg=glob.glob(S+'/fuentes/SpaceGrotesk*')[0]
css=f'''@font-face{{font-family:SG;src:url("file://{sg}");font-weight:300 700}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 18px SG;margin:0 0 6px}} .sub{{color:#666;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-bottom:26px}}
.celda{{display:grid;gap:10px;align-content:start}} .celda svg{{display:block}} .big svg{{width:120px;height:120px}}
.s{{display:flex;gap:14px;align-items:center}} .s svg{{width:24px;height:24px}} .s .x svg{{width:16px;height:16px}}
.dark{{background:{INK};padding:10px;border-radius:10px;display:inline-flex;gap:10px}}
.lock{{display:flex;align-items:center;gap:12px}} .lock svg{{width:40px;height:40px}} .lock b{{font:700 32px SG;letter-spacing:-.02em}}
.tag{{font:400 12px system-ui;color:#666}}'''
def dark(s): return s.replace(f'stroke="{PAPEL}"','stroke="@ANILLO@"').replace(INK,PAPEL).replace('@ANILLO@',INK).replace(COB,COB_D)
cells=''
for name,fn in C.items():
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big">{fn(True)}</div><div class="s">{fn(True)}<span class="x">{fn(True)}</span><span class="dark">{dark(fn(True))}{dark(fn(False))}</span></div><div class="big" style="opacity:.9">{fn(False)}</div><div class="lock">{fn(True)}<b>xila</b></div><span class="tag">una tinta · con el nombre</span></div>'
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Xila · ronda 1 · cuatro conceptos desde el brocado (rombos, grecas, puntada, franja) dibujados con la anatomía de la librería: líneas de 2 px, barras redondeadas con hueco, punto con anillo. Cobalto provisional.</p><div class="fila">{cells}</div>')
print('ok')
