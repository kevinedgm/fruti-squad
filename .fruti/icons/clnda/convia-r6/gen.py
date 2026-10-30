# Convia · símbolos ronda 6 · estrella a mano / hecho a mano (no literal). Uso: python3 gen.py <carpeta de fuentes>
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
def star(cx, cy, R, r, k, seed, rot=-90, jit=.08):
    rr = random.Random(seed); pts = []
    for i in range(2 * k):
        rad = (R if i % 2 == 0 else r) * (1 + rr.uniform(-jit, jit))
        t = math.radians(rot + i * 180 / k + rr.uniform(-3, 3))
        pts.append((cx + rad * math.cos(t), cy + rad * math.sin(t)))
    return pts
def poly(pts):
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ' Z'
def star2(cx, cy, Rs, r, seed, rot=-90, jit=.05):
    # Rs: lista de radios de las puntas (permite puntas largas y cortas)
    rr = random.Random(seed); k = len(Rs); pts = []
    for i in range(2 * k):
        rad = (Rs[i // 2] if i % 2 == 0 else r) * (1 + rr.uniform(-jit, jit))
        t = math.radians(rot + i * 180 / k + rr.uniform(-2.5, 2.5))
        pts.append((cx + rad * math.cos(t), cy + rad * math.sin(t)))
    return pts
def loop(pts, extra=2):
    # contorno cerrado de un trazo: vuelve sobre los primeros vértices para que el cierre se note hecho a mano
    return pts + pts[:extra]
def dash(x0, y0, x1, y1, seed, w=8):
    return f'<path d="{brush(curve(lambda t: (x0 + (x1 - x0) * t, y0 + (y1 - y0) * t), 8), lambda t: w * (1 - .4 * t), seed, .15)}" fill="{{c}}"/>'
# E1 · estrella de un trazo, cerrada, inclinada; el cierre se cruza como al dibujarla a mano
p = star2(100, 104, [74] * 6, 36, 3, rot=-80)
P['E1'] = ('Trazo cerrado', 'Una estrella dibujada de un solo trazo que se cierra cruzándose, como hecha con plumón; inclinada, en movimiento.',
           f'<path d="{brush(loop(p), lambda t: 15 + 4 * math.sin(math.pi * t * 3), 5, .12)}" fill="{{c}}"/>')
# E2 · doble trazo: la estrella dibujada dos veces, un poco desfasada, como boceto con energía
p1 = star2(98, 104, [70] * 6, 34, 11, rot=-86); p2 = star2(104, 100, [72] * 6, 35, 12, rot=-78)
P['E2'] = ('Doble trazo', 'La estrella dibujada dos veces, un poco desfasada: la energía de un boceto rápido, de fiesta.',
           f'<path d="{brush(loop(p1, 1), lambda t: 9, 13, .15)}" fill="{{c}}"/><path d="{brush(loop(p2, 1), lambda t: 7, 14, .2)}" fill="{{c}}"/>')
# E3 · estrella sólida de pincel + chispas cortas (trazos, no esferas)
P['E3'] = ('Pincel y chispas', 'Una estrella sólida de borde pincelado, con tres chispas cortas: la fiesta que empieza.',
           f'<path d="{smooth(star2(92, 110, [66, 60, 68, 58, 64, 62], 30, 21, rot=-84))}" fill="{{c}}"/>'
           + dash(150, 38, 166, 22, 31) + dash(166, 66, 188, 60, 32) + dash(130, 28, 132, 8, 33))
# E4 · estrella de carrizo: 8 puntas largas y cortas, de un trazo
p = star2(100, 100, [80, 50, 80, 50, 80, 50, 80, 50], 30, 41, rot=-90, jit=.04)
P['E4'] = ('Estrella de carrizo', 'Ocho puntas, largas y cortas, como las estrellas de carrizo del convite; de un trazo y con cierre a mano.',
           f'<path d="{brush(loop(p), lambda t: 12 + 3 * math.sin(math.pi * t * 4), 42, .12)}" fill="{{c}}"/>')
def svg(k, c=INK, size=None, suf=''):
    body = P[k][2].replace('{c}', c).replace('id="m', f'id="m{suf}').replace('url(#m', f'url(#m{suf}')
    wh = f' width="{size}" height="{size}"' if size else ''
    return f'<svg viewBox="0 0 200 200"{wh} role="img" aria-label="Convia, {P[k][0]}">{body}</svg>'
for k in P:
    open(f'{k}.svg', 'w').write(svg(k))
font = os.path.join(F, 'InstrumentSans[wdth,wght].ttf')
cards = ''.join(f'''<article><div class="big">{svg(k, suf=k+'a')}</div>
<div class="row"><span>{svg(k, size=24, suf=k+'b')}</span><span>{svg(k, size=16, suf=k+'c')}</span><span class="dk">{svg(k, '#ffffff', 40, suf=k+'d')}</span><span>{svg(k, '#d6246e', 40, suf=k+'f')}</span><span class="dk" style="background:#2a1a5e">{svg(k, '#ffb627', 40, suf=k+'g')}</span></div>
<div class="lk">{svg(k, size=44, suf=k+'e')}<b>Convia</b></div>
<h2>{k} · {P[k][0]}</h2><p>{P[k][1]}</p></article>''' for k in P)
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Convia · símbolos r6</title><style>
@font-face{{font-family:IS;src:url("file://{font}")}}
body{{margin:0;padding:32px;background:#f4f4f1;color:{INK};font:15px/1.45 IS,system-ui,sans-serif}}
h1{{margin:0 0 4px;font-size:26px}}.lead{{margin:0 0 24px;color:#55555a}}
main{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}
article{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;gap:14px;align-content:start}}
.big svg{{width:100%;max-width:170px;display:block;margin:8px auto}}
.row{{display:flex;gap:14px;align-items:center}}.dk{{background:#1b1b1d;border-radius:10px;padding:6px;display:inline-flex}}
.lk{{display:flex;align-items:center;gap:10px;border-top:1px solid #ececE8;padding-top:14px}}.lk b{{font:600 30px IS;letter-spacing:-.01em}}
h2{{margin:0;font-size:16px}}p{{margin:0;color:#55555a}}
</style></head><body><h1>Convia · símbolos, ronda 6 · estrella a mano</h1><p class="lead">Lo que gustó de S3 y S4: trazo a mano, energía de fiesta y forma clara de estrella. Sin rayos ni esferas. Forma en tinta y una muestra de color festivo provisional. Tamaños: grande, 24 px, 16 px y sobre oscuro.</p><main>{cards}</main></body></html>'''
open('lamina.html', 'w').write(html)
