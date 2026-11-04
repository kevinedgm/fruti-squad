# Kiwi · «Busca por lo que sientes» como sellos · r02 · dirección A elegida, en 3 tamaños con tokens del DS directorio Manik.
# Uso: python3 gen.py → propuesta.html. Pictogramas: Lucide reutilizados (trazo 2). Colores: solo tokens existentes.
import os, re, math
D = os.path.dirname(os.path.abspath(__file__))
L = '/root/.cache/fruti-uva/package/icons/'
ico = lambda n: ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse|polygon)[^>]*/>', open(L + n + '.svg').read()))
# Tokens del DS (build.py · P): fondos de categoría y tintas que ya existen
T = dict(tinta='#14213D', muted='#4A5674', bruma='#F5FAFB', blanco='#FFFFFF', linea='#DCE4EA', ui='#00788A', azul='#234899', icalido='#8A5A00',
         catc='#E4F5F7', catk='#FFF4E0', cata='#EEF2F8')
TRIADA = [('catc', 'ui'), ('catk', 'icalido'), ('cata', 'azul')]   # rota cada tres, como hoy
CATS = [('scan-face', 'Piel', 'Dermatología'), ('brain', 'Salud mental', 'Psicología y psiquiatría'), ('apple', 'Alimentación', 'Nutrición'),
        ('flower-2', 'Salud íntima', 'Ginecología y urología'), ('baby', 'Niñas y niños', 'Pediatría'), ('stethoscope', 'Chequeo general', 'Medicina general')]

