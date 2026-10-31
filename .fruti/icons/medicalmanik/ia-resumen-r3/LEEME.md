# Ecosistema Manik · IA · diálogo de antecedentes r3 (velo sutil)

Pedido del usuario (2026-10-31): el velo de r2 «se ve muy tosco y muy exagerado»; quiere algo discreto, elegante, sutil: un overlay transparente con estrellitas apareciendo alrededor.

Publicado: https://claude.ai/artifact/UHr2QRaTuubusR4vAwfnsC · base: `../ia-resumen-r2/` (se conserva la piel de IA).

## Velo r3 [propuesta]
- Cubre solo el **cuerpo**: la cabecera queda visible y su destello **orbita** (la IA analiza); el pie queda libre («Empezar consulta» siempre disponible).
- Velo **blanco translúcido** (55 %) con desenfoque de 2 px; el contenido de abajo apenas borroso (3 px) y atenuado; se aclara en 0.6 s al terminar.
- **15 estrellitas** (destello de 4 puntas, 6–12 px, cian #3DB8C9 y azul Manik) repartidas alrededor, que aparecen, giran un poco y se desvanecen a ritmos distintos (2.2–3.6 s). Decorativas.
- Al centro, sin caja: destello pequeño en órbita, «Analizando antecedentes» y el paso actual en gris.
- Micropausa ≈1.4 s; se queda si el resumen aún no llega. Movimiento reducido: sin estrellitas ni transiciones.
- Se quitaron de r2: malla de color, grano, barrido de luz, barra de avance, placa oscura y revelado con máscara. La aurora de la cabecera se mueve más lento (8 s) y solo mientras piensa.

## Corrección (aplica también a r1 y r2, republicados)
En pantallas bajas la cabecera y el pie del diálogo se encogían y recortaban el subtítulo y el chip «Sugerido por IA». Ahora cabecera y pie no se encogen; solo el cuerpo se desplaza.

## Verificación
Playwright 1300 y 390 px: sin desbordes ni errores JS; `aria-busy`, región viva, foco en «Empezar consulta»; en «Aún analizando» se puede empezar.

[pendiente: aprobación del velo sutil]
