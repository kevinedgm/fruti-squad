# Bitácora % Alcohol por volumen · r01 · F3 con el design system NisaLab (tokens.json). Uso: python3 gen.py → prototipo.html
# Nombres de personas y lecturas: de ejemplo.
import os, re, json
D = os.path.dirname(os.path.abspath(__file__))
TOK = json.load(open(os.path.join(D, '..', 'nabi-design-system', 'tokens.json')))
VARS = []
for t in TOK['color']['tokens']: VARS.append(f"--{t['name']}:{t['value']}")
for g in ('spacing', 'radius', 'sizing', 'shadow', 'motion'):
    for t in TOK[g]['tokens']: VARS.append(f"--{t['name']}:{t['value']}")
for k, v in TOK['type']['families'].items(): VARS.append(f"--font-{k}:{v}")
ROOT = ':root{' + ';'.join(VARS) + ';color-scheme:light}'
L = '/root/.cache/fruti-uva/package/icons/'
def ico(n, s=18, cls='i'):
    inner = ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse|polygon)[^>]*/>', open(L + n + '.svg').read()))
    return f'<svg class="{cls}" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{inner}</svg>'

CSS = r'''
/* Modal de bitácora: banda azul de marca arriba; cuerpo en lienzo gris con tarjetas blancas; pie fijo. Escritorio primero, apila bajo 720 px. */
*{box-sizing:border-box}html,body{margin:0}[hidden]{display:none!important}
body{background:#3a4258;font:14px/22px var(--font-sans);color:var(--text);min-height:100vh;padding:max(16px,env(safe-area-inset-left,0px));padding-top:16px;padding-bottom:16px;padding-right:max(16px,env(safe-area-inset-right,0px))}
.i{flex:none}.mono{font-family:var(--font-datos);font-variant-numeric:tabular-nums}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
:focus-visible{outline:2px solid var(--primary);outline-offset:2px}
/* control de estados del prototipo (no es parte del diseño) */
.ctl{max-width:880px;margin:0 auto 12px;display:flex;flex-wrap:wrap;gap:8px;align-items:center;color:#fff;font-size:13px}
.ctl b{font-weight:600;margin-right:4px}.ctl button{min-height:36px;padding:0 12px;border-radius:var(--radius-sm);border:1px solid rgba(255,255,255,.35);background:transparent;color:#fff;font:500 13px var(--font-sans);cursor:pointer}
.ctl button[aria-pressed="true"]{background:#fff;color:var(--primary);border-color:#fff}
/* modal */
.modal{max-width:880px;margin:0 auto;background:var(--bg);border-radius:var(--radius-lg);box-shadow:var(--shadow-overlay);overflow:hidden;display:grid;grid-template-rows:auto 1fr auto;max-height:calc(100vh - 80px)}
.mh{background:var(--primary);color:var(--surface);padding:18px 20px 18px 24px;display:flex;gap:16px;align-items:flex-start}
.mh .t{flex:1;min-width:0;display:grid;gap:4px}
.codes{display:flex;flex-wrap:wrap;gap:6px}.codes span{font:500 12px/18px var(--font-datos);letter-spacing:.02em;padding:1px 8px;border-radius:var(--radius-sm);border:1px solid rgba(255,255,255,.3)}
.mh h1{margin:0;font:600 22px/30px var(--font-display);letter-spacing:-.005em}
.mh p{margin:0;font-size:13px;line-height:18px;color:#C9D2E8}
.x{width:40px;height:40px;display:grid;place-items:center;border-radius:var(--radius-sm);border:0;background:rgba(255,255,255,.12);color:var(--surface);cursor:pointer}
.x:hover{background:rgba(255,255,255,.2)}.x:focus-visible{outline-color:var(--pera)}
.mb{overflow:auto;padding:20px 24px;display:grid;gap:20px;align-content:start}
/* avisos */
.al{display:flex;gap:12px;align-items:flex-start;padding:12px 14px;border-radius:var(--radius-md)}
.al .i{margin-top:2px}.al b{display:block;font-weight:600}.al p{margin:2px 0 0;color:var(--text);font-size:13px;line-height:20px}
.al.alerta{background:var(--alerta-soft);color:var(--alerta)}.al.primary{background:var(--primary-soft);color:var(--primary)}
.al small{display:block;font:600 11px/16px var(--font-sans);letter-spacing:.06em;text-transform:uppercase;margin-bottom:2px}
/* secciones */
.sec{display:grid;gap:12px}
.sec>h2{margin:0;display:flex;align-items:center;gap:8px;font:600 16px/24px var(--font-display)}
.sec>h2 .i{color:var(--text-muted)}
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-md);box-shadow:var(--shadow-1)}
.gen{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:12px}
.gen>.card{padding:16px;display:grid;gap:14px;align-content:start}
.dl{display:grid;gap:2px}.dl dt{font:500 13px/18px var(--font-sans);color:var(--text-muted)}.dl dd{margin:0}
.dl dd .mono{font-size:13px;color:var(--text-muted);margin-left:6px}
/* campos */
.f{display:grid;gap:6px}.f>label,.f .lb{font:500 13px/18px var(--font-sans)}
.f .req{color:var(--text-muted);font-weight:400}
.ctrl{display:flex;align-items:stretch;min-height:var(--control-h);background:var(--surface);border:1px solid var(--border-control);border-radius:var(--radius-md);box-shadow:var(--shadow-inset);overflow:hidden;transition:border-color var(--quick) ease,box-shadow var(--quick) ease}
.ctrl:focus-within{border-color:var(--primary);box-shadow:var(--shadow-inset),0 0 0 3px var(--primary-soft)}
.ctrl input,.ctrl textarea{flex:1;min-width:0;border:0;outline:0;background:none;padding:0 12px;font:500 14px/20px var(--font-datos);color:var(--text)}
.ctrl input.num{text-align:right}
.ctrl .u{display:flex;align-items:center;padding:0 10px;font:500 12px var(--font-datos);color:var(--text-muted);border-left:1px solid var(--border)}
.ctrl .lk{display:none;align-items:center;padding:0 0 0 10px;color:var(--text-muted)}
.ctrl.ro{background:var(--bg);box-shadow:none}.ctrl.ro .lk{display:flex}.ctrl.ro input,.ctrl.ro textarea{color:var(--text-muted)}
.f[data-err] .ctrl{border-color:var(--fuera);box-shadow:var(--shadow-inset),0 0 0 3px var(--fuera-soft)}
.msg{display:flex;gap:6px;align-items:flex-start;font:500 12px/16px var(--font-sans);color:var(--fuera)}
.msg[hidden]{display:none}.help{font-size:12px;line-height:16px;color:var(--text-muted)}
textarea{resize:vertical;min-height:72px;padding:10px 12px!important;font-family:var(--font-sans)!important;font-weight:400!important}
/* firmas */
.firmas{padding:0!important;gap:0!important}.firmas h3{margin:0;padding:12px 16px;border-bottom:1px solid var(--border);display:flex;gap:8px;align-items:center;font:600 14px/20px var(--font-sans)}
.firmas h3 .i{color:var(--primary)}
.fp{display:grid;grid-template-columns:32px minmax(0,1fr) auto;gap:10px;align-items:center;padding:12px 16px;border-bottom:1px solid var(--border)}.fp:last-child{border-bottom:0}
.av{width:32px;height:32px;border-radius:var(--radius-pill);display:grid;place-items:center;font:600 12px var(--font-sans);background:var(--bg);color:var(--text-muted)}
.av.ok{background:var(--primary-soft);color:var(--primary)}
.fp small{display:block;font-size:12px;line-height:16px;color:var(--text-muted)}.fp b{font-weight:600}
.fp .mono{font-size:12px}
/* píldoras de estado */
.st{display:inline-flex;align-items:center;gap:6px;padding:3px 10px 3px 8px;border-radius:var(--radius-sm);font:500 13px/18px var(--font-sans);white-space:nowrap}
.st.ok{background:var(--conforme-soft);color:var(--on-conforme-soft)}.st.bad{background:var(--fuera-soft);color:var(--fuera)}
.st.warn{background:var(--alerta-soft);color:var(--alerta)}.st.pend{background:var(--bg);color:var(--text-muted)}
/* mesa de trabajo */
.wb{display:grid;grid-template-columns:minmax(0,1fr) 280px;gap:12px;align-items:start}
.ph{display:flex;justify-content:space-between;gap:12px;align-items:baseline;padding:12px 16px;border-bottom:1px solid var(--border)}
.ph h3{margin:0;font:600 14px/20px var(--font-sans)}.ph span{font-size:12px;color:var(--text-muted)}
.rh,.rr{display:grid;grid-template-columns:32px minmax(0,1fr) minmax(0,1fr);gap:10px;align-items:center;padding:0 16px}
.rh{padding-top:10px;padding-bottom:6px;font:500 13px/18px var(--font-sans);color:var(--text-muted)}
.rr{padding-top:6px;padding-bottom:6px;position:relative}.rr:last-child{padding-bottom:14px}
.rr:focus-within::before{content:"";position:absolute;left:0;top:6px;bottom:6px;width:3px;border-radius:0 3px 3px 0;background:var(--pera)}
.rr:last-child:focus-within::before{bottom:14px}
.n{width:28px;height:28px;border-radius:var(--radius-pill);display:grid;place-items:center;background:var(--bg);font:500 13px var(--font-datos);color:var(--text-muted)}
.res{padding:16px;display:grid;gap:14px}
.res .ov{font:600 11px/16px var(--font-sans);letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted)}
.big{font:500 32px/36px var(--font-datos);font-variant-numeric:tabular-nums;color:var(--text)}.big small{font-size:13px;color:var(--text-muted);margin-left:6px}
.big.empty{color:var(--text-muted)}
.rep{display:grid;gap:6px}.rep .v{font:500 14px/20px var(--font-datos)}
.crit{border-top:1px solid var(--border);padding-top:12px;font-size:12px;line-height:18px;color:var(--text-muted)}
.crit b{color:var(--text);font-weight:600}
/* referencia */
details.ref{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-md)}
details.ref summary{list-style:none;cursor:pointer;display:flex;gap:10px;align-items:center;padding:12px 16px;min-height:44px}
details.ref summary::-webkit-details-marker{display:none}
details.ref summary b{font-weight:600}details.ref summary small{display:block;font-size:12px;line-height:16px;color:var(--text-muted)}
details.ref summary .ch{margin-left:auto;transition:transform var(--quick) ease;color:var(--text-muted)}details.ref[open] summary .ch{transform:rotate(180deg)}
.ref .nota{margin:0 16px 8px;padding:8px 12px;border-radius:var(--radius-sm);background:var(--bg);font-size:12px;line-height:18px;color:var(--text-muted)}
.ref dl{margin:0 16px 12px;display:grid}.ref dl div{display:grid;grid-template-columns:150px minmax(0,1fr);gap:12px;padding:8px 0;border-top:1px solid var(--border);font-size:13px;line-height:18px}
.ref dt{font-weight:500}.ref dd{margin:0;color:var(--text-muted)}.ref dd b{display:block;font-weight:500;color:var(--text)}
/* adjuntos */
.drop{display:flex;gap:12px;align-items:center;padding:14px 16px;border:1.5px dashed var(--border-control);border-radius:var(--radius-md);background:var(--surface);cursor:pointer}
.drop:hover,.drop:focus-within{border-color:var(--primary);background:var(--primary-soft)}
.drop .ic{width:36px;height:36px;display:grid;place-items:center;border-radius:var(--radius-sm);background:var(--bg);color:var(--primary)}
.drop b{font-weight:600}.drop small{display:block;font-size:12px;color:var(--text-muted)}
.drop.ro{pointer-events:none;opacity:.6}
/* pie */
.mf{display:flex;gap:8px;justify-content:flex-end;align-items:center;padding:12px 24px;background:var(--surface);border-top:1px solid var(--border)}
.mf .hint{margin-right:auto;font-size:12px;color:var(--text-muted)}
.btn{display:inline-flex;align-items:center;gap:8px;min-height:var(--control-h);padding:0 16px;border-radius:var(--radius-sm);font:600 14px/20px var(--font-sans);border:1px solid transparent;cursor:pointer;transition:transform var(--quick) var(--ease-out),box-shadow var(--quick) ease,background var(--quick) ease}
.btn-p{background:var(--primary);color:var(--surface);box-shadow:var(--shadow-primary)}.btn-p:hover{background:var(--primary-hover);box-shadow:var(--shadow-primary-hover);transform:translateY(-1px)}
.btn-s{background:var(--surface);color:var(--primary);border-color:var(--border-control);box-shadow:var(--shadow-1)}.btn-s:hover{background:var(--bg)}
.btn[hidden]{display:none}
@media (max-width:720px){.gen,.wb{grid-template-columns:minmax(0,1fr)}.mb{padding:16px}.mh{padding:16px}.mf{padding:12px 16px;flex-wrap:wrap}.mf .hint{flex-basis:100%}.ref dl div{grid-template-columns:1fr;gap:2px}}
@media (prefers-reduced-motion:reduce){.btn,.ctrl,details.ref summary .ch{transition:none}.btn-p:hover{transform:none}}
'''

