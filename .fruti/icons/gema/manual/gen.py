# GEMA · manual de marca (artifact). Genera manual.html con los SVG finales embebidos.
import os, re, itertools
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final')
cnt = itertools.count()
def leer(n): return open(os.path.join(F, n)).read()
def svg(n, w=None, h=None, label='GEMA', extra='', repl=None):
    s = leer(n); vb = re.search(r'viewBox="([^"]+)"', s).group(1)
    i = re.sub(r'<title>.*?</title>', '', s[s.index('>', s.index('<svg')) + 1: s.rindex('</svg>')])
    for a, b in (repl or {}).items(): i = i.replace(a, b)
    k = next(cnt)
    for old in set(re.findall(r'id="([^"]+)"', i)): i = i.replace(f'id="{old}"', f'id="{old}-{k}"').replace(f'url(#{old})', f'url(#{old}-{k})')
    dims = (f' width="{w}"' if w else '') + (f' height="{h}"' if h else '')
    return f'<svg viewBox="{vb}"{dims} role="img" aria-label="{label}"{extra}>{i}</svg>'
S, SC, NOM = 'gema-simbolo.svg', 'gema-simbolo-chico.svg', 'GEMA, Gestión de Muestras y Análisis'
html = f'''<title>Manual de marca GEMA</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap">
<style>
/* Layout: manual en láminas (regla a la izquierda, muestra a la derecha); portada sobre el degradado navy. Tokens de la marca GEMA. */
:root{{--navy:#052A76;--azul:#3D67AE;--azul-claro:#7aa2f0;--tinta:#0a0a0b;--papel:#f2f2ee;
  --bg:var(--papel);--fg:#0a0a0b;--muted:#55555c;--linea:#d6d6d0;--sup:#ffffff;--sup2:#e8e8e2;--brand:var(--navy);
  --gema-pico-a:var(--navy);--gema-pico-b:var(--azul);
  --font:"Onest",ui-sans-serif,system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#0a0a0b;--fg:#f2f2ee;--muted:#a3a3a8;--linea:#2a2a30;--sup:#16161a;--sup2:#1f1f24;--brand:var(--azul);--gema-pico-a:var(--azul);--gema-pico-b:var(--azul-claro);color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0a0a0b;--fg:#f2f2ee;--muted:#a3a3a8;--linea:#2a2a30;--sup:#16161a;--sup2:#1f1f24;--brand:var(--azul);--gema-pico-a:var(--azul);--gema-pico-b:var(--azul-claro);color-scheme:dark}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--fg);font:400 16px/1.55 var(--font)}}
.w{{max-width:1120px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
h1,h2,h3{{text-wrap:balance;margin:0;letter-spacing:-.015em}} h2{{font-size:clamp(28px,4vw,40px);line-height:1.1;font-weight:700}}
p{{margin:0;max-width:62ch}} .muted{{color:var(--muted)}} code,.mono{{font-family:var(--mono);font-size:.86em}}
.eti{{font:500 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
:focus-visible{{outline:3px solid var(--fg);outline-offset:3px;border-radius:4px}}
.portada{{background:linear-gradient(160deg,var(--azul),var(--navy) 70%);color:#fff;--gema-pico-a:#7aa2f0;--gema-pico-b:#8fb3ff}}
.portada .w{{padding-block:56px 48px;display:grid;gap:36px}} .portada .logo{{color:#fff;width:min(340px,80%);height:auto}}
.portada p{{font-size:clamp(18px,2.4vw,22px);color:#dfe7f7;max-width:42ch}} .portada .datos{{display:flex;flex-wrap:wrap;gap:8px 24px;font:500 13px var(--mono);color:#c9d5ef}}
nav.indice{{border-bottom:1px solid var(--linea)}} nav.indice ul{{list-style:none;margin:0;padding:12px 0;display:flex;flex-wrap:wrap;gap:4px 18px}}
nav.indice a{{color:var(--fg);text-decoration:none;font-weight:500;font-size:14px;padding:6px 0;display:inline-block}} nav.indice a:hover{{text-decoration:underline;text-underline-offset:4px}}
section.lam{{border-bottom:1px solid var(--linea)}}
section.lam>.w{{padding-block:56px;display:grid;grid-template-columns:minmax(0,4fr) minmax(0,7fr);gap:32px 48px;align-items:start}}
@media (max-width:820px){{section.lam>.w{{grid-template-columns:1fr;padding-block:40px}}}}
.regla{{display:grid;gap:14px}} .muestra{{display:grid;gap:16px;min-width:0}}
.caja{{background:var(--sup);border:1px solid var(--linea);border-radius:10px;padding:24px;min-width:0}}
.caja.noche{{background:#0a0a0b;color:#f2f2ee;border-color:#2a2a30;--gema-pico-a:var(--azul);--gema-pico-b:var(--azul-claro)}}
.caja.papel{{background:var(--papel);color:#0a0a0b;border-color:#d6d6d0;--gema-pico-a:var(--navy);--gema-pico-b:var(--azul)}}
.fila{{display:flex;flex-wrap:wrap;gap:16px;align-items:center}}
.par{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}} @media (max-width:560px){{.par{{grid-template-columns:1fr}}}}
.anat{{display:grid;grid-template-columns:auto minmax(0,1fr);gap:24px;align-items:center}} @media (max-width:560px){{.anat{{grid-template-columns:1fr}}}}
.anat ol{{margin:0;padding-left:20px;display:grid;gap:8px}}
.tams{{display:flex;gap:20px;align-items:flex-end;flex-wrap:wrap}} .tams figure{{margin:0;display:grid;justify-items:center;gap:6px}} .tams figcaption{{font:500 12px var(--mono);color:var(--muted)}}
.proteccion{{display:inline-grid;padding:20px;outline:1.5px dashed var(--muted);outline-offset:-1px}}
.colores{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}} @media (max-width:640px){{.colores{{grid-template-columns:1fr}}}}
.col{{border-radius:10px;border:1px solid var(--linea);overflow:hidden;background:var(--sup)}} .col .sw{{height:100px}} .col .tx{{padding:14px 16px;display:grid;gap:2px}} .col b{{font-weight:600}}
.grad{{height:72px;border-radius:10px;background:linear-gradient(90deg,var(--navy),var(--azul));display:flex;justify-content:space-between;align-items:flex-end;padding:10px 14px;color:#fff;font:500 12px var(--mono)}}
table{{width:100%;border-collapse:collapse;font-size:14px;color:inherit}} th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--linea);vertical-align:top}}
th{{font-weight:600;color:var(--muted);font-size:12px;letter-spacing:.06em;text-transform:uppercase}} td.n{{font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}} .tabla{{overflow-x:auto}}
.ok,.no{{font:600 13px var(--font);display:inline-flex;gap:6px;align-items:center}} .ok::before{{content:"✓";font-weight:700}} .no::before{{content:"✕";font-weight:700}}
.escala{{display:grid;gap:14px}} .escala div{{display:grid;grid-template-columns:110px minmax(0,1fr);gap:16px;align-items:baseline;border-bottom:1px solid var(--linea);padding-bottom:12px}}
@media (max-width:560px){{.escala div{{grid-template-columns:1fr;gap:4px}}}}
.btn{{font:600 15px var(--font);border:0;border-radius:6px;min-height:44px;padding:0 18px;color:#fff;cursor:pointer}}
.noche .btn{{background:var(--azul)}} .papel .btn{{background:var(--navy)}}
.chip{{font:600 12px var(--font);padding:3px 10px;border-radius:999px;color:#fff}} .noche .chip{{background:var(--azul)}} .papel .chip{{background:var(--navy)}}
.lnk{{color:inherit;font-weight:600;text-decoration:underline;text-underline-offset:3px}}
.barra{{display:flex;gap:10px;align-items:center;padding-bottom:14px;border-bottom:1px solid;border-color:inherit}}
.res{{color:inherit;width:100%;border-collapse:collapse;margin-top:12px;font-size:14px}} .res td{{padding:8px 6px 8px 0;border-bottom:1px solid;border-color:inherit}} .res td.v{{text-align:right;font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}}
.fol{{font:500 12px var(--mono);opacity:.75}}
.icono{{width:84px;height:84px;border-radius:20px;display:grid;place-items:center}} .icono img{{width:84px;height:84px;border-radius:20px}}
.tab{{display:inline-flex;gap:8px;align-items:center;padding:8px 14px;border-radius:8px 8px 0 0;font-size:13px;background:var(--sup2)}}
.notif{{display:grid;gap:2px;padding:14px;border-radius:14px;background:var(--sup2);max-width:340px;font-size:14px}} .notif .h{{display:flex;gap:6px;align-items:center;font-size:12px;color:var(--muted)}}
.malos{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}} @media (max-width:820px){{.malos{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
.malo{{border:1px solid var(--linea);border-radius:10px;overflow:hidden;background:var(--sup)}} .malo .v{{height:120px;display:grid;place-items:center}} .malo p{{padding:12px 14px;font-size:14px}}
.archivos{{list-style:none;margin:0;padding:0}} .archivos li{{padding:8px 0;border-bottom:1px solid var(--linea)}}
footer .w{{padding-block:32px 48px;color:var(--muted);font-size:14px}}
</style>

<header class="portada"><div class="w">
  <span class="eti" style="color:#c9d5ef">Manual de marca · versión 1.0</span>
  {svg('gema-logotipo-vertical.svg', label=NOM, extra=' class="logo"', repl={'currentColor':'#ffffff'})}
  <p>El sistema con el que el laboratorio registra cada muestra, sus análisis, sus resultados y sus informes.</p>
  <div class="datos"><span>Identidad congelada el 17 nov 2026</span><span>Símbolo · Pantalla + Resultado</span><span>Color · Degradado navy</span><span>Letra · Onest</span></div>
</div></header>
<nav class="indice" aria-label="Secciones del manual"><div class="w"><ul>
  <li><a href="#idea">Idea</a></li><li><a href="#simbolo">Símbolo</a></li><li><a href="#logotipo">Logotipo</a></li><li><a href="#color">Color</a></li>
  <li><a href="#tipografia">Tipografía</a></li><li><a href="#aplicaciones">Aplicaciones</a></li><li><a href="#incorrectos">Usos incorrectos</a></li><li><a href="#archivos">Archivos</a></li>
</ul></div></nav>
<main>
<section class="lam" id="idea" aria-labelledby="h-idea"><div class="w">
  <div class="regla"><span class="eti">Idea</span><h2 id="h-idea">El resultado que buscas, en la pantalla del instrumento</h2></div>
  <div class="muestra">
    <p>GEMA significa <b>Gestión de Muestras y Análisis</b>. Es el sistema interno del laboratorio: registra las muestras que llegan, los análisis que se les hacen, los resultados, los informes y lo que se cobra por ellos.</p>
    <p class="muted">El símbolo dibuja lo que el laboratorio mira todos los días: la pantalla de un instrumento con la señal de un análisis. Entre los picos, el del resultado destaca en el azul de la marca. El color viene del navy de Nisa Nabani, y la letra es la misma de SAM.</p>
  </div>
</div></section>
<section class="lam" id="simbolo" aria-labelledby="h-simbolo"><div class="w">
  <div class="regla"><span class="eti">Símbolo</span><h2 id="h-simbolo">Pantalla + Resultado</h2>
    <p>Hay dos dibujos del mismo símbolo. El grande se usa desde 32 px. Por debajo va la versión chica: marco más grueso y solo el pico del resultado.</p>
    <p class="muted">Área de protección: alrededor del símbolo deja libre, como mínimo, la cuarta parte de su ancho.</p></div>
  <div class="muestra">
    <div class="caja anat">{svg(S, 160, 160)}
      <ol><li><b>Marco</b>, en tinta: la pantalla del instrumento.</li><li><b>Señal</b>, en tinta: la lectura del análisis, con un pico menor.</li><li><b>Pico del resultado</b>, en degradado navy: lo que el análisis busca.</li></ol></div>
    <div class="caja"><div class="tams">
      <figure>{svg(SC, 16, 16)}<figcaption>16 · chico</figcaption></figure><figure>{svg(SC, 24, 24)}<figcaption>24 · chico</figcaption></figure>
      <figure>{svg(S, 32, 32)}<figcaption>32</figcaption></figure><figure>{svg(S, 48, 48)}<figcaption>48</figcaption></figure><figure>{svg(S, 96, 96)}<figcaption>96</figcaption></figure>
      <figure><span class="proteccion">{svg(S, 72, 72)}</span><figcaption>área libre</figcaption></figure></div></div>
  </div>
</div></section>
<section class="lam" id="logotipo" aria-labelledby="h-logotipo"><div class="w">
  <div class="regla"><span class="eti">Logotipo</span><h2 id="h-logotipo">Nombre arriba, definición abajo</h2>
    <p>«GEMA» en Onest 700 y debajo su definición, «Gestión de Muestras y Análisis», en Onest 500. <b>Horizontal</b> para la barra de la app y documentos; <b>vertical</b> para portadas e inicio; <b>compacto</b>, sin definición, donde no cabe.</p>
    <p class="muted">El texto está convertido a trazos; no se reescribe con otra letra.</p></div>
  <div class="muestra">
    <div class="par"><div class="caja papel">{svg('gema-logotipo-horizontal.svg', label=NOM, extra=' style="width:100%;max-width:260px;height:auto;color:#0a0a0b"')}</div>
      <div class="caja noche">{svg('gema-logotipo-horizontal.svg', label=NOM, extra=' style="width:100%;max-width:260px;height:auto;color:#f2f2ee"')}</div></div>
    <div class="par"><div class="caja papel fila" style="justify-content:center">{svg('gema-logotipo-vertical.svg', label=NOM, extra=' style="width:150px;height:auto;color:#0a0a0b"')}</div>
      <div class="caja noche fila" style="justify-content:center">{svg('gema-logotipo-compacto.svg', label='GEMA', extra=' style="width:150px;height:auto;color:#f2f2ee"')}</div></div>
  </div>
</div></section>
<section class="lam" id="color" aria-labelledby="h-color"><div class="w">
  <div class="regla"><span class="eti">Color</span><h2 id="h-color">Degradado en la marca, color plano en la app</h2>
    <p>El degradado navy (<code>#052A76 → #3D67AE</code>) solo vive en las superficies de marca: el pico del símbolo, el icono de la app y el panel de inicio de sesión.</p>
    <p>En la interfaz el color es plano y siempre con texto blanco: <b>navy</b> en tema claro y <b>azul medio</b> en oscuro, donde el navy no se vería.</p>
    <p class="muted">En la app, el color entra en <code>--g-color-brand</code> de Grana.</p></div>
  <div class="muestra">
    <div class="grad"><span>#052A76</span><span>Degradado navy</span><span>#3D67AE</span></div>
    <div class="colores">
      <div class="col"><div class="sw" style="background:#052A76"></div><div class="tx"><b>Navy</b><span class="mono">#052A76</span><span class="muted">Botones y estado activo en claro</span></div></div>
      <div class="col"><div class="sw" style="background:#3D67AE"></div><div class="tx"><b>Azul medio</b><span class="mono">#3D67AE</span><span class="muted">Botones y estado activo en oscuro</span></div></div>
      <div class="col"><div class="sw" style="background:#7aa2f0"></div><div class="tx"><b>Azul claro</b><span class="mono">#7AA2F0</span><span class="muted">Pico del símbolo sobre fondo oscuro</span></div></div>
    </div>
    <div class="caja tabla"><table><thead><tr><th>Par</th><th>Contraste</th><th>Uso</th></tr></thead><tbody>
      <tr><td>Blanco sobre navy</td><td class="n">13.1:1</td><td><span class="ok">Botones y estados en claro</span></td></tr>
      <tr><td>Navy sobre papel</td><td class="n">11.7:1</td><td><span class="ok">Títulos o enlaces en claro</span></td></tr>
      <tr><td>Blanco sobre azul medio</td><td class="n">5.6:1</td><td><span class="ok">Botones y estados en oscuro</span></td></tr>
      <tr><td>Azul medio sobre negro</td><td class="n">3.5:1</td><td><span class="ok">Superficie de botón en oscuro; nunca texto</span></td></tr>
      <tr><td>Navy sobre negro</td><td class="n">1.5:1</td><td><span class="no">Nunca en tema oscuro</span></td></tr>
    </tbody></table></div>
  </div>
</div></section>
<section class="lam" id="tipografia" aria-labelledby="h-tipografia"><div class="w">
  <div class="regla"><span class="eti">Tipografía</span><h2 id="h-tipografia">Onest para todo; mono para los valores</h2>
    <p><b>Onest</b> va en la marca y en la interfaz; es la misma letra de SAM. <b>JetBrains Mono</b> se reserva para folios, valores y unidades que se comparan en columna.</p>
    <p class="muted">Ambas de Google Fonts, licencia libre (OFL).</p></div>
  <div class="muestra"><div class="caja escala">
    <div><span class="eti">Título · 700</span><span style="font-size:32px;font-weight:700;line-height:1.1">Resultados del día</span></div>
    <div><span class="eti">Subtítulo · 600</span><span style="font-size:20px;font-weight:600">Agua residual · planta norte</span></div>
    <div><span class="eti">Texto · 400</span><span>La muestra llegó a las 09:40 y quedó asignada al área de aguas para DBO₅, SST y pH.</span></div>
    <div><span class="eti">Datos · mono</span><span class="mono" style="font-size:14px">M-2026-1184 · 18.4 mg/L · 7.21 · 196 mg/100 mL A.A.</span></div>
    <div><span class="eti">Prueba</span><span>Il1 · O0 · rn m · DBO₅ · ñ á é</span></div>
  </div></div>
</div></section>
<section class="lam" id="aplicaciones" aria-labelledby="h-aplicaciones"><div class="w">
  <div class="regla"><span class="eti">Aplicaciones</span><h2 id="h-aplicaciones">Así se ve en GEMA</h2>
    <p>Botones y estados en color plano con texto blanco. El icono de la app va sobre el degradado navy; la pestaña usa el símbolo chico; la notificación, una silueta de una sola tinta.</p>
    <p class="muted">Ejemplos con datos ficticios.</p></div>
  <div class="muestra">
    <div class="par">
      <div class="caja papel" style="border-color:#d6d6d0"><div class="barra" style="border-color:#d6d6d0">{svg(S, 26, 26)}<b>GEMA</b></div>
        <table class="res" style="border-color:#d6d6d0"><tr><td><span class="fol">M-2026-1184</span><br><b>Agua residual</b></td><td>DBO₅</td><td class="v">18.4 mg/L</td></tr><tr><td><span class="fol">M-2026-1186</span><br><b>Suelo agrícola</b></td><td>pH</td><td class="v"><span class="chip">En análisis</span></td></tr></table>
        <div class="fila" style="margin-top:16px"><button class="btn" type="button">Registrar muestra</button><a class="lnk" href="#aplicaciones">Ver informe</a></div></div>
      <div class="caja noche"><div class="barra" style="border-color:#2a2a30">{svg(S, 26, 26)}<b>GEMA</b></div>
        <table class="res" style="border-color:#2a2a30"><tr><td><span class="fol">M-2026-1184</span><br><b>Agua residual</b></td><td>DBO₅</td><td class="v">18.4 mg/L</td></tr><tr><td><span class="fol">M-2026-1186</span><br><b>Suelo agrícola</b></td><td>pH</td><td class="v"><span class="chip">En análisis</span></td></tr></table>
        <div class="fila" style="margin-top:16px"><button class="btn" type="button">Registrar muestra</button><a class="lnk" href="#aplicaciones">Ver informe</a></div></div>
    </div>
    <div class="caja fila" style="gap:24px">
      <span class="icono" style="background:linear-gradient(160deg,#3D67AE,#052A76);--gema-pico-a:#7aa2f0;--gema-pico-b:#8fb3ff">{svg(S, 58, 58, repl={'currentColor':'#ffffff'})}</span>
      <span class="tab">{svg(SC, 16, 16)}<span>Recepción · GEMA</span></span>
      <div class="notif"><span class="h">{svg('gema-notificacion.svg', 16, 16, repl={'#ffffff':'currentColor'})}<span>GEMA · ahora</span></span><b>Resultados listos: M-2026-1184</b><span class="muted">El informe está listo para revisión.</span></div>
    </div>
  </div>
</div></section>
<section class="lam" id="incorrectos" aria-labelledby="h-incorrectos"><div class="w">
  <div class="regla"><span class="eti">Usos incorrectos</span><h2 id="h-incorrectos">Lo que no se hace</h2>
    <p>El símbolo no se deforma ni se recolorea. El degradado no va en botones ni en texto. El navy no se usa en tema oscuro.</p></div>
  <div class="muestra"><div class="malos">
    <div class="malo"><div class="v">{svg(S, 64, 64, label='Símbolo deformado', extra=' style="transform:scaleX(1.5)"')}</div><p><span class="no">Deformarlo</span></p></div>
    <div class="malo"><div class="v" style="--gema-pico-a:#e0663a;--gema-pico-b:#f5b52e">{svg(S, 64, 64, label='Símbolo en otro color')}</div><p><span class="no">Cambiar el azul por otro color</span></p></div>
    <div class="malo"><div class="v"><span style="background:linear-gradient(90deg,#052A76,#3D67AE);color:#fff;font-weight:600;padding:12px 16px;border-radius:6px;font-size:14px">Registrar</span></div><p><span class="no">Degradado en un botón</span></p></div>
    <div class="malo"><div class="v" style="background:#0a0a0b"><span style="background:#052A76;color:#fff;font-weight:600;padding:12px 16px;border-radius:6px;font-size:14px">Registrar</span></div><p><span class="no">Navy sobre fondo oscuro</span></p></div>
  </div></div>
</div></section>
<section class="lam" id="archivos" aria-labelledby="h-archivos"><div class="w">
  <div class="regla"><span class="eti">Archivos</span><h2 id="h-archivos">Dónde está cada pieza</h2>
    <p>Todo vive en el repositorio, en <code>.fruti/icons/gema/final/</code>. Los SVG «sobre-claro» y «sobre-oscuro» llevan colores fijos para usarse como imagen; los demás heredan los colores del CSS de la página.</p></div>
  <div class="muestra"><ul class="caja archivos">
    <li><code>gema-simbolo.svg</code>, <code>gema-simbolo-chico.svg</code> · símbolo grande y chico</li>
    <li><code>gema-logotipo-horizontal|vertical|compacto.svg</code> · con variantes <code>-sobre-claro</code> y <code>-sobre-oscuro</code></li>
    <li><code>favicon.svg</code>, <code>favicon-32.png</code> · pestaña del navegador</li>
    <li><code>icon-192.png</code>, <code>icon-512.png</code>, <code>maskable-512.png</code>, <code>apple-touch-icon.png</code> · PWA</li>
    <li><code>gema-notificacion.svg</code>, <code>notificacion-96.png</code> · notificaciones push</li>
    <li><code>gema-marca.css</code> · tokens: <code>--g-color-brand</code>, degradado, tinta, papel y fuentes</li>
    <li><code>manifest.fragmento.json</code> · nombre, colores e iconos de la PWA</li>
  </ul></div>
</div></section>
</main>
<footer><div class="w">GEMA · Gestión de Muestras y Análisis · Manual de marca 1.0 · 17 de noviembre de 2026</div></footer>
'''
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'manual.html'), 'w').write(html); print('ok', len(html)//1024, 'KB')
