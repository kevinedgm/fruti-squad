# Plan A · informe de diagnóstico de 2 páginas. Uso: python gen-informe.py <lotes.csv> "<Nombre del cliente>" <carpeta de fuentes>
# Produce informe.html (carta, 2 páginas) listo para imprimir a PDF con Chromium.
import csv,sys,statistics as st,datetime
CSV,CLIENTE,FD=sys.argv[1],sys.argv[2],sys.argv[3]
INK='#0e0f1c'; BG='#ffffff'; IND='#4338ca'; OLIVA='#4d7c0f'; MUTED='#5a5c72'; LINE='#e4e5ee'; BAD='#c62828'; GRIS='#c9cad6'
R=[]
for d in csv.DictReader(open(CSV)):
    for k in d:
        if k not in ('lote','mes','agave'): d[k]=float(d[k])
    d['mt']=d['merma_horneado']+d['merma_molienda']+d['merma_fermentacion']+d['merma_destilacion']; R.append(d)
L=sum(d['litros'] for d in R); C=sum(d['costo_total_mxn'] for d in R); KG=sum(d['kg_agave'] for d in R)
ET=('merma_horneado','merma_molienda','merma_fermentacion','merma_destilacion')
MED={k:st.median(d[k] for d in R) for k in ET}
for d in R: d['exceso']=sum(max(0,d[k]-MED[k]) for k in ET if d[k]-MED[k]>.04)
atip=[d for d in R if d['exceso']>0]; med=st.median(d['mt'] for d in R)
perd=sum(d['litros']*d['exceso']/(1-d['mt']) for d in atip); cpl=C/L
esp=[d for d in R if d['agave']=='Espadín']; silv=[d for d in R if d['agave']!='Espadín']
def margen(g): return sum((d['precio_venta_litro_mxn']-d['costo_total_mxn']/d['litros'])*d['litros'] for d in g)/sum(d['litros'] for d in g)
pf=max(R,key=lambda d:d['merma_fermentacion']); ph=max(R,key=lambda d:d['merma_horneado'])
medF=st.median(d['merma_fermentacion'] for d in R)
n=lambda v:f'{v:,.0f}'; p=lambda v:f'{v*100:.0f} %'; p1=lambda v:f'{v*100:.1f} %'
# --- gráficas SVG
def barras(key,fmt,color,W=330,H=150):
    ml=44; mx=max(d[key] for d in R)*1.1; bw=(W-ml-6)/len(R); s=f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Space Grotesk, sans-serif" font-size="9">'
    for i in range(5):
        v=mx*i/4; y=H-24-(H-34)*i/4; s+=f'<line x1="{ml}" x2="{W-6}" y1="{y:.1f}" y2="{y:.1f}" stroke="{LINE}"/><text x="{ml-5}" y="{y+3:.1f}" text-anchor="end" fill="{MUTED}">{fmt(v)}</text>'
    for i,d in enumerate(R):
        h=(H-34)*d[key]/mx; x=ml+i*bw+bw*.18; s+=f'<rect x="{x:.1f}" y="{H-24-h:.1f}" width="{bw*.64:.1f}" height="{h:.1f}" rx="3" fill="{color(d)}"/><text x="{x+bw*.32:.1f}" y="{H-9}" text-anchor="middle" fill="{MUTED}">{d["lote"]}</text>'
    return s+'</svg>'
