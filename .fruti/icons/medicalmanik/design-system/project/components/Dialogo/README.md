# Dialogo

Diálogo: tarea corta que se termina sin salir de la vista. Aprobado 2026-11-05 (`../../formularios-r01/`).

- **¿Diálogo, panel o página?** Confirmación: sin campos. Diálogo de formulario: hasta 6 campos, un grupo, no hace falta ver lo de atrás. Panel lateral: 7 a 12 campos o hay que seguir viendo el contexto (componente pendiente). Página: más de 12 campos, varios grupos o pasos.
- **Anatomía:** cabecera (título `title-2` con verbo + objeto, una línea de contexto en «muted» y cerrar de 44 px), cuerpo (24 px de relleno, 12 px entre campos; solo él se desplaza) y pie (borde superior «line», acciones a la derecha: terciario «Cancelar» y el principal).
- **Medidas:** `dialog-sm` 400 (confirmación), `dialog-md` 560 (formulario), `dialog-lg` 720 (con un par de columnas). Radio `radius-2xl`, `shadow-pop`, fondo detrás `scrim`.
- **Celular (< 640 px):** hoja inferior a todo el ancho, hasta el 90 % del alto, pie fijo con acciones apiladas y el principal arriba.
- **Foco:** al abrir, al primer campo (en confirmación, al botón seguro «Cancelar»); no sale del diálogo; al cerrar vuelve al botón que lo abrió. Usar `<dialog>` con `showModal()` o `role="dialog"`/`alertdialog` con `aria-modal`.
- **Cerrar:** X, «Cancelar» o Esc. Con cambios sin guardar, primero «¿Descartar los cambios?». Un clic fuera no cierra un formulario; sí una confirmación.
- **Nunca un diálogo sobre otro**, salvo la confirmación de descartar.
- **Guardar:** el botón pasa a cargando; al terminar se cierra y un aviso breve confirma («Cita guardada»). Si falla, sigue abierto con el error arriba y los datos intactos.
- **Confirmación destructiva:** el título es la pregunta con el objeto, el cuerpo dice la consecuencia, acciones «Cancelar» y «Sí, eliminar» (Boton destructivo-confirmación). Nunca «Aceptar».
