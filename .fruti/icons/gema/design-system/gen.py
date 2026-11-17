# GEMA · design system (artifact de tipo Design System). Escribe project/.
# Fuentes: marca congelada (../final/, ../identidad/LEEME.md). Lo que la marca no decidió va marcado PROPUESTA; lo heredado de SAM, «heredado de SAM».
import os, json, re, datetime
B = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(B, 'project')
def w(rel, txt):
    p = os.path.join(P, rel); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(txt)
F = os.path.join(B, '..', 'final')
def cuerpo(n):
    s = open(os.path.join(F, n)).read(); s = re.sub(r'<title>.*?</title>', '', s)
    return s[s.index('>', s.index('<svg')) + 1: s.rindex('</svg>')].strip()
SIM = cuerpo('gema-simbolo.svg').replace('var(--gema-pico-a,#052A76)', 'var(--brand-grad-end,#052A76)').replace('var(--gema-pico-b,#3D67AE)', 'var(--brand-grad-start,#3D67AE)')
PROP = 'PROPUESTA (pendiente de aprobar): '
def c(n, l, d, u): return {'name': n, 'value': {'light': l, 'dark': d}, 'usage': u}
tokens = {'name': 'GEMA', 'version': 1,
 'color': {'themes': [{'id': 'light', 'name': 'Claro'}, {'id': 'dark', 'name': 'Oscuro'}], 'tokens': [
  c('surface', '#f2f2ee', '#0a0a0b', 'Fondo de la página. Claro: Papel. Oscuro: Noche (heredado de SAM).'),
  c('surface-raised', '#ffffff', '#16161a', 'Tarjetas, tablas de resultados, paneles y diálogos sobre `surface`.'),
  c('surface-sunken', '#e8e8e2', '#1f1f24', 'Hover de filas y campos de solo lectura.'),
  c('line', '#d6d6d0', '#2a2a30', 'Separadores de filas y bordes decorativos.'),
  c('line-control', '#7a7a82', '#6e6e78', 'Borde de campos y botones secundarios (3.3:1 o más en ambos temas; heredado de SAM).'),
  c('ink', '#0a0a0b', '#f2f2ee', 'Texto principal sobre las tres superficies (17.6:1 o más). Enlaces y foco.'),
  c('ink-muted', '#55555c', '#a3a3a8', 'Folios, unidades secundarias, fechas y ayudas (6.0:1 o más).'),
  c('brand', '#052A76', '#3D67AE', 'Color plano de la interfaz: botón principal, estado «En análisis», selección. Claro: navy (13.1:1 con blanco). Oscuro: azul medio (5.6:1 con blanco; 3.2:1 sobre `surface-raised`). Nunca navy en oscuro: mide 1.5:1 sobre negro. Entra en `--g-color-brand` de Grana.'),
  c('on-brand', '#ffffff', '#ffffff', 'Texto e iconos sobre `brand`.'),
  c('brand-grad-start', '#3D67AE', '#7aa2f0', 'Inicio (arriba) del degradado navy. SOLO superficies de marca: pico del símbolo, icono de la app, panel de inicio de sesión. Nunca en botones ni texto.'),
  c('brand-grad-end', '#052A76', '#3D67AE', 'Final (abajo) del degradado navy. Mismo uso que `brand-grad-start`.'),
  c('focus', '#0a0a0b', '#f2f2ee', 'Anillo de foco de 3 px con 3 px de separación, en todos los controles.'),
  c('danger', '#b42318', '#ff8a7a', 'Resultado «No cumple», errores y muestras vencidas. Siempre con ✕ y palabra (heredado de SAM).'),
  c('warning', '#8a5a00', '#f5b941', 'Muestra «Por vencer» (tiempo de entrega). Siempre con palabra (heredado de SAM).'),
 ]},
 'type': {'fonts': [], 'families': {'sans': '"Onest", ui-sans-serif, system-ui, sans-serif', 'mono': '"JetBrains Mono", ui-monospace, monospace'},
  'groups': [
   {'name': 'Títulos', 'family': 'sans', 'styles': [
     {'name': 'display', 'fontSize': '32px', 'lineHeight': '36px', 'fontWeight': 700, 'sample': 'Resultados del día', 'usage': 'Título de pantalla en escritorio; uno por vista.'},
     {'name': 'title', 'fontSize': '23px', 'lineHeight': '28px', 'fontWeight': 700, 'sample': 'Muestras recibidas', 'usage': 'Título de pantalla en celular y de diálogos.'},
     {'name': 'subtitle', 'fontSize': '18px', 'lineHeight': '24px', 'fontWeight': 600, 'sample': 'Parámetros', 'usage': 'Encabezado de sección o panel.'}]},
   {'name': 'Texto', 'family': 'sans', 'styles': [
     {'name': 'item-title', 'fontSize': '15px', 'lineHeight': '20px', 'fontWeight': 600, 'sample': 'Agua residual · planta norte', 'usage': 'Nombre de una muestra en listas y tablas.'},
     {'name': 'body', 'fontSize': '16px', 'lineHeight': '24px', 'fontWeight': 400, 'sample': 'La muestra llegó a las 09:40.', 'usage': 'Texto corrido: observaciones y notas.'},
     {'name': 'body-sm', 'fontSize': '14px', 'lineHeight': '20px', 'fontWeight': 400, 'sample': 'DBO₅, SST, pH', 'usage': 'Parámetros y metadatos en `ink-muted`.'},
     {'name': 'label', 'fontSize': '14px', 'lineHeight': '20px', 'fontWeight': 600, 'sample': 'Registrar muestra', 'usage': 'Botones, pestañas y etiquetas de campo.'},
     {'name': 'caption', 'fontSize': '12px', 'lineHeight': '16px', 'fontWeight': 600, 'sample': 'En análisis', 'usage': 'Estados y encabezados de tabla.'}]},
   {'name': 'Datos', 'family': 'mono', 'styles': [
     {'name': 'folio', 'fontSize': '12px', 'lineHeight': '16px', 'fontWeight': 500, 'sample': 'M-2026-1184', 'usage': 'Folios de muestra, lote e informe.'},
     {'name': 'value', 'fontSize': '14px', 'lineHeight': '20px', 'fontWeight': 500, 'sample': '18.4 mg/L', 'usage': 'Valores de resultado con su unidad, alineados a la derecha, números tabulares.'}]}]},
 'spacing': {'note': 'Escala de 4 px heredada de SAM.', 'tokens': [
   {'name': 'space-1', 'value': '4px', 'usage': 'Entre folio, nombre y parámetros de una muestra.'},
   {'name': 'space-2', 'value': '8px', 'usage': 'Entre elementos de una fila: estado y valor, icono y texto.'},
   {'name': 'space-3', 'value': '12px', 'usage': 'Relleno vertical de filas de resultados y tarjetas.'},
   {'name': 'space-4', 'value': '16px', 'usage': 'Margen lateral mínimo en celular; relleno de paneles.'},
   {'name': 'space-6', 'value': '24px', 'usage': 'Entre secciones de una pantalla.'},
   {'name': 'space-8', 'value': '32px', 'usage': 'Entre bloques grandes en escritorio.'}]},
 'radius': {'tokens': [
   {'name': 'radius-sm', 'value': '6px', 'usage': 'Botones, campos y tarjetas (heredado de SAM).'},
   {'name': 'radius-md', 'value': '10px', 'usage': 'Paneles, tablas y diálogos.'},
   {'name': 'radius-pill', 'value': '999px', 'usage': 'Estados.'}]},
 'size': {'tokens': [
   {'name': 'control-height', 'value': '44px', 'usage': 'Altura mínima de botones y campos.'},
   {'name': 'symbol-min', 'value': '32px', 'usage': 'Por debajo, el símbolo chico.'}]}}
