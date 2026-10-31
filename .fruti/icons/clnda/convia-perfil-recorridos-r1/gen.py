# Convia · perfil de negocio: RECORRIDOS (r1). Patrón aprobado del hotel r2 con el tema del giro recorridos.
# El negocio es el OPERADOR; cada recorrido abre una hoja con paradas, precio según cuántos van, próximas salidas, qué incluye y punto de encuentro.
# Pedido del usuario (2026-10-31): imágenes de los lugares del tour, desde cuántas personas, precio, los lugares.
# Operador FICTICIO («Ejemplo»): fotos de relleno desenfocadas; precios, fechas, guías y contactos inventados. Las paradas son lugares públicos de Oaxaca.
# Uso: python3 gen.py <carpeta de salida con img/>. Las fotos no se guardan en el repo.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
sys.path.insert(0, F)
import rasgos as RG
G = 'recorridos'
T = json.load(open(os.path.join(F, 'tema.json'))); K = T['categorias'][G]
# punto de recorridos (#1baf7a) da 2.58:1 sobre papel: los puntos de la métrica usan el color de texto del giro.
N = dict(perla='#f9f9f7', sup='#ffffff', tinta='#1b1d1a', sec='#5c5f5b', linea='#e6e6e2', foto='#ececea', gtexto=K['texto'], gfondo=K['fondo'], gpunto=K['texto'], gdk='#0b5a3e')
def raw(p): return open(os.path.join(F, p)).read()
def clean(s, cls): s = s.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1); return re.sub(r' role="img" aria-label="[^"]*"', '', s, 1)
logo = raw(f'sellos/{G}-logotipo-giro.svg').replace('<svg ', '<svg class="logo" ', 1)
LOGO_BASE = raw('svg/logotipo.svg').replace('<svg ', '<svg class="logo" ', 1)
SELLO = clean(raw(f'sellos/{G}-sello.svg'), 'sello-h')
STAR = re.search(r'd="([^"]+)"', raw('svg/simbolo.svg')).group(1)
ICO_G = clean(raw(f'iconos/{G}.svg'), 'ico')
O = dict(
 n='Caminantes de Antequera', kick='Operador de recorridos · Centro', desde=300, v=61, w=55, fav=.47, ras=['solo', 'ingles', 'mascotas'],
 d='Recorridos a pie y en camioneta con grupos pequeños. Empezamos en 2019 caminando el centro al amanecer; hoy también salimos a los Valles Centrales.',
 guias=[('LM', 'Lucía M.', 'Español e inglés · historia y arquitectura'), ('RA', 'Rodrigo A.', 'Español, inglés y zapoteco básico · gastronomía y mercados')],
 tours=[
  dict(id='cantera', n='Caminata de cantera al amanecer', tipo='A pie', dur='2 h', dif='Fácil', idi='Español · inglés', grupo=(2, 10),
       precio=[(1, 450), (2, 300)], salidas=[('Dom 1 nov', '7:00', 6), ('Sáb 7 nov', '7:00', 9), ('Dom 8 nov', '7:00', 2)],
       enc='Atrio del Templo de Santo Domingo', v=28, w=25, fotos=['02.jpg', '12.jpg', '07.jpg'],
       paradas=[('Templo de Santo Domingo', 'La cantera verde con la primera luz.', '02.jpg'), ('Andador Macedonio Alcalá', 'Fachadas y portones antes de que abran.', '12.jpg'),
                ('Jardín Conzatti', 'Pausa y vista de los laureles.', '13.jpg'), ('Barrio de Jalatlaco', 'Calles empedradas y murales.', '07.jpg'), ('Café en el barrio', 'Termina con café de olla.', '03.jpg')],
       inc=['Guía bilingüe', 'Café de olla al final'], noinc=['Propinas']),
  dict(id='barrios', n='Barrios al atardecer: Jalatlaco y Xochimilco', tipo='A pie', dur='2.5 h', dif='Fácil', idi='Español · inglés', grupo=(2, 8),
       precio=[(1, 520), (2, 380)], salidas=[('Vie 6 nov', '17:30', 5), ('Vie 13 nov', '17:30', 8)],
       enc='Esquina del Templo de San Matías Jalatlaco', v=14, w=12, fotos=['07.jpg', '13.jpg'],
       paradas=[('Templo de San Matías Jalatlaco', 'Historia del barrio de curtidores.', '07.jpg'), ('Calles de Jalatlaco', 'Murales y casas de adobe.', '12.jpg'),
                ('Acueducto de San Felipe', 'Los arcos de Xochimilco.', '13.jpg'), ('Xochimilco', 'Talleres de tejedores y cierre con nieve.', '02.jpg')],
       inc=['Guía bilingüe', 'Nieve al final'], noinc=['Propinas']),
  dict(id='mitla', n='Día en Mitla y Hierve el Agua', tipo='En camioneta', dur='9 h', dif='Moderada (escaleras y terreno)', idi='Español · inglés', grupo=(2, 7),
       precio=[(1, 1800), (2, 1200), (4, 950)], salidas=[('Sáb 7 nov', '8:00', 3), ('Mar 10 nov', '8:00', 7), ('Sáb 14 nov', '8:00', 7)],
       enc='Frente al Teatro Macedonio Alcalá', v=19, w=18, fotos=['11.jpg', '02.jpg', '13.jpg'],
       paradas=[('Árbol del Tule', 'Parada corta en Santa María del Tule.', '12.jpg'), ('Teotitlán del Valle', 'Taller de tapetes de lana teñida.', '07.jpg'),
                ('Zona arqueológica de Mitla', 'Grecas de piedra; entrada incluida.', '13.jpg'), ('Comida en Mitla', 'Comida tradicional (no incluida).', '03.jpg'), ('Hierve el Agua', 'Cascadas petrificadas y pozas.', '11.jpg')],
       inc=['Transporte ida y vuelta', 'Guía bilingüe', 'Entradas a Mitla y Hierve el Agua', 'Agua'], noinc=['Comida', 'Propinas']),
 ],
 contacto=[('whatsapp', 'WhatsApp para apartar', '951 000 0004'), ('tel', 'Teléfono', '951 000 0005'), ('ig', 'Instagram', '@recorridos.ejemplo'), ('web', 'Sitio web', 'ejemplo.com')],
 posts=[('2026-10-29', '29 oct 2026', 'Salida especial a Hierve el Agua el 14 de noviembre: ya va la camioneta a la mitad.', '11.jpg'),
        ('2026-10-01', '1 oct 2026', 'Nuevo recorrido de barrios al atardecer, los viernes.', '07.jpg')],
)
RAS = {k: dict(n=n, ico=RG.svg(k, cls='ico')) for k, (n, c, _) in RG.RASGOS.items()}
html = open(os.path.join(D, 'plantilla.html')).read()
html = (html.replace('/*DATA*/', 'const O=' + json.dumps(O, ensure_ascii=False) + ';const RAS=' + json.dumps(RAS, ensure_ascii=False)
                     + ';const ICO_G=' + json.dumps(ICO_G) + ';const SELLO=' + json.dumps(SELLO) + ';')
        .replace('<!--LOGO-->', logo).replace('<!--LOGOBASE-->', LOGO_BASE).replace('%STAR%', STAR))
for k, x in N.items(): html = html.replace('%' + k + '%', x)
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
