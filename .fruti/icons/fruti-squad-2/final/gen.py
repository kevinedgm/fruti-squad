# Fruti Squad · paquete final de marca (identidad nueva, 2026-10-30).
# Símbolos (sistema Átomos): Squad «Espiral», Kiwi «Tres tamaños», Lima «Biblioteca», Coco «Visor», Bruno «Cierre», Mora «Red de conocimiento».
# Color: duotono (trazo neutro; el punto, la evidencia, en el color de cada integrante; el orquestador reúne los cinco). Letra: Bricolage Grotesque.
# Uso: python3 gen.py <carpeta con BricolageGrotesque[opsz,wdth,wght].ttf> → <id>/svg/*.svg, tema.json, lamina.html
import os, sys, json
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
H = os.path.dirname(os.path.abspath(__file__)); FD = sys.argv[1]
INK, WHITE, DARK, PAPER = '#18181b', '#ffffff', '#0f0f12', '#f5f5f2'
SUB_L, SUB_D = '#52525b', '#b9b9b4'
M = {  # id: nombre, producto, color vivo (oscuro), color sobre claro, verbo
 'squad': ('Fruti Squad', 'Workflow Pack', None, None, 'orquestar'),
 'kiwi': ('Kiwi', 'UX Architect', '#34e0a1', '#0f9e6e', 'estructura'),
 'lima': ('Lima', 'Design System Governance', '#d4ff3a', '#6f8c00', 'gobierna'),
 'coco': ('Coco', 'UI Audit', '#ff9f1c', '#c26a00', 'audita'),
 'bruno': ('Bruno', 'Frontend Implementation Engineer', '#4361ee', '#3a54d6', 'implementa'),
 'mora': ('Mora', 'Documentation & Knowledge Engineer', '#f72585', '#d0156e', 'documenta'),
}
ORDER = ['kiwi', 'lima', 'coco', 'bruno', 'mora']
def lum(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def cr(a, b): x, y = sorted((lum(a), lum(b))); return round((y + .05) / (x + .05), 2)
# ---- geometría (64×64) ----
def d(x, y, r, f='§'): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}"/>'
def fr(x, y, w, h, r, fill='none'): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" stroke="§" stroke-width="3.5" fill="{fill}"/>'
def ln(p, w=3.5): return f'<path d="{p}" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
SYM = {
 'squad': ''.join(f'<rect x="{32 - s / 2}" y="{32 - s / 2}" width="{s}" height="{s}" rx="{rx}" stroke="§" stroke-width="3" transform="rotate({i * 11} 32 32)"/>' for i, (s, rx) in enumerate([(54, 14), (43, 11), (33, 9), (24, 7), (16, 5)])) + d(32, 32, 4, 'ª'),
 'kiwi': fr(4, 4, 56, 56, 12) + fr(13, 13, 38, 38, 9) + fr(21, 21, 22, 22, 6) + d(32, 32, 5.5, 'ª'),
 'lima': fr(20, 4, 40, 34, 9) + fr(12, 13, 40, 34, 9, '¤') + fr(4, 22, 40, 36, 9, '¤') + d(24, 40, 6, 'ª'),
 'coco': ln('M4 18V12a8 8 0 0 1 8-8h6M46 4h6a8 8 0 0 1 8 8v6M60 46v6a8 8 0 0 1-8 8h-6M18 60h-6a8 8 0 0 1-8-8v-6') + fr(18, 18, 28, 28, 7) + d(32, 32, 5.5, 'ª'),
 'bruno': '<path d="M27 4H16A12 12 0 0 0 4 16v32a12 12 0 0 0 12 12h3" stroke="§" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="5 5"/><path d="M37 60h11a12 12 0 0 0 12-12V16A12 12 0 0 0 48 4h-3" stroke="§" stroke-width="3.5" stroke-linecap="round"/>' + ln('M38 6L26 58', 4) + d(44, 32, 5.5, 'ª'),
 'mora': fr(4, 4, 56, 56, 12) + ln('M19 19L44 21M44 21L45 45M44 21L20 44', 3) + d(19, 19, 6, 'ª') + d(44, 21, 4.5) + d(45, 45, 4.5) + d(20, 44, 4.5),
}
def grad(gid, dark):
    stops = ''.join(f'<stop offset="{i/4:.2f}" stop-color="{M[k][2] if dark else M[k][3]}"/>' for i, k in enumerate(ORDER))
    return f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">{stops}</linearGradient></defs>'
def body(k, line, dot, bg, gid='g'):
    defs = ''
    if dot == 'GRAD_D' or dot == 'GRAD_L':
        defs = grad(gid, dot == 'GRAD_D'); dot = f'url(#{gid})'
    return defs + SYM[k].replace('§', line).replace('ª', dot).replace('¤', bg)
