# Nexa Squad · ronda 7 · tipografía con la familia Huecos en B Cian (aprobado 2026-11-08). python3 gen.py -> tipografia.html
import os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D,'../r5-huecos/gen.py')).read().split('for i, n, r in AG:\n    open(')[0]
ns = {'__file__': os.path.join(D,'../r5-huecos/gen.py')}; exec(src, ns)
AG, CUT = ns['AG'], ns['CUT']
TINTA, CLARO_B, CIAN, CIAN_O = '#16161B', '#F3F3EE', '#22C3E6', '#00728A'
OPS = [
 ('a','Archivo','Archivo:wdth,wght@62..125,100..900',"'Archivo'",800,"font-stretch:112%",'Grotesca ancha y pesada: se ve hecha de bloques, como los símbolos. Mucha presencia en banners; ocupa más en nombres largos.'),
 ('b','Geist','Geist:wght@100..900',"'Geist'",600,'','Técnica y limpia, con aire de herramienta de desarrollo. Sobria; deja que el símbolo cargue la personalidad.'),
 ('c','Bricolage Grotesque','Bricolage+Grotesque:opsz,wght@12..96,400..800',"'Bricolage Grotesque'",700,'','La letra de Fruti Squad: las dos marcas se leen como hermanas. Riesgo: Nexa se confunde con Fruti.'),
]
def sym(id_, size, uid, label, bloque=TINTA, acc=CIAN):
    return (f'<svg viewBox="0 0 48 48" width="{size}" height="{size}" role="img" aria-label="{label}"><defs><mask id="{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48">'
            f'<rect width="48" height="48" fill="#fff"/>{CUT[id_]}</mask></defs><rect x="4" y="4" width="40" height="40" rx="7" fill="{acc}"/>'
            f'<rect x="4" y="4" width="40" height="40" rx="7" fill="{bloque}" mask="url(#{uid})"/></svg>')
c=[0]
def u(): c[0]+=1; return f't{c[0]}'
fuentes = '&'.join('family='+g for _,_,g,_,_,_,_ in OPS)
def op(k, nom, g, fam, peso, extra, txt):
    st = f"font-family:{fam},ui-sans-serif,system-ui,sans-serif;{extra}"
    agentes = ''.join(f'<div class="fa">{sym(i,36,u(),n)}<div><b style="{st};font-weight:{peso}">{n}</b><span style="{st};font-weight:400">{r}</span></div></div>' for i,n,r in AG[1:])
    return f'''<section class="op" aria-labelledby="h{k}"><header><p class="ojo">Opción {k.upper()}</p><h2 id="h{k}">{nom}</h2><p>{txt}</p></header>
<div class="firma cl">{sym('squad',72,u(),'Nexa Squad')}<div><b style="{st};font-weight:{peso}">Nexa Squad</b><span style="{st}">Composición de módulos, de punta a punta</span></div></div>
<div class="firma os">{sym('squad',72,u(),'Nexa Squad',CLARO_B,CIAN_O)}<div><b style="{st};font-weight:{peso}">Nexa Squad</b><span style="{st}">Composición de módulos, de punta a punta</span></div></div>
<div class="banner" style="{st}">{sym('kompa',120,u(),'Kompa',CLARO_B,CIAN_O)}<div><p class="eb" style="font-weight:600">Nexa Squad · agente</p><b style="font-weight:{peso}">Kompa</b><span>Acomoda cada sección: qué crece, qué cede y qué nunca se mueve.</span></div></div>
<div class="agentes">{agentes}</div>
<p class="cuerpo" style="{st};font-weight:400">Empieza con <code>/orka</code> y di lo que quieres con tus palabras. Orka decide qué agentes trabajan y en qué orden; tú solo apruebas reglas de negocio y lo que no se puede deshacer.</p>
</section>'''
HTML = f'''<title>Nexa Squad · Tipografía r7</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fuentes}&display=swap">
<style>
/* Tres columnas iguales: firma en claro y oscuro, banner de marketplace, firmas de agentes y un párrafo */
:root{{--bg:#f5f5f2;--fg:#16161b;--muted:#5a5a65;--line:#dbdbd4;--card:#fff;--paper:#fff;--night:#101014;--nightfg:#f3f3ee;--ui:ui-sans-serif,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#131317;--fg:#ededea;--muted:#a2a2ac;--line:#2b2b32;--card:#1a1a1f;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#131317;--fg:#ededea;--muted:#a2a2ac;--line:#2b2b32;--card:#1a1a1f;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--ui);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1280px;margin:0 auto;display:grid;gap:32px}}
h1{{font-size:clamp(28px,4.6vw,46px);line-height:1.05;margin:0;text-wrap:balance}} h2{{margin:0;font-size:24px}}
.intro{{display:grid;gap:10px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}}
.ojo{{margin:0;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.tres{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.op{{display:grid;gap:12px;align-content:start;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;min-width:0}}
.op header{{display:grid;gap:4px}} .op header p{{margin:0;font-size:14.5px}}
.firma{{display:flex;gap:14px;align-items:center;padding:16px;border-radius:12px;min-width:0}} .firma b{{display:block;font-size:30px;line-height:1;letter-spacing:-.01em}} .firma span{{display:block;font-size:14px;opacity:.75;margin-top:6px}}
.cl{{background:var(--paper);color:#16161b;border:1px solid var(--line)}} .os{{background:var(--night);color:var(--nightfg)}}
.banner{{display:flex;gap:16px;align-items:center;padding:18px;border-radius:12px;background:#16161b;color:#f3f3ee;aspect-ratio:1200/630;max-width:100%;overflow:hidden}}
.banner svg{{flex:none;width:30%;height:auto}} .banner .eb{{margin:0;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:{CIAN}}} .banner b{{display:block;font-size:clamp(26px,3vw,40px);line-height:1}} .banner span{{display:block;font-size:13.5px;opacity:.8;margin-top:6px}}
.agentes{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}} .fa{{display:flex;gap:8px;align-items:center;min-width:0;color:#16161b;background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:8px}}
.fa b{{display:block;font-size:17px;line-height:1.1}} .fa span{{display:block;font-size:12px;color:#5a5a65;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.cuerpo{{margin:0;font-size:16px;line-height:1.55}} code{{font-family:ui-monospace,monospace;font-size:.92em;background:color-mix(in srgb,{CIAN} 18%,transparent);padding:1px 5px;border-radius:5px}}
@media (max-width:1000px){{.tres{{grid-template-columns:1fr}}}}
</style>
<div class="w"><div class="intro"><p class="ojo">Ronda 7 · tipografía · color aprobado: tinta y cian</p><h1>Nexa Squad: tres letras para la marca</h1>
<p>El color quedó en tinta con el hueco en cian. Ahora falta la letra del nombre y de los productos. Las tres opciones son de Google Fonts y se prueban en lo mismo: firma, banner de marketplace (1200 × 630), firmas de agentes y un párrafo.</p></div>
<div class="tres">{''.join(op(*o) for o in OPS)}</div></div>'''
open(os.path.join(D,'tipografia.html'),'w').write(HTML); print('ok')
