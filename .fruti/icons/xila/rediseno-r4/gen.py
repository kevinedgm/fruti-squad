# Xila · rediseño · ronda 4 · un logo que cambia de dibujo según el tamaño (usuario: «debe funcionar para logo e iconos de diferentes tamaños»).
# Principio: a 16 px una puntada de un emblema de 9 × 9 mide 1.5 px y el ojo ya no la separa. Cada tamaño tiene su propio dibujo con menos puntadas
# y más gruesas, todos con las mismas tres piezas: la x bordada, el rombo naranja y el centro naranja (el dato).
# python3 gen.py svg  -> svg/*.svg ; node png.cjs ; python3 gen.py html -> banco.html
import os, sys, base64, json
D = os.path.dirname(os.path.abspath(__file__)); IC = os.path.join(D, '..', '..')
src = open(os.path.join(D,'..','rediseno-r2','gen.py')).read().split('OPS = [')[0]
ns = {'__file__': os.path.join(D,'..','rediseno-r2','gen.py')}; exec(src, ns)
palabra_bordada = ns['palabra_bordada']
COB, HIL, TINTA, MANTA, BLANCO = '#1f4bd8', '#d14e0a', '#15171f', '#f6f1e8', '#ffffff'
def x(cx, cy, s, c, w):
    h = s/2; return f'<path d="M{cx-h:.2f} {cy-h:.2f}L{cx+h:.2f} {cy+h:.2f}M{cx+h:.2f} {cy-h:.2f}L{cx-h:.2f} {cy+h:.2f}" stroke="{c}" stroke-width="{w:.2f}" stroke-linecap="round" fill="none"/>'
def malla(n, fn, pad, sz, w, fondo=TINTA, r=11):
    g = (64 - 2*pad)/n; s = f'<rect x="0" y="0" width="64" height="64" rx="{r}" fill="{fondo}"/>'
    for i in range(n):
        for j in range(n):
            c = fn(i, j)
            if c: s += x(pad + j*g + g/2, pad + i*g + g/2, g*sz, c, g*w)
    return s
def L(i, j):  # 9 × 9: la x en el rombo (ronda 3, A)
    if (i, j) == (4, 4): return HIL
    if 2 <= i <= 6 and 2 <= j <= 6 and (i == j or i + j == 8): return BLANCO
    if abs(i-4) + abs(j-4) == 4: return HIL
def M(i, j):  # 5 × 5: la x de 5 puntadas y las 4 puntas del rombo
    if (i, j) == (2, 2): return HIL
    if (i == j or i + j == 4) and (i, j) in [(1,1),(1,3),(3,1),(3,3)]: return BLANCO
    if (i, j) in [(0,2),(2,0),(2,4),(4,2)]: return HIL
def S(i, j):  # 3 × 3: solo la x; el centro naranja
    if (i, j) == (1, 1): return HIL
    if i == j or i + j == 2: return BLANCO
NIV = [  # id, nombre, rango, svg
 ('l', 'Grande', '64 px o más', malla(9, L, 4, .72, .30)),
 ('m', 'Mediano', '32 a 48 px', malla(5, M, 5, .74, .26)),
 ('s', 'Chico', '20 a 28 px', malla(3, S, 7, .78, .24)),
 ('xs', 'Favicon', '16 px', f'<rect width="64" height="64" rx="12" fill="{TINTA}"/>' + x(32, 32, 34, BLANCO, 11) + f'<circle cx="32" cy="32" r="9" fill="{HIL}"/>'),
]
TAM = [16, 24, 32, 48, 64, 128]
USO = {'l': (64, 999), 'm': (32, 48), 's': (20, 28), 'xs': (0, 16)}
def svgfile(inner): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{inner}</svg>'
if sys.argv[1] == 'svg':
    os.makedirs(f'{D}/svg', exist_ok=True)
    for k, n, r, s in NIV: open(f'{D}/svg/{k}.svg', 'w').write(svgfile(s))
    json.dump([[k, t] for k, *_ in NIV for t in TAM], open(f'{D}/svg/jobs.json', 'w')); print('svg ok'); sys.exit()
def png(k, t): return 'data:image/png;base64,' + base64.b64encode(open(f'{D}/png/{k}-{t}.png', 'rb').read()).decode()
filas = ''
for k, n, r, s in NIV:
    a, b = USO[k]
    celdas = ''.join(f'<td class="{"si" if a <= t <= b else ""}"><img src="{png(k,t)}" width="{t}" height="{t}" alt="{n} a {t} px"></td>' for t in TAM)
    filas += f'<tr><th><b>{n}</b><span>{r}</span></th>{celdas}</tr>'
zoom = ''.join(f'<figure><div class="z"><img src="{png(k, t)}" alt="{n} a {t} px, ampliado" style="width:{t*6}px;height:{t*6}px"></div><figcaption><b>{n}</b> a {t} px reales, ampliado × 6</figcaption></figure>'
               for k, n, r, s, t in [(*NIV[3], 16), (*NIV[2], 24), (*NIV[1], 32)])
