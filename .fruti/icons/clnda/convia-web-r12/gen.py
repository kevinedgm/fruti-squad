# r12: portada con el hero aprobado (r3): logo de Convia al centro como doodle de temporada, frase, buscador grande y sellos;
# el encabezado muestra logo chico y buscador solo al bajar. Temporadas por fecha (Muertos, Guelaguetza, Noche de Rábanos).
# r11: modelo perfil + actividad + sede en el directorio: pestaña Agenda (talleres, recorridos, eventos, exposiciones por fecha, con «Organiza» y «En»),
# «Seguir» organizadores y avisos de nuevas actividades (aprobado 2026-10-31). Talleres y recorridos dejan de ser giros. Fechas verificadas con el calendario 2026.
# r10: cocinas de restaurantes (8 regiones de Oaxaca + otras) como filtro «¿Qué se te antoja?» y en la tarjeta; catálogo en convia-final/cocinas.py.
# r9: tarjetas uniformes (solo datos básicos, rasgos como sellitos de ícono) y ficha de perfil por lugar (#lugar/id) con todo el detalle y la calificación.
# r8.1: los «Ejemplo» llevan foto de relleno desenfocada con placa de vidrio y su nombre (solo demo).
# Convia · página principal r8 = r7 + «rasgos» (Va bien para…: trabajar, intercambio de idiomas, networking, inglés, ir solo, mascota, vegano, silla de ruedas) como etiquetas neutras en tarjetas y filtros. Solo en lugares «Ejemplo»: de los negocios reales no sabemos estos datos.
# Convia · página principal r7 = r6 + métrica «X de cada 10 volverían» (umbral 10 visitas; antes «Recién llegado»), distintivo «Favorito Convia», sello en encabezados de sección y «Organiza» en talleres/eventos.
# Las métricas son SIMULADAS y solo se asignan a lugares «Ejemplo»; los negocios reales no llevan cifras.
# Convia · página principal r6 = r5 + fotos reales aportadas por el usuario (demo interna). Datos de negocios reales: solo lo que muestran sus imágenes; lo demás «por confirmar».
# Convia · página principal r5: directorio por giro + «Mis lugares» (quiero ir · ya fui con escala propia) + sellos.
# Cambios pedidos por el usuario (2026-10-31): fondo perla (sin beige), estructura de directorio, insignias de lugares visitados.
# Uso: python3 gen.py <carpeta de salida con img/>. Las fotos de negocios reales NO se guardan en el repo (derechos de terceros); se procesan aparte y solo van en la demo privada. Negocios y datos ficticios. El «ya fui» de la demo se guarda solo en el navegador de quien la prueba.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
T = json.load(open(os.path.join(F, 'tema.json'))); CAT = T['categorias']
N = dict(perla='#f9f9f7', sup='#ffffff', tinta='#1b1d1a', sec='#5c5f5b', linea='#e6e6e2', foto='#ececea', cantera='#2f5a45', suave='#e3ece6')
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls):
    s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
