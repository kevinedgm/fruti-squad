# Laranda · manual de uso (artifact). Incrusta los SVG de final/svg.
import base64
F='../final'
def s(n): return open(f'{F}/svg/{n}.svg').read()
INK='#15121C'; HUESO='#F6F4EF'; ARENA='#EAE6DE'; VIO='#5B3BB5'; VIO2='#4A2DA8'; LILA='#C4B5F0'; NIEBLA='#ECE7FA'; NAR='#E0611A'; NART='#F2C9B2'; NARD='#F2A074'; ORO='#D9A400'; VERDE='#0E8F5E'; ROJO='#A8202F'; SUAVE='#4F4B57'
gif=base64.b64encode(open(f'{F}/png/simbolo-bloom.gif','rb').read()).decode()
cvd=base64.b64encode(open(f'{F}/png/daltonismo.png','rb').read()).decode()
fav_d=s('favicon').replace('var(--k)',LILA).replace('var(--f)',INK).replace('var(--a)',NARD)
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Marca Laranda</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Onest:wght@400;500;700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Manual de marca de Laranda: hueso, tinta, violeta intenso y naranja. Oscuro: tinta con lila y naranja claro. */
:root{{--bg:{HUESO};--surf:#ffffff;--text:{INK};--muted:{SUAVE};--line:rgb(21 18 28/.10);--brand:{VIO};--acc:{NAR};--acc-t:{NART};--soft:{NIEBLA};--disp:"Bricolage Grotesque",system-ui,sans-serif;--sans:"Onest",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:{INK};--surf:#221E2E;--text:{HUESO};--muted:#B9B4C4;--line:rgb(246 244 239/.12);--brand:{LILA};--acc:{NARD};--acc-t:#3A2A22;--soft:#2E2940;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:{INK};--surf:#221E2E;--text:{HUESO};--muted:#B9B4C4;--line:rgb(246 244 239/.12);--brand:{LILA};--acc:{NARD};--acc-t:#3A2A22;--soft:#2E2940;color-scheme:dark}}
body{{margin:0;background:var(--bg);color:var(--text);font:17px/1.55 var(--sans)}}
main{{max-width:900px;margin:0 auto;padding-inline:16px;padding-block:28px 80px;display:grid;gap:56px}}
h1,h2{{margin:0;font-family:var(--disp);font-weight:700;line-height:1.1;letter-spacing:-.01em;text-wrap:balance}} h1{{font-size:clamp(2rem,6vw,3.2rem)}} h2{{font-size:clamp(1.5rem,4vw,2rem)}}
h3{{margin:0;font:700 1rem var(--sans)}} p{{margin:0;max-width:64ch}} .sub{{color:var(--muted)}} code{{font:500 .82em var(--mono)}}
.eyebrow{{font:500 .72rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--brand)}}
section{{display:grid;gap:18px;min-width:0}}
.hero{{display:grid;gap:18px;padding-block:12px 28px}} .hero .wm{{width:min(100%,480px)}} .hero .wm svg{{width:100%;height:auto;display:block}} .hero .big{{font:600 clamp(1.2rem,3vw,1.5rem)/1.3 var(--disp);max-width:32ch}}
.tiles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}} .tile{{border:1px solid var(--line);border-radius:14px;padding:16px;display:grid;gap:10px;justify-items:center;min-width:0}} .tile small{{font:500 .72rem var(--mono);text-align:center}} .tile svg{{display:block;width:100%;max-width:130px;height:auto}}
.clara{{background:{HUESO};color:{INK}}} .clara small{{color:{SUAVE}}} .oscura{{background:{INK};color:{HUESO};border-color:{INK}}} .oscura small{{color:#B9B4C4}}
.fila{{display:flex;gap:16px;align-items:flex-end;flex-wrap:wrap}} .fila span{{display:block;overflow:hidden}} .fila svg{{width:100%;height:100%}}
.tab{{display:flex;align-items:center;gap:8px;border-radius:8px 8px 0 0;padding:8px 12px;width:190px;font-size:12px;background:#fff;color:#111;border:1px solid #ddd}} .tab span{{width:16px;height:16px;flex:none}} .barra{{background:#e9edf2;padding:8px 8px 0;border-radius:8px}} .barra.n{{background:#35363a}} .barra.n .tab{{background:#202124;color:#e8eaed;border-color:#3c4043}}
.sw{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:14px}} .sw>div{{display:grid;gap:4px}} .sw .c{{height:60px;border-radius:10px;border:1px solid var(--line)}} .sw code{{color:var(--muted)}}
.wrap{{overflow-x:auto;min-width:0}} table{{border-collapse:collapse;width:100%;font-size:.92rem}} th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}} th{{font:500 .72rem var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}} .num{{font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}}
.tipo{{display:grid;gap:14px}} .tipo>div{{display:grid;grid-template-columns:190px 1fr;gap:14px;align-items:baseline;border-top:1px solid var(--line);padding-top:10px}} .tipo .f1{{font:700 2rem/1.1 var(--disp)}} .tipo .f2{{font:400 1.2rem var(--sans)}} .tipo .f3{{font:500 1.1rem var(--mono)}}
.ui{{background:var(--surf);border:1px solid var(--line);border-radius:12px;padding:14px;display:grid;gap:10px;max-width:420px}} .ui h4{{margin:0;font:700 18px var(--disp)}} .ui p{{color:var(--muted);font-size:.95rem}}
.chip{{display:inline-flex;align-items:center;gap:6px;font-weight:600;font-size:12px;padding:4px 10px;border-radius:999px;background:var(--soft);color:var(--brand)}} .chip span{{width:14px;height:14px;display:block}} .chip svg{{width:100%;height:100%}}
.btn{{display:inline-block;background:{ORO};color:{INK};font-weight:700;padding:9px 14px;border-radius:10px}} .btn2{{display:inline-block;background:var(--brand);color:var(--bg);font-weight:700;padding:9px 14px;border-radius:10px}} .lnk{{color:var(--acc);font-weight:700}}
.est{{display:flex;gap:8px;flex-wrap:wrap;font-size:12px;font-weight:600}} .est span{{padding:4px 10px;border-radius:6px;color:#fff}}
.folio{{background:#FBF9F4;color:{INK};border:1px solid #E7E1D6;border-radius:4px;padding:14px;font:12px/1.5 var(--mono);display:grid;gap:4px;max-width:360px}} .folio b{{font:700 15px var(--disp)}} .folio .sello{{width:52px;height:52px;justify-self:end}} .folio .sello svg{{width:100%;height:100%}}
img{{max-width:100%;height:auto;display:block;border-radius:12px;border:1px solid var(--line)}}
.regla{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}} .regla>div{{border-top:3px solid var(--text);padding-top:10px;display:grid;gap:4px}} .regla .no{{border-color:{ROJO}}}
@media (max-width:600px){{.tipo>div{{grid-template-columns:1fr}}}}
</style></head><body><main>
<header class="hero"><span class="eyebrow">Manual de marca · Laranda</span><h1 style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Laranda</h1>
<div class="wm">{s('lockup-h').replace(INK,'var(--text)').replace(HUESO,'var(--bg)').replace(VIO,'var(--brand)').replace(NAR,'var(--acc)')}</div>
<p class="big">Tu oficio, en flor. <span style="color:var(--muted);font-weight:400">Your craft, in bloom.</span></p>
<p class="sub">Laranda es la jacaranda sin la jota: misma floración, mismo violeta, nombre propio. La marca no ilustra un árbol; captura el instante de florecer, cuando el oficio de un profesional independiente se hace público: perfil, agenda, folio, reseñas.</p></header>

<section><span class="eyebrow">El símbolo</span><h2>Una flor dibujada, con un pétalo que se abre</h2>
<p>Línea de tinta a mano, cinco lóbulos abiertos, una mancha violeta plana que no coincide con la línea, como una impresión mal registrada. El lóbulo superior derecho está separado del resto y es el único en naranja: es el que se abre. La garganta queda vacía: el punto que se llena. El desfase de la mancha es fijo, siempre hacia abajo y a la derecha.</p>
<div class="tiles"><div class="tile clara">{s('simbolo')}<small>claro</small></div><div class="tile clara">{s('simbolo-tinta')}<small>una tinta</small></div><div class="tile oscura">{s('simbolo-oscuro')}<small>oscuro: línea hueso, mancha lila</small></div><div class="tile oscura">{s('simbolo-blanco')}<small>una tinta sobre oscuro</small></div></div>
<h3>De 16 a 32 px: la silueta</h3><p class="sub">Cinco discos, uno separado, garganta vacía. Deriva de la flor y conserva sus dos rasgos. Favicon, avatar chico, chips y sellos pequeños.</p>
<div class="fila"><span style="width:16px;height:16px">{s('silueta')}</span><span style="width:24px;height:24px">{s('silueta')}</span><span style="width:32px;height:32px">{s('silueta')}</span><span style="width:40px;height:40px">{s('simbolo')}</span><span style="width:64px;height:64px">{s('simbolo')}</span><span style="width:32px;height:32px">{s('silueta-acento')}</span></div></section>

<section><span class="eyebrow">Bloom</span><h2>La flor se abre</h2>
<p>Al publicar el perfil, confirmar una cita o recibir la primera reseña, la flor se abre en 500 ms: los lóbulos crecen desde la garganta y el lóbulo naranja se separa al final. Con «reducir movimiento», aparece ya abierta.</p>
<div class="fila"><span style="width:160px;height:160px;border-radius:14px"><img alt="Animación bloom" src="data:image/gif;base64,{gif}" style="border:0"></span><span style="width:160px;height:160px">{s('simbolo-bloom')}</span></div><p class="sub">Izquierda: GIF. Derecha: el SVG animado, que respeta la preferencia del sistema.</p></section>

<section><span class="eyebrow">App icon, avatar y favicon</span><h2>Violeta con línea hueso</h2>
<p>Fondo violeta, línea en hueso, mancha en lila, lóbulo en naranja claro. El maskable deja un margen del 20 %. El favicon usa la silueta y cambia con el esquema del sistema: violeta en claro, lila en oscuro.</p>
<div class="fila"><span style="width:120px;height:120px">{s('app-icon-redondeado')}</span><span style="width:120px;height:120px;border-radius:50%">{s('app-icon-maskable')}</span><span style="width:60px;height:60px;border-radius:50%">{s('avatar')}</span><span style="width:60px;height:60px">{s('app-icon-claro')}</span><div class="barra"><div class="tab"><span>{s('favicon')}</span>laranda</div></div><div class="barra n"><div class="tab"><span>{fav_d}</span>laranda</div></div></div></section>

<section><span class="eyebrow">Logotipo y lockups</span><h2>laranda, en caja baja</h2>
<p>Bricolage Grotesque 600 convertida a trazados. Siempre en minúsculas. Lockup horizontal para web, correo y cabeceras; vertical para redes y carteles. Área de respeto: la altura del punto central de la flor. Mínimos: horizontal 120 px, vertical 80 px, símbolo 40 px (silueta por debajo), wordmark 80 px.</p>
<div class="tiles"><div class="tile clara" style="max-width:none">{s('lockup-h').replace('viewBox','style="max-width:380px" viewBox')}<small>horizontal</small></div><div class="tile oscura">{s('lockup-h-oscuro').replace('viewBox','style="max-width:380px" viewBox')}<small>horizontal oscuro</small></div><div class="tile clara">{s('lockup-v').replace('viewBox','style="max-width:150px" viewBox')}<small>vertical</small></div><div class="tile clara">{s('lockup-h-tinta').replace('viewBox','style="max-width:380px" viewBox')}<small>una tinta</small></div></div></section>

<section><span class="eyebrow">Color</span><h2>Intenso y neutro en género</h2>
<p>Violeta para marca y acción; naranja como acento; oro solo para reservar; verde y rojo para estados, siempre con icono y texto. Fondo hueso frío. Validado con simulación de daltonismo: todas las parejas se distinguen con visión normal y bajo protanopia, deuteranopia y tritanopia con el apoyo del icono.</p>
<div class="sw"><div><div class="c" style="background:{VIO}"></div><b>violeta</b><code>{VIO}</code></div><div><div class="c" style="background:{VIO2}"></div><b>presionado</b><code>{VIO2}</code></div><div><div class="c" style="background:{LILA}"></div><b>lila</b><code>{LILA}</code></div><div><div class="c" style="background:{NAR}"></div><b>naranja</b><code>{NAR}</code></div><div><div class="c" style="background:{NART}"></div><b>naranja tinte</b><code>{NART}</code></div><div><div class="c" style="background:{ORO}"></div><b>oro · reservar</b><code>{ORO}</code></div><div><div class="c" style="background:{VERDE}"></div><b>verde · éxito</b><code>{VERDE}</code></div><div><div class="c" style="background:{ROJO}"></div><b>rojo · error</b><code>{ROJO}</code></div><div><div class="c" style="background:{INK}"></div><b>tinta</b><code>{INK}</code></div><div><div class="c" style="background:{HUESO}"></div><b>hueso</b><code>{HUESO}</code></div></div>
<div class="wrap"><table><thead><tr><th>Par</th><th>Contraste</th><th>Sirve para</th></tr></thead><tbody>
<tr><td>Tinta sobre hueso</td><td class="num">16.8:1</td><td>Texto</td></tr><tr><td>Violeta sobre hueso</td><td class="num">7.0:1</td><td>Texto, símbolo, botones (texto blanco 7.7:1)</td></tr><tr><td>Naranja sobre hueso</td><td class="num">3.2:1</td><td>Gráfico y texto grande; texto chico en tinta sobre tinte (12.1:1)</td></tr><tr><td>Tinta sobre oro</td><td class="num">8.2:1</td><td>Botón Reservar</td></tr><tr><td>Blanco sobre verde / rojo</td><td class="num">4.1:1 / 7.2:1</td><td>Estados, con icono y texto</td></tr><tr><td>Lila / naranja claro sobre tinta</td><td class="num">9.9:1 / 8.9:1</td><td>Marca y acento en oscuro</td></tr></tbody></table></div>
<img alt="Simulación de daltonismo de la lámina" src="data:image/png;base64,{cvd}"><p class="sub">Arriba a la izquierda, visión normal; después protanopia, deuteranopia y tritanopia.</p></section>

<section><span class="eyebrow">Tipografía</span><h2>Bricolage Grotesque y Onest</h2>
<div class="tipo"><div><span class="f1">Bricolage 600/700</span><p>Wordmark, títulos y cifras grandes. Tamaño óptico 96 en el wordmark. Tiene algo de dibujo en las curvas que conversa con la flor.</p></div><div><span class="f2">Onest 400 / 500 / 700</span><p>Interfaz y cuerpo: etiquetas, botones, ayudas. Nunca compite con la primaria en una misma línea.</p></div><div><span class="f3">Plex Mono 500</span><p>Folios y códigos.</p></div></div></section>

<section><span class="eyebrow">En uso</span><h2>Perfil, estados y folio</h2>
<div class="fila"><div class="ui"><h4>Andrés Cortés</h4><div style="display:flex;gap:6px;flex-wrap:wrap"><span class="chip"><span>{s('silueta').replace(VIO,'var(--brand)').replace(HUESO,'var(--soft)')}</span>Barbería</span><span class="chip" style="background:var(--acc-t);color:var(--text)"><span>{s('silueta').replace(VIO,'var(--acc)').replace(HUESO,'var(--acc-t)')}</span>Afeitado clásico</span></div><p>Corte, barba y navaja. Centro, Oaxaca.</p><div><span class="btn">Reservar</span> &nbsp; <span class="btn2">Ver agenda</span></div><p>Próximo espacio: <b>vie 24 oct · 16:00</b> · <span class="lnk">ver todos</span></p><div class="est"><span style="background:{VERDE}">✓ Folio emitido</span><span style="background:{ROJO}">✕ Cancelada</span></div></div>
<div class="folio"><b>laranda</b>FOLIO LR-2026-00417<br>Corte y barba · Andrés C.<br>24 oct 2026 · 16:00 · $350.00<br>Pagado · tarjeta ····4821<span class="sello">{s('sello')}</span></div></div>
<p class="sub">El oro solo aparece en Reservar. Cada estado lleva color, icono y texto. El folio va en papel crema con la flor en tinta como sello.</p></section>

<section><span class="eyebrow">Uso</span><h2>Reglas cortas</h2>
<div class="regla"><div><h3>Área de respeto</h3><p>La altura del punto central de la flor, alrededor de toda pieza.</p></div><div><h3>Fondos permitidos</h3><p>Hueso, blanco, arena, tinta y violeta. Sobre fotografía, con un bloque de hueso detrás.</p></div><div><h3>El desfase</h3><p>Siempre hacia abajo y a la derecha, la misma distancia. No se «corrige».</p></div><div class="no"><h3>No</h3><p>No cerrar los lóbulos, no quitar el separado, no rellenar la garganta, no degradados, no oro fuera de reservar, no la J de jacaranda, no explicar el nombre.</p></div></div>
<p class="sub">Archivos en <code>.fruti/icons/laranda/final/</code>: SVG, PNG 16 a 1024, favicon.ico, maskable, GIF y <code>tema.json</code>.</p></section>
</main></body></html>'''
open('guia-marca.html','w').write(html); print(len(html))
