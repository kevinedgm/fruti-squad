# Nabi

Nabi es el sistema de laboratorio de Nisa Nabani: recepción de muestras, lotes, ensayos, captura y revisión de resultados, y certificados. Lo usan analistas, supervisores de calidad y personal de recepción, casi siempre en escritorio, durante toda la jornada. La interfaz es densa y funcional: se escanea y se compara, no se contempla.

![Lockup de Nabi](/_blob/3534ef111e16fe05c60c372a3d61e030)

## Principios

- **El dato manda.** Cada pantalla tiene un valor o un estado protagonista; todo lo demás se subordina. La marca vive en el encabezado, la carga y los documentos, no en las tablas.
- **Dos voces tipográficas.** Poppins habla (títulos, etiquetas, texto), como en el manual de Nisa Nabani; IBM Plex Mono mide (resultados, límites, unidades, folios). Si un número se mide, se compara o se copia, va en Plex Mono. Ver la sección «Valores y resultados».
- **Una sola muestra pera.** El pera marca lo que está en curso: la muestra activa, la fila seleccionada, el pocillo del símbolo. Si hay dos cosas en pera, una sobra.
- **División no es estado.** Los colores secundarios del manual identifican divisiones; los estados tienen colores propios que no se confunden con ninguna.
- **Nada depende solo del color.** Conforme, fuera de especificación, alerta y pendiente llevan icono y texto, además de color.
- **Tema claro, nunca blanco sobre blanco.** El lienzo es gris de laboratorio (`bg` #F2F4F8) y las superficies blancas se separan de él con borde y una sombra mínima. El sistema no tiene tema oscuro.
- **El color sigue al significado.** Un estado tiene el mismo color, icono y texto en todos los módulos. Ver la sección «Módulos».

## Contenido y tono

Preciso, breve, sin adornos. Los botones dicen la acción y el objeto: Registrar muestra, Capturar resultado, Liberar lote, Emitir certificado. Los errores dicen qué pasó y cómo corregirlo: «El resultado está fuera del intervalo del método (0.005–10 mg/L). Revisa la dilución.» Términos del laboratorio sin traducir: LD, LC, lote, alícuota, especificación, método.

## Color

Los primarios de Nisa Nabani ordenan la interfaz; los secundarios del laboratorio dan los estados.

- Lienzo y superficies: `bg` (#F2F4F8) es el fondo de la app; `surface` (blanco) para tarjetas, tablas y paneles; `surface-sunken` (#EEF1F6) para cabeceras de tabla y zonas hundidas; `surface-hover` (#F5F7FB) para filas al pasar. Bordes en dos pesos: `border` (#DFE3EC) separa, `border-strong` (#CDD3DF) delimita.
- `primary` (azul real #052A76) es la acción primaria, los enlaces y el encabezado. `primary-soft` para la fila seleccionada.
- `pera` (#C2D225) es la muestra: el pocillo del símbolo y la muestra activa. Nunca texto sobre blanco (1.7:1). `pera-soft` para el registro en curso.
- Estados: `conforme` (#2E7D32), `fuera` (#B42318), `alerta` (texto #8A6100, relleno #E9B10A) y `pendiente` (pizarra #475467). Cada uno con su fondo `*-soft` y su texto `on-*-soft`. Ninguno reutiliza un color de división.
- Divisiones (`div-*`): los ocho secundarios del manual, uno por división (Aguas #00B4D8, Agrícolas #553739, Ambiental #38B000, Alimentos #F48C06, Bebidas #3D67AE, Bebidas de agave #006D53, Farmacia #3D0066, Consultoría #052A76). Solo en el azulejo del icono y en marcas de documento; el nombre siempre en `text`, porque cuatro de ellos no llegan a 4.5:1 como texto. Ver el componente «Divisiones».
- Contrastes verificados: todo texto ≥ 4.5:1 sobre su fondo (`text-muted` 6.2:1 sobre `bg`, `text-subtle` 4.7:1 sobre `surface-sunken`); `border-control` 3.3:1 sobre `surface`. Por eso los campos viven sobre `surface`, no sobre `bg` (3.0:1).

## Tipografía

- **Poppins** (`display`, `sans`). La tipografía del manual de Nisa Nabani para títulos, subtítulos y textos. 700 solo en `display`; 600 en títulos y botones; 400 en texto. 14 px de cuerpo: su x-height alta lee como 15 px de otras familias.
- **IBM Plex Mono** (`datos`). Para valores y resultados de análisis. Cifras de ancho fijo, para que las columnas se alineen solas; cero con barra (`font-feature-settings: "zero"`) para no confundir 0 con O; tiene µ, ±, ×, ≤, ≥, ° y superíndices.
- **IBM Plex Mono** se conserva aunque el manual no la incluye: el manual no cubre datos tabulares y Poppins no alinea cifras en columna.
- Se cargan de Google Fonts: `Poppins:wght@400;500;600;700` e `IBM Plex Mono:wght@400;500;600`.

## Espacio, forma y elevación

Escala de 4 px. Filas de tabla de 40 px (`row-h`), controles de 40 px en escritorio y 44 px en táctil. Radios contenidos: 6, 8 y 12 px; la píldora solo para pocillos y puntos de estado. Elevación en una escala corta: `shadow-1` separa tarjetas y tablas del lienzo, `shadow-2` para lo que se levanta al pasar, `shadow-overlay` para lo que flota (menús, paneles, avisos), `shadow-inset` hunde los campos y `shadow-primary` / `shadow-primary-hover` dan cuerpo al botón primario. Las sombras son azuladas y cortas: insinúan, no decoran.

## Movimiento

La carga es el símbolo: la muestra pera recorre la N, 200 ms por paso (`paso-carga`). Con `prefers-reduced-motion` se detiene en el pocillo final. Todo lo demás es `quick` (150 ms).

![Carga](/_blob/6358d06d47e59e7d479475ad1ab7587b)

## Iconografía y marca

- Iconos de trazo de 1.75 px a 18 px (`icon`), en el color del texto que acompañan.
- El pocillo es el átomo gráfico: los estados en tablas se marcan con un pocillo de 10 px (`pozo`) del color del estado, junto al texto.
- Símbolo, wordmark y lockups en la sección «Marca» y en el grupo de assets «Marca».

## Pendiente

- La interfaz actual del producto usa Verdant WebKit con acento esmeralda. Este sistema propone el azul y pera de Nisa Nabani; falta decidir si sustituye el acento de Verdant o si convive con él.
- Los nombres de estado de muestra (Recibida, En análisis, En revisión, Liberada, Rechazada) son una propuesta: confirmar con el flujo real del laboratorio.
