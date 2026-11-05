# NisaLab · revisión de color del design system completo · r01. Uso: python3 gen.py → revision.html
# Fuente: ../nabi-design-system/tokens.json (53 colores) y components/*/preview.html (usos reales con var()).
# Es PROPUESTA: no cambia tokens.json hasta aprobarse.
import os, re, json, glob, html
D = os.path.dirname(os.path.abspath(__file__)); DS = os.path.join(D, '..', 'nabi-design-system')
T = json.load(open(os.path.join(DS, 'tokens.json')))['color']['tokens']
V = {t['name']: t['value'] for t in T}; V['focus'] = V['primary']
import subprocess  # usos medidos en los componentes ANTES de aplicar la reducción (commit 60673b6)
TOP = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True, cwd=D).stdout.strip()
REF = '60673b6'; BASE = '.fruti/icons/nisa-sistema/nabi-design-system'
_ls = subprocess.run(['git', 'ls-tree', '-r', '--name-only', REF, BASE + '/components'], capture_output=True, text=True, cwd=TOP).stdout.split()
H = {f.split('/')[-2]: subprocess.run(['git', 'show', f'{REF}:{f}'], capture_output=True, text=True, cwd=TOP).stdout for f in _ls if f.endswith('preview.html')}
T = json.loads(subprocess.run(['git', 'show', f'{REF}:{BASE}/tokens.json'], capture_output=True, text=True, cwd=TOP).stdout)['color']['tokens']
V = {t['name']: t['value'] for t in T}; V['focus'] = V['primary']
def usos(n):
    p = re.compile(r'var\(--(?:nn-)?' + re.escape(n) + r'\s*[,)]')
    return sum(len(p.findall(s)) for s in H.values())
def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b): la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + .05) / (lb + .05)
def c(a, b): return f'{cr(V.get(a, a), V.get(b, b)):.1f}:1'
e = html.escape

