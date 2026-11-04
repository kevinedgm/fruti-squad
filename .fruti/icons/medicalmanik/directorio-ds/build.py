# Directorio Manik · sistema de diseño (artifact Design System https://claude.ai/artifact/MTg2EAZVsJKZJRFCWGvAuj).
# Fuentes: manual del directorio v2 (manik-guia/guia.html, dirección bienestar), paquete de marca (manik-final/),
# prototipo bienestar v1 (directorio-c/plantilla.html) y panel de usuario r1 (estado del perfil, propuesta).
# Uso: python3 build.py <carpeta> → <carpeta>/project/
import json, os, re, sys, datetime
OUT = sys.argv[1]; H = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(H, '..')
B = {'simbolo.svg': ('2ebaab02bb8b4e269a3f6ab20613a454', 713), 'simbolo-1tinta.svg': ('94e996605f8ca1d79a9cd7b190125616', 782), 'simbolo-blanco.svg': ('ec1682c529c070a8b57f92353476fcc5', 777),
     'logotipo.svg': ('57085c856be07748a81086e18dacf543', 6012), 'logotipo-blanco.svg': ('49bf277b95bde2a6b92748b5f6decd97', 6014), 'logotipo-1tinta.svg': ('81db1d82ed0fbba7517a025894771c96', 6088),
     'logotipo-endoso.svg': ('74cd7f9a5841c79cfa0776a46e89518f', 21353), 'logotipo-vertical.svg': ('4a3c158f65047191a411bbd063306a82', 5697), 'app-icon.svg': ('649db9aac380d26c37d9608fa0ab7059', 781), 'favicon.svg': ('9c501f10d8c6e8b647898a08f4660f8d', 715)}
IC = {'apple': ('59c9026f4361579d6565e002d37aa394', 434), 'arrow-right': ('c02f1d3c46f69f3e9ab86d6e149cd24f', 285), 'baby': ('bffce7e670b218077617c587ca216e77', 501), 'badge-check': ('1efcc430f1d8581e1b217e25414e72cf', 441),
      'brain': ('c7725c8635a7359d0ae861fa9af3b491', 644), 'calendar-check': ('78a88b0185e49d97e7630d94b7ae4933', 400), 'clock': ('6e298b6e404e6880d3284d52df90d99b', 291), 'flower-2': ('06649d68a358dfe2e5b5d6143b3ed2fe', 541),
      'map-pin': ('8389860ec5dca7cc8b2708df2f5563d2', 381), 'message-circle-heart': ('21dc1a574f46993477af211b735ed84a', 503), 'scan-face': ('5be0694cbd64b077ce08b3219fcd45ef', 501), 'search': ('0235df5ca74a7d93874a616fc4ebfb4e', 296),
      'shield-check': ('b060ab8579ae54758d78049bac18ec9c', 440), 'stethoscope': ('8923094109ea7baf0b0f7d5c7ac2537a', 440),
      'phone': ('0e935b117994d67d75a44837f84fd38d', 450), 'sliders-horizontal': ('fa7b33777be5b1c760e35290bcd32274', 488), 'x': ('e6f628fb19fa4f195ab2773b1cfb2568', 274), 'arrow-left': ('8fe5734f360aabed7087f054d4ff2cf7', 285)}
AV = {'avatar-mujer.svg': ('5763706af92fba364ea1dc94fdb3780f', 993), 'avatar-hombre.svg': ('fac2739f409e7fb1f8d316a107789c08', 988), 'avatar-neutro.svg': ('e90aec85c1eaced6d13e1aef3c2cd58c', 894)}
B.update(AV)
blob = lambda n: f'/_blob/{B[n][0]}'
def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]; c = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)
P = dict(blanco='#FFFFFF', bruma='#F5FAFB', lavado='#EEF3F5', tinta='#14213D', muted='#4A5674', linea='#DCE4EA', control='#6B7590', cian='#009BB0', ui='#00788A', uih='#00606F',
         sky='#D3F0F4', sun='#FFEFD2', estrella='#E3A21C', exito='#15814B', exitos='#E7F5EE', onexito='#157B4A', azul='#234899', catc='#E4F5F7', catk='#FFF4E0', cata='#EEF2F8', calido='#6B4A00', icalido='#8A5A00',
         f0='#CDEEF2', f1='#FBE7C9', cicono='#7FDCE6', ctexto='#C7D2E4')
