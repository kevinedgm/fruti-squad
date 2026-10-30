# CLNDA Booking, Shop y Menú · paquete final (sistema C de la ronda 2: forma + color).
# La llave índigo de CLNDA no cambia; el dato se vuelve el objeto del oficio en el color del producto.
# Uso: python3 gen.py <carpeta con SpaceGrotesk[wght].ttf> → <producto>/svg/*.svg, tema.json, lamina.html
import sys, os, json
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
H = os.path.dirname(os.path.abspath(__file__)); FD = sys.argv[1]
BG, INK, IND, INDD = '#f5f6fb', '#0e0f1c', '#4338ca', '#8b8cf8'
P = {  # clave: nombre, uso, marca (≥3:1 sobre blanco), texto (≥4.5:1 sobre blanco), oscuro (sobre tinta)
    'booking': ('Booking', 'Reservas para hoteles', '#0891b2', '#0e7490', '#22d3ee'),
    'shop':    ('Shop', 'Tienda en línea', '#db2777', '#be185d', '#f472b6'),
    'menu':    ('Menú', 'Restaurantes', '#ea580c', '#c2410c', '#fb923c'),
}
def lum(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def cr(a, b): x, y = sorted((lum(a), lum(b))); return round((y + .05) / (x + .05), 2)
# fuentes en trazados
def inst(w):
    p = f'/tmp/clnda-sg{w}.ttf'
    if not os.path.exists(p): instancer.instantiateVariableFont(TTFont(FD + '/SpaceGrotesk[wght].ttf'), {'wght': w}).save(p)
    return p
FT = {w: (inst(w), TTFont(inst(w))) for w in (400, 700)}
def palabra(s, size, x0, y0, w=700, track=0):
    path, font = FT[w]; upm = font['head'].unitsPerEm
    hf = hb.Font(hb.Face(hb.Blob.from_file_path(path))); b = hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf, b, {'kern': True})
    gs = font.getGlyphSet(); order = font.getGlyphOrder(); k = size / upm; x = x0; d = ''
    for i, ps in zip(b.glyph_infos, b.glyph_positions):
        pen = SVGPathPen(gs); gs[order[i.codepoint]].draw(TransformPen(pen, (k, 0, 0, -k, x, y0))); d += pen.getCommands(); x += ps.x_advance * k + track
    return d, x
def svg(body, vb): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
BR = 'M40 10 H36 a8 8 0 0 0 -8 8 V26 a6 6 0 0 1 -6 6 a6 6 0 0 1 6 6 V46 a8 8 0 0 0 8 8 H40'
BR16 = 'M38 10 H36 a9 9 0 0 0 -9 9 V25 a7 7 0 0 1 -7 7 a7 7 0 0 1 7 7 V45 a9 9 0 0 0 9 9 H38'
def glifo(k, c, bg, sw=2.4):
    if k == 'booking':   # hoja de calendario: encabezado lleno, argollas y cuerpo
        return (f'<rect x="38.6" y="25.4" width="15" height="14" rx="3" stroke="{c}" stroke-width="{sw}"/>'
                f'<path d="M38.6 28.4a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v2.6h-15z" fill="{c}"/><path d="M42.6 22.6v3.4M49.6 22.6v3.4" stroke="{c}" stroke-width="{sw}"/>')
    if k == 'shop':      # etiqueta de precio con su ojal
        return f'<path d="M38.5 27.2a2.4 2.4 0 0 1 2.4-2.4h7l6.4 7.2l-6.4 7.2h-7a2.4 2.4 0 0 1 -2.4-2.4z" fill="{c}"/><circle cx="48.2" cy="32" r="1.9" fill="{bg}"/>'
    return f'<circle cx="46" cy="32" r="7" stroke="{c}" stroke-width="{sw}"/><circle cx="46" cy="32" r="3" fill="{c}"/>'  # plato
def symb(k, ll, c, bg):
    return f'<path d="{BR}" stroke="{ll}" stroke-width="7" transform="translate(-3 0)"/>{glifo(k, c, bg)}'
