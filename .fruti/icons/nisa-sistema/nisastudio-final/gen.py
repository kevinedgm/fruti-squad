# NisaStudio · paquete final. App interna de Nisa Nabani para crear piezas de redes con plantillas de la marca.
# Símbolo «Encuadre» (ronda 1, opción 1); color «Índigo → turquesa» (ronda 3, opción C).
# Uso: python3 gen.py <carpeta con poppins-latin-{400,700}-normal.woff> <carpeta temporal> <carpeta de fuentes para la lámina>; después node png.cjs
import json, os, re, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
H = os.path.dirname(os.path.abspath(__file__)); WOFF, TMP, FL = sys.argv[1], sys.argv[2], sys.argv[3]
C1, C2, IN, AM, W, MUTED, TINTA = '#4F46E5', '#14B8A6', '#3730A3', '#FDE68A', '#FFFFFF', '#535B70', '#141B33'

# — símbolo: dos esquinas de recorte (trazo 8, puntas redondas) y tres células dentro; la mediana, arriba a la derecha, en acento —
# caja útil 6–94 en ambos ejes
def sim(c=IN, a=C2, x=0, y=0, k=1.0):
    P = lambda px, py: f'{x + px * k:.2f} {y + py * k:.2f}'
    sw, r6 = 8 * k, 6 * k
    return (f'<path d="M{P(10, 34)} V{y + 16 * k:.2f} a{r6:.2f} {r6:.2f} 0 0 1 {r6:.2f} {-r6:.2f} H{x + 34 * k:.2f}" fill="none" stroke="{c}" stroke-width="{sw:.2f}" stroke-linecap="round"/>'
            f'<path d="M{P(90, 66)} V{y + 84 * k:.2f} a{r6:.2f} {r6:.2f} 0 0 1 {-r6:.2f} {r6:.2f} H{x + 66 * k:.2f}" fill="none" stroke="{c}" stroke-width="{sw:.2f}" stroke-linecap="round"/>'
            f'<circle cx="{x + 44 * k:.2f}" cy="{y + 56 * k:.2f}" r="{15 * k:.2f}" fill="{c}"/><circle cx="{x + 66 * k:.2f}" cy="{y + 38 * k:.2f}" r="{11 * k:.2f}" fill="{a}"/>'
            f'<circle cx="{x + 64 * k:.2f}" cy="{y + 64 * k:.2f}" r="{6 * k:.2f}" fill="{c}"/>')
GRAD = f'<defs><linearGradient id="nsg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{C1}"/><stop offset="1" stop-color="{C2}"/></linearGradient></defs>'
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
    d1, b1, x1 = texto('Nisa', size, x0, y0, 700); d2, b2, _ = texto('Studio', size, x1 + size * 0.01, y0, 400)
    return d1 + d2, (b1[0], min(b1[1], b2[1]), b2[2], max(b1[3], b2[3]))
