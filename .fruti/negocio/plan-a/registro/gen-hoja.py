# Plan A · hoja de registro por lote (carta, 1 página, para llenar a mano). Uso: python gen-hoja.py <carpeta de fuentes>
import sys; FD=sys.argv[1]
INK='#0e0f1c'; IND='#4338ca'; MUTED='#5a5c72'; LINE='#c9cad6'; SOFT='#f4f4fa'
lock=open('/home/user/fruti-squad/.fruti/icons/clnda/final/svg/lockup.svg').read(); firma=open('/home/user/fruti-squad/.fruti/icons/clnda/final/svg/firma.svg').read()
def campo(lbl,w='1fr',unit=''): return f'<div class="c" style="grid-column:span {w}"><span>{lbl}{(" · "+unit) if unit else ""}</span><i></i></div>'
def fila(*cs): return '<div class="f">'+''.join(cs)+'</div>'
def bloque(num,titulo,nota,cuerpo): return f'<section class="b"><header><b>{num}</b><h2>{titulo}</h2><p>{nota}</p></header>{cuerpo}</section>'
tina=''.join(f'<tr><td>{i}</td><td></td><td></td><td></td></tr>' for i in range(1,11))
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Hoja de registro por lote</title>
<style>
@font-face{{font-family:"Space Grotesk";src:url("file://{FD}/SpaceGrotesk[wght].ttf");font-weight:300 700}}
@page{{size:letter;margin:0}} *{{box-sizing:border-box}}
html,body{{margin:0;background:#eee;color:{INK};font:9pt/1.3 "Space Grotesk",system-ui,sans-serif}}
.pag{{width:8.5in;height:11in;padding:.45in .5in .4in;background:#fff;margin:0 auto;display:grid;grid-template-rows:auto 1fr auto;gap:7pt}}
@media print{{html,body{{background:#fff}}}}
.cab{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid {INK};padding-bottom:5pt}} .cab .lk{{width:95pt}} .cab svg{{width:100%;height:auto;display:block}} .cab h1{{margin:0;font-size:15pt;font-weight:700;letter-spacing:-.01em}} .cab p{{margin:0;font-size:8pt;color:{MUTED}}}
main{{display:grid;grid-template-columns:1fr 1fr;gap:7pt;align-content:start}}
.b{{border:1px solid {LINE};border-radius:5pt;padding:6pt 7pt;display:grid;gap:5pt;align-content:start}} .b.w{{grid-column:1/-1}}
.b header{{display:grid;grid-template-columns:14pt 1fr;gap:4pt;align-items:baseline}} .b header b{{color:{IND};font-size:12pt}} .b h2{{margin:0;font-size:10pt;font-weight:700}} .b header p{{grid-column:2;margin:0;font-size:7.5pt;color:{MUTED}}}
.f{{display:grid;grid-template-columns:repeat(6,1fr);gap:5pt}} .c{{display:grid;gap:2pt}} .c span{{font-size:7pt;color:{MUTED};text-transform:uppercase;letter-spacing:.04em}} .c i{{display:block;height:15pt;border-bottom:1px solid {INK}}}
table{{border-collapse:collapse;width:100%;font-size:8pt}} th,td{{border:1px solid {LINE};padding:2.5pt 4pt;text-align:left;height:14pt}} th{{background:{SOFT};font-weight:500;color:{MUTED};font-size:7pt;text-transform:uppercase;letter-spacing:.04em}}
.obs i{{height:40pt;border:1px solid {LINE};border-radius:3pt}}
.calc{{background:{SOFT};border-radius:4pt;padding:5pt 7pt;font-size:7.5pt;color:{MUTED}}} .calc b{{color:{INK}}}
.pie{{display:flex;justify-content:space-between;align-items:center;font-size:7.5pt;color:{MUTED};border-top:1px solid {LINE};padding-top:4pt}} .pie .fm{{width:120pt}} .pie svg{{width:100%;height:auto;display:block}}
</style></head><body><section class="pag">
<header class="cab"><div><h1>Hoja de registro por lote</h1><p>Una hoja por lote, cinco minutos. Lo que no se anota no se puede mejorar.</p></div><div class="lk">{lock}</div></header>
<main>
{bloque(1,'El lote','Identificación y agave.',fila(campo('Lote (número)',2),campo('Fecha de inicio',2),campo('Fecha de fin',2))+fila(campo('Tipo de agave',2),campo('Origen / parcela',2),campo('Edad',1,'años'),campo('Piñas',1,'núm.')))}
{bloque(2,'Horneado','Pesar al entrar y al salir del horno: la diferencia es la merma de horneado.',fila(campo('Agave al entrar',2,'kg'),campo('Agave cocido al salir',2,'kg'),campo('Horas de horneado',1,'h'),campo('Días tapado',1))+fila(campo('Leña usada',2,'cargas o $'),campo('Temperatura de piedra',2,'°C si se mide'),campo('Fecha de encendido',2)))}
{bloque(3,'Molienda','Litros de jugo y kilos de bagazo: lo que se queda en el bagazo es merma de molienda.',fila(campo('Tahona o molino',2),campo('Jugo obtenido',2,'L'),campo('Bagazo húmedo',2,'kg'))+fila(campo('Agua añadida',2,'L'),campo('Litros que entran a tina',2,'L'),campo('Fecha',2)))}
{bloque(4,'Destilación','Litros y grado por corte, en cada destilación. Cabeza y cola son merma de destilación.',
 '<table><thead><tr><th>Destilación</th><th>Cabeza L / °</th><th>Cuerpo L / °</th><th>Cola L / °</th><th>Fecha</th></tr></thead><tbody><tr><td>Primera (común)</td><td></td><td></td><td></td><td></td></tr><tr><td>Segunda (rectificación)</td><td></td><td></td><td></td><td></td></tr><tr><td>Tercera (si aplica)</td><td></td><td></td><td></td><td></td></tr></tbody></table>'+fila(campo('Mezcal final',2,'L'),campo('Grado final',2,'% vol'),campo('Ajuste con agua',2,'L')))}
{bloque(5,'Fermentación','Una línea por día: temperatura del mosto, grados Brix si se miden, y qué se observó (espuma, olor, lluvia).',
 '<table><thead><tr><th style="width:9%">Día</th><th style="width:22%">Temp. °C</th><th style="width:22%">Brix / densidad</th><th>Observación</th></tr></thead><tbody>'+tina+'</tbody></table>'+fila(campo('Tina (número o material)',2),campo('Litros al llenar',2,'L'),campo('Litros al vaciar',2,'L')))}
<section class="b"><header><b>6</b><h2>Costos del lote</h2><p>Todo lo que se gastó en este lote, aunque se haya pagado después.</p></header>
{fila(campo('Agave',3,'$'),campo('Leña',3,'$'))}{fila(campo('Jornales',3,'$'),campo('Otros (agua, gas, transporte)',3,'$'))}{fila(campo('Total del lote',3,'$'),campo('Precio de venta esperado',3,'$ por L'))}
<div class="c obs"><span>Observaciones del lote</span><i></i></div>
<div class="calc"><b>Para calcular después:</b> rendimiento = kg de agave ÷ litros finales · merma de horneado = 1 − cocido ÷ entrada · merma de fermentación = 1 − litros al vaciar ÷ litros al llenar · merma de destilación = (cabeza + cola) ÷ (cabeza + cuerpo + cola) · costo por litro = total ÷ litros finales.</div></section>
</main>
<footer class="pie"><span>Registro de producción · quien llena: ____________________ · firma del maestro: ____________________</span><div class="fm">{firma}</div></footer>
</section></body></html>'''
open('hoja-registro.html','w').write(html); print('ok')
