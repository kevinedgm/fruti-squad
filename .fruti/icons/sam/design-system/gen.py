# SAM · design system (artifact de tipo Design System). Escribe project/ para publicarlo.
# Fuentes: marca congelada (../final/, ../identidad/LEEME.md). Lo que la marca no decidió va marcado como PROPUESTA.
import os, json, re, datetime
B = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(B, 'project')
def w(rel, txt):
    p = os.path.join(P, rel); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(txt)
F = os.path.join(B, '..', 'final')
def cuerpo(n):
    s = open(os.path.join(F, n)).read(); s = re.sub(r'<title>.*?</title>', '', s)
    return s[s.index('>', s.index('<svg')) + 1: s.rindex('</svg>')].strip()
C2 = cuerpo('sam-simbolo.svg').replace('var(--g-color-brand,#c6f432)', 'var(--brand,#c6f432)').replace('var(--sam-tinta,#0a0a0b)', 'var(--on-brand,#0a0a0b)')
C4 = cuerpo('sam-simbolo-chico.svg').replace('var(--g-color-brand,#c6f432)', 'var(--brand,#c6f432)').replace('var(--sam-tinta,#0a0a0b)', 'var(--on-brand,#0a0a0b)')
PROP = ''  # propuestas aprobadas por el usuario el 2026-11-13
def c(n, d, l, u): return {'name': n, 'value': {'dark': d, 'light': l}, 'usage': u}
tokens = {
 'name': 'SAM', 'version': 1,
 'color': {'themes': [{'id': 'dark', 'name': 'Oscuro'}, {'id': 'light', 'name': 'Claro'}], 'tokens': [
  c('surface', '#0a0a0b', '#f2f2ee', 'Fondo de la página. Oscuro: Noche. Claro: Papel.'),
  c('surface-raised', '#16161a', '#ffffff', 'Tarjetas de actividad, paneles y diálogos sobre `surface`.'),
  c('surface-sunken', '#1f1f24', '#e8e8e2', 'Hover de filas, pestañas inactivas y campos de solo lectura.'),
  c('line', '#2a2a30', '#d6d6d0', 'Separadores y bordes decorativos (no llevan significado; no necesitan 3:1).'),
  c('line-control', '#6e6e78', '#7a7a82', PROP + 'Borde de campos y botones secundarios: 3.3:1 o más sobre `surface`, `surface-raised` y `surface-sunken` en ambos temas.'),
  c('ink', '#f2f2ee', '#0a0a0b', 'Texto principal sobre `surface`, `surface-raised` y `surface-sunken` (17.6:1 o más en ambos temas). En claro también enlaces y foco.'),
  c('ink-muted', '#a3a3a8', '#55555c', 'Texto secundario: metadatos, fechas, ayudas. 6.0:1 o más sobre las tres superficies en ambos temas.'),
  c('brand', '#c6f432', '#c6f432', 'Voltaje. SOLO relleno: botón principal, estado activo («En curso»), tarjeta del símbolo y `--g-color-brand` de Grana. Nunca texto. Sobre `surface` claro mide 1.1:1: ahí siempre lleva `brand-edge`.'),
  c('on-brand', '#0a0a0b', '#0a0a0b', 'Texto e iconos sobre `brand` (15.4:1). También la palomita del símbolo.'),
  c('brand-edge', '#c6f432', '#0a0a0b', 'Contorno de todo relleno `brand`. En oscuro coincide con el relleno; en claro es tinta (2 px en botones, 1.5 px en estados).'),
  c('focus', '#f2f2ee', '#0a0a0b', 'Anillo de foco de 3 px con 3 px de separación. 17.6:1 sobre `surface` en ambos temas; nunca Voltaje (en claro no se ve).'),
  c('danger', '#ff8a7a', '#b42318', PROP + 'Estado «Vencida» y errores. Texto 5.3:1 o más sobre las tres superficies en ambos temas. Siempre con palabra o icono.'),
  c('warning', '#f5b941', '#8a5a00', PROP + 'Estado «Por vencer». 4.8:1 o más en ambos temas. Se distingue de `danger` por la palabra, no por el tono (entre ellos miden 1.1–1.3:1).'),
  c('info', '#8ab4ff', '#2f5bd3', PROP + 'Avisos informativos y enlaces dentro de avisos. 4.8:1 o más en ambos temas.'),
 ]},
 'type': {
  'fonts': [],
  'families': {'sans': '"Onest", ui-sans-serif, system-ui, sans-serif', 'mono': '"JetBrains Mono", ui-monospace, monospace'},
  'groups': [
   {'name': 'Títulos', 'family': 'sans', 'styles': [
     {'name': 'display', 'fontSize': '32px', 'lineHeight': '36px', 'fontWeight': 700, 'letterSpacing': '-0.01em', 'sample': 'Mis actividades', 'usage': 'Título de pantalla en escritorio. Uno por vista.'},
     {'name': 'title', 'fontSize': '23px', 'lineHeight': '28px', 'fontWeight': 700, 'sample': 'Mis actividades', 'usage': 'Título de pantalla en celular y de diálogos.'},
     {'name': 'subtitle', 'fontSize': '18px', 'lineHeight': '24px', 'fontWeight': 600, 'sample': 'Notificación de prueba', 'usage': 'Encabezado de sección o panel.'}]},
   {'name': 'Texto', 'family': 'sans', 'styles': [
     {'name': 'item-title', 'fontSize': '15px', 'lineHeight': '20px', 'fontWeight': 600, 'sample': 'El reporte diario de atrasos no llegó a Discord', 'usage': 'Título de una actividad en listas y tarjetas.'},
     {'name': 'body', 'fontSize': '16px', 'lineHeight': '24px', 'fontWeight': 400, 'sample': 'Revisé el webhook y la tarea programada.', 'usage': 'Texto corrido: descripciones y comentarios.'},
     {'name': 'body-sm', 'fontSize': '14px', 'lineHeight': '20px', 'fontWeight': 400, 'sample': '3 abiertas · 1 vence hoy', 'usage': 'Resúmenes y metadatos en `ink-muted`.'},
     {'name': 'label', 'fontSize': '14px', 'lineHeight': '20px', 'fontWeight': 600, 'sample': 'Avanzar etapa', 'usage': 'Botones, pestañas y etiquetas de campo.'},
     {'name': 'caption', 'fontSize': '12px', 'lineHeight': '16px', 'fontWeight': 600, 'sample': 'En curso', 'usage': 'Estados (chips) y notas breves.'}]},
   {'name': 'Datos', 'family': 'mono', 'styles': [
     {'name': 'folio', 'fontSize': '12px', 'lineHeight': '16px', 'fontWeight': 500, 'sample': 'INC-2041 · TAR-0187', 'usage': 'Folios, horas y valores que se comparan en columna (números tabulares).'}]}]},
 'spacing': {'note': 'Escala de 4 px tomada de las maquetas de la marca.', 'tokens': [
   {'name': 'space-1', 'value': '4px', 'usage': 'Entre folio, título y metadatos de una actividad.'},
   {'name': 'space-2', 'value': '8px', 'usage': 'Entre elementos de una fila: chip y fecha, icono y texto.'},
   {'name': 'space-3', 'value': '12px', 'usage': 'Relleno de tarjetas de actividad; separación entre tarjetas de una lista.'},
   {'name': 'space-4', 'value': '16px', 'usage': 'Margen lateral mínimo en celular; relleno de paneles.'},
   {'name': 'space-6', 'value': '24px', 'usage': 'Entre secciones de una pantalla.'},
   {'name': 'space-8', 'value': '32px', 'usage': 'Entre bloques grandes en escritorio.'}]},
 'radius': {'tokens': [
   {'name': 'radius-sm', 'value': '6px', 'usage': 'Botones, campos y tarjetas de actividad (las maquetas de la marca).'},
   {'name': 'radius-md', 'value': '10px', 'usage': 'Paneles y diálogos.'},
   {'name': 'radius-pill', 'value': '999px', 'usage': 'Estados (chips).'}]},
 'size': {'note': 'Tamaños de control.', 'tokens': [
   {'name': 'control-height', 'value': '44px', 'usage': 'Altura mínima de botones y campos (objetivo táctil de 44 px).'},
   {'name': 'symbol-min', 'value': '32px', 'usage': 'Por debajo de este tamaño se usa el símbolo chico.'}]},
}
w('tokens.json', json.dumps(tokens, ensure_ascii=False, indent=2))
README = '''SAM es la herramienta con la que el equipo de desarrollo y soporte registra, mueve y cierra su trabajo. Su marca se resume en tres decisiones: el símbolo Tarjetas dice «actividad» sin letra, Voltaje es un relleno que marca lo activo, y Onest se usa igual en la marca y en la interfaz. La interfaz se construye con Grana; este sistema es la capa de marca y de dominio encima de Grana.

## Voz y contenido

- Escribe en español, en segunda persona («Te toca revisar la evidencia»), con frases cortas y verbos concretos: «Avanzar etapa», «Adjuntar evidencia», «Nueva actividad». Nunca «Gestionar».
- Usa mayúscula solo al inicio y en nombres propios: «Mis actividades», no «Mis Actividades».
- Nombra los estados por lo que significan para quien trabaja: «En curso», «Revisión», «Nuevo», «Vencida».
- Los folios van tal cual en `folio`: `INC-2041`, `TAR-0187`. Las fechas, cortas: «Vence hoy, 18:00», «15 nov».
- Los errores dicen qué pasó y cómo seguir, sin disculpas: «No se pudo adjuntar el archivo: pesa más de 20 MB. Comprímelo y vuelve a intentar.»
- Sin emojis.

## Color

- Pinta la página con `surface`, las tarjetas con `surface-raised` y los hovers con `surface-sunken`. Texto en `ink`; metadatos en `ink-muted`.
- `brand` (Voltaje) es solo relleno: botón principal, estado activo y la tarjeta del símbolo. Pon encima `on-brand`. Nunca escribas texto en `brand`.
- Todo relleno `brand` lleva contorno `brand-edge`. En oscuro no se nota; en claro es lo que lo separa del fondo (Voltaje sobre Papel mide 1.1:1).
- El foco es `focus`, 3 px sólidos con 3 px de separación, en todos los controles. Nunca Voltaje.
- Una sola acción principal en Voltaje por vista. Las demás, secundarias (borde `line-control`) o de texto.
- `danger` (vencida, errores), `warning` (por vencer) e `info` (avisos) llevan siempre su palabra: el color no basta.
- En la app, Voltaje entra en `--g-color-brand` de Grana y `on-brand` en `--g-color-on-brand`. El resto de la equivalencia con los tokens de Grana está pendiente: no conocemos su lista completa.

## Tipografía

- Todo en Onest (`sans`). Títulos de pantalla en `title` (celular) o `display` (escritorio), uno por vista; secciones en `subtitle`; texto en `body`.
- Títulos de actividad en `item-title`; metadatos en `body-sm` y `ink-muted`; botones en `label`; estados en `caption`.
- Folios, horas y datos en columna, en `folio` (JetBrains Mono) con números tabulares.
- Ambas fuentes vienen de Google Fonts (licencia OFL); no hay archivos de fuente en el sistema.

## Espacio, forma y profundidad

- Espaciado en pasos de 4 px (`space-1` a `space-8`). Margen lateral mínimo `space-4` en celular.
- Radios: `radius-sm` en botones, campos y tarjetas; `radius-md` en paneles y diálogos; `radius-pill` en estados.
- Sin sombras: la profundidad la dan las superficies (`surface` → `surface-raised`) y los bordes `line`.
- Altura mínima de controles: `control-height` (44 px).

## Movimiento

- Solo para explicar un cambio de estado: la tarjeta que avanza de etapa se desliza hacia delante 8 px y se asienta (200 ms, curva de salida `cubic-bezier(0.16, 1, 0.3, 1)`).
- Con `prefers-reduced-motion`, el cambio es inmediato, sin desplazamiento.

## Símbolo y logotipo

- Símbolo Tarjetas: la tarjeta anterior en contorno de tinta (ya pasó), la actual en Voltaje con contorno de tinta y la palomita en `on-brand`.
- Desde `symbol-min` (32 px) usa el símbolo grande; por debajo, el chico (tarjetas más separadas, trazo más grueso).
- Logotipo horizontal en la barra de la app y documentos; vertical en portadas e inicio; compacto (sin «Simple Activity Manager») donde no cabe el descriptor.
- No lo deformes, no cambies Voltaje por otro color, no quites el contorno sobre fondo claro, no separes la palomita.
- Como `<img>` usa las versiones «sobre-oscuro» o «sobre-claro» (colores fijos). En línea, el símbolo hereda la tinta con `currentColor`.

## Iconografía

- Los iconos de interfaz los pone Grana. Pendiente de definir: qué familia usa Grana y si la marca necesita alguno propio.
- El icono pequeño de las notificaciones push es una silueta blanca de una tinta (`notificacion-96.png`).

## Componentes

Botón, Estado, Tarjeta de actividad y Barra de la app son componentes de dominio de SAM sobre Grana. Cada uno tiene su guía y su vista previa en ambos temas.
'''
w('README.md', README)
w('assets/Logos/README.md', '''# Logos

Logotipos de SAM con colores fijos, para usar como `<img>`, en correos y documentos.

- `*-sobre-oscuro.svg`: tinta Papel `#f2f2ee`, para fondos `surface` oscuros.
- `*-sobre-claro.svg`: tinta Noche `#0a0a0b`, para fondos `surface` claros.
- Horizontal: barra de la app y documentos. Vertical: portadas e inicio. Compacto: sin descriptor, espacios chicos.
- Área libre: la altura de la tarjeta Voltaje del símbolo.
''')
w('assets/Iconos/README.md', '''# Iconos

- `favicon.svg`: símbolo chico; cambia la tinta con el tema del navegador (Noche en claro, Papel en oscuro).
- `icon-512.png`: icono de la PWA sobre Noche, con esquinas redondeadas.
- `maskable-512.png`: icono adaptable de Android; el símbolo cabe en la zona segura (300 de 512).
- `notificacion-96.png`: icono pequeño de notificación push; silueta blanca de una tinta sobre transparente.
''')
# Componentes: estilos en bundle.css (con valores de respaldo del tema oscuro por si tokens.css aún no existe)
CSS = '''/* SAM · componentes de dominio sobre Grana. Valores de respaldo: tema oscuro. */
.sam{font-family:var(--font-sans,"Onest",ui-sans-serif,system-ui,sans-serif);color:var(--ink,#f2f2ee)}
.sam-btn{display:inline-flex;align-items:center;justify-content:center;gap:var(--space-2,8px);min-height:var(--control-height,44px);padding:0 18px;border-radius:var(--radius-sm,6px);font:600 14px/20px var(--font-sans,"Onest",sans-serif);cursor:pointer;border:0;text-decoration:none}
.sam-btn--primario{background:var(--brand,#c6f432);color:var(--on-brand,#0a0a0b);box-shadow:inset 0 0 0 2px var(--brand-edge,#c6f432)}
.sam-btn--secundario{background:transparent;color:var(--ink,#f2f2ee);box-shadow:inset 0 0 0 1.5px var(--line-control,#6e6e78)}
.sam-btn--texto{background:transparent;color:var(--ink,#f2f2ee);text-decoration:underline;text-underline-offset:3px;padding:0 4px}
.sam-btn--primario:hover{filter:brightness(1.06)} .sam-btn--secundario:hover{background:var(--surface-sunken,#1f1f24)}
.sam-btn:active{transform:translateY(1px)}
.sam-btn[aria-disabled="true"]{background:var(--surface-sunken,#1f1f24);color:var(--ink-muted,#a3a3a8);box-shadow:none;cursor:not-allowed}
.sam-btn:focus-visible,.sam-card:focus-visible{outline:3px solid var(--focus,#f2f2ee);outline-offset:3px}
.sam-chip{display:inline-flex;align-items:center;gap:4px;font:600 12px/16px var(--font-sans,"Onest",sans-serif);padding:2px 9px;border-radius:var(--radius-pill,999px);white-space:nowrap}
.sam-chip--activo{background:var(--brand,#c6f432);color:var(--on-brand,#0a0a0b);box-shadow:inset 0 0 0 1.5px var(--brand-edge,#c6f432)}
.sam-chip--neutro{color:var(--ink,#f2f2ee);box-shadow:inset 0 0 0 1px var(--line-control,#6e6e78)}
.sam-chip--peligro{color:var(--danger,#ff8a7a);box-shadow:inset 0 0 0 1px currentColor}
.sam-chip--aviso{color:var(--warning,#f5b941);box-shadow:inset 0 0 0 1px currentColor}
.sam-card{display:grid;gap:var(--space-1,4px);padding:var(--space-3,12px);background:var(--surface-raised,#16161a);border:1px solid var(--line,#2a2a30);border-radius:var(--radius-sm,6px);color:var(--ink,#f2f2ee);text-decoration:none}
.sam-card:hover{background:var(--surface-sunken,#1f1f24)}
.sam-card__folio{font:500 12px/16px var(--font-mono,"JetBrains Mono",monospace);font-variant-numeric:tabular-nums;color:var(--ink-muted,#a3a3a8)}
.sam-card__titulo{font:600 15px/20px var(--font-sans,"Onest",sans-serif);overflow-wrap:anywhere}
.sam-card__pie{display:flex;flex-wrap:wrap;gap:var(--space-2,8px);align-items:center;margin-top:var(--space-1,4px);font:400 13px/18px var(--font-sans,"Onest",sans-serif);color:var(--ink-muted,#a3a3a8)}
.sam-bar{display:flex;align-items:center;gap:var(--space-2,8px);padding:10px var(--space-4,16px);background:var(--surface,#0a0a0b);border-bottom:1px solid var(--line,#2a2a30);color:var(--ink,#f2f2ee)}
.sam-bar__nombre{font:700 20px/1 var(--font-sans,"Onest",sans-serif);letter-spacing:-.01em}
.sam-bar__sp{flex:1}
.sam-bar__btn{min-width:44px;min-height:44px;display:grid;place-items:center;border-radius:var(--radius-sm,6px);background:transparent;border:0;color:var(--ink,#f2f2ee);cursor:pointer}
.sam-bar__btn:hover{background:var(--surface-sunken,#1f1f24)} .sam-bar__btn:focus-visible{outline:3px solid var(--focus,#f2f2ee);outline-offset:2px}
@media (prefers-reduced-motion:reduce){.sam-btn:active{transform:none}}
'''
w('components/bundle.css', CSS)
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap">'
BASE = '<style>body{margin:0;background:var(--surface,#0a0a0b)}.p{display:flex;flex-wrap:wrap;gap:16px;align-items:center;padding:20px}</style>'
def prev(marker, body): return f'{marker}\n<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}{BASE}</head><body class="sam">{body}</body></html>\n'
w('components/Boton/preview.html', prev('<!-- @dsCard group="Acciones" height=120 subtitle="Principal, secundario, texto y desactivado" -->',
  '<div class="p"><button class="sam-btn sam-btn--primario" type="button">Avanzar etapa</button><button class="sam-btn sam-btn--secundario" type="button">Reasignar</button><a class="sam-btn sam-btn--texto" href="#">Adjuntar evidencia</a><button class="sam-btn sam-btn--primario" type="button" aria-disabled="true">Cerrar actividad</button></div>'))
