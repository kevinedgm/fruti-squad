# Ecosistema Manik · integra al sistema de diseño las rondas aprobadas el 2026-11-05:
#   controles-r01 (botones, campos y controles de selección) y formularios-r01 (formularios y diálogos).
# Paso idempotente sobre project/ (no usa build.py: project/ ya tiene cambios posteriores, como Administración e IA,
# que build.py no reproduce). Uso: python3 controles_formularios.py
import json, os, re, importlib.util, datetime
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, 'project'); M = os.path.join(D, '..')

def load(name, rel):
    s = importlib.util.spec_from_file_location(name, os.path.join(M, rel)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

# 1 · tokens nuevos (antes de cargar las rondas, para que lean los valores ya en el sistema)
tp = os.path.join(P, 'tokens.json'); T = json.load(open(tp))
def upsert(group, name, value, usage):
    toks = T[group]['tokens']
    for x in toks:
        if x['name'] == name: x.update(value=value, usage=usage); return
    toks.append({'name': name, 'value': value, 'usage': usage})
upsert('color', 'scrim', 'rgba(20, 33, 61, 0.40)', 'Fondo detrás de diálogos y hojas inferiores: tinta al 40 %. Nunca como color de superficie.')
upsert('layout', 'control-height-compact', '36px', 'Botones y chips compactos: SOLO filas de tabla y barras de filtros. En formularios, siempre control-height.')
upsert('layout', 'form-max', '640px', 'Ancho máximo de un formulario en página.')
upsert('layout', 'dialog-sm', '400px', 'Diálogo de confirmación (sin campos).')
upsert('layout', 'dialog-md', '560px', 'Diálogo de formulario (hasta 6 campos).')
upsert('layout', 'dialog-lg', '720px', 'Diálogo de formulario con un par de columnas.')
T['version'] = max(T.get('version', 2), 3)
json.dump(T, open(tp, 'w'), indent=1, ensure_ascii=False)

# las rondas evaluadas no se reescriben: se guardan antes de importarlas y se restauran después
KEEP = {p: open(os.path.join(M, p)).read() for p in ('controles-r01/controles.html', 'formularios-r01/formularios.html')}
C = load('ctl', 'controles-r01/gen.py')
F = load('frm', 'formularios-r01/gen.py')
for p, t in KEEP.items(): open(os.path.join(M, p), 'w').write(t)
CSS = C.HTML.split('<style>', 1)[1].split('</style>', 1)[0]
CSSF = F.EXTRA
ic = C.ic
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700&display=swap">'
JS = '''<script>document.querySelectorAll('.sw:not([disabled])').forEach(s=>s.addEventListener('click',()=>{const on=s.getAttribute('aria-checked')!=='true';s.setAttribute('aria-checked',on);const t=s.parentElement.querySelector('.sw-t');if(t)t.textContent=on?'Activado':'Desactivado'}));
document.querySelectorAll('.chip:not([disabled])').forEach(c=>c.addEventListener('click',()=>c.setAttribute('aria-pressed',c.getAttribute('aria-pressed')!=='true')));
document.querySelectorAll('[role=radiogroup]').forEach(g=>{const bs=[...g.querySelectorAll('[role=radio]')];bs.forEach((b,i)=>{b.addEventListener('click',()=>bs.forEach(x=>{x.setAttribute('aria-checked',x===b);x.tabIndex=x===b?0:-1}));b.addEventListener('keydown',e=>{const d={ArrowRight:1,ArrowDown:1,ArrowLeft:-1,ArrowUp:-1}[e.key];if(d){e.preventDefault();const n=bs[(i+d+bs.length)%bs.length];n.click();n.focus()}})})});
document.querySelectorAll('input[data-ind]').forEach(i=>i.indeterminate=true);</script>'''
def page(grp, h, body, extra=''):
    return (f'<!-- @dsCard group="{grp}" height={h} -->\n<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>{CSS}{CSSF}'
            f'body{{padding:16px;background:var(--canvas)}}.pv{{display:grid;gap:14px}}.fila{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}{extra}</style></head><body><div class="pv">{body}</div>{JS}</body></html>')

comps = {}
# ---------- Boton ----------
B = C.boton
comps['Boton'] = ('Acciones', 192, page('Acciones', 192,
    '<div class="fila">' + B('b1', 'Guardar receta', '') + B('b2', 'Vista previa', '') + B('b3', 'Cancelar', '') + B('b4', 'Eliminar receta', '', 'trash') + B('b5', 'Sí, eliminar', '') + '</div>'
    '<div class="fila">' + B('b1', 'Guardar receta', 'l') + B('b1', 'Guardar receta', 'd') + B('b2', 'Vista previa', 'd') + f'<button type="button" class="ibtn" aria-label="Imprimir">{ic("print")}</button>' + '</div>'
    f'<div class="fila"><button type="button" class="btn b1 c">{ic("plus")}<span>Agregar</span></button><button type="button" class="btn b2 c">Exportar</button><button type="button" class="btn b3 c">Ver todo</button><button type="button" class="ibtn s" aria-label="Más acciones">{ic("more")}</button><span class="nota">Compacto 36 px · solo tablas y filtros</span></div>'),
 '''Botón: la acción principal es azul Manik en TODAS las apps, sin importar el color del producto. Aprobado 2026-11-05 (`../../controles-r01/`).

- **Variantes.** `primario` («manik» / «on-manik»), una por vista. `secundario` («surface», borde «line-control», texto «manik»). `terciario` (solo texto). `destructivo` (contorno y texto «error») para iniciar una acción que borra. `destructivo-confirmación` (relleno «error», blanco encima 5.07:1) SOLO dentro del diálogo que confirma. `icono` (44 × 44, «muted», con `aria-label`).
- **Estados.** Hover: «manik-hover» en el primario; «surface-soft» en secundario, terciario e icono; «error-soft» en el destructivo. Presionado: «surface-pressed» o sombra interior. Foco: anillo «focus» 2 px con 2 px de separación. Cargando: icono girando a la izquierda, mismo ancho, `aria-busy`, no se puede pulsar dos veces. Deshabilitado: «surface-soft», borde «line», texto «muted» (5.98:1), sin color de acción, `aria-disabled`.
- **Tamaños.** `control-height` 44 px en todo. `control-height-compact` 36 px solo en filas de tabla y barras de filtros.
- **El botón principal de un formulario nunca se deshabilita:** se pulsa y el formulario dice qué falta.
- Por qué no el color del producto: Farmacia, Compras y Grupos se parecen a éxito, aviso y error; un botón verde o rojo diría otra cosa. El mismo botón en todas las apps evita reaprender al cambiar de app.
- El consumidor provee: verbo + objeto, estado de carga y `aria-disabled`.''')

# ---------- Campo ----------
cm, inp = C.campo, C.inp
sel = lambda fid, v, est='': f'<span class="sel {est}"><select id="{fid}"{" disabled" if est == "d" else ""}><option>{v}</option></select>{ic("chev", "ico chev")}</span>'
comps['Campo'] = ('Formularios', 446, page('Formularios', 446,
    '<div class="grid2">' + cm('Medicamento', inp('m1', 'Losartán'), ayuda='Nombre genérico o comercial.', fid='m1')
    + cm('Dosis diaria', inp('m2', '140', 'e', '', 'mg'), err='Máximo 100 mg al día', fid='m2')
    + cm('Vía', sel('m3', 'Oral'), fid='m3') + cm('Folio', inp('m4', 'EXP-0000-0001', 'ro'), fid='m4')
    + cm('Correo', inp('m5', '', ph='nombre@correo.com', tipo='email'), opc=True, fid='m5') + cm('Sucursal', inp('m6', 'Centro', 'd'), fid='m6')
    + f'<div class="campo"><label for="m7">Buscar paciente</label><span class="bus">{ic("search")}<input id="m7" class="in" type="search" placeholder="Nombre, folio o teléfono"></span></div>'
    + '<div class="campo"><label for="m8">Indicaciones <span class="opc">(opcional)</span></label><textarea id="m8" class="in" rows="2"></textarea></div></div>'),
 '''Campo de captura. Atkinson en todo el texto: distingue 1, l e I, y 0 y O. Aprobado 2026-11-05 (`../../controles-r01/`).

- **Tipos:** texto, número con unidad, lista, fecha, buscador (icono a la izquierda y botón para borrar) y área de texto (mínimo 96 px).
- **Anatomía:** etiqueta `label` arriba, siempre visible, en sustantivo y sin dos puntos; ayuda abajo en «muted»; el texto de ejemplo dentro del campo no sustituye a la etiqueta.
- **Medidas:** 44 px, borde 1 px «line-control», radio `radius-md`, texto 16 px.
- **Estados.** Hover: borde «muted». Foco: borde «manik» y anillo «focus» 2 px. Error: borde 2 px «error», icono y mensaje que dice qué hacer («Máximo 100 mg al día»), `aria-invalid` y `aria-describedby`. Solo lectura: «surface-soft» con borde «line» (se puede copiar). Deshabilitado: «surface-soft», borde «line», texto «muted».
- **Opcional:** se marca «(opcional)»; lo obligatorio no lleva marca.
- **Números clínicos** (dosis, peso, glucosa): cifras tabulares, alineados a la derecha, unidad fija como sufijo en «muted». La unidad la pone el sistema.
- El consumidor provee: etiqueta, unidad, rango válido y mensaje, `id` y `aria-describedby`.''')

# ---------- selección ----------
chk, sw, seg, chip = C.chk, C.sw, C.seg, C.chip
comps['Casilla'] = ('Formularios', 316, page('Formularios', 316,
    f'<fieldset><legend>Antecedentes</legend>{chk("Diabetes", checked=True)}{chk("Hipertensión")}{chk("Seleccionar todo", ind=True)}{chk("Alergias registradas", "e")}<span class="err">{ic("alert")}Confirma si hay alergias</span>{chk("Cirugías previas", "d")}</fieldset>'),
 '''Casilla: varias opciones a la vez, o una sola que se confirma con «Guardar».

- Caja de 20 px, radio 6, borde 1.5 px «line-control»; marcada en «manik» con palomita blanca; parcial (indeterminada) con guion.
- Toda la fila (44 px) es tocable; la etiqueta es el `<label>` del `<input type="checkbox">` nativo.
- Error: borde 2 px «error» y mensaje debajo del grupo. Deshabilitada: caja «surface-soft», borde «line», texto «muted».
- Un grupo lleva `<fieldset>` y `<legend>`.''')
comps['OpcionUnica'] = ('Formularios', 202, page('Formularios', 202,
    f'<fieldset><legend>Tipo de consulta</legend>{chk("Primera vez", tipo="radio", checked=True, name="tc")}{chk("Seguimiento", tipo="radio", name="tc")}{chk("Urgencia", "d", "radio", name="tc")}</fieldset>'),
 '''Opción única: una sola opción entre 2 y 5 visibles. Con más de 5, Campo de tipo lista.

- Círculo de 20 px, borde 1.5 px «line-control»; elegida con punto «manik».
- Fila de 44 px tocable, `<input type="radio">` nativo con el mismo `name`, dentro de `<fieldset>` y `<legend>`.
- Siempre hay una elegida por defecto cuando existe una respuesta razonable; si no, ninguna y el formulario la pide al enviar.''')
comps['Interruptor'] = ('Formularios', 200, page('Formularios', 200,
    sw('Recordatorio por mensaje', True) + sw('Mostrar en el directorio') + sw('Firma electrónica', True, 'd')),
 '''Interruptor: SOLO para ajustes que se aplican al momento, sin botón «Guardar». Si el cambio espera a «Guardar», es Casilla.

- Pista de 44 × 26: apagado «line-control» (3.28:1), encendido «manik»; perilla blanca de 20 px.
- `<button role="switch" aria-checked>` con la etiqueta a la izquierda (`aria-labelledby`) y el estado escrito a la derecha («Activado» / «Desactivado»): nunca solo la posición.
- Deshabilitado: pista «line», texto «muted». Respeta `prefers-reduced-motion`.''')
comps['ControlSegmentado'] = ('Formularios', 142, page('Formularios', 142,
    seg(['Día', 'Semana', 'Mes'], 1, 'Vista de la agenda') + seg(['Lista', 'Tarjetas'], 0, 'Vista de recetas')),
 '''Control segmentado: cambia la vista de lo mismo (día, semana, mes). De 2 a 4 opciones cortas. No filtra datos (eso es ChipFiltro) ni navega a otra sección (eso son pestañas).

- Contenedor «surface-soft» con borde «line» y radio `radius-md`; opción de 36 px; la elegida en «surface» con `shadow-card` y texto «manik».
- `role="radiogroup"` con `role="radio"` y `aria-checked`; flechas para moverse, una sola parada de tabulador.''')
comps['ChipFiltro'] = ('Formularios', 76, page('Formularios', 76,
    '<div class="fila" role="group" aria-label="Filtrar citas">' + chip('Hoy', True) + chip('Primera vez') + chip('Por confirmar', True) + chip('Canceladas', d=True) + '</div>'),
 '''Chip de filtro: filtra una lista; se pueden combinar.

- Píldora de 36 px, borde «line-control», texto «ink» 600; activo en «manik-soft» con borde y texto «manik» y palomita (la palomita lo dice sin color).
- `<button aria-pressed>`; el grupo lleva `role="group"` y `aria-label`.
- Deshabilitado: «surface-soft», borde «line», texto «muted».''')

# ---------- Dialogo ----------
dlg_static = f'''<div class="dlg-st md" role="dialog" aria-labelledby="d1t" aria-describedby="d1s"><header class="dh"><div><h2 id="d1t">Nueva cita</h2><p id="d1s">Mariana Ruiz · Expediente 0001</p></div><button type="button" class="ibtn" aria-label="Cerrar">{ic("x")}</button></header>
<div class="db">{cm("Tipo de consulta", sel("dq1", "Seguimiento"), fid="dq1")}<div class="par">{cm("Día", inp("dq2", "2026-11-12", tipo="date"), fid="dq2")}{cm("Hora", sel("dq3", "10:00"), fid="dq3")}</div></div>
<footer class="df"><button type="button" class="btn b3">Cancelar</button><button type="button" class="btn b1">Guardar cita</button></footer></div>
<div class="dlg-st sm" role="alertdialog" aria-labelledby="d2t" aria-describedby="d2s"><header class="dh"><div><h2 id="d2t">¿Eliminar la receta de Mariana Ruiz?</h2></div></header>
<div class="db"><p id="d2s">Se borra del expediente y la farmacia ya no podrá surtirla. No se puede deshacer.</p></div>
<footer class="df"><button type="button" class="btn b3">Cancelar</button><button type="button" class="btn b5">Sí, eliminar</button></footer></div>'''
comps['Dialogo'] = ('Superposiciones', 680, page('Superposiciones', 680, f'<div class="velo">{dlg_static}</div>',
    '.velo{background:var(--scrim);border-radius:var(--radius-2xl);padding:24px;display:flex;flex-wrap:wrap;gap:24px;align-items:flex-start;justify-content:center}'
    '.dlg-st{background:var(--surface);border-radius:var(--radius-2xl);box-shadow:var(--shadow-pop);display:flex;flex-direction:column;width:100%}.dlg-st.md{max-width:var(--dialog-md)}.dlg-st.sm{max-width:var(--dialog-sm)}'),
 '''Diálogo: tarea corta que se termina sin salir de la vista. Aprobado 2026-11-05 (`../../formularios-r01/`).

- **¿Diálogo, panel o página?** Confirmación: sin campos. Diálogo de formulario: hasta 6 campos, un grupo, no hace falta ver lo de atrás. Panel lateral: 7 a 12 campos o hay que seguir viendo el contexto (componente pendiente). Página: más de 12 campos, varios grupos o pasos.
- **Anatomía:** cabecera (título `title-2` con verbo + objeto, una línea de contexto en «muted» y cerrar de 44 px), cuerpo (24 px de relleno, 12 px entre campos; solo él se desplaza) y pie (borde superior «line», acciones a la derecha: terciario «Cancelar» y el principal).
- **Medidas:** `dialog-sm` 400 (confirmación), `dialog-md` 560 (formulario), `dialog-lg` 720 (con un par de columnas). Radio `radius-2xl`, `shadow-pop`, fondo detrás `scrim`.
- **Celular (< 640 px):** hoja inferior a todo el ancho, hasta el 90 % del alto, pie fijo con acciones apiladas y el principal arriba.
- **Foco:** al abrir, al primer campo (en confirmación, al botón seguro «Cancelar»); no sale del diálogo; al cerrar vuelve al botón que lo abrió. Usar `<dialog>` con `showModal()` o `role="dialog"`/`alertdialog` con `aria-modal`.
- **Cerrar:** X, «Cancelar» o Esc. Con cambios sin guardar, primero «¿Descartar los cambios?». Un clic fuera no cierra un formulario; sí una confirmación.
- **Nunca un diálogo sobre otro**, salvo la confirmación de descartar.
- **Guardar:** el botón pasa a cargando; al terminar se cierra y un aviso breve confirma («Cita guardada»). Si falla, sigue abierto con el error arriba y los datos intactos.
- **Confirmación destructiva:** el título es la pregunta con el objeto, el cuerpo dice la consecuencia, acciones «Cancelar» y «Sí, eliminar» (Boton destructivo-confirmación). Nunca «Aceptar».''')

# ---------- Formulario (patrón) ----------
comps['Formulario'] = ('Patrones', 833, page('Patrones', 833, F.pagina),
 '''Formulario en página. Aprobado 2026-11-05 (`../../formularios-r01/`).

- **Una columna.** Dos solo para pares cortos que se leen juntos (inicio y fin, presión sistólica y diastólica); nunca tres.
- **Orden de la tarea**, no de la base de datos; lo que se calcula no se pide; se llena lo que ya se sabe (paciente, fecha, médico en sesión).
- **Grupos con título** (`title-2`) con más de 5 campos: `space-3` (12 px) entre campos, `space-8` (32 px) entre grupos; sin líneas.
- **Ancho por dato** y `form-max` (640 px) para todo el formulario.
- **Acciones al final**, a la derecha: terciario «Cancelar» y luego el principal con verbo + objeto. La destructiva a la izquierda, separada. En celular, apiladas a todo el ancho, el principal arriba.
- **Validación:** al salir del campo y al enviar; mientras se escribe solo para límites clínicos. Al enviar con errores, resumen arriba (número de errores y un enlace a cada uno) que recibe el foco; los datos se quedan. Error del servidor: aviso arriba con la acción posible. Salir con cambios pide «¿Descartar los cambios?».
- **El botón principal nunca se deshabilita.**''')

for name, (grp, h, html, md) in comps.items():
    os.makedirs(os.path.join(P, 'components', name), exist_ok=True)
    open(os.path.join(P, 'components', name, 'preview.html'), 'w').write(html)
    open(os.path.join(P, 'components', name, 'README.md'), 'w').write(f'# {name}\n\n{md}\n')

# 2 · README: sección nueva (reemplaza la anterior si existe) y pendientes
rp = os.path.join(P, 'README.md'); R = open(rp).read()
SEC = '''## Controles, formularios y diálogos (aprobado 2026-11-05)

Una sola familia para las siete apps: lo que cambia por app es el sello y el nombre; todo lo que se toca usa el azul Manik, 44 px, `radius-md` y el mismo foco. Rondas: `../../controles-r01/` y `../../formularios-r01/`.

- **Componentes:** Boton, Campo, Casilla, OpcionUnica, Interruptor, ControlSegmentado, ChipFiltro, Dialogo y el patrón Formulario.
- **Deshabilitado** (todas las piezas): «surface-soft», borde «line», texto «muted»; sin color de acción. Se dice por qué cerca del control.
- **Compacto** (`control-height-compact`, 36 px) solo en filas de tabla y barras de filtros.
- **Formularios:** una columna, orden de la tarea, grupos con título, ancho por dato, `form-max` 640 px, «(opcional)» en lo opcional, el botón principal nunca se deshabilita.
- **Contenedor por tamaño:** confirmación · diálogo hasta 6 campos · panel lateral 7 a 12 (pendiente) · página.
- **Diálogos:** `dialog-sm/md/lg` 400/560/720, `scrim` detrás, hoja inferior en celular, foco atrapado y de regreso, Esc con cambios pide descartar, clic fuera no cierra formularios.

'''
R = re.sub(r'## Controles, formularios y diálogos.*?(?=\n## )\n', '', R, flags=re.S)
R = R.replace('## Iconografía', SEC + '## Iconografía', 1)
R = R.replace('- Componentes por app (tablas, formularios largos, agenda) cuando se diseñe cada producto.',
              '- Componentes por app (tablas, agenda) cuando se diseñe cada producto.\n- Panel lateral (formularios de 7 a 12 campos con contexto visible).')
R = R.replace('- Controles de 44 px; barra superior de 64 px.', '- Controles de 44 px (36 px compactos solo en tablas y filtros); barra superior de 64 px.')
open(rp, 'w').write(R)

# 3 · design-system.json: nota de cambio (conserva assets y blobs)
jp = os.path.join(P, 'design-system.json'); J = json.load(open(jp))
J['lastChange'] = {'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'by': 'Kevin', 'via': 'Claude Code',
                   'note': 'Familia de controles y reglas de formularios y diálogos aprobadas: Boton y Campo con todos sus estados; Casilla, OpcionUnica, Interruptor, ControlSegmentado, ChipFiltro, Dialogo y el patrón Formulario; tokens scrim, control-height-compact, form-max y dialog-sm/md/lg.'}
json.dump(J, open(jp, 'w'), indent=2, ensure_ascii=False)
print('ok', sorted(comps))
