# SAM · plantillas de correo (2026-11-13). HTML de tablas con estilos en línea (Gmail, Outlook, Apple Mail).
# Escribe plantillas/<id>.html con variables {{...}} y muestras.json con datos ficticios para la galería.
import os, json, html as H
B = os.path.dirname(os.path.abspath(__file__)); os.makedirs(os.path.join(B, 'plantillas'), exist_ok=True)
TINTA, PAPEL, BL, LIMA, MUTED, LINEA = '#0a0a0b', '#f2f2ee', '#ffffff', '#c6f432', '#55555c', '#d6d6d0'
DANGER, WARN = '#b42318', '#8a5a00'
FONT = "Onest,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"; MONO = "'JetBrains Mono',Consolas,'Courier New',monospace"
def boton(txt, url):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:24px 0 0"><tr>'
            f'<td bgcolor="{LIMA}" style="background:{LIMA};border:2px solid {TINTA};border-radius:6px">'
            f'<a href="{url}" style="display:inline-block;padding:12px 22px;font:600 15px/20px {FONT};color:{TINTA};text-decoration:none">{txt}</a></td></tr></table>')
def chip(txt, tipo):
    st = {'activo': f'background:{LIMA};color:{TINTA};border:1.5px solid {TINTA}', 'neutro': f'color:{TINTA};border:1px solid #7a7a82',
          'peligro': f'color:{DANGER};border:1px solid {DANGER}', 'aviso': f'color:{WARN};border:1px solid {WARN}'}[tipo]
    return f'<span style="display:inline-block;{st};border-radius:999px;padding:2px 9px;font:600 12px/16px {FONT};white-space:nowrap">{txt}</span>'
def actividad(folio, titulo, chip_html, meta):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:20px 0 0;border:1px solid {LINEA};border-radius:6px"><tr><td style="padding:14px 16px">'
            f'<div style="font:500 12px/16px {MONO};color:{MUTED}">{folio}</div>'
            f'<div style="font:600 16px/22px {FONT};color:{TINTA};margin:4px 0 8px">{titulo}</div>'
            f'<div style="font:400 13px/18px {FONT};color:{MUTED}">{chip_html}&nbsp;&nbsp;{meta}</div></td></tr></table>')
