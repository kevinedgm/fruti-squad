# Ecosistema Manik · sistema de diseño (artifact Design System). Uso: python3 build.py → project/
import json, os, datetime
B = {'medicalmanik.svg': 'b960064adc8e2ea3bc0ad52ba4c1645a', 'expediente.svg': '26b606b673244009be944a9421937b3e', 'agenda.svg': '529d392899981fb38c2f1b46bfd8b30b',
     'compras.svg': '512f89f0825ba83a074cf5f1ccd8bf6d', 'farmacia.svg': 'e38ede352a1a2363095cd3e0c9fb9e7d', 'impulsa.svg': '07c6485f4953617c0f53277d02d95fb9',
     'grupos.svg': 'e26c3ae0f4bf9928c5d4a88e716fca12', 'ecosistema.svg': '15d37dbf5372ca4e4ff1216403ec6e0a', 'ecosistema-1tinta.svg': '3d5b89799a2b4a082727102d35a3720b',
     'medicalmanik-1tinta.svg': 'b67c4621ed3f312229c92a046e94b9bc'}
SRC = '/home/user/fruti-squad/.fruti/icons/medicalmanik/final/svg/'
blob = lambda n: f'/_blob/{B[n]}'

def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]; c = [v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4 for v in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 2)
def mix(a, b, t):
    a = [int(a[i:i+2], 16) for i in (1, 3, 5)]; b = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return '#' + ''.join(f'{round(x * (1 - t) + y * t):02X}' for x, y in zip(a, b))
INK = '#14213D'
def on(c, bg, need=4.5):  # oscurece hacia la tinta hasta cumplir el contraste
    t = 0
    while cr(c, bg) < need and t < 1: t += .05; c2 = mix(c, INK, t); c = c2 if cr(c2, bg) > cr(c, bg) else c
    return c

N = dict(canvas='#F5F7FB', surface='#FFFFFF', soft='#EEF1F7', pressed='#E4E9F2', ink=INK, muted='#4A5674', subtle='#7A849C', line='#E1E6F0', control='#858EA5', noche='#0F1C3F')
MANIK, CIAN = '#234899', '#009BB0'  # cian del pin de Manik (directorio)
PROD = [('expediente', 'Expediente', '#234899', 'Médicos', 'Historia clínica, consultas, notas y recetas del paciente.'),
        ('agenda', 'Agenda', '#007C8C', 'Asistentes', 'Citas, confirmaciones y sala de espera.'),
        ('compras', 'Compras', '#A15C07', 'Administración', 'Órdenes de compra, proveedores y facturación.'),
        ('farmacia', 'Farmacia', '#1B7F52', 'Farmacia', 'Inventario, recetas surtidas y existencias por sucursal.'),
        ('impulsa', 'Impulsa', '#504CA1', 'Marketing clínico', 'Campañas de prevención y sus resultados.'),
        ('grupos', 'Grupos', '#C73A55', 'Administradores de grupo', 'Clínicas, hospitales, usuarios y permisos del grupo.')]
EST = [('exito', '#15814B', 'Guardado, completado, surtido. Siempre con icono y texto.'), ('aviso', '#A75F00', 'Requiere atención: vence pronto, existencias bajas. Siempre con icono y texto.'),
       ('error', '#C33F4E', 'Falló o no se permite: dosis fuera de rango, alergia, pago rechazado. Siempre con icono y texto.'), ('info', '#3F7695', 'Información neutral o en proceso. Siempre con icono y texto.')]

os.makedirs('project/components', exist_ok=True); os.chdir('project')
def t(n, v, u): return {'name': n, 'value': v, 'usage': u}
col = [
 t('canvas', N['canvas'], 'Fondo de página de todas las apps y del inicio del ecosistema. Gris con un sesgo al azul Manik.'),
 t('surface', N['surface'], 'Tarjetas, tablas, paneles, barra superior y barra lateral (la navegación es clara: los sellos azules no se leen sobre azul noche).'),
 t('surface-soft', N['soft'], 'Agrupación, encabezados de tabla, hover neutro, campos de solo lectura.'),
 t('surface-pressed', N['pressed'], 'Presionado neutro.'),
 t('ink', N['ink'], f"Texto principal. {cr(N['ink'], N['surface'])}:1 sobre surface, {cr(N['ink'], N['canvas'])}:1 sobre canvas."),
 t('muted', N['muted'], f"Texto secundario, metadatos, encabezados de columna. {cr(N['muted'], N['surface'])}:1 / {cr(N['muted'], N['canvas'])}:1."),
 t('subtle', N['subtle'], f"SOLO NO-TEXTO: iconos decorativos y separadores gráficos ({cr(N['subtle'], N['surface'])}:1)."),
 t('line', N['line'], 'Divisores y bordes de tarjeta. Decorativo.'),
 t('line-control', N['control'], f"Borde de campos y controles sin relleno: {cr(N['control'], N['surface'])}:1 sobre surface, {cr(N['control'], N['canvas'])}:1 sobre canvas."),
 t('noche', N['noche'], 'Azul noche: planos oscuros puntuales (franja de confianza, piezas impresas, sellos a una tinta en blanco). No es fondo de navegación, ni de portada ni de inicio de sesión: esos van en luz.'),
 t('manik', MANIK, f"Azul MedicalManik: sello madre, acción principal de TODAS las apps, enlaces y foco. Blanco encima {cr('#FFFFFF', MANIK)}:1."),
 t('manik-hover', mix(MANIK, INK, .3), 'Hover y presionado de manik.'),
 t('manik-soft', mix(MANIK, '#FFFFFF', .9), f"Selección, navegación activa, filtro activo; texto encima en manik ({cr(MANIK, mix(MANIK, '#FFFFFF', .9))}:1)."),
 t('on-manik', '#FFFFFF', 'Texto e iconos sobre manik.'),
 t('cian', CIAN, f"Cian de Manik, el mismo del pin del directorio. Acento gráfico: iconos sobre luz, detalles de portada. Nunca texto pequeño ni fondo de texto ({cr(CIAN, '#FFFFFF')}:1 con blanco) ni color de producto."),
 t('bruma', '#F5FAFB', 'Fondo de portada, inicio de sesión e inicio del ecosistema, como el directorio Manik. Dentro de las apps manda «canvas».'),
 t('luz-cian', '#D3F0F4', f"Luz fría de marca: halo de fondo en portada, inicio de sesión e inicio del ecosistema, y círculo detrás de iconos. Texto encima en ink ({cr(INK, '#D3F0F4')}:1)."),
 t('luz-calida', '#FFEFD2', f"Luz cálida de marca, pareja de «luz-cian»: segundo halo y avisos amables. Texto encima en ink ({cr(INK, '#FFEFD2')}:1)."),
 t('focus', '{manik}', 'Anillo de foco de 2 px con 2 px de separación, en todas las apps.'),
]
for k, n, c, quien, _ in PROD:
    s = mix(c, '#FFFFFF', .92); o = on(c, s)
    col += [t(f'app-{k}', c, f"Identidad de {n} Manik ({quien}): su sello, su tarjeta en el inicio y en el selector, la marca de app activa. No es color de botones ni de estados. Blanco encima {cr('#FFFFFF', c)}:1."),
            t(f'app-{k}-soft', s, f'Fondo de la tarjeta de {n} Manik en el inicio y en el selector.'),
            t(f'app-{k}-ink', o, f'Texto con el color de {n} sobre app-{k}-soft: {cr(o, s)}:1.')]