t = lambda n, v, u: {'name': n, 'value': v, 'usage': u}
W, Br, T = P['blanco'], P['bruma'], P['tinta']
col = [
 t('bruma', Br, 'Fondo de página y base de los halos de luz. También fondo de chips de datos (distancia, calificación) dentro de una ficha blanca.'),
 t('blanco', W, 'Tarjetas (ficha de médico, buscador, menú), botón de horario sin elegir y barra de navegación.'),
 t('lavado', P['lavado'], 'Fondo detrás de un marco de presentación o de una zona agrupada. No compite con «bruma».'),
 t('tinta', T, f"Todo el texto y el logotipo. {cr(T, W)}:1 sobre blanco, {cr(T, Br)}:1 sobre bruma. También fondo del botón «Buscar», del chip activo y de la franja de confianza."),
 t('muted', P['muted'], f"Texto secundario: especialidad, conteos, ayudas, etiquetas del buscador. {cr(P['muted'], W)}:1 sobre blanco, {cr(P['muted'], Br)}:1 sobre bruma."),
 t('linea', P['linea'], 'Bordes de tarjeta y de chips en reposo, y divisor del buscador. Decorativo: nunca el único borde de un control.'),
 t('linea-control', P['control'], f"Borde de controles al pasar el cursor y del selector de ancho: {cr(P['control'], W)}:1 sobre blanco."),
 t('cian', P['cian'], f"Cian Manik, el del pin: el sello y áreas grandes de marca. Blanco encima {cr(W, P['cian'])}:1: solo texto de 24 px o más; nunca botones."),
 t('cian-ui', P['ui'], f"Cian de interfaz: botón «Agendar», horarios, enlaces e iconos de acción. Blanco encima {cr(W, P['ui'])}:1; sobre blanco {cr(P['ui'], W)}:1."),
 t('cian-ui-hover', P['uih'], 'Hover y presionado de «cian-ui».'),
 t('luz-cian', P['sky'], f"Halo frío de los fondos y círculo detrás de iconos. Icono «cian-ui» encima {cr(P['ui'], P['sky'])}:1 (gráfico; no texto pequeño)."),
 t('luz-calida', P['sun'], f"Halo cálido, «Nuevo en Manik» y franja de anuncio. Tinta encima {cr(T, P['sun'])}:1."),
 t('estrella', P['estrella'], f"Solo la estrella de calificación ({cr(P['estrella'], W)}:1 con blanco): siempre con el número escrito en tinta al lado («4.9»)."),
 t('exito', P['exito'], f"Confirmaciones y mensajes de éxito sobre blanco ({cr(P['exito'], W)}:1). Sobre «exito-suave» se usa «on-exito-suave». Siempre con icono y texto."),
 t('exito-suave', P['exitos'], 'Fondo de la insignia «Cédula verificada».'),
 t('on-exito-suave', P['onexito'], f"Texto e icono de «Cédula verificada» sobre «exito-suave»: {cr(P['onexito'], P['exitos'])}:1. El verde del prototipo (#15814B) daba {cr(P['exito'], P['exitos'])}:1 y no cumplía AA."),
 t('categoria-cian', P['catc'], f"Fondo de tarjeta de categoría (1.ª de cada tres). Tinta encima {cr(T, P['catc'])}:1."),
 t('categoria-calida', P['catk'], f"Fondo de tarjeta de categoría (2.ª de cada tres). Tinta encima {cr(T, P['catk'])}:1."),
 t('categoria-azul', P['cata'], f"Fondo de tarjeta de categoría (3.ª de cada tres). Tinta encima {cr(T, P['cata'])}:1."),
 t('texto-calido', P['calido'], f"Etiqueta «Patrocinado» sobre blanco: {cr(P['calido'], W)}:1."),
 t('icono-calido', P['icalido'], f"Icono dentro del círculo de «luz-calida» ({cr(P['icalido'], P['sun'])}:1)."),
 t('foto-inicio', P['f0'], 'Inicio del degradado de fondo del avatar sin foto. Solo ahí.'),
 t('foto-fin', P['f1'], 'Fin del degradado de fondo del avatar sin foto.'),
 t('silueta', '#93AAB9', 'Silueta del avatar sin foto (cabeza y bata). Gráfico decorativo: el nombre del médico siempre va en texto al lado.'),
 t('silueta-pelo', '#7F97A7', 'Cabello de las siluetas de mujer y hombre.'),
 t('silueta-linea', '#E9F3F3', 'Solapas y estetoscopio sobre la silueta.'),
 t('confianza-icono', P['cicono'], f"Iconos sobre la franja de confianza (tinta): {cr(P['cicono'], T)}:1."),
 t('confianza-texto', P['ctexto'], f"Texto secundario sobre la franja de confianza: {cr(P['ctexto'], T)}:1."),
 t('azul-medicalmanik', P['azul'], 'Solo en el respaldo «de MedicalManik». Nunca en la interfaz del directorio.'),
 t('focus', '{cian-ui}', 'Anillo de foco de 3 px con 2 px de separación en todo control.'),
]
S_ = lambda n, fs, lh, fw, sample, usage, **k: dict(name=n, fontSize=fs, lineHeight=lh, fontWeight=fw, sample=sample, usage=usage, **k)
tokens = {'name': 'Directorio Manik', 'version': 1,
 'color': {'themes': [{'id': 'light', 'name': 'Claro'}], 'tokens': col},
 'type': {'fonts': [], 'families': {'display': '"Urbanist", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif', 'sans': '"Onest", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'},
  'groups': [
   {'name': 'Primaria · Urbanist', 'family': 'display', 'note': 'Titulares y mensajes cortos en 300, grandes y con el espaciado cerrado; nombres de médico, precios y categorías en 600. La misma letra de títulos de las herramientas de la clínica.', 'styles': [
     S_('display', '64px', '66px', 300, 'Cuidarte ya no tiene que ser difícil.', 'Titular de portada (escritorio). Una por pantalla; la palabra clave en 600.', letterSpacing='-0.035em'),
     S_('display-movil', '44px', '46px', 300, 'Cuidarte ya no tiene que ser difícil.', 'Titular de portada en celular.', letterSpacing='-0.035em'),
     S_('seccion', '40px', '44px', 400, 'Dermatólogas cerca de ti', 'Título de sección; la palabra clave en 600 («Busca por lo que sientes»).', letterSpacing='-0.03em'),
     S_('nombre', '22px', '26px', 600, 'Dra. Mariana Soto', 'Nombre del médico en la ficha.', letterSpacing='-0.01em'),
     S_('categoria', '19px', '22px', 600, 'Salud mental', 'Nombre de la categoría.'),
     S_('precio', '18px', '24px', 600, '$900', 'Precio de la consulta, alineado a la derecha del nombre.'),
     S_('telefono', '22px', '28px', 600, '222 555 0187', 'Número para agendar por teléfono; seleccionable entero.', fontVariantNumeric='tabular-nums')]},
   {'name': 'Secundaria · Onest', 'family': 'sans', 'note': 'Todo lo demás: textos, horarios, precios, direcciones y opiniones. 17 px de base; horarios con cifras tabulares para que se alineen.', 'styles': [
     S_('lead', '19px', '29px', 400, 'Encuentra a tu especialista, lee lo que opinan otros pacientes y agenda en un minuto.', 'Bajada del titular, en «muted».'),
     S_('body', '17px', '26px', 400, 'Revisamos la cédula profesional de cada médico antes de publicarlo.', 'Texto corrido. Base del directorio.'),
     S_('body-sm', '15px', '22px', 400, 'Dermatóloga · acné y lunares', 'Especialidad, atajos, conteos y textos de apoyo.'),
     S_('dato', '14px', '20px', 400, '4.9 · 312 opiniones', 'Chips de datos de la ficha: calificación, distancia.'),
     S_('etiqueta', '13px', '18px', 600, 'Qué necesitas', 'Etiquetas del buscador, «Patrocinado».'),
     S_('boton', '16px', '20px', 600, 'Agendar', 'Botones.'),
     S_('horario', '15px', '20px', 600, '16:30', 'Botones de horario, con cifras tabulares.', fontVariantNumeric='tabular-nums')]}]},
 'spacing': {'tokens': [t('space-1', '4px', 'Icono–texto en chips pequeños.'), t('space-2', '8px', 'Entre chips, horarios y atajos.'), t('space-3', '12px', 'Dentro de la barra; entre filas de la ficha.'),
   t('space-4', '16px', 'Padding de ficha; separación entre fichas; gutter mínimo en celular.'), t('space-6', '24px', 'Entre bloques de una sección.'), t('space-9', '36px', 'Padding vertical de sección en celular.'),
   t('space-11', '44px', 'Margen lateral de secciones en escritorio.'), t('space-14', '56px', 'Padding vertical de sección en escritorio.')]},
 'radius': {'tokens': [t('radius-icono', '14px', 'Cuadro del icono flotante y de la franja de confianza.'), t('radius-icono-cat', '16px', 'Cuadro blanco del icono de categoría.'), t('radius-foto', '20px', 'Foto 3:4 del médico (la interfaz redondea; la foto llega recta).'),
   t('radius-cat', '24px', 'Tarjeta de categoría.'), t('radius-ficha', '28px', 'Ficha de médico y franja de confianza; 24 px en celular.'), t('radius-pill', '999px', 'Buscador, botones, horarios, chips y atajos.')]},
 'shadow': {'tokens': [t('shadow-buscador', '0 1px 2px rgba(20, 33, 61, 0.06), 0 12px 32px rgba(20, 33, 61, 0.10)', 'El buscador sobre los halos de luz.'),
   t('shadow-hover', '0 12px 30px rgba(20, 33, 61, 0.08)', 'Ficha de médico al pasar el cursor.'), t('shadow-flotante', '0 10px 30px rgba(20, 33, 61, 0.14)', 'Tarjetitas flotantes sobre la foto de portada («Cita confirmada»).')]},
 'layout': {'tokens': [t('control-height', '42px', 'Chips, horarios y selectores (objetivo táctil ≥ 24 px de WCAG 2.2, holgado).'), t('boton-height', '48px', 'Botón «Agendar».'), t('buscar-height', '54px', 'Botón «Buscar» dentro del buscador.'),
   t('content-max', '1280px', 'Ancho máximo del directorio.'), t('foto-ratio', '0.75', 'Foto del médico 3:4 vertical.'),
   t('foto-ficha-movil', '72px', 'Ancho de la foto o avatar en la ficha compacta (celular, el 70 % del uso).'), t('foto-ficha', '132px', 'Ancho de la foto en la ficha amplia (contenedor de 560 px o más).'),
   t('ficha-amplia', '560px', 'Ancho de contenedor desde el que la ficha pasa a su versión amplia (container query).'),
   t('bp-tableta', '640px', 'Desde aquí: tableta (dos columnas de fichas, filtros en fila).'), t('bp-escritorio', '1024px', 'Desde aquí: escritorio (buscador en píldora doble, navegación completa).'),
   t('barra-inferior', '72px', 'Alto de la barra de acción fija del perfil en celular, más el inset inferior del dispositivo.')]}}
os.makedirs(f'{OUT}/project/components', exist_ok=True); os.chdir(f'{OUT}/project')
json.dump(tokens, open('tokens.json', 'w'), ensure_ascii=False, indent=1)
V = {x['name']: x['value'] for x in col}

def ico(n, cls='ico'):
    f = os.path.join(M, 'directorio-c', 'iconos', n + '.svg')
    s = open(f if os.path.exists(f) else os.path.join(H, 'iconos-extra', n + '.svg')).read()
    inner = ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse)[^>]*/>', s))
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{inner}</svg>'
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Onest:wght@400..700&display=swap">'
BASE = f'''html,body{{margin:0}}body{{background:var(--bruma,{Br});color:var(--tinta,{T});font:17px/26px var(--font-sans,"Onest",system-ui,sans-serif);padding:16px}}
.d{{font-family:var(--font-display,"Urbanist",sans-serif)}}.num{{font-variant-numeric:tabular-nums}}.mut{{color:var(--muted,{P['muted']})}}p{{margin:0}}
:focus-visible{{outline:3px solid var(--focus,{P['ui']});outline-offset:2px}}
.ico{{width:20px;height:20px;flex:none;display:block}}
.btn{{display:inline-flex;align-items:center;gap:8px;white-space:nowrap;border-radius:999px;font:600 16px/20px var(--font-sans,"Onest",sans-serif);border:0;cursor:pointer;padding:0 22px;min-height:var(--boton-height,48px)}}
.agendar{{background:var(--cian-ui,{P['ui']});color:#fff}}.agendar:hover{{background:var(--cian-ui-hover,{P['uih']})}}
.buscar{{background:var(--tinta,{T});color:#fff;min-height:var(--buscar-height,54px);padding:0 26px;font-size:17px}}.buscar:hover{{background:#000}}
.contorno{{background:var(--blanco,#fff);color:var(--tinta,{T});border:1.5px solid var(--tinta,{T});min-height:46px;padding:0 20px}}
.enlace{{background:none;color:var(--tinta,{T});padding:0;min-height:44px;text-decoration:underline;text-underline-offset:3px}}
.chip{{font:500 15px var(--font-sans,"Onest",sans-serif);color:var(--tinta,{T});background:var(--blanco,#fff);border:1.5px solid var(--linea,{P['linea']});border-radius:999px;min-height:var(--control-height,42px);padding:0 16px;cursor:pointer;display:inline-flex;align-items:center;gap:6px}}
.chip:hover{{border-color:var(--linea-control,{P['control']})}}.chip[aria-pressed="true"]{{background:var(--tinta,{T});border-color:var(--tinta,{T});color:#fff}}
.times{{display:flex;flex-wrap:wrap;gap:6px}}.times button{{font:600 15px var(--font-sans,"Onest",sans-serif);font-variant-numeric:tabular-nums;color:var(--cian-ui,{P['ui']});background:var(--blanco,#fff);border:1.5px solid var(--cian-ui,{P['ui']});border-radius:999px;min-height:var(--control-height,42px);padding:0 14px;cursor:pointer}}
.times button[aria-pressed="true"]{{background:var(--cian-ui,{P['ui']});color:#fff}}.times .mash{{border:0;background:none;color:var(--tinta,{T});padding:0 6px;text-decoration:underline;text-underline-offset:3px}}
.meta{{display:flex;flex-wrap:wrap;gap:6px}}.meta span{{display:inline-flex;align-items:center;gap:5px;font-size:14px;line-height:20px;background:var(--bruma,{Br});border-radius:999px;padding:4px 10px}}.meta span .ico{{width:15px;height:15px}}
.meta .v{{color:var(--on-exito-suave,{P['onexito']});font-weight:600;background:var(--exito-suave,{P['exitos']})}}.meta .st b{{color:var(--estrella,{P['estrella']});font-weight:400}}.meta .new{{background:var(--luz-calida,{P['sun']});font-weight:600}}'''
def page(grp, h, body, css=''):
    return f'<!-- @dsCard group="{grp}" height={h} -->\n<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>{BASE}{css}</style></head><body>{body}</body></html>'
