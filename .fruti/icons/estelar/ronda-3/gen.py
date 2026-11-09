# Estelar · ronda 3 · color sobre C1 (marca) + C3 (16–24 px), elegidos 2026-11-09. python3 gen.py -> color.html
# Base compartida con Xila (manta y tinta) para que tinte, telar y bordado se lean como familia; el acento sale de un tinte natural de Oaxaca.
import os, base64
D = os.path.dirname(os.path.abspath(__file__)); IC = os.path.join(D, '..', '..')
MANTA, TINTA, NOCHE, NOCHEFG = '#F6F1E8', '#15171F', '#15171F', '#F6F1E8'
P7 = ['...X...', '.X.X.X.', '..XXX..', 'XXXOXXX', '..XXX..', '.X.X.X.', '...X...']
P5 = ['X.X.X', '.XXX.', 'XXOXX', '.XXX.', 'X.X.X']
PAL = [('caracol','Caracol','Púrpura de caracol (Purpura pansa), el tinte de la costa de Oaxaca.','#7B2D8E','#C98BDB'),
       ('pericon','Pericón','Amarillo dorado del pericón: la estrella como luz.','#8A5E00','#F4BE4C'),
       ('nogal','Nogal','Café del nogal: tierra y madera del telar.','#6E4426','#C99872')]
def L(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]; c=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in c]; return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b): return (max(L(a),L(b))+.05)/(min(L(a),L(b))+.05)
def runs(row):
    out, i = [], 0
    while i < len(row):
        if row[i] == 'X':
            j = i
            while j < len(row) and row[j] == 'X': j += 1
            out.append((i, j-i)); i = j
        else: i += 1
    return out
def tejido(P, g, o, tinta, flote, centro, hilos=True, alto=.6):
    n = len(P); s = ''
    if hilos:
        for j in range(n): s += f'<line x1="{o+j*g+g/2:.2f}" y1="{o-2:.2f}" x2="{o+j*g+g/2:.2f}" y2="{o+n*g+2:.2f}" stroke="{tinta}" stroke-width="{g*.14:.2f}" opacity=".4" stroke-linecap="round"/>'
    for i, row in enumerate(P):
        h = g*alto; y = o + i*g + (g-h)/2
        for a, Ln in runs(row): s += f'<rect x="{o+a*g+g*.08:.2f}" y="{y:.2f}" width="{Ln*g-g*.16:.2f}" height="{h:.2f}" rx="{h/2:.2f}" fill="{flote}"/>'
        for j, ch in enumerate(row):
            if ch == 'O': s += f'<rect x="{o+j*g+g*.2:.2f}" y="{o+i*g+g*.2:.2f}" width="{g*.6:.2f}" height="{g*.6:.2f}" rx="{g*.15:.2f}" fill="{centro}" stroke="{centro}" stroke-width="{g*.16:.2f}"/>'
    return s
def svg(inner, size, label): return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" role="img" aria-label="{label}">{inner}</svg>'
def C1(t, f, c): return tejido(P7, 8, 4, t, f, c)
def C3(t, f, c): return tejido(P5, 11.2, 4, t, f, c, hilos=False, alto=.74)
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(p,'rb').read()).decode()
GRANA, XILA = uri(os.path.join(IC,'grana','grana.svg')), uri(os.path.join(IC,'xila','final','svg','simbolo.svg'))
TRAT = [('estrella','La estrella en color','Los flotes llevan el tinte; la urdimbre y el centro van en tinta.'),
        ('centro','Solo el centro en color','Todo en tinta y el hecho del centro con el tinte, como la última puntada de Xila en cobalto.')]
def colores(tr, claro, cl, os_):
    t = TINTA if claro else NOCHEFG; a = cl if claro else os_
    return (t, a, t) if tr == 'estrella' else (t, t, a)
