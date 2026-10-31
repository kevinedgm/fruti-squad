# Uva · indicador único «fuera de rango» r2 (captura de signos vitales, Expediente Manik).
# Pedido del usuario (2026-10-31): ninguna de r1 (banda, medidor, escala); «algo menos complejo, más simple».
# Un solo SVG; el contenedor pone --uva-alto:1 · --uva-bajo:1 · --uva-normal:1 y el color con --uva-accent. Trazo 2.
import os, json
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, 'variantes'); os.makedirs(V, exist_ok=True)
ID = 'out-of-range'
AC = 'stroke:var(--uva-accent,currentColor)'
on = lambda k, f=False: f'opacity:var(--uva-{k},0);{AC}' + (';fill:var(--uva-accent,currentColor)' if f else '')
VAR = {
 'a': ('Flecha', 'Solo una flecha: arriba alto, abajo bajo; un guion cuando está en rango. Lo que usan los reportes de laboratorio.', False,
   '<path class="uva-{i}__alto" d="M12 19V5M6 11l6-6 6 6"/><path class="uva-{i}__bajo" d="M12 5v14M6 13l6 6 6-6"/><path class="uva-{i}__normal" d="M7 12h10"/>'),
 'b': ('Triángulo', 'Un triángulo relleno hacia arriba o hacia abajo, como en los monitores de signos. Se ve aun a 12 px.', True,
   '<path class="uva-{i}__alto" d="M12 6.5 18.5 17h-13z"/><path class="uva-{i}__bajo" d="M12 17.5 18.5 7h-13z"/><circle class="uva-{i}__normal" cx="12" cy="12" r="2.5"/>'),
 'c': ('Chevrón', 'El trazo mínimo: un ángulo arriba o abajo. El más discreto; a 16 px pesa poco.', False,
   '<path class="uva-{i}__alto" d="m6 15 6-6 6 6"/><path class="uva-{i}__bajo" d="m6 9 6 6 6-6"/><path class="uva-{i}__normal" d="M7 12h10"/>'),
 'd': ('Flecha en círculo', 'La flecha dentro de un círculo: se lee como «señal», no como acción, y el círculo se rellena suave con el color del estado.', False,
   '<circle class="uva-{i}__fondo" cx="12" cy="12" r="9.5"/><path class="uva-{i}__alto" d="M12 16.5v-9M8 11.5l4-4 4 4"/><path class="uva-{i}__bajo" d="M12 7.5v9M8 12.5l4 4 4-4"/><path class="uva-{i}__normal" d="M8.5 12h7"/>'),
}
def svg(v):
    n, h, fill, body = VAR[v]
    st = f'.uva-{ID}{{stroke-width:var(--uva-stroke,2)}}' + ''.join(f'.uva-{ID}__{k}{{{on(k, fill)}}}' for k in ('alto', 'bajo', 'normal'))
    if v == 'd': st += f'.uva-{ID}__fondo{{{AC};fill:var(--uva-accent,currentColor);fill-opacity:.12}}'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            f'class="uva-icon uva-{ID}" aria-hidden="true" focusable="false"><style>{st}</style>{body.replace("{i}", ID)}</svg>')
datos = []
for v, (n, h, _, _) in VAR.items():
    s = svg(v); open(os.path.join(V, f'{ID}-{v}.svg'), 'w').write(s); datos.append(dict(v=v, n=n, h=h, svg=s))
json.dump(datos, open(os.path.join(D, 'variantes.json'), 'w'), ensure_ascii=False, indent=1)
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const V=' + json.dumps(datos, ensure_ascii=False) + ';')
open(os.path.join(D, 'revision.html'), 'w').write(html); print('ok')
