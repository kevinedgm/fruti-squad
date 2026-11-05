# NisaLab

NisaLab es el sistema de laboratorio de Nisa Nabani: recepción de muestras, lotes, ensayos, captura y revisión de resultados, y certificados. Lo usan analistas, supervisores de calidad y personal de recepción, casi siempre en escritorio, durante toda la jornada. La interfaz es densa y funcional: se escanea y se compara, no se contempla.

![NisaLab de Nisa Nabani](/_blob/c98fb7a71514f449f585b481e0c7b6a8)

## Principios

- **El dato manda.** Cada pantalla tiene un valor o un estado protagonista; todo lo demás se subordina. La marca vive en el encabezado, la carga y los documentos, no en las tablas.
- **Dos voces tipográficas.** Poppins habla (títulos, etiquetas, texto), como en el manual de Nisa Nabani; Google Sans Code mide (resultados, límites, unidades, folios). Si un número se mide, se compara o se copia, va en Google Sans Code. Ver la sección «Valores y resultados».
- **Una sola cosa pera.** El pera marca lo que está en curso: la muestra activa, el registro que se edita, la célula que creció del símbolo. Si hay dos cosas en pera, una sobra.
- **Área no es estado.** Los colores de área identifican cada división dentro de NisaLab; los estados tienen colores propios.
- **Nada depende solo del color.** Conforme, fuera de especificación, alerta y pendiente llevan icono y texto, además de color.
- **Tema claro, nunca blanco sobre blanco.** El lienzo es gris de laboratorio (`bg` #F2F4F8) y las superficies blancas se separan de él con borde y una sombra mínima. El sistema no tiene tema oscuro.
- **El color sigue al significado.** Un estado tiene el mismo color, icono y texto en todos los módulos. Ver la sección «Módulos».

## Contenido y tono

Preciso, breve, sin adornos. Los botones dicen la acción y el objeto: Registrar muestra, Capturar resultado, Liberar lote, Emitir certificado. Los errores dicen qué pasó y cómo corregirlo: «El resultado está fuera del intervalo del método (0.005–10 mg/L). Revisa la dilución.» Términos del laboratorio sin traducir: LD, LC, lote, alícuota, especificación, método.

## Color

Los primarios de Nisa Nabani ordenan la interfaz; los secundarios del laboratorio dan los estados.

- **Básicos (6):** `bg` (#F2F4F8) lienzo, encabezado de tabla, hover, solo lectura y deshabilitado; `surface` (blanco) tarjetas, tablas, campos y texto sobre azul; `text` (#141B33); `text-muted` (#535B70) metadatos, placeholders y «Pendiente»; `border` (#DFE3EC) separa; `border-control` (#858DA3) contorno de campos, 3.3:1 sobre `surface` y 3.0:1 sobre `bg`.
- **Marca (4):** `primary` (azul real #052A76) acción, enlace, foco, encabezado y texto sobre pera; `primary-hover` (#021C52); `primary-soft` (#E8EDF7) selección, registro en curso, «En proceso» y «Generando informe»; `pera` (#C2D225) una sola cosa por pantalla: la célula que creció, lo que está en curso (filete o punto) y «Urgente». Nunca texto sobre blanco (1.7:1).
- **Estados (7):** `conforme` (#2E7D32), `conforme-soft` y `on-conforme-soft` (el verde sobre su fondo mide 4.4:1, por eso lleva texto propio); `alerta` (#8A6100) y `alerta-soft`; `fuera` (#B42318) y `fuera-soft`. Alerta y fuera se leen sobre su fondo (4.9 y 5.5:1). Proceso y pago usan estos mismos colores: No ingresada y Pago parcial en alerta, Terminada y Pagada en conforme, Cancelada y No pagada en fuera, Cortesía en primary. «Pendiente» va en gris (`text-muted` sobre `bg`), con reloj y texto: no es urgente.
- **Áreas (8, `area-*`):** identidad de cada división (OKLCH: luz 0.60 para las ocho e intensidad máxima por tono, tope 0.17): Aguas #0C8CB7, Agrícolas #AA7408, Ambiental #0E9A47, Alimentos #CE5708, Bebidas #9163D4, Bebidas de agave #0F9487, Farmacia #C64D8E, Consultoría #4E79E3. Solo en la marca del área, su encabezado y los filtros; nunca estado, nunca en tablas.
- **Regla:** 25 colores en total. Un módulo no crea colores propios; si algo parece necesitar uno, primero se busca cuál de estos ya nombra lo mismo.
- **Retirados el 2026-11-05** (se unieron a uno existente): `surface-sunken`, `surface-hover`, `pendiente-soft` → `bg`; `text-subtle`, `pendiente`, `on-pendiente-soft` → `text-muted`; `border-strong` → `border`; `on-primary` → `surface`; `on-pera`, `focus`, `pago-cortesia` → `primary`; `pera-soft` → `primary-soft`; `on-fuera-soft`, `pago-no-pagada` → `fuera`; `on-alerta-soft`, `alerta-fill`, `pago-parcial` → `alerta`; `muestra-*` y `on-muestra-*` → el estado de su familia; `pago-pagada` → `conforme`.

## Tipografía

- **Poppins** (`display`, `sans`). La tipografía del manual de Nisa Nabani para títulos, subtítulos y textos. 700 solo en `display`; 600 en títulos y botones; 400 en texto. 14 px de cuerpo: su x-height alta lee como 15 px de otras familias.
- **Google Sans Code** (`datos`). Para valores y resultados de análisis. Cifras de ancho fijo, para que las columnas se alineen solas; cero con barra de fábrica para no confundir 0 con O; tiene µ, ±, ×, ≤, ≥ y °. Es la que ya usa bitácoras en producción.
- **Google Sans Code** se usa aunque el manual de Nisa Nabani no la incluye: el manual no cubre datos tabulares y Poppins no alinea cifras en columna.
- Se cargan de Google Fonts: `Poppins:wght@400;500;600;700` e `Google Sans Code:wght@400;500;600`.

## Espacio, forma y elevación

Escala de 4 px. Filas de tabla de 40 px (`row-h`), controles de 40 px en escritorio y 44 px en táctil. Radios contenidos: 6, 8 y 12 px; la píldora solo para puntos de estado, etiquetas de área y avatares. Elevación en una escala corta: `shadow-1` separa tarjetas y tablas del lienzo, `shadow-2` para lo que se levanta al pasar, `shadow-overlay` para lo que flota (menús, paneles, avisos), `shadow-inset` hunde los campos y `shadow-primary` / `shadow-primary-hover` dan cuerpo al botón primario. Las sombras son azuladas y cortas: insinúan, no decoran.

## Diálogos

Una sola estructura para trabajar un registro (720 px) o decidir (440 px): encabezado, cuerpo y pie sobre `surface`. El encabezado da la identidad: avatar de 48 con el fondo suave y el ícono del tono, contexto en `overline` azul, título `title-1` y subtítulo `body` gris. El tono (neutro, aviso, destructivo, éxito) solo cambia el avatar y, si es destructivo, el botón principal. Ver el componente «Dialogo».

## Movimiento

La carga es el símbolo: las células de Colonia aparecen una tras otra, 200 ms por paso (`paso-carga`), y la pera crece al final. Con `prefers-reduced-motion` el símbolo queda quieto. Todo lo demás es `quick` (150 ms).

## Iconografía y marca

- Iconos de trazo de 1.75 px a 18 px (`icon`), en el color del texto que acompañan.
- La célula es el átomo gráfico: los estados en tablas se marcan con un punto de 10 px (`pozo`) del color del estado, junto al texto.
- Símbolo, logotipos e íconos en la sección «Marca» y en los grupos de assets «Marca» y «Áreas».

## Pendiente

- La interfaz actual del producto usa Verdant WebKit con acento esmeralda. Este sistema propone el azul y pera de Nisa Nabani; falta decidir si sustituye el acento de Verdant o si convive con él.