w('components/Boton/README.md', '''# Botón

Botón de acción de SAM: principal en Voltaje, secundario con borde y de texto.

- **Principal** (`sam-btn sam-btn--primario`): la acción que hace avanzar el trabajo («Avanzar etapa», «Nueva actividad»). Una por vista. Relleno `brand`, texto `on-brand`, contorno `brand-edge`.
- **Secundario** (`sam-btn--secundario`): acciones alternas («Reasignar»). Borde `line-control`.
- **Texto** (`sam-btn--texto`): acciones menores y enlaces («Adjuntar evidencia»). Subrayado, en `ink`.
- **Desactivado**: `aria-disabled="true"` y un texto cerca que diga qué falta; no lo quites del orden de tabulación.
- El consumidor pone la etiqueta: un verbo concreto. Altura mínima `control-height`; foco con `focus`.
- No: dos botones principales en el mismo bloque, Voltaje con texto blanco, un icono sin etiqueta.
''')
w('components/Estado/preview.html', prev('<!-- @dsCard group="Estados" height=88 subtitle="Activo, neutros y alertas" -->',
  '<div class="p"><span class="sam-chip sam-chip--activo">En curso</span><span class="sam-chip sam-chip--neutro">Nuevo</span><span class="sam-chip sam-chip--neutro">Revisión</span><span class="sam-chip sam-chip--neutro">Cerrada</span><span class="sam-chip sam-chip--aviso">Por vencer</span><span class="sam-chip sam-chip--peligro">Vencida</span></div>'))
