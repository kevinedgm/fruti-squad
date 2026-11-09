# Estelar · guía de marca. Usa ../final (símbolos y tema). python3 gen.py -> guia.html (la tarjeta va como archivo aparte: ../final/png/tarjeta-redes.png)
import os, json, base64
H = os.path.dirname(os.path.abspath(__file__)); FIN = os.path.join(H, '..', 'final'); IC = os.path.join(H, '..', '..')
T = json.load(open(os.path.join(FIN, 'tema.json'))); C = T['color']
def sv(n): return open(os.path.join(FIN, 'svg', n + '.svg')).read()
def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(p,'rb').read()).decode()
GRANA, XILA = uri(os.path.join(IC,'grana','grana.svg')), uri(os.path.join(IC,'xila','final','svg','simbolo.svg'))
GRID = ''.join(f'<line x1="{4+i*8}" y1="0" x2="{4+i*8}" y2="64" stroke="{C["caracol"]["claro"]}" stroke-width=".2"/><line x1="0" y1="{4+i*8}" x2="64" y2="{4+i*8}" stroke="{C["caracol"]["claro"]}" stroke-width=".2"/>' for i in range(8))
cons = sv('simbolo').replace('</svg>', GRID + '</svg>')
mal = [('Pintar la urdimbre de caracol', sv('simbolo').replace('stroke="#15171F"', 'stroke="#7B2D8E"')),
       ('Caracol claro sobre manta', sv('simbolo').replace('#7B2D8E', '#C98BDB')),
       ('La estrella de 7 a 16 px', sv('simbolo').replace('<svg ', '<svg style="width:16px;height:16px" ')),
       ('Otro tinte por producto', sv('simbolo').replace('#7B2D8E', '#D14E0A'))]
