# Escudo de Oaxaca · r4 (2026-11-03). Pedido: «diseño moderno, disruptivo, con movimiento». r1-r3 no gustaron.
# Silueta nueva (esquinas cortadas, base en punta). Las ocho regiones como ocho colores. Tres ideas cinéticas:
# A Ensamble (ocho piezas que llegan y forman el escudo) · B Onda (ocho contornos que laten) · C Franjas (ocho bandas en diagonal).
# El estado final quieto es el escudo; respeta prefers-reduced-motion. Uso: python3 gen.py → revision.html, svg/
import os, math
D = os.path.dirname(os.path.abspath(__file__)); os.makedirs(os.path.join(D, 'svg'), exist_ok=True)
COL = ['#5E7F2A', '#0E7C86', '#1F5136', '#B5651D', '#8E1B2E', '#B0245E', '#6D4C41', '#1F4E8C']  # Cañada…Costa (r3)
REG = ['Cañada', 'Papaloapan', 'Sierra Norte', 'Mixteca', 'Valles Centrales', 'Istmo', 'Sierra Sur', 'Costa']
SIL = 'M24,0 H216 L240,24 V150 C240,212 184,254 120,282 C56,254 0,212 0,150 V24 Z'
FONDO = '#F7F1E6'
def svg(p, body, t): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-14 -14 268 310" class="esc esc-{p}" role="img" aria-label="{t}"><title>{t}</title>{body}</svg>'
def a(p='a'):
    cx, cy = 104, 128; ang = [-104, -58, -20, 18, 62, 104, 150, 206]; b = [f'<clipPath id="{p}-s"><path d="{SIL}"/></clipPath>']
    for k in range(8):
        a0, a1 = math.radians(ang[k]), math.radians(ang[(k + 1) % 8] + (360 if k == 7 else 0))
        mid = (a0 + a1) / 2; dx, dy = 60*math.cos(mid), 60*math.sin(mid); rot = (-1)**k * 14
        w = f'M{cx},{cy} L{cx + 500*math.cos(a0):.1f},{cy + 500*math.sin(a0):.1f} L{cx + 500*math.cos(mid):.1f},{cy + 500*math.sin(mid):.1f} L{cx + 500*math.cos(a1):.1f},{cy + 500*math.sin(a1):.1f}Z'
        b.append(f'<g class="pz" style="--dx:{dx:.0f}px;--dy:{dy:.0f}px;--r:{rot}deg;--i:{k}"><path d="{w}" clip-path="url(#{p}-s)" fill="{COL[k]}" stroke="{FONDO}" stroke-width="5" stroke-linejoin="round"/></g>')
    return svg(p, ''.join(b), 'Escudo de Oaxaca, propuesta A: ensamble')
def b(p='b'):
    b = []
    for k in range(8):
        s = 1 - k * .118
        b.append(f'<g class="ola" style="--i:{k}"><path d="{SIL}" transform="translate({120*(1-s):.1f} {141*(1-s):.1f}) scale({s:.3f})" fill="none" stroke="{COL[k]}" stroke-width="{9/s:.1f}" stroke-linejoin="round"/></g>')
    b.append(f'<circle cx="120" cy="141" r="9" fill="{COL[4]}" class="nucleo"/>')
    return svg(p, ''.join(b), 'Escudo de Oaxaca, propuesta B: onda')
def c(p='c'):
    b = [f'<clipPath id="{p}-s"><path d="{SIL}"/></clipPath><g clip-path="url(#{p}-s)"><g transform="rotate(-28 120 141)">']
    for k in range(8):
        b.append(f'<g class="fr" style="--i:{k}"><rect x="-200" y="{-40 + k*39.3:.1f}" width="640" height="40.5" fill="{COL[k]}"/></g>')
    b.append('</g></g>')
    return svg(p, ''.join(b), 'Escudo de Oaxaca, propuesta C: franjas')
F = {'a': a, 'b': b, 'c': c}
for k, f in F.items(): open(os.path.join(D, 'svg', f'oaxaca-{k}.svg'), 'w').write(f(k + 'f'))
html = open(os.path.join(D, 'plantilla.html')).read()
for k, f in F.items(): html = html.replace('{{' + k.upper() + '}}', f(k))
html = html.replace('{{LEY}}', ''.join(f'<li><span style="background:{c}"></span>{n}</li>' for n, c in zip(REG, COL)))
assert '{{' not in html
open(os.path.join(D, 'revision.html'), 'w').write(html); print('ok')