for k, c, u in EST:
    s = mix(c, '#FFFFFF', .9); o = on(c, s)
    col += [t(k, c, f"{u} {cr(c, N['surface'])}:1 sobre surface."), t(f'{k}-soft', s, f'Fondo del estado {k}.'), t(f'on-{k}-soft', o, f'Texto sobre {k}-soft: {cr(o, s)}:1.')]

S_ = lambda n, fs, lh, fw, sample, usage, **k: dict(name=n, fontSize=fs, lineHeight=lh, fontWeight=fw, sample=sample, usage=usage, **k)
tokens = {'name': 'Ecosistema Manik', 'version': 2,
 'color': {'themes': [{'id': 'light', 'name': 'Claro'}], 'tokens': col},
 'type': {'fonts': [], 'families': {'display': '"Urbanist", "Segoe UI", system-ui, sans-serif', 'sans': '"Atkinson Hyperlegible Next", "Atkinson Hyperlegible", system-ui, -apple-system, "Segoe UI", sans-serif'},
  'groups': [
   {'name': 'Primaria · Urbanist', 'family': 'display', 'note': 'La letra del directorio Manik: marca, saludos y títulos, para que pacientes y clínicas vean la misma familia. 300 grande solo en portada e inicio; 600 en títulos y nombres de app. Nunca en párrafos, tablas ni valores clínicos.', 'styles': [
     S_('display', '40px', '44px', 300, 'Buenos días, Dra. Ramírez', 'Saludo del inicio del ecosistema y títulos de portada, ligero como en el directorio. Una por pantalla.', letterSpacing='-0.03em'),
     S_('title-1', '24px', '32px', 600, 'Expediente de Mariana Ruiz', 'Título de página.', letterSpacing='-0.01em'),
     S_('title-2', '18px', '26px', 600, 'Signos vitales', 'Título de tarjeta, panel y diálogo.'),
     S_('app-name', '16px', '24px', 600, 'Farmacia', 'Nombre del producto junto a su sello: «Farmacia» en 600 y «Manik» en 400.')]},
   {'name': 'Secundaria · Atkinson Hyperlegible Next', 'family': 'sans', 'note': 'Toda la interfaz y todo dato clínico. Diseñada para distinguir I l 1 y 0 O: en dosis, folios y claves no hay confusión. Cifras tabulares (font-variant-numeric: tabular-nums) en tablas y valores.', 'styles': [
     S_('body', '16px', '24px', 400, 'Paciente con hipertensión controlada; continuar tratamiento.', 'Texto corrido, notas clínicas, descripciones.'),
     S_('body-sm', '14px', '20px', 400, 'Última consulta: 12 oct 2026 · Dr. L. Ortega', 'Texto en tablas y listas densas.'),
     S_('label', '14px', '20px', 600, 'Dosis', 'Etiquetas de campo, encabezados de columna, pestañas.'),
     S_('button', '15px', '20px', 600, 'Guardar receta', 'Botones.'),
     S_('dato', '16px', '24px', 500, 'Losartán 50 mg · 1 c/12 h', 'Valores clínicos en tablas y tarjetas: dosis, signos, claves. Con cifras tabulares.'),
     S_('dato-xl', '28px', '32px', 600, '120/80 mmHg', 'Valor protagonista de una tarjeta (presión, glucosa, existencias).'),
     S_('caption', '13px', '18px', 400, 'Editado hace 3 min por A. Pérez', 'Metadatos y ayudas. Piso del sistema: nada clínico por debajo de 13 px.'),
     S_('overline', '12px', '16px', 700, 'ALERGIAS', 'Etiqueta en mayúsculas sobre un dato.', letterSpacing='0.08em')]}]},
 'spacing': {'tokens': [t('space-1', '4px', 'Icono–texto.'), t('space-2', '8px', 'Dentro de controles y chips.'), t('space-3', '12px', 'Entre campos de un grupo.'), t('space-4', '16px', 'Padding de tarjeta compacta; gutter mínimo en móvil.'),
   t('space-6', '24px', 'Padding de tarjeta y panel.'), t('space-8', '32px', 'Entre secciones de una vista.'), t('space-12', '48px', 'Entre grupos grandes, preferido a separadores.'), t('space-16', '64px', 'Márgenes del inicio del ecosistema en escritorio.')]},
 'radius': {'tokens': [t('radius-sm', '10px', 'Chips cuadrados, campos pequeños.'), t('radius-md', '14px', 'Botones, campos.'), t('radius-lg', '18px', 'Tarjetas de app del inicio, menús, selector.'), t('radius-2xl', '24px', 'Tarjetas de contenido y diálogos.'), t('radius-pill', '999px', 'Estados, avatares.')]},
 'shadow': {'tokens': [t('shadow-card', '0 1px 2px rgba(20, 33, 61, 0.05), 0 5px 14px rgba(20, 33, 61, 0.05)', 'Tarjetas en reposo cuando no basta el borde.'),
   t('shadow-hover', '0 2px 4px rgba(20, 33, 61, 0.06), 0 8px 20px rgba(20, 33, 61, 0.08)', 'Tarjeta de app al pasar el cursor.'),
   t('shadow-pop', '0 2px 8px rgba(20, 33, 61, 0.08), 0 18px 44px rgba(20, 33, 61, 0.16)', 'Selector del ecosistema, menús y diálogos.')]},
 'layout': {'tokens': [t('control-height', '44px', 'Alto de botones y campos (también objetivo táctil).'), t('header-height', '64px', 'Barra superior de cada app.'), t('content-wide', '1440px', 'Ancho máximo de vistas de trabajo.'), t('content-reading', '72ch', 'Ancho de notas clínicas.')]}}
