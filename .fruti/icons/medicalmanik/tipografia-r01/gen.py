# MedicalManik · tipografía · ronda 1 (usuario, 2026-11-09): sustitutos de Google Fonts para la tipografía de marca
# Filson Pro (títulos, subtítulos y CTA) y Scandia (párrafos e información secundaria). python3 gen.py -> comparacion.html
# Referencia real: la palabra «MedicalManik» del logotipo está trazada en Filson Pro (../final/svg/medicalmanik-palabra.svg).
import os
D = os.path.dirname(os.path.abspath(__file__))
PAL = open(os.path.join(D, '..', 'final', 'svg', 'medicalmanik-palabra.svg')).read().replace('<svg ', '<svg class="ref" ')
AZUL, TINTA, SUB = '#234899', '#16233F', '#566078'
FIL = [('Figtree','Figtree:wght@400;700',700,'Geométrica amable de trazo parejo; la «a» de dos pisos y las curvas abiertas son las más cercanas a Filson.'),
       ('Outfit','Outfit:wght@400;700',700,'Geométrica pura, más redonda; la «a» de un piso la aleja de Filson, pero conserva la calidez.'),
       ('Plus Jakarta Sans','Plus+Jakarta+Sans:wght@400;700',700,'Geométrica moderna y un poco más estrecha; muy usada en producto digital.'),
       ('Lexend','Lexend:wght@400;700',700,'Ancha y muy legible, hecha para lectura fácil; la más redonda de lectura.'),
       ('Urbanist','Urbanist:wght@400;700',700,'La actual del ecosistema, como referencia: más geométrica y fría que Filson.')]
SCA = [('Albert Sans','Albert+Sans:wght@400;600','Grotesca de inspiración escandinava, como Scandia: limpia, con terminales rectos.'),
       ('DM Sans','DM+Sans:opsz,wght@9..40,400;9..40,600','Geométrica baja en contraste, muy pareja en texto chico.'),
       ('Hanken Grotesk','Hanken+Grotesk:wght@400;600','Grotesca neutra y abierta; cifras claras para tablas.'),
       ('Manrope','Manrope:wght@400;600','Semi-geométrica con aire técnico; buena en interfaz densa.'),
       ('Atkinson Hyperlegible Next','Atkinson+Hyperlegible+Next:wght@400;600','La actual de las apps, como referencia: distingue I l 1 y 0 O en dosis y folios.')]
