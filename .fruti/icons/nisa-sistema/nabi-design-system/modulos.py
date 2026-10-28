# Nabi DS · identidad v2 + manual de módulos (ejemplo: Usuarios).
# Uso: python3 modulos.py <carpeta-project> <iconos.json>
#   Aplica la identidad v2 aprobada (28/10/2026) a tokens.json y escribe la sección modulos.md y los
#   componentes EncabezadoModulo, EstadoUsuario, TablaUsuarios, FormularioUsuario y ModuloUsuarios.
#   Edita sobre la copia leída del design system publicado (no reconstruye: build.py fue la v1).
import json, os, sys
P, ICJ = sys.argv[1], sys.argv[2]
IC = json.load(open(ICJ))
def i(n, cls='i'): return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{IC[n]}</svg>'

# ---------- 1 · tokens v2 ----------
T = json.load(open(f'{P}/tokens.json'))
col = {t['name']: t for t in T['color']['tokens']}
col['bg'].update(value='#F2F4F8', usage='Fondo de página, «papel de laboratorio». Las superficies blancas se separan de él: nunca blanco sobre blanco. Texto encima: «text» 15.5:1, «text-muted» 6.2:1. Los campos no van directo sobre «bg» (su borde baja a 3.0:1): van sobre «surface».')
col['surface'].update(usage='Tarjetas, tablas, paneles y campos: lo que se trabaja. Con «border» y «shadow-1» en reposo.')
col['surface-sunken'].update(value='#EEF1F6', usage='Encabezados de tabla, campos de solo lectura, estado neutro. «text-muted» encima 6.0:1; «text-subtle» 4.7:1.')
col['border'].update(value='#DFE3EC', usage='Filete de 1 px entre filas y alrededor de tarjetas. Decorativo: la separación la hace junto con la sombra.')
col['text-subtle'].update(usage='Placeholders. 5.3:1 sobre «surface», 4.7:1 sobre «surface-sunken».')
col['border-control'].update(usage='Bordes de campos y casillas: 3.3:1 sobre «surface». Los campos van sobre «surface».')
new = []
for t in T['color']['tokens']:
    new.append(t)
    if t['name'] == 'border':
        new.append({'name': 'border-strong', 'value': '#CDD3DF', 'usage': 'Contorno de pocillos vacíos y divisores que deben verse sobre «surface-sunken».'})
    if t['name'] == 'surface-sunken':
        new.append({'name': 'surface-hover', 'value': '#F5F7FB', 'usage': 'Hover de filas, opciones de menú y elementos de lista: un paso de tinta, no un color. «text-muted» encima 6.3:1.'})
T['color']['tokens'] = new
T['type']['families']['editorial'] = '"Newsreader", Georgia, "Times New Roman", serif'
if not any(g['name'] == 'Editorial' for g in T['type']['groups']):
    T['type']['groups'].append({'name': 'Editorial', 'family': 'editorial',
      'note': 'Newsreader itálica. La tercera voz: solo frases que se leen, no datos ni controles. Entradillas de módulo, lemas, estados vacíos y portadas de documento. Google Fonts: Newsreader:ital,opsz,wght@1,6..72,400;1,6..72,500.',
      'styles': [
        {'name': 'entradilla', 'fontSize': '17px', 'lineHeight': '24px', 'fontWeight': 400, 'fontStyle': 'italic', 'sample': 'Quién entra a Nabi y qué puede hacer.', 'usage': 'Una línea bajo el título del módulo, en «text-muted». Opcional.'},
        {'name': 'lema', 'fontSize': '22px', 'lineHeight': '31px', 'fontWeight': 400, 'fontStyle': 'italic', 'sample': 'Cada muestra, en su lugar.', 'usage': 'Inicio de sesión, portadas y estados vacíos amplios.'}]})
T['shadow'] = {'tokens': [
  {'name': 'shadow-1', 'value': '0 1px 0 rgba(20, 27, 51, 0.03), 0 1px 2px rgba(20, 27, 51, 0.06)', 'usage': 'Tarjetas, tablas y botones secundarios en reposo. Teñida de tinta azul, no negra.'},
  {'name': 'shadow-2', 'value': '0 1px 2px rgba(20, 27, 51, 0.05), 0 10px 28px -14px rgba(5, 42, 118, 0.22)', 'usage': 'La tarjeta que se presenta sola: inicio de sesión, diálogo pequeño, tarjeta protagonista. Una por pantalla.'},
  {'name': 'shadow-overlay', 'value': '0 12px 32px rgba(5, 42, 118, 0.16)', 'usage': 'Lo que flota: menús, paneles laterales, diálogos, barra de acciones en lote.'},
  {'name': 'shadow-inset', 'value': 'inset 0 1px 1px rgba(20, 27, 51, 0.05)', 'usage': 'Campos de texto: se sienten hundidos, no dibujados.'},
  {'name': 'shadow-primary', 'value': 'inset 0 1px 0 rgba(255, 255, 255, 0.16), 0 1px 2px rgba(5, 42, 118, 0.30), 0 6px 14px -6px rgba(5, 42, 118, 0.45)', 'usage': 'Botón primario: brillo arriba y sombra abajo. Sin degradado.'},
  {'name': 'shadow-primary-hover', 'value': 'inset 0 1px 0 rgba(255, 255, 255, 0.18), 0 2px 4px rgba(5, 42, 118, 0.30), 0 10px 20px -8px rgba(5, 42, 118, 0.50)', 'usage': 'Hover del botón primario, junto con 1 px hacia arriba.'}]}
T['version'] = 2
json.dump(T, open(f'{P}/tokens.json', 'w'), ensure_ascii=False, indent=1)

# ---------- 2 · CSS común de los ejemplos de módulo (solo tokens) ----------
HEAD = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
  '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=IBM+Plex+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@1,6..72,400;1,6..72,500&display=swap"><style>')
