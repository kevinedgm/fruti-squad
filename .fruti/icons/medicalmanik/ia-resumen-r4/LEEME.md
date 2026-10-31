# Ecosistema Manik · IA · diálogo de antecedentes r4 (piel ligera)

Pedido del usuario (2026-10-31): la cabecera del diálogo (azul noche con aurora) se siente agresiva y pesada; hacer el diálogo más sutil y elegante.

Publicado: https://claude.ai/artifact/XAJfmi6rhXxwMVozEBQbzs · base: `../ia-resumen-r3/` (velo sutil con estrellitas, sin cambios).

## Piel ligera [propuesta]
- **Cabecera blanca** con un lavado de luz cian casi imperceptible arriba y un halo suave en la esquina; título en tinta, subtítulo gris.
- **Filo de 3 px** arriba del diálogo (cian → azul Manik → se desvanece): la firma de IA, discreta.
- **El destello** en placa azul noche de 40 px es la única marca fuerte (antes 48 px dentro de una cabecera oscura).
- **Chip «Sugerido por IA»** en azul suave con el destello en noche (antes contorno cian sobre oscuro).
- Borde del diálogo: el divisor normal del sistema (antes anillo degradado de 2 px). Idea principal con filo cian de 2 px, sin fondo.
- Se quitaron la cabecera noche, la aurora y el anillo degradado.

## Qué la sigue distinguiendo de un diálogo normal
Filo de color arriba · destello en la cabecera · chip «Sugerido por IA» · velo con estrellitas al abrir · botón de IA «Actualizar resumen».

## Verificación
Playwright 1300 y 390 px: sin desbordes ni errores JS; mismos comportamientos de r3 (aria-busy, región viva, foco, «Empezar consulta» siempre disponible).

[pendiente: aprobación]
