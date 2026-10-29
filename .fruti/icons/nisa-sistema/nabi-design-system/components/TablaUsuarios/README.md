# TablaUsuarios

Tabla de un módulo de personas o registros: se escanea por nombre, se compara por rol y estado y se actúa por fila o en lote.

- **Contenedor:** `surface` + `border` + `shadow-1`, radio `radius-md`, sobre «bg». Es lo único elevado de la pantalla.
- **Encabezado:** `label` en «text-muted» sobre «surface-sunken». Ordenables con flecha doble y `aria-sort` en la columna activa.
- **Filas de 56 px** cuando hay dos líneas (nombre + correo); 40 px (`row-h`) cuando hay una.
- **Persona:** iniciales en círculo («primary-soft» / «primary»), nombre en Poppins 600, correo en Plex Mono 12 («text-muted»). Foto si existe, del mismo tamaño.
- **Datos que se comparan o copian** (último acceso, folios, fechas) en Plex Mono con cero con barra.
- **Estado:** `EstadoUsuario`, siempre en la misma columna, al final antes de acciones.
- **Interacción:** hover → «surface-hover»; seleccionada → «primary-soft» + casilla marcada; registro en curso (el que está abierto en el panel) → un solo pocillo pera junto al nombre. Acciones por fila (Editar, Más) aparecen al pasar o enfocar la fila y siempre en táctil.
- **Selección múltiple:** aparece la barra de acciones en lote (tinta, `shadow-overlay`) con el conteo en Plex Mono y máximo tres acciones.
- **Pie:** rango en Plex Mono y paginación; más de 50 filas → paginar o virtualizar.
- El consumidor provee: columnas, filas, orden, selección y acciones permitidas por rol.
