# Directorio Manik · prototipo navegable (2026-11-04). Sistema: directorio-ds (tokens, componentes, avatares).
# Ficha: anatomía aprobada (ficha-medico/r03 opción C). Inicio: aprobado (inicio/r03). Flujo de agendar: propuesta sin aprobar.
# Uso: python3 gen.py → prototipo.html (iconos Lucide y SVG de marca en línea; datos de ejemplo)
import os, re, json, base64
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
L = '/root/.cache/fruti-uva/package/icons/'
NOMBRES = ['search', 'map-pin', 'calendar-check', 'phone', 'badge-check', 'x', 'arrow-left', 'arrow-right', 'sliders-horizontal', 'scan-face', 'brain', 'apple',
           'flower-2', 'baby', 'stethoscope', 'message-circle-heart', 'shield-check', 'clock', 'circle-check', 'copy', 'bell', 'chevron-right', 'locate-fixed', 'menu']
ICONS = {n: ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse|polygon)[^>]*/>', open(L + n + '.svg').read())) for n in NOMBRES}
uri = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
IMG = {'logo': uri('manik-final/svg/logotipo.svg'), 'logoB': uri('manik-final/svg/logotipo-blanco.svg'),
       'mujer': uri('directorio-ds/avatares/avatar-mujer.svg'), 'hombre': uri('directorio-ds/avatares/avatar-hombre.svg'), 'neutro': uri('directorio-ds/avatares/avatar-neutro.svg')}
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const ICONS=' + json.dumps(ICONS) + ';const IMG=' + json.dumps(IMG) + ';')
open(os.path.join(D, 'prototipo.html'), 'w').write(html); print('ok', len(html) // 1024, 'KB')