json.dump(tokens, open('tokens.json', 'w'), ensure_ascii=False, indent=1)
V = {x['name']: x['value'] for x in col}

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700&display=swap">'
BASE = '''html,body{margin:0}body{background:var(--canvas,#F5F7FB);color:var(--ink,#14213D);font:16px/24px var(--font-sans,"Atkinson Hyperlegible Next",system-ui,sans-serif);padding:16px}
.d{font-family:var(--font-display,"Urbanist",sans-serif)}.num{font-variant-numeric:tabular-nums}.mut{color:var(--muted,#4A5674)}
.row{display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.btn{display:inline-flex;align-items:center;gap:8px;min-height:var(--control-height,44px);padding:0 18px;border-radius:var(--radius-md,14px);font:600 15px/20px var(--font-sans,"Atkinson Hyperlegible Next",sans-serif);border:1px solid transparent;cursor:pointer}
.btn:focus-visible,button:focus-visible,a:focus-visible{outline:2px solid var(--focus,#234899);outline-offset:2px}
.b1{background:var(--manik,#234899);color:var(--on-manik,#fff)}.b1:hover{background:var(--manik-hover,#1C3A79)}.b2{background:var(--surface,#fff);color:var(--manik,#234899);border-color:var(--line-control,#858EA5)}.b3{background:transparent;color:var(--manik,#234899)}.b4{background:var(--surface,#fff);color:var(--error,#C33F4E);border-color:var(--error,#C33F4E)}
.ico{width:18px;height:18px;flex:none;display:block}
.est{display:inline-flex;align-items:center;gap:6px;padding:3px 12px 3px 9px;border-radius:var(--radius-pill,999px);font:600 13px/18px var(--font-sans,sans-serif)}
.card{background:var(--surface,#fff);border:1px solid var(--line,#E1E6F0);border-radius:var(--radius-2xl,24px)}'''
def page(grp, h, body, css=''):
    return f'<!-- @dsCard group="{grp}" height={h} -->\n<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>{BASE}{css}</style></head><body>{body}</body></html>'
I = {'ok': '<path d="M5 12.5l4.5 4.5L19 7.5"/>', 'warn': '<path d="M12 3.5l9.5 16.5h-19z"/><path d="M12 10v4M12 17h.01"/>', 'bad': '<circle cx="12" cy="12" r="9"/><path d="M15 9l-6 6M9 9l6 6"/>',
     'info': '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>', 'search': '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>', 'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
     'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>', 'bell': '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10 21h4"/>'}
