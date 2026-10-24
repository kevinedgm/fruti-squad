# Nabi

Nabi es el sistema de laboratorio de Nisa Nabani: recepción de muestras, lotes, ensayos, captura y revisión de resultados, y certificados. Lo usan analistas, supervisores de calidad y personal de recepción, casi siempre en escritorio, durante toda la jornada. La interfaz es densa y funcional: se escanea y se compara, no se contempla.

![Lockup de Nabi](/_blob/3534ef111e16fe05c60c372a3d61e030)

## Principios

- **El dato manda.** Cada pantalla tiene un valor o un estado protagonista; todo lo demás se subordina. La marca vive en el encabezado, la carga y los documentos, no en las tablas.
- **Dos voces tipográficas.** Archivo habla (títulos, etiquetas, texto); IBM Plex Mono mide (resultados, límites, unidades, folios). Si un número se mide, se compara o se copia, va en Plex Mono. Ver la sección «Valores y resultados».
- **Una sola muestra pera.** El pera marca lo que está en curso: la muestra activa, la fila seleccionada, el pocillo del símbolo. Si hay dos cosas en pera, una sobra.
- **Nada depende solo del color.** Conforme, fuera de especificación, alerta y pendiente llevan icono y texto, además de color.
- **Tema claro.** El sistema no tiene tema oscuro.

## Contenido y tono

Preciso, breve, sin adornos. Los botones dicen la acción y el objeto: Registrar muestra, Capturar resultado, Liberar lote, Emitir certificado. Los errores dicen qué pasó y cómo corregirlo: «El resultado está fuera del intervalo del método (0.005–10 mg/L). Revisa la dilución.» Términos del laboratorio sin traducir: LD, LC, lote, alícuota, especificación, método.

## Color

Los primarios de Nisa Nabani ordenan la interfaz; los secundarios del laboratorio dan los estados.

- `primary` (azul real #052A76) es la acción primaria, los enlaces y el encabezado. `primary-soft` para la fila seleccionada.
- `pera` (#C2D225) es la muestra: el pocillo del símbolo y la muestra activa. Nunca texto sobre blanco (1.7:1). `pera-soft` para el registro en curso.
- Estados de resultado: `conforme` (verde del laboratorio #006D53), `fuera` (#B42318), `alerta` (texto #8A4B00; el naranja del laboratorio #F48C06 solo como relleno) y `pendiente` (azul secundario #3D67AE). Cada uno con su fondo `*-soft` y su texto `on-*-soft`.
- Contrastes verificados: todo texto ≥ 4.5:1 sobre su fondo; `border-control` 3.3:1.

## Tipografía

- **Archivo** (`display`, `sans`). Una sola familia variable en dos anchos: 125 % y 700 en `display` y `title-1`, la misma voz del wordmark; ancho normal en todo lo demás. 15 px de cuerpo para pantallas densas.
- **IBM Plex Mono** (`datos`). Para valores y resultados de análisis. Cifras de ancho fijo, para que las columnas se alineen solas; cero con barra (`font-feature-settings: "zero"`) para no confundir 0 con O; tiene µ, ±, ×, ≤, ≥, ° y superíndices.
- Las dos se cargan de Google Fonts: `Archivo:wdth,wght@62..125,100..900` y `IBM Plex Mono:wght@400;500;600`.

## Espacio, forma y elevación

Escala de 4 px. Filas de tabla de 40 px (`row-h`), controles de 40 px en escritorio y 44 px en táctil. Radios contenidos: 6, 8 y 12 px; la píldora solo para pocillos y puntos de estado. Sin sombras en tarjetas; solo lo que flota lleva `shadow-overlay`.

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