logo = raw('svg/logotipo.svg').replace('<svg ', '<svg class="logo" ', 1)
ICO = {k: clean(raw(f'iconos/{k}.svg'), 'ico') for k in CAT}
SELLO = {k: clean(raw(f'sellos/{k}-sello-solido.svg'), 'sello') for k in CAT}
SELLO_L = {k: clean(raw(f'sellos/{k}-sello.svg'), 'sello') for k in CAT}
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
LOGO_TXT = re.sub(r' fill="[^"]*"', '', ''.join(re.findall(r'<path[^>]*/>', raw('svg/logotipo.svg'))[1:]))
NOMBRES = {'cafes': 'Cafés', 'restaurantes': 'Restaurantes', 'hoteles': 'Hoteles boutique', 'talleres': 'Talleres', 'recorridos': 'Recorridos y tours', 'museos': 'Museos y galerías'}
INSIGNIA = {'cafes': 'Cafetero', 'restaurantes': 'Buen diente', 'hoteles': 'Huésped de patio', 'talleres': 'Manos a la obra', 'recorridos': 'Caminante', 'museos': 'Ojo curioso'}
# id, categoría, nombre, barrio, detalle, etiquetas (nuevo / buscado / finde), cuándo (si es evento)
R = [  # negocios reales (fotos del usuario, demo interna): id, giro, nombre, zona, detalle, etiquetas, cuándo, info, img, alt, ajuste
 ('e1','restaurantes','Expendio Tradición','Oaxaca','Casona en esquina; interior con piso de pasta y celosía de madera',['buscado'],'','','02.jpg','Fachada de una casona blanca en esquina con macetas de agave en la azotea','cover'),
 ('c7','cafes','Cafébre · orfebrería de café','Oaxaca','Patio con mural, mesas largas de madera y luces colgantes',['buscado'],'','','07.jpg','Patio de café con pared verde, mural y mesas de madera','cover'),
 ('c8','cafes','Gattó','Oaxaca','Barra de café, bebidas frías y smoothies',['nuevo'],'','','08.jpg','Barra de café con pizarrones de menú','cover'),
 ('c9','cafes','Muss Café','Oaxaca','En la planta baja de una casona de cantera',['nuevo','buscado'],'','','09.jpg','Fachada de cantera con balcón de herrería y la entrada de Muss Café','cover'),
 ('t5','talleres','Puntada maravillosa · taller de bordado','Centro','Bordado en relieve; desde 15 años, cupo de 10 personas',['nuevo'],'Próxima fecha por confirmar','Donativo $600 (incluye materiales)','04.png'.replace('png','jpg'),'Cartel del taller de bordado Puntada maravillosa','cover'),
 ('t6','talleres','Naturalmente tricolor · taller de teñido','Centro','Teñido con cempasúchil, grana y añil; cupo de 10 personas',['buscado'],'Próxima fecha por confirmar','Donativo $600 (incluye materiales)','05.jpg','Cartel del taller de teñido Naturalmente tricolor','cover'),
 ('g4','recorridos','Xiadani Tours','Oaxaca','Operador de tours en Oaxaca',['nuevo'],'','','06.jpg','Logotipo de Xiadani Tours','contain'),
 ('h4','hoteles','Hotel Bottega','Por confirmar','Alberca iluminada y jardín',['nuevo'],'','','10.jpg','Hotel con alberca iluminada al atardecer','cover'),
 ('h5','hoteles','Hotel boutique (nombre por confirmar)','Por confirmar','Terraza con alberca y vista de noche',[],'','','11.jpg','Terraza de hotel con alberca iluminada de noche','cover'),
 ('h6','hoteles','Hotel boutique (nombre por confirmar)','Por confirmar','Patio con tragaluz, arcos y faroles',['buscado'],'','','12.jpg','Patio interior con arcos, faroles y salas blancas','cover'),
]
L = [  # id, giro, nombre, barrio, detalle, etiquetas, cuándo, horario/precio
 ('c1','cafes','Café Tres Patios','Jalatlaco','Café de olla, pan de yema de la casa y patio con bugambilia',['buscado'],'','Lun–Dom 8:00–21:00 · $'),
 ('c2','cafes','Tostadora Norte','Reforma','Abrió en septiembre; tuestan aquí mismo los martes',['nuevo'],'','Mar–Dom 9:00–19:00 · $$'),
 ('c3','cafes','La Ventanita','Centro','Barra de cinco bancos; espresso y galleta de nata',['nuevo','buscado'],'','Lun–Sáb 7:30–15:00 · $'),
 ('c4','cafes','Café del Andador','Centro','Terraza en segundo piso con vista a la calle',['buscado'],'','Lun–Dom 9:00–22:00 · $$'),
 ('c5','cafes','Molienda Lenta','Xochimilco','Métodos de filtrado y repostería de temporada',['nuevo'],'','Mié–Dom 10:00–20:00 · $$'),
 ('c6','cafes','Café Azotea Azul','Reforma','Para trabajar: mesas grandes y enchufes',[],'','Lun–Vie 8:00–20:00 · $$'),
 ('r1','restaurantes','Cocina Siete Fuegos','Xochimilco','Menú corto de temporada que cambia cada semana',['buscado'],'','Mar–Dom 13:00–22:00 · $$$'),
 ('r2','restaurantes','Fonda Patio Chico','Centro','Comida corrida casera de lunes a sábado',['nuevo'],'','Lun–Sáb 13:00–17:30 · $'),
 ('r3','restaurantes','Mesa de Barro','Jalatlaco','Seis tiempos los sábados en mesa compartida',['finde','buscado'],'Sáb 20:00','Reserva previa · $1,200'),
 ('r4','restaurantes','Taquería El Portalito','Centro','Tacos de barbacoa, solo fines de semana',['finde'],'Sáb y Dom 8:00','Hasta agotar · $'),
 ('r5','restaurantes','Mariscos La Barra','Reforma','Pescado zarandeado y cocteles al estilo de la costa',['nuevo'],'','Mar–Dom 12:00–19:00 · $$'),
 ('r6','restaurantes','Comedor Na Rosa','Centro','Garnachas y queso horneado como en el Istmo',['buscado'],'','Lun–Sáb 9:00–18:00 · $'),
 ('r7','restaurantes','Ramen de Barrio','Jalatlaco','Ramen y gyozas; caldo de doce horas',['nuevo'],'','Mar–Dom 14:00–22:00 · $$'),
 ('r8','restaurantes','Trattoria del Llano','Centro','Pasta fresca hecha cada mañana',[],'','Lun–Dom 13:00–23:00 · $$'),
 ('r9','restaurantes','Fonda Serrana','Xochimilco','Caldo de res, tamales de frijol y trucha de la sierra',['finde'],'Sáb y Dom 9:00','Desayunos y comidas · $'),
 ('h1','hoteles','Hotel Patio de Luz','Centro','Nueve habitaciones alrededor de un patio de cantera',['buscado'],'','Desde $2,480 por noche'),
 ('h2','hoteles','Casa Cantera Verde','Jalatlaco','Cinco cuartos y desayuno en la azotea',['nuevo'],'','Desde $1,950 por noche'),
 ('h3','hoteles','Posada del Laurel','Xochimilco','Casona restaurada, jardín y bicis para huéspedes',[],'','Desde $1,600 por noche'),
 ('t1','talleres','Barro bruñido para principiantes','Centro','Grupo de seis; te llevas tu pieza',['finde','buscado'],'Sáb 26 · 11:00','3 h · $650'),
 ('t2','talleres','Grabado en linóleo','Xochimilco','Diseñas, tallas e imprimes tu estampa',['finde','nuevo'],'Dom 27 · 10:00','2.5 h · $550'),
 ('t3','talleres','Cocina de moles','Reforma','De la milpa a la mesa, con comida incluida',['buscado'],'Sáb 26 · 10:00','4 h · $1,100'),
 ('t4','talleres','Tejido en telar de cintura (intro)','Jalatlaco','Clase introductoria con maestra tejedora',['nuevo'],'Vie 25 · 17:00','3 h · $700'),
 ('g1','recorridos','Caminata de cantera al amanecer','Centro','Grupo pequeño; termina con café',['finde','buscado'],'Dom 27 · 7:00','2 h · $300'),
 ('g2','recorridos','Ruta de mercados','Centro','Probar, preguntar y comprar con guía local',['finde'],'Sáb 26 · 9:00','3 h · $450'),
 ('g3','recorridos','Bici por los barrios','Jalatlaco','Ritmo tranquilo; bici y casco incluidos',['nuevo','finde'],'Dom 27 · 8:30','3 h · $500'),
 ('m1','museos','Casa de la Gráfica','Centro','Colección de estampa y biblioteca de consulta',['buscado'],'','Mar–Dom 10:00–18:00 · Gratis'),
 ('m2','museos','Galería Patio Norte','Reforma','Artistas jóvenes; inauguración este sábado',['nuevo','finde'],'Sáb 26 · 12:00','Entrada libre'),
 ('m3','museos','Museo del Hilo','Centro','Sala temporal de bordados contemporáneos',[],'','Lun–Sáb 10:00–20:00 · $50'),
]
ORG = {'t5': 'Museo Textil de Oaxaca', 't6': 'Museo Textil de Oaxaca',  # real (según sus carteles)
       't1': 'Taller Barro Vivo', 't2': 'Estudio La Prensa', 't3': 'Cocina de Milpa', 't4': 'Colectivo Hilo Largo',
       'g1': 'Caminantes de Antequera', 'g2': 'Mercados con Calma', 'g3': 'Rodada Lenta', 'r3': 'Mesa de Barro', 'm2': 'Galería Patio Norte'}
