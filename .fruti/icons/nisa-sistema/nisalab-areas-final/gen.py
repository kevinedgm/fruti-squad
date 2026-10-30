# NisaLab · paquete final de las áreas. Uso:
#   python3 gen.py <carpeta con poppins-latin-{400,600}-normal.woff> <carpeta temporal>
# Toma paleta, íconos y marca de ../nisalab-areas-2/gen.py (la ronda aprobada) y escribe svg/<área>/, tema.json y lamina.html.
import importlib.util, json, os, re, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

H = os.path.dirname(os.path.abspath(__file__))
WOFF, TMP = sys.argv[1], sys.argv[2]

# — la ronda aprobada como módulo (sin fuentes locales: deja su lámina con Google Fonts) —
_argv = sys.argv; sys.argv = [_argv[0]]
spec = importlib.util.spec_from_file_location('areas2', os.path.join(H, '..', 'nisalab-areas-2', 'gen.py'))
A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
sys.argv = _argv
AZ, PE, W, TINTA, MUTED = A.AZ, A.PE, A.W, A.TINTA, '#535B70'

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
CAP = fuente(600)[0]['OS/2'].sCapHeight / fuente(600)[0]['head'].unitsPerEm

def svg(vb, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'
def cuerpo(s):
    """El contenido de un <svg> generado por la ronda (sin la etiqueta raíz)."""
    return s[s.index('>') + 1:s.rindex('</svg>')]

def glifo(k, color, s, x, y):
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({s:.4f})">{A.ICON[k](color)}</g>'
GS = A.gr * 2 * 0.62 / 40
def marca(k, color, tono='color', u=''):
    """tono: color | blanco (células blancas, sobre azul) | 1tinta (currentColor, el ícono calado)."""
    otras = [c for c in A.CEL if c[3] != PE]
    gx, gy, gr = A.gx, A.gy, A.gr
    if tono == '1tinta':
        m = f'm{k}{u}'
        cel = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="currentColor"/>' for x, y, r, _ in otras)
        return svg('-2 -2 104 104', f'<defs>{mascara(k, gx, gy, GS, m, 104, -2)}</defs>{cel}<circle cx="{gx}" cy="{gy}" r="{gr}" fill="currentColor" mask="url(#{m})"/>', f'{nombre(k)} NisaLab')
    base = W if tono == 'blanco' else AZ
    cel = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{base}"/>' for x, y, r, _ in otras)
    return svg('-2 -2 104 104', f'{cel}<circle cx="{gx}" cy="{gy}" r="{gr}" fill="{color}"/>{glifo(k, color, GS, gx - 20 * GS, gy - 20 * GS)}', f'{nombre(k)} NisaLab')

def mascara(k, cx, cy, s, mid, size, o):
    """Máscara que cala el ícono: blanco = se ve; el ícono (y sus detalles en color) en negro."""
    g = A.ICON[k]('#000').replace('#fff', '#000')
    # los detalles que el ícono dibuja en el color del área (vena, puntos) vuelven a blanco: son parte del fondo
    detalles = A.ICON[k]('#FFFFFE')
    det = ''.join(re.findall(r'<[^>]*#FFFFFE[^>]*/>', detalles)).replace('#FFFFFE', '#fff')
    return (f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="{o}" y="{o}" width="{size}" height="{size}"><rect x="{o}" y="{o}" width="{size}" height="{size}" fill="#fff"/>'
            f'<g transform="translate({cx - 20 * s:.2f} {cy - 20 * s:.2f}) scale({s:.4f})">{g}{det}</g></mask>')

def icono(k, color, tono='color'):
    if tono == '1tinta':
        m = f'i{k}'
        return svg('0 0 48 48', f'<defs>{mascara(k, 24, 24, .875, m, 48, 0)}</defs><circle cx="24" cy="24" r="24" fill="currentColor" mask="url(#{m})"/>', nombre(k))
    return svg('0 0 48 48', cuerpo(A.chip(k, color)), nombre(k))

NOM = {k: n for k, n, _ in A.AREAS}
def nombre(k): return NOM[k]

S = 100; SIM = 1.27 * S; GAP = 0.30 * S
def logotipo(k, color, tono='color'):
    base = SIM / 2 + CAP * S / 2
    c_area, c_nl = {'color': (AZ, MUTED), 'blanco': (W, '#C9D3EA'), '1tinta': ('currentColor', 'currentColor')}[tono]
    d1, b1, x1 = texto(NOM[k], S, SIM + GAP, base, 600)
    d2, b2, x2 = texto('NisaLab', S, x1 + 0.28 * S, base, 400)
    k_ = SIM / 100
    m = marca(k, color, tono, u='l')
    inner = cuerpo(m).split('</title>', 1)[1]
    body = f'<g transform="scale({k_:.4f})">{inner}</g><path d="{d1}" fill="{c_area}"/><path d="{d2}" fill="{c_nl}"/>'
    return svg(f'-4 -4 {b2[2] + 8:.1f} {SIM + 8:.1f}', body, f'{NOM[k]} NisaLab')

out = {}
for k, n, c in A.AREAS:
    d = os.path.join(H, 'svg', k); os.makedirs(d, exist_ok=True)
    piezas = {'marca': marca(k, c), 'marca-blanco': marca(k, c, 'blanco'), 'marca-1tinta': marca(k, c, '1tinta'),
              'icono': icono(k, c), 'icono-1tinta': icono(k, c, '1tinta'),
              'logotipo': logotipo(k, c), 'logotipo-blanco': logotipo(k, c, 'blanco'), 'logotipo-1tinta': logotipo(k, c, '1tinta')}
    for p, s in piezas.items():
        open(os.path.join(d, p + '.svg'), 'w').write(s)
    out[k] = piezas

json.dump({'sistema': 'NisaLab', 'patron_nombre': '«Área NisaLab» (por ejemplo, «Aguas NisaLab»)',
           'paleta': {'metodo': f'OKLCH con luminosidad {A.L_} e intensidad {A.C_} iguales; solo cambia el tono, fuera del rango del pera (100–125°)',
                      'areas': {k: {'nombre': n, 'hex': c, 'token': f'area-{k}', 'blanco_encima': A.cr(W, c)} for k, n, c in A.AREAS}},
           'iconos': 'Dibujados en retícula de 40, formas redondas y blancas, grosor de trazo 3–4', 'tamano_minimo_px': 16},
          open(os.path.join(H, 'tema.json'), 'w'), ensure_ascii=False, indent=2)

def inl(s, h, color=None):
    st = f'height:{h}px;width:auto;display:block;flex:none' + (f';color:{color}' if color else '')
    return s.replace('<svg ', f'<svg style="{st}" ', 1)
filas = ''
for k, n, c in A.AREAS:
    p = out[k]
    filas += (f'<tr><th>{n}<small>{c}</small></th><td>{inl(p["marca"], 56)}</td><td class="az">{inl(p["marca-blanco"], 56)}</td><td>{inl(p["marca-1tinta"], 56, TINTA)}</td>'
              f'<td>{inl(p["icono"], 40)}</td><td>{inl(p["icono-1tinta"], 40, TINTA)}</td><td>{inl(p["logotipo"], 40)}</td></tr>')
lamina = f'''<title>NisaLab · áreas, paquete final</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
/* Vista general del paquete de áreas: blanco, tinta y azul real de Nisa Nabani. */
:root{{--az:{AZ};--fg:{TINTA};--muted:{MUTED};--line:#DFE3EC;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:14px/1.45 system-ui,sans-serif;padding-block:0 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1180px;margin:0 auto}} h1{{font:600 22px/1.3 system-ui,sans-serif;margin:36px 0 16px}} .tw{{overflow-x:auto}}
table{{border-collapse:collapse;width:100%;min-width:900px}} th,td{{padding:12px;border-bottom:1px solid var(--line);vertical-align:middle;text-align:left}} thead th{{font-size:12px;color:var(--muted);font-weight:600}}
tbody th{{font-weight:600;white-space:nowrap}} tbody th small{{display:block;font-weight:400;color:var(--muted);font-family:ui-monospace,monospace}} td.az{{background:var(--az)}}
</style>
<main><h1>Áreas de NisaLab · paquete final</h1><div class="tw"><table><thead><tr><th>Área</th><th>marca</th><th>marca-blanco</th><th>marca-1tinta</th><th>icono</th><th>icono-1tinta</th><th>logotipo</th></tr></thead><tbody>{filas}</tbody></table></div></main>'''
open(os.path.join(H, 'lamina.html'), 'w').write(lamina)
print('ok', len(out) * 8, 'svg')
