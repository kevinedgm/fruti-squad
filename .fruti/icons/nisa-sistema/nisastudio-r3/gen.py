# NisaStudio · ronda 3 de color: colores de marketing y redes. Lo que se lee como «social media» es saturación alta, brillo y degradado,
# más que un tono en particular; por eso cada opción es un degradado de dos colores vivos + un acento claro.
# Uso: python3 gen.py <carpeta de fuentes> → color.html
import importlib.util, os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..'); F = sys.argv[1]
_a = sys.argv; sys.argv = [_a[0], F]
spec = importlib.util.spec_from_file_location('r1', os.path.join(NS, 'nisastudio-r1', 'gen.py')); R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
sys.argv = _a
cr = R.cr
COL = [('A', 'Fucsia → coral', '#D81B60', '#FF7043', '#B0144E', '#FFE066', 'Energía de campaña: el par más reconocible de redes, cálido y llamativo.'),
       ('B', 'Violeta → rosa', '#6D28D9', '#EC4899', '#5B21B6', '#FDE68A', 'Creativo y actual; muy usado en herramientas de contenido. Algo menos cálido que A.'),
       ('C', 'Índigo → turquesa', '#4F46E5', '#14B8A6', '#3730A3', '#FDE68A', 'Campañas digitales con tono tecnológico; el más sobrio de los tres.')]
_li = lambda n: re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(NS, n)).read().strip())
FAM = ''.join(f'<div class="app lab">{_li(n)}</div>' for n in ('nisalab-final/svg/app-icon.svg', 'nisadata-final/svg/app-icon.svg', 'nisaresults-final/svg/app-icon.svg'))
def lock(sv, w): return f'<div class="lk"><div class="sm">{sv}</div><div><div class="wm" style="color:{w}"><b>Nisa</b>Studio</div><div class="rs">de <b style="color:{w}">Nisa Nabani</b></div></div></div>'
cards = ''
for k, n, c1, c2, w, ac, i in COL:
    g = f'linear-gradient(135deg,{c1},{c2})'
    cards += (f'<div class="c"><h3>{k} · {n}</h3><div class="sws"><span><i style="background:{c1}"></i>{c1}</span><span><i style="background:{c2}"></i>{c2}</span><span><i style="background:{ac}"></i>{ac}</span></div>'
              f'{lock(R.s1(w, c2), w)}<div class="apps">{FAM}<div class="app" style="background:{g}">{R.s1("#FFFFFF", ac)}</div><span class="mut">NisaLab · NisaData · NisaResults · NisaStudio</span></div>'
              f'<div class="post" style="background:{g}"><span class="pk">¿Sabías que…?</span><b>El sarro en tu agua no es suciedad: es calcio y magnesio.</b><span class="pp">1 / 5</span></div>'
              f'<p>{i}</p><p class="m">Blanco sobre {c1}: {cr("#FFFFFF", c1)}:1 · sobre {c2}: {cr("#FFFFFF", c2)}:1</p></div>')
css = R.css + '''
.post{border-radius:14px;padding:18px;color:#fff;display:grid;gap:8px;aspect-ratio:4/5;max-width:220px;align-content:end;position:relative}.post b{font:700 19px/1.25 Poppins}.pk{font:600 12px Poppins;letter-spacing:.06em;text-transform:uppercase;opacity:.9}
.pp{position:absolute;top:14px;right:14px;font:500 12px Poppins;background:rgba(255,255,255,.22);border-radius:999px;padding:2px 8px}
.sws{flex-wrap:wrap}'''
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaStudio ronda 3</title><style>{css}</style><body>'
        '<h1>NisaStudio · ronda 3: colores de marketing y redes</h1><p class="lead">Lo que hace que un color «se sienta» de redes sociales es la saturación alta, el brillo y el degradado, más que un tono concreto. Cada opción es un degradado propio (no copia el de ninguna red social), con un acento claro. Se ve en el logotipo, en el lanzador junto a los otros productos y en una pieza de ejemplo.</p>'
        f'<div class="g">{cards}</div></body></html>')
open(os.path.join(H, 'color.html'), 'w').write(html)
for k, n, c1, c2, w, ac, _ in COL: print(k, n, cr('#FFFFFF', c1), cr('#FFFFFF', c2), 'palabra', cr(w, '#FFFFFF'))
