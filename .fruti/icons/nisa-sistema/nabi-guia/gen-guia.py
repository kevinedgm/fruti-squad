F='../nabi-final/svg/'
sv=lambda n:open(F+n+'.svg').read()
html=f'''<title>Nabi · manual de marca</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@125,700&family=Onest:wght@400;500;600&display=swap">
<style>
/* Manual de una casa de laboratorio: blanco, azul real y una muestra pera. Columna de 68ch, piezas en rejilla de placa. */
:root{{--bg:#FFFFFF;--fg:#141B33;--azul:#052A76;--pera:#C2D225;--muted:#5A6070;--line:#E2E5EC;--sunk:#F4F6FA;--display:"Archivo",system-ui,sans-serif;--sans:"Onest",system-ui,sans-serif;color-scheme:light}}
body{{background:var(--bg);color:var(--fg);font:16px/1.55 var(--sans);margin:0;padding-block:0 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1040px;margin:0 auto}}
h1,h2{{font-family:var(--display);font-stretch:125%;font-weight:700;letter-spacing:-.01em;text-wrap:balance;margin:0;color:var(--azul)}}
h1{{font-size:clamp(30px,5.4vw,50px);line-height:1.05}} h2{{font-size:24px;line-height:1.15;margin-bottom:12px}}
p{{max-width:68ch;margin:0 0 12px}} .muted{{color:var(--muted)}} code{{font-size:13px;background:var(--sunk);padding:1px 5px;border-radius:4px}}
.hero{{padding:52px 0 34px;border-bottom:1px solid var(--line);display:grid;gap:20px}} .hero .wm svg{{width:min(440px,100%);height:auto;display:block}}
.ov{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:500}}
section{{padding:38px 0;border-bottom:1px solid var(--line)}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(210px,1fr))}}
.c{{border:1px solid var(--line);border-radius:12px;padding:18px;display:grid;gap:10px;align-content:start;min-width:0}} .c.d{{background:var(--azul);border-color:var(--azul)}} .c.d .cap{{color:#C9D0E2}}
.c svg,.c img{{max-width:100%;height:auto;display:block;max-height:120px;margin:auto}} .cap{{font-size:13px;color:var(--muted)}}
.sw{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(160px,1fr))}} .sw div{{border-radius:12px;padding:14px;min-height:110px;display:grid;align-content:end;gap:2px;font-size:13px;border:1px solid var(--line)}} .sw b{{font-family:var(--display);font-stretch:125%;font-size:15px}}
.tw{{overflow-x:auto}} table{{border-collapse:collapse;width:100%;font-size:14px}} th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}} th{{font-weight:600}}
.two{{display:grid;gap:28px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}}
.no{{display:grid;gap:8px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}} .no div{{border:1px solid var(--line);border-radius:8px;padding:12px 14px;font-size:14px}} .no div::before{{content:"✕ ";color:#B42318;font-weight:700}}
.anim svg{{width:120px;height:120px}}
</style>
<main>
<header class="hero"><span class="ov">Manual de marca · v1 · marca de familia de Nisa Nabani</span><div class="wm">{sv('lockup-familia')}</div><h1>La N está hecha de muestras.</h1><p class="muted">Nabi es el sistema de laboratorio de Nisa Nabani: muestras, lotes, ensayos y certificados. Su símbolo es una placa de 4 × 4 pocillos. Los llenos dibujan la N; uno, en pera, es la muestra que se está trabajando.</p></header>

<section><h2>Símbolo</h2><p>Diez pocillos llenos forman la N y seis vacíos quedan como puntos, para que la letra se lea antes que la placa. La muestra pera ocupa el pocillo superior derecho: el final del trazo de la N.</p>
<div class="g"><div class="c">{sv('simbolo')}<span class="cap">Color</span></div><div class="c">{sv('simbolo-tinta')}<span class="cap">Una tinta</span></div><div class="c d">{sv('simbolo-blanco')}<span class="cap">Sobre azul</span></div><div class="c">{sv('favicon-tinta')}<span class="cap">Favicon 16–32 px: solo la N, sin vacíos</span></div></div></section>

<section><h2>Carga y estado</h2><div class="two"><div class="c anim">{sv('carga')}<span class="cap">La muestra recorre la N</span></div><div><p>El símbolo se mueve. La muestra pera recorre los diez pocillos en el orden en que se traza la N, 200 ms por paso. Sirve como indicador de carga y de proceso dentro del sistema.</p><p class="muted">Con «reducir movimiento» la animación se detiene y la muestra queda en su pocillo final. Archivos: <code>carga.svg</code>, <code>carga-blanco.svg</code> y <code>carga.gif</code>.</p></div></div></section>

<section><h2>Wordmark y lockups</h2><p>«nabi» en minúsculas, en Archivo 700 al 125 % de ancho, la familia ancha que conversa con el logo de Nisa Nabani. El punto de la i es un pocillo pera. Va en trazados.</p>
<div class="g"><div class="c">{sv('wordmark')}<span class="cap">Wordmark · mínimo 72 px</span></div><div class="c">{sv('lockup-h')}<span class="cap">Horizontal · mínimo 120 px</span></div><div class="c">{sv('lockup-familia')}<span class="cap">De familia, con Nisa Nabani</span></div><div class="c">{sv('lockup-v')}<span class="cap">Vertical · mínimo 80 px</span></div><div class="c d">{sv('lockup-h-blanco')}<span class="cap">Sobre azul</span></div><div class="c d">{sv('lockup-familia-blanco')}<span class="cap">De familia sobre azul</span></div></div>
<p style="margin-top:14px"><b>Área de respeto:</b> un pocillo alrededor de toda pieza. <b>De familia</b> en documentos para clientes y en la portada del sistema; <b>horizontal</b> dentro de la interfaz.</p></section>

<section><h2>Color</h2><p>Los primarios del laboratorio, sin añadir otro. El azul ordena y el pera marca la muestra.</p>
<div class="sw"><div style="background:#052A76;color:#fff;border-color:#052A76"><b>Azul real</b><span>#052A76 · texto, símbolo, fondos</span></div><div style="background:#C2D225"><b>Pera</b><span>#C2D225 · la muestra; nunca texto</span></div><div><b>Blanco</b><span>#FFFFFF · fondo</span></div></div>
<div class="tw" style="margin-top:16px"><table><tr><th>Par</th><th>Ratio</th><th>Uso</th></tr><tr><td>Azul sobre blanco</td><td>13.1:1</td><td>Texto y símbolo</td></tr><tr><td>Pera sobre azul</td><td>7.8:1</td><td>Acento</td></tr><tr><td>Azul sobre pera</td><td>7.8:1</td><td>Texto sobre fondo pera</td></tr><tr><td>Pera sobre blanco</td><td>1.7:1</td><td>Solo como pocillo del símbolo</td></tr></table></div>
<p class="muted" style="margin-top:10px">Pendiente: la interfaz del sistema usa Verdant WebKit con acento esmeralda. Hay que decidir si la UI adopta azul y pera o si la marca vive solo en el shell (logo, carga, portada).</p></section>

<section><h2>App icon y avatar</h2><div class="g"><div class="c">{sv('app-icon')}<span class="cap">App icon · azul</span></div><div class="c">{sv('app-icon-claro')}<span class="cap">Claro</span></div><div class="c">{sv('app-icon-maskable')}<span class="cap">Maskable · margen amplio</span></div><div class="c">{sv('avatar')}<span class="cap">Avatar</span></div></div></section>

<section><h2>Lo que no se hace</h2><div class="no"><div>Mover, quitar o añadir pocillos.</div><div>Más de una muestra pera.</div><div>Usar el pera como texto.</div><div>Rellenar los pocillos vacíos.</div><div>Poner la placa dentro de un contorno de microplaca.</div><div>Cambiar los pocillos a cuadrados.</div></div></section>

<section style="border:0"><h2>Archivos</h2><p>SVG en <code>nabi-final/svg</code>; PNG en <code>nabi-final/png</code> (icon 1024/512/192, maskable, claro, avatar, símbolos 512, favicon 16/32/48 y .ico, wordmark y lockups a 240 px, tarjeta de redes 1200×630, <code>carga.gif</code>). <code>tema.json</code> y <code>pruebas.md</code> con colores, reglas y contrastes.</p></section>
</main>'''
open('guia.html','w').write(html); print('ok')
