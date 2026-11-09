# Xila · rediseño · ronda 7 · letra de apoyo con el color Añil (elegido 2026-11-09). python3 gen.py -> banco.html
import os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D,'..','rediseno-r6','gen.py')).read().split('def tarj(')[0]
ns = {'__file__': os.path.join(D,'..','rediseno-r6','gen.py')}; exec(src, ns)
niveles, palabra, sv, grafica, PAL = ns['niveles'], ns['palabra'], ns['sv'], ns['grafica'], ns['PAL']
P = [p for p in PAL if p[0] == 'anil'][0][3]; lv = niveles(P)
TIPO = [('Fraunces','Fraunces:opsz,wght@9..144,600','Fraunces',600,'La actual de Xila: serif editorial, cálida y con peso.'),
        ('Newsreader','Newsreader:opsz,wght@6..72,600','Newsreader',600,'Serif de periódico: sobria y precisa, como una buena nota de datos.'),
        ('Gloock','Gloock','Gloock',400,'Alto contraste y remates afilados: editorial con dramatismo de revista.'),
        ('Young Serif','Young+Serif','Young Serif',400,'Trazo grueso y redondeado, hecho a mano: artesanal, va con el bordado.'),
        ('Familjen Grotesk','Familjen+Grotesk:wght@600','Familjen Grotesk',600,'Una sans con carácter (no serif): directa y moderna, con curvas propias.')]
fuentes = '&'.join('family='+t[1] for t in TIPO) + '&family=Instrument+Sans:wght@400;600'
def tarj(n, g, fam, w, d):
    F = f"font-family:'{fam}',Georgia,serif;font-weight:{w}"
    return f'''<article class="c"><header><h3>{n}</h3><p>{d}</p></header>
<div class="port" style="background:{P['fondo']}">{sv(lv[0], 92)}<div><p class="eb">{palabra(34, P['g_fondo'], P['rombo'])}</p><b style="{F}">Primero la pregunta, después la gráfica.</b></div></div>
<div class="nota"><b style="{F}">Las ventas de agosto suben 20&nbsp;% contra el año pasado</b><p>Oaxaca crece más que las demás regiones desde marzo; el resto se mantiene estable.</p>{grafica(P)}</div>
<div class="ui"><span style="{F}">¿Cómo vamos?</span><small>Tablero · Ventas por región</small></div></article>'''
HTML = f'''<title>Xila · Rediseño r7</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fuentes}&display=swap">
<style>
/* Cinco letras con el mismo material: portada en añil, título de gráfica con su hallazgo, y el encabezado de un tablero */
:root{{--bg:#efebe3;--fg:#15171f;--muted:#5b5f6e;--line:#dcd6ca;--card:#fffdf9;--f:'Instrument Sans',ui-sans-serif,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1240px;margin:0 auto;display:grid;gap:28px}} h1{{font:600 clamp(32px,5vw,52px)/1.05 var(--f);margin:0;text-wrap:balance}}
.intro{{display:grid;gap:12px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}} .ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.tres{{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:16px}}
.c{{display:grid;gap:12px;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;align-content:start;min-width:0}} .c header{{display:grid;gap:4px}} .c h3{{margin:0;font-size:21px}} .c p{{margin:0;font-size:14.5px}}
.port{{display:flex;gap:16px;align-items:center;padding:18px;border-radius:12px;min-width:0}} .port>div{{min-width:0}} .port .eb{{margin:0 0 6px}} .port b{{display:block;color:#F4F1EA;font-size:clamp(22px,2.4vw,28px);line-height:1.12}}
.nota{{display:grid;gap:8px;padding:14px;border-radius:12px;background:#F4F1EA;border:1px solid var(--line);color:#16255C}} .nota b{{display:block;font-size:21px;line-height:1.2}} .nota p{{margin:0;color:#4a5274}}
.ui{{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;padding:12px 14px;border-radius:12px;background:#fff;border:1px solid var(--line);color:#16255C}} .ui span{{font-size:26px;line-height:1}} .ui small{{color:#5b5f6e}}
</style>
<div class="w"><div class="intro"><p class="ojo">Rediseño · ronda 7 · letra · color: Añil</p><h1>Xila: la letra del hallazgo</h1>
<p>El nombre siempre va bordado. Esta letra es la que acompaña: el lema, los títulos de gráfica (que en Xila dicen el hallazgo) y los encabezados de tablero. El texto corrido y las etiquetas siguen en Instrument Sans. Cinco opciones, de la más sobria a la más artesanal.</p></div>
<div class="tres">{''.join(tarj(*t) for t in TIPO)}</div></div>'''
open(os.path.join(D,'banco.html'),'w').write(HTML); print('ok')
