# Ecosistema Manik · app shell r02 (navbar, sidebar con módulos y submódulos, pie; alternativa para apps de 2 secciones).
# Pedido (2026-11-05): «los appshells con navbar, sidebar, footer, los sidebars con módulos y submódulos y para aplicaciones
# pequeñas que solo tienen 2 secciones una alternativa distinta». Reemplaza la propuesta r01 (../shell/, 2026-10-24, sin aprobar).
# Reutiliza la familia de controles aprobada (../controles-r01/gen.py) y los tokens del sistema. Uso: python3 gen.py → shell.html
import os, json, ast, importlib.util
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
s = importlib.util.spec_from_file_location('ctl', os.path.join(M, 'controles-r01/gen.py')); C = importlib.util.module_from_spec(s); s.loader.exec_module(C)
V, ic = C.V, C.ic
CSS0 = C.HTML.split('<style>', 1)[1].split('</style>', 1)[0]
src = open(os.path.join(M, 'shell/gen.py')).read(); i = src.index('ICON = {'); j = src.index('\n}', i) + 2
ICON = ast.literal_eval(src[i + 7:j])  # Lucide, mismo set de la r01
ICON.update({'chevr': '<path d="m9 18 6-6-6-6"/>', 'panel-l': '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 3v18"/><path d="m16 15-3-3 3-3"/>',
             'panel-r': '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 3v18"/><path d="m14 9 3 3-3 3"/>', 'megaphone': '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
             'download': '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/>', 'x': '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>'})
SELLOS = C.SELLOS; ECO = 'data:image/svg+xml;base64,' + __import__('base64').b64encode(open(os.path.join(M, 'final/svg/ecosistema.svg'), 'rb').read()).decode()

APPS = {
 'expediente': {'n': 'Expediente', 'patron': 'modulos', 'busca': 'Buscar paciente, expediente o CURP',
   'nav': [['home', 'Hoy', 6, []], ['users', 'Pacientes', 0, []], ['steth', 'Consultas', 0, []], ['clock', 'Lista de espera', 3, []],
           ['pill', 'Clínico', 0, [['Recetas', 0], ['Órdenes de estudios', 0], ['Resultados', 2], ['Vacunas', 0]]],
           ['file', 'Documentos', 0, [['Consentimientos', 0], ['Certificados', 0], ['Plantillas', 0]]], ['bars', 'Reportes', 0, []]],
   'activo': ['Clínico', 'Resultados'], 'filtros': ['Hoy', 'Esta semana', 'Por revisar'], 'cta': 'Pedir estudio', 'sub': '2 resultados nuevos desde ayer',
   'cols': ['Paciente', 'Estudio', 'Recibido', 'Estado'],
   'filas': [['Mariana Ruiz', 'Biometría hemática', '05/11 08:12', ['aviso', 'Por revisar']], ['Jorge Salas', 'Perfil de lípidos', '05/11 07:40', ['aviso', 'Por revisar']],
             ['Lucía Peña', 'Glucosa en ayuno', '04/11 17:05', ['exito', 'Revisado']], ['Andrés Mora', 'Química sanguínea', '04/11 12:30', ['exito', 'Revisado']]]},
 'agenda': {'n': 'Agenda', 'patron': 'plano', 'busca': 'Buscar paciente o cita',
   'nav': [['home', 'Hoy', 0, []], ['cal', 'Calendario', 0, []], ['door', 'Sala de espera', 4, []], ['users', 'Pacientes', 0, []], ['bell', 'Recordatorios', 0, []]],
   'activo': ['Sala de espera'], 'filtros': ['Todos', 'En sala', 'Sin llegar'], 'cta': 'Registrar llegada', 'sub': '4 pacientes esperando · Consultorio 2',
   'cols': ['Paciente', 'Cita', 'Llegó', 'Estado'],
   'filas': [['Mariana Ruiz', '10:00 · Dra. Ramírez', '09:48', ['info', 'En sala']], ['Jorge Salas', '10:30 · Dra. Ramírez', '10:05', ['info', 'En sala']],
             ['Lucía Peña', '10:30 · Dr. Ortega', '10:12', ['info', 'En sala']], ['Andrés Mora', '11:00 · Dr. Ortega', '—', ['aviso', 'Sin llegar']]]},
 'impulsa': {'n': 'Impulsa', 'patron': 'pequena', 'busca': '',
   'nav': [['megaphone', 'Campañas', 0, []], ['bars', 'Resultados', 0, []]],
   'activo': ['Campañas'], 'filtros': ['Activas', 'Terminadas'], 'cta': 'Nueva campaña', 'sub': '3 campañas activas este mes',
   'cols': ['Campaña', 'Público', 'Termina', 'Estado'],
   'filas': [['Revisión de presión', '1 240 pacientes', '30/11', ['exito', 'Activa']], ['Vacuna de influenza', '860 pacientes', '15/12', ['exito', 'Activa']],
             ['Chequeo anual', '2 100 pacientes', '31/12', ['exito', 'Activa']], ['Día del corazón', '980 pacientes', '29/09', ['info', 'Terminada']]]},
}