def symb16(k, ll, c, bg):  # trazo más grueso y objeto más grande, para 16–24 px
    return (f'<path d="{BR16}" stroke="{ll}" stroke-width="9" transform="translate(-3 0)"/>'
            f'<g transform="translate(46 32) scale(1.22) translate(-46 -32)">{glifo(k, c, bg, 3.2)}</g>')
def lockup(k, nombre, wk, ll, c, bg):
    d1, x1 = palabra('CLNDA', 100, 0, 98, 700, -1.5)
    d2, x2 = palabra(nombre, 100, x1 + 22, 98, 400)
    return svg(f'<g transform="translate(-6 -4) scale(1.95)">{symb(k, ll, c, bg)}</g><g transform="translate(118 0)"><path d="{d1}" fill="{wk}"/><path d="{d2}" fill="{c}"/></g>', f'0 0 {118 + x2 + 4:.0f} 120')
def app(k, bgc, ll, c, r=0):
    return svg(f'<rect width="512" height="512" rx="{r}" fill="{bgc}"/><g transform="translate(80 80) scale(5.5)">{symb(k, ll, c, bgc)}</g>', '0 0 512 512')
tema = {'familia': 'CLNDA · productos', 'sistema': 'C · forma + color: llave índigo constante; el dato es el objeto del oficio en el color del producto',
        'base': {'tinta': INK, 'fondo': BG, 'indigo': IND, 'indigo-oscuro': INDD}, 'productos': {}}
