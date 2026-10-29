# EncabezadoModulo

Encabezado de un módulo: dice dónde estás, qué es este módulo, cuántos registros hay y cuál es la acción principal.

- **Ruta** (`label`, «text-muted»): sección › módulo. El último tramo no es enlace.
- **Título** (`title-1` ampliado: Poppins 600, 24/32): el nombre del módulo en plural, sin icono. El icono del módulo vive en el menú lateral; repetirlo junto al título no agrega información.
- **Entradilla** (Poppins 400 15/22, «text-muted»): una línea opcional que dice para qué sirve el módulo. Solo en módulos de configuración o de consulta poco frecuente; en módulos de trabajo diario (Recepción, Captura) se omite.
- **Conteo** (`valor-sm`/Plex Mono): totales que importan para decidir («3 invitaciones pendientes»), no todos los totales.
- **Acciones**: a la derecha, alineadas a la base del título. Una sola primaria (`shadow-primary`): «Agregar usuario». Secundarias en `btn-s` (Exportar). Máximo tres visibles; el resto en un menú «Más».
- Sin fondo propio: el encabezado se apoya en «bg»; la tarjeta de la tabla es lo que se eleva.
- El consumidor provee: ruta, título, entradilla (opcional), conteos y acciones.
