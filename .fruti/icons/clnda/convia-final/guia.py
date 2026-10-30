# Convia · genera guia.html (manual de identidad) desde tema.json y svg/. Uso: python3 guia.py (después de gen.py y png.cjs)
import base64, json, os
D = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(D, 'tema.json'))); C = T['color']; K = T['contraste']; CAT = T['categorias']
u = lambda f: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.normpath(os.path.join(D, 'svg', f)), 'rb').read()).decode()
og = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(D, 'png', 'og-1200x630.png'), 'rb').read()).decode()
def sw(n, h, note): return f'<div class="sw"><i style="background:{h}"></i><div><b>{n}</b><code>{h}</code><small>{note}</small></div></div>'
cats = ''.join(f'''<div class="cat"><div class="catsw"><i style="background:{c['punto']}"></i><i style="background:{c['fondo']}"></i><i style="background:{c['texto']}"></i></div>
<span class="chip" style="background:{c['fondo']};color:{c['texto']}"><b class="dot" style="background:{c['punto']}"></b>{c['nombre']}</span>
<small><code>{c['punto']}</code> punto · <code>{c['fondo']}</code> fondo · <code>{c['texto']}</code> texto {c['texto/fondo']}:1</small></div>''' for c in CAT.values())
EJ = [('cafes', 'Café Tres Patios', 'Jalatlaco · abierto hasta 21:00'), ('hoteles', 'Hotel Patio de Luz', 'Centro · desde $2,480'),
      ('talleres', 'Barro bruñido para principiantes', 'Sáb 26 · 11:00 · $650'), ('recorridos', 'Caminata de cantera al amanecer', 'Dom 27 · 7:00 · $300')]
