# Xila · rediseño · ronda 5 · color y tipografía sobre el sistema de cuatro dibujos (ronda 4, aprobado 2026-11-09). python3 gen.py -> banco.html
import os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D,'..','rediseno-r2','gen.py')).read().split('OPS = [')[0]
ns = {'__file__': os.path.join(D,'..','rediseno-r2','gen.py')}; exec(src, ns); GL = ns['GL']
def lum(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]; c=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in c]; return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b): a,b=lum(a),lum(b); return (max(a,b)+.05)/(min(a,b)+.05)
def x(cx, cy, s, c, w):
    h = s/2; return f'<path d="M{cx-h:.2f} {cy-h:.2f}L{cx+h:.2f} {cy+h:.2f}M{cx+h:.2f} {cy-h:.2f}L{cx-h:.2f} {cy+h:.2f}" stroke="{c}" stroke-width="{w:.2f}" stroke-linecap="round" fill="none"/>'
def niveles(P):
    F, X, R, C = P['fondo'], P['x'], P['rombo'], P['centro']; borde = P.get('borde')
    def tile(r=11): return f'<rect x=".75" y=".75" width="62.5" height="62.5" rx="{r}" fill="{F}"' + (f' stroke="{borde}" stroke-width="1.5"/>' if borde else '/>')
    def malla(n, fn, pad, sz, w):
        g = (64 - 2*pad)/n; s = tile()
        for i in range(n):
            for j in range(n):
                c = fn(i, j)
                if c: s += x(pad + j*g + g/2, pad + i*g + g/2, g*sz, c, g*w)
        return s
    L = lambda i, j: C if (i, j) == (4, 4) else (X if 2 <= i <= 6 and 2 <= j <= 6 and (i == j or i + j == 8) else (R if abs(i-4) + abs(j-4) == 4 else None))
    M = lambda i, j: C if (i, j) == (2, 2) else (X if (i, j) in [(1,1),(1,3),(3,1),(3,3)] else (R if (i, j) in [(0,2),(2,0),(2,4),(4,2)] else None))
    S = lambda i, j: C if (i, j) == (1, 1) else (X if i == j or i + j == 2 else None)
    return [malla(9, L, 4, .72, .30), malla(5, M, 5, .74, .26), malla(3, S, 7, .78, .24),
            tile(12) + x(32, 32, 34, X, 11) + f'<circle cx="32" cy="32" r="9" fill="{C}"/>']
def palabra(h, col, dot):
    g = h/7; s = ''; ox = 0
    for ch in 'xila':
        rows = GL[ch]; cols = [j for row in rows for j, c in enumerate(row) if c in 'Xo']; a, b = min(cols), max(cols)
        for i, row in enumerate(rows):
            for j, c in enumerate(row):
                if c in 'Xo': s += x(ox + (j-a)*g + g/2, i*g + g/2, g*.78, dot if c == 'o' else col, g*.3)
        ox += (b - a + 1)*g + g*.9
    return f'<svg viewBox="-2 -2 {ox+2:.0f} {h+4}" height="{h}" role="img" aria-label="xila" style="max-width:100%">{s}</svg>'
def sv(inner, size, label='xila'): return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" role="img" aria-label="{label}">{inner}</svg>'
def grafica(P):  # una gráfica de Xila: gris para el contexto, el color de marca para el dato que importa
    base, dato, txt = P['g_gris'], P['g_dato'], P['g_txt']
    pts = [(10,70),(40,64),(70,66),(100,58),(130,60),(160,50),(190,52),(220,38)]
    otras = [[(10,62),(40,66),(70,60),(100,63),(130,61),(160,64),(190,60),(220,62)], [(10,76),(40,74),(70,77),(100,72),(130,74),(160,71),(190,73),(220,70)]]
    s = ''.join(f'<polyline points="{" ".join(f"{a},{b}" for a,b in o)}" fill="none" stroke="{base}" stroke-width="2"/>' for o in otras)
    s += f'<polyline points="{" ".join(f"{a},{b}" for a,b in pts)}" fill="none" stroke="{dato}" stroke-width="2.6"/><circle cx="220" cy="38" r="5" fill="{P["g_fondo"]}"/><circle cx="220" cy="38" r="3.4" fill="{dato}"/>'
    s += f'<text x="10" y="18" font-size="12.5" font-weight="600" fill="{txt}" font-family="Instrument Sans,sans-serif">Oaxaca crece más que las demás</text><text x="230" y="42" font-size="11" fill="{dato}" font-family="Instrument Sans,sans-serif" font-weight="600">+18&#160;%</text>'
    return f'<svg viewBox="0 0 270 90" width="100%" role="img" aria-label="Ejemplo de gráfica" style="display:block;background:{P["g_fondo"]};border-radius:10px">{s}</svg>'
