# Botón

Botón de acción de SAM: principal en Voltaje, secundario con borde y de texto.

- **Principal** (`sam-btn sam-btn--primario`): la acción que hace avanzar el trabajo («Avanzar etapa», «Nueva actividad»). Una por vista. Relleno `brand`, texto `on-brand`, contorno `brand-edge`.
- **Secundario** (`sam-btn--secundario`): acciones alternas («Reasignar»). Borde `line-control`.
- **Texto** (`sam-btn--texto`): acciones menores y enlaces («Adjuntar evidencia»). Subrayado, en `ink`.
- **Desactivado**: `aria-disabled="true"` y un texto cerca que diga qué falta; no lo quites del orden de tabulación.
- El consumidor pone la etiqueta: un verbo concreto. Altura mínima `control-height`; foco con `focus`.
- No: dos botones principales en el mismo bloque, Voltaje con texto blanco, un icono sin etiqueta.
