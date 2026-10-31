# Convia · página principal r4: directorio por giro + estantes (nuevos, más buscados, este fin) + pasaporte de sellos «ya fui».
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
L = [
 ('c1','cafes','Café Tres Patios','Jalatlaco','Café de olla y pan de la casa',['buscado'],''),
 ('c2','cafes','Tostadora Norte','Reforma','Abrió en septiembre; tueste propio',['nuevo'],''),
 ('c3','cafes','La Ventanita','Centro','Barra de cinco bancos, espresso',['nuevo','buscado'],''),
 ('c4','cafes','Café del Andador','Centro','Terraza en segundo piso',['buscado'],''),
 ('c5','cafes','Molienda Lenta','Xochimilco','Métodos de filtrado y repostería',['nuevo'],''),
 ('r1','restaurantes','Cocina Siete Fuegos','Xochimilco','Menú corto de temporada',['buscado'],''),
 ('r2','restaurantes','Fonda Patio Chico','Centro','Comida corrida de lunes a sábado',['nuevo'],''),
 ('r3','restaurantes','Mesa de Barro','Jalatlaco','Seis tiempos los sábados',['finde','buscado'],'Sáb 20:00'),
 ('h1','hoteles','Hotel Patio de Luz','Centro','Nueve habitaciones alrededor de un patio',['buscado'],''),
 ('h2','hoteles','Casa Cantera Verde','Jalatlaco','Cinco cuartos, desayuno en la azotea',['nuevo'],''),
 ('t1','talleres','Barro bruñido para principiantes','Centro','Grupo de seis · para ir solo',['finde','buscado'],'Sáb 11:00'),
 ('t2','talleres','Grabado en linóleo','Xochimilco','Te llevas tu estampa',['finde','nuevo'],'Dom 10:00'),
 ('t3','talleres','Cocina de moles','Reforma','De la milpa a la mesa',['buscado'],'Sáb 10:00'),
 ('g1','recorridos','Caminata de cantera al amanecer','Centro','Grupo pequeño · 2 h',['finde','buscado'],'Dom 7:00'),
 ('g2','recorridos','Ruta de mercados','Centro','Probar, preguntar, comprar',['finde'],'Sáb 9:00'),
 ('g3','recorridos','Bici por los barrios','Jalatlaco','Ritmo tranquilo · 3 h',['nuevo','finde'],'Dom 8:30'),
 ('m1','museos','Casa de la Gráfica','Centro','Colección de estampa',['buscado'],''),
 ('m2','museos','Galería Patio Norte','Reforma','Artistas jóvenes; abre sábados',['nuevo','finde'],'Sáb 12:00'),
]
data = [dict(id=i, cat=c, n=n, z=z, d=d, tags=t, when=w) for i, c, n, z, d, t, w in L]
catmeta = {k: dict(nombre=NOMBRES[k], insignia=INSIGNIA[k], fondo=v['fondo'], texto=v['texto'], punto=v['punto']) for k, v in CAT.items()}
svgs = {'ico': ICO, 'sello': SELLO, 'selloL': SELLO_L}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const DATA=' + json.dumps(data, ensure_ascii=False) + ';const CAT=' + json.dumps(catmeta, ensure_ascii=False) + ';const SVG=' + json.dumps(svgs) + ';')
        .replace('<!--LOGO-->', logo).replace('%STAR%', STAR))
for k, v in N.items(): html = html.replace('%' + k + '%', v)
open(os.path.join(D, 'index.html'), 'w').write(html)
print('ok', len(html))
