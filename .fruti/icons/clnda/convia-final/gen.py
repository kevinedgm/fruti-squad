# Convia · manual de identidad v2. Uso: python3 gen.py <carpeta con Fraunces-Suave-500.ttf> && node png.cjs
# Fraunces-Suave-500.ttf = instancia de Fraunces variable con SOFT 100, WONK 0, opsz 96, wght 500 (fontTools.varLib.instancer).
# Símbolo E1b (../convia-r7/E1b.svg), paleta Cantera + colores de categoría, Fraunces suave (marca y títulos) + Figtree (texto).
import sys, os, re, json
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FD = sys.argv[1] if len(sys.argv) > 1 else '.'
D = os.path.dirname(os.path.abspath(__file__))
GL = os.path.join(FD, 'Fraunces-Suave-500.ttf')
STAR = re.search(r'<path d="([^"]+)"', open(os.path.join(D, '..', 'convia-r7', 'E1b.svg')).read()).group(1)

CAT = {  # color por categoría: punto (marcador, ícono), fondo (etiqueta), texto (≥ 4.5:1 sobre fondo y sobre papel)
 'cafes': ('Cafés', '#eda100', '#f6e9ce', '#855a00'), 'restaurantes': ('Restaurantes', '#e5622a', '#f4e0d4', '#a5471e'),
 'hoteles': ('Hoteles boutique', '#2a78d6', '#dae4ec', '#2260ab'), 'talleres': ('Talleres', '#c2447a', '#f0dcdf', '#a33966'),
 'museos': ('Museos y galerías', '#7a3fa0', '#e6dce5', '#7a3fa0'), 'recorridos': ('Recorridos', '#1baf7a', '#d8ebdf', '#11704e'),
}
C = {  # tokens de color (contraste verificado en tema.json)
 'papel': '#f7f5f0', 'superficie': '#ffffff', 'tinta': '#1b1d1a', 'texto_sec': '#5b605a', 'linea': '#e2ded4', 'cantera': '#2f5a45',
 'oscuro_fondo': '#141714', 'oscuro_superficie': '#1d201c', 'oscuro_tinta': '#f2f0ea', 'oscuro_texto_sec': '#a9ada6', 'cantera_clara': '#8fc4a8', 'cantera_suave': '#e3ece6', 'arena': '#ebe6da',
}
def lum(h):
    c = [int(h[i:i+2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b):
    x, y = sorted([lum(a), lum(b)], reverse=True); return round((x + .05) / (y + .05), 2)

def text_path(text, size, x, y):
    blob = hb.Blob.from_file_path(GL); font = hb.Font(hb.Face(blob))
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties(); hb.shape(font, buf, {'kern': True, 'liga': True})
    tt = TTFont(GL); gs = tt.getGlyphSet(); s = size / tt['head'].unitsPerEm; order = tt.getGlyphOrder()
    pen = SVGPathPen(gs); cx = 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        gs[order[info.codepoint]].draw(TransformPen(pen, (s, 0, 0, -s, x + (cx + pos.x_offset) * s, y - pos.y_offset * s))); cx += pos.x_advance
    return pen.getCommands(), cx * s

def star(fill, size, x=0, y=0):
    k = size / 200
    return f'<path transform="translate({x:.2f} {y:.2f}) scale({k:.4f})" d="{STAR}" fill="{fill}"/>'
def svg(w, h, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" role="img" aria-label="{label}">{body}</svg>'

files = {}
for n, f in [('simbolo', C['cantera']), ('simbolo-oscuro', C['cantera_clara']), ('simbolo-tinta', 'currentColor')]:
    files[f'svg/{n}.svg'] = svg(200, 200, star(f, 200), 'Convia')
# logotipo horizontal: estrella 64 + «Convia» Fraunces suave 58
tp, tw = text_path('Convia', 58, 74, 52)
W = 74 + tw + 2
for n, s, t in [('logotipo', C['cantera'], C['tinta']), ('logotipo-oscuro', C['cantera_clara'], C['oscuro_tinta']), ('logotipo-tinta', 'currentColor', 'currentColor')]:
    files[f'svg/{n}.svg'] = svg(W, 68, star(s, 64, 0, 2) + f'<path d="{tp}" fill="{t}"/>', 'Convia')
# solo palabra
wp, ww = text_path('Convia', 58, 0, 52)
files['svg/palabra.svg'] = svg(ww + 2, 68, f'<path d="{wp}" fill="{C["tinta"]}"/>', 'Convia')
# ícono de app y favicon
files['svg/app-icon.svg'] = svg(512, 512, f'<rect width="512" height="512" rx="112" fill="{C["cantera"]}"/>' + star(C['papel'], 330, 91, 91), 'Convia')
files['svg/favicon.svg'] = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"><style>path{fill:' + C['cantera'] + '}'
                           '@media (prefers-color-scheme:dark){path{fill:' + C['cantera_clara'] + '}}</style>' + f'<path d="{STAR}"/></svg>')
# imagen para compartir (1200×630)
op, ow = text_path('Convia', 120, 0, 0)
lp, lw = text_path('Lo que vale la pena en Oaxaca,', 46, 0, 0)
lp2, _ = text_path('escogido por gente de aquí.', 46, 0, 0)
files['svg/og.svg'] = svg(1200, 630, f'<rect width="1200" height="630" fill="{C["papel"]}"/>' + star(C['cantera'], 120, 96, 120)
    + f'<g transform="translate(236 214)"><path d="{op}" fill="{C["tinta"]}"/></g>'
    + f'<g transform="translate(96 420)"><path d="{lp}" fill="{C["tinta"]}"/></g><g transform="translate(96 480)"><path d="{lp2}" fill="{C["tinta"]}"/></g>'
    + f'<rect x="96" y="540" width="80" height="4" fill="{C["cantera"]}"/>', 'Convia: lo que vale la pena en Oaxaca')
for k, v in files.items():
    open(os.path.join(D, k), 'w').write(v)

tema = {
 'nombre': 'Convia', 'origen': 'convite (invitación) + vía (camino)',
 'simbolo': 'Estrella de un solo trazo, hecha a mano e inclinada; abstraída de las estrellas que se cargan en el convite. Fuente: convia-r7/E1b.svg',
 'color': C,
 'contraste': {
   'cantera/papel': cr(C['cantera'], C['papel']), 'papel/cantera (texto en botón)': cr(C['papel'], C['cantera']),
   'tinta/papel': cr(C['tinta'], C['papel']), 'texto_sec/papel': cr(C['texto_sec'], C['papel']),
   'cantera_clara/oscuro_fondo': cr(C['cantera_clara'], C['oscuro_fondo']), 'oscuro_tinta/oscuro_fondo': cr(C['oscuro_tinta'], C['oscuro_fondo']),
   'oscuro_texto_sec/oscuro_fondo': cr(C['oscuro_texto_sec'], C['oscuro_fondo']),
   'cantera/cantera_suave': cr(C['cantera'], C['cantera_suave'])},
 'categorias': {k: {'nombre': n, 'punto': p, 'fondo': f, 'texto': t, 'texto/fondo': cr(t, f), 'texto/papel': cr(t, C['papel']), 'punto/papel': cr(p, C['papel'])} for k, (n, p, f, t) in CAT.items()},
 'tipografia': {'display': 'Fraunces 500 con SOFT 100, WONK 0, opsz 96 (logotipo, títulos)', 'texto': 'Figtree 400/500/600/700 (todo lo demás; números tabulares en horarios y precios)',
                'licencia': 'SIL Open Font License (Google Fonts)'},
 'reglas': ['Primario: cantera. Apoyo: tinta, papel, arena y cantera suave. La fotografía de los lugares es la protagonista.',
            'Fraunces solo en logotipo y títulos; horarios, precios y botones van en Figtree.',
            'Formas suaves: radio 16 px en tarjetas y fotos, 12 px en campos, botones en píldora; hacen juego con la estrella.',
            'Cada categoría tiene un color, pero nunca se identifica solo por color: siempre lleva su nombre (y su ícono cuando exista).',
            'El punto de categoría (vivo) se usa en marcadores e íconos sobre fondo de su color o con borde blanco; las etiquetas usan fondo + texto oscuro (AA).',
            'El color de categoría no sustituye al primario: botones, enlaces y foco siempre en cantera.',
            'Área de seguridad: media altura de la estrella alrededor del logotipo.',
            'Tamaño mínimo: estrella 16 px; logotipo 24 px de alto.',
            'El logotipo nunca se redibuja: se usan los SVG de esta carpeta (texto convertido a trazos).'],
}
json.dump(tema, open(os.path.join(D, 'tema.json'), 'w'), ensure_ascii=False, indent=1)
print('ok', len(files), 'svg', tema['contraste'])
