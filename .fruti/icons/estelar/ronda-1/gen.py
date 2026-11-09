# Estelar · ronda 1 · cuatro conceptos de símbolo en tinta. python3 gen.py -> banco.html
# Fuente: doc «Estelar · Brief de concepto y mensaje» (2026-11-08): telar + estrella; «una estrella hecha de hilos cruzados»;
# lema «Del hilo suelto a la estrella»; diseñas en copo de nieve, publicas en estrella. Vecinas: Grana (tinte) y Xila (bordado).
import os, math, base64
D = os.path.dirname(os.path.abspath(__file__)); IC = os.path.join(D, '..', '..')
K = 'var(--k)'; B = 'var(--fondo)'  # tinta y fondo de la tarjeta (el «halo» que hace el cruce por encima/por debajo)
def ln(pts, w=5, c=K): return f'<polyline points="{" ".join(f"{x:.2f},{y:.2f}" for x,y in pts)}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def seg(a, b, w=5): return ln([a, b], w + 4, B) + ln([a, b], w)
def lerp(a, b, t): return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)

# A · Estrella tejida: dos cuadros entrelazados (urdimbre y trama) forman la estrella de ocho puntas; en cada cruce un hilo pasa por encima y el otro por debajo.
def estrella_tejida(w=4):
    # dos cuadros iguales, uno girado 45°: el octagrama. El cruce por encima / por debajo se resuelve en la ronda 2 si se elige.
    c, s_ = 32, 19; r = s_*math.sqrt(2)
    A = [(c-s_,c-s_),(c+s_,c-s_),(c+s_,c+s_),(c-s_,c+s_),(c-s_,c-s_)]
    Bq = [(c,c-r),(c+r,c),(c,c+r),(c-r,c),(c,c-r)]
    return ln(A, w) + ln(Bq, w) + f'<circle cx="{c}" cy="{c}" r="4.5" fill="{K}"/>'
# B · Hilo suelto: un solo hilo dibuja la estrella de cuatro puntas y su punta final queda suelta, ondulando hacia fuera.
def hilo_suelto(w=4.6):
    c = 32; R = 24; r = 6
    pts = []
    for i in range(4):
        a = -math.pi/2 + i*math.pi/2
        pts.append((c + R*math.cos(a), c + R*math.sin(a)))
    d = f'M{pts[0][0]:.2f} {pts[0][1]:.2f}'
    for i in range(1, 5):
        p = pts[i % 4]; d += f' Q{c:.2f} {c:.2f} {p[0]:.2f} {p[1]:.2f}'
    d += f' C{c+2:.2f} 1 {c+16:.2f} 2 {c+17:.2f} 9 S{c+27:.2f} 12 {c+28:.2f} 4'
    return f'<path d="{d}" fill="none" stroke="{K}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/><circle cx="{c}" cy="{c}" r="{r*.7:.1f}" fill="{K}"/>'
# C · Telar: la estrella de ocho puntas de los textiles de telar de cintura, tejida en una urdimbre de 7 × 7: donde la trama pasa por encima, se ve la estrella.
PAT = ['...X...', '.X.X.X.', '..XXX..', 'XXXOXXX', '..XXX..', '.X.X.X.', '...X...']
def telar():
    g = 8; o = 4; out = ''
    for j in range(7):
        x = o + j*g + g/2; out += f'<line x1="{x}" y1="3" x2="{x}" y2="61" stroke="{K}" stroke-width="1.2" opacity=".45"/>'
    for i, row in enumerate(PAT):
        for j, ch in enumerate(row):
            x, y = o + j*g, o + i*g
            if ch == 'X': out += f'<rect x="{x+.8}" y="{y+1.6}" width="{g-1.6}" height="{g-3.2}" rx="1.6" fill="{K}"/>'
            if ch == 'O': out += f'<rect x="{x+.8}" y="{y+.8}" width="{g-1.6}" height="{g-1.6}" rx="1.6" fill="none" stroke="{K}" stroke-width="2"/>'
    return out
# D · Esquema estrella: el modelo que entrega el producto: un hecho al centro y cinco dimensiones, unidas por hilos de dos cabos.
def esquema():
    c = 32; out = ''
    for i in range(5):
        a = -math.pi/2 + i*2*math.pi/5; ex, ey = c + 22*math.cos(a), c + 22*math.sin(a)
        nx, ny = -math.sin(a), math.cos(a)
        for s in (-1, 1):
            pts = []
            for k in range(13):
                t = k/12; r = 8 + t*14; w = s*1.6*math.sin(t*math.pi*3)
                pts.append((c + r*math.cos(a) + nx*w, c + r*math.sin(a) + ny*w))
            out += ln(pts, 2.2)
        out += f'<circle cx="{ex:.2f}" cy="{ey:.2f}" r="5.2" fill="{B}" stroke="{K}" stroke-width="3.2"/>'
    return out + f'<rect x="{c-8}" y="{c-8}" width="16" height="16" rx="3.5" fill="{K}"/>'