ic = lambda k, c='currentColor': f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[k]}</svg>'
est = lambda k, ik, txt: f'<span class="est" style="background:var(--{k}-soft,{V[k+"-soft"]});color:var(--on-{k}-soft,{V["on-"+k+"-soft"]})">{ic(ik)}{txt}</span>'
img = lambda n, z, alt='': f'<img src="{blob(n)}" width="{z}" height="{z}" alt="{alt}" style="display:block;flex:none">'
ECO_BTN = f'<button class="eco" aria-label="Ecosistema Manik: cambiar de app" aria-haspopup="dialog">{img("ecosistema.svg", 24)}</button>'
TOP_CSS = '''.top{display:flex;align-items:center;gap:12px;height:var(--header-height,64px);padding:0 16px;background:var(--surface,#fff);border:1px solid var(--line,#E1E6F0);border-radius:var(--radius-lg,18px)}
.nm{font:16px/24px var(--font-display,"Urbanist",sans-serif);color:var(--muted,#4A5674);white-space:nowrap}.nm b{font-weight:600;color:var(--ink,#14213D)}
.sp{flex:1;min-width:0}.srch{display:flex;align-items:center;gap:8px;height:40px;border:1px solid var(--line-control,#858EA5);border-radius:var(--radius-md,14px);padding:0 12px;color:var(--muted,#4A5674);font-size:14px;width:280px;max-width:40%;background:var(--surface,#fff)}
.eco{width:44px;height:44px;border-radius:12px;border:0;background:transparent;display:grid;place-items:center;cursor:pointer}.eco:hover{background:var(--surface-soft,#EEF1F7)}.eco[aria-expanded="true"]{background:var(--manik-soft,#E9EDF5)}
.av{width:36px;height:36px;border-radius:50%;background:var(--surface-soft,#EEF1F7);display:grid;place-items:center;font:600 13px/1 var(--font-sans,sans-serif);color:var(--ink,#14213D)}
.ib{width:44px;height:44px;display:grid;place-items:center;color:var(--muted,#4A5674)}'''
TILE_CSS = '''.tiles{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}.tile{display:grid;justify-items:center;gap:6px;padding:14px 8px 12px;border-radius:var(--radius-lg,18px);text-decoration:none;color:var(--ink,#14213D);font:600 14px/20px var(--font-sans,sans-serif);text-align:center}
.tile:hover{background:var(--surface-soft,#EEF1F7)}.tile.on{background:var(--manik-soft,#E9EDF5)}.tile small{font:500 12px/16px var(--font-sans,sans-serif);color:var(--manik,#234899)}'''
CUR = ' aria-current="page"'
tiles = lambda actual, z=44: ''.join(f'<a class="tile{" on" if n == actual else ""}" href="#{k}"{CUR if n == actual else ""}>{img(k + ".svg", z)}<span>{n}</span>{"<small>Aquí estás</small>" if n == actual else ""}</a>' for k, n, *_ in PROD)
comps = {}
comps['SelloProducto'] = ('Marca', 208, ''.join(f'<figure style="margin:0;display:grid;justify-items:center;gap:8px;width:132px">{img(k + ".svg", 88, n + " Manik")}<figcaption class="d" style="font-size:14px;line-height:20px;text-align:center"><b style="font-weight:600">{n}</b> <span class="mut">Manik</span></figcaption></figure>' for k, n, *_ in PROD),
 'body{display:flex;gap:4px;flex-wrap:wrap;justify-content:center;align-items:end}',
 'Sello de cada producto: la misma línea de pulso en un contenedor que cuenta qué es la app.\n\n- La línea es idéntica en todos; el rasgo vive en el borde y nunca la corta: carpeta (Expediente), argollas (Agenda), ticket (Compras), cruz (Farmacia), flecha (Impulsa), tarjeta detrás (Grupos).\n- Nombre: el producto en Urbanist 600 (`app-name`) y «Manik» en 400 y «muted». Nunca «Manik Farmacia» ni solo «Farmacia» como marca.\n- Color: `app-<producto>` es identidad, no interfaz (ver README, Color).\n- Tamaño mínimo 24 px; a 16 px solo en pestañas del navegador.\n- El consumidor provee: el producto y el tamaño. Archivos en el grupo de assets «Sellos».')
comps['EncabezadoApp'] = ('Navegación', 100, f'<div class="top">{img("farmacia.svg", 34, "")}<span class="nm"><b>Farmacia</b> Manik</span><span class="sp"></span><span class="srch">{ic("search")}Buscar producto, receta o lote</span><span class="ib">{ic("bell")}</span>{ECO_BTN}<span class="av">MR</span></div>', TOP_CSS,
 'Barra superior que comparten todas las apps: sello y nombre de la app a la izquierda; búsqueda, avisos, el botón del ecosistema y el avatar a la derecha.\n\n- 64 px (`header-height`), fondo «surface», borde «line». La navegación es clara en todo el ecosistema.\n- El botón del ecosistema (mosaico de seis cuadros, 24 px en un área de 44) va siempre en el mismo lugar: justo antes del avatar. Su nombre accesible: «Ecosistema Manik: cambiar de app».\n- El sello de la app a 32–36 px. Clic en el sello o el nombre: inicio de esa app.\n- El consumidor provee: la app, la búsqueda propia de la app y el usuario.')
comps['SelectorEcosistema'] = ('Navegación', 460, f'<div class="top">{img("farmacia.svg", 34, "")}<span class="nm"><b>Farmacia</b> Manik</span><span class="sp"></span><button class="eco" aria-label="Ecosistema Manik: cambiar de app" aria-expanded="true" aria-controls="sel">{img("ecosistema.svg", 24)}</button><span class="av">MR</span></div><div id="sel" class="pop" role="dialog" aria-label="Ecosistema Manik"><div class="ph">{img("ecosistema.svg", 18)}<span class="nm"><b>Ecosistema</b> Manik</span></div><nav class="tiles" aria-label="Apps del ecosistema">{tiles("Farmacia")}</nav><a class="all" href="#inicio">Ir al inicio del ecosistema {ic("arrow")}</a></div>',
 TOP_CSS + TILE_CSS + '.pop{margin:8px 0 0 auto;width:min(380px,100%);background:var(--surface,#fff);border:1px solid var(--line,#E1E6F0);border-radius:var(--radius-lg,18px);box-shadow:var(--shadow-pop,0 18px 44px rgba(20,33,61,.16));padding:16px}.ph{display:flex;align-items:center;gap:8px;margin-bottom:10px}.all{display:flex;align-items:center;justify-content:center;gap:6px;border-top:1px solid var(--line,#E1E6F0);margin-top:10px;padding-top:12px;color:var(--manik,#234899);font:600 14px/20px var(--font-sans,sans-serif);text-decoration:none}',
 'Panel que abre el botón del ecosistema: las apps a las que la persona tiene acceso, con la actual marcada.\n\n- Se abre bajo el botón, alineado a la derecha; 380 px de ancho; sombra `shadow-pop`. Cierra con Escape, clic fuera o al elegir una app; el foco vuelve al botón.\n- Rejilla de 3 columnas: sello a 44 px y nombre del producto (sin «Manik»: el panel ya lo dice). La app actual: fondo «manik-soft», «Aquí estás» y `aria-current="page"`.\n- Solo muestra las apps con acceso. Al pie, «Ir al inicio del ecosistema».\n- Orden fijo en todo el sistema: Expediente, Agenda, Compras, Farmacia, Impulsa, Grupos.\n- El consumidor provee: la lista de apps con acceso y la app actual.')