CSS = r'''
.wrap{max-width:1320px;grid-template-columns:minmax(0,1fr)}section{grid-template-columns:minmax(0,1fr)}
.ctl{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center}.ctl>div{display:flex;flex-wrap:wrap;gap:8px;align-items:center;min-width:0;max-width:100%}.ctl .seg{max-width:100%}.ctl b{font:600 14px/20px var(--font-sans)}
/* marco que simula el ancho del dispositivo; el shell responde a su contenedor */
.sh-marco{container-type:inline-size;margin:0 auto;width:100%;border:1px solid var(--line);border-radius:var(--radius-2xl);overflow:hidden;background:var(--canvas);box-shadow:var(--shadow-card);transition:max-width .2s}
.sh-marco[data-ancho=tab]{max-width:834px}.sh-marco[data-ancho=cel]{max-width:390px}
@media (prefers-reduced-motion:reduce){.sh-marco{transition:none}}
.sh{position:relative;display:grid;grid-template-columns:264px minmax(0,1fr);grid-template-rows:var(--header-height) minmax(0,1fr);height:760px;background:var(--canvas);color:var(--ink);overflow:hidden}
.sh.riel{grid-template-columns:72px minmax(0,1fr)}
.sh.pequena{grid-template-columns:minmax(0,1fr);grid-template-rows:var(--header-height) auto minmax(0,1fr)}
.sh-salto{position:absolute;left:8px;top:-60px;z-index:20;background:var(--manik);color:var(--on-manik);padding:10px 14px;border-radius:var(--radius-md);font:600 14px/20px var(--font-sans)}.sh-salto:focus{top:8px}
/* barra superior */
.sh-nav{grid-column:1/-1;display:flex;align-items:center;gap:8px;padding:0 16px 0 12px;background:var(--surface);border-bottom:1px solid var(--line);min-width:0}
.sh-marca{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);min-height:44px;padding:0 8px;border-radius:var(--radius-md);flex:none}
.sh-marca img{width:32px;height:32px}.sh-marca span{font:400 16px/24px var(--font-display);color:var(--muted)}.sh-marca b{font-weight:600;color:var(--ink)}
.sh-bus{flex:1;max-width:460px;margin-left:24px}.sh-bus .in{min-height:40px;background:var(--canvas);border-color:var(--line-control)}
.sh-der{margin-left:auto;display:flex;align-items:center;gap:4px}
.sh-ib{position:relative}.sh-badge{position:absolute;top:6px;right:5px;min-width:18px;height:18px;padding:0 4px;border-radius:999px;background:var(--manik);color:var(--on-manik);font:700 11px/18px var(--font-sans);text-align:center;box-shadow:0 0 0 2px var(--surface)}
.sh-eco img{width:24px;height:24px}
.sh-yo{display:flex;align-items:center;gap:10px;margin-left:8px;padding:4px 8px 4px 4px;border-radius:999px;border:0;background:transparent;cursor:pointer;color:var(--ink)}
.sh-yo:hover{background:var(--surface-soft)}.sh-av{width:36px;height:36px;border-radius:50%;background:var(--app-expediente-soft);color:var(--manik);display:grid;place-items:center;font:700 13px/1 var(--font-sans)}
.sh-yo span{display:grid;text-align:left}.sh-yo b{font:600 14px/18px var(--font-sans)}.sh-yo small{font-size:13px;line-height:16px;color:var(--muted)}
.sh-menu{display:none}
/* barra lateral */
.sh-side{background:var(--surface);border-right:1px solid var(--line);display:flex;flex-direction:column;min-height:0;min-width:0}
.sh-lista{flex:1;overflow-y:auto;padding:12px;display:grid;align-content:start;gap:2px}
.sh-lista ul{list-style:none;margin:0;padding:0;display:grid;gap:2px}
.sh-it{display:flex;align-items:center;gap:12px;width:100%;min-height:44px;padding:0 12px;border:0;border-radius:var(--radius-md);background:transparent;color:var(--ink);text-decoration:none;font:400 15px/20px var(--font-sans);cursor:pointer;text-align:left;position:relative}
.sh-it .ico{width:20px;height:20px;color:var(--muted)}.sh-it .sh-tx{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sh-it:hover{background:var(--surface-soft)}
.sh-it[aria-current=page]{background:var(--manik-soft);color:var(--manik);font-weight:600}.sh-it[aria-current=page] .ico{color:var(--manik)}
.sh-it.padre{font-weight:600}.sh-it.padre .ico{color:var(--manik)}
.sh-cnt{min-width:24px;height:22px;padding:0 7px;border-radius:999px;background:var(--manik-soft);color:var(--manik);font:700 12px/22px var(--font-sans);text-align:center}
.sh-it[aria-current=page] .sh-cnt{background:var(--surface)}
.sh-ch{width:16px!important;height:16px!important;transition:transform .15s}.sh-it[aria-expanded=true] .sh-ch{transform:rotate(180deg)}
.sh-sub{margin:2px 0 6px 21px!important;padding-left:12px!important;border-left:1.5px solid var(--line)}
.sh-sub .sh-it{min-height:40px;font-size:15px;color:var(--muted);padding-left:12px}.sh-sub .sh-it[aria-current=page]{color:var(--manik)}
.sh-sub[hidden]{display:none!important}
.sh-pie-side{border-top:1px solid var(--line);padding:8px 12px 12px;display:grid;gap:2px}
.sh-tip{display:none}
/* riel */
.sh.riel .sh-lista,.sh.riel .sh-pie-side{padding-left:12px;padding-right:12px}
.sh.riel .sh-it{justify-content:center;padding:0;width:48px}.sh.riel .sh-tx,.sh.riel .sh-ch,.sh.riel .sh-cnt:not(.pt){display:none}
.sh.riel .sh-sub{display:none!important}
.sh.riel .sh-it .sh-cnt.pt{position:absolute;top:4px;right:2px;min-width:8px;width:8px;height:8px;padding:0;font-size:0}
.sh.riel .sh-it:hover .sh-tip,.sh.riel .sh-it:focus-visible .sh-tip{display:block;position:absolute;left:58px;top:50%;transform:translateY(-50%);background:var(--ink);color:#fff;font:600 13px/18px var(--font-sans);padding:6px 10px;border-radius:8px;white-space:nowrap;z-index:5;pointer-events:none}
.sh-fly{position:absolute;z-index:6;width:240px;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-lg);box-shadow:var(--shadow-pop);padding:8px}
.sh.riel .sh-fly .sh-it{justify-content:flex-start;padding:0 12px;width:100%}.sh.riel .sh-fly .sh-tx,.sh.riel .sh-fly .sh-cnt{display:revert}
.sh-fly p{font:700 12px/16px var(--font-sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding:8px 12px 6px}
/* contenido */
.sh-main{min-width:0;min-height:0;overflow-y:auto;display:flex;flex-direction:column}
.sh-pag{flex:1;padding:28px 32px 32px;display:grid;gap:20px;align-content:start;width:100%;margin:0 auto}
.sh.pequena .sh-pag{max-width:1120px}
.sh-migas{display:flex;gap:6px;align-items:center;font-size:14px;line-height:20px;color:var(--muted)}.sh-migas a{color:var(--muted);min-height:24px;display:inline-flex;align-items:center}.sh-migas .ico{width:14px;height:14px}
.sh-cab{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-end;justify-content:space-between}.sh-cab>div:first-child{display:grid;gap:4px}
.sh-cab h1{font:600 24px/32px var(--font-display);letter-spacing:-.01em;margin:0}.sh-cab p{color:var(--muted);font-size:15px;line-height:22px}
.sh-cab .fila{gap:10px}
.sh-trab{display:block;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-2xl);overflow:hidden}
.sh-herr{display:flex;flex-wrap:wrap;gap:10px;align-items:center;padding:14px 16px;border-bottom:1px solid var(--line)}
.sh-trab table{width:100%;border-collapse:collapse}.sh-trab th{font:600 14px/20px var(--font-sans);color:var(--muted);text-align:left;padding:12px 16px;border-bottom:1px solid var(--line);background:var(--surface)}
.sh-trab td{padding:12px 16px;border-bottom:1px solid var(--line);font:400 15px/22px var(--font-sans)}.sh-trab tr:last-child td{border-bottom:0}.sh-trab td.num{font-variant-numeric:tabular-nums;color:var(--muted)}
.sh-trab td:first-child{font-weight:600}
.sh-est{display:inline-flex;align-items:center;gap:6px;padding:3px 12px 3px 9px;border-radius:999px;font:600 13px/18px var(--font-sans)}.sh-est .ico{width:16px;height:16px}
.sh-foot{display:flex;flex-wrap:wrap;gap:6px 20px;align-items:center;min-height:44px;padding:8px 32px;border-top:1px solid var(--line);font-size:13px;line-height:18px;color:var(--muted)}
.sh-foot a{color:var(--muted);min-height:24px;display:inline-flex;align-items:center}.sh-foot .sp{flex:1}.sh-ok{display:inline-flex;gap:6px;align-items:center}.sh-ok i{width:8px;height:8px;border-radius:50%;background:var(--exito)}
/* app pequeña: pestañas bajo la barra */
.sh-tabs{grid-column:1/-1;background:var(--surface);border-bottom:1px solid var(--line);padding:0 32px}
.sh-tabs ul{list-style:none;margin:0 auto;padding:0;display:flex;gap:8px;max-width:1056px}
.sh-tab{display:flex;align-items:center;gap:8px;min-height:48px;padding:0 6px;margin-bottom:-1px;border-bottom:3px solid transparent;color:var(--muted);text-decoration:none;font:600 15px/20px var(--font-sans)}
.sh-tab .ico{width:18px;height:18px}.sh-tab:hover{color:var(--ink)}.sh-tab[aria-current=page]{color:var(--manik);border-bottom-color:var(--manik)}
/* cajón (tableta y celular) */
.sh-velo{position:absolute;inset:0;background:var(--scrim);z-index:8}.sh-velo[hidden]{display:none}
.sh-cajon-x{display:none}
@container (max-width:1023px){
 .sh,.sh.riel{grid-template-columns:minmax(0,1fr)}
 .sh-menu{display:inline-grid}
 .sh-side{position:absolute;z-index:9;top:0;bottom:0;left:0;width:300px;transform:translateX(-102%);transition:transform .2s;box-shadow:var(--shadow-pop);visibility:hidden}
 .sh.cajon .sh-side{transform:none;visibility:visible}
 .sh-cajon-x{display:flex;align-items:center;justify-content:space-between;height:var(--header-height);padding:0 12px 0 20px;border-bottom:1px solid var(--line)}
 .sh-cajon-x b{font:600 16px/24px var(--font-display)}
 .sh.riel .sh-it{justify-content:flex-start;padding:0 12px;width:100%}.sh.riel .sh-tx,.sh.riel .sh-ch,.sh.riel .sh-cnt{display:revert}.sh.riel .sh-sub:not([hidden]){display:grid!important}
 .sh-plegar{display:none!important}.sh-yo>span:last-child{display:none}.sh-pag{padding:24px}.sh-foot{padding:8px 24px}.sh-tabs{padding:0 24px}
}
@container (max-width:639px){
 .sh-bus{display:none}.sh-lupa{display:inline-grid!important}.sh-marca span{display:none}.sh-marca{padding:0 4px}
 .sh-pag{padding:20px 16px}.sh-foot{padding:8px 16px}.sh-tabs{padding:0 16px}.sh-tab{flex:1;justify-content:center}.sh-tabs li{flex:1}
 .sh-cab{align-items:stretch}.sh-cab .fila{width:100%}.sh-cab .fila .btn{flex:1}
 .sh-trab thead{display:none}.sh-trab tr{display:grid;grid-template-columns:1fr auto;gap:2px 12px;padding:12px 16px;border-bottom:1px solid var(--line)}.sh-trab tr:last-child{border-bottom:0}
 .sh-trab td{padding:0;border:0}.sh-trab td:nth-child(4){grid-column:2;grid-row:1/3;align-self:center}.sh-trab td:nth-child(3){grid-column:1}
 .sh-herr .chip:nth-child(n+3){display:none}
}
.sh-lupa{display:none}
@media (prefers-reduced-motion:reduce){.sh-side,.sh-ch{transition:none}}
/* reglas */
.reglas{margin:0;padding-left:30px;display:grid;gap:10px;max-width:84ch}
.patrones{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:16px}
.mini{border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;height:150px;display:grid;grid-template-rows:22px 1fr;background:var(--canvas)}
.mini .n{background:var(--surface);border-bottom:1px solid var(--line)}.mini .b{display:grid;grid-template-columns:70px 1fr;min-height:0}.mini .b.t{grid-template-columns:1fr;grid-template-rows:18px 1fr}
.mini .s{background:var(--surface);border-right:1px solid var(--line);padding:8px 6px;display:grid;gap:5px;align-content:start}.mini .s i{height:7px;border-radius:3px;background:var(--surface-pressed)}.mini .s i.a{background:var(--manik)}.mini .s i.k{margin-left:12px;width:70%}
.mini .tb{background:var(--surface);border-bottom:1px solid var(--line);display:flex;gap:8px;padding:0 12px;align-items:end}.mini .tb i{width:36px;height:3px;background:var(--surface-pressed)}.mini .tb i.a{background:var(--manik)}
.mini .c{padding:10px}.mini .c i{display:block;height:100%;border-radius:8px;background:var(--surface);border:1px solid var(--line)}
'''

