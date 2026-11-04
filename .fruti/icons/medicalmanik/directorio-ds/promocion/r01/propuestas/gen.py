# Kiwi · Promociones de Impulsa · r01 · R1 F2. Uso: python3 gen.py → index.html (kit enlazado) y publicar.html (kit en línea)
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
LOCAL += r"""
.lista{display:grid;gap:12px}
.fm{border:1px solid var(--wf-g3);border-radius:18px;padding:12px;display:grid;grid-template-columns:56px minmax(0,1fr) auto;gap:4px 12px;align-items:center}
.fm .av{width:56px;aspect-ratio:3/4;border-radius:10px;background:var(--wf-g2);grid-row:1/4}.fm small{color:var(--wf-g6);font-size:13px}.fm .wf-btn{grid-row:1/4;grid-column:3}
.promo{border:2px dashed var(--wf-g7);border-radius:18px;overflow:hidden;display:grid;background:var(--wf-g1);text-decoration:none;color:inherit}
.promo .img{aspect-ratio:2/1;background:repeating-linear-gradient(45deg,var(--wf-g3) 0 10px,var(--wf-g2) 10px 20px);display:grid;place-items:center;font-size:12px;color:var(--wf-g7)}
.promo .tx{padding:12px 14px;display:grid;gap:4px}.promo .tx b{font-size:17px;line-height:1.25}.promo .tx small{color:var(--wf-g6);font-size:13px}
.etq{justify-self:start;font-size:12px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;border:1.5px solid var(--wf-g9);border-radius:999px;padding:2px 10px;background:var(--wf-g0)}
.promo.sin .img{display:none}
.pp .ban{aspect-ratio:2/1;border-radius:18px;background:repeating-linear-gradient(45deg,var(--wf-g3) 0 10px,var(--wf-g2) 10px 20px);display:grid;place-items:center;font-size:13px;color:var(--wf-g7)}
.pp h1{margin:0;font-size:26px;line-height:1.15}.dato{display:grid;grid-template-columns:auto 1fr;gap:6px 14px;font-size:15px}.dato dt{color:var(--wf-g6)}.dato dd{margin:0;font-weight:700}
.anun{border:1.5px solid var(--wf-g9);border-radius:16px;padding:12px;display:grid;grid-template-columns:48px minmax(0,1fr);gap:4px 12px;align-items:center}.anun .av{width:48px;aspect-ratio:3/4;border-radius:8px;background:var(--wf-g2);grid-row:1/3}
@container wf (min-width:600px){.lista{grid-template-columns:repeat(2,minmax(0,1fr))}.lista .promo{grid-column:1/-1;grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.lista .promo .img{aspect-ratio:auto;min-height:150px}.lista .promo.sin{grid-template-columns:1fr}}
@container wf (min-width:1024px){.ppc{grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:40px;align-items:start}}
"""
BODY = r"""<div class="wf-ctl" role="region" aria-label="Controles del wireframe">
  <span class="wf-brand"><svg viewBox="0 0 64 64" fill="none" aria-hidden="true"><rect x="4" y="4" width="56" height="56" rx="12" stroke="#ffffff" stroke-width="3.5"/><rect x="13" y="13" width="38" height="38" rx="9" stroke="#ffffff" stroke-width="3.5"/><rect x="21" y="21" width="22" height="22" rx="6" stroke="#ffffff" stroke-width="3.5"/><circle cx="32" cy="32" r="5.5" fill="#34e0a1"/></svg><span>Kiwi<small>Fruti Squad</small></span></span>
  <strong>Promociones de Impulsa · r01 · F2</strong>
  <fieldset><legend>Espacio</legend><button data-w="1440" aria-pressed="false">expanded 1440</button><button data-w="834" aria-pressed="false">medium 834</button><button data-w="393" aria-pressed="true">compact 393</button></fieldset>
  <label>Estado <select id="wf-state" data-wf-states>
    <option value="default">Resultados con una promoción</option><option value="sinimg">Promoción sin imagen</option><option value="carga">Carga de resultados</option><option value="error">Error: no carga la promoción</option><option value="pagina">Página de la promoción</option><option value="fuera">Página: anunciante fuera del directorio</option><option value="vencida">Página: promoción vencida (vacío)</option></select></label>
  <label><input type="checkbox" id="wf-notes" checked> Notas</label>
</div>
<div class="wf-stage"><p class="wf-frame-label" id="wf-label"></p><div class="wf-frame" id="wf-frame"><div id="wf-banner"></div><main id="wf-view" tabindex="-1"></main></div></div>"""
JS = r"""
let S = {w:393, st:'default'};
const N = t => `<span class="wf-note">${t}</span>`;
const F = (n, d) => `<div class="fm"><span class="av"></span><b>${n}</b><small>${d}</small><small>Céd. Prof. 0000000</small><a class="wf-btn" href="#">Agendar</a></div>`;
const PROMO = (sin) => `<a class="promo${sin?' sin':''}" href="#" aria-label="Patrocinado: Clínica Dermalia. Revisión de lunares a $650. Ver promoción"><span class="img">Banner de Impulsa · recorte 2:1</span><span class="tx"><span class="etq">Patrocinado</span><b>Revisión de lunares a $650</b><small>Clínica Dermalia · hasta el 30 de noviembre</small></span></a>`;
function view(){
  const st = S.st;
  const top = `<header class="top"><span class="logo">manik</span><span class="sp"></span><a class="wf-btn wf-btn--quiet" href="#">← Inicio</a></header>`;
  if (st==='error') return top + `<div class="cc"><h1 style="margin:0;font-size:24px">Dermatólogas cerca de ti</h1><p class="wf-muted" style="margin:0">12 especialistas · Angelópolis, Puebla</p><div class="lista">${F('Dra. Mariana Soto','Dermatóloga · 1.8 km · $900')}${F('Dr. Iván Hernández','Dermatólogo · 4.0 km · $700')}${F('Dra. Carla Luna','Dermatóloga · 2.2 km · $1,100')}</div>${N('Si la promoción no carga, los resultados salen igual, sin hueco y sin mensaje de error: el paciente no pidió la promoción.')}</div>`;
  if (['default','sinimg','carga'].includes(st)) {
    const lista = st==='carga' ? `<div class="lista wf-skel" aria-busy="true">${'<div class="fm"><span class="av"></span><div class="wf-line" style="width:70%"></div><div class="wf-line" style="width:50%"></div></div>'.repeat(3)}</div>${N('La promoción se carga junto con los resultados: nunca aparece después y empuja la lista.')}`
      : `<div class="lista">${F('Dra. Mariana Soto','Dermatóloga · 1.8 km · $900')}${F('Dr. Iván Hernández','Dermatólogo · 4.0 km · $700')}${PROMO(st==='sinimg')}${F('Dra. Carla Luna','Dermatóloga · 2.2 km · $1,100')}${F('Dra. Fernanda Quiroz','Dermatóloga · 3.1 km · $750')}</div>
      ${N(st==='sinimg' ? 'Sin imagen: la tarjeta queda solo con «Patrocinado», título y anunciante. Nunca un hueco gris.' : 'Posición: después del 2.º resultado, nunca primera; máximo 1 cada 5 resultados; nunca 2 seguidas; solo de la especialidad o zona buscada. «Patrocinado» va primero y como texto (también en el nombre accesible). Borde y ancho completo distintos de la ficha: no se confunde con un médico. Toda la tarjeta es un enlace a la página de la promoción.')}
      ${N('La imagen se recorta a 2:1 en celular y va a la izquierda en tableta y escritorio; el título es texto real, no se lee de la imagen [incógnita 1: formato del banner de Impulsa]. No dice «Impulsa» ni usa su violeta: el paciente no conoce la herramienta.')}`;
    return top + `<div class="cc"><h1 style="margin:0;font-size:24px">Dermatólogas cerca de ti</h1><p class="wf-muted" style="margin:0">12 especialistas · Angelópolis, Puebla</p>${lista}</div>`;
  }
  if (st==='vencida') return top + `<div class="cc"><div class="ok"><span class="etq">Patrocinado</span><h1 id="h1">Esta promoción ya terminó</h1><p>Terminó el 30 de noviembre. Clínica Dermalia sigue en Manik.</p></div><div class="acc"><a class="wf-btn wf-btn--primary" href="#">Ver Clínica Dermalia</a><a class="wf-btn wf-btn--quiet" href="#">Volver a los resultados</a></div>${N('Vacío: el enlace puede llegar compartido después de la vigencia. No se muestra el precio vencido; se ofrece seguir con el anunciante.')}</div>`;
  const fuera = st==='fuera';
  const anun = fuera
    ? `<div class="anun"><span class="av"></span><b>Laboratorio Ejemplo</b><span class="wf-muted wf-small">No agenda en Manik · Teléfono 222 555 0190</span></div>`
    : `<div class="anun"><span class="av"></span><b>Clínica Dermalia · Dra. Mariana Soto</b><span class="wf-muted wf-small">Dermatóloga · Céd. Prof. 0000000 · Angelópolis</span></div>`;
  const cta = fuera ? `<a class="wf-btn wf-btn--primary" href="#">Llamar · 222 555 0190</a>` : `<a class="wf-btn wf-btn--primary" href="#">Agendar con esta promoción</a><a class="wf-btn wf-btn--quiet" href="#">Ver perfil</a>`;
  return top + `<div class="cc pp"><a class="wf-btn wf-btn--quiet" href="#" style="justify-self:start">← Resultados</a><div class="ppc" style="display:grid;gap:16px">
   <div style="display:grid;gap:14px"><span class="ban">Banner de Impulsa · completo</span>${N('Aquí el banner se muestra completo (sin recorte): es su página.')}</div>
   <div style="display:grid;gap:14px"><span class="etq">Patrocinado</span><h1 id="h1">Revisión de lunares a $650</h1>
   <p style="margin:0">Revisión completa de lunares con dermatoscopio. Incluye una consulta de seguimiento si hace falta.</p>
   <dl class="dato"><dt>Precio</dt><dd>$650 (normal $900)</dd><dt>Vigencia</dt><dd>Hasta el 30 de noviembre</dd><dt>Dónde</dt><dd>Angelópolis, Puebla</dd><dt>Condiciones</dt><dd>Primera vez · pago en el consultorio</dd></dl>
   ${anun}<div class="acc">${cta}</div>
   ${N(fuera ? 'Anunciante que no está en el directorio (laboratorio, farmacia): no hay perfil ni agenda; la acción es llamar [incógnita 4].' : '«Agendar con esta promoción» abre la agenda del anunciante con la promoción aplicada (el consultorio la ve en la cita). Anunciante con nombre y cédula: la confianza no la da Manik, la da el médico.')}
   ${N('Aviso legal de publicidad en salud (número de permiso o aviso COFEPRIS), si aplica, va al pie de esta página [incógnita 3, no verificada].')}</div></div></div>`;
}
"""
JS += r"""
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
"""
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&display=swap" rel="stylesheet"><!-- solo chrome -->'
open(os.path.join(D, 'index.html'), 'w').write(f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="wf-fidelidad" content="F2">
<title>Wireframe · Promociones · r01</title>
{FONTS}
<link rel="stylesheet" href="vendor/wireframe-kit.css">
<style>{LOCAL}</style>
</head>
<body class="wf">
{BODY}
<script>{JS}</script>
</body>
</html>''')
open(os.path.join(D, 'publicar.html'), 'w').write(f'''<title>Promociones · wireframe</title>
<meta name="claude:viewport-fit-sides" content="cover">
{FONTS}
<style>{KIT}{LOCAL}
.wf-ctl,.wf-stage{{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}</style>
<script>document.documentElement.lang='es'</script>
{BODY}
<script>document.body.classList.add('wf');{JS}</script>
''')
print('ok')
