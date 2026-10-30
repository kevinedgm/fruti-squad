# NisaResults · paquete final. Portal de clientes de Nisa Nabani: resultados e informes, y página pública de calidad con QR.
# Símbolo «Banda de control» (ronda 1, opción 1) en azul real + cian (ronda 2, opción B; colores del manual de Nisa Nabani).
# Uso: python3 gen.py <carpeta con poppins-latin-{400,700}-normal.woff> <carpeta temporal> <carpeta de fuentes para la lámina>; después node png.cjs
import json, os, re, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
H = os.path.dirname(os.path.abspath(__file__)); WOFF, TMP, FL = sys.argv[1], sys.argv[2], sys.argv[3]
AZ, CI, W, MUTED, TINTA = '#052A76', '#00B4D8', '#FFFFFF', '#535B70', '#141B33'

# — símbolo: dos límites (barras de 88 × 7, radio 3.5) y tres células dentro; la del centro, más grande y en cian —
# caja útil x 6–94, y 22–78 (88 × 56)
def sim(c=AZ, a=CI, x=0, y=0, k=1.0):
    t = lambda v, o: f'{o + v * k:.2f}'
    return (f'<rect x="{t(6, x)}" y="{t(22, y)}" width="{88 * k:.2f}" height="{7 * k:.2f}" rx="{3.5 * k:.2f}" fill="{c}"/>'
            f'<rect x="{t(6, x)}" y="{t(71, y)}" width="{88 * k:.2f}" height="{7 * k:.2f}" rx="{3.5 * k:.2f}" fill="{c}"/>'
            f'<circle cx="{t(22, x)}" cy="{t(56, y)}" r="{9 * k:.2f}" fill="{c}"/><circle cx="{t(50, x)}" cy="{t(46, y)}" r="{11 * k:.2f}" fill="{a}"/>'
            f'<circle cx="{t(78, x)}" cy="{t(53, y)}" r="{9 * k:.2f}" fill="{c}"/>')
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
    d1, b1, x1 = texto('Nisa', size, x0, y0, 700); d2, b2, _ = texto('Results', size, x1 + size * 0.01, y0, 400)
    return d1 + d2, (b1[0], min(b1[1], b2[1]), b2[2], max(b1[3], b2[3]))