# Decisión por color: (queda | une → destino | quita), motivo
K, U, Q = 'queda', 'une', 'quita'
DEC = {
 'bg': (K, '', 'Lienzo. Absorbe hover, encabezado de tabla, solo lectura y estado pendiente.'),
 'surface': (K, '', 'Tarjetas, tablas, campos. También el texto sobre azul (blanco).'),
 'surface-sunken': (U, 'bg', f'#EEF1F6 frente a #F2F4F8: casi igual. Sobre él, el borde de campo mide {c("border-control", "surface-sunken")} y no cumple; sobre bg, {c("border-control", "bg")}.'),
 'surface-hover': (U, 'bg', 'Tercer gris claro entre bg y surface; el hover de fila se lee igual con bg.'),
 'text': (K, '', f'Texto principal. {c("text", "bg")} sobre bg.'),
 'text-muted': (K, '', f'Etiquetas, ayudas, placeholders, pendiente. {c("text-muted", "bg")} sobre bg.'),
 'text-subtle': (U, 'text-muted', 'Segundo gris de texto casi igual al primero (#646B80 frente a #535B70).'),
 'border': (K, '', 'Separa filas y tarjetas. Decorativo.'),
 'border-strong': (U, 'border', 'Tercer gris de borde; solo hacía falta sobre surface-sunken, que también se va.'),
 'border-control': (K, '', f'Contorno de campos: el único borde que debe medir 3:1 ({c("border-control", "surface")}).'),
 'primary': (K, '', f'Acción, enlace, foco, encabezado, texto sobre pera ({c("primary", "pera")}).'),
 'primary-hover': (K, '', 'Hover y presionado de la acción principal.'),
 'on-primary': (U, 'surface', 'Mismo valor que surface (#FFFFFF).'),
 'primary-soft': (K, '', f'Selección, filtro activo, «En proceso». Azul encima {c("primary", "primary-soft")}.'),
 'pera': (K, '', 'La célula del símbolo, lo que está en curso y «Urgente». Una sola cosa por pantalla.'),
 'pera-soft': (U, 'primary-soft', 'El registro en curso ya se marca con el filete pera; el fondo puede ser el de selección.'),
 'on-pera': (U, 'primary', 'Mismo valor que primary (#052A76).'),
 'focus': (U, 'primary', 'No es un color: es un alias de primary. La regla del anillo queda en el README.'),
 'conforme': (K, '', f'Conforme, terminada, pagada. {c("conforme", "surface")} sobre blanco.'),
 'conforme-soft': (K, '', 'Fondo de conforme y de «Terminada».'),
 'on-conforme-soft': (K, '', f'Necesario: conforme sobre su fondo mide {c("conforme", "conforme-soft")} (mínimo 4.5).'),
 'fuera': (K, '', f'Fuera de especificación, cancelada, no pagada. {c("fuera", "fuera-soft")} sobre su fondo.'),
 'fuera-soft': (K, '', 'Fondo de fuera y de «Cancelada».'),
 'on-fuera-soft': (U, 'fuera', f'fuera ya se lee sobre su fondo ({c("fuera", "fuera-soft")}).'),
 'alerta': (K, '', f'Cerca del límite, no ingresada, pago parcial. {c("alerta", "alerta-soft")} sobre su fondo.'),
 'alerta-soft': (K, '', 'Fondo de alerta y de «No ingresada».'),
 'on-alerta-soft': (U, 'alerta', f'alerta ya se lee sobre su fondo ({c("alerta", "alerta-soft")}).'),
 'alerta-fill': (Q, '', 'Sin ningún uso en los componentes; los marcadores pueden ir en alerta.'),
 'pendiente': (U, 'text-muted', '#475467 frente a #535B70: el mismo gris. Pendiente no es urgente: se dice con gris, reloj y texto.'),
 'pendiente-soft': (U, 'bg', 'Fondo gris neutro: el del lienzo basta.'),
 'on-pendiente-soft': (U, 'text-muted', 'Igual que pendiente.'),
}
AREAS = [t['name'] for t in T if t['name'].startswith('area-')]
for a in AREAS: DEC[a] = (K, '', 'Identidad del área (no estado). Va en la marca y el ícono de cada área; los archivos de marca ya la usan.')
MAPA = {'muestra-no-ingresada': 'alerta-soft', 'on-muestra-no-ingresada': 'alerta', 'muestra-en-proceso': 'primary-soft', 'on-muestra-en-proceso': 'primary',
        'muestra-generando-informe': 'primary-soft', 'on-muestra-generando-informe': 'primary', 'muestra-terminada': 'conforme-soft', 'on-muestra-terminada': 'on-conforme-soft',
        'muestra-cancelada': 'fuera-soft', 'on-muestra-cancelada': 'fuera', 'pago-no-pagada': 'fuera', 'pago-parcial': 'alerta', 'pago-pagada': 'conforme', 'pago-cortesia': 'primary'}
MOT = {'pago-no-pagada': 'Mismo valor que fuera.', 'pago-cortesia': 'Mismo valor que primary.', 'pago-pagada': 'Mismo valor que on-muestra-terminada; conforme mide 5.1:1 sobre blanco.',
       'pago-parcial': 'Naranja propio; alerta dice lo mismo (queda saldo) y mide 5.5:1.', 'muestra-generando-informe': 'Único violeta del sistema. Con En proceso lo distinguen el ícono de etapa (¼ y ¾) y el texto.'}
for k, v in MAPA.items(): DEC[k] = (U, v, MOT.get(k, 'Pastel propio que repite la familia de un estado existente (ámbar, azul, verde, rojo).'))

GR = [('Básicos', lambda n: n in ('bg', 'surface', 'surface-sunken', 'surface-hover', 'text', 'text-muted', 'text-subtle', 'border', 'border-strong', 'border-control')),
      ('Marca', lambda n: n.startswith(('primary', 'on-primary', 'pera', 'on-pera', 'focus'))),
      ('Estados del resultado', lambda n: n.split('-')[0] in ('conforme', 'fuera', 'alerta', 'pendiente') or n.startswith('on-') and n.split('-')[1] in ('conforme', 'fuera', 'alerta', 'pendiente')),
      ('Áreas', lambda n: n.startswith('area-')),
      ('Proceso de la muestra y pago', lambda n: 'muestra-' in n or n.startswith('pago-'))]
