# Convia · perfil de negocio: MUSEO (r1). Primer perfil construido sobre el modelo aprobado perfil + actividad + sede (convia-final/modelo-datos.md).
# El museo es un perfil «lugar»; su pestaña principal son las ACTIVIDADES donde es organizador o sede: Ahora · Próximas · Pasadas
# (exposiciones con rango de fechas, talleres con cupo y precio, eventos). Pasadas: «N marcaron que fueron» y «volverían».
# Museo FICTICIO («Ejemplo», el «Museo del Hilo» del directorio): fotos de relleno; actividades, organizadores, precios, cifras y contactos inventados.
# Uso: python3 gen.py <carpeta de salida con img/>. Las fotos no se guardan en el repo.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
sys.path.insert(0, F)
import rasgos as RG, amenidades as AM
G = 'museos'
T = json.load(open(os.path.join(F, 'tema.json'))); K = T['categorias'][G]
N = dict(perla='#f9f9f7', sup='#ffffff', tinta='#1b1d1a', sec='#5c5f5b', linea='#e6e6e2', foto='#ececea', gtexto=K['texto'], gfondo=K['fondo'], gpunto=K['punto'], gdk='#5f2f7e')
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls): s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
logo = raw(f'sellos/{G}-logotipo-giro.svg').replace('<svg ', '<svg class="logo" ', 1)
LOGO_BASE = raw('svg/logotipo.svg').replace('<svg ', '<svg class="logo" ', 1)
SELLO = clean(raw(f'sellos/{G}-sello.svg'), 'sello-h')
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
ICO_G = clean(raw(f'iconos/{G}.svg'), 'ico')
ICO_T = clean(raw('iconos/talleres.svg'), 'ico')
YO = 'Museo del Hilo'
# actividades (modelo: tipo, organizador, sede = este museo, fechas o rango, precio, cupo); estado: ahora / proxima / pasada
A = [
 dict(id='puntadas', tipo='exposicion', n='Puntadas que cuentan', sub='Bordado contemporáneo de Oaxaca', org=YO, rango=('3 oct', '30 nov 2026'), sala='Sala temporal', precio='Incluida con tu entrada',
      d='Doce bordadoras y bordadores de distintas regiones muestran cómo el bordado cuenta historias de hoy.', estado='ahora', fotos=['13.jpg', '12.jpg']),
 dict(id='relleno', tipo='taller', n='Bordado de relleno para principiantes', org='Colectivo Hilo Largo', orgtipo='Organizador independiente', fechas=[('Sáb 8 nov', '11:00', 4), ('Sáb 22 nov', '11:00', 9)],
      precio=450, cupo=10, edad='Desde 14 años', dur='3 h', tellevas='Tu muestra bordada en bastidor.', d='Puntadas de relleno sobre manta con hilo de algodón; bastidor y materiales incluidos.', estado='proxima', fotos=['07.jpg']),
 dict(id='timbre', tipo='taller', n='Pinta tu timbre postal', org='Ana P., ilustradora', orgtipo='Organizadora independiente', fechas=[('Dom 16 nov', '11:00', 12)],
      precio=250, cupo=12, edad='Desde 7 años', dur='1.5 h', tellevas='Tu timbre pintado, impreso en tamaño postal.', d='Para niñas, niños y adultos: diseñas y pintas un timbre inspirado en los bordados de la sala.', estado='proxima', fotos=['03.jpg']),
 dict(id='charla', tipo='evento', n='Charla: tintes naturales de Oaxaca', org=YO, fechas=[('Jue 13 nov', '18:00', 40)], precio='Entrada libre', cupo=40, dur='1 h',
      d='Grana, añil y pericón: de dónde salen los colores del textil oaxaqueño.', estado='proxima', fotos=['12.jpg']),
 dict(id='costa', tipo='exposicion', n='Hilos de la Costa', sub='Huipiles y telar de cintura', org=YO, rango=('5 dic 2026', '28 feb 2027'), sala='Sala temporal', precio='Incluida con tu entrada',
      d='Piezas de comunidades de la Costa, con video de sus tejedoras.', estado='proxima', fotos=['02.jpg']),
 dict(id='telar', tipo='exposicion', n='Telar de cintura: oficio vivo', org=YO, rango=('1 jun', '15 sep 2026'), fueron=312, v=312, w=280, estado='pasada', fotos=['13.jpg']),
 dict(id='grana', tipo='taller', n='Teñido con grana', org='Colectivo Hilo Largo', orgtipo='Organizador independiente', fechas=[('Sáb 20 sep 2026', '11:00', 0)], fueron=10, v=10, w=9, cupo=10, estado='pasada', fotos=['07.jpg']),
 dict(id='noche', tipo='evento', n='Noche de museos', org=YO, fechas=[('Vie 26 sep 2026', '19:00', 0)], fueron=140, v=140, w=118, estado='pasada', fotos=['11.jpg']),
]
M = dict(
 n=YO, kick='Museo · Centro', v=58, w=51, fav=.44, ras=['accesible', 'ingles'], entrada='$50', libre='Domingos entrada libre',
 d='Museo dedicado al textil de Oaxaca: telar de cintura, bordado y tintes naturales. Ocupa una casona del centro con tres salas permanentes y una temporal.',
 hor={'0': ['10:00', '18:00'], '1': None, '2': ['10:00', '19:00'], '3': ['10:00', '19:00'], '4': ['10:00', '19:00'], '5': ['10:00', '19:00'], '6': ['10:00', '19:00']},
 salas=[('Sala 1 · Telar de cintura', 'Cómo se teje y quién lo hace hoy.', '13.jpg'), ('Sala 2 · Bordado', 'Puntadas de las ocho regiones.', '12.jpg'), ('Sala 3 · Tintes', 'Grana, añil y otros colores de la tierra.', '07.jpg')],
 visita=[('reloj', 'Duración sugerida', '1 hora'), ('gente', 'Visitas guiadas', 'Sábados 12:00, incluidas con la entrada'), ('bolsa', 'Guardarropa', 'Gratis; mochilas grandes no pasan a sala')],
 amen=['wifi', 'aire'],
 contacto=[('tel', 'Teléfono', '951 000 0008'), ('ig', 'Instagram', '@museo.ejemplo'), ('web', 'Sitio web', 'ejemplo.com')],
 dir='Calle Ejemplo 000, Centro, Oaxaca de Juárez',
 galeria=[('13.jpg', 'Sala temporal'), ('12.jpg', 'Patio'), ('07.jpg', 'Sala de tintes'), ('02.jpg', 'Fachada'), ('03.jpg', 'Sala de bordado')],
 act=A,
)
RAS = {k: dict(n=n, ico=RG.svg(k, cls='ico')) for k, (n, c, _) in RG.RASGOS.items()}
AMS = {k: dict(n=n, ico=AM.svg(k, cls='ico')) for k, n in AM.NOMBRES.items()}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const R=' + json.dumps(M, ensure_ascii=False) + ';const RAS=' + json.dumps(RAS, ensure_ascii=False) + ';const AMS=' + json.dumps(AMS, ensure_ascii=False)
                     + ';const ICO_G=' + json.dumps(ICO_G) + ';const ICO_T=' + json.dumps(ICO_T) + ';const SELLO=' + json.dumps(SELLO) + ';')
        .replace('<!--LOGO-->', logo).replace('<!--LOGOBASE-->', LOGO_BASE).replace('%STAR%', STAR))
for k, x in N.items(): html = html.replace('%' + k + '%', x)
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
