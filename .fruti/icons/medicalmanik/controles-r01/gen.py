# Ecosistema Manik · familia de controles r01 (botones, campos y controles de selección).
# Pedido (2026-11-05): «la familia de botones, inputs y de control para todas las aplicaciones del ecosistema Manik,
# para que se homogenicen todas». Alcance: las 7 apps; el directorio para pacientes tiene su propia familia (píldora).
# Valores: se leen de design-system/project/tokens.json (no hay colores escritos a mano). Uso: python3 gen.py → controles.html
import json, os, base64
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
T = json.load(open(os.path.join(M, 'design-system/project/tokens.json')))
V = {}
for g in ('color', 'radius', 'shadow', 'layout', 'spacing'):
    for x in T[g]['tokens']: V[x['name']] = x['value']
for k, v in V.items():
    if isinstance(v, str) and v.startswith('{'): V[k] = V[v.strip('{}')]
ROOT = ';'.join(f'--{k}:{v}' for k, v in V.items())
FAM = T['type']['families']

def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b):
    la, lb = sorted((lum(V.get(a, a)), lum(V.get(b, b))), reverse=True); return f'{(la + .05) / (lb + .05):.2f}'

def uri(p): return 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
APPS = [('expediente', 'Expediente'), ('agenda', 'Agenda'), ('compras', 'Compras'), ('farmacia', 'Farmacia'),
        ('impulsa', 'Impulsa'), ('grupos', 'Grupos'), ('administracion', 'Administración')]
SELLOS = {k: uri(f'final/svg/{k}.svg') for k, _ in APPS}

# Lucide (trazo 2, retícula 24)
L = {'check': '<path d="M20 6 9 17l-5-5"/>', 'chev': '<path d="m6 9 6 6 6-6"/>', 'search': '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
     'x': '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>', 'alert': '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
     'plus': '<path d="M5 12h14"/><path d="M12 5v14"/>', 'cal': '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
     'trash': '<path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>',
     'print': '<path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>',
     'more': '<circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/>',
     'load': '<path d="M21 12a9 9 0 1 1-6.219-8.56"/>', 'info': '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
     'minus': '<path d="M5 12h14"/>', 'lock': '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>'}
def ic(n, cls='ico'): return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{L[n]}</svg>'

# ---------- botones ----------
ESTADOS = [('', 'Reposo'), ('h', 'Hover'), ('p', 'Presionado'), ('f', 'Foco'), ('l', 'Cargando'), ('d', 'Deshabilitado')]
VARS = [('b1', 'Principal', 'Guardar receta', None), ('b2', 'Secundario', 'Vista previa', None), ('b3', 'Terciario', 'Cancelar', None),
        ('b4', 'Destructivo', 'Eliminar receta', 'trash'), ('b5', 'Destructivo · confirmación', 'Sí, eliminar', None)]
def boton(v, txt, est, icon=None, size=''):
    cl = f'btn {v} {size} {est}'.split()
    attrs = ''
    if est == 'd': attrs = ' aria-disabled="true"'
    if est == 'l': attrs = ' aria-busy="true"'
    inner = (ic('load', 'ico gira') + f'<span>{txt}</span>') if est == 'l' else ((ic(icon) if icon else '') + f'<span>{txt}</span>')
    return f'<button type="button" class="{" ".join(cl)}"{attrs} tabindex="-1">{inner}</button>'
btab = '<tr><th scope="col">Variante</th>' + ''.join(f'<th scope="col">{n}</th>' for _, n in ESTADOS) + '</tr>'
for v, n, t, i in VARS:
    btab += f'<tr><th scope="row">{n}</th>' + ''.join(f'<td>{boton(v, t, e, i)}</td>' for e, _ in ESTADOS) + '</tr>'
AD = ' aria-disabled="true"'
icbtn = ''.join(f'<td><button type="button" class="ibtn {e}" aria-label="Imprimir"{AD if e == "d" else ""} tabindex="-1">{ic("load", "ico gira") if e == "l" else ic("print")}</button></td>' for e, _ in ESTADOS)
btab += f'<tr><th scope="row">Solo icono</th>{icbtn}</tr>'

