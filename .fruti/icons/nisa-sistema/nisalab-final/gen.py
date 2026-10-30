# NisaLab · paquete final de marca (símbolo Colonia, variante 2 · Construida).
# Uso: python3 gen.py <carpeta con poppins-latin-{400,500,700}-normal.woff> <carpeta temporal>
# Escribe svg/, tema.json y lamina.html; los PNG se exportan con png.js.
import json, os, re, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

H = os.path.dirname(os.path.abspath(__file__))
WOFF, TMP = sys.argv[1], sys.argv[2]
AZ, PE, W, TINTA = '#052A76', '#C2D225', '#FFFFFF', '#141B33'

# — células: las del símbolo aprobado (nisalab-colonia/svg/simbolo.svg) —
_s = open(os.path.join(H, '..', 'nisalab-colonia', 'svg', 'simbolo.svg')).read()
CEL = [(float(x), float(y), float(r), c) for x, y, r, c in re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)" fill="([^"]+)"', _s)]
def celulas(az=AZ, pe=PE, x=0, y=0, k=1.0):
    return ''.join(f'<circle cx="{x + cx * k:.2f}" cy="{y + cy * k:.2f}" r="{r * k:.2f}" fill="{pe if c == PE else az}"/>' for cx, cy, r, c in CEL)

# — texto a trazos —
_f = {}
def fuente(w):
    if w not in _f:
        f = TTFont(os.path.join(WOFF, f'poppins-latin-{w}-normal.woff')); f.flavor = None
        p = os.path.join(TMP, f'poppins-{w}.ttf'); f.save(p); _f[w] = (TTFont(p), p)
    return _f[w]
def texto(s, size, x0, y0, w):
    f, p = fuente(w)
    hf = hb.Font(hb.Face(hb.Blob.from_file_path(p))); b = hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf, b, {'kern': True})
    gs = f.getGlyphSet(); order = f.getGlyphOrder(); k = size / f['head'].unitsPerEm; x = x0; d = ''; bp = BoundsPen(gs)
    for i, ps in zip(b.glyph_infos, b.glyph_positions):
        pen = SVGPathPen(gs); g = gs[order[i.codepoint]]
        g.draw(TransformPen(pen, (k, 0, 0, -k, x, y0))); g.draw(TransformPen(bp, (k, 0, 0, -k, x, y0)))
        d += pen.getCommands(); x += ps.x_advance * k
    return d, bp.bounds, x
CAP = fuente(700)[0]['OS/2'].sCapHeight / fuente(700)[0]['head'].unitsPerEm

def nombre(x0, y0, size):
    """«Nisa» en 700 y «Lab» en 400; devuelve path, ancho final."""
    d1, b1, x1 = texto('Nisa', size, x0, y0, 700)
    d2, b2, x2 = texto('Lab', size, x1 + size * 0.01, y0, 400)
    return d1 + d2, (b1[0], min(b1[1], b2[1]), b2[2], max(b1[3], b2[3]))

def svg(vb, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'

S = 100            # tamaño del texto
SIM = 1.27 * S     # alto del símbolo frente al texto (como en la ronda aprobada)
GAP = 0.30 * S
def horizontal(col_txt, az=AZ, pe=PE, respaldo=False):
    k = SIM / 100
    base = SIM / 2 + CAP * S / 2  # línea base: el centro de la versal coincide con el centro del símbolo
    d, bb = nombre(SIM + GAP, base, S)
    body = celulas(az, pe, 0, 0, k) + f'<path d="{d}" fill="{col_txt}"/>'
    w = bb[2]
    if respaldo:
        dr, br, _ = texto('de ', 34, SIM + GAP + 2, base + 52, 400)
        dn, bn, _ = texto('Nisa Nabani', 34, br[2] + 9, base + 52, 700)
        body += f'<path d="{dr}" fill="{"#535B70" if col_txt in (AZ, TINTA) else col_txt}"/><path d="{dn}" fill="{col_txt}"/>'
        w = max(w, bn[2])
        h = base + 62
    else:
        h = SIM
    return svg(f'-4 -4 {w + 8:.1f} {h + 8:.1f}', body, 'NisaLab' + (' de Nisa Nabani' if respaldo else ''))
def vertical(col_txt=TINTA):
    k = 1.5; ts = 64
    d, bb = nombre(0, 0, ts); tw = bb[2] - bb[0]
    sw = 100 * k; ancho = max(sw, tw)
    d, bb = nombre((ancho - tw) / 2 - bb[0], sw + 26 + CAP * ts, ts)
    return svg(f'-6 -6 {ancho + 12:.1f} {sw + 26 + CAP * ts + 22:.1f}', celulas(x=(ancho - sw) / 2, k=k) + f'<path d="{d}" fill="{col_txt}"/>', 'NisaLab')

out = {
    'simbolo': svg('-2 -2 104 104', celulas(), 'NisaLab'),
    'simbolo-1tinta': svg('-2 -2 104 104', celulas('currentColor', 'currentColor'), 'NisaLab'),
    'simbolo-blanco': svg('-2 -2 104 104', celulas(W, PE), 'NisaLab'),
    'logotipo': horizontal(AZ),
    'logotipo-blanco': horizontal(W, W, PE),
    'logotipo-1tinta': horizontal('currentColor', 'currentColor', 'currentColor'),
    'logotipo-respaldo': horizontal(AZ, respaldo=True),
    'logotipo-vertical': vertical(AZ),
    'app-icon': svg('0 0 1024 1024', f'<rect width="1024" height="1024" fill="{AZ}"/>' + celulas(W, PE, 262, 262, 5.0), 'NisaLab'),
    'app-icon-maskable': svg('0 0 1024 1024', f'<rect width="1024" height="1024" fill="{AZ}"/>' + celulas(W, PE, 322, 322, 3.8), 'NisaLab'),
    'favicon': svg('-2 -2 104 104', celulas(), 'NisaLab'),
}
os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
for k_, v in out.items():
    open(os.path.join(H, 'svg', k_ + '.svg'), 'w').write(v)

def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 2)
json.dump({'marca': 'NisaLab', 'respaldo': 'de Nisa Nabani', 'arquitectura': {'empresa': 'Nisa Nabani', 'sistema': 'NisaLab', 'productos': '«Producto NisaLab» (por definir)'},
           'simbolo': 'Colonia: cuatro células tangentes con separación constante; una sola en pera, arriba a la derecha',
           'color': {'azul-real': {'hex': AZ, 'uso': 'símbolo, logotipo y fondo del ícono de app', 'blanco_encima': cr(W, AZ)},
                     'pera': {'hex': PE, 'uso': 'una sola célula del símbolo; nunca texto', 'sobre_blanco': cr(PE, W), 'sobre_azul': cr(PE, AZ)},
                     'tinta': {'hex': TINTA, 'uso': 'versión a una tinta en documentos'}},
           'tipografia': {'logotipo': '«Nisa» Poppins 700 + «Lab» Poppins 400, convertidos a trazos', 'interfaz': 'Poppins (manual de Nisa Nabani) + IBM Plex Mono para datos'},
           'tamano_minimo': {'pantalla_px': 16, 'impreso_mm': 6}},
          open(os.path.join(H, 'tema.json'), 'w'), ensure_ascii=False, indent=2)

def inl(n, h, extra=''):
    return out[n].replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block{extra}" ', 1)
lamina = f'''<title>NisaLab · paquete final</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
/* Vista general del paquete: blanco, tinta y azul real de Nisa Nabani. */
:root{{--az:{AZ};--fg:{TINTA};--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:15px/1.5 system-ui,sans-serif;padding-block:0 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1120px;margin:0 auto}} header{{padding:40px 0 24px}} h2{{font:600 13px/1.4 system-ui,sans-serif;color:var(--muted);margin:0 0 10px;letter-spacing:.04em;text-transform:uppercase}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}} .c{{border:1px solid var(--line);border-radius:18px;padding:22px;display:grid;place-items:center;gap:10px;min-height:160px}} .c.az{{background:var(--az);border-color:var(--az)}} .c small{{color:var(--muted);font-size:12px}} .c.az small{{color:#C9D3EA}}
.row{{display:flex;gap:18px;align-items:flex-end;flex-wrap:wrap}}
</style>
<main><header>{inl('logotipo', 72)}</header>
<div class="g">
<div class="c">{inl('simbolo', 120)}<small>simbolo.svg</small></div>
<div class="c">{inl('logotipo', 60)}<small>logotipo.svg</small></div>
<div class="c">{inl('logotipo-respaldo', 78)}<small>logotipo-respaldo.svg</small></div>
<div class="c">{inl('logotipo-vertical', 140)}<small>logotipo-vertical.svg</small></div>
<div class="c az">{inl('logotipo-blanco', 60)}<small>logotipo-blanco.svg</small></div>
<div class="c" style="color:{TINTA}">{inl('logotipo-1tinta', 60)}<small>logotipo-1tinta.svg</small></div>
<div class="c"><div class="row">{inl('app-icon', 120, ';border-radius:26px')}{inl('app-icon-maskable', 120, ';border-radius:60px')}</div><small>app-icon.svg · app-icon-maskable.svg</small></div>
<div class="c"><div class="row">{inl('favicon', 32)}{inl('favicon', 24)}{inl('favicon', 16)}</div><small>favicon.svg a 32, 24 y 16 px</small></div>
</div></main>'''
open(os.path.join(H, 'lamina.html'), 'w').write(lamina)
print('ok', list(out))
