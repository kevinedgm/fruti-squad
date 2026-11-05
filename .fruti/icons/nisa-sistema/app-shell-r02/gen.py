# App Shell NisaLab · r02 · estilo editorial: casi blanco, radios amplios, sombras suaves, campos delicados. Propuesta de ajuste de tokens (PROPUESTA abajo); no cambia tokens.json. Uso: python3 gen.py → shell.html
# Sidebar con módulos, submódulos desplegables y accesos frecuentes; navbar; footer. Datos de ejemplo.
import os, re, json, base64
D = os.path.dirname(os.path.abspath(__file__)); N = os.path.join(D, '..')
TOK = json.load(open(os.path.join(N, 'nabi-design-system', 'tokens.json')))
V = [f"--{t['name']}:{t['value']}" for t in TOK['color']['tokens']]
for g in ('spacing', 'radius', 'sizing', 'shadow', 'motion'): V += [f"--{t['name']}:{t['value']}" for t in TOK[g]['tokens']]
V += [f"--font-{k}:{v}" for k, v in TOK['type']['families'].items()]
TY = {s['name']: (g['family'], s) for g in TOK['type']['groups'] for s in g['styles']}
V += [f"--t-{n}:{s['fontWeight']} {s['fontSize']}/{s['lineHeight']} var(--font-{fam})" for n, (fam, s) in TY.items()]
# Propuesta de ajuste de valores (mismos nombres de token; nada nuevo)
PROPUESTA = {'bg': '#F7F8FA', 'border': '#E6E9EF', 'surface-hover': '#F7F8FA',
 'radius-sm': '8px', 'radius-md': '12px', 'radius-lg': '16px',
 'shadow-1': '0 1px 2px rgba(20, 27, 51, 0.04), 0 4px 14px -6px rgba(20, 27, 51, 0.08)',
 'shadow-2': '0 2px 6px rgba(20, 27, 51, 0.04), 0 18px 40px -18px rgba(5, 42, 118, 0.20)',
 'shadow-inset': 'inset 0 1px 2px rgba(20, 27, 51, 0.04)'}
V = [x for x in V if x.split(':', 1)[0][2:] not in PROPUESTA] + [f'--{k}:{v}' for k, v in PROPUESTA.items()]
ROOT = ':root{' + ';'.join(V) + ';color-scheme:light}' 
L = '/root/.cache/fruti-uva/package/icons/'
def ico(n, s=18):
    inner = ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse|polygon)[^>]*/>', open(L + n + '.svg').read()))
    return f'<svg class="i" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{inner}</svg>'
uri = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(N, p), 'rb').read()).decode()
LOGO, LOGO_R = uri('nisalab-final/svg/logotipo.svg'), uri('nisalab-final/svg/logotipo-respaldo.svg')
SIM_SVG = re.sub(r'<title>.*?</title>', '', open(os.path.join(N, 'nisalab-final/svg/simbolo.svg')).read()).replace('role="img" aria-label="NisaLab"', 'class="sim" width="32" height="32" role="img" aria-label="NisaLab"')

MODS = [
 ('inicio', 'house', 'Inicio', []),
 ('recepcion', 'inbox', 'Recepción', ['Registrar muestra', 'Órdenes de análisis', 'Etiquetas por imprimir']),
 ('muestras', 'test-tubes', 'Muestras', ['En proceso', 'Por ingresar', 'Historial']),
 ('captura', 'flask-conical', 'Captura', ['Resultados por capturar', 'Revisión de resultados']),
 ('bitacoras', 'clipboard-list', 'Bitácoras', ['Alcohol por volumen', 'Metanol y aldehídos', 'Extracto seco', 'Acidez', 'Azúcares', 'Congenéricos']),
 ('informes', 'file-text', 'Informes', ['Por generar', 'Por firmar', 'Emitidos', 'Certificados']),
 ('catalogos', 'library', 'Catálogos', ['Normas', 'Métodos', 'Equipos', 'Clientes']),
 ('admin', 'users', 'Administración', ['Usuarios', 'Roles y permisos']),
]
PEND = {'Por ingresar': 4, 'Resultados por capturar': 22, 'Por firmar': 3, 'Alcohol por volumen': 1}
FREC = [('clipboard-list', 'Bitácora · Alcohol por volumen', 'bitacoras'), ('inbox', 'Registrar muestra', 'recepcion'), ('file-text', 'Informes por generar', 'informes')]
ACT_MOD, ACT_SUB = 'bitacoras', 'Alcohol por volumen'

