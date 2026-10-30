# Nisa Nabani · app shell común (NisaLab, NisaData, NisaStudio), prototipo r1.
# Fijo: estructura, medidas, barra superior (selector de apps, búsqueda, avisos, usuario), forma del menú lateral y área de trabajo.
# Cambia por app (tokens): logo, color del menú lateral, color de la sección activa y secciones del menú.
# Uso: python3 gen.py <íconos lucide> → shell.html (para publicar como Artifact)
import json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..'); LU = sys.argv[1]
def ic(n):
    s = open(os.path.join(LU, n + '.svg')).read(); s = s[s.index('<svg'):]
    s = re.sub(r'\s+', ' ', s); s = re.sub(r'\s(width|height)="24"', '', s); s = re.sub(r'\sclass="[^"]*"', '', s)
    return s.replace('<svg ', '<svg class="i" aria-hidden="true" focusable="false" ', 1)
def sv(ruta, uid):
    s = re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(NS, ruta)).read().strip())
    s = s.replace('id="nsg"', f'id="nsg-{uid}"').replace('url(#nsg)', f'url(#nsg-{uid})')
    return s.replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
NN = re.sub(r'\s(width|height)="[^"]*"', '', sv('nabi-design-system/marca-nisa/nisa-nabani-logo.svg', 'nn'), count=2)
def marca(a):
    m = re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(NS, 'nisalab-areas-final', 'svg', a, 'marca.svg')).read().strip())
    return m.replace('<svg ', '<svg class="am" aria-hidden="true" focusable="false" ', 1)
AREA = {'aguas': ('Aguas', '#007CA3', marca('aguas')), 'bebidas': ('Bebidas alcohólicas', '#7A5DA9', marca('bebidas')), 'alimentos': ('Alimentos', '#A6552D', marca('alimentos'))}
# páginas de NisaLab: variante por área (opción B aprobada) o global
PAG_LAB = {
  'Recepción': dict(sec='Recepción', titulo='Recepción de muestras', sub='12 muestras hoy · 3 por etiquetar', accion='Registrar muestra', area='aguas'),
  'Muestras': dict(sec='Muestras', titulo='Muestras', sub='104 en curso · 9 urgentes', accion='Buscar muestra', area='alimentos'),
  'Captura': dict(sec='Captura', titulo='Captura de resultados', sub='22 parámetros por capturar', accion='Capturar', area='aguas'),
  'Bitácoras': dict(sec='Bitácoras', titulo='Bitácora', sub='Turno matutino · 8 registros · 1 sin firmar', accion='Nuevo registro', area='bebidas'),
  'Informes': dict(sec='Informes', titulo='Informes', sub='7 por generar · 3 por firmar', accion='Generar informe', area='aguas'),
  'Catálogos': dict(sec='Catálogos', titulo='Normas', sub='64 normas · 5 por vencer', accion='Agregar norma', area=None, entradilla='Normas y métodos contra los que se evalúa cada parámetro.'),
  'Usuarios': dict(sec='Administración', titulo='Usuarios', sub='24 usuarios · 3 invitaciones pendientes', accion='Agregar usuario', area=None, entradilla='Quién entra a NisaLab y qué puede hacer.'),
}
APPS = {
 'lab': dict(nombre='NisaLab', desc='Muestras, resultados e informes', side='#052A76', side2='#0A3487', acc='#C2D225', txt='#C9D3EA', logo=sv('nisalab-final/svg/logotipo.svg', 'l'), icono=sv('nisalab-final/svg/app-icon.svg', 'li'),
            nav=[('inbox', 'Recepción'), ('test-tubes', 'Muestras'), ('flask-conical', 'Captura'), ('clipboard-list', 'Bitácoras'), ('file-text', 'Informes'), ('library', 'Catálogos'), ('users', 'Usuarios')],
            ruta='Recepción / Aguas', titulo='Recepción de muestras', sub='12 muestras hoy · 3 por etiquetar', accion='Registrar muestra'),
 'data': dict(nombre='NisaData', desc='Tendencias y salud del laboratorio', side='#1F2532', side2='#2A3142', acc='#FF8A1F', txt='#C9CED8', logo=sv('nisadata-final/svg/logotipo.svg', 'd'), icono=sv('nisadata-final/svg/app-icon.svg', 'di'),
             nav=[('layout-dashboard', 'Panel'), ('trending-up', 'Tendencias'), ('flask-conical', 'Áreas'), ('users', 'Clientes'), ('shield-check', 'Calidad'), ('wallet', 'Cobranza'), ('file-text', 'Reportes')],
             ruta='Panel', titulo='Panel del laboratorio', sub='Actualizado hoy 09:42 · últimos 90 días', accion='Exportar reporte'),
 'studio': dict(nombre='NisaStudio', desc='Piezas para redes y avisos', side='#3730A3', side2='#4038B5', acc='#14B8A6', txt='#D6D3F5', logo=sv('nisastudio-final/svg/logotipo.svg', 's'), icono=sv('nisastudio-final/svg/app-icon.svg', 'si'),
               nav=[('house', 'Inicio'), ('layout-template', 'Plantillas'), ('images', 'Mis piezas'), ('calendar-days', 'Fechas'), ('palette', 'Marca'), ('folder', 'Biblioteca')],
               ruta='Plantillas', titulo='Plantillas', sub='Efemérides, avisos, promociones y carruseles', accion='Nueva pieza'),
}
AREAJS = {k: dict(nombre=n, color=c, svg=m) for k, (n, c, m) in AREA.items()}
NAVJS = {k: dict(pags=(PAG_LAB if k == 'lab' else None), nombre=a['nombre'], side=a['side'], side2=a['side2'], acc=a['acc'], txt=a['txt'], ruta=a['ruta'], titulo=a['titulo'], sub=a['sub'], accion=a['accion'],
                 nav=[(ic(i), t) for i, t in a['nav']]) for k, a in APPS.items()}
