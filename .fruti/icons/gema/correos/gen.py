# GEMA · plantillas de correo a clientes y proveedores (2026-11-17). Remitente: el laboratorio Nisa Nabani (decisión del usuario).
# GEMA no aparece ante el cliente. Estilo de GEMA: navy, Onest. Logo del laboratorio y datos de contacto: variables (no se inventan).
# Sin enlaces a portal (el portal de clientes se retira, ADR-011): los documentos van como PDF adjunto.
import os, json, re
B = os.path.dirname(os.path.abspath(__file__)); os.makedirs(os.path.join(B, 'plantillas'), exist_ok=True)
TINTA, PAPEL, BL, NAVY, AZUL, MUTED, LINEA, DANGER = '#0a0a0b', '#f2f2ee', '#ffffff', '#052A76', '#3D67AE', '#55555c', '#d6d6d0', '#b42318'
FONT = "Onest,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"; MONO = "'JetBrains Mono',Consolas,'Courier New',monospace"
def h1(t): return f'<h1 style="margin:0 0 16px;font:700 23px/28px {FONT};color:{TINTA}">{t}</h1>'
def p(t): return f'<p style="margin:0 0 12px;font:400 16px/24px {FONT};color:{TINTA}">{t}</p>'
def nota(t): return f'<p style="margin:20px 0 0;font:400 14px/20px {FONT};color:{MUTED}">{t}</p>'
def adjunto(nombre, peso):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:20px 0 0;border:1px solid {LINEA};border-radius:6px"><tr>'
            f'<td width="44" style="padding:12px 0 12px 14px" valign="middle"><div style="width:32px;height:40px;border-radius:4px;background:{NAVY};color:{BL};font:700 10px/40px {FONT};text-align:center">PDF</div></td>'
            f'<td style="padding:12px 14px" valign="middle"><div style="font:600 15px/20px {FONT};color:{TINTA}">{nombre}</div><div style="font:400 13px/18px {FONT};color:{MUTED}">Adjunto · {peso}</div></td></tr></table>')
def datos(pares):
    filas = ''.join(f'<tr><td style="padding:6px 12px 6px 0;font:400 14px/20px {FONT};color:{MUTED};white-space:nowrap" valign="top">{k}</td><td style="padding:6px 0;font:600 14px/20px {FONT};color:{TINTA}">{v}</td></tr>' for k, v in pares)
    return f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:8px 0 0">{filas}</table>'