def campo(id_, label, unit=None, num=True, hidden_label=False, val=''):
    lab = f'<label for="{id_}"{" class=vh" if hidden_label else ""}>{label}</label>'
    u = f'<span class="u" aria-hidden="true">{unit}</span>' if unit else ''
    return (f'<div class="f" id="f-{id_}">{lab}<div class="ctrl"><span class="lk">{ico("lock", 14)}</span>'
            f'<input id="{id_}" {"inputmode=decimal class=num" if num else ""} autocomplete="off" value="{val}" aria-describedby="m-{id_}">{u}</div>'
            f'<span class="msg" id="m-{id_}" hidden>{ico("circle-alert", 14)}<span></span></span></div>')

FILAS = ''.join(f'<div class="rr" role="group" aria-label="Corrida {i}"><span class="n" aria-hidden="true">{i}</span>'
                f'{campo(f"alc{i}", f"Alcohol por volumen, corrida {i}", "% Alc. Vol.", hidden_label=True)}{campo(f"tmp{i}", f"Temperatura, corrida {i}", "°C", hidden_label=True)}</div>' for i in (1, 2, 3))
REF = [('Promedio', 'Rango permitido: 35–55 % Alc. Vol. a 20 °C', 'NOM-070-SCFI-2016')] + [(f'Medición {i}', 'Sin rango normativo configurado', 'Criterio configurado para el ensayo') for i in (1, 2, 3)] \
    + [(f'Temperatura {i}', 'Sin rango normativo configurado', 'Criterio configurado para el ensayo') for i in (1, 2, 3)] + [('U exp', 'Sin rango normativo configurado', 'Criterio configurado para el ensayo')]