CSS = r'''
*{box-sizing:border-box}[hidden]{display:none!important}
html,body{margin:0}body{background:var(--bg);color:var(--text);font:15px/22px var(--font-sans);padding:var(--space-6)}
:focus-visible{outline:2px solid var(--focus);outline-offset:2px;border-radius:4px}
.i{width:16px;height:16px;flex:none;stroke:currentColor;fill:none;stroke-width:1.75;stroke-linecap:round;stroke-linejoin:round}
.mono{font-family:var(--font-datos);font-feature-settings:"zero"}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* encabezado de módulo */
.mh{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 24px;align-items:end;padding-bottom:var(--space-5)}
@media (max-width:640px){.mh{grid-template-columns:minmax(0,1fr)}.mh .acts{justify-content:flex-start;flex-wrap:wrap}}
.crumb{grid-column:1/-1;font:500 13px/18px var(--font-sans);color:var(--text-muted);display:flex;gap:6px;align-items:center}
.crumb a{color:var(--text-muted);text-decoration:none}.crumb a:hover{color:var(--primary);text-decoration:underline;text-underline-offset:3px}
.t1{margin:0;font:700 26px/32px var(--font-display);font-stretch:125%;letter-spacing:-.015em;color:var(--text)}
.deck{margin:2px 0 0;font:italic 400 17px/24px var(--font-editorial);color:var(--text-muted)}
.cnt{font:500 13px/18px var(--font-datos);color:var(--text-muted);margin-top:6px}
.cnt b{color:var(--text);font-weight:600}
.acts{display:flex;gap:var(--space-2);align-items:center}
/* botones */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:var(--control-h);padding:0 16px;border-radius:var(--radius-sm);font:600 14px/20px var(--font-sans);border:1px solid transparent;cursor:pointer;white-space:nowrap;transition:transform var(--quick) var(--ease-out),box-shadow var(--quick) ease,background var(--quick) ease}
.btn-p{background:var(--primary);color:var(--on-primary);box-shadow:var(--shadow-primary)}
.btn-p:hover{background:var(--primary-hover);box-shadow:var(--shadow-primary-hover);transform:translateY(-1px)}
.btn-p:active{transform:none;box-shadow:var(--shadow-primary)}
.btn-p:focus-visible{outline-offset:3px}
.btn-s{background:var(--surface);color:var(--primary);border-color:var(--border-control);box-shadow:var(--shadow-1)}
.btn-s:hover{background:var(--surface-hover)}
.btn-g{background:transparent;color:var(--primary)}.btn-g:hover{background:var(--surface-hover)}
.btn-d{background:var(--surface);color:var(--fuera);border-color:var(--fuera)}.btn-d:hover{background:var(--fuera-soft)}
.ib{width:32px;height:32px;display:inline-grid;place-items:center;border:0;border-radius:var(--radius-sm);background:transparent;color:var(--text-muted);cursor:pointer}
.ib:hover{background:var(--surface-hover);color:var(--text)}
/* barra de herramientas */
.tb{display:flex;flex-wrap:wrap;gap:var(--space-2);align-items:center;padding:var(--space-3);border-bottom:1px solid var(--border)}
.fld{display:flex;align-items:center;gap:8px;min-height:var(--control-h);background:var(--surface);border:1px solid var(--border-control);border-radius:var(--radius-md);box-shadow:var(--shadow-inset);padding:0 10px;color:var(--text-muted);transition:border-color var(--quick) ease,box-shadow var(--quick) ease}
.fld:focus-within{border-color:var(--primary);box-shadow:var(--shadow-inset),0 0 0 3px var(--primary-soft)}
.fld input,.fld select{border:0;outline:0;background:none;font:15px/22px var(--font-sans);color:var(--text);min-width:0;width:100%;min-height:38px}
.fld input::placeholder{color:var(--text-subtle)}
.chip{display:inline-flex;align-items:center;gap:6px;min-height:32px;padding:0 10px;border-radius:var(--radius-sm);border:1px solid var(--border);background:var(--surface);font:500 13px/18px var(--font-sans);color:var(--text);cursor:pointer}
.chip:hover{background:var(--surface-hover)}
.chip[aria-pressed="true"]{background:var(--primary-soft);border-color:var(--primary-soft);color:var(--primary)}
.chip .n{font:500 12px var(--font-datos);color:inherit;opacity:.8}
/* tarjeta y tabla */
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-md);box-shadow:var(--shadow-1);overflow:hidden}
.tbl{width:100%;border-collapse:collapse}
.tbl th{background:var(--surface-sunken);font:500 13px/18px var(--font-sans);color:var(--text-muted);text-align:left;padding:9px 12px;border-bottom:1px solid var(--border);white-space:nowrap}
.tbl th button{font:inherit;color:inherit;background:none;border:0;padding:0;display:inline-flex;gap:4px;align-items:center;cursor:pointer}
.tbl th button:hover{color:var(--text)}
.tbl td{padding:8px 12px;border-bottom:1px solid var(--border);vertical-align:middle;height:56px}
.tbl tr:last-child td{border-bottom:0}
.tbl tbody tr{transition:background var(--quick) ease}
.tbl tbody tr:hover td{background:var(--surface-hover)}
.tbl tbody tr[aria-selected="true"] td{background:var(--primary-soft)}
.tbl .ck{width:44px}.tbl .ck input{width:18px;height:18px;accent-color:var(--primary);margin:0}
.who{display:flex;align-items:center;gap:10px;min-width:0}
.av{width:32px;height:32px;border-radius:var(--radius-pill);background:var(--primary-soft);color:var(--primary);display:grid;place-items:center;font:600 12px var(--font-sans);flex:none}
.av.off{background:var(--surface-sunken);color:var(--text-muted)}
.who b{display:flex;align-items:center;gap:6px;font-weight:600}
.who small{display:block;font:400 12px/16px var(--font-datos);color:var(--text-muted);font-feature-settings:"zero"}
.cur{width:8px;height:8px;border-radius:50%;background:var(--pera);box-shadow:0 0 0 2px var(--pera-soft);flex:none}
.dt{font:500 13px/18px var(--font-datos);color:var(--text-muted);font-feature-settings:"zero";white-space:nowrap}
.ra{display:flex;gap:2px;justify-content:flex-end;opacity:0;transition:opacity var(--quick) ease}
.tbl tbody tr:hover .ra,.tbl tbody tr:focus-within .ra,.tbl tbody tr[aria-selected="true"] .ra{opacity:1}
@media (hover:none){.ra{opacity:1}}
.tw{overflow-x:auto;position:relative}.tw .tbl{min-width:860px}
/* estado de usuario */
.est{display:inline-flex;align-items:center;gap:6px;padding:3px 10px 3px 8px;border-radius:var(--radius-sm);font:500 13px/18px var(--font-sans);white-space:nowrap}
.est .i{width:15px;height:15px}
.e-act{background:var(--conforme-soft);color:var(--on-conforme-soft)}
.e-inv{background:var(--pendiente-soft);color:var(--on-pendiente-soft)}
.e-sus{background:var(--alerta-soft);color:var(--on-alerta-soft)}
.e-blo{background:var(--fuera-soft);color:var(--on-fuera-soft)}
.e-baja{background:var(--surface-sunken);color:var(--text-muted)}
/* barra de acciones en lote */
.bulk{display:flex;flex-wrap:wrap;gap:var(--space-2);align-items:center;background:var(--text);color:var(--on-primary);border-radius:var(--radius-md);padding:6px 6px 6px 14px;box-shadow:var(--shadow-overlay);margin:var(--space-3)}
.bulk .n{font:500 13px var(--font-datos);font-feature-settings:"zero";margin-right:auto}
.bulk .btn{min-height:32px;background:transparent;color:var(--on-primary);border-color:rgba(255,255,255,.35)}
.bulk .btn:hover{background:rgba(255,255,255,.08)}
.bulk :focus-visible{outline-color:var(--pera)}
/* pie de tabla */
.tf{display:flex;justify-content:space-between;align-items:center;gap:var(--space-3);padding:10px 12px;border-top:1px solid var(--border);font:500 13px var(--font-datos);color:var(--text-muted);font-feature-settings:"zero"}
/* panel lateral (formulario) */
.panel{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);box-shadow:var(--shadow-overlay);width:min(440px,100%);display:grid;grid-template-rows:auto minmax(0,1fr) auto;max-height:100%}
.ph{display:flex;align-items:flex-start;gap:12px;padding:18px 20px 14px;border-bottom:1px solid var(--border)}
.ph h2{margin:0;font:600 17px/24px var(--font-sans)}
.ph p{margin:2px 0 0;font:400 13px/18px var(--font-sans);color:var(--text-muted)}
.pb{padding:18px 20px;display:grid;align-content:start;gap:var(--space-5);overflow:auto}
.pf{display:flex;flex-wrap:wrap;gap:var(--space-2);justify-content:flex-end;padding:14px 20px;border-top:1px solid var(--border);background:var(--surface)}
.f{display:grid;gap:6px}
.f>label,.f legend{font:500 13px/18px var(--font-sans);color:var(--text)}
.f .req{color:var(--text-muted);font-weight:400}
.f .help{font:400 12px/16px var(--font-sans);color:var(--text-muted)}
.f .err{display:flex;gap:6px;align-items:flex-start;font:500 12px/16px var(--font-sans);color:var(--on-fuera-soft)}
.f .err .i{width:14px;height:14px;margin-top:1px}
.f[data-state="error"] .fld{border-color:var(--fuera);box-shadow:var(--shadow-inset),0 0 0 3px var(--fuera-soft)}
fieldset.f{border:0;margin:0;padding:0}
.opts{display:grid;gap:6px}
.opt{display:grid;grid-template-columns:18px 1fr;gap:2px 10px;align-items:start;padding:10px 12px;border:1px solid var(--border);border-radius:var(--radius-md);cursor:pointer;background:var(--surface);transition:border-color var(--quick) ease,background var(--quick) ease}
.opt:hover{background:var(--surface-hover)}
.opt input{margin:2px 0 0;width:18px;height:18px;accent-color:var(--primary)}
.opt b{font:600 14px/20px var(--font-sans)}
.opt small{grid-column:2;font:400 12px/16px var(--font-sans);color:var(--text-muted)}
.opt:has(input:checked){border-color:var(--primary);background:var(--primary-soft)}
.checks{display:flex;flex-wrap:wrap;gap:6px}
.checks label{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:0 10px;border:1px solid var(--border);border-radius:var(--radius-sm);font:500 13px var(--font-sans);cursor:pointer;background:var(--surface)}
.checks label:has(input:checked){border-color:var(--primary-soft);background:var(--primary-soft);color:var(--primary)}
.checks input{width:16px;height:16px;accent-color:var(--primary);margin:0}
.danger{border-top:1px solid var(--border);padding-top:var(--space-4);display:grid;gap:8px}
.danger p{margin:0;font:400 13px/18px var(--font-sans);color:var(--text-muted)}
/* aviso y vacíos */
.toast{display:flex;align-items:center;gap:12px;background:var(--text);color:var(--on-primary);border-radius:var(--radius-md);padding:8px 8px 8px 14px;box-shadow:var(--shadow-overlay);font:500 14px var(--font-sans)}
.toast .btn{min-height:32px;background:var(--surface);color:var(--text)}
.empty{display:grid;justify-items:center;gap:8px;text-align:center;padding:48px 24px}
.empty .lm{font:italic 400 22px/30px var(--font-editorial);color:var(--text);margin:0}
.empty p{margin:0;color:var(--text-muted);max-width:44ch}
@media (prefers-reduced-motion:reduce){.btn,.tbl tbody tr,.ra,.fld,.opt{transition:none}.btn-p:hover{transform:none}}
'''
def head(): return HEAD + CSS + '</style></head><body>'

