# Convia · página principal r3: identidad propia en la estructura (no solo en los adornos).
# Ideas: buscador como frase («Hoy voy … y busco …»), la semana como recorrido dibujado a mano (la «vía» del nombre),
# categorías como sellos estampados, notas a mano del «amigo que sabe». Uso: python3 gen.py. Datos ficticios.
import os, re, json, math, random
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
T = json.load(open(os.path.join(F, 'tema.json'))); C = T['color']; CAT = T['categorias']
STAR = re.search(r'd="([^"]+)"', open(os.path.join(F, 'svg', 'simbolo.svg')).read()).group(1)
def svgin(path, cls='', keep_label=False):
    s = open(os.path.join(F, path)).read()
    s = s.replace('<svg ', f'<svg class="{cls}" ' + ('' if keep_label else 'aria-hidden="true" '), 1)
    if not keep_label: s = re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
    return s
logo = svgin('svg/logotipo.svg', 'logo', True)
ico = {k: svgin(f'iconos/{k}.svg', 'ico') for k in CAT}
star = lambda fill, cls='st': f'<svg class="{cls}" viewBox="0 0 200 200" aria-hidden="true"><path fill="{fill}" d="{STAR}"/></svg>'
def hand(w, h, seed, kind='under'):
    # trazo a mano (subrayado o círculo) con la misma mano que la estrella
    r = random.Random(seed)
    if kind == 'under':
        pts = [(4 + i * (w - 8) / 8, h * .55 + r.uniform(-2.2, 2.2) + (i / 8) * -2) for i in range(9)]
    else:
        pts = [(w / 2 + (w / 2 - 6) * math.cos(t) * (1 + r.uniform(-.04, .04)), h / 2 + (h / 2 - 6) * math.sin(t) * (1 + r.uniform(-.06, .06)))
               for t in [math.radians(-100 + i * 380 / 18) for i in range(19)]]
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
    return f'<svg class="hand {kind}" viewBox="0 0 {w} {h}" preserveAspectRatio="none" aria-hidden="true"><path d="{d}" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def seg(seed, side):
    # tramo del recorrido entre paradas: baja ondulando hacia el lado del siguiente plan
    r = random.Random(seed); x0, x1 = 50, 50; bulge = 34 if side == 'r' else -34
    pts = [(x0 + bulge * math.sin(math.pi * t) + r.uniform(-1.5, 1.5), t * 100) for t in [i / 10 for i in range(11)]]
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
    return f'<svg class="seg" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><path d="{d}" fill="none" stroke="{C["cantera"]}" stroke-width="3" stroke-linecap="round" stroke-dasharray="1 9" vector-effect="non-scaling-stroke"/></svg>'
PARADAS = [('Vie 25', '19:00', 'museos', 'Noche de grabado en la galería', 'Con amigos · Entrada libre', 'Llega temprano: a las 20:00 ya no cabe nadie.'),
           ('Sáb 26', '11:00', 'talleres', 'Barro bruñido para principiantes', 'Para ir solo · $650', 'Grupo de seis; nadie llega sabiendo.'),
           ('Sáb 26', '20:00', 'restaurantes', 'Menú de temporada a seis tiempos', 'En pareja · $1,200', 'Pide la mesa del patio.'),
           ('Dom 27', '7:00', 'recorridos', 'Caminata de cantera al amanecer', 'Grupo pequeño · $300', 'La luz sobre la cantera verde vale la desvelada.')]
via = ''
for i, (dia, hora, k, t, m, nota) in enumerate(PARADAS):
    c = CAT[k]; side = 'l' if i % 2 == 0 else 'r'
    card = f'''<article class="stop" style="--f:{c['fondo']};--t:{c['texto']};--p:{c['punto']}"><p class="when"><b>{dia}</b> · {hora}</p>
<span class="chip">{ico[k]}{c['nombre']}</span><h3><a href="#">{t}</a></h3><p class="meta">{m}</p><p class="nota">{nota}</p></article>'''
    via += f'''<li class="row {side}"><div class="cell a">{card if side == 'l' else ''}</div><div class="cell mid">{seg(10 + i, 'r' if side == 'l' else 'l')}<span class="pin" style="--p:{c['punto']}">{star(c['punto'], 'pin-st')}</span></div><div class="cell b">{card if side == 'r' else ''}</div></li>'''
