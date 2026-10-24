# Agenda Manik para grupos · Uso: python3 gen.py → agenda-grupos.html
s = open('plantilla.html').read().replace('/*DATA*/', 'const SELLO=' + open('sellos.json').read() + ';')
open('agenda-grupos.html', 'w').write(s); print('ok')
