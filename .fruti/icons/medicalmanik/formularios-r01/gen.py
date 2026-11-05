# Ecosistema Manik · reglas de formularios y de formularios en diálogos · r01 (propuesta).
# Pedido (2026-11-05): «las reglas para el diseño de formularios, composición de formularios en dialogs».
# Reutiliza la familia de controles r01 (../controles-r01/gen.py: CSS, iconos y piezas) para no duplicar estilos;
# valores desde ../design-system/project/tokens.json. Uso: python3 gen.py → formularios.html
import os, importlib.util, json
D = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('ctl', os.path.join(D, '../controles-r01/gen.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
V, ic, campo, inp, sw, seg, chk = C.V, C.ic, C.campo, C.inp, C.sw, C.seg, C.chk
CSS = C.HTML.split('<style>', 1)[1].split('</style>', 1)[0]
SELLO = C.SELLOS['agenda']

def sel(fid, opts, val=None):
    o = ''.join(f'<option{" selected" if x == val else ""}>{x}</option>' for x in opts)
    return f'<span class="sel"><select id="{fid}">{o}</select>{ic("chev", "ico chev")}</span>'
def reglas(items): return '<ol class="reglas">' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def sino(si, no): return f'<div class="sino"><div class="si"><span class="tag ok">{ic("check")}Así</span>{si}</div><div class="no"><span class="tag mal">{ic("x")}Así no</span>{no}</div></div>'

# ---------- 1. formulario ----------
r_form = reglas([
 '<b>Una columna.</b> El ojo baja en línea recta y no se salta campos. Dos columnas solo para pares cortos que se leen juntos (inicio y fin, presión sistólica y diastólica); nunca tres en un formulario.',
 '<b>Orden de la tarea, no de la base de datos.</b> Lo que se sabe primero va primero; lo que se calcula no se pide.',
 '<b>Grupos con título</b> cuando hay más de 5 campos: título de tarjeta (18/26), 12 px entre campos del grupo y 32 px entre grupos. El aire separa; las líneas no hacen falta.',
 '<b>El ancho del campo dice el tamaño del dato:</b> dosis o código postal cortos, nombre o dirección completos. Ancho máximo del formulario: 640 px.',
 '<b>Etiqueta arriba, siempre visible,</b> en sustantivo y sin dos puntos («Dosis diaria»). El texto de ejemplo dentro del campo no sustituye a la etiqueta: desaparece al escribir.',
 '<b>Formato en la ayuda, no en la etiqueta:</b> «Como aparece en la identificación».',
 '<b>Lo opcional se marca «(opcional)»;</b> lo obligatorio no lleva marca. Si casi todo es opcional, el formulario sobra campos.',
 '<b>Se llena lo que ya se sabe:</b> paciente, fecha de hoy, médico en sesión. La unidad la pone el sistema.',
 '<b>Acciones al final,</b> alineadas a la derecha: terciario «Cancelar» y luego el principal con verbo + objeto («Guardar receta»). La destructiva va a la izquierda, separada. En celular, apiladas a todo el ancho, el principal arriba.',
 '<b>El botón principal nunca se deshabilita</b> para esperar datos: se pulsa y el formulario dice qué falta. Un botón gris no explica nada.'])
r_val = reglas([
 '<b>Cuándo:</b> al salir del campo y al enviar. Nunca mientras se escribe, salvo un límite clínico que conviene ver al momento (dosis máxima).',
 '<b>Cómo:</b> borde de error, icono y un mensaje que dice qué hacer («Máximo 100 mg al día»), nunca solo «Campo inválido».',
 '<b>Al enviar con errores:</b> un resumen arriba con el número de errores y un enlace a cada uno; el foco va al resumen. Los datos escritos se quedan.',
 '<b>Al corregir,</b> el error se va en cuanto el valor es válido.',
 '<b>Error del servidor:</b> aviso arriba del formulario, en lenguaje claro, con la acción posible («No se guardó por falta de conexión. Tus datos siguen aquí. Reintentar»).',
 '<b>Salir con cambios sin guardar</b> pide confirmación: «¿Descartar los cambios?».'])
pagina = f'''<div class="ejemplo"><form class="pform" novalidate aria-labelledby="pf-t">
 <h3 id="pf-t">Datos del paciente</h3>
 <div class="resumen" role="alert" tabindex="-1" id="pf-res"><b>{ic("alert")}Revisa 1 dato</b><a href="#pf-cel">Celular: escribe 10 dígitos</a></div>
 <fieldset class="grupo"><legend class="gt">Identificación</legend>
  {campo("Nombre completo", inp("pf-nom", "Mariana Ruiz López"), ayuda="Como aparece en la identificación.", fid="pf-nom")}
  <div class="par">{campo("Fecha de nacimiento", inp("pf-nac", "1992-03-14", tipo="date"), fid="pf-nac")}{campo("Sexo", sel("pf-sex", ["Mujer", "Hombre", "Prefiere no decir"], "Mujer"), fid="pf-sex")}</div></fieldset>
 <fieldset class="grupo"><legend class="gt">Contacto</legend>
  <div class="w-m">{campo("Celular", inp("pf-cel", "222 555 01", "e"), err="Escribe 10 dígitos", fid="pf-cel")}</div>
  {campo("Correo", inp("pf-cor", "", ph="nombre@correo.com", tipo="email"), opc=True, fid="pf-cor")}</fieldset>
 <div class="acc"><span class="sp"></span><button type="button" class="btn b3">Cancelar</button><button type="button" class="btn b1">Guardar paciente</button></div>
</form><p class="nota">Una columna, dos grupos, un par corto en dos columnas, ancho por dato, error con resumen arriba.</p></div>'''
pares = sino('<p>«Dosis diaria» arriba del campo; «mg» fijo a la derecha; «Máximo 100 mg al día» debajo si falla.</p>',
             '<p>«Dosis (mg):» a la izquierda; «Ej. 50» como única pista; «Error» en rojo sin decir qué hacer.</p>')

# ---------- 2. contenedor ----------
cont = '''<div class="tw" tabindex="0" role="region" aria-label="Qué contenedor usar"><table class="dec"><thead><tr><th scope="col">Contenedor</th><th scope="col">Cuándo</th><th scope="col">Ejemplo</th></tr></thead><tbody>
<tr><td>Diálogo de confirmación</td><td>Una decisión, sin campos. Sobre todo lo que no se deshace.</td><td>Eliminar receta, cancelar cita.</td></tr>
<tr><td>Diálogo de formulario</td><td>Tarea corta: hasta 6 campos, un solo grupo, se termina sin salir. No necesita ver lo de atrás.</td><td>Nueva cita, agregar alergia, cambiar contraseña.</td></tr>
<tr><td>Panel lateral</td><td>7 a 12 campos, o hay que seguir viendo la información de atrás mientras se llena.</td><td>Editar un medicamento viendo la receta; filtros avanzados.</td></tr>
<tr><td>Página</td><td>Más de 12 campos, varios grupos o pasos, o algo que se guarda a medias.</td><td>Registro de paciente, nota de consulta, alta de clínica.</td></tr></tbody></table></div>'''

# ---------- 3. diálogos ----------
r_dlg = reglas([
 f'<b>Anatomía:</b> cabecera (título con verbo + objeto, una línea de contexto y cerrar de 44 px), cuerpo (el formulario) y pie (acciones). Solo el cuerpo se desplaza; cabecera y pie se quedan.',
 f'<b>Anchos:</b> 400 px confirmación, 560 px formulario, 720 px formulario con un par de columnas. Radio {V["radius-2xl"]}, sombra <span class="mono">shadow-pop</span>, fondo detrás en tinta al 40 %.',
 '<b>Celular (menos de 640 px):</b> hoja que sube desde abajo, a todo el ancho y hasta el 90 % del alto; pie fijo con acciones apiladas, el principal arriba.',
 '<b>Al abrir,</b> el foco va al primer campo (en una confirmación, al botón seguro «Cancelar»). El foco no sale del diálogo hasta cerrarlo y luego vuelve al botón que lo abrió.',
 '<b>Cerrar:</b> X, «Cancelar» o Esc. Si hay cambios, primero «¿Descartar los cambios?». Un clic fuera no cierra un formulario (se perderían datos); sí cierra una confirmación.',
 '<b>Nunca un diálogo sobre otro,</b> salvo la confirmación de descartar. Si la tarea pide abrir otra cosa, es un panel o una página.',
 '<b>Al guardar:</b> el botón muestra «cargando», el diálogo se cierra al terminar y un aviso breve confirma («Cita guardada»). Si falla, el diálogo sigue abierto con el error arriba y los datos intactos.',
 '<b>Confirmación destructiva:</b> el título es la pregunta con el objeto («¿Eliminar la receta de Mariana Ruiz?»), el cuerpo dice la consecuencia, y las acciones son «Cancelar» y «Sí, eliminar» en rojo sólido. Nunca «Aceptar».'])

anat = f'''<div class="anat" aria-hidden="true">
 <div class="dlg-mock"><div class="dh"><div><b>Nueva cita</b><small>Mariana Ruiz · Expediente 0001</small></div><span class="xm">{ic("x")}</span></div>
 <div class="db"><span class="lin"></span><span class="caj"></span><span class="lin"></span><span class="caj"></span><span class="lin c"></span><span class="caj c"></span></div>
 <div class="df"><span class="pb t">Cancelar</span><span class="pb p">Guardar cita</span></div></div>
 <ol class="marcas"><li><b>Cabecera</b> 24 px de relleno · título 18/26 · contexto 14/20 · cerrar 44 px</li><li><b>Cuerpo</b> 24 px · se desplaza solo él · 12 px entre campos</li><li><b>Pie</b> borde superior <span class="mono">line</span> · acciones a la derecha · 10 px entre botones</li></ol></div>'''

dlg_form = f'''<dialog class="dlg md" id="d-cita" aria-labelledby="dc-t" aria-describedby="dc-s">
 <form method="dialog" class="dlg-in" novalidate id="f-cita">
  <header class="dh"><div><h2 id="dc-t">Nueva cita</h2><p id="dc-s">Mariana Ruiz · Expediente 0001</p></div><button type="button" class="ibtn" data-cerrar aria-label="Cerrar">{ic("x")}</button></header>
  <div class="db">
   <div class="err-srv" id="dc-err" hidden role="alert">{ic("alert")}<span>No se guardó por falta de conexión. Tus datos siguen aquí.</span></div>
   {campo("Tipo de consulta", sel("dc-tipo", ["Seguimiento", "Primera vez", "Urgencia"]), fid="dc-tipo")}
   <div class="par">{campo("Día", inp("dc-dia", "2026-11-12", tipo="date"), fid="dc-dia")}{campo("Hora", sel("dc-hora", ["09:00", "09:30", "10:00", "10:30"], "10:00"), fid="dc-hora")}</div>
   {campo("Motivo", '<textarea id="dc-mot" class="in" rows="3" placeholder="Revisión de presión arterial"></textarea>', opc=True, fid="dc-mot")}
   {sw("Enviar recordatorio al paciente", True)}
  </div>
  <footer class="df"><button type="button" class="btn b3" data-cerrar>Cancelar</button><button type="submit" class="btn b1" id="dc-ok"><span>Guardar cita</span></button></footer>
 </form></dialog>'''
dlg_conf = f'''<dialog class="dlg sm" id="d-del" aria-labelledby="dd-t" aria-describedby="dd-s">
 <form method="dialog" class="dlg-in">
  <header class="dh"><div><h2 id="dd-t">¿Eliminar la receta de Mariana Ruiz?</h2></div></header>
  <div class="db"><p id="dd-s">Se borra del expediente y la farmacia ya no podrá surtirla. No se puede deshacer.</p></div>
  <footer class="df"><button type="button" class="btn b3" data-cerrar autofocus>Cancelar</button><button type="button" class="btn b5" data-cerrar>Sí, eliminar</button></footer>
 </form></dialog>'''
dlg_desc = f'''<dialog class="dlg sm" id="d-desc" aria-labelledby="dx-t" aria-describedby="dx-s">
 <form method="dialog" class="dlg-in">
  <header class="dh"><div><h2 id="dx-t">¿Descartar los cambios?</h2></div></header>
  <div class="db"><p id="dx-s">La cita no se guardó.</p></div>
  <footer class="df"><button type="button" class="btn b3" id="dx-no" autofocus>Seguir editando</button><button type="button" class="btn b4" id="dx-si">Descartar</button></footer>
 </form></dialog>'''

movil = f'''<div class="tel" aria-hidden="true"><div class="tel-fondo"></div><div class="hoja-m">
 <span class="asa"></span><div class="dh"><div><b>Nueva cita</b><small>Mariana Ruiz</small></div><span class="xm">{ic("x")}</span></div>
 <div class="db"><span class="lin"></span><span class="caj"></span><span class="lin"></span><span class="caj"></span><span class="lin c"></span><span class="caj alto"></span></div>
 <div class="df col"><span class="pb p">Guardar cita</span><span class="pb t">Cancelar</span></div></div></div>'''

DEC = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in [
 ('Contenedor por tamaño', 'Confirmación · diálogo hasta 6 campos · panel lateral 7 a 12 · página más de 12. El panel lateral no existe todavía en el sistema: se diseña en otra ronda.'),
 ('Anchos de diálogo', '400 / 560 / 720 px.'),
 ('Hoja inferior en celular', 'El diálogo cambia de forma, no de contenido.'),
 ('Clic fuera', 'No cierra formularios; sí confirmaciones.'),
 ('Botón principal siempre activo', 'Se valida al pulsar; el resumen dice qué falta.'),
 ('Ancho máximo de formulario', '640 px en página.'),
 ('Fondo detrás del diálogo', 'Tinta #14213D al 40 %. No es un token todavía.'),
 ('Pendiente de la r01 de controles', '«(opcional)» en vez de asterisco, deshabilitado y compacto siguen sin aprobar.')])

EXTRA = f'''
.wrap{{max-width:1100px}}
.reglas{{margin:0;padding-left:30px;display:grid;gap:10px;max-width:80ch}}.reglas li{{padding-left:4px}}
.dos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:24px;align-items:start}}
.ejemplo{{display:grid;gap:10px}}
.pform{{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-2xl);padding:24px;display:grid;gap:32px;max-width:640px}}
.grupo{{display:grid;gap:12px}}.gt{{font:600 18px/26px var(--font-display);color:var(--ink);margin-bottom:4px}}
.par{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr));gap:12px 16px}}
.w-m{{max-width:260px}}
.resumen{{border:2px solid var(--error);background:var(--error-soft);border-radius:var(--radius-md);padding:12px 16px;display:grid;gap:4px;color:var(--on-error-soft)}}
.resumen b{{display:flex;gap:8px;align-items:center}}.resumen a{{color:var(--on-error-soft);margin-left:26px;min-height:24px;display:inline-flex;align-items:center;justify-self:start}}
.pform .acc,.df{{gap:10px}}
.sino{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:12px}}.sino>div{{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-lg);padding:16px;display:grid;gap:8px}}
.tag{{display:inline-flex;gap:6px;align-items:center;font:600 14px/20px var(--font-sans)}}.tag .ico{{width:16px;height:16px}}.tag.ok{{color:var(--exito)}}.tag.mal{{color:var(--error)}}
/* diálogo real */
.dlg{{border:0;padding:0;border-radius:var(--radius-2xl);box-shadow:var(--shadow-pop);background:var(--surface);color:var(--ink);width:calc(100% - 32px);max-height:min(720px,calc(100vh - 48px))}}
.dlg.md{{max-width:560px}}.dlg.sm{{max-width:400px}}.dlg::backdrop{{background:rgba(20,33,61,.4)}}
.dlg[open]{{display:flex}}.dlg-in{{display:flex;flex-direction:column;width:100%;max-height:inherit}}
.dh{{display:flex;align-items:flex-start;gap:12px;padding:20px 16px 12px 24px}}.dh>div{{flex:1;display:grid;gap:2px;padding-top:6px}}
.dh h2{{font:600 18px/26px var(--font-display)}}.dh p,.dh small{{font-size:14px;line-height:20px;color:var(--muted)}}
.db{{padding:8px 24px 24px;overflow-y:auto;display:grid;gap:12px;flex:1}}.db>p{{color:var(--ink)}}
.df{{display:flex;justify-content:flex-end;flex-wrap:wrap;padding:16px 24px;border-top:1px solid var(--line)}}
.err-srv{{display:flex;gap:8px;align-items:flex-start;background:var(--error-soft);color:var(--on-error-soft);border-radius:var(--radius-md);padding:10px 14px;font-size:14px;line-height:20px}}.err-srv .ico{{margin-top:1px}}
@media (max-width:639px){{.dlg{{width:100%;max-width:none!important;margin:auto 0 0;border-radius:var(--radius-2xl) var(--radius-2xl) 0 0;max-height:90vh}}
 .df{{flex-direction:column-reverse}}.df .btn{{width:100%}}.pform .acc{{flex-direction:column-reverse;align-items:stretch}}.pform .acc .sp{{display:none}}}}
/* maqueta de anatomía */
.anat{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:24px;align-items:center}}
.dlg-mock,.hoja-m{{background:var(--surface);border-radius:var(--radius-2xl);box-shadow:var(--shadow-pop);overflow:hidden;display:grid}}
.dlg-mock .dh,.hoja-m .dh{{outline:2px dashed var(--info);outline-offset:-6px}}.dlg-mock .db,.hoja-m .db{{outline:2px dashed var(--exito);outline-offset:-6px;padding-top:16px}}.dlg-mock .df,.hoja-m .df{{outline:2px dashed var(--aviso);outline-offset:-6px}}
.dh b{{font:600 18px/26px var(--font-display)}}.xm{{width:44px;height:44px;display:grid;place-items:center;color:var(--muted)}}
.lin{{height:10px;width:30%;border-radius:4px;background:var(--surface-pressed)}}.caj{{height:44px;border:1px solid var(--line-control);border-radius:var(--radius-md)}}.lin.c{{width:22%}}.caj.c{{width:55%}}.caj.alto{{height:72px}}
.pb{{display:inline-grid;place-items:center;height:44px;padding:0 18px;border-radius:var(--radius-md);font:600 15px/20px var(--font-sans)}}.pb.p{{background:var(--manik);color:var(--on-manik)}}.pb.t{{color:var(--manik)}}
.df.col{{flex-direction:column}}.df.col .pb{{width:100%}}
.marcas{{margin:0;padding-left:22px;display:grid;gap:12px}}.marcas li::marker{{font-weight:700}}
.marcas li:nth-child(1)::marker{{color:var(--info)}}.marcas li:nth-child(2)::marker{{color:var(--exito)}}.marcas li:nth-child(3)::marker{{color:var(--aviso)}}
.tel{{width:300px;height:560px;border:10px solid var(--ink);border-radius:40px;position:relative;overflow:hidden;background:var(--canvas);justify-self:center}}
.tel-fondo{{position:absolute;inset:0;background:rgba(20,33,61,.4)}}.hoja-m{{position:absolute;left:0;right:0;bottom:0;border-radius:24px 24px 0 0}}
.asa{{width:40px;height:4px;border-radius:2px;background:var(--line-control);justify-self:center;margin-top:8px}}
.toast{{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--ink);color:#fff;border-radius:var(--radius-md);padding:12px 18px;display:flex;gap:8px;align-items:center;font:600 15px/20px var(--font-sans);box-shadow:var(--shadow-pop)}}
.lanzar{{display:flex;flex-wrap:wrap;gap:10px}}
@media (max-width:760px){{.anat{{grid-template-columns:1fr}}}}
'''

HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Formularios Ecosistema Manik</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}{EXTRA}</style></head><body><main class="wrap">
<header class="cab"><span class="eti">Ecosistema Manik · ronda 1 · propuesta</span><h1>Formularios y diálogos</h1>
<p>Cómo se arma un formulario en cualquiera de las siete apps, y cuándo y cómo va dentro de un diálogo. Usa los controles de la <a href="https://claude.ai/artifact/RKhaYZMyrrJLETw2Q1ts2W">familia de controles r01</a>.</p></header>

