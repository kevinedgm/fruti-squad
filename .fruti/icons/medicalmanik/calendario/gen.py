# Agenda semanal de Expediente Manik · Uso: python3 gen.py → agenda.html
import json
s = open('plantilla.html').read().replace('/*DATA*/', 'const SELLO=' + open('sellos.json').read() + ';')
open('agenda.html', 'w').write(s); print('ok')
