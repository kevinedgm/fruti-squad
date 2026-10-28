# FormularioUsuario

Formulario de alta y edición en panel lateral: se llena sin perder de vista la tabla.

- **Contenedor:** panel derecho de 440 px, `surface`, `radius-lg`, `shadow-overlay`; encabezado con título (`title-2`), una línea de qué pasará y «Cerrar»; pie fijo con «Cancelar» (secundario) y la acción primaria con verbo + objeto («Enviar invitación», «Guardar cambios»).
- **Campos:** etiqueta `label` arriba, ayuda `caption` abajo; borde «border-control», `shadow-inset`, anillo «primary-soft» al enfocar. El correo va en Plex Mono porque se copia y se compara.
- **Errores:** al salir del campo; borde «fuera», anillo «fuera-soft», icono y mensaje que dice cómo corregir («Falta el dominio: debe terminar en @nisanabani.mx»). Al enviar con errores, el foco va al primero.
- **Opciones excluyentes** (rol): tarjetas de opción con descripción, la elegida en «primary-soft» con borde «primary». **Múltiples** (divisiones): casillas en chip.
- **Zona de riesgo** solo en edición, separada por un filete, con el botón destructivo (`btn-d`) y su consecuencia escrita. Nunca junto a «Guardar».
- **Riesgo:** cerrar con cambios sin guardar pide confirmar («Descartar cambios»); suspender pide motivo; dar de baja es otra acción con confirmación.
- El consumidor provee: modo (alta/edición), valores, roles y divisiones disponibles, y permisos.
