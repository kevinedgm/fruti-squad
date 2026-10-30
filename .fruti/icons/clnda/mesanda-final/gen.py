# Mesanda (de CLNDA Studio) · paquete final de marca.
# Decisiones del usuario (2026-10-30): nombre Mesanda (mesa + comanda); símbolo H1 «mesa con estela»; color: blanco, negro y acento amarillo señal.
# Logotipo: Manrope 800 en trazados. Uso: python3 gen.py <carpeta con Manrope[wght].ttf> → svg/, tema.json, lamina.html
import sys, os, json
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
H = os.path.dirname(os.path.abspath(__file__)); FD = sys.argv[1]
NEG, BLA, AMA, AMA_TX, GRIS = '#0b0b0c', '#ffffff', '#facc15', '#7a5a00', '#f4f4f5'
def lum(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def cr(a, b): x, y = sorted((lum(a), lum(b))); return round((y + .05) / (x + .05), 2)
def inst(w):
    p = f'/tmp/mesanda-manrope{w}.ttf'
    if not os.path.exists(p): instancer.instantiateVariableFont(TTFont(FD + '/Manrope[wght].ttf'), {'wght': w}).save(p)
    return p
FT = {w: (inst(w), TTFont(inst(w))) for w in (500, 800)}
def palabra(s, size, x0, y0, w=800, track=0):
    path, font = FT[w]; upm = font['head'].unitsPerEm
    hf = hb.Font(hb.Face(hb.Blob.from_file_path(path))); b = hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf, b, {'kern': True})
    gs = font.getGlyphSet(); order = font.getGlyphOrder(); k = size / upm; x = x0; d = ''
    for i, ps in zip(b.glyph_infos, b.glyph_positions):
        pen = SVGPathPen(gs); gs[order[i.codepoint]].draw(TransformPen(pen, (k, 0, 0, -k, x, y0))); d += pen.getCommands(); x += ps.x_advance * k + track
    return d, x
def svg(body, vb): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
MESA = '<circle cx="38" cy="32" r="14" fill="{m}"/><rect x="30" y="7" width="16" height="7" rx="3.5" fill="{m}"/><rect x="30" y="50" width="16" height="7" rx="3.5" fill="{m}"/><rect x="56" y="24" width="7" height="16" rx="3.5" fill="{m}"/>'
def symb(m, e): return MESA.format(m=m) + f'<path d="M6 26h8M3 32h11M6 38h8" stroke="{e}" stroke-width="4.5"/>'
def symb16(m, e): return MESA.format(m=m) + f'<path d="M5 26.5h10M5 37.5h10" stroke="{e}" stroke-width="6"/>'  # 16–24 px
def lockup(m, e, tx, by=None):
    d, x = palabra('Mesanda', 100, 0, 92, 800, -2.5)
    body = f'<g transform="scale(1.9)">{symb(m, e)}</g><g transform="translate(152 0)"><path d="{d}" fill="{tx}"/></g>'
    w, h = 152 + x + 4, 122
    if by:
        d1, x1 = palabra('de ', 30, 0, 150, 500); d2, x2 = palabra('CLNDA', 30, x1, 150, 800); d3, x3 = palabra(' Studio', 30, x2, 150, 500)
        body += f'<g transform="translate(156 0)" fill="{by}"><path d="{d1}{d3}" opacity=".7"/><path d="{d2}"/></g>'; h = 164
    return svg(body, f'0 0 {w:.0f} {h}')
def app(bg, m, e, r=0, small=False):
    f = symb16 if small else symb
    return svg(f'<rect width="512" height="512" rx="{r}" fill="{bg}"/><g transform="translate(64 64) scale(6)">{f(m, e)}</g>', '0 0 512 512')
