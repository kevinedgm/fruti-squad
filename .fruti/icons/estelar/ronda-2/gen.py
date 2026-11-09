# Estelar · ronda 2 · desarrollo de C «Telar» (elegido 2026-11-09). python3 gen.py -> banco.html
import os, base64
D = os.path.dirname(os.path.abspath(__file__)); IC = os.path.join(D, '..', '..')
K = 'var(--k)'
P7 = ['...X...', '.X.X.X.', '..XXX..', 'XXXOXXX', '..XXX..', '.X.X.X.', '...X...']
P5 = ['X.X.X', '.XXX.', 'XXOXX', '.XXX.', 'X.X.X']
def runs(row):  # tramos seguidos de X en una fila: (inicio, largo)
    out, i = [], 0
    while i < len(row):
        if row[i] == 'X':
            j = i
            while j < len(row) and row[j] == 'X': j += 1
            out.append((i, j - i)); i = j
        else: i += 1
    return out
def urdimbre(P, g, o, hilos=True, alto=.6):
    n = len(P); s = ''
    if hilos:
        for j in range(n): s += f'<line x1="{o+j*g+g/2:.2f}" y1="{o-2:.2f}" x2="{o+j*g+g/2:.2f}" y2="{o+n*g+2:.2f}" stroke="{K}" stroke-width="{g*.14:.2f}" opacity=".4" stroke-linecap="round"/>'
    for i, row in enumerate(P):
        h = g*alto; y = o + i*g + (g-h)/2
        for a, L in runs(row):
            s += f'<rect x="{o+a*g+g*.08:.2f}" y="{y:.2f}" width="{L*g-g*.16:.2f}" height="{h:.2f}" rx="{h/2:.2f}" fill="{K}"/>'
        for j, ch in enumerate(row):
            if ch == 'O': s += f'<rect x="{o+j*g+g*.2:.2f}" y="{o+i*g+g*.2:.2f}" width="{g*.6:.2f}" height="{g*.6:.2f}" rx="{g*.15:.2f}" fill="none" stroke="{K}" stroke-width="{g*.16:.2f}"/>'
    return s
V = [
 ('v1', 'C1 · Urdimbre de 7', urdimbre(P7, 8, 4), 'La ronda 1 depurada: la urdimbre (hilos verticales) se queda como fondo tenue y la trama sale en tramos redondeados donde pasa por encima.', 'La más fiel al telar. A 16 px la urdimbre desaparece y queda un asterisco.'),
 ('v2', 'C2 · Flotes', urdimbre(P7, 8, 4, hilos=False, alto=.72), 'Sin urdimbre: solo los flotes, los tramos de trama que pasan por encima. El centro queda abierto: el hecho del modelo.', 'Más limpia y con más peso. Riesgo: los tramos de un solo cuadro se vuelven puntos, y el conjunto se lee como sol o chispa más que como estrella de ocho puntas.'),
 ('v3', 'C3 · Estrella de 5', urdimbre(P5, 11.2, 4, hilos=False, alto=.74), 'La misma estrella en una retícula de 5 × 5: menos puntadas y más grandes. Pensada para 16 a 32 px.', 'La que mejor aguanta chica. Pierde las puntas finas de la de 7, y con los puntos en las esquinas puede leerse como dado o cara.'),
 ('v4', 'C4 · Hilo suelto', urdimbre(P7, 7.2, 4, hilos=False, alto=.72) + f'<path d="M50.2 51.6 C55 51.6 56 57 59 57.5 S62 55 62 53" fill="none" stroke="{K}" stroke-width="4" stroke-linecap="round"/>', 'Los flotes y, en la punta de abajo a la derecha, un hilo que se sale del tejido: el lema «Del hilo suelto a la estrella».', 'Cuenta la historia completa. El hilo suelto es un detalle que a 16 px se pierde, así que necesitaría una versión chica sin él.'),
]
def svg(inner, size, label): return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" role="img" aria-label="{label}">{inner}</svg>'
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(p,'rb').read()).decode()
GRANA, XILA = uri(os.path.join(IC,'grana','grana.svg')), uri(os.path.join(IC,'xila','final','svg','simbolo.svg'))
tarj = ''.join(f'''<article class="c" id="{k}"><div class="par"><div class="cl">{svg(s,128,n)}</div><div class="os">{svg(s,128,n)}</div></div>
<div class="chicos"><span class="cl">{svg(s,32,n)}</span><span class="cl">{svg(s,24,n)}</span><span class="cl">{svg(s,16,n)}</span><span class="os">{svg(s,16,n)}</span>
<span class="tab">{svg(s,16,n)} Estelar · mapa</span></div>
<h2>{n}</h2><p>{q}</p><p class="lec"><b>Lectura</b>{l}</p>
<div class="eco"><span><img src="{GRANA}" alt="Grana" width="40" height="40"><small>Grana · tinte</small></span><span class="yo">{svg(s,44,n)}<small>Estelar · telar</small></span><span><img src="{XILA}" alt="Xila" width="40" height="40"><small>Xila · bordado</small></span></div></article>''' for k,n,s,q,l in V)
css = open(os.path.join(D,'..','ronda-1','banco.html')).read().split('<style>')[1].split('</style>')[0]
HTML = f'''<title>Estelar · Símbolos r2</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Fraunces:opsz,wght@9..144,600&display=swap">
<style>{css}
.chicos{{flex-wrap:wrap;align-items:center}} .chicos .tab{{width:auto;height:auto;display:flex;gap:6px;align-items:center;padding:6px 12px;border-radius:9px 9px 0 0;background:#fff;border:1px solid var(--line);border-bottom:0;font-size:13px;color:#16171d;--k:#16171d}}
</style>
<div class="w"><div class="intro"><p class="ojo">Ronda 2 · desarrollo de C «Telar» · en tinta</p><h1>Estelar: la estrella del telar</h1>
<p>Elegiste el telar. Esta ronda lo afina en cuatro direcciones: con urdimbre o sin ella, en retícula de 7 o de 5, y con el hilo suelto del lema. La regla que separa a Estelar de Xila: Xila borda con puntadas en X; Estelar teje con flotes, tramos de trama que pasan por encima de la urdimbre.</p></div>
<div class="banco">{tarj}</div>
<section class="cierre"><h2>Cómo decidir</h2><ul>
<li><b>Para la marca</b> (portada, README, presentación) conviene la de 7: tiene las puntas finas de la estrella del telar.</li>
<li><b>Para 16 a 24 px</b> (favicon, pestaña) la de 5 se lee mejor. Puedes elegir una grande y una chica, como hizo Xila con su versión de 16 px.</li>
<li><b>El hilo suelto</b> suma la historia del lema; decide si la marca la cuenta o si se queda en el texto.</li></ul></section></div>'''
open(os.path.join(D,'banco.html'),'w').write(HTML); print('ok')
