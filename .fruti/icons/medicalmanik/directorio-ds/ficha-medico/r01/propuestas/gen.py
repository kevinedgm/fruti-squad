# Kiwi · FichaMedico (directorio Manik) · r01 · R2 F2. Uso: python3 gen.py → index.html (kit enlazado) y publicar.html (kit en línea, para el artifact)
import os
D = os.path.dirname(os.path.abspath(__file__))
KIT = open(os.path.join(D, 'vendor', 'wireframe-kit.css')).read()
LOCAL = r'''
/* Composición local de la ronda (solo grises del kit) */
.fl{display:grid;gap:12px;grid-template-columns:1fr;align-items:start;container:lista/inline-size}
@container wf (min-width:600px){.fl{grid-template-columns:repeat(2,minmax(0,1fr))}}
.res-h{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:8px;margin-bottom:12px}
.res-h h1{font-size:24px;margin:0}
.fbar{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 16px}
.fbar .wf-btn{min-height:40px}
.fx{container:ficha/inline-size;min-width:0}
.fc{border:1px solid var(--wf-g3);border-radius:var(--wf-r-card);padding:14px;background:var(--wf-g0);display:grid;gap:10px;min-width:0}
.av{width:64px;aspect-ratio:3/4;border-radius:10px;background:repeating-linear-gradient(45deg,var(--wf-g2) 0 6px,var(--wf-g1) 6px 12px);display:grid;place-items:end center;font-size:10px;color:var(--wf-g6);padding-bottom:3px;flex:none;text-align:center;line-height:1.1}
.av.sm{width:44px;font-size:0}
.idr{display:flex;gap:12px;align-items:start;min-width:0}
.idr>div{min-width:0;display:grid;gap:2px}
.nm{font-weight:700;font-size:17px;line-height:1.25;overflow-wrap:anywhere}
.sp{font-size:14px;color:var(--wf-g6)}
.cf{font-size:13px;display:flex;flex-wrap:wrap;gap:4px 10px}
.cf b{font-weight:600}
.box{border:1px solid var(--wf-g4);border-radius:10px;padding:10px 12px;display:grid;gap:6px}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap}
.pr{font-weight:700;font-size:17px;white-space:nowrap}.pr small{font-weight:400;font-size:12px;color:var(--wf-g6);margin-right:4px}
.lu{font-weight:600;font-size:14px}
.when{font-size:14px}.when b{font-weight:700}
.sl{display:flex;flex-wrap:wrap;gap:6px}.sl button{min-height:40px;min-width:64px;border:1px solid var(--wf-g9);border-radius:999px;background:var(--wf-g0);font-weight:600;font-variant-numeric:tabular-nums}
.sl button[aria-pressed=true]{background:var(--wf-g8);color:var(--wf-g0)}
.sl .mas{border:0;text-decoration:underline;min-width:0;font-weight:500}
.ac{display:flex;gap:8px;flex-wrap:wrap}.ac .wf-btn{flex:1 1 140px}
.tel{font-size:20px;font-weight:700;font-variant-numeric:tabular-nums;letter-spacing:.02em}
.lk{font-size:13px;text-decoration:underline;background:none;border:0;padding:4px 0;min-height:32px;text-align:left}
.big{font-size:22px;font-weight:800;line-height:1.1}
.cr{display:grid;gap:0;border:1px solid var(--wf-g3);border-radius:10px}
.cr>div{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 10px;padding:10px 12px;align-items:center}
.cr>div+div{border-top:1px solid var(--wf-g3)}
.cr .md{font-size:13px;color:var(--wf-g6);grid-column:1}
.cr .wf-btn{grid-row:1/3;grid-column:2;min-height:44px}
.msg{font-size:13px;border:1px dashed var(--wf-g6);border-radius:8px;padding:6px 10px}
.dis[aria-disabled=true]{border-style:dashed;background:var(--wf-g1);color:var(--wf-g6)}
@container ficha (min-width:520px){
  .fc.amplia{grid-template-columns:132px minmax(0,1fr);column-gap:18px}
  .fc.amplia>.idr .av{width:132px}
  .fc.amplia>.idr{grid-column:1/-1}
  .fc.amplia>*:not(.idr){grid-column:2}
  .fc.amplia>.idr{display:contents}
  .fc.amplia>.idr>.av{grid-row:1/span 6}
}
.side h3{margin-top:0}.side .wf-actions{flex-direction:column;align-items:stretch}
'''
BODY = r'''<div class="wf-ctl" role="region" aria-label="Controles del wireframe">
  <span class="wf-brand"><svg viewBox="0 0 64 64" fill="none" aria-hidden="true"><rect x="4" y="4" width="56" height="56" rx="12" stroke="#ffffff" stroke-width="3.5"/><rect x="13" y="13" width="38" height="38" rx="9" stroke="#ffffff" stroke-width="3.5"/><rect x="21" y="21" width="22" height="22" rx="6" stroke="#ffffff" stroke-width="3.5"/><circle cx="32" cy="32" r="5.5" fill="#34e0a1"/></svg><span>Kiwi<small>Fruti Squad</small></span></span>
  <strong>FichaMedico · r01 · F2</strong>
  <fieldset><legend>Versión</legend>
    <button data-v="actual" aria-pressed="false">Actual</button><button data-v="a" aria-pressed="true">A · Bloques</button><button data-v="b" aria-pressed="false">B · Próximo lugar</button><button data-v="c" aria-pressed="false">C · Consultorios</button>
  </fieldset>
  <fieldset><legend>Espacio</legend>
    <button data-w="1440" aria-pressed="false">expanded 1440</button><button data-w="834" aria-pressed="false">medium 834</button><button data-w="393" aria-pressed="true">compact 393</button>
  </fieldset>
  <label>Estado
    <select id="wf-state" data-wf-states>
      <option value="default">Default</option><option value="loading">Carga</option><option value="empty">Vacío por filtros</option>
      <option value="error">Error de horarios</option><option value="offline">Sin conexión</option><option value="taken">Horario ocupado</option>
      <option value="nolugar">Sin lugar en 2 semanas</option><option value="long">Contenido largo</option>
    </select>
  </label>
  <label><input type="checkbox" id="wf-notes" checked> Notas</label>
</div>
<div class="wf-stage">
  <p class="wf-frame-label" id="wf-label"></p>
  <div class="wf-frame" id="wf-frame">
    <div class="wf-shell" id="shell">
      <aside class="wf-side side" aria-label="Filtros"><h3>Filtros</h3><div class="wf-actions"><button class="wf-btn" aria-pressed="true">Cita en línea ✓</button><button class="wf-btn" aria-pressed="false">Con lugar hoy</button><button class="wf-btn" aria-pressed="false">Hasta $800</button></div><span class="wf-note">Expanded: filtros persistentes a la izquierda. Compact/medium: botón «Filtros» que abre una hoja.</span></aside>
      <div>
        <header class="wf-top"><strong>manik</strong><span class="wf-muted wf-small">Dermatóloga · Angelópolis, Puebla</span></header>
        <div id="wf-banner"></div>
        <main class="wf-main" id="wf-view" tabindex="-1"></main>
      </div>
    </div>
  </div>
  <div style="max-width:1100px;margin:24px auto 0" id="explica"></div>
</div>'''
JS = r'''
const MED = [
 {id:'soto', av:'mujer', n:'Dra. Mariana Soto', sp:'Dermatóloga · acné y lunares', ced:1, r:'4.9', op:312, cons:[
   {lu:'Angelópolis', km:'1.8', pr:'$900', modo:'linea', dia:'Hoy', hs:['16:30','17:00','18:30']},
   {lu:'Centro', km:'5.2', pr:'$700', modo:'tel', tel:'222 555 0140'}]},
 {id:'quiroz', av:'mujer', n:'Dra. Fernanda Quiroz', sp:'Dermatóloga · cosmética', ced:1, r:'4.7', op:41, cons:[
   {lu:'Centro', km:'3.1', pr:'$750', modo:'tel', tel:'222 555 0187'}]},
 {id:'hdz', av:'hombre', n:'Dr. Iván Hernández', sp:'Dermatólogo · alergias de piel', ced:1, r:null, op:0, cons:[
   {lu:'La Paz', km:'4.0', pr:'$700', modo:'linea', dia:'Lunes 3', hs:['10:00','11:00']}]},
 {id:'ramos', av:'neutra', n:'Alex Ramos Treviño', sp:'Dermatología pediátrica', ced:1, r:'4.8', op:57, cons:[
   {lu:'San Manuel', km:'2.6', pr:'$800', modo:'linea', dia:'Mañana', hs:['9:00','9:30','12:00']},
   {lu:'Zavaleta', km:'6.0', pr:'$800', modo:'linea', dia:'Jueves 6', hs:['17:00']},
   {lu:'Cholula', km:'9.4', pr:'$650', modo:'tel', tel:'222 555 0122'}]},
];
const LARGA = {id:'larga', av:'mujer', n:'Dra. María de los Ángeles Hernández-Villaseñor', sp:'Dermatóloga · dermatología oncológica y cirugía dermatológica', ced:1, r:'4.8', op:1284, cons:[
   {lu:'Torre Médica Angelópolis, piso 7', km:'12.4', pr:'$1,250', modo:'linea', dia:'Miércoles 12', hs:['8:00','8:30','13:30']},{lu:'Centro', km:'5.0', pr:'$1,100', modo:'tel', tel:'222 555 0199'}]};
let S = {w:393, v:'a', st:'default'};
const AVL = {mujer:'silueta mujer', hombre:'silueta hombre', neutra:'silueta neutra'};
const av = (m, cls='') => `<div class="av ${cls}" role="img" aria-label="Sin foto: ${m.n}">${AVL[m.av]}</div>`;
const conf = m => `<p class="cf">${m.ced?'<span>✓ <b>Cédula verificada</b></span>':''}${m.r?`<span>★ <b>${m.r}</b> · ${m.op.toLocaleString('es-MX')} opiniones</span>`:'<span class="wf-status wf-status--draft">Nuevo en Manik</span>'}</p>`;
const off = () => S.st==='offline';
function slots(c, m){
  if (off()) return `<p class="msg">Sin conexión: los horarios pueden haber cambiado.</p>`;
  if (S.st==='error' && m.id==='soto') return `<p class="msg" role="alert">No pudimos cargar los horarios. <button class="lk">Reintentar</button></p>`;
  if (S.st==='nolugar' && m.id==='soto') return `<p class="when"><b>Sin lugar en las próximas 2 semanas</b> en ${c.lu}</p><button class="lk">Centro tiene lugar mañana · ver</button>`;
  const sel = (S.st==='taken' && m.id==='soto') ? '16:30' : (m.id==='soto' ? '17:00' : null);
  const taken = (S.st==='taken' && m.id==='soto') ? `<p class="msg" role="status">Ese horario se acaba de ocupar. Elige otro.</p>` : '';
  const hs = c.hs.slice(0,3).map(h=>`<button aria-pressed="${h===sel && S.st!=='taken'}"${S.st==='taken'&&h==='16:30'?' disabled style="text-decoration:line-through;border-style:dashed"':''}>${h}</button>`).join('');
  return `<p class="when"><b>${c.dia}</b> · ${c.hs.length} horario${c.hs.length>1?'s':''}</p><div class="sl" role="group" aria-label="Horarios ${c.lu}">${hs}${c.hs.length>=3?'<button class="mas">Más horarios</button>':''}</div>${taken}`;
}
function accion(c, primary=true){
  if (c.modo==='tel') return `<p class="tel">${c.tel}</p><div class="ac"><a class="wf-btn ${primary?'wf-btn--primary':''}" href="#llamar">Llamar</a><button class="wf-btn">Copiar número</button></div>`;
  const dis = off() || (S.st==='nolugar'); 
  return `<div class="ac"><button class="wf-btn ${primary&&!dis?'wf-btn--primary':''} dis" aria-disabled="${dis}">${off()?'Agendar · requiere conexión':'Agendar'}</button></div>`;
}
const modoTxt = c => c.modo==='tel' ? 'Agenda por teléfono' : 'Agenda en línea';
const otros = m => m.cons.length>1 ? `<button class="lk">${m.cons.length} consultorios · ver los otros ${m.cons.length-1}</button>` : '';
const V = {
 actual: m => { const c=m.cons[0]; return `<article class="fc amplia">${`<div class="idr">${av(m)}<div><p class="nm">${m.n}</p><p class="sp">${m.sp}</p><p class="lu">⌖ ${c.lu} · ${c.km} km</p></div><p class="pr" style="margin-left:auto"><small>Consulta</small>${c.pr}</p></div>`}${conf(m)}${c.modo==='linea'?slots(c,m):'<p class="when"><b>Agenda por teléfono</b> · llama y pide tu cita</p>'}${accion(c)}${m.cons.length>1?`<button class="lk">Atiende en ${m.cons.length} consultorios · ver todos</button>`:''}</article>`; },
 a: m => { const c=m.cons[0]; return `<article class="fc amplia"><div class="idr">${av(m)}<div><p class="nm">${m.n}</p><p class="sp">${m.sp}</p>${conf(m)}</div></div>
   <section class="box" aria-label="Consultorio ${c.lu}"><div class="row"><span class="lu">⌖ ${c.lu} · ${c.km} km</span><span class="pr"><small>Consulta</small>${c.pr}</span></div><span class="wf-status ${c.modo==='linea'?'wf-status--on':''}">${modoTxt(c)}</span>
   ${c.modo==='linea'?slots(c,m):''}${accion(c)}${otros(m)}</section></article>`; },
 b: m => { const c=m.cons[0]; const top = c.modo==='linea' ? (off()?'<span class="big">Horarios sin conexión</span>':(S.st==='nolugar'&&m.id==='soto'?'<span class="big">Sin lugar 2 semanas</span>':`<span class="big">${c.dia} ${c.hs[0]}</span>`)) : '<span class="big">Por teléfono</span>';
   return `<article class="fc"><div class="row">${top}<span class="pr"><small>Consulta</small>${c.pr}</span></div>
   <div class="idr">${av(m,'sm')}<div><p class="nm">${m.n}</p><p class="sp">${m.sp}</p><p class="lu">⌖ ${c.lu} · ${c.km} km${m.cons.length>1?` <span class="wf-muted">+${m.cons.length-1} consultorio${m.cons.length>2?'s':''}</span>`:''}</p>${conf(m)}</div></div>
   ${c.modo==='linea'?slots(c,m):''}${accion(c)}</article>`; },
 c: m => { const rows = m.cons.slice(0,2).map((c,i)=>`<div><span class="lu">${c.lu} · ${c.km} km · ${c.pr}</span><a class="wf-btn ${i===0&&!(off()&&c.modo==='linea')?'wf-btn--primary':''}" href="#${c.modo}">${c.modo==='tel'?'Llamar':'Agendar'}</a><span class="md">${c.modo==='tel'?'Por teléfono · '+c.tel:(off()?'En línea · sin conexión':(S.st==='nolugar'&&m.id==='soto'&&i===0?'En línea · sin lugar 2 semanas':`En línea · ${c.dia} ${c.hs[0]}`))}</span></div>`).join('');
   return `<article class="fc amplia"><div class="idr">${av(m)}<div><p class="nm">${m.n}</p><p class="sp">${m.sp}</p>${conf(m)}</div></div><div class="cr" role="list" aria-label="Consultorios">${rows}</div>${m.cons.length>2?`<button class="lk">Ver ${m.cons.length-2} consultorio${m.cons.length>3?'s':''} más</button>`:''}${S.st==='taken'&&m.id==='soto'?'<p class="msg">Ese horario se acaba de ocupar. Elige otro.</p>':''}${S.st==='error'&&m.id==='soto'?'<p class="msg" role="alert">No pudimos cargar los horarios. <button class="lk">Reintentar</button></p>':''}</article>`; },
};
const NOTAS = {
 actual:'Actual (sistema v5): identidad arriba, el consultorio y el precio en la misma cabecera, luego confianza, horarios y acción. Riesgo: el precio se lee como «del médico»; «Atiende en 2 consultorios» queda al final, lejos del precio al que afecta.',
 a:'A · Bloques: arriba QUIÉN (identidad + confianza); abajo un bloque delimitado con TODO lo del consultorio mostrado (lugar, distancia, precio, forma de agendar, horarios, acción) y el acceso a los otros consultorios dentro del mismo bloque. El borde dice «estos datos van juntos».',
 b:'B · Próximo lugar: lo primero que se lee es cuándo hay lugar (o «Por teléfono») y el precio; el médico pasa a segundo plano con avatar chico. Sirve a quien tiene prisa; pierde peso la confianza.',
 c:'C · Consultorios: el médico arriba; debajo, una fila por consultorio (máx. 2 visibles) con lugar, distancia, precio, forma de agendar y su propia acción. Muestra las formas mixtas sin abrir el perfil; los horarios se eligen después. Más alta con 2+ consultorios.'};
function ficha(m){ return `<div class="fx">${V[S.v](m)}</div>`; }
function render(){
  const f=document.getElementById('wf-frame'), L=document.getElementById('wf-label');
  f.style.setProperty('--wf-w', S.w+'px'); L.style.setProperty('--wf-w', S.w+'px');
  L.textContent=`Marco ${S.w}px · ${S.w<600?'compact':S.w<1024?'medium':'expanded'} (referencia declarada) · versión ${S.v.toUpperCase()}`;
  document.querySelectorAll('[data-w]').forEach(b=>b.setAttribute('aria-pressed', String(+b.dataset.w===S.w)));
  document.querySelectorAll('[data-v]').forEach(b=>b.setAttribute('aria-pressed', String(b.dataset.v===S.v)));
  document.getElementById('wf-banner').innerHTML = off() ? '<p class="wf-banner" role="status"><b>Sin conexión.</b> Ves los resultados guardados; los horarios pueden haber cambiado. Puedes llamar.</p>' : '';
  const head = `<div class="res-h"><h1>Dermatólogas cerca de ti</h1><span class="wf-muted wf-small">${S.st==='empty'?'0':'12'} resultados · Más cerca</span></div>${S.w<1024?'<div class="fbar"><button class="wf-btn">Filtros (2)</button><button class="wf-btn">Más cerca</button></div>':''}`;
  let list;
  if (S.st==='loading') list = `<div class="fl wf-skel" aria-busy="true">${'<div class="fc"><div class="idr"><div class="av"></div><div style="flex:1"><div class="wf-line" style="width:70%"></div><div class="wf-line" style="width:50%"></div></div></div><div class="wf-line"></div><div class="wf-line" style="width:40%"></div><div class="wf-box" style="height:44px;border-radius:999px"></div></div>'.repeat(3)}</div><span class="wf-note">Misma huella que la ficha; los horarios pueden llegar después que el resto.</span>`;
  else if (S.st==='empty') list = `<div class="wf-state"><h2>No hay dermatólogas con estos filtros</h2><p class="wf-muted">Filtros activos: Cita en línea · Hasta $500. 4 especialistas cumplen si quitas «Hasta $500».</p><div class="wf-actions" style="justify-content:center"><button class="wf-btn wf-btn--primary">Quitar «Hasta $500»</button><button class="wf-btn wf-btn--quiet">Limpiar filtros</button></div></div>`;
  else list = `<div class="fl" role="list">${(S.st==='long'?[LARGA,...MED.slice(1)]:MED).map(ficha).join('')}</div>`;
  document.getElementById('wf-view').innerHTML = head + list + `<span class="wf-note">${NOTAS[S.v]}</span>`;
  document.getElementById('shell').style.gridTemplateColumns = '';
}
document.addEventListener('click', e=>{const w=e.target.closest('[data-w]'); if(w){S.w=+w.dataset.w; render();} const v=e.target.closest('[data-v]'); if(v){S.v=v.dataset.v; render();}
  const sb=e.target.closest('.sl button:not(.mas)'); if(sb&&!sb.disabled){sb.parentElement.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed', String(x===sb)));}});
document.getElementById('wf-state').addEventListener('change', e=>{S.st=e.target.value; render();});
document.getElementById('wf-notes').addEventListener('change', e=>document.body.classList.toggle('wf-no-notes', !e.target.checked));
render();
'''
HEAD_FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&display=swap" rel="stylesheet"><!-- solo chrome -->'
idx = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="wf-fidelidad" content="F2">
<title>Wireframe · FichaMedico · r01</title>
{HEAD_FONTS}
<link rel="stylesheet" href="vendor/wireframe-kit.css">
<style>{LOCAL}</style>
</head>
<body class="wf">
{BODY}
<script>{JS}</script>
</body>
</html>'''
open(os.path.join(D, 'index.html'), 'w').write(idx)
pub = f'''<title>Ficha del médico · wireframe</title>
<meta name="claude:viewport-fit-sides" content="cover">
{HEAD_FONTS}
<style>{KIT}{LOCAL}
body.wf{{padding-left:0;padding-right:0}}.wf-ctl{{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}.wf-stage{{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}</style>
<script>document.documentElement.lang='es';document.addEventListener('DOMContentLoaded',()=>document.body.classList.add('wf'))</script>
{BODY}
<script>document.body.classList.add('wf');{JS}</script>
'''
open(os.path.join(D, 'publicar.html'), 'w').write(pub)
print('ok')
