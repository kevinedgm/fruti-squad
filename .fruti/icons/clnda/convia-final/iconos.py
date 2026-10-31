# Convia · íconos de categoría con trazo de plumón suave (familia de la estrella E1b). Uso: python3 iconos.py
# Cada ícono se dibuja como trazos de pincel con borde ligeramente irregular (determinista), en una caja de 200.
import os, json, math, random
D = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(D, 'tema.json'))); CAT = T['categorias']; C = T['color']
def wob(seed, amp, harm=(2, 3, 5)):
    r = random.Random(seed); ph = [(h, r.uniform(0, 6.28), r.uniform(.4, 1) / h ** .6) for h in harm]
    return lambda t: amp * sum(a * math.sin(h * t + p) for h, p, a in ph)
def smooth(pts, closed=True):
    n = len(pts); d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for i in (range(n) if closed else range(n - 1)):
        p0 = pts[(i - 1) % n] if closed or i > 0 else pts[i]; p1 = pts[i]; p2 = pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if closed or i + 2 < n else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6); c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}'
    return d + (' Z' if closed else '')
def resample(pts, n=60):
    L = [0]
    for a, b in zip(pts, pts[1:]): L.append(L[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
    out = []
    for i in range(n):
        t = L[-1] * i / (n - 1); j = max(k for k in range(len(L)) if L[k] <= t) if t < L[-1] else len(L) - 2
        j = min(j, len(pts) - 2); seg = (L[j + 1] - L[j]) or 1; u = (t - L[j]) / seg
        out.append((pts[j][0] + (pts[j + 1][0] - pts[j][0]) * u, pts[j][1] + (pts[j + 1][1] - pts[j][1]) * u))
    return out
def stroke(pts, w=15, seed=1, closed=False):
    # contorno de un trazo de plumón con extremos redondeados
    if closed: pts = pts + pts[:2]
    c = resample(pts, max(24, int(sum(math.hypot(b[0]-a[0], b[1]-a[1]) for a, b in zip(pts, pts[1:])) / 4)))
    wv = wob(seed, .12); L, R = [], []
    for i, (x, y) in enumerate(c):
        a = c[max(i - 1, 0)]; b = c[min(i + 1, len(c) - 1)]; dx, dy = b[0] - a[0], b[1] - a[1]; m = math.hypot(dx, dy) or 1
        nx, ny = -dy / m, dx / m; hw = w / 2 * (1 + wv(i / len(c) * 6.28))
        L.append((x + nx * hw, y + ny * hw)); R.append((x - nx * hw, y - ny * hw))
    x0, y0 = c[0]; x1, y1 = c[-1]
    def cap(p, q, cx, cy):  # media vuelta redondeada entre dos lados
        a0 = math.atan2(p[1] - cy, p[0] - cx); r = math.hypot(p[0] - cx, p[1] - cy)
        return [(cx + r * math.cos(a0 + math.pi * k / 6), cy + r * math.sin(a0 + math.pi * k / 6)) for k in range(1, 6)]
    poly = L + cap(L[-1], R[-1], x1, y1) + R[::-1] + cap(R[0], L[0], x0, y0)
    return f'<path d="{smooth(poly)}"/>'
def arcpts(cx, cy, r, a0, a1, n=24, sy=1):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)), cy + sy * r * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]
def jit(pts, seed, amp=1.6):
    r = random.Random(seed); return [(x + r.uniform(-amp, amp), y + r.uniform(-amp, amp)) for x, y in pts]
def rr(x0, y0, x1, y1, k=14):
    # rectángulo con esquinas suaves: puntos extra junto a cada esquina para que no se vuelva mancha
    return [(x0 + k, y0), (x1 - k, y0), (x1 - k * .3, y0 + k * .3), (x1, y0 + k), (x1, y1 - k), (x1 - k * .3, y1 - k * .3), (x1 - k, y1),
            (x0 + k, y1), (x0 + k * .3, y1 - k * .3), (x0, y1 - k), (x0, y0 + k), (x0 + k * .3, y0 + k * .3)]
