# NisaStudio · ronda 1: color propio (A/B/C) y símbolo (1/2/3), decisiones separadas.
# App interna para generar piezas de redes con plantillas de la marca (efemérides, avisos, promociones, carruseles «¿Sabías que…?»).
# Restricción de color: distinto de NisaLab (azul real + pera), NisaData (grafito + mandarina) y NisaResults (azul real + cian).
# Uso: python3 gen.py <carpeta de fuentes> → nisaresults.html
import os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..'); F = sys.argv[1]
def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)
COL = [('A', 'Ciruela + coral', '#4E1B4A', '#FF8B75', 'Cálido y creativo; se separa de los tres azules y del grafito de la familia.'),
       ('B', 'Magenta + amarillo', '#8A1858', '#FFC93C', 'El más vivo: dice «redes y contenido» de inmediato. Es el que más contrasta con el resto.'),
       ('C', 'Violeta + rosa', '#3B2A8C', '#FF8AC2', 'Creativo pero sobrio; queda cerca del azul de NisaLab, así que se distingue menos.')]
def s1(b, a):  # encuadre: dos esquinas de recorte y células dentro; la grande en acento
    return (f'<svg viewBox="0 0 100 100"><path d="M10 34 V16 a6 6 0 0 1 6 -6 H34" fill="none" stroke="{b}" stroke-width="8" stroke-linecap="round"/>'
            f'<path d="M90 66 V84 a6 6 0 0 1 -6 6 H66" fill="none" stroke="{b}" stroke-width="8" stroke-linecap="round"/>'
            f'<circle cx="44" cy="56" r="15" fill="{b}"/><circle cx="66" cy="38" r="11" fill="{a}"/><circle cx="64" cy="64" r="6" fill="{b}"/></svg>')
def s2(b, a):  # cuadrícula de publicaciones: 2 × 2 células, una en acento (el feed)
    c = ''
    for i, (x, y) in enumerate(((30, 30), (70, 30), (30, 70), (70, 70))):
        c += f'<rect x="{x - 17}" y="{y - 17}" width="34" height="34" rx="11" fill="{a if i == 1 else b}"/>'
    return f'<svg viewBox="0 0 100 100">{c}</svg>'
def s3(b, a):  # carrusel: tres láminas redondeadas, la del centro al frente y en acento
    return (f'<svg viewBox="0 0 100 100"><rect x="8" y="30" width="30" height="40" rx="9" fill="{b}" opacity=".55"/><rect x="62" y="30" width="30" height="40" rx="9" fill="{b}" opacity=".55"/>'
            f'<rect x="28" y="18" width="44" height="58" rx="12" fill="{b}"/><circle cx="50" cy="40" r="9" fill="{a}"/><rect x="38" y="56" width="24" height="6" rx="3" fill="{a}"/>'
            f'<circle cx="42" cy="88" r="3.5" fill="{b}"/><circle cx="50" cy="88" r="3.5" fill="{a}"/><circle cx="58" cy="88" r="3.5" fill="{b}"/></svg>')
SIM = [('1', 'Encuadre', s1, 'Esquinas de recorte con células dentro: componer una pieza. Habla de diseño sin ser un pincel o una paleta genéricos.'),
       ('2', 'Cuadrícula de publicaciones', s2, 'Cuatro piezas en cuadrícula, como el perfil de Instagram. Se entiende al instante; se parece a íconos de «apps».'),
       ('3', 'Carrusel', s3, 'Láminas en fila con sus puntos de paso: el carrusel de «¿Sabías que…?». Muy propio, pero más detallado y menos legible a 16 px.')]
