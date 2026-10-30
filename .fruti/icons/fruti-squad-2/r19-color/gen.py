# Fruti Squad · ronda 19: color. Familia de símbolos completa (usuario eligió la Espiral para el orquestador: «me gusta la opción 2»).
# Tres maneras de usar el color; paleta viva y moderna validada con el validador de dataviz (CVD deutan ≥ 12 sobre oscuro).
import os, re, itertools
H = os.path.dirname(os.path.abspath(__file__))
INK, PAPER, DARK = '#18181b', '#f5f5f2', '#0f0f12'
COL = {'squad': None, 'kiwi': '#34e0a1', 'lima': '#d4ff3a', 'coco': '#ff9f1c', 'bruno': '#4361ee', 'mora': '#f72585'}
ACENTO = '#f72585'
_n = itertools.count()
def d(x, y, r, f='§'): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}"/>'
def fr(x, y, w, h, r, fill='none'): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" stroke="§" stroke-width="3.5" fill="{fill}"/>'
def ln(p, w=3.5): return f'<path d="{p}" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def esp():
    o = ''.join(f'<rect x="{32 - s / 2}" y="{32 - s / 2}" width="{s}" height="{s}" rx="{rx}" stroke="§" stroke-width="3" transform="rotate({i * 11} 32 32)"/>' for i, (s, rx) in enumerate([(54, 14), (43, 11), (33, 9), (24, 7), (16, 5)]))
    return o + d(32, 32, 4, 'ª')
SYM = {
 'squad': esp(),
 'kiwi': fr(4, 4, 56, 56, 12) + fr(13, 13, 38, 38, 9) + fr(21, 21, 22, 22, 6) + d(32, 32, 5.5, 'ª'),
 'lima': fr(20, 4, 40, 34, 9) + fr(12, 13, 40, 34, 9, '¤') + fr(4, 22, 40, 36, 9, '¤') + d(24, 40, 6, 'ª'),
 'coco': ln('M4 18V12a8 8 0 0 1 8-8h6M46 4h6a8 8 0 0 1 8 8v6M60 46v6a8 8 0 0 1-8 8h-6M18 60h-6a8 8 0 0 1-8-8v-6') + fr(18, 18, 28, 28, 7) + d(32, 32, 5.5, 'ª'),
 'bruno': '<path d="M27 4H16A12 12 0 0 0 4 16v32a12 12 0 0 0 12 12h3" stroke="§" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="5 5"/><path d="M37 60h11a12 12 0 0 0 12-12V16A12 12 0 0 0 48 4h-3" stroke="§" stroke-width="3.5" stroke-linecap="round"/>' + ln('M38 6L26 58', 4) + d(44, 32, 5.5, 'ª'),
 'mora': fr(4, 4, 56, 56, 12) + ln('M19 19L44 21M44 21L45 45M44 21L20 44', 3) + d(19, 19, 6, 'ª') + d(44, 21, 4.5) + d(45, 45, 4.5) + d(20, 44, 4.5),
}
NOM = [('squad', 'Fruti Squad', 'Workflow Pack'), ('kiwi', 'Kiwi', 'UX Architect'), ('lima', 'Lima', 'Design System Governance'), ('coco', 'Coco', 'UI Audit'),
       ('bruno', 'Bruno', 'Frontend Implementation Engineer'), ('mora', 'Mora', 'Documentation & Knowledge Engineer')]
GRAD = ''.join(f'<stop offset="{i/4:.2f}" stop-color="{c}"/>' for i, c in enumerate([COL[k] for k in ('kiwi', 'lima', 'coco', 'bruno', 'mora')]))
def svg(k, linea, punto, fondo):
    n = next(_n); b = SYM[k]
    defs = ''
    if punto == 'GRAD':
        defs = f'<defs><linearGradient id="g{n}" x1="0" y1="0" x2="1" y2="1">{GRAD}</linearGradient></defs>'; punto = f'url(#g{n})'
    return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{defs}{b.replace("§", linea).replace("ª", punto).replace("¤", fondo)}</svg>'
# A · monocromo + un acento (el punto, igual para todos)
def A(k, dark): return svg(k, '#fff' if dark else INK, ACENTO, DARK if dark else '#fff')
# B · un color por integrante (todo el símbolo); el squad en neutro con punto degradado
def B(k, dark):
    if k == 'squad': return svg(k, '#fff' if dark else INK, 'GRAD', DARK if dark else '#fff')
    c = COL[k] if dark else {'kiwi': '#0f9e6e', 'lima': '#5f7a00', 'coco': '#b86a00', 'bruno': '#3a54d6', 'mora': '#d0156e'}[k]
    return svg(k, c, c, DARK if dark else '#fff')
