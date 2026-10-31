# Convia · perfil de negocio: HOTEL (r1). Pedido del usuario 2026-10-31: perfil completo tipo red social (portada, galería,
# información, habitaciones con precios, amenidades, rasgos, horarios, contacto para reservar, ubicación, «volverían», cronología).
# Hotel FICTICIO («Ejemplo»): fotos de relleno desenfocadas (no son de este hotel), contactos y dirección ficticios.
# Uso: python3 gen.py <carpeta de salida con img/>. Las fotos no se guardan en el repo.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
sys.path.insert(0, F)
import rasgos as RG, amenidades as AM
T = json.load(open(os.path.join(F, 'tema.json'))); H = T['categorias']['hoteles']
N = dict(perla='#f9f9f7', sup='#ffffff', tinta='#1b1d1a', sec='#5c5f5b', linea='#e6e6e2', foto='#ececea', cantera='#2f5a45', suave='#e3ece6',
         hfondo=H['fondo'], htexto=H['texto'])
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls): s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
logo = raw('svg/logotipo.svg').replace('<svg ', '<svg class="logo" ', 1)
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
ICO_H = clean(raw('iconos/hoteles.svg'), 'ico')
HOTEL = dict(
 n='Hotel Patio de Luz', zona='Centro, Oaxaca', desde='$2,480',
 d='Casona del siglo XIX restaurada, con nueve habitaciones alrededor de un patio de cantera. Desayuno oaxaqueño en la terraza y alberca templada al fondo del jardín.',
 v=33, w=28, fav=.42, ras=['accesible', 'ingles'],
 datos=[('Desde', '$2,480 por noche'), ('Habitaciones', '9'), ('Llegada', 'desde 15:00'), ('Salida', 'hasta 12:00'), ('Recepción', 'abierta 24 h'), ('Idiomas', 'español e inglés')],
 amen=['alberca', 'desayuno', 'wifi', 'recepcion', 'terraza', 'aire', ('traslado', 'con costo')],
 no=[('estacionamiento', 'Sin estacionamiento propio; hay pensión a dos calles')],
 cuartos=[
  dict(n='Habitación Patio', cap='2 personas', cama='Cama queen', m2='22 m²', extra=['Vista al patio', 'Regadera'], p='$2,480', fotos=['12.jpg', '13.jpg', '03.jpg']),
  dict(n='Doble Jardín', cap='Hasta 4 personas', cama='2 camas matrimoniales', m2='30 m²', extra=['Salida al jardín', 'Ideal familias'], p='$3,100', fotos=['11.jpg', '13.jpg', '07.jpg']),
  dict(n='Suite Cantera', cap='2 adultos y 1 niño', cama='Cama king', m2='40 m²', extra=['Tina', 'Sala', 'Terraza privada'], p='$3,600', fotos=['13.jpg', '12.jpg', '11.jpg', '03.jpg']),
 ],
 galeria=[('12.jpg', 'Patio central'), ('11.jpg', 'Alberca y jardín de noche'), ('13.jpg', 'Sala del patio'), ('03.jpg', 'Comedor del desayuno'),
          ('07.jpg', 'Terraza'), ('02.jpg', 'Fachada y calle'), ('13.jpg', 'Pasillo de arcos'), ('11.jpg', 'Habitaciones al jardín')],
 contacto=[('whatsapp', 'WhatsApp para reservar', '951 000 0000'), ('tel', 'Teléfono', '951 000 0001'), ('mail', 'Correo', 'reservas@ejemplo.com'),
           ('web', 'Sitio web', 'ejemplo.com'), ('ig', 'Instagram', '@hotel.ejemplo')],
 dir='Calle Ejemplo 000, Centro, Oaxaca de Juárez',
 posts=[('2026-10-15', '15 oct 2026', 'Abrimos la terraza para cenas de jueves a sábado, de 19:00 a 22:00. También para quien no se hospeda.', '11.jpg', 'Terraza iluminada de noche'),
        ('2026-09-02', '2 sep 2026', 'Desayuno de temporada: chocolate de agua, pan de yema y fruta del mercado.', '03.jpg', 'Mesa de desayuno'),
        ('2026-07-01', '1 jul 2026', 'Para Guelaguetza quedan pocas fechas. Escríbenos con tiempo por WhatsApp.', '', '')],
)
RAS = {k: dict(n=n, crit=c, ico=RG.svg(k, cls='ico')) for k, (n, c, _) in RG.RASGOS.items()}
AMS = {k: dict(n=n, ico=AM.svg(k, cls='ico')) for k, n in AM.NOMBRES.items()}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const H=' + json.dumps(HOTEL, ensure_ascii=False) + ';const RAS=' + json.dumps(RAS, ensure_ascii=False) + ';const AMS=' + json.dumps(AMS, ensure_ascii=False) + ';const ICO_H=' + json.dumps(ICO_H) + ';')
        .replace('<!--LOGO-->', logo).replace('%STAR%', STAR))
for k, v in N.items(): html = html.replace('%' + k + '%', v)
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
