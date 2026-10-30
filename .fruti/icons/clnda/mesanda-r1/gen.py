# Mesanda (de CLNDA Studio) · ronda 1 de símbolo. Nombre elegido 2026-10-30: mesa + comanda, «la mesa anda».
# Símbolos en tinta a propósito: se decide la forma sin que el color la secuestre; el color va en la ronda 2 (evitar el naranja del competidor).
# Uso: python3 gen.py → simbolos.html
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#14161f', '#f6f6f3'
def s(body, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round">{body.replace("§", c)}</svg>'
S = [
 ('A', 'La mesa en el plano', 'Una mesa con sus cuatro sillas, vista desde arriba: es la pantalla principal del producto.',
  'Se entiende sin explicar; funciona a 16 px; une marca e interfaz (el mismo dibujo es el plano).', 'Otros sistemas de restaurante usan dibujos de mesa; hay que cuidar que el trazo sea propio.',
  '<circle cx="32" cy="32" r="14" fill="§"/><rect x="24" y="7" width="16" height="7" rx="3.5" fill="§"/><rect x="24" y="50" width="16" height="7" rx="3.5" fill="§"/><rect x="7" y="24" width="7" height="16" rx="3.5" fill="§"/><rect x="50" y="24" width="7" height="16" rx="3.5" fill="§"/>'),
 ('B', 'La ruta del mesero', 'Una M trazada como el recorrido entre mesas: «la mesa anda».',
  'Monograma propio: la inicial y el concepto en un trazo.', 'A 16 px los puntos se funden; necesita versión simplificada.',
  '<path d="M13 47V20l19 21 19-21v27" stroke="§" stroke-width="7"/><circle cx="13" cy="47" r="6" fill="§"/><circle cx="32" cy="41" r="6" fill="§"/><circle cx="51" cy="47" r="6" fill="§"/>'),
 ('C', 'Dos campanas, una m', 'Dos campanas de servicio forman la «m» minúscula.',
  'La más memorable: se lee letra y servicio a la vez; el icono de comida más universal, dicho de otra forma.', 'La campana sugiere restaurante elegante; a algunos negocios informales puede sonarles lejana.',
  '<path d="M9 45a11.5 13 0 0 1 23 0M32 45a11.5 13 0 0 1 23 0" stroke="§" stroke-width="6.5"/><path d="M6 47h52" stroke="§" stroke-width="6.5"/><circle cx="20.5" cy="25.5" r="3.6" fill="§"/><circle cx="43.5" cy="25.5" r="3.6" fill="§"/>'),
 ('D', 'La mesa que anda', 'Una mesa en movimiento: el servicio fluye.',
  'Cuenta la promesa (rapidez) con un gesto simple.', 'Las líneas de velocidad son un recurso visto en apps de entrega.',
  '<circle cx="39" cy="32" r="15" fill="§"/><path d="M8 24h12M5 32h12M8 40h12" stroke="§" stroke-width="5.5"/>'),
]
def card(k, t, i, a, r, b):
    big = s(b); inv = s(b, '#ffffff')
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{t}</h2></header>'
            f'<div class="lk"><span class="sym">{big}</span><span class="nm">Mesanda</span></div><span class="by">de <b>CLNDA</b> Studio</span>'
            f'<div class="mini"><span class="t">{big}</span><span class="t s24">{big}</span><span class="t s16">{big}</span><span class="t ap">{inv}</span></div>'
            f'<p class="id">{i}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.55 'Manrope',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto}}h1{{font:800 28px/1.2 'Manrope';margin:0 0 6px}}.lead{{color:#4b4e5a;max-width:860px;margin:0 0 22px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.c{{background:#fff;border:1px solid #e3e3dc;border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:10px;min-width:0}}
.c header{{display:flex;gap:10px;align-items:center}}.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font:700 18px 'Manrope';margin:0}}
.lk{{display:flex;align-items:center;gap:12px;margin-top:6px;min-width:0}}.sym svg{{width:56px;height:56px;display:block}}.nm{{font:800 40px/1 'Manrope';letter-spacing:-.025em}}
.by{{font-size:13px;color:#5d606b;margin:-4px 0 0 68px}}.by b{{color:{INK}}}
.mini{{display:flex;gap:8px;align-items:center}}.t{{width:40px;height:40px;border-radius:10px;border:1px solid #ecece6;display:grid;place-items:center}}.t svg{{width:32px;height:32px}}.t.s24 svg{{width:24px;height:24px}}.t.s16 svg{{width:16px;height:16px}}
.t.ap{{background:{INK};border-color:{INK}}}.t.ap svg{{width:24px;height:24px}}
.id{{margin:0;font-weight:600}}.pr{{margin:0;font-size:14px;color:#4b4e5a}}.pr b{{color:{INK}}}
@media (max-width:820px){{.g{{grid-template-columns:1fr}}.nm{{font-size:32px}}.by{{margin-left:0}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Símbolo de Mesanda</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>Mesanda · ronda 1 de símbolo</h1>'
        '<p class="lead">Cuatro ideas para el símbolo, todas en tinta a propósito: primero se elige la forma y después el color (que no será naranja, para no parecerse a la app vieja). Cada una en grande, a 32, 24 y 16 px, y como app icon. Tipografía provisional.</p>'
        f'<div class="g">{"".join(card(*x) for x in S)}</div></main></body></html>')
open(os.path.join(H, 'simbolos.html'), 'w').write(html); print('ok')