def apiladas(W=330,H=150):
    et=[('merma_horneado','Horneado',IND),('merma_molienda','Molienda','#8b8cf8'),('merma_fermentacion','Fermentación',OLIVA),('merma_destilacion','Destilación','#b7c98a')]
    ml=40; mx=max(.3,max(d['mt'] for d in R)*1.1); bw=(W-ml-6)/len(R); s=f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Space Grotesk, sans-serif" font-size="9">'
    for i in range(4):
        v=mx*i/3; y=H-24-(H-34)*i/3; s+=f'<line x1="{ml}" x2="{W-6}" y1="{y:.1f}" y2="{y:.1f}" stroke="{LINE}"/><text x="{ml-5}" y="{y+3:.1f}" text-anchor="end" fill="{MUTED}">{p(v)}</text>'
    for i,d in enumerate(R):
        x=ml+i*bw+bw*.18; y0=H-24
        for k,_,c in et:
            h=(H-34)*d[k]/mx; s+=f'<rect x="{x:.1f}" y="{y0-h:.1f}" width="{bw*.64:.1f}" height="{max(0,h-1.5):.1f}" fill="{c}"/>'; y0-=h
        s+=f'<text x="{x+bw*.32:.1f}" y="{H-9}" text-anchor="middle" fill="{MUTED if d["exceso"]==0 else BAD}">{d["lote"]}</text>'
    leg=' '.join(f'<span><i style="background:{c}"></i>{nm}</span>' for _,nm,c in et)
    return s+'</svg>',leg