CH = ico('chevron-down', 16).replace('class="i"', 'class="i ch"')
def modulo(k, icon, nombre, subs):
    act = k == ACT_MOD
    if not subs:
        return f'<li><a class="m" href="#" data-tip="{nombre}">{ico(icon, 20)}<span class="lb">{nombre}</span></a></li>'
    items = ''.join(f'<li><a class="s" href="#"{" aria-current=page" if act and s == ACT_SUB else ""}><span class="lb">{s}</span>'
                    + (f'<span class="ct mono" aria-label="{PEND[s]} pendientes">{PEND[s]}</span>' if s in PEND else '') + '</a></li>' for s in subs)
    return (f'<li class="grp{" act" if act else ""}"><button class="m" type="button" aria-expanded="{str(act).lower()}" aria-controls="sm-{k}" data-tip="{nombre}">{ico(icon, 20)}<span class="lb">{nombre}</span>{CH}</button>'
            f'<ul class="sub" id="sm-{k}" role="list">{items}</ul></li>')
MENU = ''.join(modulo(*m) for m in MODS)
FRECH = ''.join(f'<li><a class="f" href="#" data-tip="{t}">{ico(i, 18)}<span class="lb">{t}</span></a></li>' for i, t, _ in FREC)

FILAS = [('AG-2610-0147', 'Mezcal joven · lote de ejemplo', 'M. Ruiz', '04/11 12:40', 'firma', 'Por firmar'),
         ('AG-2610-0151', 'Mezcal reposado · lote de ejemplo', '—', '—', 'pend', 'Sin capturar'),
         ('AG-2610-0139', 'Destilado de agave · lote de ejemplo', 'L. Pacheco', '03/11 17:05', 'ok', 'Firmada'),
         ('AG-2610-0132', 'Mezcal joven · lote de ejemplo', 'M. Ruiz', '02/11 10:12', 'ok', 'Firmada')]
EST = {'firma': ('alerta', 'pen-line'), 'pend': ('pend', 'clock'), 'ok': ('ok', 'circle-check')}
TAB = ''.join(f'<tr><td class="mono">{a}</td><td>{b}</td><td>{c}</td><td class="mono mut">{d}</td><td><span class="st {EST[e][0]}">{ico(EST[e][1], 14)}{f}</span></td></tr>' for a, b, c, d, e, f in FILAS)

