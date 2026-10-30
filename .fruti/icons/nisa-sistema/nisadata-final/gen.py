# NisaData · paquete final. Producto hermano de NisaLab (analítica: tendencias, comportamiento y salud del laboratorio).
# Símbolo «Columnas de células» (ronda 1, opción 1) en grafito + mandarina (opción C).
# Uso: python3 gen.py <carpeta con poppins-latin-{400,500,700}-normal.woff> <carpeta temporal> <carpeta de fuentes para la lámina>
#      y después node png.cjs
import json, os, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
H = os.path.dirname(os.path.abspath(__file__)); WOFF, TMP, FL = sys.argv[1], sys.argv[2], sys.argv[3]
GR, MA, W, MUTED, AZ, PE = '#1F2532', '#FF8A1F', '#FFFFFF', '#535B70', '#052A76', '#C2D225'

# — símbolo: tres columnas de 1, 2 y 3 células; radios 10, 12 y 14; separación constante de 4; base común —
R, G = (10, 12, 14), 4
CEL = []; cx = 10 + R[0]
for i, r in enumerate(R):
    if i: cx += R[i - 1] + G + r
    for j in range(i + 1):
        CEL.append((cx, 96 - r - j * (2 * r + G), r, i == 2 and j == i))  # la última célula de la columna alta es la mandarina
def celulas(c=GR, a=MA, x=0, y=0, k=1.0):
    return ''.join(f'<circle cx="{x + cx * k:.2f}" cy="{y + cy * k:.2f}" r="{r * k:.2f}" fill="{a if ac else c}"/>' for cx, cy, r, ac in CEL)

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
    d1, b1, x1 = texto('Nisa', size, x0, y0, 700)
    d2, b2, _ = texto('Data', size, x1 + size * 0.01, y0, 400)
    return d1 + d2, (b1[0], min(b1[1], b2[1]), b2[2], max(b1[3], b2[3]))