def p(t, extra=''): return f'<p style="margin:0 0 12px;font:400 16px/24px {FONT};color:{TINTA}{extra}">{t}</p>'
def h1(t): return f'<h1 style="margin:0 0 16px;font:700 23px/28px {FONT};color:{TINTA}">{t}</h1>'
def nota(t): return f'<p style="margin:20px 0 0;font:400 14px/20px {FONT};color:{MUTED}">{t}</p>'
def plantilla(asunto, preheader, cuerpo, motivo):
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light">
<title>{asunto}</title></head>
<body style="margin:0;padding:0;background:{PAPEL}">
<div style="display:none;max-height:0;overflow:hidden;opacity:0">{preheader}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PAPEL}" style="background:{PAPEL}"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:560px">
<tr><td style="padding:0 4px 16px"><img src="{{{{logo_url}}}}" width="140" height="40" alt="SAM, Simple Activity Manager" style="display:block;border:0"></td></tr>
<tr><td bgcolor="{BL}" style="background:{BL};border:1px solid {LINEA};border-radius:10px;padding:28px 28px 32px">
{cuerpo}
</td></tr>
<tr><td style="padding:16px 4px 0;font:400 13px/19px {FONT};color:{MUTED}">{motivo}<br>
<a href="{{{{preferencias_url}}}}" style="color:{TINTA};text-decoration:underline">Elegir qué avisos recibo</a></td></tr>
</table></td></tr></table></body></html>
'''
ACT = actividad('{{folio}}', '{{titulo}}', '{{chip}}', '{{meta}}')
MOT_ACT = 'Recibes este correo porque participas en esta actividad en SAM.'
T = {}
T['asignacion'] = ('Te asignaron {{folio}}: {{titulo}}', '{{asignador}} te asignó esta actividad.',
  h1('Te asignaron una actividad') + p('<b>{{asignador}}</b> te asignó esta actividad. Estás a cargo de la etapa <b>{{etapa}}</b>.') + ACT + boton('Abrir actividad', '{{actividad_url}}'), MOT_ACT)
T['etapa'] = ('{{folio}} avanzó a {{etapa}}', '{{autor}} la movió de {{etapa_anterior}} a {{etapa}}.',
  h1('Una actividad avanzó de etapa') + p('<b>{{autor}}</b> movió esta actividad de <b>{{etapa_anterior}}</b> a <b>{{etapa}}</b>. Ahora te toca a ti.') + ACT + boton('Revisar actividad', '{{actividad_url}}'), MOT_ACT)
T['comentario'] = ('Comentario nuevo en {{folio}}', '{{autor}}: {{comentario_corto}}',
  h1('Comentario nuevo') + p('<b>{{autor}}</b> comentó en <span style="font-family:' + MONO + ';font-size:14px">{{folio}}</span>:') +
  f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:4px 0 0"><tr><td style="border-left:3px solid {LINEA};padding:4px 0 4px 14px;font:400 16px/24px {FONT};color:{TINTA}">{{{{comentario}}}}</td></tr></table>' +
  ACT + boton('Responder', '{{actividad_url}}'), MOT_ACT)
T['por-vencer'] = ('{{folio}} vence {{vence_corto}}', 'Te queda poco tiempo para cerrar esta actividad.',
  h1('Una actividad está por vencer') + p('Esta actividad vence <b>{{vence_largo}}</b> y sigue en <b>{{etapa}}</b>. Si necesitas más tiempo, cambia la fecha desde la actividad.') + ACT + boton('Abrir actividad', '{{actividad_url}}'), MOT_ACT)
T['vencida'] = ('{{folio}} venció {{vencio_corto}}', 'La actividad sigue abierta después de su fecha.',
  h1('Una actividad venció') + p('Esta actividad venció <b>{{vencio_largo}}</b> y sigue abierta en <b>{{etapa}}</b>. Ciérrala, reasígnala o cambia su fecha.') + ACT + boton('Abrir actividad', '{{actividad_url}}'), MOT_ACT)
# Reporte de atrasos: misma plantilla, tres periodos
def reporte_cuerpo():
    cifra = lambda n, et: (f'<td width="33%" style="padding:12px 8px;border:1px solid {LINEA};border-radius:6px" valign="top">'
                          f'<div style="font:700 26px/30px {FONT};color:{TINTA}">{n}</div><div style="font:400 13px/18px {FONT};color:{MUTED}">{et}</div></td>')
    return (h1('{{titulo_reporte}}') + p('{{resumen}}') +
      f'<table role="presentation" width="100%" cellpadding="0" cellspacing="6" border="0" style="margin:8px -6px 0"><tr>{cifra("{{n_atrasadas}}", "actividades atrasadas")}{cifra("{{n_nuevas}}", "{{etiqueta_nuevas}}")}{cifra("{{n_personas}}", "personas con atrasos")}</tr></table>' +
      f'<h2 style="margin:24px 0 8px;font:600 18px/24px {FONT};color:{TINTA}">Las más atrasadas</h2>' +
      f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse">'
      f'<tr><th align="left" style="padding:8px 8px 8px 0;border-bottom:1px solid {LINEA};font:600 12px/16px {FONT};color:{MUTED}">Actividad</th>'
      f'<th align="left" style="padding:8px;border-bottom:1px solid {LINEA};font:600 12px/16px {FONT};color:{MUTED}">Responsable</th>'
      f'<th align="right" style="padding:8px 0 8px 8px;border-bottom:1px solid {LINEA};font:600 12px/16px {FONT};color:{MUTED}">Atraso</th></tr>'
      '{{filas}}</table>' + boton('Ver todos los atrasos', '{{reporte_url}}'))
def fila(folio, titulo, resp, dias):
    return (f'<tr><td style="padding:10px 8px 10px 0;border-bottom:1px solid {LINEA}" valign="top"><div style="font:500 12px/16px {MONO};color:{MUTED}">{folio}</div>'
            f'<div style="font:600 14px/20px {FONT};color:{TINTA}">{titulo}</div></td>'
            f'<td style="padding:10px 8px;border-bottom:1px solid {LINEA};font:400 14px/20px {FONT};color:{TINTA}" valign="top">{resp}</td>'
            f'<td align="right" style="padding:10px 0 10px 8px;border-bottom:1px solid {LINEA};font:600 14px/20px {FONT};color:{DANGER};white-space:nowrap" valign="top">{dias}</td></tr>')
T['reporte'] = ('{{titulo_reporte}}', '{{resumen}}', reporte_cuerpo(), 'Recibes este reporte por tu rol en SAM ({{rol}}).')
T['invitacion'] = ('Te invitaron a SAM', '{{invitador}} te dio acceso a SAM. Crea tu contraseña para entrar.',
  h1('Te invitaron a SAM') + p('<b>{{invitador}}</b> te dio acceso a SAM, la herramienta del equipo para registrar, mover y cerrar actividades.') +
  p('Tu usuario es <b>{{correo}}</b>. Crea tu contraseña para entrar.') + boton('Crear mi contraseña', '{{enlace}}') +
  nota('El enlace vence en {{vigencia}}. Si no esperabas esta invitación, ignora este correo.'), 'Recibes este correo porque alguien de tu equipo te invitó a SAM.')
T['recuperar'] = ('Restablece tu contraseña de SAM', 'Usa este enlace para crear una contraseña nueva.',
  h1('Restablece tu contraseña') + p('Recibimos una solicitud para cambiar la contraseña de <b>{{correo}}</b>. Usa este botón para crear una nueva.') +
  boton('Crear contraseña nueva', '{{enlace}}') + nota('El enlace vence en {{vigencia}} y solo funciona una vez. Si no lo pediste, ignora este correo: tu contraseña no cambia.'),
  'Recibes este correo porque se pidió restablecer la contraseña de tu cuenta de SAM.')
for k, (a, pre, c, m) in T.items():
    open(os.path.join(B, 'plantillas', f'{k}.html'), 'w').write(plantilla(a, pre, c, m))
# Muestras con datos ficticios
base = {'actividad_url': '#', 'preferencias_url': '#'}
ACTS = {'folio': 'INC-2041', 'titulo': 'El reporte diario de atrasos no llegó a Discord'}
FILAS = ''.join(fila(*x) for x in [('INC-2033', 'Ticket de WhatsApp sin evidencia adjunta', 'Óscar Ruiz', '12 días'),
  ('TAR-0179', 'Actualizar plantilla de alta de proveedores', 'Laura Méndez', '8 días'), ('INC-2036', 'Error al adjuntar PDF mayores de 10 MB', 'Daniela Ortiz', '5 días'),
  ('TAR-0184', 'Documentar el flujo de cierre de incidencias para el equipo de soporte técnico nocturno', 'Óscar Ruiz', '3 días')])
REP = {'filas': FILAS, 'reporte_url': '#'}
M = [
 ('asignacion', 'Avisos de actividad', 'Te asignaron una actividad', {**ACTS, 'asignador': 'Laura Méndez', 'etapa': 'En curso', 'chip': chip('En curso', 'activo'), 'meta': 'Vence hoy, 18:00'}),
 ('etapa', 'Avisos de actividad', 'Avanzó de etapa', {**ACTS, 'autor': 'Óscar Ruiz', 'etapa_anterior': 'En curso', 'etapa': 'Revisión', 'chip': chip('Revisión', 'neutro'), 'meta': 'Vence hoy, 18:00'}),
 ('comentario', 'Avisos de actividad', 'Comentario nuevo', {**ACTS, 'autor': 'Daniela Ortiz', 'comentario': 'Ya revisé el webhook: el token de Discord había expirado. Lo renové y dejé el log en la evidencia. ¿Puedes confirmar que hoy sí llegó el reporte?', 'comentario_corto': 'Ya revisé el webhook: el token de Discord había expirado…', 'chip': chip('En curso', 'activo'), 'meta': 'Vence hoy, 18:00'}),
 ('por-vencer', 'Avisos de actividad', 'Por vencer', {**ACTS, 'vence_corto': 'hoy a las 18:00', 'vence_largo': 'hoy a las 18:00', 'etapa': 'En curso', 'chip': chip('Por vencer', 'aviso'), 'meta': 'Vence hoy, 18:00'}),
 ('vencida', 'Avisos de actividad', 'Vencida', {'folio': 'INC-2033', 'titulo': 'Ticket de WhatsApp sin evidencia adjunta', 'vencio_corto': 'hace 3 días', 'vencio_largo': 'el 10 de noviembre', 'etapa': 'Nuevo', 'chip': chip('Vencida', 'peligro'), 'meta': 'Venció 10 nov'}),
 ('reporte', 'Reportes de atrasos', 'Reporte diario (OR)', {**REP, 'titulo_reporte': 'Atrasos del día · 13 nov 2026', 'resumen': 'Hoy hay 7 actividades atrasadas, 2 más que ayer.', 'n_atrasadas': '7', 'n_nuevas': '2', 'etiqueta_nuevas': 'se atrasaron hoy', 'n_personas': '4', 'rol': 'reporte diario de atrasos'}),
 ('reporte', 'Reportes de atrasos', 'Reporte semanal (WR)', {**REP, 'titulo_reporte': 'Atrasos de la semana · 9 al 13 nov 2026', 'resumen': 'Cerraron la semana 7 actividades atrasadas, 3 menos que la semana anterior.', 'n_atrasadas': '7', 'n_nuevas': '5', 'etiqueta_nuevas': 'se atrasaron esta semana', 'n_personas': '4', 'rol': 'reporte semanal de atrasos'}),
 ('reporte', 'Reportes de atrasos', 'Reporte mensual (MR)', {**REP, 'titulo_reporte': 'Atrasos de octubre 2026', 'resumen': 'Octubre cerró con 11 actividades atrasadas; se atrasaron 23 a lo largo del mes.', 'n_atrasadas': '11', 'n_nuevas': '23', 'etiqueta_nuevas': 'se atrasaron en el mes', 'n_personas': '6', 'rol': 'reporte mensual de atrasos'}),
 ('invitacion', 'Acceso a la cuenta', 'Invitación', {'invitador': 'Laura Méndez', 'correo': 'daniela.ortiz@ejemplo.com', 'enlace': '#', 'vigencia': '72 horas'}),
 ('recuperar', 'Acceso a la cuenta', 'Recuperar contraseña', {'correo': 'daniela.ortiz@ejemplo.com', 'enlace': '#', 'vigencia': '1 hora'}),
]
out = []
for k, grupo, nombre, d in M:
    s = open(os.path.join(B, 'plantillas', f'{k}.html')).read(); vars_ = {**base, **d}
    asunto = T[k][0]
    for kk, vv in vars_.items(): s = s.replace('{{' + kk + '}}', vv); asunto = asunto.replace('{{' + kk + '}}', vv)
    s = s.replace('{{logo_url}}', 'LOGO')
    falt = [x for x in __import__('re').findall(r'\{\{(\w+)\}\}', s)]
    assert not falt, (k, falt)
    out.append({'id': k, 'grupo': grupo, 'nombre': nombre, 'asunto': asunto, 'html': s})
json.dump(out, open(os.path.join(B, 'muestras.json'), 'w'), ensure_ascii=False)
print('ok', len(T), 'plantillas,', len(out), 'muestras')
