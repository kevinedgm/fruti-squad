import xml.dom.minidom as m
ps = open('paths.txt').read().split('\n')
PA, PB = ps
GAP = open('gap.d').read()
CX, CY, R = 265.97, 226.1, 136.1
W = 19.3
core = [(173.5,251.2),(182.5,250.0),(186.2,244.8),(190.0,236.2),(202.5,186.2),(206.5,174.2),(212.0,165.2),(219.2,158.5),(224.8,163.5),(228.2,168.0),(233.0,178.2),(249.5,256.5),(252.2,266.0),(257.5,275.5),(265.2,282.8),(274.2,274.2),(279.8,264.5),(298.8,206.2),(302.0,198.5),(308.8,189.0),(315.5,183.5),(322.8,189.8),(329.0,199.5),(343.8,248.0),(346.0,253.2),(348.8,254.8),(357.8,257.0)]
logo_line = [(115,251.2)] + core + [(417,257.0)]
def pts(l): return ' '.join('%.1f,%.1f' % p for p in l)

COL = 'var(--manik-color,#6e6eb5)'
BGC = 'var(--manik-bg,#fff)'
LN = 'fill:none;stroke-width:%s;stroke-linecap:round;stroke-linejoin:round' % W
RESPIRA = '@keyframes manik-respira{from{opacity:1}to{opacity:.55}}'
# Exact gap (vectorized from the logo) + baseline bands that run past the circle edge
HUECO = '<path d="%s"/><rect x="120" y="237.5" width="22" height="27.5"/><rect x="390" y="249.25" width="20" height="15.75"/>' % GAP
BURBUJA = '<circle cx="%s" cy="%s" r="%s"/>%s' % (CX, CY, R, PB)

def svg(cls, vb, body, css, desc):
    import re
    css = re.sub(r'(?<![\w-])\.(b|t|k|mv|a|z|g)(?=[{,.\s])', lambda mm: '.manik-loader--%s .%s' % (cls, mm.group(1)), css)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" aria-hidden="true" focusable="false" class="manik-loader manik-loader--%s">\n'
            '  <!-- Manik Impulsa · loader «%s»: %s -->\n'
            '  <style>%s%s</style>\n%s\n</svg>\n') % (vb, cls, cls, desc, css, RESPIRA, body)

out = {}
# ---------- 1 MONITOR ----------
import math
P = 400
LW = 9  # thin signal outside the bubble
def chaikin(p, n=3):
    for _ in range(n):
        q = [p[0]]
        for (x0, y0), (x1, y1) in zip(p, p[1:]):
            q += [(.75*x0+.25*x1, .75*y0+.25*y1), (.25*x0+.75*x1, .25*y0+.75*y1)]
        q.append(p[-1]); p = q
    return p
def ease(x0, x1, y0, y1, n=14):
    return [(x0+(x1-x0)*i/n, y0+(y1-y0)*(1-math.cos(math.pi*i/n))/2) for i in range(n+1)]
# centre line of one period: M, then a smooth return from the right baseline (257.2) to the left one (251.25)
linea = []
for k in range(-1, 3):
    o = k * P
    linea += [(x+o, y) for x, y in chaikin(core, 1)]
    linea += [(x+o, y) for x, y in ease(410, 520, 257.2, 251.25)]
linea = [(-300, 251.25)] + linea + [(1300, 257.2)]
# inside the bubble: exact gap of the logo + smooth band between copies (top edge eases 249.25 -> 237.38)
def tramo(k):
    o = k * P
    top = ease(405, 520, 249.25, 237.38)
    pg = [(x+o, y) for x, y in top] + [(125+P+o, 237.38), (125+P+o, 265.12), (405+o, 265.12)]
    return '<g transform="translate(%d 0)">%s</g><polygon points="%s"/>' % (o, HUECO, ' '.join('%.2f,%.2f' % q for q in pg))
TR = ''.join(tramo(k) for k in range(-1, 3))
css = ('.b{fill:%s}.t{fill:none;stroke:%s;stroke-width:%s;stroke-linecap:round;stroke-linejoin:round}.k{fill:%s}' % (COL, COL, LW, BGC) +
       '.mv{animation:manik-monitor 1800ms infinite}'
       '@keyframes manik-monitor{0%%,30%%{transform:translateX(0);animation-timing-function:cubic-bezier(.55,0,.15,1)}100%%{transform:translateX(-%dpx)}}' % P +
       '@media (prefers-reduced-motion:reduce){.mv{animation:none}.manik-loader--monitor{animation:manik-respira 1600ms ease-in-out infinite alternate}}')