def ln(pts, seed, closed=False, w=14):
    return f'<path d="{smooth(jit(pts, seed), closed)}" stroke-width="{w}"/>'
def circ(cx, cy, r, seed, n=18, sy=1):
    return [(cx + r * math.cos(2 * math.pi * k / n), cy + sy * r * math.sin(2 * math.pi * k / n)) for k in range(n)]
I = {
 'cafes': ln([(48, 84), (152, 84), (148, 132), (128, 164), (72, 164), (52, 132)], 1, True)
          + ln([(150, 100), (172, 104), (174, 126), (148, 136)], 2) + ln([(80, 62), (74, 48), (82, 34)], 3, w=11) + ln([(112, 62), (106, 48), (114, 34)], 4, w=11),
 'restaurantes': ln(circ(104, 104, 46, 5), 5, True) + ln([(30, 38), (30, 168)], 6, w=12) + ln([(18, 38), (19, 70), (30, 78), (41, 70), (42, 38)], 7, w=10)
          + ln([(178, 168), (178, 38), (166, 64), (166, 104), (178, 106)], 8, w=12),
 'hoteles': ln([(28, 52), (28, 166)], 9) + ln([(28, 130), (176, 130), (176, 166)], 10) + ln([(54, 106), (164, 106), (176, 118)], 11, w=12)
          + ln(circ(68, 90, 15, 12, 14, .55), 12, True, w=11),
 'talleres': ln([(78, 34), (122, 34)], 13, w=12) + ln([(86, 36), (84, 60), (58, 86), (52, 122), (66, 156), (100, 168), (134, 156), (148, 122), (142, 86), (116, 60), (114, 36)], 14)
          + ln([(58, 82), (36, 78), (34, 104), (54, 108)], 15, w=11) + ln([(142, 82), (164, 78), (166, 104), (146, 108)], 16, w=11),
 'museos': ln(rr(30, 36, 170, 164, 12), 16, True) + ln([(56, 138), (88, 94), (110, 122), (126, 106), (146, 138)], 17, w=12)
          + ln(circ(130, 70, 10, 18, 10), 18, True, w=9),
 'recorridos': ln([(40, 166), (70, 150), (116, 148), (134, 122), (100, 98), (110, 70), (148, 60)], 19, w=13)
          + ln([(150, 72), (150, 24)], 20, w=11) + ln([(152, 26), (184, 36), (152, 48)], 21, True, w=10) + '<circle cx="40" cy="166" r="11" stroke="none" fill="currentFill"/>',
}
def svg(k, col, bg=None, size=None):
    wh = f' width="{size}" height="{size}"' if size else ''
    g = f'<g fill="none" stroke="{col}" stroke-linecap="round" stroke-linejoin="round">' + I[k].replace('currentFill', col) + '</g>'
    if bg: g = f'<circle cx="100" cy="100" r="100" fill="{bg}"/><g transform="translate(30 30) scale(.7)">{g}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"{wh} role="img" aria-label="{CAT[k]["nombre"]}">{g}</svg>'
if __name__ == '__main__':
    for k, c in CAT.items():
        open(os.path.join(D, 'iconos', f'{k}.svg'), 'w').write(svg(k, 'currentColor'))
        open(os.path.join(D, 'iconos', f'{k}-color.svg'), 'w').write(svg(k, c['texto'], c['fondo']))
    rows = ''.join(f'''<div class="c"><div class="r">{svg(k, C['tinta'], size=72)}{svg(k, c['texto'], c['fondo'], 72)}{svg(k, C['tinta'], size=24)}{svg(k, C['tinta'], size=16)}</div><b style="color:{c['texto']}">{c['nombre']}</b></div>''' for k, c in CAT.items())
    open(os.path.join(D, 'iconos', 'vista.html'), 'w').write(f'<!doctype html><meta charset="utf-8"><style>body{{margin:0;padding:28px;background:{C["papel"]};font:600 15px sans-serif}}main{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}.c{{background:#fff;border:1px solid {C["linea"]};border-radius:16px;padding:18px;display:grid;gap:10px}}.r{{display:flex;gap:16px;align-items:center}}</style><main>{rows}</main>')
    print('ok')
