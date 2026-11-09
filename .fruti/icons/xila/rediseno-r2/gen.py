# Xila · rediseño · ronda 2 (usuario: «no me gustó ninguna, quiero propuestas con más identidad»). python3 gen.py -> banco.html
# Regla de la ronda: cada propuesta es un sistema con personalidad propia (símbolo + nombre + color + textura), no un icono suelto.
import os, math, base64
D = os.path.dirname(os.path.abspath(__file__)); IC = os.path.join(D, '..', '..')
COB, HIL, JAC, CIR, IND, JAD, NOP = '#1f4bd8', '#d14e0a', '#986bb8', '#6b3361', '#533295', '#1f9380', '#13582a'   # categórica de Xila (tema.json)
K, B = 'var(--k)', 'var(--fondo)'
def x(cx, cy, s, col, w):
    h = s/2; return f'<path d="M{cx-h:.2f} {cy-h:.2f}L{cx+h:.2f} {cy+h:.2f}M{cx+h:.2f} {cy-h:.2f}L{cx-h:.2f} {cy+h:.2f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round" fill="none"/>'
# 1 · Flor del Istmo: la flor bordada de los huipiles de Tehuantepec es una gráfica radial; el largo de cada pétalo es un dato, cada pétalo una serie.
def flor():
    L = [25, 17, 23, 14, 26, 16, 21, 19]; cols = [COB, HIL, JAC, JAD, COB, HIL, JAC, JAD]; s = ''
    for i, (l, c) in enumerate(zip(L, cols)):
        a = i*45 - 90
        s += f'<g transform="rotate({a} 32 32)"><path d="M38 32 Q{38+l*.45:.1f} {32-l*.32:.1f} {38+l:.1f} 32 Q{38+l*.45:.1f} {32+l*.32:.1f} 38 32Z" fill="{c}"/>'
        s += ''.join(f'<line x1="{38+t*l:.1f}" y1="{32-l*.26*math.sin(t*math.pi):.1f}" x2="{38+t*l:.1f}" y2="{32+l*.26*math.sin(t*math.pi):.1f}" stroke="{B}" stroke-width=".7" opacity=".55"/>' for t in (.25,.45,.65,.82)) + '</g>'
    return s + f'<circle cx="32" cy="32" r="7.5" fill="{B}"/>' + x(32, 32, 7, K, 2.6)
# 2 · Huipil: un emblema de 9 × 9 puntadas: la X de Xila en cobalto cruza el rombo del huipil en hilo naranja.
def huipil():
    s = f'<rect x="2" y="2" width="60" height="60" rx="10" fill="{K}"/>'
    for i in range(9):
        for j in range(9):
            cx, cy = 8 + j*6, 8 + i*6
            if i == j or i + j == 8: s += x(cx, cy, 4.4, COB if (i, j) != (4, 4) else HIL, 2.1)
            elif abs(i-4) + abs(j-4) == 4 or abs(i-4) + abs(j-4) == 2: s += x(cx, cy, 4.4, HIL, 2.1)
            else: s += x(cx, cy, 3, B, 1) if (i + j) % 2 == 0 else ''
    return s
# 3 · Aguja: la aguja borda y su hilo se vuelve la gráfica; el último valor queda anudado con un punto.
def aguja():
    return (f'<path d="M6 58 L38 26" stroke="{K}" stroke-width="6.5" stroke-linecap="round"/><path d="M6 58 L9 55" stroke="{K}" stroke-width="2" stroke-linecap="round"/>'
            f'<ellipse cx="35" cy="29" rx="4.6" ry="1.6" transform="rotate(-45 35 29)" fill="{B}"/>'
            f'<path d="M35 29 C40 33 41 38 44 36 S47 22 50 20 S54 26 57 12" stroke="{COB}" stroke-width="3.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="57" cy="12" r="5.4" fill="{B}"/><circle cx="57" cy="12" r="3.8" fill="{HIL}"/>')
