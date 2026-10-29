# Manik · manual de marca. Uso: python3 gen-guia.py → guia.html
F = '../manik-final/svg/'
sv = lambda n: open(F + n + '.svg').read()
def var(s, tag):  # ids únicos por copia (clipPath/mask)
    for a in ['"m"', '"t"', '"w"', '"l"', '"lb"', '"l1"', '"le"', '"lv"', '"ai"', '"fv"']:
        s = s.replace('id=' + a, f'id="{a[1:-1]}{tag}"').replace(f'url(#{a[1:-1]})', f'url(#{a[1:-1]}{tag})')
    return s
SIM = sv('simbolo')
mal = [
 ('Cambiar el color', var(SIM, 'x1').replace('#009BB0', '#1B7F52')),
 ('Agregar degradados', var(SIM, 'x2').replace('fill="#009BB0"', 'fill="url(#gx)"').replace('<title>', '<defs><linearGradient id="gx" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#234899"/><stop offset="1" stop-color="#00BDD0"/></linearGradient></defs><title>')),
 ('Rotar o inclinar', var(SIM, 'x3').replace('<svg ', '<svg style="transform:rotate(-14deg)" ')),
 ('Deformar', var(SIM, 'x4').replace('<svg ', '<svg style="transform:scaleX(1.45)" ')),
 ('Sombras y efectos', var(SIM, 'x5').replace('<svg ', '<svg style="filter:drop-shadow(6px 8px 4px rgba(0,0,0,.45))" ')),
 ('Cambiar la línea por otro dibujo', var(SIM, 'x6').replace('M-6 63 L13 63 L27 12 L49 86 L71 25 L84 64 L106 64', 'M20 50 L80 50 M50 20 L50 80')),
]
malh = ''.join(f'<figure class="mal"><div>{s}</div><figcaption>{t}</figcaption></figure>' for t, s in mal)
FOTO = open('foto.html').read()
html = f'''<title>Manik · manual de marca</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Onest:wght@400..700&display=swap">
<style>
/* Manual de una marca para pacientes en la dirección bienestar: luz cian y cálida, Urbanist ligera y Onest, pin cian. Columna de 68ch y láminas en rejilla. Tema claro deliberado. */
:root{{--bg:#FFFFFF;--fg:#14213D;--cian:#009BB0;--cianui:#00788A;--muted:#4A5674;--line:#DCE4EA;--sunk:#F5FAFB;--wash:#EEF3F5;--sky:#D3F0F4;--sun:#FFEFD2;--azul:#234899;--estrella:#E3A21C;--noche:#0F1C3F;
--display:"Urbanist","Segoe UI",system-ui,sans-serif;--sans:"Onest","Segoe UI",system-ui,sans-serif;color-scheme:light}}
body{{background:var(--bg);color:var(--fg);font:17px/1.6 var(--sans);margin:0;padding-block:0 72px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1080px;margin:0 auto}}
h1,h2,h3{{font-family:var(--display);font-weight:600;letter-spacing:-.02em;text-wrap:balance;margin:0}}
h1{{font-size:clamp(40px,7vw,72px);line-height:1.02;font-weight:300;letter-spacing:-.035em}} h2{{font-size:clamp(28px,3.4vw,36px);line-height:1.1;font-weight:400;letter-spacing:-.03em;margin-bottom:8px}} h3{{font-size:18px;margin:18px 0 6px}}
p{{max-width:68ch;margin:0 0 12px}} .muted{{color:var(--muted)}} .ov{{font:600 13px/1.4 var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.num{{font:600 14px var(--display);color:var(--cianui);display:block;margin-bottom:4px}}
.hero{{padding:56px clamp(20px,4vw,48px) 44px;margin-top:16px;border-radius:28px;display:grid;gap:22px;background:radial-gradient(ellipse 55% 75% at 0% 0%,var(--sky),transparent 70%),radial-gradient(ellipse 45% 70% at 100% 100%,var(--sun),transparent 70%),var(--sunk)}} .hero .wm svg{{width:min(520px,100%);height:auto;display:block}}
.hero .lema{{font:300 clamp(30px,4.4vw,48px)/1.08 var(--display);letter-spacing:-.03em;color:var(--fg);margin:0}} .hero .lema b{{font-weight:600;color:var(--cianui)}}
section{{padding:44px 0;border-bottom:1px solid var(--line)}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}
.c{{border:1px solid var(--line);border-radius:16px;padding:20px;display:grid;gap:12px;align-content:start;min-width:0;background:var(--bg)}} .c.d{{background:var(--noche);border-color:var(--noche)}} .c.d .cap{{color:#C9D3EA}} .c.s{{background:var(--sunk)}}
.c svg{{max-width:100%;height:auto;display:block;max-height:130px;margin:auto}} .cap{{font-size:14px;color:var(--muted);line-height:1.4}}
.facts{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin:16px 0}} .facts div{{background:var(--sunk);border-radius:14px;padding:14px 16px}} .facts b{{display:block;font:600 13px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.arq{{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));margin-top:12px}} .arq div{{border:1px solid var(--line);border-radius:14px;padding:14px 16px}} .arq b{{font-family:var(--display)}}
.anat{{display:grid;grid-template-columns:minmax(0,240px) minmax(0,1fr);gap:28px;align-items:center}} .anat .fig{{background:var(--sunk);border-radius:18px;padding:36px;position:relative}}
.anat ol{{margin:0;padding-left:22px;display:grid;gap:8px}}
.resp{{display:grid;place-items:center;background:var(--sunk);border-radius:18px;padding:28px}} .resp .box{{outline:2px dashed var(--cianui);outline-offset:0;padding:22px;position:relative}} .resp svg{{height:80px;width:auto;display:block}}
.sw{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(180px,1fr))}} .sw div{{border-radius:16px;padding:16px;min-height:150px;display:grid;align-content:end;gap:2px;font-size:14px;line-height:1.4;border:1px solid var(--line)}} .sw b{{font:600 16px var(--display)}}
.bar{{display:flex;height:22px;border-radius:999px;overflow:hidden;margin:14px 0 6px}} .bar i{{display:block}}
.tw{{overflow-x:auto}} table{{border-collapse:collapse;width:100%;font-size:15px}} th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}} th{{font-weight:600;background:var(--sunk)}}
.type{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}} .spec{{border:1px solid var(--line);border-radius:16px;padding:20px}} .spec .big{{font-size:46px;line-height:1.1;margin:6px 0}}
.two{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}} .si,.nosi{{border-radius:14px;padding:16px 18px;font-size:16px}} .si{{background:#E6F4F6}} .nosi{{background:#F9ECED}} .si b,.nosi b{{display:block;font:600 14px var(--sans);margin-bottom:6px}} .si b{{color:var(--cianui)}} .nosi b{{color:#9C3443}}
.si ul,.nosi ul{{margin:0;padding-left:20px;display:grid;gap:6px}}
.apps{{background:radial-gradient(ellipse 60% 60% at 100% 0%,var(--sun),transparent 70%),var(--wash);border-radius:28px;padding:clamp(16px,3vw,28px);display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));align-items:start}}
.ficha{{border:1px solid var(--line);border-radius:24px;background:#fff;padding:20px;display:grid;gap:12px;max-width:420px}} .ficha .t{{display:flex;gap:12px}} .ficha .av{{width:56px;height:56px;border-radius:50%;background:var(--sky);color:var(--cianui);display:grid;place-items:center;font:600 18px var(--display);flex:none}}
.ficha h4{{margin:0;font:600 18px var(--display)}} .ficha small{{display:block;color:var(--muted);font-size:15px}} .stars{{font-size:15px}} .stars i{{font-style:normal;color:var(--estrella);letter-spacing:1px}}
.slots{{display:flex;gap:8px;flex-wrap:wrap;align-items:center;font-size:15px;color:var(--muted)}} .slots span{{border:1.5px solid var(--cianui);color:var(--cianui);background:#fff;border-radius:999px;padding:6px 14px;font-weight:600;font-variant-numeric:tabular-nums}}
.btnm{{background:var(--cianui);color:#fff;border-radius:999px;min-height:48px;display:grid;place-items:center;font:600 17px var(--sans)}}
.search{{border:1.5px solid #6B7590;background:#fff;border-radius:999px;padding:10px 10px 10px 20px;display:flex;gap:10px;align-items:center;font-size:17px;color:var(--muted);max-width:520px}} .search b{{margin-left:auto;background:var(--cianui);color:#fff;border-radius:999px;padding:10px 18px;font-weight:600}} .tag{{display:inline-flex;align-items:center;gap:6px;background:var(--sunk);border-radius:999px;padding:4px 10px;font-size:14px;color:var(--fg)}}
.phone{{width:260px;border-radius:34px;border:10px solid var(--fg);background:var(--sunk);padding:18px 14px;display:grid;gap:12px;justify-items:center}} .phone .ico{{width:76px;height:76px;border-radius:18px;overflow:hidden;box-shadow:0 2px 6px rgba(20,33,61,.15)}} .phone .ico svg{{width:100%;height:100%;display:block}} .phone small{{font-size:13px}}
.mal{{margin:0;border:1px solid var(--line);border-radius:14px;padding:16px;display:grid;gap:10px;justify-items:center;overflow:hidden}} .mal div{{height:90px;display:grid;place-items:center}} .mal svg{{height:80px;width:auto}} .mal figcaption{{font-size:14px;font-weight:600}} .mal figcaption::before{{content:"✕ ";color:#9C3443}}
.files li{{margin:4px 0}} code{{font-size:14px;background:var(--sunk);padding:2px 6px;border-radius:6px}}
.src{{font-size:14px;color:var(--muted)}} .src a{{color:var(--cianui)}}
.fotos{{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));align-items:start}} .fig2{{margin:0;display:grid;gap:8px}} .fig2 svg{{width:100%;height:auto;display:block;max-width:440px}}
.fotos th{{width:110px;background:var(--sunk)}} .reglas{{margin:0;padding-left:20px;display:grid;gap:8px}}
.up{{background:#fff;border:1px solid var(--line);border-radius:24px;padding:20px 22px;max-width:520px;box-shadow:0 1px 2px rgba(20,33,61,.05),0 6px 18px rgba(20,33,61,.06)}} .up .upt{{font:600 20px var(--display);margin:0 0 4px}} .up ol{{margin:0;padding-left:22px;display:grid;gap:6px}}
@media (max-width:700px){{.anat{{grid-template-columns:1fr}}}}
</style>
<main>
<header class="hero"><span class="ov">Manual de marca · v2 · directorio de pacientes de MedicalManik</span><div class="wm">{var(sv('logotipo-endoso'),'h')}</div>
<p class="lema">Tu médico, <b>a la mano</b>.</p>
<p class="muted">Manik es donde los pacientes encuentran a su especialista, ven sus opiniones y agendan una cita en línea. Es la cara pública del ecosistema MedicalManik: la misma M de pulso de las herramientas que usan las clínicas, ahora dentro de un pin que dice «aquí, cerca de ti».</p></header>

<section><span class="num">01</span><h2>Nombre</h2>
<p>«Manik» viene del maya. Lo que dicen las fuentes:</p>
<div class="facts"><div><b>Qué es</b>El séptimo día del Tzolk'in, el calendario maya de 260 días.</div><div><b>Su glifo</b>Una mano derecha semiempuñada, en actitud de agarrar.</div><div><b>Su asociación</b>El venado: en otras lenguas mesoamericanas ese día se llama «venado».</div><div><b>Lo que no se sabe</b>El significado exacto de la palabra sigue en discusión entre especialistas.</div></div>
<p>De la mano sale el lema: <b>tu médico, a la mano</b>, es decir, cerca y fácil. No le atribuimos a la palabra significados que las fuentes no respaldan (por ejemplo, «sanador»).</p>
<h3>Cómo se escribe</h3>
<p>En el logotipo, «manik» va en minúsculas. En un texto se escribe «Manik», con mayúscula inicial, sin apóstrofo y sin «Mi», «Directorio» u otras palabras delante.</p>
<h3>Lugar en la familia</h3>
<div class="arq"><div><b>MedicalManik</b><br><span class="muted">La empresa. Sello madre.</span></div><div><b>Expediente, Agenda, Compras… Manik</b><br><span class="muted">Las herramientas de la clínica: «Producto Manik».</span></div><div><b>Manik</b><br><span class="muted">Lo que conoce el paciente. Se respalda con «de MedicalManik».</span></div></div>
<p style="margin-top:14px"><b>Una sola identidad visual.</b> Las herramientas de la clínica comparten esta identidad en su marca, portada e inicio: Urbanist, el cian del pin y los fondos de luz. La diferencia está en el texto: aquí Onest, porque el paciente escanea y decide; en las herramientas, Atkinson, porque el médico lee dosis y claves.</p></section>

<section><span class="num">02</span><h2>Símbolo</h2>
<div class="anat"><div class="fig">{var(SIM,'a')}</div><div><ol><li><b>La línea de pulso.</b> Es idéntica en toda la familia MedicalManik: se forma una M que también es un latido. Nunca se redibuja.</li><li><b>El cuadro redondeado.</b> El mismo contenedor de las apps del ecosistema.</li><li><b>La punta.</b> El único rasgo propio de Manik: convierte el cuadro en un pin de ubicación, «aquí, cerca de ti».</li></ol></div></div>
<h3>Versiones</h3>
<div class="g"><div class="c">{var(SIM,'b')}<span class="cap">Color. La versión principal.</span></div><div class="c" style="color:var(--fg)">{var(sv('simbolo-1tinta'),'b')}<span class="cap">Una tinta: sellos, grabados, documentos en blanco y negro.</span></div><div class="c d">{var(sv('simbolo-blanco'),'b')}<span class="cap">Blanco, sobre fondos oscuros o fotografías oscuras.</span></div><div class="c s">{var(sv('favicon'),'b')}<span class="cap">Favicon y avatar de redes: el símbolo solo.</span></div></div>
<h3>Tamaño mínimo y área de respeto</h3>
<div class="two"><div class="resp"><div class="box">{var(SIM,'r')}</div></div><div><p>Alrededor del símbolo y del logotipo se deja libre, como mínimo, <b>un cuarto del ancho del símbolo</b> en todos los lados (la línea punteada). Ningún texto, borde o imagen entra en esa zona.</p><p>Tamaño mínimo: <b>24 px</b> en pantalla y <b>8 mm</b> de ancho impreso. Por debajo de eso, la punta del pin deja de leerse.</p></div></div></section>

<section><span class="num">03</span><h2>Logotipo</h2>
<div class="g"><div class="c">{var(sv('logotipo'),'c')}<span class="cap">Horizontal. Para la web, la app y casi todo.</span></div><div class="c">{var(sv('logotipo-endoso'),'c')}<span class="cap">Con respaldo. Cuando el contexto es institucional: convenios, materiales para clínicas, prensa.</span></div><div class="c">{var(sv('logotipo-vertical'),'c')}<span class="cap">Vertical. Espacios cuadrados o angostos: carteles, credenciales.</span></div><div class="c d">{var(sv('logotipo-blanco'),'c')}<span class="cap">En blanco sobre oscuro: el símbolo conserva su color.</span></div></div>
<p class="muted" style="margin-top:14px">El texto «manik» del logotipo es un dibujo: Sora 600 con el espaciado cerrado (−0.04 em), convertido a trazos. No cambia con la letra de la interfaz (Urbanist y Onest) y nunca se reescribe con una fuente: siempre se usan los archivos.</p></section>

<section><span class="num">04</span><h2>Color</h2>
<div class="sw"><div style="background:var(--cian);color:#fff;border-color:var(--cian)"><b>Cian Manik</b>#009BB0<br>El sello y las áreas grandes de marca.</div><div style="background:var(--cianui);color:#fff;border-color:var(--cianui)"><b>Cian interfaz</b>#00788A<br>Botones, enlaces y texto en cian.</div><div style="background:var(--fg);color:#fff;border-color:var(--fg)"><b>Tinta</b>#14213D<br>Texto y logotipo.</div><div style="background:var(--estrella)"><b>Calificación</b>#E3A21C<br>Solo las estrellas.</div><div style="background:var(--sunk)"><b>Bruma</b>#F5FAFB<br>Fondo de página y de tarjetas de categoría.</div><div style="background:var(--sky);border-color:var(--sky)"><b>Luz cian</b>#D3F0F4<br>Halo de fondo y círculo detrás de iconos.</div><div style="background:var(--sun);border-color:var(--sun)"><b>Luz cálida</b>#FFEFD2<br>Segundo halo, «Nuevo en Manik» y promociones.</div><div style="background:var(--azul);color:#fff;border-color:var(--azul)"><b>Azul MedicalManik</b>#234899<br>Solo en «de MedicalManik».</div></div>
<div class="bar" aria-hidden="true"><i style="width:40%;background:var(--sunk)"></i><i style="width:22%;background:#fff"></i><i style="width:10%;background:var(--sky)"></i><i style="width:6%;background:var(--sun)"></i><i style="width:12%;background:var(--fg)"></i><i style="width:8%;background:var(--cianui)"></i><i style="width:2%;background:var(--estrella)"></i></div>
<p class="cap">Proporción en una pantalla típica: bruma y blanco dominan; la luz cian y la cálida dan ambiente; tinta para leer; cian para lo que se toca; las estrellas son un detalle.</p>
<div class="tw"><table><thead><tr><th>Combinación</th><th>Contraste</th><th>Se puede usar para</th></tr></thead><tbody>
<tr><td>Blanco sobre cian Manik</td><td>3.3:1</td><td>El sello y textos grandes (24 px o más). No para botones.</td></tr>
<tr><td>Blanco sobre cian interfaz</td><td>5.2:1</td><td>Botones, etiquetas, cualquier texto.</td></tr>
<tr><td>Tinta sobre blanco</td><td>16:1</td><td>Todo el texto.</td></tr>
<tr><td>Estrellas sobre blanco</td><td>2.2:1</td><td>Solo como gráfico, siempre con el número escrito en tinta al lado («4.9»).</td></tr>
<tr><td>Cian interfaz sobre luz cian</td><td>4.3:1</td><td>Iconos dentro del círculo de luz. No para texto pequeño.</td></tr>
<tr><td>Tinta sobre luz cálida</td><td>14:1</td><td>Etiquetas como «Nuevo en Manik» y avisos de promoción.</td></tr></tbody></table></div>
<p style="margin-top:12px"><b>El sello nunca lleva degradado.</b> Es de un solo color para que se imprima, borde y selle igual en todos lados. La luz suave (de cian a cálido) vive solo en fondos y en fotografía.</p></section>

<section><span class="num">05</span><h2>Tipografía</h2>
<div class="type"><div class="spec"><span class="ov">Primaria · Urbanist</span><div class="big" style="font-family:var(--display);font-weight:300;letter-spacing:-.035em">Cuidarte ya no tiene que ser difícil.</div><p class="muted">Titulares y mensajes cortos: 300, grande y con el espaciado cerrado. Nombres de médicos, precios y categorías en 600. Es la misma letra de títulos de las herramientas de la clínica.</p></div>
<div class="spec"><span class="ov">Secundaria · Onest</span><div class="big" style="font-weight:500;font-variant-numeric:tabular-nums">Hoy 16:30 · $900</div><p class="muted">Todo lo demás: textos, horarios, precios, direcciones y opiniones. 17 px de base. Horarios y precios con cifras tabulares para que se alineen.</p></div></div>
<p class="muted" style="margin-top:12px">Se cargan de Google Fonts: <code>Urbanist:wght@300..700</code> y <code>Onest:wght@400..700</code>.</p></section>

<section><span class="num">06</span><h2>Voz</h2>
<p>Hablamos como una persona que conoce a buenos médicos y te ayuda a llegar con uno: de tú, claro y sin tecnicismos. Primero lo que el paciente necesita saber (quién, dónde, cuándo, cuánto cuesta); después, lo demás.</p>
<div class="two"><div class="si"><b>Así sí</b><ul><li>«Dermatólogos cerca de ti»</li><li>«Hoy tiene espacio a las 11:30»</li><li>«Te mandamos un recordatorio un día antes»</li><li>«124 pacientes opinaron sobre la Dra. Herrera»</li><li>«Busca por lo que sientes»</li><li>«Cuidarte ya no tiene que ser difícil»</li></ul></div>
<div class="nosi"><b>Así no</b><ul><li>«Directorio de profesionales de la salud»</li><li>«Disponibilidad en el slot 11:30»</li><li>«Su cita ha sido registrada exitosamente en el sistema»</li><li>«¡Los mejores doctores!» (prometer lo que no se puede medir)</li></ul></div></div></section>

<section><span class="num">07</span><h2>Aplicaciones</h2>
<div class="apps"><div><h3>Búsqueda</h3><div class="search">Qué necesitas · Dónde<b>Buscar</b></div>
<h3>Ficha de médico</h3><div class="ficha"><div class="t"><span class="av">LH</span><div style="flex:1;min-width:0"><h4 style="display:flex;justify-content:space-between;gap:12px">Dra. Lucía Herrera <span>$900</span></h4><small>Pediatra · a 1.2 km</small><span class="stars"><i aria-hidden="true">★</i> <b>4.9</b> <span class="muted">· 124 opiniones</span></span></div></div><div><span class="tag">Cédula verificada</span></div><div class="slots">Hoy <span>11:30</span><span>12:00</span><span>16:30</span></div><div class="btnm">Agendar</div></div>
<p class="cap" style="margin-top:10px">Fotografía de médicos y de marca: ver la sección 08.</p></div>
<div><h3>Ícono de app</h3><div class="phone"><span class="ico">{var(sv('app-icon'),'p')}</span><small>Manik</small></div><p class="cap" style="margin-top:10px">El símbolo sobre blanco, con aire alrededor. El nombre bajo el ícono es «Manik».</p></div></div></section>

{FOTO}
<section><span class="num">09</span><h2>Usos incorrectos</h2><div class="g">{malh}</div>
<p class="muted" style="margin-top:12px">Tampoco: poner el símbolo sobre fotografías sin contraste, separar la punta del cuadro, escribir «manik» con otra fuente, o usar el azul de Expediente para el sello.</p></section>

<section><span class="num">10</span><h2>Archivos</h2><ul class="files"><li><code>svg/simbolo.svg</code>, <code>simbolo-1tinta.svg</code>, <code>simbolo-blanco.svg</code>, <code>favicon.svg</code></li><li><code>svg/logotipo.svg</code>, <code>logotipo-endoso.svg</code>, <code>logotipo-vertical.svg</code>, <code>logotipo-blanco.svg</code>, <code>logotipo-1tinta.svg</code></li><li><code>svg/app-icon.svg</code> y <code>png/</code> de 16 a 512 px</li><li><code>tema.json</code>: colores y contrastes</li></ul>
<p class="src">Fuentes sobre Manik': <a href="https://journals.iai.spk-berlin.de/index.php/indiana/article/download/1672/1310/3630">Barrera Vásquez (Indiana)</a> · <a href="https://revistas-filologicas.unam.mx/estudios-cultura-maya/index.php/ecm/article/download/518/513">Acuña (Estudios de Cultura Maya, UNAM)</a> · <a href="https://en.wikipedia.org/wiki/Tzolk%CA%BCin">Tzolk'in</a>.</p>
<p class="src">Pendiente antes de publicar la marca: verificar registro de «Manik» y disponibilidad de manik.mx; confirmar con el área legal la sección de consentimiento y definir quién revisa los retratos.</p></section>
</main>'''
open('guia.html', 'w').write(html)
print('ok')
