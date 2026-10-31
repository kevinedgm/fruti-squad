# Ecosistema Manik · panel de usuario r1: el inicio del ecosistema suma «Tu perfil en Manik» (directorio público) y «Tu cuenta».
# Pedido del usuario (2026-10-31): en el panel donde se eligen las apps, el usuario actualiza su cuenta personal y su perfil público
# en el directorio Manik: insignia de Manik, ver cómo luce su perfil, configurar su información y ver si está visible o no.
# Uso: python3 gen.py <salida>. Sellos e insignia como <img> en data URI (los SVG de la familia comparten ids de máscara).
import sys, os, json, base64
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
APPS = [('expediente', 'Expediente', 'Consultas, recetas y expediente clínico'), ('agenda', 'Agenda', 'Citas, confirmaciones y sala de espera'),
        ('farmacia', 'Farmacia', 'Surtido, existencias y caducidades'), ('compras', 'Compras', 'Compras, proveedores y facturación'),
        ('impulsa', 'Impulsa', 'Campañas de prevención y pacientes'), ('grupos', 'Grupos', 'Clínicas, sedes y permisos del grupo')]
DATA = {'apps': [{'id': a, 'n': n, 'q': q, 'img': uri(f'final/svg/{a}.svg')} for a, n, q in APPS],
        'pin': uri('manik-final/svg/simbolo.svg'), 'logo': uri('manik-final/svg/logotipo.svg'),
        'adm': uri('final/svg/administracion.svg'), 'eco': uri('final/svg/ecosistema.svg')}
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const DATA=' + json.dumps(DATA) + ';')
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
