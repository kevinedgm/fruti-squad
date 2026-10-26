# Correos del ecosistema MedicalManik. Uso: python3 gen.py
# Escribe plantillas/<id>.html (con variables {{...}} para el servicio de envío), plantillas/<id>.txt,
# manifiesto.json (asunto, preheader y variables de cada correo) y vista.html (todas con datos de ejemplo).
# Reglas de correo: tablas de maquetación, estilos en línea, ancho máximo 600 px, letra con respaldo Arial,
# botones hechos con tablas, texto alternativo en imágenes y texto previo (preheader) oculto.
import base64, json, os, re, html

H = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(H, 'plantillas'), exist_ok=True)

# --- tokens (tema.json de final/ y manik-final/) ---
AZUL, TINTA, MUTED, LINEA, FONDO = '#234899', '#14213D', '#4A5674', '#E1E6F0', '#F3F5F9'
IMPULSA, MANIK_UI, OK, AVISO, ERROR, ESTRELLA = '#504CA1', '#00788A', '#15814B', '#A75F00', '#C33F4E', '#E3A21C'
TIT = "'Sora',Arial,Helvetica,sans-serif"
TXT = "'Atkinson Hyperlegible Next',Arial,Helvetica,sans-serif"
FUENTES = 'https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:wght@400;700&family=Sora:wght@600&display=swap'

MARCAS = {  # cabecera: imagen, ancho, alto, texto alternativo, nombre visible, color del producto
    'ecosistema': ('medicalmanik-128.png', 36, 36, 'MedicalManik', 'MedicalManik', AZUL),
    'expediente': ('expediente-128.png', 36, 36, 'Expediente Manik', 'Expediente Manik', AZUL),
    'impulsa': ('impulsa-128.png', 36, 36, 'Impulsa Manik', 'Impulsa Manik', IMPULSA),
    'manik': ('manik-logotipo.png', 110, 25, 'Manik', None, MANIK_UI),
}

# --- piezas ---
def h1(t): return f'<h1 style="margin:0 0 12px;font-family:{TIT};font-size:26px;line-height:1.25;font-weight:600;color:{TINTA}">{t}</h1>'
def h2(t): return f'<h2 style="margin:28px 0 10px;font-family:{TIT};font-size:18px;line-height:1.3;font-weight:600;color:{TINTA}">{t}</h2>'
def p(t, color=TINTA, size=16, mb=14): return f'<p style="margin:0 0 {mb}px;font-family:{TXT};font-size:{size}px;line-height:1.55;color:{color}">{t}</p>'
def small(t): return p(t, MUTED, 14)
def boton(texto, url, color):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:22px 0 8px"><tr>'
            f'<td bgcolor="{color}" style="border-radius:10px;background:{color}">'
            f'<a href="{url}" style="display:inline-block;padding:14px 26px;font-family:{TXT};font-size:16px;font-weight:700;color:#FFFFFF;text-decoration:none;border-radius:10px">{texto}</a>'
            f'</td></tr></table>')
def enlace(texto, url, color=AZUL): return f'<a href="{url}" style="color:{color};font-weight:700;text-decoration:underline">{texto}</a>'
def recibo(filas, total=None):
    r = ''.join(f'<tr><td style="padding:10px 0;border-bottom:1px solid {LINEA};font-family:{TXT};font-size:15px;color:{MUTED}">{k}</td>'
                f'<td align="right" style="padding:10px 0;border-bottom:1px solid {LINEA};font-family:{TXT};font-size:15px;color:{TINTA}">{v}</td></tr>' for k, v in filas)
    if total:
        r += (f'<tr><td style="padding:14px 0 4px;font-family:{TXT};font-size:16px;font-weight:700;color:{TINTA}">{total[0]}</td>'
              f'<td align="right" style="padding:14px 0 4px;font-family:{TIT};font-size:20px;font-weight:600;color:{TINTA}">{total[1]}</td></tr>')
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:8px 0 6px">{r}</table>'
def caja(contenido, fondo='#F6F8FC', borde=LINEA):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:16px 0"><tr>'
            f'<td style="padding:16px 18px;background:{fondo};border:1px solid {borde};border-radius:12px">{contenido}</td></tr></table>')
