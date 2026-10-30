# CLNDA Studio · productos · ronda 2: cómo se distingue cada producto (nombres elegidos: familia C · Booking, Shop, Menú).
# Tres sistemas: A color en el dato, B forma en el dato, C forma + color. La llave índigo no cambia: es lo que hace familia.
# Colores validados con el validador de dataviz (CVD deutan ≥ 10, todos ≥ 3:1 sobre blanco). Uso: python3 gen.py → productos.html
import os
H = os.path.dirname(os.path.abspath(__file__))
IND, INDD, INK, BG = '#4338ca', '#8b8cf8', '#0e0f1c', '#f5f6fb'
BR = 'M40 10 H36 a8 8 0 0 0 -8 8 V26 a6 6 0 0 1 -6 6 a6 6 0 0 1 6 6 V46 a8 8 0 0 0 8 8 H40'
PROD = [  # nombre, uso, color
    ('Booking', 'Reservas para hoteles', '#0891b2', 'cian'),
    ('Shop', 'Tienda en línea', '#db2777', 'rosa'),
    ('Menú', 'Restaurantes', '#ea580c', 'naranja'),
]
def glifo(p, c, bg):
    if p == 'Booking':   # hoja de calendario: encabezado lleno, argollas y cuerpo (y la calenda en «calendar»)
        return (f'<rect x="38.6" y="25.4" width="15" height="14" rx="3" stroke="{c}" stroke-width="2.4"/>'
                f'<path d="M38.6 28.4a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v2.6h-15z" fill="{c}"/><path d="M42.6 22.6v3.4M49.6 22.6v3.4" stroke="{c}" stroke-width="2.4"/>')
    if p == 'Shop':      # etiqueta de precio con su ojal
        return f'<path d="M38.5 27.2a2.4 2.4 0 0 1 2.4-2.4h7l6.4 7.2l-6.4 7.2h-7a2.4 2.4 0 0 1 -2.4-2.4z" fill="{c}"/><circle cx="48.2" cy="32" r="1.9" fill="{bg}"/>'
    return f'<circle cx="46" cy="32" r="7" stroke="{c}" stroke-width="2.4"/><circle cx="46" cy="32" r="3" fill="{c}"/>'  # plato
def sim(sistema, p, c, dark=False, tinta=False):
    ll = INK if tinta else (INDD if dark else IND); bg = INK if dark else '#fff'
    pt = INK if tinta else (BG if dark else INK)
    if sistema == 'A': g = f'<circle cx="46" cy="32" r="6.5" fill="{pt if tinta else c}"/>'
    elif sistema == 'B': g = glifo(p, pt, bg)
    else: g = glifo(p, pt if tinta else c, bg)
    return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="{BR}" stroke="{ll}" stroke-width="7" transform="translate(-3 0)"/>{g}</svg>'
SIS = [
    ('A', 'Color en el dato', 'La llave es la de siempre; el punto toma el color del producto.',
     'El cambio más pequeño: el símbolo sigue siendo el de CLNDA.', 'En una tinta o a 16 px los tres son idénticos: solo el color los distingue.'),
    ('B', 'Forma en el dato', 'El punto se vuelve un objeto del oficio: hoja de calendario, etiqueta de precio, plato. Todo en tinta.',
     'Se distinguen sin color (impresión, fax, sello) y cuentan qué hace cada uno.', 'Sin color propio, en el panel se confunden de lejos.'),
    ('C', 'Forma + color', 'El objeto del oficio en el color del producto; la llave índigo une a la familia.',
     'Doble señal: forma y color. El color sirve después para el panel (acento) y la venta.', 'Tres colores nuevos que gobernar; hay que fijar reglas para que no compitan con el índigo.'),
]
def lock(s, p, c):
    col = c if s != 'B' else IND
    return f'<div class="lk">{sim(s, p, c)}<span class="wm">CLNDA</span><span class="pw" style="color:{col}">{p}</span></div>'