def svg(vb, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'

S = 100; KS = 1.25 * S / 88   # el símbolo mide 1.25 veces el cuerpo del texto de ancho
SW, SH = 88 * KS, 56 * KS; GAP = 0.24 * S
def horizontal(txt, c=AZ, a=CI, respaldo=False):
    base = SH / 2 + CAP * S / 2                         # versal centrada en la altura del símbolo
    body = sim(c, a, -6 * KS, -22 * KS, KS)
    d, bb = nombre(SW + GAP, base, S); body += f'<path d="{d}" fill="{txt}"/>'; w = bb[2]
    if respaldo:
        dr, br, _ = texto('de ', 34, SW + GAP + 2, base + 52, 400); dn, bn, _ = texto('Nisa Nabani', 34, br[2] + 9, base + 52, 700)
        body += f'<path d="{dr}" fill="{MUTED if txt == AZ else txt}"/><path d="{dn}" fill="{txt}"/>'; w = max(w, bn[2]); h = base + 62
    else:
        h = SH
    return svg(f'-4 -4 {w + 8:.1f} {h + 8:.1f}', body, 'NisaResults' + (' de Nisa Nabani' if respaldo else ''))
def vertical(txt=AZ):
    k = 2.0; ts = 64; d, bb = nombre(0, 0, ts); tw = bb[2] - bb[0]; sw, sh = 88 * k, 56 * k; an = max(sw, tw)
    d, bb = nombre((an - tw) / 2 - bb[0], sh + 30 + CAP * ts, ts)
    return svg(f'-6 -6 {an + 12:.1f} {sh + 30 + CAP * ts + 22:.1f}', sim(x=(an - sw) / 2 - 6 * k, y=-22 * k, k=k) + f'<path d="{d}" fill="{txt}"/>', 'NisaResults')
def icono(ancho, rx=0, lado=1024):  # símbolo blanco + cian sobre azul real, centrado
    k = ancho / 88; x = (lado - 88 * k) / 2 - 6 * k; y = (lado - 56 * k) / 2 - 22 * k
    return svg(f'0 0 {lado} {lado}', f'<rect width="{lado}" height="{lado}" rx="{rx}" fill="{AZ}"/>' + sim(W, CI, x, y, k), 'NisaResults')
out = {
    'simbolo': svg('4 18 92 64', sim(), 'NisaResults'), 'simbolo-blanco': svg('4 18 92 64', sim(W, CI), 'NisaResults'),
    'simbolo-1tinta': svg('4 18 92 64', sim('currentColor', 'currentColor'), 'NisaResults'),
    'logotipo': horizontal(AZ), 'logotipo-blanco': horizontal(W, W, CI), 'logotipo-1tinta': horizontal('currentColor', 'currentColor', 'currentColor'),
    'logotipo-respaldo': horizontal(AZ, respaldo=True), 'logotipo-respaldo-blanco': horizontal(W, W, CI, respaldo=True), 'logotipo-vertical': vertical(),
    'sello': svg('0 0 100 100', f'<circle cx="50" cy="50" r="50" fill="{AZ}"/>' + sim(W, CI, 50 - 50 * .62, 50 - 50 * .62, .62), 'Analizada por Nisa Nabani'),
    'app-icon': icono(600), 'app-icon-maskable': icono(470), 'favicon': icono(80, 22, 100),
}
os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
for k_, v in out.items(): open(os.path.join(H, 'svg', k_ + '.svg'), 'w').write(v)

def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)
tema = {'marca': 'NisaResults', 'respaldo': 'de Nisa Nabani',
        'producto': 'Portal de clientes de Nisa Nabani: cada cliente consulta sus resultados e informes, y decide si publica la página de calidad de su agua con un código QR para sus huéspedes.',
        'arquitectura': 'Producto hermano de NisaLab y NisaData; es el que ve el cliente, por eso usa colores del manual de Nisa Nabani. En la página pública manda la marca del cliente y Nisa Nabani firma como laboratorio.',
        'simbolo': 'Banda de control: dos límites y tres células dentro; la del centro, más grande y en cian. Es la gráfica de monitoreo con su zona aceptable convertida en símbolo.',
        'color': {'azul-real': {'hex': AZ, 'uso': 'símbolo, logotipo, encabezado del portal y acción principal', 'blanco_encima': cr(W, AZ)},
                  'cian': {'hex': CI, 'uso': 'una célula del símbolo, sección activa y el punto del último análisis; nunca texto sobre blanco ni estado', 'sobre_blanco': cr(CI, W), 'sobre_azul': cr(CI, AZ)}},
        'semaforo': 'Óptimo (verde) y No óptimo (rojo) son estados de resultado, no de marca: la marca nunca usa verde ni rojo.',
        'tipografia': {'logotipo': '«Nisa» Poppins 700 + «Results» Poppins 400, convertidos a trazos', 'interfaz': 'Poppins + IBM Plex Mono para valores'},
        'reglas': ['Una sola célula cian por símbolo.', 'La marca nunca usa verde ni rojo: son Óptimo y No óptimo.',
                   'En la página pública manda la marca del cliente; NisaResults no aparece: el sello dice «Analizada por Nisa Nabani».',
                   'Cada resultado público cita contra qué norma o criterio se compara y la fecha de la última muestra.',
                   'Las barras siempre horizontales y el símbolo nunca se rota.'],
        'tamano_minimo': {'pantalla_px': 16, 'impreso_mm': 6}}
json.dump(tema, open(os.path.join(H, 'tema.json'), 'w'), ensure_ascii=False, indent=2)

