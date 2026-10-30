# hub.nisanabani.com · puerta de entrada a las aplicaciones de Nisa Nabani (personal interno), prototipo r1.
# Una sola cuenta → lanzador con las apps a las que la persona tiene acceso (hoy NisaLab y NisaData). La marca de la puerta es la de la empresa, no un producto.
# Uso: python3 gen.py → hub.html (para publicar como Artifact)
import os, re
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..')
def sv(ruta, st):
    s = re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(NS, ruta)).read().strip())
    s = re.sub(r'\s(width|height)="[^"]*"', '', s.split('>', 1)[0]) + '>' + s.split('>', 1)[1]
    return s.replace('<svg ', f'<svg style="{st}" aria-hidden="true" focusable="false" ', 1)
NN = sv('nabi-design-system/marca-nisa/nisa-nabani-logo.svg', 'height:44px;width:auto;display:block;max-width:100%')
NN_s = NN.replace('height:44px', 'height:30px')
NN_w = NN.replace('rgb(1.998901%, 16.499329%, 46.299744%)', '#FFFFFF').replace('height:44px', 'height:52px')
NN_m = NN.replace('height:44px', 'height:36px')
LAB = sv('nisalab-final/svg/app-icon.svg', 'width:56px;height:56px;border-radius:14px;display:block;flex:none')
DAT = sv('nisadata-final/svg/app-icon.svg', 'width:56px;height:56px;border-radius:14px;display:block;flex:none')
LAB_s, DAT_s = LAB.replace('56px;height:56px;border-radius:14px', '28px;height:28px;border-radius:7px'), DAT.replace('56px;height:56px;border-radius:14px', '28px;height:28px;border-radius:7px')
LAB_W = sv('nisalab-final/svg/logotipo.svg', 'height:26px;width:auto;display:block')
DAT_W = sv('nisadata-final/svg/logotipo.svg', 'height:26px;width:auto;display:block')
html = f'''<title>Aplicaciones Nisa Nabani</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Puerta de entrada interna: la marca de la empresa arriba, las apps como objetos grandes y tocables. Papel de laboratorio, azul real para la acción. Tema claro deliberado. */
:root{{--bg:#F2F4F8;--sf:#FFFFFF;--tx:#141B33;--mu:#535B70;--ln:#DFE3EC;--az:#052A76;--az-h:#021C52;--pe:#C2D225;--err:#A11D1D;
--sans:Poppins,system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:light}}
[hidden]{{display:none!important}}*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--tx);font:15px/1.55 var(--sans);padding-block:0 40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
h1,h2,h3{{margin:0;text-wrap:balance}}p{{margin:0}}button,input{{font:inherit}}
:focus-visible{{outline:3px solid var(--az);outline-offset:2px}}
/* acceso: panel de marca + formulario */
.acc{{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);min-height:max(640px,100dvh);margin-inline:calc(-1 * max(16px,env(safe-area-inset-left,0px)));margin-bottom:-40px}}
.marca{{position:relative;overflow:hidden;background:var(--az);color:#fff;padding:40px clamp(28px,5vw,64px);display:flex;flex-direction:column;justify-content:space-between;gap:32px}}
.cel i{{position:absolute;border-radius:50%;background:#0B3A93;will-change:transform}}.cel .c1{{width:420px;height:420px;right:-120px;bottom:-140px;background:#0A3487}}.cel .c2{{width:230px;height:230px;right:150px;top:-60px;background:#0C3C98}}
.cel .c3{{width:150px;height:150px;right:70px;top:150px;background:var(--pe)}}.cel .c4{{width:90px;height:90px;right:250px;bottom:170px;background:#1446A8}}.cel .c5{{width:46px;height:46px;right:40px;top:90px;background:#00B4D8}}.cel .c6{{width:24px;height:24px;right:360px;top:120px;background:#2C5BBE}}
@media (prefers-reduced-motion:no-preference){{.cel .c1{{animation:fl 18s ease-in-out infinite}}.cel .c2{{animation:fl 22s ease-in-out infinite reverse}}.cel .c3{{animation:fl 14s ease-in-out infinite}}.cel .c4{{animation:fl 16s ease-in-out infinite reverse}}.cel .c5{{animation:fl 11s ease-in-out infinite}}
@keyframes fl{{50%{{transform:translate(-10px,12px) scale(1.03)}}}}}}
.mt,.mm,.mb{{position:relative}}.mm h2{{font:600 clamp(28px,3.2vw,40px)/1.15 var(--sans);letter-spacing:-.01em;max-width:13ch}}
.prods{{list-style:none;margin:22px 0 0;padding:0;display:grid;gap:12px}}.prods li{{display:flex;align-items:center;gap:12px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:10px 14px;max-width:340px;backdrop-filter:blur(6px)}}
.prods svg{{width:36px!important;height:36px!important;border-radius:9px!important;box-shadow:0 0 0 1px rgba(255,255,255,.25)}}.prods b{{display:block;font-weight:600}}.prods span{{font-size:13px;color:#C9D3EA;line-height:1.3}}.prods span b{{color:#fff;font-size:15px}}
.mb{{font:500 12px var(--mono);color:#9FB0D6}}
.form{{background:var(--sf);display:grid;place-items:center;padding:40px 24px}}.fi-in{{width:100%;max-width:380px;display:grid;gap:24px}}
.fi-in h1{{font:600 26px/1.2 var(--sans)}}.sub{{color:var(--mu);font-size:14px;margin-top:4px}}.solo-movil{{display:none}}
form{{display:grid;gap:14px}}label{{display:grid;gap:6px;font:500 14px var(--sans)}}
.fld{{position:relative;display:flex;align-items:center}}.fld svg{{position:absolute;left:12px;width:18px;height:18px;fill:none;stroke:#8A93A8;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;pointer-events:none;transition:stroke .15s}}
.fld input{{width:100%;height:48px;border:1px solid #C9CED8;border-radius:12px;padding:0 12px 0 40px;color:var(--tx);background:var(--bg);transition:border-color .15s,box-shadow .15s,background .15s}}
.fld input:focus{{outline:none;border-color:var(--az);background:#fff;box-shadow:0 0 0 4px #E8EDF7}}.fld:focus-within svg{{stroke:var(--az)}}.fld input[aria-invalid="true"]{{border-color:var(--err);box-shadow:0 0 0 4px #FCE4E4}}
.ver{{position:absolute;right:6px;height:36px;border:0;background:none;color:var(--az);font:600 13px var(--sans);padding:0 10px;border-radius:8px;cursor:pointer}}.ver:hover{{background:#EEF1F6}}#clave{{padding-right:84px}}
.err{{color:var(--err);font-size:13px;margin-top:-6px}}.fila{{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}}
.chk{{display:flex;align-items:center;gap:8px;font:400 14px var(--sans);color:var(--mu);cursor:pointer}}.chk input{{width:18px;height:18px;accent-color:var(--az);margin:0}}
.pri{{position:relative;height:50px;border:0;border-radius:12px;background:var(--az);color:#fff;font-weight:600;font-size:16px;cursor:pointer;box-shadow:inset 0 1px 0 rgba(255,255,255,.16),0 8px 18px -8px rgba(5,42,118,.55);transition:background .15s,transform .15s,box-shadow .15s}}
.pri:hover{{background:var(--az-h);transform:translateY(-1px);box-shadow:inset 0 1px 0 rgba(255,255,255,.18),0 12px 22px -10px rgba(5,42,118,.6)}}.pri:active{{transform:none}}
.carga{{display:none;gap:6px;align-items:center;justify-content:center}}.carga i{{width:8px;height:8px;border-radius:50%;background:#fff;animation:pu .9s ease-in-out infinite}}.carga i:nth-child(2){{animation-delay:.15s}}.carga i:nth-child(3){{animation-delay:.3s;background:var(--pe)}}
@keyframes pu{{50%{{transform:scale(.5);opacity:.6}}}}.pri.cargando .lbl{{display:none}}.pri.cargando .carga{{display:flex}}
.lnk{{color:var(--az);font:500 14px var(--sans);background:none;border:0;padding:4px 0;cursor:pointer}}.aviso{{font-size:13px;color:var(--mu);border-top:1px solid var(--ln);padding-top:16px}}
@media (max-width:860px){{.acc{{grid-template-columns:1fr;min-height:0}}.marca{{min-height:220px;padding:24px max(16px,env(safe-area-inset-left,0px))}}.mm h2{{font-size:26px}}.prods{{display:none}}.mt{{display:none}}.form{{padding:28px 16px 48px}}.solo-movil{{display:block}}}}
/* lanzador */
.top{{max-width:1080px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:20px 0}}
.who{{display:flex;align-items:center;gap:10px;background:var(--sf);border:1px solid var(--ln);border-radius:999px;padding:4px 14px 4px 4px;font-size:14px;cursor:pointer}}.av{{width:32px;height:32px;border-radius:50%;background:#E8EDF7;color:var(--az);display:grid;place-items:center;font:600 12px var(--sans)}}
.who small{{display:block;color:var(--mu);font-size:12px;line-height:1.2}}.who b{{display:block;font-weight:600;line-height:1.2}}
main.lz{{max-width:1080px;margin:0 auto;display:grid;gap:22px}}.hola h1{{font:600 28px/1.25 var(--sans)}}.hola p{{color:var(--mu)}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.app{{background:var(--sf);border:1px solid var(--ln);border-radius:18px;padding:22px;display:grid;gap:16px;text-decoration:none;color:inherit;transition:box-shadow .15s ease,transform .15s ease;min-width:0}}
.app:hover{{box-shadow:0 1px 2px rgba(20,27,51,.05),0 14px 30px -18px rgba(5,42,118,.35);transform:translateY(-2px)}}
.an{{font:400 24px/1.1 var(--sans);letter-spacing:-.01em}}.an b{{font-weight:700}}.ah{{display:flex;align-items:center;gap:14px}}.ah p{{color:var(--mu);font-size:14px;margin-top:4px}}
.dato{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}}.dato div{{background:var(--bg);border-radius:12px;padding:12px 14px;min-width:0}}.dato b{{display:block;font:600 20px var(--sans)}}.dato span{{font-size:12px;color:var(--mu)}}
.ult{{font-size:13px;color:var(--mu);display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;align-items:center}}.abrir{{font:600 14px var(--sans);color:var(--az);white-space:nowrap}}
.nota{{font-size:13px;color:var(--mu);border:1px dashed #B9C0CE;border-radius:14px;padding:14px 16px}}
.pie{{max-width:1080px;margin:28px auto 0;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;font-size:12px;color:var(--mu)}}.pie span{{font-family:var(--mono)}}
@media (max-width:760px){{.grid{{grid-template-columns:1fr}}.card{{padding:24px}}.who small{{display:none}}}}
@media (prefers-reduced-motion:reduce){{.app{{transition:none}}.app:hover{{transform:none}}}}
</style>
<section class="acc" id="v-acceso" aria-label="Iniciar sesión">
<div class="marca" aria-hidden="false"><div class="cel" aria-hidden="true"><i class="c1"></i><i class="c2"></i><i class="c3"></i><i class="c4"></i><i class="c5"></i><i class="c6"></i></div>
<div class="mt">{NN_w}</div><div class="mm"><h2>Todo el laboratorio,<br>con una sola cuenta.</h2>
<ul class="prods"><li>{LAB_s}<span><b>NisaLab</b>Muestras, resultados e informes</span></li><li>{DAT_s}<span><b>NisaData</b>Tendencias y salud del laboratorio</span></li></ul></div>
<p class="mb">hub.nisanabani.com</p></div>
<div class="form"><div class="fi-in"><div class="solo-movil">{NN_m}</div><div><h1>Inicia sesión</h1><p class="sub">Usa tu cuenta del laboratorio.</p></div>
<form id="f" novalidate><label for="correo">Correo<span class="fld"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg><input id="correo" type="email" autocomplete="username" value="k.mendez@nisanabani.mx" aria-describedby="e-correo"></span></label><span class="err" id="e-correo" hidden>Escribe tu correo del laboratorio.</span>
<label for="clave">Contraseña<span class="fld"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg><input id="clave" type="password" autocomplete="current-password" aria-describedby="e-clave"><button type="button" class="ver" id="ver" aria-pressed="false">Mostrar</button></span></label><span class="err" id="e-clave" hidden>Escribe tu contraseña.</span>
<div class="fila"><label class="chk" for="rec"><input type="checkbox" id="rec" checked> Recordarme en este equipo</label><button class="lnk" type="button">Olvidé mi contraseña</button></div>
<button class="pri" type="submit" id="entrar"><span class="lbl">Entrar</span><span class="carga" aria-hidden="true"><i></i><i></i><i></i></span></button></form>
<p class="aviso">Solo personal de Nisa Nabani. Si no tienes cuenta, pídela a Administración.</p></div></div></section>
<div id="v-apps" hidden>
<header class="top">{NN_s}<button class="who" type="button" aria-haspopup="menu"><span class="av">KM</span><span><b>Karla Méndez</b><small>Supervisión de calidad</small></span></button></header>
<main class="lz"><div class="hola"><h1>Buenos días, Karla</h1><p>Elige con qué vas a trabajar. Ves solo las aplicaciones a las que tienes acceso.</p></div>
<div class="grid">
<a class="app" href="#"><div class="ah">{LAB}<div><h2 class="an" style="color:#052A76"><b>Nisa</b>Lab</h2><p>Recepción de muestras, captura de resultados, bitácoras e informes.</p></div></div>
<div class="dato"><div><b>18</b><span>muestras por ingresar</span></div><div><b>7</b><span>informes por generar</span></div></div>
<div class="ult"><span>Última vez: Recepción · Aguas, hoy 08:12</span><span class="abrir">Abrir NisaLab →</span></div></a>
<a class="app" href="#"><div class="ah">{DAT}<div><h2 class="an" style="color:#1F2532"><b>Nisa</b>Data</h2><p>Tendencias, comportamiento y salud del laboratorio.</p></div></div>
<div class="dato"><div><b>3.6 días</b><span>tiempo de entrega · meta 4</span></div><div><b>91 %</b><span>entregadas a tiempo</span></div></div>
<div class="ult"><span>Última vez: Panel, ayer 17:40</span><span class="abrir">Abrir NisaData →</span></div></a></div>
<p class="nota">Cuando se sume otra aplicación (por ejemplo, la administración de NisaResults) aparece aquí como una tarjeta más, solo para quien tenga permiso. Datos de ejemplo.</p></main>
<footer class="pie"><span>hub.nisanabani.com</span><button class="lnk" type="button" id="salir">Cerrar sesión</button></footer></div>
<script>
const f=document.getElementById('f'),ok=(id,v)=>{{const i=document.getElementById(id),e=document.getElementById('e-'+id);i.setAttribute('aria-invalid',!v);e.hidden=v;return v;}};
f.addEventListener('submit',ev=>{{ev.preventDefault();const a=ok('correo',f.correo.value.trim().includes('@')),b=ok('clave',f.clave.value.length>0);
 if(!a){{f.correo.focus();return;}}if(!b){{f.clave.focus();return;}}const be=document.getElementById('entrar');be.classList.add('cargando');be.setAttribute('aria-busy','true');setTimeout(()=>{{be.classList.remove('cargando');be.removeAttribute('aria-busy');document.getElementById('v-acceso').hidden=true;document.getElementById('v-apps').hidden=false;document.querySelector('.hola h1').setAttribute('tabindex','-1');document.querySelector('.hola h1').focus();}},700);}});
const ver=document.getElementById('ver');ver.addEventListener('click',()=>{{const on=f.clave.type==='password';f.clave.type=on?'text':'password';ver.textContent=on?'Ocultar':'Mostrar';ver.setAttribute('aria-pressed',on);}});
document.getElementById('salir').addEventListener('click',()=>{{document.getElementById('v-apps').hidden=true;document.getElementById('v-acceso').hidden=false;f.clave.value='';f.clave.focus();}});
</script>'''
open(os.path.join(H, 'hub.html'), 'w').write(html); print('ok')
