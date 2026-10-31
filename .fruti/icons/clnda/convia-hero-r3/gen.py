# Convia · hero del directorio r3: el LOGO es el protagonista y el doodle (pedido del usuario 2026-10-31).
# Centrado: logo de temporada → frase de temporada → buscador → intenciones como sellos. Fondo discreto (perla + tinte de temporada).
# El nombre «Convia» siempre legible; por temporada cambian la estrella, los adornos alrededor del nombre, el tinte, la frase y el enlace.
# Uso: python3 gen.py <carpeta de salida>.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
T = json.load(open(os.path.join(F, 'tema.json'))); CAT = T['categorias']; C = T['color']
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls): s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
paths = re.findall(r'<path[^>]*/>', raw('svg/logotipo.svg'))
LOGO_TXT = re.sub(r' fill="[^"]*"', '', ''.join(paths[1:]))
ICO = {k: clean(raw(f'iconos/{k}.svg'), 'ico') for k in CAT}
SEL = [('recorridos', 'A dónde ir esta semana'), ('cafes', 'Un café nuevo'), ('restaurantes', 'Dónde comer hoy'), ('talleres', 'Un taller para ir solo'), ('hoteles', 'Dónde dormir')]
SELLOS = ''.join(f'<a class="sello" href="#" data-demo style="--f:{CAT[k]["fondo"]};--t:{CAT[k]["texto"]};--r:{[-6,4,-3,6,-4][i]}deg"><span class="aro" aria-hidden="true"></span>{ICO[k]}<span class="sl">{n}</span></a>' for i, (k, n) in enumerate(SEL))
html = open(os.path.join(D, 'plantilla.html')).read()
for k, v in {'<!--SELLOS-->': SELLOS, '%cantera%': C['cantera'], '%suave%': C['cantera_suave']}.items(): html = html.replace(k, v)
html = html.replace('/*DATA*/', 'const STAR=' + json.dumps(STAR) + ';const LOGO_TXT=' + json.dumps(LOGO_TXT) + ';')
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
