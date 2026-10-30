# Producto de restaurantes de CLNDA Studio · ronda 2 de nombres: nombre y símbolo propios, respaldado por «de CLNDA Studio».
# Usuario: «que tenga un nombre y un símbolo propio». Criterios: fácil de decir en español, corto, que cuente el servicio o «pocos clics».
# Uso: python3 gen.py → nombres.html
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#0e0f1c', '#f5f6fb'
N = [  # nombre, idea, a favor, riesgo, recomendado
    ('Toque', '«A un toque»: pedir tocando fotos. Y el toque blanco es el gorro del chef.',
     'Cuenta el concepto del producto (pocos clics) y el oficio en una palabra; corta y fácil de decir.', 'Palabra común: registrarla sola puede costar; quizá necesite un apellido («Toque Restaurante»).', True),
    ('Ronda', 'La ronda del mesero por las mesas y «otra ronda» en la mesa. Eco de la calenda, que da la vuelta al pueblo.',
     'Cálida, social, muy mexicana; el círculo da símbolo fácil.', 'Más de bar que de restaurante; no dice «orden» ni «rápido».', False),
    ('Comal', 'El comal: redondo, al centro de la cocina mexicana, siempre caliente.',
     'Propia de Oaxaca y de México; nadie la olvida.', 'Suena a cocina tradicional, no a software moderno; ya hay muchos restaurantes llamados Comal.', False),
    ('Pase', 'El pase: la ventana donde la cocina entrega los platos al mesero.',
     'Palabra de oficio: quien trabaja en restaurante la reconoce; cuenta el momento clave (la orden sale bien).', 'El dueño que no viene de cocina puede no entenderla.', False),
    ('Sobremesa', 'El rato después de comer, cuando ya nadie tiene prisa.',
     'La más evocadora: promete que el servicio fluye sin estrés.', 'Larga (4 sílabas) y habla del final, no de la operación.', False),
]
cards = ''.join(f'<section class="c{" rec" if r else ""}">{"<span class=tag>Recomendado</span>" if r else ""}<div class="nm">{n}</div><span class="by">de <b>CLNDA</b> Studio</span>'
                f'<p class="id">{i}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {k}</p></section>' for n, i, a, k, r in N)
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.55 'Space Grotesk',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto}}h1{{font:700 28px/1.2 'Space Grotesk';margin:0 0 6px}}.lead{{color:#4a4d63;max-width:860px;margin:0 0 22px}}
.g{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.c{{position:relative;background:#fff;border:1px solid #dfe1ec;border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:8px;min-width:0}}.c.rec{{border:2px solid {INK}}}
.tag{{position:absolute;top:16px;right:16px;font:500 11px 'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:.06em;color:#fff;background:{INK};border-radius:6px;padding:4px 8px}}
.nm{{font:700 40px/1.05 'Space Grotesk';letter-spacing:-.02em;overflow-wrap:anywhere;margin-top:6px}}.by{{font-size:13px;color:#5b5e73;margin-bottom:6px}}.by b{{color:{INK}}}
.id{{margin:0;font-weight:500}}.pr{{margin:0;font-size:14px;color:#4a4d63}}.pr b{{color:{INK};font-weight:600}}
.nota{{background:#fff;border:1px solid #dfe1ec;border-radius:16px;padding:20px 22px;color:#4a4d63;font-size:14px;display:grid;gap:6px}}.nota b{{color:{INK}}}
@media (max-width:980px){{.g{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}@media (max-width:640px){{.g{{grid-template-columns:1fr}}.tag{{position:static;align-self:flex-start}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Nombre propio del comandero</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>Producto de restaurantes · nombre propio</h1>'
        '<p class="lead">Ya no «CLNDA + palabra»: el producto tiene nombre y símbolo propios, y CLNDA Studio lo respalda como firma («de CLNDA Studio»). Aquí solo se elige el nombre; el símbolo y el color nacen de él en la siguiente ronda. Tipografía neutra a propósito. Ningún nombre verificado ante el IMPI.</p>'
        f'<div class="g">{cards}<div class="nota"><b>Criterio</b><span>1. Se dice fácil en español, en voz alta, en un restaurante con ruido.</span><span>2. Cuenta el servicio o la promesa «pocos clics».</span><span>3. Da un símbolo propio, distinto de la llave de CLNDA.</span><span>4. No suena a la app vieja ni a software genérico.</span></div></div></main></body></html>')
open(os.path.join(H, 'nombres.html'), 'w').write(html); print('ok')
