# Xila · guía de marca del rediseño. python3 guia.py -> guia.html (+ tarjeta-redes.png aparte)
import os, json, base64
H = os.path.dirname(os.path.abspath(__file__)); IC = os.path.join(H, '..', '..')
T = json.load(open(os.path.join(H, 'tema.json'))); C = {k: v['valor'] for k, v in T['color'].items()}
def sv(n): return open(os.path.join(H, 'svg', n + '.svg')).read()
def uri(p, mime='image/svg+xml'): return f'data:{mime};base64,' + base64.b64encode(open(p,'rb').read()).decode()
def png(n): return uri(os.path.join(H, 'png', n + '.png'), 'image/png')
GRANA, ESTELAR = uri(os.path.join(IC,'grana','grana.svg')), uri(os.path.join(IC,'estelar','final','svg','simbolo.svg'))
AN, AN2, AN3, AN4, MANTA, TXT2 = C['anil'], C['anil_medio'], C['anil_claro'], C['anil_bruma'], C['manta'], C['texto2']
FAM, SANS = "'Familjen Grotesk',ui-sans-serif,sans-serif", "'Instrument Sans',ui-sans-serif,system-ui,sans-serif"
niv = [('grande','64 px o más'),('mediano','32 a 48 px'),('chico','20 a 28 px'),('favicon','16 px')]
familia = ''.join(f'<figure><div class="t">{sv("simbolo-"+n)}</div><figcaption><b>{n.capitalize()}</b><span>{r}</span></figcaption></figure>' for n, r in niv)
familia_cl = ''.join(f'<figure><div class="t">{sv("simbolo-"+n+"-claro")}</div></figure>' for n, _ in niv)
reales = ''.join(f'<figure><img src="{png(p)}" width="{t}" height="{t}" alt=""><img class="z" src="{png(p)}" alt="{t} px ampliado"><figcaption>{t} px reales y × 6</figcaption></figure>' for p, t in [('favicon-16',16),('favicon-32',32),('favicon-48',48)])
pal = ''.join(f'<div class="sw"><i style="background:{v["valor"]}"></i><span><b>{k.replace("_"," ").capitalize()}</b><code>{v["valor"]}</code><small>{v["uso"]}</small></span></div>' for k, v in T['color'].items())
reglas = ''.join(f'<li>{r}</li>' for r in T['reglas'])
mal = [('Escalar el grande a 16 px', sv('simbolo-grande').replace('<svg ', '<svg style="width:16px;height:16px" ')),
       ('Rombo en otro color', sv('simbolo-grande').replace(AN3, '#E5007E')),
       ('Emblema añil sobre añil', '<span style="display:grid;place-items:center;width:96px;height:96px;background:' + AN + ';border-radius:12px">' + sv('simbolo-grande').replace('<svg ', '<svg style="width:72px;height:72px" ') + '</span>'),
       ('Escribir el nombre con una fuente', f'<span style="font:600 34px {FAM};color:{AN}">xila</span>')]