def pasos(items):
    r = ''.join(f'<tr><td valign="top" width="40" style="padding:8px 0"><div style="width:28px;height:28px;line-height:28px;border-radius:14px;background:#E8EEF8;color:{AZUL};text-align:center;font-family:{TIT};font-size:14px;font-weight:600">{i}</div></td>'
                f'<td style="padding:8px 0;font-family:{TXT};font-size:16px;line-height:1.5;color:{TINTA}"><b>{t}</b><br><span style="color:{MUTED};font-size:15px">{d}</span></td></tr>'
                for i, (t, d) in enumerate(items, 1))
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:6px 0">{r}</table>'
def vinetas(items, color=AZUL):
    r = ''.join(f'<tr><td valign="top" width="22" style="padding:5px 0;font-family:{TXT};font-size:16px;color:{color}">&#10003;</td>'
                f'<td style="padding:5px 0;font-family:{TXT};font-size:16px;line-height:1.5;color:{TINTA}">{t}</td></tr>' for t in items)
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:4px 0 8px">{r}</table>'
def cifras(items):  # 2 por fila: (etiqueta, valor, comparación)
    filas = ''
    for i in range(0, len(items), 2):
        celdas = ''
        for et, val, comp in items[i:i + 2]:
            celdas += (f'<td width="50%" valign="top" style="padding:6px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
                       f'<td style="padding:16px;background:#F6F8FC;border:1px solid {LINEA};border-radius:12px">'
                       f'<div style="font-family:{TXT};font-size:14px;color:{MUTED}">{et}</div>'
                       f'<div style="font-family:{TIT};font-size:30px;line-height:1.2;font-weight:600;color:{TINTA};margin:4px 0">{val}</div>'
                       f'<div style="font-family:{TXT};font-size:14px;color:{MUTED}">{comp}</div></td></tr></table></td>')
        filas += f'<tr>{celdas}</tr>'
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:6px -6px">{filas}</table>'
def barras(datos, color=AZUL):  # ancho de cada barra = variable en % (el sistema la calcula: valor / máximo de la semana)
    r = ''
    for dia, var, ancho in datos:
        r += (f'<tr><td width="44" style="padding:5px 8px 5px 0;font-family:{TXT};font-size:14px;color:{MUTED}">{dia}</td>'
              f'<td style="padding:5px 0"><table role="presentation" width="{ancho}%" cellpadding="0" cellspacing="0" border="0"><tr>'
              f'<td height="18" bgcolor="{color}" style="height:18px;background:{color};border-radius:4px;font-size:0;line-height:0">&nbsp;</td></tr></table></td>'
              f'<td width="36" align="right" style="padding:5px 0 5px 8px;font-family:{TXT};font-size:14px;font-weight:700;color:{TINTA}">{var}</td></tr>')
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:4px 0 6px">{r}</table>'
def codigo(c):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:18px 0"><tr>'
            f'<td style="padding:14px 22px;background:#F6F8FC;border:1px dashed {AZUL};border-radius:12px;font-family:{TIT};font-size:32px;letter-spacing:8px;font-weight:600;color:{TINTA}">{c}</td></tr></table>')
def cita(texto, autor):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:14px 0"><tr>'
            f'<td style="padding:4px 0 4px 16px;border-left:3px solid {ESTRELLA}">'
            f'<p style="margin:0 0 6px;font-family:{TXT};font-size:17px;line-height:1.5;font-style:italic;color:{TINTA}">«{texto}»</p>'
            f'<p style="margin:0;font-family:{TXT};font-size:14px;color:{MUTED}">{autor}</p></td></tr></table>')