USERS = [
 ('MR', 'María Ruiz Téllez', 'm.ruiz@nisanabani.mx', 'Analista', 'Aguas · Alimentos', '2026-10-28 09:41', 'act'),
 ('JO', 'Jorge Orozco', 'j.orozco@nisanabani.mx', 'Supervisor de calidad', 'Todas', '2026-10-28 08:15', 'act'),
 ('LP', 'Lucía Pacheco', 'l.pacheco@nisanabani.mx', 'Recepción', 'Bebidas de agave', '—', 'inv'),
 ('AV', 'Andrés Villalobos', 'a.villalobos@nisanabani.mx', 'Analista', 'Ambiental', '2026-10-21 17:02', 'sus'),
 ('SR', 'Sofía Ramírez', 's.ramirez@nisanabani.mx', 'Analista', 'Farmacia', '2026-10-27 12:30', 'blo'),
 ('EC', 'Ernesto Cano', 'e.cano@nisanabani.mx', 'Administración', 'Todas', '2026-08-02 10:11', 'baja'),
]
EST = {'act': ('e-act', 'circle-check', 'Activo'), 'inv': ('e-inv', 'mail', 'Invitación enviada'), 'sus': ('e-sus', 'circle-pause', 'Suspendido'),
       'blo': ('e-blo', 'lock', 'Bloqueado'), 'baja': ('e-baja', 'ban', 'Dado de baja')}
