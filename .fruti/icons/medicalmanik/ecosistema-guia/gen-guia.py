# Ecosistema Manik · manual de marca. Uso: python3 gen-guia.py → guia.html
# Fuente de las decisiones: ../final (sellos, tema.json, LEEME) y ../design-system/project (README, tokens).
import json, re

F = '../final/svg/'
T = json.load(open('../final/tema.json'))
_n = [0]
def sv(n, h=None):
    """SVG con ids únicos por copia (clipPath/mask)."""
    _n[0] += 1; k = _n[0]
    s = open(F + n + '.svg').read()
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="{m.group(1)}-{k}"', s)
    s = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{m.group(1)}-{k})', s)
    return s if h is None else s.replace('<svg ', f'<svg style="height:{h}px;width:auto" ', 1)

PROD = [  # (archivo, nombre, para quién, rasgo, tipo)
    ('expediente', 'Expediente', 'médicos', 'pestaña de carpeta', 'silueta'),
    ('agenda', 'Agenda', 'asistentes', 'argollas de calendario', 'pieza separada'),
    ('compras', 'Compras', 'compras y facturación', 'borde dentado de ticket', 'silueta'),
    ('farmacia', 'Farmacia', 'farmacia', 'cruz', 'pieza separada'),
    ('impulsa', 'Impulsa', 'campañas de prevención y marketing', 'flecha que sale de la esquina', 'pieza separada'),
    ('grupos', 'Grupos', 'administradores de clínicas y hospitales', 'segunda tarjeta detrás', 'silueta'),
]
P = T['productos']

sellos = ''.join(
    f'<div class="c">{sv(a)}<b class="pn"><span>{n}</span> Manik</b><span class="cap">Para {para}. Rasgo: {r} ({t}).</span></div>'
    for a, n, para, r, t in PROD)
tabla = ''.join(
    f'<tr><td><span class="dot" style="background:{P[n]["hex"]}"></span>{n} Manik</td><td><code>app-{a}</code> {P[n]["hex"]}</td><td>{P[n]["contraste_blanco"]}:1</td><td>{P[n]["contraste_noche"]}:1</td></tr>'
    for a, n, *_ in PROD)
noche = ''.join(f'<span style="color:#fff">{sv(a + "-1tinta", 56)}</span>' for a, *_ in PROD)

LINEA = 'M-6 63 L13 63 L27 12 L49 86 L71 25 L84 64 L106 64'
mal = [
    ('Redibujar la línea para un producto', sv('agenda').replace(LINEA, 'M-6 63 L20 63 L35 30 L50 75 L65 40 L106 40')),
    ('Cruz de Farmacia en rojo', '#D62828'.join(sv('farmacia').rsplit('#1B7F52', 1))),
    ('Cian como color de producto', sv('expediente').replace('fill="#234899"', 'fill="#00BDD0"')),
    ('Rasgo que corta la línea', sv('grupos').replace('<svg ', '<svg style="transform:rotate(8deg)" ', 1).replace(LINEA, LINEA.replace('L49 86', 'L49 106'))),
    ('Degradados o sombras', sv('compras').replace('<svg ', '<svg style="filter:drop-shadow(6px 8px 4px rgba(0,0,0,.45))" ', 1)),
    ('Botón en el color del producto', '<span class="fakebtn">Guardar</span>'),
]
malh = ''.join(f'<figure class="mal"><div>{s}</div><figcaption>{t}</figcaption></figure>' for t, s in mal)