def layout(marca, preheader, cuerpo, pie_extra='', titulo='MedicalManik'):
    img, w, hgt, alt, nombre, color = MARCAS[marca]
    nombre_html = (f'<td style="padding-left:10px;font-family:{TIT};font-size:17px;font-weight:600;color:{TINTA}">{nombre}</td>' if nombre else '')
    empresa = 'Manik es parte de MedicalManik.' if marca == 'manik' else 'MedicalManik, el ecosistema digital para su consultorio.'
    dudas = '¿Dudas? Escríbenos a' if marca == 'manik' else '¿Dudas? Escríbanos a'  # pacientes: de tú; médicos: de usted
    return f'''<!doctype html>
<html lang="es" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>{titulo}</title>
<link href="{FUENTES}" rel="stylesheet">
<style>body{{margin:0;padding:0;-webkit-text-size-adjust:100%}}table{{border-collapse:collapse}}img{{border:0;display:block}}a{{color:{AZUL}}}
@media (max-width:620px){{.px{{padding-left:20px!important;padding-right:20px!important}}}}</style>
</head>
<body style="margin:0;padding:0;background:{FONDO}">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:{FONDO}">{preheader}&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{FONDO}" style="background:{FONDO}"><tr><td align="center" style="padding:28px 12px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;background:#FFFFFF;border-radius:16px;overflow:hidden">
<tr><td height="4" bgcolor="{color}" style="height:4px;background:{color};font-size:0;line-height:0">&nbsp;</td></tr>
<tr><td class="px" style="padding:24px 36px 8px"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
<td><img src="{{{{assets_url}}}}/{img}" width="{w}" height="{hgt}" alt="{alt}" style="display:block;width:{w}px;height:{hgt}px"></td>{nombre_html}</tr></table></td></tr>
<tr><td class="px" style="padding:20px 36px 32px">{cuerpo}</td></tr>
<tr><td class="px" style="padding:20px 36px 28px;border-top:1px solid {LINEA}">
<p style="margin:0 0 6px;font-family:{TXT};font-size:13px;line-height:1.5;color:{MUTED}">{empresa} {dudas} <a href="mailto:{{{{soporte_correo}}}}" style="color:{MUTED}">{{{{soporte_correo}}}}</a>.</p>
{pie_extra}<p style="margin:0;font-family:{TXT};font-size:13px;line-height:1.5;color:{MUTED}">{{{{empresa_direccion}}}}</p>
</td></tr></table></td></tr></table>
</body></html>'''

def baja(texto): return f'<p style="margin:0 0 6px;font-family:{TXT};font-size:13px;line-height:1.5;color:{MUTED}">{texto} <a href="{{{{baja_url}}}}" style="color:{MUTED}">Dejar de recibirlo</a>.</p>'
def motivo(texto): return f'<p style="margin:0 0 6px;font-family:{TXT};font-size:13px;line-height:1.5;color:{MUTED}">{texto}</p>'

# --- correos ---
C = []
def correo(id, grupo, nombre, marca, asunto, preheader, cuerpo, pie='', cuando=''):
    C.append(dict(id=id, grupo=grupo, nombre=nombre, marca=marca, asunto=asunto, preheader=preheader, cuando=cuando,
                  html=layout(marca, preheader, cuerpo, pie, asunto)))