DSE = ' data-state="error"'
AIT = ' aria-invalid="true"'
def est(k): c, ic, t = EST[k]; return f'<span class="est {c}">{i(ic)}{t}</span>'
def row(u, sel=False, cur=False):
    ini, n, m, rol, div, acc, k = u
    asel = ' aria-selected="true"' if sel else ''
    curm = '<span class=cur title="En edición"></span><span class=vh>en edición</span>' if cur else ''
    return (f'<tr{asel}><td class="ck"><input type="checkbox" aria-label="Seleccionar a {n}"{" checked" if sel else ""}></td>'
            f'<td><div class="who"><span class="av{" off" if k == "baja" else ""}" aria-hidden="true">{ini}</span><span><b>{n}{curm}</b><small>{m}</small></span></div></td>'
            f'<td>{rol}</td><td>{div}</td><td class="dt">{acc}</td><td>{est(k)}</td>'
            f'<td><div class="ra"><button class="ib" aria-label="Editar a {n}">{i("pencil")}</button><button class="ib" aria-label="Más acciones para {n}">{i("ellipsis")}</button></div></td></tr>')
THEAD = ('<thead><tr><th class="ck"><input type="checkbox" aria-label="Seleccionar todos"></th><th><button>Usuario ' + i('arrow-up-down', 'i') + '</button></th>'
         '<th>Rol</th><th>Divisiones</th><th><button>Último acceso ' + i('arrow-up-down') + '</button></th><th>Estado</th><th><span class="vh">Acciones</span></th></tr></thead>')
HEADER = ('<header class="mh"><nav class="crumb" aria-label="Ruta"><a href="#">Administración</a><span aria-hidden="true">/</span><span aria-current="page">Usuarios</span></nav>'
          '<div><h1 class="t1">Usuarios</h1><p class="deck">Quién entra a Nabi y qué puede hacer.</p><p class="cnt"><b>24</b> usuarios · <b>3</b> invitaciones pendientes</p></div>'
          f'<div class="acts"><button class="btn btn-s">{i("download")}Exportar</button><button class="btn btn-p">{i("user-plus")}Agregar usuario</button></div></header>')
TOOLBAR = (f'<div class="tb"><label class="fld" style="flex:1;min-width:220px;max-width:360px">{i("search")}<span class="vh">Buscar usuario</span><input placeholder="Buscar por nombre o correo"></label>'
           '<button class="chip" aria-pressed="false">Rol ' + i('chevron-down') + '</button><button class="chip" aria-pressed="true">Estado: Activo <span class="n">18</span></button><button class="chip" aria-pressed="false">División ' + i('chevron-down') + '</button>'
           '<button class="btn btn-g" style="min-height:32px;margin-left:auto">Limpiar filtros</button></div>')

def comp(name, group, h, body, md, w=None):
    os.makedirs(f'{P}/components/{name}', exist_ok=True)
    mark = f'<!-- @dsCard group="{group}" height={h}' + (f' width={w}' if w else '') + ' -->\n'
    open(f'{P}/components/{name}/preview.html', 'w').write(mark + head() + body + '</body></html>')
    open(f'{P}/components/{name}/README.md', 'w').write(f'# {name}\n\n{md}\n')

comp('EncabezadoModulo', 'Módulos', 190, HEADER,
'''Encabezado de un módulo: dice dónde estás, qué es este módulo, cuántos registros hay y cuál es la acción principal.

- **Ruta** (`label`, «text-muted»): sección › módulo. El último tramo no es enlace.
- **Título** (`title-1` ampliado: Archivo 700 al 125 %, 26/32): el nombre del módulo en plural, sin icono. El icono del módulo vive en el menú lateral; repetirlo junto al título no agrega información.
- **Entradilla** (`entradilla`, Newsreader itálica, «text-muted»): una línea opcional que dice para qué sirve el módulo. Solo en módulos de configuración o de consulta poco frecuente; en módulos de trabajo diario (Recepción, Captura) se omite.
- **Conteo** (`valor-sm`/Plex Mono): totales que importan para decidir («3 invitaciones pendientes»), no todos los totales.
- **Acciones**: a la derecha, alineadas a la base del título. Una sola primaria (`shadow-primary`): «Agregar usuario». Secundarias en `btn-s` (Exportar). Máximo tres visibles; el resto en un menú «Más».
- Sin fondo propio: el encabezado se apoya en «bg»; la tarjeta de la tabla es lo que se eleva.
- El consumidor provee: ruta, título, entradilla (opcional), conteos y acciones.''')

comp('EstadoUsuario', 'Feedback', 96, '<div style="display:flex;flex-wrap:wrap;gap:12px">' + ''.join(est(k) for k in EST) + '</div>',
'''Estado de una cuenta de usuario: icono + texto sobre el fondo suave del estado, con los mismos colores semánticos que los estados de muestra.

| Estado | Color | Icono | Cuándo |
|---|---|---|---|
| Activo | `conforme-soft` / `on-conforme-soft` | círculo con palomita | Puede entrar |
| Invitación enviada | `pendiente-soft` / `on-pendiente-soft` | sobre | Aún no crea su contraseña |
| Suspendido | `alerta-soft` / `on-alerta-soft` | pausa | Acceso detenido por un administrador; reversible |
| Bloqueado | `fuera-soft` / `on-fuera-soft` | candado | Bloqueo por intentos fallidos; se desbloquea solo o por sistemas |
| Dado de baja | `surface-sunken` / `text-muted` | prohibido | Ya no trabaja en el laboratorio; se conserva por trazabilidad |

- El color sigue al significado, no al módulo: verde = está bien, azul = pendiente, naranja = requiere atención, rojo = impedido, gris = fuera de uso.
- Nunca solo color ni solo punto: icono y palabra siempre.
- El pera no es un estado: marca el registro en curso (ver TablaUsuarios).
- Los nombres de estado son una propuesta: confirmar con la política de cuentas del laboratorio.''')

