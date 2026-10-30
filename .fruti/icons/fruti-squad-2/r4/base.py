# Fruti Squad · ronda 3: el método de Manik y Nisa Nabani aplicado a la squad (usuario 2026-10-30).
# Sello madre = cuadro de color con una marca blanca CONSTANTE; cada producto = mismo sello + un RASGO en el borde (silueta o pieza separada por un corte)
# + color propio. El color nunca es la única señal. Identificador del ecosistema: retícula de seis cuadros.
# Marca constante: la fruta (círculo con hoja) con la semilla calada: «Fruti» + la evidencia que cada agente entrega.
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
P = [  # id, nombre, rol (producto), verbo, color, color de la marca, rasgo
 ('squad', 'Fruti Squad', 'Workflow Pack', 'orquestar', '#18181b', '#ffffff'),
 ('kiwi', 'Kiwi', 'UX Architect', 'organizar', '#4f8a2b', '#ffffff'),
 ('lima', 'Lima', 'Design System Governance', 'validar', '#c5e04b', INK),
 ('coco', 'Coco', 'UI Audit', 'inspeccionar', '#8a5a3b', '#ffffff'),
 ('bruno', 'Bruno', 'Implementation', 'conectar', '#2563eb', '#ffffff'),
 ('mora', 'Mora', 'Documentation', 'catalogar', '#7e2e8c', '#ffffff'),
]
def lum(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def cr(a, b): x, y = sorted((lum(a), lum(b))); return (y + .05) / (x + .05)
TILE = '<rect x="8" y="8" width="48" height="48" rx="13"/>'
# rasgos: (forma que se recorta del cuadro con un margen, forma que se dibuja)
R = {
 'squad': ('', ''),
 'kiwi': ('<rect x="40" y="2" width="22" height="22" rx="7"/>', '<rect x="43" y="5" width="16" height="16" rx="5"/>'),
 'lima': ('<circle cx="51" cy="13" r="12"/>', '<circle cx="51" cy="13" r="9"/><path d="M46.5 13l3 3 5.5-6" stroke="¤" stroke-width="2.6" fill="none"/>'),
 'coco': ('<path d="M44 44l16 16" stroke-width="13" stroke="#000"/>', '<path d="M47 47l12 12" stroke-width="7" stroke="§" stroke-linecap="round"/>'),
 'bruno': ('<rect x="52" y="24" width="12" height="16" rx="4"/>', '<rect x="55" y="26" width="7" height="12" rx="2.5"/><path d="M62 29h2M62 35h2" stroke="§" stroke-width="2.5"/>'),
 'mora': ('', ''),
}
def marca_fruta(c):
    return (f'<circle cx="30" cy="36" r="12.5" fill="{c}"/><path d="M33 24.5c0-6.5 5.5-11 12.5-11 0 6.5-5.5 11-12.5 11z" fill="{c}"/>'
            f'<circle cx="30" cy="36" r="3.8" fill="#000"/>')
def sello(k, color, mc, uid, tinta=False):
    cut, draw = R[k]
    if tinta: color, mc = 'currentColor', None
    m = (f'<mask id="m{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/>'
         f'<g fill="#000">{cut}</g>' + marca('#000').replace('fill="#000"/>', 'fill="#000"/>', 1) + '</mask>')
    # la marca se cala en la versión a una tinta; en color se pinta encima
    mk = '' if tinta else marca(mc).replace('<circle cx="30" cy="36" r="3.8" fill="#000"/>', f'<circle cx="30" cy="36" r="3.8" fill="{color}"/>')
    tile_mask = (f'<mask id="t{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/><g fill="#000">{cut}</g>'
                 + (marca('#000') if tinta else '') + '</mask>')
    if tinta:
        tile_mask = tile_mask.replace('<circle cx="30" cy="36" r="3.8" fill="#000"/>', '<circle cx="30" cy="36" r="3.8" fill="#fff"/>')
    d = draw.replace('§', color).replace('¤', mc if mc else '#fff')
    if tinta: d = draw.replace('§', 'currentColor').replace('¤', '#fff')
    back = ''
    if k == 'mora':
        back = (f'<mask id="b{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/>'
                f'<rect x="5" y="5" width="54" height="54" rx="16" fill="#000"/></mask><rect x="15" y="1" width="46" height="46" rx="13" fill="{color}" mask="url(#b{uid})"/>')
    return (f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{back}{tile_mask}<g mask="url(#t{uid})" fill="{color}">{TILE}</g>'
            f'<g fill="{color}">{d}</g>{mk}</svg>')
u = [0]
def S(k, c, mc, t=False):
    u[0] += 1; return sello(k, c, mc, u[0], t)

HOLE = '<circle cx="30" cy="36" r="3.8" fill="#000"/>'
MARCAS = {
 'A': ('Monograma F', 'La F de Fruti con el brazo de abajo convertido en punto: la letra y la evidencia en una pieza.',
       'Propio y escalable como letra; muy legible a 16 px.', 'Las marcas de letra son frías si el dibujo no tiene un detalle memorable.',
       lambda c: f'<path d="M22 50V18h22M22 32h12" stroke="{c}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="43" cy="44" r="6" fill="{c}"/>'),
 'B': ('La entrega', 'Una curva que pasa el punto de un lado al otro: el handoff, la idea central del producto.',
       'Cuenta qué hace la squad sin palabras; se ve dinámica.', 'Puede leerse como «recargar» o «compartir» si la curva es muy circular.',
       lambda c: f'<path d="M17 40a15 15 0 0 1 27-13" stroke="{c}" stroke-width="7.5" stroke-linecap="round" fill="none"/><path d="M45 18l1 10-10 1" stroke="{c}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="40" cy="44" r="6.5" fill="{c}"/>'),
 'C': ('El gajo', 'Un solo gajo de cítrico: fruta sin dibujar una fruta entera; cada agente es un gajo del todo.',
       'Sigue siendo «Fruti» pero más abstracto y moderno que la fruta con hoja.', 'Un gajo suelto puede leerse como gráfica de pastel o pizza.',
       lambda c: f'<path d="M20 46L32 17a26 26 0 0 1 20 25z" fill="{c}" stroke="{c}" stroke-width="4" stroke-linejoin="round"/><path d="M33 41l7-14" stroke="#000" stroke-width="2.6" stroke-linecap="round"/>'),
 'D': ('Hoja que valida', 'Una hoja cuya vena central es una palomita: fresco por fuera, verificado por dentro.',
       'Une la tensión de la marca (frutas + gobernanza) en un solo dibujo.', 'Hoja y palomita son motivos comunes; el ángulo de la hoja debe ser propio.',
       lambda c: f'<path d="M15 47C15 27 29 15 50 15c0 21-12 34-33 34z" fill="{c}"/><path d="M23 33l7 7 12-14" stroke="#000" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'),
}
