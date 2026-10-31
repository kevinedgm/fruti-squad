# Convia · perfil de negocio: TALLER (r1). Patrón aprobado (hotel r2) + hoja de fechas y cupo de recorridos r1 (aprobado), con el color de talleres.
# El negocio es el ESTUDIO; cada taller abre una hoja con «Qué vas a hacer» (pasos), «Te llevas», fechas con cupo, lugares × precio,
# edad mínima, incluye / qué llevar y dónde es. Pestañas: Talleres · Piezas · Maestros · ¿Volverían? · Contacto.
# Estudio FICTICIO («Ejemplo», el «Taller Barro Vivo» del directorio): fotos de relleno; maestros, precios, fechas y contactos inventados.
# Uso: python3 gen.py <carpeta de salida con img/>. Las fotos no se guardan en el repo.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
sys.path.insert(0, F)
import rasgos as RG
G = 'talleres'
T = json.load(open(os.path.join(F, 'tema.json'))); K = T['categorias'][G]
N = dict(perla='#f9f9f7', sup='#ffffff', tinta='#1b1d1a', sec='#5c5f5b', linea='#e6e6e2', foto='#ececea', gtexto=K['texto'], gfondo=K['fondo'], gpunto=K['punto'], gdk='#82294f')
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls): s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
logo = raw(f'sellos/{G}-logotipo-giro.svg').replace('<svg ', '<svg class="logo" ', 1)
LOGO_BASE = raw('svg/logotipo.svg').replace('<svg ', '<svg class="logo" ', 1)
SELLO = clean(raw(f'sellos/{G}-sello.svg'), 'sello-h')
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
ICO_G = clean(raw(f'iconos/{G}.svg'), 'ico')
DONDE = 'Estudio · Calle Ejemplo 000, Centro'
O = dict(
 n='Taller Barro Vivo', kick='Estudio de barro · Centro', desde=550, v=34, w=31, fav=.5, ras=['solo', 'ingles'], cupo='3–8',
 d='Estudio de barro en el centro. Enseñamos técnicas de los pueblos alfareros de los Valles Centrales en grupos pequeños; el barro y las piedras de bruñir son de la región.',
 guias=[('OR', 'Ofelia R.', 'Maestra alfarera · bruñido y barro rojo'), ('DM', 'Daniel M.', 'Ceramista · torno y engobes')],
 tours=[
  dict(id='brunido', n='Barro bruñido para principiantes', tipo='Principiantes', dur='3 h', dif='Desde 15 años', idi='Español · inglés', grupo=(3, 6), maestro='Ofelia R.',
       precio=[(1, 650)], salidas=[('Sáb 7 nov', '11:00', 2), ('Sáb 14 nov', '11:00', 6), ('Sáb 21 nov', '11:00', 6)], enc=DONDE, v=22, w=20,
       fotos=['03.jpg', '07.jpg', '13.jpg'],
       paradas=[('Conoce el barro', 'De dónde viene y cómo se prepara.', '03.jpg'), ('Modela tu pieza', 'Un cuenco o un vaso, con técnica de pellizco.', '07.jpg'),
                ('Bruñe con piedra', 'Pules con piedra de río hasta que brille.', '13.jpg'), ('Llévatela', 'Se quema en el horno y la recoges en 10 días.', '12.jpg')],
       tellevas='Tu pieza bruñida y quemada. La recoges en 10 días o te la enviamos dentro de la ciudad ($80).',
       inc=['Barro y herramientas', 'Quemado en horno', 'Café o agua del día'], noinc=['Envío fuera de la ciudad'], llevar=['Ropa que se pueda manchar', 'Uñas cortas ayudan']),
  dict(id='torno', n='Torno para principiantes', tipo='Principiantes', dur='2.5 h', dif='Desde 16 años', idi='Español', grupo=(2, 4), maestro='Daniel M.',
       precio=[(1, 800)], salidas=[('Vie 6 nov', '17:00', 4), ('Vie 13 nov', '17:00', 1)], enc=DONDE, v=8, w=7,
       fotos=['13.jpg', '03.jpg'],
       paradas=[('Centra el barro', 'El paso más difícil: lo practicas con ayuda.', '13.jpg'), ('Abre y levanta', 'Das forma a dos o tres piezas.', '03.jpg'),
                ('Retoca', 'Eliges tu mejor pieza y la dejas lista.', '07.jpg')],
       tellevas='Tu mejor pieza, esmaltada. Lista en 3 semanas.',
       inc=['Barro, torno y delantal', 'Esmalte y dos quemas'], noinc=['Envío'], llevar=['Ropa cómoda que se pueda manchar']),
  dict(id='engobes', n='Pintura sobre barro con engobes', tipo='Todos los niveles', dur='2 h', dif='Desde 12 años', idi='Español · inglés', grupo=(3, 8), maestro='Daniel M.',
       precio=[(1, 550)], salidas=[('Dom 8 nov', '10:00', 8), ('Dom 22 nov', '10:00', 7)], enc=DONDE, v=4, w=4,
       fotos=['07.jpg', '12.jpg'],
       paradas=[('Elige tu pieza', 'Plato o taza ya modelados.', '07.jpg'), ('Diseña', 'Grecas, flores o tu propio dibujo.', '12.jpg'), ('Pinta con engobes', 'Pigmentos de barro de colores.', '03.jpg')],
       tellevas='Tu pieza pintada y quemada. La recoges en 10 días.',
       inc=['Pieza, engobes y pinceles', 'Quemado en horno'], noinc=['Envío'], llevar=['Ideas o un dibujo de referencia (opcional)']),
 ],
 contacto=[('whatsapp', 'WhatsApp para apartar', '951 000 0007'), ('ig', 'Instagram', '@taller.ejemplo'), ('web', 'Sitio web', 'ejemplo.com')],
 posts=[('2026-10-30', '30 oct 2026', 'Abrimos fechas de noviembre. El del sábado 7 ya casi se llena.', '03.jpg'),
        ('2026-10-12', '12 oct 2026', 'Nuevo taller de pintura con engobes, también para niñas y niños desde 12 años.', '07.jpg')],
 piezas=[('03.jpg', 'Cuenco bruñido'), ('07.jpg', 'Taza con engobe'), ('13.jpg', 'Plato de torno'), ('12.jpg', 'Vaso bruñido'), ('02.jpg', 'Jarra pequeña'), ('11.jpg', 'Platos pintados')],
)
RAS = {k: dict(n=n, ico=RG.svg(k, cls='ico')) for k, (n, c, _) in RG.RASGOS.items()}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const O=' + json.dumps(O, ensure_ascii=False) + ';const RAS=' + json.dumps(RAS, ensure_ascii=False)
                     + ';const ICO_G=' + json.dumps(ICO_G) + ';const SELLO=' + json.dumps(SELLO) + ';')
        .replace('<!--LOGO-->', logo).replace('<!--LOGOBASE-->', LOGO_BASE).replace('%STAR%', STAR))
for k, x in N.items(): html = html.replace('%' + k + '%', x)
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