PAL = [
 ('noche','Noche e hilo', 'El emblema en tinta, la x en manta y el hilo naranja en el rombo y el dato. En las gráficas el dato sigue en cobalto: la marca es naranja y la librería, azul.',
  dict(fondo='#15171f', x='#f6f1e8', rombo='#ff8a3d', centro='#ff8a3d', g_fondo='#f6f1e8', g_gris='#b9b6ae', g_dato='#1f4bd8', g_txt='#15171f'), 'Naranja sobre tinta {:.1f}:1 · manta sobre tinta {:.1f}:1', ('#ff8a3d','#15171f','#f6f1e8','#15171f')),
 ('cobalto','Cobalto', 'El emblema en el cobalto de la librería: marca y gráficas comparten color. La x en manta y el rombo en durazno, porque el naranja fuerte no se distingue sobre azul (1.6:1).',
  dict(fondo='#1f4bd8', x='#f6f1e8', rombo='#ffb070', centro='#ffb070', g_fondo='#f6f1e8', g_gris='#b9b6ae', g_dato='#1f4bd8', g_txt='#15171f'), 'Durazno sobre cobalto {:.1f}:1 · manta sobre cobalto {:.1f}:1', ('#ffb070','#1f4bd8','#f6f1e8','#1f4bd8')),
 ('manta','Manta', 'El emblema claro, como bordado sobre la tela: x en tinta, rombo en hilo naranja y el centro en cobalto. Es la regla de las gráficas: el dato que importa, en azul.',
  dict(fondo='#f6f1e8', x='#15171f', rombo='#d14e0a', centro='#1f4bd8', borde='#d8d1c3', g_fondo='#f6f1e8', g_gris='#b9b6ae', g_dato='#1f4bd8', g_txt='#15171f'), 'Naranja sobre manta {:.1f}:1 · cobalto sobre manta {:.1f}:1', ('#d14e0a','#f6f1e8','#1f4bd8','#f6f1e8')),
]
TIPO = [('Fraunces','Fraunces:opsz,wght@9..144,600','Fraunces',600,'La actual: serif editorial con carácter; cálida y con peso.'),
        ('Newsreader','Newsreader:opsz,wght@6..72,600','Newsreader',600,'Serif de periódico, más sobria y precisa: «una buena nota de datos».'),
        ('Instrument Serif','Instrument+Serif','Instrument Serif',400,'Serif angosta y elegante; la misma del lema de Estelar: une a la familia.')]
