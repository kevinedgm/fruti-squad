# Portal de clientes · ronda 3 de nombres: claros, en español, que coincidan con el subdominio.
# El sello de la página pública usa la empresa («Nisa Nabani», el laboratorio), no el nombre del producto.
# Uso: python3 gen.py <carpeta de fuentes> → nombres.html
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = sys.argv[1]
N = [  # logotipo (html), subdominio, juego de palabras, a favor, riesgo
    ('<b>Nisa</b>Claro', 'nisaclaro.nisanabani.com', '«Más claro, ni el agua»: transparencia y agua limpia, con Nisa por delante.', 'Español, positivo; cuenta la idea del QR para el huésped.', 'Habla mucho de agua; el portal también tiene alimentos, bebidas y más.'),
    ('<b>Nisa</b>Ver', 'nisaver.nisanabani.com', 'Se oye como «a ver»: «a ver mis resultados». Nisa + ver.', 'Corto, natural, se dice como se escribe.', 'Muy simple; puede leerse «Nisa ver» sin el juego.'),
    ('Con<b>Nisa</b>', 'connisa.nisanabani.com', '«Consulta» + «con Nisa»: tus resultados, con Nisa.', 'Se entiende en una frase: «revísalo en ConNisa».', 'La doble n puede escribirse mal (conisa).'),
    ('<b>Nis</b>Avisa', 'nisavisa.nisanabani.com', '«Nisa avisa»: el portal te avisa cuando hay resultados nuevos.', 'Juego claro y simpático; promete una función útil.', 'Se centra en avisos, no en consulta; la «a» compartida confunde al escribirlo.'),
    ('<b>Nisa</b>quí', 'nisaqui.nisanabani.com', '«Nisa aquí»: aquí están tus resultados.', 'Cercano, muy mexicano.', 'El acento en la dirección no existe (nisaqui); informal para algunos clientes.'),
    ('<b>Nísa</b>lo', 'nisalo.nisanabani.com', 'Como «googléalo»: un verbo. «¿Tu informe? Nísalo».', 'Memorable; la marca se vuelve acción.', 'Juguetón; el acento se pierde en la dirección.'),
]
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700)) + f"@font-face{{font-family:'IBM Plex Mono';src:url('file://{F}/IBMPlexMono.ttf')}}"
css = ff + '''
*{box-sizing:border-box}body{margin:0;background:#F2F4F8;color:#141B33;font:400 14px/1.5 Poppins,sans-serif;padding:32px}
h1{font:700 26px/1.2 Poppins;color:#052A76;margin:0 0 4px}.lead{color:#535B70;max-width:880px;margin:0 0 24px}
.g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.c{background:#fff;border:1px solid #DFE3EC;border-radius:14px;padding:22px;display:flex;flex-direction:column;gap:10px;min-width:0}
.wm{font:400 38px/1 Poppins;color:#052A76;letter-spacing:-.01em}.wm b{font-weight:700}.url{font:500 13px 'IBM Plex Mono',monospace;background:#EEF1F6;border-radius:8px;padding:6px 10px;align-self:flex-start;overflow-wrap:anywhere}
.id{font-weight:500;margin:4px 0 0}.pr{margin:0;font-size:13px;color:#535B70}.pr span{font-weight:600;color:#141B33}
.sello{margin-top:24px;background:#fff;border:1px solid #DFE3EC;border-radius:14px;padding:22px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);gap:24px;align-items:center}
.sello h2{font:600 12px/1 Poppins;letter-spacing:.06em;text-transform:uppercase;color:#535B70;margin:0 0 10px}.sello p{margin:0;color:#535B70}
.qr{border:1px solid #DFE3EC;border-radius:16px;padding:16px;display:grid;gap:10px}.hotel{font:600 20px Poppins}.sl{display:inline-flex;gap:8px;align-items:center;border:1px dashed #9AA1B1;border-radius:999px;padding:6px 14px;font-size:13px;color:#535B70;justify-self:start}.sl b{color:#052A76}
@media (max-width:900px){.g,.sello{grid-template-columns:1fr}}@media (max-width:480px){body{padding:16px}}
'''
cards = ''.join(f'<div class="c"><div class="wm">{w}</div><span class="url">{u}</span><p class="id">{i}</p><p class="pr"><span>A favor:</span> {a}</p><p class="pr"><span>Riesgo:</span> {r}</p></div>' for w, u, i, a, r in N)
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Nombres del portal</title><style>{css}</style><body>'
        '<h1>Portal de clientes · ronda 3 de nombres</h1><p class="lead">Juegos de palabras con Nisa, en español y fáciles de decir; el nombre es también la dirección dentro del sitio de Nisa Nabani. Ninguno está verificado ante el IMPI.</p>'
        f'<div class="g">{cards}</div>'
        '<div class="sello"><div><h2>El sello de la página pública</h2><p>El huésped no conoce los productos de Nisa, pero sí entiende «laboratorio». Por eso el sello usa la empresa, no el nombre del portal: así el nombre del portal solo tiene que funcionar para el cliente.</p></div>'
        '<div class="qr"><span class="hotel">Hotel Las Palmas · Calidad del agua</span><span>Alberca · Habitaciones · Regaderas</span><span class="sl">Analizada por <b>Nisa Nabani</b> · laboratorio</span></div></div></body></html>')
open(os.path.join(H, 'nombres.html'), 'w').write(html); print('ok')
