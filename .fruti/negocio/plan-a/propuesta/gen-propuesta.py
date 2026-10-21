# Plan A · propuesta escrita tras la reunión. Uso: python gen-propuesta.py <datos.json> <carpeta de fuentes>
import sys,json
D=json.load(open(sys.argv[1])); FD=sys.argv[2]
INK='#0e0f1c'; IND='#4338ca'; MUTED='#5a5c72'; LINE='#e4e5ee'; SOFT='#f4f4fa'
lock=open('/home/user/fruti-squad/.fruti/icons/clnda/final/svg/lockup.svg').read(); firma=open('/home/user/fruti-squad/.fruti/icons/clnda/final/svg/firma.svg').read()
completo=D['paquete']=='completo'
precio='$25,000' if completo else '$15,000'; plazo='dos semanas' if completo else 'una semana'
entregables=[('Informe de diagnóstico, 2 páginas','El hallazgo principal en una frase, costo por litro, rendimiento y mermas por etapa de cada lote, los lotes fuera de lo normal y tres recomendaciones con su evidencia.'),
 ('Hoja de registro por lote','Para que a partir del siguiente lote se anote lo que hoy falta, en cinco minutos por lote. En papel y en Excel.'),
 ('Sesión de lectura, 1 hora','Leemos juntos el informe con quien lleve la producción y la administración, y acordamos qué cambiar primero.')]
