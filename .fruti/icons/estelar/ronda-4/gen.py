# Estelar · ronda 4 · tipografía con C1 + C3 en Caracol, estrella en color (2026-11-09). python3 gen.py -> tipografia.html
import os, base64, importlib.util
D = os.path.dirname(os.path.abspath(__file__)); IC = os.path.join(D, '..', '..')
src = open(os.path.join(D,'..','ronda-3','gen.py')).read().split('def uri(')[0]
ns = {'__file__': os.path.join(D,'..','ronda-3','gen.py')}; exec(src, ns)
C1, C3, svg = ns['C1'], ns['C3'], ns['svg']
MANTA, TINTA, NOCHE, NOCHEFG, CAR, CAR_O = '#F6F1E8', '#15171F', '#15171F', '#F6F1E8', '#7B2D8E', '#C98BDB'
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(p,'rb').read()).decode()
XILA_WM = uri(os.path.join(IC,'xila','final','svg','wordmark.svg'))
OPS = [('a','Instrument Sans','Instrument+Sans:wght@400..700',"'Instrument Sans'",700,'La letra de Xila (y de su interfaz): Estelar y Xila firmarían igual. Sobria, ancha, técnica.'),
       ('b','Fraunces','Fraunces:opsz,wght@9..144,400..700',"'Fraunces'",600,'La serif de los títulos de Xila: cálida y editorial, con aire de oficio. La que más se aleja del «software genérico».'),
       ('c','Schibsted Grotesk','Schibsted+Grotesk:wght@400..800',"'Schibsted Grotesk'",700,'Grotesca de periódico, compacta y firme. Propia de Estelar; no la usa nadie más en el ecosistema.')]
fuentes = '&'.join('family='+g for _,_,g,_,_,_ in OPS)
def op(k, nom, g, fam, peso, txt):
    st = f"font-family:{fam},ui-sans-serif,system-ui,sans-serif"
    return f'''<section class="op" aria-labelledby="h{k}"><header><p class="ojo">Opción {k.upper()}</p><h2 id="h{k}">{nom}</h2><p>{txt}</p></header>
<div class="firma cl">{svg(C1(TINTA,CAR,TINTA),72,'Estelar')}<div><b style="{st};font-weight:{peso}">Estelar</b><span style="{st}">Del hilo suelto a la estrella</span></div></div>
<div class="firma os">{svg(C1(NOCHEFG,CAR_O,NOCHEFG),72,'Estelar')}<div><b style="{st};font-weight:{peso}">Estelar</b><span style="{st}">Del hilo suelto a la estrella</span></div></div>
<div class="banner" style="{st}"><div><p class="eb">Estelar</p><b style="font-weight:{peso}">Diseña en copo de nieve. Publica en estrella.</b><span>Conecta tu base y mira su mapa.</span></div>{svg(C1(NOCHEFG,CAR_O,NOCHEFG),130,'Estelar')}</div>
<div class="fam"><span class="tab">{svg(C3(TINTA,CAR,TINTA),16,'Estelar')}<b style="{st};font-weight:{peso}">Estelar</b> · mapa</span><img src="{XILA_WM}" alt="xila" height="30"></div>
<p class="cuerpo" style="{st}">Cada vez que quieres entender un negocio desde su base de datos, repites lo mismo. Estelar te muestra el mapa, te guía para tejer un modelo estrella y guarda todo en una receta.</p></section>'''
HTML = f'''<title>Estelar · Tipografía r4</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fuentes}&display=swap">
<style>
/* Tres columnas iguales: firma clara y oscura, portada, pestaña junto a la firma de Xila, y un párrafo */
:root{{--bg:#efebe3;--fg:#15171f;--muted:#5b5f6e;--line:#dcd6ca;--card:#fffdf9;--ui:ui-sans-serif,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--ui);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1280px;margin:0 auto;display:grid;gap:28px}} h1{{font-size:clamp(28px,4.6vw,46px);line-height:1.05;margin:0;text-wrap:balance}} h2{{margin:0;font-size:24px}}
.intro{{display:grid;gap:10px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}}
.ojo{{margin:0;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.tres{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.op{{display:grid;gap:12px;align-content:start;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;min-width:0}} .op header{{display:grid;gap:4px}} .op header p{{margin:0;font-size:14.5px}}
.firma{{display:flex;gap:14px;align-items:center;padding:16px;border-radius:12px;min-width:0}} .firma b{{display:block;font-size:38px;line-height:1;letter-spacing:-.01em}} .firma span{{display:block;font-size:14px;opacity:.75;margin-top:6px}}
.cl{{background:{MANTA};color:{TINTA};border:1px solid var(--line)}} .os{{background:{NOCHE};color:{NOCHEFG}}}
.banner{{display:flex;gap:12px;align-items:center;justify-content:space-between;padding:20px;border-radius:12px;background:{NOCHE};color:{NOCHEFG};min-height:220px;max-width:100%}}
.banner svg{{flex:none;width:32%;height:auto}} .banner>div{{min-width:0}} .banner .eb{{margin:0 0 6px;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:{CAR_O};font-weight:700}} .banner b{{display:block;font-size:clamp(20px,2vw,26px);line-height:1.1}} .banner span{{display:block;font-size:13.5px;opacity:.8;margin-top:8px}}
.fam{{display:flex;gap:14px;align-items:flex-end;flex-wrap:wrap;padding:12px;border-radius:12px;background:{MANTA};border:1px solid var(--line)}} .tab{{display:flex;gap:7px;align-items:center;padding:7px 12px;border-radius:9px 9px 0 0;background:#fff;border:1px solid var(--line);border-bottom:0;font-size:14px;color:{TINTA}}}
.cuerpo{{margin:0;font-size:16px;line-height:1.55}}
@media (max-width:1000px){{.tres{{grid-template-columns:1fr}}}}
</style>
<div class="w"><div class="intro"><p class="ojo">Ronda 4 · tipografía · color: Caracol, la estrella en color</p><h1>Estelar: tres letras para el nombre</h1>
<p>El tinte quedó en Caracol. Lo apliqué con la estrella en color, porque solo el centro casi no se ve a 16 px. Ahora falta la letra del nombre. Las tres son de Google Fonts y se prueban en la firma, una portada de 1200 × 630, una pestaña junto a la firma de Xila y un párrafo del brief.</p></div>
<div class="tres">{''.join(op(*o) for o in OPS)}</div></div>'''
open(os.path.join(D,'tipografia.html'),'w').write(HTML); print('ok')