filas = ''
for k, nom, txt, cl, os_ in PAL:
    celdas = ''
    for tr, tn, tt in TRAT:
        c_cl, c_os = colores(tr, True, cl, os_), colores(tr, False, cl, os_)
        celdas += f'''<div class="tr"><p class="et">{tn}</p><div class="par"><div class="cl">{svg(C1(*c_cl),120,'Estelar')}</div><div class="os">{svg(C1(*c_os),120,'Estelar')}</div></div>
<div class="chicos"><span class="cl">{svg(C3(*c_cl),24,'Estelar')}</span><span class="cl">{svg(C3(*c_cl),16,'Estelar')}</span><span class="os">{svg(C3(*c_os),16,'Estelar')}</span>
<span class="eco"><img src="{GRANA}" alt="Grana" width="30" height="30">{svg(C1(*c_cl),34,'Estelar')}<img src="{XILA}" alt="Xila" width="30" height="30"></span></div><p class="nota">{tt}</p></div>'''
    filas += f'''<section class="pal" id="{k}"><header><div class="sw"><i style="background:{cl}"></i><i style="background:{os_}"></i></div><div><h2>{nom}</h2><p>{txt}</p>
<p class="cr">Claro {cl}: {cr(cl,MANTA):.1f}:1 sobre manta · Oscuro {os_}: {cr(os_,NOCHE):.1f}:1 sobre noche. Pasa como texto (4.5:1) en los dos.</p></div></header><div class="dos">{celdas}</div></section>'''
HTML = f'''<title>Estelar · Color r3</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Fraunces:opsz,wght@9..144,600&display=swap">
<style>
/* Una banda por tinte; dentro, dos formas de aplicarlo, cada una en claro, oscuro, chico y junto a Grana y Xila */
:root{{--bg:#efebe3;--fg:#15171f;--muted:#5b5f6e;--line:#dcd6ca;--card:#fffdf9;--f:'Instrument Sans',ui-sans-serif,system-ui,sans-serif;--d:'Fraunces',Georgia,serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1180px;margin:0 auto;display:grid;gap:28px}}
h1{{font:600 clamp(32px,5vw,52px)/1.05 var(--d);margin:0;text-wrap:balance}} .intro{{display:grid;gap:12px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}}
.ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.pal{{display:grid;gap:16px;padding:20px;background:var(--card);border:1px solid var(--line);border-radius:18px}}
.pal header{{display:flex;gap:16px;align-items:center}} .sw{{display:flex;gap:4px}} .sw i{{display:block;width:34px;height:54px;border-radius:10px}}
.pal h2{{margin:0;font:600 28px/1.1 var(--d)}} .pal header p{{margin:2px 0 0;font-size:15px}} .cr{{color:var(--muted);font-size:13.5px!important;font-variant-numeric:tabular-nums}}
.dos{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}} .tr{{display:grid;gap:10px;min-width:0}}
.et{{margin:0;font-size:12px;letter-spacing:.06em;text-transform:uppercase;font-weight:600;color:var(--muted)}}
.par{{display:grid;grid-template-columns:1fr 1fr;gap:8px}} .par>div{{display:grid;place-items:center;aspect-ratio:1.25;border-radius:12px;max-width:100%;min-width:0}} .par svg{{width:72%;height:auto}}
.cl{{background:{MANTA};border:1px solid var(--line)}} .os{{background:{NOCHE}}}
.chicos{{display:flex;gap:8px;align-items:center;flex-wrap:wrap}} .chicos>span{{display:grid;place-items:center;width:44px;height:44px;border-radius:9px}}
.chicos .eco{{width:auto;display:flex;gap:12px;padding:0 14px;background:{MANTA};border:1px solid var(--line)}}
.nota{{margin:0;font-size:14px;color:var(--muted)}}
.cierre{{max-width:72ch;display:grid;gap:8px}} .cierre h2{{font:600 26px var(--d);margin:0}} .cierre ul{{margin:0;padding-left:20px;display:grid;gap:6px}}
@media (max-width:820px){{.dos{{grid-template-columns:1fr}}}}
</style>
<div class="w"><div class="intro"><p class="ojo">Ronda 3 · color · C1 para la marca, C3 para chico</p><h1>Estelar: con qué tinte se teje</h1>
<p>El fondo (manta) y la tinta son los de Xila, para que tinte, telar y bordado se lean como una familia. Grana ya es carmín y Xila es cobalto con hilo naranja; Estelar necesita un tinte que no choque con ellos. Tres tintes naturales de Oaxaca, cada uno aplicado de dos formas.</p></div>
{filas}
<section class="cierre"><h2>Qué mirar</h2><ul>
<li><b>Junto a Grana y Xila:</b> la tira chica de cada opción muestra a las tres marcas lado a lado.</li>
<li><b>La estrella en color</b> le da más presencia a Estelar; <b>solo el centro en color</b> la hace hermana directa de Xila (tinta y un dato en color).</li>
<li><b>Solo el centro en color</b> deja el tinte en un cuadro chico: a 16 px casi no se ve, y la marca queda en tinta.</li>
<li><b>Caracol</b> está cerca de dos colores de la paleta de gráficas de Xila (jacaranda y ciruela); como marca no se cruzan, pero conviene saberlo.</li></ul></section></div>'''
open(os.path.join(D,'color.html'),'w').write(HTML); print('ok')