# — lámina —
def inl(n, h):
    s = re.sub(r'<title>.*?</title>', '', out[n])
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block;max-width:100%" aria-hidden="true" ', 1)
_li = lambda n: re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(H, '..', n)).read().strip()).replace('<svg ', '<svg style="height:96px;width:auto;display:block;border-radius:22%" aria-hidden="true" ', 1)
cons = (f'<svg viewBox="0 6 100 92" style="height:230px;width:auto;display:block" aria-hidden="true">{sim("#E4E7EE", "#C9F0F6")}'
        '<rect x="6" y="22" width="88" height="7" rx="3.5" fill="none" stroke="#8A93A8" stroke-width=".5" stroke-dasharray="2 1.5"/>'
        '<rect x="6" y="71" width="88" height="7" rx="3.5" fill="none" stroke="#8A93A8" stroke-width=".5" stroke-dasharray="2 1.5"/>'
        f'<text x="50" y="16" font-size="4.6" text-anchor="middle" fill="{MUTED}" font-family="Poppins">límite superior · 88 × 7</text>'
        f'<text x="50" y="88" font-size="4.6" text-anchor="middle" fill="{MUTED}" font-family="Poppins">límite inferior</text>'
        f'<text x="22" y="57.8" font-size="5" text-anchor="middle" fill="{TINTA}" font-family="Poppins">r 9</text><text x="50" y="47.8" font-size="5" text-anchor="middle" fill="{TINTA}" font-family="Poppins">r 11</text>'
        f'<text x="78" y="54.8" font-size="5" text-anchor="middle" fill="{TINTA}" font-family="Poppins">r 9</text></svg>')
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{FL}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700))
css = ff + f'''
*{{box-sizing:border-box}}body{{margin:0;background:#F2F4F8;color:{TINTA};font:400 14px/1.5 Poppins,sans-serif;padding:32px}}
h1{{font:700 26px/1.2 Poppins;margin:0 0 4px;color:{AZ}}}.lead{{color:{MUTED};max-width:880px;margin:0 0 24px}}
section{{background:#fff;border:1px solid #DFE3EC;border-radius:14px;padding:24px;margin-bottom:20px}}h2{{font:600 12px/1 Poppins;letter-spacing:.06em;text-transform:uppercase;color:{MUTED};margin:0 0 16px}}
.row{{display:flex;flex-wrap:wrap;gap:28px;align-items:center}}.osc{{background:{AZ};border-radius:12px;padding:24px}}.c2{{display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:center}}
.c2 p{{margin:0 0 8px;color:{MUTED}}}.apps{{display:flex;gap:16px;align-items:center;flex-wrap:wrap}}.apps svg{{border-radius:22%}}.cap{{font-size:12px;color:{MUTED}}}
.sw{{display:flex;gap:16px;flex-wrap:wrap}}.sw div{{border-radius:12px;padding:16px;min-width:200px;font-size:13px}}.reg{{margin:0;padding-left:20px}}.reg li{{margin:4px 0}}.tam{{display:flex;gap:18px;align-items:flex-end}}
.sello{{display:inline-flex;align-items:center;gap:10px;border:1px dashed #C9CED8;border-radius:999px;padding:8px 16px 8px 8px;font-size:14px;color:{MUTED}}}.sello b{{color:{AZ}}}
@media (max-width:700px){{.c2{{grid-template-columns:1fr}}}}@media (max-width:480px){{body{{padding:16px}}section{{padding:16px}}}}
'''
tam = ''.join(inl('simbolo', px) for px in (48, 32, 24, 16))
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaResults</title><style>{css}</style><body>'
        f'<h1>NisaResults · paquete final</h1><p class="lead">{tema["producto"]} {tema["arquitectura"]}</p>'
        f'<section><h2>Logotipo</h2><div class="row">{inl("logotipo-respaldo", 96)}{inl("logotipo", 60)}{inl("logotipo-vertical", 150)}</div></section>'
        f'<section><h2>Sobre azul real</h2><div class="osc"><div class="row">{inl("logotipo-respaldo-blanco", 96)}{inl("simbolo-blanco", 56)}</div></div></section>'
        f'<section><h2>Símbolo · construcción</h2><div class="c2">{cons}<div><p>{tema["simbolo"]}</p><p>Las células son de la familia de Colonia (NisaLab) y de las columnas de NisaData; las barras son lo propio de NisaResults.</p><div class="tam">{tam}</div></div></div></section>'
        f'<section><h2>Sello de la página pública</h2><div class="sello">{inl("sello", 32)}<span>Analizada por <b>Nisa Nabani</b> · laboratorio</span></div><p class="cap" style="margin-top:10px">La página del QR lleva la marca del cliente; Nisa Nabani firma como laboratorio con el símbolo en círculo.</p></section>'
        f'<section><h2>Ícono de app y familia</h2><div class="apps">{_li("nisalab-final/svg/app-icon.svg")}{_li("nisadata-final/svg/app-icon.svg")}{inl("app-icon", 96)}{inl("app-icon-maskable", 96)}{inl("favicon", 32)}<span class="cap">NisaLab · NisaData · NisaResults · maskable · favicon</span></div></section>'
        f'<section><h2>Color</h2><div class="sw"><div style="background:{AZ};color:#fff"><b>Azul real</b><br>{AZ}<br>Blanco encima {tema["color"]["azul-real"]["blanco_encima"]}:1</div>'
        f'<div style="background:{CI};color:{AZ}"><b>Cian</b><br>{CI}<br>Azul real encima {tema["color"]["cian"]["sobre_azul"]}:1 · nunca texto sobre blanco ({tema["color"]["cian"]["sobre_blanco"]}:1)</div></div><p class="cap" style="margin-top:10px">{tema["semaforo"]}</p></section>'
        f'<section><h2>Reglas</h2><ol class="reg">{"".join(f"<li>{r}</li>" for r in tema["reglas"])}</ol></section></body></html>')
open(os.path.join(H, 'lamina.html'), 'w').write(html)
print('ok', json.dumps(tema['color'], ensure_ascii=False))