malh = ''.join(f'<figure class="no"><span>{s}</span><figcaption>✕ {t}</figcaption></figure>' for t, s in mal)
css = f''':root{{--papel:{MANTA};--tinta:{AN};--sub:{TXT2};--linea:#dcd6ca;--tarjeta:#fffdf9}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--papel:#0f1530;--tinta:#eef0f8;--sub:#b3bcd9;--linea:#2a3563;--tarjeta:#16204a;color-scheme:dark}}}}
:root[data-theme="dark"]{{--papel:#0f1530;--tinta:#eef0f8;--sub:#b3bcd9;--linea:#2a3563;--tarjeta:#16204a;color-scheme:dark}}
body{{margin:0;background:var(--papel);color:var(--tinta);font:16px/1.6 {SANS};padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 56px}}
main{{max-width:1060px;margin:0 auto;display:grid;gap:42px}}
.hero{{max-width:1060px;margin:0 auto 8px;background:{AN};color:{MANTA};border-radius:0 0 24px 24px;padding:48px 40px;display:grid;gap:22px}}
.hero .wm svg{{height:84px;width:auto;max-width:100%}} .hero h1{{margin:0;font:600 clamp(32px,5vw,52px)/1.05 {FAM};max-width:18ch}} .hero p{{margin:0;color:{AN4};max-width:60ch}}
h2{{font:600 32px/1.1 {FAM};margin:0 0 12px}} section>p{{margin:0 0 14px;max-width:70ch;color:var(--sub)}}
.box{{background:var(--tarjeta);border:1px solid var(--linea);border-radius:18px;padding:22px}}
.fam{{display:flex;gap:24px;flex-wrap:wrap;align-items:flex-end}} .fam figure{{margin:0;display:grid;gap:8px;justify-items:center}} .fam .t svg{{width:96px;height:96px}} .fam figcaption{{display:grid;text-align:center;line-height:1.3}} .fam span{{font-size:13px;color:var(--sub)}}
.fam.claro{{margin-top:14px;background:{AN};border-color:{AN}}}
.reales{{display:flex;gap:28px;flex-wrap:wrap;align-items:flex-end}} .reales figure{{margin:0;display:grid;gap:8px;justify-items:start}} .reales img.z{{width:144px;height:144px;image-rendering:pixelated;border-radius:8px}} .reales figcaption{{font-size:13px;color:var(--sub)}}
.wm2{{display:grid;gap:12px}} .wm2 div{{padding:22px;border-radius:14px}} .wm2 svg{{height:72px;width:auto;max-width:100%}} .cl{{background:{MANTA};border:1px solid var(--linea)}} .os{{background:{AN}}}
.pal{{display:grid;gap:10px}} .sw{{display:grid;grid-template-columns:46px minmax(0,1fr);gap:10px;align-items:center}} .sw i{{width:46px;height:46px;border-radius:10px;border:1px solid var(--linea)}} .sw span{{display:grid;line-height:1.3}} .sw code{{font-size:13px;color:var(--sub)}} .sw small{{color:var(--sub)}}
.tipo{{display:grid;gap:16px}} .tipo .p{{font:600 46px/1.05 {FAM}}} .tipo .s{{font:400 18px/1.55 {SANS}}} .tipo small{{display:block;color:var(--sub);font:13px {SANS};margin-top:4px}}
.apps{{display:flex;gap:18px;flex-wrap:wrap;align-items:flex-end}} .apps .ic svg{{width:104px;height:104px;display:block}} .tab{{display:flex;gap:8px;align-items:center;padding:8px 14px;border-radius:10px 10px 0 0;background:#fff;border:1px solid var(--linea);border-bottom:0;font-size:14px;color:{AN}}} .tab svg{{width:16px;height:16px}}
.eco{{display:flex;gap:30px;justify-content:center;align-items:center;flex-wrap:wrap;padding:22px;border-radius:14px;background:{MANTA};color:{AN}}} .eco figure{{margin:0;display:grid;justify-items:center;gap:6px;font-size:13px}} .eco svg,.eco img{{width:64px;height:64px}}
.nos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px}} .no{{margin:0;background:var(--tarjeta);border:1px solid var(--linea);border-radius:14px;padding:16px;display:grid;justify-items:center;gap:8px;text-align:center}} .no>span{{display:grid;place-items:center;min-width:96px;min-height:96px;background:{MANTA};border-radius:12px}} .no svg{{width:72px;height:72px}} .no figcaption{{color:#B42318;font-weight:600;font-size:14px}}
img.tarj{{width:100%;border-radius:16px;display:block}} ol{{margin:0;padding-left:22px}} li{{margin:4px 0}}'''
html = (f'<title>Xila · Guía de marca</title><meta name="claude:viewport-fit-sides" content="cover">'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@600&family=Instrument+Sans:wght@400;600&display=swap">'
 f'<style>{css}</style><header class="hero"><div class="wm">{sv("wordmark-oscuro")}</div><h1>Primero la pregunta, después la gráfica.</h1><p>Guía de marca 2.0: la x bordada en el rombo del huipil, el nombre en punto de cruz y un solo color, el añil.</p></header><main>'
 '<section><h2>La idea</h2><p>Xila borda los datos. El emblema es la x de Xila dentro del rombo del huipil, y el centro, en otro tono, es el dato: la misma regla que siguen sus gráficas, donde solo lo que importa va en color. El nombre se escribe en punto de cruz y el punto de la i también es el dato.</p>'
 f'<div class="eco"><figure><img src="{GRANA}" alt="">Grana · tiñe</figure><figure><img src="{ESTELAR}" alt="">Estelar · teje</figure><figure>{sv("simbolo-grande")}<b>Xila · borda</b></figure></div></section>'
 f'<section><h2>Un dibujo por tamaño</h2><p>Un emblema de 9 × 9 puntadas no se lee a 16 px: cada puntada mediría 1.5 px. Por eso hay cuatro dibujos con las mismas piezas; conforme baja el tamaño quedan menos puntadas y más gruesas. Cada uno se usa solo en su rango.</p>'
 f'<div class="box fam">{familia}</div><div class="box fam claro">{familia_cl}</div><div class="box reales" style="margin-top:14px">{reales}</div></section>'
 f'<section><h2>El nombre</h2><p>«xila» siempre va bordado en punto de cruz; nunca se escribe con una fuente. Desde 24 px de alto; más chico, se usa el símbolo con el texto al lado.</p><div class="wm2"><div class="cl">{sv("lockup")}</div><div class="os">{sv("lockup-oscuro")}</div></div></section>'
 f'<section><h2>Color: añil</h2><p>Un solo tinte en varias intensidades sobre manta. En las gráficas, el dato que importa va en añil y el contexto en gris. Contrastes medidos con la fórmula WCAG.</p><div class="box pal">{pal}</div><div class="box" style="margin-top:14px"><ol>{reglas}</ol></div></section>'
 f'<section><h2>Tipografía</h2><div class="box tipo"><div><span class="p">Oaxaca crece más que las demás regiones</span><small>Primaria · Familjen Grotesk 600 · lema, títulos de sección y el título de cada gráfica, que dice el hallazgo</small></div>'
 f'<div><span class="s">Ventas mensuales, enero a agosto de 2026. Oaxaca 1 210 400 (+18.2 %), Puebla 884 120 (+2.1 %).</span><small>Secundaria · Instrument Sans 400 y 600 · texto, ejes, etiquetas, tablas y botones, con cifras tabulares</small></div></div></section>'
 f'<section><h2>Aplicaciones</h2><div class="apps"><span class="ic">{sv("app-icon-redondeado")}</span><span class="tab">{sv("favicon")} xila · ventas</span></div>'
 '<p style="margin-top:16px">Vista previa para enlaces y redes, 1200 × 630:</p><img class="tarj" src="tarjeta-redes.png" alt="xila: Primero la pregunta, después la gráfica."></section>'
 f'<section><h2>Usos incorrectos</h2><div class="nos">{malh}</div></section></main>')
open(os.path.join(H,'guia.html'),'w').write(html); print('ok')
