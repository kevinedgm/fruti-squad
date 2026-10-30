# Mesanda · ronda 4 de color: paleta por psicología del color (usuario: «usa psicología del color, una paleta más acorde»).
# Paleta por funciones, no por gusto: apetito (rojo), atención (maíz), confianza (carbón), hospitalidad (masa).
# Dos variantes del rojo: Chile (terroso) y Jamaica (moderno). Uso: python3 gen.py → color.html
import os
H = os.path.dirname(os.path.abspath(__file__))
CARB, MASA, MAIZ, MAIZ_TX = '#1f1a17', '#faf5ec', '#f2b632', '#7a5a00'
def lum(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def cr(a, b): x, y = sorted((lum(a), lum(b))); return (y + .05) / (x + .05)
MESA = '<circle cx="38" cy="32" r="14" fill="§"/><rect x="30" y="7" width="16" height="7" rx="3.5" fill="§"/><rect x="30" y="50" width="16" height="7" rx="3.5" fill="§"/><rect x="56" y="24" width="7" height="16" rx="3.5" fill="§"/>'
EST = '<path d="M6 26h8M3 32h11M6 38h8" stroke="#" stroke-width="4.5"/>'
def sim(mesa, estela): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round">{MESA.replace("§", mesa)}{EST.replace("#", estela)}</svg>'
V = [
 ('A', 'Chile', '#9f1d2b', 'Rojo de chile seco y barro: terroso, mexicano, de cocina de verdad.'),
 ('B', 'Jamaica', '#a3195b', 'Rojo de agua de jamaica: igual de apetitoso, más moderno y menos visto en restaurantes.'),
]
def roles(rojo, nrojo):
    R = [
     (rojo, nrojo, 'Apetito y calidez', 'Identidad: símbolo, app icon, publicidad. Nunca en la interfaz (ahí el rojo es error).', 'Asociación aprendida fuerte: en México rojo + amarillo = comida. El efecto fisiológico «el rojo da hambre» tiene evidencia débil.'),
     (MAIZ, 'Maíz', 'Atención sin alarma', 'La estela del símbolo y, en la interfaz, lo que necesita al mesero: «cuenta pedida».', 'El amarillo es el color que el ojo detecta primero (alta luminosidad); por eso se usa en señalización. Nunca como texto sobre claro: para texto, ' + MAIZ_TX + '.'),
     (CARB, 'Carbón', 'Confianza y orden', 'El producto: texto, botón principal («Enviar a cocina»), mesas ocupadas.', 'Neutro oscuro y cálido: seriedad de sistema de caja sin la frialdad del azul (al que se le atribuye, también con evidencia débil, quitar apetito).'),
     (MASA, 'Masa', 'Hospitalidad', 'Fondo de la app y de los materiales: crema en vez de blanco puro.', 'Cálido y menos deslumbrante en jornadas largas; refuerza la temperatura «de cocina» de la marca.'),
    ]
    return ''.join(f'<tr><td><span class="sw" style="background:{c}"></span></td><td><b>{n}</b><br><code>{c}</code></td><td><b>{p}</b><br>{u}</td><td class="ev">{e}</td></tr>' for c, n, p, u, e in R)
def plano():
    def mesa(n, fill, tx, label, extra=''):
        return f'<div class="m" style="background:{fill};color:{tx};{extra}"><b>{n}</b><span>{label}</span></div>'
    return ('<div class="plano">' + mesa('1', '#fff', CARB, 'Libre', f'border:2px dashed #b9b0a3') + mesa('2', CARB, '#fff', 'Ocupada · 3') +
            mesa('3', MAIZ, CARB, '⏵ Cuenta pedida') + mesa('4', CARB, '#fff', 'Ocupada · 2') + '</div>')
def card(k, n, rojo, idea):
    return (f'<section class="c"><header><span class="k">{k}</span><h2>Mesa mexicana · {n}</h2></header><p class="id">{idea}</p>'
            f'<div class="row"><div class="cell" style="background:{MASA}">{sim(rojo, MAIZ_TX)}<span class="nm" style="color:{CARB}">Mesanda</span></div>'
            f'<div class="cell" style="background:{rojo}">{sim("#ffffff", MAIZ)}<span class="nm" style="color:#fff">Mesanda</span></div></div>'
            f'<div class="mini"><span class="ap" style="background:{rojo}">{sim("#ffffff", MAIZ)}</span><span class="ap" style="background:{CARB}">{sim(MASA, MAIZ)}</span>'
            f'<span class="btn">Enviar a cocina</span><span class="ct">{rojo} sobre masa {cr(rojo, MASA):.1f}:1 · blanco sobre {rojo} {cr("#ffffff", rojo):.1f}:1</span></div>'
            f'<table><thead><tr><th></th><th>Color</th><th>Función y uso</th><th>Por qué (y qué tan sólido es)</th></tr></thead><tbody>{roles(rojo, n)}</tbody></table>'
            f'<p class="lb">Así se reparten en la interfaz (el rojo no aparece):</p>{plano()}</section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{MASA};color:{CARB};font:400 15px/1.55 'Manrope',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto}}h1{{font:800 28px/1.2 'Manrope';margin:0 0 6px}}.lead{{color:#5a5048;max-width:900px;margin:0 0 22px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.c{{background:#fff;border:1px solid #e8e0d2;border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:12px;min-width:0}}
.c header{{display:flex;gap:10px;align-items:center}}.k{{width:28px;height:28px;border-radius:8px;background:{CARB};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font:700 18px 'Manrope';margin:0}}.id{{margin:0;color:#5a5048}}
.row{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}.cell{{border:1px solid #efe7da;border-radius:12px;padding:14px;display:flex;align-items:center;gap:8px;min-width:0}}
.cell svg{{width:38px;height:38px;flex:none}}.nm{{font:800 24px/1 'Manrope';letter-spacing:-.025em;overflow-wrap:anywhere}}
.mini{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}.ap{{width:52px;height:52px;border-radius:13px;display:grid;place-items:center}}.ap svg{{width:34px;height:34px}}
.btn{{background:{CARB};color:#fff;border-radius:10px;padding:10px 16px;font-weight:700;font-size:14px}}.ct{{font:600 12px ui-monospace,monospace;color:#6b6157}}
table{{width:100%;border-collapse:collapse;font-size:13px}}th{{text-align:left;font:700 11px 'Manrope';text-transform:uppercase;letter-spacing:.05em;color:#6b6157;padding:6px 6px;border-bottom:1px solid #efe7da}}
td{{padding:8px 6px;border-bottom:1px solid #f3ede3;vertical-align:top}}td code{{font-size:11.5px;color:#6b6157}}.sw{{display:block;width:22px;height:22px;border-radius:6px;border:1px solid rgba(0,0,0,.1)}}.ev{{color:#5a5048}}
.lb{{margin:0;font-weight:700;font-size:13px}}.plano{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;background:{MASA};border-radius:12px;padding:12px}}
.m{{border-radius:12px;padding:10px;min-height:70px;display:flex;flex-direction:column;justify-content:space-between;font-size:12.5px;font-weight:600}}.m b{{font-size:18px}}
@media (max-width:980px){{.g{{grid-template-columns:1fr}}}}@media (max-width:560px){{.row{{grid-template-columns:1fr}}.plano{{grid-template-columns:1fr 1fr}}table,thead,tbody,tr,td,th{{display:block}}thead{{display:none}}tr{{display:grid;grid-template-columns:30px 1fr;gap:4px 8px;padding:8px 0;border-bottom:1px solid #efe7da}}td{{border:0;padding:0}}td:nth-child(3),td:nth-child(4){{grid-column:2}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Color de Mesanda · psicología</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>Mesanda · paleta por psicología del color</h1>'
        '<p class="lead">Una paleta por funciones: cada color tiene un trabajo (apetito, atención, confianza, hospitalidad) y un lugar donde se usa. Lo que ya decidimos se mantiene: nada de naranja, y el color de marca no compite con los estados de las mesas. Dos variantes del rojo; el resto es igual. Para cada color se indica qué tan sólida es la evidencia.</p>'
        f'<div class="g">{"".join(card(*v) for v in V)}</div></main></body></html>')
open(os.path.join(H, 'color.html'), 'w').write(html); print('ok')