correo('bienvenida', 'Cuenta', 'Bienvenida al registrarse', 'ecosistema',
  'Le damos la bienvenida a MedicalManik, {{tratamiento}} {{apellido}}',
  'Su cuenta está lista. Tres pasos para empezar a recibir pacientes.',
  h1('Le damos la bienvenida, {{tratamiento}} {{apellido}}') +
  p('Su cuenta está lista. Con estos tres pasos su consultorio queda funcionando y los pacientes pueden encontrarlo en Manik.') +
  pasos([('Complete su perfil profesional', 'Cédula, especialidad, foto y dirección del consultorio.'),
         ('Configure su agenda', 'Días, horarios y duración de cada consulta.'),
         ('Publique su perfil en Manik', 'Así los pacientes pueden verlo y agendar en línea.')]) +
  boton('Entrar a MedicalManik', '{{app_url}}', AZUL) +
  small('Su usuario es {{correo}}. Si necesita ayuda para configurar su cuenta, responda a este correo y le acompañamos paso a paso.'),
  motivo('Recibe este correo porque creó una cuenta en MedicalManik.'), 'Al terminar el registro.')

correo('confirmar-correo', 'Cuenta', 'Confirmar correo', 'ecosistema',
  'Su código de confirmación: {{codigo}}',
  'Escriba este código en MedicalManik para confirmar su correo.',
  h1('Confirme su correo') + p('Escriba este código en la pantalla de registro de MedicalManik:') + codigo('{{codigo}}') +
  small('El código vence en {{minutos_vigencia}} minutos. Si usted no se registró en MedicalManik, ignore este correo; nadie podrá usar su dirección sin el código.'),
  motivo('Recibe este correo porque alguien escribió esta dirección al registrarse.'), 'Al crear la cuenta o al cambiar de correo.')

correo('restablecer-contrasena', 'Cuenta', 'Restablecer contraseña', 'ecosistema',
  'Restablezca su contraseña de MedicalManik',
  'El enlace funciona durante {{minutos_vigencia}} minutos.',
  h1('Restablezca su contraseña') + p('Recibimos una solicitud para cambiar la contraseña de {{correo}}.') +
  boton('Crear nueva contraseña', '{{restablecer_url}}', AZUL) +
  small('El enlace funciona durante {{minutos_vigencia}} minutos y solo una vez.') +
  caja(p('<b>¿No lo solicitó usted?</b> Ignore este correo: su contraseña actual sigue funcionando. Si recibe varios de estos correos sin haberlos pedido, avísenos.', TINTA, 15, 0)),
  motivo('Solicitud hecha el {{fecha_solicitud}} desde {{dispositivo}}.'), 'Cuando el usuario pide cambiar su contraseña.')

correo('plan-activado', 'Pagos', 'Compra de plan (Plan Pro)', 'ecosistema',
  'Su Plan {{plan}} está activo',
  'Pago recibido por {{total}}. Esto es lo que puede hacer ahora.',
  h1('Su Plan {{plan}} está activo') + p('Gracias, {{tratamiento}} {{apellido}}. Recibimos su pago y su plan ya está funcionando.') +
  recibo([('Plan', '{{plan}} · {{periodo}}'), ('Subtotal', '{{subtotal}}'), ('IVA 16%', '{{iva}}'), ('Método de pago', '{{metodo_pago}}'),
          ('Próximo cobro', '{{proximo_cobro}}')], ('Total pagado', '{{total}}')) +
  h2('Lo que incluye su plan') + vinetas(['{{beneficio_1}}', '{{beneficio_2}}', '{{beneficio_3}}', '{{beneficio_4}}']) +
  boton('Ir a mi cuenta', '{{app_url}}', AZUL) +
  small('Si necesita factura, pídala desde Mi cuenta › Facturación. Le llegará en otro correo con el PDF y el XML.'),
  motivo('Recibe este correo porque se hizo un pago en su cuenta de MedicalManik.'), 'Al confirmarse el pago de un plan o un cambio de plan.')

