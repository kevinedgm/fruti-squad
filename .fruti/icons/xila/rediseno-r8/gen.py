# Xila · rediseño · ronda 8 · pares tipográficos (usuario: «2 fuentes, primaria y secundaria, haz las propuestas»). Color: Añil. python3 gen.py -> banco.html
import os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D,'..','rediseno-r6','gen.py')).read().split('def tarj(')[0]
ns = {'__file__': os.path.join(D,'..','rediseno-r6','gen.py')}; exec(src, ns)
niveles, palabra, sv, PAL = ns['niveles'], ns['palabra'], ns['sv'], ns['PAL']
P = [p for p in PAL if p[0] == 'anil'][0][3]; lv = niveles(P)
AN, AN2, AN3, MANTA = '#16255C', '#2F4FA8', '#7FA0E0', '#F4F1EA'
PARES = [  # nombre, primaria (familia, peso), secundaria (familia), qué cuenta
 ('Editorial', ('Newsreader', 600), 'Instrument Sans', 'Serif de periódico para los hallazgos y una sans limpia para todo lo demás. Sobria y precisa, como una buena nota de datos.'),
 ('Artesanal', ('Young Serif', 400), 'Hanken Grotesk', 'Una serif gruesa, hecha a mano, que va con el bordado; la sans de apoyo es neutra para que los números se lean sin ruido.'),
 ('Revista', ('Gloock', 400), 'IBM Plex Sans', 'Títulos de alto contraste con dramatismo de revista y una sans técnica, con cifras muy claras para tablas y ejes.'),
 ('Clara', ('Fraunces', 600), 'Atkinson Hyperlegible Next', 'La serif actual de Xila con una sans diseñada para máxima legibilidad (baja visión): coherente con el pilar «para todos los ojos».'),
 ('Moderna', ('Familjen Grotesk', 600), 'Instrument Sans', 'Dos sans: una con carácter para títulos y otra neutra para el texto. La más contemporánea y la que menos dice «oficio».'),
]
G = {'Newsreader': 'Newsreader:opsz,wght@6..72,600', 'Young Serif': 'Young+Serif', 'Gloock': 'Gloock', 'Fraunces': 'Fraunces:opsz,wght@9..144,600',
     'Familjen Grotesk': 'Familjen+Grotesk:wght@600', 'Instrument Sans': 'Instrument+Sans:wght@400;600', 'Hanken Grotesk': 'Hanken+Grotesk:wght@400;600',
     'IBM Plex Sans': 'IBM+Plex+Sans:wght@400;600', 'Atkinson Hyperlegible Next': 'Atkinson+Hyperlegible+Next:wght@400;600'}
fuentes = '&'.join('family=' + v for v in G.values())
def chart(sec):
    S = f"font-family:'{sec}',sans-serif"
    pts = [(40,96),(80,88),(120,90),(160,78),(200,80),(240,66),(280,68),(320,48)]
    o1 = [(40,84),(80,90),(120,82),(160,86),(200,83),(240,87),(280,82),(320,84)]
    o2 = [(40,104),(80,102),(120,106),(160,100),(200,103),(240,99),(280,101),(320,98)]
    s = ''.join(f'<line x1="40" x2="330" y1="{y}" y2="{y}" stroke="#d8d4ca" stroke-width="1"/><text x="32" y="{y+4}" text-anchor="end" font-size="11" fill="#5b6280" style="{S};font-variant-numeric:tabular-nums">{v}</text>' for y, v in [(48,'1.2 M'),(76,'900 k'),(104,'600 k')])
    s += ''.join(f'<polyline points="{" ".join(f"{a},{b}" for a,b in o)}" fill="none" stroke="#c4c6cf" stroke-width="2"/>' for o in (o1, o2))
    s += f'<polyline points="{" ".join(f"{a},{b}" for a,b in pts)}" fill="none" stroke="{AN}" stroke-width="2.6"/><circle cx="320" cy="48" r="5" fill="{MANTA}"/><circle cx="320" cy="48" r="3.4" fill="{AN}"/>'
    s += f'<text x="328" y="44" font-size="12" font-weight="600" fill="{AN}" style="{S}">Oaxaca</text><text x="328" y="58" font-size="11" fill="{AN}" style="{S};font-variant-numeric:tabular-nums">1.21 M</text>'
    s += f'<text x="328" y="88" font-size="11" fill="#5b6280" style="{S}">Puebla</text><text x="328" y="102" font-size="11" fill="#5b6280" style="{S}">Chiapas</text>'
    s += ''.join(f'<text x="{x}" y="122" text-anchor="middle" font-size="11" fill="#5b6280" style="{S}">{m}</text>' for x, m in [(40,'ene'),(120,'mar'),(200,'may'),(280,'jul'),(320,'ago')])
    return f'<svg viewBox="0 0 390 130" width="100%" role="img" aria-label="Ventas por región, enero a agosto" style="display:block">{s}</svg>'
