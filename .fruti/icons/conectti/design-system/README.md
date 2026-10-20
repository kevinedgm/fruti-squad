Conectti es la interfaz de un laboratorio de análisis de muestras químicas: recepción, seguimiento, resultados e informes. Su lenguaje visual es el de un instrumento de medición: fondo neutro y frío, un solo azul que significa «puedes actuar aquí», cifras alineadas y color de estado solo donde hay un veredicto.

## Principios

- **Un solo tema, claro.** Conectti no tiene modo oscuro: es una herramienta de laboratorio que se usa con luz de trabajo y se imprime. No agregues superficies oscuras ni paneles invertidos.
- **Neutro primero.** El grafito y el blanco ocupan casi toda la pantalla. El color se reserva para la acción (`brand`), la selección (`accent`) y el veredicto (`success`, `warning`, `danger`).
- **Cada color, un significado.** Azul = interactivo o informativo. Verde azulado = seleccionado o en curso. Verde, ámbar y rojo = conforme, atención y no conforme. No se mezclan.
- **Delimitar con borde, no con sombra.** Las tarjetas se separan del fondo con `surface` sobre `bg` y un contorno `border`. La sombra (`shadow-md`) es solo para lo que flota.
- **Las cifras mandan.** Resultados, folios y límites van en mono (`data`, `kpi`) y alineados a la derecha, para comparar de un vistazo.

## Contenido y tono

- Español de México, frases cortas y concretas. Acciones en infinitivo: «Registrar muestra», «Exportar informe», «Validar resultado».
- Estados en el vocabulario del laboratorio: «Conforme», «No conforme», «Por revisar», «En análisis», «Recibida».
- Unidades SI con espacio entre número y unidad: `25 °C`, `0.05 mg/L`, `6.84 pH`. Punto decimal. Mantén las cifras significativas del método; no redondees en la interfaz.
- Sin emoji y sin signos de exclamación en mensajes del sistema.

## Color

**Superficies y texto**

- Fondo de página: `bg`. Tarjetas, tablas y formularios: `surface` con contorno `border`. Menús, popovers y diálogos: `surface-raised` con `shadow-md`. Lo que va «dentro» de otra superficie (encabezado de tabla, resumen, campo de solo lectura): `surface-sunken`.
- Texto principal y cifras: `text`. Descripciones y encabezados de columna: `text-muted`. Unidades, leyendas, marcas de tiempo y placeholders: `text-subtle`, nunca por debajo de 12px. Los tres cumplen 4.5:1 o más sobre las cuatro superficies.

**Acción y selección**

- Botón principal: `primary` con `on-primary`; hover y presionado `primary-strong`. Un solo botón principal por vista.
- Enlaces: `link` (alias de `brand-text`), subrayado en hover.
- Fila, celda o tarjeta seleccionada: fondo `selection` y texto `text`. Elemento activo o en curso (pestaña activa, punto «En análisis»): `active`.
- Foco de teclado: anillo sólido de 2px en `focus` con 2px de separación. Siempre visible, también sobre botones rellenos.
- `info` comparte el cobalto de `brand` a propósito: un aviso informativo se lee como interfaz, no como estado.

**Veredictos de resultado**

| Estado | Relleno | Insignia | Texto suelto |
| --- | --- | --- | --- |
| Conforme | `success` + `on-success` | `success-soft` + `on-success-soft` | `success-text` |
| Por revisar / cerca del límite | `warning` + `on-warning` | `warning-soft` + `on-warning-soft` | `warning-text` |
| No conforme / error | `danger` + `on-danger` | `danger-soft` + `on-danger-soft` | `danger-text` |
| Sin estado | `neutral` + `on-neutral` | `neutral-soft` + `on-neutral-soft` | `neutral-text` |

- Un veredicto lleva siempre palabra o icono además del color. `success` y `danger` tienen luminosidad parecida y no se distinguen solo por tono con daltonismo rojo-verde.
- En una tabla de resultados colorea la insignia o el valor fuera de especificación, nunca la fila entera.

**Categorías**

- `cat-1` a `cat-8` identifican tipos de muestra, matrices (agua, suelo, alimento…) o áreas del laboratorio en chips e iconos: relleno `cat-N` + `on-cat-N`, chip `cat-N-soft` + `on-cat-N-soft`. Asigna cada categoría una vez y no la reutilices para otra cosa.
- No uses `cat-*` en gráficas; para eso está `viz-*`.

## Tipografía

- **IBM Plex Sans** (`--font-sans`) para toda la interfaz; **IBM Plex Mono** (`--font-mono`) para datos. Ambas desde Google Fonts, pesos 400, 500 y 600.
- Jerarquía de una vista: `title-1` en la cabecera, `title-3` en tarjetas, `body` en el contenido, `label` en campos, botones y encabezados de columna, `caption` en ayudas y pie de tabla.
- `display` solo en tableros e informes, uno por vista. `overline` solo para rótulos cortos sobre KPIs o grupos, en mayúsculas.
- Resultados, folios (`CT-2026-004187`), lotes y límites: `data`, alineados a la derecha. Incertidumbre y límite de detección bajo el resultado: `data-sm` en `text-subtle`.
- KPIs: la cifra en `kpi` y `text`; la unidad y el periodo en `caption` y `text-subtle`, al lado o debajo.
- Si una cifra va en Plex Sans (dentro de una frase, por ejemplo), aplica `font-variant-numeric: tabular-nums`.