# ---------- campos ----------
def campo(lbl, ctl, ayuda='', err='', opc=False, fid=''):
    o = ' <span class="opc">(opcional)</span>' if opc else ''
    a = f'<span class="ayuda" id="{fid}-a">{ayuda}</span>' if ayuda else ''
    e = f'<span class="err" id="{fid}-e">{ic("alert")}{err}</span>' if err else ''
    return f'<div class="campo"><label for="{fid}">{lbl}{o}</label>{ctl}{e}{a}</div>'
def inp(fid, val='', est='', ph='', unit='', tipo='text', extra=''):
    desc = []
    if est == 'e': desc.append(f'{fid}-e')
    att = f' id="{fid}" type="{tipo}" value="{val}" placeholder="{ph}"'
    if est == 'e': att += ' aria-invalid="true"'
    if est == 'ro': att += ' readonly'
    if est == 'd': att += ' disabled'
    if desc: att += f' aria-describedby="{" ".join(desc)}"'
    cls = f'in {est}'.strip()
    if unit: return f'<span class="in-u {est}"><input class="num"{att}{extra} inputmode="decimal"><span class="u" aria-hidden="true">{unit}</span></span>'
    return f'<input class="{cls}"{att}{extra}>'
CEST = [('', 'Reposo'), ('h', 'Hover'), ('f', 'Foco'), ('e', 'Error'), ('ro', 'Solo lectura'), ('d', 'Deshabilitado')]
ctab = '<tr><th scope="col">Estado</th><th scope="col">Texto</th><th scope="col">Número con unidad</th><th scope="col">Lista</th></tr>'
for e, n in CEST:
    val = '' if e in ('',) else 'Mariana Ruiz'
    num = '' if e == '' else ('140' if e == 'e' else '72.5')
    msg = 'Escribe el nombre como en la identificación' if e == 'e' else ''
    nmsg = 'Máximo 100 mg al día' if e == 'e' else ''
    sel_att = ' disabled' if e == 'd' else ''
    SELERR = f' aria-invalid="true" aria-describedby="s-{e or "r"}-e"'
    sel = f'<span class="sel {e}"><select id="s-{e or "r"}"{sel_att}{SELERR if e == "e" else ""}><option>{"Elige una vía" if e == "" else "Oral"}</option><option>Oral</option><option>Intravenosa</option></select>{ic("chev", "ico chev")}</span>'
    if e == 'ro': sel = f'<span class="sel ro"><input class="in ro" id="s-ro" value="Oral" readonly></span>'
    ctab += (f'<tr><th scope="row">{n}</th><td>{campo("Nombre del paciente", inp("t-" + (e or "r"), val, e, "Nombre y apellidos"), err=msg, fid="t-" + (e or "r"))}</td>'
             f'<td>{campo("Dosis diaria", inp("n-" + (e or "r"), num, e, "", "mg"), err=nmsg, fid="n-" + (e or "r"))}</td>'
             f'<td>{campo("Vía", sel, err="Elige la vía de administración" if e == "e" else "", fid="s-" + (e or "r"))}</td></tr>')

# ---------- selección ----------
def chk(lbl, est='', tipo='checkbox', checked=False, ind=False, name='g'):
    a = (' checked' if checked else '') + (' disabled' if est == 'd' else '') + (' aria-invalid="true"' if est == 'e' else '')
    if ind: a += ' data-ind="1"'
    return f'<label class="op {est}"><input type="{tipo}" name="{name}"{a}><span class="caja {"radio" if tipo == "radio" else ""}">{ic("check", "ico c")}{ic("minus", "ico m")}</span><span>{lbl}</span></label>'
def sw(lbl, on=False, est=''):
    d = ' disabled' if est == 'd' else ''
    return f'<div class="sw-f {est}"><span class="sw-l" id="swl-{lbl[:4]}{est}{on}">{lbl}</span><button type="button" role="switch" class="sw" aria-checked="{"true" if on else "false"}" aria-labelledby="swl-{lbl[:4]}{est}{on}"{d}><span class="th"></span></button><span class="sw-t" aria-hidden="true">{"Activado" if on else "Desactivado"}</span></div>'
def seg(opts, sel=0, lbl='Vista', idn='seg'):
    return f'<div class="seg" role="radiogroup" aria-label="{lbl}">' + ''.join(f'<button type="button" role="radio" aria-checked="{"true" if i == sel else "false"}" tabindex="{0 if i == sel else -1}">{o}</button>' for i, o in enumerate(opts)) + '</div>'
