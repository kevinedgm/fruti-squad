# Escudo de Oaxaca · r3 (2026-11-03). Pedido: «diseño nuevo, moderno, algo que represente a las 8 regiones», con forma de escudo.
# Las ocho regiones son la estructura del escudo; cada una con su color y su pictograma (propuesta a validar con cada región).
# A ocho cuarteles · B ocho gajos · C mosaico (mapa abstracto, Valles al centro). Uso: python3 gen.py → svg/, revision.html
import os, math, re, base64, json
D = os.path.dirname(os.path.abspath(__file__)); SV = os.path.join(D, 'svg')
r1 = open(os.path.join(D, '..', 'r1', 'gen.py')).read(); exec(r1[:r1.index('# ---------- A ·')])  # paleta, star, huaje
L = '/root/.cache/fruti-uva/package/icons/'
def luc(n): return ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse)[^>]*/>', open(L + n + '.svg').read()))
PROPIOS = {
 'cactus': '<path d="M10 21V5a2 2 0 0 1 4 0v16"/><path d="M10 13H8a2 2 0 0 1-2-2V8"/><path d="M14 11h2a2 2 0 0 0 2-2V6"/><path d="M5 21h14"/>',
 'mariposa': '<path d="M12 8v11"/><path d="M12 11C10 6 5 3.5 3.5 5.5S4 11.5 12 12"/><path d="M12 11c2-5 7-7.5 8.5-5.5S20 11.5 12 12"/><path d="M12 13.5c-3 0-6.5 1.5-5.5 4.5s4.5 1 5.5-2.5"/><path d="M12 13.5c3 0 6.5 1.5 5.5 4.5s-4.5 1-5.5-2.5"/><path d="m12 8-2-3.5M12 8l2-3.5"/>',
 'agave': '<path d="M12 20V4"/><path d="M12 20C11 14 8 10 4 8"/><path d="M12 20c1-6 4-10 8-12"/><path d="M12 20c-2-3-5-5-9-5.5"/><path d="M12 20c2-3 5-5 9-5.5"/><path d="M5 20h14"/>',
}
# región, color, pictograma, por qué (inferencia: validar con gente de cada región)
REG = [
 ('Cañada', '#5E7F2A', 'cactus', 'Las columnas de cactus de la reserva Tehuacán-Cuicatlán.'),
 ('Papaloapan', '#0E7C86', 'mariposa', '«Papaloapan»: río de las mariposas, en náhuatl.'),
 ('Sierra Norte', '#1F5136', 'tree-pine', 'Bosques de pino; la sierra de Juárez.'),
 ('Mixteca', '#B5651D', 'cloud-rain', 'Ñuu Savi: «pueblo de la lluvia», como se nombran los mixtecos.'),
 ('Valles Centrales', '#8E1B2E', 'agave', 'Maguey y mezcal; color grana, que se producía aquí.'),
 ('Istmo', '#B0245E', 'wind', 'El viento del Istmo; el magenta de sus flores bordadas.'),
 ('Sierra Sur', '#6D4C41', 'mountain', 'La sierra madre del sur, tierra adentro.'),
 ('Costa', '#1F4E8C', 'waves', 'El Pacífico.'),
]
def picto(n, cx, cy, size, col='#fff', sw=2.2):
    body = PROPIOS.get(n) or luc(n); k = size / 24
    return f'<g transform="translate({cx - size/2:.1f} {cy - size/2:.1f}) scale({k:.3f})" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{body}</g>'
SIL = 'M30,30 H270 V196 A120,124 0 0 1 30,196 Z'
def escudo(p, cuerpo, nombre=True, titulo=''):
    b = [f'<clipPath id="{p}-s"><path d="{SIL}"/></clipPath><g clip-path="url(#{p}-s)">{cuerpo}</g>',
         f'<path d="{SIL}" fill="none" stroke="{TINTA}" stroke-width="5"/>']
    vb = '22 22 256 306'
    if nombre:
        b.append(f'<path d="M20,334 L50,326 V358 L20,366 L32,350 Z M280,334 L250,326 V358 L280,366 L268,350 Z" fill="{TINTA}"/>'
                 f'<rect x="46" y="322" width="208" height="34" rx="3" fill="{CAL}" stroke="{TINTA}" stroke-width="2.5"/>'
                 f'<text x="150" y="346" text-anchor="middle" font-family="{FONT}" font-size="19" font-weight="800" letter-spacing="7" fill="{TINTA}">OAXACA</text>')
        vb = '10 22 280 350'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{titulo}"><title>{titulo}</title>{"".join(b)}</svg>'
C = {n: c for n, c, *_ in REG}; PI = {n: p for n, _, p, _ in REG}

def a(p='a', nombre=True, iconos=True):  # Ocho cuarteles, 2 × 4, en orden aproximado del mapa (norte arriba)
    orden = [('Cañada', 'Papaloapan'), ('Mixteca', 'Sierra Norte'), ('Valles Centrales', 'Istmo'), ('Sierra Sur', 'Costa')]
    b = [f'<rect width="300" height="400" fill="{CAL}"/>']; h = 74
    for i, fila in enumerate(orden):
        for j, n in enumerate(fila):
            x, y = 30 + j*120, 30 + i*h
            b.append(f'<rect x="{x}" y="{y}" width="120" height="{h}" fill="{C[n]}" stroke="{CAL}" stroke-width="4"/>')
            if iconos: b.append(picto(PI[n], x + 60, y + h/2 - (6 if i == 3 else 0), 36))
    return escudo(p, ''.join(b), nombre, 'Escudo de Oaxaca, propuesta A: ocho cuarteles')

