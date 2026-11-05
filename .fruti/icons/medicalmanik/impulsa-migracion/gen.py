# Impulsa Manik · guía de migración al sistema común. Aprobado (2026-11-05): «alinéalo en los tres puntos» (tipografía,
# color de acción, lienzo). Sin acceso al código de Impulsa: la guía da valores, búsquedas, orden y comprobaciones.
# Valores leídos de ../design-system/project/tokens.json. Mediciones de ancho: Chromium, Google Fonts, 2026-11-05.
# Uso: python3 gen.py → guia.html
import os, json, html
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
T = json.load(open(os.path.join(M, 'design-system/project/tokens.json')))
V = {}
for g in ('color', 'radius', 'shadow', 'layout', 'spacing'):
    for x in T[g]['tokens']: V[x['name']] = x['value']
for k, v in V.items():
    if isinstance(v, str) and v.startswith('{'): V[k] = V[v.strip('{}')]
TIPO = {s['name']: s for g in T['type']['groups'] for s in g['styles']}
FAM = T['type']['families']

CSS_VARS = ['canvas', 'surface', 'surface-soft', 'surface-pressed', 'ink', 'muted', 'line', 'line-control', 'manik', 'manik-hover', 'manik-soft', 'on-manik', 'focus',
            'app-impulsa', 'app-impulsa-soft', 'app-impulsa-ink', 'exito', 'exito-soft', 'on-exito-soft', 'aviso', 'aviso-soft', 'on-aviso-soft', 'error', 'error-soft', 'on-error-soft',
            'info', 'info-soft', 'on-info-soft', 'radius-sm', 'radius-md', 'radius-lg', 'radius-2xl', 'control-height', 'control-height-compact', 'header-height']
snippet = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
           '<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700&display=swap" rel="stylesheet">\n\n'
           ':root {\n' + ''.join(f'  --{k}: {V[k]};\n' for k in CSS_VARS) +
           f'  --font-display: {FAM["display"]};\n  --font-sans: {FAM["sans"]};\n}}\n'
           'body { background: var(--canvas); color: var(--ink); font: 400 16px/24px var(--font-sans); }\n'
           'h1, h2, h3 { font-family: var(--font-display); font-weight: 600; }\n'
           '.btn-primario { background: var(--manik); color: var(--on-manik); }\n.btn-primario:hover { background: var(--manik-hover); }\n'
           ':focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }\n'
           'table, .num { font-variant-numeric: tabular-nums; }')

MAPA = [  # (qué es, hoy en Impulsa, pasa a, token)
 ('Fondo de página', '#F4F4F4', V['canvas'], 'canvas'),
 ('Botón principal: fondo', '#504CA1', V['manik'], 'manik'),
 ('Botón principal: hover y presionado', 'violeta más oscuro', V['manik-hover'], 'manik-hover'),
 ('Botón secundario: texto y borde', 'violeta', f'{V["manik"]} · borde {V["line-control"]}', 'manik · line-control'),
 ('Enlaces', 'violeta', V['manik'], 'manik'),
 ('Selección, pestaña o filtro activo (fondo suave)', 'violeta claro', V['manik-soft'], 'manik-soft'),
 ('Anillo de foco', 'el que tenga', f'{V["focus"]}, 2 px, separación 2 px', 'focus'),
 ('Sello, tarjeta en el inicio y en el selector', '#504CA1', f'{V["app-impulsa"]} (sin cambio)', 'app-impulsa'),
 ('Fondo de la tarjeta de Impulsa', '—', V['app-impulsa-soft'], 'app-impulsa-soft'),
 ('Grises de texto, bordes y superficies', 'grises neutros', f'ink {V["ink"]} · muted {V["muted"]} · line {V["line"]} · surface-soft {V["surface-soft"]}', 'por rol'),
]
mapa = ''.join(f'<tr><th scope="row">{a}</th><td><span class="sw" style="background:{b if b.startswith("#") else "transparent"}"></span>{b}</td><td><span class="sw" style="background:{c.split()[0] if c.startswith("#") else "transparent"}"></span>{html.escape(c)}</td><td><code>{d}</code></td></tr>' for a, b, c, d in MAPA)
ESTILOS = [('Título de página', 'title-1'), ('Título de tarjeta, panel o diálogo', 'title-2'), ('Texto', 'body'), ('Texto en tablas', 'body-sm'), ('Etiqueta de campo', 'label'), ('Botón', 'button'), ('Dato clínico o cifra', 'dato')]
tipos = ''.join(f'<tr><th scope="row">{a}</th><td>{"Urbanist" if b.startswith("title") else "Atkinson Hyperlegible Next"}</td><td class="num">{TIPO[b]["fontSize"]} / {TIPO[b]["lineHeight"]} · {TIPO[b]["fontWeight"]}</td><td><code>{b}</code></td></tr>' for a, b in ESTILOS)
MED = [('Revisión de presión arterial', '0.978', '1.153', '1.085'), ('Campañas activas este mes', '0.997', '1.180', '1.159'), ('1 240 pacientes · 30/11/2026', '0.989', '1.171', '1.053'),
       ('Nueva campaña', '0.983', '1.140', '1.150'), ('Guardar y enviar', '0.977', '1.121', '1.127'), ('Resultados por segmento de edad', '0.972', '1.176', '1.142')]
