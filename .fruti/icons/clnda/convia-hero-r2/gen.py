# Convia · hero del directorio r2 = B (portal de arcos, navegación) + C (cielo vivo) + TEMPORADAS tipo doodle.
# Pedido del usuario (2026-10-31): poder tematizar la portada para fechas especiales (Día de Muertos, Guelaguetza…), cambiando fondo y logo.
# Regla: lo fijo (arcos, buscador, intenciones, palabra «Convia») no cambia; cambian cielo, adornos, la ESTRELLA del logo, el texto y el enlace a la agenda.
# Cada temporada es un dato (ver TEMPORADAS en plantilla.html); la portada elige sola según la fecha y, fuera de temporada, usa el cielo según la hora.
# Uso: python3 gen.py <carpeta de salida>. Sin fotos.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
sys.path.insert(0, F)
from iconos import ln, arcpts
T = json.load(open(os.path.join(F, 'tema.json'))); CAT = T['categorias']; C = T['color']
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls): s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
logo = raw('svg/logotipo.svg'); paths = re.findall(r'<path[^>]*/>', logo)
LOGO_TXT = ''.join(paths[1:])  # la palabra «Convia» (la estrella se dibuja aparte, por temporada)
ICO = {k: clean(raw(f'iconos/{k}.svg'), 'ico') for k in CAT}
ORDEN = ['cafes', 'restaurantes', 'hoteles', 'museos', 'agenda']
NOM = {'cafes': 'Cafés', 'restaurantes': 'Restaurantes', 'hoteles': 'Hoteles', 'museos': 'Museos', 'agenda': 'Agenda'}
CAL = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>'
def arco(k, i):
    c = CAT.get(k) or dict(fondo=C['cantera_suave'], texto=C['cantera'], punto=C['cantera'])
    pts = [(10, 205)] + arcpts(75, 75, 65, 180, 360, 20) + [(140, 205)]
    inner = [(26, 205)] + arcpts(75, 75, 49, 180, 360, 18) + [(124, 205)]
    return (f'<a class="arco" href="#" data-demo style="--f:{c["fondo"]};--t:{c["texto"]};--p:{c["punto"]}"><svg viewBox="0 0 150 210" aria-hidden="true">'
            f'<path class="fondo" d="M26 205 L26 75 A49 49 0 0 1 124 75 L124 205 Z"/>'
            f'<g fill="none" class="piedra" stroke-linecap="round" stroke-linejoin="round">{ln(pts, 100 + i, w=7)}{ln(inner, 120 + i, w=3)}'
            f'{ln([(4, 205), (146, 205)], 140 + i, w=6)}{ln([(60, 12), (75, 4), (90, 12)], 160 + i, w=4)}</g></svg>'
            f'<span class="arco-i">{ICO.get(k, CAL)}</span><span class="arco-n">{NOM[k]}</span></a>')
ARCOS = ''.join(arco(k, i) for i, k in enumerate(ORDEN))
html = open(os.path.join(D, 'plantilla.html')).read()
for k, v in {'<!--ARCOS-->': ARCOS, '%cantera%': C['cantera'], '%suave%': C['cantera_suave']}.items(): html = html.replace(k, v)
html = html.replace('/*DATA*/', 'const STAR=' + json.dumps(STAR) + ';const LOGO_TXT=' + json.dumps(LOGO_TXT) + ';const ICO=' + json.dumps({k: ICO[k] for k in ['recorridos', 'cafes', 'restaurantes', 'talleres', 'hoteles']}) + ';')
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
