# Convia · perfil de negocio: RESTAURANTE (r1). Sigue el patrón aprobado del hotel r2 (tema del giro, mosaico, ficha llavero, boleto,
# pestañas abajo en celular). Decisión del usuario (2026-10-31): el menú se captura EN Convia y el restaurante pone un QR en sus mesas
# que abre ese menú en Convia («el gancho»). Modo QR: index.html#qr.
# Restaurante FICTICIO («Ejemplo»): fotos de relleno desenfocadas; menú, precios, contactos y dirección inventados.
# Uso: python3 gen.py <carpeta de salida con img/>. Las fotos no se guardan en el repo.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
sys.path.insert(0, F)
import rasgos as RG, amenidades as AM, cocinas as CO
G = 'restaurantes'
T = json.load(open(os.path.join(F, 'tema.json'))); K = T['categorias'][G]
N = dict(perla='#f9f9f7', sup='#ffffff', tinta='#1b1d1a', sec='#5c5f5b', linea='#e6e6e2', foto='#ececea', gtexto=K['texto'], gfondo=K['fondo'], gpunto=K['punto'], gdk='#843818')
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls): s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
logo = raw(f'sellos/{G}-logotipo-giro.svg').replace('<svg ', '<svg class="logo" ', 1)
LOGO_BASE = raw('svg/logotipo.svg').replace('<svg ', '<svg class="logo" ', 1)
SELLO = clean(raw(f'sellos/{G}-sello.svg'), 'sello-h')
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
ICO_G = clean(raw(f'iconos/{G}.svg'), 'ico')
v = lambda es, en, des, den, p, *f: dict(es=es, en=en, des=des, den=den, p=p, veg='veg' in f, pic='pic' in f, dest='dest' in f)
R = dict(
 n='Cocina Siete Fuegos', coc=['valles', 'mixteca'], kick='Restaurante · Xochimilco', precio='$$$', v=80, w=71, fav=.5, ras=['vegano', 'accesible'],
 d='Menú corto de temporada que cambia cada semana. Cocina de leña, maíz nixtamalizado en casa y producto de productores de los Valles Centrales.',
 # horario por día (0 = domingo); None = cerrado
 hor={'0': ['13:00', '20:00'], '1': None, '2': ['13:00', '22:00'], '3': ['13:00', '22:00'], '4': ['13:00', '22:00'], '5': ['13:00', '23:00'], '6': ['13:00', '23:00']},
 reserva='Reserva recomendada de viernes a domingo',
 actualizado='28 oct 2026',
 menu=[
  dict(id='empezar', es='Para empezar', en='Starters', items=[
   v('Tetelas de frijol con hoja de aguacate', 'Bean tetelas with avocado leaf', 'Masa de la casa, salsa de chile pasilla oaxaqueño.', 'House masa, Oaxacan pasilla chile salsa.', 95, 'veg', 'dest'),
   v('Ensalada de nopal y quelites', 'Cactus and wild greens salad', 'Nopal asado, quelites de temporada, vinagreta de limón.', 'Grilled cactus, seasonal greens, lime dressing.', 110, 'veg'),
   v('Tlayuda chica de asiento y quesillo', 'Small tlayuda with asiento and Oaxaca cheese', 'Al comal, con frijol y salsa de molcajete.', 'Griddled, with beans and stone-ground salsa.', 120),
   v('Sopa de guías', 'Squash vine soup', 'Guías de calabaza, elote y chepiche.', 'Squash vines, corn and chepiche herb.', 105, 'veg')]),
  dict(id='fuertes', es='Platos fuertes', en='Mains', items=[
   v('Mole negro con pollo de rancho', 'Black mole with free-range chicken', 'Receta de la casa, con arroz blanco.', 'House recipe, served with white rice.', 280, 'dest'),
   v('Mole amarillo de verduras con chochoyotes', 'Yellow vegetable mole with masa dumplings', 'Chile chilcostle, ejote, chayote y papa.', 'Chilcostle chile, green beans, chayote and potato.', 230, 'veg', 'dest'),
   v('Pescado a la talla', 'Grilled fish a la talla', 'Pesca del día con adobo de chile guajillo.', 'Catch of the day with guajillo chile adobo.', 310, 'pic'),
   v('Costilla en chileajo', 'Pork rib in chileajo', 'Chileajo rojo, papas de rancho.', 'Red chileajo sauce, country potatoes.', 295, 'pic'),
   v('Mole de caderas (temporada)', 'Mole de caderas (seasonal)', 'De octubre a noviembre: caldo espeso de chivo con ejote y guaje.', 'October to November: rich goat stew with green beans and guaje.', 320, 'dest')]),
  dict(id='postres', es='Postres', en='Desserts', items=[
   v('Nicuatole de coco', 'Coconut nicuatole', 'Dulce de maíz y coco, con grana.', 'Corn and coconut pudding.', 75, 'veg'),
   v('Pan de yema con helado de chocolate', 'Egg-yolk bread with chocolate ice cream', 'Helado de chocolate de metate.', 'Stone-ground chocolate ice cream.', 90)]),
  dict(id='bebidas', es='Bebidas', en='Drinks', items=[
   v('Agua de chilacayota', 'Chilacayota squash water', 'Del día, con piloncillo.', 'Made daily, with piloncillo.', 45, 'veg'),
   v('Chocolate de agua', 'Hot chocolate with water', 'Chocolate de metate.', 'Stone-ground chocolate.', 60, 'veg'),
   v('Café de olla', 'Café de olla', 'Con canela y piloncillo.', 'With cinnamon and piloncillo.', 45, 'veg'),
   v('Mezcal espadín (copa)', 'Espadín mezcal (glass)', 'Pregunta por los de temporada.', 'Ask for seasonal ones.', 95)])],
 galeria=[('03.jpg', 'Comedor', 'lugar'), ('07.jpg', 'Patio', 'lugar'), ('13.jpg', 'Salón de arcos', 'lugar'), ('02.jpg', 'Fachada', 'lugar'), ('12.jpg', 'Patio con luz', 'lugar'), ('11.jpg', 'Terraza de noche', 'lugar')],
 amen=['terraza', 'wifi', 'aire'], no=[('estacionamiento', 'Sin estacionamiento; hay en la calle')],
 contacto=[('whatsapp', 'WhatsApp para reservar', '951 000 0002'), ('tel', 'Teléfono', '951 000 0003'), ('ig', 'Instagram', '@restaurante.ejemplo'), ('web', 'Sitio web', 'ejemplo.com')],
 dir='Calle Ejemplo 000, Xochimilco, Oaxaca de Juárez',
 posts=[('2026-10-28', '28 oct 2026', 'Menú de Muertos: mole negro, pan de yema y chocolate de agua hasta el 3 de noviembre.', '03.jpg'),
        ('2026-10-07', '7 oct 2026', 'Ya abrimos domingos de 13:00 a 20:00.', ''),
        ('2026-09-15', '15 sep 2026', 'Llegó el chile chilcostle de la temporada: vuelve el mole amarillo de verduras.', '07.jpg')],
)
# Región de cada platillo (respalda la cocina regional del perfil; demo: asignación ilustrativa que el restaurante y Convia validarían).
REG = {'Tetelas de frijol con hoja de aguacate': 'mixteca', 'Mole de caderas (temporada)': 'mixteca', 'Tlayuda chica de asiento y quesillo': 'valles', 'Sopa de guías': 'valles',
       'Mole negro con pollo de rancho': 'valles', 'Mole amarillo de verduras con chochoyotes': 'valles', 'Nicuatole de coco': 'valles', 'Agua de chilacayota': 'valles', 'Chocolate de agua': 'valles'}
