# ControlSegmentado

Control segmentado: cambia la vista de lo mismo (día, semana, mes). De 2 a 4 opciones cortas. No filtra datos (eso es ChipFiltro) ni navega a otra sección (eso son pestañas).

- Contenedor «surface-soft» con borde «line» y radio `radius-md`; opción de 36 px; la elegida en «surface» con `shadow-card` y texto «manik».
- `role="radiogroup"` con `role="radio"` y `aria-checked`; flechas para moverse, una sola parada de tabulador.