w('tokens.json', json.dumps(tokens, ensure_ascii=False, indent=2))
w('README.md', '''GEMA (Gestión de Muestras y Análisis) es el sistema interno del laboratorio: registra las muestras que llegan, sus análisis, sus resultados, los informes y el cobro. La marca se resume en tres decisiones: el símbolo es la pantalla de un instrumento con el pico del resultado; el azul viene del navy de Nisa Nabani y su degradado solo vive en la marca; y la letra es Onest, la misma de SAM. La interfaz se construye con Grana; este sistema es la capa de marca y de dominio encima.

## Voz y contenido

- Español, segunda persona, frases cortas y verbos concretos: «Registrar muestra», «Asignar análisis», «Emitir informe».
- Mayúscula solo al inicio: «Resultados del día».
- Escribe valores y unidades como en el informe: `18.4 mg/L`, `7.21`, `196 mg/100 mL A.A.`; subíndices reales (DBO₅); punto decimal.
- Folios tal cual en `folio`: `M-2026-1184`.
- Los resultados se dicen como se dictaminan: «Cumple», «No cumple», «En análisis».
- Errores con causa y salida: «No se pudo emitir el informe: falta el resultado de pH. Captúralo y vuelve a intentar.»
- Sin emojis.

## Color

- Página en `surface`, tablas y tarjetas en `surface-raised`, hovers en `surface-sunken`; texto en `ink`, metadatos en `ink-muted`.
- `brand` es el color plano de la interfaz, siempre con `on-brand` (blanco): navy en claro, azul medio en oscuro. Una acción principal por vista.
- El degradado (`brand-grad-start` → `brand-grad-end`) solo va en superficies de marca: el pico del símbolo, el icono de la app y el panel de inicio de sesión. Nunca en botones, estados ni texto.
- Navy nunca en tema oscuro: mide 1.5:1 sobre negro.
- «Cumple» va en `ink` con ✓: no lleva color. «No cumple» va en `danger` con ✕. Así los dos dictámenes nunca se distinguen solo por tono (un verde y un rojo se confunden con daltonismo).
- `warning` marca muestras «Por vencer». Todo estado lleva palabra.
- En la app, `brand` entra en `--g-color-brand` de Grana y `on-brand` en `--g-color-on-brand`. El resto de la equivalencia con Grana está pendiente.

## Tipografía

- Onest (`sans`) en todo: `display` o `title` para la pantalla, `subtitle` para secciones, `body` para texto, `item-title` para el nombre de una muestra.
- Folios en `folio` y valores con unidad en `value` (JetBrains Mono, números tabulares, alineados a la derecha).

## Espacio, forma y profundidad

- Pasos de 4 px (`space-1` a `space-8`), radios `radius-sm`, `radius-md` y `radius-pill`, controles de `control-height`: todo heredado de SAM.
- Sin sombras: profundidad por superficies y `line`.

## Movimiento

- Solo para cambios de estado: un resultado nuevo aparece con un fundido de 150 ms. Con `prefers-reduced-motion`, sin animación.

## Símbolo y logotipo

- Símbolo «Pantalla + Resultado»: marco y señal en tinta; el pico del resultado en el degradado.
- Desde `symbol-min` (32 px) el grande; por debajo el chico (marco grueso, solo el pico del resultado).
- Logotipo: «GEMA» arriba y «Gestión de Muestras y Análisis» abajo. Horizontal en la barra de la app y documentos; vertical en portadas e inicio; compacto donde no cabe la definición.
- Como `<img>` usa las versiones «sobre-claro» o «sobre-oscuro».
- No deformar, no recolorear el pico, no usar degradado en botones.

## Iconografía

- Los iconos de interfaz los pone Grana; pendiente confirmar su familia.
- Notificaciones push: silueta blanca de una tinta con el pico calado (`notificacion-96.png`).

## Componentes

Botón, Estado, Fila de resultado y Barra de la app son componentes de dominio sobre Grana, con guía y vista previa en ambos temas.
''')
w('assets/Logos/README.md', '# Logos\n\nLogotipos de GEMA con colores fijos para `<img>`, correos y documentos.\n\n- `*-sobre-claro.svg`: tinta `#0a0a0b`, pico navy `#052A76 → #3D67AE`.\n- `*-sobre-oscuro.svg`: tinta `#f2f2ee`, pico `#3D67AE → #7aa2f0`.\n- Horizontal: barra y documentos. Vertical: portadas e inicio. Compacto: sin definición.\n')
w('assets/Iconos/README.md', '# Iconos\n\n- `favicon.svg`: símbolo chico; cambia de tinta con el tema del navegador.\n- `icon-512.png`, `maskable-512.png`: icono de la PWA sobre el degradado navy; el adaptable deja el símbolo en la zona segura.\n- `notificacion-96.png`: silueta blanca de una tinta, pico calado.\n')
CSS = '''/* GEMA · componentes de dominio sobre Grana. Valores de respaldo: tema claro. */
.gema{font-family:var(--font-sans,"Onest",ui-sans-serif,system-ui,sans-serif);color:var(--ink,#0a0a0b)}
.gema-btn{display:inline-flex;align-items:center;justify-content:center;gap:var(--space-2,8px);min-height:var(--control-height,44px);padding:0 18px;border-radius:var(--radius-sm,6px);font:600 14px/20px var(--font-sans,"Onest",sans-serif);cursor:pointer;border:0;text-decoration:none}
.gema-btn--primario{background:var(--brand,#052A76);color:var(--on-brand,#ffffff)}
.gema-btn--secundario{background:transparent;color:var(--ink,#0a0a0b);box-shadow:inset 0 0 0 1.5px var(--line-control,#7a7a82)}
.gema-btn--texto{background:transparent;color:var(--ink,#0a0a0b);text-decoration:underline;text-underline-offset:3px;padding:0 4px}
.gema-btn--primario:hover{filter:brightness(1.12)} .gema-btn--secundario:hover{background:var(--surface-sunken,#e8e8e2)}
.gema-btn[aria-disabled="true"]{background:var(--surface-sunken,#e8e8e2);color:var(--ink-muted,#55555c);box-shadow:none;cursor:not-allowed}
.gema-btn:focus-visible,.gema-fila:focus-visible{outline:3px solid var(--focus,#0a0a0b);outline-offset:3px}
.gema-estado{display:inline-flex;align-items:center;gap:4px;font:600 12px/16px var(--font-sans,"Onest",sans-serif);padding:2px 9px;border-radius:var(--radius-pill,999px);white-space:nowrap}
.gema-estado--activo{background:var(--brand,#052A76);color:var(--on-brand,#ffffff)}
.gema-estado--neutro{color:var(--ink,#0a0a0b);box-shadow:inset 0 0 0 1px var(--line-control,#7a7a82)}
.gema-estado--cumple{color:var(--ink,#0a0a0b);padding-left:0}
.gema-estado--nocumple{color:var(--danger,#b42318);box-shadow:inset 0 0 0 1px currentColor}
.gema-estado--aviso{color:var(--warning,#8a5a00);box-shadow:inset 0 0 0 1px currentColor}
.gema-tabla{width:100%;border-collapse:collapse;background:var(--surface-raised,#ffffff);border:1px solid var(--line,#d6d6d0);border-radius:var(--radius-md,10px);color:var(--ink,#0a0a0b);font:400 14px/20px var(--font-sans,"Onest",sans-serif)}
.gema-tabla th{text-align:left;font:600 12px/16px var(--font-sans,"Onest",sans-serif);color:var(--ink-muted,#55555c);padding:10px 12px;border-bottom:1px solid var(--line,#d6d6d0)}
.gema-tabla td{padding:var(--space-3,12px);border-bottom:1px solid var(--line,#d6d6d0);vertical-align:top}
.gema-tabla tr:last-child td{border-bottom:0} .gema-fila:hover td{background:var(--surface-sunken,#e8e8e2)}
.gema-tabla .n{text-align:right}
.gema-folio{display:block;font:500 12px/16px var(--font-mono,"JetBrains Mono",monospace);color:var(--ink-muted,#55555c);font-variant-numeric:tabular-nums}
.gema-nombre{font:600 15px/20px var(--font-sans,"Onest",sans-serif)}
.gema-valor{font:500 14px/20px var(--font-mono,"JetBrains Mono",monospace);font-variant-numeric:tabular-nums;white-space:nowrap}
.gema-bar{display:flex;align-items:center;gap:var(--space-2,8px);padding:10px var(--space-4,16px);background:var(--surface,#f2f2ee);border-bottom:1px solid var(--line,#d6d6d0);color:var(--ink,#0a0a0b)}
.gema-bar__nombre{font:700 20px/1 var(--font-sans,"Onest",sans-serif)} .gema-bar__sp{flex:1} .gema-bar__ctx{font-size:13px;color:var(--ink-muted,#55555c)}
.gema-bar__btn{min-width:44px;min-height:44px;display:grid;place-items:center;border-radius:var(--radius-sm,6px);background:transparent;border:0;color:var(--ink,#0a0a0b);cursor:pointer}
.gema-bar__btn:hover{background:var(--surface-sunken,#e8e8e2)} .gema-bar__btn:focus-visible{outline:3px solid var(--focus,#0a0a0b);outline-offset:2px}
'''
w('components/bundle.css', CSS)
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap">'
BASE = '<style>body{margin:0;background:var(--surface,#f2f2ee)}.p{display:flex;flex-wrap:wrap;gap:16px;align-items:center;padding:20px}</style>'
def prev(m, body): return f'{m}\n<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}{BASE}</head><body class="gema">{body}</body></html>\n'
w('components/Boton/preview.html', prev('<!-- @dsCard group="Acciones" height=120 subtitle="Principal, secundario, texto y desactivado" -->',
  '<div class="p"><button class="gema-btn gema-btn--primario" type="button">Registrar muestra</button><button class="gema-btn gema-btn--secundario" type="button">Asignar análisis</button><a class="gema-btn gema-btn--texto" href="#">Ver informe</a><button class="gema-btn gema-btn--primario" type="button" aria-disabled="true">Emitir informe</button></div>'))
