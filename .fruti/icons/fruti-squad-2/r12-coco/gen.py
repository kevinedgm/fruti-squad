# Fruti Squad · ronda 12 · Coco UI Audit. Elegidos: Kiwi «Tres tamaños», Lima «Biblioteca» (usuario: «vamos con el 2»).
# Coco audita: cumplimiento visual, consistencia, accesibilidad observable, desviaciones del contrato. Mismo idioma: marcos redondeados trazo 3.5 + punto.
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
def svg(b, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b.replace("§", c).replace("¤", "#fff" if c == INK else INK)}</svg>'
def d(x, y, r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="§"/>'
def o(x, y, r, w=3.5, fill='none'): return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="§" stroke-width="{w}" fill="{fill}"/>'
def fr(x, y, w, h, r, fill='none'): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" stroke="§" stroke-width="3.5" fill="{fill}"/>'
def ln(p, w=3.5): return f'<path d="{p}" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
KIWI = fr(4, 4, 56, 56, 12) + fr(13, 13, 38, 38, 9) + fr(21, 21, 22, 22, 6) + d(32, 32, 5.5)
LIMA = fr(20, 4, 40, 34, 9) + fr(12, 13, 40, 34, 9, '¤') + fr(4, 22, 40, 36, 9, '¤') + d(24, 40, 6)
C = [
 ('Visor', 'Las esquinas de un visor encuadran la pieza: Coco la inspecciona antes de aprobarla. El punto es lo que está revisando.',
  'Dice «inspeccionar» sin la lupa genérica; conversa con los marcos de Kiwi y Lima (es un marco abierto).', 'Puede recordar el icono de «escanear» o de cámara.',
  ln('M4 18V12a8 8 0 0 1 8-8h6M46 4h6a8 8 0 0 1 8 8v6M60 46v6a8 8 0 0 1-8 8h-6M18 60h-6a8 8 0 0 1-8-8v-6') + fr(18, 18, 28, 28, 7) + d(32, 32, 5.5)),
 ('Hallazgo', 'Una retícula pareja de puntos y uno que no cumple, marcado con anillo: la desviación que la auditoría encuentra.',
  'Es exactamente lo que entrega una auditoría: lo que se sale del patrón.', 'Sin el marco, se parece a un patrón decorativo; con marco, a un teclado numérico.',
  fr(4, 4, 56, 56, 12) + ''.join(d(x, y, 3.4) for x in (18, 32, 46) for y in (18, 32, 46) if (x, y) != (46, 46)) + o(46, 46, 6)),
 ('Comparación', 'Contrato contra implementación: dos marcos iguales, pero el punto del segundo se movió. Coco ve la diferencia.',
  'Cuenta el corazón de R0 (comparar lo aprobado con lo construido); muy propio.', 'Dos marcos pequeños pierden detalle a 16 px, y el conjunto se puede leer como una cara o un robot.',
  fr(4, 14, 26, 36, 7) + fr(34, 14, 26, 36, 7) + d(17, 32, 5) + d(50, 25, 5) + ln('M47 42h6', 3)),
 ('Lente', 'Un lente sobre un marco: la lupa de la auditoría, en el idioma de la familia.',
  'La lectura más inmediata de «audit».', 'La lupa es el icono de «buscar» en casi cualquier interfaz: se confunde.',
  fr(4, 4, 42, 42, 10) + o(38, 38, 14, 3.5, '¤') + d(38, 38, 5) + ln('M48 48l10 10', 5)),
]
cards = ''.join(f'''<section class="c"><span class="n">{i+1}</span>{svg(b)}<div><h2>{t}</h2><p>{idea}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p>
<div class="sm"><span class="pq">{svg(b)}</span><span class="pq p24">{svg(b)}</span><span class="pq dk">{svg(b, "#fff")}</span><span class="pair">{svg(KIWI)}{svg(LIMA)}{svg(b)}<small>Kiwi · Lima · Coco</small></span></div></div></section>''' for i, (t, idea, a, r, b) in enumerate(C))
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.fam{{display:flex;gap:18px;align-items:center;background:#fff;border:1px solid #e3e3de;border-radius:14px;padding:12px 16px;flex-wrap:wrap}}.fam svg{{width:44px;height:44px}}.fam span{{display:flex;gap:8px;align-items:center}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.c{{position:relative;background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;grid-template-columns:124px minmax(0,1fr);gap:18px;align-items:start}}
.c>svg{{width:124px;height:124px}}.n{{position:absolute;top:12px;left:14px;font-size:12px;font-weight:800;color:#8a8a84}}h2{{font-size:20px;margin:0 0 4px}}
.c p{{margin:0 0 6px;font-size:14px;color:#3a3a37}}.c p.pr{{color:#5b5b56}}.pr b{{color:{INK}}}
.sm{{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px;align-items:center}}.pq{{display:inline-grid;place-items:center;width:30px;height:30px;border:1px solid #ececE6;border-radius:8px}}.pq svg{{width:16px;height:16px}}.pq.p24{{width:38px;height:38px}}.pq.p24 svg{{width:24px;height:24px}}.pq.dk{{background:{INK};border-color:{INK}}}
.pair{{display:inline-flex;flex-wrap:wrap;align-items:center;gap:10px;border:1px solid #ececE6;border-radius:10px;padding:6px 10px}}.pair svg{{width:30px;height:30px}}.pair small{{color:#6b6b66}}
@media (max-width:860px){{.g{{grid-template-columns:1fr}}}}@media (max-width:440px){{.c{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Coco UI Audit · símbolo</title>'
        f'<style>{css}</style></head><body><main><h1>Coco · UI Audit</h1>'
        f'<p class="lead">Coco audita: cumplimiento visual, consistencia, accesibilidad y desviaciones del contrato. Cuatro opciones en el idioma de la familia, cada una vista junto a Kiwi y Lima.</p>'
        f'<div class="fam"><span>{svg(KIWI)}<b>Kiwi</b> UX Architect</span><span>{svg(LIMA)}<b>Lima</b> Design System Governance</span></div>'
        f'<div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'coco.html'), 'w').write(html); print('ok')
