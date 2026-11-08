# Nexa Squad · paquete final de marca (2026-11-08).
# Símbolos: familia Huecos (../r5-huecos): un bloque 40×40 en 48, radio 7; el agente es el hueco, sacado de su SKILL.md.
# Color: B Cian (claro: bloque tinta + hueco cian; oscuro: bloque claro + hueco cian oscuro). Letra: Bricolage Grotesque (700 / 400), en trazos.
# Uso: python3 gen.py <carpeta con BricolageGrotesque-Bold.ttf y BricolageGrotesque-Regular.ttf> → <id>/svg/*.svg, tema.json; luego node png.cjs
import os, sys, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
H = os.path.dirname(os.path.abspath(__file__)); FD = sys.argv[1]
src = open(os.path.join(H, '../r5-huecos/gen.py')).read().split('for i, n, r in AG:\n    open(')[0]
ns = {'__file__': os.path.join(H, '../r5-huecos/gen.py')}; exec(src, ns); CUT = ns['CUT']
TINTA, CLARO, OSCURO, PAPEL, BLANCO = '#16161B', '#F3F3EE', '#101014', '#F5F5F2', '#FFFFFF'
CIAN, CIAN_O = '#22C3E6', '#00728A'
SUB_L, SUB_D = '#5A5A65', '#B4B4AE'
M = {  # id: nombre, producto (squad.json), verbo
 'squad': ('Nexa Squad', 'Composición de módulos', 'componer'),
 'orka': ('Orka', 'Conductor', 'dirigir'), 'inqa': ('Inqa', 'Product Analyst', 'separar'),
 'arko': ('Arko', 'Systems Architect', 'proteger'), 'fluxa': ('Fluxa', 'Flow Designer', 'ordenar'),
 'kompa': ('Kompa', 'Layout Composer', 'acomodar'), 'kura': ('Kura', 'Component Curator', 'reutilizar'),
 'forja': ('Forja', 'Build Engineer', 'construir'), 'vera': ('Vera', 'QA Auditor', 'verificar'),
}
ORDER = list(M)
def lum(h):
    c = [int(h[i:i+2], 16)/255 for i in (1, 3, 5)]; c = [x/12.92 if x <= .04045 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a, b): x, y = sorted((lum(a), lum(b))); return round((y+.05)/(x+.05), 2)
def cuerpo(k, bloque, acc, uid):
    under = f'<rect x="4" y="4" width="40" height="40" rx="7" fill="{acc}"/>' if acc else ''
    return (f'<defs><mask id="{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48"><rect width="48" height="48" fill="#fff"/>{CUT[k]}</mask></defs>'
            f'{under}<rect x="4" y="4" width="40" height="40" rx="7" fill="{bloque}" mask="url(#{uid})"/>')
def svg(inner, vb='0 0 48 48', label=None):
    a = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"{a}>{inner}</svg>'
FT = {700: os.path.join(FD, 'BricolageGrotesque-Bold.ttf'), 400: os.path.join(FD, 'BricolageGrotesque-Regular.ttf')}
TT = {w: TTFont(p) for w, p in FT.items()}
def palabra(s, size, x0, y0, w):
    font = TT[w]; upm = font['head'].unitsPerEm
    hf = hb.Font(hb.Face(hb.Blob.from_file_path(FT[w]))); b = hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf, b, {'kern': True})
    gs = font.getGlyphSet(); order = font.getGlyphOrder(); k = size/upm; x = x0; dd = ''
    for i, ps in zip(b.glyph_infos, b.glyph_positions):
        pen = SVGPathPen(gs); gs[order[i.codepoint]].draw(TransformPen(pen, (k, 0, 0, -k, x, y0))); dd += pen.getCommands(); x += ps.x_advance*k
    return dd, x