html = f'''<title>Ecosistema Manik · manual de marca</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700&display=swap">
<style>
/* Manual de la familia de herramientas clínicas con la identidad del directorio Manik: Urbanist, cian del pin y luz. Tema claro deliberado: el ecosistema no tiene tema oscuro. */
:root{{--bg:#FFFFFF;--canvas:#F5F7FB;--fg:#14213D;--muted:#4A5674;--line:#E1E6F0;--sunk:#EEF1F7;--manik:#234899;--manik-soft:#E9EDF5;--cian:#009BB0;--bruma:#F5FAFB;--luz-cian:#D3F0F4;--luz-calida:#FFEFD2;--noche:#0F1C3F;
--display:"Urbanist","Segoe UI",system-ui,sans-serif;--sans:"Atkinson Hyperlegible Next","Atkinson Hyperlegible",system-ui,sans-serif;color-scheme:light}}
body{{background:var(--bg);color:var(--fg);font:17px/1.6 var(--sans);margin:0;padding-block:0 72px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1080px;margin:0 auto}}
h1,h2,h3{{font-family:var(--display);font-weight:600;letter-spacing:-.02em;text-wrap:balance;margin:0}}
h1{{font-size:clamp(40px,7vw,72px);line-height:1.02;font-weight:300;letter-spacing:-.035em}} h2{{font-size:26px;line-height:1.2;margin-bottom:6px}} h3{{font-size:18px;margin:22px 0 8px}}
p{{max-width:68ch;margin:0 0 12px}} .muted{{color:var(--muted)}} .ov{{font:600 13px/1.4 var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.num{{font:600 14px var(--display);color:var(--manik);display:block;margin-bottom:4px}}
.hero{{padding:56px clamp(20px,4vw,48px) 44px;margin-top:16px;border-radius:28px;display:grid;gap:20px;background:radial-gradient(ellipse 55% 75% at 0% 0%,var(--luz-cian),transparent 70%),radial-gradient(ellipse 45% 70% at 100% 100%,var(--luz-calida),transparent 70%),var(--bruma)}}
.hero .row{{display:flex;flex-wrap:wrap;align-items:center;gap:18px}} .hero .row svg{{height:96px;width:auto;display:block}}
.hero .mos svg{{height:56px;width:auto;display:block}}
section{{padding:44px 0;border-bottom:1px solid var(--line)}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}
.c{{border:1px solid var(--line);border-radius:16px;padding:20px;display:grid;gap:10px;align-content:start;min-width:0;background:var(--bg)}}
.c svg{{max-width:100%;height:auto;display:block;max-height:110px;margin:auto}} .cap{{font-size:14px;color:var(--muted);line-height:1.4}}
.pn{{font:400 20px/1.2 var(--display);letter-spacing:-.01em}} .pn span{{font-weight:600}}
.arq{{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));margin-top:12px}} .arq div{{border:1px solid var(--line);border-radius:14px;padding:14px 16px}} .arq b{{font-family:var(--display)}}
.anat{{display:grid;grid-template-columns:minmax(0,260px) minmax(0,1fr);gap:28px;align-items:center}} .anat .fig{{background:var(--canvas);border-radius:18px;padding:30px}} .anat .fig svg{{width:100%;height:auto;display:block}}
.anat ol{{margin:0;padding-left:22px;display:grid;gap:8px}}
.noche{{background:var(--noche);border-radius:18px;padding:22px;display:flex;flex-wrap:wrap;gap:18px;align-items:center}}
.resp{{display:grid;place-items:center;background:var(--canvas);border-radius:18px;padding:28px}} .resp .box{{outline:2px dashed var(--manik);padding:22px}} .resp svg{{height:80px;width:auto;display:block}}
.two{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}
.sw{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}} .sw div{{border-radius:16px;padding:16px;min-height:130px;display:grid;align-content:end;gap:2px;font-size:14px;line-height:1.4;border:1px solid var(--line)}} .sw b{{font:600 16px var(--display)}}
.bar{{display:flex;height:22px;border-radius:999px;overflow:hidden;margin:14px 0 6px;border:1px solid var(--line)}} .bar i{{display:block}}
.tw{{overflow-x:auto}} table{{border-collapse:collapse;width:100%;font-size:15px;font-variant-numeric:tabular-nums}} th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}} th{{font-weight:600;background:var(--canvas)}}
.dot{{display:inline-block;width:12px;height:12px;border-radius:4px;margin-right:8px;vertical-align:-1px}}
.st{{display:inline-flex;align-items:center;gap:6px;border-radius:8px;padding:2px 10px;font-weight:600;font-size:15px}}
.type{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}} .spec{{border:1px solid var(--line);border-radius:16px;padding:20px}} .spec .big{{font-size:40px;line-height:1.15;margin:6px 0}}
.si,.nosi{{border-radius:14px;padding:16px 18px;font-size:16px}} .si{{background:#E8F2ED}} .nosi{{background:#F9ECED}} .si b,.nosi b{{font-family:var(--display);display:block;margin-bottom:6px}}
.si ul,.nosi ul{{margin:0;padding-left:20px;display:grid;gap:6px}}
.bar64{{height:64px;background:#fff;border:1px solid var(--line);border-radius:14px;display:flex;align-items:center;gap:12px;padding:0 16px;max-width:560px}}
.bar64 svg{{height:32px;width:auto;display:block}} .bar64 .pn{{font-size:18px}} .bar64 .mos{{margin-left:auto;display:grid;place-items:center;width:44px;height:44px;border-radius:12px;border:1px solid var(--line)}} .bar64 .mos svg{{height:24px}}
.tiles{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));max-width:720px}}
.tile{{border:1px solid var(--line);border-radius:18px;padding:16px;display:grid;gap:8px;background:#fff}} .tile svg{{height:44px;width:auto;display:block}} .tile small{{color:var(--muted);font-size:14px}}
.tile.h{{box-shadow:0 6px 18px rgba(20,33,61,.10)}}
.mal{{margin:0;border:1px solid var(--line);border-radius:14px;padding:16px;display:grid;gap:10px;justify-items:center;overflow:hidden}} .mal div{{height:90px;display:grid;place-items:center}} .mal svg{{height:80px;width:auto}}
.mal figcaption{{font-size:14px;color:#B3261E;font-weight:600;text-align:center}}
.fakebtn{{background:#C73A55;color:#fff;border-radius:10px;padding:10px 18px;font:600 16px var(--sans)}}
.files li{{margin:4px 0}} code{{font-size:14px;background:var(--sunk);padding:2px 6px;border-radius:6px}}
.pend li{{margin:6px 0}}
@media (max-width:700px){{.anat{{grid-template-columns:1fr}}}}
</style>
<main>
<header class="hero"><span class="ov">Manual de marca · v2 · herramientas clínicas de MedicalManik</span>
<div class="row">{sv('medicalmanik')}<h1>Ecosistema <b style="font-weight:600">Manik</b></h1></div>
<p class="muted">Las apps con las que una clínica u hospital atiende, agenda, compra, surte, comunica y administra. Una empresa, un sello y seis productos que se reconocen como familia: la misma M de pulso, cada una con su rasgo y su color.</p>
<div class="mos">{sv('ecosistema')}</div></header>

<section><span class="num">01</span><h2>Arquitectura y nombre</h2>
<div class="arq"><div><b>MedicalManik</b><br><span class="muted">La empresa y el sello madre: la M de pulso en el cuadro limpio.</span></div>
<div><b>«Producto» Manik</b><br><span class="muted">Cada herramienta: Expediente, Agenda, Compras, Farmacia, Impulsa y Grupos.</span></div>
<div><b>Ecosistema Manik</b><br><span class="muted">El conjunto. Su identificador es el mosaico de seis cuadros.</span></div>
<div><b>Manik</b><br><span class="muted">El directorio para pacientes. Tiene su propio manual.</span></div></div>
<p style="margin-top:14px"><b>Una sola identidad visual.</b> Las herramientas de la clínica usan la misma identidad que el directorio Manik en la marca, la portada, el inicio de sesión, el inicio del ecosistema y los títulos: Urbanist, el cian del pin y los fondos de luz. Dentro de cada app manda la legibilidad clínica: Atkinson en interfaz y datos, y el botón en azul Manik.</p>
<h3>Cómo se escribe</h3>
<p>Siempre «<b>Producto Manik</b>»: Expediente Manik, Agenda Manik. Nunca «Manik Expediente», «Expediente MM» ni «App de Agenda». En interfaz, el producto va en peso 600 y «Manik» en peso regular:</p>
<p class="pn" style="font-size:26px"><span>Expediente</span> Manik</p>
<p>La empresa se escribe «MedicalManik», junto y con dos mayúsculas.</p></section>

<section><span class="num">02</span><h2>El sello</h2>
<div class="anat"><div class="fig">{sv('medicalmanik')}</div><div><ol>
<li><b>La línea de pulso.</b> Una M que también es un latido. Es idéntica en los siete sellos y nunca se redibuja por producto.</li>
<li><b>El cuadro redondeado.</b> El contenedor común de toda la familia.</li>
<li><b>El rasgo del producto.</b> Vive en el borde del cuadro y nunca corta la línea: es una silueta (carpeta, ticket, tarjeta detrás) o una pieza separada por un corte transparente (argollas, cruz, flecha).</li>
<li><b>Sin rasgo = MedicalManik.</b> El cuadro limpio es la empresa.</li></ol></div></div></section>

<section><span class="num">03</span><h2>Los seis productos</h2>
<div class="g">{sellos}</div>
<p class="muted" style="margin-top:14px">El color de producto acompaña al nombre; nunca es la única señal. La cruz de Farmacia va siempre en el verde del producto: la cruz roja es un emblema protegido.</p></section>

<section><span class="num">04</span><h2>Versiones, tamaño y respeto</h2>
<h3>Una tinta</h3>
<p>Para fondos oscuros, sellos y grabados se usa la versión a una tinta (la línea queda calada). Sobre azul noche, los sellos a color no alcanzan 3:1; por eso ahí van en blanco:</p>
<div class="noche">{noche}</div>
<h3>Tamaño mínimo y área de respeto</h3>
<div class="two"><div class="resp"><div class="box">{sv('farmacia')}</div></div><div><p>Alrededor del sello se deja libre, como mínimo, <b>un cuarto de su ancho</b> en todos los lados. Ningún texto, borde o imagen entra en esa zona.</p><p>Tamaño mínimo: <b>24 px</b> en interfaz. Por debajo, los rasgos de producto dejan de distinguirse.</p></div></div></section>

<section><span class="num">05</span><h2>El identificador del ecosistema</h2>
<div class="two"><div class="resp">{sv('ecosistema', 120)}</div><div><p>Seis cuadros, uno por producto, en sus colores. Es el botón que abre el selector de apps desde cualquier herramienta y lleva de vuelta al inicio del ecosistema.</p><p>Es un <b>emblema fijo</b>: sigue teniendo seis cuadros aunque se sumen productos. El selector, en cambio, sí muestra todas las apps.</p><p class="muted">Retícula de 24, como un icono de interfaz. Existe a color y a una tinta.</p></div></div></section>

<section><span class="num">06</span><h2>Color</h2>
<p><b>Dos papeles que no se mezclan.</b></p>
<div class="two"><div class="c"><b style="font-family:var(--display)">Identidad: en qué app estás</b><span class="cap">El color de producto (<code>app-*</code>) va en el sello, en la tarjeta del inicio y del selector, y en el fondo suave al pasar el cursor.</span></div>
<div class="c"><b style="font-family:var(--display)">Interfaz: qué puedes hacer</b><span class="cap">La acción principal es azul Manik en todas las apps, y los estados son los mismos en todas. Así nadie reaprende al cambiar de app.</span></div></div>
<p style="margin-top:14px">Por qué: tres colores de producto se parecen a estados (Farmacia a éxito, Compras a aviso, Grupos a error). Un «Guardar» rojo en Grupos se leería como peligro.</p>
<h3>Productos</h3>
<div class="tw"><table><thead><tr><th>Producto</th><th>Token</th><th>Blanco encima</th><th>Sobre azul noche</th></tr></thead><tbody>{tabla}</tbody></table></div>
<h3>Interfaz y neutros</h3>
<div class="sw"><div style="background:var(--manik);color:#fff;border-color:var(--manik)"><b>Azul Manik</b>#234899<br>Acción principal, enlaces, foco.</div>
<div style="background:var(--fg);color:#fff;border-color:var(--fg)"><b>Tinta</b>#14213D<br>Texto. 15.97:1.</div>
<div style="background:#fff"><b>Superficie</b>#FFFFFF<br>Tarjetas, barras y menús.</div>
<div style="background:var(--canvas)"><b>Lienzo</b>#F5F7FB<br>Fondo de las apps, con sesgo al azul.</div>
<div style="background:var(--cian);color:var(--fg);border-color:var(--cian)"><b>Cian Manik</b>#009BB0<br>El cian del pin. Acento gráfico: nunca texto pequeño ni producto.</div>
<div style="background:var(--bruma)"><b>Bruma</b>#F5FAFB<br>Fondo de portada, inicio de sesión e inicio del ecosistema.</div>
<div style="background:var(--luz-cian);border-color:var(--luz-cian)"><b>Luz cian</b>#D3F0F4<br>Halo frío de fondo y círculo detrás de iconos.</div>
<div style="background:var(--luz-calida);border-color:var(--luz-calida)"><b>Luz cálida</b>#FFEFD2<br>Halo cálido, pareja de la luz cian.</div>
<div style="background:var(--noche);color:#fff;border-color:var(--noche)"><b>Noche</b>#0F1C3F<br>Planos oscuros puntuales y sellos a una tinta en blanco.</div></div>
<div class="bar" aria-hidden="true"><i style="width:60%;background:var(--canvas)"></i><i style="width:20%;background:#fff"></i><i style="width:12%;background:var(--fg)"></i><i style="width:6%;background:var(--manik)"></i><i style="width:2%;background:var(--cian)"></i></div>
<p class="cap">Proporción en una pantalla de trabajo: lienzo y superficie dominan; tinta para leer; azul para lo que se toca; el color de producto aparece solo en el sello y en el selector.</p>
<h3>Luz de marca</h3>
<p>Portada, inicio de sesión e inicio del ecosistema van sobre <b>bruma</b> con dos halos suaves, uno cian y uno cálido, igual que el directorio Manik. Dentro de las apps el fondo es el lienzo de trabajo: la luz es para dar la bienvenida, no para trabajar encima.</p>
<h3>Estados, iguales en todas las apps</h3>
<p><span class="st" style="background:#E8F2ED;color:#157C4A">Éxito</span> <span class="st" style="background:#F6EFE6;color:#A05C03">Aviso</span> <span class="st" style="background:#F9ECED;color:#BA3D4D">Error</span> <span class="st" style="background:#ECF1F4;color:#3D7291">Información</span></p>
<p class="muted">Siempre con icono y texto (Lucide: circle-check, triangle-alert, circle-x, info).</p></section>

<section><span class="num">07</span><h2>Tipografía</h2>
<div class="type"><div class="spec"><span class="ov">Primaria · Urbanist</span><div class="big" style="font-family:var(--display);font-weight:300;letter-spacing:-.03em">Buenos días, Dra. Ramírez</div><p class="muted">La letra del directorio Manik, así pacientes y clínicas ven la misma familia. 300 grande en portada e inicio; 600 en títulos y nombres de producto. Nunca en párrafos, tablas ni datos clínicos.</p></div>
<div class="spec"><span class="ov">Secundaria · Atkinson Hyperlegible Next</span><div class="big" style="font-weight:500;font-variant-numeric:tabular-nums">Paracetamol 500 mg · 1 c/8 h</div><p class="muted">Toda la interfaz y todo dato. Distingue 1, l e I; 0 y O; rn y m: en un expediente evita leer mal una dosis o una clave.</p></div></div>
<ul><li>Cifras tabulares en tablas, dosis y signos vitales.</li><li>Piso de 13 px: nada clínico por debajo.</li><li>Las dos en Google Fonts: <code>Urbanist:wght@300..700</code> y <code>Atkinson Hyperlegible Next:wght@400;500;600;700</code>.</li></ul></section>

<section><span class="num">08</span><h2>Voz</h2>
<p>Directa y clínica. El verbo dice lo que pasa; los errores dicen el límite. Trato de usted o por título profesional.</p>
<div class="two"><div class="si"><b>Así sí</b><ul><li>«Guardar receta»</li><li>«Surtir»</li><li>«Fuera de rango: máximo 100 mg al día»</li><li>«Buenos días, Dra. Ramírez»</li></ul></div>
<div class="nosi"><b>Así no</b><ul><li>«Procesar»</li><li>«Ocurrió un error»</li><li>«¡Hola, doc!»</li><li>«Operación realizada exitosamente en el sistema»</li></ul></div></div></section>

<section><span class="num">09</span><h2>Aplicaciones</h2>
<h3>Barra superior de una app</h3>
<div class="bar64">{sv('agenda')}<span class="pn"><span>Agenda</span> Manik</span><span class="mos" aria-hidden="true">{sv('ecosistema')}</span></div>
<p class="cap" style="margin-top:8px">64 px de alto, sobre superficie blanca. Sello a 32 px, nombre en Urbanist y el mosaico del ecosistema a la derecha para cambiar de app.</p>
<h3>Inicio y selector del ecosistema</h3>
<div class="tiles">{''.join(f'<div class="tile{" h" if i == 1 else ""}">{sv(a)}<span class="pn" style="font-size:17px"><span>{n}</span> Manik</span><small>Para {para}</small></div>' for i, (a, n, para, *_) in enumerate(PROD[:3]))}</div>
<p class="cap" style="margin-top:8px">Una tarjeta por app: sello, nombre y para quién es. Al pasar el cursor, una sombra corta (como en la segunda).</p></section>

<section><span class="num">10</span><h2>Usos incorrectos</h2><div class="g">{malh}</div>
<p class="muted" style="margin-top:12px">Tampoco: cambiar el color de un producto, usar el azul de Expediente para otro sello, poner sellos a color sobre azul noche, o escribir el nombre al revés («Manik Agenda»).</p></section>

<section><span class="num">11</span><h2>Archivos</h2><ul class="files">
<li><code>svg/&lt;producto&gt;.svg</code> y <code>&lt;producto&gt;-1tinta.svg</code> para medicalmanik, expediente, agenda, compras, farmacia, impulsa y grupos.</li>
<li><code>svg/ecosistema.svg</code> y <code>ecosistema-1tinta.svg</code>: el mosaico.</li>
<li><code>png/&lt;archivo&gt;-{{16,32,64,128,512}}.png</code> con transparencia.</li>
<li><code>tema.json</code>: colores, para quién es cada producto y contrastes medidos.</li></ul>
<h3>Pendiente</h3><ul class="pend">
<li>No hay logotipos de nombre por producto convertidos a trazos: hoy el nombre se compone con Urbanist en interfaz.</li>
<li>Manik Impulsa (en producción) difiere en tipografía (Ubuntu), color de acción (violeta) y lienzo (gris neutro). Falta decidir si se alinea.</li>
<li>Confirmar si existe un inicio de sesión único entre apps.</li>
</ul></section>
</main>'''
open('guia.html', 'w').write(html)
print('ok')
