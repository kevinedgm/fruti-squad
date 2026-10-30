# Convia · símbolos ronda 3 · orgánico / hecho a mano (no literal). Uso: python3 gen.py <carpeta de fuentes>
# Formas con borde irregular determinista (suma de senos con fase fija): parecen trazadas a mano y se regeneran igual.
import sys, os, math, random
F = sys.argv[1] if len(sys.argv) > 1 else '.'
INK = '#1b1b1d'

def wob(seed, amp, harm=(2, 3, 5, 7)):
    r = random.Random(seed); ph = [(h, r.uniform(0, 6.28), r.uniform(.4, 1) / h ** .6) for h in harm]
    return lambda t: amp * sum(a * math.sin(h * t + p) for h, p, a in ph)

def smooth(pts, closed=True):
    # Catmull-Rom → Bézier cúbica
    n = len(pts); d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p0 = pts[(i - 1) % n] if closed or i > 0 else pts[i]; p1 = pts[i]; p2 = pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if closed or i + 2 < n else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}'
    return d + (' Z' if closed else '')

def blob(cx, cy, r, seed, amp=.07, n=48, sx=1, sy=1):
    w = wob(seed, r * amp)
    return smooth([(cx + (r + w(t)) * sx * math.cos(t), cy + (r + w(t)) * sy * math.sin(t)) for t in [i * 2 * math.pi / n for i in range(n)]])