def chip(t, on=False, d=False):
    return f'<button type="button" class="chip" aria-pressed="{"true" if on else "false"}"{" disabled" if d else ""}>{ic("check", "ico ck")}<span>{t}</span></button>'

sel_html = f'''<div class="grid3">
 <div class="lam"><h4>Casilla</h4><p class="nota">Varias opciones a la vez, o una sola que se confirma con «Guardar».</p>
  <fieldset><legend>Antecedentes</legend>{chk("Diabetes", checked=True)}{chk("Hipertensión")}{chk("Seleccionar todo", ind=True)}{chk("Alergias registradas", "e")}<span class="err">{ic("alert")}Confirma si hay alergias</span>{chk("Cirugías previas", "d")}</fieldset></div>
 <div class="lam"><h4>Opción única</h4><p class="nota">Una sola opción de 2 a 5 visibles; con más, lista.</p>
  <fieldset><legend>Tipo de consulta</legend>{chk("Primera vez", tipo="radio", checked=True, name="tc")}{chk("Seguimiento", tipo="radio", name="tc")}{chk("Urgencia", "d", "radio", name="tc")}</fieldset></div>
 <div class="lam"><h4>Interruptor</h4><p class="nota">Solo para ajustes que se aplican al momento, sin «Guardar».</p>
  {sw("Recordatorio por mensaje", True)}{sw("Mostrar en el directorio")}{sw("Firma electrónica", True, "d")}</div>
 <div class="lam"><h4>Control segmentado</h4><p class="nota">Cambia la vista de lo mismo; de 2 a 4 opciones cortas.</p>
  {seg(["Día", "Semana", "Mes"], 1, "Vista de la agenda")}{seg(["Lista", "Tarjetas"], 0, "Vista de recetas")}</div>
 <div class="lam"><h4>Chip de filtro</h4><p class="nota">Filtra una lista; se pueden combinar.</p>
  <div class="fila" role="group" aria-label="Filtrar citas">{chip("Hoy", True)}{chip("Primera vez")}{chip("Por confirmar", True)}{chip("Canceladas", d=True)}</div></div>
 <div class="lam"><h4>Buscador y área de texto</h4>
  <div class="campo"><label for="bq">Buscar paciente</label><span class="bus">{ic("search")}<input id="bq" class="in" type="search" placeholder="Nombre, folio o teléfono" value="Ruiz"><button type="button" class="ibtn s" aria-label="Borrar búsqueda">{ic("x")}</button></span></div>
  <div class="campo"><label for="ta">Indicaciones <span class="opc">(opcional)</span></label><textarea id="ta" class="in" rows="3" placeholder="Tomar con alimentos"></textarea><span class="ayuda">Se imprimen en la receta.</span></div></div>
</div>'''

# ---------- ejemplo integrado ----------
app_seg = '<div class="seg apps" role="radiogroup" aria-label="App de ejemplo">' + ''.join(f'<button type="button" role="radio" data-app="{k}" data-n="{n}" aria-checked="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{n}</button>' for i, (k, n) in enumerate(APPS)) + '</div>'
sellos_js = json.dumps(SELLOS)
ejemplo = f'''<div class="demo">
 <div class="appbar"><img id="sello" src="{SELLOS["expediente"]}" alt="" width="32" height="32"><span class="appn"><b id="appn">Expediente</b> Manik</span><span class="sp"></span><button type="button" class="ibtn" aria-label="Más acciones">{ic("more")}</button></div>
 <form class="hoja" novalidate>
  <div class="hcab"><div><h3>Nueva receta</h3><p class="nota">Mariana Ruiz · 34 años</p></div>{seg(["Medicamento", "Estudio"], 0, "Tipo de indicación")}</div>
  <div class="grid2">
   {campo("Medicamento", inp("x-med", "Losartán", "", "Busca por nombre o sustancia"), fid="x-med")}
   {campo("Dosis diaria", inp("x-dos", "", "", "", "mg"), ayuda="Escribe más de 100 para ver el error.", fid="x-dos")}
   {campo("Vía", '<span class="sel"><select id="x-via"><option>Oral</option><option>Intravenosa</option><option>Tópica</option></select>' + ic("chev", "ico chev") + '</span>', fid="x-via")}
   {campo("Inicio", inp("x-ini", "2026-11-05", "", "", tipo="date"), fid="x-ini")}
  </div>
  {sw("Enviar recordatorio al paciente", True)}
  <div class="acc"><button type="button" class="btn b4">{ic("trash")}<span>Descartar</span></button><span class="sp"></span><button type="button" class="btn b3">Cancelar</button><button type="button" class="btn b2">Vista previa</button><button type="submit" class="btn b1" id="x-ok"><span>Guardar receta</span></button></div>
 </form>
 <p class="nota">Cambia de app: solo cambian el sello y el nombre. Botones, campos y controles son los mismos en las siete.</p>
</div>'''