REF_H = ''.join(f'<div><dt>{a}</dt><dd>{b}<b>Referencia: {c}</b></dd></div>' for a, b, c in REF)

BODY = f'''<div class="ctl" role="group" aria-label="Estados del prototipo"><b>Estado de ejemplo:</b>
<button data-s="nueva" aria-pressed="true">Nueva</button><button data-s="conforme" aria-pressed="false">Capturada · conforme</button><button data-s="fuera" aria-pressed="false">Repetibilidad fuera</button><button data-s="reabierta" aria-pressed="false">Reabierta</button><button data-s="firmada" aria-pressed="false">Firmada</button></div>
<div class="modal" role="dialog" aria-modal="true" aria-labelledby="t-bit">
<header class="mh"><div class="t"><div class="codes"><span>BIT-02-01</span><span>Rev. 01</span></div><h1 id="t-bit">% Alcohol por volumen</h1><p>Vigente desde el 1 de octubre de 2021 · NOM-070-SCFI-2016</p></div>
<button class="x" type="button" aria-label="Cerrar bitácora">{ico("x", 20)}</button></header>
<div class="mb">
<div class="al alerta" id="al-plazo" role="status">{ico("clock", 18)}<div><small>Cierre fuera de plazo</small><b>La fecha programada de entrega ya venció</b><p>Al registrar se pedirá una justificación. Guardar sin cerrar no la pide; si la bitácora fue reabierta, puedes reutilizar su motivo.</p></div></div>
<div class="al primary" id="al-reab" role="status" hidden>{ico("rotate-ccw", 18)}<div><small>Reabierta por supervisión</small><b>Corrige la lectura 2 y vuelve a registrar</b><p>Motivo: «La corrida 2 se capturó con la temperatura de la corrida 3.» · J. Orozco, 4 nov 2026 16:20</p></div></div>
<section class="sec" aria-labelledby="h-gen"><h2 id="h-gen">{ico("info", 18)}Información general</h2>
<div class="gen"><div class="card"><div class="f" id="f-fecha"><label for="fecha">Fecha de análisis <span class="req">(obligatoria)</span></label><div class="ctrl"><span class="lk">{ico("lock", 14)}</span><input id="fecha" type="date" min="2024-01-01" max="2026-11-05" aria-describedby="m-fecha" required></div><span class="msg" id="m-fecha" hidden>{ico("circle-alert", 14)}<span></span></span></div>
<dl class="dl"><dt>Equipo utilizado</dt><dd>Densímetro digital Anton Paar<span class="mono">DD-01</span></dd></dl></div>
<div class="card firmas"><h3>{ico("shield-check", 18)}Firmas y visto bueno</h3>
<div class="fp" id="fp-an"><span class="av" aria-hidden="true">?</span><div><small>Analista</small><b>Pendiente de captura</b></div><span class="st pend">{ico("clock", 14)}Pendiente</span></div>
<div class="fp" id="fp-vb"><span class="av" aria-hidden="true">?</span><div><small>Visto bueno</small><b>Pendiente de supervisión</b></div><span class="st pend">{ico("clock", 14)}Pendiente</span></div></div></div></section>
<section class="sec" aria-labelledby="h-med"><h2 id="h-med">{ico("flask-conical", 18)}Mediciones y temperaturas</h2>
<div class="wb"><div class="card"><div class="ph"><h3>Lecturas</h3><span class="mono">3 corridas</span></div>
<div class="rh" aria-hidden="true"><span>#</span><span>Alc. vol.</span><span>Temperatura</span></div>{FILAS}</div>
<div class="card res" aria-live="polite"><div><span class="ov">Promedio</span><div class="big empty" id="prom">—<small>% Alc. Vol.</small></div><span class="help" id="prom-h">Se calcula al capturar las tres lecturas.</span></div>
{campo("uexp", "U<sub>exp</sub> (incertidumbre expandida)", "% Alc. Vol.", val="0.02")}
<div class="rep"><span class="ov">Repetibilidad</span><div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap"><span class="v" id="rep">—</span><span id="rep-st"></span></div></div>
<div class="crit"><b>Criterio de aceptación</b><br>Repetibilidad ±0.1 % alc. vol. · Reproducibilidad ±0.2 % alc. vol.</div></div></div>
<details class="ref"><summary>{ico("book-open", 18)}<span><b>Referencia de evaluación</b><small>Ayuda para evitar errores de captura; no vale para auditoría.</small></span>{ico("chevron-down", 18, "i ch")}</summary>
<p class="nota">Estos rangos solo generan avisos preventivos durante la captura. No sustituyen el método, la norma vigente, el informe de resultados ni los registros controlados de una auditoría.</p><dl>{REF_H}</dl></details></section>
<section class="sec" aria-labelledby="h-obs"><h2 id="h-obs">{ico("message-square", 18)}Observaciones</h2>
<div class="f"><label for="obs" class="vh">Observaciones</label><div class="ctrl"><span class="lk">{ico("lock", 14)}</span><textarea id="obs" rows="3" placeholder="Sin observaciones registradas."></textarea></div></div></section>
<section class="sec" aria-labelledby="h-doc"><h2 id="h-doc">{ico("paperclip", 18)}Documentos adjuntos</h2>
<label class="drop" for="arch" id="drop"><span class="ic">{ico("upload", 18)}</span><span><b>Adjuntar archivos</b><small>Arrastra aquí o haz clic. PDF, imágenes u Office; hasta 10 archivos de 10 MB.</small></span><input id="arch" type="file" multiple class="vh"></label>
<span class="help">No hay documentos adjuntos.</span></section>
</div>
<footer class="mf"><span class="hint" id="hint">Las lecturas se guardan en la bitácora al registrar.</span><button class="btn btn-s" type="button">Cerrar</button><button class="btn btn-p" type="button" id="reg">{ico("check", 18)}Registrar lecturas</button></footer>
</div>'''