w('components/Boton/README.md', '''# Botón

Botón de acción de GEMA en color plano: principal, secundario y de texto.

- **Principal** (`gema-btn gema-btn--primario`): la acción que avanza el trabajo («Registrar muestra», «Emitir informe»). Una por vista. Fondo `brand`, texto `on-brand`. Nunca con degradado.
- **Secundario** (`gema-btn--secundario`): acciones alternas. Borde `line-control`.
- **Texto** (`gema-btn--texto`): acciones menores y enlaces.
- **Desactivado**: `aria-disabled="true"` y un texto cerca que diga qué falta.
- El consumidor pone la etiqueta (verbo concreto). Altura mínima `control-height`; foco `focus`.
''')
w('components/Estado/preview.html', prev('<!-- @dsCard group="Estados" height=88 subtitle="Proceso y dictamen" -->',
  '<div class="p"><span class="gema-estado gema-estado--neutro">Recibida</span><span class="gema-estado gema-estado--activo">En análisis</span><span class="gema-estado gema-estado--aviso">Por vencer</span><span class="gema-estado gema-estado--cumple">✓ Cumple</span><span class="gema-estado gema-estado--nocumple">✕ No cumple</span></div>'))
w('components/Estado/README.md', '''# Estado

Dice en qué punto del proceso está una muestra o cuál fue el dictamen de un resultado.

- **Proceso:** «Recibida» (`--neutro`), «En análisis» (`--activo`, único estado con `brand`), «Por vencer» (`--aviso`, `warning`).
- **Dictamen:** «✓ Cumple» (`--cumple`, en `ink`, sin color) y «✕ No cumple» (`--nocumple`, `danger`). El símbolo y la palabra siempre van juntos.
- El consumidor pone el texto (una o dos palabras) y elige la variante.
''')
FIL = [('M-2026-1184', 'Agua residual · planta norte', 'DBO₅', '18.4 mg/L', 'cumple', '✓ Cumple'), ('M-2026-1185', 'Mezcal joven · lote 0711', 'Metanol', '312 mg/100 mL A.A.', 'nocumple', '✕ No cumple'),
       ('M-2026-1186', 'Suelo agrícola · parcela 3', 'pH', '—', 'activo', 'En análisis')]
