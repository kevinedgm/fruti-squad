# Laranda

Plataforma para profesionales independientes de belleza y cuidado personal en México: perfil, agenda, folio y reseñas. Habla como colega, no como marca: «tu oficio», «tu agenda», «tu folio». Español e inglés sin juegos de palabras que se pierdan. Móvil primero: los profesionales la usan desde el teléfono, entre cita y cita.

![Lockup de Laranda](/_blob/9cabaca099c454bb0284a894cb38bee7)

## Principios

- **Artesanal sin ser rústico.** La flor es un dibujo a mano con una mancha de color desfasada; todo lo demás es limpio y preciso. El carácter vive en la marca y en la tipografía de títulos, no en texturas ni ornamentos.
- **Neutro en género.** Violeta intenso, naranja, fondo hueso frío. Nada de rosas, nada de degradados violeta-rosa, nada de pétalos genéricos.
- **El oro se gana.** `reserve` aparece una sola vez por pantalla: el botón Reservar y la confirmación de cita. Si aparece en otro lugar, está mal.
- **Nada depende solo del color.** Cada categoría y cada estado lleva color, icono y texto.
- **Florece en público.** La flor es un símbolo de estado: aparece y se abre cuando el negocio florece (perfil publicado, folio emitido, primera reseña).

## Contenido y tono

Frases cortas, verbos concretos: florece, ordena, cobra, vuelve. Nunca «potencia», «sinergia», «revoluciona», «emprendedor exitoso». Los botones dicen lo que hacen: Reservar, Publicar perfil, Emitir folio. Los errores dicen qué pasó y cómo seguir. Tagline: «Tu oficio, en flor.» / «Your craft, in bloom.»

## Color

Un violeta para la acción y la marca, un naranja de acento, un oro reservado, dos estados y neutros. Validado con simulación de daltonismo: todas las parejas se distinguen con visión normal, y bajo protanopia, deuteranopia y tritanopia con el apoyo de icono y texto en los estados.

- `brand` #5B3BB5 es la acción primaria, el foco y la mancha de la flor; `brand-strong` para hover y presionado; `brand-soft` y `brand-tint` para fondos de foco y chips. Sobre `brand` siempre `on-brand`.
- `accent` #E0611A es el acento de marca: el lóbulo que se abre, enlaces y destacados. Como texto solo a 18 px o más (3.2:1 sobre `bg`); texto chico va en `text` sobre `accent-soft`.
- `reserve` #D9A400 solo en Reservar y en la confirmación de cita, con texto en `on-reserve` (8.2:1). Nunca blanco sobre oro.
- `success` y `danger` siempre con icono y etiqueta; sus avisos usan `*-soft` con `on-*-soft`.
- Oscuro: `brand` sube a lila #C4B5F0 y `accent` a #F2A074; la línea de la flor pasa de tinta a hueso (`ink-draw`). Los estados en oscuro son provisionales: cumplen contraste, pero no se han probado en campo.

![Simulación de daltonismo](/_blob/3cbe572c65ceb949265ee4091efea6f6)

## Tipografía

- **Bricolage Grotesque** 600–700 (`display`) para el wordmark, `display`, `title-1` y `title-2`. Tiene algo de dibujo en las curvas que conversa con la flor. Una `display` por pantalla.
- **Onest** 400, 500 y 700 (`sans`) para todo el cuerpo y los controles. 16 px mínimo en móvil.
- **IBM Plex Mono** 500 (`mono`) para folios: número, hora y precio.
- Las tres se cargan de Google Fonts; el wordmark va en trazados y no depende de la fuente instalada.

## Espacio, forma y elevación

Escala de 4 px. Gutter lateral de 16 px en móvil (`space-4`). Controles de 44 px de alto (`control-h`); Reservar en cabecera, 52 px. Radios: 8 chips chicos, 12 campos y tarjetas, 14 botones y hojas, 20 hojas inferiores, píldora para chips de categoría y avatar. Tarjetas delimitadas por `border`; `shadow-sm` solo cuando el borde no basta; `shadow-sheet` para la hoja inferior.

## Movimiento

`bloom` (500 ms, `ease-out`): la flor se abre al publicar perfil, confirmar cita o recibir la primera reseña; los lóbulos crecen desde la garganta y el lóbulo naranja se separa al final. Con `prefers-reduced-motion`, aparece abierta. Todo lo demás es `quick` (150 ms).

![Bloom](/_blob/6d0098676610c87b34af960f1c5c0f20)

## Iconografía y marca

- Iconos de trazo de 1.75 px a 20 px (`icon`), en el color del texto que acompañan. Sin emoji.
- Símbolo: la flor dibujada, 40 px o más (`mark-min`); de 16 a 32 px, la silueta. Área de respeto: la altura del punto central. Reglas completas, archivos y app icon en la sección «Marca» y en el grupo de assets «Marca».

## Accesibilidad

WCAG 2.2 AA: texto 4.5:1 sobre su fondo en ambos temas, componentes y bordes 3:1, objetivos táctiles de 44 px, foco visible de 2 px en `focus`. Las etiquetas de categoría y estado nunca son solo color.