w('components/Estado/README.md', '''# Estado

Chip que dice en qué etapa o situación está una actividad.

- **Activo** (`sam-chip--activo`): solo «En curso», lo que alguien está trabajando ahora. Relleno `brand` con contorno `brand-edge`.
- **Neutro** (`sam-chip--neutro`): el resto de etapas («Nuevo», «Revisión», «Cerrada»). Las etapas las define cada plantilla de flujo; el chip muestra su nombre.
- **Por vencer** y **Vencida** (`sam-chip--aviso`, `sam-chip--peligro`): con `warning` y `danger`.
- Siempre con palabra: el color nunca es la única señal.
- El consumidor pone el texto de la etapa (corto, una o dos palabras).
''')
ACT = [('INC-2041', 'El reporte diario de atrasos no llegó a Discord', 'activo', 'En curso', 'Vence hoy, 18:00'),
       ('TAR-0187', 'Migrar plantillas de alta de usuario al editor visual y revisar los campos dinámicos que quedaron sin validación', 'neutro', 'Revisión', 'Vence 15 nov'),
       ('INC-2033', 'Ticket de WhatsApp sin evidencia adjunta', 'peligro', 'Vencida', 'Venció 10 nov')]
cards = ''.join(f'<a class="sam-card" href="#"><span class="sam-card__folio">{f}</span><span class="sam-card__titulo">{t}</span><span class="sam-card__pie"><span class="sam-chip sam-chip--{k}">{e}</span><span>{v}</span></span></a>' for f, t, k, e, v in ACT)
w('components/TarjetaActividad/preview.html', prev('<!-- @dsCard group="Actividades" height=360 subtitle="En curso, título largo y vencida" -->',
  f'<div style="display:grid;gap:12px;padding:20px;max-width:420px">{cards}</div>'))
