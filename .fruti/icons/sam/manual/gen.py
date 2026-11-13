# SAM · manual de marca (artifact). Genera manual.html con los SVG finales embebidos.
import os, re
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final')
def leer(n): return open(os.path.join(F, n)).read()
def interior(s): return s[s.index('>', s.index('<svg')) + 1: s.rindex('</svg>')]
def vb(s): return re.search(r'viewBox="([^"]+)"', s).group(1)
def svg(n, w=None, h=None, cls='', label='SAM', extra=''):
    s = leer(n); i = re.sub(r'<title>.*?</title>', '', interior(s))
    dims = (f' width="{w}"' if w else '') + (f' height="{h}"' if h else '')
    return f'<svg viewBox="{vb(s)}"{dims} class="{cls}" role="img" aria-label="{label}"{extra}>{i}</svg>'
C2, C4 = 'sam-simbolo.svg', 'sam-simbolo-chico.svg'
LOGO = 'SAM, Simple Activity Manager'
# Variantes incorrectas
bruto = re.sub(r'<title>.*?</title>', '', interior(leer(C2)))
sin_contorno = bruto.replace('stroke="currentColor" stroke-width="2.6"/>\n  <path', 'stroke="none"/>\n  <path', 1)
html = f'''<title>Manual de marca SAM</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap">
<style>
/* Layout: manual en bandas; cada sección es una lámina con su regla a la izquierda y la muestra a la derecha. Los tokens son los de la marca. */
:root{{
  --noche:#0a0a0b; --papel:#f2f2ee; --voltaje:#c6f432; --tinta:#0a0a0b;
  --bg:var(--papel); --fg:#0a0a0b; --muted:#55555c; --linea:#d6d6d0; --sup:#ffffff; --sup2:#e8e8e2;
  --font:"Onest",ui-sans-serif,system-ui,sans-serif; --mono:"JetBrains Mono",ui-monospace,monospace;
  --g-color-brand:var(--voltaje); --sam-tinta:var(--tinta);
}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#0a0a0b;--fg:#f2f2ee;--muted:#a3a3a8;--linea:#2a2a30;--sup:#16161a;--sup2:#1f1f24;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0a0a0b;--fg:#f2f2ee;--muted:#a3a3a8;--linea:#2a2a30;--sup:#16161a;--sup2:#1f1f24;color-scheme:dark}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--fg);font:400 16px/1.55 var(--font)}}
.w{{max-width:1120px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
h1,h2,h3{{text-wrap:balance;margin:0;letter-spacing:-.015em}}
h2{{font-size:clamp(28px,4vw,40px);line-height:1.1;font-weight:700}} h3{{font-size:18px;font-weight:600}}
p{{margin:0;max-width:62ch}} .muted{{color:var(--muted)}}
code,.mono{{font-family:var(--mono);font-size:.86em}}
.eti{{font:500 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
/* Portada: siempre en noche, como el icono de la app */
.portada{{background:var(--noche);color:#f2f2ee;--sam-tinta:#0a0a0b}}
.portada .w{{padding-block:56px 48px;display:grid;gap:40px}}
.portada .logo{{color:#f2f2ee;width:min(360px,80%);height:auto}}
.portada p{{font-size:clamp(18px,2.4vw,22px);color:#cfcfca;max-width:40ch}}
.portada .datos{{display:flex;flex-wrap:wrap;gap:8px 24px;font:500 13px var(--mono);color:#a3a3a8}}
nav.indice{{border-bottom:1px solid var(--linea)}}
nav.indice ul{{list-style:none;margin:0;padding:12px 0;display:flex;flex-wrap:wrap;gap:4px 18px}}
nav.indice a{{color:var(--fg);text-decoration:none;font-weight:500;font-size:14px;padding:6px 0;display:inline-block}}
nav.indice a:hover{{text-decoration:underline;text-underline-offset:4px}}
section.lam{{border-bottom:1px solid var(--linea)}}
section.lam>.w{{padding-block:56px;display:grid;grid-template-columns:minmax(0,4fr) minmax(0,7fr);gap:32px 48px;align-items:start}}
.regla{{display:grid;gap:14px}}
.muestra{{display:grid;gap:16px;min-width:0}}
@media (max-width:820px){{section.lam>.w{{grid-template-columns:1fr;padding-block:40px}}}}
.caja{{background:var(--sup);border:1px solid var(--linea);border-radius:10px;padding:24px;min-width:0}}
.caja.noche{{background:var(--noche);color:#f2f2ee;border-color:#2a2a30}} .caja.papel{{background:var(--papel);color:#0a0a0b;border-color:#d6d6d0}}
.fila{{display:flex;flex-wrap:wrap;gap:16px;align-items:center}}
.par{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}} @media (max-width:560px){{.par{{grid-template-columns:1fr}}}}
:focus-visible{{outline:3px solid var(--fg);outline-offset:3px;border-radius:4px}}
/* Símbolo: anatomía */
.anat{{display:grid;grid-template-columns:auto minmax(0,1fr);gap:24px;align-items:center}} @media (max-width:560px){{.anat{{grid-template-columns:1fr}}}}
.anat ol{{margin:0;padding-left:20px;display:grid;gap:8px}}
.tams{{display:flex;gap:20px;align-items:flex-end;flex-wrap:wrap}} .tams figure{{margin:0;display:grid;justify-items:center;gap:6px}} .tams figcaption{{font:500 12px var(--mono);color:var(--muted)}}
.proteccion{{position:relative;display:inline-grid;padding:22px;outline:1.5px dashed var(--muted);outline-offset:-1px}}
/* Color */
.colores{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}} @media (max-width:640px){{.colores{{grid-template-columns:1fr}}}}
.col{{border-radius:10px;border:1px solid var(--linea);overflow:hidden;background:var(--sup)}}
.col .sw{{height:110px}} .col .tx{{padding:14px 16px;display:grid;gap:2px}} .col b{{font-weight:600}}
table{{width:100%;border-collapse:collapse;font-size:14px}} th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--linea);vertical-align:top}}
th{{font-weight:600;color:var(--muted);font-size:12px;letter-spacing:.06em;text-transform:uppercase}} td.n{{font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}}
.tabla{{overflow-x:auto}}
.ok,.no{{font:600 13px var(--font);display:inline-flex;gap:6px;align-items:center}}
.ok::before{{content:"✓";font-weight:700}} .no::before{{content:"✕";font-weight:700}}
/* Tipografía */
.escala{{display:grid;gap:14px}} .escala div{{display:grid;grid-template-columns:110px minmax(0,1fr);gap:16px;align-items:baseline;border-bottom:1px solid var(--linea);padding-bottom:12px}}
@media (max-width:560px){{.escala div{{grid-template-columns:1fr;gap:4px}}}}
/* Aplicaciones */
.btn{{font:600 15px var(--font);border:0;border-radius:6px;min-height:44px;padding:0 18px;background:var(--voltaje);color:#0a0a0b;cursor:pointer}}
.papel .btn{{box-shadow:inset 0 0 0 2px #0a0a0b}}
.chip{{font:600 12px var(--font);padding:3px 10px;border-radius:999px;background:var(--voltaje);color:#0a0a0b}} .papel .chip{{box-shadow:inset 0 0 0 1.5px #0a0a0b}}
.lnk{{color:inherit;font-weight:600;text-decoration:underline;text-underline-offset:3px}}
.barra{{display:flex;gap:10px;align-items:center;padding-bottom:14px;border-bottom:1px solid;border-color:inherit}}
.act{{display:grid;gap:4px;margin-top:14px}} .act .fol{{font:500 12px var(--mono);opacity:.75}}
.icono{{width:84px;height:84px;border-radius:20px;background:var(--noche);display:grid;place-items:center;color:#f2f2ee;--sam-tinta:#0a0a0b}}
.tab{{display:inline-flex;gap:8px;align-items:center;padding:8px 14px;border-radius:8px 8px 0 0;font-size:13px;background:var(--sup2)}}
.notif{{display:grid;gap:2px;padding:14px;border-radius:14px;background:var(--sup2);max-width:340px;font-size:14px}} .notif .h{{display:flex;gap:6px;align-items:center;font-size:12px;color:var(--muted)}}
/* Usos incorrectos */
.malos{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}} @media (max-width:820px){{.malos{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
.malo{{border:1px solid var(--linea);border-radius:10px;overflow:hidden;background:var(--sup)}} .malo .v{{height:120px;display:grid;place-items:center}} .malo p{{padding:12px 14px;font-size:14px}}
.archivos li{{padding:8px 0;border-bottom:1px solid var(--linea)}} .archivos{{list-style:none;margin:0;padding:0}}
footer .w{{padding-block:32px 48px;color:var(--muted);font-size:14px}}
@media (prefers-reduced-motion:no-preference){{.portada .logo{{animation:entra .6s cubic-bezier(.16,1,.3,1) both}}@keyframes entra{{from{{transform:translateY(8px)}}to{{transform:none}}}}}}
</style>

<header class="portada"><div class="w">
  <span class="eti" style="color:#a3a3a8">Manual de marca · versión 1.0</span>
  {svg('sam-logotipo-vertical.svg', cls='logo', label=LOGO)}
  <p>La herramienta con la que el equipo de desarrollo y soporte registra, mueve y cierra su trabajo.</p>
  <div class="datos"><span>Identidad congelada el 13 nov 2026</span><span>Símbolo · Tarjetas</span><span>Color · Voltaje</span><span>Letra · Onest</span></div>
</div></header>

<nav class="indice" aria-label="Secciones del manual"><div class="w"><ul>
  <li><a href="#idea">Idea</a></li><li><a href="#simbolo">Símbolo</a></li><li><a href="#logotipo">Logotipo</a></li><li><a href="#color">Color</a></li>
  <li><a href="#tipografia">Tipografía</a></li><li><a href="#aplicaciones">Aplicaciones</a></li><li><a href="#incorrectos">Usos incorrectos</a></li><li><a href="#archivos">Archivos</a></li>
</ul></div></nav>

<main>
<section class="lam" id="idea" aria-labelledby="h-idea"><div class="w">
  <div class="regla"><span class="eti">Idea</span><h2 id="h-idea">Una actividad pasa adelante y queda hecha</h2></div>
  <div class="muestra">
    <p>SAM significa <b>Simple Activity Manager</b>. Todo el día, el equipo hace lo mismo: toma una actividad, la mueve de etapa o de persona y la cierra con evidencia. El símbolo cuenta exactamente eso: la tarjeta anterior queda atrás, en contorno, porque ya pasó; la tarjeta actual va adelante, en color, y lleva la palomita de completada.</p>
    <p class="muted">Tres decisiones lo sostienen: el símbolo dice «actividad» sin necesidad de letra, el color es un relleno que marca lo que está activo, y la misma letra se usa en la marca y en la interfaz, para que la marca sea la app.</p>
  </div>
</div></section>

<section class="lam" id="simbolo" aria-labelledby="h-simbolo"><div class="w">
  <div class="regla"><span class="eti">Símbolo</span><h2 id="h-simbolo">Tarjetas</h2>
    <p>Hay dos dibujos del mismo símbolo. El grande se usa desde 32 px. Por debajo de 32 px va la versión chica: las tarjetas se separan más y los trazos engrosan para que la palomita no se pierda.</p>
    <p class="muted">Área de protección: alrededor del símbolo deja libre, como mínimo, la altura de la tarjeta lima.</p></div>
  <div class="muestra">
    <div class="caja anat">{svg(C2, 160, 160)}
      <ol><li><b>Tarjeta anterior</b>, en contorno de tinta: la etapa que ya pasó.</li><li><b>Tarjeta actual</b>, rellena de Voltaje con contorno de tinta: la actividad en curso.</li><li><b>Palomita</b>, siempre en tinta: la actividad se completa.</li></ol></div>
    <div class="caja"><div class="tams">
      <figure>{svg(C4, 16, 16)}<figcaption>16 · chico</figcaption></figure><figure>{svg(C4, 24, 24)}<figcaption>24 · chico</figcaption></figure>
      <figure>{svg(C2, 32, 32)}<figcaption>32</figcaption></figure><figure>{svg(C2, 48, 48)}<figcaption>48</figcaption></figure><figure>{svg(C2, 96, 96)}<figcaption>96</figcaption></figure>
      <figure><span class="proteccion">{svg(C2, 72, 72)}</span><figcaption>área libre</figcaption></figure></div></div>
  </div>
</div></section>

<section class="lam" id="logotipo" aria-labelledby="h-logotipo"><div class="w">
  <div class="regla"><span class="eti">Logotipo</span><h2 id="h-logotipo">Tres arreglos, un mismo nombre</h2>
    <p><b>Horizontal</b> para la barra de la app, documentos y correos. <b>Vertical</b> para portadas y la pantalla de inicio. <b>Compacto</b>, sin descriptor, cuando el espacio no da para «Simple Activity Manager».</p>
    <p class="muted">El nombre está dibujado en Onest 700 y convertido a trazos; el descriptor, en Onest 500. No se reescribe con otra letra.</p></div>
  <div class="muestra">
    <div class="par"><div class="caja noche">{svg('sam-logotipo-horizontal.svg', cls='', label=LOGO, extra=' style="width:100%;max-width:260px;height:auto;color:#f2f2ee"')}</div>
      <div class="caja papel">{svg('sam-logotipo-horizontal.svg', label=LOGO, extra=' style="width:100%;max-width:260px;height:auto;color:#0a0a0b"')}</div></div>
    <div class="par"><div class="caja noche fila" style="justify-content:center">{svg('sam-logotipo-vertical.svg', label=LOGO, extra=' style="width:150px;height:auto;color:#f2f2ee"')}</div>
      <div class="caja papel fila" style="justify-content:center">{svg('sam-logotipo-compacto.svg', label='SAM', extra=' style="width:150px;height:auto;color:#0a0a0b"')}</div></div>
  </div>
</div></section>

<section class="lam" id="color" aria-labelledby="h-color"><div class="w">
  <div class="regla"><span class="eti">Color</span><h2 id="h-color">Voltaje es relleno, nunca texto</h2>
    <p>Voltaje marca lo que está activo: el botón principal, el estado «en curso» y la tarjeta del símbolo. Siempre toca tinta: texto oscuro encima y, sobre papel, contorno de tinta.</p>
    <p>En tema claro, el texto, los enlaces y el foco van en tinta. Voltaje no se oscurece para leerse sobre papel: se vería como otro color.</p>
    <p class="muted">En la app, Voltaje entra en <code>--g-color-brand</code> de Grana.</p></div>
  <div class="muestra">
    <div class="colores">
      <div class="col"><div class="sw" style="background:#c6f432"></div><div class="tx"><b>Voltaje</b><span class="mono">#C6F432</span><span class="muted">Relleno de lo activo</span></div></div>
      <div class="col"><div class="sw" style="background:#0a0a0b"></div><div class="tx"><b>Noche / Tinta</b><span class="mono">#0A0A0B</span><span class="muted">Fondo oscuro, texto y contornos</span></div></div>
      <div class="col"><div class="sw" style="background:#f2f2ee;border-bottom:1px solid var(--linea)"></div><div class="tx"><b>Papel</b><span class="mono">#F2F2EE</span><span class="muted">Fondo claro y texto sobre noche</span></div></div>
    </div>
    <div class="caja tabla"><table><thead><tr><th>Par</th><th>Contraste</th><th>Uso</th></tr></thead><tbody>
      <tr><td>Tinta sobre Voltaje</td><td class="n">15.4:1</td><td><span class="ok">Texto de botones y estados</span></td></tr>
      <tr><td>Voltaje sobre Noche</td><td class="n">15.4:1</td><td><span class="ok">Relleno en tema oscuro</span></td></tr>
      <tr><td>Tinta sobre Papel</td><td class="n">17.6:1</td><td><span class="ok">Texto, enlaces y foco en tema claro</span></td></tr>
      <tr><td>Voltaje sobre Papel</td><td class="n">1.1:1</td><td><span class="no">Nunca como texto ni sin contorno de tinta</span></td></tr>
    </tbody></table></div>
  </div>
</div></section>

<section class="lam" id="tipografia" aria-labelledby="h-tipografia"><div class="w">
  <div class="regla"><span class="eti">Tipografía</span><h2 id="h-tipografia">Onest en todo; mono para los datos</h2>
    <p><b>Onest</b> va en la marca y en la interfaz: hecha para pantallas, con letras bien diferenciadas y números claros. <b>JetBrains Mono</b> solo para folios, horas y datos que se comparan en columna.</p>
    <p class="muted">Ambas son de Google Fonts, con licencia libre (OFL).</p></div>
  <div class="muestra"><div class="caja escala">
    <div><span class="eti">Título · 700</span><span style="font-size:32px;font-weight:700;line-height:1.1">Mis actividades</span></div>
    <div><span class="eti">Subtítulo · 600</span><span style="font-size:20px;font-weight:600">El reporte diario de atrasos no llegó a Discord</span></div>
    <div><span class="eti">Texto · 400</span><span>Revisé el webhook y la tarea programada. Adjunto la evidencia del log y paso la incidencia a revisión.</span></div>
    <div><span class="eti">Etiqueta · 500</span><span style="font-size:14px;font-weight:500">Asignado a Soporte técnico · vence hoy</span></div>
    <div><span class="eti">Datos · mono</span><span class="mono" style="font-size:14px">INC-2041 · TAR-0187 · 14:05 · 18 nov</span></div>
    <div><span class="eti">Prueba</span><span>Il1 · O0 · rn m · ñ á é ü</span></div>
  </div></div>
</div></section>

<section class="lam" id="aplicaciones" aria-labelledby="h-aplicaciones"><div class="w">
  <div class="regla"><span class="eti">Aplicaciones</span><h2 id="h-aplicaciones">Así se ve en SAM</h2>
    <p>El botón principal y el estado activo llevan Voltaje con texto en tinta. En tema claro, ambos suman un contorno de tinta. El icono de la app va sobre noche; la pestaña usa el símbolo chico; la notificación, una silueta de una sola tinta.</p>
    <p class="muted">Ejemplos con datos ficticios.</p></div>
  <div class="muestra">
    <div class="par">
      <div class="caja noche" style="--sam-tinta:#0a0a0b"><div class="barra" style="border-color:#2a2a30">{svg(C2, 26, 26)}<b>SAM</b></div>
        <div class="act"><span class="fol">INC-2041</span><b>El reporte diario de atrasos no llegó a Discord</b><span class="fila" style="gap:8px"><span class="chip">En curso</span><span style="color:#a3a3a8;font-size:13px">Vence hoy, 18:00</span></span></div>
        <div class="fila" style="margin-top:16px"><button class="btn" type="button">Avanzar etapa</button><a class="lnk" href="#aplicaciones">Adjuntar evidencia</a></div></div>
      <div class="caja papel"><div class="barra" style="border-color:#d6d6d0">{svg(C2, 26, 26)}<b>SAM</b></div>
        <div class="act"><span class="fol">INC-2041</span><b>El reporte diario de atrasos no llegó a Discord</b><span class="fila" style="gap:8px"><span class="chip">En curso</span><span style="color:#55555c;font-size:13px">Vence hoy, 18:00</span></span></div>
        <div class="fila" style="margin-top:16px"><button class="btn" type="button">Avanzar etapa</button><a class="lnk" href="#aplicaciones">Adjuntar evidencia</a></div></div>
    </div>
    <div class="caja fila" style="gap:24px">
      <span class="icono">{svg(C2, 58, 58)}</span>
      <span class="tab">{svg(C4, 16, 16)}<span>Mis actividades · SAM</span></span>
      <div class="notif"><span class="h">{svg('sam-notificacion.svg', 16, 16, extra=' style="color:var(--fg)"').replace('#ffffff', 'currentColor')}<span>SAM · ahora</span></span><b>INC-2041 avanzó a Revisión</b><span class="muted">Te toca revisar la evidencia adjunta.</span></div>
    </div>
  </div>
</div></section>

<section class="lam" id="incorrectos" aria-labelledby="h-incorrectos"><div class="w">
  <div class="regla"><span class="eti">Usos incorrectos</span><h2 id="h-incorrectos">Lo que no se hace</h2>
    <p>El símbolo no se deforma, no se recolorea y no se separa en partes. Voltaje no va sobre papel sin su contorno de tinta ni se usa como color de texto.</p></div>
  <div class="muestra"><div class="malos">
    <div class="malo"><div class="v"><svg viewBox="0 0 48 48" width="64" height="64" role="img" aria-label="Símbolo deformado" style="transform:scaleX(1.5)">{bruto}</svg></div><p><span class="no">Deformarlo</span></p></div>
    <div class="malo"><div class="v" style="--g-color-brand:#22d3ee">{svg(C2, 64, 64, label='Símbolo en otro color')}</div><p><span class="no">Cambiar Voltaje por otro color</span></p></div>
    <div class="malo"><div class="v" style="background:#f2f2ee;color:#0a0a0b"><svg viewBox="0 0 48 48" width="64" height="64" role="img" aria-label="Tarjeta lima sin contorno sobre papel">{sin_contorno}</svg></div><p><span class="no">Quitar el contorno sobre papel</span></p></div>
    <div class="malo"><div class="v" style="background:#f2f2ee"><span style="color:#c6f432;font-weight:700;font-size:20px">Nueva actividad</span></div><p><span class="no">Usar Voltaje como texto</span></p></div>
  </div></div>
</div></section>

<section class="lam" id="archivos" aria-labelledby="h-archivos"><div class="w">
  <div class="regla"><span class="eti">Archivos</span><h2 id="h-archivos">Dónde está cada pieza</h2>
    <p>Todo vive en el repositorio, en <code>.fruti/icons/sam/final/</code>. Los SVG «sobre-oscuro» y «sobre-claro» llevan colores fijos para usarse como imagen; los demás heredan los colores del CSS de la página.</p></div>
  <div class="muestra"><ul class="caja archivos">
    <li><code>sam-simbolo.svg</code>, <code>sam-simbolo-chico.svg</code> · símbolo grande y chico</li>
    <li><code>sam-logotipo-horizontal|vertical|compacto.svg</code> · con variantes <code>-sobre-oscuro</code> y <code>-sobre-claro</code></li>
    <li><code>favicon.svg</code>, <code>favicon-32.png</code> · pestaña del navegador</li>
    <li><code>icon-192.png</code>, <code>icon-512.png</code>, <code>maskable-512.png</code>, <code>apple-touch-icon.png</code> · PWA</li>
    <li><code>sam-notificacion.svg</code>, <code>notificacion-96.png</code> · notificaciones push</li>
    <li><code>sam-marca.css</code> · tokens: <code>--g-color-brand</code>, tinta, noche, papel y fuentes</li>
    <li><code>manifest.fragmento.json</code> · nombre, colores e iconos de la PWA</li>
  </ul></div>
</div></section>
</main>
<footer><div class="w">SAM · Simple Activity Manager · Manual de marca 1.0 · 13 de noviembre de 2026</div></footer>
'''
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'manual.html'), 'w').write(html); print('ok', len(html)//1024, 'KB')