def svg(vb, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'

S = 100; SIM = 1.2 * S; GAP = 0.26 * S
def horizontal(txt, c=GR, a=MA, respaldo=False):
    k = SIM / 100; base = SIM * 0.96 - (SIM * 0.92 - CAP * S) / 2  # versal centrada en la altura real del símbolo (y 4–96)
    d, bb = nombre(SIM + GAP, base, S); body = celulas(c, a, 0, 0, k) + f'<path d="{d}" fill="{txt}"/>'; w = bb[2]
    if respaldo:
        dr, br, _ = texto('de ', 34, SIM + GAP + 2, base + 52, 400); dn, bn, _ = texto('Nisa Nabani', 34, br[2] + 9, base + 52, 700)
        body += f'<path d="{dr}" fill="{MUTED if txt == GR else txt}"/><path d="{dn}" fill="{txt}"/>'; w = max(w, bn[2]); h = base + 62
    else:
        h = SIM
    return svg(f'-4 -4 {w + 8:.1f} {h + 8:.1f}', body, 'NisaData' + (' de Nisa Nabani' if respaldo else ''))
def vertical(txt=GR):
    k = 1.5; ts = 64; d, bb = nombre(0, 0, ts); tw = bb[2] - bb[0]; sw = 100 * k; an = max(sw, tw)
    d, bb = nombre((an - tw) / 2 - bb[0], sw + 26 + CAP * ts, ts)
    return svg(f'-6 -6 {an + 12:.1f} {sw + 26 + CAP * ts + 22:.1f}', celulas(x=(an - sw) / 2, k=k) + f'<path d="{d}" fill="{txt}"/>', 'NisaData')
def icono(k, off, rx):  # símbolo blanco + mandarina sobre grafito, centrado ópticamente
    return svg('0 0 1024 1024', f'<rect width="1024" height="1024" rx="{rx}" fill="{GR}"/>' + celulas(W, MA, off, off, k), 'NisaData')
out = {
    'simbolo': svg('6 0 88 100', celulas(), 'NisaData'),
    'simbolo-blanco': svg('6 0 88 100', celulas(W, MA), 'NisaData'),
    'simbolo-1tinta': svg('6 0 88 100', celulas('currentColor', 'currentColor'), 'NisaData'),
    'logotipo': horizontal(GR), 'logotipo-blanco': horizontal(W, W, MA), 'logotipo-1tinta': horizontal('currentColor', 'currentColor', 'currentColor'),
    'logotipo-respaldo': horizontal(GR, respaldo=True), 'logotipo-respaldo-blanco': horizontal(W, W, MA, respaldo=True), 'logotipo-vertical': vertical(),
    'app-icon': icono(5.4, 242, 0), 'app-icon-maskable': icono(4.1, 307, 0),
    'favicon': svg('0 0 100 100', f'<rect width="100" height="100" rx="22" fill="{GR}"/>' + celulas(W, MA, 11, 9, 0.78), 'NisaData'),
}
os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
for k_, v in out.items(): open(os.path.join(H, 'svg', k_ + '.svg'), 'w').write(v)

def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)
tema = {'marca': 'NisaData', 'respaldo': 'de Nisa Nabani', 'producto': 'Panel de analítica: tendencias, comportamiento y salud del laboratorio. Lee los datos de NisaLab.',
        'arquitectura': 'Producto hermano de NisaLab dentro de Nisa Nabani: nombre y símbolo propios, mismo patrón «Nisa» + palabra y mismo respaldo.',
        'simbolo': 'Columnas de células: tres columnas de 1, 2 y 3 células (radios 10, 12, 14; separación 4; base común); la célula superior de la columna alta en mandarina.',
        'color': {'grafito': {'hex': GR, 'uso': 'símbolo, logotipo, fondo del ícono de app y superficies de marca', 'blanco_encima': cr(W, GR)},
                  'mandarina': {'hex': MA, 'uso': 'una sola célula del símbolo y acentos de marca; nunca texto sobre blanco ni alerta', 'sobre_blanco': cr(MA, W), 'sobre_grafito': cr(MA, GR), 'grafito_encima': cr(GR, MA)}},
        'tipografia': {'logotipo': '«Nisa» Poppins 700 + «Data» Poppins 400, convertidos a trazos', 'interfaz': 'Poppins + IBM Plex Mono para datos (la misma de NisaLab)'},
        'reglas': ['Una sola célula mandarina por símbolo.', 'El color de producto vive en marca, ícono de app, acceso y navegación; nunca en tablas ni en estatus.',
                   'La mandarina no es alerta ni estado: no se usa para «pago parcial», avisos ni errores.', 'Las gráficas del panel usan su propia paleta de datos, no grafito y mandarina.',
                   'No rotar ni reacomodar las columnas; la base siempre abajo.'],
        'tamano_minimo': {'pantalla_px': 16, 'impreso_mm': 6}}
json.dump(tema, open(os.path.join(H, 'tema.json'), 'w'), ensure_ascii=False, indent=2)