body_tbl = ('<div class="card"><div class="bulk" role="region" aria-label="Acciones para la selección"><span class="n">2 seleccionados</span><button class="btn">Cambiar rol</button><button class="btn">Suspender</button><button class="btn" aria-label="Quitar selección">' + i('x') + '</button></div>'
            '<div class="tw" tabindex="0" role="region" aria-label="Tabla de usuarios"><table class="tbl" aria-label="Usuarios">' + THEAD + '<tbody>' + row(USERS[0], cur=True) + row(USERS[1], sel=True) + row(USERS[2], sel=True) + ''.join(row(u) for u in USERS[3:]) + '</tbody></table></div>'
            '<div class="tf"><span>1–6 de 24</span><span><button class="btn btn-g" style="min-height:32px">Anterior</button><button class="btn btn-g" style="min-height:32px">Siguiente</button></span></div></div>')
comp('TablaUsuarios', 'Data display', 560, body_tbl,
'''Tabla de un módulo de personas o registros: se escanea por nombre, se compara por rol y estado y se actúa por fila o en lote.

- **Contenedor:** `surface` + `border` + `shadow-1`, radio `radius-md`, sobre «bg». Es lo único elevado de la pantalla.
- **Encabezado:** `label` en «text-muted» sobre «surface-sunken». Ordenables con flecha doble y `aria-sort` en la columna activa.
- **Filas de 56 px** cuando hay dos líneas (nombre + correo); 40 px (`row-h`) cuando hay una.
- **Persona:** iniciales en círculo («primary-soft» / «primary»), nombre en Archivo 600, correo en Plex Mono 12 («text-muted»). Foto si existe, del mismo tamaño.
- **Datos que se comparan o copian** (último acceso, folios, fechas) en Plex Mono con cero con barra.
- **Estado:** `EstadoUsuario`, siempre en la misma columna, al final antes de acciones.
- **Interacción:** hover → «surface-hover»; seleccionada → «primary-soft» + casilla marcada; registro en curso (el que está abierto en el panel) → un solo pocillo pera junto al nombre. Acciones por fila (Editar, Más) aparecen al pasar o enfocar la fila y siempre en táctil.
- **Selección múltiple:** aparece la barra de acciones en lote (tinta, `shadow-overlay`) con el conteo en Plex Mono y máximo tres acciones.
- **Pie:** rango en Plex Mono y paginación; más de 50 filas → paginar o virtualizar.
- El consumidor provee: columnas, filas, orden, selección y acciones permitidas por rol.''', w=1100)

def form(edit=False, err=False):
    u = USERS[0]
    return ('<aside class="panel" role="dialog" aria-modal="true" aria-labelledby="pt">'
      f'<div class="ph"><div style="flex:1"><h2 id="pt">{"Editar usuario" if edit else "Agregar usuario"}</h2><p>{"Los cambios se aplican la próxima vez que entre." if edit else "Le enviaremos una invitación para crear su contraseña."}</p></div><button class="ib" aria-label="Cerrar">{i("x")}</button></div>'
      '<div class="pb">'
      f'<div class="f"><label for="fn">Nombre completo</label><label class="fld"><input id="fn" value="{u[1] if edit else "Lucía Pacheco Ortiz"}" autocomplete="off"></label></div>'
      f'<div class="f"{DSE if err else ""}><label for="fm">Correo del laboratorio</label><label class="fld">{i("mail")}<input id="fm" class="mono" style="font-family:var(--font-datos);font-size:14px" value="{u[2] if edit else ("l.pacheco@nisanabani" if err else "l.pacheco@nisanabani.mx")}" aria-describedby="fm-h"{AIT if err else ""}></label>'
      + (f'<span class="err" id="fm-h">{i("circle-alert")}Falta el dominio: debe terminar en @nisanabani.mx.</span>' if err else '<span class="help" id="fm-h">Será su usuario para entrar.</span>') + '</div>'
      '<fieldset class="f"><legend>Rol</legend><div class="opts">'
      + ''.join(f'<label class="opt"><input type="radio" name="rol"{" checked" if r == ("Analista" if edit else "Recepción") else ""}><b>{r}</b><small>{d}</small></label>' for r, d in [
          ('Recepción', 'Registra muestras y entrega certificados.'), ('Analista', 'Captura resultados de sus divisiones.'),
          ('Supervisor de calidad', 'Revisa y libera resultados; emite certificados.'), ('Administración', 'Gestiona usuarios, clientes y catálogos.')])
      + '</div></fieldset>'
      '<fieldset class="f"><legend>Divisiones <span class="req">· al menos una</span></legend><div class="checks">'
      + ''.join(f'<label><input type="checkbox"{" checked" if d in (("Aguas", "Alimentos") if edit else ("Bebidas de agave",)) else ""}>{d}</label>' for d in ['Aguas', 'Agrícolas', 'Ambiental', 'Bebidas', 'Alimentos', 'Farmacia', 'Bebidas de agave', 'Consultoría'])
      + '</div></fieldset>'
      + ('<div class="danger"><b style="font:600 14px var(--font-sans)">Zona de riesgo</b><p>Suspender detiene su acceso hoy; sus resultados y firmas se conservan.</p><div><button class="btn btn-d">Suspender acceso</button></div></div>' if edit else '')
      + '</div>'
      f'<div class="pf"><button class="btn btn-s">Cancelar</button><button class="btn btn-p">{i("send") if not edit else ""}{"Guardar cambios" if edit else "Enviar invitación"}</button></div></aside>')