ESTICO = {'exito': 'ok', 'aviso': 'warn', 'info': 'clock', 'error': 'x'}
JS = r'''
const A=__APPS__,I=__ICON__,S=__SELLOS__;
const ico=(n,c='ico')=>`<svg class="${c}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${I[n]||''}</svg>`;
const EI={exito:'ok',aviso:'warn',info:'clock',error:'x'};
let app='expediente',riel=false,act=null;
const sh=document.getElementById('sh'),marco=document.getElementById('marco');
function navLateral(a){
 let h='';a.nav.forEach(([i,t,n,sub],k)=>{
  const tip=`<span class="sh-tip">${t}</span>`,cnt=n?`<span class="sh-cnt ${riel?'pt':''}" aria-label="${n} pendientes">${n}</span>`:'';
  if(!sub.length){const cur=act[0]===t?' aria-current="page"':'';h+=`<li><a href="#" class="sh-it" data-m="${t}"${cur}>${ico(i)}<span class="sh-tx">${t}</span>${cnt}${tip}</a></li>`}
  else{const abierto=act[0]===t,id='sm-'+k,pend=sub.reduce((s,x)=>s+x[1],0);
   h+=`<li><button type="button" class="sh-it ${abierto?'padre':''}" aria-expanded="${abierto}" aria-controls="${id}" data-g="${k}">${ico(i)}<span class="sh-tx">${t}</span>${pend&&!abierto?`<span class="sh-cnt ${riel?'pt':''}" aria-label="${pend} pendientes">${pend}</span>`:''}${ico('chev','ico sh-ch')}${tip}</button>
   <ul class="sh-sub" id="${id}" ${abierto?'':'hidden'}>${sub.map(([s,c])=>`<li><a href="#" class="sh-it" data-m="${t}" data-s="${s}"${act[0]===t&&act[1]===s?' aria-current="page"':''}><span class="sh-tx">${s}</span>${c?`<span class="sh-cnt" aria-label="${c} pendientes">${c}</span>`:''}</a></li>`).join('')}</ul></li>`}});
 return h}
function render(){
 const a=A[app];act=act||a.activo;const peq=a.patron==='pequena';
 sh.className='sh'+(peq?' pequena':'')+(riel&&!peq?' riel':'');
 const est=([e,t])=>{const v={exito:['--exito-soft','--on-exito-soft'],aviso:['--aviso-soft','--on-aviso-soft'],info:['--info-soft','--on-info-soft'],error:['--error-soft','--on-error-soft']}[e];return `<span class="sh-est" style="background:var(${v[0]});color:var(${v[1]})">${ico(EI[e])}${t}</span>`};
 const titulo=act[1]||act[0],migas=act[1]?`<nav class="sh-migas" aria-label="Ubicación"><a href="#">${act[0]}</a>${ico('chevr')}<span aria-current="page">${act[1]}</span></nav>`:'';
 const nav=`<header class="sh-nav">
  <button type="button" class="ibtn sh-menu" aria-label="Abrir menú" aria-expanded="false" aria-controls="side" id="bmenu" ${peq?'hidden':''}>${ico('menu')}</button>
  <a class="sh-marca" href="#" aria-label="${a.n} Manik, inicio"><img src="${S[app]}" alt=""><span><b>${a.n}</b> Manik</span></a>
  ${a.busca?`<div class="sh-bus"><span class="bus">${ico('search')}<input class="in" type="search" aria-label="${a.busca}" placeholder="${a.busca}"></span></div>`:''}
  <div class="sh-der">${a.busca?`<button type="button" class="ibtn sh-lupa" aria-label="Buscar">${ico('search')}</button>`:''}
   <button type="button" class="ibtn sh-ib" aria-label="Avisos, 3 sin leer">${ico('bell')}<span class="sh-badge" aria-hidden="true">3</span></button>
   <button type="button" class="ibtn sh-eco" aria-label="Ecosistema Manik: cambiar de app" aria-haspopup="dialog"><img src="__ECO__" alt=""></button>
   <button type="button" class="sh-yo" aria-label="Cuenta de Dra. Ana Ramírez"><span class="sh-av" aria-hidden="true">AR</span><span><b>Dra. Ana Ramírez</b><small>Clínica Santa Lucía</small></span></button></div></header>`;
 const side=peq?'':`<aside class="sh-side" id="side" aria-label="Menú de ${a.n}"><div class="sh-cajon-x"><b>${a.n} Manik</b><button type="button" class="ibtn" id="bcerrar" aria-label="Cerrar menú">${ico('x')}</button></div>
  <nav class="sh-lista" aria-label="${a.n}"><ul>${navLateral(a)}</ul></nav>
  <div class="sh-pie-side"><a href="#" class="sh-it">${ico('help')}<span class="sh-tx">Ayuda</span><span class="sh-tip">Ayuda</span></a>
  <button type="button" class="sh-it sh-plegar" id="bplegar" aria-pressed="${riel}">${ico(riel?'panel-r':'panel-l')}<span class="sh-tx">${riel?'Desplegar menú':'Plegar menú'}</span><span class="sh-tip">${riel?'Desplegar menú':'Plegar menú'}</span></button></div></aside>`;
 const tabs=peq?`<nav class="sh-tabs" aria-label="${a.n}"><ul>${a.nav.map(([i,t])=>`<li><a href="#" class="sh-tab" data-m="${t}"${act[0]===t?' aria-current="page"':''}>${ico(i)}${t}</a></li>`).join('')}</ul></nav>`:'';
 const cta=peq&&act[0]!=='Campañas'?'':`<button type="button" class="btn b1">${ico('plus')}<span>${a.cta}</span></button>`;
 const main=`<div class="sh-main"><main class="sh-pag" id="contenido" tabindex="-1">${migas}
  <div class="sh-cab"><div><h1>${titulo}</h1><p>${act[0]==='Resultados'&&peq?'Alcance y respuesta de tus campañas':a.sub}</p></div><div class="fila"><button type="button" class="btn b2">${ico('download')}<span>Exportar</span></button>${cta}</div></div>
  <section class="sh-trab" aria-label="${titulo}"><div class="sh-herr" role="group" aria-label="Filtros">${a.filtros.map((t,i)=>`<button type="button" class="chip" aria-pressed="${i===0}">${ico('ok','ico ck')}<span>${t}</span></button>`).join('')}</div>
  <table><thead><tr>${a.cols.map(c=>`<th scope="col">${c}</th>`).join('')}</tr></thead><tbody>${a.filas.map(f=>`<tr><td>${f[0]}</td><td>${f[1]}</td><td class="num">${f[2]}</td><td>${est(f[3])}</td></tr>`).join('')}</tbody></table></section></main>
  <footer class="sh-foot"><span>${a.n} Manik 4.2</span><span class="sh-ok"><i aria-hidden="true"></i>Sistema en línea</span><span class="sp"></span><a href="#">Aviso de privacidad</a><a href="#">Ayuda y soporte</a></footer></div>`;
 sh.innerHTML=`<a class="sh-salto" href="#contenido">Saltar al contenido</a>${nav}${tabs}${side}${main}<div class="sh-velo" id="velo" hidden></div>`;
 wire()}
function cerrarCajon(){sh.classList.remove('cajon');const v=document.getElementById('velo');if(v)v.hidden=true;const b=document.getElementById('bmenu');if(b){b.setAttribute('aria-expanded','false');b.focus()}}
function cerrarFly(){const f=sh.querySelector('.sh-fly');if(f){const o=f._o;f.remove();if(o){o.setAttribute('aria-expanded','false');o.focus()}}}
function wire(){
 sh.querySelectorAll('a.sh-it[data-m],a.sh-tab').forEach(l=>l.addEventListener('click',e=>{e.preventDefault();act=l.dataset.s?[l.dataset.m,l.dataset.s]:[l.dataset.m];const caj=sh.classList.contains('cajon');render();if(caj){}document.getElementById('contenido').focus()}));
 sh.querySelectorAll('button[data-g]').forEach(b=>b.addEventListener('click',()=>{
  if(sh.classList.contains('riel')&&getComputedStyle(sh.querySelector('.sh-menu')).display==='none'){abrirFly(b);return}
  const ul=document.getElementById(b.getAttribute('aria-controls')),ab=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',ab);ul.hidden=!ab}));
 const p=document.getElementById('bplegar');if(p)p.addEventListener('click',()=>{riel=!riel;render();document.getElementById('bplegar').focus()});
 const m=document.getElementById('bmenu');if(m)m.addEventListener('click',()=>{sh.classList.add('cajon');document.getElementById('velo').hidden=false;m.setAttribute('aria-expanded','true');document.getElementById('bcerrar').focus()});
 const x=document.getElementById('bcerrar');if(x)x.addEventListener('click',cerrarCajon);
 const v=document.getElementById('velo');if(v)v.addEventListener('click',cerrarCajon);
 sh.querySelectorAll('.chip').forEach(c=>c.addEventListener('click',()=>c.setAttribute('aria-pressed',c.getAttribute('aria-pressed')!=='true')));
}
function abrirFly(b){cerrarFly();const k=+b.dataset.g,[ , t, , sub]=A[app].nav[k];const f=document.createElement('div');f.className='sh-fly';f.setAttribute('role','group');f.setAttribute('aria-label',t);f._o=b;
 f.innerHTML=`<p>${t}</p><ul style="list-style:none;margin:0;padding:0;display:grid;gap:2px">${sub.map(([s,c])=>`<li><a href="#" class="sh-it" data-m="${t}" data-s="${s}"${act[0]===t&&act[1]===s?' aria-current="page"':''}><span class="sh-tx">${s}</span>${c?`<span class="sh-cnt">${c}</span>`:''}</a></li>`).join('')}</ul>`;
 const r=b.getBoundingClientRect(),q=sh.getBoundingClientRect();f.style.left=(r.right-q.left+10)+'px';f.style.top=(r.top-q.top)+'px';sh.appendChild(f);b.setAttribute('aria-expanded','true');
 f.querySelectorAll('a').forEach(l=>l.addEventListener('click',e=>{e.preventDefault();act=[l.dataset.m,l.dataset.s];render()}));f.querySelector('a').focus()}
document.addEventListener('keydown',e=>{if(e.key==='Escape'){if(sh.querySelector('.sh-fly'))cerrarFly();else if(sh.classList.contains('cajon'))cerrarCajon()}});
document.addEventListener('click',e=>{const f=sh.querySelector('.sh-fly');if(f&&!f.contains(e.target)&&!e.target.closest('button[data-g]'))f.remove()});
document.querySelectorAll('[role=radiogroup]').forEach(g=>{const bs=[...g.querySelectorAll('[role=radio]')];const pick=b=>{bs.forEach(x=>{x.setAttribute('aria-checked',x===b);x.tabIndex=x===b?0:-1});
 if(b.dataset.app){app=b.dataset.app;act=null;riel=false;render()}if(b.dataset.ancho){marco.dataset.ancho=b.dataset.ancho;riel=false;sh.classList.remove('cajon');render()}};
 bs.forEach((b,i)=>{b.addEventListener('click',()=>pick(b));b.addEventListener('keydown',e=>{const d={ArrowRight:1,ArrowDown:1,ArrowLeft:-1,ArrowUp:-1}[e.key];if(d){e.preventDefault();const n=bs[(i+d+bs.length)%bs.length];pick(n);n.focus()}})})});
render();
'''
JS = JS.replace('__APPS__', json.dumps(APPS, ensure_ascii=False)).replace('__ICON__', json.dumps(ICON)).replace('__SELLOS__', json.dumps({k: SELLOS[k] for k in APPS})).replace('__ECO__', ECO)