# — lámina —
LAB = os.path.join(H, '..', 'nisalab-final', 'svg')
def inl(n, h, src=None):
    s = open(os.path.join(src, n + '.svg')).read() if src else out[n]
    import re; s = re.sub(r'<title>.*?</title>', '', s)
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block;max-width:100%" aria-hidden="true" ', 1)
cons = ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MA if ac else "#8A93A8"}" stroke-width=".6" stroke-dasharray="2 1.5"/>' for cx, cy, r, ac in CEL)
cons_svg = (f'<svg viewBox="0 -6 100 110" style="height:260px;width:auto;display:block" aria-hidden="true">{celulas("#E4E7EE", "#FFD8B0")}{cons}'
            '<line x1="0" y1="96" x2="100" y2="96" stroke="#8A93A8" stroke-width=".5"/>'
            + ''.join(f'<text x="{cx}" y="{cy + 1.6}" font-size="5" text-anchor="middle" fill="{GR}" font-family="Poppins">r {r}</text>' for cx, cy, r, ac in CEL) +
            '<text x="50" y="103.5" font-size="4.6" text-anchor="middle" fill="#535B70" font-family="Poppins">base común · separación 4</text></svg>')
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{FL}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700))
css = ff + f'''
*{{box-sizing:border-box}}body{{margin:0;background:#F2F4F8;color:{GR};font:400 14px/1.5 Poppins,sans-serif;padding:32px}}
h1{{font:700 26px/1.2 Poppins;margin:0 0 4px}}.lead{{color:{MUTED};max-width:860px;margin:0 0 24px}}
section{{background:#fff;border:1px solid #DFE3EC;border-radius:14px;padding:24px;margin-bottom:20px}}h2{{font:600 12px/1 Poppins;letter-spacing:.06em;text-transform:uppercase;color:{MUTED};margin:0 0 16px}}
.row{{display:flex;flex-wrap:wrap;gap:28px;align-items:center}}.osc{{background:{GR};border-radius:12px;padding:24px}}.c2{{display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:center}}
.c2 p{{margin:0 0 8px;color:{MUTED}}}.apps{{display:flex;gap:16px;align-items:center;flex-wrap:wrap}}.apps svg{{border-radius:22%}}.cap{{font-size:12px;color:{MUTED}}}
.sw{{display:flex;gap:16px;flex-wrap:wrap}}.sw div{{border-radius:12px;padding:16px;min-width:200px;font-size:13px}}
.reg{{margin:0;padding-left:20px}}.reg li{{margin:4px 0}}.tam{{display:flex;gap:18px;align-items:flex-end}}
@media (max-width:700px){{.c2{{grid-template-columns:1fr}}}}@media (max-width:480px){{body{{padding:16px}}section{{padding:16px}}}}
'''
tam = ''.join(inl('simbolo', px) for px in (64, 48, 32, 24, 16))
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaData</title><style>{css}</style><body>'
        f'<h1>NisaData · paquete final</h1><p class="lead">{tema["producto"]} {tema["arquitectura"]}</p>'
        f'<section><h2>Logotipo</h2><div class="row">{inl("logotipo-respaldo", 96)}{inl("logotipo", 64)}{inl("logotipo-vertical", 150)}</div></section>'
        f'<section><h2>Sobre grafito</h2><div class="osc"><div class="row">{inl("logotipo-respaldo-blanco", 96)}{inl("simbolo-blanco", 72)}</div></div></section>'
        f'<section><h2>Símbolo · construcción</h2><div class="c2">{cons_svg}<div><p>Tres columnas de células, de 1, 2 y 3: datos que crecen. Los radios crecen con la columna (10, 12, 14) y la separación es siempre 4, como en Colonia.</p><p>La célula de arriba de la columna alta es la única mandarina: el dato que importa.</p><div class="tam">{tam}</div></div></div></section>'
        f'<section><h2>Ícono de app y familia</h2><div class="apps">{inl("app-icon", 96, LAB).replace("NisaLab", "")}{inl("app-icon", 96)}{inl("app-icon-maskable", 96)}{inl("favicon", 32)}<span class="cap">NisaLab · NisaData · maskable · favicon</span></div></section>'
        f'<section><h2>Color</h2><div class="sw"><div style="background:{GR};color:#fff"><b>Grafito</b><br>{GR}<br>Blanco encima {tema["color"]["grafito"]["blanco_encima"]}:1</div>'
        f'<div style="background:{MA};color:{GR}"><b>Mandarina</b><br>{MA}<br>Grafito encima {tema["color"]["mandarina"]["grafito_encima"]}:1 · nunca texto sobre blanco ({tema["color"]["mandarina"]["sobre_blanco"]}:1)</div></div></section>'
        f'<section><h2>Reglas</h2><ol class="reg">{"".join(f"<li>{r}</li>" for r in tema["reglas"])}</ol></section></body></html>')
open(os.path.join(H, 'lamina.html'), 'w').write(html)
print('ok', json.dumps(tema['color'], ensure_ascii=False))
