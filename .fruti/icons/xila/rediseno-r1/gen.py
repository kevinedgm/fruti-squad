# Xila · rediseño · ronda 1 (usuario, 2026-11-09: «vamos a rediseñar la identidad de Xila»; brief: doc «Xila · Brief de concepto y mensaje»).
# Del brief: Xila parte de la pregunta de quien mira; el dato que importa va en color y el resto en gris; «más allá de la línea y la barra»; cada dato, una puntada.
# python3 gen.py -> banco.html
import os, math, base64
D = os.path.dirname(os.path.abspath(__file__)); IC = os.path.join(D, '..', '..')
K, C, G, B = 'var(--k)', 'var(--c)', 'var(--g)', 'var(--fondo)'
def x(cx, cy, s, col, w=3.2):
    h = s/2; return f'<path d="M{cx-h:.2f} {cy-h:.2f}L{cx+h:.2f} {cy+h:.2f}M{cx+h:.2f} {cy-h:.2f}L{cx-h:.2f} {cy+h:.2f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round" fill="none"/>'
# A · actual: la greca bordada (de ../final/svg/simbolo-16.svg), como referencia
ACT = [(10,54),(21,54),(21,43),(32,43),(32,32),(43,32),(43,21),(54,21),(54,10)]
A = ''.join(x(cx, cy, 8, C if i == len(ACT)-1 else K) for i, (cx, cy) in enumerate(ACT))
# B · El que se sale: una retícula de 4 × 4 puntadas en gris; una sola, en cobalto, se sale del patrón (la regla de Xila: el dato que importa en color).
Bm = ''
for i in range(4):
    for j in range(4):
        if (i, j) == (1, 2): continue
        Bm += x(11 + j*14, 11 + i*14, 7.5, G, 3)
Bm += f'<g transform="rotate(22 39 25)">' + x(39, 25, 10.5, C, 4.4) + '</g>'
# C · El hilo que se sale: una fila de puntadas que se vuelve línea y termina en su último valor (punto con anillo), la anatomía de Xila.
Cm = ''.join(x(9 + i*10, 44, 7, K, 3) for i in range(3))
Cm += f'<path d="M34 44 C40 44 41 30 47 28 S53 22 55 16" stroke="{C}" stroke-width="3.4" fill="none" stroke-linecap="round"/>'
Cm += f'<circle cx="55" cy="16" r="6" fill="{B}"/><circle cx="55" cy="16" r="4.2" fill="{C}"/>'
# D · Bastidor: el aro de bordar enmarca una pequeña gráfica de barras hecha de puntadas; la barra que responde la pregunta va en cobalto.
Dm = f'<circle cx="32" cy="32" r="27" stroke="{K}" stroke-width="3.6" fill="none"/><path d="M50 12.5 l5.5 -5.5" stroke="{K}" stroke-width="3.6" stroke-linecap="round"/>'
for j, (n, col) in enumerate([(2, G), (4, C), (3, G)]):
    for k in range(n): Dm += x(21 + j*11, 46 - k*9.5, 7, col, 3)
# E · La X de dos hilos: la inicial hecha con dos hilos que se cruzan; el de cobalto pasa por encima, el de tinta por debajo.
Em = (f'<path d="M12 12 L52 52" stroke="{K}" stroke-width="7" stroke-linecap="round"/>'
      f'<path d="M52 12 L12 52" stroke="{B}" stroke-width="13" stroke-linecap="butt"/>'
      f'<path d="M52 12 L12 52" stroke="{C}" stroke-width="7" stroke-linecap="round"/>'
      f'<circle cx="12" cy="12" r="5" fill="{K}"/><circle cx="52" cy="52" r="5" fill="{K}"/>')
