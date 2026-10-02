import math
W = 0.75   # medio trazo
R = 'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'
f = lambda v: f'{v:.2f}'.rstrip('0').rstrip('.')
def svg(id_, nota, piezas):
    return f'<svg {R} class="uva-icon uva-{id_}">\n  <style>.uva-{id_}{{stroke-width:var(--uva-stroke,1.5)}}</style>\n  <!-- {nota} -->\n' + ''.join(f'  {p}\n' for p in piezas) + '</svg>\n'

# A6: separación entre BORDES de dos círculos / círculo-rect (aprox. por distancia de ejes)
def sep_cc(a, b): return math.dist(a[:2], b[:2]) - a[2] - b[2] - 2 * W
def margen_c(c): x, y, r = c; return min(x - r - W, y - r - W, 24 - (x + r + W), 24 - (y + r + W))
informe = []

# ---- A · tallo bézier: 3 uvas (2+1) y el tallo es un trazado que termina en un anclaje con su manejador
uA = [(7.5, 12.5, 2.25), (15, 12.5, 2.25), (11.25, 18.99, 2.25)]
id_ = 'vector-grape-a'
A = svg(id_, 'A · tallo bézier: el tallo del racimo es un trazado que termina en un anclaje con su manejador', [
    *[f'<circle class="uva-{id_}__uva" cx="{f(x)}" cy="{f(y)}" r="{f(r)}"/>' for x, y, r in uA],
    f'<path class="uva-{id_}__trazado" d="M11.25 9.25C11.25 6.75 12.5 5.5 14.75 5.5"/>',
    f'<rect class="uva-{id_}__anclaje" x="14.75" y="4" width="3" height="3" rx=".75"/>',
    f'<path class="uva-{id_}__manejador" d="M17.75 5.5h1.5"/>',
    f'<circle class="uva-{id_}__punta" cx="20.25" cy="5.5" r="1"/>'])
informe.append(('A', [('uva-uva', min(sep_cc(uA[i], uA[j]) for i in range(3) for j in range(i + 1, 3))),
                      ('anclaje(y≤7.75)-uva sup (borde 9.5)', 9.5 - 7.75), ('margen uvas', min(map(margen_c, uA))),
                      ('margen punta', 24 - (20.25 + 1 + W)), ('margen anclaje arriba', 4 - W)]))

# ---- B · silueta como trazado: contorno festoneado del racimo (3-2-1) con anclajes en las cúspides
r = 2.75
cs = [(7, 9), (12, 9), (17, 9), (9.5, 13.33), (14.75 - .25, 13.33), (12, 17.66)]
orden = [0, 1, 2, 4, 5, 3]   # recorrido exterior, en sentido horario
cx_, cy_ = sum(c[0] for c in cs) / 6, sum(c[1] for c in cs) / 6
def corte(a, b):   # intersección exterior de dos círculos de radio r
    (x1, y1), (x2, y2) = a, b; d = math.dist(a, b); h = math.sqrt(r * r - (d / 2) ** 2)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2; ux, uy = (y2 - y1) / d, -(x2 - x1) / d
    p, q = (mx + ux * h, my + uy * h), (mx - ux * h, my - uy * h)
    return max(p, q, key=lambda t: math.dist(t, (cx_, cy_)))
pts = [corte(cs[orden[i - 1]], cs[orden[i]]) for i in range(6)]   # pts[i] = entre orden[i-1] y orden[i]
d = f'M{f(pts[0][0])} {f(pts[0][1])}'
for i in range(6):
    c = cs[orden[i]]; a0 = math.atan2(pts[i][1] - c[1], pts[i][0] - c[0]); p1 = pts[(i + 1) % 6]
    a1 = math.atan2(p1[1] - c[1], p1[0] - c[0]); barrido = (a1 - a0) % (2 * math.pi)
    d += f'A{f(r)} {f(r)} 0 {1 if barrido > math.pi else 0} 1 {f(p1[0])} {f(p1[1])}'
d += 'Z'
id_ = 'vector-grape-b'
sel = [pts[1], pts[2]]   # cúspides superiores: anclajes seleccionados
B = svg(id_, 'B · silueta como trazado: el contorno festoneado del racimo es un trazado vectorial con sus anclajes', [
    f'<path class="uva-{id_}__contorno" d="{d}"/>',
    f'<path class="uva-{id_}__tallo" d="M12 6.25V3.5"/>',
    *[f'<rect class="uva-{id_}__anclaje" x="{f(x - 1.25)}" y="{f(y - 1.25)}" width="2.5" height="2.5" rx=".5" fill="currentColor"/>' for x, y in sel]])
ys = [c[1] for c in cs]; xs = [c[0] for c in cs]
informe.append(('B', [('margen izq', min(xs) - r - W), ('margen der', 24 - (max(xs) + r + W)), ('margen abajo', 24 - (max(ys) + r + W)),
                      ('tallo-contorno', 0), ('cúspides', [tuple(round(v, 2) for v in p) for p in pts])]))

# ---- C · uva seleccionada: la uva de abajo es un anclaje con su manejador bézier atravesándola
uC = [(7.5, 11.75, 2.25), (15, 11.75, 2.25)]
id_ = 'vector-grape-c'
C = svg(id_, 'C · uva seleccionada: la uva de abajo es un anclaje y la cruza su manejador bézier', [
    *[f'<circle class="uva-{id_}__uva" cx="{f(x)}" cy="{f(y)}" r="{f(r_)}"/>' for x, y, r_ in uC],
    f'<path class="uva-{id_}__tallo" d="M11.25 8.5V6.75c0-1.5 1.25-2.5 2.75-2.5"/>',
    f'<rect class="uva-{id_}__anclaje" x="9.25" y="17" width="4" height="4" rx="1"/>',
    f'<path class="uva-{id_}__manejador" d="M5.75 19h3.5M13.25 19h3.5"/>',
    f'<circle class="uva-{id_}__punta" cx="4.75" cy="19" r="1"/>',
    f'<circle class="uva-{id_}__punta" cx="17.75" cy="19" r="1"/>'])
informe.append(('C', [('uva-uva', sep_cc(uC[0], uC[1])), ('uva sup (borde 14.75)-anclaje (borde 16.25)', 16.25 - 14.75),
                      ('margen punta izq', 4.75 - 1 - W), ('margen anclaje abajo', 24 - (21 + W))]))
for v, s in zip('abc', [A, B, C]): open(f'vector-grape-{v}.svg', 'w').write(s)
for v, items in informe:
    print(v, '·', ' · '.join(f'{k} {round(x, 2) if isinstance(x, float) else x}' for k, x in items))
