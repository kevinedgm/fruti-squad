# Administración Manik · ronda 1: tres propuestas de sello (rasgo en el borde del cuadro, la línea de pulso idéntica) + color + cómo aparece
# en el inicio del ecosistema solo para cuentas del equipo MedicalManik. Pedido del usuario (2026-10-31).
# Uso: python3 gen.py <salida>  → <salida>/index.html (lee los sellos finales de ../final/svg).
import sys, os, math, json
D = os.path.dirname(os.path.abspath(__file__)); FIN = os.path.join(D, '..', 'final', 'svg')
PAPEL = '#F6F8FC'; LINEA = 'M-6 63 L13 63 L27 12 L49 86 L71 25 L84 64 L106 64'; r = 21
CUADRO = f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z'
ESCUDO = f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V60 C100 82 78 96 50 106 C22 96 0 82 0 60 V{r} A{r} {r} 0 0 1 {r} 0 Z'
def engrane(cx, cy, ro=13, ri=9.6, n=8, hole=4.2):
    pts = []
    for i in range(n * 4):
        a = 2 * math.pi * i / (n * 4) - math.pi / 2
        rr = ro if (i % 4) in (1, 2) else ri
        pts.append(f'{cx + rr*math.cos(a):.2f} {cy + rr*math.sin(a):.2f}')
    d = 'M' + ' L'.join(pts) + ' Z'
    d += f' M{cx+hole} {cy} A{hole} {hole} 0 1 0 {cx-hole} {cy} A{hole} {hole} 0 1 0 {cx+hole} {cy} Z'
    return d
GEAR = engrane(95, 1)
CORCH = 'M-3 16 V-3 H16 M84 -3 H103 V16 M-3 84 V103 H16 M84 103 H103 V84'
# (clave, nombre, silueta, pieza trazada, pieza rellena, idea, fuerza, riesgo)
PROPS = [
 ('A', 'Corchetes de control', CUADRO, CORCH, '', 'Cuatro esquinas de encuadre separadas del cuadro, como el visor que enfoca todo el sistema: desde aquí se supervisa y se configura cada app.',
  'Se distingue de los seis: es el único rasgo que rodea el cuadro completo', 'A 24 px las esquinas se vuelven puntos; necesita 32 px para leerse bien'),
 ('B', 'Engrane', CUADRO, '', GEAR, 'Un engrane separado en la esquina superior derecha, donde ya viven la cruz de Farmacia y la flecha de Impulsa: el signo universal de «configuración».',
  'Se entiende al instante; sigue el patrón de pieza en la esquina', 'Es el ícono de «Ajustes» de cualquier app; puede leerse como una opción, no como un producto'),
 ('C', 'Escudo', ESCUDO, '', '', 'El cuadro termina en punta abajo, como un escudo: el lugar donde se protege y se gobierna el sistema. Rasgo de silueta, como la carpeta de Expediente o el ticket de Compras.',
  'Silueta propia, se reconoce aun a 24 px y a una tinta', 'Escudo suele leerse como «seguridad»; aquí es más amplio (usuarios, configuración, apps)')]
COLORES = [('grafito', '#3A4558', 'Grafito', 'Neutro azulado: herramienta interna, «detrás de escena». No compite con ningún producto ni estado. 9.67:1 con blanco.'),
           ('ciruela', '#7A3B6B', 'Ciruela', 'Más carácter, pero cae entre el violeta de Impulsa y el rojo de Grupos. 7.88:1.'),
           ('tinta', '#14213D', 'Tinta', 'El color del texto del sistema: «la casa». Riesgo: es casi el azul noche de Manik IA. 15.97:1.')]
import sys as _s; _s.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final')); from m_original import convertir
def sello(k, d, trazo, relleno, color='currentColor', uid=''):
    i = f'{k}{uid}'
    m = f'<mask id="m{i}" maskUnits="userSpaceOnUse" x="-8" y="-18" width="126" height="126"><rect x="-8" y="-18" width="126" height="126" fill="#fff"/>'
    if trazo: m += f'<path d="{trazo}" fill="none" stroke="#000" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>'
    if relleno: m += f'<path d="{relleno}" fill="#000" stroke="#000" stroke-width="9" stroke-linejoin="round" fill-rule="evenodd"/>'
    m += '</mask>'
    s = f'<defs><clipPath id="c{i}"><path d="{d}"/></clipPath>{m}</defs><g mask="url(#m{i})"><path d="{d}" fill="{color}"/><path clip-path="url(#c{i})" d="{LINEA}" fill="none" stroke="{PAPEL}" stroke-width="13" stroke-linejoin="round"/></g>'
    if trazo: s += f'<path d="{trazo}" fill="none" stroke="{color}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
    if relleno: s += f'<path d="{relleno}" fill="{color}" fill-rule="evenodd"/>'
    return convertir(f'<svg viewBox="-8 -18 126 126" aria-hidden="true">{s}</svg>')[0]  # M original (2026-11-05)
APPS = [('expediente', 'Expediente', 'Médicos', 'Consultas, recetas y expediente clínico'), ('agenda', 'Agenda', 'Asistentes', 'Citas, confirmaciones y sala de espera'),
        ('compras', 'Compras', 'Administración de la clínica', 'Compras, proveedores y facturación'), ('farmacia', 'Farmacia', 'Farmacia', 'Surtido, existencias y caducidades'),
        ('impulsa', 'Impulsa', 'Marketing clínico', 'Campañas de prevención y pacientes'), ('grupos', 'Grupos', 'Administradores de grupo', 'Clínicas, sedes y permisos del grupo')]
SELLOS = {a: open(os.path.join(FIN, f'{a}.svg')).read() for a, *_ in APPS}
DATA = {'props': [{'k': k, 'n': n, 'idea': idea, 'f': f, 'r': rr, 'svg': sello(k, d, t, rel, uid='x')} for k, n, d, t, rel, idea, f, rr in PROPS],
        'propSvg': {k: (d, t, rel) for k, n, d, t, rel, *_ in PROPS},
        'colores': [{'id': i, 'hex': h, 'n': n, 'd': dd} for i, h, n, dd in COLORES],
        'apps': [{'id': a, 'n': n, 'para': p, 'q': q, 'svg': SELLOS[a]} for a, n, p, q in APPS]}
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const DATA=' + json.dumps(DATA, ensure_ascii=False) + ';const LINEA=' + json.dumps(LINEA) + ';')
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