def fila_dec(t, v, por): return f'<tr><td>{t}</td><td>{v}</td><td>{por}</td></tr>'
dec = ''.join([
    fila_dec('Tamaños', '<b>Estándar 44 px</b> (todo) y <b>compacto 36 px</b> solo en filas de tabla y barras de filtros', 'Un solo alto en formularios; el compacto ahorra alto en listas densas y sigue arriba de 24 px (WCAG 2.5.8).'),
    fila_dec('Deshabilitado', f'Fondo <span class="mono">surface-soft</span>, borde <span class="mono">line</span>, texto <span class="mono">muted</span> ({cr("muted", "surface-soft")}:1), sin color de acción', 'Sin color = no se puede tocar. Se lee igual (no se aclara el texto) y se dice por qué cerca del control.'),
    fila_dec('Hover y presionado', '<span class="mono">manik-hover</span> en el principal; <span class="mono">surface-soft</span> y <span class="mono">surface-pressed</span> en los demás; <span class="mono">error-soft</span> en el destructivo', 'Usa tokens que ya existían; ningún color nuevo.'),
    fila_dec('Cargando', 'Icono girando a la izquierda, mismo ancho, <span class="mono">aria-busy</span>', 'El botón no salta ni se puede pulsar dos veces.'),
    fila_dec('Destructivo', 'Contorno rojo para iniciar; sólido rojo solo en el diálogo que confirma', f'Blanco sobre <span class="mono">error</span>: {cr("#FFFFFF", "error")}:1. El rojo sólido aparece una sola vez, cuando ya se decidió.'),
    fila_dec('Campo opcional', 'Se marca «(opcional)»; lo obligatorio no lleva marca', 'En formularios clínicos casi todo es obligatorio: marcar la excepción es menos ruido que un asterisco en cada campo.'),
    fila_dec('Hover de campo', f'Borde <span class="mono">muted</span> ({cr("muted", "surface")}:1)', 'Confirma que el campo responde sin cambiar su tamaño.'),
    fila_dec('Casilla, opción, interruptor', f'20 px dentro de una fila de 44 px; borde <span class="mono">line-control</span> 1.5 px; marcado en <span class="mono">manik</span>', 'Toda la fila es tocable; el mismo azul de acción en todo control.'),
])

HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Controles Ecosistema Manik</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{{ROOT};--font-display:{FAM["display"]};--font-sans:{FAM["sans"]};--compacto:36px;color-scheme:light}}
*{{box-sizing:border-box}}[hidden]{{display:none!important}}
body{{margin:0;background:var(--canvas);color:var(--ink);font:400 16px/24px var(--font-sans);padding:0 16px}}
h1,h2,h3,h4{{font-family:var(--font-display);margin:0;font-weight:600;color:var(--ink)}}h1{{font-size:32px;line-height:38px;letter-spacing:-.01em}}h2{{font-size:24px;line-height:32px}}h3{{font-size:18px;line-height:26px}}h4{{font-size:16px;line-height:24px}}p{{margin:0}}
.wrap{{max-width:1240px;margin:0 auto;padding:32px 0 80px;display:grid;gap:48px}}
.nota{{font-size:14px;line-height:20px;color:var(--muted)}}.mono{{font-family:ui-monospace,Menlo,monospace;font-size:13px;background:var(--surface-soft);border-radius:6px;padding:1px 5px}}
.eti{{font:600 13px/18px var(--font-sans);color:var(--muted);letter-spacing:.04em;text-transform:uppercase}}
.cab{{display:grid;gap:8px;max-width:76ch}}
section{{display:grid;gap:18px}}
.lam{{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-2xl);padding:20px;display:grid;gap:14px;align-content:start;min-width:0}}
.tw{{overflow-x:auto;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-2xl)}}
table{{border-collapse:collapse;width:100%}}th,td{{text-align:left;vertical-align:middle;padding:12px 14px;border-bottom:1px solid var(--line)}}
thead th,tr:first-child th[scope=col]{{font:600 14px/20px var(--font-sans);color:var(--muted);background:var(--surface-soft);white-space:nowrap}}
th[scope=row]{{font:600 14px/20px var(--font-sans);white-space:nowrap}}tr:last-child>*{{border-bottom:0}}
.ctab td{{min-width:230px;vertical-align:top}}
.grid3{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:16px}}.grid2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:16px}}
.fila{{display:flex;flex-wrap:wrap;gap:8px;align-items:center}}.sp{{flex:1}}
.ico{{width:18px;height:18px;flex:none}}.gira{{animation:gira .8s linear infinite}}@keyframes gira{{to{{transform:rotate(360deg)}}}}
@media (prefers-reduced-motion:reduce){{.gira{{animation:none}}}}
:focus-visible{{outline:2px solid var(--focus);outline-offset:2px}}

