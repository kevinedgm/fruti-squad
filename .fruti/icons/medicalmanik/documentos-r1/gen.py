# Expediente Manik · documentos para el paciente r1: «Estado de salud» (al terminar la consulta) y «Resumen clínico» (a solicitud).
# Pedido del usuario (2026-10-31): plantilla tipo hoja membretada; el médico es el protagonista; Expediente Manik muy discreto en logo y color.
# Uso: python3 gen.py <salida> → index.html. Iconos de antecedentes (variantes recomendadas de ../../antecedentes) y sello en data URI. Datos ficticios.
import sys, os, json, base64
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
ANT = json.load(open(os.path.join(M, '..', 'antecedentes', 'variantes.json')))
RECO = {'allergies': 'b', 'non-pathological-history': 'a', 'pathological-history': 'a', 'surgeries': 'c', 'vaccines': 'b', 'family-history': 'a', 'gyneco-obstetric-history': 'a', 'perinatal-history': 'b'}
ICON = {x['id']: x['svg'] for x in ANT if RECO.get(x['id']) == x['v']}
sello = 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, 'final', 'svg', 'expediente-1tinta.svg'), 'rb').read()).decode()
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const ICON=' + json.dumps(ICON) + ';const SELLO=' + json.dumps(sello) + ';')
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