RAS = {  # rasgos simulados solo para «Ejemplo»: clave o (clave, cuándo)
 'c1': [('idiomas', 'Vie 18:00'), 'mascotas'], 'c2': [('networking', 'Jue 9:00'), 'trabajar'], 'c4': [('idiomas', 'Mié 19:00'), 'ingles'],
 'c5': ['trabajar', 'vegano'], 'c6': ['trabajar', 'ingles'], 'r1': ['vegano', 'accesible'], 'r3': ['solo', 'ingles'], 'r4': ['mascotas'],
 'h1': ['accesible', 'ingles'], 'h2': ['trabajar', 'mascotas'], 'h3': ['mascotas'], 't1': ['solo', 'ingles'], 't2': ['solo'], 't3': ['solo'],
 't4': ['solo'], 'g1': ['solo', 'ingles', 'mascotas'], 'g2': ['ingles'], 'g3': ['solo'], 'm1': ['accesible', 'trabajar'],
 'm2': [('networking', 'Sáb 12:00')], 'm3': ['accesible']}
COCS = {'r1': ['valles', 'mixteca'], 'r2': ['valles'], 'r3': ['istmo', 'costa'], 'r4': ['valles'], 'r5': ['costa', 'mariscos'], 'r6': ['istmo'],
        'r7': ['asiatica'], 'r8': ['italiana'], 'r9': ['sierra-norte']}  # solo «Ejemplo»; de los restaurantes reales no sabemos su cocina
