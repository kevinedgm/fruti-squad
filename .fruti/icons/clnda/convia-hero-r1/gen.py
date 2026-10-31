# Convia · hero del directorio, ronda 1: tres direcciones (A convite de estrellas · B portal de arcos · C ventana del día).
# Pedido del usuario (2026-10-31): un hero art moderno, único, que «enmarque». Trazo de plumón de la familia de íconos (iconos.ln).
# Uso: python3 gen.py <carpeta de salida>. Sin fotos.
import os, re, json, sys, math, random
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
sys.path.insert(0, F)
from iconos import ln, circ, arcpts, rr
T = json.load(open(os.path.join(F, 'tema.json'))); CAT = T['categorias']; C = T['color']
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls): s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
LOGO = raw('svg/logotipo.svg').replace('<svg ', '<svg class="logo" ', 1)
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
ICO = {k: clean(raw(f'iconos/{k}.svg'), 'ico') for k in CAT}
ORDEN = ['cafes', 'restaurantes', 'hoteles', 'museos', 'talleres', 'recorridos']
NOM = {'cafes': 'Cafés', 'restaurantes': 'Restaurantes', 'hoteles': 'Hoteles', 'museos': 'Museos', 'talleres': 'Talleres', 'recorridos': 'Recorridos'}
def star(x, y, s, fill='none', stroke='none', sw=0, rot=0, cls=''):
    return (f'<g class="{cls}" transform="translate({x} {y}) rotate({rot}) scale({s/200:.4f}) translate(-100 -100)">'
            f'<path d="{STAR}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/></g>')
# ---------- A · convite de estrellas
pos = [(118, 300, 64, -14), (210, 352, 54, 10), (318, 362, 60, -6), (420, 320, 52, 14), (470, 222, 48, -10), (88, 190, 46, 8)]
A_svg = ('<svg class="hA-art" viewBox="0 0 560 440" aria-hidden="true">'
         + ''.join(f'<circle cx="{random.Random(i).uniform(20,540):.0f}" cy="{random.Random(i+50).uniform(20,420):.0f}" r="{random.Random(i+9).uniform(1.5,3.5):.1f}" fill="#f9f9f7" opacity=".25"/>' for i in range(26))
         + '<path d="M70 330 C160 400 360 410 470 320" fill="none" stroke="#f9f9f7" stroke-opacity=".28" stroke-width="2" stroke-dasharray="2 9" stroke-linecap="round"/>'
         + star(290, 190, 300, stroke='#f9f9f7', sw=5, rot=-8, cls='big')
         + ''.join(f'<g class="fl f{i}">{star(x, y, s, fill=CAT[k]["punto"], rot=r)}</g>' for i, (k, (x, y, s, r)) in enumerate(zip(ORDEN, pos)))
         + '</svg>')
# ---------- B · portal de arcos (cada arco es un botón de giro)
def arco(k, i):
    w, h = 150, 210
    pts = [(10, 205)] + arcpts(75, 75, 65, 180, 360, 20) + [(140, 205)]
    inner = [(26, 205)] + arcpts(75, 75, 49, 180, 360, 18) + [(124, 205)]
    c = CAT[k]
    return (f'<a class="arco" href="#" data-demo style="--f:{c["fondo"]};--t:{c["texto"]};--p:{c["punto"]}"><svg viewBox="0 0 {w} {h}" aria-hidden="true">'
            f'<path class="fondo" d="M26 205 L26 75 A49 49 0 0 1 124 75 L124 205 Z"/>'
            f'<g fill="none" stroke="#2f5a45" stroke-linecap="round" stroke-linejoin="round">{ln(pts, 100 + i, w=7)}{ln(inner, 120 + i, w=3)}'
            f'{ln([(4, 205), (146, 205)], 140 + i, w=6)}{ln([(60, 12), (75, 4), (90, 12)], 160 + i, w=4)}</g></svg>'
            f'<span class="arco-i">{ICO[k]}</span><span class="arco-n">{NOM[k]}</span></a>')
