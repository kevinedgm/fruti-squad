# CLNDA · producto de restaurantes · ronda 1 de nombres (antes «Menú»; el producto resultó ser comandero local con plano de mesas).
# Uso: python3 gen.py → nombres.html
import os
H = os.path.dirname(os.path.abspath(__file__))
IND, INK, BG, NAR = '#4338ca', '#0e0f1c', '#f5f6fb', '#c2410c'
BR = 'M40 10 H36 a8 8 0 0 0 -8 8 V26 a6 6 0 0 1 -6 6 a6 6 0 0 1 6 6 V46 a8 8 0 0 0 8 8 H40'
SIM = f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="{BR}" stroke="{IND}" stroke-width="7" transform="translate(-3 0)"/><circle cx="46" cy="32" r="7" stroke="{NAR}" stroke-width="2.4"/><circle cx="46" cy="32" r="3" fill="{NAR}"/></svg>'
N = [  # nombre, qué nombra, a favor, riesgo, recomendado
    ('Comanda', 'El acto que hace el producto: tomar y enviar la orden.', 'Es la palabra que usa todo restaurante en México; nadie la confunde con la carta. Encaja en la familia C (la palabra del sector).', 'Suena a solo cocina: la cuenta, el plano y los reportes quedan implícitos.', True),
    ('Mesa', 'El centro del diseño: todo vive dentro de la mesa.', 'Corta, visual, coincide con la pantalla principal (el plano).', 'Puede leerse como «reservar mesa», que es otro producto.', False),
    ('Menú', 'El nombre elegido antes.', 'Ya está diseñado; se entiende en español e inglés.', 'Hace pensar en la carta que lee el comensal, no en la herramienta del mesero.', False),
    ('Salón', 'El espacio que se administra: plano, mesas, servicio.', 'Abarca todo el servicio, no solo la orden.', 'En México también es salón de belleza o de fiestas.', False),
]
cards = ''.join(f'<section class="c{" rec" if r else ""}">{"<span class=tag>Recomendado</span>" if r else ""}<div class="lk">{SIM}<span class="wm">CLNDA</span><span class="pw">{n}</span></div><p class="id">{i}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {k}</p></section>' for n, i, a, k, r in N)
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.55 'Space Grotesk',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto}}h1{{font:700 28px/1.2 'Space Grotesk';margin:0 0 6px}}.lead{{color:#4a4d63;max-width:840px;margin:0 0 22px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.c{{position:relative;background:#fff;border:1px solid #dfe1ec;border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:10px;min-width:0}}.c.rec{{border:2px solid {IND}}}
.tag{{position:absolute;top:16px;right:16px;font:500 11px 'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:.06em;color:#fff;background:{IND};border-radius:6px;padding:4px 8px}}
.lk{{display:flex;align-items:center;gap:6px;min-width:0;margin-top:4px}}.lk svg{{width:44px;height:44px;flex:none}}
.wm{{font:700 32px/1 'Space Grotesk';letter-spacing:-.015em}}.pw{{font:400 32px/1 'Space Grotesk';color:{NAR};overflow-wrap:anywhere}}
.id{{margin:0;font-weight:500}}.pr{{margin:0;font-size:14px;color:#4a4d63}}.pr b{{color:{INK};font-weight:600}}
.nota{{margin-top:16px;color:#4a4d63;font-size:14px;max-width:840px}}
@media (max-width:760px){{.g{{grid-template-columns:1fr}}.tag{{position:static;align-self:flex-start}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Nombre del comandero CLNDA</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>Producto de restaurantes · nombre</h1>'
        '<p class="lead">El producto resultó ser un comandero local: plano de mesas, órdenes con fotos y cuenta concentrada, gratis en la computadora del negocio y con nube de pago. El nombre tiene que decirle eso al dueño del restaurante. Símbolo (el plato) y color provisionales; ningún nombre verificado ante el IMPI.</p>'
        f'<div class="g">{cards}</div><p class="nota">Criterio: el nombre debe nombrar lo que el dueño compra (la operación del servicio), no lo que ve el comensal, y no chocar con otro producto de la familia (Booking ya cubre reservas).</p></main></body></html>')
open(os.path.join(H, 'nombres.html'), 'w').write(html); print('ok')