SIM = {  # métricas simuladas solo para «Ejemplo»: visitas registradas, cuántos volverían, proporción de «De mis favoritos»
 'c1': (64, 52, .45), 'c2': (6, 5, 0), 'c3': (31, 22, .2), 'c4': (48, 35, .25), 'c5': (4, 4, 0), 'c6': (18, 11, .1),
 'r1': (80, 71, .5), 'r2': (12, 9, .2), 'r3': (25, 22, .42), 'r4': (40, 30, .3), 'h1': (33, 28, .4), 'h2': (5, 4, 0), 'h3': (14, 10, .2),
 't1': (22, 20, .5), 't2': (3, 3, 0), 't3': (19, 15, .3), 't4': (7, 6, 0), 'g1': (28, 25, .45), 'g2': (15, 11, .2), 'g3': (2, 2, 0),
 'm1': (50, 38, .3), 'm2': (9, 8, 0), 'm3': (11, 8, .2),
 'r5': (12, 10, .3), 'r6': (36, 31, .45), 'r7': (5, 5, 0), 'r8': (20, 14, .2), 'r9': (9, 8, 0)}
data = [dict(id=i, cat=c, n=n, z=z, d=d, tags=t, when=w, info=x, img=im, alt=al, fit=fi) for i, c, n, z, d, t, w, x, im, al, fi in R] + \
       [dict(id=i, cat=c, n=n, z=z, d=d, tags=t, when=w, info=x, ej=True) for i, c, n, z, d, t, w, x in L]
# Fotos de relleno para «Ejemplo» (pedido del usuario 2026-10-31): solo fotos sin letreros ni logotipos, siempre desenfocadas
# y con placa de vidrio con el nombre ficticio, para que no se reconozca el negocio real de la foto.
RELLENO = {'cafes': ['07.jpg', '03.jpg', '02.jpg'], 'restaurantes': ['03.jpg', '07.jpg', '02.jpg', '13.jpg'], 'hoteles': ['11.jpg', '12.jpg', '13.jpg'],
           'talleres': ['03.jpg', '07.jpg', '13.jpg', '12.jpg'], 'recorridos': ['02.jpg', '11.jpg', '07.jpg'], 'museos': ['13.jpg', '12.jpg', '02.jpg']}
_n = {}
for p in data:
    if p.get('ej'):
        k = p['cat']; i = _n.get(k, 0); _n[k] = i + 1
        p.update(img=RELLENO[k][i % len(RELLENO[k])], alt='', fit='cover', relleno=True)
data = [p for p in data if p['cat'] not in ('talleres', 'recorridos')]  # ahora son actividades u organizadores
for p in data:
    p['org'] = ORG.get(p['id'], '')
    p['coc'] = COCS.get(p['id'], [])
    p['ras'] = [r if isinstance(r, tuple) else (r, '') for r in RAS.get(p['id'], [])]
    if p['id'] in SIM: p['v'], p['w'], p['fav'] = SIM[p['id']]
