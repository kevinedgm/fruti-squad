# Escudo de Oaxaca · r7 (2026-11-04). Crítica de r6: «torpe»; pedir homogeneidad de trazo, simetría y pulido.
# Reglas de construcción (verificadas por código en verificar.cjs):
#   1. Un solo grosor de trazo W en todo el emblema; sin rellenos. Los puntos son trazos de longitud cero (diámetro = W).
#   2. Retícula de 4 unidades en una caja de 240 × 300; eje vertical en x = 120.
#   3. Simetría bilateral exacta: las piezas se definen por mitades y se reflejan (espejo()).
#   4. Ningún hueco entre trazos es menor que W (distancia entre ejes de trazos paralelos ≥ 2W).
import math, re
W = 10; CX = 120
def grupo(body): return f'<g fill="none" stroke="currentColor" stroke-width="{W}" stroke-linecap="round" stroke-linejoin="round">{body}</g>'
def espejo(d): return f'<path d="{d}"/><path d="{d}" transform="matrix(-1 0 0 1 {2*CX} 0)"/>'
def punto(x, y): return f'M{x:.2f},{y:.2f}h0'
def poly(pts, closed=False): return 'M' + ' L'.join(f'{x:g},{y:g}' for x, y in pts) + ('Z' if closed else '')
def mitad_simetrica(half):  # half: lista de puntos de izquierda al eje; devuelve el perfil completo reflejado
    return half + [(2*CX - x, y) for x, y in reversed(half)]
# ---------- piezas ----------
def escudo_espanol(x0, top, base):  # lados rectos y base en semicírculo
    r = CX - x0; mid = base - r
    return f'M{x0},{top} H{2*CX - x0} V{mid} A{r},{r} 0 0 1 {x0},{mid} Z'
def escudo_punta(x0, top, base, ch=16):  # esquinas superiores achaflanadas y base en punta de dos arcos
    x1 = 2*CX - x0; r = (base - top) * 1.05
    return f'M{x0 + ch},{top} H{x1 - ch} L{x1},{top + ch} V{top + (base - top)*.42:g} Q{x1},{base - 44} {CX},{base} Q{x0},{base - 44} {x0},{top + (base - top)*.42:g} V{top + ch} Z'
def mitla(by, steps=3, run=16, rise=16, top_half=16):  # plataforma escalonada (contorno), simétrica; escalón = 2W
    half_w = top_half + steps*run; pts = [(CX - half_w, by)]; x, y = CX - half_w, by
    for i in range(steps):
        y -= rise; pts.append((x, y)); x += run; pts.append((x, y))
    return poly(mitad_simetrica(pts[:-1]), True)
def cadena(cy, lw=36, lh=24, ov=12, gap=16):  # cadena rota: dos eslabones entrelazados a cada lado; hueco interior = W
    o = ''
    for k in range(2):
        x = CX - gap/2 - lw - k*(lw - ov); r = lh/2
        o += espejo(f'M{x + r},{cy - r} H{x + lw - r} A{r},{r} 0 0 1 {x + lw - r},{cy + r} H{x + r} A{r},{r} 0 0 1 {x + r},{cy - r} Z')
    return o
def aguila(top):
    # Águila explayada: cuerpo en lente, cuatro plumas rectas por ala (separadas para dejar hueco ≥ W), cola en abanico.
    # Única excepción a la simetría: la cabeza mira a la izquierda, como en el escudo nacional y en el actual.
    t = math.tan(math.radians(28)); o = ''
    hx, hy = CX, top + 16
    o += f'<path d="M{hx + 6},{hy + 13} A14,14 0 1 0 {hx - 12},{hy + 6} M{hx - 13},{hy - 2} L{hx - 26},{hy + 4} L{hx - 14},{hy + 12}"/>'
    o += f'<path d="M{CX},{top + 34} Q{CX + 16},{top + 64} {CX},{top + 96} Q{CX - 16},{top + 64} {CX},{top + 34}Z"/>'
    for k, L in enumerate((84, 70, 56, 42)):
        y = top + 48 + k*24; o += espejo(f'M{CX - 22},{y} L{CX - 22 - L},{y - L*t:.1f}')
    o += f'<path d="M{CX},{top + 104} V{top + 110}"/>' + espejo(f'M{CX - 10},{top + 102} L{CX - 18},{top + 112}')
    return o
def huaje(cy):  # rama en arco y tres vainas (lentes) que cuelgan debajo de ella, simétrica
    o = f'<path d="M{CX - 56},{cy - 36} Q{CX},{cy - 68} {CX + 56},{cy - 36}"/>'
    pod = lambda x, top, h, w: f'M{x},{top} Q{x + w},{top + h/2} {x},{top + h} Q{x - w},{top + h/2} {x},{top}Z'
    o += f'<path d="{pod(CX, cy - 36, 84, 24)}"/>' + espejo(pod(CX - 40, cy - 30, 66, 20))
    return o
def octagrama(cx, cy, r):  # estrella de ocho puntas: dos cuadrados girados 45°
    sq = lambda a: poly([(cx + r*math.cos(math.radians(a + 90*k)), cy + r*math.sin(math.radians(a + 90*k))) for k in range(4)], True)
    return f'<path d="{sq(45)}"/><path d="{sq(0)}"/>'
# ---------- emblemas ----------
def a():  # Escudo con cimera: águila, Mitla, cadena rota y ocho puntos (las regiones) en la base
    o = aguila(-26)
    o += f'<path d="{escudo_espanol(32, 112, 300)}"/><path d="M32,192 H208"/>'
    o += f'<path d="{mitla(176)}"/>'
    o += cadena(226)
    for k in range(8):
        t = math.radians(36 + k * (108 / 7)); o += f'<path d="{punto(CX + 60*math.cos(t), 214 + 58*math.sin(t))}"/>'
    return grupo(o)
def b():  # Óvalo: el óvalo del lema como doble anillo con ocho puntos; al centro el huaje sobre Mitla
    o = f'<ellipse cx="{CX}" cy="150" rx="104" ry="136"/><ellipse cx="{CX}" cy="150" rx="80" ry="112"/>'
    for k in range(8):
        t = math.radians(-90 + 22.5 + 45*k); o += f'<path d="{punto(CX + 92*math.cos(t), 150 + 124*math.sin(t))}"/>'
    o += huaje(124) + f'<path d="{mitla(222, 2, 14, 16, 12)}"/>'
    return grupo(o)
def escudo_punta2(x0, top, base, ch=16):
    x1 = 2*CX - x0; mid = top + 128
    return f'M{x0 + ch},{top} H{x1 - ch} L{x1},{top + ch} V{mid} C{x1},{base - 64} {CX + 56},{base - 20} {CX},{base} C{CX - 56},{base - 20} {x0},{base - 64} {x0},{mid} V{top + ch} Z'
def c():  # Escudo en punta: estrella de ocho puntas (las regiones) con su centro; cadena rota abajo
    o = f'<path d="{escudo_punta2(28, 8, 296)}"/>'
    o += octagrama(CX, 108, 68) + f'<circle cx="{CX}" cy="108" r="24"/><path d="{punto(CX, 108)}"/>'
    o += cadena(216)
    return grupo(o)
E = {'a': a, 'b': b, 'c': c}
VB = '-6 -30 252 340'