CSS = r'''
/* App Shell: sidebar blanco a la izquierda (264 px, 72 plegado, cajón en celular); navbar blanca arriba; contenido sobre el lienzo; footer delgado al pie del contenido. */
*{box-sizing:border-box}html,body{margin:0;height:100%}[hidden]{display:none!important}
body{background:#3a4258;color:var(--text);font:var(--t-body)}
.i{flex:none}.mono{font-family:var(--font-datos);font-variant-numeric:tabular-nums}.mut{color:var(--text-muted)}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
:focus-visible{outline:2px solid var(--primary);outline-offset:2px}
/* controles del prototipo */
.ctl{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:10px max(16px,env(safe-area-inset-right,0px)) 10px max(16px,env(safe-area-inset-left,0px));color:#fff;font-size:13px}
.ctl b{font-weight:600;margin-right:4px}.ctl button{min-height:36px;padding:0 12px;border-radius:var(--radius-sm);border:1px solid rgba(255,255,255,.35);background:transparent;color:#fff;font:500 13px var(--font-sans);cursor:pointer}
.ctl button[aria-pressed="true"]{background:#fff;color:var(--primary);border-color:#fff}
/* marco que simula la ventana */
.frame{margin:0 auto;max-width:1440px;height:calc(100vh - 56px);min-height:640px;background:var(--bg);display:grid;grid-template-columns:var(--sw,264px) minmax(0,1fr);overflow:hidden;position:relative;border-radius:var(--radius-lg) var(--radius-lg) 0 0}
.frame.mini{--sw:72px}
/* ===== sidebar */
.side{background:var(--surface);border-right:1px solid var(--border);display:grid;grid-template-rows:auto 1fr auto;min-height:0;z-index:3}
.brand{display:flex;align-items:center;gap:10px;height:64px;padding:0 20px;border-bottom:1px solid var(--border)}
.brand img.l{height:28px;width:auto}.brand svg.sim{display:none}
.scroll{overflow-y:auto;overflow-x:hidden;padding:16px 12px;display:grid;grid-template-columns:minmax(0,1fr);gap:20px;align-content:start;min-width:0}.side{min-width:0}.side li,.side nav{min-width:0}
.gt{margin:0 0 6px;padding:0 10px;font:var(--t-overline);letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted)}
.side ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:minmax(0,1fr);gap:2px}
.m,.f{display:flex;align-items:center;gap:12px;width:100%;min-height:40px;padding:0 10px;border:0;border-radius:var(--radius-md);background:transparent;color:var(--text);font:500 14px/20px var(--font-sans);text-decoration:none;cursor:pointer;text-align:left}
.m .i{color:var(--text-muted)}.f .i{color:var(--primary)}
.m:hover,.f:hover,.s:hover{background:var(--bg)}
.m .lb,.f .lb{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ch{color:var(--text-muted);transition:transform var(--quick) ease}.m[aria-expanded="true"] .ch{transform:rotate(180deg)}
.grp.act>.m{color:var(--primary);font-weight:600}.grp.act>.m .i:first-child{color:var(--primary)}
.sub{padding:2px 0 6px 22px!important;margin-left:10px!important;border-left:1px solid var(--border)}
.m[aria-expanded="false"]+.sub{display:none}
.s{display:flex;align-items:center;gap:8px;min-height:36px;padding:0 10px 0 12px;border-radius:var(--radius-sm);color:var(--text-muted);font:400 14px/20px var(--font-sans);text-decoration:none;position:relative}
.s[aria-current="page"]{background:var(--primary-soft);color:var(--primary);font-weight:600}
.s[aria-current="page"]::before{content:"";position:absolute;left:-23px;top:8px;bottom:8px;width:3px;border-radius:3px;background:var(--pera)}
.s .lb{flex:1;min-width:0}.ct{min-width:22px;padding:0 6px;border-radius:999px;background:var(--bg);color:var(--text-muted);font:500 12px/20px var(--font-datos);text-align:center}
.s[aria-current="page"] .ct{background:var(--surface);color:var(--primary)}
.foot-side{border-top:1px solid var(--border);padding:10px 12px;display:grid;gap:2px}
/* plegado */
.mini .brand{padding:0;justify-content:center}.mini .brand img.l{display:none}.mini .brand svg.sim{display:block}
.mini .lb,.mini .ch,.mini .gt,.mini .sub,.mini .ct{display:none!important}
.mini .m,.mini .f{justify-content:center;padding:0;position:relative}.mini .scroll{padding:16px 12px}
.mini .grp.act>.m{background:var(--primary-soft)}
.mini [data-tip]:hover::after{content:attr(data-tip);position:absolute;left:calc(100% + 10px);top:50%;transform:translateY(-50%);white-space:nowrap;background:var(--text);color:var(--surface);font:500 12px/18px var(--font-sans);padding:4px 8px;border-radius:var(--radius-sm);z-index:5}
/* ===== navbar */
.main{display:grid;grid-template-rows:64px 1fr;min-width:0;min-height:0}
.nav{background:var(--surface);border-bottom:1px solid var(--border);display:flex;align-items:center;gap:12px;padding:0 20px 0 12px;min-width:0}
.ib{width:40px;height:40px;display:grid;place-items:center;border:0;border-radius:var(--radius-sm);background:transparent;color:var(--text-muted);cursor:pointer;position:relative;flex:none}.ib:hover{background:var(--bg);color:var(--text)}
.crumb{display:flex;align-items:center;gap:6px;min-width:0;font:var(--t-label);color:var(--text-muted);white-space:nowrap;overflow:hidden}
.crumb a{color:var(--text-muted);text-decoration:none;display:inline-flex;align-items:center;min-height:32px;padding:0 4px;margin:0 -4px}.crumb a:hover{color:var(--primary);text-decoration:underline;text-underline-offset:3px}.crumb [aria-current]{color:var(--text);font-weight:600;overflow:hidden;text-overflow:ellipsis}
.sp{flex:1}
.search{display:flex;align-items:center;gap:8px;width:min(340px,32vw);min-height:40px;padding:0 10px 0 12px;border:1px solid var(--border-control);border-radius:var(--radius-md);background:var(--surface);box-shadow:var(--shadow-inset);color:var(--text-muted);font:var(--t-body)}
.search span{flex:1;min-width:0;text-align:left;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.search .kbd{flex:none}.kbd{font:500 11px/18px var(--font-datos);padding:0 6px;border:1px solid var(--border);border-radius:4px;color:var(--text-muted)}
.badge{position:absolute;top:3px;right:2px;min-width:18px;height:18px;padding:0 5px;border-radius:999px;background:var(--fuera);color:var(--surface);font:600 11px/18px var(--font-sans);border:2px solid var(--surface);box-sizing:content-box}
.user{display:flex;align-items:center;gap:10px;min-height:44px;padding:2px 8px 2px 2px;border:0;border-radius:var(--radius-md);background:transparent;cursor:pointer;text-align:left}.user:hover{background:var(--bg)}
.uav{width:36px;height:36px;border-radius:999px;display:grid;place-items:center;background:var(--primary-soft);color:var(--primary);font:600 13px var(--font-sans)}
.user b{display:block;font:600 14px/18px var(--font-sans);color:var(--text)}.user small{display:block;font:var(--t-caption);color:var(--text-muted)}
.sep{width:1px;height:28px;background:var(--border)}
/* ===== contenido */
.cont{overflow:auto;display:grid;grid-template-rows:1fr auto;min-height:0}
.page{padding:24px 32px;display:grid;gap:20px;align-content:start}
.ph{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:flex-end;justify-content:space-between}
.ph .ctx{margin:0;font:var(--t-overline);letter-spacing:.06em;text-transform:uppercase;color:var(--primary)}
.ph h1{margin:2px 0 0;font:600 24px/32px var(--font-display);letter-spacing:-.005em}.ph p{margin:2px 0 0;color:var(--text-muted)}
.btn{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:0 16px;border-radius:var(--radius-sm);font:var(--t-button);border:1px solid transparent;cursor:pointer}
.btn.p{background:var(--primary);color:var(--surface);box-shadow:var(--shadow-primary)}.btn.s{background:var(--surface);color:var(--primary);border-color:var(--border-control);box-shadow:var(--shadow-1)}
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);box-shadow:var(--shadow-1);overflow:hidden}
.tw{overflow-x:auto}table{border-collapse:collapse;width:100%;min-width:640px}
th{text-align:left;font:var(--t-label);color:var(--text-muted);padding:10px 16px;background:var(--bg);white-space:nowrap}td{padding:12px 16px;border-top:1px solid var(--border);white-space:nowrap}
tbody tr:hover td{background:var(--surface-hover,var(--bg))}
.st{display:inline-flex;align-items:center;gap:6px;padding:3px 10px 3px 8px;border-radius:var(--radius-sm);font:500 13px/18px var(--font-sans)}
.st.ok{background:var(--conforme-soft);color:var(--on-conforme-soft)}.st.alerta{background:var(--alerta-soft);color:var(--alerta)}.st.pend{background:var(--bg);color:var(--text-muted)}
/* ===== footer */
.ft{display:flex;flex-wrap:wrap;align-items:center;gap:8px 20px;padding:14px 32px;border-top:1px solid var(--border);background:var(--surface);font:var(--t-caption);color:var(--text-muted)}
.ft img{height:20px;width:auto}.ft .ok{display:inline-flex;align-items:center;gap:6px}.ft .dot{width:8px;height:8px;border-radius:50%;background:var(--conforme)}
.ft .sp{flex:1}.ft a{color:var(--primary);text-decoration:none;font-weight:500;display:inline-flex;align-items:center;min-height:32px}.ft a:hover{text-decoration:underline;text-underline-offset:3px}
/* ===== celular: cajón */
.velo{display:none}
.frame.cel{grid-template-columns:minmax(0,1fr);max-width:390px;height:780px;border-radius:var(--radius-lg)}
.cel .side{position:absolute;inset:0 auto 0 0;width:300px;box-shadow:var(--shadow-overlay);transform:translateX(-102%);transition:transform var(--quick) var(--ease-out)}
.cel.open .side{transform:none}.cel.open .velo{display:block;position:absolute;inset:0;background:rgba(20,27,51,.55);z-index:2}
.cel .search,.cel .user div,.cel .sep,.cel .apps,.cel .crumb .mid{display:none}
.cel .search-ib{display:grid!important}.search-ib{display:none!important}
.cel .page{padding:16px}.cel .ft{padding:12px 16px}.cel .nav{padding:0 8px;gap:4px}.cel .ph h1{font-size:22px;line-height:30px}
@media (prefers-reduced-motion:reduce){.ch,.cel .side{transition:none}}

/* ===== r02 · estilo editorial */
body{background:#3a4258}
.frame{background:var(--bg);gap:0}
.side{background:transparent;border-right:0}
.brand{border-bottom:0;height:72px;padding:0 24px}
.scroll{padding:8px 16px 16px;gap:28px}
.gt{font-weight:600;color:var(--text-muted);opacity:1;padding:0 12px;margin-bottom:8px}
.m,.f{border-radius:var(--radius-md);min-height:40px;padding:0 12px;font-weight:500}
.m:hover,.f:hover,.s:hover{background:rgba(20,27,51,.04)}
.grp.act>.m{color:var(--text)}.grp.act>.m .i:first-child{color:var(--primary)}
.sub{border-left:0!important;padding:2px 0 6px 16px!important;margin-left:10px!important}.s .lb{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.s{border-radius:var(--radius-md);min-height:36px;padding:0 12px}
.s[aria-current="page"]{background:var(--surface);color:var(--primary);box-shadow:var(--shadow-1)}
.s[aria-current="page"]::before{left:-12px;top:50%;bottom:auto;width:6px;height:6px;margin-top:-3px;border-radius:50%}
.ct{background:rgba(20,27,51,.05)}
.foot-side{border-top:0;padding:12px 16px 16px}
.main{margin:12px 12px 0 0;background:var(--surface);border-radius:var(--radius-lg) var(--radius-lg) 0 0;box-shadow:0 0 0 1px rgba(20,27,51,.04),0 10px 40px -12px rgba(20,27,51,.12);grid-template-rows:68px 1fr;overflow:hidden}
.nav{background:rgba(255,255,255,.85);backdrop-filter:saturate(1.4) blur(10px);border-bottom:1px solid var(--border);padding:0 24px 0 16px}
.search{border:1px solid var(--border);border-radius:var(--radius-md);background:var(--bg);box-shadow:none;width:min(360px,32vw)}
.search:hover{border-color:var(--border-control)}
.ib{border-radius:var(--radius-md)}.ib:hover{background:var(--bg)}
.badge{background:var(--primary);border-color:var(--surface)}
.user{border-radius:var(--radius-md)}.uav{background:var(--bg);box-shadow:inset 0 0 0 1px var(--border)}
.sep{background:var(--border)}
.cont{background:var(--surface)}
.page{padding:36px 40px 32px;gap:28px;max-width:1120px}
.ph .ctx{color:var(--primary)}
.ph h1{font:600 30px/38px var(--font-display);letter-spacing:-.02em;margin-top:6px}
.ph p{font-size:15px;line-height:24px;margin-top:4px}
.btn{border-radius:var(--radius-sm);min-height:40px;padding:0 18px}
.btn.s{border-color:var(--border);box-shadow:var(--shadow-1)}.btn.s:hover{border-color:var(--border-control)}
.btn.p{box-shadow:0 1px 2px rgba(5,42,118,.25),0 8px 20px -8px rgba(5,42,118,.45)}
/* barra de filtros con campos delicados: borde suave y línea inferior de 3:1 */
.tools{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end}
.fld{display:grid;gap:6px;min-width:0}.fld label{font:var(--t-label);color:var(--text)}
.ctrl{display:flex;align-items:center;gap:8px;min-height:42px;padding:0 14px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-md);
 box-shadow:inset 0 -1px 0 var(--border-control),var(--shadow-1);color:var(--text);font:var(--t-body);transition:box-shadow var(--quick) ease,border-color var(--quick) ease}
.ctrl:hover{border-color:#D5DAE3}
.ctrl:focus-within{border-color:var(--primary);box-shadow:inset 0 -1px 0 var(--primary),0 0 0 4px var(--primary-soft)}
.ctrl input,.ctrl select{border:0;outline:0;background:none;font:inherit;color:inherit;min-width:0;width:100%;min-height:40px;appearance:none}
.ctrl input::placeholder{color:var(--text-muted)}.ctrl .i{color:var(--text-muted)}
.f-q{flex:1 1 280px}.f-e{flex:0 1 200px}.f-f{flex:0 1 180px}
.card{border:0;border-radius:var(--radius-lg);box-shadow:0 0 0 1px rgba(20,27,51,.05),var(--shadow-2)}
th{background:transparent;font:var(--t-overline);letter-spacing:.06em;text-transform:uppercase;padding:14px 20px;border-bottom:1px solid var(--border)}
td{padding:16px 20px;border-top:1px solid #EEF0F4}tbody tr:first-child td{border-top:0}
tbody tr:hover td{background:var(--bg)}
.st{border-radius:999px;padding:3px 10px 3px 8px}
.ft{background:transparent;border-top:1px solid var(--border);padding:16px 40px}
.cel .main{margin:0;border-radius:0}.cel .page{padding:20px 16px}.cel .ph h1{font-size:24px;line-height:32px}.cel .ft{padding:12px 16px}
.cel .side{background:var(--bg)}
'''
BODY = f'''<div class="ctl" role="group" aria-label="Vista del prototipo"><b>Vista:</b><button data-v="exp" aria-pressed="true">Escritorio</button><button data-v="mini" aria-pressed="false">Menú plegado</button><button data-v="cel" aria-pressed="false">Celular</button><button data-v="celopen" aria-pressed="false">Celular · menú abierto</button></div>
<div class="frame" id="frame">
<aside class="side" aria-label="Menú de NisaLab"><div class="brand"><img class="l" src="{LOGO}" alt="NisaLab">{SIM_SVG}</div>
<div class="scroll"><nav aria-labelledby="g-frec"><p class="gt" id="g-frec">Accesos frecuentes</p><ul role="list">{FRECH}</ul></nav>
<nav aria-labelledby="g-mod"><p class="gt" id="g-mod">Módulos</p><ul role="list">{MENU}</ul></nav></div>
<div class="foot-side"><a class="m" href="#" data-tip="Ayuda">{ico("circle-help", 20)}<span class="lb">Ayuda</span></a><button class="m" type="button" id="plegar" data-tip="Plegar menú">{ico("panel-left-close", 20)}<span class="lb">Plegar menú</span></button></div></aside>
<div class="velo" id="velo"></div>
<div class="main"><header class="nav"><button class="ib" type="button" id="menu" aria-label="Abrir o plegar el menú">{ico("menu", 20)}</button>
<nav class="crumb" aria-label="Ruta"><a href="#">Bitácoras</a><span aria-hidden="true">/</span><span aria-current="page">Alcohol por volumen</span></nav><span class="sp"></span>
<button class="search" type="button" aria-label="Buscar en NisaLab (Ctrl K)">{ico("search", 18)}<span>Buscar folio, muestra o cliente</span><span class="kbd">Ctrl K</span></button>
<button class="ib search-ib" type="button" aria-label="Buscar">{ico("search", 20)}</button>
<button class="ib" type="button" aria-label="Avisos: 3 sin leer">{ico("bell", 20)}<span class="badge" aria-hidden="true">3</span></button>
<button class="ib apps" type="button" aria-label="Aplicaciones de Nisa Nabani">{ico("layout-grid", 20)}</button><span class="sep" aria-hidden="true"></span>
<button class="user" type="button" aria-label="Cuenta de Mariana Ruiz, analista"><span class="uav" aria-hidden="true">MR</span><div><b>Mariana Ruiz</b><small>Analista · Bebidas</small></div></button></header>
<div class="cont"><main class="page" id="contenido"><div class="ph"><div><p class="ctx">Bitácoras · BIT-02-01</p><h1>Alcohol por volumen</h1><p>8 registros esta semana · 1 por firmar</p></div><div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn s">{ico("download", 16)}Exportar</button><button class="btn p">{ico("plus", 16)}Nueva bitácora</button></div></div>
<div class="tools" role="search" aria-label="Filtrar bitácoras"><div class="fld f-q"><label for="q">Buscar</label><span class="ctrl">{ico("search", 18)}<input id="q" placeholder="Folio, muestra o analista"></span></div>
<div class="fld f-e"><label for="e">Estado</label><span class="ctrl"><select id="e"><option>Todos</option><option>Por firmar</option><option>Sin capturar</option><option>Firmada</option></select>{ico("chevron-down", 16)}</span></div>
<div class="fld f-f"><label for="d">Desde</label><span class="ctrl"><input id="d" class="mono" value="01/11/2026"></span></div></div>
<div class="card"><div class="tw"><table><caption class="vh">Bitácoras de alcohol por volumen (ejemplo)</caption><thead><tr><th>Folio</th><th>Muestra</th><th>Analista</th><th>Capturada</th><th>Estado</th></tr></thead><tbody>{TAB}</tbody></table></div></div></main>
<footer class="ft"><img src="{LOGO_R}" alt="NisaLab de Nisa Nabani"><span class="mono">v3.4.1</span><span class="ok"><span class="dot" aria-hidden="true"></span>Sistema en línea</span><span class="sp"></span><span>Hora del servidor <span class="mono">05/11/2026 10:42</span></span><a href="#">Soporte</a></footer></div></div></div>'''
JS = r'''
const F=document.getElementById('frame');
function vista(v){document.querySelectorAll('[data-v]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.v===v)));
 F.classList.toggle('mini',v==='mini');F.classList.toggle('cel',v.startsWith('cel'));F.classList.toggle('open',v==='celopen');}
document.querySelectorAll('[data-v]').forEach(b=>b.addEventListener('click',()=>vista(b.dataset.v)));
document.querySelectorAll('.grp>.m').forEach(b=>b.addEventListener('click',()=>{if(F.classList.contains('mini')){F.classList.remove('mini');vista('exp');b.setAttribute('aria-expanded','true');return}b.setAttribute('aria-expanded',String(b.getAttribute('aria-expanded')!=='true'))}));
document.getElementById('plegar').addEventListener('click',()=>vista(F.classList.contains('mini')?'exp':'mini'));
document.getElementById('menu').addEventListener('click',()=>{if(F.classList.contains('cel'))vista(F.classList.contains('open')?'cel':'celopen');else vista(F.classList.contains('mini')?'exp':'mini')});
document.getElementById('velo').addEventListener('click',()=>vista('cel'));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&F.classList.contains('open'))vista('cel')});
'''
out = f'''<title>App Shell NisaLab</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Google+Sans+Code:wght@400;500;600&display=swap">
<style>{ROOT}{CSS}</style><script>document.documentElement.lang='es'</script>
{BODY}<script>{JS}</script>'''
open(os.path.join(D, 'shell.html'), 'w').write(out)
print('ok', len(out) // 1024, 'KB')