<section aria-labelledby="s1"><h2 id="s1">1 · Composición del formulario</h2><div class="dos">{r_form}{pagina}</div></section>
<section aria-labelledby="s2"><h2 id="s2">2 · Etiquetas, ayudas y errores</h2>{pares}<h3>Validación</h3>{r_val}</section>
<section aria-labelledby="s3"><h2 id="s3">3 · ¿Diálogo, panel o página?</h2><p class="nota">Se decide por el tamaño de la tarea y por si hay que seguir viendo lo de atrás.</p>{cont}</section>
<section aria-labelledby="s4"><h2 id="s4">4 · Formularios en diálogos</h2>{anat}{r_dlg}
 <div class="lam"><h4>Pruébalos</h4><p class="nota">Escribe algo y pulsa Esc: pide descartar. «Guardar cita» falla la primera vez (sin conexión simulada) y guarda la segunda.</p>
 <div class="lanzar"><button type="button" class="btn b1" data-abrir="d-cita">{ic("plus")}<span>Nueva cita</span></button><button type="button" class="btn b4" data-abrir="d-del">{ic("trash")}<span>Eliminar receta</span></button></div></div>
 <div class="dos"><div class="lam"><h4>En celular · hoja inferior</h4><p class="nota">Mismo contenido; sube desde abajo, a todo el ancho y hasta el 90 % del alto. Acciones apiladas al alcance del pulgar, el principal arriba.</p></div>{movil}</div></section>
