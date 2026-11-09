# Xila · rediseño · ronda 3: cruce de 2 «Huipil» y 4 «Letra bordada» (usuario, 2026-11-09). python3 gen.py -> banco.html
import os, base64
D = os.path.dirname(os.path.abspath(__file__)); IC = os.path.join(D, '..', '..')
src = open(os.path.join(D,'..','rediseno-r2','gen.py')).read().split('OPS = [')[0]
ns = {'__file__': os.path.join(D,'..','rediseno-r2','gen.py')}; exec(src, ns)
x, GL, letra, palabra_bordada, COB, HIL = ns['x'], ns['GL'], ns['letra'], ns['palabra_bordada'], ns['COB'], ns['HIL']
TINTA, MANTA = '#15171f', '#f6f1e8'
def malla(n, fn, fondo, w=None, pad=4):
    g = (64 - 2*pad)/n; w = w or g*.3; s = f'<rect x="1" y="1" width="62" height="62" rx="11" fill="{fondo}"/>'
    for i in range(n):
        for j in range(n):
            c = fn(i, j)
            if c: s += x(pad + j*g + g/2, pad + i*g + g/2, g*.72, c, w)
    return s
# A · La x en el rombo: el rombo del huipil en naranja rodea la x bordada en blanco; el centro, en naranja, es el dato.
def fA(i, j):
    d = abs(i-4) + abs(j-4)
    if (i, j) == (4, 4): return HIL
    if 2 <= i <= 6 and 2 <= j <= 6 and (i == j or i + j == 8): return '#ffffff'
    if d == 4: return HIL
    return None
# B · Huipil de 7: el emblema de la ronda 2 simplificado a 7 × 7 para que aguante chico: la X en cobalto y el rombo en naranja.
def fB(i, j):
    if (i, j) == (3, 3): return HIL
    if i == j or i + j == 6: return COB
    if abs(i-3) + abs(j-3) == 3: return HIL
    return None
# C · Cuello de huipil: el marco bordado del cuello del huipil (cobalto y naranja alternados) y, al centro, la x bordada en tinta sobre manta.
def fC(i, j):
    if i in (0, 8) or j in (0, 8): return COB if (i + j) % 2 == 0 else HIL
    if (i, j) == (4, 4): return HIL
    if 2 <= i <= 6 and 2 <= j <= 6 and (i == j or i + j == 8): return TINTA
    return None
SIMB = {'a': malla(9, fA, TINTA), 'b': malla(7, fB, TINTA, pad=5), 'c': malla(9, fC, MANTA)}
# Banda: la textura de marca, rombos de huipil corriendo como una franja bordada (se repite cada 9 puntadas).
def banda(w_px, h_px, fondo, a, b):
    g = h_px/9; n = int(w_px/g) + 1; s = f'<rect width="{w_px}" height="{h_px}" fill="{fondo}"/>'
    for i in range(9):
        for j in range(n):
            jj = j % 8; d = abs(i-4) + abs(jj-4)
            if d == 4: s += x(j*g + g/2, i*g + g/2, g*.7, a, g*.28)
            elif d == 2 or (i, jj) == (4, 4): s += x(j*g + g/2, i*g + g/2, g*.7, b, g*.28)
    return f'<svg viewBox="0 0 {w_px} {h_px}" width="100%" preserveAspectRatio="xMinYMid slice" aria-hidden="true" style="display:block;height:{h_px}px">{s}</svg>'
OPS = [
 ('a','La x en el rombo', 'El rombo del huipil, en naranja, abraza la x bordada en blanco; el centro naranja es el dato. Une las dos ideas en un solo emblema: la letra y el textil.', 'La más completa. Riesgo: blanco, naranja y tinta juntos en 16 px se vuelven una mancha con un punto.'),
 ('b','Huipil de 7', 'El emblema de la ronda 2 simplificado a 7 × 7 para que aguante chico; el nombre va en la letra bordada. El emblema es la firma y la letra, la voz.', 'La más fuerte a 16 px. Riesgo: sin la letra, el emblema no dice «x» tan claro.'),
 ('c','Cuello de huipil', 'El marco bordado del cuello del huipil (cobalto y naranja) encuadra la x bordada en tinta sobre manta: como asomarse por el cuello de la prenda.', 'La más textil y la que mejor funciona en claro. Riesgo: el marco de dos colores es fino a 16 px.'),
]
def svg(inner, size, label): return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" role="img" aria-label="{label}">{inner}</svg>'
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(p,'rb').read()).decode()
GRANA, ESTELAR = uri(os.path.join(IC,'grana','grana.svg')), uri(os.path.join(IC,'estelar','final','svg','simbolo.svg'))
def tarj(k, n, q, l):
    s = SIMB[k]
    return f'''<article class="c" id="{k}"><div class="hero os">{svg(s,140,n)}<div>{palabra_bordada(58)}<p class="lema">Primero la pregunta, después la gráfica.</p></div></div>
<div class="band">{banda(1200, 40, TINTA, HIL, COB)}</div>
<div class="fila"><div class="cl sq">{svg(s,96,n)}</div><div class="chicos"><span class="cl">{svg(s,32,n)}</span><span class="cl">{svg(s,24,n)}</span><span class="cl">{svg(s,16,n)}</span><span class="os">{svg(s,16,n)}</span><span class="tab cl">{svg(s,16,n)} xila · ventas</span></div></div>
<div class="claro cl">{svg(s,64,n)}<div style="--k:#15171f">{palabra_bordada(40)}</div></div>
<h2>{n}</h2><p>{q}</p><p class="lec"><b>Lectura</b>{l}</p>
<div class="eco cl"><span><img src="{GRANA}" alt="" width="38" height="38"><small>Grana</small></span><span><img src="{ESTELAR}" alt="" width="38" height="38"><small>Estelar</small></span><span class="yo">{svg(s,42,n)}<small>Xila</small></span></div></article>'''
css = open(os.path.join(D,'..','rediseno-r2','banco.html')).read().split('<style>')[1].split('</style>')[0]
HTML = f'''<title>Xila · Rediseño r3</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,800;1,9..144,500&display=swap">
<style>{css}
.band{{border-radius:10px;overflow:hidden;max-width:100%}} .claro{{display:flex;gap:16px;align-items:center;padding:16px;border-radius:12px}} .claro svg[aria-label="xila"]{{max-width:100%}}
.banco{{grid-template-columns:repeat(auto-fill,minmax(360px,1fr))}} .hero{{flex-wrap:wrap}}
</style>
<div class="w"><div class="intro"><p class="ojo">Rediseño · ronda 3 · Huipil + Letra bordada</p><h1>Xila: el huipil y la letra, juntos</h1>
<p>Te gustaron el emblema del huipil y la letra bordada. En las tres propuestas el nombre se escribe en punto de cruz, con el punto de la i en naranja como dato, y una franja de rombos funciona como textura de marca. Lo que cambia es el emblema.</p></div>
<div class="banco">{''.join(tarj(*o) for o in OPS)}</div></div>'''
open(os.path.join(D,'banco.html'),'w').write(HTML); print('ok')
