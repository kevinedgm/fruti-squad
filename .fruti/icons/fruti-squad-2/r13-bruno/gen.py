# Fruti Squad · ronda 13 · Bruno (Frontend R3). Elegidos: Kiwi «Tres tamaños», Lima «Biblioteca», Coco «Visor» (usuario: «vamos con la 1»).
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
 ('Interruptor', 'El marco se vuelve un control: el punto cambió de lado. La pieza ya no solo se ve, ya responde.',
  'La lectura más clara de «comportamiento» y «estado»; usa marco + punto como los demás.', 'Es el icono estándar de un switch: lo propio está en las proporciones de la familia.',
  fr(4, 16, 56, 32, 16) + d(44, 32, 9)),
 ('Foco', 'La pieza con su anillo de foco alrededor: lo que hace Bruno que nadie más ve, que funcione con teclado y sea accesible.',
  'Muy propio (el anillo de foco es un detalle de oficio); conversa con los marcos de Kiwi.', 'Junto a la familia se parece a Coco (marco con esquinas alrededor) y a Kiwi (marcos dentro de marcos).',
  fr(3, 3, 58, 58, 15, 'none', ' stroke-dasharray="7 5"') + fr(13, 13, 38, 38, 9) + d(32, 32, 6)),
 ('Evento', 'Dos piezas unidas: el punto viaja de una a otra. Props que entran, eventos que salen.',
  'Cuenta «conectar» (la habilidad de Bruno en el squad) con marcos y punto.', 'Se lee como unos lentes o el icono de «vincular».',
  fr(4, 18, 20, 28, 6) + fr(40, 18, 20, 28, 6) + ln('M24 32h16') + d(32, 32, 5.5)),
 ('Pulso', 'El punto dentro del marco con ondas: la interacción que ocurre al tocar.',
  'Cuenta interacción y respuesta inmediata; dinámico, bueno para animar.', 'Es prácticamente el icono de wifi: descartable.',
  fr(4, 4, 56, 56, 12) + d(32, 36, 6) + '<path d="M22 28a14 14 0 0 1 20 0M16 21a23 23 0 0 1 32 0" stroke="§" stroke-width="3.5" stroke-linecap="round"/>'),
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
        '<meta name="claude:viewport-fit-sides" content="true"><title>Bruno · símbolo</title>'
        f'<style>{css}</style></head><body><main><h1>Bruno · Frontend</h1>'
        '<p class="lead">Bruno convierte la pieza aprobada en comportamiento real: props, eventos, estados, teclado, foco y ARIA. Cuatro opciones en el idioma de la familia, vistas junto a Kiwi, Lima y Coco. El nombre de producto de Bruno todavía es provisional.</p>'
        f'<div class="fam"><span>{svg(KIWI)}<b>Kiwi</b></span><span>{svg(LIMA)}<b>Lima</b></span><span>{svg(COCO)}<b>Coco</b></span></div>'
        f'<div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'bruno.html'), 'w').write(html); print('ok')
