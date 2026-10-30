# Fruti Squad · ronda 11 · Lima. Usuario: «Lima es Lima Design System Governance». Lectura: igual que con Kiwi («UX Architect»),
# el símbolo debe contar el producto completo: un SISTEMA de diseño (muchas piezas coherentes) que está GOBERNADO (una fuente manda).
# Idioma fijado por Kiwi: marcos redondeados en trazo 3.5 + punto lleno.
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
def svg(b, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b.replace("§", c).replace("¤", "#fff" if c == INK else INK)}</svg>'
def d(x, y, r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="§"/>'
def fr(x, y, w, h, r, fill='none'): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" stroke="§" stroke-width="3.5" fill="{fill}"/>'
def ln(p, w=3.5): return f'<path d="{p}" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
KIWI = fr(4, 4, 56, 56, 12) + fr(13, 13, 38, 38, 9) + fr(21, 21, 22, 22, 6) + d(32, 32, 5.5)
L = [
 ('Fuente única', 'Un marco manda y tres marcos heredan: tokens y contratos bajan de una sola fuente a cada componente. Eso es gobernar un sistema de diseño.',
  'Cuenta «design system» (muchas piezas iguales) y «governance» (una fuente que manda) en un dibujo; distinta de Kiwi y legible.', 'Puede recordar un diagrama de árbol u organigrama.',
  fr(18, 4, 28, 22, 7) + d(32, 15, 5) + ln('M32 26v8M12 34h40M12 34v4M32 34v4M52 34v4') + fr(4, 40, 16, 18, 5) + fr(24, 40, 16, 18, 5) + fr(44, 40, 16, 18, 5) + d(12, 49, 2.6) + d(32, 49, 2.6) + d(52, 49, 2.6)),
 ('Biblioteca', 'Marcos apilados: la colección de componentes del sistema. El de enfrente lleva el punto: la versión aprobada que todos usan.',
  'Dice «sistema» y «biblioteca» de inmediato; silueta muy distinta de Kiwi.', 'Las tarjetas apiladas son comunes en iconos de «copias» o «capas».',
  fr(20, 4, 40, 34, 9) + fr(12, 13, 40, 34, 9, '¤') + fr(4, 22, 40, 36, 9, '¤') + d(24, 40, 6)),
 ('Alineación', 'Piezas de distintos tamaños alineadas a una misma regla: la consistencia que exige el sistema. La regla es la gobernanza.',
  'El concepto de «estándar» sin palomita ni escudo; elegante.', 'Más abstracto: necesita el nombre del producto para leerse como gobernanza.',
  ln('M4 12h56', 4) + fr(6, 12, 14, 18, 4) + fr(25, 12, 14, 30, 4) + fr(44, 12, 14, 44, 4) + d(51, 46, 3.6)),
 ('Clasificación', 'Un marco en cuatro casillas: reutilizar, extender, crear o dejar local. Cada pieza en su lugar dentro del sistema.',
  'La decisión más propia de Lima; misma geometría que Kiwi.', 'Una cuadrícula 2×2 recuerda a iconos de «apps».',
  fr(4, 4, 56, 56, 12) + ln('M32 8v48M8 32h48') + d(45, 19, 6)),
]
cards = ''.join(f'''<section class="c"><span class="n">{i+1}</span>{svg(b)}<div><h2>{t}</h2><p>{idea}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p>
<div class="sm"><span class="pq">{svg(b)}</span><span class="pq p24">{svg(b)}</span><span class="pq dk">{svg(b, "#fff")}</span><span class="pair">{svg(KIWI)}{svg(b)}<span><b>Lima</b> Design System Governance</span></span></div></div></section>''' for i, (t, idea, a, r, b) in enumerate(L))
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.c{{position:relative;background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;grid-template-columns:124px minmax(0,1fr);gap:18px;align-items:start}}
.c>svg{{width:124px;height:124px}}.n{{position:absolute;top:12px;left:14px;font-size:12px;font-weight:800;color:#8a8a84}}h2{{font-size:20px;margin:0 0 4px}}
.c p{{margin:0 0 6px;font-size:14px;color:#3a3a37}}.c p.pr{{color:#5b5b56}}.pr b{{color:{INK}}}
.sm{{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px;align-items:center}}.pq{{display:inline-grid;place-items:center;width:30px;height:30px;border:1px solid #ececE6;border-radius:8px}}.pq svg{{width:16px;height:16px}}.pq.p24{{width:38px;height:38px}}.pq.p24 svg{{width:24px;height:24px}}.pq.dk{{background:{INK};border-color:{INK}}}
.pair{{display:inline-flex;align-items:center;gap:8px;border:1px solid #ececE6;border-radius:10px;padding:6px 10px;font-size:14px}}.pair svg{{width:30px;height:30px}}
@media (max-width:860px){{.g{{grid-template-columns:1fr}}}}@media (max-width:440px){{.c{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Lima Design System Governance · símbolo</title>'
        f'<style>{css}</style></head><body><main><h1>Lima · Design System Governance · ronda 2</h1>'
        '<p class="lead">Como con Kiwi, el símbolo tiene que contar el producto completo: un sistema de diseño (muchas piezas coherentes) que está gobernado (una fuente manda). Mismo idioma que Kiwi: marcos redondeados, mismo trazo, punto lleno.</p>'
        f'<div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'lima.html'), 'w').write(html); print('ok')