DOC_CSS = f'''.lista{{container-type:inline-size;display:grid;gap:12px}}
.doc{{background:var(--blanco,#fff);border:1px solid var(--linea,{P['linea']});border-radius:24px;padding:14px;display:grid;grid-template-columns:var(--foto-ficha-movil,72px) minmax(0,1fr);gap:12px 14px;align-items:start;transition:box-shadow .2s ease}}
.doc:hover{{box-shadow:var(--shadow-hover,0 12px 30px rgba(20,33,61,.08))}}
.face{{border-radius:16px;aspect-ratio:3/4;overflow:hidden;background:linear-gradient(160deg,var(--foto-inicio,{P['f0']}),var(--foto-fin,{P['f1']}))}}.face img{{width:100%;height:100%;display:block;object-fit:cover}}
.hd{{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 10px;min-width:0}}.hd>div{{min-width:0;display:grid;gap:2px}}
.doc h3{{margin:0;font:600 20px/24px var(--font-display,"Urbanist",sans-serif);letter-spacing:-.01em}}.doc h3 a{{color:inherit;text-decoration:none}}.doc h3 a:hover{{text-decoration:underline}}
.spec{{color:var(--muted,{P['muted']});font-size:15px;line-height:22px}}.lugar{{display:flex;align-items:center;gap:5px;font-size:15px;line-height:22px;font-weight:600}}.lugar .ico{{width:16px;height:16px;color:var(--cian-ui,{P['ui']})}}
.price{{font:600 18px/24px var(--font-display,"Urbanist",sans-serif);white-space:nowrap}}.price small{{display:block;font:400 13px/18px var(--font-sans,"Onest",sans-serif);color:var(--muted,{P['muted']})}}
.bd{{grid-column:1/-1;display:grid;gap:10px;min-width:0}}
.when{{font-size:15px;line-height:22px;font-weight:600}}.when span{{font-weight:400;color:var(--muted,{P['muted']})}}
.mash{{font:600 15px var(--font-sans,"Onest",sans-serif);color:var(--tinta,{T});background:none;border:0;min-height:var(--control-height,42px);padding:0 6px;text-decoration:underline;text-underline-offset:3px;cursor:pointer}}
.tel{{font:600 22px/28px var(--font-display,"Urbanist",sans-serif);font-variant-numeric:tabular-nums;user-select:all}}
.acc{{display:flex;flex-wrap:wrap;gap:8px}}.acc .btn{{flex:1 1 140px;justify-content:center;text-decoration:none}}
.mas{{font-size:15px;line-height:22px;color:var(--tinta,{T});font-weight:600;text-underline-offset:3px;padding:4px 0}}.mas span{{font-weight:400;color:var(--muted,{P['muted']})}}
@container (min-width:560px){{.doc{{grid-template-columns:var(--foto-ficha,132px) minmax(0,1fr);gap:8px 18px;padding:16px;border-radius:var(--radius-ficha,28px)}}.face{{grid-row:1/3;border-radius:var(--radius-foto,20px)}}.bd{{grid-column:2}}.doc h3{{font-size:22px;line-height:26px}}.price{{text-align:right}}.acc .btn{{flex:0 0 auto}}}}
@media (prefers-reduced-motion:reduce){{.doc{{transition:none}}}}
.marco{{display:grid;gap:8px}}.marco>b{{font:600 13px/18px var(--font-sans,"Onest",sans-serif);color:var(--muted,{P['muted']});letter-spacing:.04em;text-transform:uppercase}}.cel{{max-width:390px}}'''
def ficha(av, nombre, spec, lugar, km, precio, meta, cuerpo, mas=None):
    extra = f'<a class="mas" href="#consultorios">Atiende en {mas} consultorios <span>· ver todos</span></a>' if mas else ''
    return (f'<article class="doc"><div class="face"><img src="{blob("avatar-" + av + ".svg")}" alt="Sin foto: {nombre}"></div>'
            f'<div class="hd"><div><h3><a href="#perfil">{nombre}</a></h3><p class="spec">{spec}</p><p class="lugar">{ico("map-pin")}{lugar} · {km} km</p></div><p class="price"><small>Consulta</small>{precio}</p></div>'
            f'<div class="bd"><div class="meta">{meta}</div>{cuerpo}{extra}</div></article>')
ST = lambda r, n: f'<span class="st"><b aria-hidden="true">★</b> {r} · {n} opiniones</span>'
KM = lambda k, c=None: f'<span>{ico("map-pin")}{(c + " · ") if c else ""}{k} km</span>'
VER = f'<span class="v">{ico("badge-check")}Cédula verificada</span>'
TIMES = lambda hs, sel=None, mas=False: '<div class="times" role="group" aria-label="Horarios">' + ''.join(f'<button type="button" class="num" aria-pressed="{"true" if h == sel else "false"}">{h}</button>' for h in hs) + ('<button type="button" class="mash">Más horarios</button>' if mas else '') + '</div>'
AGENDAR = f'<div class="acc"><button type="button" class="btn agendar">Agendar {ico("arrow-right")}</button></div>'
LLAMAR = f'<span class="tel">222 555 0187</span><div class="acc"><a class="btn agendar" href="tel:+522225550187">{ico("phone")}Llamar</a><button type="button" class="btn contorno">Copiar número</button></div>'
comps = {}
comps['Boton'] = ('Acciones', 96, f'<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center"><button class="btn agendar">Agendar {ico("arrow-right")}</button><button class="btn buscar">Buscar</button><a class="btn agendar" href="tel:+522225550187" style="text-decoration:none">{ico("phone")}Llamar</a><button class="btn contorno">Copiar número</button><button class="btn enlace">Ver promoción</button></div>', '',
 'Botones del directorio: todos en píldora; el color dice qué tipo de acción es.\n\n- **Agendar** (`cian-ui`, blanco encima 5.2:1, 48 px): la acción que lleva a una cita. Una por ficha.\n- **Llamar** (mismo estilo que Agendar, icono phone): acción principal de un consultorio que agenda por teléfono. Enlace `tel:` con el número en formato internacional (+52…); el número también va escrito.\n- En celular, los botones de la ficha van a todo el ancho; en la barra de acción del perfil, a la derecha.\n- **Buscar** (`tinta`, 54 px): solo dentro del buscador.\n- **Contorno** (blanco con borde y texto `tinta`): acciones secundarias como «Copiar número».\n- **Enlace**: texto `tinta` subrayado para «Ver promoción», «Ver perfil».\n- Nunca botones en `cian` (3.3:1 con blanco): ese cian es del sello.\n- Foco: anillo `focus` de 3 px. El consumidor provee: verbo + objeto, carga y `aria-disabled`.')