/* ===== botones ===== */
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:var(--control-height);padding:0 18px;border-radius:var(--radius-md);border:1px solid transparent;font:600 15px/20px var(--font-sans);cursor:pointer;white-space:nowrap;transition:background-color .12s,border-color .12s}}
.btn.c{{min-height:var(--compacto);padding:0 14px;font-size:14px}}
.btn.f{{outline:2px solid var(--focus);outline-offset:2px}}
.b1{{background:var(--manik);color:var(--on-manik)}}.b1:hover,.b1.h{{background:var(--manik-hover)}}.b1:active,.b1.p{{background:var(--manik-hover);box-shadow:inset 0 2px 0 rgba(0,0,0,.18)}}
.b2{{background:var(--surface);color:var(--manik);border-color:var(--line-control)}}.b2:hover,.b2.h{{background:var(--surface-soft)}}.b2:active,.b2.p{{background:var(--surface-pressed)}}
.b3{{background:transparent;color:var(--manik)}}.b3:hover,.b3.h{{background:var(--surface-soft)}}.b3:active,.b3.p{{background:var(--surface-pressed)}}
.b4{{background:var(--surface);color:var(--error);border-color:var(--error)}}.b4:hover,.b4.h{{background:var(--error-soft);color:var(--on-error-soft)}}.b4:active,.b4.p{{background:var(--error-soft);box-shadow:inset 0 2px 0 rgba(0,0,0,.08)}}
.b5{{background:var(--error);color:#fff}}.b5:hover,.b5.h{{background:var(--on-error-soft)}}.b5:active,.b5.p{{background:var(--on-error-soft);box-shadow:inset 0 2px 0 rgba(0,0,0,.18)}}
.btn.l{{cursor:progress}}
.btn.d,.btn[aria-disabled=true],.ibtn.d,.ibtn[aria-disabled=true]{{background:var(--surface-soft)!important;color:var(--muted)!important;border-color:var(--line)!important;box-shadow:none!important;cursor:not-allowed}}
.b3.d,.b3[aria-disabled=true]{{background:transparent!important;border-color:transparent!important}}
.ibtn{{width:var(--control-height);height:var(--control-height);display:inline-grid;place-items:center;border-radius:var(--radius-md);border:1px solid transparent;background:transparent;color:var(--muted);cursor:pointer}}
.ibtn:hover,.ibtn.h{{background:var(--surface-soft);color:var(--ink)}}.ibtn:active,.ibtn.p{{background:var(--surface-pressed)}}.ibtn.f{{outline:2px solid var(--focus);outline-offset:2px}}
.ibtn.s{{width:36px;height:36px}}
.btab td{{min-width:120px}}

/* ===== campos ===== */
.campo{{display:grid;gap:6px;align-content:start;min-width:0}}
label,legend{{font:600 14px/20px var(--font-sans);color:var(--ink)}}.opc{{font-weight:400;color:var(--muted)}}
.ayuda{{font-size:14px;line-height:20px;color:var(--muted)}}
.err{{display:flex;gap:6px;align-items:flex-start;font-size:14px;line-height:20px;color:var(--error)}}.err .ico{{width:16px;height:16px;margin-top:2px}}
.in,.in-u,.sel select{{width:100%;min-height:var(--control-height);border:1px solid var(--line-control);border-radius:var(--radius-md);background:var(--surface);color:var(--ink);font:400 16px/22px var(--font-sans);padding:0 14px}}
textarea.in{{padding:10px 14px;min-height:96px;resize:vertical}}
.in::placeholder,.in-u input::placeholder{{color:var(--muted)}}
.in:hover,.in.h,.in-u:hover,.in-u.h,.sel select:hover,.sel.h select{{border-color:var(--muted)}}
.in:focus,.in.f,.in-u:focus-within,.in-u.f,.sel select:focus,.sel.f select{{outline:2px solid var(--focus);outline-offset:2px;border-color:var(--manik)}}
.in.e,.in[aria-invalid=true],.in-u.e,.sel.e select{{border:2px solid var(--error);padding:0 13px}}
.in.ro,.in[readonly],.in-u.ro{{background:var(--surface-soft);border-color:var(--line)}}
.in:disabled,.in.d,.in-u.d,.sel select:disabled{{opacity:1;-webkit-text-fill-color:var(--muted);background:var(--surface-soft);border-color:var(--line);color:var(--muted);cursor:not-allowed}}
.in-u{{display:flex;align-items:center;gap:8px;padding:0 14px 0 0}}.in-u input{{flex:1;min-width:0;border:0;background:transparent;font:inherit;color:inherit;height:40px;padding:0 0 0 14px;text-align:right;font-variant-numeric:tabular-nums;outline:none}}
.in-u .u{{color:var(--muted);font-size:15px}}.in-u.e{{padding-right:13px}}
.sel{{position:relative;display:block}}.sel select{{appearance:none;padding-right:42px;cursor:pointer}}.sel .chev{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--muted);pointer-events:none}}
.sel.ro .in{{cursor:default}}
.bus{{position:relative;display:block}}.bus>.ico{{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--muted)}}.bus .in{{padding-left:42px;padding-right:44px}}.bus .ibtn{{position:absolute;right:4px;top:50%;transform:translateY(-50%)}}
input[type=search]::-webkit-search-cancel-button{{display:none}}