comp('FormularioUsuario', 'Forms', 1010, '<div style="display:flex;flex-wrap:wrap;gap:24px;align-items:flex-start">' + form(err=True) + form(edit=True) + '</div>',
'''Formulario de alta y edición en panel lateral: se llena sin perder de vista la tabla.

- **Contenedor:** panel derecho de 440 px, `surface`, `radius-lg`, `shadow-overlay`; encabezado con título (`title-2`), una línea de qué pasará y «Cerrar»; pie fijo con «Cancelar» (secundario) y la acción primaria con verbo + objeto («Enviar invitación», «Guardar cambios»).
- **Campos:** etiqueta `label` arriba, ayuda `caption` abajo; borde «border-control», `shadow-inset`, anillo «primary-soft» al enfocar. El correo va en Plex Mono porque se copia y se compara.
- **Errores:** al salir del campo; borde «fuera», anillo «fuera-soft», icono y mensaje que dice cómo corregir («Falta el dominio: debe terminar en @nisanabani.mx»). Al enviar con errores, el foco va al primero.
- **Opciones excluyentes** (rol): tarjetas de opción con descripción, la elegida en «primary-soft» con borde «primary». **Múltiples** (divisiones): casillas en chip.
- **Zona de riesgo** solo en edición, separada por un filete, con el botón destructivo (`btn-d`) y su consecuencia escrita. Nunca junto a «Guardar».
- **Riesgo:** cerrar con cambios sin guardar pide confirmar («Descartar cambios»); suspender pide motivo; dar de baja es otra acción con confirmación.
- El consumidor provee: modo (alta/edición), valores, roles y divisiones disponibles, y permisos.''', w=1000)

# ---------- 3 · módulo completo e interactivo ----------
JS = r'''
<script>
(function(){
  var tb=document.getElementById('tb'),rows=[].slice.call(tb.querySelectorAll('tr')),q=document.getElementById('q'),bulk=document.getElementById('bulk'),bn=document.getElementById('bn');
  var all=document.getElementById('all'),panel=document.getElementById('panel'),scrim=document.getElementById('scrim'),toast=document.getElementById('toast'),empty=document.getElementById('empty');
  var estF=null,opener=null;
  function apply(){var v=q.value.trim().toLowerCase(),n=0;rows.forEach(function(r){var ok=(!v||r.dataset.s.indexOf(v)>=0)&&(!estF||r.dataset.e===estF);r.hidden=!ok;if(ok)n++});empty.hidden=n>0;document.getElementById('rng').textContent=n?('1–'+n+' de 24'):'0 de 24';document.getElementById('qv').textContent=q.value}
  q.addEventListener('input',apply);
  document.querySelectorAll('[data-est]').forEach(function(c){c.onclick=function(){var on=c.getAttribute('aria-pressed')!=='true';document.querySelectorAll('[data-est]').forEach(function(o){o.setAttribute('aria-pressed','false')});c.setAttribute('aria-pressed',on);estF=on?c.dataset.est:null;apply()}});
  document.querySelectorAll('[data-clear]').forEach(function(b){b.onclick=function(){q.value='';estF=null;document.querySelectorAll('[data-est]').forEach(function(o){o.setAttribute('aria-pressed','false')});apply();q.focus()}});
  function sel(){var s=rows.filter(function(r){return r.querySelector('input').checked});rows.forEach(function(r){r.setAttribute('aria-selected',r.querySelector('input').checked)});bulk.hidden=!s.length;bn.textContent=s.length+(s.length===1?' seleccionado':' seleccionados');all.checked=s.length===rows.length;all.indeterminate=s.length>0&&s.length<rows.length}
  rows.forEach(function(r){r.querySelector('input').onchange=sel});
  all.onchange=function(){rows.forEach(function(r){if(!r.hidden)r.querySelector('input').checked=all.checked});sel()};
  document.getElementById('unsel').onclick=function(){rows.forEach(function(r){r.querySelector('input').checked=false});sel()};
  function open(mode,r,from){
    opener=from;panel.hidden=false;scrim.hidden=false;
    document.getElementById('pt').textContent=mode==='edit'?'Editar usuario':'Agregar usuario';
    document.getElementById('pd').textContent=mode==='edit'?'Los cambios se aplican la próxima vez que entre.':'Le enviaremos una invitación para crear su contraseña.';
    document.getElementById('fn').value=r?r.dataset.n:'';document.getElementById('fm').value=r?r.dataset.m:'';
    document.getElementById('go').lastChild.textContent=mode==='edit'?'Guardar cambios':'Enviar invitación';
    document.getElementById('riesgo').hidden=mode!=='edit';
    document.querySelectorAll('.cur').forEach(function(c){c.remove()});
    if(r)r.querySelector('.who b').insertAdjacentHTML('beforeend','<span class="cur" title="En edición"></span>');
    ferr(false);document.getElementById('fn').focus();
  }
  function close(){panel.hidden=true;scrim.hidden=true;document.querySelectorAll('.cur').forEach(function(c){c.remove()});if(opener)opener.focus()}
  document.getElementById('add').onclick=function(){open('add',null,this)};
  rows.forEach(function(r){r.querySelector('[data-edit]').onclick=function(){open('edit',r,this)}});
  document.getElementById('px').onclick=close;document.getElementById('pc').onclick=close;scrim.onclick=close;
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!panel.hidden)close()});
  function ferr(on,msg){var f=document.getElementById('ff');f.dataset.state=on?'error':'idle';document.getElementById('fm').setAttribute('aria-invalid',on);document.getElementById('fme').hidden=!on;if(msg)document.getElementById('fmt').textContent=msg}
  document.getElementById('fm').addEventListener('blur',function(){var v=this.value.trim();if(v&&!/@nisanabani\.mx$/.test(v))ferr(true,'Debe ser un correo @nisanabani.mx.');else ferr(false)});
  document.getElementById('frm').onsubmit=function(e){e.preventDefault();var v=document.getElementById('fm').value.trim();
    if(!/@nisanabani\.mx$/.test(v)){ferr(true,v?'Debe ser un correo @nisanabani.mx.':'Escribe el correo del laboratorio.');document.getElementById('fm').focus();return}
    var go=document.getElementById('go');go.setAttribute('aria-busy','true');go.disabled=true;
    setTimeout(function(){go.removeAttribute('aria-busy');go.disabled=false;var edit=document.getElementById('pt').textContent==='Editar usuario';close();
      document.getElementById('tt').textContent=edit?'Cambios guardados.':'Invitación enviada a '+v+'.';toast.hidden=false;document.getElementById('tu').hidden=edit;document.getElementById('tx').focus()},700)};
  document.getElementById('tx').onclick=function(){toast.hidden=true};document.getElementById('tu').onclick=function(){document.getElementById('tt').textContent='Invitación cancelada.';this.hidden=true};
})();
</script>'''
body_mod = ('<div style="position:relative;min-height:760px">' + HEADER.replace('<button class="btn btn-p">', '<button class="btn btn-p" id="add">')
  + '<div class="card">'
  + f'<div class="tb"><label class="fld" style="flex:1;min-width:220px;max-width:360px">{i("search")}<span class="vh">Buscar usuario</span><input id="q" placeholder="Buscar por nombre o correo" autocomplete="off"></label>'
  + '<span class="vh">Filtrar por estado:</span>' + ''.join(f'<button class="chip" data-est="{k}" aria-pressed="false">{EST[k][2]}</button>' for k in ('act', 'inv', 'sus', 'blo'))
  + '<button class="btn btn-g" data-clear style="min-height:32px;margin-left:auto">Limpiar filtros</button></div>'
  + f'<div class="bulk" id="bulk" hidden role="region" aria-label="Acciones para la selección"><span class="n" id="bn" aria-live="polite"></span><button class="btn">Cambiar rol</button><button class="btn">Suspender</button><button class="btn" id="unsel" aria-label="Quitar selección">{i("x")}</button></div>'
  + '<div class="tw" tabindex="0" role="region" aria-label="Tabla de usuarios"><table class="tbl" aria-label="Usuarios">' + THEAD.replace('aria-label="Seleccionar todos"', 'id="all" aria-label="Seleccionar todos"') + '<tbody id="tb">'
  + ''.join(row(u).replace('<tr>', f'<tr data-s="{(u[1] + " " + u[2]).lower()}" data-e="{u[6]}" data-n="{u[1]}" data-m="{u[2]}">', 1).replace('aria-label="Editar a', 'data-edit aria-label="Editar a') for u in USERS)
  + '</tbody></table></div>'
  + '<div class="empty" id="empty" hidden><p class="lm">Ningún usuario coincide.</p><p>No hay resultados para «<span id="qv"></span>» con los filtros actuales.</p><button class="btn btn-s" data-clear>Limpiar filtros</button></div>'
  + '<div class="tf"><span id="rng">1–6 de 24</span><span><button class="btn btn-g" style="min-height:32px">Anterior</button><button class="btn btn-g" style="min-height:32px">Siguiente</button></span></div></div>'
  + '<div id="scrim" hidden style="position:fixed;inset:0;background:rgba(20,27,51,.18)"></div>'
  + '<aside class="panel" id="panel" hidden role="dialog" aria-modal="true" aria-labelledby="pt" style="position:fixed;top:16px;right:16px;bottom:16px">'
  + f'<div class="ph"><div style="flex:1"><h2 id="pt">Agregar usuario</h2><p id="pd"></p></div><button class="ib" id="px" aria-label="Cerrar">{i("x")}</button></div>'
  + '<form id="frm" novalidate style="display:contents"><div class="pb">'
  + '<div class="f"><label for="fn">Nombre completo</label><label class="fld"><input id="fn" autocomplete="off"></label></div>'
  + f'<div class="f" id="ff"><label for="fm">Correo del laboratorio</label><label class="fld">{i("mail")}<input id="fm" style="font-family:var(--font-datos);font-size:14px" aria-describedby="fmh fme" autocomplete="off"></label><span class="help" id="fmh">Será su usuario para entrar.</span><span class="err" id="fme" hidden>{i("circle-alert")}<span id="fmt"></span></span></div>'
  + '<fieldset class="f"><legend>Rol</legend><div class="opts">' + ''.join(f'<label class="opt"><input type="radio" name="rol"{" checked" if r == "Analista" else ""}><b>{r}</b><small>{d}</small></label>' for r, d in [('Recepción', 'Registra muestras y entrega certificados.'), ('Analista', 'Captura resultados de sus divisiones.'), ('Supervisor de calidad', 'Revisa y libera resultados.'), ('Administración', 'Gestiona usuarios y catálogos.')]) + '</div></fieldset>'
  + '<div class="danger" id="riesgo" hidden><b style="font:600 14px var(--font-sans)">Zona de riesgo</b><p>Suspender detiene su acceso hoy; sus resultados y firmas se conservan.</p><div><button type="button" class="btn btn-d">Suspender acceso</button></div></div>'
  + '</div><div class="pf"><button type="button" class="btn btn-s" id="pc">Cancelar</button><button class="btn btn-p" id="go">' + i('send') + 'Enviar invitación</button></div></form></aside>'
  + '<div class="toast" id="toast" hidden role="status" style="position:fixed;left:50%;bottom:24px;transform:translateX(-50%)"><span id="tt"></span><button class="btn" id="tu">Deshacer</button><button class="ib" id="tx" aria-label="Cerrar aviso" style="color:var(--on-primary)">' + i('x') + '</button></div>'
  + '</div>' + JS)
