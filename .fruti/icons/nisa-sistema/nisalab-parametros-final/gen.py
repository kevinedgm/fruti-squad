# NisaLab · tipos de parámetro · paquete final (ficha de elemento, ronda 1 opción B aprobada).
# Uso: python3 gen.py <carpeta con poppins-latin-600-normal.woff> <carpeta temporal> [carpeta de fuentes para la lámina]
# Escribe svg/<tipo>/{ficha,ficha-blanco,ficha-1tinta}.svg, tema.json y lamina.html.
import json, os, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

H = os.path.dirname(os.path.abspath(__file__))
WOFF, TMP = sys.argv[1], sys.argv[2]
FL = sys.argv[3] if len(sys.argv) > 3 else ''
AZ, TINTA, MUTED, W = '#052A76', '#141B33', '#535B70', '#FFFFFF'
TIPOS = [  # clave, nombre, letras, ejemplos
    ('microbiologicos', 'Microbiológicos', 'Mb', 'Coliformes, E. coli, Salmonella, mohos y levaduras'),
    ('fisicoquimicos', 'Fisicoquímicos', 'Fq', 'pH, conductividad, turbidez, dureza, sólidos'),
    ('metales', 'Metales', 'Me', 'Plomo, arsénico, mercurio, cadmio, hierro'),
    ('organicos', 'Orgánicos', 'Or', 'Plaguicidas, compuestos volátiles, hidrocarburos'),
    ('nutrimentales', 'Nutrimentales', 'Nu', 'Proteína, grasa, humedad, cenizas, fibra'),
]
L, R, SIZE = 48, 10.5, 23  # retícula, radio de la ficha, cuerpo de las letras

f = TTFont(os.path.join(WOFF, 'poppins-latin-600-normal.woff')); f.flavor = None
TTF = os.path.join(TMP, 'poppins-600.ttf'); f.save(TTF); f = TTFont(TTF)
CAP = f['OS/2'].sCapHeight / f['head'].unitsPerEm
def letras(s):
    """Trazos de las letras centradas en la ficha: centro óptico por caja real horizontal y por altura de mayúscula vertical."""
    hf = hb.Font(hb.Face(hb.Blob.from_file_path(TTF))); b = hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf, b, {'kern': True})
    gs = f.getGlyphSet(); order = f.getGlyphOrder(); k = SIZE / f['head'].unitsPerEm
    def dibuja(x0, y0):
        x, d, bp = x0, '', BoundsPen(gs)
        for i, ps in zip(b.glyph_infos, b.glyph_positions):
            pen = SVGPathPen(gs); g = gs[order[i.codepoint]]
            g.draw(TransformPen(pen, (k, 0, 0, -k, x, y0))); g.draw(TransformPen(bp, (k, 0, 0, -k, x, y0)))
            d += pen.getCommands(); x += (ps.x_advance - 0.02 * f['head'].unitsPerEm) * k
        return d, bp.bounds
    _, bb = dibuja(0, 0)
    return dibuja(L / 2 - (bb[0] + bb[2]) / 2, L / 2 + CAP * SIZE / 2)