filas = ''.join(f'<tr class="gema-fila" tabindex="0"><td><span class="gema-folio">{f}</span><span class="gema-nombre">{n}</span></td><td>{p}</td><td class="n"><span class="gema-valor">{v}</span></td><td><span class="gema-estado gema-estado--{k}">{e}</span></td></tr>' for f, n, p, v, k, e in FIL)
w('components/FilaResultado/preview.html', prev('<!-- @dsCard group="Resultados" height=260 subtitle="Cumple, no cumple y en análisis" -->',
  f'<div style="padding:20px;max-width:640px"><table class="gema-tabla"><thead><tr><th>Muestra</th><th>Parámetro</th><th class="n">Valor</th><th>Dictamen</th></tr></thead><tbody>{filas}</tbody></table></div>'))
w('components/FilaResultado/README.md', '''# Fila de resultado

Una fila por parámetro analizado: muestra, parámetro, valor con unidad y dictamen.

- Columnas en este orden: muestra (`gema-folio` + `gema-nombre`), parámetro, valor (`gema-valor`, a la derecha) y Estado de dictamen.
- Sin valor todavía: «—» en el valor y el estado «En análisis».
- La fila completa lleva al detalle de la muestra (`tabindex="0"` y foco visible).
- El consumidor da folio, nombre, parámetro, valor ya formateado con su unidad (punto decimal) y dictamen. Datos de la vista previa: ficticios.
''')
w('components/BarraApp/preview.html', prev('<!-- @dsCard group="Navegación" height=96 subtitle="Logotipo compacto, sucursal y menú" -->',
  f'<div class="gema-bar"><svg viewBox="0 0 48 48" width="28" height="28" aria-hidden="true">{SIM}</svg><span class="gema-bar__nombre">GEMA</span><span class="gema-bar__sp"></span><span class="gema-bar__ctx">Recepción · Oaxaca</span><button class="gema-bar__btn" type="button" aria-label="Abrir menú"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button></div>'))
