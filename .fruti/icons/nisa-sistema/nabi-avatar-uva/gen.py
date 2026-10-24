# Uva · E2 · familia user-avatar de Nabi (cara mínima de la ronda 4, opción A)
# Uso: python3 gen.py   → escribe <id>-<variante>.svg y piezas.json (para medir separaciones)
import re, json

K, CX, CY = 1.0, 12.0, 12.0      # retícula 24 sin escalar: a 1.5 de trazo la cara necesita todo el lienzo (A6)
def T(d): return d
def P(x, y): return x, y

def ojo(x, y):  # punto de r 0.3 con trazo: crece y adelgaza con --uva-stroke (reglas: rellenos y grosor)
    return ('circle', {'cx': x, 'cy': y, 'r': 0.3})

# Cara de la ronda 4 (A) redibujada en 24: ceja suelta · ceja que baja y se vuelve nariz · dos puntos · boca corta
CARA = [('ceja', ('path', {'d': 'M6.4 9 Q8.2 7.3 10.1 8.5'})),
        ('ojo-izq', ojo(8.1, 12.3)), ('ojo-der', ojo(16.5, 12.3)),
        ('ceja-nariz', ('path', {'d': 'M18 9 C16.8 7.4 14.5 7.5 13.6 9.2 L11.9 15.9 L14 16.4'})),
        ('boca', ('path', {'d': 'M10.6 19.8 L14.2 19.6'}))]
# Con lentes: los aros tapan cejas y ojos; la nariz y la boca bajan para respirar
LENTES = [('lentes', ('path', {'d': 'M6 12 A2.3 2.3 0 1 1 10.6 12 A2.3 2.3 0 1 1 6 12 M13.4 12 A2.3 2.3 0 1 1 18 12 A2.3 2.3 0 1 1 13.4 12 M10.6 11.4 Q12 10.6 13.4 11.4'})),
          ('nariz', ('path', {'d': 'M12.3 16.1 L11.6 17.6 L13.4 17.9'})),
          ('boca', ('path', {'d': 'M10.6 21.25 L14.2 21.05'}))]

R = 'relleno'
ARCO = 'M3.1 7.4 C3.8 4.2 7.4 3 12 3 C16.6 3 20.2 4.2 20.9 7.4'
PELO = {
 # a · línea: el pelo es un trazo más; corto termina en la sien, largo baja hasta los hombros
 ('a', 'm'): [('pelo', ('path', {'d': ARCO}))],
 ('a', 'f'): [('pelo', ('path', {'d': 'M4.4 21 C2.4 17 2.3 12.4 2.7 8.6 C3.3 4.6 7.2 3 12 3 C16.8 3 20.7 4.6 21.3 8.6 C21.7 12.4 21.6 17 19.6 21'}))],
 # b · masa: el pelo es una forma llena, como en los avatares de Notion
 ('b', 'm'): [('pelo', ('path', {'d': 'M2.2 8.6 C2.4 4.2 6.6 2 12 2 C17.4 2 21.6 4.2 21.8 8.6 C21 6.2 19 5.2 16.4 5.2 C14.6 5.2 13 5.4 12 5.8 C10.4 5.2 8.6 5 6.8 5.4 C5 5.8 3.8 6.8 3.4 8.6Z'}, R))],
 ('b', 'f'): [('pelo', ('path', {'d': 'M2.2 21.4 C2 16 2 11 2.2 8.6 C2.4 4.2 6.6 2 12 2 C17.4 2 21.6 4.2 21.8 8.6 C22 11 22 16 21.8 21.4 L17.6 21.4 C18.8 19.4 19.6 16.4 20.2 13 C20.5 11.2 20.7 9.8 20.7 8.6 C20 6.2 18.6 5.2 16.4 5.2 C14.6 5.2 13 5.4 12 5.8 C10.4 5.2 8.6 5 6.8 5.4 C5 5.8 3.8 6.8 3.3 8.6 C3.3 9.8 3.4 11.4 3.8 13.4 C4.5 16.2 5.6 19 7 21.4Z'}, R))],
 # c · moño: el mismo arco corto para todos; el moño lateral es el único rasgo que cambia
 ('c', 'm'): [('pelo', ('path', {'d': ARCO}))],
 ('c', 'f'): [('pelo', ('path', {'d': ARCO + ' M18.95 4.57 A1.35 1.35 0 1 1 20.47 2.35 A1.35 1.35 0 1 1 18.95 4.57'}))],
}
MIEMBROS = [('masculine', 'm', False), ('feminine', 'f', False), ('masculine-glasses', 'm', True), ('feminine-glasses', 'f', True)]

def svg(id_, v, piezas):
    cls = f'uva-{id_}-{v}'
    css = f'.{cls}{{stroke-width:var(--uva-stroke,1.5)}}'
    if any(len(p[1]) > 2 for p in piezas): css += f'.{cls}__{R}{{fill:currentColor;stroke:none}}'
    els = ''
    for nom, (tag, at, *extra) in piezas:
        a = ' '.join(f'{k}="{val}"' for k, val in at.items())
        c = f' class="{cls}__{extra[0]}"' if extra else ''
        els += f'<{tag} data-pieza="{nom}"{c} {a}/>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="uva-icon {cls}" aria-hidden="true" '
            f'data-nombre="{v.upper()} · user-avatar-{id_}"><style>{css}</style>{els}</svg>')

out = {}
for v in 'abc':
    for mid, g, lentes in MIEMBROS:
        piezas = PELO[(v, g)] + (LENTES if lentes else CARA)
        s = svg(mid, v, piezas)
        open(f'user-avatar-{mid}-{v}.svg', 'w').write(s)
        out[f'{mid}-{v}'] = s
json.dump(out, open('piezas.json', 'w'))
print('ok', len(out))