correo('creditos-impulsa', 'Pagos', 'Compra de créditos Impulsa', 'impulsa',
  'Sus {{creditos}} créditos de Impulsa están listos',
  'Saldo actual: {{saldo_creditos}} créditos. Ya puede lanzar su campaña.',
  h1('Sus créditos están listos') + p('Compró <b>{{creditos}} créditos</b> de Impulsa. Ya puede usarlos en sus campañas de prevención.') +
  caja(f'<div style="font-family:{TXT};font-size:14px;color:{MUTED}">Saldo disponible</div>'
       f'<div style="font-family:{TIT};font-size:34px;line-height:1.2;font-weight:600;color:{IMPULSA}">{{{{saldo_creditos}}}} créditos</div>'
       f'<div style="font-family:{TXT};font-size:15px;color:{TINTA}">Alcanza para enviar unos {{{{alcance_estimado}}}} mensajes.</div>', '#F1F0FA', '#D9D7EF') +
  recibo([('Paquete', '{{paquete}}'), ('Créditos', '{{creditos}}'), ('Subtotal', '{{subtotal}}'), ('IVA 16%', '{{iva}}'), ('Método de pago', '{{metodo_pago}}')],
         ('Total pagado', '{{total}}')) +
  boton('Crear una campaña', '{{impulsa_url}}', IMPULSA) +
  small('Los créditos no vencen mientras su cuenta esté activa. Si una campaña no se envía, los créditos regresan a su saldo.'),
  motivo('Recibe este correo porque se hizo una compra en Impulsa Manik.'), 'Al confirmarse el pago de créditos.')

correo('renovacion-proxima', 'Pagos', 'Aviso de renovación', 'ecosistema',
  'Su Plan {{plan}} se renueva el {{proximo_cobro}}',
  'Cobraremos {{total}} a {{metodo_pago}}. No tiene que hacer nada.',
  h1('Su plan se renueva en 7 días') + p('El <b>{{proximo_cobro}}</b> renovaremos su Plan {{plan}}. No tiene que hacer nada si quiere seguir igual.') +
  recibo([('Plan', '{{plan}} · {{periodo}}'), ('Se cobrará a', '{{metodo_pago}}'), ('Fecha', '{{proximo_cobro}}')], ('Monto', '{{total}}')) +
  boton('Revisar mi plan', '{{plan_url}}', AZUL) +
  small('Puede cambiar de plan o de tarjeta antes de esa fecha desde Mi cuenta › Plan y pagos.'),
  motivo('Recibe este aviso porque tiene un plan con renovación automática.'), '7 días antes de cada renovación.')

correo('pago-fallido', 'Pagos', 'Pago no procesado', 'ecosistema',
  'No pudimos cobrar su Plan {{plan}}',
  'Actualice su método de pago antes del {{fecha_limite}} para no perder acceso.',
  h1('No pudimos cobrar su plan') +
  caja(p(f'<b style="color:{ERROR}">Pago rechazado:</b> {{{{motivo_rechazo}}}}', TINTA, 15, 0), '#FBEEF0', '#F0C9CF') +
  p('Intentamos cobrar <b>{{total}}</b> a {{metodo_pago}} para renovar su Plan {{plan}}.') +
  p('Su cuenta sigue funcionando normalmente hasta el <b>{{fecha_limite}}</b>. Volveremos a intentar el cobro el {{fecha_reintento}}.') +
  boton('Actualizar método de pago', '{{pago_url}}', AZUL) +
  small('Después del {{fecha_limite}} su cuenta pasa al plan gratuito: sus expedientes y citas se conservan, pero algunas funciones se desactivan.'),
  motivo('Recibe este correo porque falló el cobro de su plan.'), 'Cuando el banco rechaza un cobro de renovación.')

correo('factura', 'Pagos', 'Factura disponible (CFDI)', 'ecosistema',
  'Factura {{folio}} de MedicalManik',
  'Adjuntamos el PDF y el XML de su factura por {{total}}.',
  h1('Su factura está lista') + p('Adjuntamos su factura en PDF y XML.') +
  recibo([('Folio', '{{folio}}'), ('RFC receptor', '{{rfc}}'), ('Concepto', '{{concepto}}'), ('Fecha', '{{fecha_factura}}'), ('Uso de CFDI', '{{uso_cfdi}}')],
         ('Total', '{{total}}')) +
  boton('Descargar factura', '{{factura_url}}', AZUL) +
  small('Si algún dato fiscal es incorrecto, responda a este correo antes de fin de mes para corregirla.'),
  motivo('Recibe este correo porque pidió factura de un pago en MedicalManik.'), 'Al timbrarse una factura solicitada.')