/* ===== selección ===== */
fieldset{{border:0;margin:0;padding:0;display:grid;gap:2px}}legend{{padding:0;margin-bottom:6px}}
.op{{display:flex;align-items:center;gap:12px;min-height:var(--control-height);cursor:pointer;font:400 16px/22px var(--font-sans);font-weight:400}}
.op input{{position:absolute;opacity:0;width:1px;height:1px}}
.caja{{width:20px;height:20px;flex:none;border:1.5px solid var(--line-control);border-radius:6px;background:var(--surface);display:grid;place-items:center;color:var(--on-manik)}}
.caja.radio{{border-radius:50%}}.caja .ico{{width:14px;height:14px;display:none}}.caja.radio .ico{{display:none!important}}
.op:hover .caja{{border-color:var(--muted)}}
.op input:checked+.caja{{background:var(--manik);border-color:var(--manik)}}.op input:checked+.caja .c{{display:block}}
.op input[data-ind]+.caja{{background:var(--manik);border-color:var(--manik)}}.op input[data-ind]+.caja .m{{display:block}}
.op input:checked+.caja.radio{{background:var(--surface);box-shadow:inset 0 0 0 4px var(--surface),inset 0 0 0 10px var(--manik)}}
.op input:focus-visible+.caja{{outline:2px solid var(--focus);outline-offset:2px}}
.op.e .caja{{border:2px solid var(--error)}}
.op.d{{color:var(--muted);cursor:not-allowed}}.op.d .caja{{background:var(--surface-soft);border-color:var(--line)}}
.sw-f{{display:flex;align-items:center;gap:12px;min-height:var(--control-height)}}.sw-l{{flex:1}}.sw-t{{font-size:14px;color:var(--muted);min-width:96px}}
.sw{{width:44px;height:26px;border-radius:999px;border:0;padding:0;background:var(--line-control);position:relative;cursor:pointer;flex:none;transition:background-color .15s}}
.sw .th{{position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:var(--surface);box-shadow:0 1px 2px rgba(20,33,61,.3);transition:transform .15s}}
.sw[aria-checked=true]{{background:var(--manik)}}.sw[aria-checked=true] .th{{transform:translateX(18px)}}
.sw:disabled{{background:var(--line);cursor:not-allowed}}.sw:disabled .th{{box-shadow:none}}.sw-f.d{{color:var(--muted)}}
@media (prefers-reduced-motion:reduce){{.sw,.sw .th,.btn{{transition:none}}}}
.seg{{justify-self:start;display:inline-flex;gap:2px;padding:3px;background:var(--surface-soft);border:1px solid var(--line);border-radius:var(--radius-md);max-width:100%;overflow-x:auto}}
.seg button{{min-height:36px;padding:0 14px;border:0;border-radius:11px;background:transparent;color:var(--muted);font:600 14px/20px var(--font-sans);cursor:pointer;white-space:nowrap}}
.seg button:hover{{color:var(--ink)}}.seg button[aria-checked=true]{{background:var(--surface);color:var(--manik);box-shadow:var(--shadow-card)}}
.chip{{display:inline-flex;align-items:center;gap:6px;min-height:var(--compacto);padding:0 14px;border-radius:999px;border:1px solid var(--line-control);background:var(--surface);color:var(--ink);font:600 14px/20px var(--font-sans);cursor:pointer}}
.chip .ck{{display:none;width:16px;height:16px}}.chip:hover{{background:var(--surface-soft)}}
.chip[aria-pressed=true]{{background:var(--manik-soft);border-color:var(--manik);color:var(--manik)}}.chip[aria-pressed=true] .ck{{display:block}}
.chip:disabled{{background:var(--surface-soft);border-color:var(--line);color:var(--muted);cursor:not-allowed}}