# 4 · Letra bordada: «xila» escrita en punto de cruz (retícula de 5 × 7); el punto de la i, en naranja, es el dato. El símbolo es la x sola.
GL = {'x': ['.....', '.....', 'X...X', '.X.X.', '..X..', '.X.X.', 'X...X'],
      'i': ['..o..', '.....', '.XX..', '..X..', '..X..', '..X..', '.XXX.'],
      'l': ['.XX..', '..X..', '..X..', '..X..', '..X..', '..X..', '.XXX.'],
      'a': ['.....', '.....', '.XXX.', '....X', '.XXXX', 'X...X', '.XXXX']}
def letra(ch, ox, oy, g, col=None, w=2.4):
    s = ''
    for i, row in enumerate(GL[ch]):
        for j, c in enumerate(row):
            if c in 'Xo': s += x(ox + j*g + g/2, oy + i*g + g/2, g*.78, HIL if c == 'o' else (col or K), w)
    return s
def xsimb():
    s = f'<rect x="2" y="2" width="60" height="60" rx="10" fill="{COB}"/>'
    g = 10.4; rows = GL['x'][2:]
    for i, row in enumerate(rows):
        for j, c in enumerate(row):
            if c == 'X': s += x(6 + j*g + g/2, 6 + i*g + g/2, g*.72, '#fff' if (i, j) != (4, 4) else HIL, 3.4)
    return s
def palabra_bordada(h):
    g = h/7; s = ''; ox = 0
    for ch in 'xila':
        cols = [j for row in GL[ch] for j, c in enumerate(row) if c in 'Xo']; a, b = min(cols), max(cols)
        s += letra(ch, ox - a*g, 0, g, w=g*.3); ox += (b - a + 1)*g + g*.9
    return f'<svg viewBox="-2 -2 {ox+2:.0f} {h+4}" height="{h}" role="img" aria-label="xila">{s}</svg>'