# C · duotono: trazo neutro, el punto en el color de quien produce la evidencia; el squad reúne todos en degradado
def C(k, dark):
    linea = '#fff' if dark else INK
    p = 'GRAD' if k == 'squad' else COL[k]
    if not dark and k == 'lima': p = '#8fb300'
    return svg(k, linea, p, DARK if dark else '#fff')
SIS = [
 ('A', 'Blanco y negro con un acento', 'Todos en tinta; solo el punto, la evidencia, va en un mismo color vivo. La identidad la llevan las siluetas.',
  'La más sobria y la más fácil de mantener; muy moderna. Funciona igual en claro y en oscuro.', 'Los integrantes no tienen color propio: en un marketplace se distinguen solo por forma y nombre.', A),
 ('B', 'Un color por integrante', 'Cada símbolo completo en su color: menta, ácido, ámbar, azul eléctrico y magenta. El orquestador en neutro con el punto que reúne los cinco colores.',
  'Máxima diferenciación en tiendas y redes; cada producto tiene su color de portada.', 'En claro los colores vivos deben oscurecerse para leerse; son dos versiones por color.', B),
 ('C', 'Duotono: la evidencia lleva el color', 'Trazo neutro para todos y el punto en el color de cada integrante: la evidencia lleva la firma de quien la produjo. El orquestador reúne los cinco colores en su punto.',
  'Une las dos ventajas: familia sobria y color propio; además cuenta el producto (cada agente firma su evidencia).', 'El color ocupa poco espacio: a 16 px el punto se nota menos.', C),
]
def card(k, t, idea, a, r, F):
    claro = ''.join(f'<figure>{F(i, False)}<figcaption>{n}</figcaption></figure>' for i, n, _ in NOM)
    oscuro = ''.join(f'<figure>{F(i, True)}<figcaption>{n}</figcaption></figure>' for i, n, _ in NOM)
    lk = ''.join(f'<div class="lk">{F(i, True)}<span><b>{n}</b><i>{p}</i></span></div>' for i, n, p in (NOM[3], NOM[0]))
    peq = ''.join(f'<span class="pq">{F(i, False)}</span>' for i, n, _ in NOM) + ''.join(f'<span class="pq dk">{F(i, True)}</span>' for i, n, _ in NOM)
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{t}</h2></header><p class="id">{idea}</p>'
            f'<div class="fam">{claro}</div><div class="fam dk">{oscuro}</div><div class="row">{peq}</div><div class="lks">{lk}</div>'
            f'<p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
sw = ''.join(f'<span class="sw"><i style="background:{c}"></i><b>{k.capitalize()}</b> {c}</span>' for k, c in COL.items() if c)
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{PAPER};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}.pal{{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:13.5px}}.sw{{display:inline-flex;gap:6px;align-items:center}}.sw i{{width:14px;height:14px;border-radius:4px}}
.c{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:22px;display:grid;gap:12px;min-width:0}}.c header{{display:flex;gap:10px;align-items:center}}
.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font-size:19px;margin:0}}.id{{margin:0;color:#3a3a37}}
.fam{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;border:1px solid #ececE6;border-radius:14px;padding:14px}}.fam.dk{{background:{DARK};border-color:{DARK};color:#fff}}
.fam figure{{margin:0;display:grid;justify-items:center;gap:6px;font-size:13px;font-weight:600}}.fam svg{{width:64px;height:64px}}
.row{{display:flex;flex-wrap:wrap;gap:6px}}.pq{{display:inline-grid;place-items:center;width:28px;height:28px;border:1px solid #ececE6;border-radius:7px}}.pq svg{{width:16px;height:16px}}.pq.dk{{background:{DARK};border-color:{DARK}}}
.lks{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}}.lk{{display:flex;align-items:center;gap:14px;background:{DARK};color:#fff;border-radius:14px;padding:14px 18px;min-width:0}}.lk svg{{width:52px;height:52px;flex:none}}.lk span{{display:grid;line-height:1.2}}.lk b{{font-size:22px}}.lk i{{font-style:normal;color:#c9c9c4}}
.pr{{margin:0;font-size:14px;color:#4b4b47}}.pr b{{color:{INK}}}
@media (max-width:900px){{.fam{{grid-template-columns:repeat(3,minmax(0,1fr))}}.lks{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · color</title>'
        f'<style>{css}</style></head><body><main><h1>Fruti Squad · color (ronda 19)</h1>'
        '<p class="lead">La familia de símbolos ya está completa. Ahora el color, con una paleta viva y moderna (distinta de la ronda que no gustó), probada para daltonismo sobre fondo oscuro. Tres maneras de usarla; cada una en claro, en oscuro, a 16 px y como producto.</p>'
        f'<div class="pal">{sw}</div>{"".join(card(*x) for x in SIS)}</main></body></html>')
open(os.path.join(H, 'color.html'), 'w').write(html); print('ok')