ETQ = {K: ('Queda', 'k'), U: ('Se une', 'u'), Q: ('Se quita', 'q')}
def fila(t):
    n = t['name']; d, dst, mot = DEC[n]; v = V[n]
    a = f' → <code>{dst}</code>' if dst else ''
    return (f'<tr class="{ETQ[d][1]}"><td><span class="dot" style="background:{v}"></span><code>{n}</code></td><td><code>{t["value"]}</code></td><td class="num">{usos(n)}</td>'
            f'<td><span class="tag {ETQ[d][1]}">{ETQ[d][0]}</span>{a}</td><td>{mot}</td></tr>')
TAB = ''
for g, f in GR:
    rows = [t for t in T if f(t['name'])]
    k = sum(DEC[t['name']][0] == K for t in rows)
    TAB += f'<tr class="gh"><th colspan="5">{g} · {len(rows)} hoy → {k} quedan</th></tr>' + ''.join(fila(t) for t in rows)
QUEDAN = [n for n in V if n != 'focus' and DEC.get(n, (None,))[0] == K]
NUCLEO = [n for n in QUEDAN if not n.startswith('area-')]

# ---------- Muestras de estado: actual frente a propuesta
def etapa(n):
    B = '<svg width="13" height="13" viewBox="0 0 16 16" aria-hidden="true">'
    if n == 0: return B + '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75" stroke-dasharray="2.6 2.1"/></svg>'
    if n == 3: return B + '<circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M4.8 8.2 7 10.4 11.2 5.9" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    if n == 4: return B + '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75"/><path d="M3.4 12.6 12.6 3.4" stroke="currentColor" stroke-width="1.75"/></svg>'
    arc = 'M8 8 V2.5 A5.5 5.5 0 0 1 8 13.5 Z' if n == 1 else 'M8 8 V2.5 A5.5 5.5 0 1 1 2.5 8 Z'
    return B + f'<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75"/><path d="{arc}" fill="currentColor"/></svg>'
PROC = [('no-ingresada', 'No ingresada', 0), ('en-proceso', 'En proceso', 1), ('generando-informe', 'Generando informe', 2), ('terminada', 'Terminada', 3), ('cancelada', 'Cancelada', 4)]
PAGO = [('no-pagada', 'No pagada'), ('parcial', 'Pago parcial'), ('pagada', 'Pagada'), ('cortesia', 'Cortesía')]
def pills(prop):
    out = ''
    for k, t, i in PROC:
        bg = V[MAPA['muestra-' + k]] if prop else V['muestra-' + k]; tx = V[MAPA['on-muestra-' + k]] if prop else V['on-muestra-' + k]
        out += f'<span class="ps" style="background:{bg};color:{tx}">{etapa(i)}{t}<small>{cr(tx, bg):.1f}</small></span>'
    out += '<span class="sep"></span>'
    for k, t in PAGO:
        col = V[MAPA['pago-' + k]] if prop else V['pago-' + k]
        out += f'<span class="et" style="color:{col};border-color:{col}">{t}<small>{cr(col, "#FFFFFF"):.1f}</small></span>'
    return out
def tabla(prop):
    head = V['bg'] if prop else V['surface-sunken']; hov = V['bg'] if prop else V['surface-hover']
    ro = V['bg'] if prop else V['surface-sunken']; pend = (V['bg'], V['text-muted']) if prop else (V['pendiente-soft'], V['on-pendiente-soft'])
    cur = V['primary-soft'] if prop else V['pera-soft']
    return f'''<div class="mini"><div class="mr h" style="background:{head}"><span>Parámetro</span><span>Resultado</span><span>Estado</span></div>
<div class="mr"><span>pH</span><span class="v">7.40</span><span class="rs" style="background:{V['conforme-soft']};color:{V['on-conforme-soft']}">Conforme</span></div>
<div class="mr" style="background:{hov}"><span>Plomo <small>(hover)</small></span><span class="v">0.012</span><span class="rs" style="background:{V['fuera-soft']};color:{V['fuera'] if prop else V['on-fuera-soft']}">Fuera</span></div>
<div class="mr cur" style="background:{cur}"><span>Coliformes <small>(en curso)</small></span><span class="v">—</span><span class="rs" style="background:{pend[0]};color:{pend[1]}">Pendiente</span></div>
<label class="fl">Temperatura (solo lectura)</label><span class="campo" style="background:{ro}"><span>20.0</span><small>borde {cr(V['border-control'], ro):.2f}:1</small></span></div>'''

