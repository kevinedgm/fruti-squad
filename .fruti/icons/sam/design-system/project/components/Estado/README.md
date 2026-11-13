# Estado

Chip que dice en qué etapa o situación está una actividad.

- **Activo** (`sam-chip--activo`): solo «En curso», lo que alguien está trabajando ahora. Relleno `brand` con contorno `brand-edge`.
- **Neutro** (`sam-chip--neutro`): el resto de etapas («Nuevo», «Revisión», «Cerrada»). Las etapas las define cada plantilla de flujo; el chip muestra su nombre.
- **Por vencer** y **Vencida** (`sam-chip--aviso`, `sam-chip--peligro`): con `warning` y `danger`.
- Siempre con palabra: el color nunca es la única señal.
- El consumidor pone el texto de la etapa (corto, una o dos palabras).