<section aria-labelledby="s5"><h2 id="s5">Decisiones de esta ronda</h2><div class="tw" tabindex="0" role="region" aria-label="Decisiones"><table class="dec"><thead><tr><th scope="col">Tema</th><th scope="col">Propuesta</th></tr></thead><tbody>{DEC}</tbody></table></div></section>
</main>
{dlg_form}{dlg_conf}{dlg_desc}
<div class="toast" id="toast" role="status" hidden>{ic("check")}<span>Cita guardada</span></div>
<script>
let origen=null,sucio=false,intentos=0;
const $=id=>document.getElementById(id),fc=$('f-cita'),dc=$('d-cita');
document.querySelectorAll('[data-abrir]').forEach(b=>b.addEventListener('click',()=>{{origen=b;const d=$(b.dataset.abrir);d.showModal();if(d===dc){{sucio=false;$('dc-tipo').focus()}}}}));
document.querySelectorAll('dialog').forEach(d=>d.addEventListener('close',()=>{{if(d!==$('d-desc')&&origen)origen.focus()}}));
fc.addEventListener('input',()=>sucio=true);
function cerrarCita(){{if(sucio){{$('d-desc').showModal()}}else dc.close()}}
dc.addEventListener('cancel',e=>{{if(sucio){{e.preventDefault();$('d-desc').showModal()}}}});
dc.querySelectorAll('[data-cerrar]').forEach(b=>b.addEventListener('click',cerrarCita));
$('dx-no').addEventListener('click',()=>{{$('d-desc').close();$('dc-tipo').focus()}});
$('dx-si').addEventListener('click',()=>{{$('d-desc').close();sucio=false;fc.reset();$('dc-err').hidden=true;dc.close()}});
$('d-del').querySelectorAll('[data-cerrar]').forEach(b=>b.addEventListener('click',()=>$('d-del').close()));
$('d-del').addEventListener('click',e=>{{if(e.target===$('d-del'))$('d-del').close()}});
fc.addEventListener('submit',e=>{{e.preventDefault();const b=$('dc-ok');if(b.getAttribute('aria-busy'))return;b.setAttribute('aria-busy','true');b.classList.add('l');
 b.innerHTML={json.dumps(ic("load", "ico gira"))}+'<span>Guardar cita</span>';
 setTimeout(()=>{{b.removeAttribute('aria-busy');b.classList.remove('l');b.innerHTML='<span>Guardar cita</span>';intentos++;
  if(intentos===1){{$('dc-err').hidden=false;$('dc-err').scrollIntoView({{block:'nearest'}})}}else{{$('dc-err').hidden=true;sucio=false;dc.close();const t=$('toast');t.hidden=false;setTimeout(()=>t.hidden=true,2600)}}}},900)}});
document.querySelectorAll('.sw:not([disabled])').forEach(s=>s.addEventListener('click',()=>{{const on=s.getAttribute('aria-checked')!=='true';s.setAttribute('aria-checked',on);sucio=true;const t=s.parentElement.querySelector('.sw-t');if(t)t.textContent=on?'Activado':'Desactivado'}}));
</script></body></html>'''
if __name__ == '__main__':  # importable sin reescribir la ronda evaluada
    open(os.path.join(D, 'formularios.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