/* ===== ejemplo ===== */
.demo{{display:grid;gap:12px}}.appbar{{display:flex;align-items:center;gap:10px;height:var(--header-height);padding:0 16px;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-2xl) var(--radius-2xl) 0 0}}
.appn{{font:400 16px/24px var(--font-display)}}.appn b{{font-weight:600}}
.hoja{{background:var(--surface);border:1px solid var(--line);border-top:0;border-radius:0 0 var(--radius-2xl) var(--radius-2xl);padding:24px;display:grid;gap:20px;margin-top:-12px}}
.hcab{{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between}}
.acc{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;border-top:1px solid var(--line);padding-top:18px}}
.apps{{flex-wrap:nowrap}}
.dec td{{vertical-align:top;font-size:15px;line-height:22px}}.dec td:first-child{{font-weight:600;white-space:nowrap}}
.dec td:nth-child(3){{color:var(--muted)}}
@media (max-width:640px){{.acc .sp{{display:none}}.acc .btn{{flex:1 1 auto}}h1{{font-size:26px;line-height:32px}}}}
</style></head><body><main class="wrap">
<header class="cab"><span class="eti">Ecosistema Manik · ronda 1 · propuesta</span><h1>Botones, campos y controles</h1>
<p>Una sola familia para las siete apps. El color de producto vive en el sello; todo lo que se toca usa el azul Manik, el mismo alto, el mismo radio y el mismo foco. Así quien pasa de Agenda a Farmacia no reaprende nada.</p>
<p class="nota">Valores leídos de los tokens del sistema de diseño del Ecosistema. Las decisiones nuevas están marcadas como propuesta al final.</p></header>

<section aria-labelledby="s0"><h2 id="s0">En una app real</h2>{app_seg}{ejemplo}</section>

<section aria-labelledby="s1"><h2 id="s1">Botones</h2>
<p class="nota">Una acción principal por vista. El destructivo empieza en contorno; el rojo sólido solo confirma. Las muestras de estado están fijas (no se enfocan); el ejemplo de arriba es interactivo.</p>
<div class="tw" tabindex="0" role="region" aria-label="Botones por estado"><table class="btab">{btab}</table></div>
<div class="lam"><h4>Compacto · 36 px</h4><p class="nota">Solo en filas de tabla y barras de filtros. En formularios, siempre 44 px.</p>
<div class="fila"><button type="button" class="btn b1 c">{ic("plus")}<span>Agregar</span></button><button type="button" class="btn b2 c">Exportar</button><button type="button" class="btn b3 c">Ver todo</button><button type="button" class="ibtn s" aria-label="Más acciones">{ic("more")}</button></div></div></section>

