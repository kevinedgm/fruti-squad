# Manik IA · manual de marca

Pedido del usuario (2026-10-31): un manual de marca solo para la capa de IA, llamada **Manik IA**, aislado del manual del Ecosistema Manik, porque la IA solo vive en Expediente Manik. Incluye botones, diálogo, overlay e interacción.

Publicado: https://claude.ai/artifact/LYq9oKz49WMM2ihwALM1WL · fuente: `manual.html` (sin skeleton; la publicación lo agrega).

## Contenido
01 Principios · 02 Nombre y voz · 03 Símbolo · 04 Color · 05 Tipografía · 06 Movimiento · 07 Botón · 08 Menú de acciones · 09 Resultado sugerido · 10 Diálogo · 11 Velo de pensamiento · 12 Accesibilidad · 13 Alcance. Con ejemplos vivos: movimiento («Ver de nuevo»), botones, resultado aceptable y diálogo con velo («Actualizar resumen»).

## Fuentes (aprobadas por el usuario)
Función «IA» (`../ia-ronda-1/`), dirección C tinta noche (`../ia-ronda-2/`), regla respira/orbita/traza (`../ia-ronda-3/`), diálogo de antecedentes (`../ia-resumen-r1/`), velo sutil con estrellitas (`../ia-resumen-r3/`), piel ligera (`../ia-resumen-r4/`, última ronda; tomada como vigente al pedir el manual).

## Decisiones nuevas en el manual [propuesta]
- **Nombre:** «Manik IA» nombra el sistema (documentos, ventas, capacitación); en la interfaz el médico solo ve «IA» (mantiene la decisión de función, no personaje ni producto).
- **Voz impersonal**, sin primera persona: «Se encontraron 3 valores» (antes «Encontré»).
- **Colores propios:** `ia` #0F1C3F, `ia-hover` #1B2B57, `ia-destello` #5FD3E2, `ia-estrella` #3DB8C9; `ia-suave` = manik-soft. Contrastes medidos: blanco/ia 16.69, destello/ia 9.46, noche/ia-suave 14.22; cian sobre blanco 1.76 (prohibido).
- **Aislado pero heredado:** documento propio; tipografía, azul de acción, estados, espacio y radios vienen de Expediente Manik.
- Tema claro únicamente, como el ecosistema.

## Verificación
Playwright 1300 y 390 px con fuentes locales: sin desbordes ni errores JS; velo y aceptar resultado funcionan; casillas de 20 px.

## Pendiente
CIE-10 o CIE-11; materializar los tokens `ia-*` en Expediente; comportamiento clínico de cada función.