for k, (nombre, uso, mc, tx, dk) in P.items():
    W = {
        'simbolo': svg(symb(k, IND, mc, '#fff'), '0 0 64 64'),
        'simbolo-oscuro': svg(symb(k, INDD, dk, INK), '0 0 64 64'),
        'simbolo-tinta': svg(symb(k, INK, INK, '#fff'), '0 0 64 64'),
        'simbolo-blanco': svg(symb(k, '#fff', '#fff', INK), '0 0 64 64'),
        'simbolo-16': svg(symb16(k, IND, mc, '#fff'), '0 0 64 64'),
        'simbolo-16-oscuro': svg(symb16(k, INDD, dk, INK), '0 0 64 64'),
        'favicon': f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke-linecap="round" stroke-linejoin="round"><style>:root{{--l:{IND};--c:{mc};--b:#fff}}@media(prefers-color-scheme:dark){{:root{{--l:{INDD};--c:{dk};--b:{INK}}}}}</style>{symb16(k, "var(--l)", "var(--c)", "var(--b)")}</svg>',
        'app-icon': app(k, INK, INDD, dk), 'app-icon-redondeado': app(k, INK, INDD, dk, 112), 'app-icon-claro': app(k, '#fff', IND, mc),
        'lockup': lockup(k, nombre, INK, IND, mc, '#fff'), 'lockup-oscuro': lockup(k, nombre, BG, INDD, dk, INK),
        'lockup-tinta': lockup(k, nombre, INK, INK, INK, '#fff'),
    }
    os.makedirs(f'{H}/{k}/svg', exist_ok=True)
    for n, s in W.items(): open(f'{H}/{k}/svg/{n}.svg', 'w').write(s)
    tema['productos'][k] = {'nombre': f'CLNDA {nombre}', 'uso': uso, 'objeto': {'booking': 'hoja de calendario', 'shop': 'etiqueta de precio', 'menu': 'plato'}[k],
        'color': {'marca': mc, 'texto': tx, 'oscuro': dk},
        'contraste': {'marca/blanco': cr(mc, '#ffffff'), 'texto/blanco': cr(tx, '#ffffff'), 'texto/fondo': cr(tx, BG), 'oscuro/tinta': cr(dk, INK)}}
    assert cr(tx, '#ffffff') >= 4.5 and cr(tx, BG) >= 4.5 and cr(mc, '#ffffff') >= 3 and cr(dk, INK) >= 4.5, k
tema['reglas'] = {
    'llave': 'siempre índigo (#4338ca en claro, #8b8cf8 sobre tinta); nunca toma el color del producto',
    'marca': 'color del objeto y de la palabra del producto en lockups (texto grande, ≥ 24 px)',
    'texto': 'enlaces, etiquetas y texto de interfaz en color de producto por debajo de 24 px',
    'oscuro': 'objeto y palabra sobre tinta',
    'interfaz': 'acción primaria del panel sigue siendo índigo (familia); el color del producto es acento: icono activo, chip, gráfica principal',
    'cliente_final': 'el huésped o comprador ve la marca del negocio y la firma «hecho por CLNDA» (sin nombre de producto)',
}
json.dump(tema, open(f'{H}/tema.json', 'w'), indent=2, ensure_ascii=False)
# lámina
def img(k, n, cls=''): return f'<img class="{cls}" src="{k}/svg/{n}.svg" alt="">'
filas = ''
for k, (nombre, uso, mc, tx, dk) in P.items():
    filas += (f'<section class="p"><header><h2>CLNDA {nombre}</h2><span>{uso}</span>'
              f'<span class="sw"><i style="background:{mc}"></i>{mc}</span><span class="sw"><i style="background:{tx}"></i>texto {tx}</span><span class="sw"><i style="background:{dk}"></i>oscuro {dk}</span></header>'
              f'<div class="row"><div class="cell"><img class="lk" src="{k}/svg/lockup.svg" alt="CLNDA {nombre}"></div>'
              f'<div class="cell dk"><img class="lk" src="{k}/svg/lockup-oscuro.svg" alt=""></div></div>'
              f'<div class="row s"><div class="cell">{img(k,"simbolo","s64")}{img(k,"simbolo-16","s24")}{img(k,"simbolo-16","s16")}</div>'
              f'<div class="cell dk">{img(k,"simbolo-oscuro","s64")}{img(k,"simbolo-16-oscuro","s24")}{img(k,"simbolo-16-oscuro","s16")}</div>'
              f'<div class="cell">{img(k,"simbolo-tinta","s64")}<img class="lk sm" src="{k}/svg/lockup-tinta.svg" alt=""></div>'
              f'<div class="cell ap">{img(k,"app-icon-redondeado","ai")}{img(k,"app-icon-claro","ai bd")}</div></div></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 14px/1.5 'Space Grotesk',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font:700 28px/1.2 'Space Grotesk';margin:0}}.lead{{margin:0;color:#4a4d63;max-width:820px}}
.p{{background:#fff;border:1px solid #dfe1ec;border-radius:16px;padding:20px;display:grid;gap:12px;min-width:0}}
.p header{{display:flex;flex-wrap:wrap;gap:6px 16px;align-items:baseline}}h2{{font:700 20px 'Space Grotesk';margin:0}}.p header>span{{color:#4a4d63}}
.sw{{display:inline-flex;gap:6px;align-items:center;font:500 12px 'JetBrains Mono',monospace}}.sw i{{width:12px;height:12px;border-radius:3px}}
.row{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}.row.s{{grid-template-columns:repeat(4,minmax(0,1fr))}}
.cell{{border:1px solid #eceef5;border-radius:12px;padding:16px;display:flex;align-items:center;gap:14px;min-height:88px;min-width:0;flex-wrap:wrap}}.cell.dk{{background:{INK};border-color:{INK}}}
.lk{{height:44px;max-width:100%}}.lk.sm{{height:26px}}.s64{{width:56px}}.s24{{width:24px}}.s16{{width:16px}}.ai{{width:64px;border-radius:14px}}.bd{{border:1px solid #dfe1ec}}
@media (max-width:820px){{.row,.row.s{{grid-template-columns:1fr 1fr}}.lk{{height:34px}}}}@media (max-width:480px){{.row,.row.s{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Productos CLNDA</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>CLNDA Booking, Shop y Menú</h1>'
        '<p class="lead">Paquete final, sistema C: la llave índigo hace familia y el objeto del oficio, en el color de cada producto, dice cuál es. Lockup en claro y sobre tinta; símbolo a 64, 24 y 16 px; una tinta; app icon oscuro y claro.</p>'
        f'{filas}</main></body></html>')
open(f'{H}/lamina.html', 'w').write(html)
print('ok', json.dumps({k: v['contraste'] for k, v in tema['productos'].items()}))