correo('resumen-semanal', 'Actividad', 'Estadísticas de la semana', 'expediente',
  'Su semana: {{citas_atendidas}} consultas y {{pacientes_nuevos}} pacientes nuevos',
  'Resumen del {{semana}}: citas, pacientes nuevos, visitas a su perfil y opiniones.',
  h1('Su semana en el consultorio') + p('Resumen del <b>{{semana}}</b>, comparado con la semana anterior.', MUTED) +
  cifras([('Consultas atendidas', '{{citas_atendidas}}', '{{citas_cambio}} vs. semana anterior'),
          ('Pacientes nuevos', '{{pacientes_nuevos}}', '{{pacientes_cambio}} vs. semana anterior'),
          ('Visitas a su perfil en Manik', '{{visitas_perfil}}', '{{visitas_cambio}} vs. semana anterior'),
          ('Opiniones nuevas', '{{opiniones_nuevas}}', 'Promedio {{promedio_opiniones}} de 5')]) +
  h2('Consultas por día') + barras([(d, '{{citas_%s}}' % k, '{{barra_%s}}' % k) for d, k in
                                   [('Lun', 'lun'), ('Mar', 'mar'), ('Mié', 'mie'), ('Jue', 'jue'), ('Vie', 'vie'), ('Sáb', 'sab')]]) +
  small('Su día con más consultas fue el {{dia_mas_ocupado}}. {{faltas}} pacientes no llegaron a su cita.') +
  h2('Lo que dijo un paciente') + cita('{{opinion_destacada}}', '{{opinion_autor}}') +
  caja(p('<b>Esta semana:</b> tiene {{citas_proxima_semana}} citas agendadas y {{espacios_libres}} espacios libres.', TINTA, 15, 0)) +
  boton('Ver estadísticas completas', '{{estadisticas_url}}', AZUL),
  baja('Recibe este resumen cada lunes.'), 'Cada lunes a las 7:00, con los datos de la semana anterior.')

correo('nueva-opinion', 'Actividad', 'Nueva opinión de paciente', 'ecosistema',
  'Un paciente opinó sobre su consulta',
  '{{calificacion}} de 5: «{{opinion_inicio}}»',
  h1('Tiene una opinión nueva') + p('Un paciente que atendió el {{fecha_consulta}} calificó su consulta en Manik.') +
  p(f'<span style="color:{ESTRELLA};font-size:20px;letter-spacing:2px">&#9733;&#9733;&#9733;&#9733;&#9733;</span> <b>{{{{calificacion}}}} de 5</b>') +
  cita('{{opinion}}', '{{opinion_autor}}') +
  p('Responder las opiniones, aunque sea con una línea, ayuda a que otros pacientes confíen en usted.') +
  boton('Responder opinión', '{{opinion_url}}', AZUL),
  baja('Le avisamos de cada opinión nueva.'), 'Cuando un paciente publica una opinión en Manik.')