sel = ''.join(f'''<div class="sel"><div class="selr"><img src="{u('../sellos/' + k + '-sello.svg')}" alt="Sello Convia {c['nombre']}"><img src="{u('../sellos/' + k + '-sello-solido.svg')}" alt="Sello sólido Convia {c['nombre']}"></div>
<img class="sl" src="{u('../sellos/' + k + '-logotipo.svg')}" alt="Convia {c['nombre']}"></div>''' for k, c in CAT.items())
cards = ''.join(f'''<article class="card"><div class="ph"></div><span class="chip" style="background:{CAT[k]['fondo']};color:{CAT[k]['texto']}"><b class="dot" style="background:{CAT[k]['punto']}"></b>{CAT[k]['nombre']}</span>
<h4>{n}</h4><p>{m}</p></article>''' for k, n, m in EJ)
html = f'''<title>Convia Marca</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT,WONK@9..144,300..700,0..100,0..1&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* Manual de identidad: una columna editorial; secciones numeradas porque son un orden de lectura. Tema claro por decisión de marca. */
:root{{--papel:{C['papel']};--sup:#fff;--tinta:{C['tinta']};--sec:{C['texto_sec']};--linea:{C['linea']};--cantera:{C['cantera']};--suave:{C['cantera_suave']};--arena:{C['arena']};
--display:"Fraunces",Georgia,serif;--dv:"SOFT" 100,"WONK" 0,"opsz" 96;--text:"Figtree",system-ui,-apple-system,"Segoe UI",sans-serif;--r:16px;--r-s:12px;color-scheme:light}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--papel);color:var(--tinta);font:400 16px/1.6 var(--text)}}
.wrap{{max-width:1080px;margin:0 auto;padding-left:max(24px,env(safe-area-inset-left,0px));padding-right:max(24px,env(safe-area-inset-right,0px))}}
.d{{font-family:var(--display);font-weight:500;font-variation-settings:var(--dv)}}
header.h .wrap{{padding-block:64px 40px;display:grid;gap:26px}}header.h img{{height:72px;width:auto;max-width:100%}}
.h h1{{font-size:clamp(38px,5vw,60px);line-height:1.05;margin:0;letter-spacing:-.02em;text-wrap:balance;max-width:18ch}}.h p{{margin:0;color:var(--sec);font-size:18px;max-width:58ch}}
section .wrap{{padding-block:44px;border-top:1px solid var(--linea);display:grid;gap:22px}}
.n{{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--cantera);font-weight:600;margin:0}}
h2{{font-size:34px;line-height:1.1;margin:0;letter-spacing:-.01em}}h3{{font:600 15px var(--text);margin:0}}
p{{margin:0;max-width:68ch}}.muted{{color:var(--sec)}}code{{font-size:.86em}}
.g2{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}.g3{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}.g4{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}}
.tile{{background:var(--sup);border:1px solid var(--linea);border-radius:var(--r);padding:32px;display:grid;place-items:center;min-height:180px;min-width:0}}.tile.dk{{background:{C['oscuro_fondo']};border-color:{C['oscuro_fondo']}}}
.tile img{{max-width:100%;height:56px}}.tile img.s{{height:96px}}.cap{{font-size:13px;color:var(--sec);margin-top:8px}}
.safe{{justify-self:start;padding:28px;border:1px dashed var(--sec);border-radius:var(--r);background:var(--sup)}}.safe img{{height:56px;display:block}}
.sw{{display:flex;gap:12px;align-items:center;min-width:0}}.sw i{{flex:0 0 52px;height:52px;border-radius:var(--r-s);border:1px solid #0001}}.sw div{{display:grid;line-height:1.3;min-width:0}}.sw code,.sw small{{font-size:12.5px;color:var(--sec)}}
.prim{{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:10px}}.prim div{{border-radius:var(--r);padding:16px;min-height:120px;display:flex;flex-direction:column;justify-content:flex-end;font-size:13px}}.prim b{{font-size:15px}}
.cat{{display:grid;gap:10px;background:var(--sup);border:1px solid var(--linea);border-radius:var(--r);padding:16px;min-width:0}}.catsw{{display:flex;gap:6px}}.catsw i{{width:34px;height:34px;border-radius:10px;border:1px solid #0001}}.cat small{{color:var(--sec);font-size:12px;line-height:1.5}}
.chip{{display:inline-flex;align-items:center;gap:7px;justify-self:start;border-radius:999px;padding:4px 12px 4px 9px;font-weight:600;font-size:13px}}.dot{{width:9px;height:9px;border-radius:50%;display:inline-block}}
.card{{background:var(--sup);border:1px solid var(--linea);border-radius:var(--r);padding:12px;display:grid;gap:8px;min-width:0}}.card .ph{{aspect-ratio:4/3;border-radius:var(--r-s);background:var(--arena)}}.card h4{{margin:0;font:500 19px/1.2 var(--display);font-variation-settings:var(--dv)}}.card p{{font-size:14px;color:var(--sec);font-variant-numeric:tabular-nums}}
.type{{background:var(--sup);border:1px solid var(--linea);border-radius:var(--r);padding:28px;display:grid;gap:20px;min-width:0}}.lbl{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--sec);display:block;margin-bottom:4px}}
.forma{{display:flex;flex-wrap:wrap;gap:16px;align-items:center}}.btn{{background:var(--cantera);color:#fff;border-radius:999px;padding:12px 22px;font-weight:600}}.btn.l{{background:transparent;color:var(--tinta);border:1px solid var(--tinta)}}.field{{border:1px solid var(--linea);background:var(--papel);border-radius:var(--r-s);padding:11px 14px;min-width:200px;color:var(--sec)}}
.voz{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}.voz div{{background:var(--sup);border:1px solid var(--linea);border-radius:var(--r);padding:20px}}.voz ul{{margin:8px 0 0;padding-left:18px}}
.sel{{background:var(--sup);border:1px solid var(--linea);border-radius:var(--r);padding:18px;display:grid;gap:14px;min-width:0}}.selr{{display:flex;gap:12px}}.selr img{{width:min(46%,150px);height:auto}}.sl{{height:30px;width:auto;max-width:100%;justify-self:start}}
.og{{width:100%;height:auto;border:1px solid var(--linea);border-radius:var(--r)}}ol.r{{margin:0;padding-left:20px;display:grid;gap:6px}}
@media (max-width:860px){{.g2,.g3,.voz{{grid-template-columns:1fr}}.g4{{grid-template-columns:repeat(2,minmax(0,1fr))}}.prim{{grid-template-columns:1fr 1fr}}}}
@media (max-width:480px){{.g4{{grid-template-columns:1fr}}}}
</style>
<header class="h"><div class="wrap"><img src="{u('logotipo.svg')}" alt="Convia"><h1 class="d">Lo que vale la pena en Oaxaca, escogido por gente de aquí.</h1>
<p>Manual de identidad de Convia, el directorio web de planes, lugares y talleres de Oaxaca. Versión 2. Marca independiente.</p></div></header>
<main>
<section><div class="wrap"><p class="n">01 · Concepto</p><h2 class="d">Una invitación con buen gusto</h2>
<p><b>Convia</b> une <i>convite</i>, la invitación que recorre las calles, y <i>vía</i>, el camino. Habla como un amigo de aquí que sabe a dónde ir, con la calma de una buena guía: elegante, pulcra y suave; nunca folclórica ni infantil.</p>
<p class="muted">El símbolo es una estrella de un solo trazo, dibujada a mano e inclinada, abstraída de las estrellas que se cargan en el convite. Su trazo suave marca el tono de todo lo demás: letras con terminaciones redondeadas y esquinas amables.</p></div></section>
<section><div class="wrap"><p class="n">02 · Logotipo</p><h2 class="d">Versiones</h2>
<div class="g2"><div><div class="tile"><img src="{u('logotipo.svg')}" alt="Logotipo sobre claro"></div><p class="cap">Principal, sobre claro</p></div>
<div><div class="tile dk"><img src="{u('logotipo-oscuro.svg')}" alt="Logotipo sobre oscuro"></div><p class="cap">Sobre oscuro</p></div></div>
<div class="g3"><div><div class="tile"><img class="s" src="{u('simbolo.svg')}" alt="Símbolo"></div><p class="cap">Símbolo solo (avatar, sello, marcador)</p></div>
<div><div class="tile"><img src="{u('palabra.svg')}" alt="Palabra Convia"></div><p class="cap">Solo palabra</p></div>
<div><div class="tile"><img class="s" src="{u('app-icon.svg')}" alt="Ícono de app" style="height:120px;border-radius:26px"></div><p class="cap">Ícono de app y de redes</p></div></div>
<h3>Área de seguridad y tamaño mínimo</h3><div class="safe"><img src="{u('logotipo.svg')}" alt="Logotipo con área de seguridad"></div>
<p class="muted">Alrededor del logotipo se deja libre media altura de la estrella. Mínimo: logotipo 24 px de alto; estrella sola 16 px. El logotipo no se reescribe con la fuente: se usan los SVG del paquete (texto convertido a trazos).</p></div></section>
<section><div class="wrap"><p class="n">03 · Color</p><h2 class="d">Primario y de apoyo</h2><p class="muted">Cantera es el color de la marca: botones, enlaces, foco y símbolo. Los de apoyo ordenan la página sin competir con la fotografía.</p>
<div class="prim"><div style="background:{C['cantera']};color:#fff"><b>Cantera · primario</b>{C['cantera']} · {K['papel/cantera (texto en botón)']}:1 con texto claro</div>
<div style="background:{C['tinta']};color:#fff"><b>Tinta</b>{C['tinta']} · texto</div><div style="background:{C['papel']};border:1px solid var(--linea)"><b>Papel</b>{C['papel']} · fondo</div>
<div style="background:{C['arena']}"><b>Arena</b>{C['arena']} · fotos en carga, bloques</div><div style="background:{C['cantera_suave']}"><b>Cantera suave</b>{C['cantera_suave']} · destacados</div></div>
<div class="g3">{sw('Texto secundario', C['texto_sec'], f"{K['texto_sec/papel']}:1 sobre papel")}{sw('Línea', C['linea'], 'divisores y bordes')}{sw('Superficie', C['superficie'], 'tarjetas y campos')}</div>
<h3>Modo oscuro</h3><div class="g3">{sw('Fondo', C['oscuro_fondo'], 'fondo')}{sw('Tinta', C['oscuro_tinta'], f"{K['oscuro_tinta/oscuro_fondo']}:1")}{sw('Cantera clara', C['cantera_clara'], f"{K['cantera_clara/oscuro_fondo']}:1 · primario en oscuro")}</div></div></section>
<section><div class="wrap"><p class="n">04 · Categorías</p><h2 class="d">Un color para cada tipo de lugar</h2>
<p class="muted">Cada categoría tiene tres tonos: <b>punto</b> (marcador del mapa e ícono), <b>fondo</b> (etiqueta) y <b>texto</b> (contraste AA sobre su fondo y sobre papel). El color ayuda a reconocer de un vistazo, pero nunca va solo: la categoría siempre lleva su nombre. Seis colores no se distinguen entre sí sólo por tono para todas las personas; por eso el nombre es obligatorio.</p>
<div class="g3">{cats}</div><h3>Así se ven en el directorio</h3><div class="g4">{cards}</div>
<p class="muted">Regla: el color de categoría nunca reemplaza al primario. Un botón de «Ver plan» es cantera aunque esté en una tarjeta de taller.</p>
<h3>Sellos y logotipos de categoría</h3><p class="muted">Cada categoría es una submarca de Convia: un sello circular (claro y sólido) y un logotipo horizontal «Convia | Categoría». El sello se usa en portadas de sección, redes, distintivos para negocios aprobados y material impreso; el logotipo, en encabezados de sección.</p>
<div class="g3">{sel}</div>
<p class="muted">Tamaño mínimo del sello: 64 px (el texto del aro deja de leerse abajo de eso; en tamaños menores se usa la estrella sobre el fondo de la categoría). El sello no cambia de colores ni se combina con otro. La estrella del logotipo de categoría siempre es cantera: la marca madre manda.</p></div></section>
<section><div class="wrap"><p class="n">05 · Tipografía</p><h2 class="d">Fraunces suave y Figtree</h2>
<div class="type"><div><span class="lbl">Display · Fraunces 500 · SOFT 100 · logotipo y títulos</span><p class="d" style="font-size:52px;line-height:1.05;letter-spacing:-.02em">Talleres para ir solo</p></div>
<div><span class="lbl">Título de sección · Fraunces 500 · 34 px</span><p class="d" style="font-size:34px;line-height:1.1">Esta semana</p></div>
<div><span class="lbl">Texto · Figtree 400 · 16 px</span><p>Cerámica, cocina y grabado en el Centro y Jalatlaco. Grupos pequeños; no necesitas experiencia.</p></div>
<div><span class="lbl">Datos · Figtree 600 · números tabulares</span><p style="font-weight:600;font-variant-numeric:tabular-nums">Sáb 26 · 11:00 · $650 · 4 lugares</p></div></div>
<p class="muted">Fraunces lleva el eje «SOFT» al máximo para redondear sus terminaciones y hacer juego con la estrella. Horarios, precios y botones siempre en Figtree. Ambas son gratuitas (Google Fonts, licencia OFL).</p></div></section>
<section><div class="wrap"><p class="n">06 · Forma</p><h2 class="d">Esquinas suaves</h2>
<div class="forma"><span class="btn">Ver planes</span><span class="btn l">Solicitar acceso</span><span class="field">Busco: algo que hacer</span></div>
<p class="muted">Radio 16 px en tarjetas, fotos y paneles; 12 px en campos; botones en píldora. Líneas de 1 px en el tono «línea». Nada de esquinas rectas ni sombras duras.</p></div></section>
<section><div class="wrap"><p class="n">07 · Voz</p><h2 class="d">Como un amigo que sabe</h2>
<div class="voz"><div><h3>Así sí</h3><ul><li>«Este sábado hay un taller de barro para ir solo.»</li><li>«Abre hasta las 21:00; llega antes del atardecer.»</li><li>«Nueve habitaciones alrededor de un patio.»</li></ul></div>
<div><h3>Así no</h3><ul><li>«¡¡Descubre la MAGIA de Oaxaca!!»</li><li>«Los 100 lugares imperdibles.»</li><li>Emojis, mayúsculas sostenidas, superlativos.</li></ul></div></div></div></section>
<section><div class="wrap"><p class="n">08 · Aplicaciones</p><h2 class="d">Para compartir</h2><img class="og" src="{og}" alt="Imagen para compartir: logotipo de Convia y la frase lo que vale la pena en Oaxaca, escogido por gente de aquí">
<p class="muted">Imagen para compartir (1200×630), ícono de app (512, 192 y 180 px) y favicon que cambia con el modo claro u oscuro. Archivos en <code>convia-final/</code>.</p></div></section>
<section><div class="wrap"><p class="n">09 · Pendiente</p><h2 class="d">Antes de publicar</h2><ol class="r"><li>Buscar «Convia» en Marcanet (IMPI), clases 9, 35, 39 y 42; revisar dominios y redes.</li><li>Íconos de categoría (para acompañar color y nombre).</li><li>Guía de fotografía.</li><li>Textos de marca en inglés.</li></ol></div></section>
</main>'''
open(os.path.join(D, 'guia.html'), 'w').write(html)
print('ok', len(html))
