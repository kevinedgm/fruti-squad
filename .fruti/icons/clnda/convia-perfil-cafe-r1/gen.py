# Convia · perfil de negocio: CAFÉ (r1). Patrón aprobado (hotel r2) con el color de cafés; reutiliza la carta y el modo QR del restaurante r1.
# Lo propio del café: se va sin reservar (acción principal = «Cómo llegar»), bloque «¿Sirve para trabajar?», pestaña de encuentros
# (networking, catación…) y origen del café en la carta. Es «Recién llegado» (6 visitas): muestra ese estado en un perfil.
# Café FICTICIO («Ejemplo», el mismo «Tostadora Norte» del directorio): fotos de relleno; carta, precios, wifi y contactos inventados.
# Pluma Hidalgo y Sierra Mazateca son zonas cafetaleras reales de Oaxaca; las notas de cata son inventadas.
# Uso: python3 gen.py <carpeta de salida con img/>. Las fotos no se guardan en el repo.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
sys.path.insert(0, F)
import rasgos as RG, amenidades as AM
G = 'cafes'
T = json.load(open(os.path.join(F, 'tema.json'))); K = T['categorias'][G]
# punto de cafés (#eda100) da 1.99:1 sobre papel: la métrica usa el color de texto del giro.
N = dict(perla='#f9f9f7', sup='#ffffff', tinta='#1b1d1a', sec='#5c5f5b', linea='#e6e6e2', foto='#ececea', gtexto=K['texto'], gfondo=K['fondo'], gpunto=K['texto'], gdk='#6b4800')
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls): s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
logo = raw(f'sellos/{G}-logotipo-giro.svg').replace('<svg ', '<svg class="logo" ', 1)
LOGO_BASE = raw('svg/logotipo.svg').replace('<svg ', '<svg class="logo" ', 1)
SELLO = clean(raw(f'sellos/{G}-sello.svg'), 'sello-h')
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
ICO_G = clean(raw(f'iconos/{G}.svg'), 'ico')
v = lambda es, en, des, den, p, *f, o='': dict(es=es, en=en, des=des, den=den, p=p, veg='veg' in f, pic=False, dest='dest' in f, reg='', o=o)
C = dict(
 n='Tostadora Norte', kick='Café · Reforma', v=6, w=5, fav=0, ras=[['trabajar', ''], ['networking', 'jue 9:00']],
 d='Café de especialidad que abrió en septiembre. Tostamos aquí los martes: el tostador se ve desde la barra. Dos mesas largas compartidas y una barra a la ventana.',
 hor={'0': ['9:00', '15:00'], '1': None, '2': ['9:00', '19:00'], '3': ['9:00', '19:00'], '4': ['8:00', '19:00'], '5': ['9:00', '19:00'], '6': ['9:00', '19:00']},
 ancla=('Americano', 45), wifi='45 Mb',
 trabajo=[('wifi', 'Wifi', 'Probado en la revisión: 45 Mbps'), ('enchufe', 'Enchufes', 'En 8 de 12 lugares'), ('ruido', 'Ruido', 'Tranquilo en la mañana; más animado después de las 17:00'),
          ('reloj', 'Quedarte', 'Sin presión para volver a consumir')],
 origenes=[('Pluma Hidalgo', 'Lavado · chocolate y naranja'), ('Sierra Mazateca', 'Natural · frutos rojos')],
 encuentros=[dict(dia='Jueves', h='9:00', n='Desayuno de freelancers', tipo='Networking', ras='networking', d='Llega con tu laptop; cada quien se presenta en un minuto. Gratis, consumo aparte.', cada='Cada semana'),
             dict(dia='Sábado 7 nov', h='11:00', n='Catación abierta', tipo='Taller corto', ras='', d='Probamos tres cafés de Oaxaca y cómo cambian según el método. $120, cupo de 8.', cada='Una vez al mes')],
 actualizado='25 oct 2026',
 menu=[
  dict(id='espresso', es='Espresso y con leche', en='Espresso & milk', items=[
   v('Espresso', 'Espresso', 'Doble, de la mezcla de la casa.', 'Double shot, house blend.', 40),
   v('Americano', 'Americano', 'Espresso alargado con agua.', 'Espresso lengthened with water.', 45, 'veg'),
   v('Capuchino', 'Cappuccino', 'Leche entera o de avena (+$10).', 'Whole or oat milk (+$10).', 55, 'dest'),
   v('Latte de avena', 'Oat latte', 'Con leche de avena de la casa.', 'With house-made oat milk.', 65, 'veg')]),
  dict(id='filtrados', es='Filtrados', en='Brewed', items=[
   v('V60 · Pluma Hidalgo', 'V60 · Pluma Hidalgo', 'Lavado; notas a chocolate y naranja.', 'Washed; chocolate and orange notes.', 65, 'veg', 'dest', o='Pluma Hidalgo'),
   v('Chemex para dos · Sierra Mazateca', 'Chemex for two · Sierra Mazateca', 'Natural; notas a frutos rojos.', 'Natural; red fruit notes.', 120, 'veg', o='Sierra Mazateca'),
   v('Cold brew', 'Cold brew', 'Infusión en frío de 18 horas.', '18-hour cold infusion.', 60, 'veg')]),
  dict(id='otras', es='Otras bebidas', en='Other drinks', items=[
   v('Café de olla', 'Café de olla', 'Con canela y piloncillo.', 'With cinnamon and piloncillo.', 40, 'veg'),
   v('Chocolate de agua', 'Hot chocolate with water', 'Chocolate de metate.', 'Stone-ground chocolate.', 50, 'veg'),
   v('Tisana de hierbas', 'Herbal tea', 'Hierbabuena, cedrón y limón.', 'Mint, lemon verbena and lemon.', 40, 'veg')]),
  dict(id='comer', es='Pan y algo de comer', en='Bread & bites', items=[
   v('Pan de yema', 'Egg-yolk bread', 'De panadería del barrio.', 'From a neighborhood bakery.', 25),
   v('Concha de café', 'Coffee concha', 'Hecha con nuestro café.', 'Made with our coffee.', 30, 'dest'),
   v('Tostada de aguacate', 'Avocado toast', 'Pan de masa madre, aguacate y semillas.', 'Sourdough, avocado and seeds.', 95, 'veg'),
   v('Molletes', 'Molletes', 'Frijol, quesillo y pico de gallo.', 'Beans, Oaxaca cheese and pico de gallo.', 85)])],
 galeria=[('07.jpg', 'Barra y patio', 'lugar'), ('03.jpg', 'Mesas compartidas', 'lugar'), ('02.jpg', 'Fachada', 'lugar'), ('12.jpg', 'Barra a la ventana', 'lugar'), ('13.jpg', 'Rincón', 'lugar')],
 amen=['wifi', 'terraza'], no=[('estacionamiento', 'Sin estacionamiento; hay bici estacionamiento')],
 contacto=[('ig', 'Instagram', '@cafe.ejemplo'), ('whatsapp', 'WhatsApp', '951 000 0006'), ('web', 'Sitio web', 'ejemplo.com')],
 dir='Calle Ejemplo 000, Reforma, Oaxaca de Juárez',
 posts=[('2026-10-21', '21 oct 2026', 'Llegó café de la Sierra Mazateca; lo tenemos en Chemex para dos.', '07.jpg'),
        ('2026-09-12', '12 sep 2026', '¡Abrimos! De martes a domingo, desde las 9:00.', '')],
)
RAS = {k: dict(n=n, crit=c, ico=RG.svg(k, cls='ico')) for k, (n, c, _) in RG.RASGOS.items()}
AMS = {k: dict(n=n, ico=AM.svg(k, cls='ico')) for k, n in AM.NOMBRES.items()}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const R=' + json.dumps(C, ensure_ascii=False) + ';const RAS=' + json.dumps(RAS, ensure_ascii=False) + ';const AMS=' + json.dumps(AMS, ensure_ascii=False)
                     + ';const ICO_G=' + json.dumps(ICO_G) + ';const SELLO=' + json.dumps(SELLO) + ';const LEAF=' + json.dumps(RG.svg('vegano', cls='ico')) + ';const WIFI=' + json.dumps(AM.svg('wifi', cls='ico')) + ';')
        .replace('<!--LOGO-->', logo).replace('<!--LOGOBASE-->', LOGO_BASE).replace('%STAR%', STAR))
for k, x in N.items(): html = html.replace('%' + k + '%', x)
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