catmeta = {k: dict(nombre=NOMBRES[k], insignia=INSIGNIA[k], fondo=v['fondo'], texto=v['texto'], punto=v['punto']) for k, v in CAT.items()}
sys.path.insert(0, F); import rasgos as RG, cocinas as CO
# --- modelo: organizadores y actividades (ficticios salvo Museo Textil de Oaxaca y Xiadani Tours, reales sin fechas confirmadas)
A1 = 'https://claude.ai/artifact/'
ORGS = {
 'hilo': dict(n='Colectivo Hilo Largo', tipo='Colectivo', url=A1 + 'VKn5a1v2ZNpzYg1Mh3ebpo'),
 'barro': dict(n='Taller Barro Vivo', tipo='Estudio', url=A1 + '5WRkf4WB9J64pmTM1JWMRK'),
 'caminantes': dict(n='Caminantes de Antequera', tipo='Operador de recorridos', url=A1 + '5SJK5By7AyzoAjE7g6zJuf'),
 'prensa': dict(n='Estudio La Prensa', tipo='Estudio'), 'milpa': dict(n='Cocina de Milpa', tipo='Escuela de cocina'),
 'mercados': dict(n='Mercados con Calma', tipo='Operador de recorridos'), 'rodada': dict(n='Rodada Lenta', tipo='Operador de recorridos'),
 'ana': dict(n='Ana P., ilustradora', tipo='Persona'),
 'museo-hilo': dict(n='Museo del Hilo', tipo='Museo', lugar='m3', url=A1 + 'VLXvEMM7XVw6T5MbYVhG5u'),
 'tostadora': dict(n='Tostadora Norte', tipo='Café', lugar='c2', url=A1 + '7HoET7Tj5544sRNVzESfdh'),
 'andador': dict(n='Café del Andador', tipo='Café', lugar='c4'), 'patio-norte': dict(n='Galería Patio Norte', tipo='Galería', lugar='m2'),
 'mto': dict(n='Museo Textil de Oaxaca', tipo='Museo', real=True), 'xiadani': dict(n='Xiadani Tours', tipo='Operador de recorridos', real=True),
}
PERFIL = {'c2': A1 + '7HoET7Tj5544sRNVzESfdh', 'r1': A1 + 'MMk5Ck3qhFLxzx1dYcc2HF', 'h1': A1 + 'Q39D6bxh733WB2cVWFPKWF', 'm3': A1 + 'VLXvEMM7XVw6T5MbYVhG5u'}
# Prototipo (pedido del usuario 2026-10-31): cualquier tarjeta abre la página completa de SU GIRO, aunque se repita la misma para todos los del giro.
PGIRO = {'cafes': A1 + '7HoET7Tj5544sRNVzESfdh', 'restaurantes': A1 + 'MMk5Ck3qhFLxzx1dYcc2HF', 'hoteles': A1 + 'Q39D6bxh733WB2cVWFPKWF', 'museos': A1 + 'VLXvEMM7XVw6T5MbYVhG5u'}
PTIPO = {'taller': A1 + '5WRkf4WB9J64pmTM1JWMRK', 'recorrido': A1 + '5SJK5By7AyzoAjE7g6zJuf', 'organizador': A1 + 'VKn5a1v2ZNpzYg1Mh3ebpo'}
for p in data:
    p['url'] = PGIRO[p['cat']]
_giro = {p['id']: p['cat'] for p in data}
for k, o in ORGS.items():  # todo organizador tiene página: lugar → la de su giro; operador → recorridos; estudio/escuela → taller; colectivo/persona → organizador
    if o.get('url'): continue
    if o.get('lugar'): o['url'] = PGIRO[_giro[o['lugar']]]
    elif o['tipo'].startswith('Operador'): o['url'] = PTIPO['recorrido']
    elif o['tipo'] == 'Museo': o['url'] = PGIRO['museos']
    elif o['tipo'] in ('Estudio', 'Escuela de cocina'): o['url'] = PTIPO['taller']
    else: o['url'] = PTIPO['organizador']