fuentes = '&'.join('family=' + g for _, g, *_ in FIL + SCA)
def fila_fil(n, g, w, d):
    F = f"font-family:'{n}',sans-serif"
    return f'''<article class="c"><header><h3>{n}</h3><p>{d}</p></header>
<div class="cmp"><div class="lado"><small>Filson Pro (logotipo real)</small>{PAL}</div><div class="lado"><small>{n} {w}</small><span class="wm" style="{F};font-weight:{w}">MedicalManik</span></div></div>
<div class="muestra"><b style="{F};font-weight:{w}">Expediente de Mariana Ruiz</b><span style="{F};font-weight:400">Signos vitales · Consulta del 9 de noviembre</span><button type="button" style="{F};font-weight:{w}">Agendar cita</button></div></article>'''
def fila_sca(n, g, d):
    F = f"font-family:'{n}',sans-serif"
    return f'''<article class="c"><header><h3>{n}</h3><p>{d}</p></header>
<div class="muestra2" style="{F}"><p>La receta se envía al correo del paciente y queda guardada en su expediente. Puedes reimprimirla desde Documentos en cualquier momento.</p>
<p class="dato"><b style="font-weight:600">Paracetamol 500 mg</b> · 1 tableta cada 8 h · Lote I1l-0O8 · Folio 0010 · Cédula 1023 4567</p><p class="sec">Última actualización: hoy, 10:42 · Dra. Ramírez</p></div></article>'''
HTML = f'''<title>MedicalManik · Tipografía r1</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fuentes}&display=swap">
<style>
/* Dos bandas: candidatas a Filson Pro (comparadas contra el logotipo real) y candidatas a Scandia (párrafo y datos clínicos) */
:root{{--bg:#f3f5f9;--fg:{TINTA};--muted:{SUB};--line:#dde2ec;--card:#fff;--azul:{AZUL};--ui:'Atkinson Hyperlegible Next',ui-sans-serif,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0f1524;--fg:#e8ecf5;--muted:#a3adc4;--line:#26304a;--card:#161e33;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0f1524;--fg:#e8ecf5;--muted:#a3adc4;--line:#26304a;--card:#161e33;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--ui);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1180px;margin:0 auto;display:grid;gap:30px}} h1{{font:700 clamp(30px,5vw,48px)/1.05 'Figtree',sans-serif;margin:0;text-wrap:balance}} h2{{font:700 26px/1.15 'Figtree',sans-serif;margin:0}}
.intro{{display:grid;gap:12px;max-width:72ch}} .intro p,.sec>p{{margin:0;color:var(--muted)}} .ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.sec{{display:grid;gap:14px}} .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:14px}}
.c{{display:grid;gap:12px;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;align-content:start;min-width:0}} .c header{{display:grid;gap:2px}} .c h3{{margin:0;font-size:20px}} .c header p{{margin:0;font-size:14px;color:var(--muted)}}
.cmp{{display:grid;gap:10px;padding:14px;border-radius:12px;background:#fff;border:1px solid var(--line);color:{AZUL}}} .lado{{display:grid;gap:2px}} .lado small{{font-size:12px;color:{SUB}}}
.ref{{height:30px;width:auto;max-width:100%;color:{AZUL}}} .wm{{font-size:34px;line-height:1;letter-spacing:-.005em}}
.muestra{{display:grid;gap:6px;justify-items:start;padding:14px;border-radius:12px;background:#fff;border:1px solid var(--line);color:{TINTA}}} .muestra b{{font-size:22px;line-height:1.2}} .muestra span{{color:{SUB};font-size:15px}}
.muestra button{{margin-top:6px;border:0;border-radius:999px;background:{AZUL};color:#fff;font-size:16px;padding:10px 22px;cursor:pointer}} .muestra button:focus-visible{{outline:3px solid {AZUL};outline-offset:2px}}
.muestra2{{display:grid;gap:8px;padding:14px;border-radius:12px;background:#fff;border:1px solid var(--line);color:{TINTA}}} .muestra2 p{{margin:0;font-size:16px;line-height:1.55}} .dato{{font-variant-numeric:tabular-nums;font-size:15px!important}} .sec2,.muestra2 .sec{{color:{SUB};font-size:14px!important}}
.nota{{padding:16px 18px;border-radius:14px;background:var(--card);border:1px solid var(--line);max-width:80ch}} .nota p{{margin:0 0 6px}}
</style>
<div class="w"><div class="intro"><p class="ojo">MedicalManik · tipografía · ronda 1</p><h1>Parecidas a Filson Pro y Scandia, en Google Fonts</h1>
<p>Filson Pro y Scandia son de pago. Estas son las alternativas libres más cercanas a cada una. Las candidatas a Filson se comparan contra la palabra MedicalManik del logotipo, que está trazada en Filson Pro real. Las candidatas a Scandia se prueban en un párrafo y en una línea de receta, donde importa distinguir I, l, 1, 0 y O.</p></div>
<section class="nota"><p><b>Antes de decidir:</b> el 5 de noviembre se acordó una sola pareja para toda la marca, Urbanist y Atkinson Hyperlegible, y retirar Scandia. Este cambio la reemplaza.</p><p>Atkinson está en las apps por una razón clínica: distingue dosis, folios y cédulas sin confusión. Por eso cada candidata a Scandia trae la misma línea de receta, para que veas si mantiene esa claridad.</p></section>
<section class="sec"><h2>Títulos, subtítulos y botones (en lugar de Filson Pro)</h2><div class="grid">{''.join(fila_fil(*f) for f in FIL)}</div></section>
<section class="sec"><h2>Párrafos e información secundaria (en lugar de Scandia)</h2><div class="grid">{''.join(fila_sca(*s) for s in SCA)}</div></section></div>'''
open(os.path.join(D,'comparacion.html'),'w').write(HTML); print('ok')
