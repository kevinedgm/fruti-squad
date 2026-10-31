# Administración Manik · pantalla principal r1 (resumen). Pedido del usuario (2026-10-31): «sigue con la pantalla principal de administración».
# Brief: equipo MedicalManik; usuarios activos, configuración del sistema; ver qué requiere atención y entrar a configurar.
# Uso: python3 gen.py <salida>. Sellos como <img> data URI. Datos de ejemplo.
import sys, os, json, base64
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
APPS = ['expediente', 'agenda', 'farmacia', 'compras', 'impulsa', 'grupos']
DATA = {'adm': uri('final/svg/administracion.svg'), 'eco': uri('final/svg/ecosistema.svg'), 'pin': uri('manik-final/svg/simbolo.svg'),
        'apps': {a: uri(f'final/svg/{a}.svg') for a in APPS}}
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const DATA=' + json.dumps(DATA) + ';')
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
