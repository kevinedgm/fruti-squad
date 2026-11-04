# Kiwi · Cita confirmada · r01 · R1 F2. Uso: python3 gen.py → index.html (kit enlazado) y publicar.html (kit en línea)
# Datos de ejemplo: paciente, celular y enlace ficticios.
import os
D = os.path.dirname(os.path.abspath(__file__))
KIT = open(os.path.join(D, 'vendor', 'wireframe-kit.css')).read()
LOCAL = r'''
.top{display:flex;align-items:center;gap:8px;padding:10px 16px;border-bottom:1px solid var(--wf-g3)}.top .sp{flex:1}.top .logo{font-weight:800}
.cc{display:grid;gap:18px;padding:20px 16px 32px}
.ok{display:grid;gap:10px;justify-items:start}.ok .ic{width:52px;height:52px;border-radius:50%;border:2px solid var(--wf-g9);display:grid;place-items:center;font-size:24px;font-weight:800}
.ok h1{margin:0;font-size:28px;line-height:1.1}.ok p{margin:0}
.res{border:1.5px solid var(--wf-g9);border-radius:18px;padding:16px;display:grid;gap:12px}
.res .cuando{font-size:20px;font-weight:800;line-height:1.2}.res .fila{display:grid;grid-template-columns:24px minmax(0,1fr);gap:8px;align-items:start}.res .fila i{font-style:normal;text-align:center}
.res small{display:block;color:var(--wf-g6);font-size:14px}
.acc{display:flex;flex-wrap:wrap;gap:8px}
.msg{border:1px solid var(--wf-g3);border-radius:16px;padding:14px;display:grid;gap:8px;background:var(--wf-g1)}
.burbuja{background:var(--wf-g0);border:1px solid var(--wf-g4);border-radius:16px 16px 16px 4px;padding:12px;font-size:14px;line-height:1.45;max-width:340px}
.burbuja b{display:block;margin-bottom:4px}.cuenta{font-size:12px;color:var(--wf-g6)}
.mas{display:grid;gap:10px}.mas p{margin:0}
.cols{display:grid;gap:18px}
@container wf (min-width:600px){.cc,.top{padding-left:32px;padding-right:32px}}
@container wf (min-width:1024px){.cc,.top{padding-left:64px;padding-right:64px}.cols{grid-template-columns:minmax(0,1fr) 380px;grid-template-areas:'res msg' 'mas msg';gap:18px 40px;align-items:start}.a-res{grid-area:res}.a-msg{grid-area:msg}.a-mas{grid-area:mas}.ok h1{font-size:36px}}
'''
BODY = r'''<div class="wf-ctl" role="region" aria-label="Controles del wireframe">
  <span class="wf-brand"><svg viewBox="0 0 64 64" fill="none" aria-hidden="true"><rect x="4" y="4" width="56" height="56" rx="12" stroke="#ffffff" stroke-width="3.5"/><rect x="13" y="13" width="38" height="38" rx="9" stroke="#ffffff" stroke-width="3.5"/><rect x="21" y="21" width="22" height="22" rx="6" stroke="#ffffff" stroke-width="3.5"/><circle cx="32" cy="32" r="5.5" fill="#34e0a1"/></svg><span>Kiwi<small>Fruti Squad</small></span></span>
  <strong>Cita confirmada · r01 · F2</strong>
  <fieldset><legend>Espacio</legend><button data-w="1440" aria-pressed="false">expanded 1440</button><button data-w="834" aria-pressed="false">medium 834</button><button data-w="393" aria-pressed="true">compact 393</button></fieldset>
  <label>Estado <select id="wf-state" data-wf-states>
    <option value="default">Confirmada · mensaje enviado (vacío: no aplica, no hay listas)</option><option value="error">Error: no pudimos enviar el mensaje</option><option value="pendiente">Pendiente de que el médico acepte [incógnita]</option><option value="recordatorio">Mensaje: recordatorio del día anterior</option></select></label>
  <label><input type="checkbox" id="wf-notes" checked> Notas</label>
</div>
<div class="wf-stage"><p class="wf-frame-label" id="wf-label"></p><div class="wf-frame" id="wf-frame"><div id="wf-banner"></div><main id="wf-view" tabindex="-1"></main></div></div>'''
JS = r'''
let S = {w:393, st:'default'};
const N = t => `<span class="wf-note">${t}</span>`;
const SMS1 = 'Manik: Cita confirmada con Dr. Mario Díaz Soto, mié 4 nov 17:00, Hospital NeoDemo Xalapa. Cambiar o cancelar: mnk.example/c/7KQ2';
const SMS2 = 'Manik: Mañana 17:00 tienes cita con Dr. Mario Díaz Soto en Hospital NeoDemo Xalapa. Cambiar o cancelar: mnk.example/c/7KQ2';
function view(){
  const st = S.st, pend = st==='pendiente';
  const top = `<header class="top"><span class="logo">manik</span><span class="sp"></span></header>`;
  const ok = pend
    ? `<div class="ok" role="status"><span class="ic" aria-hidden="true">…</span><h1 id="h1">Tu cita está apartada</h1><p>El consultorio la confirma en las próximas horas. Te avisamos por mensaje al <b>222 555 0100</b>.</p>${N('Solo si el médico debe aceptar cada cita [incógnita 2]. El horario queda apartado para que nadie más lo tome. Sin «confirmada» hasta que lo esté: el paciente no debe llegar a una cita que no existe.')}</div>`
    : `<div class="ok" role="status"><span class="ic" aria-hidden="true">✓</span><h1 id="h1">Tu cita está confirmada</h1><p>Ana, te esperan el miércoles a las 17:00.</p>${N('El foco llega a este título al cargar (lector de pantalla lo anuncia). Se saluda con el nombre de pila que escribió: confirma que la cita quedó a su nombre.')}</div>`;
  const res = `<section class="res" aria-labelledby="h-res"><h2 id="h-res" class="wf-sr">Detalle de la cita</h2><span class="cuando">Miércoles 4 de noviembre, 17:00</span>
   <span class="fila"><i aria-hidden="true">◉</i><span><b>Dr. Mario Díaz Soto</b><small>Gastroenterología y Nutrición Pediátrica</small></span></span>
   <span class="fila"><i aria-hidden="true">⌖</i><span><b>Hospital NeoDemo Xalapa</b><small>Carretera Xalapa-Veracruz #1960, Xalapa, Veracruz</small></span></span>
   <span class="fila"><i aria-hidden="true">$</i><span><b>$800</b><small>Pagas en el consultorio</small></span></span>
   <span class="fila"><i aria-hidden="true">☺</i><span><b>Paciente: Ana Pérez</b><small>Celular 222 555 0100</small></span></span>
   <div class="acc">${pend?'':'<a class="wf-btn wf-btn--primary" href="#">Agregar a mi calendario</a>'}<a class="wf-btn" href="#">Cómo llegar</a></div>
   ${N('Día de la semana + fecha + hora completos: «miércoles 4 de noviembre», nunca «4/11» (en México y EUA se leen distinto). Acción principal: agregar al calendario (archivo .ics o enlace a Google/Apple): es lo que evita olvidar la cita. «Cómo llegar» abre el mapa.')}</section>`;
  let msg;
  if (st==='error') msg = `<section class="msg" aria-labelledby="h-msg"><h2 id="h-msg" style="margin:0;font-size:16px">No pudimos enviarte el mensaje</h2><p style="margin:0" role="alert">Tu cita sí está confirmada. Revisa que tu celular sea correcto: <b>222 555 0100</b>.</p><div class="acc"><a class="wf-btn" href="#">Reintentar envío</a><a class="wf-btn wf-btn--quiet" href="#">Corregir celular</a></div>${N('La cita no se pierde por un fallo del mensaje; se dice primero. Sin el mensaje no hay enlace para cambiar o cancelar: por eso se pide guardar la cita en el calendario y se ofrece reintentar.')}</section>`;
  else if (st==='recordatorio') msg = `<section class="msg" aria-labelledby="h-msg"><h2 id="h-msg" style="margin:0;font-size:16px">Recordatorio (un día antes)</h2><p class="burbuja">${SMS2}</p><span class="cuenta">${SMS2.length} caracteres · SMS con acentos: 2 tramos de 70</span>${N('Se envía el día anterior. Mismo enlace que la confirmación.')}</section>`;
  else msg = `<section class="msg" aria-labelledby="h-msg"><h2 id="h-msg" style="margin:0;font-size:16px">Te enviamos la confirmación</h2><p style="margin:0">Por mensaje al <b>222 555 0100</b>. Ahí está el enlace para cambiar o cancelar tu cita.</p><p class="burbuja"><b>Vista del mensaje</b>${SMS1}</p><span class="cuenta">${SMS1.length} caracteres · SMS con acentos: 2 tramos de 70</span><a class="wf-btn wf-btn--quiet" href="#" style="justify-self:start">¿No te llegó? Reenviar</a>${N('Sin cuenta, el enlace del mensaje es la única puerta a la cita: abre «Detalle de su cita» sin iniciar sesión. Canal SMS o WhatsApp [incógnita 1]. En SMS, cada acento hace que se cobre por tramos de 70 caracteres: el texto va corto y sin dirección completa. «Reenviar» se habilita a los 60 s.')}</section>`;
  const mas = `<section class="mas" aria-labelledby="h-mas"><h2 id="h-mas" style="margin:0;font-size:17px">¿Necesitas algo más?</h2>
   <div class="acc"><a class="wf-btn wf-btn--quiet" href="#">Cambiar o cancelar</a><a class="wf-btn wf-btn--quiet" href="#">Llamar al consultorio · 228 555 0142</a><a class="wf-btn wf-btn--quiet" href="#">Volver al inicio</a></div>
   ${N('Cambiar o cancelar está aquí también (misma sesión), pero sin peso: la mayoría no lo necesita. Cancelar pedirá confirmación en la pantalla siguiente (destructivo). Plazo para cancelar [incógnita 3].')}</section>`;
  return top + `<div class="cc">${ok}<div class="cols"><div class="a-res">${res}</div><div class="a-msg">${msg}</div><div class="a-mas">${mas}</div></div></div>`;
}
function render(){
  const f=document.getElementById('wf-frame'), L=document.getElementById('wf-label');
  f.style.setProperty('--wf-w', S.w+'px'); L.style.setProperty('--wf-w', S.w+'px');
  L.textContent=`Marco ${S.w}px · ${S.w<600?'compact':S.w<1024?'medium':'expanded'} (referencia declarada)`;
  document.querySelectorAll('[data-w]').forEach(b=>b.setAttribute('aria-pressed', String(+b.dataset.w===S.w)));
  document.getElementById('wf-view').innerHTML = view();
}
document.addEventListener('click', e=>{const w=e.target.closest('[data-w]'); if(w){S.w=+w.dataset.w; render();}});
document.getElementById('wf-state').addEventListener('change', e=>{S.st=e.target.value; render();});
document.getElementById('wf-notes').addEventListener('change', e=>document.body.classList.toggle('wf-no-notes', !e.target.checked));
render();
'''
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&display=swap" rel="stylesheet"><!-- solo chrome -->'
open(os.path.join(D, 'index.html'), 'w').write(f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="wf-fidelidad" content="F2">
<title>Wireframe · Cita confirmada · r01</title>
{FONTS}
<link rel="stylesheet" href="vendor/wireframe-kit.css">
<style>{LOCAL}</style>
</head>
<body class="wf">
{BODY}
<script>{JS}</script>
</body>
</html>''')
open(os.path.join(D, 'publicar.html'), 'w').write(f'''<title>Cita confirmada · wireframe</title>
<meta name="claude:viewport-fit-sides" content="cover">
{FONTS}
<style>{KIT}{LOCAL}
.wf-ctl,.wf-stage{{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}</style>
<script>document.documentElement.lang='es'</script>
{BODY}
<script>document.body.classList.add('wf');{JS}</script>
''')
print('ok')