def svg(vb, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'

S = 100; SZ = 1.15 * S; KS = SZ / 88; GAP = 0.24 * S
def horizontal(txt, c=IN, a=C2, respaldo=False):
    base = SZ / 2 + CAP * S / 2
    body = sim(c, a, -6 * KS, -6 * KS, KS); d, bb = nombre(SZ + GAP, base, S); body += f'<path d="{d}" fill="{txt}"/>'; w = bb[2]
    if respaldo:
        dr, br, _ = texto('de ', 34, SZ + GAP + 2, base + 52, 400); dn, bn, _ = texto('Nisa Nabani', 34, br[2] + 9, base + 52, 700)
        body += f'<path d="{dr}" fill="{MUTED if txt == IN else txt}"/><path d="{dn}" fill="{txt}"/>'; w = max(w, bn[2]); h = base + 62
    else:
        h = SZ
    return svg(f'-4 -4 {w + 8:.1f} {h + 8:.1f}', body, 'NisaStudio' + (' de Nisa Nabani' if respaldo else ''))
def vertical(txt=IN):
    k = 1.8; ts = 64; d, bb = nombre(0, 0, ts); tw = bb[2] - bb[0]; sw = 88 * k; an = max(sw, tw)
    d, bb = nombre((an - tw) / 2 - bb[0], sw + 30 + CAP * ts, ts)
    return svg(f'-6 -6 {an + 12:.1f} {sw + 30 + CAP * ts + 22:.1f}', sim(x=(an - sw) / 2 - 6 * k, y=-6 * k, k=k) + f'<path d="{d}" fill="{txt}"/>', 'NisaStudio')
def icono(ancho, rx=0, lado=1024):  # símbolo blanco + amarillo claro sobre el degradado
    k = ancho / 88; o = (lado - 88 * k) / 2 - 6 * k
    return svg(f'0 0 {lado} {lado}', GRAD + f'<rect width="{lado}" height="{lado}" rx="{rx}" fill="url(#nsg)"/>' + sim(W, AM, o, o, k), 'NisaStudio')
out = {
    'simbolo': svg('4 4 92 92', sim(), 'NisaStudio'), 'simbolo-blanco': svg('4 4 92 92', sim(W, AM), 'NisaStudio'),
    'simbolo-1tinta': svg('4 4 92 92', sim('currentColor', 'currentColor'), 'NisaStudio'),
    'logotipo': horizontal(IN), 'logotipo-blanco': horizontal(W, W, AM), 'logotipo-1tinta': horizontal('currentColor', 'currentColor', 'currentColor'),
    'logotipo-respaldo': horizontal(IN, respaldo=True), 'logotipo-respaldo-blanco': horizontal(W, W, AM, respaldo=True), 'logotipo-vertical': vertical(),
    'app-icon': icono(560), 'app-icon-maskable': icono(440), 'favicon': icono(76, 22, 100),
}
os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
for k_, v in out.items(): open(os.path.join(H, 'svg', k_ + '.svg'), 'w').write(v)

def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)
tema = {'marca': 'NisaStudio', 'respaldo': 'de Nisa Nabani',
        'producto': 'App interna de Nisa Nabani para crear piezas de redes y avisos con plantillas de la marca: efemérides, avisos, promoción de servicios y carruseles «¿Sabías que…?».',
        'arquitectura': 'Cuarta app de la familia (después de NisaLab, NisaData y NisaResults); entra por hub.nisanabani.com. Su color es de producto: las piezas que genera llevan la identidad de Nisa Nabani, no la de NisaStudio.',
        'simbolo': 'Encuadre: dos esquinas de recorte y tres células dentro; la mediana, arriba a la derecha, en acento. Componer una pieza.',
        'color': {'indigo': {'hex': C1, 'uso': 'inicio del degradado; fondo con texto blanco', 'blanco_encima': cr(W, C1)},
                  'turquesa': {'hex': C2, 'uso': 'fin del degradado y acento del símbolo sobre blanco; nunca texto', 'blanco_encima': cr(W, C2)},
                  'indigo-profundo': {'hex': IN, 'uso': 'logotipo y símbolo sobre fondos claros', 'sobre_blanco': cr(IN, W)},
                  'amarillo-claro': {'hex': AM, 'uso': 'acento del símbolo sobre el degradado', 'sobre_indigo': cr(AM, C1)}},
        'degradado': f'135°, {C1} → {C2}',
        'tipografia': {'logotipo': '«Nisa» Poppins 700 + «Studio» Poppins 400, convertidos a trazos', 'interfaz': 'Poppins'},
        'reglas': ['El texto blanco pequeño va sobre el lado índigo del degradado; sobre el turquesa solo títulos grandes.',
                   'Una sola célula de acento por símbolo.',
                   'El índigo y el turquesa son de la app; las piezas que salen de NisaStudio usan la identidad de Nisa Nabani.',
                   'No rotar el encuadre ni mover las células fuera de las esquinas.'],
        'tamano_minimo': {'pantalla_px': 16, 'impreso_mm': 6}}
json.dump(tema, open(os.path.join(H, 'tema.json'), 'w'), ensure_ascii=False, indent=2)

