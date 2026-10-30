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
/* acceso */
.acc{{min-height:100%;display:grid;place-items:center;padding-block:40px}}
.card{{width:100%;max-width:420px;background:var(--sf);border:1px solid var(--ln);border-radius:20px;padding:32px;display:grid;gap:22px;box-shadow:0 1px 2px rgba(20,27,51,.05),0 18px 40px -24px rgba(5,42,118,.25)}}
.card h1{{font:600 22px/1.3 var(--sans)}}.card .sub{{color:var(--mu);font-size:14px;margin-top:4px}}
form{{display:grid;gap:14px}}label{{display:grid;gap:6px;font:500 14px var(--sans)}}
input{{height:46px;border:1px solid #858DA3;border-radius:10px;padding:0 12px;color:var(--tx);background:#fff;box-shadow:inset 0 1px 1px rgba(20,27,51,.05)}}input:focus{{outline:none;border-color:var(--az);box-shadow:0 0 0 3px #E8EDF7}}
input[aria-invalid="true"]{{border-color:var(--err)}}.err{{color:var(--err);font-size:13px}}
.pri{{height:48px;border:0;border-radius:10px;background:var(--az);color:#fff;font-weight:600;cursor:pointer;box-shadow:inset 0 1px 0 rgba(255,255,255,.16),0 6px 14px -6px rgba(5,42,118,.45)}}.pri:hover{{background:var(--az-h)}}
.lnk{{color:var(--az);font:500 14px var(--sans);background:none;border:0;padding:4px 0;cursor:pointer;justify-self:start}}
.apps-mini{{display:flex;align-items:center;gap:10px;border-top:1px solid var(--ln);padding-top:18px;font-size:13px;color:var(--mu)}}.apps-mini span:first-of-type{{margin-left:4px}}
.url{{font:500 12px var(--mono);color:var(--mu);text-align:center;margin-top:14px}}
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
<div><div class="card">{NN}<div><h1>Aplicaciones de Nisa Nabani</h1><p class="sub">Entra con tu cuenta del laboratorio. Es la misma para todas las aplicaciones.</p></div>
<form id="f" novalidate><label for="correo">Correo<input id="correo" type="email" autocomplete="username" value="k.mendez@nisanabani.mx" aria-describedby="e-correo"></label><span class="err" id="e-correo" hidden>Escribe tu correo del laboratorio.</span>
<label for="clave">Contraseña<input id="clave" type="password" autocomplete="current-password" aria-describedby="e-clave"></label><span class="err" id="e-clave" hidden>Escribe tu contraseña.</span>
<button class="pri" type="submit">Entrar</button><button class="lnk" type="button">Olvidé mi contraseña</button></form>
<div class="apps-mini">{LAB_s}{DAT_s}<span>Una cuenta para NisaLab y NisaData</span></div></div>
<p class="url">hub.nisanabani.com · solo personal de Nisa Nabani</p></div></section>
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
 if(!a){{f.correo.focus();return;}}if(!b){{f.clave.focus();return;}}document.getElementById('v-acceso').hidden=true;document.getElementById('v-apps').hidden=false;document.querySelector('.hola h1').setAttribute('tabindex','-1');document.querySelector('.hola h1').focus();}});
document.getElementById('salir').addEventListener('click',()=>{{document.getElementById('v-apps').hidden=true;document.getElementById('v-acceso').hidden=false;f.clave.value='';f.clave.focus();}});
</script>'''
open(os.path.join(H, 'hub.html'), 'w').write(html); print('ok')