CON = [
 ('a','A · Estrella tejida', estrella_tejida(), 'Dos cuadros de hilo, uno girado, forman la estrella de ocho puntas; el punto al centro es el hecho del modelo.', 'La más fiel al brief («estrella hecha de hilos cruzados»). Es un motivo muy usado (octagrama) y también es un símbolo religioso en varias culturas; si se elige, el entrelazado de hilos tendría que hacerla propia.'),
 ('b','B · Hilo suelto', hilo_suelto(), 'Un solo hilo dibuja la estrella de cuatro puntas y su extremo queda suelto: el lema «Del hilo suelto a la estrella» en una línea.', 'La que cuenta la historia completa y la más ligera. Riesgo: la estrella de cuatro puntas se usa mucho como símbolo de «IA» o «brillo», y el brief pide no sonar a IA.'),
 ('c','C · Telar', telar(), 'La estrella de ocho puntas de los textiles de telar de cintura, tejida en una urdimbre de 7 × 7. Donde la trama pasa por encima, aparece la estrella.', 'La que más se emparienta con Xila (punto de cruz) y Grana (tinte): tinte, telar y bordado. Riesgo: a 16 px se vuelve textura o asterisco.'),
 ('d','D · Esquema estrella', esquema(), 'El modelo que el producto entrega: un hecho al centro y cinco dimensiones, unidos por hilos de dos cabos.', 'La más literal para quien modela datos. Riesgo: se parece a cualquier icono de red o de molécula.'),
]
def svg(inner, size, label): return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" role="img" aria-label="{label}">{inner}</svg>'
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(p,'rb').read()).decode()
GRANA, XILA = uri(os.path.join(IC,'grana','grana.svg')), uri(os.path.join(IC,'xila','final','svg','simbolo.svg'))
tarj = ''.join(f'''<article class="c" id="{k}"><div class="par"><div class="cl">{svg(s,128,n)}</div><div class="os">{svg(s,128,n)}</div></div>
<div class="chicos"><span class="cl">{svg(s,32,n)}</span><span class="cl">{svg(s,16,n)}</span><span class="os">{svg(s,16,n)}</span></div>
<h2>{n}</h2><p>{q}</p><p class="lec"><b>Lectura</b>{l}</p>
<div class="eco"><span><img src="{GRANA}" alt="Grana" width="40" height="40"><small>Grana · tinte</small></span><span class="yo">{svg(s,44,n)}<small>Estelar · telar</small></span><span><img src="{XILA}" alt="Xila" width="40" height="40"><small>Xila · bordado</small></span></div></article>''' for k,n,s,q,l in CON)
HTML = f'''<title>Estelar · Símbolos r1</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Fraunces:opsz,wght@9..144,600&display=swap">
<style>
/* Banco de cuatro conceptos: cada uno en grande (claro y oscuro), a 32 y 16 px, y al lado de Grana y Xila */
:root{{--bg:#f4f2ee;--fg:#16171d;--muted:#5b5d66;--line:#dddad3;--card:#fff;--k:#16171d;--fondo:#fff;--noche:#121318;--nochefg:#f4f2ee;--f:'Instrument Sans',ui-sans-serif,system-ui,sans-serif;--d:'Fraunces',Georgia,serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#131418;--fg:#ecebe6;--muted:#a4a5ad;--line:#2b2c33;--card:#1b1c21;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#131418;--fg:#ecebe6;--muted:#a4a5ad;--line:#2b2c33;--card:#1b1c21;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1180px;margin:0 auto;display:grid;gap:32px}}
h1{{font:600 clamp(32px,5vw,52px)/1.05 var(--d);margin:0;text-wrap:balance}} .intro{{display:grid;gap:12px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}}
.ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.banco{{display:grid;grid-template-columns:repeat(auto-fill,minmax(500px,1fr));gap:18px}}
.c{{display:grid;gap:12px;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;align-content:start;min-width:0}}
.par{{display:grid;grid-template-columns:1fr 1fr;gap:10px}} .par>div{{display:grid;place-items:center;aspect-ratio:1.3;border-radius:12px;max-width:100%}}
.cl{{background:#fff;--k:#16171d;--fondo:#fff;border:1px solid var(--line)}} .os{{background:var(--noche);--k:var(--nochefg);--fondo:var(--noche)}}
.chicos{{display:flex;gap:8px}} .chicos span{{display:grid;place-items:center;width:52px;height:52px;border-radius:10px}}
h2{{margin:2px 0 0;font:600 24px/1.15 var(--d)}} .c p{{margin:0;font-size:15px}} .lec{{color:var(--muted);font-size:14.5px!important}} .lec b{{display:block;font-size:12px;letter-spacing:.06em;text-transform:uppercase}}
.eco{{display:flex;gap:10px;padding:12px;border-radius:12px;background:#fff;border:1px solid var(--line);--k:#16171d;--fondo:#fff;color:#16171d;justify-content:space-around}}
.eco span{{display:grid;justify-items:center;gap:4px}} .eco small{{font-size:12px;color:#5b5d66}} .eco .yo small{{font-weight:600;color:#16171d}}
.cierre{{max-width:72ch;display:grid;gap:8px}} .cierre h2{{font-size:26px}} .cierre ul{{margin:0;padding-left:20px;display:grid;gap:6px}}
@media (max-width:560px){{.banco{{grid-template-columns:1fr}}}}
</style>
<div class="w"><div class="intro"><p class="ojo">Ronda 1 · símbolos en tinta, sin color ni letra final</p><h1>Estelar: cuatro formas de tejer una estrella</h1>
<p>Del brief: Estelar teje los hilos sueltos de una base de datos hasta que forman una estrella. Telar nombra el proceso y estrella, el resultado. Cada concepto se prueba en grande, a 16 px y junto a sus vecinas del ecosistema: Grana (el tinte) y Xila (el bordado).</p></div>
<div class="banco">{tarj}</div>
<section class="cierre"><h2>Cómo comparar</h2><ul>
<li><b>¿Se lee a 16 px?</b> Es el tamaño de la pestaña del navegador y del favicon.</li>
<li><b>¿Cuenta algo que el producto hace de verdad?</b> La regla del brief: si una imagen no tiene nada detrás, no se usa.</li>
<li><b>¿Encaja junto a Grana y Xila?</b> Tinte, telar y bordado pueden ser una familia de textil mexicano.</li></ul></section></div>'''
open(os.path.join(D,'banco.html'),'w').write(HTML); print('ok')