cards = ''
DIS = ' aria-disabled="true"'
for i, (k, n, c, quien, desc) in enumerate(PROD):
    lock = k == 'grupos'
    cards += (f'<a class="app{" lock" if lock else ""}" href="#{k}" style="--tint:var(--app-{k}-soft,{V["app-" + k + "-soft"]})"{DIS if lock else ""}><span class="ah">{img(k + ".svg", 52)}<span class="go">{ic("lock" if lock else "arrow")}</span></span>'
              f'<span class="an"><b>{n}</b> Manik</span><span class="aq">{quien}</span><span class="ad">{desc}</span>'
              + (f'<span class="al">Sin acceso · pídelo a tu administrador de grupo</span>' if lock else (f'<span class="al">Última vez: hoy, 09:40</span>' if i == 0 else '')) + '</a>')
comps['InicioEcosistema'] = ('Patrones', 680, f'<main class="home"><div class="hh"><div>{img("medicalmanik.svg", 40)}</div><div><p class="ov">ECOSISTEMA MANIK</p><h1 class="d">Buenos días, Dra. Ramírez</h1><p class="mut">¿A qué app quieres ir? Clínica Santa Lucía · Grupo Médico del Valle</p></div></div><div class="grid">{cards}</div></main>',
 '.home{display:grid;gap:24px;padding:24px;border-radius:var(--radius-2xl,24px);background:radial-gradient(ellipse 60% 70% at 0% 0%,var(--luz-cian,#D3F0F4),transparent 70%),radial-gradient(ellipse 50% 60% at 100% 0%,var(--luz-calida,#FFEFD2),transparent 70%),var(--bruma,#F5FAFB)}.hh{display:flex;gap:16px;align-items:center}.ov{margin:0;font:700 12px/16px var(--font-sans,sans-serif);letter-spacing:.08em;color:var(--muted,#4A5674)}h1{margin:2px 0;font-size:36px;line-height:40px;font-weight:300;letter-spacing:-.03em}.hh p.mut{margin:0;font-size:15px}'
 '.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}.app{display:grid;gap:4px;align-content:start;padding:18px;border-radius:var(--radius-lg,18px);background:var(--surface,#fff);border:1px solid var(--line,#E1E6F0);text-decoration:none;color:var(--ink,#14213D);transition:box-shadow .15s}'
 '.app:hover{box-shadow:var(--shadow-hover,0 8px 20px rgba(20,33,61,.08));background:var(--tint)}.ah{display:flex;justify-content:space-between;align-items:start;margin-bottom:8px}.go{color:var(--muted,#4A5674)}.an{font:18px/26px var(--font-display,"Urbanist",sans-serif);color:var(--muted,#4A5674)}.an b{font-weight:600;color:var(--ink,#14213D)}'
 '.aq{font:600 13px/18px var(--font-sans,sans-serif);color:var(--muted,#4A5674)}.ad{font-size:14px;line-height:20px;color:var(--ink,#14213D)}.al{margin-top:6px;font-size:13px;line-height:18px;color:var(--muted,#4A5674)}.lock{background:var(--surface-soft,#EEF1F7)}.lock img{filter:grayscale(1);opacity:.55}.lock .an b{color:var(--muted,#4A5674)}'
 '@media (prefers-reduced-motion:reduce){.app{transition:none}}',
 'La primera pantalla después de iniciar sesión: el ecosistema completo para que la persona elija a qué app ir.\n\n- Flujo: inicio de sesión único → Inicio del ecosistema → app elegida. Desde cualquier app se vuelve con el botón del ecosistema («Ir al inicio del ecosistema»).\n- Saludo en `display` (Urbanist 300) sobre «bruma» con los halos «luz-cian» y «luz-calida», como el directorio Manik, con el nombre y la clínica o grupo activo; «¿A qué app quieres ir?» como subtítulo.\n- Una tarjeta por app en el orden fijo: sello a 52 px, nombre «Producto Manik», para quién es y qué hace en una línea. Al pasar el cursor, la tarjeta toma `app-<producto>-soft`.\n- Apps sin acceso: visibles pero apagadas (sello en gris), con candado y «Sin acceso · pídelo a tu administrador de grupo»; `aria-disabled`. Así la persona sabe que existen y a quién pedirlas.\n- Si la persona solo tiene una app, el inicio se salta y entra directo (propuesta, por confirmar).\n- El consumidor provee: nombre y tratamiento, clínica o grupo activo, apps con y sin acceso, último uso.')
comps['Boton'] = ('Acciones', 92, '<button class="btn b1">Guardar receta</button><button class="btn b2">Agregar medicamento</button><button class="btn b3">Ver historial</button><button class="btn b4">Cancelar cita</button>', '',
 'Botón: la acción principal es azul Manik en TODAS las apps, sin importar el color del producto.\n\n- `primario`: «manik» con «on-manik»; una por vista. `secundario`: «surface», borde «line-control», texto «manik». `terciario`: solo texto. `destructivo`: borde y texto «error», siempre con confirmación.\n- 44 px (`control-height`), radio `radius-md`, texto `button` (Atkinson 600). Foco: anillo «focus» 2 px.\n- Por qué no el color del producto: los colores de Farmacia, Compras y Grupos coinciden con éxito, aviso y error; un botón verde o rojo diría otra cosa. El mismo botón en todas las apps también evita reaprender al cambiar de app.\n- El consumidor provee: verbo + objeto, estado de carga y `aria-disabled`.')