if completo: entregables.insert(1,('Tablero con sus datos','La misma información del informe, en una página que se abre en el celular o la computadora, con sus '+str(D['lotes'])+' lotes. Privado: solo lo ve quien ustedes digan.'))
filas=''.join(f'<tr><td><b>{t}</b></td><td>{d}</td></tr>' for t,d in entregables)
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Propuesta · {D['cliente']}</title>
<style>
@font-face{{font-family:"Space Grotesk";src:url("file://{FD}/SpaceGrotesk[wght].ttf");font-weight:300 700}}
@page{{size:letter;margin:0}} *{{box-sizing:border-box}}
html,body{{margin:0;background:#eee;color:{INK};font:10.5pt/1.45 "Space Grotesk",system-ui,sans-serif}}
.pag{{width:8.5in;height:11in;padding:.65in .7in .55in;background:#fff;margin:0 auto 12px;display:grid;grid-template-rows:auto 1fr auto;gap:14pt;page-break-after:always}}
@media print{{html,body{{background:#fff}} .pag{{margin:0}}}}
.cab{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid {INK};padding-bottom:8pt}} .cab .lk{{width:120pt}} .cab svg{{width:100%;height:auto;display:block}} .cab .meta{{text-align:right;font-size:8.5pt;color:{MUTED}}} .cab .meta b{{display:block;font-size:11pt;color:{INK}}}
main{{display:grid;gap:12pt;align-content:start}} h1{{font-size:19pt;line-height:1.15;margin:0;letter-spacing:-.01em}} h2{{font-size:11pt;margin:0 0 3pt}} h3{{font-size:8.5pt;margin:0;color:{MUTED};text-transform:uppercase;letter-spacing:.06em;font-weight:500}} p{{margin:0;max-width:66ch}}
.cita{{border-left:3px solid {IND};padding:4pt 10pt;font-size:11.5pt;line-height:1.35;color:{INK}}} .cita small{{display:block;font-size:8.5pt;color:{MUTED};margin-top:3pt}}
table{{border-collapse:collapse;width:100%;font-size:9.5pt}} td,th{{padding:6pt 8pt;border-bottom:1px solid {LINE};vertical-align:top;text-align:left}} td:first-child{{width:34%}} th{{font-size:8pt;color:{MUTED};text-transform:uppercase;letter-spacing:.05em;font-weight:500}}
.dos{{display:grid;grid-template-columns:1fr 1fr;gap:14pt}} .caja{{background:{SOFT};border-radius:6pt;padding:9pt 11pt;font-size:9.5pt}} .caja b.p{{font-size:19pt;display:block;letter-spacing:-.01em;line-height:1.1}} .caja ul{{margin:4pt 0 0;padding-left:14pt}} .caja li{{margin:2pt 0}}
.pasos{{display:grid;grid-template-columns:repeat(4,1fr);gap:8pt}} .paso{{border-top:2px solid {IND};padding-top:5pt;font-size:9pt}} .paso b{{display:block;font-size:8pt;color:{MUTED};text-transform:uppercase;letter-spacing:.05em}}
.firmas{{display:grid;grid-template-columns:1fr 1fr;gap:24pt;margin-top:8pt}} .firmas div{{border-top:1px solid {INK};padding-top:4pt;font-size:8.5pt;color:{MUTED}}}
.pie{{display:flex;justify-content:space-between;align-items:center;font-size:8pt;color:{MUTED};border-top:1px solid {LINE};padding-top:6pt}} .pie .f{{width:150pt}} .pie svg{{width:100%;height:auto;display:block}}
</style></head><body>
<section class="pag">
<header class="cab"><div class="lk">{lock}</div><div class="meta"><b>{D['cliente']}</b>Propuesta · diagnóstico de producción<br>{D['fecha']} · válida {D['vigencia']}</div></header>
<main>
<div><h3>Para</h3><p>{D['contacto']}</p></div>
<h1>Que sus {D['lotes']} lotes digan cuánto cuesta cada litro y dónde se pierde producto.</h1>
<div class="cita">{D['palabras']}<small>Lo que nos dijeron en la reunión del {D['reunion']}. Esta propuesta responde a eso.</small></div>
<div><h3>Punto de partida</h3><p>Hoy el registro es: {D['registro_actual']}. Es suficiente para empezar: con kilos, litros, grado y gastos por lote se calcula el costo por litro, el rendimiento y la merma total; las mermas por etapa se estiman donde falte dato y se registran a partir del siguiente lote con la hoja que incluye este trabajo.</p></div>
<div><h3>Qué entregamos</h3><table><thead><tr><th>Entregable</th><th>Qué contiene</th></tr></thead><tbody>{filas}</tbody></table></div>
<div><h3>Cómo se trabaja</h3><div class="pasos"><div class="paso"><b>Día 1</b>Recibimos los registros de los {D['lotes']} lotes, como estén.</div><div class="paso"><b>Días 2 a 4</b>Limpieza y cálculo. Les preguntamos lo que no cuadre; una llamada de 20 minutos.</div><div class="paso"><b>Días 5 a {'9' if completo else '6'}</b>Informe{' y tablero' if completo else ''}. Revisión interna.</div><div class="paso"><b>{'Día 10' if completo else 'Día 7'}</b>Sesión de lectura y entrega. Cierre.</div></div></div>
</main>
<footer class="pie"><span>Página 1 de 2 · confidencial</span><div class="f">{firma}</div></footer>
</section>
<section class="pag">
<header class="cab"><div class="lk">{lock}</div><div class="meta"><b>{D['cliente']}</b>Inversión, condiciones y aceptación</div></header>
<main>
<div class="dos">
<div class="caja"><h3>Inversión</h3><b class="p">{precio} MXN</b><span>{'Diagnóstico + tablero + sesión' if completo else 'Diagnóstico + hoja de registro + sesión'} · {plazo} · IVA incluido</span><ul><li>50 % al aceptar, 50 % a la entrega.</li><li>Garantía: si el diagnóstico no encuentra una pérdida evitable mayor a la inversión, se cobra la mitad.</li></ul></div>
<div class="caja"><h3>Lo que necesitamos de ustedes</h3><ul><li>Registros de los últimos {D['lotes']} lotes: kilos de agave, litros, grado y gastos. Foto de la libreta o archivo, como estén.</li><li>Mermas por etapa si las anotan; si no, no pasa nada.</li><li>Ventas por canal del mismo periodo, solo si quieren ver margen.</li><li>Una persona de contacto para dudas, 20 minutos en toda la semana.</li></ul></div>
</div>
<div><h3>Después, si lo quieren</h3><p>Actualización mensual del tablero con los lotes nuevos por $3,000 MXN al mes, sin permanencia. {'' if not completo else 'Si usan o llegan a usar un sistema de registro, el tablero se conecta a él y se actualiza solo.'} No se vende en esta propuesta; se decide en la sesión de lectura, con el informe en la mesa.</p></div>
<div><h3>Condiciones</h3><p>Los datos son de {D['cliente']} y no se comparten con nadie; el tablero es privado y se borra cuando lo pidan. El informe puede citarse como caso de éxito solo con su autorización por escrito. Esta propuesta es válida {D['vigencia']} a partir de la fecha de arriba.</p></div>
<div><h3>Aceptación</h3><p>Para empezar basta responder a este correo o mensaje con «de acuerdo» y la fecha en que enviarán los registros. Si prefieren firma:</p>
<div class="firmas"><div>Por {D['cliente']}<br>Nombre, cargo y fecha</div><div>Por CLNDA Studio<br>Kevin · Oaxaca</div></div></div>
</main>
<footer class="pie"><span>Página 2 de 2 · CLNDA Studio · hola@clnda.studio</span><div class="f">{firma}</div></footer>
</section>
</body></html>'''
open('propuesta.html','w').write(html); print('ok')