correo('cita-confirmada', 'Pacientes', 'Cita confirmada (paciente, Manik)', 'manik',
  'Tu cita con {{medico}} está confirmada',
  '{{fecha_cita}} a las {{hora_cita}} en {{consultorio}}.',
  h1('Tu cita está confirmada') + p('Te esperan el <b>{{fecha_cita}} a las {{hora_cita}}</b>.') +
  caja(f'<div style="font-family:{TIT};font-size:18px;font-weight:600;color:{TINTA}">{{{{medico}}}}</div>'
       f'<div style="font-family:{TXT};font-size:15px;color:{MUTED};margin-bottom:10px">{{{{especialidad}}}}</div>'
       + recibo([('Cuándo', '{{fecha_cita}}, {{hora_cita}}'), ('Dónde', '{{consultorio}}<br>{{direccion}}'), ('Consulta', '{{precio}} · pagas en el consultorio')])) +
  boton('Agregar a mi calendario', '{{calendario_url}}', MANIK_UI) +
  p(f'{enlace("Cómo llegar", "{{mapa_url}}", MANIK_UI)} &nbsp;·&nbsp; {enlace("Cambiar o cancelar", "{{gestionar_url}}", MANIK_UI)}', TINTA, 15) +
  small('Te mandamos un recordatorio un día antes. Si no puedes ir, cancela con tiempo para que otra persona use ese espacio.'),
  motivo('Recibes este correo porque agendaste una cita en Manik.'), 'Al agendar una cita en el directorio.')

# --- datos de ejemplo para la vista ---
EJ = dict(assets_url='img', soporte_correo='ayuda@medicalmanik.com', empresa_direccion='MedicalManik · Puebla, México (dirección de ejemplo)',
  baja_url='#', app_url='#', tratamiento='Dra.', apellido='Soto', correo='mariana.soto@ejemplo.com', codigo='482 913', minutos_vigencia='15',
  restablecer_url='#', fecha_solicitud='26 de octubre de 2026, 22:14', dispositivo='Chrome en Windows',
  plan='Pro', periodo='mensual', subtotal='$1,034.48', iva='$165.52', total='$1,200.00', metodo_pago='Visa terminación 4821', proximo_cobro='26 de noviembre de 2026',
  beneficio_1='Agendas ilimitadas para todos sus consultorios', beneficio_2='Receta electrónica con su firma', beneficio_3='Perfil destacado en el directorio Manik',
  beneficio_4='Soporte prioritario por WhatsApp',
  creditos='500', saldo_creditos='650', alcance_estimado='650', paquete='Paquete 500', impulsa_url='#',
  plan_url='#', pago_url='#', motivo_rechazo='la tarjeta no tiene fondos suficientes.', fecha_limite='2 de noviembre de 2026', fecha_reintento='29 de octubre',
  folio='MM-2026-004812', rfc='SOAM850312AB1', concepto='Plan Pro mensual', fecha_factura='26 de octubre de 2026', uso_cfdi='G03 Gastos en general', factura_url='#',
  semana='19 al 25 de octubre', citas_atendidas='42', citas_cambio='&#9650; 8 más', pacientes_nuevos='9', pacientes_cambio='&#9650; 3 más',
  visitas_perfil='318', visitas_cambio='&#9660; 12 menos', opiniones_nuevas='5', promedio_opiniones='4.9',
  citas_lun='7', citas_mar='6', citas_mie='8', citas_jue='11', citas_vie='7', citas_sab='3',
  barra_lun='64', barra_mar='55', barra_mie='73', barra_jue='100', barra_vie='64', barra_sab='27', dia_mas_ocupado='jueves', faltas='2',
  opinion_destacada='Me explicó todo sin prisa y el tratamiento sí funcionó.', opinion_autor='Paciente, 23 de octubre',
  citas_proxima_semana='37', espacios_libres='11', estadisticas_url='#',
  calificacion='5', opinion_inicio='Me explicó todo sin prisa…', fecha_consulta='23 de octubre', opinion='Me explicó todo sin prisa y el tratamiento sí funcionó. Muy puntual.',
  opinion_url='#', medico='Dra. Mariana Soto', especialidad='Dermatóloga', fecha_cita='jueves 30 de octubre', hora_cita='16:30',
  consultorio='Torre Médica Atlixcáyotl, piso 6', direccion='Blvd. Atlixcáyotl 2501, Puebla', precio='$900', calendario_url='#', mapa_url='#', gestionar_url='#')