comps['Campo'] = ('Formularios', 200, f'<div class="f"><label for="m">Medicamento</label><input id="m" value="Losartán"><small class="mut">Nombre genérico o comercial.</small></div><div class="f"><label for="ds">Dosis</label><div class="in err"><input id="ds" class="num" value="500" aria-invalid="true" aria-describedby="e1"><span class="mut num">mg</span></div><small id="e1" class="er">{ic("bad")}Fuera de rango: máximo 100 mg al día.</small></div>',
 '.f{display:grid;gap:6px;min-width:220px;flex:1}label{font:600 14px/20px var(--font-sans,sans-serif)}input{height:44px;border:1px solid var(--line-control,#858EA5);border-radius:var(--radius-md,14px);padding:0 14px;font:16px var(--font-sans,sans-serif);color:var(--ink,#14213D);background:var(--surface,#fff)}input:focus{outline:2px solid var(--focus,#234899);outline-offset:1px}'
 '.in{display:flex;align-items:center;gap:8px;height:44px;border:1px solid var(--line-control,#858EA5);border-radius:var(--radius-md,14px);padding:0 14px;background:var(--surface,#fff)}.in input{border:0;height:auto;padding:0;width:100%;text-align:right;outline:0}.in.err{border:2px solid var(--error,#C33F4E)}small{font-size:13px;line-height:18px}.er{display:flex;gap:6px;align-items:center;color:var(--error,#C33F4E)}body{display:flex;gap:16px;flex-wrap:wrap}',
 'Campo de captura. Atkinson en todo el texto: distingue 1, l e I, y 0 y O.\n\n- 44 px, borde «line-control», radio `radius-md`, etiqueta `label` arriba y ayuda `caption` abajo.\n- Campos numéricos clínicos (dosis, peso, glucosa): cifras tabulares, alineados a la derecha, unidad fija como sufijo en «muted». La unidad la pone el sistema, no la persona.\n- Error: borde de 2 px en «error», icono y mensaje que dice el límite («máximo 100 mg al día»). Nunca solo color.\n- El consumidor provee: etiqueta, unidad, rango válido y mensaje, `id` y `aria-describedby`.')
comps['Estado'] = ('Retroalimentación', 92, est('exito', 'ok', 'Receta surtida') + est('aviso', 'warn', 'Existencias bajas') + est('error', 'bad', 'Alergia: penicilina') + est('info', 'info', 'En sala de espera'), 'body{display:flex;gap:10px;flex-wrap:wrap;align-items:center}',
 'Estado: icono + texto sobre el fondo suave del estado, iguales en todas las apps.\n\n- Éxito, aviso, error e información; texto `on-<estado>-soft` (≥4.5:1).\n- Nunca solo color: los colores de producto se parecen a los de estado (Farmacia/éxito, Compras/aviso, Grupos/error); el icono y la palabra los separan.\n- Las alergias van siempre como error, en la cabecera del paciente.\n- El consumidor provee: el estado y el texto exacto.')
vit = [('PRESIÓN', '120/80', 'mmHg'), ('FREC. CARDIACA', '72', 'lpm'), ('GLUCOSA', '104', 'mg/dL'), ('PESO', '68.4', 'kg')]
comps['CabeceraPaciente'] = ('Datos', 250, f'<div class="card pc"><div class="pt"><span class="av2">MR</span><div><p class="d nmp">Mariana Ruiz Ortega</p><p class="mut sm num">42 años · F · Exp. <b class="id">MR-0107-II1</b> · Tipo O+</p></div><span class="sp"></span>{est("error", "bad", "Alergia: penicilina")}</div><div class="vs">' + ''.join(f'<div class="v"><span class="ov">{a}</span><span class="num vx">{b}</span><span class="mut sm">{u}</span></div>' for a, b, u in vit) + '</div></div>',
 '.pc{padding:20px;display:grid;gap:16px}.pt{display:flex;gap:14px;align-items:center;flex-wrap:wrap}.av2{width:48px;height:48px;border-radius:50%;background:var(--app-expediente-soft,#EAEEF6);color:var(--app-expediente-ink,#234899);display:grid;place-items:center;font:600 16px var(--font-display,"Urbanist",sans-serif)}.nmp{margin:0;font-size:20px;line-height:28px;font-weight:600}.sm{margin:0;font-size:14px;line-height:20px}.id{font-weight:600;color:var(--ink,#14213D);letter-spacing:.02em}.sp{flex:1}'
 '.vs{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:12px}.v{display:grid;gap:2px;padding:12px 14px;border-radius:var(--radius-md,14px);background:var(--surface-soft,#EEF1F7)}.ov{font:700 12px/16px var(--font-sans,sans-serif);letter-spacing:.08em;color:var(--muted,#4A5674)}.vx{font:600 28px/32px var(--font-sans,sans-serif)}',
 'Cabecera del paciente en Expediente: quién es, su clave y lo que no puede pasarse por alto.\n\n- Nombre en Urbanist 600; edad, sexo, clave de expediente y tipo de sangre en `body-sm`. La clave en 600 con tracking 0.02em: Atkinson distingue I, l y 1 (MR-0107-II1).\n- Alergias siempre visibles como estado «error» con icono, a la derecha del nombre.\n- Signos en `dato-xl` (Atkinson 600, cifras tabulares) con la unidad aparte en «muted».\n- El consumidor provee: datos del paciente, alergias, últimos signos con fecha.')
