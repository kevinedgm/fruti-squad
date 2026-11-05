# Campo

Campo de captura. Atkinson en todo el texto: distingue 1, l e I, y 0 y O. Aprobado 2026-11-05 (`../../controles-r01/`).

- **Tipos:** texto, número con unidad, lista, fecha, buscador (icono a la izquierda y botón para borrar) y área de texto (mínimo 96 px).
- **Anatomía:** etiqueta `label` arriba, siempre visible, en sustantivo y sin dos puntos; ayuda abajo en «muted»; el texto de ejemplo dentro del campo no sustituye a la etiqueta.
- **Medidas:** 44 px, borde 1 px «line-control», radio `radius-md`, texto 16 px.
- **Estados.** Hover: borde «muted». Foco: borde «manik» y anillo «focus» 2 px. Error: borde 2 px «error», icono y mensaje que dice qué hacer («Máximo 100 mg al día»), `aria-invalid` y `aria-describedby`. Solo lectura: «surface-soft» con borde «line» (se puede copiar). Deshabilitado: «surface-soft», borde «line», texto «muted».
- **Opcional:** se marca «(opcional)»; lo obligatorio no lleva marca.
- **Números clínicos** (dosis, peso, glucosa): cifras tabulares, alineados a la derecha, unidad fija como sufijo en «muted». La unidad la pone el sistema.
- El consumidor provee: etiqueta, unidad, rango válido y mensaje, `id` y `aria-describedby`.
