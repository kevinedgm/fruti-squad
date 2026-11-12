# Arquitectura de agentes: un solo bucle con skills

Revisión de Fruti Squad frente a *Building agents: when to fold subagents into your main agent loop* (Anthropic). Tesis del artículo: un solo agente con skills que se cargan cuando hacen falta suele dar mejor calidad, menos costo y menos latencia que una cadena de subagentes; un subagente se conserva solo si una evaluación muestra que el agente único empeora.

## Dónde está Fruti hoy

Fruti ya sigue el patrón que el artículo recomienda:

| El artículo recomienda | Fruti |
|---|---|
| Un solo bucle; el plan y la ejecución en el mismo modelo | Kiwi, Lima, Coco, Bruno y Mora corren como skills en la misma conversación; no hay subagentes |
| Divulgación progresiva: descripciones cortas, detalle solo cuando hace falta | "Route first, read second": `.fruti/runtime/<agente>.yaml` dice qué leer en cada operación |
| Los límites duros en herramientas, no en el prompt | `fruti fidelity` (FID-GEOMETRY-001) y los chequeos deterministas del `audit-manifest.yaml` corren en scripts antes del juicio del modelo |
| Pasar estado compacto, no copiar documentos | `handoffs/current.json` es un índice a artefactos, con `round` |

Conclusión: **no hay subagentes que juntar**. Lo que aplica son los otros dos consejos del artículo.

## Lo que aplica

### 1. Medir con un conjunto fijo de tareas

`fruti test` califica una petición, pero cada ronda usa una petición distinta, así que no se pueden comparar versiones del squad. Se agregó `evals/` con 6 casos fijos y `fruti test --case <caso>`, que marca la ronda con el caso para comparar rondas del mismo caso. Cada caso se corre dos veces (el artículo reporta una regresión que apareció en una sola de dos corridas).

### 2. Dónde un subagente sí podría ganar (por medir)

El artículo conserva un subagente cuando el contexto crece demasiado o cuando conviene un contexto limpio. En Fruti hay un punto que cumple lo segundo:

| Punto | Riesgo hoy | Prueba propuesta |
|---|---|---|
| `model_review` de Coco (jerarquía, claridad, densidad, composición adaptativa) | Coco califica con juicio su propia construcción, en el mismo contexto donde la decidió. La fidelidad estructural ya se sacó a un script por esta razón; la revisión visual no | Correr solo `model_review` en un subagente de contexto limpio que recibe F2, F3, contrato y tokens, y comparar con `evals/` |
| Ronda completa Kiwi → Mora en una conversación | El contexto acumula F2, contrato, F3, auditoría y documentación | Medir con los casos 01 y 03 si la calidad de Mora baja al final de la ronda |

Ninguno se cambia sin la línea base de `evals/`.

### 3. Elegir bien entre skills que conviven

El artículo advierte que la selección empeora con muchas herramientas o skills parecidas. Fruti convive con `impeccable`, `improve-animations`, `skill-architect`. El caso 06 (cambio de token) verifica que la petición llegue a Lima y no a Kiwi.

## Regla

Cambiar una cosa a la vez, correr `evals/` antes y después, comparar caso por caso, y conservar el cambio solo si ningún caso empeora.