## Espacio, forma y elevación

- Escala de 4px: `space-1` … `space-16`. Margen lateral de vista `space-6`; entre secciones `space-8`; padding de tarjeta `space-5`; padding de celda `space-2` vertical y `space-3` horizontal.
- Radios: campos y botones `radius-sm`; tarjetas y menús `radius-md` (= `radius-shape`); diálogos `radius-lg`.
- Bordes: `border` en reposo, `border-strong` en hover y bajo el encabezado de tabla, `border-control` en todo campo editable (3:1 o más).
- Sombras: ninguna en tarjetas por defecto; `shadow-sm` solo si el borde no basta; `shadow-md` para lo que flota.

## Vistas de gestión

- Orden fijo: **cabecera** (`title-1`, descripción en `text-muted`, acción principal a la derecha) → **barra de herramientas** (buscador, filtros, acciones masivas) → **área de datos** (tabla o tarjetas en `surface`) → **pie** (paginación y conteo en `caption`).
- Tablas: encabezado en `surface-sunken` con `label` en `text-muted` y `border-strong` debajo; filas con divisor `border`; hover de fila `neutral-soft`; fila seleccionada `selection`. Números a la derecha en `data`.
- Formularios: campo en `surface` con `border-control` y `radius-sm`; etiqueta `label` arriba; ayuda en `caption`; error con contorno `danger` y mensaje en `danger-text` con icono; solo lectura en `neutral-soft`; deshabilitado con texto `text-subtle` y sin hover.
- Estados obligatorios en toda vista: carga (esqueleto en `surface-sunken`), vacío (`body-lg` en `text-muted`, más una acción), error (aviso `danger-soft`), deshabilitado, hover y foco.

## Gráficas

- Series: `viz-1` … `viz-6` en ese orden. Alternan claro y oscuro para distinguirse también por luminosidad. Más de 6 series: agrupa el resto en «Otros» con `viz-context`.
- Para destacar una serie: esa en `viz-focus` y con etiqueta directa; todas las demás en `viz-context`, sin leyenda de color.
- Cuadrícula `viz-grid`; ejes y unidades `viz-axis` en `caption`. Límite de especificación (LMP, límite de detección): línea discontinua `viz-limit` con su etiqueta de texto.
- Cada gráfica lleva una línea de lectura bajo el título («Cada punto es una muestra; la línea roja es el límite máximo permisible»). Sin pasteles ni donas para porcentajes pequeños: usa barras.

## Pantalla de acceso

- Estructura: formulario a la izquierda (7fr) y panel de arte a la derecha (5fr). Debajo de 1024px el panel pasa a banda superior; debajo de 600px desaparece.
- Formulario: bloque de 360px alineado a la izquierda. `overline` «Laboratorio de análisis» sobre el título `display` «Entra a Conectti». Campos y botón de 44px de alto con 20px entre campos. «Entrar» es la única acción primaria, a todo el ancho y con flecha. La ayuda va bajo una línea `border`, en `text-muted`.
- Error de credenciales: aviso `danger-soft` + `on-danger-soft` con icono, sobre los campos. Se conserva el usuario y el foco va a Contraseña.

**Arte de acceso: degradado y vidrio esmerilado**

- Es el único lugar de Conectti con degradado y vidrio. Nunca en vistas de datos, tarjetas ni diálogos.
- Fondo del panel: un degradado lineal de `brand-soft` a `surface` con dos resplandores radiales encima, `brand` desde la esquina inferior izquierda y `accent` desde la superior derecha. Dos discos sólidos (`brand` y `accent`) asoman detrás del vidrio para que el esmerilado se note.
- Vidrio: `glass` con `glass-border`, `shadow-glass`, `radius-lg` y `backdrop-filter: blur(var(--blur-glass)) saturate(140%)`.
- Dentro del vidrio va un dato del dominio, como un cromatograma con su pico anotado: trazo `brand`, referencia en `border-strong`, pico en `accent`. El texto va en `text` y `text-muted`; nunca `text-subtle`, porque sobre el vidrio baja a 3.6:1.
- Sin morados ni violetas: el degradado es solo cobalto y verde azulado.

## Iconografía y logotipo

- Iconos de trazo uniforme a 16px (en línea con `body`) y 20px (botones de icono), en el color del texto al que acompañan. Ningún emoji.
- Logotipo: la ligadura **tt**. El nombre va en minúsculas, «conectti», en IBM Plex Sans 600 convertida a trazados; las dos t comparten una sola barra en `accent` que sobresale a la derecha como marca de calibración, y el punto de la i repite `accent`. Las letras van en `brand`. El símbolo es la tt sola. Archivos y reglas de uso en la sección «Marca»; assets en el grupo «Marca».
- En texto corrido el nombre se escribe «Conectti», con mayúscula; la minúscula es solo del logotipo.

## Correspondencia con Grana

Los nombres de color son los mismos roles del tema Matraz de Grana: `brand` aquí equivale a `--g-color-brand` allá, y así con todos. Espaciado y radios conservan los valores de Matraz (`space-4` = `--g-space-4`, `radius-md` = `--g-radius-md`). Agregados de Conectti: `surface-raised`, `shadow-*`, la familia `viz-*`, el vidrio (`glass`, `glass-border`, `blur-glass`) y la tipografía.