CSS = '''
:root{--bg:#F2F4F8;--surface:#fff;--text:#141B33;--muted:#535B70;--border:#DFE3EC;--ctrl:#858DA3;--primary:#052A76;--psoft:#E8EDF7;--pera:#C2D225;
--ok:#2E7D32;--oksoft:#E3F1E4;--onok:#1E5A22;--bad:#B42318;--badsoft:#FDE7E5;--warn:#8A6100;--warnsoft:#FBF0CC;
--sans:"Poppins",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace;color-scheme:light}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 var(--sans)}
h1,h2,h3{margin:0;text-wrap:balance}p{margin:0}code,.num{font:500 12.5px var(--mono)}
.wrap{max-width:1240px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
header{background:var(--primary);color:#fff}header .wrap{padding-block:28px 34px;display:grid;gap:12px}
header h1{font:700 clamp(28px,5vw,42px)/1.1 var(--sans);letter-spacing:-.02em}header h1 span{font-weight:400}header p{color:#C3CBE4;max-width:64ch}
.big{display:flex;flex-wrap:wrap;gap:10px}.big span{border:1px solid rgba(255,255,255,.3);border-radius:8px;padding:6px 12px;font-size:14px}.big b{font:600 22px var(--mono);margin-right:6px}
.big .p{border-color:var(--pera)}.big .p b{color:var(--pera)}
section{display:grid;grid-template-columns:minmax(0,1fr);gap:16px;padding-block:32px;border-bottom:1px solid var(--border);min-width:0}
section>h2{font:700 26px/1.2 var(--sans);letter-spacing:-.015em}section>h2 span{font-weight:400}.ey{font:600 11px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--primary)}
.intro{color:var(--muted);max-width:70ch}.pie{font-size:13px;color:var(--muted)}
.tres{display:grid;gap:12px}@media(min-width:860px){.tres{grid-template-columns:repeat(3,minmax(0,1fr))}}
.card{background:#fff;border:1px solid var(--border);border-radius:12px;padding:18px;display:grid;gap:6px;align-content:start}.card p{color:var(--muted);font-size:14px}
.card .kk{font:600 11px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.tw{overflow-x:auto;background:#fff;border:1px solid var(--border);border-radius:12px}
table{border-collapse:collapse;width:100%;font-size:13.5px;min-width:760px}th{text-align:left;padding:9px 12px;color:var(--muted);font:500 12.5px var(--sans);background:var(--bg)}
tr.gh th{background:#fff;color:var(--text);font:600 14px var(--sans);padding-top:18px;border-top:1px solid var(--border)}
td{padding:8px 12px;border-top:1px solid var(--border);vertical-align:top}td.num{text-align:right}tr.q td,tr.u td{color:var(--muted)}
.dot{display:inline-block;width:14px;height:14px;border-radius:4px;margin-right:8px;vertical-align:-2px;border:1px solid rgba(20,27,51,.15)}
.tag{display:inline-block;font:600 11.5px var(--sans);border-radius:6px;padding:1px 8px;white-space:nowrap}.tag.k{background:var(--oksoft);color:var(--onok)}.tag.u{background:var(--psoft);color:var(--primary)}.tag.q{background:var(--badsoft);color:var(--bad)}
.paleta{display:flex;flex-wrap:wrap;gap:8px}.sw{display:grid;gap:4px;width:118px;font-size:12px;color:var(--muted)}.sw i{display:block;height:54px;border-radius:10px;border:1px solid rgba(20,27,51,.1)}.sw code{font-size:11.5px;color:var(--text)}
.duo{display:grid;gap:16px}@media(min-width:1000px){.duo{grid-template-columns:repeat(2,minmax(0,1fr))}}
.lado{background:#fff;border:1px solid var(--border);border-radius:14px;padding:16px;display:grid;gap:12px;align-content:start;min-width:0}.lt{font:700 12px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.fila{display:flex;flex-wrap:wrap;gap:6px;align-items:center}.sep{flex-basis:100%}
.ps,.et,.rs{display:inline-flex;align-items:center;gap:5px;font:500 12.5px/18px var(--sans);border-radius:999px;padding:3px 10px;white-space:nowrap}.ps small,.et small{font:500 10.5px var(--mono);opacity:.85}
.et{border:1.5px solid;border-radius:6px;background:#fff}.rs{border-radius:6px;font-size:12px;justify-self:start}
.mini{display:grid;gap:0;border:1px solid var(--border);border-radius:10px;overflow:hidden;font-size:13px}.mr{display:grid;grid-template-columns:minmax(0,1.3fr) 70px minmax(0,1fr);gap:10px;align-items:center;padding:8px 12px;border-top:1px solid var(--border);background:#fff}
.mr.h{border:0;color:var(--muted);font-size:12px;font-weight:500}.mr .v{font:500 13px var(--mono);text-align:right}.mr small{color:var(--muted)}.mr.cur{box-shadow:inset 3px 0 0 var(--pera)}
.fl{font-size:12px;font-weight:500;color:var(--muted);padding:10px 12px 4px;border-top:1px solid var(--border)}.campo{display:flex;justify-content:space-between;align-items:center;margin:0 12px 12px;min-height:40px;padding:0 12px;border:1px solid var(--ctrl);border-radius:8px;font:500 13px var(--mono)}.campo small{font:500 11px var(--sans);color:var(--muted)}
.dec{display:grid;gap:12px}@media(min-width:860px){.dec{grid-template-columns:repeat(3,minmax(0,1fr))}}.rec{font-size:12.5px;font-weight:600;color:var(--onok);background:var(--oksoft);border-radius:6px;padding:2px 8px;justify-self:start}
.lista{margin:0;padding-left:20px;display:grid;gap:6px;max-width:72ch}
footer{padding-block:24px 40px;color:var(--muted);font-size:13px}
'''
def sw(n): return f'<div class="sw"><i style="background:{V[n]}"></i><code>{n}</code>{V[n]}</div>'
GRUPOS_FIN = [('Básicos (6)', ['bg', 'surface', 'text', 'text-muted', 'border', 'border-control']), ('Marca (4)', ['primary', 'primary-hover', 'primary-soft', 'pera']),
              ('Estados (7)', ['conforme', 'conforme-soft', 'on-conforme-soft', 'alerta', 'alerta-soft', 'fuera', 'fuera-soft']), ('Áreas (8)', AREAS)]