W = {
    'simbolo': svg(symb(NEG, AMA), '0 0 64 64'),                 # sobre blanco: estela amarilla decorativa
    'simbolo-oscuro': svg(symb(BLA, AMA), '0 0 64 64'),          # sobre negro
    'simbolo-amarillo': svg(symb(NEG, NEG), '0 0 64 64'),        # sobre amarillo, todo negro
    'simbolo-negro': svg(symb(NEG, NEG), '0 0 64 64'), 'simbolo-blanco': svg(symb(BLA, BLA), '0 0 64 64'),
    'simbolo-16': svg(symb16(NEG, NEG), '0 0 64 64'), 'simbolo-16-oscuro': svg(symb16(BLA, AMA), '0 0 64 64'),
    'favicon': f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke-linecap="round" stroke-linejoin="round"><style>:root{{--m:{NEG};--e:{NEG}}}@media(prefers-color-scheme:dark){{:root{{--m:{BLA};--e:{AMA}}}}}</style>{symb16("var(--m)", "var(--e)")}</svg>',
    'app-icon': app(NEG, BLA, AMA), 'app-icon-redondeado': app(NEG, BLA, AMA, 112), 'app-icon-amarillo': app(AMA, NEG, NEG, 112),
    'lockup': lockup(NEG, AMA, NEG), 'lockup-oscuro': lockup(BLA, AMA, BLA), 'lockup-amarillo': lockup(NEG, NEG, NEG), 'lockup-negro': lockup(NEG, NEG, NEG),
    'lockup-respaldo': lockup(NEG, AMA, NEG, NEG), 'lockup-respaldo-oscuro': lockup(BLA, AMA, BLA, BLA),
}
os.makedirs(f'{H}/svg', exist_ok=True)
for n, s in W.items(): open(f'{H}/svg/{n}.svg', 'w').write(s)
tema = {
    'nombre': 'Mesanda', 'respaldo': 'de CLNDA Studio', 'formula': 'mesa + comanda («la mesa anda»)',
    'simbolo': 'mesa redonda con tres sillas y estela de velocidad en lugar de la cuarta (H1)',
    'color': {'negro': NEG, 'blanco': BLA, 'amarillo': AMA, 'amarillo-texto': AMA_TX, 'gris-fondo': GRIS},
    'reglas': {
        'acento': 'amarillo solo en dos funciones de la app: acción principal (Enviar a cocina) y lo que necesita al mesero (Cuenta pedida)',
        'texto_sobre_amarillo': 'siempre negro (12.8:1); nunca blanco',
        'amarillo_sobre_blanco': 'nunca como texto ni icono funcional (1.5:1); en el logotipo claro la estela es decorativa; para texto amarillo-texto',
        'simbolo_16': 'por debajo de 24 px usar simbolo-16 (dos líneas gruesas); sobre blanco, todo negro',
        'naranja': 'prohibido (competidor)',
        'cliente_final': 'Mesanda es herramienta del negocio; el comensal no la ve',
    },
    'tipografia': {'marca': 'Manrope 800 (trazados)', 'interfaz': 'Manrope 400–700'},
    'contraste': {'negro/amarillo': cr(NEG, AMA), 'negro/blanco': cr(NEG, BLA), 'amarillo/blanco': cr(AMA, BLA), 'amarillo-texto/blanco': cr(AMA_TX, BLA)},
}
json.dump(tema, open(f'{H}/tema.json', 'w'), indent=2, ensure_ascii=False)
def img(n, c=''): return f'<img class="{c}" src="svg/{n}.svg" alt="">'
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{GRIS};color:{NEG};font:400 14px/1.5 'Manrope',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font:800 28px/1.2 'Manrope';margin:0}}.lead{{margin:0;color:#52525b;max-width:860px}}
.p{{background:#fff;border:1px solid #e4e4e7;border-radius:16px;padding:20px;display:grid;gap:12px;min-width:0}}h2{{font:700 13px 'Manrope';letter-spacing:.06em;text-transform:uppercase;color:#52525b;margin:0}}
.row{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}.row.s{{grid-template-columns:repeat(4,minmax(0,1fr))}}
.cell{{border:1px solid #ececef;border-radius:12px;padding:18px;display:flex;align-items:center;gap:14px;min-height:96px;min-width:0;flex-wrap:wrap}}.dk{{background:{NEG};border-color:{NEG}}}.am{{background:{AMA};border-color:{AMA}}}
.lk{{height:46px;max-width:100%}}.lkb{{height:62px;max-width:100%}}.s64{{width:56px}}.s24{{width:24px}}.s16{{width:16px}}.ai{{width:72px}}
.sw{{display:flex;gap:10px;align-items:center}}.sw i{{width:40px;height:40px;border-radius:10px;border:1px solid rgba(0,0,0,.08)}}.sw b{{display:block}}.sw code{{font-size:12px;color:#52525b}}
ul{{margin:0;padding-left:18px;color:#3f3f46}}li{{margin:2px 0}}
@media (max-width:860px){{.row,.row.s{{grid-template-columns:1fr 1fr}}}}@media (max-width:500px){{.row,.row.s{{grid-template-columns:1fr}}}}'''
cols = [(NEG, 'Negro', 'texto, mesas ocupadas, fondos de marca'), (BLA, 'Blanco', 'fondo de la app y de los materiales'), (AMA, 'Amarillo señal', 'acción principal y «cuenta pedida»'), (AMA_TX, 'Amarillo texto', 'texto amarillo sobre blanco (6.4:1)')]
sw = ''.join(f'<div class="sw"><i style="background:{c}"></i><span><b>{n}</b><code>{c}</code><br>{u}</span></div>' for c, n, u in cols)
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Mesanda · marca</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>Mesanda · paquete de marca</h1>'
        '<p class="lead">Comandero de CLNDA Studio. La mesa con estela dice «mesa» y «rápido»; blanco y negro hacen el trabajo y el amarillo señala lo que necesita al mesero.</p>'
        f'<section class="p"><h2>Logotipo</h2><div class="row"><div class="cell"><img class="lk" src="svg/lockup.svg" alt="Mesanda"></div><div class="cell dk"><img class="lk" src="svg/lockup-oscuro.svg" alt=""></div><div class="cell am"><img class="lk" src="svg/lockup-amarillo.svg" alt=""></div></div>'
        f'<div class="row" style="grid-template-columns:1fr 1fr"><div class="cell"><img class="lkb" src="svg/lockup-respaldo.svg" alt="Mesanda de CLNDA Studio"></div><div class="cell dk"><img class="lkb" src="svg/lockup-respaldo-oscuro.svg" alt=""></div></div></section>'
        f'<section class="p"><h2>Símbolo y app icon</h2><div class="row s"><div class="cell">{img("simbolo","s64")}{img("simbolo-16","s24")}{img("simbolo-16","s16")}</div>'
        f'<div class="cell dk">{img("simbolo-oscuro","s64")}{img("simbolo-16-oscuro","s24")}{img("simbolo-16-oscuro","s16")}</div>'
        f'<div class="cell am">{img("simbolo-amarillo","s64")}{img("simbolo-16","s24")}</div><div class="cell">{img("app-icon-redondeado","ai")}{img("app-icon-amarillo","ai")}</div></div></section>'
        f'<section class="p"><h2>Color</h2><div class="row s">{sw}</div></section>'
        '<section class="p"><h2>Reglas</h2><ul><li>El amarillo tiene dos trabajos en la app: la acción principal y la mesa que necesita al mesero. Nada más.</li>'
        '<li>Sobre amarillo, siempre texto negro (12.8:1). Nunca texto amarillo sobre blanco (1.5:1): para eso, amarillo texto.</li>'
        '<li>Debajo de 24 px, el símbolo pequeño (dos líneas gruesas).</li><li>Nada de naranja.</li><li>«de CLNDA Studio» acompaña al logotipo en ventas y materiales; en la app basta Mesanda.</li></ul></section>'
        '</main></body></html>')
open(f'{H}/lamina.html', 'w').write(html)
print('ok', tema['contraste'])
