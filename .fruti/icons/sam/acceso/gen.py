# SAM · login y galería de correos (artifact). Genera acceso.html.
import os, json, re, base64, html as H
B = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(B, '..')
def cuerpo(n):
    s = open(os.path.join(S, 'final', n)).read(); s = re.sub(r'<title>.*?</title>', '', s)
    return s[s.index('>', s.index('<svg')) + 1: s.rindex('</svg>')].strip()
def vb(n): return re.search(r'viewBox="([^"]+)"', open(os.path.join(S, 'final', n)).read()).group(1)
C2 = cuerpo('sam-simbolo.svg').replace('var(--g-color-brand,#c6f432)', 'var(--brand)').replace('var(--sam-tinta,#0a0a0b)', 'var(--on-brand)')
LOGOC = cuerpo('sam-logotipo-compacto.svg').replace('var(--g-color-brand,#c6f432)', 'var(--brand)').replace('var(--sam-tinta,#0a0a0b)', 'var(--on-brand)')
LOGOH = cuerpo('sam-logotipo-horizontal.svg').replace('var(--g-color-brand,#c6f432)', 'var(--brand)').replace('var(--sam-tinta,#0a0a0b)', 'var(--on-brand)')
png = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(S, 'correos', 'sam-logo-correo@2x.png'), 'rb').read()).decode()
M = json.load(open(os.path.join(S, 'correos', 'muestras.json')))
grupos = []
for m in M:
    if m['grupo'] not in grupos: grupos.append(m['grupo'])
galeria = ''
for g in grupos:
    items = ''
    for i, m in enumerate([x for x in M if x['grupo'] == g]):
        src = H.escape(m['html'].replace('LOGO', png), quote=True)
        items += (f'<figure class="mail"><figcaption><span class="eti">{m["nombre"]} · <code>plantillas/{m["id"]}.html</code></span>'
                  f'<span class="asunto"><span class="k">Asunto</span> {H.escape(m["asunto"])}</span></figcaption>'
                  f'<iframe title="Correo: {H.escape(m["nombre"])}" sandbox="allow-same-origin" srcdoc="{src}"></iframe></figure>')
    galeria += f'<section class="grupo" aria-labelledby="g-{len(galeria)}"><h3 id="g-{len(galeria)}">{g}</h3><div class="mails">{items}</div></section>'