OPS = [
 ('1','Flor del Istmo', flor(), 'La flor bordada de los huipiles de Tehuantepec, hecha gráfica: cada pétalo es una serie y su largo es un dato, como una gráfica radial. El centro es una puntada en X.', 'La de más presencia y color; se reconoce de lejos. Riesgo: usa cuatro colores y en tinta pierde la idea de «un dato en color».', 'Fraunces'),
 ('2','Huipil', huipil(), 'Un emblema de 9 × 9 puntadas sobre tinta: la X de Xila en cobalto cruza el rombo del huipil en hilo naranja, y el centro, en naranja, es el dato.', 'Se ve como un parche bordado: tiene textura y es muy propio. Riesgo: a 16 px es un cuadro con una X.', 'Fraunces'),
 ('3','Aguja', aguja(), 'La aguja borda y su hilo se vuelve la gráfica; el último valor queda anudado con un punto naranja. Bordar a mano es elegir la forma según la pregunta.', 'Cuenta el oficio y el producto en un gesto. Riesgo: la línea fina pierde fuerza a 16 px.', 'Fraunces'),
 ('4','Letra bordada', xsimb(), 'El nombre se escribe en punto de cruz y el punto de la i, en naranja, es el dato. El símbolo es la x sola, bordada en blanco sobre cobalto.', 'La identidad la carga el nombre: cualquier palabra en este punto de cruz es Xila. Riesgo: la letra pixelada se acerca a lo «retro digital».', 'bordada'),
]
def svg(inner, size, label): return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" role="img" aria-label="{label}">{inner}</svg>'
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(p,'rb').read()).decode()
GRANA, ESTELAR = uri(os.path.join(IC,'grana','grana.svg')), uri(os.path.join(IC,'estelar','final','svg','simbolo.svg'))
def tarj(k, n, s, q, l, wm):
    nombre = palabra_bordada(54) if wm == 'bordada' else '<b class="wm">xila</b>'
    return f'''<article class="c" id="p{k}"><div class="hero os">{svg(s,150,n)}<div>{nombre}<p class="lema">Primero la pregunta, después la gráfica.</p></div></div>
<div class="fila"><div class="cl sq">{svg(s,96,n)}</div><div class="chicos"><span class="cl">{svg(s,32,n)}</span><span class="cl">{svg(s,16,n)}</span><span class="os">{svg(s,16,n)}</span><span class="tab cl">{svg(s,16,n)} xila · ventas</span></div></div>
<h2><span>{k}</span> {n}</h2><p>{q}</p><p class="lec"><b>Lectura</b>{l}</p>
<div class="eco cl"><span><img src="{GRANA}" alt="" width="38" height="38"><small>Grana</small></span><span><img src="{ESTELAR}" alt="" width="38" height="38"><small>Estelar</small></span><span class="yo">{svg(s,42,n)}<small>Xila</small></span></div></article>'''
HTML = f'''<title>Xila · Rediseño r2</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,800;1,9..144,500&display=swap">
<style>
/* Cuatro sistemas: cada tarjeta abre con su portada (símbolo + nombre + lema) y debajo prueba tamaños y familia */
:root{{--bg:#efebe3;--fg:#15171f;--muted:#5b5f6e;--line:#dcd6ca;--card:#fffdf9;--f:'Instrument Sans',ui-sans-serif,system-ui,sans-serif;--d:'Fraunces',Georgia,serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1180px;margin:0 auto;display:grid;gap:30px}} h1{{font:800 clamp(34px,5.4vw,58px)/1.02 var(--d);margin:0;text-wrap:balance}}
.intro{{display:grid;gap:12px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}} .ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.banco{{display:grid;grid-template-columns:repeat(auto-fill,minmax(530px,1fr));gap:18px}}
.c{{display:grid;gap:12px;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:18px;align-content:start;min-width:0}}
.cl{{background:#f6f1e8;--k:#15171f;--fondo:#f6f1e8;border:1px solid var(--line);color:#15171f}} .os{{background:#15171f;--k:#f6f1e8;--fondo:#15171f;color:#f6f1e8}}
.hero{{display:flex;gap:22px;align-items:center;padding:24px;border-radius:14px;min-width:0;--k:#f6f1e8}} .hero>div{{min-width:0}} .hero svg{{flex:none;max-width:40%;height:auto}}
.wm{{display:block;font:800 64px/.9 var(--d);letter-spacing:-.02em}} .lema{{margin:10px 0 0;font:italic 500 18px/1.25 var(--d);opacity:.85}}
.hero .lema{{color:#d9d4c9}} .hero svg[aria-label="xila"]{{max-width:100%;--k:#f6f1e8}}
.fila{{display:flex;gap:10px;align-items:center;flex-wrap:wrap}} .sq{{display:grid;place-items:center;width:120px;height:120px;border-radius:12px}}
.chicos{{display:flex;gap:8px;align-items:center;flex-wrap:wrap}} .chicos>span{{display:grid;place-items:center;width:50px;height:50px;border-radius:10px}}
.chicos .tab{{width:auto;height:auto;display:flex;gap:7px;padding:7px 12px;border-radius:9px 9px 0 0;border-bottom:0;font-size:13px;background:#fff;--fondo:#fff}}
h2{{margin:2px 0 0;font:600 26px/1.15 var(--d)}} h2 span{{color:var(--muted);font-weight:600}} .c p{{margin:0;font-size:15px}} .lec{{color:var(--muted);font-size:14.5px!important}} .lec b{{display:block;font-size:12px;letter-spacing:.06em;text-transform:uppercase}}
.eco{{display:flex;gap:10px;padding:12px;border-radius:12px;justify-content:space-around}} .eco span{{display:grid;justify-items:center;gap:4px}} .eco small{{font-size:12px;color:#5b5f6e}} .eco .yo small{{font-weight:600;color:#15171f}}
@media (max-width:600px){{.banco{{grid-template-columns:1fr}} .hero{{flex-direction:column;align-items:flex-start}}}}
</style>
<div class="w"><div class="intro"><p class="ojo">Rediseño · ronda 2 · más identidad</p><h1>Xila: cuatro sistemas con carácter</h1>
<p>La ronda 1 eran iconos sueltos. Esta vez cada propuesta es un sistema completo: símbolo, nombre, color y textura, con la portada al frente. Todas salen del bordado oaxaqueño y de una regla del brief (el dato que importa en color), pero cada una con voz propia. Los colores son los de la paleta de gráficas de Xila.</p></div>
<div class="banco">{''.join(tarj(*o) for o in OPS)}</div></div>'''
open(os.path.join(D,'banco.html'),'w').write(HTML); print('ok')