def svg(body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {L}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'
TILE = f'<rect width="{L}" height="{L}" rx="{R}"'

tema = {'sistema': 'NisaLab · tipos de parámetro', 'forma': 'ficha de elemento: cuadrado redondeado con dos letras', 'color': {'ficha': AZ, 'letras': W, 'contraste': 13.13},
        'reglas': ['El tipo nunca usa tono: el círculo de color es del área y el color semántico es del estado.',
                   'La ficha siempre va con el nombre del tipo al lado, salvo en columnas angostas con encabezado «Tipo» y nombre en tooltip y lector de pantalla.',
                   'Mayúscula + minúscula, dos letras, sin punto.'], 'tipos': []}
anchos = {}
for k, n, l, ej in TIPOS:
    d, bb = letras(l); anchos[l] = round(bb[2] - bb[0], 1)
    o = os.path.join(H, 'svg', k); os.makedirs(o, exist_ok=True)
    lab = f'{n} ({l})'
    open(os.path.join(o, 'ficha.svg'), 'w').write(svg(f'{TILE} fill="{AZ}"/><path d="{d}" fill="{W}"/>', lab))
    open(os.path.join(o, 'ficha-blanco.svg'), 'w').write(svg(f'{TILE} fill="{W}"/><path d="{d}" fill="{AZ}"/>', lab))
    open(os.path.join(o, 'ficha-1tinta.svg'), 'w').write(svg(
        f'<defs><mask id="nl-{k}"><rect width="{L}" height="{L}" fill="#fff"/><path d="{d}" fill="#000"/></mask></defs>{TILE} fill="currentColor" mask="url(#nl-{k})"/>', lab))
    tema['tipos'].append({'clave': k, 'nombre': n, 'letras': l, 'ejemplos': ej, 'token': f'parametro-{k}'})
json.dump(tema, open(os.path.join(H, 'tema.json'), 'w'), ensure_ascii=False, indent=2)

# — lámina —
def inl(k, var, px, uid):
    s = open(os.path.join(H, 'svg', k, var + '.svg')).read().strip()
    s = s.replace(f'nl-{k}', f'nl-{k}-{uid}')
    return s.replace('<svg ', f'<svg width="{px}" height="{px}" style="display:block;flex:none" aria-hidden="true" ', 1).replace(s[s.index('<title>'):s.index('</title>') + 8], '')
u = iter(range(10000))
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{FL}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700)) + f"@font-face{{font-family:'IBM Plex Mono';src:url('file://{FL}/IBMPlexMono.ttf')}}" if FL else '<link>'
fonts = '' if FL else '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono&display=swap">'
tarj = ''.join(f'<div class="tj"><div class="tm">{"".join(inl(k, "ficha", px, next(u)) for px in (64, 32, 24, 16))}</div><b>{n}</b><code>{l} · parametro-{k}</code><p>{ej}</p></div>' for k, n, l, ej in TIPOS)
vers = ''.join(f'<div class="vr {c}"><div class="tm">{"".join(inl(k, v, 40, next(u)) for k, *_ in TIPOS)}</div><span>{t}</span></div>'
               for v, c, t in (('ficha', '', 'ficha.svg · sobre fondos claros'), ('ficha-blanco', 'oscuro', 'ficha-blanco.svg · sobre azul real o fotos oscuras'), ('ficha-1tinta', 'tinta', 'ficha-1tinta.svg · una tinta (currentColor), letras caladas')))
filas = [('microbiologicos', 'Coliformes totales', 'Aguas', '#007CA3', '&lt;1.1 NMP/100 mL', 'Conforme', 'ok'), ('fisicoquimicos', 'pH', 'Aguas', '#007CA3', '7.42', 'Conforme', 'ok'),
         ('metales', 'Plomo', 'Alimentos', '#A6552D', '0.031 mg/kg', 'Fuera de límite', 'er'), ('organicos', 'Clorpirifos', 'Agrícolas', '#946400', 'En proceso', 'Pendiente', 'av'),
         ('nutrimentales', 'Proteína', 'Alimentos', '#A6552D', '12.4 g/100 g', 'Conforme', 'ok')]
NOM = {k: n for k, n, *_ in TIPOS}
def tabla():
    return ('<div class="tw"><table><thead><tr><th>Parámetro</th><th>Tipo</th><th>Área</th><th>Resultado</th><th>Estado</th></tr></thead><tbody>'
            + ''.join(f'<tr><td>{p}</td><td><span class="tp">{inl(k, "ficha", 18, next(u))}{NOM[k]}</span></td><td><span class="ar"><i style="background:{ac}"></i>{a}</span></td><td class="m">{r}</td><td><span class="st {ec}">{e}</span></td></tr>' for k, p, a, ac, r, e, ec in filas)
            + '</tbody></table></div>')