def lum(h):
    c = [int(h[i:i+2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return round((la + .05) / (lb + .05), 2)
CONTRASTES = [(f, t, cr(T[t], T[f]), cr(T['tinta'], T[f])) for f, t in TRIADA]

svgi = lambda n, size, color, sw=2: f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ico(n)}</svg>'

# ---------- A · Sello circular con leyenda en arco
def selloA(i, c, pre=''):
    f, t = TRIADA[i % 3]; F, C = T[f], T[t]
    leyenda = f'{c[1].upper()} · {c[2].upper()} · '
    return (f'<button class="a-cat" style="--f:{F};--c:{C}"><svg class="a-sello" viewBox="0 0 140 140" aria-hidden="true">'
            f'<defs><path id="arc{pre}{i}" d="M70,70 m-50,0 a50,50 0 1,1 100,0 a50,50 0 1,1 -100,0"/></defs>'
            f'<circle cx="70" cy="70" r="68" fill="{F}"/><circle cx="70" cy="70" r="63" fill="none" stroke="{C}" stroke-width="1.5"/>'
            f'<g class="g-ley"><circle cx="70" cy="70" r="37" fill="#fff"/><circle cx="70" cy="70" r="37" fill="none" stroke="{C}" stroke-width="1.5" stroke-dasharray="2 3.2"/></g>'
            f'<g class="g-comp"><circle cx="70" cy="70" r="50" fill="#fff"/><circle cx="70" cy="70" r="50" fill="none" stroke="{C}" stroke-width="2" stroke-dasharray="2.5 4"/><g transform="translate(43 43) scale(2.25)">{svgi(c[0], 24, C, 1.8)}</g></g>'
            f'<text class="ley" font-family="Onest,sans-serif" font-size="11" font-weight="600" letter-spacing="1.4" fill="{C}"><textPath href="#arc{pre}{i}" startOffset="0" textLength="312" lengthAdjust="spacing">{leyenda * max(1, round(314 / (len(leyenda) * 8.0)))}</textPath></text>'
            f'<g class="g-ley" transform="translate(52 52) scale(1.5)">{svgi(c[0], 24, C)}</g></svg>'
            f'<span class="nom">{c[1]}</span><span class="esp">{c[2]}</span></button>')

# ---------- B · Estampilla con borde perforado
def selloB(i, c):
    f, t = TRIADA[i % 3]; F, C = T[f], T[t]
    return (f'<button class="b-cat" style="--f:{F};--c:{C}"><span class="b-estampa"><span class="b-in"><span class="b-num" aria-hidden="true">N.º 0{i+1}</span>'
            f'<span class="b-ic">{svgi(c[0], 40, C)}</span><span class="b-val" aria-hidden="true">MANIK</span></span></span>'
            f'<span class="nom">{c[1]}</span><span class="esp">{c[2]}</span></button>')

# ---------- C · Emblema: cada categoría con su propia silueta
def roseta(n, r1, r2, cx=60, cy=60):   # borde ondulado tipo sello de garantía
    pts = []
    for k in range(n * 2 * 6):
        a = 2 * math.pi * k / (n * 12); r = r1 + (r2 - r1) * (0.5 + 0.5 * math.cos(a * n))
        pts.append(f'{cx + r * math.sin(a):.2f},{cy - r * math.cos(a):.2f}')
    return 'M' + ' L'.join(pts) + 'Z'
def poligono(n, r, rot=0, cx=60, cy=60):
    return 'M' + ' L'.join(f'{cx + r * math.sin(2*math.pi*k/n + rot):.2f},{cy - r * math.cos(2*math.pi*k/n + rot):.2f}' for k in range(n)) + 'Z'
FORMAS = [('roseta', roseta(14, 50, 56)), ('flor', roseta(6, 42, 56)), ('hexágono', poligono(6, 55, math.pi/6)),
          ('roseta', roseta(10, 48, 56)), ('flor', roseta(5, 42, 56)), ('octágono', poligono(8, 55, math.pi/8))]
def selloC(i, c):
    f, t = TRIADA[i % 3]; F, C = T[f], T[t]; forma = FORMAS[i][1]
    return (f'<button class="c-cat" style="--f:{F};--c:{C}"><svg class="c-em" viewBox="0 0 120 120" aria-hidden="true">'
            f'<path d="{forma}" fill="{F}" stroke="{C}" stroke-width="1.5" stroke-linejoin="round"/><circle cx="60" cy="60" r="31" fill="#fff"/>'
            f'<g transform="translate(42 42) scale(1.5)">{svgi(c[0], 24, C)}</g></svg>'
            f'<span class="nom">{c[1]}</span><span class="esp">{c[2]}</span></button>')

# ---------- Actual (referencia)
def actual(i, c):
    f, t = TRIADA[i % 3]
    return (f'<button class="x-cat" style="--f:{T[f]}"><span class="x-ic">{svgi(c[0], 22, T["ui"])}</span><span><b>{c[1]}</b><small>{c[2]}</small></span></button>')

DIRS = [
 ('actual', 'Actual', 'Tarjeta de color con icono en un cuadro blanco.', 'Referencia: funciona, pero se parece a cualquier directorio.', actual),
 ('a', 'A · Sello circular', 'Doble anillo con la categoría escrita en arco y el pictograma al centro, como un sello de calidad.',
  'Hipótesis: el arco y el doble anillo se leen de inmediato como «sello» y transmiten respaldo. Riesgo: la leyenda en arco es decorativa y pequeña (oculta para lector de pantalla); el nombre real va debajo.', selloA),
 ('b', 'B · Estampilla', 'Borde perforado de timbre postal, número de serie y pictograma grande.',
  'Hipótesis: lo más cálido y coleccionable; invita a tocar. Riesgo: el tono lúdico puede restar seriedad médica.', selloB),
 ('c', 'C · Emblema con silueta propia', 'Cada categoría tiene su forma: roseta, flor, hexágono, octágono. El borde ondulado es el de un sello de garantía.',
  'Hipótesis: la identidad viene de la silueta; se reconoce cada categoría sin leer. Riesgo: más piezas que mantener (una forma por categoría nueva).', selloC),
]

CSS = f'''
:root{{--tinta:{T['tinta']};--muted:{T['muted']};--bruma:{T['bruma']};--blanco:#fff;--linea:{T['linea']};--ui:{T['ui']};
  --display:"Urbanist",ui-sans-serif,system-ui,sans-serif;--sans:"Onest",ui-sans-serif,system-ui,sans-serif}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bruma);color:var(--tinta);font:16px/1.5 var(--sans)}}
.wrap{{max-width:1240px;margin:0 auto;padding:24px max(16px,env(safe-area-inset-left,0px)) 64px}}
header h1{{font:300 clamp(30px,6vw,46px)/1.05 var(--display);letter-spacing:-.03em;margin:0 0 8px}}header h1 b{{font-weight:600}}
header p{{margin:0;color:var(--muted);max-width:70ch}}
.meta{{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 0}}.meta span{{background:var(--blanco);border:1px solid var(--linea);border-radius:999px;padding:4px 12px;font-size:13px}}
.dir{{margin-top:36px;display:grid;gap:14px}}.dir>h2{{margin:0;font:600 24px/1.2 var(--display)}}.dir>p{{margin:0;color:var(--muted);max-width:75ch}}.hip{{font-size:14px;border-left:3px solid var(--ui);padding-left:10px}}
.pantallas{{display:grid;gap:20px;align-items:start}}@media (min-width:1000px){{.pantallas{{grid-template-columns:390px minmax(0,1fr)}}}}
.marco{{background:var(--blanco);border:1px solid var(--linea);border-radius:28px;padding:20px 16px;display:grid;gap:14px;min-width:0}}
.marco .et{{font:600 12px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.marco h3{{margin:0;font:400 28px/1.1 var(--display);letter-spacing:-.03em}}.marco h3 b{{font-weight:600}}.marco .sub{{margin:-6px 0 0;color:var(--muted);font-size:15px}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}}
.esc .grid{{grid-template-columns:repeat(3,minmax(0,1fr))}}@media (min-width:1100px){{.esc .grid{{grid-template-columns:repeat(6,minmax(0,1fr))}}}}
button{{font:inherit;color:inherit;cursor:pointer}}button:focus-visible{{outline:3px solid var(--ui);outline-offset:3px}}
.nom{{display:block;font:600 17px/1.15 var(--display);text-align:center}}.esp{{display:block;font-size:13px;line-height:18px;color:var(--muted);text-align:center}}
/* Actual */
.x-cat{{display:grid;gap:22px;align-content:space-between;text-align:left;border:0;border-radius:24px;padding:16px;min-height:150px;background:var(--f)}}
.x-ic{{display:grid;place-items:center;width:48px;height:48px;border-radius:16px;background:#fff}}.x-cat b{{font:600 19px/1.15 var(--display);display:block}}.x-cat small{{color:var(--muted);font-size:14px}}
/* A */
.a-cat{{display:grid;justify-items:center;gap:4px;background:none;border:0;padding:6px 2px 10px;border-radius:20px;transition:transform .25s ease}}
.a-sello{{width:min(100%,132px);height:auto;margin-bottom:6px;transition:transform .35s ease}}.a-cat:hover .a-sello{{transform:rotate(-8deg)}}
/* B */
.b-cat{{display:grid;justify-items:center;gap:4px;background:none;border:0;padding:4px 0 10px}}
.b-estampa{{width:min(100%,124px);aspect-ratio:4/5;padding:7px;background:radial-gradient(circle at 7px 7px,var(--bruma) 4px,transparent 4.6px) -7px -7px/14px 14px,#fff;filter:drop-shadow(0 2px 6px rgba(20,33,61,.12));margin-bottom:8px;transition:transform .25s ease;rotate:-2deg}}
.b-cat:nth-child(even) .b-estampa{{rotate:2deg}}.b-cat:hover .b-estampa{{transform:translateY(-4px) rotate(2deg)}}
.b-in{{display:grid;grid-template-rows:auto 1fr auto;justify-items:center;align-items:center;height:100%;background:var(--f);border:1.5px solid var(--c);padding:8px 6px}}
.b-num{{font:600 10px var(--sans);letter-spacing:.12em;color:var(--c)}}.b-val{{font:700 10px var(--display);letter-spacing:.3em;color:var(--c)}}
/* C */
.c-cat{{display:grid;justify-items:center;gap:4px;background:none;border:0;padding:6px 2px 10px}}
.c-em{{width:min(100%,120px);height:auto;margin-bottom:6px;transition:transform .3s ease}}.c-cat:hover .c-em{{transform:scale(1.05) rotate(6deg)}}
@media (prefers-reduced-motion:reduce){{*{{transition:none!important}}.a-cat:hover .a-sello,.b-cat:hover .b-estampa,.c-cat:hover .c-em{{transform:none}}}}
table{{border-collapse:collapse;font-size:14px;background:#fff;border:1px solid var(--linea);border-radius:16px;overflow:hidden}}td,th{{padding:8px 12px;border-bottom:1px solid var(--linea);text-align:left}}
.sw{{display:inline-block;width:14px;height:14px;border-radius:4px;vertical-align:-2px;border:1px solid var(--linea);margin-right:6px}}
'''
CSS += """
.a-cat{container-type:inline-size;width:100%}
.a-sello{width:min(100%,var(--s,132px))}
@container (max-width:104px){.ley{display:none}}
.g-comp{display:none}.t-s .ley,.t-s .g-ley{display:none}.t-s .g-comp{display:inline}
@container (max-width:104px){.g-ley{display:none}.g-comp{display:inline}}
.tam{display:grid;gap:12px}.tam .grid{gap:8px 10px}
.t-s .grid{grid-template-columns:repeat(3,minmax(0,1fr))}.t-s .nom{font-size:15px}.t-s .esp{font-size:12px;line-height:16px}.t-s{--s:88px}
.t-m .grid{grid-template-columns:repeat(3,minmax(0,1fr))}.t-m{--s:112px}
.t-l .grid{grid-template-columns:repeat(6,minmax(0,1fr))}.t-l{--s:132px}
.f390{max-width:390px}.f834{max-width:834px}
.medida{font-size:13px;color:var(--muted)}
.lado{display:grid;gap:20px;align-items:start}@media (min-width:900px){.lado{grid-template-columns:390px 390px}}
.escala{display:flex;flex-wrap:wrap;gap:24px;align-items:end}.escala figure{margin:0;display:grid;justify-items:center;gap:6px;font-size:13px;color:var(--muted)}
"""
def marco(clase, ancho, titulo, pre, nota):
    cel = ''.join(selloA(i, c, pre) for i, c in enumerate(CATS))
    return (f'<div class="marco tam {clase} {ancho}" aria-label="{titulo}"><span class="et">{titulo}</span><h3>Busca por <b>lo que sientes</b></h3>'
            f'<p class="sub">Si no sabes a qué especialista ir, empieza por aquí.</p><div class="grid">{cel}</div><p class="medida">{nota}</p></div>')
def escala():
    figs = ''.join(f'<figure><div class="tam {k}" style="width:{w}px">{selloA(0, CATS[0], "e"+k)}</div><figcaption>{t} · {w} px</figcaption></figure>' for k, w, t in (('t-s', 88, 'Compacto'), ('t-m', 112, 'Mediano'), ('t-l', 132, 'Grande')))
    return f'<div class="escala">{figs}</div>'
def antes():
    cel = ''.join(selloA(i, c, 'r1') for i, c in enumerate(CATS))
    return f'<div class="marco f390" style="--s:132px" aria-label="Ronda 1"><span class="et">Ronda 1 · celular</span><div class="grid">{cel}</div><p class="medida" id="m-r1"></p></div>'
filas = ''.join(f'<tr><td><span class="sw" style="background:{T[f]}"></span>{f}</td><td><span class="sw" style="background:{T[t]}"></span>{t}</td><td>{a}:1</td><td>{b}:1</td></tr>' for f, t, a, b in CONTRASTES)
html = f'''<title>Sellos en tres tamaños</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Onest:wght@400..700&display=swap">
<style>{CSS}</style>
<script>document.documentElement.lang='es'</script>
<main class="wrap"><header><h1>Sello circular en <b>tres tamaños</b></h1>
<p>Ronda 2 de las categorías de «Busca por lo que sientes»: la dirección A (sello circular) elegida en la ronda 1, con un tamaño para cada pantalla, más chico en celular.</p>
<div class="meta"><span>Dirección A elegida</span><span>Tokens del DS (sin colores nuevos)</span><span>Pictogramas Lucide reutilizados</span><span>Datos: categorías reales del inicio</span></div></header>
<section class="dir" aria-labelledby="t-esc"><h2 id="t-esc">La escala: tres tamaños</h2><p>El sello cambia de contenido, no solo de tamaño: por debajo de unos 104 px la leyenda del arco quedaría en menos de 8 px y no se podría leer, así que el compacto conserva el doble anillo y el pictograma, sin texto en el arco.</p>{escala()}</section>
<section class="dir" aria-labelledby="t-cel"><h2 id="t-cel">Celular: compacto, 3 por fila</h2><p>Antes, 2 por fila con sellos de 132 px; ahora, 3 por fila con sellos de 88 px. La sección ocupa casi la mitad de alto y se ven las 6 categorías sin bajar.</p>
<div class="lado">{antes()}{marco('t-s','f390','Ronda 2 · celular 390 px','s','')}</div></section>
<section class="dir" aria-labelledby="t-tab"><h2 id="t-tab">Tableta: mediano, 3 por fila</h2>{marco('t-m','f834','Tableta 834 px','m','Sello de 112 px con leyenda.')}</section>
<section class="dir" aria-labelledby="t-escr"><h2 id="t-escr">Escritorio: grande, 6 en una fila</h2>{marco('t-l','','Escritorio','l','Sello de 132 px con leyenda.')}</section>
<section class="dir" aria-labelledby="t-acc"><h2 id="t-acc">Accesibilidad y reglas comunes</h2>
<p>En las tres direcciones el nombre de la categoría y la especialidad son texto real debajo del sello (es lo que lee el lector de pantalla y lo que se amplía); lo escrito dentro del sello es decorativo. El área táctil es toda la tarjeta (más de 120 × 150 px). El movimiento al pasar el cursor se apaga con «reducir movimiento».</p>
<table><thead><tr><th>Fondo</th><th>Tinta del sello</th><th>Tinta / fondo</th><th>Texto tinta / fondo</th></tr></thead><tbody>{filas}</tbody></table></section>
</main>'''
html += "\n<script>addEventListener('load',()=>{const g=[...document.querySelectorAll('.lado .grid')].map(x=>Math.round(x.getBoundingClientRect().height));const ps=document.querySelectorAll('.lado .medida');if(g.length===2){ps[0].textContent='Alto de las 6 categorías: '+g[0]+' px';ps[1].textContent='Alto de las 6 categorías: '+g[1]+' px';}})</script>"
open(os.path.join(D, 'propuesta.html'), 'w').write(html)
print('ok', CONTRASTES)
