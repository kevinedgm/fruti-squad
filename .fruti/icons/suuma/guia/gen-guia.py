import os
F='../final/svg/'
sv=lambda n:open(F+n+'.svg').read()
html=f'''<title>SUUMA · manual de marca</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Onest:wght@400;500;700&display=swap">
<style>
/* Manual de marca de una sola tinta: página blanca, tinta, cadmio como única nota. Columna de lectura de 68ch, piezas en rejilla. */
:root{{--bg:#FFFFFF;--papel:#F5F4F0;--fg:#121212;--muted:#5F5E5A;--line:#E3E2DD;--cadmio:#FFD400;--display:"Bricolage Grotesque",system-ui,sans-serif;--sans:"Onest",system-ui,sans-serif;color-scheme:light}}
body{{background:var(--bg);color:var(--fg);font:16px/1.55 var(--sans);margin:0;padding-block:0 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1040px;margin:0 auto}}
h1,h2,h3{{font-family:var(--display);font-weight:600;letter-spacing:-.01em;text-wrap:balance;margin:0}}
h1{{font-size:clamp(34px,6vw,56px);line-height:1.02}} h2{{font-size:26px;line-height:1.15;margin-bottom:12px}} h3{{font-size:18px;margin-bottom:6px}}
p{{max-width:68ch;margin:0 0 12px}} .muted{{color:var(--muted)}}
.hero{{padding:56px 0 36px;border-bottom:1px solid var(--line);display:grid;gap:22px}} .hero .wm{{max-width:520px}} .hero .wm svg{{width:100%;height:auto;display:block}}
.ov{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:500}}
section{{padding:40px 0;border-bottom:1px solid var(--line)}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}}
.c{{border:1px solid var(--line);border-radius:10px;padding:18px;display:grid;gap:10px;align-content:start;min-width:0}} .c.d{{background:var(--fg);color:#fff;border-color:var(--fg)}} .c.p{{background:var(--papel)}} .c.y{{background:var(--cadmio)}}
.c svg{{max-width:100%;height:auto;display:block;max-height:120px;margin:auto}} .c .cap{{font-size:13px}} .c.d .cap{{color:#bbb}}
.sw{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(150px,1fr))}} .sw div{{border-radius:10px;padding:14px;min-height:110px;display:grid;align-content:end;gap:2px;font-size:13px;border:1px solid var(--line)}} .sw b{{font-family:var(--display);font-size:16px}} .sw code{{font-family:ui-monospace,monospace;font-size:12px}}
table{{border-collapse:collapse;width:100%;font-size:14px}} th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}} th{{font-weight:600}} .tw{{overflow-x:auto}}
ul{{padding-left:20px;margin:0 0 12px}} li{{margin:4px 0;max-width:68ch}}
.two{{display:grid;gap:28px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}}
.type{{display:grid;gap:4px}} .type .b{{font-family:var(--display);font-size:44px;line-height:1;font-weight:600;letter-spacing:-.01em}} .type .o{{font-size:20px}}
.no{{display:grid;gap:8px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}} .no div{{border:1px solid var(--line);border-radius:8px;padding:12px 14px;font-size:14px}} .no div::before{{content:"✕ ";color:#C8102E;font-weight:700}}
</style>
<main>
<header class="hero"><span class="ov">Manual de marca · v1</span><div class="wm">{sv('wordmark')}</div><h1>Una u dentro de la otra.</h1><p class="muted">SUUMA conecta a profesionales independientes de belleza y cuidado personal con quienes los buscan. El nombre viene de «suma»; la segunda u no se escribe al lado: vive dentro de la primera. Cada quien conserva su forma y, juntas, hacen el nombre.</p></header>

<section><h2>Símbolo</h2><p>La doble U anidada es el símbolo y, a la vez, parte del wordmark. La u exterior es la u de la palabra; la interior es más fina, cuelga del mismo eje y se pinta en cadmio. Se usa sola en favicon, app icon, avatar y sellos.</p>
<div class="g"><div class="c">{sv('simbolo')}<span class="cap">Símbolo · tinta y cadmio</span></div><div class="c">{sv('simbolo-tinta')}<span class="cap">Una tinta</span></div><div class="c d">{sv('simbolo-blanco')}<span class="cap">Sobre tinta</span></div><div class="c y">{sv('app-icon-cadmio')}<span class="cap">Sobre cadmio: todo en tinta</span></div></div>
<p style="margin-top:14px"><b>Anatomía.</b> Cuenco exterior con el tallo de Bricolage Grotesque 600; interior al 60 % del grosor, ancho igual al cuenco menos dos tallos y medio, arranca al 60 % de la altura de x y termina 1.45 tallos por encima de la línea base. Esas proporciones no se ajustan a ojo: los archivos ya las traen.</p></section>

<section><h2>Wordmark y lockups</h2><p>«suma» en Bricolage Grotesque 600 (tamaño óptico 96, caja baja, tracking −1 %), en trazados: no depende de la fuente instalada. La segunda u se lee por el anidado, no por una letra extra.</p>
<div class="g"><div class="c">{sv('wordmark')}<span class="cap">Wordmark · mínimo 80 px de ancho</span></div><div class="c d">{sv('wordmark-oscuro')}<span class="cap">Sobre tinta</span></div><div class="c">{sv('lockup-h')}<span class="cap">Lockup horizontal · mínimo 140 px</span></div><div class="c">{sv('lockup-v')}<span class="cap">Lockup vertical · mínimo 90 px</span></div></div>
<div class="tw" style="margin-top:16px"><table><tr><th>Pieza</th><th>Uso</th><th>Mínimo</th><th>Archivo</th></tr>
<tr><td>Símbolo</td><td>Favicon, app icon, avatar, sello</td><td>16 px</td><td>simbolo · simbolo-tinta · simbolo-blanco</td></tr>
<tr><td>Wordmark</td><td>Documentos, firmas, cabecera</td><td>80 px</td><td>wordmark · wordmark-tinta · wordmark-oscuro</td></tr>
<tr><td>Lockup horizontal</td><td>Web, correo, cabecera de perfil</td><td>140 px</td><td>lockup-h · -oscuro · -tinta</td></tr>
<tr><td>Lockup vertical</td><td>Social, stickers, carteles</td><td>90 px</td><td>lockup-v · -oscuro</td></tr></table></div>
<p style="margin-top:12px"><b>Área de respeto:</b> la altura de la u interior, alrededor de toda pieza.</p></section>

<section><h2>Color</h2><p>Dos neutros y una nota. La tinta ordena, el blanco respira, el cadmio marca. El cadmio nunca es texto: va en la u interior, en fondos con texto en tinta, en chips y destacados. La acción primaria es tinta con texto blanco.</p>
<div class="sw"><div style="background:#121212;color:#fff;border-color:#121212"><b>Tinta</b><code>#121212</code><span>Texto, acción primaria, fondo oscuro</span></div><div style="background:#FFFFFF"><b>Blanco</b><code>#FFFFFF</code><span>Fondo y superficies</span></div><div style="background:#F5F4F0"><b>Papel</b><code>#F5F4F0</code><span>Superficies hundidas, tablas</span></div><div style="background:#FFD400"><b>Cadmio</b><code>#FFD400</code><span>La u interior, destacados, chips. Nunca texto.</span></div><div style="background:#FFF3B0"><b>Cadmio suave</b><code>#FFF3B0</code><span>Fondos marcados, filas activas</span></div><div style="background:#fff;color:#5F5E5A"><b>Texto secundario</b><code>#5F5E5A</code><span>Metadatos, ayudas (6.5:1)</span></div></div>
<div class="tw" style="margin-top:16px"><table><tr><th>Par</th><th>Ratio</th><th>Mínimo</th></tr><tr><td>Tinta sobre blanco</td><td>18.7:1</td><td>4.5</td></tr><tr><td>Tinta sobre cadmio</td><td>13.1:1</td><td>4.5</td></tr><tr><td>Texto secundario sobre blanco</td><td>6.5:1</td><td>4.5</td></tr><tr><td>Cadmio sobre tinta (acento)</td><td>13.1:1</td><td>3</td></tr><tr><td>Cadmio sobre blanco</td><td>1.4:1</td><td>no usar como texto ni control</td></tr></table></div>
<p class="muted" style="margin-top:10px">Éxito #0E7C4A y error #C8102E son provisionales hasta el design system; siempre con icono y texto.</p></section>

<section><h2>Tipografía</h2><div class="two"><div class="type"><span class="ov">Marca y títulos</span><span class="b">Bricolage Grotesque</span><p class="muted">600 para títulos; 700 solo en display grande. Tamaño óptico según el cuerpo. Una display por pantalla.</p></div><div class="type"><span class="ov">Interfaz y cuerpo</span><span class="o">Onest 400, 500 y 700. Neutra, abierta, 16 px mínimo en móvil.</span><p class="muted">Folios y datos: IBM Plex Mono 500 (provisional).</p></div></div></section>

<section><h2>App icon, favicon y avatar</h2><div class="g"><div class="c">{sv('app-icon')}<span class="cap">App icon · tinta, u blanca, interior cadmio</span></div><div class="c">{sv('app-icon-maskable')}<span class="cap">Maskable · margen 42 %</span></div><div class="c">{sv('app-icon-claro')}<span class="cap">Claro, para fondos oscuros del sistema</span></div><div class="c">{sv('avatar')}<span class="cap">Avatar en círculo</span></div></div>
<p style="margin-top:12px">El favicon cambia con el esquema del sistema: tinta en claro, blanco en oscuro, siempre con el interior en cadmio. PNG a 16, 32 y 48 más <code>favicon.ico</code>.</p></section>

<section><h2>Lo que no se hace</h2><div class="no"><div>Escribir «suuma» con dos u separadas en el wordmark.</div><div>Poner ojos, boca o cara a la u.</div><div>Usar el cadmio como color de texto o de borde de control.</div><div>Degradados, sombras, 3D o contornos en el símbolo.</div><div>Rellenar el interior con otro color que no sea cadmio, tinta o blanco.</div><div>Rotar, estirar o separar las dos u.</div></div></section>

<section style="border:0"><h2>Archivos</h2><p>SVG en <code>final/svg</code>, PNG en <code>final/png</code> (icon 1024/512/192, maskable, avatar, favicon 16/32/48 + .ico, wordmark y lockups a 240 px de alto, tarjeta de redes 1200×630). <code>tema.json</code> trae colores, tipografía y reglas en formato máquina; <code>pruebas.md</code>, los contrastes.</p></section>
</main>'''
open('guia.html','w').write(html); print('ok',len(html))
