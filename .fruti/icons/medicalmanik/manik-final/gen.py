# Manik (directorio de pacientes) · paquete final. Uso: python3 gen.py <ruta a Sora[wght].ttf> <scratchpad>
import sys, json
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
SORA, S = sys.argv[1], sys.argv[2]
CIAN, CIAN_UI, INK, AZ, PAPEL = '#009BB0', '#00788A', '#14213D', '#234899', '#F6F8FC'
LINEA = 'M-6 63 L13 63 L27 12 L49 86 L71 25 L84 64 L106 64'
r = 21
PIN = f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H66 Q59 100 56 106 L50 119 L44 106 Q41 100 34 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z'
# — texto a trazos —
_f = {}
def fuente(w):
    if w not in _f:
        f = TTFont(SORA); instantiateVariableFont(f, {'wght': w}, inplace=True); p = f'{S}/sora-{w}.ttf'; f.save(p); _f[w] = (TTFont(p), p)
    return _f[w]
def texto(s, size, x0, y0, w=600, track=0.0):
    f, p = fuente(w); hf = hb.Font(hb.Face(hb.Blob.from_file_path(p))); b = hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf, b, {'kern': True})
    gs = f.getGlyphSet(); order = f.getGlyphOrder(); k = size / f['head'].unitsPerEm; x = x0; d = ''; bp = BoundsPen(gs)
    for i, ps in zip(b.glyph_infos, b.glyph_positions):
        pen = SVGPathPen(gs); g = gs[order[i.codepoint]]; g.draw(TransformPen(pen, (k, 0, 0, -k, x, y0))); g.draw(TransformPen(bp, (k, 0, 0, -k, x, y0))); d += pen.getCommands(); x += ps.x_advance * k + track * size
    return d, bp.bounds
# — sello —
def sello(fondo=CIAN, linea=PAPEL, uid='m', x=0, y=0, k=1.0, mono=False):
    t = f'translate({x} {y}) scale({k})'
    if mono:  # una tinta: la línea queda calada
        return (f'<defs><mask id="{uid}" maskUnits="userSpaceOnUse" x="-10" y="-10" width="130" height="140"><path d="{PIN}" fill="#fff"/><path d="{LINEA}" fill="none" stroke="#000" stroke-width="13" stroke-linejoin="round"/></mask></defs>'
                f'<g transform="{t}"><path d="{PIN}" fill="{fondo}" mask="url(#{uid})"/></g>')
    return (f'<defs><clipPath id="{uid}"><path d="{PIN}"/></clipPath></defs><g transform="{t}"><path d="{PIN}" fill="{fondo}"/>'
            f'<path clip-path="url(#{uid})" d="{LINEA}" fill="none" stroke="{linea}" stroke-width="13" stroke-linejoin="round"/></g>')
def svg(vb, body, label): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n'
out = {}
out['simbolo'] = svg('-2 -2 104 123', sello(), 'Manik')
out['simbolo-1tinta'] = svg('-2 -2 104 123', sello(fondo='currentColor', mono=True, uid='t'), 'Manik')
out['simbolo-blanco'] = svg('-2 -2 104 123', sello(fondo='#FFFFFF', mono=True, uid='w'), 'Manik')
# logotipo: «manik» Sora 600, tracking −0.04
wd, wb = texto('manik', 100, 0, 0, 600, -0.04); W = wb[2] - wb[0]; H = -wb[1]  # altura sobre la línea base
def lockup(color_txt, endoso=False, fondo_sello=CIAN, mono=False, uid='l'):
    k = (H * 1.18) / 119; sx = 0; sw = 100 * k; gap = H * 0.32
    tx = sw + gap - wb[0]; ty = H * 0.98
    d, _ = texto('manik', 100, tx, ty, 600, -0.04)
    body = sello(fondo=fondo_sello, uid=uid, x=0, y=(ty - H) - 0.06 * H, k=k, mono=mono) + f'<path d="{d}" fill="{color_txt}"/>'
    w = sw + gap + W
    if endoso:
        de, eb = texto('de MedicalManik', 24, w + 22, ty, 500, 0); body += f'<path d="M{w+11:.1f} {ty-H*0.75:.1f} V{ty+2:.1f}" stroke="{color_txt if color_txt!=INK else "#C9D1DF"}" stroke-width="1.5"/><path d="{de}" fill="{AZ if color_txt==INK else color_txt}"/>'
        w = eb[2]
    return svg(f'-2 {ty-H-0.08*H-14:.1f} {w+4:.1f} {H*1.18+28:.1f}', body, 'Manik' + (' de MedicalManik' if endoso else ''))
out['logotipo'] = lockup(INK)
out['logotipo-blanco'] = lockup('#FFFFFF', uid='lb')
out['logotipo-1tinta'] = lockup('currentColor', fondo_sello='currentColor', mono=True, uid='l1')
out['logotipo-endoso'] = lockup(INK, endoso=True, uid='le')
# vertical
k = 120 / 119; d, vb2 = texto('manik', 64, 0, 0, 600, -0.04); vw = vb2[2] - vb2[0]
out['logotipo-vertical'] = svg(f'{-max(0,(vw-100*k)/2)-4:.1f} -4 {max(vw,100*k)+8:.1f} {120+20+64+12}', sello(uid='lv', k=k) + f'<path d="{texto("manik",64,(100*k-vw)/2-vb2[0],120+20+64*0.74,600,-0.04)[0]}" fill="{INK}"/>', 'Manik')
# ícono de app: sello sobre blanco con aire
out['app-icon'] = svg('0 0 1024 1024', f'<rect width="1024" height="1024" rx="0" fill="#FFFFFF"/>' + sello(uid='ai', x=232, y=178, k=5.6), 'Manik')
out['favicon'] = svg('-2 -2 104 123', sello(uid='fv'), 'Manik')
for k_, v in out.items(): open(f'svg/{k_}.svg', 'w').write(v)
def lum(h):
    c = [int(h[i:i+2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]; return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 2)
json.dump({'marca': 'Manik', 'respaldo': 'de MedicalManik', 'lema': 'Tu médico, a la mano.',
  'color': {'manik-cian': {'hex': CIAN, 'uso': 'el sello y grandes áreas de marca', 'blanco_encima': cr('#FFFFFF', CIAN)},
            'manik-cian-ui': {'hex': CIAN_UI, 'uso': 'botones, enlaces y texto en cian (texto blanco encima)', 'blanco_encima': cr('#FFFFFF', CIAN_UI)},
            'tinta': {'hex': INK, 'uso': 'texto y logotipo'}, 'azul-medicalmanik': {'hex': AZ, 'uso': 'solo en «de MedicalManik»'},
            'calificacion': {'hex': '#F2B33D', 'uso': 'estrellas (gráfico); el número va en tinta'}},
  'tipografia': {'logotipo': 'Sora 600, tracking −0.04 em, en minúsculas, convertido a trazos', 'interfaz': 'Atkinson Hyperlegible Next, como el ecosistema'}},
  open('tema.json', 'w'), ensure_ascii=False, indent=2)
print('ok', list(out))