malh = ''.join(f'<figure class="no"><span>{s}</span><figcaption>✕ {t}</figcaption></figure>' for t, s in mal)
reglas = ''.join(f'<li>{r}</li>' for r in T['reglas'])
pal = ''.join(f'<div class="sw"><i style="background:{v["claro"]}"></i><i style="background:{v["oscuro"]}"></i><span><b>{k.capitalize()}</b><code>{v["claro"]} · {v["oscuro"]}</code><small>{v.get("uso","")}</small></span></div>' for k, v in C.items())
SER = "'Instrument Serif',Georgia,serif"; SHO = "'Big Shoulders Display',Impact,sans-serif"; SAN = "'Instrument Sans',ui-sans-serif,system-ui,sans-serif"
css = f''':root{{--papel:{C["manta"]["claro"]};--tinta:{C["tinta"]["claro"]};--sub:{C["tinta2"]["claro"]};--linea:#dcd6ca;--tarjeta:{C["superficie"]["claro"]};--acento:{C["caracol"]["claro"]}}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--papel:#111218;--tinta:#f0ece4;--sub:#a9adbd;--linea:#2c2f3b;--tarjeta:#1b1d27;--acento:{C["caracol"]["oscuro"]};color-scheme:dark}}}}
:root[data-theme="dark"]{{--papel:#111218;--tinta:#f0ece4;--sub:#a9adbd;--linea:#2c2f3b;--tarjeta:#1b1d27;--acento:{C["caracol"]["oscuro"]};color-scheme:dark}}
body{{margin:0;background:var(--papel);color:var(--tinta);font:16px/1.6 {SAN};padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 56px}}
main{{max-width:1060px;margin:0 auto;display:grid;gap:40px}}
.hero{{max-width:1060px;margin:0 auto 8px;background:{C["manta"]["oscuro"]};color:{C["tinta"]["oscuro"]};border-radius:0 0 24px 24px;padding:48px 40px;display:flex;gap:36px;align-items:center;flex-wrap:wrap}}
.hero svg{{width:150px;height:150px}} .hero .e{{margin:0;font:800 16px {SHO};letter-spacing:.14em;color:{C["caracol"]["oscuro"]}}} .hero h1{{margin:4px 0 0;font:800 clamp(56px,9vw,96px)/.9 {SHO}}}
.hero p.l{{margin:10px 0 0;font:italic 400 clamp(22px,3vw,30px)/1.2 {SER};color:#c9c6bf}}
h2{{font:800 34px/1 {SHO};margin:0 0 12px;letter-spacing:.01em}} section>p{{margin:0 0 14px;max-width:70ch;color:var(--sub)}}
.box{{background:var(--tarjeta);border:1px solid var(--linea);border-radius:18px;padding:22px}}
.par{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}} .par figure{{margin:0;display:grid;gap:8px;justify-items:center;padding:18px;border-radius:14px}} .par svg{{width:96px;height:96px}} .par figcaption{{font-size:13px}}
.cl{{background:{C["manta"]["claro"]};color:{C["tinta"]["claro"]};border:1px solid var(--linea)}} .os{{background:{C["manta"]["oscuro"]};color:{C["tinta"]["oscuro"]}}}
.cons{{display:flex;gap:28px;align-items:center;flex-wrap:wrap}} .cons svg{{width:220px;height:220px;background:{C["manta"]["claro"]};border-radius:12px;border:1px solid var(--linea)}} .cons ul{{margin:0;padding-left:20px;flex:1;min-width:260px}}
.pal{{display:grid;gap:10px}} .sw{{display:grid;grid-template-columns:40px 40px minmax(0,1fr);gap:8px;align-items:center}} .sw i{{width:40px;height:40px;border-radius:10px;border:1px solid var(--linea)}} .sw span{{display:grid;line-height:1.3}} .sw code{{font-size:13px;color:var(--sub)}} .sw small{{color:var(--sub)}}
.tipo{{display:grid;gap:14px}} .tipo .n{{font:800 64px/1 {SHO}}} .tipo .l{{font:italic 400 34px/1.15 {SER}}} .tipo .t{{font:400 17px/1.55 {SAN}}} .tipo small{{display:block;color:var(--sub);font:13px {SAN};margin-top:4px}}
.wm{{display:grid;gap:12px}} .wm div{{padding:20px;border-radius:14px}} .wm svg{{height:70px;width:auto;max-width:100%}}
.apps{{display:flex;gap:16px;flex-wrap:wrap;align-items:flex-end}} .apps .ic svg{{width:96px;height:96px;border-radius:22px;display:block}}
.tab{{display:flex;gap:8px;align-items:center;padding:8px 14px;border-radius:10px 10px 0 0;background:#fff;border:1px solid var(--linea);border-bottom:0;font-size:14px;color:{C["tinta"]["claro"]}}} .tab svg{{width:16px;height:16px}}
.eco{{display:flex;gap:28px;justify-content:center;align-items:center;flex-wrap:wrap;padding:22px;border-radius:14px}} .eco figure{{margin:0;display:grid;justify-items:center;gap:6px;font-size:13px}} .eco svg,.eco img{{width:64px;height:64px}}
.nos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px}} .no{{margin:0;background:var(--tarjeta);border:1px solid var(--linea);border-radius:14px;padding:16px;display:grid;justify-items:center;gap:8px;text-align:center}}
.no span{{display:grid;place-items:center;width:96px;height:96px;background:{C["manta"]["claro"]};border-radius:12px}} .no svg{{width:72px;height:72px}} .no figcaption{{color:#B42318;font-weight:600;font-size:14px}}
img.tarj{{width:100%;border-radius:16px;display:block}} ol{{margin:0;padding-left:22px}} li{{margin:4px 0}}
@media (max-width:760px){{.par{{grid-template-columns:repeat(2,minmax(0,1fr))}}.hero{{padding:32px 20px}}}}'''
html = (f'<title>Estelar · Guía de marca</title><meta name="claude:viewport-fit-sides" content="cover">'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800&family=Instrument+Serif:ital@0;1&family=Instrument+Sans:wght@400;600&display=swap">'
 f'<style>{css}</style><header class="hero">{sv("simbolo-oscuro")}<div><p class="e">GUÍA DE MARCA</p><h1>Estelar</h1><p class="l">Del hilo suelto a la estrella</p></div></header><main>'
 '<section><h2>La idea</h2><p>Estelar teje los hilos sueltos de una base de datos hasta que forman una estrella. El símbolo es la estrella de ocho puntas del telar de cintura: la urdimbre (los hilos verticales) es la estructura de la base, los flotes en caracol son lo que el modelo deja ver, y el cuadro del centro es el hecho alrededor del cual giran las dimensiones.</p>'
 f'<div class="box eco cl"><figure><img src="{GRANA}" alt="">Grana · el tinte</figure><figure>{sv("simbolo")}<b>Estelar · el telar</b></figure><figure><img src="{XILA}" alt="">Xila · el bordado</figure></div></section>'
 f'<section><h2>El símbolo</h2><p>Dos dibujos de la misma estrella: el de 7 × 7 con urdimbre para la marca, desde 32 px, y el de 5 × 5 sin urdimbre para 16 a 24 px, donde los hilos finos ya no se ven.</p>'
 f'<div class="par"><figure class="cl">{sv("simbolo")}<figcaption>Marca · claro</figcaption></figure><figure class="os">{sv("simbolo-oscuro")}<figcaption>Marca · oscuro</figcaption></figure><figure class="cl">{sv("simbolo-16")}<figcaption>Chico · claro</figcaption></figure><figure class="os">{sv("simbolo-16-oscuro")}<figcaption>Chico · oscuro</figcaption></figure></div>'
 f'<div class="box cons" style="margin-top:14px">{cons}<ul><li>Retícula de 7 × 7 celdas de 8 en un lienzo de 64, margen de 4.</li><li>Flotes de 0.6 celdas de alto con extremos redondos; la urdimbre, a 0.14 celdas y 40 % de opacidad.</li><li>El centro, un cuadro abierto que se rellena en tinta: el hecho.</li><li>Margen de respeto: la mitad del símbolo alrededor.</li></ul></div></section>'
 f'<section><h2>Color</h2><p>La manta y la tinta son las de Xila; el acento es el púrpura de caracol, el tinte de la costa de Oaxaca. Los contrastes se midieron con la fórmula WCAG.</p><div class="box pal">{pal}</div><div class="box" style="margin-top:14px"><ol>{reglas}</ol></div></section>'
 f'<section><h2>Tipografía</h2><div class="box tipo"><div><span class="n">Estelar</span><small>Big Shoulders Display 800 · el nombre y las etiquetas cortas en mayúsculas</small></div>'
 f'<div><span class="l">Diseña en copo de nieve. Publica en estrella.</span><small>Instrument Serif cursiva · el lema y los titulares de portada</small></div>'
 f'<div><span class="t">Conecta tu base y mira su mapa: tablas, relaciones conocidas y las que Estelar descubre para que las confirmes.</span><small>Instrument Sans · el texto y la interfaz, la letra de lectura de Xila</small></div></div>'
 f'<div class="wm" style="margin-top:14px"><div class="cl">{sv("wordmark")}</div><div class="os">{sv("wordmark-oscuro")}</div></div></section>'
 f'<section><h2>Aplicaciones</h2><div class="apps"><span class="ic">{sv("app-icon-redondeado")}</span><span class="tab">{sv("simbolo-16")} Estelar · mapa</span></div>'
 '<p style="margin-top:16px">Vista previa para enlaces y redes, 1200 × 630:</p><img class="tarj" src="tarjeta-redes.png" alt="Estelar: Diseña en copo de nieve. Publica en estrella."></section>'
 f'<section><h2>Usos incorrectos</h2><div class="nos">{malh}</div></section></main>')
open(os.path.join(H,'guia.html'),'w').write(html); print('ok')