w('components/BarraApp/README.md', '''# Barra de la app

Barra superior con el logotipo compacto, el área y la sucursal activas y el menú.

- Símbolo grande a 28 px (en línea; marco y señal en `ink`, pico en el degradado) y «GEMA» en Onest 700.
- A la derecha, el contexto en `ink-muted` («Recepción · Oaxaca»): el laboratorio tiene dos sucursales con instalación propia.
- Botón de menú de 44 × 44 px con `aria-label`. El título de la pantalla va debajo, no en la barra.
''')
w('components/Cover/preview.html', '<!-- @dsCard height=288 -->\n<!doctype html><html lang="es"><head><meta charset="utf-8">' + FONTS + '''
<style>
body{margin:0;background:var(--surface,#f2f2ee)}
.cv{position:relative;width:960px;height:288px;overflow:hidden}
.cv svg{position:absolute;left:0;top:0}
.ground{fill:var(--surface,#f2f2ee)} .navy{fill:var(--brand-grad-end,#052A76)} .azul{fill:var(--brand-grad-start,#3D67AE)} .raised{fill:var(--surface-raised,#ffffff)} .ink{fill:var(--ink,#0a0a0b)}
.edge{fill:none;stroke:var(--ink,#0a0a0b);stroke-width:6} .r{rx:10px}
.txt{position:absolute;left:48px;bottom:40px;max-width:440px}
.n{font:700 120px/.92 "Onest",ui-sans-serif,system-ui,sans-serif;letter-spacing:-.02em;color:var(--ink,#0a0a0b);margin:0}
.t{font:500 14px/20px "Onest",ui-sans-serif,system-ui,sans-serif;color:var(--ink-muted,#55555c);margin:12px 0 0}
</style></head><body>
<div class="cv"><svg width="960" height="288" viewBox="0 0 960 288" aria-hidden="true">
<!-- blocks: brand-grad-end (navy) 320×288 bleeding off the right, brand-grad-start (azul) 160×200, ink 96×64; radius-md 10px
     arrangement: one tall navy slab at the right edge with the azul block stepping in front, like the instrument screen
     pattern: literal motif (the symbol's signal): the two-peak trace crossing the blocks; README: "el pico del resultado"
     steps and radii: space-8 32px insets, space-6 24px offsets, radius-md 10px -->
<rect class="ground" width="960" height="288"/>
<rect class="navy r" x="680" y="-10" width="300" height="310"/>
<rect class="azul r" x="560" y="56" width="176" height="200"/>
<rect class="ink r" x="872" y="216" width="120" height="64"/>
<path d="M496 232H560C590 232 600 168 616 168C632 168 642 232 672 232C708 232 724 64 752 64C780 64 796 232 832 232H960" fill="none" stroke="var(--surface,#f2f2ee)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
<div class="txt"><p class="n">GEMA</p><p class="t">Gestión de Muestras y Análisis</p></div></div>
</body></html>
''')
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
A = {'Logos': {'gema-logotipo-horizontal-sobre-claro.svg': ('b8d159f2ef7bed08ffbd23f8c21464e5', 32341, 'image/svg+xml'),
               'gema-logotipo-horizontal-sobre-oscuro.svg': ('2f109444f0bc3128031534bc39914ab9', 32343, 'image/svg+xml'),
               'gema-logotipo-vertical-sobre-claro.svg': ('f4f79b76902d207d39f2668e97f84ddc', 32355, 'image/svg+xml'),
               'gema-logotipo-vertical-sobre-oscuro.svg': ('44450e1ed1c841a0910e4f08ca04ed99', 32357, 'image/svg+xml'),
               'gema-logotipo-compacto-sobre-claro.svg': ('6e60b621c31a95f29542161126605c46', 2297, 'image/svg+xml'),
               'gema-logotipo-compacto-sobre-oscuro.svg': ('dca1f98e940c85d82ab3f181d20953b6', 2299, 'image/svg+xml')},
     'Iconos': {'favicon.svg': ('23189a0d3a2fc0e43c5c3a3e5e994f7a', 650, 'image/svg+xml'), 'icon-512.png': ('02818a4ac00c726667bd485a426506c4', 92658, 'image/png'),
                'maskable-512.png': ('393de1d61e5d24059553f7744b653901', 67507, 'image/png'), 'notificacion-96.png': ('877ffeda2d81a17627a83b550eb2864d', 2269, 'image/png')}}
idx = {'v': 3, 'layout': 'files', 'createdOnFiles': {'v': 1, 'at': now}, 'title': 'GEMA', 'namespace': 'GEMA', 'libraries': [], 'sections': {}, 'groups': ['Logos', 'Iconos'],
       'assetGroups': {g: {'name': g, 'tile': 'l' if g == 'Logos' else 'm', 'order': list(fs), 'files': {n: {'name': n, 'blob': b, 'size': s, 'type': t} for n, (b, s, t) in fs.items()}} for g, fs in A.items()},
       'blobs': {}, 'docs': {'sections': []}, 'lastChange': {'by': 'Claude', 'at': now, 'via': 'Claude Code', 'note': 'Primera versión desde la marca congelada (Pantalla + Resultado, degradado navy, Onest).'}}
w('design-system.json', json.dumps(idx, ensure_ascii=False, indent=2)); print('ok')
