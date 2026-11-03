# Escudo de Oaxaca · r5 (2026-11-03). Pedido: moderno, con significado, que incorpore de forma NO literal elementos del
# escudo actual; por ahora solo blanco y negro. Tres propuestas; cada forma traduce un elemento del escudo actual.
# Uso: python3 gen.py → svg/, revision.html
import os, math, base64
D = os.path.dirname(os.path.abspath(__file__)); SV = os.path.join(D, 'svg')
N, B = '#111111', '#FFFFFF'
SIL = 'M24,0 H216 L240,24 V150 C240,212 184,254 120,282 C56,254 0,212 0,150 V24 Z'
def rombo(x, y, r, c): return f'<path d="M{x},{y-r} L{x+r},{y} L{x},{y+r} L{x-r},{y}Z" fill="{c}"/>'
def svg(body, t, vb='-8 -8 256 300'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{t}"><title>{t}</title>{body}</svg>'

def ruptura(p, fg, bg):
    # La escalera de Mitla corta el escudo en dos y separa las mitades: las cadenas que se rompen.
    st = [(-20,214),(30,214),(30,186),(70,186),(70,158),(110,158),(110,130),(150,130),(150,102),(190,102),(190,74),(260,74)]
    s = ' L'.join(f'{x},{y}' for x, y in st)
    b = [f'<clipPath id="{p}-u"><path d="M-20,-20 L260,-20 L{s} Z"/></clipPath>'.replace('L260,-20 L-20,214', 'L260,-20 L260,74 L-20,214') if False else
         f'<clipPath id="{p}-u"><path d="M-20,-20 H260 V74 L' + ' L'.join(f'{x},{y}' for x, y in reversed(st)) + ' Z"/></clipPath>',
         f'<clipPath id="{p}-d"><path d="M-20,320 H260 V74 L' + ' L'.join(f'{x},{y}' for x, y in reversed(st)) + ' Z"/></clipPath>',
         f'<path d="{SIL}" fill="{fg}" clip-path="url(#{p}-u)" transform="translate(-4 -5)"/>',
         f'<path d="{SIL}" fill="{fg}" clip-path="url(#{p}-d)" transform="translate(4 5)"/>']
    for k in range(8): b.append(rombo(38 + k*23.4, 34, 7, bg))
    return svg(''.join(b), 'Propuesta A: Ruptura')

def huajes(p, fg, bg):
    # Ocho vainas de huaje forman el escudo; sus puntas dibujan el perfil escalonado de Mitla; una semilla en cada una.
    w, g = 25, 5.86; tops = [48, 32, 16, 0, 0, 16, 32, 48]
    b = [f'<clipPath id="{p}-s"><path d="M-10,-10 H250 V150 C250,212 184,262 120,290 C56,262 -10,212 -10,150 Z"/></clipPath><g clip-path="url(#{p}-c)">']
    b = [f'<clipPath id="{p}-c"><path d="M0,-60 H240 V150 C240,212 184,254 120,282 C56,254 0,212 0,150 Z"/></clipPath><g clip-path="url(#{p}-c)">']
    for k in range(8):
        x = k * (w + g); b.append(f'<rect x="{x:.1f}" y="{tops[k]}" width="{w}" height="320" rx="{w/2}" fill="{fg}"/>')
        b.append(f'<circle cx="{x + w/2:.1f}" cy="{tops[k] + 104 - abs(k - 3.5)*6:.1f}" r="5.5" fill="{bg}"/>')
    b.append('</g>')
    return svg(''.join(b), 'Propuesta B: Huajes')

def eslabon(p, fg, bg):
    # El óvalo del lema es un eslabón abierto; adentro, la plataforma escalonada de Mitla y ocho estrellas en arco.
    cx, cy, rx, ry = 120, 136, 78, 96; sw = 15
    pt = lambda t: (cx + rx*math.cos(math.radians(t)), cy + ry*math.sin(math.radians(t)))
    a0, a1 = pt(100), pt(80)
    b = [f'<path d="{SIL}" fill="{fg}"/>',
         f'<path d="M{a0[0]:.1f},{a0[1]:.1f} A{rx},{ry} 0 1 1 {a1[0]:.1f},{a1[1]:.1f}" fill="none" stroke="{bg}" stroke-width="{sw}" stroke-linecap="butt"/>']
    for i, (w, h) in enumerate(((96, 14), (70, 14), (44, 14))):
        b.append(f'<rect x="{cx - w/2}" y="{cy + 62 - (i+1)*16}" width="{w}" height="{h}" fill="{bg}"/>')
    for k in range(8):
        t = math.radians(200 + k * 140/7); b.append(rombo(cx + 46*math.cos(t), cy + 6 + 52*math.sin(t), 6, bg))
    return svg(''.join(b), 'Propuesta C: Eslabón')

F = {'a': ruptura, 'b': huajes, 'c': eslabon}
for k, f in F.items():
    open(os.path.join(SV, f'oaxaca-{k}-negro.svg'), 'w').write(f(k + 'n', N, B))
    open(os.path.join(SV, f'oaxaca-{k}-blanco.svg'), 'w').write(f(k + 'b', B, N))
def uri(s): return 'data:image/svg+xml;base64,' + base64.b64encode(s.encode()).decode()
def tam(f, k):
    s = f(k + 't', N, B); i = f(k + 'i', B, N)
    return (''.join(f'<figure><img src="{uri(s)}" width="{n}" height="{n}" alt=""><figcaption>{n}</figcaption></figure>' for n in (48, 32, 16)) +
            f'<figure><span class="inv"><img src="{uri(i)}" width="40" height="40" alt=""></span><figcaption>invertido</figcaption></figure>')
html = open(os.path.join(D, 'plantilla.html')).read()
for k, f in F.items(): html = html.replace('{{' + k.upper() + '}}', f(k, N, B)).replace('{{T' + k.upper() + '}}', tam(f, k))
assert '{{' not in html
open(os.path.join(D, 'revision.html'), 'w').write(html); print('ok')