PH_CSS = f'''.fila{{display:flex;gap:24px;flex-wrap:wrap;align-items:start}}.marco{{display:grid;gap:8px;flex:1 1 300px;max-width:390px}}.marco>b{{font:600 13px/18px var(--font-sans,"Onest",sans-serif);color:var(--muted,{P['muted']});letter-spacing:.04em;text-transform:uppercase}}
.tel-f{{border:1px solid var(--linea,{P['linea']});border-radius:28px;overflow:hidden;background:var(--blanco,#fff);position:relative;min-height:420px;display:flex;flex-direction:column}}
.halo{{background:radial-gradient(70% 90% at 0% 0%,var(--luz-cian,{P['sky']}),transparent 70%),radial-gradient(60% 80% at 100% 20%,var(--luz-calida,{P['sun']}),transparent 70%),var(--bruma,{Br})}}
.sheet{{margin-top:auto;background:var(--blanco,#fff);border-radius:24px 24px 0 0;box-shadow:0 -8px 30px rgba(20,33,61,.12);padding:10px 16px calc(16px + env(safe-area-inset-bottom,0px));display:grid;gap:14px}}.asa{{justify-self:center;width:40px;height:4px;border-radius:2px;background:var(--linea,{P['linea']})}}
.velo{{position:absolute;inset:0;background:rgba(20,33,61,.32);display:flex;flex-direction:column}}
.ib{{width:44px;height:44px;display:grid;place-items:center;border:0;background:none;color:var(--tinta,{T});border-radius:50%;cursor:pointer}}.ib:hover{{background:var(--bruma,{Br})}}'''
comps['Buscador'] = ('Búsqueda', 600, f'''<div class="fila">
<div class="marco"><b>Celular · cerrado</b><div class="tel-f halo" style="min-height:300px;padding:20px 16px;gap:16px;display:grid;align-content:start"><h2 class="d" style="margin:0;font:300 34px/38px var(--font-display,'Urbanist',sans-serif);letter-spacing:-.03em">Cuidarte ya no tiene que ser <b style="font-weight:600">difícil</b>.</h2>
<button class="campo" type="button" aria-haspopup="dialog">{ico("search")}<span><b>¿Qué necesitas?</b><small>Cerca de Angelópolis, Puebla</small></span></button></div></div>
<div class="marco"><b>Celular · abierto (pantalla completa)</b><form class="tel-f full" role="search" onsubmit="return false"><div class="tb"><button class="ib" type="button" aria-label="Volver">{ico("arrow-left")}</button><b class="d">Buscar</b></div>
<div class="fs"><label for="q1">Qué necesitas</label><input id="q1" value="Dermatól" autocomplete="off"></div><div class="fs"><label for="w1">Dónde</label><input id="w1" value="Angelópolis, Puebla" autocomplete="off"><button type="button" class="ubi">{ico("map-pin")}Usar mi ubicación</button></div>
<ul class="sug" aria-label="Sugerencias"><li><a href="#r">{ico("search")}<span><b>Dermatól</b>ogía · especialidad</span></a></li><li><a href="#r">{ico("scan-face")}<span>Manchas en la piel · lo que sientes</span></a></li><li><a href="#r">{ico("stethoscope")}<span>Dra. Daniela <b>Dermatól</b>oga Ruiz</span></a></li></ul>
<button class="btn buscar" type="submit">Buscar</button></form></div></div>
<div class="marco" style="max-width:none;margin-top:24px"><b>Escritorio · 1024 px o más</b><form class="search" role="search" onsubmit="return false"><div class="f">{ico("search")}<div><label for="q">Qué necesitas</label><input id="q" value="Dermatóloga" autocomplete="off"></div></div><div class="f">{ico("map-pin")}<div><label for="w">Dónde</label><input id="w" value="Angelópolis, Puebla" autocomplete="off"></div></div><button class="btn buscar" type="submit">Buscar</button></form></div>''',
 PH_CSS + f'''.campo{{display:flex;align-items:center;gap:12px;width:100%;text-align:left;background:var(--blanco,#fff);border:0;border-radius:999px;padding:10px 18px;min-height:60px;box-shadow:var(--shadow-buscador,0 12px 32px rgba(20,33,61,.10));cursor:pointer;color:var(--tinta,{T})}}.campo .ico{{color:var(--cian-ui,{P['ui']})}}.campo b{{display:block;font:600 17px/22px var(--font-sans,"Onest",sans-serif)}}.campo small{{display:block;font-size:14px;line-height:20px;color:var(--muted,{P['muted']})}}
.full{{padding:8px 16px 16px;gap:12px}}.tb{{display:flex;align-items:center;gap:6px}}.tb b{{font-size:18px}}.fs{{display:grid;gap:4px;border:1.5px solid var(--linea-control,{P['control']});border-radius:18px;padding:8px 14px}}.fs label{{font-size:13px;line-height:18px;font-weight:600;color:var(--muted,{P['muted']})}}.fs input{{border:0;outline:0;font:500 17px var(--font-sans,"Onest",sans-serif);color:var(--tinta,{T});padding:0;min-width:0}}.fs:focus-within{{outline:3px solid var(--focus,{P['ui']});outline-offset:2px}}
.ubi{{justify-self:start;display:inline-flex;align-items:center;gap:6px;border:0;background:none;color:var(--cian-ui,{P['ui']});font:600 15px var(--font-sans,"Onest",sans-serif);min-height:36px;padding:0;cursor:pointer}}.ubi .ico{{width:16px;height:16px}}
.sug{{list-style:none;margin:0;padding:0;display:grid}}.sug a{{display:flex;align-items:center;gap:10px;min-height:48px;color:var(--tinta,{T});text-decoration:none;font-size:16px;border-bottom:1px solid var(--linea,{P['linea']})}}.sug .ico{{color:var(--muted,{P['muted']});width:18px;height:18px}}.sug b{{font-weight:700}}.full .buscar{{margin-top:auto;justify-content:center}}
.search{{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr) auto;align-items:center;background:var(--blanco,#fff);border-radius:999px;padding:8px;box-shadow:var(--shadow-buscador,0 12px 32px rgba(20,33,61,.10));max-width:640px;border:1px solid var(--linea,{P['linea']})}}
.f{{display:flex;align-items:center;gap:10px;padding:6px 16px;min-width:0}}.f+.f{{border-left:1px solid var(--linea,{P['linea']})}}.f .ico{{color:var(--cian-ui,{P['ui']})}}.f div{{display:grid;min-width:0}}
.f label{{font-size:13px;line-height:18px;font-weight:600;color:var(--muted,{P['muted']})}}.f input{{border:0;outline:0;font:500 17px var(--font-sans,"Onest",sans-serif);color:var(--tinta,{T});background:none;padding:0;min-width:0;width:100%}}.search:focus-within{{outline:3px solid var(--focus,{P['ui']});outline-offset:3px}}
@media (max-width:560px){{.search{{grid-template-columns:1fr;border-radius:26px;padding:10px}}.f+.f{{border-left:0;border-top:1px solid var(--linea,{P['linea']})}}.buscar{{justify-content:center}}}}''',
 'Buscador. **Celular primero:** un solo campo que abre la búsqueda a pantalla completa; en escritorio, la píldora doble.\n\n- **Celular, cerrado:** un botón-campo blanco de 60 px bajo el titular: «¿Qué necesitas?» y, debajo, el lugar actual («Cerca de Angelópolis, Puebla»). Abre la búsqueda (`aria-haspopup="dialog"`).\n- **Celular, abierto:** pantalla completa con «Volver», los dos campos con etiqueta visible, «Usar mi ubicación», sugerencias que marcan en negrita lo escrito (especialidad, síntoma o médico) y «Buscar» a todo el ancho abajo, al alcance del pulgar. El teclado no tapa el botón: la pantalla se ajusta a la altura visible.\n- **Tableta:** igual que celular en vertical; en horizontal, la píldora doble.\n- **Escritorio (≥ 1024 px):** píldora con «Qué necesitas» y «Dónde», iconos en `cian-ui`, botón «Buscar» en `tinta`, sombra `shadow-buscador`, foco en toda la píldora.\n- El consumidor provee: valores, sugerencias, ubicación (con permiso) y la acción de búsqueda (`role="search"`).')
comps['BarraFiltros'] = ('Búsqueda', 560, f'''<div class="fila">
<div class="marco"><b>Celular · resultados</b><div class="tel-f"><div class="rh"><h2 class="d"><b>Dermatólogas</b> cerca de ti</h2><p class="mut">12 en Angelópolis</p></div><div class="bf"><button type="button" class="chip" aria-haspopup="dialog">{ico("sliders-horizontal")}Filtros <span class="n">2</span></button><button type="button" class="chip" aria-haspopup="dialog">Más cerca</button></div><div class="ph"></div><div class="ph"></div></div></div>
<div class="marco"><b>Celular · hoja de filtros abierta</b><div class="tel-f"><div class="velo"><div class="sheet" role="dialog" aria-label="Filtros"><span class="asa" aria-hidden="true"></span><div class="sh"><b class="d">Filtros</b><button class="ib" type="button" aria-label="Cerrar">{ico("x")}</button></div>
<fieldset><legend>Cómo agendar</legend><div class="row"><button type="button" class="chip" aria-pressed="true">Agenda en Manik</button><button type="button" class="chip" aria-pressed="true">Con lugar hoy</button></div></fieldset>
<fieldset><legend>Precio de consulta</legend><div class="row"><button type="button" class="chip" aria-pressed="false">Hasta $500</button><button type="button" class="chip" aria-pressed="false">Hasta $800</button><button type="button" class="chip" aria-pressed="false">Hasta $1,200</button></div></fieldset>
<div class="pie"><button type="button" class="btn enlace">Limpiar</button><button type="button" class="btn agendar">Ver 5 especialistas</button></div></div></div></div></div></div>''',
 PH_CSS + f'''.rh{{padding:18px 16px 8px}}.rh h2{{margin:0;font:400 28px/32px var(--font-display,"Urbanist",sans-serif);letter-spacing:-.02em}}.rh h2 b{{font-weight:600}}.rh p{{font-size:15px}}
.bf{{position:sticky;top:0;display:flex;gap:8px;padding:8px 16px 12px;background:var(--blanco,#fff);border-bottom:1px solid var(--linea,{P['linea']})}}.n{{display:inline-grid;place-items:center;min-width:22px;height:22px;border-radius:11px;background:var(--tinta,{T});color:#fff;font-size:13px;font-weight:700}}
.ph{{margin:12px 16px 0;height:110px;border-radius:24px;background:var(--bruma,{Br});border:1px solid var(--linea,{P['linea']})}}
.sh{{display:flex;justify-content:space-between;align-items:center}}.sh b{{font-size:20px}}fieldset{{border:0;margin:0;padding:0;display:grid;gap:8px}}legend{{font:600 15px/22px var(--font-sans,"Onest",sans-serif);padding:0;margin-bottom:8px}}.row{{display:flex;flex-wrap:wrap;gap:8px}}
.pie{{display:flex;gap:12px;align-items:center;justify-content:space-between;border-top:1px solid var(--linea,{P['linea']});padding-top:12px}}.pie .agendar{{flex:1;justify-content:center}}''',
 'Filtros y orden en celular y tableta: un botón fijo que abre una hoja inferior, en lugar de una fila de chips que se sale de la pantalla.\n\n- **Barra:** bajo el título de resultados, fija al desplazarse (`position: sticky`): «Filtros» con el número de filtros activos y el orden actual («Más cerca»). Ambos abren hojas inferiores (`aria-haspopup="dialog"`).\n- **Hoja:** esquinas de 24 px arriba, asa, título y cerrar (44 px); grupos con `fieldset`/`legend`: «Cómo agendar» (Agenda en Manik, Con lugar hoy) y «Precio de consulta» (Hasta $500, $800, $1,200); chips con `aria-pressed`.\n- **Pie:** «Limpiar» y el botón principal con el resultado en vivo («Ver 5 especialistas»): el paciente sabe qué obtiene antes de cerrar. Respeta el inset inferior del dispositivo.\n- Los filtros se evalúan **por consultorio** (ver README, Consultorios).\n- **Escritorio (≥ 1024 px):** los mismos filtros como fila de chips sobre la lista (ver Chip).\n- Cierra con «Cerrar», tocando fuera o con Escape; el foco vuelve al botón que la abrió.\n- El consumidor provee: filtros activos, orden, conteo de resultados para cada combinación.')
