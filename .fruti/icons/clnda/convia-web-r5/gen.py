# Convia · página principal r5: directorio por giro + «Mis lugares» (quiero ir · ya fui con escala propia) + sellos.
# Cambios pedidos por el usuario (2026-10-31): fondo perla (sin beige), estructura de directorio, insignias de lugares visitados.
# Uso: python3 gen.py. Negocios y datos ficticios. El «ya fui» de la demo se guarda solo en el navegador de quien la prueba.
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
data = [dict(id=i, cat=c, n=n, z=z, d=d, tags=t, when=w, info=x) for i, c, n, z, d, t, w, x in L]
catmeta = {k: dict(nombre=NOMBRES[k], insignia=INSIGNIA[k], fondo=v['fondo'], texto=v['texto'], punto=v['punto']) for k, v in CAT.items()}
svgs = {'ico': ICO, 'sello': SELLO, 'selloL': SELLO_L}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const DATA=' + json.dumps(data, ensure_ascii=False) + ';const CAT=' + json.dumps(catmeta, ensure_ascii=False) + ';const SVG=' + json.dumps(svgs) + ';')
        .replace('<!--LOGO-->', logo).replace('%STAR%', STAR))
for k, v in N.items(): html = html.replace('%' + k + '%', v)
open(os.path.join(D, 'index.html'), 'w').write(html)
print('ok', len(html))
