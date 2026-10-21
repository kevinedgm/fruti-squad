# CLNDA Studio · guía de marca (artifact). Incrusta los SVG de final/svg.
F='../final'
def s(n): return open(f'{F}/svg/{n}.svg').read()
INK='#0e0f1c'; BG='#f5f6fb'; IND='#4338ca'; INDD='#8b8cf8'; LIMA='#c6f23d'; OLIVA='#4d7c0f'
fav_d=s('favicon').replace('var(--l)',LIMA).replace('var(--p)',BG)
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Marca CLNDA Studio</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@500&display=swap">
<style>
/* Guía de marca de CLNDA Studio: tinta, fondo, índigo y lima. Oscura por defecto cuando el sistema lo pide. */
:root{{--bg:{BG};--surf:#ffffff;--text:{INK};--muted:#4b4d63;--line:rgb(14 15 28/.10);--brand:{IND};--lime:{OLIVA};--lime-fill:{LIMA};--sans:"Space Grotesk",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:{INK};--surf:#181a2e;--text:{BG};--muted:#a9abc4;--line:rgb(245 246 251/.12);--brand:{INDD};--lime:{LIMA};color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:{INK};--surf:#181a2e;--text:{BG};--muted:#a9abc4;--line:rgb(245 246 251/.12);--brand:{INDD};--lime:{LIMA};color-scheme:dark}}
body{{margin:0;background:var(--bg);color:var(--text);font:17px/1.55 var(--sans)}}
main{{max-width:900px;margin:0 auto;padding-inline:16px;padding-block:28px 80px;display:grid;gap:56px}}
h1,h2{{margin:0;font-weight:700;line-height:1.1;letter-spacing:-.02em;text-wrap:balance}} h1{{font-size:clamp(2rem,6vw,3.2rem)}} h2{{font-size:clamp(1.5rem,4vw,2rem)}}
h3{{margin:0;font:700 1rem var(--sans)}} p{{margin:0;max-width:64ch}} .sub{{color:var(--muted)}} code{{font:500 .82em var(--mono)}}
.eyebrow{{font:500 .72rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--brand)}}
section{{display:grid;gap:18px;min-width:0}}
.hero{{display:grid;gap:18px;padding-block:12px 28px}} .hero .wm{{width:min(100%,460px)}} .hero .wm svg{{width:100%;height:auto;display:block}} .hero .big{{font:700 clamp(1.2rem,3vw,1.5rem)/1.3 var(--sans);max-width:32ch}}
.tiles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}} .tile{{border:1px solid var(--line);border-radius:12px;padding:16px;display:grid;gap:10px;justify-items:center;min-width:0}}
.tile small{{font:500 .72rem var(--mono);text-align:center}} .tile svg{{display:block;width:100%;max-width:120px;height:auto}}
.clara{{background:{BG};color:{INK}}} .clara small{{color:#4b4d63}} .oscura{{background:{INK};color:{BG};border-color:{INK}}} .oscura small{{color:#a9abc4}}
.fila{{display:flex;gap:16px;align-items:flex-end;flex-wrap:wrap}} .fila span{{display:block}} .fila svg{{width:100%;height:100%}}
.tab{{display:flex;align-items:center;gap:8px;border-radius:8px 8px 0 0;padding:8px 12px;width:200px;font-size:12px;background:#fff;color:#111;border:1px solid #ddd}} .tab span{{width:16px;height:16px;flex:none}} .barra{{background:#e9edf2;padding:8px 8px 0;border-radius:8px}} .barra.n{{background:#35363a}} .barra.n .tab{{background:#202124;color:#e8eaed;border-color:#3c4043}}
.sw{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:14px}} .sw>div{{display:grid;gap:4px}} .sw .c{{height:64px;border-radius:8px;border:1px solid var(--line)}} .sw code{{color:var(--muted)}}
.wrap{{overflow-x:auto;min-width:0}} table{{border-collapse:collapse;width:100%;font-size:.92rem}} th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}} th{{font:500 .72rem var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}} .num{{font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}}
.tipo{{display:grid;gap:14px}} .tipo>div{{display:grid;grid-template-columns:170px 1fr;gap:14px;align-items:baseline;border-top:1px solid var(--line);padding-top:10px}} .tipo .f1{{font:700 2rem/1.1 var(--sans);letter-spacing:-.02em}} .tipo .f2{{font:400 1.2rem var(--sans)}} .tipo .f3{{font:500 1.1rem var(--mono)}}
.ui{{display:flex;gap:10px;align-items:center;flex-wrap:wrap;font:500 14px var(--sans)}} .btn{{padding:9px 14px;border-radius:8px;font-weight:700}}
.gh{{display:flex;gap:12px;align-items:center;background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font:14px system-ui;max-width:420px}} .gh span{{width:48px;height:48px;border-radius:50%;overflow:hidden;display:block;flex:none}} .gh b{{display:block;font-size:16px}} .gh small{{color:#8b949e}}
.firma{{width:min(100%,280px)}} .firma svg{{width:100%;height:auto;display:block}}
.tarjeta{{border-radius:12px;overflow:hidden;border:1px solid var(--line)}} .tarjeta svg{{width:100%;height:auto;display:block}}
.regla{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}} .regla>div{{border-top:3px solid var(--text);padding-top:10px;display:grid;gap:4px}} .regla .no{{border-color:#d63a3a}}
@media (max-width:600px){{.tipo>div{{grid-template-columns:1fr}}}}
</style></head><body><main>
<header class="hero"><span class="eyebrow">Identidad · CLNDA Studio</span><h1 style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">CLNDA Studio</h1>
<div class="wm" data-claro>{s('lockup').replace(INK,'var(--text)').replace(IND,'var(--brand)').replace(OLIVA,'var(--lime)')}</div>
<p class="big">Diseñamos soluciones en software y datos.</p>
<p class="sub">CLNDA es «calenda» sin vocales: la fiesta de Oaxaca escrita como la escribiría un programador. La marca es una llave de código abierta con el dato dentro, y un cursor que sigue parpadeando al final del nombre: siempre hay algo escribiéndose.</p></header>

<section><span class="eyebrow">El símbolo</span><h2>La llave y el dato</h2>
<p>Una llave <code>{{</code> en índigo y un punto en tinta: el código abre, el dato está dentro. Sobre tinta la llave sube a índigo claro; en superficies de pantalla donde la marca debe brillar (avatar, app icon, portadas) puede ir en lima.</p>
<div class="tiles"><div class="tile clara">{s('simbolo')}<small>claro · índigo</small></div><div class="tile clara">{s('simbolo-tinta')}<small>una tinta</small></div><div class="tile oscura">{s('simbolo-oscuro')}<small>sobre tinta · regla</small></div><div class="tile oscura">{s('simbolo-lima')}<small>sobre tinta · variante lima</small></div></div>
<div class="fila"><span style="width:16px;height:16px">{s('simbolo-16')}</span><span style="width:24px;height:24px">{s('simbolo-16')}</span><span style="width:32px;height:32px">{s('simbolo')}</span><span style="width:48px;height:48px">{s('simbolo')}</span><span style="width:64px;height:64px">{s('simbolo')}</span></div>
<p class="sub">De 16 a 24 px se usa la versión de trazo grueso; de 32 px en adelante, la normal.</p></section>

<section><span class="eyebrow">App icon, avatar y favicon</span><h2>Oscuro con lima</h2>
<p>El app icon y el avatar de GitHub van en tinta con la llave en lima: es la única pieza donde la lima lleva el símbolo. El favicon cambia solo con el esquema del navegador: índigo en claro, lima en oscuro.</p>
<div class="fila"><span style="width:120px;height:120px">{s('app-icon-redondeado')}</span><span style="width:60px;height:60px">{s('app-icon-redondeado')}</span><span style="width:120px;height:120px">{s('app-icon-claro')}</span><div class="barra"><div class="tab"><span>{s('favicon')}</span>CLNDA Studio</div></div><div class="barra n"><div class="tab"><span>{fav_d}</span>CLNDA Studio</div></div></div>
<div class="gh"><span>{s('avatar')}</span><div><b>clnda-studio</b><small>Software y ciencia de datos · Oaxaca</small></div></div></section>

<section><span class="eyebrow">Logotipo</span><h2>CLNDA con cursor</h2>
<p>Space Grotesk 700 convertida a trazados, con un cursor de bloque al final: lima sobre tinta, oliva sobre fondo claro. En web el cursor puede parpadear; en impreso queda fijo.</p>
<div class="tiles"><div class="tile clara" style="max-width:none">{s('wordmark').replace('viewBox','style="max-width:320px" viewBox')}<small>claro</small></div><div class="tile oscura">{s('wordmark-oscuro').replace('viewBox','style="max-width:320px" viewBox')}<small>oscuro</small></div></div>
<div class="tiles"><div class="tile clara" style="max-width:none">{s('lockup').replace('viewBox','style="max-width:360px" viewBox')}<small>lockup claro</small></div><div class="tile oscura">{s('lockup-lima').replace('viewBox','style="max-width:360px" viewBox')}<small>lockup oscuro con lima</small></div></div></section>

<section><span class="eyebrow">Color</span><h2>Tinta, fondo, índigo y lima</h2>
<p>Índigo es la marca y la acción primaria en claro. Lima es la acción primaria en oscuro y el cursor. Nunca lima sobre fondo claro: baja a oliva.</p>
<div class="sw"><div><div class="c" style="background:{INK}"></div><b>tinta</b><code>{INK}</code></div><div><div class="c" style="background:{BG}"></div><b>fondo</b><code>{BG}</code></div><div><div class="c" style="background:{IND}"></div><b>índigo</b><code>{IND}</code></div><div><div class="c" style="background:{INDD}"></div><b>índigo oscuro</b><code>{INDD}</code></div><div><div class="c" style="background:{LIMA}"></div><b>lima</b><code>{LIMA}</code></div><div><div class="c" style="background:{OLIVA}"></div><b>lima en claro</b><code>{OLIVA}</code></div></div>
<div class="wrap"><table><thead><tr><th>Par</th><th>Contraste</th><th>Sirve para</th></tr></thead><tbody>
<tr><td>Índigo sobre fondo</td><td class="num">7.3:1</td><td>Símbolo, texto, botones</td></tr><tr><td>Índigo oscuro sobre tinta</td><td class="num">6.5:1</td><td>Símbolo y enlaces en oscuro</td></tr><tr><td>Lima sobre tinta</td><td class="num">14.6:1</td><td>Símbolo, cursor y botones en oscuro</td></tr><tr><td>Oliva sobre fondo</td><td class="num">4.6:1</td><td>Cursor y texto lima en claro</td></tr><tr><td>Tinta sobre fondo</td><td class="num">17.6:1</td><td>Texto</td></tr></tbody></table></div>
<h3>En interfaz</h3><div class="ui"><span class="btn" style="background:{IND};color:#fff">Ver trabajo</span><span class="btn" style="background:{LIMA};color:{INK}">Contacto</span><span style="color:var(--brand);text-decoration:underline">clnda.studio</span></div></section>

<section><span class="eyebrow">Tipografía</span><h2>Space Grotesk y JetBrains Mono</h2>
<div class="tipo"><div><span class="f1">Grotesk 700</span><p>Títulos y el nombre. Tracking ligeramente negativo. El logotipo nace de este peso.</p></div><div><span class="f2">Grotesk 400 / 500</span><p>Cuerpo e interfaz. 500 para etiquetas y botones.</p></div><div><span class="f3">Mono 500</span><p>Código, cifras y la firma de producto.</p></div></div></section>

<section><span class="eyebrow">Firma y redes</span><h2>«hecho por CLNDA Studio»</h2>
<p>En pies de producto va el símbolo a 16 px con la frase en Space Grotesk 500, al 85 % de opacidad. La tarjeta de redes es tinta con lima.</p>
<div class="firma">{s('firma').replace(INK,'var(--text)').replace(IND,'var(--brand)')}</div>
<div class="tarjeta">{s('tarjeta-redes')}</div></section>

<section><span class="eyebrow">Uso</span><h2>Reglas cortas</h2>
<div class="regla"><div><h3>Tamaño mínimo</h3><p>Símbolo 32 px; de 16 a 24 px la versión gruesa. Logotipo 96 px de ancho; lockup 120 px.</p></div><div><h3>Espacio libre</h3><p>Alrededor, al menos el grosor del trazo de la llave.</p></div><div><h3>Lima</h3><p>Solo sobre tinta. En claro, oliva. La llave en lima solo en avatar, app icon y portadas.</p></div><div class="no"><h3>No</h3><p>No cerrar la llave, no cambiar el grosor, no usar degradados, no escribir CLNDA con la fuente del sistema en lugar de los archivos, no volver al rosa.</p></div></div>
<p class="sub">Archivos en <code>.fruti/icons/clnda/final/</code> (SVG, PNG, favicon, <code>tema.json</code>).</p></section>
</main></body></html>'''
open('guia-marca.html','w').write(html); print(len(html))
