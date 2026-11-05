# Directorio para pacientes · tipografía del logotipo del nombre nuevo · r01.
# Pedido (2026-11-05): «una propuesta con diferentes tipos de tipografías para evaluar la que mejor se pueda adaptar y funcione
# bien en web, impreso y papel». Nombre aún sin elegir: se prueban los 3 recomendados de ../directorio-nombre-r02/.
# Solo familias de Google Fonts (licencia libre, como decidió el manual). Mediciones en el navegador. Uso: python3 gen.py → tipografias.html
import os, base64, json
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
uri = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
PIN = uri('manik-final/svg/simbolo.svg'); PIN1 = uri('manik-final/svg/simbolo-1tinta.svg'); PINB = uri('manik-final/svg/simbolo-blanco.svg')
T = {x['name']: x['value'] for x in json.load(open(os.path.join(M, 'directorio-ds/project/tokens.json')))['color']['tokens']}
# (familia, pesos [raíz, manik], carácter)
F = [('Sora', 300, 600, 'La del logotipo vigente. Geométrica, ancha, terminales rectos.'),
     ('Urbanist', 300, 600, 'La letra de marca de toda la familia MedicalManik. Geométrica y ligera.'),
     ('Onest', 400, 600, 'La letra de interfaz del directorio. Neo-grotesca, abierta, hecha para pantalla.'),
     ('Plus Jakarta Sans', 400, 700, 'Humanista-geométrica, x alta, muy usada en salud digital.'),
     ('Outfit', 300, 600, 'Geométrica redondeada, amable; letras simples.'),
     ('Nunito', 400, 800, 'Terminales redondos: la más cálida; se ve infantil si se exagera.'),
     ('Lexend', 300, 600, 'Diseñada para lectura fácil: espaciado amplio y formas muy claras.'),
     ('Manrope', 400, 700, 'Técnica y nítida; x alta sin ser ancha.')]
fams = '&'.join('family=' + f.replace(' ', '+') + f':wght@{a};{b}' for f, a, b, _ in F)
NOMBRES = [('medi', 'MediManik'), ('doc', 'DocManik'), ('doctor', 'DoctorManik')]

cards = ''
for i, (f, a, b, car) in enumerate(F):
    st = f"font-family:'{f}',sans-serif"
    wm = lambda: f'<span class="wm" style="{st}"><span class="r" style="font-weight:{a}">medi</span><span style="font-weight:{b}">manik</span></span>'
    cards += f'''<article class="card" data-f="{f}" aria-labelledby="f{i}"><header class="ch"><h3 id="f{i}">{f}</h3><span class="nota">{car}</span></header>
 <div class="c1"><img src="{PIN}" alt="" class="p">{wm()}</div>
 <div class="row"><div class="web"><span class="tag">Web · barra de 64 px</span><span class="nav"><img src="{PIN}" alt="">{wm()}</span><span class="nav chico"><img src="{PIN}" alt="">{wm()}<small>12 px</small></span></div>
 <div class="imp"><span class="tag">Impreso · una tinta</span><span class="ink"><img src="{PIN1}" alt="">{wm()}</span><span class="rev"><img src="{PINB}" alt="">{wm()}</span></div></div>
 <div class="pap"><span class="tag">Papel · tinta corrida, 9 px ≈ 3 mm</span><span class="papel"><img src="{PIN1}" alt="">{wm()}</span><span class="papel g"><img src="{PIN1}" alt="">{wm()}</span></div>
 <dl class="med"><dt>Altura de x</dt><dd data-m="x">—</dd><dt>Ancho del nombre</dt><dd data-m="w">—</dd><dt>Lectura en chico</dt><dd data-m="ap">—</dd></dl></article>'''

HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tipografía del directorio</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{fams}&family=Onest:wght@400..700&display=swap" rel="stylesheet">
<style>
:root{{--bruma:{T["bruma"]};--blanco:{T["blanco"]};--tinta:{T["tinta"]};--muted:{T["muted"]};--linea:{T["linea"]};--cian-ui:{T["cian-ui"]};--luz-cian:{T["luz-cian"]};--luz-calida:{T["luz-calida"]};--azul:{T["azul-medicalmanik"]};color-scheme:light}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bruma);color:var(--tinta);font:400 16px/24px "Onest",system-ui,sans-serif;padding:0 16px}}
h1,h2,h3{{font-family:"Urbanist",sans-serif;margin:0}}h1{{font-weight:300;font-size:clamp(30px,5vw,44px);line-height:1.1;letter-spacing:-.02em}}h1 b{{font-weight:600}}h2{{font:600 24px/32px "Urbanist"}}h3{{font:600 18px/26px "Urbanist"}}p{{margin:0}}
.wrap{{max-width:1240px;margin:0 auto;padding:40px 0 80px;display:grid;gap:36px;grid-template-columns:minmax(0,1fr)}}
.cab{{display:grid;gap:12px;max-width:80ch;background:radial-gradient(ellipse 60% 90% at 0 0,var(--luz-cian),transparent 70%),radial-gradient(ellipse 50% 80% at 100% 0,var(--luz-calida),transparent 70%);border-radius:28px;padding:28px}}
.eti{{font:600 13px/18px "Onest";letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}}.nota{{font-size:14px;line-height:20px;color:var(--muted)}}
.ctl{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}.ctl b{{font-size:14px}}
.seg{{display:inline-flex;gap:2px;padding:3px;background:var(--blanco);border:1px solid var(--linea);border-radius:999px}}.seg button{{min-height:40px;padding:0 16px;border:0;border-radius:999px;background:transparent;font:600 14px/20px "Onest";color:var(--muted);cursor:pointer}}.seg button[aria-checked=true]{{background:var(--tinta);color:#fff}}
button:focus-visible{{outline:3px solid var(--cian-ui);outline-offset:2px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,560px),1fr));gap:16px}}
.card{{background:var(--blanco);border:1px solid var(--linea);border-radius:24px;padding:20px;display:grid;gap:14px;min-width:0}}.ch{{display:grid;gap:2px}}
.wm{{letter-spacing:-.03em;line-height:1;white-space:nowrap;color:var(--tinta)}}
.c1{{display:flex;align-items:center;justify-content:center;gap:12px;padding:28px 12px;border-radius:18px;background:var(--bruma);overflow:hidden}}.c1 .p{{height:58px}}.c1 .wm{{font-size:44px}}
.row{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.web,.imp,.pap{{display:grid;gap:10px;align-content:start;padding:14px;border:1px solid var(--linea);border-radius:16px;min-width:0;overflow:hidden}}
.tag{{font:600 12px/16px "Onest";color:var(--muted)}}
.nav{{display:flex;align-items:center;gap:8px;height:40px}}.nav img{{height:28px}}.nav .wm{{font-size:20px}}.nav.chico{{height:24px}}.nav.chico img{{height:16px}}.nav.chico .wm{{font-size:12px;letter-spacing:-.01em}}.nav small{{margin-left:auto;font-size:11px;color:var(--muted)}}
.ink,.rev{{display:flex;align-items:center;gap:8px;padding:10px;border-radius:10px}}.ink img,.rev img{{height:26px}}.ink .wm{{font-size:20px;color:#000}}.rev{{background:var(--tinta)}}.rev .wm{{font-size:20px;color:#fff}}
.pap{{background:#F4EFE4}}.papel{{display:flex;align-items:center;gap:4px;filter:url(#corrida)}}.papel img{{height:12px}}.papel .wm{{font-size:9px;letter-spacing:0;color:#1d1d1d}}.papel.g img{{height:20px}}.papel.g .wm{{font-size:15px;letter-spacing:-.01em}}
.med{{display:grid;grid-template-columns:repeat(3,auto 1fr);gap:4px 10px;margin:0;font-size:14px}}.med dt{{color:var(--muted)}}.med dd{{margin:0;font-weight:600;font-variant-numeric:tabular-nums}}
table{{border-collapse:collapse;width:100%;background:var(--blanco)}}th,td{{text-align:left;padding:10px 14px;border-bottom:1px solid var(--linea);font-size:15px;line-height:22px}}th{{color:var(--muted);font-size:14px}}.tw{{overflow-x:auto;border:1px solid var(--linea);border-radius:16px}}
.reco{{background:var(--blanco);border:1px solid var(--linea);border-radius:24px;padding:24px;display:grid;gap:12px;max-width:90ch}}ol{{margin:0;padding-left:24px;display:grid;gap:8px}}
@media (max-width:640px){{.row{{grid-template-columns:1fr}}.c1 .wm{{font-size:30px}}.c1 .p{{height:40px}}.med{{grid-template-columns:auto 1fr}}}}
</style></head><body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><filter id="corrida"><feMorphology operator="dilate" radius="0.35"/><feGaussianBlur stdDeviation="0.35"/></filter></svg>
<main class="wrap">
<header class="cab"><span class="eti">Directorio para pacientes · tipografía del logotipo · ronda 1</span>
<h1>Ocho letras para el <b>nombre nuevo</b>, probadas en pantalla, impreso y papel</h1>
<p>Cada tipografía pasa por las mismas pruebas: logotipo grande, barra de la app (20 px y 12 px), impreso a una tinta y en negativo, y papel con tinta corrida a 9 px (unos 3 mm, como en una receta o una tarjeta). Todas son de Google Fonts: libres para web, impresos y apps, como decidió el manual.</p>
<p class="nota">El logotipo final se convierte a trazos y se ajusta a mano (espaciado, la unión de las letras). Aquí se elige la familia, no el dibujo final.</p></header>
<div class="ctl"><b id="ln">Nombre</b><div class="seg" role="radiogroup" aria-labelledby="ln">{"".join(f'<button type="button" role="radio" data-n="{k}" aria-checked="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{n}</button>' for i, (k, n) in enumerate(NOMBRES))}</div>
<b id="lp">Pesos</b><div class="seg" role="radiogroup" aria-labelledby="lp"><button type="button" role="radio" data-p="dos" aria-checked="true">Raíz ligera + manik</button><button type="button" role="radio" data-p="uno" aria-checked="false" tabindex="-1">Todo en un peso</button></div></div>
<section aria-labelledby="s1"><h2 id="s1">Las ocho</h2><div class="grid">{cards}</div></section>
<section aria-labelledby="s2"><h2 id="s2">Comparación medida</h2><p class="nota">Altura de x: qué tan grandes se ven las minúsculas para un mismo tamaño (más alta = se lee mejor en chico). Ancho: cuánto ocupa el nombre en ems (menos = cabe mejor en tarjetas y pantallas angostas). Se recalcula al cambiar de nombre.</p>
<div class="tw" tabindex="0" role="region" aria-label="Comparación medida"><table><thead><tr><th scope="col">Familia</th><th scope="col">Altura de x</th><th scope="col">Ancho del nombre</th><th scope="col">Carácter</th></tr></thead><tbody id="tb"></tbody></table></div></section>
<section class="reco" aria-labelledby="s3"><h2 id="s3">Cómo elegir</h2><ol>
<li><b>Papel manda:</b> si a 9 px con tinta corrida se confunden «m», «n» y «a», se descarta, aunque se vea bien en pantalla.</li>
<li><b>Tiene que convivir con el pin:</b> el símbolo es geométrico, de esquinas redondeadas; una letra muy humanista o muy redonda lo contradice.</li>
<li><b>Debe ser pariente de Urbanist y Onest</b> (la marca y la interfaz del directorio), sin ser idéntica a una de ellas si se quiere que el logotipo sea propio.</li>
<li><b>Ancho:</b> DoctorManik es largo; si se elige ese nombre, pesa más una familia estrecha.</li></ol>
<h3>Lectura de esta ronda [inferencia]</h3><ol>
<li><b>Sora</b> es la candidata más fuerte: comparte con Plus Jakarta Sans la altura de x más alta (55 %), ya es la letra del logotipo vigente y su geometría es la del pin. Su costo: es la más ancha.</li>
<li><b>Manrope</b> es la alternativa si se quiere un nombre más compacto sin perder lectura en chico (x 54 %).</li>
<li><b>Hallazgo para cualquier familia:</b> la raíz en peso 300 se debilita en papel a 9 px. En impresos pequeños (menos de unos 4 mm de alto) la raíz sube a 400, o todo el nombre va en un solo peso.</li>
<li>Urbanist y Onest funcionan, pero son las letras de marca e interfaz: el logotipo se confundiría con el texto que lo rodea.</li></ol>
<p id="lectura" class="nota"></p></section>
</main>
<script>
const NOM={{medi:['medi','manik'],doc:['doc','manik'],doctor:['doctor','manik']}};const W={json.dumps({f: [a, b] for f, a, b, _ in F})};const CAR={json.dumps({f: c for f, _, _, c in F}, ensure_ascii=False)};
let n='medi',p='dos';
function aplicar(){{document.querySelectorAll('.card').forEach(c=>{{const f=c.dataset.f;c.querySelectorAll('.wm').forEach(w=>{{const [r,m]=w.children;r.textContent=NOM[n][0];m.textContent=NOM[n][1];r.style.fontWeight=p==='dos'?W[f][0]:W[f][1]}})}});medir()}}
function medir(){{const cv=document.createElement('canvas').getContext('2d');const filas=[];
 document.querySelectorAll('.card').forEach(c=>{{const f=c.dataset.f;cv.font=`${{W[f][1]}} 100px '${{f}}'`;const x=cv.measureText('x').actualBoundingBoxAscent/100;
  cv.font=`${{p==='dos'?W[f][0]:W[f][1]}} 100px '${{f}}'`;let w=cv.measureText(NOM[n][0]).width;cv.font=`${{W[f][1]}} 100px '${{f}}'`;w=(w+cv.measureText(NOM[n][1]).width)/100*0.97;
  c.querySelector('[data-m=x]').textContent=Math.round(x*100)+' %';c.querySelector('[data-m=w]').textContent=w.toFixed(2)+' em';
  const ap=x>=.54?'muy buena':x>=.5?'buena':'justa';c.querySelector('[data-m=ap]').textContent=ap;filas.push([f,x,w])}});
 const xs=filas.map(r=>r[1]),ws=filas.map(r=>r[2]);document.getElementById('tb').innerHTML=filas.map(([f,x,w])=>`<tr><td>${{f}}</td><td>${{Math.round(x*100)}} %${{x===Math.max(...xs)?' · la más alta':''}}</td><td>${{w.toFixed(2)}} em${{w===Math.min(...ws)?' · la más estrecha':w===Math.max(...ws)?' · la más ancha':''}}</td><td class="nota">${{CAR[f]}}</td></tr>`).join('');
 document.getElementById('lectura').textContent='Medido en este navegador con las fuentes ya cargadas; la altura de x es la de la letra «x» del peso fuerte.'}}
document.querySelectorAll('[role=radiogroup]').forEach(g=>{{const bs=[...g.querySelectorAll('[role=radio]')];const pick=b=>{{bs.forEach(x=>{{x.setAttribute('aria-checked',x===b);x.tabIndex=x===b?0:-1}});if(b.dataset.n)n=b.dataset.n;if(b.dataset.p)p=b.dataset.p;aplicar()}};
 bs.forEach((b,i)=>{{b.addEventListener('click',()=>pick(b));b.addEventListener('keydown',e=>{{const d={{ArrowRight:1,ArrowLeft:-1}}[e.key];if(d){{e.preventDefault();const k=bs[(i+d+bs.length)%bs.length];pick(k);k.focus()}}}})}})}});
document.fonts.ready.then(aplicar);
</script></body></html>'''
open(os.path.join(D, 'tipografias.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
