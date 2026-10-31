# Convia · íconos de «rasgos» (Va bien para…): qué se puede hacer en un lugar. Mismo trazo de plumón que los íconos de giro.
# Uso: python3 rasgos.py → rasgos/<clave>.svg + rasgos/vista.html. Nombres y criterios: RASGOS (propuesta, pendiente de aprobación).
import os, math
from iconos import ln, circ, rr, C, D
def ell(cx, cy, rx, ry, n=18): return [(cx + rx * math.cos(2 * math.pi * k / n), cy + ry * math.sin(2 * math.pi * k / n)) for k in range(n)]
dot = lambda x, y, r: f'<circle cx="{x}" cy="{y}" r="{r}" stroke="none" fill="currentFill"/>'
I = {
 'trabajar': ln(rr(46, 40, 154, 120, 12), 31, True) + ln([(20, 150), (180, 150)], 32) + ln([(84, 150), (90, 138), (110, 138), (116, 150)], 33, w=10),
 'idiomas': ln(ell(76, 72, 52, 38), 34, True) + ln([(52, 104), (40, 132), (78, 110)], 35, w=11)
          + ln(ell(132, 130, 46, 34), 36, True) + ln([(150, 160), (164, 184), (128, 164)], 37, w=11),
 'networking': ln(circ(100, 44, 20, 38, 12), 38, True, w=12) + ln(circ(44, 150, 20, 39, 12), 39, True, w=12) + ln(circ(156, 150, 20, 40, 12), 40, True, w=12)
          + ln([(88, 64), (56, 130)], 41, w=11) + ln([(112, 64), (144, 130)], 42, w=11) + ln([(66, 150), (134, 150)], 43, w=11),
 'ingles': ln(circ(100, 100, 70, 44, 20), 44, True) + ln(ell(100, 100, 30, 70, 16), 45, True, w=11) + ln([(32, 100), (168, 100)], 46, w=11),
 'solo': ln(circ(100, 60, 28, 47, 14), 47, True) + ln([(44, 172), (50, 132), (100, 108), (150, 132), (156, 172)], 48),
 'mascotas': ln(ell(100, 134, 40, 32), 49, True) + dot(52, 88, 15) + dot(82, 54, 15) + dot(118, 54, 15) + dot(148, 88, 15),
 'vegano': ln([(40, 162), (50, 98), (96, 52), (166, 34), (152, 104), (108, 150)], 50, True) + ln([(40, 162), (124, 78)], 51, w=11),
 'accesible': dot(86, 34, 15) + ln([(86, 62), (90, 112), (138, 112), (156, 158), (176, 150)], 52, w=13)
          + ln([(58, 98), (40, 120), (42, 152), (64, 174), (98, 176), (122, 160)], 53, w=13),
}
# clave: (nombre, criterio de revisión, ¿lleva día y hora?)
RASGOS = {
 'trabajar': ('Para trabajar', 'Wifi probado en la revisión, enchufes al alcance de las mesas y se puede quedar dos horas o más sin presión para consumir otra vez.', False),
 'idiomas': ('Intercambio de idiomas', 'Encuentro de conversación que se repite con día y hora fijos; la ficha siempre muestra cuándo es.', True),
 'networking': ('Networking', 'Encuentro recurrente para conocer gente de un oficio o comunidad (por ejemplo, freelancers); con día y hora.', True),
 'ingles': ('Te atienden en inglés', 'Hay personal que atiende en inglés en el horario publicado; si es solo menú, no cuenta.', False),
 'solo': ('Para ir solo', 'Grupo abierto o barra: llegar sin compañía es lo normal, no la excepción.', False),
 'mascotas': ('Con mascota', 'Se puede entrar con perro o gato, al menos en una zona del lugar.', False),
 'vegano': ('Opciones veganas', 'Al menos dos platillos o bebidas completos sin ingredientes de origen animal, marcados en la carta.', False),
 'accesible': ('Silla de ruedas', 'Entrada sin escalones (o rampa) y baño adaptado, comprobados en la revisión.', False),
}
def svg(k, col='currentColor', size=None, cls=None):
    wh = f' width="{size}" height="{size}"' if size else ''
    c = f' class="{cls}" aria-hidden="true"' if cls else f' role="img" aria-label="{RASGOS[k][0]}"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"{wh}{c}><g fill="none" stroke="{col}" stroke-linecap="round" stroke-linejoin="round">'
            + I[k].replace('currentFill', col) + '</g></svg>')
if __name__ == '__main__':
    for k in I: open(os.path.join(D, 'rasgos', f'{k}.svg'), 'w').write(svg(k))
    rows = ''.join(f'<div class="c"><div class="r">{svg(k, C["tinta"], 72)}{svg(k, C["tinta"], 24)}{svg(k, C["tinta"], 16)}</div><b>{n}</b><small>{t}</small></div>' for k, (n, t, _) in RASGOS.items())
    open(os.path.join(D, 'rasgos', 'vista.html'), 'w').write(f'<!doctype html><meta charset="utf-8"><style>body{{margin:0;padding:28px;background:{C["papel"]};font:600 15px sans-serif;width:980px}}main{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}.c{{background:#fff;border:1px solid {C["linea"]};border-radius:16px;padding:18px;display:grid;gap:8px;align-content:start}}.r{{display:flex;gap:16px;align-items:center}}small{{font-weight:400;color:#5c5f5b;line-height:1.4}}</style><main>{rows}</main>')
    print('ok')
