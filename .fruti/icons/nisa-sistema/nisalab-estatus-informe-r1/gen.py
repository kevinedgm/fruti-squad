# NisaLab · iconos de estatus del informe, ronda 1. Pedido del usuario (2026-11-03): iconos para «En proceso»,
# «Listo para generar informe» e «Informe generado» (recepción → emisión del informe de resultados).
# Fuente aprobada: componente EstadoMuestra (nabi-design-system). Colores de pastilla = tokens muestra-*; no cambian.
# Contrato Uva: viewBox 24, trazo 2, puntas redondas, currentColor. Uso: python3 gen.py → variantes/, revision.html
import os, json, re
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, 'variantes'); os.makedirs(V, exist_ok=True)
L = '/root/.cache/fruti-uva/package/icons/'
def luc(n): return ''.join(re.findall(r'<(?:path|circle|rect|line|polyline)[^>]*/>', open(L + n + '.svg').read()))
def svg(i, b): return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
                       f'class="uva-icon uva-{i}" aria-hidden="true" focusable="false"><style>.uva-{i}{{stroke-width:var(--uva-stroke,2)}}</style>{b}</svg>')
C = '<circle cx="12" cy="12" r="10"/>'
FILL = ' fill="currentColor"'
def puntos(n): return ''.join(f'<circle cx="{x}" cy="12" r="2.6"{FILL if k < n else ""}/>' for k, x in enumerate((4.5, 12, 19.5)))
# Actual (EstadoMuestra): círculo que se llena; se redibuja en la retícula 24 para compararlo igual.
def etapa(n):
    if n == 3: return ('<mask id="uva-estatus-generado-a-m"><rect width="24" height="24" fill="white" stroke="none"/><path d="m8 12 3 3 5-5" stroke="black"/></mask>'
                       '<circle cx="12" cy="12" r="10" fill="currentColor" mask="url(#uva-estatus-generado-a-m)"/>')
    arc = 'M12 12V5a7 7 0 0 1 0 14z' if n == 1 else 'M12 12V5a7 7 0 1 1-7 7z'
    return C + f'<path d="{arc}" fill="currentColor" stroke="none"/>'
EST = [('en-proceso', 'En proceso', '#E0F2FE', '#075985', 'Con folio interno. Acción: capturar parámetros.'),
       ('listo-informe', 'Listo para generar informe', '#EDE9FE', '#5B21B6', 'Parámetros capturados. Acción: generar el informe.'),
       ('informe-generado', 'Informe generado', '#DCFCE7', '#166534', 'Informe emitido. Sin acción pendiente.')]
DIR = [
 ('a', 'Actual · el círculo se llena', 'Lo que ya está en EstadoMuestra: mitad, tres cuartos, lleno con palomita.',
  'Ventaja: ya existe y se lee como avance. Riesgo: mitad y tres cuartos casi no se distinguen a 14 px; dice «cuánto falta», no «qué toca».',
  [etapa(1), etapa(2), etapa(3)], False),
 ('b', 'El objeto de cada etapa', 'Matraz (se analiza), portapapeles con palomita (datos completos), documento con sello (informe emitido).',
  'Ventaja: se entiende sin leer. Riesgo alto: el menú ya usa matraz para «Código de ensayo» y documento con palomita para «Informes»; el estatus se confundiría con la sección.',
  [luc('flask-conical'), luc('clipboard-check'), luc('file-badge')], False),
 ('c', 'Insignia con la siguiente acción', 'El mismo círculo y adentro lo que toca: puntos (se trabaja), flecha (toca generar), palomita (terminado).',
  'Ventaja: tres signos interiores muy distintos, no choca con iconos del menú y se extiende a No ingresada (círculo punteado) y Cancelada (prohibido).',
  [C + '<path d="M8 12h.01M12 12h.01M16 12h.01"/>', C + '<path d="M8 12h8"/><path d="m12 8 4 4-4 4"/>', C + '<path d="m8 12 3 3 5-5"/>'], True),
 ('d', 'Pasos del 1 al 3', 'Tres puntos que se llenan: uno, dos, tres. La posición en el proceso, como un indicador de pasos.',
  'Ventaja: el más simple. Riesgo: dice en qué paso va, no qué significa; con No ingresada y Cancelada ya no son tres pasos.',
  [puntos(1), puntos(2), puntos(3)], False)]
datos = []
for v, nom, met, hip, cuerpos, reco in DIR:
    ic = []
    for (k, *_), b in zip(EST, cuerpos):
        s = svg(f'estatus-{k}', b); open(os.path.join(V, f'{k}-{v}.svg'), 'w').write(s); ic.append(s)
    datos.append(dict(v=v, nom=nom, met=met, hip=hip, ic=ic, reco=reco))
EXTRA = {'no-ingresada': svg('estatus-no-ingresada', luc('circle-dashed')), 'cancelada': svg('estatus-cancelada', luc('ban'))}
for k, s in EXTRA.items(): open(os.path.join(V, f'{k}-c.svg'), 'w').write(s)
json.dump(datos, open(os.path.join(D, 'variantes.json'), 'w'), ensure_ascii=False, indent=1)
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const D=' + json.dumps(datos, ensure_ascii=False) + ';const E=' + json.dumps(EST, ensure_ascii=False) + ';const X=' + json.dumps(EXTRA) + ';')
open(os.path.join(D, 'revision.html'), 'w').write(html); print('ok', len(datos))
