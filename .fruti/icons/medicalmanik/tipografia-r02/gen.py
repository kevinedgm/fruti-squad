# MedicalManik · tipografía · ronda 2 (usuario: «las a deben ser de la misma forma»). python3 gen.py -> comparacion.html
# Hecho: la «a» de Filson Pro en el logotipo es de un piso (cuenco redondo y asta recta). Solo pasan las fuentes con esa «a»,
# en títulos y en texto. Revisado a 64 px: de un piso Outfit, Urbanist, League Spartan, Poppins, Questrial, Didact Gothic, Quicksand y Lexend;
# de dos pisos Figtree, Plus Jakarta Sans, Jost, Hanken Grotesk, Manrope, Sora, Onest y Atkinson (por eso salen de la propuesta).
import os
D = os.path.dirname(os.path.abspath(__file__))
PAL = open(os.path.join(D, '..', 'final', 'svg', 'medicalmanik-palabra.svg')).read().replace('<svg ', '<svg class="ref" ')
AZUL, TINTA, SUB = '#234899', '#16233F', '#566078'
PARES = [
 ('Outfit + Lexend', ('Outfit', 700), ('Lexend', 400), 'Outfit es la más parecida a Filson en títulos: geométrica, redonda y con la misma «a». Lexend en el texto distingue I, l y 1 porque su I lleva remates.'),
 ('Poppins + Lexend', ('Poppins', 600), ('Lexend', 400), 'Poppins es más ancha y conocida; en títulos se siente más «app». Mismo texto en Lexend.'),
 ('Lexend sola', ('Lexend', 600), ('Lexend', 400), 'Una sola familia para todo: la más simple de mantener. En títulos es un poco más ancha que Filson.'),
 ('Urbanist + Lexend', ('Urbanist', 700), ('Lexend', 400), 'Conserva el título actual del ecosistema y solo cambia el texto. Urbanist es más fría que Filson.'),
]
fams = sorted({p[1][0] for p in PARES} | {p[2][0] for p in PARES})
fuentes = '&'.join('family=' + f.replace(' ', '+') + ':wght@400;600;700' for f in fams)
def tarj(n, T, X, d):
    FT, FX = f"font-family:'{T[0]}',sans-serif", f"font-family:'{X[0]}',sans-serif"
    return f'''<article class="c"><header><h3>{n}</h3><p>{d}</p></header>
<div class="aa"><span><small>Filson Pro</small>{PAL}</span></div>
<div class="aa"><span><small>{T[0]} · títulos</small><b style="{FT};font-weight:{T[1]}">MedicalManik</b></span><span class="a" style="{FT};font-weight:{T[1]}">a</span><span class="a" style="{FX};font-weight:{X[1]}">a</span></div>
<div class="muestra"><b style="{FT};font-weight:{T[1]}">Expediente de Mariana Ruiz</b><span style="{FX}">Signos vitales · Consulta del 9 de noviembre</span>
<p style="{FX}">La receta se envía al correo del paciente y queda guardada en su expediente. Puedes reimprimirla desde Documentos.</p>
<p class="dato" style="{FX}"><b style="font-weight:600">Paracetamol 500 mg</b> · 1 tableta cada 8 h · Lote I1l-0O8 · Folio 0010</p>
<button type="button" style="{FT};font-weight:{T[1]}">Agendar cita</button></div></article>'''
HTML = f'''<title>MedicalManik · Tipografía r2</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fuentes}&display=swap">
<style>
/* Cuatro pares con la «a» de un piso de Filson: logotipo real arriba, la misma palabra y las dos «a» grandes, y una pantalla de ejemplo */
:root{{--bg:#f3f5f9;--fg:{TINTA};--muted:{SUB};--line:#dde2ec;--card:#fff;--ui:'Lexend',ui-sans-serif,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0f1524;--fg:#e8ecf5;--muted:#a3adc4;--line:#26304a;--card:#161e33;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0f1524;--fg:#e8ecf5;--muted:#a3adc4;--line:#26304a;--card:#161e33;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--ui);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1180px;margin:0 auto;display:grid;gap:26px}} h1{{font:700 clamp(30px,5vw,46px)/1.08 'Outfit',sans-serif;margin:0;text-wrap:balance}}
.intro{{display:grid;gap:12px;max-width:74ch}} .intro p{{margin:0;color:var(--muted)}} .ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(400px,1fr));gap:14px}}
.c{{display:grid;gap:12px;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;align-content:start;min-width:0}} .c header{{display:grid;gap:4px}} .c h3{{margin:0;font-size:21px}} .c header p{{margin:0;font-size:14px;color:var(--muted)}}
.aa{{display:flex;gap:14px;align-items:flex-end;flex-wrap:wrap;padding:12px 14px;border-radius:12px;background:#fff;border:1px solid var(--line);color:{AZUL}}} .aa>span{{display:grid;gap:2px}} .aa small{{font:12px var(--ui);color:{SUB}}}
.ref{{height:30px;width:auto;max-width:100%;color:{AZUL}}} .aa b{{font-size:34px;line-height:1}} .aa .a{{font-size:64px;line-height:.8;margin-left:auto}} .aa .a+.a{{margin-left:0;opacity:.75}}
.muestra{{display:grid;gap:6px;justify-items:start;padding:14px;border-radius:12px;background:#fff;border:1px solid var(--line);color:{TINTA}}} .muestra b{{font-size:22px;line-height:1.2}} .muestra span{{color:{SUB};font-size:15px}} .muestra p{{margin:0;font-size:15.5px;line-height:1.55}} .dato{{font-variant-numeric:tabular-nums}} .muestra .dato b{{font-size:inherit}}
.muestra button{{margin-top:6px;border:0;border-radius:999px;background:{AZUL};color:#fff;font-size:16px;padding:10px 22px;cursor:pointer}} .muestra button:focus-visible{{outline:3px solid {AZUL};outline-offset:2px}}
.nota{{padding:14px 18px;border-radius:14px;background:var(--card);border:1px solid var(--line);max-width:80ch}} .nota p{{margin:0 0 6px}}
</style>
<div class="w"><div class="intro"><p class="ojo">MedicalManik · tipografía · ronda 2</p><h1>La «a» de Filson, en títulos y en texto</h1>
<p>La «a» del logotipo es de un piso: un cuenco redondo con su asta recta. Revisé 19 fuentes de Google Fonts a 64 px y solo quedaron las que tienen esa «a». Cada par la comparte en títulos y en texto. En cada tarjeta ves el logotipo real, la misma palabra en la candidata y las dos «a» en grande.</p></div>
<section class="nota"><p><b>Una corrección:</b> en la ronda 1 dije que Figtree se parecía por su «a» de dos pisos. Me equivoqué: la de Filson es de un piso, así que Figtree, Plus Jakarta Sans, Hanken Grotesk y Manrope quedan fuera.</p><p><b>Un efecto:</b> Atkinson, la letra actual de los datos clínicos, también tiene la «a» de dos pisos. Para que todas las «a» sean iguales, el texto pasa a Lexend, que también distingue I, l y 1 (su I lleva remates).</p></section>
<div class="grid">{''.join(tarj(*p) for p in PARES)}</div></div>'''
open(os.path.join(D,'comparacion.html'),'w').write(HTML); print('ok')