comp('ModuloUsuarios', 'Módulos', 900, body_mod,
'''Módulo completo de Usuarios: la composición de referencia para cualquier módulo de administración de Nabi (clientes, métodos, equipos).

Orden de arriba abajo: `EncabezadoModulo` → tarjeta con barra de herramientas (búsqueda + filtros + limpiar), barra de acciones en lote (solo con selección), `TablaUsuarios`, pie con rango y paginación. «Agregar usuario» y «Editar» abren `FormularioUsuario` en panel lateral; al guardar, un aviso confirma con «Deshacer» cuando se puede revertir.

Pruébalo: busca, filtra por estado, selecciona filas, abre «Agregar usuario» y envía con un correo sin dominio. Ver la sección «Módulos» del manual para las reglas.''', w=1280)

# ---------- 4 · sección del manual ----------
open(f'{P}/modulos.md', 'w').write('''# Módulos

Cómo se arma una pantalla de módulo en Nabi (Usuarios, Clientes, Métodos, Equipos): qué color va en cada zona, qué voz tipográfica, dónde viven las acciones, cómo se muestran los estados y cómo responden las interacciones. El ejemplo vivo es el componente `ModuloUsuarios`.

## Anatomía

1. **Encabezado** (`EncabezadoModulo`): ruta · título · entradilla opcional · conteo · acciones. Sin fondo propio.
2. **Tarjeta de trabajo**: barra de herramientas, tabla y pie, en una sola tarjeta elevada (`shadow-1`).
3. **Capas** que aparecen solo cuando hacen falta: barra de acciones en lote, panel lateral del formulario, aviso con «Deshacer».

## Color por zona

| Zona | Fondo | Texto | Borde y sombra |
|---|---|---|---|
| Página | `bg` | — | — |
| Encabezado | (sobre `bg`) | título `text`; ruta, entradilla y conteo `text-muted` | — |
| Acción primaria | `primary` | `on-primary` | `shadow-primary`; hover `primary-hover` + `shadow-primary-hover` |
| Acción secundaria | `surface` | `primary` | `border-control` + `shadow-1` |
| Tarjeta de trabajo | `surface` | `text` | `border` + `shadow-1` |
| Encabezado de tabla | `surface-sunken` | `text-muted` | `border` abajo |
| Fila en hover | `surface-hover` | `text` | — |
| Fila seleccionada | `primary-soft` | `text` | casilla marcada |
| Registro en curso | — | — | un pocillo `pera` junto al nombre (uno por pantalla) |
| Campos | `surface` | `text`; placeholder `text-subtle` | `border-control` + `shadow-inset`; foco `primary` + anillo `primary-soft` |
| Filtro activo | `primary-soft` | `primary` | — |
| Estados | `*-soft` | `on-*-soft` + icono | — |
| Barra de lote, aviso | `text` (tinta) | blanco | `shadow-overlay` |
| Panel lateral | `surface` | `text` | `shadow-overlay`, `radius-lg` |
| Destructiva | `surface` | `fuera` | borde `fuera`; separada por un filete |

Proporción: casi todo es `bg`, `surface` y tinta; el azul aparece en la acción primaria, los enlaces y la selección; los colores de estado solo en la columna de estado; el pera, una vez.

## Tipografía por zona

| Elemento | Estilo |
|---|---|
| Ruta | `label` (Archivo 500 13/18) |
| Título del módulo | Archivo 700 al 125 %, 26/32 (`title-1` ampliado) |
| Entradilla | `entradilla` (Newsreader itálica 17/24) |
| Conteo, último acceso, correos, folios | Plex Mono (`valor-sm`, `folio`) con cero con barra |
| Encabezados de columna | `label` |
| Nombre en tabla | Archivo 600 15/22 |
| Botones | `button` |
| Título del panel | `title-2` |
| Ayudas y errores | `caption` |

## Encabezado: reglas

- **Título sin icono.** El icono del módulo vive en el menú lateral; junto al título repite información y compite con la acción primaria.
- **Una sola acción primaria**, arriba a la derecha, con verbo + objeto: «Agregar usuario», «Registrar cliente». Las demás, secundarias o en «Más».
- **Entradilla** solo en módulos de configuración o poco frecuentes; nunca en pantallas de captura diaria.
- **Conteos** que ayudan a decidir («3 invitaciones pendientes»), en Plex Mono.

## Tabla de personas

- Columnas en este orden: casilla · Usuario (iniciales o foto, nombre, correo) · Rol · Divisiones · Último acceso · Estado · acciones.
- Filas de 56 px (dos líneas); 40 px si solo hay una.
- Lo que se compara o copia (fechas, correos, folios) en Plex Mono; lo que se lee, en Archivo.
- Acciones por fila: «Editar» y «Más», visibles al pasar o enfocar la fila y siempre en táctil. Nunca más de dos iconos por fila.

## Estados

El color sigue al significado y es el mismo en todos los módulos:

| Significado | Tokens | Ejemplos |
|---|---|---|
| Está bien | `conforme-soft` / `on-conforme-soft` | Activo · Conforme · Liberada |
| Pendiente | `pendiente-soft` / `on-pendiente-soft` | Invitación enviada · En análisis |
| Requiere atención | `alerta-soft` / `on-alerta-soft` | Suspendido · En revisión |
| Impedido | `fuera-soft` / `on-fuera-soft` | Bloqueado · Fuera · Rechazada |
| Fuera de uso | `surface-sunken` / `text-muted` | Dado de baja · Recibida |

Siempre icono + palabra. El pera no es un estado.

## Interacciones

| Interacción | Respuesta |
|---|---|
| Pasar sobre una fila | `surface-hover` en 150 ms (`quick`); aparecen sus acciones |
| Seleccionar | `primary-soft`; aparece la barra de lote con el conteo |
| Filtrar | El chip pasa a `primary-soft`; el conteo y el pie se actualizan; si no hay resultados, estado vacío con «Limpiar filtros» |
| Ordenar | Flecha en la columna activa y `aria-sort` |
| Abrir formulario | Panel lateral con `shadow-overlay`; el registro en curso recibe el pocillo pera; Esc o «Cerrar» devuelven el foco |
| Guardar | Botón ocupado (sin doble envío); al terminar, aviso con «Deshacer» si se puede revertir |
| Botón primario | Hover: 1 px hacia arriba y sombra mayor; presionado: vuelve a su lugar |

Con `prefers-reduced-motion`: sin desplazamientos, solo cambios de color.

## Formularios

- En **panel lateral** de 440 px para altas y ediciones cortas; en página propia si pasan de ~12 campos o tienen secciones.
- Etiqueta arriba, ayuda abajo, error en lugar de la ayuda; validación al salir del campo; al enviar con errores, foco al primero.
- Opciones excluyentes con descripción → tarjetas de opción; múltiples cortas → casillas en chip.
- Pie fijo: «Cancelar» (secundario) a la izquierda de la primaria. Lo destructivo, en «Zona de riesgo», separado y con su consecuencia escrita.

## Estados de la pantalla

- **Carga:** esqueleto con la huella de la tabla (filas de 56 px); el encabezado ya visible.
- **Vacío inicial:** frase editorial («Aún no hay usuarios») + qué hacer + acción primaria.
- **Vacío por filtros:** «Ningún usuario coincide» + filtros activos + «Limpiar filtros».
- **Error:** causa + «Reintentar»; si había datos, se conservan y se marcan como no actualizados.
- **Sin permiso:** el módulo no aparece en el menú; si se llega por enlace, explicación y a quién pedir acceso.

## Por espacio

- **Escritorio (≥ 1024):** todo visible; panel lateral junto a la tabla.
- **Tableta (600–1023):** Divisiones y Último acceso pasan al detalle; el panel cubre la tabla.
- **Móvil (< 600):** cada usuario es un bloque (nombre, correo, estado); acciones en el menú «Más»; «Agregar usuario» como botón fijo abajo; el formulario a pantalla completa.
''')
print('ok', sorted(os.listdir(f'{P}/components')))
