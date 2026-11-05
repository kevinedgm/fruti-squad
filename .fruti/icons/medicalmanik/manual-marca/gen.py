# MedicalManik · manual de identidad 2026 (reemplaza el «Manual de identidad» anterior en PDF, 22 págs.).
# Pedido del usuario (2026-10-31): seguir la estructura del manual anterior y documentar toda la marca con sus productos.
# Uso: python3 gen.py <salida>  → <salida>/manual.html (sin skeleton: lo agrega la publicación). Imágenes como data URI.
import sys, os, base64
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
def uri(p): return ('data:image/png;base64,' if p.endswith('.png') else 'data:image/svg+xml;base64,') + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()  # PNG o SVG
A = {
 'LOGO': 'final/svg/medicalmanik-logotipo.svg', 'LOGOB': 'final/svg/medicalmanik-logotipo-blanco.svg', 'SELLO': 'final/svg/medicalmanik.svg',
 'SELLO1': 'final/svg/medicalmanik-1tinta.svg', 'ECO': 'final/svg/ecosistema.svg',
 'EXP': 'final/svg/expediente.svg', 'AGE': 'final/svg/agenda.svg', 'COM': 'final/svg/compras.svg', 'FAR': 'final/svg/farmacia.svg',
 'IMP': 'final/svg/impulsa.svg', 'GRU': 'final/svg/grupos.svg', 'ADM': 'final/svg/administracion.svg',
 'PIN': 'manik-final/svg/simbolo.svg', 'C1': 'manual-marca/img/correo-bienvenida.png', 'C2': 'manual-marca/img/correo-cita-confirmada.png', 'C3': 'manual-marca/img/correo-factura.png', 'MANIK': 'manik-final/svg/logotipo.svg', 'MANIKEND': 'manik-final/svg/logotipo-endoso.svg', 'B_EXP': 'sellos-b-r01/svg/expediente.svg', 'B_AGE': 'sellos-b-r01/svg/agenda.svg', 'B_COM': 'sellos-b-r01/svg/compras.svg', 'B_FAR': 'sellos-b-r01/svg/farmacia.svg', 'B_IMP': 'sellos-b-r01/svg/impulsa.svg', 'B_GRU': 'sellos-b-r01/svg/grupos.svg', 'B_ADM': 'sellos-b-r01/svg/administracion.svg'}
html = open(os.path.join(D, 'plantilla.html')).read()
import superficies  # sección generada desde los tokens de cada sistema de diseño
html = html.replace('{{SFCSS}}', superficies.CSS).replace('{{SUPERFICIES}}', superficies.HTML)
for k, p in A.items(): html = html.replace('{{' + k + '}}', uri(p))
assert '{{' not in html, html[html.index('{{'):html.index('{{') + 30]
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'manual.html'), 'w').write(html); print('ok', len(html))