page = f'''<title>SAM acceso y correos</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap">
<style>
/* Layout: dos vistas por hash. #login: panel de marca + formulario (una columna en celular). #correos: galería por grupo. Tokens del design system SAM, oscuro primero. */
:root{{--surface:#0a0a0b;--surface-raised:#16161a;--surface-sunken:#1f1f24;--line:#2a2a30;--line-control:#6e6e78;--ink:#f2f2ee;--ink-muted:#a3a3a8;
  --brand:#c6f432;--on-brand:#0a0a0b;--brand-edge:#c6f432;--focus:#f2f2ee;--danger:#ff8a7a;--warning:#f5b941;--info:#8ab4ff;
  --sans:"Onest",ui-sans-serif,system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace;color-scheme:dark}}
@media (prefers-color-scheme: light){{:root:not([data-theme="dark"]){{--surface:#f2f2ee;--surface-raised:#ffffff;--surface-sunken:#e8e8e2;--line:#d6d6d0;--line-control:#7a7a82;--ink:#0a0a0b;--ink-muted:#55555c;--brand-edge:#0a0a0b;--focus:#0a0a0b;--danger:#b42318;--warning:#8a5a00;--info:#2f5bd3;color-scheme:light}}}}
:root[data-theme="light"]{{--surface:#f2f2ee;--surface-raised:#ffffff;--surface-sunken:#e8e8e2;--line:#d6d6d0;--line-control:#7a7a82;--ink:#0a0a0b;--ink-muted:#55555c;--brand-edge:#0a0a0b;--focus:#0a0a0b;--danger:#b42318;--warning:#8a5a00;--info:#2f5bd3;color-scheme:light}}
*{{box-sizing:border-box}}
body{{background:var(--surface);color:var(--ink);font:400 16px/1.5 var(--sans)}}
a{{color:inherit}} code{{font:500 .85em var(--mono)}}
:focus-visible{{outline:3px solid var(--focus);outline-offset:3px;border-radius:4px}}
.top{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--surface);border-bottom:1px solid var(--line)}}
body::before{{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--surface)}}
.top .in{{display:flex;gap:16px;align-items:center;padding-block:8px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));max-width:1200px;margin:0 auto;flex-wrap:wrap}}
.top b{{font-weight:600}} .tabs{{display:flex;gap:4px}} .tabs a{{text-decoration:none;font-weight:600;font-size:14px;padding:10px 14px;border-radius:6px;min-height:44px;display:inline-flex;align-items:center;color:var(--ink-muted)}}
.tabs a[aria-current="page"]{{color:var(--ink);background:var(--surface-sunken)}}
.vista{{max-width:1200px;margin:0 auto;padding-block:24px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
/* Demo de estados */
.demo{{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:20px}} .demo .eti{{margin-right:4px}}
.demo button{{font:500 13px var(--sans);color:var(--ink);background:transparent;border:1px solid var(--line-control);border-radius:999px;padding:6px 12px;min-height:36px;cursor:pointer}}
.demo button[aria-pressed="true"]{{background:var(--ink);color:var(--surface);border-color:var(--ink)}}
.eti{{font:500 12px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--ink-muted)}}
/* Pantalla de login (marco de la app) */
.app{{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,6fr);min-height:620px;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--surface)}}
@media (max-width:860px){{.app{{grid-template-columns:minmax(0,1fr)}} .app .marca{{display:none}}}}
.marca{{background:var(--surface-raised);padding:40px;display:flex;flex-direction:column;justify-content:space-between;gap:32px;border-right:1px solid var(--line)}}
.marca .logoh{{width:200px;height:auto;color:var(--ink)}}
.marca .fig{{width:100%;max-width:380px;height:auto;align-self:center;color:var(--ink)}}
.marca p{{margin:0;color:var(--ink-muted);max-width:34ch;font-size:15px}}
.form{{padding:40px max(24px,6%);display:flex;flex-direction:column;justify-content:center;gap:24px;max-width:520px;width:100%;margin:0 auto}}
.logom{{display:none;width:120px;height:auto;color:var(--ink)}} @media (max-width:860px){{.logom{{display:block}} .form{{padding:32px 20px 40px;justify-content:flex-start}}}}
.form h1{{margin:0;font:700 23px/28px var(--sans);letter-spacing:-.01em}} .form .sub{{margin:6px 0 0;color:var(--ink-muted);font-size:15px}}
.campo{{display:grid;gap:6px;grid-template-columns:minmax(0,1fr)}} .campo label{{font:600 14px/20px var(--sans)}}
.ctrl{{display:flex;align-items:center;background:var(--surface-raised);border-radius:6px;box-shadow:inset 0 0 0 1.5px var(--line-control)}}
.ctrl:focus-within{{outline:3px solid var(--focus);outline-offset:3px}}
.ctrl input{{flex:1;min-width:0;background:transparent;border:0;color:var(--ink);font:400 16px var(--sans);padding:0 12px;min-height:44px;outline:none}}
.ctrl[data-error="true"]{{box-shadow:inset 0 0 0 2px var(--danger)}}
.ver{{font:600 13px var(--sans);color:var(--ink);background:transparent;border:0;padding:0 12px;min-height:44px;cursor:pointer;text-decoration:underline;text-underline-offset:3px}}
.ver:focus-visible{{outline-offset:-3px}}
.err{{color:var(--danger);font-size:14px;margin:0;display:flex;gap:6px}} .err::before{{content:"✕";font-weight:700}}
.ayuda{{color:var(--ink-muted);font-size:14px;margin:0}}
.fila{{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}}
.lnk{{font-weight:600;font-size:14px;text-decoration:underline;text-underline-offset:3px;background:none;border:0;color:var(--ink);cursor:pointer;padding:10px 0;font-family:var(--sans)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:0 18px;border-radius:6px;font:600 15px var(--sans);cursor:pointer;border:0;width:100%}}
.btn.pri{{background:var(--brand);color:var(--on-brand);box-shadow:inset 0 0 0 2px var(--brand-edge)}}
.btn.pri[aria-disabled="true"]{{opacity:.75;cursor:progress}}
.btn.sec{{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line-control)}}
.aviso{{display:grid;gap:4px;padding:12px 14px;border-radius:6px;background:var(--surface-sunken);border:1px solid var(--line);font-size:15px}}
.aviso b{{font-weight:600}} .aviso.peligro{{border-color:var(--danger)}} .aviso.peligro b{{color:var(--danger)}} .aviso.info b{{color:var(--info)}} .aviso.aviso2 b{{color:var(--warning)}}
.aviso p{{margin:0}}
.spin{{width:16px;height:16px;border-radius:50%;border:2px solid currentColor;border-right-color:transparent;animation:g 0.8s linear infinite}}
@keyframes g{{to{{transform:rotate(360deg)}}}}
@media (prefers-reduced-motion:reduce){{.spin{{animation:none;border-right-color:currentColor;opacity:.6}}}}
.reqs{{margin:0;padding:0;list-style:none;display:grid;gap:4px;font-size:14px;color:var(--ink-muted)}} .reqs li::before{{content:"○ "}} .reqs li.ok{{color:var(--ink)}} .reqs li.ok::before{{content:"✓ "}}
.supuestos{{margin-top:20px;border:1px solid var(--line);border-radius:10px;padding:14px 16px;background:var(--surface-raised)}}
.supuestos summary{{cursor:pointer;font-weight:600;min-height:28px}} .supuestos ul{{margin:10px 0 0;padding-left:20px;display:grid;gap:6px;color:var(--ink-muted);font-size:15px}}
/* Correos */
.intro{{max-width:70ch;margin:0 0 24px;color:var(--ink-muted)}}
.grupo h3{{margin:28px 0 12px;font:600 18px var(--sans)}}
.mails{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,420px),1fr));gap:20px}}
.mail{{margin:0;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--surface-raised);display:flex;flex-direction:column;min-width:0}}
.mail figcaption{{display:grid;gap:4px;padding:12px 14px;border-bottom:1px solid var(--line)}}
.asunto{{font-weight:600;font-size:15px;overflow-wrap:anywhere}} .asunto .k{{font:500 11px var(--mono);text-transform:uppercase;letter-spacing:.06em;color:var(--ink-muted);margin-right:6px}}
.mail iframe{{width:100%;height:640px;border:0;background:#f2f2ee;display:block}}
[hidden]{{display:none!important}}
</style>

<header class="top"><div class="in"><svg viewBox="{vb('sam-logotipo-compacto.svg')}" height="26" role="img" aria-label="SAM" style="color:var(--ink)">{LOGOC}</svg><b>Acceso y correos</b>
<nav class="tabs" aria-label="Vistas"><a href="#login" data-v="login">Pantalla de login</a><a href="#correos" data-v="correos">Plantillas de correo</a></nav></div></header>

<main>
<div class="vista" id="v-login">
  <div class="demo" role="group" aria-label="Ver estado de la pantalla"><span class="eti">Ver estado</span>
    <button type="button" data-s="normal">Normal</button><button type="button" data-s="vacios">Campos vacíos</button><button type="button" data-s="incorrectos">Datos incorrectos</button>
    <button type="button" data-s="entrando">Entrando</button><button type="button" data-s="bloqueada">Cuenta bloqueada</button><button type="button" data-s="sinred">Sin conexión</button>
    <button type="button" data-s="recuperar">Recuperar</button><button type="button" data-s="enviado">Enlace enviado</button><button type="button" data-s="nueva">Contraseña nueva</button>
    <button type="button" data-s="vencido">Enlace vencido</button><button type="button" data-s="lista">Contraseña cambiada</button></div>
  <div class="app">
    <aside class="marca" aria-hidden="true">
      <svg class="logoh" viewBox="{vb('sam-logotipo-horizontal.svg')}">{LOGOH}</svg>
      <svg class="fig" viewBox="0 0 48 48">{C2}</svg>
      <p>Registra, mueve y cierra el trabajo del equipo de desarrollo y soporte.</p>
    </aside>
    <section class="form" aria-labelledby="h-form">
      <svg class="logom" viewBox="{vb('sam-logotipo-horizontal.svg')}" role="img" aria-label="SAM, Simple Activity Manager">{LOGOH}</svg>
      <div id="panel"></div>
    </section>
  </div>
  <details class="supuestos"><summary>Reglas de acceso (confirmadas el 13 nov 2026)</summary><ul>
    <li>Bloqueo de 15 minutos tras 5 intentos fallidos.</li>
    <li>Contraseña nueva: al menos 12 caracteres, sin otras reglas de composición.</li>
    <li>El enlace para restablecer vence en 1 hora y funciona una vez; el de invitación, en 72 horas.</li>
    <li>La sesión no expira mientras la app instalada esté en uso; no hay casilla de «Mantener sesión».</li>
    <li>Los mensajes no dicen si un correo existe en SAM (evita adivinar cuentas).</li>
  </ul></details>
</div>

<div class="vista" id="v-correos" hidden>
  <p class="intro">Diez muestras de ocho plantillas, con datos ficticios. Cada plantilla vive en <code>.fruti/icons/sam/correos/plantillas/</code> con variables <code>{{{{así}}}}</code>. Son HTML de tablas con estilos en línea, en tema claro, con el botón Voltaje y contorno de tinta. El logotipo va en PNG porque Gmail y Outlook no muestran SVG.</p>
  {galeria}
</div>
</main>

<script>
(function(){{
  // Vistas por hash
  const vistas={{login:document.getElementById('v-login'),correos:document.getElementById('v-correos')}};
  function ruta(){{const v=(location.hash||'#login').slice(1);const k=vistas[v]?v:'login';
    for(const [n,el] of Object.entries(vistas)) el.hidden=n!==k;
    document.querySelectorAll('.tabs a').forEach(a=>{{if(a.dataset.v===k)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');}});}}
  addEventListener('hashchange',ruta);ruta();
  // Ajusta cada correo a su alto (el marco no ejecuta scripts del correo)
  const ajusta=f=>{{try{{const d=f.contentDocument;if(d&&d.body)f.style.height=(d.documentElement.scrollHeight+4)+'px';}}catch(e){{}}}};
  document.querySelectorAll('.mail iframe').forEach(f=>{{f.addEventListener('load',()=>ajusta(f));ajusta(f);}});
  addEventListener('hashchange',()=>document.querySelectorAll('.mail iframe').forEach(ajusta));

  // Login: estado de demostración
  const P=document.getElementById('panel');let st={{s:'normal',correo:'',pw:'',ver:false,nueva:'',conf:''}};
  const esc=t=>String(t).replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));
  const campoPw=(id,lab,val,auto,err,ayuda)=>`<div class="campo"><label for="${{id}}">${{lab}}</label><div class="ctrl" data-error="${{!!err}}"><input id="${{id}}" type="${{st.ver?'text':'password'}}" autocomplete="${{auto}}" value="${{esc(val)}}" ${{err?`aria-invalid="true" aria-describedby="${{id}}-e"`:(ayuda?`aria-describedby="${{id}}-a"`:'')}}><button type="button" class="ver" data-ver aria-pressed="${{st.ver}}">${{st.ver?'Ocultar':'Mostrar'}}</button></div>${{err?`<p class="err" id="${{id}}-e">${{err}}</p>`:''}}${{ayuda&&!err?`<p class="ayuda" id="${{id}}-a">${{ayuda}}</p>`:''}}</div>`;
  const campoMail=(err)=>`<div class="campo"><label for="correo">Correo</label><div class="ctrl" data-error="${{!!err}}"><input id="correo" type="email" autocomplete="username" inputmode="email" value="${{esc(st.correo)}}" ${{err?'aria-invalid="true" aria-describedby="correo-e"':''}}></div>${{err?`<p class="err" id="correo-e">${{err}}</p>`:''}}</div>`;
  const cab=(t,s)=>`<div><h1 id="h-form" tabindex="-1">${{t}}</h1>${{s?`<p class="sub">${{s}}</p>`:''}}</div>`;
  const aviso=(tipo,t,d)=>`<div class="aviso ${{tipo}}" role="${{tipo==='peligro'?'alert':'status'}}"><b>${{t}}</b><p>${{d}}</p></div>`;
  function login(extra){{
    const e=extra||{{}};
    return cab('Entra a SAM','Usa el correo de tu cuenta del equipo.')+(e.aviso||'')+
      `<form id="f-login" novalidate class="campo" style="gap:18px">${{campoMail(e.ec)}}${{campoPw('pw','Contraseña',st.pw,'current-password',e.ep)}}
      <div class="fila"><button type="button" class="lnk" data-go="recuperar">¿Olvidaste tu contraseña?</button></div>
      <button class="btn pri" type="submit" ${{e.cargando?'aria-disabled="true"':''}}>${{e.cargando?'<span class="spin" aria-hidden="true"></span>Entrando…':'Entrar'}}</button></form>`;
  }}
  const V={{
    normal:()=>login(),
    vacios:()=>login({{ec:'Escribe tu correo.',ep:'Escribe tu contraseña.'}}),
    incorrectos:()=>login({{aviso:aviso('peligro','El correo o la contraseña no coinciden','Revisa que estén bien escritos e intenta de nuevo. Después de 5 intentos, la cuenta se bloquea 15 minutos.')}}),
    entrando:()=>login({{cargando:true}}),
    bloqueada:()=>login({{aviso:aviso('aviso2','Cuenta bloqueada por 15 minutos','Hubo 5 intentos fallidos seguidos. Espera o restablece tu contraseña para entrar ahora.')}}),
    sinred:()=>login({{aviso:aviso('info','No hay conexión','Revisa tu red. Lo que escribiste sigue aquí; vuelve a pulsar Entrar cuando regrese la conexión.')}}),
    recuperar:()=>cab('Restablece tu contraseña','Te enviamos un enlace al correo de tu cuenta.')+`<form id="f-rec" novalidate class="campo" style="gap:18px">${{campoMail()}}<button class="btn pri" type="submit">Enviar enlace</button><button type="button" class="lnk" data-go="normal">Volver a entrar</button></form>`,
    enviado:()=>cab('Revisa tu correo','')+aviso('info','Enlace enviado',`Si <b>${{esc(st.correo||'tu correo')}}</b> tiene cuenta en SAM, te llegará un enlace en unos minutos. Vence en 1 hora.`)+`<p class="ayuda">¿No llegó? Revisa el correo no deseado o <button type="button" class="lnk" data-go="recuperar" style="padding:0">pide otro enlace</button>.</p><button type="button" class="btn sec" data-go="normal">Volver a entrar</button>`,
    nueva:()=>{{const ok=st.nueva.length>=12, igual=st.nueva&&st.nueva===st.conf;
      return cab('Crea una contraseña nueva','Para daniela.ortiz@ejemplo.com')+`<form id="f-nueva" novalidate class="campo" style="gap:18px">${{campoPw('nueva','Contraseña nueva',st.nueva,'new-password','', '')}}<ul class="reqs" aria-live="polite"><li class="${{ok?'ok':''}}">Al menos 12 caracteres</li><li class="${{igual?'ok':''}}">Las dos contraseñas coinciden</li></ul>${{campoPw('conf','Repite la contraseña',st.conf,'new-password','')}}<button class="btn pri" type="submit">Guardar contraseña</button></form>`;}},
    vencido:()=>cab('Este enlace ya no funciona','')+aviso('aviso2','El enlace venció o ya se usó','Los enlaces para restablecer duran 1 hora y sirven una vez. Pide uno nuevo.')+`<button type="button" class="btn pri" data-go="recuperar">Pedir otro enlace</button>`,
    lista:()=>cab('Contraseña actualizada','')+aviso('info','Listo','Ya puedes entrar con tu contraseña nueva. Cerramos las sesiones abiertas en otros dispositivos.')+`<button type="button" class="btn pri" data-go="normal">Entrar a SAM</button>`,
  }};
  let enfocar=false;
  function pinta(){{P.innerHTML=V[st.s]();document.querySelectorAll('.demo button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.s===st.s));
    if(enfocar){{const h=document.getElementById('h-form');h&&h.focus();enfocar=false;}}}}
  function ir(s){{st.s=s;enfocar=true;pinta();}}
  document.querySelector('.demo').addEventListener('click',e=>{{const b=e.target.closest('button[data-s]');if(b){{if(b.dataset.s==='vacios'){{st.correo='';st.pw='';}}ir(b.dataset.s);}}}});
  P.addEventListener('click',e=>{{const g=e.target.closest('[data-go]');if(g){{ir(g.dataset.go);return;}}
    const v=e.target.closest('[data-ver]');if(v){{st.ver=!st.ver;const id=v.parentElement.querySelector('input').id;pinta();const i=document.getElementById(id);i&&i.focus();}}}});
  P.addEventListener('input',e=>{{const t=e.target;if(t.id==='correo')st.correo=t.value;if(t.id==='pw')st.pw=t.value;
    if(t.id==='nueva'||t.id==='conf'){{st[t.id]=t.value;const pos=t.selectionStart;pinta();const i=document.getElementById(t.id);i.focus();i.setSelectionRange(pos,pos);}}}});
  P.addEventListener('submit',e=>{{e.preventDefault();const f=e.target.id;
    if(f==='f-login'){{if(!st.correo||!st.pw){{st.s='vacios';enfocar=false;pinta();const i=document.getElementById(!st.correo?'correo':'pw');i&&i.focus();return;}}
      st.s='entrando';pinta();setTimeout(()=>{{st.s='incorrectos';st.pw='';pinta();const i=document.getElementById('pw');i&&i.focus();}},1200);}}
    if(f==='f-rec'){{if(!st.correo){{const i=document.getElementById('correo');i.focus();return;}}ir('enviado');}}
    if(f==='f-nueva'){{if(st.nueva.length>=12&&st.nueva===st.conf){{st.nueva=st.conf='';ir('lista');}}else{{document.getElementById('nueva').focus();}}}}
  }});
  pinta();
}})();
</script>
'''
open(os.path.join(B, 'acceso.html'), 'w').write(page); print('ok', len(page)//1024, 'KB')
