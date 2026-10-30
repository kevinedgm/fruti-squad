# Convia · prototipo de página principal (r2): identidad v2 + orden del BrandScript. Uso: python3 gen.py
# Toma logotipo, íconos y sellos de ../convia-final/. Negocios, cifras y planes son ficticios.
import os, re, json
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
T = json.load(open(os.path.join(F, 'tema.json'))); C = T['color']; CAT = T['categorias']
def svgin(path, cls='', label=None):
    s = open(os.path.join(F, path)).read()
    s = re.sub(r'<svg ', f'<svg class="{cls}" ' + ('aria-hidden="true" ' if label is None else ''), s, 1)
    if label is None: s = re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
    return s
logo = svgin('svg/logotipo.svg', 'logo', 'Convia')
ico = {k: svgin(f'iconos/{k}.svg', 'ico') for k in CAT}
sello = svgin('sellos/cafes-sello-solido.svg', 'sello')
def chip(k, txt=None):
    c = CAT[k]; return f'<span class="chip" style="--f:{c["fondo"]};--t:{c["texto"]}">{ico[k]}{txt or c["nombre"]}</span>'
PLANES = [('talleres', 'Barro bruñido para principiantes', 'Sáb 26 · 11:00', 'Para ir solo', '$650'),
          ('recorridos', 'Caminata de cantera al amanecer', 'Dom 27 · 7:00', 'Grupo pequeño', '$300'),
          ('museos', 'Noche de grabado en la galería', 'Vie 25 · 19:00', 'Con amigos', 'Entrada libre'),
          ('restaurantes', 'Menú de temporada a seis tiempos', 'Sáb 26 · 20:00', 'En pareja', '$1,200')]
LUGARES = [('cafes', 'Café Tres Patios', 'Jalatlaco', 'Café de olla y pan de la casa, en un patio con sombra.'),
           ('hoteles', 'Hotel Patio de Luz', 'Centro', 'Nueve habitaciones alrededor de un patio de cantera.'),
           ('restaurantes', 'Cocina Siete Fuegos', 'Xochimilco', 'Cocina de temporada; menú corto que cambia cada semana.')]
