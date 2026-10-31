# Convia · página principal r7 = r6 + métrica «X de cada 10 volverían» (umbral 10 visitas; antes «Recién llegado»), distintivo «Favorito Convia», sello en encabezados de sección y «Organiza» en talleres/eventos.
# Las métricas son SIMULADAS y solo se asignan a lugares «Ejemplo»; los negocios reales no llevan cifras.
# Convia · página principal r6 = r5 + fotos reales aportadas por el usuario (demo interna). Datos de negocios reales: solo lo que muestran sus imágenes; lo demás «por confirmar».
# Convia · página principal r5: directorio por giro + «Mis lugares» (quiero ir · ya fui con escala propia) + sellos.
# Cambios pedidos por el usuario (2026-10-31): fondo perla (sin beige), estructura de directorio, insignias de lugares visitados.
# Uso: python3 gen.py <carpeta de salida con img/>. Las fotos de negocios reales NO se guardan en el repo (derechos de terceros); se procesan aparte y solo van en la demo privada. Negocios y datos ficticios. El «ya fui» de la demo se guarda solo en el navegador de quien la prueba.
import os, re, json
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
SIM = {  # métricas simuladas solo para «Ejemplo»: visitas registradas, cuántos volverían, proporción de «De mis favoritos»
 'c1': (64, 52, .45), 'c2': (6, 5, 0), 'c3': (31, 22, .2), 'c4': (48, 35, .25), 'c5': (4, 4, 0), 'c6': (18, 11, .1),
 'r1': (80, 71, .5), 'r2': (12, 9, .2), 'r3': (25, 22, .42), 'r4': (40, 30, .3), 'h1': (33, 28, .4), 'h2': (5, 4, 0), 'h3': (14, 10, .2),
 't1': (22, 20, .5), 't2': (3, 3, 0), 't3': (19, 15, .3), 't4': (7, 6, 0), 'g1': (28, 25, .45), 'g2': (15, 11, .2), 'g3': (2, 2, 0),
 'm1': (50, 38, .3), 'm2': (9, 8, 0), 'm3': (11, 8, .2)}
data = [dict(id=i, cat=c, n=n, z=z, d=d, tags=t, when=w, info=x, img=im, alt=al, fit=fi) for i, c, n, z, d, t, w, x, im, al, fi in R] + \
       [dict(id=i, cat=c, n=n, z=z, d=d, tags=t, when=w, info=x, ej=True) for i, c, n, z, d, t, w, x in L]
for p in data:
    p['org'] = ORG.get(p['id'], '')
    if p['id'] in SIM: p['v'], p['w'], p['fav'] = SIM[p['id']]
catmeta = {k: dict(nombre=NOMBRES[k], insignia=INSIGNIA[k], fondo=v['fondo'], texto=v['texto'], punto=v['punto']) for k, v in CAT.items()}
svgs = {'ico': ICO, 'sello': SELLO, 'selloL': SELLO_L}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const DATA=' + json.dumps(data, ensure_ascii=False) + ';const CAT=' + json.dumps(catmeta, ensure_ascii=False) + ';const SVG=' + json.dumps(svgs) + ';')
        .replace('<!--LOGO-->', logo).replace('%STAR%', STAR))
for k, v in N.items(): html = html.replace('%' + k + '%', v)
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html)
print('ok', len(html))
