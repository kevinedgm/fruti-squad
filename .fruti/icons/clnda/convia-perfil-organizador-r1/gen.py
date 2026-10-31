# Convia · perfil ORGANIZADOR independiente (r1), sobre el modelo aprobado perfil + actividad + sede (convia-final/modelo-datos.md).
# Un organizador no tiene giro: usa el verde base de Convia (Cantera), no un color de giro. Sus actividades pasan en varias sedes;
# cada una dice «En: <sede>» y enlaza al perfil del lugar. Pestañas: Actividades (Próximas · Pasadas) · Dónde · Quiénes · ¿Volverían? · Contacto.
# Organizador FICTICIO («Ejemplo», el «Colectivo Hilo Largo» del museo r1 y del directorio): fotos de relleno; integrantes, cifras y contactos inventados.
# Uso: python3 gen.py <carpeta de salida con img/>. Las fotos no se guardan en el repo.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
sys.path.insert(0, F)
import rasgos as RG
T = json.load(open(os.path.join(F, 'tema.json'))); C = T['color']
N = dict(perla='#f9f9f7', sup='#ffffff', tinta='#1b1d1a', sec='#5c5f5b', linea='#e6e6e2', foto='#ececea', gtexto=C['cantera'], gfondo=C['cantera_suave'], gpunto=C['cantera'], gdk='#244736')
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls): s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
LOGO = raw('svg/logotipo.svg').replace('<svg ', '<svg class="logo" ', 1)
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
CAT = {k: dict(n=v['nombre'], f=v['fondo'], t=v['texto'], ico=clean(raw(f'iconos/{k}.svg'), 'ico')) for k, v in T['categorias'].items()}
YO = 'Colectivo Hilo Largo'
SEDES = {  # sede: perfil «lugar» (con giro) o dirección suelta
 'museo': dict(n='Museo del Hilo', giro='museos', zona='Centro', perfil=True),
 'cafe': dict(n='Café Tres Patios', giro='cafes', zona='Jalatlaco', perfil=True),
 'propio': dict(n='Su taller en Jalatlaco', giro='', zona='Jalatlaco', perfil=False, dir='Calle Ejemplo 000, Jalatlaco'),
 'andador': dict(n='Andador Macedonio Alcalá', giro='', zona='Centro', perfil=False, dir='Espacio público'),
}
A = [
 dict(tipo='taller', n='Bordado de relleno para principiantes', sede='museo', fechas=[('Sáb 8 nov', '11:00', 4), ('Sáb 22 nov', '11:00', 9)], precio=450, cupo=10, dur='3 h', edad='Desde 14 años',
      tellevas='Tu muestra bordada en bastidor.', d='Puntadas de relleno sobre manta con hilo de algodón; bastidor y materiales incluidos.', estado='proxima', fotos=['07.jpg']),
 dict(tipo='taller', n='Telar de cintura: introducción', sede='propio', fechas=[('Vie 14 nov', '17:00', 6)], precio=700, cupo=6, dur='3 h', edad='Desde 15 años',
      tellevas='Una tira tejida por ti, de unos 30 cm.', d='Armas el telar, aprendes la urdimbre y tejes tu primera tira con Teresa.', estado='proxima', fotos=['13.jpg']),
 dict(tipo='evento', n='Tarde de puntadas', sede='cafe', fechas=[('Jue 20 nov', '18:00', 12)], precio=150, cupo=12, dur='2 h',
      tellevas='Lo que avances de tu bordado (y un café incluido).', d='Trae tu bordado o empieza uno con hilo y manta que te damos. Ambiente de café, sin prisa.', estado='proxima', fotos=['03.jpg']),
 dict(tipo='taller', n='Teñido con grana', sede='museo', fechas=[('Sáb 20 sep 2026', '11:00', 0)], fueron=10, v=10, w=9, estado='pasada', fotos=['07.jpg']),
 dict(tipo='evento', n='Puntadas en el andador', sede='andador', fechas=[('Dom 14 sep 2026', '10:00', 0)], fueron=46, v=46, w=41, estado='pasada', fotos=['02.jpg']),
]
O = dict(
 n=YO, ini='HL', tipo='Organizador independiente · colectivo', desde_anio='2018', v=56, w=50, fav=.45, ras=['solo'],
 d='Somos tres mujeres de Jalatlaco que bordamos, tejemos y teñimos con tintes naturales. Damos talleres en museos, cafés y en nuestro propio taller, siempre en grupos pequeños.',
 revision='Revisado por Convia: asistimos a un taller suyo (sep 2026) y pedimos referencias a dos sedes.',
 quienes=[('MR', 'Margarita R.', 'Bordado de relleno y punto de cruz'), ('TL', 'Teresa L.', 'Telar de cintura'), ('IS', 'Isabel S.', 'Tintes naturales: grana, añil, pericón')],
 privado='También damos talleres privados para escuelas, empresas y grupos de amigos.',
 contacto=[('whatsapp', 'WhatsApp', '951 000 0009'), ('ig', 'Instagram', '@colectivo.ejemplo')],
 galeria=[('07.jpg', 'Muestras de bordado'), ('13.jpg', 'Telar de cintura'), ('03.jpg', 'Taller en grupo'), ('12.jpg', 'Hilos teñidos'), ('02.jpg', 'Puntadas en el andador')],
 act=A,
)
RAS = {k: dict(n=n, ico=RG.svg(k, cls='ico')) for k, (n, c, _) in RG.RASGOS.items()}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const R=' + json.dumps(O, ensure_ascii=False) + ';const SEDES=' + json.dumps(SEDES, ensure_ascii=False) + ';const CAT=' + json.dumps(CAT, ensure_ascii=False)
                     + ';const RAS=' + json.dumps(RAS, ensure_ascii=False) + ';const ICO_T=' + json.dumps(CAT['talleres']['ico']) + ';')
        .replace('<!--LOGO-->', LOGO).replace('<!--LOGOBASE-->', LOGO).replace('%STAR%', STAR))
for k, x in N.items(): html = html.replace('%' + k + '%', x)
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
