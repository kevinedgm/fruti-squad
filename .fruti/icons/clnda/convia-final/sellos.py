# Convia · sellos y logotipos por categoría. Uso: python3 sellos.py <carpeta con Fraunces-Suave-500.ttf y Figtree-650.ttf>
# Figtree-650.ttf = instancia wght 650 de Figtree variable. Colores desde tema.json (categorías).
import sys, os, re, json, math
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FD = sys.argv[1] if len(sys.argv) > 1 else '.'
D = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(D, 'tema.json'))); C = T['color']; CAT = T['categorias']
STAR = re.search(r'<path d="([^"]+)"', open(os.path.join(D, '..', 'convia-r7', 'E1b.svg')).read()).group(1)
FR, FG = os.path.join(FD, 'Fraunces-Suave-500.ttf'), os.path.join(FD, 'Figtree-650.ttf')
_cache = {}
def font(path):
    if path not in _cache:
        tt = TTFont(path); _cache[path] = (hb.Font(hb.Face(hb.Blob.from_file_path(path))), tt, tt.getGlyphSet(), tt['head'].unitsPerEm, tt.getGlyphOrder())
    return _cache[path]
def shape(path, text, size, track=0):
    f, tt, gs, upm, order = font(path); s = size / upm
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties(); hb.shape(f, buf, {'kern': True})
    out, x = [], 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        adv = pos.x_advance * s + track; out.append((order[info.codepoint], x, adv)); x += adv
    return out, x - track, s
def line(path, text, size, x0, y0, track=0):
    gl, w, s = shape(path, text, size, track); f, tt, gs, upm, order = font(path); pen = SVGPathPen(gs)
    for g, x, _ in gl: gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x0 + x, y0)))
    return pen.getCommands(), w
def arc(path, text, size, cx, cy, r, top=True, track=0):
    # texto sobre un arco: arriba se lee en sentido horario; abajo, de izquierda a derecha por dentro
    gl, w, s = shape(path, text, size, track); f, tt, gs, upm, order = font(path); out = ''
    for g, x, adv in gl:
        mid = x + adv / 2 - w / 2
        if top:
            a = -math.pi / 2 + mid / r; px, py = cx + r * math.cos(a), cy + r * math.sin(a); rot = math.degrees(a) + 90
        else:
            a = math.pi / 2 - mid / r; px, py = cx + r * math.cos(a), cy + r * math.sin(a); rot = math.degrees(a) - 90
        pen = SVGPathPen(gs); gw = gs[g].width * s
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, -gw / 2, 0)))
        out += f'<path transform="translate({px:.2f} {py:.2f}) rotate({rot:.2f})" d="{pen.getCommands()}"/>'
    return out
def star(fill, size, x, y):
    return f'<path transform="translate({x:.2f} {y:.2f}) scale({size / 200:.4f})" d="{STAR}" fill="{fill}"/>'
def sello(nombre, fondo, tinta, ring=None):
    ring = ring or tinta
    top = arc(FG, 'CONVIA · OAXACA', 15, 120, 120, 86, True, 2.2)
    bot = arc(FG, nombre.upper(), 15, 120, 120, 97, False, 2.2)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" role="img" aria-label="Convia {nombre}">'
            f'<circle cx="120" cy="120" r="116" fill="{fondo}"/><circle cx="120" cy="120" r="108" fill="none" stroke="{ring}" stroke-width="1.6"/>'
            f'<circle cx="120" cy="120" r="70" fill="none" stroke="{ring}" stroke-width="1" stroke-dasharray="2 4"/>'
            f'<g fill="{tinta}">{top}{bot}</g>' + star(tinta, 92, 74, 74) + '</svg>')
def logotipo(nombre, star_c, txt, cat_c):
    tp, tw = line(FR, 'Convia', 58, 74, 52)
    cp, cw = line(FR, nombre, 58, 74 + tw + 22, 52)
    sep = f'<rect x="{74 + tw + 9:.1f}" y="18" width="2" height="40" rx="1" fill="{cat_c}"/>'
    W = 74 + tw + 22 + cw + 4
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} 68" role="img" aria-label="Convia {nombre}">'
            + star(star_c, 64, 0, 2) + f'<path d="{tp}" fill="{txt}"/>{sep}<path d="{cp}" fill="{cat_c}"/></svg>')
n = 0
for k, c in CAT.items():
    fs = {f'sellos/{k}-sello.svg': sello(c['nombre'], c['fondo'], c['texto']),
          f'sellos/{k}-sello-solido.svg': sello(c['nombre'], c['texto'], C['papel']),
          f'sellos/{k}-logotipo.svg': logotipo(c['nombre'], C['cantera'], C['tinta'], c['texto'])}
    for p, v in fs.items():
        open(os.path.join(D, p), 'w').write(v); n += 1
print('ok', n)