for name, (grp, h, body, css, md) in comps.items():
    os.makedirs(f'components/{name}', exist_ok=True)
    open(f'components/{name}/preview.html', 'w').write(page(grp, h, body, css))
    open(f'components/{name}/README.md', 'w').write(f'# {name}\n\n{md}\n')

# Portada
os.makedirs('components/Cover', exist_ok=True)
seals = ''.join(img(k + '.svg', 58) for k, *_ in PROD)
open('components/Cover/preview.html', 'w').write(f'''<!-- @dsCard height=288 -->
<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>
html,body{{margin:0;height:100%}}body{{background:radial-gradient(ellipse 55% 80% at 100% 0%,var(--luz-cian,#D3F0F4),transparent 70%),radial-gradient(ellipse 45% 70% at 0% 100%,var(--luz-calida,#FFEFD2),transparent 70%),var(--bruma,#F5FAFB);color:var(--ink,#14213D);font-family:var(--font-sans,"Atkinson Hyperlegible Next",sans-serif);overflow:hidden}}
.c{{position:relative;height:288px;padding:28px 32px;box-sizing:border-box;display:grid;align-content:space-between}}
.top{{display:flex;align-items:center;gap:12px}}.top span{{font:600 15px/20px var(--font-display,"Urbanist",sans-serif);color:var(--muted,#4A5674);letter-spacing:.02em}}
h1{{margin:0;font:300 52px/54px var(--font-display,"Urbanist",sans-serif);letter-spacing:-.035em}}h1 span{{font-weight:600}}
.s{{display:flex;gap:12px;flex-wrap:wrap;align-items:end}}.s img{{filter:drop-shadow(0 6px 14px rgba(20,33,61,.10))}}
p{{margin:0;color:var(--muted,#4A5674);font-size:15px;line-height:22px;max-width:520px}}
</style></head><body><div class="c"><div class="top">{img("ecosistema.svg", 28)}<span>MedicalManik</span></div><div style="display:grid;gap:10px"><h1>Ecosistema <span>Manik</span></h1><p>Un sello, seis apps clínicas: expediente, agenda, compras, farmacia, campañas y grupos. Urbanist para la marca, como el directorio Manik; Atkinson Hyperlegible Next para cada dato.</p></div><div class="s">{seals}</div></div></body></html>''')

