# Convia · símbolos ronda 4 · convite / hecho a mano (no literal). Uso: python3 gen.py <carpeta de fuentes>
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
# S1 · Estrella en vara: la estrella del convite sobre su vara marca dónde es la fiesta (y se lee como marcador de lugar).
P['S1'] = ('Estrella en vara', 'La estrella que se carga en el convite, en su vara: marca dónde es la fiesta, como un marcador de lugar.',
           f'<path d="{smooth(star(100, 72, 64, 30, 8, 2))}" fill="{{c}}"/>'
           f'<path d="{brush(curve(lambda t: (100 + 3 * math.sin(t * 5), 118 + 72 * t), 20), lambda t: 11 - 3 * t, 4, .15)}" fill="{{c}}"/>')
# S2 · Estrella de pétalos: ocho pétalos irregulares alrededor de un centro, como las estrellas de flores.
P['S2'] = ('Estrella de flores', 'Ocho pétalos alrededor de un centro, como las estrellas de flores del convite: muchos lugares, un mismo punto.',
           ''.join(f'<path d="{blob(100 + 56 * math.cos(math.radians(i * 45 - 90)), 100 + 56 * math.sin(math.radians(i * 45 - 90)), 22, 40 + i, .14, sx=.72, sy=1.15)}" fill="{{c}}" transform="rotate({i * 45} {100 + 56 * math.cos(math.radians(i * 45 - 90)):.1f} {100 + 56 * math.sin(math.radians(i * 45 - 90)):.1f})"/>' for i in range(8))
           + f'<path d="{blob(100, 100, 20, 9, .12)}" fill="{{c}}"/>')
# S3 · Estrella con rayos: estrella gruesa y rayos delgados que terminan en esferas.
rays = ''.join(f'<path d="{brush(curve(lambda t, a=a: (100 + (58 + 30 * t) * math.cos(a), 100 + (58 + 30 * t) * math.sin(a)), 12), lambda t: 5.5, 70 + j, .1)}" fill="{{c}}"/><path d="{blob(100 + 92 * math.cos(a), 100 + 92 * math.sin(a), 8, 80 + j, .15)}" fill="{{c}}"/>'
               for j, a in enumerate([math.radians(d) for d in (-45, 45, 135, 225)]))
P['S3'] = ('Estrella con rayos', 'Una estrella gruesa y rayos que terminan en esferas: la fiesta que se extiende hacia cada lugar.',
           f'<path d="{smooth(star(100, 100, 66, 30, 6, 5, rot=-90))}" fill="{{c}}"/>' + rays)
# S4 · Estrella abierta: una estrella de un trazo, con un rayo que no cierra (la invitación queda abierta).
op = star(100, 102, 80, 38, 7, 7)
P['S4'] = ('Estrella abierta', 'Una estrella dibujada de un solo trazo que no se cierra: la invitación queda abierta.',
           f'<path d="{brush([(op[i % len(op)][0], op[i % len(op)][1]) for i in range(1, len(op))], lambda t: 12 + 5 * math.sin(math.pi * t), 12, .12)}" fill="{{c}}"/>'
           f'<path d="{blob(100, 102, 12, 13, .14)}" fill="{{c}}"/>')
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
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Convia · símbolos r4</title><style>
@font-face{{font-family:IS;src:url("file://{font}")}}
body{{margin:0;padding:32px;background:#f4f4f1;color:{INK};font:15px/1.45 IS,system-ui,sans-serif}}
h1{{margin:0 0 4px;font-size:26px}}.lead{{margin:0 0 24px;color:#55555a}}
main{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}
article{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;gap:14px;align-content:start}}
.big svg{{width:100%;max-width:170px;display:block;margin:8px auto}}
.row{{display:flex;gap:14px;align-items:center}}.dk{{background:#1b1b1d;border-radius:10px;padding:6px;display:inline-flex}}
.lk{{display:flex;align-items:center;gap:10px;border-top:1px solid #ececE8;padding-top:14px}}.lk b{{font:600 30px IS;letter-spacing:-.01em}}
h2{{margin:0;font-size:16px}}p{{margin:0;color:#55555a}}
</style></head><body><h1>Convia · símbolos, ronda 4 · convite</h1><p class="lead">Inspiración: las estrellas del convite (de carrizo, papel y flores). Abstraídas, con borde hecho a mano. Forma en tinta y una muestra de color festivo provisional. Tamaños: grande, 24 px, 16 px y sobre oscuro.</p><main>{cards}</main></body></html>'''
open('lamina.html', 'w').write(html)