for sec in R['menu']:
    for it in sec['items']: it['reg'] = REG.get(it['es'], '')
for k in R['coc']: assert sum(it['reg'] == k for sec in R['menu'] for it in sec['items']) >= 2, k  # regla: ≥2 platillos por cocina regional
COC = {k: v['n'] for k, v in CO.COCINAS.items()}
RAS = {k: dict(n=n, ico=RG.svg(k, cls='ico')) for k, (n, c, _) in RG.RASGOS.items()}
AMS = {k: dict(n=n, ico=AM.svg(k, cls='ico')) for k, n in AM.NOMBRES.items()}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const R=' + json.dumps(R, ensure_ascii=False) + ';const RAS=' + json.dumps(RAS, ensure_ascii=False) + ';const AMS=' + json.dumps(AMS, ensure_ascii=False)
                     + ';const COC=' + json.dumps(COC, ensure_ascii=False) + ';const ICO_G=' + json.dumps(ICO_G) + ';const SELLO=' + json.dumps(SELLO) + ';const LEAF=' + json.dumps(RG.svg('vegano', cls='ico')) + ';')
        .replace('<!--LOGO-->', logo).replace('<!--LOGOBASE-->', LOGO_BASE).replace('%STAR%', STAR))
for k, x in N.items(): html = html.replace('%' + k + '%', x)
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
