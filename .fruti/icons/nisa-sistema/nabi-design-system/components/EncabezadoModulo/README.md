# EncabezadoModulo

Encabezado de un módulo: dice dónde estás, qué es este módulo, cuántos registros hay y cuál es la acción principal.

- **Ruta** (`label`, «text-muted»): sección › módulo. El último tramo no es enlace.
- **Título** (`title-1` ampliado: Poppins 600, 24/32): el nombre del módulo, sin icono. El icono del módulo vive en el menú lateral; repetirlo junto al título no agrega información. Excepción: la variante por área (abajo).
- **Entradilla** (Poppins 400 15/22, «text-muted»): una línea opcional que dice para qué sirve el módulo. Solo en módulos de configuración o de consulta poco frecuente; en módulos de trabajo diario (Recepción, Captura) se omite.
- **Conteo** (`valor-sm`/Plex Mono): totales que importan para decidir («3 invitaciones pendientes»), no todos los totales.
- **Acciones**: a la derecha, alineadas a la base del título. Una sola primaria (`shadow-primary`): «Agregar usuario». Secundarias en `btn-s` (Exportar). Máximo tres visibles; el resto en un menú «Más».
- Sin fondo propio: el encabezado se apoya en «bg»; la tarjeta de la tabla es lo que se eleva.
- El consumidor provee: ruta, título, entradilla (opcional), conteos y acciones.

## Variante por área

Para páginas que trabajan dentro de un área (Recepción, Bitácora y Resultados de Aguas, Alimentos, Bebidas…). Su trabajo es que nadie capture en el área equivocada: el área se reconoce de lejos, sin leer.

- **Marca del área** (Colonia con la célula del área, 52 px; 40 px bajo 640) a la izquierda del título. Es decorativa (`aria-hidden`): el nombre del área ya está en el título y en la ruta.
- **Título**: la tarea + el nombre del área en Poppins 400 «text-muted» («Recepción de muestras **Aguas**»). El color nunca es la única señal.
- **Línea del área**: borde inferior de 3 px en `area-*` (`--ac`). Es la única superficie que toma el color del área; el fondo, el texto y los botones no cambian.
- **Ruta**: sección / área («Recepción / Aguas»).
- Las acciones no cambian: una primaria, en azul real, nunca en el color del área (el color del área no es de acción).
- Páginas globales (Usuarios, catálogos de servicios y de normas) usan la variante global, sin marca ni línea.
- Supuesto vigente: «Bebidas alcohólicas» usa `area-bebidas` hasta confirmar si sustituye a «Bebidas de agave».