def sv(inner, size, label): return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" role="img" aria-label="{label}">{inner}</svg>'
fam = ''.join(f'<figure>{sv(s, 110, n)}<figcaption><b>{n}</b><span>{r}</span></figcaption></figure>' for k, n, r, s in NIV)
HTML = f'''<title>Xila · Rediseño r4</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,800;1,9..144,500&display=swap">
<style>
/* Un mismo logo en cuatro dibujos: la familia, la tabla de tamaños reales (verde = dibujo que corresponde) y el detalle de píxeles */
:root{{--bg:#efebe3;--fg:#15171f;--muted:#5b5f6e;--line:#dcd6ca;--card:#fffdf9;--ok:#e3efe6;--okb:#2f7a4b;--f:'Instrument Sans',ui-sans-serif,system-ui,sans-serif;--d:'Fraunces',Georgia,serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;--ok:#1d3326;--okb:#6fcf97;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;--ok:#1d3326;--okb:#6fcf97;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1100px;margin:0 auto;display:grid;gap:30px}} h1{{font:800 clamp(32px,5vw,54px)/1.03 var(--d);margin:0;text-wrap:balance}} h2{{font:600 26px/1.15 var(--d);margin:0 0 10px}}
.intro{{display:grid;gap:12px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}} .ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.box{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px}} section>p{{margin:0 0 12px;color:var(--muted);max-width:72ch}}
.fam{{display:flex;gap:22px;flex-wrap:wrap;align-items:flex-end}} .fam figure{{margin:0;display:grid;gap:6px;justify-items:center}} .fam figcaption{{display:grid;text-align:center;line-height:1.25}} .fam span{{font-size:13px;color:var(--muted)}}
.tw{{overflow-x:auto}} table{{border-collapse:separate;border-spacing:6px;min-width:640px}} th{{text-align:left;padding:4px 10px 4px 0;font-weight:400;white-space:nowrap}} th b{{display:block}} th span{{font-size:13px;color:var(--muted)}}
thead th{{font-size:13px;color:var(--muted);text-align:center}} td{{text-align:center;vertical-align:middle;padding:10px;border-radius:10px;background:#f6f1e8;border:1px solid var(--line)}} td.si{{background:var(--ok);border:2px solid var(--okb)}} td img{{display:block;margin:auto}}
.zoom{{display:flex;gap:20px;flex-wrap:wrap}} .zoom figure{{margin:0;display:grid;gap:8px}} .z{{background:#f6f1e8;border:1px solid var(--line);border-radius:12px;padding:12px;width:fit-content;max-width:100%;overflow:auto}} .z img{{image-rendering:pixelated;display:block}} .zoom figcaption{{font-size:14px}}
.firma{{display:flex;gap:16px;align-items:center;flex-wrap:wrap}} .firma>div{{padding:16px 20px;border-radius:12px;display:flex;gap:14px;align-items:center}} .cl{{background:#f6f1e8;--k:#15171f;border:1px solid var(--line)}} .os{{background:#15171f;--k:#f6f1e8}} .firma svg[aria-label="xila"]{{max-width:100%}}
ul{{margin:0;padding-left:20px;display:grid;gap:6px;max-width:72ch}}
</style>
<div class="w"><div class="intro"><p class="ojo">Rediseño · ronda 4 · un logo para todos los tamaños</p><h1>Xila: menos puntadas mientras más chico</h1>
<p>Tenías razón: el emblema de 9 × 9 no funciona chico. A 16 px cada puntada mide 1.5 px y el ojo ya no la separa de la de al lado. La solución de los logos que sí escalan es tener un dibujo por tamaño: los mismos elementos, con menos puntadas y más gruesas conforme el espacio se reduce.</p></div>
<section><h2>La familia: cuatro dibujos, una sola marca</h2><p>Los cuatro conservan las mismas tres piezas: la x bordada, el rombo naranja y el centro naranja (el dato). Al bajar de tamaño se quita primero el rombo y al final queda una sola X con su punto.</p><div class="box fam">{fam}</div></section>
<section><h2>Prueba a tamaño real</h2><p>Cada fila es un dibujo y cada columna un tamaño, en píxeles reales (no ampliados). En verde, el tamaño que le toca a cada dibujo: así se ve en cada lugar.</p>
<div class="box tw"><table><thead><tr><th></th>{''.join(f'<th>{t} px</th>' for t in TAM)}</tr></thead><tbody>{filas}</tbody></table></div></section>
<section><h2>Los píxeles de cerca</h2><p>El dibujo de cada tamaño, renderizado a sus píxeles reales y ampliado seis veces: cada puntada ocupa por lo menos 2 px de grueso y deja aire con la de al lado.</p><div class="box zoom">{zoom}</div></section>
<section><h2>Con el nombre</h2><div class="firma"><div class="cl"><svg viewBox="0 0 64 64" width="56" height="56" role="img" aria-label="xila">{NIV[0][3]}</svg>{palabra_bordada(44)}</div>
<div class="os"><svg viewBox="0 0 64 64" width="56" height="56" role="img" aria-label="xila">{NIV[0][3]}</svg>{palabra_bordada(44)}</div>
<div class="cl"><svg viewBox="0 0 64 64" width="28" height="28" role="img" aria-label="xila">{NIV[2][3]}</svg><span style="font:600 16px var(--f);color:#15171f">xila · ventas</span></div></div></section>
<section class="box"><h2>Reglas de uso</h2><ul><li>Desde 64 px: el grande. De 32 a 48: el mediano. De 20 a 28: el chico. A 16 px y en el favicon: la X sola con su punto.</li>
<li>Cada dibujo se usa solo en su rango; no se escala uno para cubrir otro.</li><li>El nombre bordado se usa desde 24 px de alto; más chico, el nombre va en texto normal junto al símbolo.</li></ul></section></div>'''
open(f'{D}/banco.html','w').write(HTML); print('html ok')