def fila(s, p, u, c):
    return (f'<li><span class="pp">{u}</span>{lock(s, p, c)}<div class="mini">'
            f'<span class="t s24">{sim(s, p, c)}</span><span class="t s16">{sim(s, p, c)}</span>'
            f'<span class="t dk">{sim(s, p, c, dark=True)}</span><span class="t">{sim(s, p, c, tinta=True)}</span></div></li>')
def card(k, t, i, a, r):
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{t}</h2></header><p class="id">{i}</p>'
            f'<ul>{"".join(fila(k, p, u, c) for p, u, c, _ in PROD)}</ul>'
            f'<p class="leg">Pequeños: 24 px · 16 px · sobre tinta · una tinta</p>'
            f'<p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
sw = ''.join(f'<span class="sw"><i style="background:{c}"></i><b>{p}</b> {n} {c}</span>' for p, _, c, n in PROD)
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.55 'Space Grotesk',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto}}h1{{font:700 28px/1.2 'Space Grotesk';margin:0 0 6px}}.lead{{color:#4a4d63;max-width:840px;margin:0 0 14px}}
.pal{{display:flex;flex-wrap:wrap;gap:8px 18px;margin:0 0 22px;font-size:13.5px;color:#4a4d63}}.sw{{display:inline-flex;align-items:center;gap:6px}}.sw i{{width:14px;height:14px;border-radius:4px;display:inline-block}}.sw b{{color:{INK};font-weight:600}}
.g{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.c{{background:#fff;border:1px solid #dfe1ec;border-radius:16px;padding:20px;display:flex;flex-direction:column;gap:10px;min-width:0;box-shadow:0 1px 2px rgba(14,15,28,.04)}}
.c header{{display:flex;gap:10px;align-items:center}}.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:700}}
h2{{font:600 18px/1.2 'Space Grotesk';margin:0}}.id{{margin:0;color:#4a4d63;font-size:14px}}
ul{{list-style:none;margin:4px 0 0;padding:0;display:grid;gap:12px}}li{{border-top:1px solid #eceef5;padding-top:10px}}
.pp{{display:block;font:500 11px/1 'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:.06em;color:#5b5e73;margin-bottom:6px}}
.lk{{display:flex;align-items:center;gap:6px;min-width:0}}.lk svg{{width:40px;height:40px;flex:none;margin-right:-2px}}
.wm{{font:700 26px/1 'Space Grotesk';letter-spacing:-.015em}}.pw{{font:400 26px/1 'Space Grotesk'}}
.mini{{display:flex;gap:8px;align-items:center;margin-top:8px}}.t{{width:34px;height:34px;border-radius:8px;border:1px solid #eceef5;display:grid;place-items:center}}.t svg{{width:26px;height:26px}}
.t.s24 svg{{width:24px;height:24px}}.t.s16 svg{{width:16px;height:16px}}.t.dk{{background:{INK};border-color:{INK}}}
.leg{{margin:0;font:500 11px/1.4 'JetBrains Mono',monospace;color:#5b5e73}}
.pr{{margin:0;font-size:13.5px;color:#4a4d63}}.pr b{{color:{INK};font-weight:600}}
@media (max-width:920px){{.g{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Productos CLNDA · ronda 2</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main>'
        '<h1>CLNDA Booking, Shop y Menú · cómo se distingue cada uno</h1>'
        '<p class="lead">La llave índigo no cambia: es lo que hace familia. Lo que varía es el dato, el punto de la derecha. Tres sistemas para comparar, cada uno en grande, a 24 y 16 px, sobre tinta y en una sola tinta. Los colores son una primera propuesta, probada para daltonismo.</p>'
        f'<div class="pal">{sw}</div>'
        f'<div class="g">{"".join(card(*s) for s in SIS)}</div></main></body></html>')
open(os.path.join(H, 'productos.html'), 'w').write(html); print('ok')