comps['BarraAccion'] = ('Médico', 330, f'''<div class="fila">
<div class="marco"><b>Perfil · agenda en Manik</b><div class="tel-f" style="min-height:180px"><div class="ph"></div><div class="ba"><div><b class="d">$900</b><span>Consulta · Angelópolis</span></div><button type="button" class="btn agendar">Agendar {ico("arrow-right")}</button></div></div></div>
<div class="marco"><b>Perfil · por teléfono</b><div class="tel-f" style="min-height:180px"><div class="ph"></div><div class="ba"><div><b class="d">$750</b><span>Consulta · Centro</span></div><a class="btn agendar" href="tel:+522225550187" style="text-decoration:none">{ico("phone")}Llamar</a></div></div></div></div>''',
 PH_CSS + f'''.ph{{margin:16px;height:80px;border-radius:24px;background:var(--bruma,{Br});border:1px solid var(--linea,{P['linea']})}}.ba{{margin-top:auto;display:flex;align-items:center;justify-content:space-between;gap:12px;background:var(--blanco,#fff);border-top:1px solid var(--linea,{P['linea']});box-shadow:0 -6px 20px rgba(20,33,61,.08);min-height:var(--barra-inferior,72px);padding:12px 16px calc(12px + env(safe-area-inset-bottom,0px))}}
.ba div{{display:grid}}.ba b{{font-size:20px;line-height:24px;font-weight:600}}.ba span{{font-size:14px;line-height:20px;color:var(--muted,{P['muted']})}}''',
 'Barra de acción fija al pie del perfil del médico en celular y tableta: el precio y la acción siempre al alcance del pulgar.\n\n- Izquierda: precio del consultorio elegido en `precio` y «Consulta · <consultorio>»; derecha: la acción de ese consultorio: «Agendar» o «Llamar» (`tel:`).\n- Al cambiar de consultorio en el perfil, la barra cambia con él: precio y acción nunca se mezclan entre consultorios.\n- 72 px (`barra-inferior`) más el inset inferior del dispositivo; fondo blanco, borde superior `linea` y sombra suave hacia arriba. El contenido de la página deja ese espacio libre al final.\n- **Escritorio:** no hay barra; la acción vive en la columna del consultorio elegido.\n- El consumidor provee: consultorio elegido, precio, forma de agendar y teléfono.')
comps['Chip'] = ('Búsqueda', 150, f'<div class="row" role="group" aria-label="Filtros"><button type="button" class="chip" aria-pressed="true">Con lugar hoy</button><button type="button" class="chip" aria-pressed="false">Agenda en Manik</button><button type="button" class="chip" aria-pressed="false">Hasta $800</button></div><div class="row quick"><a href="#res">{ico("scan-face")}Piel</a><a href="#res">{ico("brain")}Salud mental</a><a href="#res">{ico("apple")}Nutrición</a><a href="#res">{ico("flower-2")}Ginecología</a></div>',
 f'''body{{display:grid;gap:16px}}.row{{display:flex;flex-wrap:wrap;gap:8px}}.quick a{{display:inline-flex;align-items:center;gap:8px;text-decoration:none;color:var(--tinta,{T});background:rgba(255,255,255,.85);border:1px solid var(--linea,{P['linea']});border-radius:999px;padding:7px 14px 7px 10px;font-weight:500;font-size:15px;line-height:22px}}
.quick a .ico{{width:18px;height:18px;color:var(--cian-ui,{P['ui']})}}.quick a:hover{{background:var(--blanco,#fff);border-color:var(--linea-control,{P['control']})}}''',
 'Dos píldoras de búsqueda con papeles distintos.\n\n- **Filtro** (`button` con `aria-pressed`): «Con lugar hoy», «Agenda en Manik», «Hasta $800». Activo: fondo `tinta`, texto blanco. 42 px.\n- **Atajo** (enlace): debajo del buscador; icono en `cian-ui` y la categoría en palabras del paciente («Piel», no «Dermatología»).\n- Borde `linea` en reposo y `linea-control` al pasar el cursor.\n- En celular y tableta, los filtros viven en la hoja de BarraFiltros; los atajos se quedan bajo el buscador y pasan a la línea siguiente, nunca se salen de la pantalla.\n- El consumidor provee: etiqueta, estado y destino.')
cats = [('scan-face', 'Piel', 'Dermatología'), ('brain', 'Salud mental', 'Psicología y psiquiatría'), ('apple', 'Alimentación', 'Nutrición'), ('flower-2', 'Salud íntima', 'Ginecología y urología'), ('baby', 'Niñas y niños', 'Pediatría'), ('stethoscope', 'Chequeo general', 'Medicina general')]
comps['TarjetaCategoria'] = ('Búsqueda', 400, '<div class="cats">' + ''.join(f'<a class="cat" href="#res"><span class="ic">{ico(i)}</span><span><b>{a}</b><small>{b}</small></span></a>' for i, a, b in cats) + '</div>',
 f'''.cats{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px}}.cat{{display:grid;gap:26px;align-content:space-between;text-decoration:none;color:var(--tinta,{T});border-radius:var(--radius-cat,24px);padding:18px;min-height:168px;transition:transform .2s ease}}
.cat:nth-child(3n+1){{background:var(--categoria-cian,{P['catc']})}}.cat:nth-child(3n+2){{background:var(--categoria-calida,{P['catk']})}}.cat:nth-child(3n){{background:var(--categoria-azul,{P['cata']})}}.cat:hover{{transform:translateY(-3px)}}
.cat .ic{{display:grid;place-items:center;width:48px;height:48px;border-radius:var(--radius-icono-cat,16px);background:var(--blanco,#fff);color:var(--cian-ui,{P['ui']})}}.cat .ico{{width:22px;height:22px}}.cat b{{font:600 19px/22px var(--font-display,"Urbanist",sans-serif);display:block}}.cat small{{color:var(--muted,{P['muted']});font-size:14px;line-height:20px}}
@media (prefers-reduced-motion:reduce){{.cat{{transition:none}}.cat:hover{{transform:none}}}}''',
 'Tarjeta de categoría de «Busca por lo que sientes»: la entrada para quien no sabe a qué especialista ir.\n\n- Nombre en palabras del paciente (`categoria`, Urbanist 600) y la especialidad debajo en «muted».\n- Fondos que rotan cada tres: `categoria-cian`, `categoria-calida`, `categoria-azul`. Icono Lucide en `cian-ui` dentro de un cuadro blanco de 48 px.\n- Seis por fila en escritorio, tres en tableta y dos en celular. Al pasar el cursor sube 3 px (sin movimiento con `prefers-reduced-motion`).\n- El consumidor provee: icono, nombre, especialidad y destino.')
f1 = ficha('mujer', 'Dra. Mariana Soto', 'Dermatóloga · acné y lunares', 'Angelópolis', '1.8', '$900', ST('4.9', 312) + VER, '<p class="when">Hoy <span>· toca una hora</span></p>' + TIMES(['16:30', '17:00', '18:30'], '17:00', True) + AGENDAR, 2)
f2 = ficha('mujer', 'Dra. Fernanda Quiroz', 'Dermatóloga · cosmética', 'Centro', '3.1', '$750', ST('4.7', 41) + VER, '<p class="when">Agenda por teléfono <span>· llama y pide tu cita</span></p>' + LLAMAR)
f3 = ficha('hombre', 'Dr. Iván Hernández', 'Dermatólogo · alergias de piel', 'La Paz', '4.0', '$700', '<span class="new">Nuevo en Manik</span>' + VER, '<p class="when">Lunes 3 <span>· su primer día libre</span></p>' + TIMES(['10:00', '11:00']) + AGENDAR)
comps['FichaMedico'] = ('Resultados', 1560, f'<div class="marco cel"><b>Celular · 390 px</b><div class="lista">{f1}{f2}{f3}</div></div><div class="marco" style="margin-top:24px"><b>Tableta y escritorio · contenedor de 560 px o más</b><div class="lista" style="max-width:720px">{f1}</div></div>', DOC_CSS,
 'La ficha del médico en los resultados. **Celular primero** (70 % del uso): la versión compacta es la principal y la amplia sale del ancho del contenedor (container query a 560 px), no del dispositivo.\n\n- **Lo que cabe sin hacer scroll en celular**, en este orden: nombre y especialidad; consultorio y distancia; «Consulta» + precio; calificación y cédula en una línea; cuándo; hasta 3 horarios + «Más horarios»; acción a todo el ancho. Unas dos fichas por pantalla de 390 × 844.\n- **Compacta** (< 560 px): avatar de 72 px (`foto-ficha-movil`) junto a la cabecera; el resto ocupa todo el ancho; botones a todo el ancho; radio 24.\n- **Amplia** (≥ 560 px): foto de 132 px a la izquierda; precio alineado a la derecha; botones a su ancho; radio `radius-ficha`.\n- **Precio y forma de agendar son de cada consultorio** (decisión 2026-11-04): la ficha muestra el consultorio más cercano que cumpla los filtros y nunca mezcla datos de dos. Con más de uno: «Atiende en N consultorios · ver todos».\n- **Agenda en Manik:** horarios + «Agendar». La cita es presencial; solo se reserva desde Manik. Nunca «En línea»: se lee como consulta por video. **Por teléfono:** el número visible y **«Llamar»** como acción principal (enlace `tel:` con el número en formato internacional) + «Copiar número» secundario. **Nuevo:** «Nuevo en Manik» en lugar de la calificación.\n- Sin foto, avatar de silueta (ver FotoMedico).\n- El consumidor provee: médico, especialidad, tipo de avatar o foto, consultorio mostrado (nombre, distancia, precio, forma de agendar, horarios o teléfono), número de consultorios, calificación y verificación. Datos de ejemplo.')
comps['Horarios'] = ('Resultados', 120, '<p class="when" style="font-size:15px;font-weight:600;margin-bottom:8px">Hoy <span class="mut" style="font-weight:400">· toca una hora</span></p>' + TIMES(['9:30', '11:30', '12:00'], '11:30', True), '.mash{font:600 15px var(--font-sans,"Onest",sans-serif);color:var(--tinta,#14213D);background:none;border:0;min-height:42px;padding:0 6px;text-decoration:underline;text-underline-offset:3px;cursor:pointer}',
 'Horarios disponibles como botones en píldora: tocar uno lo elige; «Agendar» confirma.\n\n- Contorno y texto `cian-ui`; elegido: fondo `cian-ui`, texto blanco. `aria-pressed` dice cuál está elegido.\n- Cifras tabulares (`horario`) para que las horas se alineen; formato 24 h sin ceros a la izquierda (9:30).\n- Arriba, el día en palabras («Hoy», «Mañana», «Lunes 3») y una ayuda en «muted».\n- 42 px de alto: holgado para el dedo. En la ficha, máximo 3 horarios y «Más horarios» (abre el perfil en la agenda de ese consultorio); en celular nunca una fila que se salga de la pantalla.\n- El consumidor provee: fecha, horarios y el elegido.')