JS = r'''
const $=id=>document.getElementById(id);
const DATA={
 nueva:{f:'',a:['','',''],t:['','',''],obs:'',plazo:1,reab:0,ro:0,firm:0},
 conforme:{f:'2026-11-04',a:['40.12','40.10','40.15'],t:['20.1','20.0','20.1'],obs:'',plazo:1,reab:0,ro:0,firm:0},
 fuera:{f:'2026-11-04',a:['40.12','40.31','40.10'],t:['20.1','20.0','20.1'],obs:'',plazo:1,reab:0,ro:0,firm:0},
 reabierta:{f:'2026-11-04',a:['40.12','40.31','40.10'],t:['20.1','20.0','20.1'],obs:'',plazo:0,reab:1,ro:0,firm:0},
 firmada:{f:'2026-11-04',a:['40.12','40.10','40.15'],t:['20.1','20.0','20.1'],obs:'Muestra de mezcal joven, lote de ejemplo.',plazo:0,reab:0,ro:1,firm:1}};
const ids=['fecha','alc1','alc2','alc3','tmp1','tmp2','tmp3','uexp','obs'];
let tocado=new Set();
function msg(id,t){const f=$('f-'+id),m=$('m-'+id);if(!f||!m)return;if(t){f.dataset.err='';m.hidden=false;m.querySelector('span').textContent=t;$(id).setAttribute('aria-invalid','true')}else{delete f.dataset.err;m.hidden=true;$(id).removeAttribute('aria-invalid')}}
const num=v=>v.trim()===''?null:Number(v.replace(',','.'));
function calc(){
 const a=[1,2,3].map(i=>num($('alc'+i).value));
 a.forEach((v,i)=>{const id='alc'+(i+1);if(v!==null&&tocado.has(id))msg(id,(isNaN(v)||v<0||v>100)?'Escribe un número entre 0 y 100.':'')});
 const ok=a.every(v=>v!==null&&!isNaN(v));
 const P=$('prom'),R=$('rep'),S=$('rep-st'),H=$('prom-h');
 if(!ok){P.className='big empty';P.firstChild.textContent='—';R.textContent='—';S.innerHTML='';H.textContent='Se calcula al capturar las tres lecturas.';return}
 const m=a.reduce((x,y)=>x+y,0)/3, r=Math.max(...a)-Math.min(...a);
 P.className='big';P.firstChild.textContent=m.toFixed(2);
 H.textContent=(m<35||m>55)?'Fuera del rango de referencia (35–55). Revisa la captura antes de registrar.':'Dentro del rango de referencia (35–55).';
 R.textContent=r.toFixed(2)+' % alc. vol.';
 S.innerHTML=r<=0.1+1e-9?'<span class="st ok">'+ICO.ok+'Conforme (≤ 0.10)</span>':'<span class="st bad">'+ICO.bad+'Fuera de criterio (> 0.10)</span>';
}
function render(s){
 const d=DATA[s];tocado=new Set();
 document.querySelectorAll('[data-s]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.s===s)));
 $('fecha').value=d.f;[1,2,3].forEach(i=>{$('alc'+i).value=d.a[i-1];$('tmp'+i).value=d.t[i-1]});$('obs').value=d.obs;$('uexp').value='0.02';
 ids.forEach(id=>{const el=$(id);el.readOnly=!!d.ro;el.closest('.ctrl').classList.toggle('ro',!!d.ro);msg(id,'')});
 $('drop').classList.toggle('ro',!!d.ro);$('arch').disabled=!!d.ro;
 $('al-plazo').hidden=!d.plazo;$('al-reab').hidden=!d.reab;
 const an=$('fp-an'),vb=$('fp-vb');
 if(d.firm){an.innerHTML='<span class="av ok" aria-hidden="true">MR</span><div><small>Analista</small><b>M. Ruiz</b><span class="mono help"> 4 nov 2026 12:40</span></div><span class="st ok">'+ICO.ok+'Firmado</span>';
  vb.innerHTML='<span class="av ok" aria-hidden="true">JO</span><div><small>Visto bueno</small><b>J. Orozco</b><span class="mono help"> 4 nov 2026 17:05</span></div><span class="st ok">'+ICO.ok+'Firmado</span>'}
 else{an.innerHTML=PEND('Analista','Pendiente de captura');vb.innerHTML=PEND('Visto bueno','Pendiente de supervisión')}
 $('reg').hidden=!!d.ro;$('hint').textContent=d.ro?'Bitácora firmada: solo lectura. Para corregir, supervisión debe reabrirla.':(s==='reabierta'?'Al registrar se reutiliza el motivo de la reapertura.':'Las lecturas se guardan en la bitácora al registrar.');
 calc();
}
const PEND=(r,t)=>'<span class="av" aria-hidden="true">?</span><div><small>'+r+'</small><b>'+t+'</b></div><span class="st pend">'+ICO.pend+'Pendiente</span>';
document.addEventListener('input',e=>{if(e.target.matches('input')){tocado.add(e.target.id);calc()}});
document.addEventListener('focusout',e=>{if(e.target.id){tocado.add(e.target.id);if(e.target.id==='fecha')msg('fecha','');calc()}});
$('reg').addEventListener('click',()=>{
 let primero=null;
 if(!$('fecha').value){msg('fecha','Elige la fecha en que se hizo el análisis.');primero=primero||'fecha'}
 [1,2,3].forEach(i=>['alc','tmp'].forEach(k=>{const id=k+i;if($(id).value.trim()===''){msg(id,'Falta esta lectura.');primero=primero||id}}));
 if(primero){$(primero).focus();$('hint').textContent='Faltan datos: revisa los campos marcados.';return}
 $('hint').textContent='Listo para registrar (prototipo: no se envía nada).';
});
document.querySelectorAll('[data-s]').forEach(b=>b.addEventListener('click',()=>render(b.dataset.s)));
render('nueva');
'''
ICO_JS = 'const ICO=' + json.dumps({'ok': ico('circle-check', 14), 'bad': ico('circle-x', 14), 'pend': ico('clock', 14)}) + ';'

out = f'''<title>Bitácora % Alcohol por volumen</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Google+Sans+Code:wght@400;500;600&display=swap">
<style>{ROOT}{CSS}</style><script>document.documentElement.lang='es'</script>
{BODY}
<script>{ICO_JS}{JS}</script>'''
open(os.path.join(D, 'prototipo.html'), 'w').write(out)
print('ok', len(out) // 1024, 'KB')