pct = lambda s: (lambda v: '0 %' if abs(v) < .5 else f'{v:+.0f} %')((float(s) - 1) * 100)
med = ''.join(f'<tr><th scope="row">«{a}»</th><td class="num">{pct(b)}</td><td class="num">{pct(c)}</td><td class="num">{pct(d)}</td></tr>' for a, b, c, d in MED)
PASOS = [
 ('Fondo de página', 'Cambiar #F4F4F4 por canvas.', 'Una variable o un reemplazo. La diferencia mide 1.03 (no se ve): sirve para comprobar que el cambio de valores funciona sin tocar la experiencia.', 'Ninguna pantalla cambia de forma visible; las tarjetas blancas siguen separándose del fondo.'),
 ('Color de acción', 'Botones, enlaces, selección y foco a azul Manik. El violeta se queda solo en el sello y en la tarjeta de Impulsa.', 'Es el cambio de identidad de la interfaz: Impulsa se ve parte de la familia.', 'Buscar #504CA1 en el código: solo debe quedar en el sello y en la tarjeta. Contraste del botón: blanco sobre azul 8.54:1.'),
 ('Tipografía', 'Ubuntu → Urbanist en títulos y Atkinson Hyperlegible Next en todo lo demás, con la escala de la tabla.', 'Es el cambio más visible y el único que mueve anchos: botones y títulos crecen.', 'Revisar botones en barras y tablas, títulos largos y celdas con cifras en 390 px y 1440 px; nada recortado ni en dos líneas sin querer.'),
 ('Shell de app pequeña', 'Barra superior común y pestañas Campañas y Resultados (componente AppPequena). «Nueva campaña» es botón del encabezado, no pestaña.', 'Termina de alinear la navegación con las otras seis apps.', 'Las pestañas son enlaces con aria-current; el contenido va centrado a 1120 px.'),
]
pasos = ''.join(f'<li><h3>{a}</h3><p>{b}</p><p class="nota"><b>Por qué en este orden:</b> {c}</p><p class="nota"><b>Cómo se comprueba:</b> {d}</p></li>' for a, b, c, d in PASOS)
BUSCAR = ['504CA1', '504ca1', 'rgb(80, 76, 161)', 'rgb(80,76,161)', 'F4F4F4', 'f4f4f4', 'Ubuntu', "font-family"]