def brush(center, width, seed, amp=.18):
    # trazo de pincel: contorno a ambos lados de una línea central con grosor variable
    w = wob(seed, 1)
    L, R = [], []
    for i, (x, y) in enumerate(center):
        a = center[max(i - 1, 0)]; b = center[min(i + 1, len(center) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]; m = math.hypot(dx, dy) or 1
        nx, ny = -dy / m, dx / m; t = i / (len(center) - 1)
        hw = width(t) * (1 + amp * w(t * 6.28)) / 2
        L.append((x + nx * hw, y + ny * hw)); R.append((x - nx * hw, y - ny * hw))
    return smooth(L + R[::-1])

def curve(f, n=60):
    return [f(i / (n - 1)) for i in range(n)]

P = {}
# H1 · Piedra con paso: una piedra de cantera con un hueco que se abre como paso. Portal sin dibujar un arco.
hole = smooth([(100 + 25 * math.cos(t), 112 - 30 * math.sin(t)) for t in [math.pi + i * math.pi / 16 for i in range(17)]] + [(127, 150), (126, 168), (74, 168), (73, 150)])
P['H1'] = ('Piedra con paso', 'Una piedra de cantera, irregular como la tallada a mano, con un paso abierto: entrar sin dibujar una puerta.',
           f'<path d="{blob(100, 100, 82, 11, .06)} {hole}" fill-rule="evenodd" fill="{{c}}"/>')
# H2 · Trazo de convite: un solo gesto de pincel que hace una vuelta y sigue.
c2 = curve(lambda t: (30 + 140 * t + 34 * math.sin(2 * math.pi * t), 128 - 46 * t + 34 * math.cos(2 * math.pi * t) - 34), 120)
P['H2'] = ('Trazo de convite', 'Un solo gesto de pincel que da una vuelta y sigue: alguien que te invita y te lleva.',
           f'<path d="{brush(c2, lambda t: 9 + 20 * math.sin(math.pi * t ** .9), 21, .1)}" fill="{{c}}"/>')
# H3 · Reunión: formas que se juntan hacia una mayor.
P['H3'] = ('Dos piedras', 'Dos piedras que se apoyan una en otra y dejan un paso entre ellas: un portal sin arco, hecho de encuentro.',
           f'<path d="{blob(70, 112, 52, 3, .08, sx=.78, sy=1.2)}" fill="{{c}}" transform="rotate(14 70 112)"/>'
           f'<path d="{blob(134, 108, 48, 5, .08, sx=.8, sy=1.25)}" fill="{{c}}" transform="rotate(-16 134 108)"/>')
# H4 · Sello: un sello de tinta que no cierra, con una marca adentro.
ring = blob(100, 100, 84, 8, .05) + ' ' + blob(100, 100, 60, 9, .06)
P['H4'] = ('Sello abierto', 'Un sello de tinta estampado a mano que deja una salida: lo recomendado, sin cerrar el círculo.',
           f'<mask id="m4"><rect width="200" height="200" fill="#fff"/><path d="M100 100 L200 70 L200 130 Z" fill="#000"/></mask>'
           f'<path d="{ring}" fill-rule="evenodd" fill="{{c}}" mask="url(#m4)"/><path d="{blob(100, 100, 18, 12, .14)}" fill="{{c}}"/>')
# H5 · Hoja con vía: una hoja verde (Verde Antequera) cruzada por un camino que la atraviesa como nervadura.
leaf = smooth([(100 + 70 * math.sin(t) * (1 + .05 * math.sin(4 * t + 1)), 100 - 86 * math.cos(t) + 3 * math.sin(6 * t)) for t in [i * 2 * math.pi / 48 for i in range(48)]])
vein = curve(lambda t: (100 + 22 * math.sin(t * 2 * math.pi * 1.2), 30 + 150 * t), 50)
P['H5'] = ('Hoja con vía', 'Una hoja, por lo verde de la ciudad, atravesada por un camino que serpentea: la vía hecha nervadura.',
           f'<g transform="rotate(28 100 100)"><mask id="m5"><rect width="200" height="200" fill="#fff"/><path d="{brush(vein, lambda t: 9 + 4 * math.sin(math.pi * t), 31, .25)}" fill="#000"/></mask>'
           f'<path d="{leaf}" fill="{{c}}" mask="url(#m5)"/></g>')

def svg(k, c=INK, size=None, suf=''):
    body = P[k][2].replace('{c}', c).replace('id="m', f'id="m{suf}').replace('url(#m', f'url(#m{suf}')
    wh = f' width="{size}" height="{size}"' if size else ''
    return f'<svg viewBox="0 0 200 200"{wh} role="img" aria-label="Convia, {P[k][0]}">{body}</svg>'
for k in ('H1', 'H3'):
    P.pop(k)
for k in P:
    open(f'{k}.svg', 'w').write(svg(k))
font = os.path.join(F, 'InstrumentSans[wdth,wght].ttf')
cards = ''.join(f'''<article><div class="big">{svg(k, suf=k+'a')}</div>
<div class="row"><span>{svg(k, size=24, suf=k+'b')}</span><span>{svg(k, size=16, suf=k+'c')}</span><span class="dk">{svg(k, '#ffffff', 40, suf=k+'d')}</span></div>
<div class="lk">{svg(k, size=44, suf=k+'e')}<b>Convia</b></div>
<h2>{k} · {P[k][0]}</h2><p>{P[k][1]}</p></article>''' for k in P)
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Convia · símbolos r3</title><style>
@font-face{{font-family:IS;src:url("file://{font}")}}
body{{margin:0;padding:32px;background:#f4f4f1;color:{INK};font:15px/1.45 IS,system-ui,sans-serif}}
h1{{margin:0 0 4px;font-size:26px}}.lead{{margin:0 0 24px;color:#55555a}}
main{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
article{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;gap:14px;align-content:start}}
.big svg{{width:100%;max-width:170px;display:block;margin:8px auto}}
.row{{display:flex;gap:14px;align-items:center}}.dk{{background:#1b1b1d;border-radius:10px;padding:6px;display:inline-flex}}
.lk{{display:flex;align-items:center;gap:10px;border-top:1px solid #ececE8;padding-top:14px}}.lk b{{font:600 30px IS;letter-spacing:-.01em}}
h2{{margin:0;font-size:16px}}p{{margin:0;color:#55555a}}
</style></head><body><h1>Convia · símbolos, ronda 3 · orgánico</h1><p class="lead">Formas con borde de trazo a mano, no literales. Solo forma, en tinta. Tamaños: grande, 24 px, 16 px y sobre oscuro.</p><main>{cards}</main></body></html>'''
open('lamina.html', 'w').write(html)