grupo = ''.join(f'<div class="gp"><div class="gh">{inl(k, "ficha", 24, next(u))}<b>{NOM[k]}</b><span>{c} parámetros</span></div></div>' for k, c in (('microbiologicos', 6), ('fisicoquimicos', 11), ('metales', 4)))
filtros = ''.join(f'<button class="fc" aria-pressed="{"true" if i == 0 else "false"}">{inl(k, "ficha", 16, next(u))}{n}</button>' for i, (k, n, *_) in enumerate(TIPOS))
css = ff + f'''
:root{{--az:{AZ};--tinta:{TINTA};--gris:{MUTED};--bg:#F2F4F8;--sup:#fff;--borde:#DCE1EA}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--tinta);font:400 14px/1.5 Poppins,sans-serif;padding:32px}}
h1{{font:700 26px/1.2 Poppins;margin:0 0 4px;color:var(--az)}} .lead{{color:var(--gris);margin:0 0 24px;max-width:760px}}
section{{background:var(--sup);border:1px solid var(--borde);border-radius:14px;padding:24px;margin-bottom:20px;box-shadow:0 1px 2px rgba(20,27,51,.06)}}
h2{{font:600 12px/1 Poppins;letter-spacing:.06em;text-transform:uppercase;color:var(--gris);margin:0 0 14px}}
.tjs{{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px}} .tj{{border:1px solid var(--borde);border-radius:10px;padding:14px;display:flex;flex-direction:column;gap:6px}}
.tj p{{margin:0;color:var(--gris);font-size:12px;line-height:1.45}} code{{font:12px 'IBM Plex Mono',monospace;color:var(--gris)}}
.tm{{display:flex;align-items:flex-end;gap:10px;flex-wrap:wrap}} .vrs{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}
.vr{{border:1px solid var(--borde);border-radius:10px;padding:16px;display:flex;flex-direction:column;gap:10px}} .vr span{{font-size:12px;color:var(--gris)}}
.vr.oscuro{{background:var(--az)}} .vr.oscuro span{{color:#fff}} .vr.tinta{{color:{TINTA}}}
.tw{{overflow-x:auto}} table{{width:100%;border-collapse:collapse;font-size:13px}} th{{text-align:left;font-weight:500;color:var(--gris);background:#EEF1F6;padding:8px 10px}} td{{padding:9px 10px;border-top:1px solid var(--borde);white-space:nowrap}}
.m{{font-family:'IBM Plex Mono',monospace;font-size:12px}} .tp,.ar{{display:inline-flex;align-items:center;gap:8px}} .ar i{{width:12px;height:12px;border-radius:50%;display:inline-block}}
.st{{font-size:12px;font-weight:500;border-radius:6px;padding:2px 8px}} .ok{{background:#E3F2E6;color:#1E6B34}} .er{{background:#FCE4E4;color:#A11D1D}} .av{{background:#FFF1CC;color:#7A5200}}
.dos{{display:grid;grid-template-columns:1fr 1fr;gap:20px}} .dos>div{{min-width:0}} .gris{{filter:grayscale(1)}}
.gp{{border-top:1px solid var(--borde);padding:12px 0}} .gh{{display:flex;align-items:center;gap:10px}} .gh span{{color:var(--gris);font-size:12px;margin-left:auto}}
.fcs{{display:flex;flex-wrap:wrap;gap:8px}} .fc{{display:inline-flex;align-items:center;gap:8px;font:500 13px Poppins;color:var(--tinta);background:#fff;border:1px solid var(--borde);border-radius:999px;padding:6px 12px 6px 8px;min-height:32px}}
.fc[aria-pressed=true]{{border-color:var(--az);box-shadow:inset 0 0 0 1px var(--az)}}
ol{{margin:0;padding-left:20px}} li{{margin:4px 0}} .no{{color:#A11D1D}}
@media (max-width:1000px){{.tjs{{grid-template-columns:repeat(2,minmax(0,1fr))}}.vrs,.dos{{grid-template-columns:1fr}}}}
@media (max-width:480px){{body{{padding:16px}}section{{padding:16px}}.tjs{{grid-template-columns:1fr}}}}
'''
reglas = ''.join(f'<li>{r}</li>' for r in tema['reglas'] + ['Tamaño mínimo 16 px en pantalla; 18–20 px en filas de tabla.', 'No rotar, no cambiar el color de la ficha por tipo, no usar contorno solo (a 16 px pierde peso).', 'Un tipo nuevo se agrega con dos letras que no choquen con las existentes ni con símbolos químicos que se lean como resultado (Pb, Hg, As).'])
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Tipos de parámetro</title>{fonts}<style>{css}</style><body>'
        '<h1>NisaLab · tipos de parámetro</h1><p class="lead">Cada tipo de parámetro tiene su ficha, como un elemento de la tabla periódica: dos letras blancas sobre azul real. La forma cuadrada la separa del círculo de color de las áreas, y no usa tono para no competir con el área ni con el estado.</p>'
        f'<section><h2>Fichas</h2><div class="tjs">{tarj}</div></section>'
        f'<section><h2>Versiones</h2><div class="vrs">{vers}</div></section>'
        f'<section><h2>En la interfaz</h2><h2>Tabla de resultados</h2>{tabla()}<h2 style="margin-top:20px">Sin color</h2><div class="gris">{tabla()}</div>'
        f'<div class="dos" style="margin-top:20px"><div><h2>Agrupar</h2>{grupo}</div><div><h2>Filtrar</h2><div class="fcs">{filtros}</div></div></div></section>'
        f'<section><h2>Reglas</h2><ol>{reglas}</ol></section></body></html>')
open(os.path.join(H, 'lamina.html'), 'w').write(html)
print('anchos de letras (de 48):', anchos)
