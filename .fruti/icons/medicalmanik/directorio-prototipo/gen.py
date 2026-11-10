# Directorio Manik · prototipo navegable (2026-11-04). Sistema: directorio-ds (tokens, componentes, avatares).
# Ficha: anatomía aprobada (ficha-medico/r03 opción C). Inicio: aprobado (inicio/r03). Perfil: aprobado (perfil-medico/r03). Cita confirmada: aprobada (cita-confirmada/r01). Detalle de su cita: aprobado (detalle-cita/r01). Flujo de agendar: propuesta sin aprobar.
# Uso: python3 gen.py → prototipo.html (iconos Lucide y SVG de marca en línea; datos de ejemplo)
import os, re, json, base64
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
L = '/root/.cache/fruti-uva/package/icons/'
NOMBRES = ['search', 'map-pin', 'calendar-check', 'phone', 'badge-check', 'x', 'arrow-left', 'arrow-right', 'sliders-horizontal', 'scan-face', 'brain', 'apple',
           'flower-2', 'baby', 'stethoscope', 'message-circle-heart', 'shield-check', 'clock', 'circle-check', 'copy', 'bell', 'chevron-right', 'locate-fixed', 'menu']
ICONS = {n: ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse|polygon)[^>]*/>', open(L + n + '.svg').read())) for n in NOMBRES}
uri = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
def avatar(p):
    # Paleta «Mi Médico Manik» (2026-11-10): degradado avatar-inicio → luz-calida, silueta en tinta al 28 %.
    s = open(os.path.join(M, p)).read().replace('#CDEEF2', '#9FE3EC').replace('#FBE7C9', '#F5C9A6')
    a = s.index('/>', s.index('<rect')) + 2; b = s.rfind('<path', 0, s.index('#E9F3F3'))
    sil = re.sub(r' fill="#(93AAB9|7F97A7)"', '', s[a:b])
    s = s[:a] + '<g fill="#14213D" opacity=".28">' + sil + '</g>' + s[b:]
    return 'data:image/svg+xml;base64,' + base64.b64encode(s.encode()).decode()
IMG = {'logo': uri('manik-final/svg/logotipo.svg'), 'logoB': uri('manik-final/svg/logotipo-blanco.svg'),
       'mujer': avatar('directorio-ds/avatares/avatar-mujer.svg'), 'hombre': avatar('directorio-ds/avatares/avatar-hombre.svg'), 'neutro': avatar('directorio-ds/avatares/avatar-neutro.svg')}
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const ICONS=' + json.dumps(ICONS) + ';const IMG=' + json.dumps(IMG) + ';')
open(os.path.join(D, 'prototipo.html'), 'w').write(html); print('ok', len(html) // 1024, 'KB')
