# Nisa Nabani · app shell común (NisaLab, NisaData, NisaStudio), prototipo r2: sobrio, tipo Notion.
# Menú lateral gris claro (sin color de app); el selector de apps arriba del menú; área de trabajo blanca con bordes finos.
# El color de cada app solo vive en su ícono, logo, ícono de la sección activa y botón principal.
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
NAVJS = {k: dict(icono=a['icono'], desc=a['desc'], pags=(PAG_LAB if k == 'lab' else None), nombre=a['nombre'], side=a['side'], side2=a['side2'], acc=a['acc'], txt=a['txt'], ruta=a['ruta'], titulo=a['titulo'], sub=a['sub'], accion=a['accion'],
                 nav=[(ic(i), t) for i, t in a['nav']]) for k, a in APPS.items()}
logos = ''.join(f'<span class="lg" data-app="{k}"{"" if k == "lab" else " hidden"}>{a["logo"]}</span>' for k, a in APPS.items())
switch = ''.join(f'<li><button type="button" class="sw-it" data-go="{k}" role="menuitemradio" aria-checked="{"true" if k == "lab" else "false"}"><span class="sw-ic">{a["icono"]}</span><span><b>{a["nombre"]}</b><small>{a["desc"]}</small></span></button></li>' for k, a in APPS.items())
html = f'''<title>App shell Nisa Nabani</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Carcasa común, sobria (tipo Notion): menú lateral gris claro, trabajo en blanco con bordes finos. Cada app solo cambia su ícono, logo y --side (sección activa y botón principal). Tema claro deliberado. */
:root{{--bg:#F2F4F8;--sf:#FFFFFF;--tx:#141B33;--mu:#535B70;--ln:#DFE3EC;--az:#052A76;
--side:#052A76;--side2:#0A3487;--acc:#C2D225;--side-tx:#C9D3EA;--nav-h:60px;--side-w:240px;
--sans:Poppins,system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:light}}
[hidden]{{display:none!important}}*{{box-sizing:border-box}}
html,body{{height:100%}}body{{margin:0;background:var(--bg);color:var(--tx);font:14px/1.5 var(--sans);overflow:hidden}}
button{{font:inherit;color:inherit;cursor:pointer}}.i{{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round;flex:none}}
:focus-visible{{outline:3px solid var(--az);outline-offset:2px}}
.app{{display:grid;grid-template-columns:var(--side-w) 1fr;height:100%;transition:grid-template-columns .2s ease}}.app.mini{{grid-template-columns:68px 1fr}}
/* menú lateral */
.side{{background:#F6F7F9;border-right:1px solid #E6E8EE;padding:10px 8px;display:flex;flex-direction:column;gap:1px;overflow:auto;min-width:0}}
.ws{{display:flex;align-items:center;gap:10px;border:0;background:none;border-radius:8px;padding:6px 8px;text-align:left;width:100%;margin-bottom:10px}}.ws:hover,.ws[aria-expanded="true"]{{background:#ECEEF2}}
.ws .wi svg{{width:28px;height:28px;border-radius:7px;display:block}}.ws>span:not(.wi){{min-width:0}}.ws b{{display:block;font-weight:600;font-size:14px;line-height:1.25}}.ws small{{display:block;color:var(--mu);font-size:12px;line-height:1.25;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}.ws .i{{width:16px;height:16px;margin-left:auto;color:var(--mu)}}
.gl{{font:500 11px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#8A93A8;padding:10px 10px 4px}}
.ni{{display:flex;align-items:center;gap:10px;color:#3A4257;text-decoration:none;font:500 14px var(--sans);padding:7px 10px;border-radius:8px;white-space:nowrap;min-height:36px}}
.ni .i{{width:18px;height:18px;color:#7A8296}}.ni:hover{{background:#ECEEF2;color:var(--tx)}}.ni[aria-current]{{background:#E8EAF0;color:var(--tx);font-weight:600}}.ni[aria-current] .i{{color:var(--side)}}
.side .sp{{flex:1}}.app.mini .ni span,.app.mini .ws>span:not(.wi),.app.mini .ws .i,.app.mini .gl{{display:none}}.app.mini .ni{{justify-content:center}}
/* principal */
.main{{display:grid;grid-template-rows:auto 1fr;min-width:0;min-height:0;background:#FFFFFF}}
.nav{{display:flex;align-items:center;gap:6px;height:52px;padding:0 max(12px,env(safe-area-inset-right,0px)) 0 12px;border-bottom:1px solid #EEF0F3;position:relative;z-index:20}}
.ib{{width:36px;height:36px;display:grid;place-items:center;border:0;background:none;border-radius:8px;color:#7A8296}}.ib:hover{{background:#F2F3F6;color:var(--tx)}}.ib .i{{width:18px;height:18px}}
.miga{{font:500 13px var(--sans);color:var(--mu);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}}.miga b{{color:var(--tx);font-weight:500}}
.srch{{margin-left:auto;display:flex;align-items:center;gap:8px;height:34px;border:1px solid #E6E8EE;border-radius:8px;padding:0 10px;color:#8A93A8;font-size:13px;min-width:240px}}.srch .i{{width:16px;height:16px}}.srch kbd{{margin-left:auto;font:500 11px var(--mono);color:#8A93A8}}
.dot{{position:relative}}.dot::after{{content:"";position:absolute;top:8px;right:8px;width:7px;height:7px;border-radius:50%;background:#B42318;box-shadow:0 0 0 2px #fff}}
.usr{{display:flex;align-items:center;gap:8px;border:0;background:none;border-radius:8px;padding:4px 6px}}.usr:hover{{background:#F2F3F6}}.av{{width:28px;height:28px;border-radius:50%;background:#E8EAF0;color:#3A4257;display:grid;place-items:center;font:600 11px var(--sans)}}.usr .i{{width:16px;height:16px;color:#8A93A8}}
.pop{{position:absolute;background:#fff;border:1px solid #E6E8EE;border-radius:12px;box-shadow:0 1px 2px rgba(20,27,51,.04),0 12px 32px -12px rgba(20,27,51,.22);padding:6px;width:300px;max-width:calc(100vw - 24px);z-index:30}}
.pop h3{{font:500 11px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:#8A93A8;margin:6px 8px}}.pop ul{{list-style:none;margin:0;padding:0;display:grid;gap:1px}}
.sw-it{{width:100%;display:flex;align-items:center;gap:10px;border:0;background:none;border-radius:8px;padding:7px 8px;text-align:left}}.sw-it:hover{{background:#F4F5F7}}.sw-it[aria-checked="true"]{{background:#EEF0F4}}
.sw-ic svg{{width:30px;height:30px;border-radius:7px;display:block}}.sw-it b{{display:block;font-weight:600;font-size:14px}}.sw-it small{{color:var(--mu);font-size:12px}}
.hub{{display:flex;align-items:center;gap:10px;border-top:1px solid #EEF0F3;margin-top:6px;padding:10px 8px 6px;color:var(--tx);font-weight:500;font-size:13px;text-decoration:none;border-radius:8px}}.hub:hover{{background:#F4F5F7}}.hub svg.nn{{height:18px;width:auto}}
.um{{right:12px;top:48px;width:240px}}.um .hd{{padding:8px 10px;border-bottom:1px solid #EEF0F3;margin-bottom:4px}}.um .hd b{{display:block;font-size:14px}}.um .hd span{{font-size:12px;color:var(--mu)}}.mi{{width:100%;display:flex;align-items:center;gap:10px;border:0;background:none;border-radius:8px;padding:8px 10px;text-align:left;font-size:14px}}.mi .i{{width:16px;height:16px;color:#7A8296}}.mi:hover{{background:#F4F5F7}}
#sw-pop{{left:8px;top:52px}}
.work{{overflow:auto;padding:32px max(24px,env(safe-area-inset-right,0px)) 48px 40px;min-width:0}}.work>*{{max-width:1080px}}
.mh{{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 24px;align-items:end;margin-bottom:24px}}.mh h1{{font:600 26px/34px var(--sans);margin:0;letter-spacing:-.01em}}.mh .ent{{color:var(--mu);margin:4px 0 0}}.mh .cnt{{color:var(--mu);font:400 13px var(--mono);margin:6px 0 0}}
.mh.area{{grid-template-columns:auto minmax(0,1fr) auto;column-gap:16px;border-bottom:3px solid var(--ac);padding-bottom:16px}}.mh.area .am{{grid-row:1;width:52px;height:52px;align-self:center}}.mh h1 .an{{font-weight:400;color:var(--mu)}}
@media (max-width:640px){{.mh{{grid-template-columns:1fr}}.mh.area{{grid-template-columns:auto minmax(0,1fr)}}.mh .pri{{grid-column:1/-1;justify-self:start}}.mh.area .am{{width:40px;height:40px}}}}
.pri{{height:36px;border:0;border-radius:8px;background:var(--side);color:#fff;font-weight:600;font-size:14px;padding:0 14px}}.pri:hover{{filter:brightness(1.12)}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}}.ph{{background:#fff;border:1px solid #E6E8EE;border-radius:10px;padding:16px;min-height:110px;display:grid;gap:10px;align-content:start;box-shadow:0 1px 2px rgba(20,27,51,.03)}}
.ph i{{display:block;height:9px;border-radius:5px;background:#EEF0F3}}.ph i:nth-child(1){{width:40%;height:11px;background:#E3E6EC}}.ph i:nth-child(3){{width:70%}}.big{{grid-column:1/-1;min-height:220px}}
.cap{{font-size:12px;color:var(--mu);margin-top:16px}}
/* anatomía */
.anat [data-anat]{{outline:2px dashed #B42318;outline-offset:-2px;position:relative}}.anat [data-anat]::before{{content:attr(data-anat);position:absolute;z-index:30;top:4px;left:4px;background:#B42318;color:#fff;font:600 11px/1 var(--sans);padding:4px 6px;border-radius:5px;pointer-events:none}}
.tools{{position:fixed;right:max(16px,env(safe-area-inset-right,0px));bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:40;display:flex;gap:8px}}.tools button{{border:1px solid var(--ln);background:var(--sf);border-radius:999px;padding:8px 14px;font-weight:600;box-shadow:0 8px 20px -10px rgba(20,27,51,.35)}}.tools button[aria-pressed="true"]{{background:#B42318;color:#fff;border-color:#B42318}}
.scrim{{display:none}}
@media (max-width:860px){{.app,.app.mini{{grid-template-columns:1fr}}.side{{position:fixed;inset:0 auto 0 0;width:min(280px,85vw);z-index:25;transform:translateX(-100%);transition:transform .2s ease;padding-left:max(8px,env(safe-area-inset-left,0px));padding-top:calc(10px + env(safe-area-inset-top,0px))}}
.app.abierto .side{{transform:none;box-shadow:0 0 40px rgba(20,27,51,.2)}}.app.abierto .scrim{{display:block;position:fixed;inset:0;background:rgba(20,27,51,.3);z-index:24}}.srch{{display:none}}.work{{padding:20px max(16px,env(safe-area-inset-right,0px)) 40px max(16px,env(safe-area-inset-left,0px))}}.app.mini .ni span,.app.mini .gl,.app.mini .ws>span:not(.wi){{display:inline}}#sw-pop{{left:8px;top:56px}}}}
@media (prefers-reduced-motion:reduce){{.app,.side{{transition:none}}}}
</style>
<div class="app" id="app">
<nav class="side" id="side" aria-label="Secciones" data-anat="Menú lateral"></nav><div class="scrim" id="scrim"></div>
<div class="main"><header class="nav" data-anat="Barra superior">
<button class="ib" id="menu" aria-label="Menú lateral" aria-expanded="true" aria-controls="side">{ic('panel-left')}</button>
<span class="miga" id="miga"></span>
<div class="srch" role="search">{ic('search')}<span>Buscar</span><kbd>Ctrl K</kbd></div>
<button class="ib" aria-label="Ayuda">{ic('circle-help')}</button><button class="ib dot" aria-label="Avisos, 2 sin leer">{ic('bell')}</button>
<button class="usr" id="us" aria-label="Cuenta de Karla Méndez" aria-haspopup="menu" aria-expanded="false"><span class="av">KM</span>{ic('chevron-down')}</button>
<div class="pop um" id="us-pop" role="menu" aria-label="Cuenta" hidden><div class="hd"><b>Karla Méndez</b><span>Supervisión de calidad · k.mendez@nisanabani.mx</span></div><button class="mi" role="menuitem">{ic('user')}Mi cuenta</button><button class="mi" role="menuitem">{ic('settings')}Preferencias</button><button class="mi" role="menuitem">{ic('log-out')}Cerrar sesión</button></div>
</header><main class="work" id="work" data-anat="Área de trabajo"></main></div>
<div class="pop" id="sw-pop" role="menu" aria-label="Aplicaciones" hidden><h3>Aplicaciones</h3><ul>{switch}</ul><a class="hub" href="#">{NN.replace('<svg ', '<svg class="nn" ', 1)}<span>Todas las aplicaciones</span></a></div>
</div>
<div class="tools"><button id="anat" aria-pressed="false">Ver anatomía</button></div>
<script>
const A={json.dumps(NAVJS, ensure_ascii=False)},S={{chev:{json.dumps(ic('chevron-down'))},settings:{json.dumps(ic('settings'))},help:{json.dumps(ic('circle-help'))}}};
const app=document.getElementById('app'),side=document.getElementById('side'),work=document.getElementById('work'),root=document.documentElement;
let actual='lab';
const AR={json.dumps(AREAJS, ensure_ascii=False)};let pag=null;
function encabezado(a,k){{
 if(k==='lab'){{const p=a.pags[pag],ar=p.area&&AR[p.area];
  if(ar)return `<header class="mh area" style="--ac:${{ar.color}}">${{ar.svg}}<div><h1>${{p.titulo}} <span class="an">${{ar.nombre}}</span></h1><p class="cnt">${{p.sub}}</p></div><button class="pri">${{p.accion}}</button></header>`;
  return `<header class="mh"><div><h1>${{p.titulo}}</h1>${{p.entradilla?`<p class="ent">${{p.entradilla}}</p>`:''}}<p class="cnt">${{p.sub}}</p></div><button class="pri">${{p.accion}}</button></header>`;}}
 return `<header class="mh"><div><h1>${{a.titulo}}</h1><p class="cnt">${{a.sub}}</p></div><button class="pri">${{a.accion}}</button></header>`;}}
function trabajo(){{const a=A[actual];const pg=actual==='lab'?a.pags[pag]:null;document.getElementById('miga').innerHTML=actual==='lab'?(pg.area?`${{pg.sec}} / <b>${{AR[pg.area].nombre}}</b>`:`${{pg.sec}} / <b>${{pg.titulo}}</b>`):`<b>${{a.ruta}}</b>`;const p=actual==='lab'?a.pags[pag]:null;const nota=actual==='lab'?(p.area?'Encabezado por área (opción B aprobada): marca del área, nombre del área junto al título y línea de su color. Prueba Catálogos o Usuarios para ver la variante global.':'Encabezado global: sin marca ni línea de área. Prueba Recepción o Bitácoras para ver la variante por área.'):'Área de trabajo: aquí vive cada pantalla de '+a.nombre+'. La carcasa no cambia; solo el ícono de la app, el color de la sección activa y del botón principal, y las secciones.';
 work.innerHTML=encabezado(a,actual)+`<div class="cards"><div class="ph"><i></i><i></i><i></i></div><div class="ph"><i></i><i></i><i></i></div><div class="ph"><i></i><i></i><i></i></div><div class="ph big"><i></i><i></i><i></i></div></div><p class="cap">${{nota}}</p>`;}}
function pinta(k){{const a=A[k];actual=k;root.style.setProperty('--side',a.side);root.style.setProperty('--side2',a.side2);root.style.setProperty('--acc',a.acc);root.style.setProperty('--side-tx',a.txt);
 document.querySelectorAll('.sw-it').forEach(b=>b.setAttribute('aria-checked',b.dataset.go===k));
 const ini=k==='studio'?1:0;pag=k==='lab'?a.nav[0][1]:null;
 side.innerHTML=`<button class="ws" id="sw" aria-haspopup="menu" aria-expanded="false" aria-label="Cambiar de aplicación"><span class="wi">${{a.icono}}</span><span><b>${{a.nombre}}</b><small>${{a.desc}}</small></span>${{S.chev}}</button><div class="gl">Secciones</div>`+a.nav.map(([i,t],n)=>`<a href="#" class="ni" data-t="${{t}}"${{n===ini?' aria-current="page"':''}} title="${{t}}">${{i}}<span>${{t}}</span></a>`).join('')+`<div class="sp"></div><a href="#" class="ni" title="Ayuda">${{S.help}}<span>Ayuda</span></a><a href="#" class="ni" title="Configuración">${{S.settings}}<span>Configuración</span></a>`;
 side.querySelectorAll('.ni[data-t]').forEach(el=>el.addEventListener('click',e=>{{e.preventDefault();side.querySelectorAll('.ni').forEach(x=>x.removeAttribute('aria-current'));el.setAttribute('aria-current','page');if(actual==='lab'&&A.lab.pags[el.dataset.t]){{pag=el.dataset.t;trabajo();}}if(matchMedia('(max-width:860px)').matches){{app.classList.remove('abierto');}}}}));
 document.getElementById('sw').addEventListener('click',()=>{{pop(us,usp,false);pop(document.getElementById('sw'),swp);}});
 trabajo();}}
function pop(btn,el,abrir){{const on=abrir??el.hidden;el.hidden=!on;btn.setAttribute('aria-expanded',on);if(on){{el.querySelector('button,a')?.focus();}}}}
const swp=document.getElementById('sw-pop'),us=document.getElementById('us'),usp=document.getElementById('us-pop');const sw={{focus:()=>document.getElementById('sw').focus(),setAttribute:(a,v)=>document.getElementById('sw').setAttribute(a,v)}};
us.addEventListener('click',()=>{{pop(sw,swp,false);pop(us,usp);}});
document.querySelectorAll('.sw-it').forEach(b=>b.addEventListener('click',()=>{{pinta(b.dataset.go);pop(sw,swp,false);sw.focus();}}));
document.addEventListener('keydown',e=>{{if(e.key==='Escape'){{if(!swp.hidden){{pop(sw,swp,false);sw.focus();}}if(!usp.hidden){{pop(us,usp,false);us.focus();}}app.classList.remove('abierto');}}}});
document.addEventListener('click',e=>{{if(!e.target.closest('.pop,.ws,#us')){{pop(sw,swp,false);pop(us,usp,false);}}}});
const menu=document.getElementById('menu'),movil=()=>matchMedia('(max-width:860px)').matches;
menu.addEventListener('click',()=>{{if(movil()){{const on=!app.classList.contains('abierto');app.classList.toggle('abierto',on);menu.setAttribute('aria-expanded',on);}}else{{const mini=!app.classList.contains('mini');app.classList.toggle('mini',mini);menu.setAttribute('aria-expanded',!mini);}}}});
document.getElementById('scrim').addEventListener('click',()=>{{app.classList.remove('abierto');menu.setAttribute('aria-expanded',false);}});
if(movil())menu.setAttribute('aria-expanded',false);
const an=document.getElementById('anat');an.addEventListener('click',()=>{{const on=!app.classList.contains('anat');app.classList.toggle('anat',on);an.setAttribute('aria-pressed',on);an.textContent=on?'Ocultar anatomía':'Ver anatomía';}});
pinta('lab');
</script>'''
open(os.path.join(H, 'shell.html'), 'w').write(html); print('ok')
