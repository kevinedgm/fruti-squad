# Formulario

Formulario en página. Aprobado 2026-11-05 (`../../formularios-r01/`).

- **Una columna.** Dos solo para pares cortos que se leen juntos (inicio y fin, presión sistólica y diastólica); nunca tres.
- **Orden de la tarea**, no de la base de datos; lo que se calcula no se pide; se llena lo que ya se sabe (paciente, fecha, médico en sesión).
- **Grupos con título** (`title-2`) con más de 5 campos: `space-3` (12 px) entre campos, `space-8` (32 px) entre grupos; sin líneas.
- **Ancho por dato** y `form-max` (640 px) para todo el formulario.
- **Acciones al final**, a la derecha: terciario «Cancelar» y luego el principal con verbo + objeto. La destructiva a la izquierda, separada. En celular, apiladas a todo el ancho, el principal arriba.
- **Validación:** al salir del campo y al enviar; mientras se escribe solo para límites clínicos. Al enviar con errores, resumen arriba (número de errores y un enlace a cada uno) que recibe el foco; los datos se quedan. Error del servidor: aviso arriba con la acción posible. Salir con cambios pide «¿Descartar los cambios?».
- **El botón principal nunca se deshabilita.**
