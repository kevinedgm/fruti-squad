# Nisa Nabani · panel de analítica (producto hermano de NisaLab), ronda 1 de nombres.
# Patrón de la familia: «Nisa» (Poppins 700) + palabra (Poppins 400), como NisaLab. Respaldo: «de Nisa Nabani».
# Uso: python3 gen.py <carpeta de fuentes> → nombres.html
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = sys.argv[1]
N = [  # palabra, idea, a favor, riesgo
    ('Pulso', 'El laboratorio tiene pulso: ritmo, salud y cambios en el tiempo.', 'Habla de salud y de tendencia a la vez; corto y en español.', 'Muy usado en apps de salud y finanzas; hay que verificar marca.'),
    ('Rumbo', 'Hacia dónde va el laboratorio: tendencias y dirección.', 'Distinto en el sector; sugiere decisión, no solo datos.', 'Habla de dirección más que de salud.'),
    ('Vista', 'Ver todo el laboratorio de un vistazo.', 'Se entiende sin explicación.', 'Genérico; difícil de registrar y de distinguir.'),
    ('Faro', 'Lo que guía: señala dónde hay problemas antes de que lleguen.', 'Metáfora clara de alerta temprana; memorable.', 'Más poético que técnico; no dice «datos».'),
    ('Métrica', 'Medir el laboratorio con indicadores.', 'Directo, de laboratorio y de analítica a la vez.', 'Largo junto a Nisa (11 letras); suena a herramienta, no a producto.'),
    ('Ritmo', 'El ritmo de trabajo: cuánto entra, cuánto sale, cuánto tarda.', 'Habla de flujo y tiempos, que es lo que mide el panel.', 'Puede leerse como música o deporte.'),
]
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700))
css = ff + '''
:root{--az:#052A76;--tinta:#141B33;--gris:#535B70;--borde:#DFE3EC}
*{box-sizing:border-box}body{margin:0;background:#F2F4F8;color:var(--tinta);font:400 14px/1.5 Poppins,sans-serif;padding:32px}
h1{font:700 26px/1.2 Poppins;color:var(--az);margin:0 0 4px}.lead{color:var(--gris);max-width:860px;margin:0 0 24px}
.g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.c{background:#fff;border:1px solid var(--borde);border-radius:14px;padding:22px;box-shadow:0 1px 2px rgba(20,27,51,.06);display:flex;flex-direction:column;gap:10px}
.wm{font:400 38px/1 Poppins;color:var(--az);letter-spacing:-.01em}.wm b{font-weight:700}.rs{font:500 12px/1 Poppins;color:var(--gris);margin-top:-2px}.rs b{font-weight:700;color:var(--az)}
.id{font-weight:500;margin:6px 0 0}.pr{margin:0;font-size:13px;color:var(--gris)}.pr span{font-weight:600;color:var(--tinta)}
.fam{margin-top:24px;background:#fff;border:1px solid var(--borde);border-radius:14px;padding:22px}.fam h2{font:600 12px/1 Poppins;letter-spacing:.06em;text-transform:uppercase;color:var(--gris);margin:0 0 16px}
.fr{display:flex;gap:40px;flex-wrap:wrap;align-items:baseline}.fr .wm{font-size:30px}
@media (max-width:1000px){.g{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:600px){.g{grid-template-columns:1fr}body{padding:16px}}
'''
cards = ''.join(f'<div class="c"><div class="wm"><b>Nisa</b>{w}</div><div class="rs">de <b>Nisa Nabani</b></div><p class="id">{i}</p><p class="pr"><span>A favor:</span> {a}</p><p class="pr"><span>Riesgo:</span> {r}</p></div>' for w, i, a, r in N)
fam = ''.join(f'<div class="wm"><b>Nisa</b>{w}</div>' for w in ('Lab', 'Pulso', 'Rumbo'))
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Nombres del panel</title><style>{css}</style><body>'
        '<h1>Panel de analítica · ronda 1 de nombres</h1><p class="lead">Producto hermano de NisaLab: lee los datos del laboratorio y muestra tendencias, comportamiento y salud. Sigue el patrón de la familia, «Nisa» + una palabra, para que se reconozca como de Nisa Nabani. Ninguno está verificado ante el IMPI.</p>'
        f'<div class="g">{cards}</div><div class="fam"><h2>Así se vería la familia</h2><div class="fr">{fam}</div></div></body></html>')
open(os.path.join(H, 'nombres.html'), 'w').write(html); print('ok')