def rg(lbl, opts, attr):
    return f'<div class="seg" role="radiogroup" aria-label="{lbl}">' + ''.join(f'<button type="button" role="radio" data-{attr}="{k}" aria-checked="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{t}</button>' for i, (k, t) in enumerate(opts)) + '</div>'
ctl = (f'<div class="ctl"><div><b id="l-app">App</b>{rg("App de ejemplo", [("expediente", "Expediente · módulos y submódulos"), ("agenda", "Agenda · menú plano"), ("impulsa", "Impulsa · 2 secciones")], "app")}</div>'
       f'<div><b>Ancho</b>{rg("Ancho de pantalla", [("esc", "Escritorio"), ("tab", "Tableta"), ("cel", "Celular")], "ancho")}</div></div>')

def mini(kind):
    if kind == 'tabs': return '<div class="mini" aria-hidden="true"><span class="n"></span><div class="b t"><div class="tb"><i class="a"></i><i></i></div><div class="c"><i></i></div></div></div>'
    s = '<i class="a"></i><i></i><i></i><i></i><i></i>' if kind == 'plano' else '<i></i><i></i><i></i><i></i><i class="k a"></i><i class="k"></i><i class="k"></i><i></i>'
    return f'<div class="mini" aria-hidden="true"><span class="n"></span><div class="b"><div class="s">{s}</div><div class="c"><i></i></div></div></div>'

