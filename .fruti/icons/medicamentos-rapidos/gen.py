# Uva · accesos rápidos de medicamentos en la receta (Expediente Manik) r1. Pedido del usuario (2026-11-01):
# 1) reutilizar los medicamentos de la última consulta; 2) medicamentos recomendados asociados a un diagnóstico.
# Pareja: la misma pastilla (arriba a la izquierda) y un modificador abajo a la derecha. Trazo 2. Uso: python3 gen.py
import os, json, math, re
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, 'variantes'); os.makedirs(V, exist_ok=True)
PASTILLA = '<g transform="rotate(-45 9 9)"><rect x="3.5" y="6" width="11" height="6" rx="3"/><path d="M9 6v6"/></g>'
def estrella(cx, cy, R, r):
    p = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5; rr = R if k % 2 == 0 else r
        p.append(f'{cx + rr*math.cos(a):.2f} {cy + rr*math.sin(a):.2f}')
    return 'M' + ' L'.join(p) + 'Z'
I = {
 'repeat-last-medications': ('Repetir de la última consulta', 'Copia los medicamentos de la consulta anterior a la receta de hoy', [
  ('a', 'Pastilla con historial', 'La flecha que gira hacia atrás (historial): «lo de la vez pasada». Lucide la usa para historial y deshacer.',
   PASTILLA + '<path d="M13.5 17.5a4 4 0 1 0 4-4 4.4 4.4 0 0 0-3 1.2L13.5 15.5"/><path d="M13.5 12.5v3h3"/>'),
  ('b', 'Pastilla con flecha de regreso', '«Traer de atrás»: la flecha que vuelve. Riesgo: también se lee como «responder» o «deshacer».',
   PASTILLA + '<path d="M21 21v-1.5a4 4 0 0 0-4-4h-3.5"/><path d="m16 12.5-3 3 3 3"/>'),
  ('c', 'Pastilla con reloj', '«De antes». Riesgo alto: en una receta el reloj se lee como «horario de la dosis».',
   PASTILLA + '<circle cx="17.5" cy="17.5" r="4"/><path d="M17.5 15.5v2l1.5 1"/>')]),
 'diagnosis-medications': ('Recomendados para el diagnóstico', 'Medicamentos asociados al diagnóstico de esta consulta', [
  ('a', 'Pastilla con etiqueta', 'La etiqueta es el diagnóstico (el código CIE-10): la misma etiqueta que usa «Sugerir códigos CIE-10». «Medicamentos de este diagnóstico».',
   PASTILLA + '<path d="M14 14h4.2l3.3 3.3a1.4 1.4 0 0 1 0 2l-2.2 2.2a1.4 1.4 0 0 1-2 0L14 18.2z"/><path d="M16.3 16.3h.01"/>'),
  ('b', 'Pastilla con estrella', '«Recomendado». Riesgo: la estrella también es «favorito» o «calificación».',
   PASTILLA + f'<path d="{estrella(17.5, 17.8, 4.6, 2)}"/>'),
  ('c', 'Pastilla con lista', '«El protocolo»: la lista de medicamentos para ese caso. Riesgo: parece simplemente «receta».',
   PASTILLA + '<path d="M14 15h7M14 18h7M14 21h4.5"/>')]),
}
def svg(i, b): return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
                       f'class="uva-icon uva-{i}" aria-hidden="true" focusable="false"><style>.uva-{i}{{stroke-width:var(--uva-stroke,2)}}</style>{b}</svg>')
datos = []
for i, (n, desc, vs) in I.items():
    for v, met, hip, b in vs:
        s = svg(i, b); open(os.path.join(V, f'{i}-{v}.svg'), 'w').write(s); datos.append(dict(id=i, nom=n, desc=desc, v=v, met=met, hip=hip, svg=s))
json.dump(datos, open(os.path.join(D, 'variantes.json'), 'w'), ensure_ascii=False, indent=1)
L = '/root/.cache/fruti-uva/package/icons/'
def luc(n): return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + ''.join(re.findall(r'<(?:path|circle|rect|line|polyline)[^>]*/>', open(L + n + '.svg').read())) + '</svg>'
ctx = {'Agregar medicamento': luc('plus')}
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const D=' + json.dumps(datos, ensure_ascii=False) + ';const CTX=' + json.dumps(ctx, ensure_ascii=False) + ';')
open(os.path.join(D, 'revision.html'), 'w').write(html); print('ok', len(datos))