comps['Insignias'] = ('Resultados', 100, f'<div class="meta">{ST("4.9", 312)}{KM("1.8")}{VER}<span class="new">Nuevo en Manik</span></div>', '',
 'Chips de datos dentro de la ficha. Cada uno es un dato, no una acción.\n\n- **Calificación:** estrella `estrella` (solo gráfico, 2.2:1) y el número escrito en tinta: «4.9 · 312 opiniones».\n- **Distancia:** icono map-pin y «1.8 km».\n- **Cédula verificada:** `exito` sobre `exito-suave`, icono badge-check. Solo cuando Manik revisó la cédula.\n- **Nuevo en Manik:** `luz-calida`, en lugar de la calificación mientras no hay opiniones.\n- Fondo `bruma` para los neutros; 14 px (`dato`).\n- El consumidor provee: calificación y número de opiniones, distancia, verificación.')
comps['FotoMedico'] = ('Resultados', 330, '<div class="fl">' + ''.join(f'<figure><div class="face"><img src="{blob("avatar-" + k + ".svg")}" alt="{alt}"></div><figcaption>{cap}</figcaption></figure>' for k, alt, cap in (('mujer', 'Sin foto: Dra. Lucía Herrera', 'Mujer · «Dra.»'), ('hombre', 'Sin foto: Dr. Iván Hernández', 'Hombre · «Dr.»'), ('neutro', 'Sin foto: Alex Ramos, psicología', 'Neutro · sin dato'))) + '<div class="reg"><b class="d">Retrato del médico</b><p>Vertical 3:4, cara centrada. Mínimo 900 × 1200 px al subirla; se sirve en WebP a 176 × 234 en la ficha de celular (≤ 20 KB) y a 480 × 640 en el perfil y la ficha amplia (≤ 120 KB). Luz natural, fondo liso y claro, sin filtros. La foto llega recta: la interfaz pone las esquinas de 20 px.</p></div></div>',
 DOC_CSS + f'''.fl{{display:flex;gap:16px;flex-wrap:wrap;align-items:end}}figure{{margin:0;display:grid;gap:8px;width:120px}}figcaption{{font-size:13px;line-height:18px;color:var(--muted,{P['muted']})}}.reg{{flex:1;min-width:220px;display:grid;gap:6px}}.reg b{{font-size:18px}}.reg p{{font-size:15px;line-height:22px;color:var(--muted,{P['muted']})}}''',
 'La cara del médico en la ficha y el perfil.\n\n- **Con foto:** 3:4 vertical, `radius-foto`. Reglas de la sección Fotografía: mínimo 900 × 1200 px; servida en WebP a 176 × 234 en la ficha de celular (≤ 20 KB, el 70 % del uso) y a 480 × 640 en perfil y ficha amplia (≤ 120 KB), con `srcset`, luz natural, fondo liso, sin filtros ni retoque que cambie rasgos.\n- **Sin foto: avatar de silueta** (decisión 2026-11-04): médica o médico con bata y estetoscopio, en `silueta` sobre el degradado `foto-inicio` → `foto-fin`, mismo formato 3:4. Archivos en el grupo «Avatares».\n- Cuál silueta: «Dra.» → mujer; «Dr.» → hombre; si el perfil no dice tratamiento ni sexo, la **neutra**. Nunca se adivina por el nombre.\n- La silueta es un respaldo, no un perfil: el panel del médico le sigue pidiendo su foto («Los pacientes eligen con más confianza cuando ven tu cara»).\n- Texto alternativo: con foto «Dra. Lucía Herrera, dermatóloga»; sin foto «Sin foto: Dra. Lucía Herrera».\n- El consumidor provee: URL de la foto o el tipo de avatar, nombre y especialidad.')
comps['Anuncio'] = ('Resultados', 110, f'<aside class="ad" aria-label="Anuncio"><span class="lbl">Patrocinado</span><span>Clínica Dermalia: revisión de lunares, $650 hasta el 30 de noviembre.</span><a href="#promo">Ver promoción</a></aside>',
 f'''.ad{{display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center;background:var(--luz-calida,{P['sun']});border-radius:22px;padding:16px 20px;font-size:16px;line-height:24px}}.lbl{{font-weight:700;font-size:13px;line-height:18px;color:var(--texto-calido,{P['calido']});background:var(--blanco,#fff);border-radius:999px;padding:3px 10px}}.ad a{{margin-left:auto;font-weight:600;color:var(--tinta,{T})}}''',
 'Franja de anuncio entre los resultados: siempre dice que es pagada.\n\n- Fondo `luz-calida`; la etiqueta «Patrocinado» en `texto-calido` sobre blanco, primero y siempre visible.\n- Una línea con quién anuncia, qué ofrece, precio y vigencia; enlace «Ver promoción» a la derecha.\n- Ocupa el ancho de la lista y nunca imita una ficha de médico: así no se confunde con un resultado.\n- `aside` con `aria-label="Anuncio"`. El consumidor provee: anunciante, oferta, vigencia y destino.')
comps['FranjaConfianza'] = ('Confianza', 260, f'<section class="trust" aria-label="Por qué Manik"><div><span class="ic">{ico("badge-check")}</span><b class="d">Médicos verificados</b><p>Revisamos la cédula profesional de cada médico antes de publicarlo.</p></div><div><span class="ic">{ico("message-circle-heart")}</span><b class="d">Opiniones reales</b><p>Solo opina quien tuvo una cita agendada en Manik.</p></div><div><span class="ic">{ico("calendar-check")}</span><b class="d">Sin costo para ti</b><p>Buscar y agendar es gratis. Pagas la consulta directo al médico.</p></div></section>',
 f'''.trust{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;background:var(--tinta,{T});color:#fff;border-radius:var(--radius-ficha,28px);padding:30px}}.trust div{{display:grid;gap:8px;align-content:start}}
.trust .ic{{display:grid;place-items:center;width:44px;height:44px;border-radius:var(--radius-icono,14px);background:rgba(255,255,255,.1);color:var(--confianza-icono,{P['cicono']})}}.trust b{{font-size:20px;line-height:26px;font-weight:600}}.trust p{{color:var(--confianza-texto,{P['ctexto']});font-size:15px;line-height:22px}}''',
 'El único plano oscuro del directorio: tres razones para confiar, dichas como hechos.\n\n- Fondo `tinta`; títulos en blanco (Urbanist 600); texto en `confianza-texto`; iconos en `confianza-icono` dentro de un cuadro translúcido.\n- Cada razón es verificable: verificación de cédula, opiniones solo de citas agendadas, sin costo para el paciente. Nunca promesas que no se pueden medir («¡Los mejores doctores!»).\n- Tres columnas en escritorio, una en celular.\n- El consumidor provee: las tres razones y sus iconos.')
comps['Encabezado'] = ('Navegación', 200, f'<p class="lb">Celular</p><header class="nav cel"><a class="logo" href="#inicio" aria-label="Manik, inicio"><img src="{blob("logotipo.svg")}" alt="" height="26"></a><button class="menu" type="button" aria-expanded="false">Menú</button></header><p class="lb">Escritorio</p><header class="nav"><a class="logo" href="#inicio" aria-label="Manik, inicio"><img src="{blob("logotipo.svg")}" alt="" height="30"></a><ul><li><a href="#buscar" aria-current="page">Buscar médico</a></li><li><a href="#preguntas">Preguntas</a></li><li><a href="#articulos">Artículos</a></li></ul><a class="me" href="#medicos">Soy médico</a></header>',
 f'''body{{background:radial-gradient(60% 140% at 8% 10%,var(--luz-cian,{P['sky']}),transparent 70%),var(--bruma,{Br})}}.nav{{display:flex;align-items:center;gap:20px;padding:12px 8px;flex-wrap:wrap}}.logo img{{display:block;height:30px;width:auto}}
.nav ul{{display:flex;gap:6px;list-style:none;margin:0;padding:0;flex-wrap:wrap}}.nav ul a{{display:block;color:var(--tinta,{T});text-decoration:none;font-weight:500;padding:8px 14px;border-radius:999px;min-height:24px}}.nav ul a:hover{{background:rgba(255,255,255,.7)}}.nav ul a[aria-current]{{background:var(--blanco,#fff)}}
.me{{margin-left:auto;color:var(--tinta,{T});text-decoration:none;font-weight:600;padding:10px 18px;border-radius:999px;background:var(--blanco,#fff)}}
.lb{{font:600 13px/18px var(--font-sans,"Onest",sans-serif);color:var(--muted,{P['muted']});letter-spacing:.04em;text-transform:uppercase;margin:4px 8px}}.cel{{max-width:390px;flex-wrap:nowrap;justify-content:space-between}}.cel .logo img{{height:26px}}
.menu{{font:600 16px var(--font-sans,"Onest",sans-serif);background:var(--blanco,#fff);border:0;border-radius:999px;min-height:44px;padding:0 18px;color:var(--tinta,{T});cursor:pointer}}''',
 'Barra superior del directorio, sobre los halos de luz (sin fondo propio).\n\n- Logotipo horizontal a 30 px de alto (archivo, nunca reescrito con fuente). Enlaces en píldora; el actual con fondo blanco y `aria-current="page"`.\n- «Soy médico» a la derecha: la puerta para que un médico publique o administre su perfil.\n- **Celular y tableta vertical:** logotipo a 26 px y un botón «Menú» de 44 px a la derecha (abre una hoja con las secciones y «Soy médico»). La barra no es fija: el espacio vertical es para los resultados.\n- **Escritorio (≥ 1024 px):** enlaces visibles y «Soy médico» a la derecha.\n- El consumidor provee: secciones y la actual.')