R_SHELL = ''.join(f'<li>{x}</li>' for x in [
 '<b>Barra superior (64 px), igual en las siete apps:</b> sello y nombre (llevan al inicio de la app), búsqueda de la app, avisos, botón del ecosistema justo antes del avatar, y la cuenta. Nada de acciones de página aquí.',
 '<b>Barra lateral (264 px) en «surface»:</b> módulos con icono de 20 px y fila de 44 px; contador de pendientes en «manik-soft». Abajo, Ayuda y «Plegar menú».',
 '<b>Submódulos desplegables:</b> el módulo con submódulos es un botón (no un enlace) con flecha; al abrir, sus submódulos cuelgan de una línea guía, sin icono, en filas de 40 px. Se abre solo el grupo de la página actual; los demás, cuando la persona los abre. Si un grupo cerrado tiene pendientes, el módulo muestra su suma.',
 '<b>Dónde estoy:</b> la página actual en «manik-soft» con texto «manik» y <span class="mono">aria-current="page"</span>; su módulo padre en negritas con el icono en «manik». En el contenido, migas «Módulo › Submódulo».',
 '<b>Riel (72 px):</b> la barra plegada deja solo iconos, con el nombre en una etiqueta flotante al pasar o enfocar. Un módulo con submódulos abre un menú flotante con ellos. La preferencia se recuerda por persona.',
 '<b>Contenido:</b> encabezado de página (título 24/32, una línea de contexto, acciones a la derecha: secundaria y luego la principal) y debajo el área de trabajo en una tarjeta «surface» con borde «line».',
 '<b>Pie (44 px) dentro de la columna de contenido:</b> app y versión, estado del sistema, aviso de privacidad y soporte. Discreto: 13 px en «muted».',
 '<b>Tableta (menos de 1024 px):</b> la barra lateral se vuelve cajón desde la izquierda con el botón de menú; se cierra con X, Esc o tocando fuera, y el foco vuelve al botón.',
 '<b>Celular (menos de 640 px):</b> la búsqueda pasa a icono, el sello va sin nombre, las acciones de página a todo el ancho y las tablas se vuelven filas de dos líneas.'])