B_arcos = ''.join(arco(k, i) for i, k in enumerate(ORDEN))
# ---------- C · ventana del día (calle ilustrada; cielo según la hora)
def fachada(x, w, h, col, i):
    y0 = 300 - h; r = random.Random(i)
    s = f'<rect x="{x}" y="{y0}" width="{w}" height="{h}" fill="{col}"/>'
    lines = ln([(x, y0), (x + w, y0)], 200 + i, w=4) + ln([(x, y0 + 8), (x + w, y0 + 8)], 220 + i, w=2)
    # puerta en arco y ventanas con balcón
    dx = x + w / 2
    s += f'<path d="M{dx-16} 300 V{280-34} A16 16 0 0 1 {dx+16} {280-34} V300 Z" fill="#2f5a45" opacity=".85"/>'
    for j in range(2 if w > 90 else 1):
        wx = x + (w / 4 if w > 90 else w / 2) + j * w / 2 - 11; wy = y0 + 26
        s += f'<rect x="{wx}" y="{wy}" width="22" height="30" rx="11" fill="#1b1d1a" opacity=".55" class="win"/>'
        lines += ln([(wx - 6, wy + 34), (wx + 28, wy + 34)], 240 + i * 3 + j, w=3) + ''.join(ln([(wx - 4 + q * 8, wy + 34), (wx - 4 + q * 8, wy + 44)], 260 + i * 9 + j * 4 + q, w=2) for q in range(5))
    return s, lines
cols = ['#f6e9ce', '#f4e0d4', '#dae4ec', '#e6dce5', '#f0dcdf', '#d8ebdf', '#f6e9ce']
xs = [0, 120, 230, 360, 470, 600, 720]; ws = [120, 110, 130, 110, 130, 120, 80]; hs = [150, 128, 160, 120, 150, 132, 140]
fach = [fachada(x, w, h, c, i) for i, (x, w, h, c) in enumerate(zip(xs, ws, hs, cols))]
banderas = ''.join(f'<path d="M{60 + i*115} 40 l20 0 l-2 26 l-8 -6 l-8 6 z" transform="rotate({random.Random(i).uniform(-6,6):.1f} {70+i*115} 40)" fill="{CAT[k]["punto"]}"/>' for i, k in enumerate(ORDEN + ORDEN[:1]))
C_svg = ('<svg class="hC-art" viewBox="0 0 800 330" preserveAspectRatio="xMidYMax slice" aria-hidden="true">'
         '<defs><linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1"><stop class="c1" offset="0"/><stop class="c2" offset="1"/></linearGradient></defs>'
         '<rect width="800" height="330" fill="url(#cielo)"/><circle class="astro" cx="640" cy="95" r="34"/>'
         '<path d="M0 230 C120 170 220 200 330 160 C430 125 520 190 640 165 C720 150 770 170 800 160 V330 H0 Z" class="cerro"/>'
         '<path d="M0 34 C200 60 600 60 800 34" fill="none" stroke="#1b1d1a" stroke-opacity=".5" stroke-width="1.5"/>' + banderas
         + ''.join(f[0] for f in fach) + '<g fill="none" stroke="#2f5a45" stroke-linecap="round" stroke-linejoin="round">' + ''.join(f[1] for f in fach) + '</g>'
         '<rect y="300" width="800" height="30" fill="#e6e2d8"/>' + '</svg>')
html = open(os.path.join(D, 'plantilla.html')).read()
rep = {'<!--LOGO-->': LOGO, '<!--A_SVG-->': A_svg, '<!--B_ARCOS-->': B_arcos, '<!--C_SVG-->': C_svg, '%STAR%': STAR, '%cantera%': C['cantera'], '%suave%': C['cantera_suave']}
for k, v in rep.items(): html = html.replace(k, v)
html = html.replace('/*ICO*/', 'const ICO=' + json.dumps({k: ICO[k] for k in ORDEN}) + ';const CATS=' + json.dumps({k: dict(n=NOM[k], f=CAT[k]['fondo'], t=CAT[k]['texto'], p=CAT[k]['punto']) for k in ORDEN}, ensure_ascii=False) + ';')
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
