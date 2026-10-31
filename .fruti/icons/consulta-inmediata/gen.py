# Uva · consulta inmediata (Agenda Manik, botón flotante). Pedido del usuario (2026-10-31).
# Concepto: «ahora, sin cita» (no «urgencia»). Retícula 24, trazo 2 (Lucide de las apps Manik). Uso: python3 gen.py → variantes/*.svg, variantes.json, revision.html
import os, json
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, 'variantes'); os.makedirs(V, exist_ok=True)
ID = 'immediate-consult'
VAR = [
 ('a', 'Calendario con rayo', 'Una cita que ocurre ya: el calendario dice «agenda», el rayo dice «al instante». Riesgo: el rayo también es «energía» o «flash».',
  '<path d="M8 2v3M16 2v3"/><path d="M21 10V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h7"/><path d="M3 9h18"/><path d="M18.5 12 14.5 17.5h4l-1.5 4.5 4.5-6h-4z"/>'),
 ('b', 'Cronómetro con cruz', 'Atención médica medida en minutos: el cronómetro dice «ya», la cruz dice «consulta». Riesgo: puede leerse como «tiempo de espera».',
  '<path d="M10 2h4"/><path d="M12 2v3"/><path d="m19 6.5-1.5 1.5"/><circle cx="12" cy="14" r="8"/><path d="M12 10.5v7M8.5 14h7"/>'),
 ('c', 'Cruz con estela', 'La cruz médica en movimiento: líneas de velocidad a la izquierda. Riesgo: dentro de un botón flotante la cruz puede leerse como «+ agregar».',
  '<path d="M12 4h4.5v4.5H21v4.5h-4.5v4.5H12v-4.5H7.5V8.5H12z"/><path d="M2 8.5h2.5M2 12.75h3M2 17h2.5"/>'),
]
def svg(body): return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
                       f'class="uva-icon uva-{ID}" aria-hidden="true" focusable="false"><style>.uva-{ID}{{stroke-width:var(--uva-stroke,2)}}</style>{body}</svg>')
L = '/root/.cache/fruti-uva/package/icons/'
def lucide(n):
    import re
    s = open(L + n + '.svg').read(); b = ''.join(re.findall(r'<(?:path|circle|rect|line|polyline)[^>]*/>', s))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{b}</svg>'
datos = []
for v, n, h, b in VAR:
    s = svg(b); open(os.path.join(V, f'{ID}-{v}.svg'), 'w').write(s); datos.append(dict(v=v, n=n, h=h, svg=s))
conf = {k: lucide(k) for k in ['plus', 'zap', 'siren', 'calendar-plus', 'timer', 'cross']}
json.dump(datos, open(os.path.join(D, 'variantes.json'), 'w'), ensure_ascii=False, indent=1)
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const V=' + json.dumps(datos, ensure_ascii=False) + ';const CONF=' + json.dumps(conf) + ';')
open(os.path.join(D, 'revision.html'), 'w').write(html); print('ok')