fuentes = '&'.join('family='+t[1] for t in TIPO) + '&family=Instrument+Sans:wght@400;600'
colores = ''
for k, n, txt, P, crt, pares in PAL:
    lv = niveles(P); c = crt.format(cr(pares[0], pares[1]), cr(pares[2], pares[3]))
    oscuro_wm = P['fondo'] if k != 'manta' else '#15171f'
    colores += f'''<article class="c"><header><h3>{n}</h3><p>{txt}</p><p class="cr">{c}</p></header>
<div class="fam">{''.join(f'<span>{sv(s, t)}<small>{t} px</small></span>' for s, t in zip(lv, [96, 48, 24, 16]))}</div>
<div class="port" style="background:{oscuro_wm}">{sv(lv[0], 70)}{palabra(42, '#f6f1e8', P['rombo'] if k != 'manta' else '#ff8a3d')}</div>
<div class="port claro">{sv(lv[0], 56)}{palabra(34, '#15171f', '#d14e0a')}</div>
{grafica(P)}</article>'''
tipos = ''.join(f'''<article class="c t"><header><h3>{n}</h3><p>{d}</p></header><div class="port" style="background:#15171f">{sv(niveles(PAL[0][3])[0], 64)}<div><b style="font-family:'{fam}',Georgia,serif;font-weight:{w}">Primero la pregunta, después la gráfica.</b></div></div>
<div class="nota"><b style="font-family:'{fam}',Georgia,serif;font-weight:{w}">Las ventas de agosto suben 20&nbsp;% contra el año pasado</b><p>Oaxaca crece más que las demás regiones desde marzo; el resto se mantiene estable.</p></div></article>''' for n, g, fam, w, d in TIPO)
HTML = f'''<title>Xila · Rediseño r5</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fuentes}&display=swap">
<style>
/* Dos bandas: color (tres paletas con los cuatro dibujos, portada y una gráfica) y letra de apoyo (tres serif en portada y en un título de gráfica) */
:root{{--bg:#efebe3;--fg:#15171f;--muted:#5b5f6e;--line:#dcd6ca;--card:#fffdf9;--f:'Instrument Sans',ui-sans-serif,system-ui,sans-serif;--d:'Fraunces',Georgia,serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1200px;margin:0 auto;display:grid;gap:30px}} h1{{font:600 clamp(32px,5vw,52px)/1.05 var(--d);margin:0;text-wrap:balance}} h2{{font:600 28px/1.1 var(--d);margin:0}}
.intro{{display:grid;gap:12px;max-width:72ch}} .intro p,.sec>p{{margin:0;color:var(--muted);max-width:72ch}} .ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.sec{{display:grid;gap:14px}} .tres{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}}
.c{{display:grid;gap:12px;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;align-content:start;min-width:0}} .c header{{display:grid;gap:4px}} .c h3{{margin:0;font:600 22px var(--d)}} .c p{{margin:0;font-size:14.5px}} .cr{{color:var(--muted);font-size:13px!important;font-variant-numeric:tabular-nums}}
.fam{{display:flex;gap:14px;align-items:flex-end;padding:14px;border-radius:12px;background:#ffffff;border:1px solid var(--line);flex-wrap:wrap}} .fam span{{display:grid;justify-items:center;gap:4px}} .fam small{{font-size:12px;color:#5b5f6e}}
.port{{display:flex;gap:14px;align-items:center;padding:16px;border-radius:12px;min-width:0;flex-wrap:wrap}} .port.claro{{background:#f6f1e8;border:1px solid var(--line)}} .port>div{{min-width:0}}
.t .port b{{display:block;color:#f6f1e8;font-size:clamp(22px,2.6vw,30px);line-height:1.1}}
.nota{{padding:14px;border-radius:12px;background:#f6f1e8;border:1px solid var(--line);color:#15171f}} .nota b{{display:block;font-size:21px;line-height:1.2}} .nota p{{margin:6px 0 0;color:#5b5f6e}}
</style>
<div class="w"><div class="intro"><p class="ojo">Rediseño · ronda 5 · color y letra</p><h1>Xila: con qué hilo y qué letra</h1>
<p>El sistema de cuatro dibujos queda fijo. Esta ronda decide dos cosas por separado: el color de la marca y la letra que acompaña al nombre bordado en títulos y portadas.</p></div>
<section class="sec"><h2>Color</h2><p>Cada paleta se prueba en los cuatro dibujos, en una portada oscura y una clara con el nombre bordado, y en una gráfica de Xila: la marca tiene que convivir con la regla de las gráficas (gris para el contexto, el dato en color).</p><div class="tres">{colores}</div></section>
<section class="sec"><h2>Letra de apoyo</h2><p>El nombre siempre va bordado. Esta letra es para el lema, los titulares y los títulos de gráfica, que en Xila dicen el hallazgo. El texto corrido sigue en Instrument Sans.</p><div class="tres">{tipos}</div></section></div>'''
open(os.path.join(D,'banco.html'),'w').write(HTML); print('ok')