def dotc(k, dark): return ('GRAD_D' if dark else 'GRAD_L') if k == 'squad' else (M[k][2] if dark else M[k][3])
def svg(inner, vb='0 0 64 64', label=None):
    a = f' role="img" aria-label="{label.replace("&", "&amp;")}"' if label else ' aria-hidden="true"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none"{a}>{inner}</svg>'
# ---- texto en trazos ----
def inst(w):
    p = f'/tmp/fs-bricolage-{w}.ttf'
    if not os.path.exists(p): instancer.instantiateVariableFont(TTFont(FD + '/BricolageGrotesque[opsz,wdth,wght].ttf'), {'wght': w, 'opsz': 32, 'wdth': 100}).save(p)
    return p
FT = {w: (inst(w), TTFont(inst(w))) for w in (400, 700)}
def palabra(s, size, x0, y0, w):
    path, font = FT[w]; upm = font['head'].unitsPerEm
    hf = hb.Font(hb.Face(hb.Blob.from_file_path(path))); b = hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf, b, {'kern': True})
    gs = font.getGlyphSet(); order = font.getGlyphOrder(); k = size / upm; x = x0; dd = ''
    for i, ps in zip(b.glyph_infos, b.glyph_positions):
        pen = SVGPathPen(gs); gs[order[i.codepoint]].draw(TransformPen(pen, (k, 0, 0, -k, x, y0))); dd += pen.getCommands(); x += ps.x_advance * k
    return dd, x
def lockup(k, dark, gid):
    n, p = M[k][0], M[k][1]
    d1, x1 = palabra(n, 30, 0, 26, 700); d2, x2 = palabra(p, 15, 0, 48, 400)
    w = 72 + max(x1, x2) + 2
    s = body(k, WHITE if dark else INK, dotc(k, dark), DARK if dark else WHITE, gid)
    return svg(f'<g transform="scale(.875)">{s}</g><g transform="translate(70 0)"><path d="{d1}" fill="{WHITE if dark else INK}"/><path d="{d2}" fill="{SUB_D if dark else SUB_L}"/></g>', f'0 0 {w:.0f} 56', f'{n} {p}')
def app(k, gid, r=112):
    s = body(k, WHITE, dotc(k, True), DARK, gid)
    return svg(f'<rect width="512" height="512" rx="{r}" fill="{DARK}"/><g transform="translate(96 96) scale(5)">{s}</g>', '0 0 512 512', M[k][0])
tema = {'nombre': 'Fruti Squad', 'sistema': 'Átomos: el punto es la evidencia que cada agente produce y entrega; marcos redondeados en trazo 3.5',
        'color': {'tinta': INK, 'blanco': WHITE, 'oscuro': DARK, 'papel': PAPER, 'sub_claro': SUB_L, 'sub_oscuro': SUB_D},
        'tipografia': {'marca': 'Bricolage Grotesque 700 (opsz 32) en trazos', 'producto': 'Bricolage Grotesque 400', 'web': 'https://fonts.google.com/specimen/Bricolage+Grotesque'},
        'reglas': ['El trazo siempre es neutro (tinta en claro, blanco en oscuro); el color vive solo en el punto.',
                   'Cada integrante firma su evidencia con su color; el orquestador reúne los cinco en degradado.',
                   'En fondo claro se usan los tonos oscurecidos (color_claro); los vivos solo sobre oscuro.',
                   'El color nunca es la única señal: cada integrante se reconoce por su silueta.',
                   'Las plataformas (Codex, Kiro, Claude Code) se nombran en texto; nunca sus logotipos dentro de la marca.'],
        'productos': {}}
for k, (n, p, viv, cla, v) in M.items():
    out = f'{H}/{k}/svg'; os.makedirs(out, exist_ok=True)
    F = {
     'simbolo': svg(body(k, INK, dotc(k, False), WHITE, f'g{k}1'), label=n),
     'simbolo-oscuro': svg(body(k, WHITE, dotc(k, True), DARK, f'g{k}2'), label=n),
     'simbolo-tinta': svg(SYM[k].replace('§', 'currentColor').replace('ª', 'currentColor').replace('¤', 'none'), label=n),
     'lockup': lockup(k, False, f'g{k}3'), 'lockup-oscuro': lockup(k, True, f'g{k}4'),
     'app-icon': app(k, f'g{k}5'),
     'favicon': (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none"><style>:root{{--l:{INK};--b:#fff}}@media(prefers-color-scheme:dark){{:root{{--l:{WHITE};--b:{DARK}}}}}</style>'
                 + body(k, 'var(--l)', (M[k][3] if k != 'squad' else INK) if True else '', 'var(--b)', f'g{k}6').replace('url(#g' + k + '6)', INK) + '</svg>'),
    }
    for name, s in F.items(): open(f'{out}/{name}.svg', 'w').write(s)
    tema['productos'][k] = {'nombre': n, 'producto': p, 'verbo': v, 'color_oscuro': viv, 'color_claro': cla,
                            'contraste': None if not viv else {'vivo/oscuro': cr(viv, DARK), 'claro/blanco': cr(cla, WHITE)}}