EST = [('Visible', P['onexito'], P['exitos'], 'Visible en Manik', 'Los pacientes te encuentran en manik.mx/dra-lucia-herrera.'), ('Oculto', P['muted'], '#EEF1F5', 'Oculto desde el 2 nov', 'Los pacientes no te encuentran. Puedes mostrarlo cuando quieras.'),
       ('Incompleto', '#A15D02', '#FDF1E1', 'No publicado · faltan 2 datos', 'Agrega el precio de consulta y una forma de agendar en tu consultorio Centro.'), ('En revisión', '#3C7190', '#E9F1F6', 'Revisando tu cédula', 'Te avisamos por correo cuando esté lista, normalmente en 2 días hábiles.')]
comps['EstadoPerfil'] = ('Médico', 300, '<div class="eg">' + ''.join(f'<div class="ep"><span class="pill" style="color:{c};background:{s}">{e}</span><b class="d">{a}</b><p class="mut">{b}</p></div>' for e, c, s, a, b in EST) + '</div>',
 '.eg{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}.ep{display:grid;gap:6px;align-content:start;background:var(--blanco,#fff);border:1px solid var(--linea,#DCE4EA);border-radius:20px;padding:16px}.pill{justify-self:start;font:600 13px/18px var(--font-sans,"Onest",sans-serif);border-radius:999px;padding:3px 10px}.ep b{font-size:17px;line-height:22px}.ep p{font-size:14px;line-height:20px}',
 'Estado del perfil público del médico, tal como lo ve él en su panel (no el paciente). **Propuesta** del panel de usuario r1, pendiente de confirmar.\n\n- **Visible:** aparece en búsquedas; acciones «Ver mi perfil público» y «Editar perfil».\n- **Oculto:** no aparece; «Mostrar en Manik». Ocultar pide confirmación; mostrar no.\n- **Incompleto:** no se publica hasta completar lo obligatorio de cada consultorio: dirección, precio de consulta y una forma de agendar (en Manik o por teléfono). La foto se pide pero no bloquea: sin ella sale el avatar.\n- **En revisión:** se está verificando la cédula; el interruptor de visibilidad queda bloqueado.\n- Siempre texto + color; aviso e información toman los tonos del ecosistema oscurecidos para llegar a 4.5:1 sobre su fondo (#A15D02, #3C7190); aún no son tokens del directorio.\n- El consumidor provee: estado, fecha y datos faltantes. Supuestos: solo médicos tienen perfil público; la verificación de cédula existe.')
for name, (grp, h, body, css, md) in comps.items():
    os.makedirs(f'components/{name}', exist_ok=True)
    open(f'components/{name}/preview.html', 'w').write(page(grp, h, body, css))
    open(f'components/{name}/README.md', 'w').write(f'# {name}\n\n{md}\n')
os.makedirs('components/Cover', exist_ok=True)
open('components/Cover/preview.html', 'w').write(f'''<!-- @dsCard height=300 -->
<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>
html,body{{margin:0;height:100%}}body{{background:radial-gradient(60% 80% at 6% 8%,var(--luz-cian,{P['sky']}),transparent 70%),radial-gradient(50% 75% at 96% 90%,var(--luz-calida,{P['sun']}),transparent 70%),var(--bruma,{Br});color:var(--tinta,{T});font-family:var(--font-sans,"Onest",sans-serif);overflow:hidden}}
.c{{height:300px;padding:28px 34px;box-sizing:border-box;display:grid;align-content:space-between}}
.top img{{height:34px;width:auto;display:block}}
h1{{margin:0;font:300 54px/56px var(--font-display,"Urbanist",sans-serif);letter-spacing:-.035em}}h1 b{{font-weight:600}}
.b{{display:flex;gap:10px;flex-wrap:wrap;align-items:center}}.t{{font:600 15px var(--font-sans,"Onest",sans-serif);font-variant-numeric:tabular-nums;color:var(--cian-ui,{P['ui']});background:var(--blanco,#fff);border:1.5px solid var(--cian-ui,{P['ui']});border-radius:999px;padding:9px 14px}}.t.on{{background:var(--cian-ui,{P['ui']});color:#fff}}
.v{{display:inline-flex;align-items:center;gap:6px;font:600 14px var(--font-sans,"Onest",sans-serif);color:var(--on-exito-suave,{P['onexito']});background:var(--exito-suave,{P['exitos']});border-radius:999px;padding:6px 12px}}
p{{margin:0;color:var(--muted,{P['muted']});font-size:16px;line-height:24px;max-width:540px}}
</style></head><body><div class="c"><div class="top"><img src="{blob("logotipo.svg")}" alt="manik"></div><div style="display:grid;gap:10px"><h1>Tu médico, <b>a la mano</b>.</h1><p>Sistema de diseño del directorio Manik: luz cian y cálida, Urbanist ligera para hablar, Onest para decidir.</p></div><div class="b"><span class="t">16:30</span><span class="t on">17:00</span><span class="t">18:30</span><span class="v">✓ Cédula verificada</span></div></div></body></html>''')