FIN = ''.join(f'<h3 style="font:600 16px var(--sans)">{g}</h3><div class="paleta">{"".join(sw(n) for n in ns)}</div>' for g, ns in GRUPOS_FIN)
n_usados = sum(usos(t['name']) > 0 for t in T)

out = f'''<title>NisaLab · revisión de color</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap">
<style>{CSS}</style><script>document.documentElement.lang='es'</script>
<header><div class="wrap"><h1>Color de NisaLab: <span>revisión completa</span></h1><p>Los 53 colores del design system, uno por uno: cuál queda, cuál se une a otro que ya dice lo mismo y cuál sobra. Aprobada y aplicada el 5 de noviembre de 2026 (design system, versión 19).</p>
<div class="big"><span><b>53</b>hoy</span><span><b>{len(QUEDAN)}</b>propuesta</span><span><b>{len(NUCLEO)}</b>sin contar áreas</span><span class="p"><b>0</b>colores nuevos</span></div></div></header>
<main class="wrap">
<section aria-labelledby="s1"><span class="ey">Panorama</span><h2 id="s1">Qué encontré</h2>
<div class="tres"><div class="card"><span class="kk">Hecho</span><h3>Cuatro valores repetidos</h3><p>#052A76 se llama primary, on-pera y pago-cortesia; #FFFFFF es surface y on-primary; #B42318 es fuera y pago-no-pagada; #166534 es on-muestra-terminada y pago-pagada.</p></div>
<div class="card"><span class="kk">Hecho</span><h3>{53 - n_usados} de 53 sin uso con var()</h3><p>Los componentes usaban {n_usados} colores. Sin uso: alerta, alerta-fill, pendiente y 7 de las 8 áreas (estas viven en sus archivos de marca).</p></div>
<div class="card"><span class="kk">Hecho</span><h3>Dos juegos de estados</h3><p>Resultado (conforme, alerta, fuera, pendiente) y proceso (5 pasteles: ámbar, azul, violeta, verde, rojo). Cuatro de los cinco repiten la familia de un estado de resultado.</p></div></div>
<p class="intro">Criterio: un color se queda si nombra algo que ningún otro nombra, o si sin él algo no cumple contraste. Las áreas se quedan aunque no sean estados: son la identidad de cada división y ya viven en sus logotipos.</p></section>
<section aria-labelledby="s2"><span class="ey">Resultado</span><h2 id="s2">{len(QUEDAN)} colores, <span>{len(NUCLEO)} sin contar áreas</span></h2>
<p class="intro">Es la misma paleta que ya usa bitácoras (ronda 2), más las ocho áreas. Todo módulo de NisaLab se pinta con estos colores.</p>{FIN}</section>
<section aria-labelledby="s3"><span class="ey">Evidencia</span><h2 id="s3">Antes <span>y después</span></h2>
<p class="intro">Mismo marcado con los valores actuales y los propuestos. El número junto a cada etiqueta es su contraste medido. Datos de ejemplo.</p>
<div class="duo"><div class="lado"><span class="lt">Hoy · 53 colores</span><div class="fila">{pills(False)}</div>{tabla(False)}</div>
<div class="lado"><span class="lt">Propuesta · {len(QUEDAN)} colores</span><div class="fila">{pills(True)}</div>{tabla(True)}</div></div>
<ul class="lista"><li><b>Proceso:</b> conserva la familia de tono que el personal ya asocia (ámbar, azul, verde, rojo). Solo el violeta de «Generando informe» pasa a azul; lo separan de «En proceso» el ícono de etapa y el texto.</li>
<li><b>Pago:</b> las etiquetas con contorno usan los mismos colores de estado; todas superan 4.5:1 sobre blanco.</li>
<li><b>Tabla:</b> encabezado, hover, solo lectura y pendiente usan el gris del lienzo. El registro en curso conserva su filete pera sobre el fondo de selección.</li></ul></section>
<section aria-labelledby="s4"><span class="ey">Detalle</span><h2 id="s4">Los 53, <span>uno por uno</span></h2>
<p class="intro">«Usos» cuenta las veces que los componentes llamaban al color con var() antes de la reducción, incluidas las llamadas con valor de respaldo.</p>
<div class="tw"><table><thead><tr><th>Color</th><th>Valor</th><th class="num">Usos</th><th>Decisión</th><th>Por qué</th></tr></thead><tbody>{TAB}</tbody></table></div></section>
<section aria-labelledby="s5"><span class="ey">Decisiones</span><h2 id="s5">Lo que tienes <span>que elegir</span></h2>
<div class="dec"><div class="card"><span class="rec">Recomendado: unir</span><h3>1. Proceso y pago</h3><p>Los aprobaste porque el personal ya los asocia. La propuesta conserva esas familias de tono y quita 14 valores; el único cambio visible es el violeta. Alternativa: dejarlos como están (39 colores en vez de 25).</p></div>
<div class="card"><span class="rec">Recomendado: conservar</span><h3>2. Las ocho áreas</h3><p>No son estados ni básicos, pero son la identidad de cada división y están en sus logotipos e íconos. Quitarlas obligaría a rehacer esos archivos.</p></div>
<div class="card"><span class="rec">Recomendado: unir</span><h3>3. Pendiente en gris del texto</h3><p>Su gris es casi el de text-muted. Pendiente se seguiría leyendo por reloj y texto; deja de tener color propio, como corresponde a algo que no es urgente.</p></div></div></section>
<section aria-labelledby="s6"><span class="ey">Aplicado</span><h2 id="s6">Qué cambió</h2><ul class="lista">
<li>tokens.json bajó a {len(QUEDAN)} colores; el README lista cada color retirado con su destino.</li>
<li>Los 14 componentes: los que usaban colores unidos (surface-sunken, surface-hover, text-subtle, border-strong, on-primary, pera-soft, focus, on-fuera-soft, on-alerta-soft, pendiente-*) pasaron a su destino (174 reemplazos, script nabi-design-system/color-reduccion.py).</li>
<li>EstadoMuestra usa los colores de estado. README, módulos, documentación de componentes y manual de marca actualizados.</li></ul></section>
</main><footer class="wrap">Fuente: tokens.json del design system NisaLab v3 y los 14 componentes. Contrastes calculados por el generador.</footer>'''
open(os.path.join(D, 'revision.html'), 'w').write(out)
print('ok', len(QUEDAN), len(NUCLEO), n_usados)
