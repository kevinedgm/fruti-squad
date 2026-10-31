# Uva · indicadores de signos vitales (captura de signos en Expediente Manik) r1.
# Pedido del usuario (2026-10-31): icono por signo vital que muestre si el valor está alto o bajo; el color del indicador se controla con CSS.
# Un SVG por signo con las piezas «alto», «bajo» (y «normal» en el estilo C) ocultas; el contenedor elige el estado con variables:
#   --uva-alto:1 · --uva-bajo:1 · --uva-normal:1 (solo C) y el color con --uva-accent. Trazo 2 (Lucide de las apps Manik).
# Tres estilos de indicador: A flecha, B triángulo, C nivel. Uso: python3 gen.py → variantes/<id>-<estilo>.svg, revision.html
import os, json
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, 'variantes'); os.makedirs(V, exist_ok=True)
GLIFOS = {  # glifo base a la izquierda (x 2–16); la esquina superior derecha queda libre para el indicador
 'vital-temperature': ('Temperatura', '<path d="M11 4v10.5a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0z"/><path d="M9 10v6"/>'),
 'vital-blood-pressure': ('Presión arterial', '<circle cx="9" cy="13" r="7"/><path d="m9 13 3.3-3.3"/><path d="M4.6 13h1.1M9 8.1v1.1M13.4 13h-1.1"/>'),
 'vital-heart-rate': ('Frecuencia cardiaca', '<path d="M9 19.5s-6.5-4-6.5-9a3.6 3.6 0 0 1 6.5-2.2 3.6 3.6 0 0 1 6.5 2.2c0 5-6.5 9-6.5 9z"/>'),
 'vital-respiratory-rate': ('Frecuencia respiratoria', '<path d="M9 3v5.5M9 8.5l-2 2M9 8.5l2 2"/><path d="M6 8.5c-2 1-3.5 3.7-3.5 7.5 0 2.3 1 3.5 2.5 3.5 1.7 0 2.5-1.3 2.5-3.5v-4"/><path d="M12 8.5c2 1 3.5 3.7 3.5 7.5 0 2.3-1 3.5-2.5 3.5-1.7 0-2.5-1.3-2.5-3.5v-4"/>'),
 'vital-spo2': ('Saturación de oxígeno (SpO₂)', '<rect x="4" y="3.5" width="10" height="8.5" rx="2.5"/><path d="M7.5 7.5h3"/><path d="M7 12v9M11 12v9"/>'),
}
ESTILOS = {
 'a': ('Flecha', 'Arriba o abajo: la lectura más directa de «alto» y «bajo».',
       lambda i: f'<path class="uva-{i}__alto" d="M19.5 10V3M17 5.5 19.5 3 22 5.5"/><path class="uva-{i}__bajo" d="M19.5 3v7M17 7.5l2.5 2.5L22 7.5"/>', False),
 'b': ('Triángulo', 'Un triángulo relleno: más peso a tamaños chicos y se lee como «nivel». Riesgo: parece un botón de reproducir o desplegar.',
       lambda i: f'<path class="uva-{i}__alto" d="M19.5 3.5 22 8h-5z"/><path class="uva-{i}__bajo" d="M19.5 8.5 22 4h-5z"/>', True),
 'c': ('Nivel', 'Un riel con un punto arriba, en medio o abajo: muestra también el «normal». Riesgo: a 16 px el riel casi no se ve.',
       lambda i: f'<path class="uva-{i}__riel" d="M19.5 4.5v14"/><circle class="uva-{i}__alto" cx="19.5" cy="5" r="1.8"/><circle class="uva-{i}__normal" cx="19.5" cy="11.75" r="1.8"/><circle class="uva-{i}__bajo" cx="19.5" cy="18.5" r="1.8"/>', True),
}
def svg(i, e):
    nombre, est, piezas, relleno = ESTILOS[e]
    fill = 'fill:var(--uva-accent,currentColor);' if relleno else ''
    css = (f'.uva-{i}{{stroke-width:var(--uva-stroke,2)}}'
           f'.uva-{i}__alto{{opacity:var(--uva-alto,0);stroke:var(--uva-accent,currentColor);{fill}}}'
           f'.uva-{i}__bajo{{opacity:var(--uva-bajo,0);stroke:var(--uva-accent,currentColor);{fill}}}')
    if e == 'c':
        css += (f'.uva-{i}__normal{{opacity:var(--uva-normal,0);stroke:var(--uva-accent,currentColor);{fill}}}'
                f'.uva-{i}__riel{{opacity:var(--uva-riel,.35)}}')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            f'class="uva-icon uva-{i}" aria-hidden="true" focusable="false"><style>{css}</style>{GLIFOS[i][1]}{piezas(i)}</svg>')
datos = []
for i, (n, _) in GLIFOS.items():
    for e in ESTILOS:
        s = svg(i, e); open(os.path.join(V, f'{i}-{e}.svg'), 'w').write(s); datos.append(dict(id=i, n=n, e=e, svg=s))
json.dump(datos, open(os.path.join(D, 'variantes.json'), 'w'), ensure_ascii=False, indent=1)
est = {k: dict(n=v[0], h=v[1]) for k, v in ESTILOS.items()}
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const V=' + json.dumps(datos, ensure_ascii=False) + ';const EST=' + json.dumps(est, ensure_ascii=False) + ';')
open(os.path.join(D, 'revision.html'), 'w').write(html); print('ok', len(datos))