w('components/TarjetaActividad/README.md', '''# Tarjeta de actividad

Una actividad en una lista: folio, título, estado y vencimiento; toda la tarjeta lleva a su detalle.

- Orden fijo: `sam-card__folio` (en `folio`), `sam-card__titulo` (en `item-title`), `sam-card__pie` con el Estado y la fecha en `ink-muted`.
- Toda la tarjeta es un enlace al detalle; no pongas botones dentro.
- Títulos largos: se ajustan en varias líneas, nunca se cortan con puntos suspensivos en la lista.
- Lista: tarjetas separadas por `space-3`; en celular, una columna.
- El consumidor da folio, título, estado (texto y variante), vencimiento ya redactado y la URL del detalle.
- Datos de la vista previa: ficticios.
''')
w('components/BarraApp/preview.html', prev('<!-- @dsCard group="Navegación" height=96 subtitle="Logotipo compacto y menú" -->',
  f'<div class="sam-bar"><svg viewBox="0 0 48 48" width="28" height="28" aria-hidden="true">{C2}</svg><span class="sam-bar__nombre">SAM</span><span class="sam-bar__sp"></span><button class="sam-bar__btn" type="button" aria-label="Abrir menú"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button></div>'))
w('components/BarraApp/README.md', '''# Barra de la app

Barra superior de SAM con el logotipo compacto y el acceso al menú.

- Símbolo grande a 28 px (en línea, hereda `ink` con `currentColor`) y «SAM» en Onest 700.
- Fondo `surface` y borde inferior `line`. El botón de menú mide al menos 44 × 44 px y tiene `aria-label`.
- El consumidor pone las acciones de la derecha (menú, cuenta). El título de la pantalla va debajo, en `title`, no en la barra.
- El logo lleva a «Mis actividades».
''')
# Portada
w('components/Cover/preview.html', '''<!-- @dsCard height=288 -->
<!doctype html><html lang="es"><head><meta charset="utf-8">''' + FONTS + '''
<style>
body{margin:0;background:var(--surface,#0a0a0b)}
.cv{position:relative;width:960px;height:288px;overflow:hidden}
.cv svg{position:absolute;left:0;top:0}
.ground{fill:var(--surface,#0a0a0b)} .raised{fill:var(--surface-raised,#16161a)} .brand{fill:var(--brand,#c6f432)} .ink{fill:var(--ink,#f2f2ee)}
.edge{fill:none;stroke:var(--ink,#f2f2ee);stroke-width:4} .brandedge{stroke:var(--brand-edge,#c6f432);stroke-width:4}
.r{rx:10px}
.txt{position:absolute;left:48px;bottom:40px;max-width:440px}
.n{font:700 120px/.92 "Onest",ui-sans-serif,system-ui,sans-serif;letter-spacing:-.02em;color:var(--ink,#f2f2ee);margin:0}
.t{font:500 14px/20px "Onest",ui-sans-serif,system-ui,sans-serif;color:var(--ink-muted,#a3a3a8);margin:12px 0 0}
</style></head><body>
<div class="cv"><svg width="960" height="288" viewBox="0 0 960 288" aria-hidden="true">
<!-- blocks: brand (Voltaje) 256×176, ink 160×112, surface-raised 224×160; radius-md 10px
     arrangement: staggered stack bleeding off the right edge, like activity cards passing forward
     pattern: literal motif (the symbol's cards): three card outlines stepping right at space-6 pitch; README: "una tarjeta de actividad pasa adelante"
     steps and radii: space-6 24px offsets, space-8 32px gaps, radius-md 10px -->
<rect class="ground" width="960" height="288"/>
<rect class="raised r" x="528" y="24" width="224" height="160"/>
<rect class="edge r" x="560" y="56" width="224" height="160"/>
<rect class="brand brandedge r" x="680" y="88" width="256" height="176"/>
<path d="M760 178l26 24 54-54" fill="none" stroke="var(--on-brand,#0a0a0b)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
<rect class="ink r" x="872" y="-24" width="160" height="112"/>
</svg>
<div class="txt"><p class="n">SAM</p><p class="t">Simple Activity Manager</p></div></div>
</body></html>
''')
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
A = {
 'Logos': {'sam-logotipo-horizontal-sobre-oscuro.svg': ('75c38ab6810dd9c3cbd4b2f1ca5bc692', 24342, 'image/svg+xml'),
           'sam-logotipo-horizontal-sobre-claro.svg': ('9a34f8faa60581d810d55c59b12b8e85', 24342, 'image/svg+xml'),
           'sam-logotipo-vertical-sobre-oscuro.svg': ('edcb3c435794a3d894a87d6171f9c477', 24356, 'image/svg+xml'),
           'sam-logotipo-vertical-sobre-claro.svg': ('7500532a557b5a8e553b47f904f89678', 24356, 'image/svg+xml'),
           'sam-logotipo-compacto-sobre-oscuro.svg': ('a6263928723170ff69d4dc71403c833c', 2693, 'image/svg+xml'),
           'sam-logotipo-compacto-sobre-claro.svg': ('08477b2f9eaf2580bf307c75367ecfbc', 2693, 'image/svg+xml')},
 'Iconos': {'favicon.svg': ('61516da28becc84ddb9bf3aaab52feda', 452, 'image/svg+xml'),
            'icon-512.png': ('3d580ca228bdfc02a598b26f16f037b9', 15788, 'image/png'),
            'maskable-512.png': ('1213c1089cf95ead1cf423d38c01a1b1', 8741, 'image/png'),
            'notificacion-96.png': ('8b1a64bdf37647f33bec423288afb159', 1576, 'image/png')}}
idx = {'v': 3, 'layout': 'files', 'createdOnFiles': {'v': 1, 'at': now}, 'title': 'SAM', 'namespace': 'SAM', 'libraries': [],
       'sections': {}, 'groups': ['Logos', 'Iconos'],
       'assetGroups': {g: {'name': g, 'tile': 'l' if g == 'Logos' else 'm', 'order': list(fs), 'files': {n: {'name': n, 'blob': b, 'size': s, 'type': t} for n, (b, s, t) in fs.items()}} for g, fs in A.items()},
       'blobs': {}, 'docs': {'sections': []},
       'lastChange': {'by': 'Claude', 'at': now, 'via': 'Claude Code', 'note': 'Primera versión desde la marca congelada (Tarjetas, Voltaje, Onest).'}}
w('design-system.json', json.dumps(idx, ensure_ascii=False, indent=2))
print('ok')