def lock(sv, base): return f'<div class="lk"><div class="sm">{sv}</div><div><div class="wm" style="color:{base}"><b>Nisa</b>Studio</div><div class="rs">de <b style="color:{base}">Nisa Nabani</b></div></div></div>'
_li = lambda n: re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(NS, n)).read().strip())
FAM = f'<div class="app lab">{_li("nisalab-final/svg/app-icon.svg")}</div><div class="app lab">{_li("nisadata-final/svg/app-icon.svg")}</div><div class="app lab">{_li("nisaresults-final/svg/app-icon.svg")}</div>'
colh = ''.join(f'<div class="c"><h3>{k} · {n}</h3><div class="sws"><span><i style="background:{b}"></i>{b}</span><span><i style="background:{a}"></i>{a}</span></div>{lock(s1(b, a), b)}'
               f'<div class="apps">{FAM}<div class="app" style="background:{b}">{s1("#FFFFFF", a)}</div><span class="mut">NisaLab · NisaData · NisaResults · NisaStudio</span></div><p>{i}</p>'
               f'<p class="m">Blanco sobre base {cr("#FFFFFF", b)}:1 · acento sobre base {cr(a, b)}:1</p></div>' for k, n, b, a, i in COL)
G1, G2 = '#1F2532', '#8A93A8'
def tams(fn): return ''.join(f'<div style="width:{px}px;height:{px}px">{fn(G1, G2)}</div>' for px in (48, 24, 16))
simh = ''.join(f'<div class="c"><h3>{k} · {n}</h3><div class="big">{fn(G1, G2)}</div><div class="tam">{tams(fn)}</div><p>{i}</p></div>' for k, n, fn, i in SIM)
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700))
css = ff + '''
*{box-sizing:border-box}body{margin:0;background:#F2F4F8;color:#141B33;font:400 14px/1.5 Poppins,sans-serif;padding:32px}
h1{font:700 26px/1.2 Poppins;margin:0 0 4px}.lead{color:#535B70;max-width:900px;margin:0 0 24px}h2{font:600 19px/1.3 Poppins;margin:28px 0 4px}.sub{color:#535B70;margin:0 0 14px}
.g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.c{background:#fff;border:1px solid #DFE3EC;border-radius:14px;padding:20px;display:flex;flex-direction:column;gap:12px;min-width:0}
.c h3{font:600 15px/1.3 Poppins;margin:0}.c p{margin:0;color:#535B70;font-size:13px}.m{font-size:12px!important}
.sws{display:flex;gap:14px;font-size:12px;color:#535B70}.sws span{display:inline-flex;gap:6px;align-items:center}.sws i{width:18px;height:18px;border-radius:5px;display:inline-block}
.lk{display:flex;align-items:center;gap:10px;padding:10px 0;border-top:1px solid #EEF1F6;border-bottom:1px solid #EEF1F6}.sm{width:44px;height:44px;flex:none}svg{width:100%;height:100%;display:block}
.wm{font:400 28px/1 Poppins;letter-spacing:-.01em}.wm b{font-weight:700}.rs{font:500 11px/1 Poppins;color:#535B70;margin-top:3px}
.apps{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.app{width:48px;height:48px;border-radius:12px;padding:9px;overflow:hidden}.app.lab{padding:0}.mut{font-size:12px;color:#535B70}
.big{width:120px;height:120px}.tam{display:flex;gap:14px;align-items:flex-end}
@media (max-width:1000px){.g{grid-template-columns:1fr}}@media (max-width:480px){body{padding:16px}}
'''
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaStudio ronda 1</title><style>{css}</style><body>'
        '<h1>NisaStudio · ronda 1</h1><p class="lead">App interna para crear piezas de redes con plantillas de la marca: efemérides, avisos, promociones y carruseles. Dos decisiones separadas: color (con el símbolo 1 solo como referencia) y símbolo (en gris, para juzgar la forma). El color se distingue de los otros tres productos.</p>'
        f'<h2>Color de NisaStudio</h2><p class="sub">Junto a NisaLab, NisaData y NisaResults, como se verían en el lanzador.</p><div class="g">{colh}</div>'
        f'<h2>Símbolo</h2><p class="sub">Formas redondeadas como el resto de la familia. A 48, 24 y 16 px.</p><div class="g">{simh}</div></body></html>')
open(os.path.join(H, 'nisastudio.html'), 'w').write(html)
for k, n, b, a, _ in COL: print(k, n, cr('#FFFFFF', b), cr(a, b))
