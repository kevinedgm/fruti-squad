# Modo autónomo (sin ronda de kiwi ni orden de lima)

Se carga **solo** si no hay ronda aprobada de kiwi ni orden de construcción de lima para la superficie y el usuario quiere seguir con coco (por ejemplo, un proyecto sin kiwi instalado). Antes, dilo en una línea y sugiere empezar por kiwi; si el usuario prefiere seguir con coco, sigue y declara la desviación.

## Paso 1 — Descubrimiento funcional (compuerta)

1. **Superficie existente:** inspecciona el repositorio antes de preguntar nada: punto de entrada, props/API/stores/rutas, estados visibles y ocultos, permisos, acciones, flujo anterior/posterior, responsive actual, los **tokens** y **componentes** que el perfil declara (`production.token_binding`, `production.component_layout`), y los documentos de producto del repo. No preguntes lo que el código responde.
2. **Superficie nueva:** usa el contexto de la conversación y del proyecto. Si falta contexto **esencial** (quién, en qué momento del flujo, qué decide primero, qué datos reales, qué acciones, qué estados, qué sobrevive en móvil), haz 2–6 preguntas funcionales **en un solo mensaje y detente a esperar la respuesta**. Nunca preguntes por estilo.
3. **Salida obligatoria — imprime en el chat el Brief funcional**: usuario/rol, contexto, tarea (verbo + objeto), resultado esperado, dato/estado protagonista, información secundaria, acciones (primaria + secundarias), estados, permisos, flujo anterior/posterior, prioridad responsive, y una lista de **hechos / supuestos / incógnitas**.
4. Compuerta: la tarea cabe en una frase, el protagonista es conocido, el contrato de datos es real o está marcado como ilustrativo, y ninguna incógnita cambiaría la arquitectura de información. Si no se cumple, vuelve al punto 2. **No inventes** campos, estados, permisos ni reglas de negocio.

Después sigue con la clasificación del componente y el `data_contract` del Paso 1 del manual.

## R2 estructural

- **R2 Rediseño / corrección / migración** (sin estructura congelada): rediseño abierto de algo existente o petición de A/B/C. Salida `Actual + A/B/C` con un registro de aprobación. Las tres difieren en jerarquía, organización, densidad o interacción; **nunca solo en color**. Termina preguntando literalmente **«¿Cuál apruebas: A, B o C?»** y **detente**.
- En el Brief visual (Paso 3), una hipótesis estructural distinta por propuesta, descrita **sin mencionar color**.