README = f'''# Ecosistema Manik

El sistema compartido de las apps clínicas de MedicalManik: un sello, seis productos «Producto + Manik», un inicio común y un selector para pasar de una app a otra. Una clínica u hospital entra una sola vez y elige a dónde ir.

Comparte la identidad del directorio Manik (Urbanist, cian del pin y fondos de luz) en la marca, la portada, el inicio de sesión, el inicio del ecosistema y los títulos. Dentro de cada app manda la legibilidad clínica: Atkinson en interfaz y datos, y el botón en azul Manik.

## Arquitectura

- **MedicalManik** es la empresa y el sello madre: la M de pulso en el cuadro limpio.
- **Productos**, siempre «<Producto> Manik»: Expediente (médicos), Agenda (asistentes), Compras (compras y facturación), Farmacia, Impulsa (campañas de prevención y marketing) y Grupos (administradores de clínicas y hospitales).
- **Ecosistema Manik** es el conjunto. Su identificador es el mosaico de seis cuadros: el botón que abre el selector desde cualquier app.
- **Flujo:** inicio de sesión único → **Inicio del ecosistema** (todas las apps; la persona elige) → la app. Desde cualquier app, el botón del ecosistema abre el selector y lleva de vuelta al inicio.

## Los sellos

La línea de pulso es idéntica en los siete. Cada producto cambia solo el borde del contenedor, nunca la línea:

| Producto | Rasgo | Tipo |
| --- | --- | --- |
| Expediente | pestaña de carpeta | silueta |
| Agenda | argollas de calendario | pieza separada |
| Compras | borde dentado de ticket | silueta |
| Farmacia | cruz | pieza separada |
| Impulsa | flecha que sale de la esquina | pieza separada |
| Grupos | segunda tarjeta detrás | silueta |

- Las piezas separadas llevan un corte transparente: el sello funciona sobre cualquier fondo.
- La cruz de Farmacia va siempre en el color del producto, nunca en rojo (la cruz roja es un emblema protegido).
- Mínimo 24 px en interfaz. El mosaico del ecosistema es un emblema fijo: seis cuadros aunque se sumen productos.
- Archivos: grupo de assets «Sellos» (color, fondo transparente) y «Ecosistema» (mosaico en color y a una tinta).

## Color

**Dos papeles que no se mezclan.**

1. **Identidad (`app-<producto>`)**: dice en qué app estás. Va en el sello, en la tarjeta del inicio y del selector, y en el fondo suave de la tarjeta al pasar el cursor (`app-<producto>-soft`).
2. **Interfaz (`manik` y estados)**: la acción principal es azul Manik en todas las apps; los estados (`exito`, `aviso`, `error`, `info`) son los mismos en todas.

Por qué: tres colores de producto coinciden con estados (Farmacia ≈ éxito, Compras ≈ aviso, Grupos ≈ error). Si fueran color de botón, un «Guardar» rojo en Grupos se leería como peligro. Y el mismo botón en todas las apps evita reaprender al cambiar de app. Los estados llevan siempre icono y texto.

| Producto | `app-*` | Blanco encima |
| --- | --- | --- |
''' + ''.join(f"| {n} | {c} | {cr('#FFFFFF', c)}:1 |\n" for k, n, c, *_ in PROD) + f'''
- Neutros con un sesgo al azul: `canvas` {N['canvas']}, `surface` blanco, `ink` {N['ink']} ({cr(N['ink'], '#FFFFFF')}:1), `muted` {N['muted']} ({cr(N['muted'], '#FFFFFF')}:1). `subtle` es solo gráfico.
- **Navegación clara.** El azul Manik y el violeta de Impulsa no alcanzan 3:1 sobre azul noche; por eso barras y menús van en `surface`. `noche` queda para planos oscuros puntuales.
- **Luz de marca, como el directorio Manik:** portada, inicio de sesión e inicio del ecosistema van sobre `bruma` (#F5FAFB) con dos halos, `luz-cian` (#D3F0F4) y `luz-calida` (#FFEFD2). Dentro de las apps, `canvas`.
- `cian` {CIAN} es el cian del pin de Manik: acento gráfico ({cr(CIAN, '#FFFFFF')}:1 con blanco), nunca texto pequeño, fondo de texto ni color de producto.
- Tema claro únicamente, como Manik Impulsa en producción.

## Tipografía

- **Primaria · Urbanist** (Google Fonts): la letra del directorio Manik, así pacientes y clínicas ven la misma familia. Marca, saludos y títulos: 300 grande en portada e inicio; 600 en títulos y nombres de app. Nunca en párrafos, tablas ni datos clínicos.
- **Secundaria · Atkinson Hyperlegible Next** (Google Fonts): toda la interfaz y todo dato. La diseñó el Braille Institute para que cada letra se distinga: 1, l e I; 0 y O; rn y m. En un expediente eso evita leer mal una dosis o una clave.
- Cifras tabulares (`font-variant-numeric: tabular-nums`) en tablas, dosis y signos.
- Piso de 13 px: nada clínico por debajo.
- Carga: `family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700`.

## Espacio, forma y profundidad

- Espaciado 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64. Radios 10 · 14 · 18 · 24 · píldora: la misma escala que Manik Impulsa en producción.
- Profundidad por borde y espacio; sombra solo para tarjetas al pasar el cursor (`shadow-hover`) y planos flotantes (`shadow-pop`).
- Controles de 44 px; barra superior de 64 px.

## Iconografía

Lucide, trazo 2, retícula 24 (el mismo set de Impulsa). Un concepto, un icono; con texto al lado llevan `aria-hidden`. Estados: circle-check, triangle-alert, circle-x, info.

## Voz

Directa y clínica: el verbo dice lo que pasa («Guardar receta», «Surtir»). Los errores dicen el límite («Fuera de rango: máximo 100 mg al día»). Trato de usted o por título profesional en saludos («Buenos días, Dra. Ramírez»).

## Relación con Manik Impulsa (decisiones abiertas)

Manik Impulsa ya tiene su propio sistema en producción. Este sistema lo respeta en espacio, radios, sombras, estados e iconos, y difiere en tres puntos que hay que decidir:

1. **Tipografía:** Impulsa usa solo Ubuntu; aquí, Urbanist + Atkinson.
2. **Acción:** Impulsa usa su violeta (#504CA1) para botones; aquí la acción es azul Manik en todas las apps.
3. **Lienzo:** Impulsa usa grises neutros (#F4F4F4); aquí los neutros tienen un sesgo al azul.

## Pendientes

- Confirmar la regla de una sola app (¿se salta el inicio?) y los textos de «sin acceso».
- Decidir los tres puntos de Impulsa.
- Componentes por app (tablas, formularios largos, agenda) cuando se diseñe cada producto.
'''
open('README.md', 'w').write(README)

files = {}
order_s = ['medicalmanik.svg'] + [k + '.svg' for k, *_ in PROD] + ['medicalmanik-1tinta.svg']
order_e = ['ecosistema.svg', 'ecosistema-1tinta.svg']
for n in order_s + order_e:
    files[n] = {'name': n, 'blob': B[n], 'size': os.path.getsize(SRC + n), 'type': 'image/svg+xml'}
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
json.dump({'v': 3, 'layout': 'files', 'createdOnFiles': {'v': 1, 'at': now}, 'title': 'Ecosistema Manik', 'namespace': 'EcosistemaManik', 'libraries': [], 'sections': {},
  'groups': ['Sellos', 'Ecosistema'],
  'assetGroups': {'Sellos': {'name': 'Sellos', 'tile': 'm', 'order': order_s, 'files': {n: files[n] for n in order_s}},
                  'Ecosistema': {'name': 'Ecosistema', 'tile': 's', 'order': order_e, 'files': {n: files[n] for n in order_e}}},
  'blobs': {}, 'docs': {'readme': 'project/README.md', 'sections': []},
  'lastChange': {'at': now, 'by': 'Kevin', 'via': 'Claude Code', 'note': 'Adopta la identidad del directorio Manik en marca y títulos: Urbanist, cian del pin y fondos de luz; dentro de las apps siguen Atkinson y el botón azul Manik.'}},
 open('design-system.json', 'w'), indent=2, ensure_ascii=False)
os.makedirs('assets/Sellos', exist_ok=True); os.makedirs('assets/Ecosistema', exist_ok=True)
open('assets/Sellos/README.md', 'w').write('# Sellos\n\nSello madre MedicalManik y los seis productos, en color con fondo transparente (los cortes son máscaras), más el sello madre a una tinta (`currentColor`). Mínimo 24 px en interfaz.\n')
open('assets/Ecosistema/README.md', 'w').write('# Ecosistema\n\nMosaico del Ecosistema Manik, retícula 24: botón que abre el selector de apps. En color (los seis colores de producto) y a una tinta (`currentColor`). Siempre seis cuadros.\n')
print('ok', sorted(os.listdir('components')))
