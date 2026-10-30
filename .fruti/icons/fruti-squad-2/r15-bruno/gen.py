# Fruti Squad · ronda 15 · Bruno: combinaciones de Código y Del plano a la pieza (usuario: «me gustan la 2 y la 1»). Usuario: «Bruno · Frontend Implementation Engineer» (nombre de producto). Ronda 13 de referencia. Elegidos: Kiwi «Tres tamaños», Lima «Biblioteca», Coco «Visor» (usuario: «vamos con la 1»).
# Bruno convierte la pieza aprobada en comportamiento real: props, eventos, estados, teclado, foco, ARIA. Nombre de producto: provisional.
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
def svg(b, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b.replace("§", c).replace("¤", "#fff" if c == INK else INK)}</svg>'
def d(x, y, r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="§"/>'
def fr(x, y, w, h, r, fill='none', extra=''): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" stroke="§" stroke-width="3.5" fill="{fill}"{extra}/>'
def ln(p, w=3.5): return f'<path d="{p}" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
KIWI = fr(4, 4, 56, 56, 12) + fr(13, 13, 38, 38, 9) + fr(21, 21, 22, 22, 6) + d(32, 32, 5.5)
LIMA = fr(20, 4, 40, 34, 9) + fr(12, 13, 40, 34, 9, '¤') + fr(4, 22, 40, 36, 9, '¤') + d(24, 40, 6)
COCO = ln('M4 18V12a8 8 0 0 1 8-8h6M46 4h6a8 8 0 0 1 8 8v6M60 46v6a8 8 0 0 1-8 8h-6M18 60h-6a8 8 0 0 1-8-8v-6') + fr(18, 18, 28, 28, 7) + d(32, 32, 5.5)
def half(x0, y0, x1, y1, r, w=3.5, da='5 5'):
    h = (y1 - y0) - 2 * r
    dash = f'<path d="M32 {y0}H{x0 + r}a{r} {r} 0 0 0-{r} {r}v{h}a{r} {r} 0 0 0 {r} {r}H32" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-dasharray="{da}"/>'
    sol = f'<path d="M32 {y0}H{x1 - r}a{r} {r} 0 0 1 {r} {r}v{h}a{r} {r} 0 0 1-{r} {r}H32" stroke="§" stroke-width="{w}" stroke-linecap="round"/>'
    return dash + sol
B = [
 ('Etiqueta del plano', 'Las dos ideas juntas: la pieza entre &lt; &gt; (frontend) y, dentro, el marco que pasa de plano punteado a pieza sólida (implementación).',
  'Dice las tres palabras del nombre: frontend, implementación e ingeniería.', 'Es la más detallada: a 16 px el punteado se pierde y queda como la opción Código.',
  ln('M14 18L4 32l10 14M50 18l10 14-10 14', 4) + half(20, 18, 44, 46, 6, 3.5, '3.5 3.5') + d(32, 32, 4.5)),
 ('Cierre', 'Como la etiqueta de cierre &lt;/&gt;: una diagonal parte el marco. De un lado el plano punteado, del otro la pieza construida. La diagonal es el momento en que Bruno implementa.',
  'Toma el gesto de código (la barra de cierre) sin usar los signos genéricos; muy propio.', 'La diagonal puede leerse como «tachado» o «deshabilitado» si es muy larga.',
  '<path d="M27 4H16A12 12 0 0 0 4 16v32a12 12 0 0 0 12 12h3" stroke="§" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="5 5"/><path d="M37 60h11a12 12 0 0 0 12-12V16A12 12 0 0 0 48 4h-3" stroke="§" stroke-width="3.5" stroke-linecap="round"/>' + ln('M38 6L26 58', 4) + d(44, 32, 5.5)),
 ('Signos en transición', 'Solo los signos &lt; &gt; con el punto en medio: el de la izquierda punteado (lo planeado), el de la derecha sólido (lo implementado).',
  'La silueta más simple y fuerte de las cuatro; une código e implementación en un solo gesto.', 'Sin marco se aleja un poco de la familia; el punto es lo que la conserva.',
  '<path d="M24 12L6 32l18 20" stroke="§" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="6 6"/>' + ln('M40 12l18 20-18 20', 5) + d(32, 32, 6)),
 ('Plano reforzado', 'La opción 2 de antes con un punteado más grueso y espaciado, para que se lea también pequeña.',
  'Conserva la idea que te gustó y gana legibilidad a 16 px.', 'Sin los signos de código dice menos «frontend».',
  half(4, 4, 60, 60, 12, 4.5, '9 7') + d(32, 32, 6.5)),
]
cards = ''.join(f'''<section class="c"><span class="n">{i+1}</span>{svg(b)}<div><h2>{t}</h2><p>{idea}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p>
<div class="sm"><span class="pq">{svg(b)}</span><span class="pq p24">{svg(b)}</span><span class="pq dk">{svg(b, "#fff")}</span><span class="pair">{svg(KIWI)}{svg(LIMA)}{svg(COCO)}{svg(b)}<small>Kiwi · Lima · Coco · Bruno</small></span></div></div></section>''' for i, (t, idea, a, r, b) in enumerate(B))
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
        '<meta name="claude:viewport-fit-sides" content="true"><title>Bruno · Frontend Implementation Engineer</title>'
        f'<style>{css}</style></head><body><main><h1>Bruno · Frontend Implementation Engineer</h1>'
        '<p class="lead">Bruno convierte la pieza aprobada en comportamiento real: props, eventos, estados, teclado, foco y ARIA. Te gustaron Código (1) y Del plano a la pieza (2). Estas cuatro trabajan sobre las dos: combinarlas, simplificarlas o reforzar la que mejor cuenta la implementación. Junto a Kiwi, Lima y Coco.</p>'
        f'<div class="fam"><span>{svg(KIWI)}<b>Kiwi</b></span><span>{svg(LIMA)}<b>Lima</b></span><span>{svg(COCO)}<b>Coco</b></span></div>'
        f'<div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'bruno.html'), 'w').write(html); print('ok')