def tarj(n, pri, sec, d):
    F = f"font-family:'{pri[0]}',Georgia,serif;font-weight:{pri[1]}"; S = f"font-family:'{sec}',ui-sans-serif,sans-serif"
    filas = ''.join(f'<tr><td>{r}</td><td>{v}</td><td class="{c}">{p}</td></tr>' for r, v, p, c in [('Oaxaca','1 210 400','+18.2 %','up'),('Puebla','884 120','+2.1 %',''),('Chiapas','612 900','−0.8 %','')])
    return f'''<article class="c"><header><p class="par"><span style="{F}">{pri[0]}</span> <i>+</i> <span style="{S};font-weight:600">{sec}</span></p><h3>{n}</h3><p style="{S}">{d}</p></header>
<div class="port" style="background:{AN}">{sv(lv[0], 84)}<div><p class="eb">{palabra(30, MANTA, AN3)}</p><b style="{F}">Primero la pregunta, después la gráfica.</b><span style="{S}">Una librería de gráficas que parte de lo que quiere saber quien mira.</span></div></div>
<div class="nota" style="{S}"><b style="{F}">Oaxaca crece más que las demás regiones desde marzo</b><p>Ventas mensuales, enero a agosto de 2026. Las demás regiones se mantienen estables.</p>{chart(sec)}
<table><thead><tr><th>Región</th><th>Ventas</th><th>vs. 2025</th></tr></thead><tbody>{filas}</tbody></table></div>
<div class="leyenda"><span><b style="{F}">Primaria</b> · {pri[0]}: nombre de la sección, lema, título de gráfica (el hallazgo)</span><span><b style="{S};font-weight:600">Secundaria</b> · {sec}: texto, ejes, etiquetas, tablas, botones</span></div></article>'''
HTML = f'''<title>Xila · Rediseño r8</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fuentes}&display=swap">
<style>
/* Cinco pares: cada tarjeta prueba el par en una portada, una gráfica real (título, ejes, etiquetas) y una tabla con cifras */
:root{{--bg:#efebe3;--fg:#15171f;--muted:#5b5f6e;--line:#dcd6ca;--card:#fffdf9;--f:'Instrument Sans',ui-sans-serif,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1260px;margin:0 auto;display:grid;gap:28px}} h1{{font:600 clamp(32px,5vw,52px)/1.05 var(--f);margin:0;text-wrap:balance}}
.intro{{display:grid;gap:12px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}} .ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.tres{{display:grid;grid-template-columns:repeat(auto-fill,minmax(390px,1fr));gap:16px}}
.c{{display:grid;gap:12px;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;align-content:start;min-width:0}} .c header{{display:grid;gap:4px}} .c h3{{margin:0;font-size:14px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}} .c header p{{margin:0;font-size:14.5px}}
.par{{font-size:24px!important;line-height:1.15}} .par i{{font-style:normal;color:var(--muted)}}
.port{{display:flex;gap:16px;align-items:center;padding:18px;border-radius:12px;min-width:0}} .port>div{{min-width:0}} .port .eb{{margin:0 0 6px}} .port b{{display:block;color:{MANTA};font-size:clamp(22px,2.3vw,27px);line-height:1.12}} .port span{{display:block;color:#C9D6F2;font-size:14px;margin-top:8px}}
.nota{{display:grid;gap:8px;padding:14px;border-radius:12px;background:{MANTA};border:1px solid var(--line);color:{AN}}} .nota b{{display:block;font-size:20px;line-height:1.2}} .nota p{{margin:0;color:#4a5274;font-size:14px}}
table{{border-collapse:collapse;width:100%;font-size:14px;font-variant-numeric:tabular-nums}} th,td{{text-align:right;padding:6px 8px;border-bottom:1px solid #ddd8cc}} th:first-child,td:first-child{{text-align:left}} th{{font-weight:600;color:#4a5274;font-size:12.5px}} td.up{{color:{AN2};font-weight:600}}
.leyenda{{display:grid;gap:4px;font-size:13.5px;color:var(--muted)}}
</style>
<div class="w"><div class="intro"><p class="ojo">Rediseño · ronda 8 · pares tipográficos · color: Añil</p><h1>Xila: primaria y secundaria</h1>
<p>Cinco pares. La primaria lleva la voz: lema, títulos de sección y el título de cada gráfica, que dice el hallazgo. La secundaria hace el trabajo: texto, ejes, etiquetas, tablas y botones, con cifras alineadas. Cada par se prueba en una portada, una gráfica completa y una tabla. El nombre sigue bordado.</p></div>
<div class="tres">{''.join(tarj(*p) for p in PARES)}</div></div>'''
open(os.path.join(D,'banco.html'),'w').write(HTML); print('ok')
