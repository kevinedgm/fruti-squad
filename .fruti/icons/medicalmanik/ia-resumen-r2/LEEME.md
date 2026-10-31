# Ecosistema Manik · IA · diálogo de antecedentes r2 (velo y piel de IA)

Pedido del usuario (2026-10-31): al abrir o reinicializar un diálogo de IA, una micropausa con una animación fluida tipo overlay sobre todo el diálogo (como cuando una IA genera imágenes) que indique «generando / pensando»; y más personalidad en el diálogo para que no se confunda con los diálogos normales del sistema.

Publicado: https://claude.ai/artifact/KmTmBnH5pohsqmnqe6kkLB · base: `../ia-resumen-r1/`.

## Velo «la IA está pensando» [propuesta]
- Capas: fondo noche translúcido con desenfoque; malla de luz (cian, azul Manik, azul claro) que se mueve; grano de puntos; una línea de luz que barre de arriba abajo; al centro una placa oscura con el destello en **órbita** (la IA analiza), título, paso actual («Leyendo 3 consultas…», «Comparando signos y recetas…», «Preparando el resumen…») y barra de avance.
- **Micropausa de ≈1.2 s** al abrir aunque el resumen ya esté listo; 1.4 s al «Actualizar resumen». Si el resumen aún no llega, el velo se queda hasta que llegue.
- **Revelado:** el contenido pasa de borroso y apagado a nítido, de arriba abajo.
- **Nunca bloquea al médico:** el velo cubre cabecera y cuerpo, no el pie; «Empezar consulta» siempre se puede usar.
- Placa del centro sobre fondo oscuro para que el texto tenga contraste (corregido en prueba: sobre la malla clara no se leía).
- `prefers-reduced-motion`: sin malla, grano ni barrido; solo el texto, 0.5 s.

## Piel de diálogo de IA (vs diálogo normal)
| | Diálogo de IA | Diálogo normal |
|---|---|---|
| Borde | anillo degradado cian → azul Manik → noche | sin anillo |
| Cabecera | azul noche con aurora (se mueve solo mientras piensa) y filo de luz cian | blanca con divisor |
| Ícono | destello doble en placa translúcida | ninguno |
| Marca | chip «Sugerido por IA» contorneado en cian | — |
| Idea principal | bloque con filo cian | — |
| Acciones de IA | botón contorno noche con destello («Actualizar resumen») | — |
El cuerpo sigue blanco y con la tipografía clínica: la personalidad está en el marco, no en los datos.

## Verificación
Playwright 1300 y 390 px: sin desbordes ni errores JS; `aria-busy` durante el velo; foco en «Empezar consulta»; región viva anuncia pensando y listo; en «Aún analizando» se puede empezar la consulta. Diálogo de comparación con estilo destructivo del sistema.

[pendiente: aprobación; luego aplicar la misma piel al resto de diálogos de IA]
