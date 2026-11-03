# Tres emblemas en caja 200 × 230 (la cimera puede salir por arriba hasta y = -10).
from piezas import *
def escudo_sil(x0=36, x1=164, top=70, base=214):
    cx = (x0 + x1) / 2
    return f'M{x0},{top} V{base-62} C{x0},{base-24} {cx-28},{base-6} {cx},{base} C{cx+28},{base-6} {x1},{base-24} {x1},{base-62} V{top} Z'
def lienzo(x0, x1, y):
    # Lienzo enrollado: barra superior con dos volutas.
    return (f'<path d="M{x0+8},{y} H{x1-8}" {st(S)}/>'
            f'<path d="M{x0+8},{y} H{x0+2} a9,9 0 1 1 9,-9" {st(S*.85)}/><circle cx="{x0+2}" cy="{y-9}" r="2.6" {FILL}/>'
            f'<path d="M{x1-8},{y} H{x1-2} a9,9 0 1 0 -9,-9" {st(S*.85)}/><circle cx="{x1-2}" cy="{y-9}" r="2.6" {FILL}/>')
def emblema_a():
    # A · Escudo de las ocho regiones: cimera de águila, lienzo, bordura con ocho estrellas, Mitla, huaje y cadena rota.
    o = [aguila(70, 2, .95), lienzo(26, 174, 66)]
    o.append(f'<path d="{escudo_sil(36, 164, 66, 222)}" {st(S)}/>')
    o.append(f'<path d="{escudo_sil(52, 148, 82, 204)}" {st(S*.7)}/>')
    # ocho estrellas en la bordura: 3 a cada lado y 2 abajo
    pts = [(44, 96), (44, 128), (44, 160), (156, 96), (156, 128), (156, 160), (72, 204), (128, 204)]
    for x, y in pts: o.append(estrella8(x, y, 6.2, 2.6))
    o.append(f'<path d="M100,82 V140 M52,140 H148" {st(S*.7)}/>')
    o.append(mitla(76, 132, 40, 3))
    o.append(huaje(124, 88, .92))
    o.append(cadena(100, 168, .66, S*1.15))
    return ''.join(o)
def octagono(R):
    return 'M' + ' L'.join(f'{100 + R*math.cos(math.radians(-112.5 + 45*k)):.1f},{124 + R*math.sin(math.radians(-112.5 + 45*k)):.1f}' for k in range(8)) + 'Z'
def emblema_b():
    # B · Greca: marco octagonal de grecas (un lado por región) que abraza el escudo; águila de cimera.
    o = [f'<path d="{octagono(96)}" {st(S)}/>', f'<path d="{octagono(76)}" {st(S*.7)}/>']
    for k in range(8):
        if k == 0: continue  # el lado de arriba es la cimera
        ang = 45 * k; ap = 86 * math.cos(math.radians(22.5)) - 1
        o.append(f'<g transform="rotate({ang} 100 124) translate(100 {124 - ap})"><path d="M-17,5 V-5 H-7 V3 H1 V-5 H17 V5 H9 V-1" {st(S*.62)}/></g>')
    o.append(f'<rect x="72" y="20" width="56" height="28" class="cut"/>')
    o.append(aguila(71, -14, .92))
    o.append(f'<path d="{escudo_sil(64, 136, 70, 184)}" {st(S*.75)}/>')
    o.append(f'<path d="M100,70 V128 M64,128 H136" {st(S*.6)}/>')
    o.append(mitla(82, 122, 28, 3, False)); o.append(estrella8(118, 99, 13, 5.2)); o.append(cadena(100, 152, .44, S*1.5))
    return ''.join(o)
def emblema_c():
    # C · Ocho pétalos: cada pétalo una región con su pictograma; al centro, el escudo con águila y Mitla.
    o = [f'<circle cx="100" cy="122" r="84" {st(S*.6)}/>']
    for k, (n, ic) in enumerate(REGIONES):
        a = math.radians(-90 + 45 * k); x, y = 100 + 84*math.cos(a), 122 + 84*math.sin(a)
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="25" class="cut" stroke="currentColor" stroke-width="{S*.75}"/>')
        o.append(picto(ic, x, y, 26, 2.3))
    o.append(f'<path d="{escudo_sil(68, 132, 80, 168)}" {st(S*.85)}/>')
    o.append(aguila(82, 86, .56))
    o.append(mitla(100, 154, 40, 3))
    return ''.join(o)
E = {'a': emblema_a, 'b': emblema_b, 'c': emblema_c}
NOM = {'a': 'Escudo de las ocho regiones', 'b': 'Greca', 'c': 'Ocho pétalos'}