g_merma,leg=apiladas(); g_costo=barras('costo_por_litro_mxn',lambda v:f'${v:,.0f}',lambda d:IND if d['agave']=='Espadín' else GRIS)
filas=''.join(f'<tr{" class=alerta" if d["exceso"]>0 else ""}><td>{d["lote"]}</td><td>{d["agave"]}</td><td>{n(d["kg_agave"])}</td><td>{n(d["litros"])}</td><td>{d["rendimiento_kg_por_l"]:.1f}</td><td>{p1(d["merma_fermentacion"])}</td><td>{p1(d["merma_horneado"])}</td><td>{p1(d["mt"])}</td><td>${n(d["costo_por_litro_mxn"])}</td></tr>' for d in R)
lock=open('/home/user/fruti-squad/.fruti/icons/clnda/final/svg/lockup.svg').read(); firma=open('/home/user/fruti-squad/.fruti/icons/clnda/final/svg/firma.svg').read()
ms,me=margen(silv),margen(esp)
if ms>me: rec3=f'<div class="rec"><b class="num">3</b><div><h2>Mezcla de productos: un lote más de silvestre al año deja más que uno de espadín.</h2><p>El margen bruto por litro de silvestre ({len(silv)} lotes) es de ${n(ms)} contra ${n(me)} en espadín, aun con el costo por litro más alto. La restricción es el agave, no el mercado: conviene planear la compra de silvestre con un año de anticipación.</p><p class="ev">Evidencia: costo por litro y precio de venta por lote; margen = (precio − costo por litro) × litros ÷ litros.</p></div></div>'
else: rec3=f'<div class="rec"><b class="num">3</b><div><h2>Precio del silvestre: hoy deja menos margen por litro que el espadín.</h2><p>El margen bruto por litro de silvestre ({len(silv)} lotes) es de ${n(ms)} contra ${n(me)} en espadín: el precio de venta no cubre el costo extra del agave y el rendimiento más bajo. O sube el precio del silvestre a partir de ${n(sum(d["costo_total_mxn"] for d in silv)/sum(d["litros"] for d in silv)+me)} por litro, o se reduce su participación hasta que el agave baje.</p><p class="ev">Evidencia: costo por litro y precio de venta por lote; margen = (precio − costo por litro) × litros ÷ litros.</p></div></div>'
hoy=datetime.date.today().strftime('%d de %B de %Y').replace('October','octubre')
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Diagnóstico de producción · {CLIENTE}</title>
<style>
@font-face{{font-family:"Space Grotesk";src:url("file://{FD}/SpaceGrotesk[wght].ttf");font-weight:300 700}}
@page{{size:letter;margin:0}} *{{box-sizing:border-box}}
html,body{{margin:0;background:#eee;color:{INK};font:10.5pt/1.4 "Space Grotesk",system-ui,sans-serif}}
.pag{{width:8.5in;height:11in;padding:.6in .65in .55in;background:{BG};margin:0 auto 12px;display:grid;grid-template-rows:auto 1fr auto;gap:12pt;page-break-after:always;position:relative}}
@media print{{html,body{{background:#fff}} .pag{{margin:0}}}}
.cab{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid {INK};padding-bottom:8pt}}
.cab .lk{{width:120pt}} .cab svg{{width:100%;height:auto;display:block}} .cab .meta{{text-align:right;font-size:8.5pt;color:{MUTED}}} .cab .meta b{{display:block;font-size:11pt;color:{INK}}}
h1{{font-size:20pt;line-height:1.15;margin:0 0 4pt;letter-spacing:-.01em;font-weight:700}} h2{{font-size:11pt;margin:0 0 4pt;font-weight:700}} h3{{font-size:9pt;margin:0;color:{MUTED};font-weight:500;text-transform:uppercase;letter-spacing:.06em}}
p{{margin:0}} .lead{{font-size:12pt;line-height:1.35;max-width:60ch}}
.kpis{{display:grid;grid-template-columns:repeat(4,1fr);gap:10pt;margin:10pt 0}} .kpi{{border-top:2px solid {IND};padding-top:5pt}} .kpi b{{display:block;font-size:17pt;font-weight:700;letter-spacing:-.01em}} .kpi span{{font-size:8.5pt;color:{MUTED}}}
.dos{{display:grid;grid-template-columns:1fr 1fr;gap:14pt}} .fig{{display:grid;gap:4pt}} .fig .n{{font-size:8.5pt;color:{MUTED}}} .leg{{font-size:8pt;color:{MUTED};display:flex;gap:8pt;flex-wrap:wrap}} .leg i{{display:inline-block;width:7pt;height:7pt;margin-right:3pt;vertical-align:-1px;border-radius:1.5pt}}
.rec{{display:grid;grid-template-columns:20pt 1fr;gap:8pt;padding:8pt 0;border-top:1px solid {LINE}}} .rec b.num{{font-size:16pt;color:{IND};line-height:1}} .rec h2{{margin-bottom:2pt}} .rec .ev{{font-size:9pt;color:{MUTED}}}
table{{border-collapse:collapse;width:100%;font-size:8.5pt;font-variant-numeric:tabular-nums}} th,td{{padding:3pt 5pt;border-bottom:1px solid {LINE};text-align:right;white-space:nowrap}} th:first-child,td:first-child,th:nth-child(2),td:nth-child(2){{text-align:left}} th{{color:{MUTED};font-weight:500}} tr.alerta td{{color:{BAD}}}
.reg{{background:#f4f4fa;border-radius:6pt;padding:8pt 10pt;font-size:9pt}} .reg ul{{margin:3pt 0 0;padding-left:14pt}} .reg li{{margin:1pt 0}}
.pie{{display:flex;justify-content:space-between;align-items:center;font-size:8pt;color:{MUTED};border-top:1px solid {LINE};padding-top:6pt}} .pie .f{{width:150pt}} .pie svg{{width:100%;height:auto;display:block}}
.muestra{{position:absolute;top:.25in;left:.65in;font-size:7.5pt;color:{MUTED};letter-spacing:.08em;text-transform:uppercase}}
</style></head><body>
<section class="pag">
<header class="cab"><div class="lk">{lock}</div><div class="meta"><b>{CLIENTE}</b>Diagnóstico de producción · {len(R)} lotes · {R[0]['mes']} a {R[-1]['mes']}<br>{hoy}</div></header>
<main>
<h3>Hallazgo</h3>
<h1>{n(perd)} litros se fueron en {len(atip)} lotes con mermas atípicas: unos ${n(perd*cpl)} de costo sin producto.</h1>
<p class="lead">En {len(R)} lotes se produjeron {n(L)} litros a un costo promedio de ${n(cpl)} por litro. La merma total normal del palenque es {p(med)}; en {len(atip)} lotes ({", ".join(d["lote"] for d in atip)}) una etapa se salió de lo normal por más de cuatro puntos, y ahí está la pérdida que se puede evitar.</p>
<div class="kpis"><div class="kpi"><b>{n(L)} L</b><span>litros producidos</span></div><div class="kpi"><b>${n(cpl)}</b><span>costo por litro, promedio ponderado</span></div><div class="kpi"><b>{KG/L:.1f} kg/L</b><span>rendimiento: kilos de agave por litro</span></div><div class="kpi"><b>{p1(sum(d['mt']*d['litros'] for d in R)/L)}</b><span>merma total promedio</span></div></div>
<div class="dos">
<div class="fig"><h2>Mermas por etapa por lote</h2><div class="leg">{leg}</div>{g_merma}<p class="n">Un lote sano suma entre 15 y 25 %. En rojo, lotes con una etapa fuera de lo normal.</p></div>
<div class="fig"><h2>Costo por litro por lote</h2>{g_costo}<p class="n">Espadín en índigo; silvestre en gris. Dentro de espadín, los picos son mermas, no agave.</p></div>
</div>
<div class="reg" style="margin-top:12pt"><b>Cómo leer estas cifras</b><ul><li><b>Costo por litro:</b> todo lo gastado en el lote (agave, leña, jornales, otros) entre los litros que salieron del alambique.</li><li><b>Rendimiento:</b> kilos de agave que hicieron falta por cada litro; menos es mejor. Espadín suele estar entre 8 y 10; silvestres entre 12 y 18.</li><li><b>Merma por etapa:</b> porcentaje que se pierde en horneado, molienda, fermentación y destilación. Se compara cada lote con la mediana del propio palenque, no con un estándar externo.</li><li><b>Lote atípico:</b> una etapa más de cuatro puntos arriba de su mediana. Los litros perdidos son el exceso sobre lo normal, no toda la merma.</li></ul></div>
</main>
<footer class="pie"><span>Página 1 de 2 · confidencial, preparado para {CLIENTE}</span><div class="f">{firma}</div></footer>
</section>
<section class="pag">
<header class="cab"><div class="lk">{lock}</div><div class="meta"><b>{CLIENTE}</b>Tres recomendaciones y los doce lotes</div></header>
<main>
<h3>Qué cambiar primero</h3>
<div class="rec"><b class="num">1</b><div><h2>Fermentación: registrar temperatura y días de tina por lote.</h2><p>El lote {pf['lote']} perdió {p(pf['merma_fermentacion'])} en tina contra una mediana de {p(medF)}. Sin registro de tina no se puede saber si fue clima, agua o tiempo; con él, se ve antes de destilar y se decide si vale la pena pasar el lote al alambique.</p><p class="ev">Evidencia: columna «Merma ferm.» de la tabla; gráfica de mermas, lote {pf['lote']}.</p></div></div>
<div class="rec"><b class="num">2</b><div><h2>Horneado: revisar sellado y temperatura del horno antes del siguiente silvestre.</h2><p>El lote {ph['lote']} perdió {p(ph['merma_horneado'])} en el horno. Una merma de horneado arriba de 10 % casi siempre es sellado o lectura de temperatura, no el agave. En un lote de silvestre, ese 10 % vale varias veces más que en espadín.</p><p class="ev">Evidencia: columna «Merma horno», lote {ph['lote']}.</p></div></div>
{rec3}
<div class="reg"><b>Qué registrar a partir del próximo lote</b> (una hoja por lote, cinco minutos):<ul><li>Kilos de agave al entrar y al salir del horno.</li><li>Litros de jugo al salir de la molienda y al entrar a tina.</li><li>Temperatura y días de tina; fecha de inicio y fin.</li><li>Litros a la salida de cada destilación y grado.</li><li>Leña, jornales y otros gastos del lote.</li></ul></div>
<h2 style="margin-top:10pt">Los {len(R)} lotes</h2>
<table><thead><tr><th>Lote</th><th>Agave</th><th>kg agave</th><th>Litros</th><th>kg/L</th><th>Merma ferm.</th><th>Merma horno</th><th>Merma total</th><th>$/L</th></tr></thead><tbody>{filas}</tbody></table>
</main>
<footer class="pie"><span>Página 2 de 2 · siguiente paso: tablero con estos datos, actualizado cada mes</span><div class="f">{firma}</div></footer>
</section>
</body></html>'''
open('informe.html','w').write(html); print('ok',n(perd),len(atip))