logos = ''.join(f'<span class="lg" data-app="{k}"{"" if k == "lab" else " hidden"}>{a["logo"]}</span>' for k, a in APPS.items())
switch = ''.join(f'<li><button type="button" class="sw-it" data-go="{k}" role="menuitemradio" aria-checked="{"true" if k == "lab" else "false"}"><span class="sw-ic">{a["icono"]}</span><span><b>{a["nombre"]}</b><small>{a["desc"]}</small></span></button></li>' for k, a in APPS.items())
html = f'''<title>App shell Nisa Nabani</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Carcasa común de las apps internas de Nisa Nabani. La estructura es fija; cada app solo cambia --side, --side2, --acc, --side-tx y su logo. Tema claro deliberado. */
:root{{--bg:#F2F4F8;--sf:#FFFFFF;--tx:#141B33;--mu:#535B70;--ln:#DFE3EC;--az:#052A76;
--side:#052A76;--side2:#0A3487;--acc:#C2D225;--side-tx:#C9D3EA;--nav-h:60px;--side-w:240px;
--sans:Poppins,system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:light}}
[hidden]{{display:none!important}}*{{box-sizing:border-box}}
html,body{{height:100%}}body{{margin:0;background:var(--bg);color:var(--tx);font:14px/1.5 var(--sans);overflow:hidden}}
button{{font:inherit;color:inherit;cursor:pointer}}.i{{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round;flex:none}}
:focus-visible{{outline:3px solid var(--az);outline-offset:2px}}
.app{{display:grid;grid-template-rows:var(--nav-h) 1fr;height:100%}}
/* barra superior */
.nav{{display:flex;align-items:center;gap:8px;background:var(--sf);border-bottom:1px solid var(--ln);padding-left:max(12px,env(safe-area-inset-left,0px));padding-right:max(12px,env(safe-area-inset-right,0px));position:relative;z-index:20}}
.nav::after{{content:"";position:absolute;left:0;right:0;bottom:-1px;height:2px;background:linear-gradient(90deg,var(--side),var(--acc));opacity:.9}}
.ib{{width:40px;height:40px;display:grid;place-items:center;border:0;background:none;border-radius:10px;color:var(--mu)}}.ib:hover{{background:#EEF1F6;color:var(--tx)}}.ib[aria-expanded="true"]{{background:#E8EDF7;color:var(--az)}}
.lg svg{{height:30px;width:auto;display:block}}.brand{{display:flex;align-items:center;gap:6px;min-width:0}}
.srch{{flex:1;max-width:420px;margin-left:auto;display:flex;align-items:center;gap:8px;height:40px;border:1px solid var(--ln);background:var(--bg);border-radius:10px;padding:0 12px;color:var(--mu);font-size:14px}}.srch kbd{{margin-left:auto;font:500 11px var(--mono);border:1px solid var(--ln);border-radius:6px;padding:1px 6px;background:#fff}}
.dot{{position:relative}}.dot::after{{content:"";position:absolute;top:9px;right:9px;width:8px;height:8px;border-radius:50%;background:#B42318;box-shadow:0 0 0 2px #fff}}
.usr{{display:flex;align-items:center;gap:10px;border:0;background:none;border-radius:999px;padding:4px 10px 4px 4px}}.usr:hover{{background:#EEF1F6}}.av{{width:34px;height:34px;border-radius:50%;background:var(--side);color:#fff;display:grid;place-items:center;font:600 12px var(--sans)}}
.usr b{{display:block;font-weight:600;font-size:13px;line-height:1.2;text-align:left}}.usr small{{display:block;color:var(--mu);font-size:12px;line-height:1.2;text-align:left}}
.pop{{position:absolute;top:calc(var(--nav-h) - 4px);background:var(--sf);border:1px solid var(--ln);border-radius:14px;box-shadow:0 18px 40px -16px rgba(20,27,51,.3);padding:8px;width:320px;max-width:calc(100vw - 24px)}}
.pop h3{{font:600 12px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--mu);margin:6px 10px 6px}}.pop ul{{list-style:none;margin:0;padding:0;display:grid;gap:2px}}
.sw-it{{width:100%;display:flex;align-items:center;gap:12px;border:0;background:none;border-radius:10px;padding:8px 10px;text-align:left}}.sw-it:hover{{background:#F2F4F8}}.sw-it[aria-checked="true"]{{background:#EEF1F6}}
.sw-ic svg{{width:36px;height:36px;border-radius:9px;display:block}}.sw-it b{{display:block;font-weight:600}}.sw-it small{{color:var(--mu);font-size:12px}}
.hub{{display:flex;align-items:center;gap:10px;border-top:1px solid var(--ln);margin-top:6px;padding:10px;color:var(--az);font-weight:500;text-decoration:none;border-radius:10px}}.hub:hover{{background:#F2F4F8}}.hub svg.nn{{height:22px;width:auto}}
.um{{right:12px;width:260px}}.um .hd{{padding:10px;border-bottom:1px solid var(--ln);margin-bottom:6px}}.um .hd b{{display:block}}.um .hd span{{font-size:12px;color:var(--mu)}}.mi{{width:100%;display:flex;align-items:center;gap:10px;border:0;background:none;border-radius:10px;padding:9px 10px;text-align:left}}.mi:hover{{background:#F2F4F8}}
/* cuerpo */
.body{{display:grid;grid-template-columns:var(--side-w) 1fr;min-height:0;transition:grid-template-columns .2s ease}}.app.mini .body{{grid-template-columns:72px 1fr}}
.side{{background:linear-gradient(180deg,var(--side),var(--side2));color:var(--side-tx);padding:14px 12px;display:flex;flex-direction:column;gap:2px;overflow:auto;transition:background .3s}}
.ap{{display:flex;align-items:center;gap:10px;padding:6px 10px 14px;color:#fff;font:600 13px var(--sans);letter-spacing:.04em;text-transform:uppercase;opacity:.75}}
.ni{{display:flex;align-items:center;gap:12px;color:var(--side-tx);text-decoration:none;font:500 14px var(--sans);padding:10px 12px;border-radius:10px;position:relative;white-space:nowrap;min-height:44px}}
.ni:hover{{background:rgba(255,255,255,.07);color:#fff}}.ni[aria-current]{{background:rgba(255,255,255,.1);color:#fff}}.ni[aria-current]::before{{content:"";position:absolute;left:-12px;top:9px;bottom:9px;width:4px;border-radius:0 4px 4px 0;background:var(--acc)}}
.ni[aria-current] .i{{color:var(--acc)}}.side .sp{{flex:1}}.side .ni:focus-visible{{outline-color:#fff}}
.app.mini .ni span,.app.mini .ap span{{display:none}}.app.mini .ni{{justify-content:center;padding:10px}}
.work{{overflow:auto;padding:24px max(16px,env(safe-area-inset-right,0px)) 40px 28px;min-width:0}}
.ruta{{font:500 13px var(--sans);color:var(--mu)}}.wh{{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap;margin-bottom:20px}}.wh h1{{font:600 24px/32px var(--sans);margin:2px 0 0}}.wh p{{color:var(--mu);font:400 13px var(--mono);margin:4px 0 0}}
.mh{{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 24px;align-items:end;margin-bottom:20px}}.mh .ruta{{grid-column:1/-1}}.mh h1{{font:600 24px/32px var(--sans);margin:0}}.mh .ent{{color:var(--mu);margin:2px 0 0}}.mh .cnt{{color:var(--mu);font:400 13px var(--mono);margin:6px 0 0}}
.mh.area{{grid-template-columns:auto minmax(0,1fr) auto;column-gap:16px;border-bottom:3px solid var(--ac);padding-bottom:16px}}.mh.area .ruta{{grid-column:2/-1}}.mh.area .am{{grid-row:2;width:52px;height:52px;align-self:center}}.mh h1 .an{{font-weight:400;color:var(--mu)}}
@media (max-width:640px){{.mh,.mh.area{{grid-template-columns:auto minmax(0,1fr)}}.mh:not(.area){{grid-template-columns:1fr}}.mh .pri{{grid-column:1/-1;justify-self:start}}.mh.area .am{{width:40px;height:40px}}}}
.pri{{height:40px;border:0;border-radius:10px;background:var(--side);color:#fff;font-weight:600;padding:0 16px;box-shadow:0 6px 14px -8px rgba(20,27,51,.5)}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}}.ph{{background:var(--sf);border:1px solid var(--ln);border-radius:14px;padding:18px;min-height:120px;display:grid;gap:10px;align-content:start}}
.ph i{{display:block;height:10px;border-radius:5px;background:#E7EAF0}}.ph i:nth-child(1){{width:40%;height:12px;background:#D9DEE8}}.ph i:nth-child(3){{width:70%}}.big{{grid-column:1/-1;min-height:220px}}
.cap{{font-size:12px;color:var(--mu);margin-top:16px}}
/* anatomía */
.anat [data-anat]{{outline:2px dashed #B42318;outline-offset:-2px;position:relative}}.anat [data-anat]::before{{content:attr(data-anat);position:absolute;z-index:30;top:4px;left:4px;background:#B42318;color:#fff;font:600 11px/1 var(--sans);padding:4px 6px;border-radius:5px;pointer-events:none}}
.tools{{position:fixed;right:max(16px,env(safe-area-inset-right,0px));bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:40;display:flex;gap:8px}}.tools button{{border:1px solid var(--ln);background:var(--sf);border-radius:999px;padding:8px 14px;font-weight:600;box-shadow:0 8px 20px -10px rgba(20,27,51,.35)}}.tools button[aria-pressed="true"]{{background:#B42318;color:#fff;border-color:#B42318}}
.scrim{{display:none}}
@media (max-width:860px){{.body{{grid-template-columns:1fr!important}}.side{{position:fixed;top:var(--nav-h);bottom:0;left:0;width:min(280px,85vw);z-index:15;transform:translateX(-100%);transition:transform .2s ease;padding-left:max(12px,env(safe-area-inset-left,0px))}}
.app.abierto .side{{transform:none}}.app.abierto .scrim{{display:block;position:fixed;inset:var(--nav-h) 0 0 0;background:rgba(20,27,51,.35);z-index:14}}.srch,.usr>span:not(.av),.ocultar-m{{display:none}}.work{{padding:20px max(16px,env(safe-area-inset-left,0px))}}.app.mini .ni span,.app.mini .ap span{{display:inline}}}}
@media (prefers-reduced-motion:reduce){{.body,.side{{transition:none}}}}
</style>
<div class="app" id="app">
<header class="nav" data-anat="Barra superior">
<button class="ib" id="menu" aria-label="Menú lateral" aria-expanded="true" aria-controls="side">{ic('panel-left')}</button>
<button class="ib" id="sw" aria-label="Cambiar de aplicación" aria-haspopup="menu" aria-expanded="false">{ic('grip')}</button>
<a class="brand" href="#" aria-label="Inicio de la aplicación">{logos}</a>
<div class="srch" role="search">{ic('search')}<span>Buscar folio, cliente o parámetro</span><kbd>Ctrl K</kbd></div>
<button class="ib ocultar-m" aria-label="Ayuda">{ic('circle-help')}</button><button class="ib dot" aria-label="Avisos, 2 sin leer">{ic('bell')}</button>
<button class="usr" id="us" aria-haspopup="menu" aria-expanded="false"><span class="av">KM</span><span><b>Karla Méndez</b><small>Supervisión de calidad</small></span>{ic('chevron-down')}</button>
<div class="pop" id="sw-pop" role="menu" aria-label="Aplicaciones" style="left:56px" hidden><h3>Aplicaciones</h3><ul>{switch}</ul><a class="hub" href="#">{NN.replace('<svg ', '<svg class="nn" ', 1)}<span>Ir a todas las aplicaciones</span></a></div>
<div class="pop um" id="us-pop" role="menu" aria-label="Cuenta" hidden><div class="hd"><b>Karla Méndez</b><span>k.mendez@nisanabani.mx</span></div><button class="mi" role="menuitem">{ic('user')}Mi cuenta</button><button class="mi" role="menuitem">{ic('settings')}Preferencias</button><button class="mi" role="menuitem">{ic('log-out')}Cerrar sesión</button></div>
</header>
<div class="body"><nav class="side" id="side" aria-label="Secciones" data-anat="Menú lateral"></nav><div class="scrim" id="scrim"></div>
<main class="work" id="work" data-anat="Área de trabajo"></main></div></div>
<div class="tools"><button id="anat" aria-pressed="false">Ver anatomía</button></div>
<script>
const A={json.dumps(NAVJS, ensure_ascii=False)},S={{settings:{json.dumps(ic('settings'))},help:{json.dumps(ic('circle-help'))}}};
const app=document.getElementById('app'),side=document.getElementById('side'),work=document.getElementById('work'),root=document.documentElement;
let actual='lab';
const AR={json.dumps(AREAJS, ensure_ascii=False)};let pag=null;
function encabezado(a,k){{
 if(k==='lab'){{const p=a.pags[pag],ar=p.area&&AR[p.area];
  if(ar)return `<header class="mh area" style="--ac:${{ar.color}}"><span class="ruta">${{p.sec}} / ${{ar.nombre}}</span>${{ar.svg}}<div><h1>${{p.titulo}} <span class="an">${{ar.nombre}}</span></h1><p class="cnt">${{p.sub}}</p></div><button class="pri">${{p.accion}}</button></header>`;
  return `<header class="mh"><span class="ruta">${{p.sec}} / ${{p.titulo}}</span><div><h1>${{p.titulo}}</h1>${{p.entradilla?`<p class="ent">${{p.entradilla}}</p>`:''}}<p class="cnt">${{p.sub}}</p></div><button class="pri">${{p.accion}}</button></header>`;}}
 return `<header class="mh"><span class="ruta">${{a.nombre}} / ${{a.ruta}}</span><div><h1>${{a.titulo}}</h1><p class="cnt">${{a.sub}}</p></div><button class="pri">${{a.accion}}</button></header>`;}}
function trabajo(){{const a=A[actual];const p=actual==='lab'?a.pags[pag]:null;const nota=actual==='lab'?(p.area?'Encabezado por área (opción B aprobada): marca del área, nombre del área junto al título y línea de su color. Prueba Catálogos o Usuarios para ver la variante global.':'Encabezado global: sin marca ni línea de área. Prueba Recepción o Bitácoras para ver la variante por área.'):'Área de trabajo: aquí vive cada pantalla de '+a.nombre+'. La carcasa no cambia; solo el logo, el color del menú lateral, el acento y las secciones.';
 work.innerHTML=encabezado(a,actual)+`<div class="cards"><div class="ph"><i></i><i></i><i></i></div><div class="ph"><i></i><i></i><i></i></div><div class="ph"><i></i><i></i><i></i></div><div class="ph big"><i></i><i></i><i></i></div></div><p class="cap">${{nota}}</p>`;}}
function pinta(k){{const a=A[k];actual=k;root.style.setProperty('--side',a.side);root.style.setProperty('--side2',a.side2);root.style.setProperty('--acc',a.acc);root.style.setProperty('--side-tx',a.txt);
 document.querySelectorAll('.lg').forEach(l=>l.hidden=l.dataset.app!==k);document.querySelectorAll('.sw-it').forEach(b=>b.setAttribute('aria-checked',b.dataset.go===k));
 const ini=k==='studio'?1:0;pag=k==='lab'?a.nav[0][1]:null;
 side.innerHTML=`<div class="ap"><span>${{a.nombre}}</span></div>`+a.nav.map(([i,t],n)=>`<a href="#" class="ni" data-t="${{t}}"${{n===ini?' aria-current="page"':''}} title="${{t}}">${{i}}<span>${{t}}</span></a>`).join('')+`<div class="sp"></div><a href="#" class="ni" title="Ayuda">${{S.help}}<span>Ayuda</span></a><a href="#" class="ni" title="Configuración">${{S.settings}}<span>Configuración</span></a>`;
 side.querySelectorAll('.ni[data-t]').forEach(el=>el.addEventListener('click',e=>{{e.preventDefault();side.querySelectorAll('.ni').forEach(x=>x.removeAttribute('aria-current'));el.setAttribute('aria-current','page');if(actual==='lab'&&A.lab.pags[el.dataset.t]){{pag=el.dataset.t;trabajo();}}if(matchMedia('(max-width:860px)').matches){{app.classList.remove('abierto');}}}}));
 trabajo();}}
function pop(btn,el,abrir){{const on=abrir??el.hidden;el.hidden=!on;btn.setAttribute('aria-expanded',on);if(on){{el.querySelector('button,a')?.focus();}}}}
const sw=document.getElementById('sw'),swp=document.getElementById('sw-pop'),us=document.getElementById('us'),usp=document.getElementById('us-pop');
sw.addEventListener('click',()=>{{pop(us,usp,false);pop(sw,swp);}});us.addEventListener('click',()=>{{pop(sw,swp,false);pop(us,usp);}});
document.querySelectorAll('.sw-it').forEach(b=>b.addEventListener('click',()=>{{pinta(b.dataset.go);pop(sw,swp,false);sw.focus();}}));
document.addEventListener('keydown',e=>{{if(e.key==='Escape'){{if(!swp.hidden){{pop(sw,swp,false);sw.focus();}}if(!usp.hidden){{pop(us,usp,false);us.focus();}}app.classList.remove('abierto');}}}});
document.addEventListener('click',e=>{{if(!e.target.closest('.pop,#sw,#us')){{pop(sw,swp,false);pop(us,usp,false);}}}});
const menu=document.getElementById('menu'),movil=()=>matchMedia('(max-width:860px)').matches;
menu.addEventListener('click',()=>{{if(movil()){{const on=!app.classList.contains('abierto');app.classList.toggle('abierto',on);menu.setAttribute('aria-expanded',on);}}else{{const mini=!app.classList.contains('mini');app.classList.toggle('mini',mini);menu.setAttribute('aria-expanded',!mini);}}}});
document.getElementById('scrim').addEventListener('click',()=>{{app.classList.remove('abierto');menu.setAttribute('aria-expanded',false);}});
if(movil())menu.setAttribute('aria-expanded',false);
const an=document.getElementById('anat');an.addEventListener('click',()=>{{const on=!app.classList.contains('anat');app.classList.toggle('anat',on);an.setAttribute('aria-pressed',on);an.textContent=on?'Ocultar anatomía':'Ver anatomía';}});
pinta('lab');
</script>'''
open(os.path.join(H, 'shell.html'), 'w').write(html); print('ok')
