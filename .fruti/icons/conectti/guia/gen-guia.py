# Conectti · guía de marca (artifact). Incrusta los SVG de final/svg y la captura del acceso.
import base64,os
F='../final'
def s(n): return open(f'{F}/svg/{n}.svg').read()
def tok(svg): return svg.replace('#1D52BB','var(--brand)').replace('#057F7D','var(--accent)').replace('#111820','var(--text)')
login=base64.b64encode(open(f'{F}/png/login-desktop.png','rb').read()).decode()
movil=base64.b64encode(open(f'{F}/png/login-movil.png','rb').read()).decode()
fav=s('favicon').replace('<style>','<style>svg{}').replace('var(--k)','var(--brand)').replace('var(--a)','var(--accent)')
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Marca Conectti</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Guía de marca de Conectti. Tokens del Design System (tema claro); la guía añade un tema oscuro solo para la página. */
:root{{--bg:#F4F7FA;--surf:#FFFFFF;--text:#111820;--muted:#4A515C;--line:rgb(17 24 32/.10);--brand:#1D52BB;--brand-strong:#0439A1;--brand-soft:#ECF3FE;--accent:#057F7D;--accent-soft:#DEF9F7;--sans:"IBM Plex Sans",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0F1824;--surf:#172234;--text:#F4F7FA;--muted:#A9B3C1;--line:rgb(244 247 250/.12);--brand:#7A9BFF;--brand-strong:#1D52BB;--brand-soft:#1B2A4A;--accent:#5FD6CF;--accent-soft:#143A3A;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0F1824;--surf:#172234;--text:#F4F7FA;--muted:#A9B3C1;--line:rgb(244 247 250/.12);--brand:#7A9BFF;--brand-strong:#1D52BB;--brand-soft:#1B2A4A;--accent:#5FD6CF;--accent-soft:#143A3A;color-scheme:dark}}
body{{margin:0;background:var(--bg);color:var(--text);font:17px/1.55 var(--sans)}}
main{{max-width:900px;margin:0 auto;padding-inline:16px;padding-block:28px 80px;display:grid;gap:56px}}
h1,h2{{margin:0;font-weight:600;line-height:1.1;letter-spacing:-.015em;text-wrap:balance}} h1{{font-size:clamp(2rem,6vw,3.2rem)}} h2{{font-size:clamp(1.5rem,4vw,2rem)}}
h3{{margin:0;font:600 1rem var(--sans)}} p{{margin:0;max-width:64ch}} .sub{{color:var(--muted)}} code{{font:500 .82em var(--mono)}}
.eyebrow{{font:500 .72rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--brand)}}
section{{display:grid;gap:18px;min-width:0}}
.hero{{display:grid;gap:18px;padding-block:12px 28px}} .hero .wm{{width:min(100%,460px)}} .hero .wm svg{{width:100%;height:auto;display:block}} .hero .big{{font:600 clamp(1.2rem,3vw,1.5rem)/1.3 var(--sans);max-width:32ch}}
.tiles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}} .tile{{background:var(--surf);border:1px solid var(--line);border-radius:11px;padding:16px;display:grid;gap:10px;justify-items:center;min-width:0}}
.tile small{{font:500 .72rem var(--mono);color:var(--muted);text-align:center}} .tile svg{{display:block;width:100%;max-width:120px;height:auto}}
.clara{{background:#F4F7FA;border-color:#DCE2EA;color:#111820;--brand:#1D52BB;--accent:#057F7D;--text:#111820}} .clara small{{color:#4A515C}} .cob{{background:#0439A1;border-color:#0439A1;color:#fff}} .cob small{{color:#C9D6F5}}
.fila{{display:flex;gap:16px;align-items:flex-end;flex-wrap:wrap}} .fila span{{display:block}} .fila svg{{width:100%;height:100%}}
.tab{{display:flex;align-items:center;gap:8px;border-radius:8px 8px 0 0;padding:8px 12px;width:200px;font-size:12px;background:#fff;color:#111820;border:1px solid #DCE2EA}} .tab svg{{width:16px;height:16px;flex:none}} .barra{{background:#e9edf2;padding:8px 8px 0;border-radius:8px}} .barra.d{{background:#35363a}} .barra.d .tab{{background:#202124;color:#e8eaed;border-color:#3c4043}}
.sw{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}} .sw>div{{display:grid;gap:4px}} .sw .c{{height:64px;border-radius:8px;border:1px solid var(--line)}} .sw code{{color:var(--muted)}}
.wrap{{overflow-x:auto;min-width:0}} table{{border-collapse:collapse;width:100%;font-size:.92rem}} th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}} th{{font:500 .72rem var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}} .num{{font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}}
.tipo{{display:grid;gap:14px}} .tipo>div{{display:grid;grid-template-columns:150px 1fr;gap:14px;align-items:baseline;border-top:1px solid var(--line);padding-top:10px}} .tipo .f1{{font:600 2rem/1.1 var(--sans);letter-spacing:-.015em}} .tipo .f2{{font:400 1.2rem var(--sans)}} .tipo .f3{{font:500 1.1rem var(--mono)}}
.shot{{display:grid;gap:12px}} .shot img{{width:100%;height:auto;display:block;border-radius:11px;border:1px solid var(--line)}} .shots{{display:grid;grid-template-columns:3fr 1fr;gap:14px;align-items:start}}
.regla{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}} .regla>div{{border-top:3px solid var(--text);padding-top:10px;display:grid;gap:4px}} .regla .no{{border-color:#CE3632}}
@media (max-width:600px){{.tipo>div{{grid-template-columns:1fr}} .shots{{grid-template-columns:1fr}}}}
</style></head><body><main>
<header class="hero"><span class="eyebrow">Identidad · Conectti</span><h1 style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Conectti</h1>
<div class="wm">{tok(s('lockup'))}</div>
<p class="big">Medir con precisión impulsa la mejora continua.</p>
<p class="sub">Conectti es el sistema del laboratorio de análisis: control de calidad en bebidas alcohólicas, agua, alimentos y análisis clínicos. Su marca nace del nombre: las dos t de «conectti» comparten una sola barra, que es a la vez el enlace y la marca de un instrumento calibrado.</p></header>

<section><span class="eyebrow">El símbolo</span><h2>La ligadura tt</h2>
<p>Dos t de IBM Plex Sans 600, las mismas del nombre, unidas por una barra en verde azulado que sobresale a la derecha. No hay matraz ni gota: el laboratorio se dice con exactitud, no con ilustración. El símbolo es la tt sola.</p>
<div class="tiles"><div class="tile clara">{s('simbolo')}<small>color</small></div><div class="tile clara">{s('simbolo-tinta')}<small>una tinta</small></div><div class="tile cob">{s('simbolo-inverso')}<small>sobre cobalto</small></div><div class="tile clara">{s('simbolo-16')}<small>versión 16–24 px</small></div></div>
<div class="fila"><span style="width:16px;height:16px">{s('simbolo-16')}</span><span style="width:24px;height:24px">{s('simbolo-16')}</span><span style="width:32px;height:32px">{s('simbolo')}</span><span style="width:48px;height:48px">{s('simbolo')}</span><span style="width:64px;height:64px">{s('simbolo')}</span></div></section>

<section><span class="eyebrow">App icon y favicon</span><h2>En la pantalla de inicio y en la pestaña</h2>
<p>El app icon es un bloque cobalto con la tt en blanco; la barra usa un verde azulado claro (<code>#5FD6CF</code>) porque el acento del sistema no contrasta sobre cobalto. El favicon cambia solo con el esquema del navegador.</p>
<div class="fila"><span style="width:120px;height:120px">{s('app-icon-redondeado')}</span><span style="width:60px;height:60px">{s('app-icon-redondeado')}</span><span style="width:29px;height:29px">{s('app-icon-redondeado')}</span><div class="barra"><div class="tab">{fav}<span>Entra a Conectti</span></div></div><div class="barra d"><div class="tab">{s('favicon').replace('var(--k)','#FFFFFF').replace('var(--a)','#5FD6CF')}<span>Entra a Conectti</span></div></div></div></section>

<section><span class="eyebrow">Logotipo</span><h2>conectti, en minúsculas</h2>
<p>El nombre en IBM Plex Sans 600 convertido a trazados, con la tt ligada y el punto de la i en acento. En texto corrido se escribe «Conectti», con mayúscula; la minúscula es solo del logotipo.</p>
<div class="tiles"><div class="tile clara" style="max-width:none">{s('wordmark').replace('viewBox','style="max-width:320px" viewBox')}<small>color</small></div><div class="tile cob">{s('wordmark-inverso').replace('viewBox','style="max-width:320px" viewBox')}<small>sobre cobalto fuerte</small></div></div></section>

<section><span class="eyebrow">Color</span><h2>Los del sistema, sin añadir</h2>
<p>La marca usa los mismos tokens que la interfaz: cobalto para la acción y las letras, verde azulado para el acento y el dato, y el fondo claro del tablero. Tema claro único, como el Design System.</p>
<div class="sw"><div><div class="c" style="background:#1D52BB"></div><b>brand · cobalto</b><code>#1D52BB</code></div><div><div class="c" style="background:#0439A1"></div><b>brand-strong</b><code>#0439A1</code></div><div><div class="c" style="background:#057F7D"></div><b>accent · verde azulado</b><code>#057F7D</code></div><div><div class="c" style="background:#5FD6CF"></div><b>barra sobre cobalto</b><code>#5FD6CF</code></div><div><div class="c" style="background:#F4F7FA"></div><b>bg</b><code>#F4F7FA</code></div><div><div class="c" style="background:#111820"></div><b>text</b><code>#111820</code></div></div>
<div class="wrap"><table><thead><tr><th>Par</th><th>Contraste</th><th>Sirve para</th></tr></thead><tbody>
<tr><td>Cobalto sobre bg</td><td class="num">6.6:1</td><td>Logotipo, símbolo, texto</td></tr><tr><td>Verde azulado sobre bg</td><td class="num">4.5:1</td><td>Barra, punto de la i, acento</td></tr><tr><td>Blanco sobre cobalto</td><td class="num">7.1:1</td><td>tt del app icon, logotipo inverso</td></tr><tr><td>#5FD6CF sobre cobalto</td><td class="num">4.0:1</td><td>Barra del app icon (gráfico, 3:1)</td></tr></tbody></table></div></section>

<section><span class="eyebrow">Tipografía</span><h2>IBM Plex, como el sistema</h2>
<div class="tipo"><div><span class="f1">Plex Sans 600</span><p>Títulos y el nombre. Tracking ligeramente negativo en tamaños grandes. El logotipo nace de este peso.</p></div><div><span class="f2">Plex Sans 400</span><p>Cuerpo, etiquetas, ayuda. Peso 500 para etiquetas de campo.</p></div><div><span class="f3">Plex Mono 500</span><p>Cifras y códigos de muestra; tabular.</p></div></div></section>

<section><span class="eyebrow">En contexto</span><h2>La pantalla de acceso</h2>
<p>Lockup arriba a la izquierda a 34 px; formulario 7fr y arte 5fr con el degradado cobalto→verde azulado y el vidrio esmerilado, el único lugar del sistema con degradado. En móvil el arte desaparece.</p>
<div class="shots"><div class="shot"><img alt="Pantalla de acceso en desktop" src="data:image/png;base64,{login}"></div><div class="shot"><img alt="Pantalla de acceso en móvil" src="data:image/png;base64,{movil}"></div></div></section>

<section><span class="eyebrow">Uso</span><h2>Reglas cortas</h2>
<div class="regla"><div><h3>Tamaño mínimo</h3><p>Símbolo 32 px; de 16 a 24 px, la versión de trazo grueso. Logotipo 96 px de ancho; lockup 120 px.</p></div><div><h3>Espacio libre</h3><p>Alrededor, al menos el grosor de la barra.</p></div><div><h3>La barra</h3><p>Siempre en acento y siempre sobresale a la derecha: es la marca de calibración, no un subrayado.</p></div><div class="no"><h3>No</h3><p>No separar las t, no cambiar el grosor, no usar degradado en la marca, no escribir el logotipo con la fuente del sistema en lugar de los archivos.</p></div></div>
<p class="sub">Archivos en el Design System de Conectti (grupo «Marca») y en <code>.fruti/icons/conectti/final/</code>.</p></section>
</main></body></html>'''
open('guia-marca.html','w').write(html); print(len(html))
