# Ecosistema Manik · identidad de la IA · ronda 1

Pedido del usuario (2026-10-31): identidad para las funciones de IA del ecosistema (resumen del expediente, signos vitales desde el dictado, códigos CIE, contraindicaciones, sugerencias de cuidado, redactar el padecimiento actual desde la transcripción): botón para invocarla, menú de opciones, diálogo e interacción.

Publicado: https://claude.ai/artifact/EL5BptPi3hYowT6HcrXty1

## Decisiones
- **Usuario:** la IA es una **función «IA»**, no un personaje ni un 7.º sello. Los botones dicen verbo + «con IA».
- [propuesta] Tres reglas comunes: 1) la IA ayuda, no decide: nunca es la acción principal (sigue «Guardar consulta», azul Manik); 2) todo lo que produce es borrador marcado «Sugerido por IA» y no entra al expediente sin confirmación del médico, completa o dato por dato; 3) cada dato muestra la frase del dictado o el registro de origen.
- [supuesto] «IEDs» = códigos **CIE-10** (clasificación de morbilidad usada en México). Confirmar si el sistema usa CIE-10 o CIE-11.

## Direcciones
| | Marca | Botón | Generando | Resultado |
|---|---|---|---|---|
| A · Pulso que destella | línea de pulso de Manik + destello cian | blanco, borde degradado cian → azul Manik, radio 14 | el borde gira | filo izquierdo degradado + chip |
| B · Luz de marca | destello dentro de un halo | píldora con las luces cian y cálida, texto tinta | la luz se desplaza | fondo de luz suave + chip |
| C · Tinta noche | destello doble (convención) | píldora azul noche, destello cian | barra cian que corre | borde punteado (borrador) → sólido verde al aceptar |

Valores nuevos solo de la IA (degradados, `#5FD3E2` cian claro sobre noche, `#9FCFD7` borde de B) quedan como propuesta hasta elegir; lo demás son tokens del sistema.

## Interacción probada
Menú con `aria-haspopup`/`role="menu"`, flechas, Inicio/Fin, Esc devuelve el foco; acción deshabilitada con su requisito («Necesita una receta»); generando con `aria-busy` y región viva; el resultado recibe el foco; casillas por dato; aceptar o descartar. `prefers-reduced-motion` quita las animaciones.

## Verificación
Playwright 1300 y 390 px con Urbanist y Atkinson locales: sin desbordes, sin errores JS, objetivos ≥ 24 px; flujo con teclado en B. Corregido en prueba: `[hidden]` anulado por `display` (mensaje de guardado visible antes de tiempo); barra de consulta que se partía; botón de aceptar pasó a secundario (una sola acción primaria por vista).

## Pendiente
- **Usuario (2026-10-31): dirección C** (prefiere C sobre A); de A toma el borde segmentado. Animaciones en `../ia-ronda-2/`.
- Diálogo de cada función (revisar, editar, aceptar), empezando por «Redactar padecimiento actual».
- Comportamiento clínico de cada función (fuentes, límites, responsabilidad): fuera de la identidad.
