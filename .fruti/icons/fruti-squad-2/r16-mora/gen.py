# Fruti Squad · ronda 16 · Mora · Documentation & Knowledge Engineer (nombre dado por el usuario).
# Elegidos: Kiwi «Tres tamaños», Lima «Biblioteca», Coco «Visor», Bruno «Cierre». Mora documenta solo lo verificado: Design Hub, páginas,
# registro, cobertura, sincronía docs-código. Idioma: marcos redondeados trazo 3.5 + punto lleno.
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
def svg(b, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b.replace("§", c).replace("¤", "#fff" if c == INK else INK)}</svg>'
def d(x, y, r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="§"/>'
def fr(x, y, w, h, r, fill='none'): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" stroke="§" stroke-width="3.5" fill="{fill}"/>'
def ln(p, w=3.5): return f'<path d="{p}" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
KIWI = fr(4, 4, 56, 56, 12) + fr(13, 13, 38, 38, 9) + fr(21, 21, 22, 22, 6) + d(32, 32, 5.5)
LIMA = fr(20, 4, 40, 34, 9) + fr(12, 13, 40, 34, 9, '¤') + fr(4, 22, 40, 36, 9, '¤') + d(24, 40, 6)
COCO = ln('M4 18V12a8 8 0 0 1 8-8h6M46 4h6a8 8 0 0 1 8 8v6M60 46v6a8 8 0 0 1-8 8h-6M18 60h-6a8 8 0 0 1-8-8v-6') + fr(18, 18, 28, 28, 7) + d(32, 32, 5.5)
BRUNO = ('<path d="M27 4H16A12 12 0 0 0 4 16v32a12 12 0 0 0 12 12h3" stroke="§" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="5 5"/>'
         '<path d="M37 60h11a12 12 0 0 0 12-12V16A12 12 0 0 0 48 4h-3" stroke="§" stroke-width="3.5" stroke-linecap="round"/>' + ln('M38 6L26 58', 4) + d(44, 32, 5.5))
M = [
 ('Red de conocimiento', 'Dentro del marco, puntos unidos: cada pieza documentada se conecta con otras. Eso es ingeniería del conocimiento: no páginas sueltas, una red navegable.',
  'Dice «knowledge engineer» y vuelve al origen del sistema (puntos y enlaces); silueta distinta a todos.', 'Una red de puntos puede recordar iconos de «compartir», «moléculas» o la herramienta de selección poligonal.',
  fr(4, 4, 56, 56, 12) + ln('M19 19L44 21M44 21L45 45M44 21L20 44', 3) + d(19, 19, 6) + d(44, 21, 4.5) + d(45, 45, 4.5) + d(20, 44, 4.5)),
 ('Índice', 'Un marco con sus entradas; la primera, con el punto: lo que ya fue verificado entra a la documentación.',
  'La lectura más directa de «documentación»; ordenada como un Design Hub.', 'Se parece al icono genérico de «lista» o «documento».',
  fr(4, 4, 56, 56, 12) + d(18, 20, 5) + ln('M28 20h20') + ln('M18 32h30') + ln('M18 44h22')),
 ('Página viva', 'Una página con la esquina doblada y el punto dentro: la documentación que se sincroniza con lo que existe.',
  'Reconocible al instante como documento; la esquina doblada la distingue de los marcos de los demás.', 'La hoja con esquina doblada es el icono de «archivo» en todas partes.',
  '<path d="M44 4H16A12 12 0 0 0 4 16v32a12 12 0 0 0 12 12h32a12 12 0 0 0 12-12V20z" stroke="§" stroke-width="3.5" stroke-linejoin="round"/>' + ln('M44 6v8a6 6 0 0 0 6 6h8') + d(28, 36, 6)),
 ('Espejo', 'Dos marcos alineados, el código y su documentación, unidos punto a punto: lo que Mora mantiene sincronizado.',
  'Cuenta la regla de Mora (solo lo que existe y está en sincronía).', 'Dos marcos unidos se parecen al Evento que descartamos para Bruno.',
  fr(4, 10, 22, 44, 7) + fr(38, 10, 22, 44, 7) + ln('M26 24h12M26 40h12', 3) + d(15, 24, 4) + d(15, 40, 4) + d(49, 24, 4) + d(49, 40, 4)),
]
cards = ''.join(f'''<section class="c"><span class="n">{i+1}</span>{svg(b)}<div><h2>{t}</h2><p>{idea}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p>
<div class="sm"><span class="pq">{svg(b)}</span><span class="pq p24">{svg(b)}</span><span class="pq dk">{svg(b, "#fff")}</span><span class="pair">{svg(KIWI)}{svg(LIMA)}{svg(COCO)}{svg(BRUNO)}{svg(b)}<small>familia completa</small></span></div></div></section>''' for i, (t, idea, a, r, b) in enumerate(M))
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
        '<meta name="claude:viewport-fit-sides" content="true"><title>Mora · Documentation &amp; Knowledge Engineer</title>'
        f'<style>{css}</style></head><body><main><h1>Mora · Documentation &amp; Knowledge Engineer</h1>'
        '<p class="lead">Mora documenta solo lo que existe y fue verificado, y lo vuelve conocimiento navegable: Design Hub, páginas de componentes, registro, cobertura y sincronía entre documentación y código. Cuatro opciones en el idioma de la familia, vistas junto a los cuatro ya elegidos.</p>'
        f'<div class="fam"><span>{svg(KIWI)}<b>Kiwi</b></span><span>{svg(LIMA)}<b>Lima</b></span><span>{svg(COCO)}<b>Coco</b></span><span>{svg(BRUNO)}<b>Bruno</b></span></div>'
        f'<div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'mora.html'), 'w').write(html); print('ok')