R_PEQ = ''.join(f'<li>{x}</li>' for x in [
 '<b>Sin barra lateral.</b> Con 2 o 3 secciones, un menú lateral ocupa 264 px para casi nada y hace ver la app más grande de lo que es.',
 '<b>Pestañas bajo la barra superior,</b> con icono y texto, subrayado de 3 px en «manik» en la actual. Son destinos (enlaces con <span class="mono">aria-current</span>), no acciones: «Nueva campaña» es un botón en el encabezado, no una pestaña.',
 '<b>Contenido centrado</b> a 1120 px como máximo: la página se lee como un documento, no como un panel de control.',
 '<b>En celular,</b> las pestañas se reparten el ancho; no hay cajón ni barra inferior porque no hace falta.',
 '<b>Si la app crece</b> a 4 secciones o más, pasa a barra lateral plana; no se agregan pestañas.'])

HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>App shell Ecosistema Manik</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS0}{CSS}</style></head><body><div class="wrap">
<header class="cab"><span class="eti">Ecosistema Manik · shell · ronda 2 · propuesta</span><h1>Barra superior, barra lateral y pie</h1>
<p>Un mismo esqueleto para las siete apps, con dos formas de navegar según su tamaño: barra lateral con módulos y submódulos para las apps grandes, y pestañas para las apps de 2 o 3 secciones. Usa los controles aprobados el 5 de noviembre.</p></header>
<section aria-labelledby="s0"><h2 id="s0">Pruébalo</h2>
<p class="nota">En Expediente abre «Documentos», pliega el menú y toca un icono con submódulos. Cambia a Tableta para ver el cajón. Datos de ejemplo.</p>{ctl}
<div class="sh-marco" id="marco" data-ancho="esc"><div class="sh" id="sh"></div></div></section>
<section aria-labelledby="s1"><h2 id="s1">¿Qué navegación lleva cada app?</h2>
<div class="patrones"><div class="lam">{mini("tabs")}<h4>2 o 3 secciones · pestañas</h4><p class="nota">Sin barra lateral. Impulsa: Campañas y Resultados.</p></div>
<div class="lam">{mini("plano")}<h4>4 a 7 secciones · barra lateral plana</h4><p class="nota">Un nivel. Agenda, Farmacia, Grupos.</p></div>
<div class="lam">{mini("mod")}<h4>Módulos con submódulos · barra lateral por módulos</h4><p class="nota">Dos niveles, nunca tres. Expediente, Compras, Administración.</p></div></div>
<p class="nota">Se cuenta por destinos, no por acciones: «Nueva cita» o «Exportar» viven en la página, no en el menú. Un tercer nivel de navegación es señal de que el módulo es otra app o necesita pestañas dentro de la página.</p></section>
<section aria-labelledby="s2"><h2 id="s2">Shell con barra lateral</h2><ol class="reglas">{R_SHELL}</ol></section>
<section aria-labelledby="s3"><h2 id="s3">Apps pequeñas · la alternativa</h2><ol class="reglas">{R_PEQ}</ol></section>
</div><script>{JS}</script></body></html>'''

if __name__ == '__main__':
    open(os.path.join(D, 'shell.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