<section aria-labelledby="s2"><h2 id="s2">Campos</h2>
<p class="nota">Etiqueta arriba, siempre visible; ayuda abajo; el error reemplaza su lugar con icono y un mensaje que dice qué hacer. La unidad la pone el sistema.</p>
<div class="tw" tabindex="0" role="region" aria-label="Campos por estado"><table class="ctab">{ctab}</table></div></section>

<section aria-labelledby="s3"><h2 id="s3">Controles de selección</h2>{sel_html}</section>

<section aria-labelledby="s4"><h2 id="s4">Decisiones de esta ronda</h2>
<div class="tw" tabindex="0" role="region" aria-label="Decisiones"><table class="dec"><thead><tr><th scope="col">Tema</th><th scope="col">Propuesta</th><th scope="col">Por qué</th></tr></thead><tbody>{dec}</tbody></table></div>
<p class="nota">Ya vigentes y sin cambio: alto 44 px, radio {V["radius-md"]}, foco de 2 px en <span class="mono">manik</span> con 2 px de separación, borde de control <span class="mono">line-control</span> ({cr("line-control", "surface")}:1), error con borde de 2 px, icono y mensaje, unidad fija como sufijo.</p></section>
</main>
<script>
const S={sellos_js};
document.querySelectorAll('[role=radiogroup]').forEach(g=>{{const bs=[...g.querySelectorAll('[role=radio]')];
 const pick=b=>{{bs.forEach(x=>{{x.setAttribute('aria-checked',x===b);x.tabIndex=x===b?0:-1}});if(b.dataset.app){{document.getElementById('sello').src=S[b.dataset.app];document.getElementById('appn').textContent=b.dataset.n}}}};
 bs.forEach((b,i)=>{{b.addEventListener('click',()=>pick(b));b.addEventListener('keydown',e=>{{const d={{ArrowRight:1,ArrowDown:1,ArrowLeft:-1,ArrowUp:-1}}[e.key];if(d){{e.preventDefault();const n=bs[(i+d+bs.length)%bs.length];pick(n);n.focus()}}}})}})}});
document.querySelectorAll('.sw:not([disabled])').forEach(s=>s.addEventListener('click',()=>{{const on=s.getAttribute('aria-checked')!=='true';s.setAttribute('aria-checked',on);const t=s.parentElement.querySelector('.sw-t');if(t)t.textContent=on?'Activado':'Desactivado'}}));
document.querySelectorAll('.chip:not([disabled])').forEach(c=>c.addEventListener('click',()=>c.setAttribute('aria-pressed',c.getAttribute('aria-pressed')!=='true')));
document.querySelectorAll('input[data-ind]').forEach(i=>{{i.indeterminate=true;i.addEventListener('change',()=>i.removeAttribute('data-ind'))}});
const dos=document.getElementById('x-dos'),cont=dos.closest('.in-u'),cmp=dos.closest('.campo');
dos.addEventListener('input',()=>{{const v=parseFloat(dos.value),bad=v>100;cont.classList.toggle('e',bad);if(bad)dos.setAttribute('aria-invalid','true');else dos.removeAttribute('aria-invalid');
 let m=cmp.querySelector('.err');if(bad&&!m){{m=document.createElement('span');m.className='err';m.id='x-dos-e';m.innerHTML={json.dumps(ic("alert"))}+'Máximo 100 mg al día';cmp.querySelector('.ayuda').before(m);dos.setAttribute('aria-describedby','x-dos-e x-dos-a')}}
 if(!bad&&m){{m.remove();dos.setAttribute('aria-describedby','x-dos-a')}}}});
dos.setAttribute('aria-describedby','x-dos-a');
document.querySelector('.demo form').addEventListener('submit',e=>{{e.preventDefault();const b=document.getElementById('x-ok');if(b.getAttribute('aria-busy'))return;
 b.setAttribute('aria-busy','true');b.classList.add('l');b.innerHTML={json.dumps(ic("load", "ico gira"))}+'<span>Guardar receta</span>';
 setTimeout(()=>{{b.removeAttribute('aria-busy');b.classList.remove('l');b.innerHTML={json.dumps(ic("check"))}+'<span>Guardada</span>'}},1200)}});
</script></body></html>'''
if __name__ == '__main__':  # importable sin reescribir la ronda evaluada
    open(os.path.join(D, 'controles.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