json.dump(tema, open(f'{H}/tema.json', 'w'), indent=2, ensure_ascii=False)
# ---- lámina ----
def img(k, n, cls=''): return f'<img class="{cls}" src="{k}/svg/{n}.svg" alt="">'
fila = ''.join(f'<figure>{img(k, "simbolo", "s")}<figcaption><b>{M[k][0]}</b><span>{M[k][1]}</span></figcaption></figure>' for k in ['squad'] + ORDER)
filad = ''.join(f'<figure>{img(k, "simbolo-oscuro", "s")}<figcaption><b>{M[k][0]}</b></figcaption></figure>' for k in ['squad'] + ORDER)
tinta = ''.join(img(k, 'simbolo-tinta', 't') for k in ['squad'] + ORDER)
apps = ''.join(img(k, 'app-icon', 'a') for k in ['squad'] + ORDER)
locks = ''.join(f'<div class="lkc">{img(k, "lockup", "l")}</div>' for k in ['squad'] + ORDER)
locksd = ''.join(f'<div class="lkc dk">{img(k, "lockup-oscuro", "l")}</div>' for k in ['squad', 'coco'])
pal = ''.join(f'<div class="sw"><i style="background:{M[k][2]}"></i><i style="background:{M[k][3]}"></i><span><b>{M[k][0]}</b><code>{M[k][2]} · {M[k][3]}</code></span></div>' for k in ORDER)
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{PAPER};color:{INK};font:400 15px/1.5 'Bricolage Grotesque',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font:700 30px/1.15 'Bricolage Grotesque';margin:0}}.lead{{margin:0;color:#4b4b47;max-width:860px}}
.p{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;gap:14px;min-width:0}}.p.dk{{background:{DARK};border-color:{DARK};color:#fff}}h2{{font:700 13px 'Bricolage Grotesque';letter-spacing:.06em;text-transform:uppercase;margin:0;opacity:.7}}
.fam{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px}}.fam figure{{margin:0;display:grid;justify-items:center;gap:6px;text-align:center}}.fam .s{{width:72px;height:72px}}.fam figcaption{{display:grid;line-height:1.2}}.fam span{{font-size:12.5px;opacity:.7}}
.row{{display:flex;flex-wrap:wrap;gap:16px;align-items:center}}.t{{width:40px;height:40px}}.a{{width:72px;height:72px;border-radius:16px}}
.lks{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}}.lkc{{border:1px solid #ececE6;border-radius:12px;padding:16px;min-width:0}}.lkc.dk{{background:{DARK};border-color:{DARK}}}.l{{height:44px;max-width:100%}}
.pal{{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}}.sw{{display:grid;grid-template-columns:28px 28px 1fr;gap:6px;align-items:center}}.sw i{{width:28px;height:28px;border-radius:8px}}.sw span{{display:grid;line-height:1.2}}.sw code{{font-size:11px;color:#6b6b66}}
ol{{margin:0;padding-left:20px}}li{{margin:3px 0}}
@media (max-width:900px){{.fam{{grid-template-columns:repeat(3,minmax(0,1fr))}}.lks{{grid-template-columns:1fr}}.pal{{grid-template-columns:1fr 1fr}}}}'''
reglas = ''.join(f'<li>{r}</li>' for r in tema['reglas'])
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · marca</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,700&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>Fruti Squad · paquete de marca</h1>'
        '<p class="lead">Seis especialistas, un mismo idioma: marcos redondeados y un punto, la evidencia que cada agente produce y entrega. El trazo es neutro; el punto lleva el color de quien lo firma. Para Codex, Kiro y Claude Code.</p>'
        f'<section class="p"><h2>Símbolos · claro</h2><div class="fam">{fila}</div></section>'
        f'<section class="p dk"><h2>Símbolos · oscuro</h2><div class="fam">{filad}</div></section>'
        f'<section class="p"><h2>Una tinta · app icons</h2><div class="row">{tinta}</div><div class="row">{apps}</div></section>'
        f'<section class="p"><h2>Logotipos de producto</h2><div class="lks">{locks}{locksd}</div></section>'
        f'<section class="p"><h2>Color · vivo (oscuro) y claro</h2><div class="pal">{pal}</div></section>'
        f'<section class="p"><h2>Reglas</h2><ol>{reglas}</ol></section></main></body></html>')
open(f'{H}/lamina.html', 'w').write(html)
print('ok', json.dumps({k: v['contraste'] for k, v in tema['productos'].items()}))
