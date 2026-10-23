# SUUMA

Plataforma móvil que conecta a profesionales independientes de belleza y cuidado personal con quienes los buscan. Habla claro, humano y directo: «tu talento», «tu próximo cliente», «cada talento tiene su lugar». Español e inglés sin juegos de palabras. Móvil primero.

![Lockup de SUUMA](/_blob/30d7f9a23e529153954322c52142ecc9)

## Principios

- **Una u dentro de la otra.** El nombre se escribe «suma» y la segunda u vive dentro de la primera, en cadmio. Cada quien conserva su forma; juntas hacen el nombre. Nunca se escriben las dos u seguidas.
- **Editorial y vivo.** Blanco y tinta como base; el cadmio es la única nota de color. La interfaz es sobria para que el trabajo de cada profesional, sus fotos y su nombre, sea lo que se ve.
- **El cadmio marca, no ordena.** Nunca es texto ni borde de control (1.4:1 sobre blanco). Va en la u interior, en chips activos, en destacados y en fondos con texto en tinta. La acción primaria es tinta.
- **Nada depende solo del color.** Estados y categorías llevan icono y texto.
- **Sin clichés de belleza.** Ni tijeras, ni rostros, ni siluetas, ni flores literales. Sin caritas: la u no lleva ojos.

## Contenido y tono

Claro, humano, directo y optimista sin promesas exageradas. Los botones dicen lo que hacen: Contactar, Publicar perfil, Reservar. Los errores dicen qué pasó y cómo seguir. Nunca «potencia», «sinergia», «revoluciona».

## Color

Dos neutros y una nota. Validado por contraste: todo texto 4.5:1 sobre su fondo en ambos temas.

- `text` sobre `bg`: 18.7:1. `text-muted`: 6.5:1. `text-subtle` sobre `surface-sunken`: 4.9:1.
- `primary` es tinta con `on-primary` blanco: la acción principal de cada pantalla.
- `cadmio` #FFD400 solo como relleno: la u interior, chips seleccionados, destacados y fondos con texto en `on-cadmio` (13.1:1). `cadmio-soft` para filas y avisos marcados.
- `focus` es tinta en claro y cadmio en oscuro, 2 px con separación de 2 px.
- `success` y `danger` siempre con icono y etiqueta; avisos en `*-soft` con `on-*-soft`. Son provisionales hasta probarlos en producto.
- Oscuro: fondo tinta, superficies #1C1C1C, `primary` pasa a hueso; el cadmio no cambia.

## Tipografía

- **Bricolage Grotesque** 600 (`display`) para el wordmark, `display`, `title-1` y `title-2`. 700 solo en display grande. Una `display` por pantalla.
- **Onest** 400, 500 y 700 (`sans`) para todo el cuerpo y los controles. 16 px mínimo en móvil.
- **IBM Plex Mono** 500 (`mono`) para precios, horas y folios. Provisional.
- Las tres se cargan de Google Fonts; el wordmark va en trazados.

## Espacio, forma y elevación

Escala de 4 px. Gutter de 16 px en móvil (`space-4`). Controles de 44 px (`control-h`); Contactar en cabecera, 52 px. Radios 8, 12 y 16; píldora solo en avatar y puntos. Las tarjetas se separan con `border`, sin sombra; solo la hoja inferior lleva `shadow-sheet`. Etiquetas sobre datos en `overline`.

## Movimiento

Todo es `quick` (150 ms, `ease-out`). Sin animación de marca por ahora; con `prefers-reduced-motion`, sin transiciones.

## Iconografía y marca

- Iconos de trazo de 1.75 px a 20 px (`icon`), en el color del texto que acompañan. Sin emoji.
- Símbolo: la doble u anidada desde 16 px (`mark-min`). Área de respeto: la altura de la u interior. Piezas y reglas en la sección «Marca» y en el grupo de assets «Marca».

## Accesibilidad

WCAG 2.2 AA: texto 4.5:1 en ambos temas, componentes y bordes 3:1, objetivos táctiles de 44 px, foco visible de 2 px. El cadmio nunca es el único portador de información.
