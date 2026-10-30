# NisaData · guía de marca. Uso: python3 gen-guia.py → guia.html
# Fuentes: ../nisadata-final (símbolo, logotipos, tema.json), ../nisadata-panel-r1/paleta.md (paleta de datos validada).
import json, os, re
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..')
GR, MA, W, MUTED, AZ, PE = '#1F2532', '#FF8A1F', '#FFFFFF', '#535B70', '#052A76', '#C2D225'
S1, S2, S3, OT = '#1d4ed8', '#9b3d8f', '#14b8a6', '#9AA1B1'
TEMA = json.load(open(os.path.join(NS, 'nisadata-final', 'tema.json')))
_n = [0]
def sv(ruta, h=None, color=None, extra=''):
    _n[0] += 1; u = f'-{_n[0]}'
    s = open(os.path.join(NS, ruta)).read().strip()
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="{m.group(1)}{u}"', s); s = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{m.group(1)}{u})', s)
    st = (f'height:{h}px;width:auto;' if h else '') + 'display:block;flex:none;max-width:100%' + (f';color:{color}' if color else '') + extra
    return s.replace('<svg ', f'<svg style="{st}" ', 1)
F = lambda n, h=None, **k: sv(f'nisadata-final/svg/{n}.svg', h, **k)
def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)

# construcción (misma geometría que nisadata-final/gen.py)
R, G = (10, 12, 14), 4; CEL = []; cx = 10 + R[0]
for i, r in enumerate(R):
    if i: cx += R[i - 1] + G + r
    for j in range(i + 1): CEL.append((cx, 96 - r - j * (2 * r + G), r, i == 2 and j == i))
cons = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{"#FFE3C7" if a else "#E7E9EF"}" stroke="{MA if a else "#8A93A8"}" stroke-width=".6" stroke-dasharray="2 1.5"/>'
               f'<text x="{x}" y="{y + 1.7}" font-size="5" text-anchor="middle" fill="{GR}">{r}</text>' for x, y, r, a in CEL)
cons = (f'<svg viewBox="0 -4 100 112" role="img" aria-label="Construcción del símbolo: tres columnas de células de radios 10, 12 y 14 con separación 4">{cons}'
        f'<line x1="2" y1="96" x2="98" y2="96" stroke="#8A93A8" stroke-width=".5"/><text x="50" y="104" font-size="4.6" text-anchor="middle" fill="{MUTED}">base común · separación 4</text></svg>')

# usos incorrectos sobre el símbolo real
_s = open(os.path.join(NS, 'nisadata-final', 'svg', 'simbolo.svg')).read()
def var_s(trans='', swap=None):
    s = swap(_s) if swap else _s
    return s.replace('<svg ', f'<svg style="height:80px;width:auto;display:block;{trans}" ', 1)
mal = [('Rotar las columnas', var_s('transform:rotate(90deg)')),
       ('Dos células mandarina', var_s(swap=lambda s: s.replace(f'fill="{GR}"/></svg>', f'fill="{MA}"/></svg>').replace(f'r="12.00" fill="{GR}"', f'r="12.00" fill="{MA}"', 1))),
       ('Cambiar el grafito por azul', var_s(swap=lambda s: s.replace(GR, AZ))),
       ('Mandarina como alerta', f'<span class="bad-chip">Pago vencido</span>'),
       ('Colores de área en una gráfica', '<span class="bad-bars"><i style="width:80%;background:#A14E78"></i><i style="width:55%;background:#008478"></i><i style="width:35%;background:#7A5DA9"></i></span>'),
       ('Mandarina como texto', f'<span style="font:700 30px Poppins,sans-serif;color:{MA}">NisaData</span>')]
malh = ''.join(f'<figure class="mal"><div>{s}</div><figcaption>{t}</figcaption></figure>' for t, s in mal)

def bar(lbl, v, col): return f'<div class="br"><span>{lbl}</span><span class="bt"><i style="width:{v}%;background:{col}"></i></span><b>{v}</b></div>'
ejemplo = bar('Aguas', 82, S1) + bar('Alimentos', 56, S1) + bar('Bebidas alcohólicas', 38, S1)
nav = ''.join(f'<span class="ni{" on" if a else ""}">{t}</span>' for t, a in (('Panel', True), ('Tendencias', False), ('Áreas', False), ('Calidad', False)))