planes = ''.join(f'''<article class="plan"><div class="ph" aria-hidden="true"></div>{chip(k)}<h3><a href="#">{t}</a></h3>
<p class="meta"><span>{d}</span><span>{w}</span></p><p class="price">{p}</p></article>''' for k, t, d, w, p in PLANES)
lugares = ''.join(f'''<article class="lugar"><div class="ph tall" aria-hidden="true"></div>{chip(k, CAT[k]['nombre'] + ' · ' + z)}<h3><a href="#">{n}</a></h3><p class="desc">{d}</p></article>''' for k, n, z, d in LUGARES)
CN = {'cafes': '42 lugares', 'restaurantes': '68 lugares', 'hoteles': '23 lugares', 'talleres': '15 esta semana', 'museos': '19 lugares', 'recorridos': '11 esta semana'}
cats = ''.join(f'''<a class="cat" href="#" style="--f:{CAT[k]['fondo']};--t:{CAT[k]['texto']}"><span class="ci">{ico[k]}</span><b>{CAT[k]['nombre']}</b><span>{n}</span></a>''' for k, n in CN.items())
html = f'''<title>Convia Inicio</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT,WONK@9..144,300..700,0..100,0..1&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* Página principal editorial en retícula de 12 columnas; orden del BrandScript (héroe → problema → guía → plan → llamado → éxito/fracaso → negocios).
   Identidad Convia v2 (convia-final/tokens.css). Tema claro por decisión de marca. */
:root{{--papel:{C['papel']};--sup:#fff;--tinta:{C['tinta']};--sec:{C['texto_sec']};--linea:{C['linea']};--cantera:{C['cantera']};--suave:{C['cantera_suave']};--arena:{C['arena']};
--display:"Fraunces",Georgia,"Times New Roman",serif;--dv:"SOFT" 100,"WONK" 0,"opsz" 96;--text:"Figtree",system-ui,-apple-system,"Segoe UI",sans-serif;--r:16px;--r-s:12px;color-scheme:light}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--papel);color:var(--tinta);font:400 16px/1.6 var(--text)}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
a{{color:inherit}}:focus-visible{{outline:2px solid var(--cantera);outline-offset:3px;border-radius:6px}}
.wrap{{max-width:1240px;margin:0 auto;padding-left:max(24px,env(safe-area-inset-left,0px));padding-right:max(24px,env(safe-area-inset-right,0px))}}
.d{{font-family:var(--display);font-weight:500;font-variation-settings:var(--dv);letter-spacing:-.01em}}
.proto{{background:var(--tinta);color:var(--papel);font-size:13px}}.proto .wrap{{padding-block:7px;display:flex;gap:12px;flex-wrap:wrap;justify-content:space-between}}
header.top{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:color-mix(in srgb,var(--papel) 92%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--linea)}}
header.top .wrap{{display:flex;align-items:center;gap:28px;padding-block:14px}}.logo{{height:34px;width:auto;display:block}}
nav.main ul{{list-style:none;display:flex;gap:22px;margin:0;padding:0;font-size:15px}}nav.main a{{text-decoration:none;color:var(--sec)}}nav.main a:hover{{color:var(--tinta)}}
.right{{margin-left:auto;display:flex;align-items:center;gap:16px;font-size:14px;color:var(--sec)}}.right b{{color:var(--tinta)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;font:600 15px var(--text);background:var(--cantera);color:#fff;border:0;border-radius:999px;padding:12px 22px;min-height:46px;text-decoration:none;cursor:pointer}}
.btn:hover{{filter:brightness(1.08)}}.btn.l{{background:transparent;color:var(--tinta);border:1px solid var(--tinta)}}
.hero .wrap{{display:grid;grid-template-columns:7fr 5fr;gap:48px;padding-block:72px 64px;align-items:end}}
.eyebrow{{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--cantera);font-weight:600;margin:0 0 16px}}
h1{{font-size:clamp(42px,6vw,78px);line-height:1.04;margin:0;text-wrap:balance}}
.lead{{font-size:19px;color:var(--sec);margin:22px 0 0;max-width:46ch}}
.search{{background:var(--sup);border:1px solid var(--linea);border-radius:var(--r);padding:22px;display:grid;gap:14px}}
.search label{{display:grid;gap:6px;font-size:13px;color:var(--sec);font-weight:500}}
.search select{{font:500 16px var(--text);color:var(--tinta);background:var(--papel);border:1px solid var(--linea);border-radius:var(--r-s);padding:12px;min-height:48px}}
.empatia .wrap{{padding-block:8px 56px}}.empatia blockquote{{margin:0;background:var(--suave);border-radius:var(--r);padding:28px 32px;display:grid;grid-template-columns:auto 1fr;gap:20px;align-items:center}}
.empatia .star{{width:48px;height:48px}}.empatia p{{margin:0;font-size:clamp(20px,2.4vw,26px);line-height:1.3}}.empatia small{{display:block;margin-top:6px;font:400 15px var(--text);color:var(--sec)}}
section.blk .wrap{{padding-block:48px;border-top:1px solid var(--linea)}}
.blk header{{display:flex;justify-content:space-between;align-items:baseline;gap:16px;margin-bottom:24px;flex-wrap:wrap}}
h2{{font-size:clamp(28px,3.4vw,38px);line-height:1.1;margin:0}}.blk header a{{font-size:15px;color:var(--sec)}}
.grid4{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px}}.grid3{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}}
.ph{{background:var(--arena);aspect-ratio:4/3;border-radius:var(--r);margin-bottom:14px}}.ph.tall{{aspect-ratio:5/4}}
.chip{{display:inline-flex;align-items:center;gap:6px;background:var(--f);color:var(--t);border-radius:999px;padding:4px 12px 4px 8px;font-size:12.5px;font-weight:600;margin-bottom:10px}}
.chip .ico{{width:18px;height:18px;color:var(--t)}}
article h3{{font:500 22px/1.2 var(--display);font-variation-settings:var(--dv);margin:0 0 8px}}article h3 a{{text-decoration:none}}article h3 a:hover{{text-decoration:underline}}
.meta{{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:14px;color:var(--sec);margin:0}}.price{{margin:8px 0 0;font-weight:600;font-variant-numeric:tabular-nums}}.desc{{margin:0;color:var(--sec);font-size:15px}}
.cats{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px}}
.cat{{text-decoration:none;background:var(--sup);border:1px solid var(--linea);border-radius:var(--r);padding:18px;display:grid;gap:4px;transition:border-color .15s}}.cat:hover{{border-color:var(--t)}}
.ci{{width:44px;height:44px;border-radius:50%;background:var(--f);display:grid;place-items:center;margin-bottom:8px}}.ci .ico{{width:26px;height:26px;color:var(--t)}}
.cat b{{font:500 19px/1.2 var(--display);font-variation-settings:var(--dv)}}.cat span:last-child{{font-size:13px;color:var(--sec)}}
.pasos{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;counter-reset:p;list-style:none;margin:0;padding:0}}
.pasos li{{background:var(--sup);border:1px solid var(--linea);border-radius:var(--r);padding:24px;display:grid;gap:8px;align-content:start}}
.pasos li::before{{counter-increment:p;content:counter(p);font:500 32px/1 var(--display);font-variation-settings:var(--dv);color:var(--cantera)}}
.pasos b{{font:500 21px var(--display);font-variation-settings:var(--dv)}}.pasos p{{margin:0;color:var(--sec)}}
.stakes .wrap{{padding-block:56px;border-top:1px solid var(--linea);display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}}
.stakes h2{{max-width:16ch;margin-bottom:14px}}.stakes p{{margin:0 0 18px;color:var(--sec);font-size:17px;max-width:48ch}}.ctas{{display:flex;gap:12px;flex-wrap:wrap}}
.news{{background:var(--sup);border:1px solid var(--linea);border-radius:var(--r);padding:24px;display:grid;gap:12px}}
.news label{{font-weight:600}}.news .row{{display:flex;gap:10px;flex-wrap:wrap}}.news input{{flex:1 1 220px;font:16px var(--text);border:1px solid var(--linea);border-radius:999px;padding:12px 16px;min-height:46px;background:var(--papel)}}
.news small{{color:var(--sec)}}.tag{{font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;background:var(--arena);border-radius:6px;padding:2px 6px;margin-left:6px;color:var(--sec)}}
.negocio .wrap{{padding-block:24px 64px}}.negocio .box{{background:var(--cantera);color:#fff;border-radius:24px;padding:40px;display:grid;grid-template-columns:auto 1fr auto;gap:32px;align-items:center}}
.sello{{width:132px;height:132px}}.negocio h2{{color:#fff}}.negocio p{{margin:8px 0 0;color:#e3ece6;max-width:52ch}}
.negocio .btn{{background:#fff;color:var(--cantera)}}.negocio .btn.l{{background:transparent;color:#fff;border-color:#fff}}.negocio .ctas{{flex-direction:column}}
footer .wrap{{padding-block:32px 48px;border-top:1px solid var(--linea);display:flex;gap:16px;flex-wrap:wrap;justify-content:space-between;font-size:14px;color:var(--sec)}}footer .logo{{height:26px}}
@media (max-width:1000px){{nav.main{{display:none}}.hero .wrap{{grid-template-columns:1fr;padding-block:48px}}.grid4{{grid-template-columns:repeat(2,minmax(0,1fr))}}.cats{{grid-template-columns:repeat(3,minmax(0,1fr))}}.stakes .wrap{{grid-template-columns:1fr}}.negocio .box{{grid-template-columns:1fr;justify-items:start}}.negocio .ctas{{flex-direction:row}}}}
@media (max-width:620px){{.grid3,.grid4,.pasos{{grid-template-columns:1fr}}.cats{{grid-template-columns:repeat(2,minmax(0,1fr))}}.right .lang{{display:none}}.right .btn{{padding:10px 16px;min-height:44px;font-size:14px}}.logo{{height:28px}}.empatia blockquote{{grid-template-columns:1fr;padding:24px}}.negocio .box{{padding:28px}}}}
</style>
<div class="proto" role="note"><div class="wrap"><span>Prototipo · negocios, cifras y planes de ejemplo (ficticios)</span><span>Convia · página principal r2</span></div></div>
<header class="top"><div class="wrap"><a href="#" aria-label="Convia, inicio">{logo}</a>
<nav class="main" aria-label="Principal"><ul><li><a href="#hoy">Hoy</a></li><li><a href="#tipos">Dónde comer</a></li><li><a href="#tipos">Dónde dormir</a></li><li><a href="#tipos">Qué hacer</a></li><li><a href="#tipos">Talleres</a></li></ul></nav>
<div class="right"><span class="lang"><b>ES</b> · EN</span><a class="btn" href="#hoy">Ver planes de hoy</a></div></div></header>
<main>
<section class="hero"><div class="wrap"><div><p class="eyebrow">Oaxaca · semana del 23 al 29</p><h1 class="d">Lo que vale la pena en Oaxaca, escogido por gente de aquí.</h1>
<p class="lead">Cafés, hoteles pequeños, talleres y planes para esta semana. Pocos lugares, bien escogidos, para que salgas de la rutina sin perder la tarde buscando.</p></div>
<form class="search" aria-label="Buscar un plan" onsubmit="event.preventDefault()">
<label for="q1">Busco<select id="q1"><option>Algo que hacer</option><option>Dónde comer</option><option>Dónde dormir</option><option>Un café</option></select></label>
<label for="q2">Cuándo<select id="q2"><option>Hoy</option><option>Este fin de semana</option><option>Otra fecha</option></select></label>
<label for="q3">Con quién<select id="q3"><option>Voy solo</option><option>En pareja</option><option>Con amigos</option><option>Con niños</option></select></label>
<button class="btn" type="submit">Ver planes</button></form></div></section>
<section class="empatia" aria-label="Por qué Convia"><div class="wrap"><blockquote><svg class="star" viewBox="0 0 200 200" aria-hidden="true"><path fill="{C['cantera']}" d="{re.search(r'd="([^"]+)"', open(os.path.join(F, 'svg', 'simbolo.svg')).read()).group(1)}"/></svg>
<p class="d">Sabemos lo que es abrir el mapa, ver cuarenta cafés y terminar en el de siempre.<small>Por eso cada lugar de Convia pasa una revisión antes de aparecer, y la hace gente que vive aquí.</small></p></blockquote></div></section>
<section class="blk" id="hoy"><div class="wrap"><header><h2 class="d">Esta semana</h2><a href="#">Ver todos los planes</a></header><div class="grid4">{planes}</div></div></section>
<section class="blk" id="tipos"><div class="wrap"><header><h2 class="d">Explora por tipo</h2></header><nav class="cats" aria-label="Categorías">{cats}</nav></div></section>
<section class="blk"><div class="wrap"><header><h2 class="d">Así de fácil</h2></header><ol class="pasos">
<li><b>Dinos qué buscas</b><p>Qué, cuándo y con quién. Sin registrarte.</p></li><li><b>Elige entre pocos</b><p>Solo lugares que pasaron nuestra revisión; nada de listas infinitas.</p></li><li><b>Ve</b><p>Horario, cómo llegar y contacto en la misma ficha.</p></li></ol></div></section>
<section class="blk"><div class="wrap"><header><h2 class="d">Recomendados</h2><a href="#">Ver el directorio</a></header><div class="grid3">{lugares}</div></div></section>
<section class="stakes"><div class="wrap"><div><h2 class="d">No pases otro fin de semana en el lugar de siempre.</h2><p>Cada semana hay talleres, cocinas y rincones nuevos en la ciudad. Convia te los pone enfrente.</p><div class="ctas"><a class="btn" href="#hoy">Ver planes de hoy</a></div></div>
<form class="news" onsubmit="event.preventDefault()" aria-label="Recibir los planes de la semana"><label for="mail">Recibe los planes de la semana <span class="tag">Propuesta</span></label>
<div class="row"><input id="mail" type="email" placeholder="tu@correo.com" autocomplete="email"><button class="btn l" type="submit">Suscribirme</button></div><small>Un correo los jueves. Te das de baja cuando quieras.</small></form></div></section>
<section class="negocio" aria-labelledby="neg"><div class="wrap"><div class="box">{sello}<div><h2 class="d" id="neg">¿Tienes un negocio en Oaxaca?</h2><p>Solicita aparecer en Convia. Revisamos cada lugar con nuestro manual de estándares; si pasa, recibes tu ficha y el distintivo «Recomendado en Convia».</p></div>
<div class="ctas"><a class="btn" href="#">Solicitar acceso</a><a class="btn l" href="#">Leer el manual de estándares</a></div></div></div></section>
</main>
<footer><div class="wrap">{logo.replace('class="logo"', 'class="logo"', 1)}<span>Lo que vale la pena en Oaxaca, escogido por gente de aquí.</span><span>Prototipo · datos ficticios</span></div></footer>'''
open(os.path.join(D, 'index.html'), 'w').write(html)
print('ok', len(html))