body = ('  <defs><clipPath id="m-in"><circle cx="%s" cy="%s" r="%s"/></clipPath>\n' % (CX, CY, R) +
        '    <linearGradient id="m-fade" gradientUnits="userSpaceOnUse" x1="-10" x2="542" y1="0" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".25" stop-color="#fff"/><stop offset=".75" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>\n'
        '    <mask id="m-m" maskUnits="userSpaceOnUse" x="-10" y="72" width="552" height="317"><rect x="-10" y="72" width="552" height="317" fill="url(#m-fade)"/></mask></defs>\n'
        '  <g mask="url(#m-m)"><g class="mv"><polyline class="t" points="%s"/></g></g>\n' % pts(linea) +
        '  <g class="b">%s</g>\n' % BURBUJA +
        '  <g clip-path="url(#m-in)"><g class="mv k">%s</g></g>' % TR)
out['monitor'] = svg('monitor', '-10 72 552 317', body, css,
    'el logo es una ventana a un pulso continuo: fuera de la burbuja la señal es una línea fina; al cruzarla se ensancha en el hueco exacto del logo y se detiene cuando la M coincide (1.8 s). Requiere la variable CSS manik-bg con el color del fondo.')

# ---------- 2 HABLA ----------
css = ('.b{fill:%s}.k{%s;stroke-width:7;stroke:%s}' % (COL, LN, COL) +
       '.a,.z{animation:1600ms cubic-bezier(.5,0,.2,1.3) infinite}.a{animation-name:manik-arriba}.z{animation-name:manik-abajo}'
       '.k{stroke-dasharray:.28 1;stroke-dashoffset:1.28;animation:manik-senal 1600ms linear infinite}'
       '@keyframes manik-arriba{0%,8%{transform:translateY(0)}30%,70%{transform:translateY(-30px)}88%,100%{transform:translateY(0)}}'
       '@keyframes manik-abajo{0%,8%{transform:translateY(0)}30%,70%{transform:translateY(22px)}88%,100%{transform:translateY(0)}}'
       '@keyframes manik-senal{0%,22%{stroke-dashoffset:1.28;opacity:0}26%{opacity:1}74%{stroke-dashoffset:0;opacity:1}80%,100%{stroke-dashoffset:0;opacity:0}}'
       '@media (prefers-reduced-motion:reduce){.a,.z,.k{animation:none}.k{opacity:0}.manik-loader--habla{animation:manik-respira 1600ms ease-in-out infinite alternate}}')
body = ('  <g class="b"><g class="a">%s</g><g class="z">%s</g></g>\n' % (PA, PB) +
        '  <polyline class="k" pathLength="1" points="%s"/>' % pts(core))
out['habla'] = svg('habla', '112 48 314 365', body, css,
    'la burbuja se abre por el pulso como una boca que habla; dentro corre la señal y se cierra (1.6 s).')

# ---------- 3 NACE ----------
TX, TY = 140, 368
css = ('.b{fill:%s;transform-box:view-box;transform-origin:%dpx %dpx;animation:manik-burbuja 2400ms cubic-bezier(.3,1.4,.5,1) infinite}' % (COL, TX, TY) +
       '.k{%s;stroke:%s;stroke-dasharray:1 1;animation:manik-linea 2400ms infinite}' % (LN, COL) +
       '.g{fill:%s;animation:manik-hueco 2400ms infinite}' % BGC +
       '@keyframes manik-burbuja{0%,30%{transform:scale(0)}50%,82%{transform:scale(1)}94%,100%{transform:scale(0)}}'
       '@keyframes manik-linea{0%{stroke-dashoffset:1;opacity:1;animation-timing-function:cubic-bezier(.6,0,.3,1)}28%,36%{stroke-dashoffset:0;opacity:1}48%,100%{stroke-dashoffset:0;opacity:0}}'
       '@keyframes manik-hueco{0%,36%{opacity:0}48%,82%{opacity:1}94%,100%{opacity:0}}'
       '@media (prefers-reduced-motion:reduce){.b,.k,.g{animation:none}.k{opacity:0}.manik-loader--nace{animation:manik-respira 1600ms ease-in-out infinite alternate}}')
body = ('  <defs><clipPath id="n-c"><circle cx="%s" cy="%s" r="%s"/></clipPath></defs>\n' % (CX, CY, R) +
        '  <g class="b">%s</g>\n' % BURBUJA +
        '  <polyline class="k" pathLength="1" points="%s"/>\n' % pts(logo_line) +
        '  <g class="g" clip-path="url(#n-c)">%s</g>' % HUECO)
out['nace'] = svg('nace', '112 72 314 317', body, css,
    'el impulso se dibuja primero como una línea; la burbuja nace desde su cola alrededor de ella, se sostiene y se recoge (2.4 s). Requiere la variable CSS manik-bg con el color del fondo.')

for n, s in out.items():
    m.parseString(s)
    open('manik-loader-%s.svg' % n, 'w').write(s)
    print(n, 'ok', len(s))
