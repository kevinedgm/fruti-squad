# Fruti Squad · ronda 14 · Bruno. Usuario: «Bruno · Frontend Implementation Engineer» (nombre de producto). Ronda 13 de referencia. Elegidos: Kiwi «Tres tamaños», Lima «Biblioteca», Coco «Visor» (usuario: «vamos con la 1»).
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
B = [
 ('Código', 'La pieza entre los signos de una etiqueta: &lt;Componente /&gt;. Bruno la convierte en código de frontend real.',
  'La lectura más directa de «Frontend Engineer» para quien compra en un marketplace de agentes; el marco con el punto la mete en la familia.', 'Los signos &lt; &gt; son el icono genérico de «código», y en pequeño el conjunto puede leerse como un ojo.',
  ln('M15 18L4 32l11 14M49 18l11 14-11 14', 4) + fr(20, 20, 24, 24, 6) + d(32, 32, 5)),
 ('Del plano a la pieza', 'Medio marco punteado (el plano aprobado) y medio sólido (lo implementado): Bruno vuelve real lo que Kiwi, Lima y Coco definieron.',
  'Cuenta «implementation» y su lugar exacto en el flujo de la squad; muy propio.', 'A 16 px el punteado casi desaparece y se ve como un marco con una muesca.',
  '<path d="M32 4H16A12 12 0 0 0 4 16v32a12 12 0 0 0 12 12h16" stroke="§" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="5 5"/><path d="M32 4h16a12 12 0 0 1 12 12v32a12 12 0 0 1-12 12H32" stroke="§" stroke-width="3.5" stroke-linecap="round"/>' + d(32, 32, 6)),
 ('Interruptor', 'El marco se vuelve un control: la pieza ya responde y cambia de estado.',
  'Comportamiento y estado; la silueta más distinta de la familia (cápsula).', 'Es el icono estándar de un switch; dice «comportamiento» más que «ingeniería».',
  fr(4, 16, 56, 32, 16) + d(44, 32, 9)),
 ('Ensamble', 'Dos mitades de un marco que encajan y el punto como tornillo que las une: ingeniería, piezas que se montan.',
  'Dice «construir» e «ingeniería» sin herramientas literales.', 'Se parece demasiado al logotipo de una consola de videojuegos conocida (dos mitades encajadas): descartable.',
  '<path d="M28 6H16A12 12 0 0 0 4 18v28a12 12 0 0 0 12 12h12V40h-4a8 8 0 0 1 0-16h4z" stroke="§" stroke-width="3.5" stroke-linejoin="round"/><path d="M36 6h12a12 12 0 0 1 12 12v28a12 12 0 0 1-12 12H36V40" stroke="§" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M36 24V6" stroke="§" stroke-width="3.5" stroke-linecap="round"/>' + d(32, 32, 6)),
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
        '<p class="lead">Bruno convierte la pieza aprobada en comportamiento real: props, eventos, estados, teclado, foco y ARIA. Nombre de producto: Frontend Implementation Engineer. Como con los demás, el símbolo tiene que contar el nombre completo: frontend, implementación e ingeniería. Cuatro opciones en el idioma de la familia, junto a Kiwi, Lima y Coco.</p>'
        f'<div class="fam"><span>{svg(KIWI)}<b>Kiwi</b></span><span>{svg(LIMA)}<b>Lima</b></span><span>{svg(COCO)}<b>Coco</b></span></div>'
        f'<div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'bruno.html'), 'w').write(html); print('ok')
