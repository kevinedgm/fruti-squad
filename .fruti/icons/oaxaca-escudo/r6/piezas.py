# Escudo de Oaxaca · r6 · piezas en trazo grueso (monolínea, una tinta). Referencia: láminas del usuario (2026-11-03).
# Cada pieza dibuja en coordenadas propias; fg = tinta, CUT = recorte (color del fondo vía clase .cut/.cuts).
import math, re
S = 6  # trazo base en una caja de 200
L = '/root/.cache/fruti-uva/package/icons/'
def luc(n): return ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse)[^>]*/>', open(L + n + '.svg').read()))
def st(w=S): return f'fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'
FILL = 'fill="currentColor"'
def aguila(x, y, s=1):
    # Cabeza de águila de perfil (mira a la izquierda): pico ganchudo separado de la cabeza, ceja, ojo y plumas de la nuca.
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M62,62 C62,40 58,20 46,10 C38,4 26,3 17,7 L13,9 C6,11 1,18 0,26 C-1,33 2,38 7,38 C7,33 9,29 13,28 L17,29 C21,36 23,48 26,62 Z" {FILL}/>'
            f'<path d="M14,9 C11,15 12,22 17,28" class="cuts" fill="none" stroke-width="2.6" stroke-linecap="round"/>'
            f'<path d="M18,11 C23,9 29,9 34,12" class="cuts" fill="none" stroke-width="3" stroke-linecap="round"/>'
            f'<circle cx="26" cy="17" r="3.4" class="cut"/>'
            f'<path d="M35,62 L41,50 M45,62 L51,48 M55,62 L59,47" class="cuts" fill="none" stroke-width="3.2" stroke-linecap="round"/></g>')
def mitla(cx, by, w=56, n=3, puerta=True):
    # Plataforma escalonada de Mitla: n niveles sólidos y una puerta recortada.
    o, h = [], 10
    for i in range(n):
        ww = w - i * w / (n + .6); o.append(f'<rect x="{cx - ww/2:.1f}" y="{by - (i+1)*h - i*2:.1f}" width="{ww:.1f}" height="{h}" rx="1.5" {FILL}/>')
    if puerta: o.append(f'<rect x="{cx-4:.1f}" y="{by-10:.1f}" width="8" height="10" class="cut"/>')
    return ''.join(o)
def huaje(cx, ty, s=1):
    # Rama de huaje: rama con hojas pinnadas arriba y tres vainas colgando con sus semillas.
    o = [f'<g transform="translate({cx} {ty}) scale({s})">', f'<path d="M-20,12 Q0,6 20,12" {st(4.5)}/>']
    for x in (-20, 20): o.append(f'<circle cx="{x}" cy="12" r="3.4" {FILL}/>')
    for x0, bend in ((-13, -3), (0, 0), (13, 3)):
        y0 = 12 - 6*(1 - (x0/20)**2)
        o.append(f'<path d="M{x0},{y0+3:.1f} Q{x0 + bend*2},{y0 + 22:.1f} {x0 + bend},{y0 + 40:.1f}" {st(8)}/>')
        for t in (.4, .7):
            px = (1-t)**2*x0 + 2*(1-t)*t*(x0+bend*2) + t*t*(x0+bend); py = (1-t)**2*(y0+3) + 2*(1-t)*t*(y0+22) + t*t*(y0+40)
            o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="1.7" class="cut"/>')
    return ''.join(o) + '</g>'
def cadena(cx, cy, s=1, w=S):
    o = [f'<g transform="translate({cx} {cy}) scale({s})">']
    E = lambda x, y, r: f'<rect x="{x-13}" y="{y-7.5}" width="26" height="15" rx="7.5" transform="rotate({r} {x} {y})" {st(w)}/>'
    for sg in (-1, 1):
        o.append(E(sg*44, 6, sg*-18)); o.append(E(sg*24, -1, sg*-18))
        o.append(f'<path d="M{sg*9},-9 Q{sg*2},-9 {sg*1},-2" transform="rotate({sg*-18} {sg*9} 0)" {st(w)}/>')
    o.append(f'<path d="M0,-17 v-6 M-7,-14 l-4,-4 M7,-14 l4,-4" {st(w*.6)}/>')
    return ''.join(o) + '</g>'
def estrella8(cx, cy, R, r=None):
    r = r or R * .5; p = []
    for k in range(16):
        a = math.radians(-90 + k * 22.5); rr = R if k % 2 == 0 else r; p.append(f'{cx + rr*math.cos(a):.1f},{cy + rr*math.sin(a):.1f}')
    return f'<path d="M{" L".join(p)}Z" {FILL}/>'
def nopal(cx, cy, s=1):
    o = [f'<g transform="translate({cx} {cy}) scale({s})">',
         f'<ellipse cx="0" cy="8" rx="11" ry="15" {st(5)}/>', f'<ellipse cx="-14" cy="-12" rx="8" ry="11" transform="rotate(-30 -14 -12)" {st(5)}/>',
         f'<ellipse cx="14" cy="-12" rx="8" ry="11" transform="rotate(30 14 -12)" {st(5)}/>']
    for x, y in ((0, 2), (-4, 12), (4, 14), (-14, -14), (14, -14)): o.append(f'<circle cx="{x}" cy="{y}" r="2.4" {FILL}/>')
    return ''.join(o) + '</g>'
PROPIOS = {
 'cactus': '<path d="M10 21V5a2 2 0 0 1 4 0v16"/><path d="M10 13H8a2 2 0 0 1-2-2V8"/><path d="M14 11h2a2 2 0 0 0 2-2V6"/><path d="M5 21h14"/>',
 'mariposa': '<path d="M12 8v11"/><path d="M12 11C10 6 5 3.5 3.5 5.5S4 11.5 12 12"/><path d="M12 11c2-5 7-7.5 8.5-5.5S20 11.5 12 12"/><path d="M12 13.5c-3 0-6.5 1.5-5.5 4.5s4.5 1 5.5-2.5"/><path d="M12 13.5c3 0 6.5 1.5 5.5 4.5s-4.5 1-5.5-2.5"/><path d="m12 8-2-3.5M12 8l2-3.5"/>',
 'agave': '<path d="M12 20V4"/><path d="M12 20C11 14 8 10 4 8"/><path d="M12 20c1-6 4-10 8-12"/><path d="M12 20c-2-3-5-5-9-5.5"/><path d="M12 20c2-3 5-5 9-5.5"/><path d="M5 20h14"/>',
}
def picto(n, cx, cy, size, w=2.4):
    k = size / 24; body = PROPIOS.get(n) or luc(n)
    return f'<g transform="translate({cx - size/2:.1f} {cy - size/2:.1f}) scale({k:.3f})" {st(w)}>{body}</g>'
REGIONES = [('Cañada', 'cactus'), ('Papaloapan', 'mariposa'), ('Sierra Norte', 'tree-pine'), ('Istmo', 'wind'),
            ('Costa', 'waves'), ('Sierra Sur', 'mountain'), ('Valles Centrales', 'agave'), ('Mixteca', 'cloud-rain')]