def inl(n, h):
    s = re.sub(r'<title>.*?</title>', '', out[n]).replace('id="nsg"', f'id="nsg-{n}"').replace('url(#nsg)', f'url(#nsg-{n})')
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block;max-width:100%" aria-hidden="true" ', 1)
_li = lambda n: re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(H, '..', n)).read().strip()).replace('<svg ', '<svg style="height:96px;width:auto;display:block;border-radius:22%" aria-hidden="true" ', 1)
G = f'linear-gradient(135deg,{C1},{C2})'
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{FL}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700))
css = ff + f'''
*{{box-sizing:border-box}}body{{margin:0;background:#F2F4F8;color:{TINTA};font:400 14px/1.5 Poppins,sans-serif;padding:32px}}
h1{{font:700 26px/1.2 Poppins;margin:0 0 4px;color:{IN}}}.lead{{color:{MUTED};max-width:880px;margin:0 0 24px}}
section{{background:#fff;border:1px solid #DFE3EC;border-radius:14px;padding:24px;margin-bottom:20px}}h2{{font:600 12px/1 Poppins;letter-spacing:.06em;text-transform:uppercase;color:{MUTED};margin:0 0 16px}}
.row{{display:flex;flex-wrap:wrap;gap:28px;align-items:center}}.osc{{background:{G};border-radius:12px;padding:24px}}.apps{{display:flex;gap:16px;align-items:center;flex-wrap:wrap}}.apps svg{{border-radius:22%}}.cap{{font-size:12px;color:{MUTED}}}
.sw{{display:flex;gap:12px;flex-wrap:wrap}}.sw div{{border-radius:12px;padding:16px;min-width:180px;font-size:13px}}.reg{{margin:0;padding-left:20px}}.reg li{{margin:4px 0}}.tam{{display:flex;gap:18px;align-items:flex-end;margin-top:14px}}
@media (max-width:480px){{body{{padding:16px}}section{{padding:16px}}}}
'''
tam = ''.join(inl('simbolo', px) for px in (64, 48, 32, 24, 16))
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaStudio</title><style>{css}</style><body>'
        f'<h1>NisaStudio · paquete final</h1><p class="lead">{tema["producto"]} {tema["arquitectura"]}</p>'
        f'<section><h2>Logotipo</h2><div class="row">{inl("logotipo-respaldo", 96)}{inl("logotipo", 60)}{inl("logotipo-vertical", 150)}</div></section>'
        f'<section><h2>Sobre el degradado</h2><div class="osc"><div class="row">{inl("logotipo-respaldo-blanco", 96)}{inl("simbolo-blanco", 64)}</div></div></section>'
        f'<section><h2>Símbolo</h2><p>{tema["simbolo"]}</p><div class="tam">{tam}</div></section>'
        f'<section><h2>Ícono de app y familia</h2><div class="apps">{_li("nisalab-final/svg/app-icon.svg")}{_li("nisadata-final/svg/app-icon.svg")}{_li("nisaresults-final/svg/app-icon.svg")}{inl("app-icon", 96)}{inl("app-icon-maskable", 96)}{inl("favicon", 32)}<span class="cap">NisaLab · NisaData · NisaResults · NisaStudio · maskable · favicon</span></div></section>'
        f'<section><h2>Color</h2><div class="sw"><div style="background:{G};color:#fff;min-width:260px"><b>Degradado</b><br>{tema["degradado"]}</div><div style="background:{C1};color:#fff"><b>Índigo</b><br>{C1} · blanco {tema["color"]["indigo"]["blanco_encima"]}:1</div>'
        f'<div style="background:{C2};color:{TINTA}"><b>Turquesa</b><br>{C2} · blanco {tema["color"]["turquesa"]["blanco_encima"]}:1</div><div style="background:{IN};color:#fff"><b>Índigo profundo</b><br>{IN} · sobre blanco {tema["color"]["indigo-profundo"]["sobre_blanco"]}:1</div>'
        f'<div style="background:{AM};color:{TINTA}"><b>Amarillo claro</b><br>{AM} · acento sobre degradado</div></div></section>'
        f'<section><h2>Reglas</h2><ol class="reg">{"".join(f"<li>{r}</li>" for r in tema["reglas"])}</ol></section></body></html>')
open(os.path.join(H, 'lamina.html'), 'w').write(html)
print('ok', json.dumps({k: v.get('blanco_encima', v.get('sobre_blanco', v.get('sobre_indigo'))) for k, v in tema['color'].items()}))
