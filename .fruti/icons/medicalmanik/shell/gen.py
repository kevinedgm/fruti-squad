# Ecosistema Manik · shell de cada app (navbar, sidebar, footer). Uso: python3 gen.py → shell.html (página publicable)
import json
SV = '/home/user/fruti-squad/.fruti/icons/medicalmanik/final/svg/'
sello = {k: open(SV + k + '.svg').read() for k in ['expediente', 'agenda', 'compras', 'farmacia', 'impulsa', 'grupos', 'ecosistema']}
# Navegación propuesta por app (supuestos a confirmar con cada equipo). Densidad → patrón:
#   ≤3 destinos: pestañas en la barra, sin sidebar · 4–7: sidebar plano · 8 o más: sidebar por grupos, plegable a riel
APPS = {
 'expediente': {'n': 'Expediente', 'cta': 'Nueva consulta', 'busca': 'Buscar paciente por nombre, CURP o expediente', 'patron': 'grupos',
   'nav': [('Atención', [('home', 'Hoy', 6), ('users', 'Pacientes', 0), ('steth', 'Consultas', 0), ('clock', 'Lista de espera', 3)]),
           ('Clínico', [('pill', 'Recetas', 0), ('flask', 'Órdenes de estudios', 0), ('chart', 'Resultados', 2), ('syringe', 'Vacunas', 0)]),
           ('Documentos', [('file', 'Consentimientos', 0), ('award', 'Certificados', 0), ('layout', 'Plantillas', 0)]),
           ('Análisis', [('bars', 'Reportes', 0)])], 'activo': 'Hoy'},
 'agenda': {'n': 'Agenda', 'cta': 'Nueva cita', 'busca': 'Buscar paciente o cita', 'patron': 'plano',
   'nav': [('', [('home', 'Hoy', 0), ('cal', 'Calendario', 0), ('door', 'Sala de espera', 4), ('users', 'Pacientes', 0), ('bell', 'Recordatorios', 0)])], 'activo': 'Hoy'},
 'compras': {'n': 'Compras', 'cta': 'Nueva orden', 'busca': 'Buscar folio, UUID, RFC o proveedor', 'patron': 'grupos',
   'nav': [('Compras', [('cart', 'Requisiciones', 5), ('clip', 'Órdenes de compra', 0), ('truck', 'Recepción', 2), ('store', 'Proveedores', 0)]),
           ('Facturación electrónica', [('receipt', 'Facturas emitidas', 0), ('inbox', 'Facturas recibidas', 0), ('coins', 'Complementos de pago', 0), ('ban', 'Cancelaciones', 1)]),
           ('Finanzas', [('wallet', 'Cuentas por pagar', 0), ('bars', 'Reportes', 0)])], 'activo': 'Facturas emitidas'},
 'farmacia': {'n': 'Farmacia', 'cta': 'Surtir receta', 'busca': 'Buscar producto, receta o lote', 'patron': 'plano',
   'nav': [('', [('pill', 'Recetas por surtir', 8), ('pos', 'Punto de venta', 0), ('box', 'Inventario', 0), ('in', 'Entradas', 0), ('hourglass', 'Lotes y caducidades', 3), ('bars', 'Reportes', 0)])], 'activo': 'Recetas por surtir'},
 'impulsa': {'n': 'Impulsa', 'cta': 'Nueva campaña', 'busca': '', 'patron': 'pestanas',
   'nav': [('', [('bars', 'Resultados', 0), ('plus', 'Nueva campaña', 0)])], 'activo': 'Resultados'},
 'grupos': {'n': 'Grupos', 'cta': 'Invitar usuario', 'busca': 'Buscar clínica o usuario', 'patron': 'plano',
   'nav': [('', [('building', 'Clínicas y sucursales', 0), ('users', 'Usuarios', 0), ('shield', 'Roles y permisos', 0), ('grid', 'Apps y licencias', 0), ('sliders', 'Configuración del grupo', 0), ('list', 'Bitácora de auditoría', 0)])], 'activo': 'Clínicas y sucursales'},
}
ICON = {  # Lucide (ISC), trazo 2
 'home': '<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/>', 'users': '<circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M17 3.5a4 4 0 0 1 0 9M22 21a7 7 0 0 0-4-6.3"/>',
 'steth': '<path d="M5 3v6a5 5 0 0 0 10 0V3M10 14v2a5 5 0 0 0 10 0v-3"/><circle cx="20" cy="11" r="2"/>', 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'pill': '<path d="m10.5 20.5 10-10a5 5 0 1 0-7-7l-10 10a5 5 0 1 0 7 7zM8.5 8.5l7 7"/>', 'flask': '<path d="M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2h12.4a1.5 1.5 0 0 0 1.3-2L14 9V3M7 15h10"/>',
 'chart': '<path d="M3 3v18h18M7 15l4-4 3 3 5-6"/>', 'syringe': '<path d="m18 2 4 4M17 7l3-3M19 9 8.5 19.5 4.5 15.5 15 5zM9 11l4 4M5 19l-3 3M14 4l6 6"/>',
 'file': '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>', 'award': '<circle cx="12" cy="8" r="6"/><path d="M8.5 13 7 22l5-3 5 3-1.5-9"/>',
 'layout': '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>', 'bars': '<path d="M3 3v18h18"/><path d="M8 17v-5M13 17V8M18 17v-9"/>',
 'cal': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>', 'door': '<path d="M13 4h3a2 2 0 0 1 2 2v14M2 20h3M13 20h9M10 12v.01M13 4.6v16.8a.6.6 0 0 1-.7.6L5 20V5.6a1 1 0 0 1 .8-1l6.4-1.6a.6.6 0 0 1 .8.6z"/>',
 'bell': '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10 21h4"/>', 'cart': '<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2 2h3l2.7 12.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/>',
 'clip': '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2M9 12h6M9 16h6"/>', 'truck': '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2M15 18H9M19 18h2a1 1 0 0 0 1-1v-3.6a1 1 0 0 0-.2-.6l-3.5-4.4A1 1 0 0 0 17.5 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
 'store': '<path d="M3 9 4.5 4h15L21 9M3 9v11h18V9M3 9h18M9 20v-6h6v6"/>', 'receipt': '<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1zM8 8h8M8 12h8M8 16h5"/>',
 'inbox': '<path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.5 5.1 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.5-6.9A2 2 0 0 0 16.8 4H7.2a2 2 0 0 0-1.7 1.1z"/>', 'coins': '<circle cx="8" cy="8" r="6"/><path d="M18.1 10.4A6 6 0 1 1 10.3 18M7 6h1v4M16.7 13.9l.7.7-2.8 2.8"/>',
 'ban': '<circle cx="12" cy="12" r="9"/><path d="m5.6 5.6 12.8 12.8"/>', 'wallet': '<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>',
 'pos': '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 10h8M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h.01M16 18h.01"/>', 'box': '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
 'in': '<path d="M12 3v12M7 10l5 5 5-5M5 21h14"/>', 'hourglass': '<path d="M5 22h14M5 2h14M17 22v-4.2a2 2 0 0 0-.6-1.4L12 12l-4.4 4.4a2 2 0 0 0-.6 1.4V22M7 2v4.2a2 2 0 0 0 .6 1.4L12 12l4.4-4.4a2 2 0 0 0 .6-1.4V2"/>',
 'plus': '<path d="M12 5v14M5 12h14"/>', 'building': '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
 'shield': '<path d="M20 13c0 5-3.5 7.5-7.7 9a1 1 0 0 1-.6 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1.2 1.2 0 0 1 1.6 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1z"/>',
 'grid': '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
 'sliders': '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M2 14h4M10 8h4M18 16h4"/>', 'list': '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
 'search': '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>', 'menu': '<path d="M4 6h16M4 12h16M4 18h16"/>', 'chev': '<path d="m6 9 6 6 6-6"/>', 'help': '<circle cx="12" cy="12" r="9"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>',
 'gear': '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 0 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 0 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 0 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 0 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
 'panel': '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18"/>', 'ok': '<path d="M5 12.5l4.5 4.5L19 7.5"/>', 'warn': '<path d="M12 3.5l9.5 16.5h-19z"/><path d="M12 10v4M12 17h.01"/>', 'x': '<circle cx="12" cy="12" r="9"/><path d="M15 9l-6 6M9 9l6 6"/>',
}
PAGE = open('plantilla.html').read()
PAGE = PAGE.replace('/*DATA*/', 'const APPS=' + json.dumps(APPS, ensure_ascii=False) + ';const ICON=' + json.dumps(ICON) + ';const SELLO=' + json.dumps(sello) + ';')
open('shell.html', 'w').write(PAGE)
print('ok', len(PAGE))