CON = [
 ('a','Actual · Greca bordada', A, 'La marca de hoy: la greca de Mitla en punto de cruz; la última puntada en cobalto es el último valor.', 'Se queda como referencia. Su riesgo, anotado desde la ronda 1 original: se lee como escalera o «subida», un icono genérico de analítica.'),
 ('b','B · El que se sale', Bm, 'Quince puntadas en gris y una en cobalto, más grande y torcida, fuera del patrón: «¿quién se sale del patrón?» y la regla de Xila (el dato que importa en color) en un solo símbolo.', 'La más fiel al producto. Riesgo: a 16 px la retícula gris se vuelve textura y solo se ve el punto azul.'),
 ('c','C · El hilo que se sale', Cm, 'Tres puntadas y el hilo que las sigue se suelta y se vuelve línea, hasta su último valor: «más allá de la línea y la barra», con la anatomía de las gráficas de Xila.', 'Cuenta el paso de bordado a gráfica. Riesgo: se acerca al hilo suelto que exploramos para Estelar.'),
 ('d','D · Bastidor', Dm, 'El aro de bordar enmarca una gráfica pequeña hecha de puntadas; la barra que responde la pregunta va en cobalto. El aro es el lugar donde eliges la forma.', 'La más reconocible como bordado. Riesgo: el aro con columnas dentro pesa mucho a 16 px y se parece a un icono de «buscar».'),
 ('e','E · La X de dos hilos', Em, 'La inicial hecha con dos hilos que se cruzan: el de cobalto pasa por encima, como el dato que manda sobre el contexto.', 'La más simple y la que mejor aguanta a 16 px. Riesgo: una X sola se acerca a «cerrar» y a otras marcas con X.'),
]
def svg(inner, size, label): return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" role="img" aria-label="{label}">{inner}</svg>'
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(p,'rb').read()).decode()
GRANA, ESTELAR = uri(os.path.join(IC,'grana','grana.svg')), uri(os.path.join(IC,'estelar','final','svg','simbolo.svg'))
tarj = ''.join(f'''<article class="c{' act' if k=='a' else ''}" id="{k}"><div class="par"><div class="cl">{svg(s,128,n)}</div><div class="os">{svg(s,128,n)}</div></div>
<div class="chicos"><span class="cl">{svg(s,32,n)}</span><span class="cl">{svg(s,16,n)}</span><span class="os">{svg(s,16,n)}</span><span class="tab cl">{svg(s,16,n)} xila · ventas</span></div>
<h2>{n}</h2><p>{q}</p><p class="lec"><b>Lectura</b>{l}</p>
<div class="eco cl"><span><img src="{GRANA}" alt="" width="40" height="40"><small>Grana · tiñe</small></span><span><img src="{ESTELAR}" alt="" width="40" height="40"><small>Estelar · teje</small></span><span class="yo">{svg(s,44,n)}<small>Xila · borda</small></span></div></article>''' for k,n,s,q,l in CON)
HTML = f'''<title>Xila · Rediseño r1</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Fraunces:opsz,wght@9..144,600&display=swap">
<style>
/* Banco: la marca actual primero como referencia y cuatro direcciones nuevas, cada una grande, chica y junto a Grana y Estelar */
:root{{--bg:#efebe3;--fg:#15171f;--muted:#5b5f6e;--line:#dcd6ca;--card:#fffdf9;--f:'Instrument Sans',ui-sans-serif,system-ui,sans-serif;--d:'Fraunces',Georgia,serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1180px;margin:0 auto;display:grid;gap:30px}} h1{{font:600 clamp(32px,5vw,52px)/1.05 var(--d);margin:0;text-wrap:balance}}
.intro{{display:grid;gap:12px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}} .ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.banco{{display:grid;grid-template-columns:repeat(auto-fill,minmax(520px,1fr));gap:18px}}
.c{{display:grid;gap:12px;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;align-content:start;min-width:0}} .c.act{{border-style:dashed}}
.par{{display:grid;grid-template-columns:1fr 1fr;gap:10px}} .par>div{{display:grid;place-items:center;aspect-ratio:1.3;border-radius:12px;min-width:0}}
.cl{{background:#f6f1e8;--k:#15171f;--c:#1f4bd8;--g:#9a9db0;--fondo:#f6f1e8;border:1px solid var(--line);color:#15171f}}
.os{{background:#15171f;--k:#f6f1e8;--c:#7a9bff;--g:#5d6276;--fondo:#15171f}}
.chicos{{display:flex;gap:8px;align-items:center;flex-wrap:wrap}} .chicos>span{{display:grid;place-items:center;width:52px;height:52px;border-radius:10px}}
.chicos .tab{{width:auto;height:auto;display:flex;gap:7px;padding:7px 12px;border-radius:9px 9px 0 0;border-bottom:0;font-size:13px;background:#fff;--fondo:#fff}}
h2{{margin:2px 0 0;font:600 24px/1.15 var(--d)}} .c p{{margin:0;font-size:15px}} .lec{{color:var(--muted);font-size:14.5px!important}} .lec b{{display:block;font-size:12px;letter-spacing:.06em;text-transform:uppercase}}
.eco{{display:flex;gap:10px;padding:12px;border-radius:12px;justify-content:space-around}} .eco span{{display:grid;justify-items:center;gap:4px}} .eco small{{font-size:12px;color:#5b5f6e}} .eco .yo small{{font-weight:600;color:#15171f}}
.cierre{{max-width:72ch;display:grid;gap:8px}} .cierre h2{{font-size:26px}} .cierre ul{{margin:0;padding-left:20px;display:grid;gap:6px}}
@media (max-width:580px){{.banco{{grid-template-columns:1fr}}}}
</style>
<div class="w"><div class="intro"><p class="ojo">Rediseño · ronda 1 · símbolos con el color actual (cobalto, tinta y gris)</p><h1>Xila: primero la pregunta, después la puntada</h1>
<p>El brief cambió el centro de Xila: ya no es solo bordar los datos, es partir de la pregunta de quien mira y poner en color solo el dato que importa. La marca actual va primero, como referencia. Las otras cuatro salen del brief y se prueban a 16 px y junto a Grana y Estelar.</p></div>
<div class="banco">{tarj}</div>
<section class="cierre"><h2>Qué mirar</h2><ul>
<li><b>¿Dice la regla de Xila?</b> Un dato en color y el resto en gris es lo que más distingue a la librería; B, C y D lo dibujan.</li>
<li><b>¿Se distingue de Estelar?</b> Estelar teje con tramos horizontales en caracol; Xila borda con puntadas en X.</li>
<li><b>¿Aguanta a 16 px?</b> Mira la pestaña de cada tarjeta.</li></ul></section></div>'''
open(os.path.join(D,'banco.html'),'w').write(HTML); print('ok')
