# Estelar · ronda 6 · combinaciones de D (Instrument Serif) y F (Big Shoulders Display), elegidas 2026-11-09. python3 gen.py -> tipografia.html
import os, base64
D = os.path.dirname(os.path.abspath(__file__)); IC = os.path.join(D, '..', '..')
src = open(os.path.join(D,'..','ronda-3','gen.py')).read().split('def uri(')[0]
ns = {'__file__': os.path.join(D,'..','ronda-3','gen.py')}; exec(src, ns)
C1, C3, svg = ns['C1'], ns['C3'], ns['svg']
MANTA, TINTA, NOCHE, NOCHEFG, CAR, CAR_O = '#F6F1E8', '#15171F', '#15171F', '#F6F1E8', '#7B2D8E', '#C98BDB'
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(p,'rb').read()).decode()
XILA_WM = uri(os.path.join(IC,'xila','final','svg','wordmark.svg'))
SER = "'Instrument Serif',Georgia,serif"; SHO = "'Big Shoulders Display',Impact,sans-serif"; SAN = "'Instrument Sans',ui-sans-serif,system-ui,sans-serif"
# (id, título, nombre: familia/peso/estilo/tamaño, lema: familia/peso/estilo, etiqueta: familia/peso, descripción)
OPS = [
 ('1','Serif sola', (SER,400,'normal',46), (SER,400,'italic'), (SAN,600), 'Instrument Serif en todo lo de marca; el lema en cursiva, como firma. La más literaria y elegante.'),
 ('2','Industrial sola', (SHO,800,'normal',44), (SHO,600,'normal'), (SHO,700), 'Big Shoulders en todo lo de marca: el nombre, el lema y las etiquetas. La más firme, de letrero de fábrica textil.'),
 ('3','Nombre industrial, lema en serif', (SHO,800,'normal',44), (SER,400,'italic'), (SHO,700), 'El nombre y las etiquetas en Big Shoulders; el lema y los titulares en Instrument Serif cursiva. Fábrica y oficio juntos.'),
 ('4','Nombre en serif, etiquetas industriales', (SER,400,'normal',46), (SER,400,'italic'), (SHO,700), 'El nombre y el lema en Instrument Serif; las etiquetas y datos cortos en Big Shoulders mayúsculas. Elegante con un acento técnico.'),
]
def f(t, size=None, extra=''):
    fam, w = t[0], t[1]; st = t[2] if len(t) > 2 else 'normal'
    return f"font-family:{fam};font-weight:{w};font-style:{st};" + (f"font-size:{size}px;" if size else '') + extra
def op(k, nom, N, Le, Et, txt):
    return f'''<section class="op" aria-labelledby="h{k}"><header><p class="ojo">Combinación {k}</p><h2 id="h{k}">{nom}</h2><p>{txt}</p></header>
<div class="firma cl">{svg(C1(TINTA,CAR,TINTA),72,'Estelar')}<div><b style="{f(N,N[3])}">Estelar</b><span style="{f(Le,17)}">Del hilo suelto a la estrella</span></div></div>
<div class="firma os">{svg(C1(NOCHEFG,CAR_O,NOCHEFG),72,'Estelar')}<div><b style="{f(N,N[3])}">Estelar</b><span style="{f(Le,17)}">Del hilo suelto a la estrella</span></div></div>
<div class="banner"><div><p class="eb" style="{f(Et,14,'letter-spacing:.12em;text-transform:uppercase;')}">Estelar · modelado de datos</p><b style="{f(Le,None,'font-size:clamp(24px,2.4vw,32px);line-height:1.05;')}">Diseña en copo de nieve. Publica en estrella.</b><span style="font-family:{SAN}">Conecta tu base y mira su mapa.</span></div>{svg(C1(NOCHEFG,CAR_O,NOCHEFG),120,'Estelar')}</div>
<div class="fam"><span class="tab">{svg(C3(TINTA,CAR,TINTA),16,'Estelar')}<b style="{f(N,15)}">Estelar</b> · mapa</span><span class="chip" style="{f(Et,13,'letter-spacing:.08em;text-transform:uppercase;')}">5 dimensiones · 1 hecho</span><img src="{XILA_WM}" alt="xila" height="28"></div>
<p class="cuerpo">Cada vez que quieres entender un negocio desde su base de datos, repites lo mismo. Estelar te muestra el mapa, te guía para tejer un modelo estrella y guarda todo en una receta.</p></section>'''
HTML = f'''<title>Estelar · Tipografía r6</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Big+Shoulders+Display:wght@400..900&family=Instrument+Sans:wght@400;600&display=swap">
<style>
/* Cuatro combinaciones lado a lado: firma clara y oscura, portada, pestaña con etiqueta junto a Xila, párrafo */
:root{{--bg:#efebe3;--fg:#15171f;--muted:#5b5f6e;--line:#dcd6ca;--card:#fffdf9;--ui:{SAN}}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--ui);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1240px;margin:0 auto;display:grid;gap:28px}} h1{{font:400 clamp(34px,5vw,56px)/1.02 {SER};margin:0;text-wrap:balance}} h2{{margin:0;font-size:22px}}
.intro{{display:grid;gap:10px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}}
.ojo{{margin:0;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.tres{{display:grid;grid-template-columns:repeat(auto-fill,minmax(520px,1fr));gap:16px}}
.op{{display:grid;gap:12px;align-content:start;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;min-width:0}} .op header{{display:grid;gap:4px}} .op header p{{margin:0;font-size:14.5px}}
.firma{{display:flex;gap:16px;align-items:center;padding:16px;border-radius:12px;min-width:0}} .firma b{{display:block;line-height:.95;letter-spacing:-.005em}} .firma span{{display:block;opacity:.8;margin-top:6px}}
.cl{{background:{MANTA};color:{TINTA};border:1px solid var(--line)}} .os{{background:{NOCHE};color:{NOCHEFG}}}
.banner{{display:flex;gap:12px;align-items:center;justify-content:space-between;padding:22px;border-radius:12px;background:{NOCHE};color:{NOCHEFG};min-height:220px}}
.banner>div{{min-width:0}} .banner svg{{flex:none;width:28%;height:auto}} .banner .eb{{margin:0 0 8px;color:{CAR_O}}} .banner b{{display:block}} .banner span{{display:block;font-size:14px;opacity:.8;margin-top:10px}}
.fam{{display:flex;gap:12px;align-items:flex-end;flex-wrap:wrap;padding:12px;border-radius:12px;background:{MANTA};border:1px solid var(--line)}}
.tab{{display:flex;gap:7px;align-items:center;padding:7px 12px;border-radius:9px 9px 0 0;background:#fff;border:1px solid var(--line);border-bottom:0;font-size:14px;color:{TINTA}}}
.chip{{padding:4px 10px;border-radius:999px;background:#EFE3F3;color:{CAR}}}
.cuerpo{{margin:0;font-size:16px;line-height:1.55}}
@media (max-width:560px){{.tres{{grid-template-columns:1fr}}}}
</style>
<div class="w"><div class="intro"><p class="ojo">Ronda 6 · tipografía · D Instrument Serif + F Big Shoulders</p><h1>Estelar: serif, industrial o las dos</h1>
<p>Te gustaron las dos. No compiten: una es literaria y la otra de fábrica, y juntas cuentan el telar como oficio y como máquina. Aquí van solas y combinadas, en la firma, la portada, una etiqueta de datos y la pestaña. El texto corrido sigue en Instrument Sans.</p></div>
<div class="tres">{''.join(op(*o) for o in OPS)}</div></div>'''
open(os.path.join(D,'tipografia.html'),'w').write(HTML); print('ok')
