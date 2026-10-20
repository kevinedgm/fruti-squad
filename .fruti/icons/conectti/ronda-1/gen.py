# Conectti · ronda 1: cuatro conceptos para la plataforma del laboratorio. Colores tomados del Design System Conectti
# (brand #1D52BB, accent #057F7D, text #111820, bg #F4F7FA, brand-strong #0439A1). Nombre en IBM Plex Sans 600 (la del DS).
# Uso: python gen.py <carpeta de fuentes con IBMPlexSans.ttf>
import sys
S=sys.argv[1]; INK='#111820'; BG='#F4F7FA'; COB='#1D52BB'; COBS='#0439A1'; TEAL='#057F7D'; WHITE='#FFFFFF'
def svg(body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
# A · dos nodos y la marca de calibración: la muestra (izq.) y el resultado (der.) conectados; en medio, la rayita del instrumento (medir con precisión).
def nodos(c=True):
    a=TEAL if c else INK; k=COB if c else INK
    return svg(f'<path d="M20 32 H44" stroke="{k}" stroke-width="4"/><circle cx="14" cy="32" r="7" fill="{k}"/><circle cx="50" cy="32" r="7" fill="{a}"/><path d="M32 24 V40" stroke="{k}" stroke-width="4"/>')
# B · la doble t de Conectti como eslabón: dos t que comparten la barra; la barra es el enlace entre laboratorio y cliente.
def doblet(c=True):
    a=TEAL if c else INK; k=COB if c else INK
    return svg(f'<path d="M24 14 V44 a6 6 0 0 0 6 6 h4" stroke="{k}" stroke-width="6"/><path d="M40 14 V44 a6 6 0 0 1 -6 6" stroke="{a}" stroke-width="6"/><path d="M14 26 H50" stroke="{k}" stroke-width="6"/>')
# C · la onda del resultado: el perfil de una medición (pico sobre línea base) encerrado en un anillo, con el valor en color de acento. Hereda la onda de NisaNabani.
def onda(c=True):
    a=TEAL if c else INK; k=COB if c else INK
    return svg(f'<circle cx="32" cy="32" r="24" stroke="{k}" stroke-width="4"/><path d="M14 40 H22 L28 40 L33 20 L38 40 H50" stroke="{k}" stroke-width="4"/><circle cx="33" cy="20" r="4.5" fill="{a}" stroke="{BG}" stroke-width="2.5"/>')
# D · la C en red: anillo de nodos conectados que no cierra; el último nodo (acento) es el resultado que entra al sistema.
def cred(c=True):
    import math
    a=TEAL if c else INK; k=COB if c else INK; b=''
    pts=[(32+20*math.cos(math.radians(t)),32+20*math.sin(math.radians(t))) for t in (40,100,160,220,280,320)]
    for (x1,y1),(x2,y2) in zip(pts,pts[1:]): b+=f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="{k}" stroke-width="3.5"/>'
    for i,(x,y) in enumerate(pts): b+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{a if i==len(pts)-1 else k}"/>'
    b+=f'<circle cx="{32+20*math.cos(math.radians(0)):.1f}" cy="32" r="4.5" fill="{a}"/>'
    return svg(b)
C={'A · nodos y marca de calibración':nodos,'B · la doble t, eslabón':doblet,'C · la onda del resultado':onda,'D · la C en red':cred}
css=f'''@font-face{{font-family:Plex;src:url("file://{S}/fuentes/IBMPlexSans.ttf");font-weight:100 700}}
body{{margin:0;padding:28px;background:{BG};color:{INK};font:14px/1.4 Plex,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:600 18px Plex;margin:0 0 6px}} .sub{{color:#4A515C;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-bottom:26px}}
.celda{{display:grid;gap:10px;align-content:start;background:{WHITE};padding:16px;border-radius:11px;border:1px solid #DCE2EA}} .celda svg{{display:block}} .big svg{{width:120px;height:120px}}
.s{{display:flex;gap:14px;align-items:center}} .s svg{{width:24px;height:24px}} .s .x svg{{width:16px;height:16px}}
.inv{{background:{COBS};padding:10px;border-radius:8px;display:inline-flex;gap:10px}}
.lock{{display:flex;align-items:center;gap:10px}} .lock svg{{width:40px;height:40px}} .lock b{{font:600 30px Plex;letter-spacing:-.01em;color:{INK}}}
.tag{{font:400 12px Plex;color:#646B75}}'''
def inv(s): return s.replace(f'stroke="{BG}"','stroke="@R@"').replace(COB,WHITE).replace(TEAL,'#5FD6CF').replace(INK,WHITE).replace('@R@',COBS)
cells=''
for name,fn in C.items():
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big">{fn(True)}</div><div class="s">{fn(True)}<span class="x">{fn(True)}</span><span class="inv">{inv(fn(True))}{inv(fn(False))}</span></div><div class="big" style="opacity:.9">{fn(False)}</div><div class="lock">{fn(True)}<b>Conectti</b></div><span class="tag">una tinta · sobre cobalto fuerte · con el nombre en IBM Plex Sans 600</span></div>'
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Conectti · ronda 1 · cuatro conceptos para la plataforma del laboratorio, con los colores del Design System (cobalto #1D52BB, verde azulado #057F7D). Tema claro único, como el DS.</p><div class="fila">{cells}</div>')
print('ok')
