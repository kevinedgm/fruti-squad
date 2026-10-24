# Consulta de Expediente Manik · Uso: python3 gen.py → consulta.html
s = open('plantilla.html').read().replace('/*DATA*/', 'const SELLO=' + open('sellos.json').read() + ';')
open('consulta.html', 'w').write(s); print('ok')
