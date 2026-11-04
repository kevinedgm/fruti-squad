# BarraFiltros

Filtros y orden en celular y tableta: un botón fijo que abre una hoja inferior, en lugar de una fila de chips que se sale de la pantalla.

- **Barra:** bajo el título de resultados, fija al desplazarse (`position: sticky`): «Filtros» con el número de filtros activos y el orden actual («Más cerca»). Ambos abren hojas inferiores (`aria-haspopup="dialog"`).
- **Hoja:** esquinas de 24 px arriba, asa, título y cerrar (44 px); grupos con `fieldset`/`legend`: «Cómo agendar» (Cita en línea, Con lugar hoy) y «Precio de consulta» (Hasta $500, $800, $1,200); chips con `aria-pressed`.
- **Pie:** «Limpiar» y el botón principal con el resultado en vivo («Ver 5 especialistas»): el paciente sabe qué obtiene antes de cerrar. Respeta el inset inferior del dispositivo.
- Los filtros se evalúan **por consultorio** (ver README, Consultorios).
- **Escritorio (≥ 1024 px):** los mismos filtros como fila de chips sobre la lista (ver Chip).
- Cierra con «Cerrar», tocando fuera o con Escape; el foco vuelve al botón que la abrió.
- El consumidor provee: filtros activos, orden, conteo de resultados para cada combinación.