def tabla(cab, filas_var, total_var=None):
    th = ''.join(f'<th align="{a}" style="padding:8px {8 if i < len(cab)-1 else 0}px 8px {0 if i == 0 else 8}px;border-bottom:1px solid {LINEA};font:600 12px/16px {FONT};color:{MUTED}">{c}</th>' for i, (c, a) in enumerate(cab))
    tot = (f'{{{{{total_var}}}}}' if total_var else '')
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:16px 0 0;border-collapse:collapse"><tr>{th}</tr>{{{{{filas_var}}}}}{tot}</table>'
def plantilla(asunto, pre, cuerpo, motivo):
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>{asunto}</title></head>
<body style="margin:0;padding:0;background:{PAPEL}">
<div style="display:none;max-height:0;overflow:hidden;opacity:0">{pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PAPEL}" style="background:{PAPEL}"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px">
<tr><td style="padding:0 4px 16px">{{{{encabezado}}}}</td></tr>
<tr><td bgcolor="{NAVY}" style="background:{NAVY};background-image:linear-gradient(90deg,{NAVY},{AZUL});height:4px;line-height:4px;font-size:0;border-radius:10px 10px 0 0">&nbsp;</td></tr>
<tr><td bgcolor="{BL}" style="background:{BL};border:1px solid {LINEA};border-top:0;border-radius:0 0 10px 10px;padding:28px 28px 32px">
{cuerpo}
<p style="margin:24px 0 0;font:400 15px/22px {FONT};color:{TINTA}">{{{{firma}}}}</p>
</td></tr>
<tr><td style="padding:16px 4px 0;font:400 13px/19px {FONT};color:{MUTED}">{motivo}<br>{{{{pie_contacto}}}}</td></tr>
</table></td></tr></table></body></html>
'''
T = {}
T['informe-resultados'] = ('Informe de resultados · Orden {{orden}}', 'Adjuntamos el informe de resultados de las muestras de la orden {{orden}}.',
  h1('Tu informe de resultados está listo') + p('Hola, {{contacto}}. Adjuntamos el informe de resultados de la orden <b>{{orden}}</b>, recibida el {{fecha_recepcion}}.') +
  tabla([('Muestra', 'left'), ('Tipo', 'left'), ('Análisis', 'right')], 'filas') + adjunto('{{archivo}}', '{{peso}}') +
  nota('El informe firmado es el documento válido. Si tienes dudas sobre algún resultado, responde este correo e indica el folio de la muestra.'),
  'Recibes este correo porque solicitaste análisis a nuestro laboratorio.')
T['estado-cuenta'] = ('Estado de cuenta al {{fecha_corte}}', 'Tu saldo al {{fecha_corte}} es de {{saldo}}.',
  h1('Tu estado de cuenta') + p('Hola, {{contacto}}. Este es el estado de cuenta de <b>{{cliente}}</b> al {{fecha_corte}}.') +
  datos([('Saldo pendiente', '{{saldo}}'), ('Vencido', '{{vencido}}')]) +
  tabla([('Factura', 'left'), ('Vence', 'left'), ('Importe', 'right')], 'filas', 'total') + adjunto('{{archivo}}', '{{peso}}') +
  nota('Si ya realizaste el pago, ignora este aviso o envíanos el comprobante respondiendo este correo. Datos para pago: {{datos_pago}}.'),
  'Recibes este correo porque eres cliente de nuestro laboratorio.')
T['cotizacion'] = ('Cotización {{folio}} · {{servicio}}', 'Adjuntamos la cotización {{folio}}, vigente hasta el {{vigencia}}.',
  h1('Tu cotización') + p('Hola, {{contacto}}. Gracias por tu solicitud. Adjuntamos la cotización <b>{{folio}}</b> para {{servicio}}.') +
  datos([('Vigencia', 'Hasta el {{vigencia}}'), ('Tiempo de entrega', '{{tiempo_entrega}}')]) +
  tabla([('Análisis', 'left'), ('Cant.', 'right'), ('Importe', 'right')], 'filas', 'total') + adjunto('{{archivo}}', '{{peso}}') +
  nota('Para aceptarla, responde este correo con la cotización firmada o con tu orden de compra. Los precios no incluyen muestreo salvo que se indique.'),
  'Recibes este correo porque solicitaste una cotización a nuestro laboratorio.')
T['orden-compra'] = ('Orden de compra {{folio}}', 'Orden de compra {{folio}} para entrega el {{fecha_entrega}} en {{sucursal}}.',
  h1('Orden de compra') + p('Hola, {{contacto}}. Te enviamos la orden de compra <b>{{folio}}</b> de {{laboratorio}}.') +
  datos([('Entrega', '{{fecha_entrega}}'), ('Lugar', '{{sucursal}}'), ('Condiciones de pago', '{{condiciones}}')]) +
  tabla([('Producto', 'left'), ('Cant.', 'right'), ('Importe', 'right')], 'filas', 'total') + adjunto('{{archivo}}', '{{peso}}') +
  nota('Por favor confirma la recepción y la fecha de entrega respondiendo este correo. Incluye el número de orden en tu factura.'),
  'Recibes este correo porque eres proveedor de nuestro laboratorio.')
for k, (a, pre, c, m) in T.items(): open(os.path.join(B, 'plantillas', f'{k}.html'), 'w').write(plantilla(a, pre, c, m))
# Fragmentos que arma el código
def fila(celdas, alin):
    tds = ''
    for i, (txt, a) in enumerate(zip(celdas, alin)):
        pad = f'10px {8 if i < len(celdas)-1 else 0}px 10px {0 if i == 0 else 8}px'
        tds += f'<td align="{a}" valign="top" style="padding:{pad};border-bottom:1px solid {LINEA};font:400 14px/20px {FONT};color:{TINTA}">{txt}</td>'
    return f'<tr>{tds}</tr>'
def folio(f, n): return f'<div style="font:500 12px/16px {MONO};color:{MUTED}">{f}</div><div style="font:600 14px/20px {FONT};color:{TINTA}">{n}</div>'
def total(etq, v): return f'<tr><td colspan="2" align="right" style="padding:12px 8px 0 0;font:600 14px/20px {FONT};color:{TINTA}">{etq}</td><td align="right" style="padding:12px 0 0 8px;font:700 16px/22px {MONO};color:{TINTA};white-space:nowrap">{v}</td></tr>'
def num(v): return f'<span style="font-family:{MONO};white-space:nowrap">{v}</span>'
ENC = (f'<div style="font:700 20px/24px {FONT};color:{NAVY};letter-spacing:.02em">NISA NABANI</div>'
       f'<div style="font:500 12px/16px {FONT};color:{MUTED}">Laboratorio de ensayos · [aquí va el logotipo oficial: {{{{logo_url}}}}]</div>')
FIRMA = 'Atentamente,<br><b>[Nombre de quien envía]</b><br>[Área] · Nisa Nabani'
PIE = '[Dirección de la sucursal] · [Teléfono] · [Correo de contacto]'
base = {'encabezado': ENC, 'firma': FIRMA, 'pie_contacto': PIE, 'contacto': 'Mariana Torres', 'peso': '412 KB'}
M = [
 ('informe-resultados', 'A clientes', 'Informe de resultados', {'orden': 'OT-2026-0457', 'fecha_recepcion': '12 nov 2026', 'archivo': 'Informe OT-2026-0457.pdf',
   'filas': fila([folio('M-2026-1184', 'Agua residual · planta norte'), 'Aguas', num('3')], ['left', 'left', 'right']) + fila([folio('M-2026-1185', 'Agua de proceso · línea 2'), 'Aguas', num('5')], ['left', 'left', 'right'])}),
 ('estado-cuenta', 'A clientes', 'Estado de cuenta', {'cliente': 'Purificadora del Valle (ficticia)', 'fecha_corte': '15 nov 2026', 'saldo': num('$18,792.00'), 'vencido': num('$4,060.00'), 'archivo': 'Estado de cuenta 15-nov-2026.pdf', 'datos_pago': '[banco, cuenta y referencia]',
   'filas': fila([folio('F-2026-2210', 'Análisis de aguas, octubre'), '20 oct 2026 · <span style="color:' + DANGER + ';font-weight:600">✕ Vencida</span>', num('$4,060.00')], ['left', 'left', 'right']) + fila([folio('F-2026-2344', 'Análisis de aguas, noviembre'), '10 dic 2026', num('$14,732.00')], ['left', 'left', 'right']),
   'total': total('Saldo', '$18,792.00')}),
 ('cotizacion', 'A clientes', 'Cotización', {'folio': 'COT-2026-0912', 'servicio': 'análisis de mezcal (NOM-070)', 'vigencia': '17 dic 2026', 'tiempo_entrega': '5 días hábiles', 'archivo': 'Cotización COT-2026-0912.pdf',
   'filas': fila([folio('ALC-01', 'Metanol'), num('4'), num('$2,320.00')], ['left', 'right', 'right']) + fila([folio('ALC-03', 'Grado alcohólico'), num('4'), num('$1,160.00')], ['left', 'right', 'right']) + fila([folio('ALC-07', 'Alcoholes superiores'), num('4'), num('$3,480.00')], ['left', 'right', 'right']),
   'total': total('Subtotal', '$6,960.00') + total('IVA 16 %', '$1,113.60') + total('Total', '$8,073.60')}),
 ('orden-compra', 'A proveedores', 'Orden de compra', {'folio': 'OC-2026-0318', 'laboratorio': 'Nisa Nabani', 'fecha_entrega': '24 nov 2026', 'sucursal': 'sucursal Oaxaca', 'condiciones': 'Crédito a 30 días', 'archivo': 'Orden de compra OC-2026-0318.pdf', 'contacto': 'Jorge Aguilar',
   'filas': fila([folio('RE-0142', 'Ácido sulfúrico grado reactivo, 2.5 L'), num('2'), num('$2,980.00')], ['left', 'right', 'right']) + fila([folio('MA-0087', 'Viales de vidrio ámbar 40 mL, caja 72'), num('3'), num('$4,215.00')], ['left', 'right', 'right']),
   'total': total('Subtotal', '$7,195.00') + total('IVA 16 %', '$1,151.20') + total('Total', '$8,346.20')}),
]
out = []
for k, g, nombre, d in M:
    s = open(os.path.join(B, 'plantillas', f'{k}.html')).read(); v = {**base, **d}; asunto = T[k][0]
    for kk, vv in v.items(): s = s.replace('{{' + kk + '}}', vv); asunto = asunto.replace('{{' + kk + '}}', re.sub('<[^>]+>', '', vv))
    s = s.replace('{{logo_url}}', 'logo_url')
    falt = re.findall(r'\{\{(\w+)\}\}', s); assert not falt, (k, falt)
    out.append({'id': k, 'grupo': g, 'nombre': nombre, 'asunto': asunto, 'html': s})
json.dump(out, open(os.path.join(B, 'muestras.json'), 'w'), ensure_ascii=False); print('ok', len(T), 'plantillas')