html = f'''<title>Guía de marca NisaData</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Guía de un producto de analítica: blanco de papel, grafito para leer y una sola célula mandarina. Columnas de 1080 px; secciones separadas por línea. Tema claro deliberado, como la guía de NisaLab. */
:root{{--bg:#FFFFFF;--fg:{GR};--ma:{MA};--muted:{MUTED};--line:#DFE3EC;--sunk:#F3F4F7;--s1:{S1};--s2:{S2};--s3:{S3};--ot:{OT};color-scheme:light;
--display:Poppins,system-ui,sans-serif;--body:Poppins,system-ui,sans-serif;--data:"IBM Plex Mono",ui-monospace,monospace}}
body{{background:var(--bg);color:var(--fg);font:16px/1.65 var(--body);margin:0;padding-block:0 72px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1080px;margin:0 auto}}h1,h2,h3{{margin:0;text-wrap:balance}}h2{{font:700 28px/1.2 var(--display);letter-spacing:-.01em;margin-bottom:8px}}h3{{font:600 17px/1.3 var(--display);margin:24px 0 8px}}
p{{max-width:68ch;margin:0 0 12px}}.muted{{color:var(--muted)}}.num{{font:700 14px var(--display);color:var(--muted);display:block;margin-bottom:4px;font-variant-numeric:tabular-nums}}
.hero{{padding:52px clamp(20px,4vw,48px) 44px;margin-top:16px;border-radius:28px;background:var(--fg);color:#fff;display:grid;gap:18px}}.hero p{{font-size:18px;color:#C9CED8;margin:0}}.hero .ov{{color:#C9CED8}}
section{{padding:44px 0;border-bottom:1px solid var(--line)}}
.arq{{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:12px}}.arq div{{border:1px solid var(--line);border-radius:14px;padding:14px 16px}}.arq b{{display:block}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}.c{{border:1px solid var(--line);border-radius:18px;padding:22px;display:grid;place-items:center;gap:10px;min-width:0;min-height:120px}}.c.dk{{background:var(--fg);border-color:var(--fg)}}
.cap{{font-size:13px;color:var(--muted);text-align:center}}.c.dk .cap{{color:#C9CED8}}
.anat{{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);gap:28px;align-items:center}}.fig{{background:var(--sunk);border-radius:18px;padding:24px;display:grid;place-items:center}}.fig svg{{width:100%;height:auto;max-width:240px;font-family:var(--body)}}
ol,ul{{margin:0;padding-left:22px;display:grid;gap:8px}}
.sw{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}}.sw div{{border-radius:16px;padding:16px;min-height:130px;display:grid;align-content:end;gap:2px;font-size:14px;line-height:1.4;border:1px solid var(--line)}}.sw b{{font:700 16px var(--display)}}
.bar{{display:flex;height:22px;border-radius:999px;overflow:hidden;margin:14px 0 6px;border:1px solid var(--line)}}.bar i{{display:block}}
.tw{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;font-size:15px}}th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:middle}}th{{font-weight:600;background:var(--sunk);font-size:14px}}
.dot{{display:inline-block;width:14px;height:14px;border-radius:4px;margin-right:6px;vertical-align:-2px}}code{{font:13px var(--data);background:var(--sunk);padding:2px 6px;border-radius:6px}}
.type{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.spec{{border:1px solid var(--line);border-radius:16px;padding:20px;min-width:0}}.spec .big{{font-size:40px;line-height:1.15;margin:6px 0}}
.ov{{font:600 12px/1.4 var(--display);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.two{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.si,.nosi{{border-radius:14px;padding:16px 18px;font-size:15px}}.si{{background:#E9F3EC}}.nosi{{background:#FBEDEE}}.si b,.nosi b{{display:block;margin-bottom:6px}}
.ramp{{display:flex;border-radius:10px;overflow:hidden;height:34px;margin:8px 0}}.ramp i{{flex:1}}
.div{{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted)}}.div .ramp{{flex:1;margin:0}}
.br{{display:grid;grid-template-columns:minmax(0,150px) 1fr 40px;gap:12px;align-items:center;font-size:14px;padding:5px 0}}.bt{{height:14px}}.bt i{{display:block;height:100%;border-radius:0 4px 4px 0}}.br b{{font:600 13px var(--data);text-align:right}}
.chart{{border:1px solid var(--line);border-radius:16px;padding:18px 20px;max-width:520px}}.chart h4{{margin:0 0 8px;font:600 15px var(--display)}}
.login{{border:1px solid var(--line);border-radius:22px;padding:18px;min-width:0;display:grid;gap:12px;max-width:320px;width:100%;background:#fff;box-shadow:0 6px 16px rgba(31,37,50,.06)}}.login .f{{height:42px;border:1px solid #858DA3;border-radius:10px;padding:0 12px;display:flex;align-items:center;color:var(--muted);font-size:14px}}.login .b{{height:44px;border-radius:10px;background:var(--fg);color:#fff;display:grid;place-items:center;font-weight:600}}
.side{{background:var(--fg);border-radius:16px;padding:18px 14px;display:grid;gap:14px;width:100%;max-width:240px}}.ni{{color:#C9CED8;font:500 14px var(--body);padding:8px 12px;border-radius:8px;position:relative}}.ni.on{{background:rgba(255,255,255,.08);color:#fff}}.ni.on::before{{content:"";position:absolute;left:-14px;top:7px;bottom:7px;width:4px;border-radius:0 4px 4px 0;background:var(--ma)}}
.mal{{border:1px solid var(--line);border-radius:14px;padding:16px;display:grid;gap:10px;justify-items:center;overflow:hidden;margin:0}}.mal div{{height:90px;display:grid;place-items:center;width:100%}}.mal figcaption{{font-size:14px;font-weight:600}}.mal figcaption::before{{content:"✕ ";color:#B42318}}
.bad-chip{{background:var(--ma);color:var(--fg);font:600 14px var(--body);padding:6px 12px;border-radius:8px}}.bad-bars{{display:grid;gap:6px;width:80%}}.bad-bars i{{display:block;height:14px;border-radius:0 4px 4px 0}}
figure{{margin:0}}.files li,.pend li{{margin:2px 0}}
@media (max-width:700px){{.anat{{grid-template-columns:1fr}}.br{{grid-template-columns:minmax(0,110px) 1fr 36px}}}}
</style>
<main>
<header class="hero"><span class="ov">Guía de marca · v1 · panel de analítica de Nisa Nabani</span>{F('logotipo-respaldo-blanco', 96)}
<p>{TEMA["producto"]} Su símbolo son tres columnas de células que crecen: los datos del laboratorio vistos en el tiempo.</p></header>

<section><span class="num">01</span><h2>Arquitectura y nombre</h2>
<div class="arq"><div><b>Nisa Nabani</b><span class="muted">La empresa. Conserva su logo y su manual.</span></div><div><b>NisaLab</b><span class="muted">El sistema de laboratorio: donde se trabaja la muestra.</span></div><div><b>NisaData</b><span class="muted">El panel de analítica: donde se lee cómo va el laboratorio. Esta guía.</span></div></div>
<h3>Cómo se escribe</h3><p>«NisaData», junto y con dos mayúsculas. Nunca «Nisa Data», «NISADATA» ni «Nisadata». Cuando la empresa acompaña, va como respaldo: «de Nisa Nabani». NisaData y NisaLab son hermanos: comparten el patrón «Nisa» + palabra, la tipografía y el respaldo, y se distinguen por símbolo y color.</p></section>

<section><span class="num">02</span><h2>Símbolo: columnas de células</h2>
<div class="anat"><div class="fig">{cons}</div><div><ol>
<li><b>Tres columnas</b> de 1, 2 y 3 células: datos que crecen.</li>
<li><b>Las células crecen con la columna</b> (radios 10, 12 y 14) y la separación es siempre 4, como en Colonia: es el parentesco con NisaLab.</li>
<li><b>Una sola célula mandarina</b>, arriba de la columna alta: el dato que importa.</li>
<li><b>La base siempre abajo.</b> No se rota, no se reacomoda, no se agregan columnas.</li></ol></div></div>
<h3>Versiones</h3>
<div class="g"><div class="c">{F('simbolo', 96)}<span class="cap">Color. La versión principal.</span></div><div class="c dk">{F('simbolo-blanco', 96)}<span class="cap">Blanco y mandarina, sobre grafito.</span></div><div class="c">{F('simbolo-1tinta', 96, color=GR)}<span class="cap">Una tinta: documentos en blanco y negro, grabados.</span></div></div>
<h3>Tamaño mínimo y área de respeto</h3><p>Alrededor del símbolo y del logotipo se deja libre, como mínimo, el ancho de la columna alta. Tamaño mínimo: <b>16 px</b> en pantalla y <b>6 mm</b> impreso.</p></section>

<section><span class="num">03</span><h2>Logotipo</h2>
<div class="g"><div class="c">{F('logotipo', 52)}<span class="cap">Horizontal. Para casi todo.</span></div><div class="c">{F('logotipo-respaldo', 64)}<span class="cap">Con respaldo. Reportes para dirección y presentaciones.</span></div>
<div class="c">{F('logotipo-vertical', 120)}<span class="cap">Vertical. Pantalla de acceso, espacios cuadrados.</span></div>
<div class="c dk">{F('logotipo-blanco', 52)}<span class="cap">Blanco, sobre grafito. Menú lateral.</span></div><div class="c">{F('logotipo-1tinta', 52, color=GR)}<span class="cap">Una tinta.</span></div></div>
<p class="muted" style="margin-top:14px">«Nisa» en Poppins 700 y «Data» en Poppins 400. Los archivos traen el texto convertido a trazos; nunca se reescribe con la fuente.</p></section>

<section><span class="num">04</span><h2>Color de marca</h2>
<div class="sw"><div style="background:var(--fg);color:#fff;border-color:var(--fg)"><b>Grafito</b>{GR}<br>Símbolo, logotipo, menú y acción principal. Blanco encima {cr(W, GR)}:1.</div>
<div style="background:var(--ma);border-color:var(--ma)"><b>Mandarina</b>{MA}<br>Una célula del símbolo y la marca de sección activa. Grafito encima {cr(GR, MA)}:1.</div>
<div style="background:#fff"><b>Blanco</b>#FFFFFF<br>Superficies de las gráficas.</div><div style="background:var(--sunk)"><b>Niebla</b>#F3F4F7<br>Fondo de página.</div></div>
<div class="bar" aria-hidden="true"><i style="width:58%;background:var(--sunk)"></i><i style="width:20%;background:#fff"></i><i style="width:16%;background:var(--fg)"></i><i style="width:5%;background:var(--s1)"></i><i style="width:1%;background:var(--ma)"></i></div>
<p class="muted" style="font-size:14px">Proporción en una pantalla típica: niebla y blanco dominan; grafito para leer y navegar; los datos ponen el color; la mandarina es un detalle.</p>
<p>La mandarina nunca va como texto sobre blanco ({cr(MA, W)}:1) y nunca indica alerta ni estado: se parece al naranja de «Pago parcial» de NisaLab.</p></section>

<section><span class="num">05</span><h2>Tipografía</h2>
<div class="type"><div class="spec"><span class="ov">Primaria · Poppins</span><div class="big" style="font-weight:700">Tiempo de entrega</div><p class="muted">La misma de NisaLab y del manual de Nisa Nabani: títulos en 700 y 600; texto e interfaz en 400 y 500.</p></div>
<div class="spec"><span class="ov">Datos · IBM Plex Mono</span><div class="big" style="font-family:var(--data);font-weight:500;font-feature-settings:'zero'">3.6 días · 91 %</div><p class="muted">Ejes, valores y fechas: cifras de ancho fijo para que las columnas alineen.</p></div></div></section>

<section><span class="num">06</span><h2>Paleta de datos</h2>
<p>Los colores de las gráficas son distintos de los de marca. Cada color hace un solo trabajo, y la paleta se verificó con simulación de daltonismo (protanopia y deuteranopia) antes de aprobarla.</p>
<div class="tw"><table><thead><tr><th>Trabajo</th><th>Colores</th><th>Regla</th></tr></thead><tbody>
<tr><td><b>Series</b></td><td><span class="dot" style="background:var(--s1)"></span>Cobalto {S1}<br><span class="dot" style="background:var(--s2)"></span>Ciruela {S2}<br><span class="dot" style="background:var(--s3)"></span>Turquesa {S3}</td><td>En ese orden y máximo tres. La cuarta en adelante va a «Otros» (<span class="dot" style="background:var(--ot)"></span>{OT}) o a otra gráfica. Turquesa ({cr(S3, W)}:1) siempre con etiqueta.</td></tr>
<tr><td><b>Una sola medida</b></td><td><div class="ramp" aria-hidden="true">{"".join(f'<i style="background:{c}"></i>' for c in ("#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"))}</div></td><td>Rampa de cobalto, de claro a oscuro: más oscuro es más.</td></tr>
<tr><td><b>Contra la meta</b></td><td><div class="div"><span>Mejor</span><div class="ramp" aria-hidden="true"><i style="background:var(--s1)"></i><i style="background:#7a9de6"></i><i style="background:#e7e9ef"></i><i style="background:#c48bbd"></i><i style="background:var(--s2)"></i></div><span>Peor</span></div></td><td>Cobalto mejor, ciruela peor, gris en la meta. Nunca rojo y verde.</td></tr>
<tr><td><b>Estatus</b></td><td>Los de NisaLab</td><td>Solo en gráficas de estatus, en orden de etapa y con su nombre. «Cancelada» va aparte: junto a «Terminada», rojo y verde se confunden con daltonismo.</td></tr>
</tbody></table></div>
<h3>Las áreas se nombran, no se colorean</h3>
<p>Los ocho colores de área tienen la misma luminosidad a propósito: es lo que los hace funcionar como marca y lo que los inutiliza en una gráfica. Con deuteranopía, Farmacia y Bebidas de agave quedan a ΔE 0.6, cuando el mínimo es 8. En las gráficas, el área lleva su nombre y su ícono en gris, y la barra va en cobalto.</p>
<div class="chart"><h4>Carga por área</h4>{ejemplo}</div></section>

<section><span class="num">07</span><h2>Gráficas</h2><ul>
<li><b>Un solo eje.</b> Dos medidas con escalas distintas van en dos gráficas.</li>
<li><b>Trazos delgados:</b> líneas de 2 px, barras con la punta redondeada y la base recta, cuadrícula tenue.</li>
<li><b>Leyenda desde dos series</b> y etiqueta directa en el último punto. Nunca un número en cada punto.</li>
<li><b>El texto va en grafito o gris</b>, nunca en el color de la serie.</li>
<li><b>Al pasar el cursor</b> aparece el valor exacto, también con teclado. Las gráficas de líneas tienen «Ver tabla».</li>
<li><b>El color sigue a la cosa, no a su lugar:</b> si un filtro quita una serie, las demás conservan su color.</li></ul></section>

<section><span class="num">08</span><h2>Voz</h2>
<p>Un número siempre con su referencia: el periodo, la meta o el valor anterior. Decir qué cambió y por qué importa, en una línea. Los títulos de las gráficas son la pregunta que responden.</p>
<div class="two"><div class="si"><b>Así sí</b><ul><li>«Tiempo de entrega: 3.6 días · meta 4»</li><li>«¿Estamos sacando lo que entra?»</li><li>«Alimentos está 0.6 días por encima de la meta»</li></ul></div>
<div class="nosi"><b>Así no</b><ul><li>«3.6»</li><li>«Gráfica 1»</li><li>«¡Tu laboratorio está creciendo increíblemente!»</li></ul></div></div></section>

<section><span class="num">09</span><h2>Aplicaciones</h2>
<div class="g"><div class="c">{F('app-icon', 120, extra=';border-radius:26px')}<span class="cap">Ícono de app: símbolo blanco y mandarina sobre grafito.</span></div>
<div class="c"><div style="display:flex;gap:14px;align-items:flex-end">{F('favicon', 32)}{F('favicon', 24)}{F('favicon', 16)}</div><span class="cap">Favicon a 32, 24 y 16 px.</span></div>
<div class="c"><div class="login">{F('logotipo-respaldo', 38)}<div class="f">Correo</div><div class="f">Contraseña</div><div class="b">Entrar</div></div><span class="cap">Inicio de sesión.</span></div>
<div class="c"><div class="side">{F('logotipo-blanco', 26)}{nav}</div><span class="cap">Menú lateral: la mandarina marca la sección activa.</span></div></div></section>

<section><span class="num">10</span><h2>Usos incorrectos</h2><div class="g">{malh}</div>
<p class="muted" style="margin-top:12px">Tampoco: unir los logos de NisaLab y NisaData en una sola pieza, poner el símbolo sobre fotografías sin contraste, o usar grafito y mandarina como colores de series.</p></section>

<section><span class="num">11</span><h2>Archivos y pendientes</h2>
<ul class="files"><li><code>nisadata-final/</code>: símbolo, logotipos, ícono de app, favicon, PNG, <code>tema.json</code> y LEEME.</li>
<li><code>nisadata-panel-r1/</code>: pantalla principal de ejemplo y <code>paleta.md</code> con la paleta de datos validada.</li></ul>
<h3>Pendiente</h3><ul class="pend"><li>Búsqueda de anterioridades de «NisaData» ante el IMPI.</li><li>Modo oscuro de la paleta de datos.</li><li>Confirmar metas: 4 días de entrega y 95 % a tiempo.</li></ul></section>
</main>'''
open(os.path.join(H, 'guia.html'), 'w').write(html); print('ok')