HTML = f'''<title>Migración de Impulsa</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;600;700&display=swap" rel="stylesheet">
<style>
/* Guía técnica de una sola luz (tema claro único de la marca): columna de lectura, tablas de mapeo y bloque de código. */
:root{{--azul:{V["manik"]};--violeta:{V["app-impulsa"]};--violeta-s:{V["app-impulsa-soft"]};--papel:{V["canvas"]};--blanco:#FFFFFF;--tinta:{V["ink"]};--muted:{V["muted"]};--linea:{V["line"]};--suave:{V["surface-soft"]};--codigo:#0F1C3F;
 --display:{FAM["display"]};--sans:{FAM["sans"]};color-scheme:light}}
*{{box-sizing:border-box}}body{{background:var(--papel);color:var(--tinta);font:400 16px/1.6 var(--sans);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
h1,h2,h3{{font-family:var(--display);margin:0;text-wrap:balance}}h1{{font-size:clamp(30px,4.6vw,44px);line-height:1.1;font-weight:300}}h1 b{{font-weight:600}}h2{{font-size:24px;line-height:1.25;font-weight:600}}h3{{font-size:19px;font-weight:600}}p{{margin:0}}a{{color:var(--azul)}}:focus-visible{{outline:2px solid var(--azul);outline-offset:2px}}
.hoja{{max-width:1000px;margin:0 auto;padding-block:36px 96px;display:grid;gap:44px;grid-template-columns:minmax(0,1fr)}}
.eti{{font:700 12px/16px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--violeta)}}.nota{{font-size:15px;line-height:22px;color:var(--muted)}}.texto{{max-width:66ch;display:grid;gap:12px}}p.texto{{display:block}}
section{{display:grid;gap:16px}}
.cab{{display:grid;gap:12px;background:var(--blanco);border:1px solid var(--linea);border-radius:24px;padding:28px}}
.tres{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}.tres div{{background:var(--suave);border-radius:16px;padding:14px;display:grid;gap:4px}}.tres b{{font:600 16px var(--display)}}.tres span{{font-size:14px;line-height:20px;color:var(--muted)}}
.tw{{overflow-x:auto;background:var(--blanco);border:1px solid var(--linea);border-radius:18px}}table{{border-collapse:collapse;width:100%;min-width:640px}}th,td{{text-align:left;vertical-align:top;padding:11px 14px;border-bottom:1px solid var(--linea);font-size:15px;line-height:22px}}thead th{{font:700 12px/16px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:var(--suave)}}tbody tr:last-child>*{{border-bottom:0}}tbody th{{font-weight:600}}td.num{{font-variant-numeric:tabular-nums;white-space:nowrap}}
.sw{{display:inline-block;width:14px;height:14px;border-radius:4px;margin-right:6px;vertical-align:-2px;border:1px solid rgba(20,33,61,.12)}}
code{{font:13px/1.5 ui-monospace,Menlo,Consolas,monospace;background:var(--suave);border-radius:6px;padding:1px 6px}}
pre{{margin:0;background:var(--codigo);color:#E6ECF7;border-radius:18px;padding:18px 20px;overflow-x:auto;font:13px/1.6 ui-monospace,Menlo,Consolas,monospace}}
.pasos{{margin:0;padding-left:26px;display:grid;gap:16px}}.pasos li{{background:var(--blanco);border:1px solid var(--linea);border-radius:18px;padding:16px 18px;display:grid;gap:6px}}
.copiar{{justify-self:start;min-height:40px;padding:0 16px;border-radius:12px;border:1px solid var(--linea);background:var(--blanco);font:600 14px var(--sans);color:var(--azul);cursor:pointer}}
ul{{margin:0;padding-left:22px;display:grid;gap:6px}}
@media(max-width:700px){{.tres{{grid-template-columns:1fr}}}}
</style>
<main class="hoja">
<header class="cab"><span class="eti">Impulsa Manik · guía de migración · aprobada el 5 de noviembre de 2026</span>
<h1>Impulsa entra al <b>sistema común</b></h1>
<p class="texto">Impulsa ya comparte con las otras apps el espaciado, los radios, las sombras, los estados y los iconos. Le faltan tres cosas, aprobadas para alinearse. El violeta no desaparece: deja los botones y se queda donde dice «esto es Impulsa», en su sello y en su tarjeta.</p>
<div class="tres"><div><b>Lienzo</b><span>#F4F4F4 → {V["canvas"]}</span></div><div><b>Acción</b><span>violeta #504CA1 → azul Manik {V["manik"]}</span></div><div><b>Tipografía</b><span>Ubuntu → Urbanist + Atkinson Hyperlegible Next</span></div></div>
<p class="nota">Esta guía se escribió sin ver el código de Impulsa: dice qué valores cambian y cómo comprobarlo, no en qué archivos están.</p></header>

<section aria-labelledby="h1"><h2 id="h1">Por qué</h2><div class="texto"><p><b>Una sola familia de controles.</b> En las siete apps, todo lo que se toca usa el azul Manik, el mismo alto y el mismo foco; así nadie reaprende al pasar de Agenda a Impulsa.</p><p><b>Identidad e interfaz no se mezclan.</b> El color de cada producto vive en su sello y su tarjeta; si fuera color de botón, cada app tendría un «Guardar» de otro color.</p><p><b>Legibilidad.</b> Atkinson Hyperlegible Next distingue 1, l e I y 0 y O: en cifras de campañas, fechas y públicos no hay confusión.</p></div></section>

<section aria-labelledby="h2"><h2 id="h2">Qué cambia, valor por valor</h2><div class="tw" tabindex="0" role="region" aria-label="Mapeo de colores"><table><thead><tr><th scope="col">Qué es</th><th scope="col">Hoy en Impulsa</th><th scope="col">Pasa a</th><th scope="col">Token</th></tr></thead><tbody>{mapa}</tbody></table></div>
<p class="nota">Contrastes: blanco sobre azul Manik 8.54:1 (antes, sobre violeta, 7.27:1). La distancia de color entre #F4F4F4 y {V["canvas"]} es 1.03: el lienzo cambia de valor sin cambiar a la vista.</p></section>

<section aria-labelledby="h3"><h2 id="h3">Tipografía</h2><div class="tw" tabindex="0" role="region" aria-label="Escala tipográfica"><table><thead><tr><th scope="col">Uso</th><th scope="col">Familia</th><th scope="col">Tamaño / interlineado · peso</th><th scope="col">Estilo</th></tr></thead><tbody>{tipos}</tbody></table></div>
<h3>Qué tanto cambian los anchos</h3><p class="nota">Medido en el navegador con las fuentes de Google Fonts. Se supuso que Impulsa usa Ubuntu 400 en texto y 500 en botones y títulos; si usa otros pesos, los números cambian.</p>
<div class="tw" tabindex="0" role="region" aria-label="Cambio de ancho"><table><thead><tr><th scope="col">Texto</th><th scope="col">Texto 16 px (Atkinson 400)</th><th scope="col">Botón 15 px (Atkinson 600)</th><th scope="col">Título 24 px (Urbanist 600)</th></tr></thead><tbody>{med}</tbody></table></div>
<p class="texto">El texto corrido queda igual (2 a 3 % más angosto). <b>Los botones crecen del 12 al 18 %</b> y los títulos del 5 al 16 %: ahí hay que revisar barras de acciones, celdas de tabla con botones y títulos largos.</p></section>

<section aria-labelledby="h4"><h2 id="h4">Valores listos para copiar</h2><p class="nota">Variables del sistema común, leídas de los tokens publicados. Si Impulsa ya usa variables CSS, basta con apuntarlas a estas.</p>
<pre id="codigo">{html.escape(snippet)}</pre><button type="button" class="copiar" id="copiar">Copiar código</button><p class="nota" id="estado" role="status"></p></section>

<section aria-labelledby="h5"><h2 id="h5">En qué orden</h2><ol class="pasos">{pasos}</ol></section>

<section aria-labelledby="h6"><h2 id="h6">Cómo encontrar los valores en el código</h2><p class="nota">Buscar en todo el proyecto (estilos, plantillas y componentes):</p><ul>{"".join(f"<li><code>{html.escape(b)}</code></li>" for b in BUSCAR)}</ul>
<p class="nota">Al terminar, <code>504CA1</code> solo debe aparecer en el sello y en la tarjeta de Impulsa, y <code>Ubuntu</code> en ningún lado.</p></section>

<section aria-labelledby="h7"><h2 id="h7">Qué no cambia</h2><ul><li>Espaciado, radios, sombras, colores de estado e iconos: ya son los del sistema común.</li><li>El violeta como identidad: sello, tarjeta en el inicio y en el selector, «con Impulsa Manik» en las promociones del directorio.</li><li>El contenido y los flujos de Impulsa.</li></ul>
<p class="nota">Referencia completa: <a href="https://claude.ai/artifact/28z6yfie6L8btocL8QBZi9" target="_blank" rel="noopener">sistema de diseño del Ecosistema ↗</a> (Boton, Campo, AppPequena y tokens).</p></section>
</main>
<script>document.getElementById('copiar').addEventListener('click',()=>{{const t=document.getElementById('codigo').textContent,e=document.getElementById('estado');
const sel=()=>{{const r=document.createRange();r.selectNodeContents(document.getElementById('codigo'));const s=getSelection();s.removeAllRanges();s.addRange(r);e.textContent='Código seleccionado: cópialo con Ctrl+C o ⌘C.'}};
try{{navigator.clipboard.writeText(t).then(()=>e.textContent='Copiado.',sel)}}catch(_){{sel()}}}});</script>'''
open(os.path.join(D, 'guia.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