def b(p='b', nombre=True, iconos=True):  # Ocho gajos desde el centro; al centro el huaje, el nombre que las une
    cx, cy = 150, 178; b = []
    orden = ['Cañada', 'Papaloapan', 'Sierra Norte', 'Istmo', 'Costa', 'Sierra Sur', 'Valles Centrales', 'Mixteca']
    for k, n in enumerate(orden):
        a0, a1 = math.radians(-112.5 + 45*k), math.radians(-67.5 + 45*k)
        b.append(f'<path d="M{cx},{cy} L{cx + 400*math.cos(a0):.1f},{cy + 400*math.sin(a0):.1f} L{cx + 400*math.cos(a1):.1f},{cy + 400*math.sin(a1):.1f}Z" fill="{C[n]}" stroke="{CAL}" stroke-width="4"/>')
        if iconos:
            am = math.radians(-90 + 45*k); rr = 92 if k not in (3, 5) else 96
            b.append(picto(PI[n], cx + rr*math.cos(am), cy + rr*math.sin(am), 32))
    b.append(f'<circle cx="{cx}" cy="{cy}" r="46" fill="{CAL}" stroke="{TINTA}" stroke-width="3"/>' + huaje(cx, cy + 2, .62, hoja=TINTA, vaina=GRANA, semilla=CAL))
    return escudo(p, ''.join(b), nombre, 'Escudo de Oaxaca, propuesta B: ocho gajos')

MOS = {  # mapa abstracto: cada región en su posición aproximada, Valles Centrales al centro
 'Mixteca': [(30,30),(110,30),(120,110),(100,170),(30,182)],
 'Cañada': [(110,30),(185,30),(175,95),(120,110)],
 'Papaloapan': [(185,30),(270,30),(270,122),(205,126),(175,95)],
 'Sierra Norte': [(120,110),(175,95),(205,126),(200,172),(150,176)],
 'Valles Centrales': [(100,170),(120,110),(150,176),(200,172),(186,226),(114,232)],
 'Istmo': [(205,126),(270,122),(270,262),(186,226),(200,172)],
 'Sierra Sur': [(30,182),(100,170),(114,232),(186,226),(140,266),(30,252)],
 'Costa': [(30,252),(140,266),(186,226),(270,262),(270,420),(30,420)],
}
CENT = {'Mixteca': (70, 104), 'Cañada': (148, 62), 'Papaloapan': (228, 74), 'Sierra Norte': (166, 140), 'Valles Centrales': (150, 200),
        'Istmo': (236, 190), 'Sierra Sur': (78, 220), 'Costa': (150, 290)}
def c(p='c', nombre=True, iconos=True):
    b = []
    for n, pts in MOS.items():
        b.append(f'<path d="M' + ' L'.join(f'{x},{y}' for x, y in pts) + f'Z" fill="{C[n]}" stroke="{CAL}" stroke-width="4" stroke-linejoin="round"/>')
        if iconos: b.append(picto(PI[n], *CENT[n], 32 if n not in ('Sierra Norte', 'Cañada') else 28))
    return escudo(p, ''.join(b), nombre, 'Escudo de Oaxaca, propuesta C: mosaico de las ocho regiones')

F = {'a': a, 'b': b, 'c': c}
for k, f in F.items():
    open(os.path.join(SV, f'oaxaca-{k}.svg'), 'w').write(f(k))
    open(os.path.join(SV, f'oaxaca-{k}-reducido.svg'), 'w').write(f(k + 'r', False, False))
def uri(s): return 'data:image/svg+xml;base64,' + base64.b64encode(s.encode()).decode()
def lum(h):
    q = [int(h[i:i+2], 16)/255 for i in (1, 3, 5)]; q = [x/12.92 if x <= .04045 else ((x+.055)/1.055)**2.4 for x in q]
    return .2126*q[0] + .7152*q[1] + .0722*q[2]
cr = lambda h: (1.05)/(lum(h)+.05)
def tam(f, k):
    con = f(k + 't', False, True); sin = f(k + 'u', False, False)
    return (''.join(f'<figure><img src="{uri(con)}" width="{n}" height="{n}" alt=""><figcaption>{n}</figcaption></figure>' for n in (64, 32)) +
            ''.join(f'<figure><img src="{uri(sin)}" width="{n}" height="{n}" alt=""><figcaption>{n} sin iconos</figcaption></figure>' for n in (32, 16)))
leyenda = ''.join(f'<li><span class="sw" style="background:{col}"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{PROPIOS.get(pi) or luc(pi)}</svg></span><div><b>{n}</b><span>{why}</span></div></li>' for n, col, pi, why in REG)
html = open(os.path.join(D, 'plantilla.html')).read()
for k, f in F.items(): html = html.replace('{{' + k.upper() + '}}', f(k)).replace('{{T' + k.upper() + '}}', tam(f, k))
html = html.replace('{{LEY}}', leyenda).replace('{{MINCR}}', f'{min(cr(c) for _, c, *_ in REG):.1f}')
assert '{{' not in html
open(os.path.join(D, 'revision.html'), 'w').write(html)
print('ok; contraste blanco mínimo', round(min(cr(c) for _, c, *_ in REG), 2), [(n, round(cr(c), 1)) for n, c, *_ in REG])