def lockup(k, oscuro, uid):
    n, p = M[k][0], M[k][1]
    d1, x1 = palabra(n, 30, 0, 26, 700); d2, x2 = palabra(p, 15, 0, 48, 400)
    w = 66 + max(x1, x2) + 2
    s = cuerpo(k, CLARO if oscuro else TINTA, CIAN_O if oscuro else CIAN, uid)
    return svg(f'<g transform="translate(-4 -4) scale(1.333)">{s}</g><g transform="translate(66 0)"><path d="{d1}" fill="{CLARO if oscuro else TINTA}"/>'
               f'<path d="{d2}" fill="{SUB_D if oscuro else SUB_L}"/></g>', f'0 0 {w:.0f} 56', f'{n} {p}')
def app(k, uid):
    return svg(f'<rect width="512" height="512" rx="112" fill="{TINTA}"/><g transform="translate(64 64) scale(8)">{cuerpo(k, CLARO, CIAN_O, uid)}</g>', '0 0 512 512', M[k][0])
def favicon(k):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><style>.b{{fill:{TINTA}}}.a{{fill:{CIAN}}}@media(prefers-color-scheme:dark){{.b{{fill:{CLARO}}}.a{{fill:{CIAN_O}}}}}</style>'
            + cuerpo(k, 'X', 'Y', 'f').replace('fill="Y"', 'class="a"').replace('fill="X"', 'class="b"') + '</svg>')
tema = {'nombre': 'Nexa Squad', 'sistema': 'Huecos: todos los símbolos son el mismo bloque; lo que se quita es lo que el agente hace.',
        'construccion': {'lienzo': 48, 'bloque': '40×40 en (4,4)', 'radio': 7, 'reticula': 4, 'canal_min': 4, 'hueco_min': 8, 'circulo_r_min': 4, 'cortes_max': 3, 'excepcion': 'Kompa (cinco cortes, tres anchos)'},
        'color': {'tinta': TINTA, 'claro': CLARO, 'oscuro': OSCURO, 'papel': PAPEL, 'cian': CIAN, 'cian_oscuro': CIAN_O, 'sub_claro': SUB_L, 'sub_oscuro': SUB_D},
        'contraste': {'cian/tinta': cr(CIAN, TINTA), 'cian_oscuro/claro': cr(CIAN_O, CLARO), 'tinta/blanco': cr(TINTA, BLANCO), 'claro/oscuro': cr(CLARO, OSCURO)},
        'tipografia': {'marca': 'Bricolage Grotesque 700 en trazos', 'producto': 'Bricolage Grotesque 400', 'web': 'https://fonts.google.com/specimen/Bricolage+Grotesque'},
        'reglas': ['El bloque siempre es neutro (tinta en claro, claro en oscuro); el cian vive solo dentro del hueco.',
                   'Un solo acento para toda la familia: lo que hace cada agente es lo que brilla.',
                   'Sobre claro, cian #22C3E6; sobre oscuro, cian oscuro #00728A. Nunca al revés.',
                   'Cada agente se reconoce por su hueco; el color nunca es la única señal.',
                   'Las plataformas (Claude Code, Codex, Kiro) se nombran en texto; nunca sus logotipos dentro de la marca.'],
        'productos': {k: {'nombre': n, 'producto': p, 'verbo': v} for k, (n, p, v) in M.items()}}
for k in ORDER:
    n = M[k][0]; out = f'{H}/{k}/svg'; os.makedirs(out, exist_ok=True)
    F = {'simbolo': svg(cuerpo(k, TINTA, CIAN, f'{k}1'), label=n), 'simbolo-oscuro': svg(cuerpo(k, CLARO, CIAN_O, f'{k}2'), label=n),
         'simbolo-tinta': svg(cuerpo(k, 'currentColor', None, f'{k}3'), label=n),
         'lockup': lockup(k, False, f'{k}4'), 'lockup-oscuro': lockup(k, True, f'{k}5'), 'app-icon': app(k, f'{k}6'), 'favicon': favicon(k)}
    for nm, s in F.items(): open(f'{out}/{nm}.svg', 'w').write(s)
json.dump(tema, open(f'{H}/tema.json', 'w'), indent=2, ensure_ascii=False); print('ok', tema['contraste'])