README = f'''# Directorio Manik

Manik es lo que conoce el paciente: un directorio para encontrar médico, leer opiniones y agendar. Lema: «Tu médico, a la mano». En textos se escribe «Manik» (con mayúscula, sin «Mi» ni «Directorio» delante); en el logotipo, «manik». Se respalda con «de MedicalManik».

Este sistema sigue el manual de marca del directorio (dirección «bienestar», versión 2) y el prototipo de búsqueda y resultados. Tema claro único y deliberado.

## Fundamentos

- **El paciente decide rápido.** Cada pantalla responde primero quién, dónde, cuándo y cuánto cuesta; lo demás después.
- **Luz, no color.** Bruma y blanco dominan; la luz cian y la cálida dan ambiente; tinta para leer; cian de interfaz para lo que se toca; las estrellas son un detalle.
- **Confianza demostrable.** Cédula verificada, opiniones solo de citas agendadas y precios a la vista.
- **Personas reales.** Fotos de médicos reales en 3:4 y fotos de marca de México real; sin bancos de imágenes.

## Celular primero

El 70 % del uso será en celular y tableta, el 30 % en escritorio. Se diseña primero a 390 px; tableta y escritorio son ampliaciones.

- **Cortes:** celular < 640 px · tableta 640–1023 px · escritorio ≥ 1024 px (`bp-tableta`, `bp-escritorio`). Los componentes se adaptan al ancho de su contenedor (container queries) cuando pueden; la ficha cambia a 560 px (`ficha-amplia`).
- **Prioridad en la ficha:** nombre y especialidad → consultorio y distancia → precio → calificación y cédula → cuándo → hasta 3 horarios → acción. Unas dos fichas por pantalla de 390 × 844.
- **Pulgar:** la acción principal va abajo o a todo el ancho: «Buscar» al pie de la búsqueda, «Ver N especialistas» al pie de los filtros, barra de acción fija en el perfil (BarraAccion).
- **Llamar:** en un consultorio que agenda por teléfono, «Llamar» (`tel:`) es la acción principal y «Copiar número» la secundaria. El número siempre va escrito.
- **Nada se sale de la pantalla:** filtros en hoja inferior (BarraFiltros), chips que pasan de línea, máximo 3 horarios en la ficha.
- **Tableta:** dos columnas de fichas; búsqueda y filtros como en celular en vertical. **Escritorio:** buscador en píldora doble, filtros en fila; lista con mapa [propuesta].
- **Datos móviles:** fotos en WebP de 176 × 234 en la ficha de celular (≤ 20 KB); 480 × 640 solo en perfil y ficha amplia. Fuentes con `display=swap`.
- **Insets del dispositivo:** barras y hojas fijas al pie suman `env(safe-area-inset-bottom)`.

## Lugar en la familia MedicalManik

- **MedicalManik**: la empresa, sello madre.
- **Herramientas de la clínica** («Producto Manik»: Expediente, Agenda…): su propio sistema, Ecosistema Manik. Comparten con el directorio Urbanist, el cian del pin y los fondos de luz en marca y portada; dentro de las apps usan Atkinson y el botón azul Manik.
- **Manik**: el directorio para pacientes. Aquí el texto es **Onest**, porque el paciente escanea y decide; en las herramientas es Atkinson, porque el médico lee dosis y claves.

## Marca

- **Símbolo:** la línea de pulso de la familia (una M que es un latido) en un cuadro con punta de pin: «aquí, cerca de ti». Nunca se redibuja.
- **Logotipo:** «manik» en Sora 600 con espaciado −0.04 em, convertido a trazos; siempre los archivos, nunca reescrito con fuente.
- Versiones: color, una tinta, blanco; logotipo horizontal, vertical, con respaldo «de MedicalManik» y en blanco. Ícono de app y favicon.
- Área de respeto: un cuarto del ancho del símbolo por lado. Mínimo 24 px en pantalla y 8 mm impreso.
- Sin degradados en el sello: un solo color para imprimir, bordar y sellar.
- Archivos: grupos de assets «Marca» y «Logotipos».

## Color

| Token | Valor | Para |
| --- | --- | --- |
| `cian` | {P['cian']} | Sello y áreas grandes de marca. Blanco encima {cr(W, P['cian'])}:1: solo 24 px o más; nunca botones. |
| `cian-ui` | {P['ui']} | Agendar, horarios, enlaces e iconos de acción. Blanco encima {cr(W, P['ui'])}:1. |
| `tinta` | {T} | Texto y logotipo ({cr(T, W)}:1 sobre blanco). |
| `muted` | {P['muted']} | Texto secundario ({cr(P['muted'], W)}:1). |
| `bruma` | {Br} | Fondo de página. |
| `luz-cian` / `luz-calida` | {P['sky']} / {P['sun']} | Halos de fondo; «Nuevo en Manik» y anuncios en la cálida. |
| `estrella` | {P['estrella']} | Solo la estrella ({cr(P['estrella'], W)}:1): siempre con el número en tinta. |
| `exito` / `on-exito-suave` | {P['exito']} / {P['onexito']} | Confirmaciones; «Cédula verificada» usa el segundo sobre `exito-suave` ({cr(P['onexito'], P['exitos'])}:1). |
| `azul-medicalmanik` | {P['azul']} | Solo en «de MedicalManik». |

- Halos: `radial-gradient` de `luz-cian` arriba a la izquierda y `luz-calida` a la derecha sobre `bruma`. La luz vive en fondos y fotografía, nunca en el sello.
- `cian-ui` sobre `luz-cian` da {cr(P['ui'], P['sky'])}:1: válido para iconos, no para texto pequeño.

## Tipografía

- **Primaria · Urbanist**: titulares en 300, grandes y con el espaciado cerrado (−0.035 em); la palabra clave en 600 («Cuidarte ya no tiene que ser **difícil**»). Nombres de médicos, precios y categorías en 600.
- **Secundaria · Onest**: todo lo demás. Base 17 px. Horarios, precios y teléfonos con cifras tabulares.
- Carga: `family=Urbanist:wght@300..700&family=Onest:wght@400..700`.

## Forma, espacio y profundidad

- **Píldora para todo lo que se toca:** buscador, botones, horarios, chips y atajos.
- Radios: icono 14, icono de categoría 16, foto 20, categoría 24, ficha 28 (24 en celular).
- Espacio: 4 · 8 · 12 · 16 · 24 · 36 · 44 · 56, tomado del prototipo (por confirmar con desarrollo).
- Sombras suaves teñidas de tinta: buscador, ficha al pasar el cursor y tarjetitas flotantes. El resto se separa con borde `linea` y aire.
- Controles de 42 a 60 px; botones de cierre e iconos de 44 px; ancho máximo 1280 px.

## Iconografía

Lucide, trazo 2, en `cian-ui` (o `confianza-icono` sobre tinta). Dentro de un cuadro blanco (categorías) o un círculo `luz-cian` (portada). Con texto al lado, `aria-hidden`. Grupo de assets «Iconos».

## Voz

De tú, claro y sin tecnicismos, como una persona que conoce buenos médicos y te ayuda a llegar con uno.

| Así sí | Así no |
| --- | --- |
| «Dermatólogos cerca de ti» | «Directorio de profesionales de la salud» |
| «Hoy tiene espacio a las 11:30» | «Disponibilidad en el slot 11:30» |
| «Te mandamos un recordatorio un día antes» | «Su cita ha sido registrada exitosamente en el sistema» |
| «124 pacientes opinaron sobre la Dra. Herrera» | «¡Los mejores doctores!» |
| «Agenda en Manik» (la cita es presencial) | «En línea» o «Cita en línea»: se confunde con consulta por video |

## Consultorios

Un médico puede atender en varios consultorios. **Precio, horarios y forma de agendar son de cada consultorio**, no del médico (decisión 2026-11-04).

- **Para publicar**, cada consultorio necesita dirección, precio de consulta y al menos una forma de agendar: **agenda en Manik** (horarios; la cita es presencial), **por teléfono**, o **ambas**. Sin precio o sin forma de agendar, el consultorio no se publica y el perfil queda «Incompleto» [propuesta].
- **En resultados**, la ficha muestra un consultorio: el más cercano a donde busca el paciente que cumpla los filtros. Si hay más: «Atiende en N consultorios · ver todos».
- **Filtros por consultorio:** «Agenda en Manik», «Hasta $800» y «Con lugar hoy» se evalúan en cada consultorio.
- **Formas mixtas:** un consultorio puede agendar en Manik y otro solo por teléfono, o uno ofrecer las dos; cada uno muestra la suya. Con ambas, «Agendar» es la principal y «o llama al …» el enlace alternativo.
- En el perfil público, la lista de consultorios con su dirección, precio y forma de agendar [pendiente de diseñar].

## Fotografía

- **Retratos de médicos:** los sube cada médico. 3:4 vertical, mínimo 900 × 1200 px; servidos en WebP a 176 × 234 en la ficha de celular (≤ 20 KB) y a 480 × 640 en perfil y ficha amplia (≤ 120 KB). Luz natural, fondo liso y claro, sin filtros. Revisión antes de publicar: solo bloquea lo que confunde al paciente (que no sea la persona o no se vea su cara); la calidad se sugiere.
- **Sin foto:** avatar de silueta de médica o médico (o neutro si el perfil no lo indica) sobre el degradado `foto-inicio` → `foto-fin`. Decisión 2026-11-04; reemplaza la regla anterior de iniciales. La foto se sigue pidiendo en el panel.
- **Fotos de marca:** personas cuidándose en su vida diaria, México real; portada 4:5 en escritorio y 1:1 en celular.

## Accesibilidad

WCAG 2.2 AA: texto 4.5:1 en su fondo, controles de 42 px o más (objetivo mínimo 24 px), foco visible de 3 px (`focus`), estados con icono y texto, `prefers-reduced-motion` respetado. La estrella nunca va sola: el número va escrito.

## Pendientes

- Verde de «Cédula verificada»: el prototipo usaba #15814B sobre #E7F5EE (4.4:1, no cumple AA); aquí se oscurece a `on-exito-suave`.
- Estrella: el manual v2 usa {P['estrella']}; el paquete de marca anterior decía #F2B33D. Aquí manda el manual v2 (más reciente).
- Aviso e información (estado del perfil) usan los colores del ecosistema; decidir si pasan a tokens del directorio.
- Estado del perfil público: propuesta del panel de usuario, por confirmar (¿clínicas con perfil?, ¿verificación de cédula?).
- Perfil público con la lista de consultorios: por diseñar.
- Varios precios en un mismo consultorio (primera vez / subsecuente): sin decidir.
- Dominio `manik.mx` sin confirmar; datos de médicos, precios y teléfonos son de ejemplo.
- Escala de espacio tomada del prototipo; confirmar con desarrollo.
'''
open('README.md', 'w').write(README)
os.makedirs('assets/Marca', exist_ok=True); os.makedirs('assets/Logotipos', exist_ok=True); os.makedirs('assets/Iconos', exist_ok=True); os.makedirs('assets/Avatares', exist_ok=True)
open('assets/Marca/README.md', 'w').write('# Marca\n\nSímbolo de Manik (pin cian con la línea de pulso) en color, una tinta (`currentColor`) y blanco; ícono de app (1024) y favicon. Mínimo 24 px; área de respeto de un cuarto del ancho del símbolo. Nunca degradados, rotación, sombras ni otro color.\n')
open('assets/Logotipos/README.md', 'w').write('# Logotipos\n\n«manik» en Sora 600 convertido a trazos: horizontal (uso general), vertical (espacios angostos), con respaldo «de MedicalManik» (institucional), en blanco y a una tinta. Siempre el archivo; nunca reescrito con fuente.\n')
open('assets/Avatares/README.md', 'w').write('# Avatares\n\nRespaldo cuando el médico no tiene foto: silueta de médica, médico o neutra, con bata y estetoscopio, 3:4 sobre el degradado de luz. «Dra.» → mujer, «Dr.» → hombre; sin dato → neutra. Nunca se elige por el nombre.\n')
open('assets/Iconos/README.md', 'w').write('# Iconos\n\nLucide (licencia ISC), trazo 2, retícula 24, `currentColor`: los que usa el directorio en búsqueda, categorías, ficha y confianza. En interfaz van en `cian-ui`.\n')
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
rec = lambda n, b: {'name': n, 'blob': b[0], 'size': b[1], 'type': 'image/svg+xml'}
om = ['simbolo.svg', 'simbolo-1tinta.svg', 'simbolo-blanco.svg', 'app-icon.svg', 'favicon.svg']; ol = ['logotipo.svg', 'logotipo-vertical.svg', 'logotipo-endoso.svg', 'logotipo-blanco.svg', 'logotipo-1tinta.svg']
oi = [k + '.svg' for k in IC]; oa = list(AV)
json.dump({'v': 3, 'layout': 'files', 'createdOnFiles': {'v': 1, 'at': now}, 'title': 'Directorio Manik', 'namespace': 'DirectorioManik', 'libraries': [], 'sections': {},
  'groups': ['Marca', 'Logotipos', 'Avatares', 'Iconos'],
  'assetGroups': {'Marca': {'name': 'Marca', 'tile': 'm', 'order': om, 'files': {n: rec(n, B[n]) for n in om}},
                  'Logotipos': {'name': 'Logotipos', 'tile': 'l', 'order': ol, 'files': {n: rec(n, B[n]) for n in ol}},
                  'Avatares': {'name': 'Avatares', 'tile': 's', 'order': oa, 'files': {n: rec(n, AV[n]) for n in oa}},
                  'Iconos': {'name': 'Iconos', 'tile': 'xs', 'order': oi, 'files': {k + '.svg': rec(k + '.svg', IC[k]) for k in IC}}},
  'blobs': {}, 'docs': {'readme': 'project/README.md', 'sections': []},
  'lastChange': {'at': now, 'by': 'Kevin', 'via': 'Claude Code', 'note': '«Agenda en Manik» en lugar de «En línea» (la cita es presencial). Antes: Celular primero (70 % del uso): ficha compacta, búsqueda a pantalla completa, filtros en hoja inferior, barra de acción del perfil y «Llamar» para consultorios por teléfono.'}},
 open('design-system.json', 'w'), indent=2, ensure_ascii=False)
print('ok', sorted(os.listdir('components')))