# actividad: id, tipo, nombre, organizador, sede (id de lugar o texto), fecha ISO, hora, precio, publicada (ISO)
ACT = [dict(id=a, tipo=t, n=n, org=o, sede=sd, f=f, h=h, p=pr, pub=pb) for a, t, n, o, sd, f, h, pr, pb in [
 ('a1', 'recorrido', 'Caminata de cantera al amanecer', 'caminantes', 'Atrio de Santo Domingo', '2026-11-01', '7:00', '$300', '2026-10-20'),
 ('a2', 'evento', 'Intercambio de idiomas', 'andador', 'c4', '2026-11-04', '19:00', 'Gratis · consumo aparte', '2026-10-01'),
 ('a3', 'evento', 'Desayuno de freelancers', 'tostadora', 'c2', '2026-11-05', '9:00', 'Gratis · consumo aparte', '2026-10-15'),
 ('a4', 'recorrido', 'Barrios al atardecer: Jalatlaco y Xochimilco', 'caminantes', 'Templo de San Matías Jalatlaco', '2026-11-06', '17:30', '$380', '2026-10-29'),
 ('a5', 'recorrido', 'Ruta de mercados', 'mercados', 'Mercado Benito Juárez', '2026-11-07', '9:00', '$450', '2026-10-10'),
 ('a6', 'taller', 'Barro bruñido para principiantes', 'barro', 'Estudio Barro Vivo · Centro', '2026-11-07', '11:00', '$650', '2026-10-30'),
 ('a7', 'taller', 'Bordado de relleno para principiantes', 'hilo', 'm3', '2026-11-07', '11:00', '$450', '2026-10-28'),
 ('a8', 'evento', 'Inauguración: artistas jóvenes', 'patio-norte', 'm2', '2026-11-07', '12:00', 'Entrada libre', '2026-10-26'),
 ('a9', 'recorrido', 'Bici por los barrios', 'rodada', 'Jalatlaco', '2026-11-08', '8:30', '$500', '2026-10-22'),
 ('a10', 'taller', 'Grabado en linóleo', 'prensa', 'Estudio La Prensa · Xochimilco', '2026-11-08', '10:00', '$550', '2026-10-18'),
 ('a11', 'evento', 'Charla: tintes naturales de Oaxaca', 'museo-hilo', 'm3', '2026-11-12', '18:00', 'Entrada libre', '2026-10-27'),
 ('a12', 'taller', 'Telar de cintura: introducción', 'hilo', 'Su taller en Jalatlaco', '2026-11-13', '17:00', '$700', '2026-10-29'),
 ('a13', 'taller', 'Cocina de moles', 'milpa', 'Cocina de Milpa · Reforma', '2026-11-14', '10:00', '$1,100', '2026-10-05'),
 ('a14', 'taller', 'Pinta tu timbre postal', 'ana', 'm3', '2026-11-15', '11:00', '$250', '2026-10-30'),
 ('a15', 'evento', 'Tarde de puntadas', 'hilo', 'c1', '2026-11-19', '18:00', '$150', '2026-10-30'),
 ('t5', 'taller', 'Puntada maravillosa · taller de bordado', 'mto', 'Museo Textil de Oaxaca', '', '', 'Donativo $600', ''),
 ('t6', 'taller', 'Naturalmente tricolor · taller de teñido', 'mto', 'Museo Textil de Oaxaca', '', '', 'Donativo $600', ''),
]] + [dict(id='x1', tipo='exposicion', n='Puntadas que cuentan', org='museo-hilo', sede='m3', f='2026-10-03', hasta='2026-11-30', h='', p='Con la entrada · $50', pub='2026-09-28')]
import datetime as _d
for a in ACT:  # verificación: ninguna fecha inválida
    if a['f']: _d.date.fromisoformat(a['f'])
svgs = {'ico': ICO, 'sello': SELLO, 'selloL': SELLO_L, 'ras': {k: RG.svg(k, cls='ico') for k in RG.RASGOS}}
rasmeta = {k: dict(n=n, crit=t, fecha=f) for k, (n, t, f) in RG.RASGOS.items()}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const DATA=' + json.dumps(data, ensure_ascii=False) + ';const CAT=' + json.dumps(catmeta, ensure_ascii=False) + ';const SVG=' + json.dumps(svgs) + ';const RAS=' + json.dumps(rasmeta, ensure_ascii=False) + ';const COC=' + json.dumps(CO.COCINAS, ensure_ascii=False) + ';const LOGO_TXT=' + json.dumps(LOGO_TXT)+ ';const ORGS=' + json.dumps(ORGS, ensure_ascii=False) + ';const ACT=' + json.dumps(ACT, ensure_ascii=False) + ';')
        .replace('<!--LOGO-->', logo).replace('%STAR%', STAR))
for k, v in N.items(): html = html.replace('%' + k + '%', v)
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html)
print('ok', len(html))
