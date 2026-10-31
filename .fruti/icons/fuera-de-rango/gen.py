# Uva · indicador único «fuera de rango» para la captura de signos vitales (Expediente Manik) r1.
# Pedido del usuario (2026-10-31): un solo icono indicador que se adapte a todos los signos (temperatura, presión, FC, FR, SpO₂…)
# para decir «fuera de rango», alto o bajo; color controlado con CSS. Sustituye el enfoque de un icono por signo (../signos-vitales).
# El contenedor elige el estado con --uva-alto:1 · --uva-bajo:1 · --uva-normal:1 y el color con --uva-accent. Trazo 2.
import os, json
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, 'variantes'); os.makedirs(V, exist_ok=True)
ID = 'out-of-range'
on = lambda k: f'opacity:var(--uva-{k},0)'
off = lambda k: f'opacity:calc(1 - var(--uva-{k},0))'
AC = 'stroke:var(--uva-accent,currentColor)'
VAR = {
 'a': ('Banda con flecha que sale', 'Dos líneas marcan el rango normal; la flecha lo atraviesa hacia arriba (alto) o hacia abajo (bajo) y la línea que cruza se abre. Dice «salió del rango» y hacia dónde.',
   {'sup': f'{off("alto")}', 'supr': f'{on("alto")}', 'inf': f'{off("bajo")}', 'infr': f'{on("bajo")}',
    'alto': f'{on("alto")};{AC}', 'bajo': f'{on("bajo")};{AC}', 'normal': f'{on("normal")};{AC};fill:var(--uva-accent,currentColor)'},
   '<path class="uva-{i}__sup" d="M3 9h18"/><path class="uva-{i}__supr" d="M3 9h5.5M15.5 9H21"/><path class="uva-{i}__inf" d="M3 15h18"/><path class="uva-{i}__infr" d="M3 15h5.5M15.5 15H21"/>'
   '<path class="uva-{i}__alto" d="M12 13V3M8.5 6.5 12 3l3.5 3.5"/><path class="uva-{i}__bajo" d="M12 11v10M8.5 17.5 12 21l3.5-3.5"/><circle class="uva-{i}__normal" cx="12" cy="12" r="1.5"/>'),
 'b': ('Medidor', 'Un medidor de aguja: hacia la derecha alto, hacia la izquierda bajo, al centro normal. Riesgo: izquierda/derecha se lee menos rápido que arriba/abajo, y parece velocímetro.',
   {'alto': f'{on("alto")};{AC}', 'bajo': f'{on("bajo")};{AC}', 'normal': f'{on("normal")};{AC}'},
   '<path d="M3.5 17a8.5 8.5 0 0 1 17 0"/><path d="M5.2 11.5l1.4 1M18.8 11.5l-1.4 1"/><path class="uva-{i}__alto" d="M12 17l7-3.5"/><path class="uva-{i}__bajo" d="M12 17 5 13.5"/><path class="uva-{i}__normal" d="M12 17V10"/><path d="M12 17h.01"/>'),
 'c': ('Escala con punto fuera', 'Una caja es el rango normal; el punto queda dentro (normal), arriba (alto) o abajo (bajo). Se lee como «la medida cayó fuera de la caja».',
   {'alto': f'{on("alto")};{AC};fill:var(--uva-accent,currentColor)', 'bajo': f'{on("bajo")};{AC};fill:var(--uva-accent,currentColor)', 'normal': f'{on("normal")};{AC};fill:var(--uva-accent,currentColor)'},
   '<rect x="8.5" y="8" width="7" height="8" rx="2"/><path d="M12 2.5v2M12 19.5v2"/><circle class="uva-{i}__alto" cx="12" cy="3.5" r="1.6"/><circle class="uva-{i}__normal" cx="12" cy="12" r="1.6"/><circle class="uva-{i}__bajo" cx="12" cy="20.5" r="1.6"/>'),
}
def svg(v):
    n, h, css, body = VAR[v]
    st = f'.uva-{ID}{{stroke-width:var(--uva-stroke,2)}}' + ''.join(f'.uva-{ID}__{k}{{{x}}}' for k, x in css.items())
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            f'class="uva-icon uva-{ID}" aria-hidden="true" focusable="false"><style>{st}</style>{body.replace("{i}", ID)}</svg>')
datos = []
for v, (n, h, _, _) in VAR.items():
    s = svg(v); open(os.path.join(V, f'{ID}-{v}.svg'), 'w').write(s); datos.append(dict(v=v, n=n, h=h, svg=s))
json.dump(datos, open(os.path.join(D, 'variantes.json'), 'w'), ensure_ascii=False, indent=1)
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const V=' + json.dumps(datos, ensure_ascii=False) + ';')
open(os.path.join(D, 'revision.html'), 'w').write(html); print('ok')