def variables(s): return sorted(set(re.findall(r'\{\{(\w+)\}\}', s)))
def rellenar(s, imgs=None):
    def f(m):
        k = m.group(1)
        return EJ.get(k, m.group(0))
    s = re.sub(r'\{\{(\w+)\}\}', f, s)
    if imgs:
        s = re.sub(r'src="img/([\w.-]+)"', lambda m: f'src="{imgs[m.group(1)]}"', s)
    return s
def texto_plano(h):
    t = re.sub(r'(?is)<head.*?</head>', '', h)
    t = re.sub(r'(?is)<div style="display:none.*?</div>', '', t)
    t = re.sub(r'(?i)<a href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f'{m.group(2)} ({m.group(1)})' if m.group(1).startswith('{{') else m.group(2), t)
    t = re.sub(r'(?i)<br\s*/?>|</(p|h1|h2|tr|div)>', '\n', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    t = '\n'.join(re.sub(r'[ \t ͏]+', ' ', l).strip() for l in t.splitlines())
    return re.sub(r'\n{3,}', '\n\n', t).strip() + '\n'

man = []
for c in C:
    open(os.path.join(H, 'plantillas', c['id'] + '.html'), 'w').write(c['html'])
    open(os.path.join(H, 'plantillas', c['id'] + '.txt'), 'w').write(f"{c['asunto']}\n\n" + texto_plano(c['html']))
    man.append(dict(id=c['id'], grupo=c['grupo'], nombre=c['nombre'], marca=c['marca'], asunto=c['asunto'], preheader=c['preheader'],
                    cuando=c['cuando'], variables=variables(c['asunto'] + c['preheader'] + c['html'])))
json.dump(dict(fuente='correos/gen.py', variables_globales=['assets_url', 'soporte_correo', 'empresa_direccion'], correos=man),
          open(os.path.join(H, 'manifiesto.json'), 'w'), ensure_ascii=False, indent=1)

# --- vista con datos de ejemplo ---
imgs = {f: 'data:image/png;base64,' + base64.b64encode(open(os.path.join(H, 'img', f), 'rb').read()).decode() for f in os.listdir(os.path.join(H, 'img'))}
def cuerpo_de(h): return re.search(r'(?is)<body[^>]*>(.*)</body>', h).group(1)
grupos = []
for c in C:
    if c['grupo'] not in grupos: grupos.append(c['grupo'])
nav = ''.join(f'<li class="g">{g}</li>' + ''.join(f'<li><a href="#{c["id"]}">{c["nombre"]}</a></li>' for c in C if c['grupo'] == g) for g in grupos)
tarjetas = ''
for c, m in zip(C, man):
    de = 'Manik &lt;hola@manik.mx&gt;' if c['marca'] == 'manik' else 'MedicalManik &lt;hola@medicalmanik.com&gt;'
    vs = ''.join(f'<code>{v}</code>' for v in m['variables'])
    tarjetas += f'''<section class="mail" id="{c['id']}" aria-labelledby="t-{c['id']}">
<header class="meta"><p class="grp">{c['grupo']} · {c['cuando']}</p><h2 id="t-{c['id']}">{c['nombre']}</h2>
<dl><dt>De</dt><dd>{de}</dd><dt>Asunto</dt><dd><b>{rellenar(c['asunto'])}</b></dd><dt>Texto previo</dt><dd>{rellenar(c['preheader'])}</dd></dl>
<details><summary>{len(m['variables'])} variables</summary><div class="vars">{vs}</div></details></header>
<div class="screen"><div class="mailbody">{rellenar(cuerpo_de(c['html']), imgs)}</div></div></section>'''
open(os.path.join(H, 'vista.html'), 'w').write(open(os.path.join(H, 'vista-plantilla.html')).read()
     .replace('{{NAV}}', nav).replace('{{CORREOS}}', tarjetas).replace('{{N}}', str(len(C))).replace('{{FUENTES}}', FUENTES))
print(len(C), 'correos')
