# Uva · iconos de sección del expediente r1: «Laboratorio» (colesterol, triglicéridos, HbA1c, glucosa) y «Exploración física»
# (habitus exterior, cabeza, cuello, tórax, abdomen, extremidades…). Pedido del usuario (2026-11-01).
# Misma familia que ../antecedentes: retícula 24, trazo 2, formas simples. Uso: python3 gen.py → variantes/*.svg, variantes.json, revision.html
import os, json, re
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, 'variantes'); os.makedirs(V, exist_ok=True)
I = {
 'lab-results': ('Laboratorio', 'Colesterol, triglicéridos, HbA1c, glucosa', [
  ('a', 'Tubo de muestra', 'El tubo con tapón y nivel de muestra: «estudio de sangre». Es lo que usan las apps clínicas para laboratorio.',
   '<rect x="8" y="2" width="8" height="3.5" rx="1"/><path d="M9 5.5V19a3 3 0 0 0 6 0V5.5"/><path d="M9 13h6"/>'),
  ('b', 'Hoja de resultados con gota', 'El reporte de laboratorio de sangre. Riesgo: la gota sola ya significa «glucosa» en otros iconos.',
   '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M12 11c1.6 1.9 2.5 3.2 2.5 4.5a2.5 2.5 0 0 1-5 0c0-1.3.9-2.6 2.5-4.5z"/>'),
  ('c', 'Dos tubos (Lucide)', 'Referencia de Lucide: se lee «laboratorio», pero de química más que clínico.',
   '<path d="M9 2v17.5A2.5 2.5 0 0 1 6.5 22 2.5 2.5 0 0 1 4 19.5V2"/><path d="M20 2v17.5a2.5 2.5 0 0 1-2.5 2.5 2.5 2.5 0 0 1-2.5-2.5V2"/><path d="M3 2h7M14 2h7"/><path d="M9 16H4M20 16h-5"/>')]),
 'physical-exam': ('Exploración física', 'Habitus exterior, cabeza, cuello, tórax, abdomen, extremidades', [
  ('a', 'Cuerpo en encuadre', 'El cuerpo completo dentro de las esquinas de revisión: «se examina el cuerpo por regiones». Distinto del busto de los antecedentes personales.',
   '<path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/><circle cx="12" cy="7.5" r="1.5"/><path d="M8.5 11 12 12l3.5-1"/><path d="M12 12v2.5"/><path d="m9.5 18 2.5-3.5 2.5 3.5"/>'),
  ('b', 'Cuerpo de frente', 'La figura humana completa, sin marco. Riesgo: se parece al icono de «accesibilidad» o «persona».',
   '<circle cx="12" cy="4.5" r="2"/><path d="M6 9.5l6 1.5 6-1.5"/><path d="M12 11v4.5"/><path d="m8.5 21 3.5-5.5 3.5 5.5"/>'),
  ('c', 'Estetoscopio (Lucide)', 'Referencia de Lucide: muy médico, pero significa «consulta» en general; no distingue la exploración.',
   '<path d="M11 2v2M5 2v2"/><path d="M5 3H4a2 2 0 0 0-2 2v4a6 6 0 0 0 12 0V5a2 2 0 0 0-2-2h-1"/><path d="M8 15a6 6 0 0 0 12 0v-3"/><circle cx="20" cy="10" r="2"/>')]),
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
ant = json.load(open(os.path.join(D, '..', 'antecedentes', 'variantes.json')))
ctx = {'Antecedentes': [x['svg'] for x in ant if x['id'] == 'pathological-history' and x['v'] == 'a'][0], 'Signos vitales': luc('activity')}
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const D=' + json.dumps(datos, ensure_ascii=False) + ';const CTX=' + json.dumps(ctx, ensure_ascii=False) + ';')
open(os.path.join(D, 'revision.html'), 'w').write(html); print('ok', len(datos))