sellos = ''.join(f'''<a class="sello-a" href="#" style="--rot:{rot}deg" aria-label="{CAT[k]['nombre']}">{svgin(f'sellos/{k}-sello.svg', 'sello')}<span>{n}</span></a>'''
                 for (k, n), rot in zip([('cafes', '42 lugares'), ('restaurantes', '68 lugares'), ('hoteles', '23 lugares'), ('talleres', '15 esta semana'), ('museos', '19 lugares'), ('recorridos', '11 esta semana')], [-6, 4, -3, 6, -5, 3]))
LUG = [('cafes', 'Café Tres Patios', 'Jalatlaco', 'Café de olla y pan de la casa en un patio con sombra. Ve entre semana, temprano.'),
       ('hoteles', 'Hotel Patio de Luz', 'Centro', 'Nueve habitaciones alrededor de un patio de cantera. Pide la del segundo piso.'),
       ('restaurantes', 'Cocina Siete Fuegos', 'Xochimilco', 'Menú corto que cambia cada semana. Reserva el jueves para el sábado.')]
lista = ''.join(f'''<li style="--f:{CAT[k]['fondo']};--t:{CAT[k]['texto']}"><span class="num d">{i + 1:02d}</span><div class="ph" aria-hidden="true"></div>
<div><span class="chip">{ico[k]}{CAT[k]['nombre']} · {z}</span><h3><a href="#">{n}</a></h3><p>{d}</p></div>
<span class="stamp">{svgin('sellos/' + k + '-sello-solido.svg', 'mini')}</span></li>''' for i, (k, n, z, d) in enumerate(LUG))
html = f'''<title>Convia Inicio</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..700,0..100,0..1;1,9..144,300..700,0..100,0..1&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* Convia r3: la estructura cuenta la marca. Portada-frase; la semana como recorrido (vía) con paradas-estrella;
   categorías como sellos; notas a mano del «amigo que sabe». Identidad v2 (convia-final/tokens.css). Tema claro por decisión de marca. */
:root{{--papel:{C['papel']};--sup:#fff;--tinta:{C['tinta']};--sec:{C['texto_sec']};--linea:{C['linea']};--cantera:{C['cantera']};--suave:{C['cantera_suave']};--arena:{C['arena']};
--display:"Fraunces",Georgia,"Times New Roman",serif;--dv:"SOFT" 100,"WONK" 0,"opsz" 96;--text:"Figtree",system-ui,-apple-system,"Segoe UI",sans-serif;--r:16px;color-scheme:light}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--papel);color:var(--tinta);font:400 16px/1.6 var(--text)}}
a{{color:inherit}}:focus-visible{{outline:2px solid var(--cantera);outline-offset:3px;border-radius:6px}}
@media (prefers-reduced-motion:no-preference){{.sello-a{{transition:transform .25s}}.sello-a:hover{{transform:rotate(0deg) scale(1.05)}}}}
.wrap{{max-width:1180px;margin:0 auto;padding-left:max(24px,env(safe-area-inset-left,0px));padding-right:max(24px,env(safe-area-inset-right,0px))}}
.d{{font-family:var(--display);font-weight:500;font-variation-settings:var(--dv);letter-spacing:-.015em}}
.proto{{background:var(--tinta);color:var(--papel);font-size:13px}}.proto .wrap{{padding-block:6px}}
header.top .wrap{{display:flex;align-items:center;gap:28px;padding-block:18px}}.logo{{height:34px;width:auto;display:block}}
nav.main ul{{list-style:none;display:flex;gap:22px;margin:0;padding:0;font-size:15px}}nav.main a{{text-decoration:none;color:var(--sec)}}nav.main a:hover{{color:var(--tinta)}}
.lang{{margin-left:auto;font-size:14px;color:var(--sec)}}.lang b{{color:var(--tinta)}}
.btn{{display:inline-flex;align-items:center;gap:8px;font:600 15px var(--text);background:var(--cantera);color:#fff;border:0;border-radius:999px;padding:13px 24px;min-height:48px;text-decoration:none;cursor:pointer}}
.btn.l{{background:transparent;color:var(--tinta);border:1px solid var(--tinta)}}
/* portada */
.hero .wrap{{padding-block:56px 40px;position:relative}}
.hero h1{{font-size:clamp(46px,8vw,112px);line-height:.98;margin:0;max-width:11ch;position:relative}}
.hero h1 .u{{position:relative;display:inline-block}}.hand{{position:absolute;color:var(--cantera);pointer-events:none}}.hand.under{{left:-2%;bottom:-.08em;width:104%;height:.28em}}
.hero .big-star{{position:absolute;right:max(24px,6%);top:40px;width:clamp(120px,20vw,260px);transform:rotate(12deg)}}.big-star path{{fill:var(--cantera)}}
.frase{{margin-top:44px;font-size:clamp(22px,2.6vw,32px);line-height:1.6;max-width:30ch}}
.frase select{{font:inherit;font-family:var(--display);font-variation-settings:var(--dv);font-weight:500;color:var(--cantera);background:transparent;border:0;border-bottom:2px dashed var(--cantera);padding:0 .1em;appearance:none;-webkit-appearance:none;cursor:pointer;border-radius:0;field-sizing:content;max-width:100%}}
.frase .go{{margin-top:22px;display:flex;gap:16px;align-items:center;flex-wrap:wrap;font:400 15px var(--text);color:var(--sec)}}
/* recorrido */
section.blk .wrap{{padding-block:56px}}.blk h2{{font-size:clamp(32px,4vw,48px);line-height:1.05;margin:0}}.blk .sub{{margin:8px 0 0;color:var(--sec);max-width:52ch}}
.via{{list-style:none;margin:36px 0 0;padding:0}}.row{{display:grid;grid-template-columns:1fr 120px 1fr;min-height:200px}}
.cell.mid{{position:relative}}.seg{{position:absolute;inset:0;width:100%;height:100%}}
.pin{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:58px;height:58px;background:var(--papel);border-radius:50%;display:grid;place-items:center}}.pin-st{{width:46px;height:46px}}
.cell.a{{display:flex;justify-content:flex-end;align-items:center}}.cell.b{{display:flex;align-items:center}}
.stop{{max-width:400px;padding:8px 4px}}.when{{margin:0 0 6px;font-size:14px;color:var(--sec);font-variant-numeric:tabular-nums}}.when b{{color:var(--tinta)}}
.chip{{display:inline-flex;align-items:center;gap:6px;background:var(--f);color:var(--t);border-radius:999px;padding:4px 12px 4px 8px;font-size:12.5px;font-weight:600}}.chip .ico{{width:18px;height:18px;color:var(--t)}}
.stop h3{{font:500 26px/1.15 var(--display);font-variation-settings:var(--dv);margin:10px 0 4px}}.stop h3 a,.lista h3 a{{text-decoration:none}}.stop h3 a:hover,.lista h3 a:hover{{text-decoration:underline}}
.meta{{margin:0;color:var(--sec);font-size:15px;font-variant-numeric:tabular-nums}}
.nota{{margin:10px 0 0;font:italic 500 18px/1.35 var(--display);font-variation-settings:"SOFT" 100,"opsz" 36;color:var(--cantera);position:relative;padding-left:22px}}
.nota::before{{content:"";position:absolute;left:0;top:.55em;width:14px;height:2px;background:currentColor;border-radius:2px}}
/* sellos */
.sellos{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:20px;margin-top:32px}}
.sello-a{{text-decoration:none;display:grid;justify-items:center;gap:10px;transform:rotate(var(--rot))}}.sello{{width:100%;max-width:170px;height:auto}}.sello-a span{{font-size:14px;color:var(--sec)}}
/* lista editorial */
.lista{{list-style:none;margin:28px 0 0;padding:0;border-top:1px solid var(--linea)}}
.lista li{{display:grid;grid-template-columns:70px 180px 1fr 90px;gap:24px;align-items:center;padding-block:22px;border-bottom:1px solid var(--linea)}}
.num{{font-size:40px;color:var(--cantera)}}.lista .ph{{aspect-ratio:4/3;border-radius:var(--r);background:var(--arena)}}
.lista h3{{font:500 26px/1.15 var(--display);font-variation-settings:var(--dv);margin:8px 0 4px}}.lista p{{margin:0;color:var(--sec);max-width:56ch}}.mini{{width:84px;height:84px;transform:rotate(-8deg)}}
/* negocios */
.negocio .wrap{{padding-block:24px 72px}}.negocio .box{{border:2px dashed var(--cantera);border-radius:28px;padding:40px;display:grid;grid-template-columns:1fr auto;gap:32px;align-items:center;position:relative}}
.negocio h2{{font-size:clamp(28px,3.4vw,40px)}}.negocio p{{margin:10px 0 0;color:var(--sec);max-width:56ch}}.negocio .ctas{{display:flex;gap:12px;flex-wrap:wrap;margin-top:22px}}
.negocio .calca{{width:150px;height:150px;transform:rotate(8deg)}}
footer .wrap{{padding-block:28px 44px;border-top:1px solid var(--linea);display:flex;gap:16px;flex-wrap:wrap;justify-content:space-between;align-items:center;font-size:14px;color:var(--sec)}}footer .logo{{height:26px}}
@media (max-width:980px){{nav.main{{display:none}}.sellos{{grid-template-columns:repeat(3,minmax(0,1fr))}}.lista li{{grid-template-columns:50px 140px 1fr}}.lista .stamp{{display:none}}}}
@media (max-width:680px){{.hero .big-star{{width:96px;top:24px;right:16px}}.hero h1{{max-width:9ch}}
.row{{grid-template-columns:56px 1fr;min-height:0}}.row .cell.mid{{grid-column:1;grid-row:1}}
.row .cell.a,.row .cell.b{{grid-column:2;grid-row:1;padding-block:18px;display:block}}.row.r .cell.a,.row.l .cell.b{{display:none}}.pin{{width:44px;height:44px}}.pin-st{{width:34px;height:34px}}
.lista li{{grid-template-columns:1fr;gap:10px}}.lista .num{{font-size:28px}}.sellos{{grid-template-columns:repeat(2,minmax(0,1fr))}}.negocio .box{{grid-template-columns:1fr;padding:26px}}.negocio .calca{{width:110px;height:110px}}}}
</style>
<div class="proto" role="note"><div class="wrap">Prototipo r3 · negocios, planes y cifras de ejemplo (ficticios)</div></div>
<header class="top"><div class="wrap"><a href="#" aria-label="Convia, inicio">{logo}</a>
<nav class="main" aria-label="Principal"><ul><li><a href="#via">Esta semana</a></li><li><a href="#sellos">Dónde comer</a></li><li><a href="#sellos">Dónde dormir</a></li><li><a href="#sellos">Qué hacer</a></li></ul></nav>
<p class="lang"><b>ES</b> · EN</p></div></header>
<main>
<section class="hero"><div class="wrap">{star(C['cantera'], 'big-star')}
<h1 class="d">Lo que vale la pena, escogido por gente de <span class="u">aquí.{hand(300, 30, 3)}</span></h1>
<form class="frase d" onsubmit="event.preventDefault()" aria-label="Arma tu plan">
<label for="f1">Hoy voy</label> <select id="f1"><option>solo</option><option>en pareja</option><option>con amigos</option><option>con niños</option></select>
<label for="f2">y busco</label> <select id="f2"><option>un taller</option><option>dónde comer</option><option>un café tranquilo</option><option>dónde dormir</option><option>algo que hacer</option></select>
<label for="f3">cerca de</label> <select id="f3"><option>el Centro</option><option>Jalatlaco</option><option>Xochimilco</option><option>Reforma</option></select>.
<div class="go"><button class="btn" type="submit">Ver mis planes</button><span>O mira el recorrido de esta semana ↓</span></div></form></div></section>
<section class="blk" id="via"><div class="wrap"><h2 class="d">El recorrido de esta semana</h2><p class="sub">Cuatro paradas que recomendaríamos a un amigo, del viernes al domingo. Las notas son nuestras.</p>
<ol class="via">{via}</ol></div></section>
<section class="blk" id="sellos"><div class="wrap"><h2 class="d">Elige por tipo</h2><p class="sub">Cada sello es una selección hecha a mano. Ningún lugar entra sin pasar la revisión.</p><nav class="sellos" aria-label="Categorías">{sellos}</nav></div></section>
<section class="blk"><div class="wrap"><h2 class="d">Recomendados esta semana</h2><ol class="lista">{lista}</ol></div></section>
<section class="negocio" aria-labelledby="neg"><div class="wrap"><div class="box"><div><h2 class="d" id="neg">¿Tu negocio vale la pena? Gánate el sello.</h2>
<p>Solicita aparecer en Convia. Revisamos cada lugar con nuestro manual de estándares; si pasa, recibes tu ficha y la calca «Recomendado en Convia · 2027» para tu ventana.</p>
<div class="ctas"><a class="btn" href="#">Solicitar acceso</a><a class="btn l" href="#">Leer el manual de estándares</a></div></div>{svgin('distintivo/calca-cafes.svg', 'calca')}</div></div></section>
</main>
<footer><div class="wrap">{logo}<span>Lo que vale la pena en Oaxaca, escogido por gente de aquí.</span><span>Prototipo · datos ficticios</span></div></footer>'''
html = re.sub(r'width="100mm" height="100mm" ', '', html)
open(os.path.join(D, 'index.html'), 'w').write(html)
print('ok', len(html))
