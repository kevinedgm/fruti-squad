# ModuloUsuarios

Módulo completo de Usuarios: la composición de referencia para cualquier módulo de administración de NisaLab (clientes, métodos, equipos).

Orden de arriba abajo: `EncabezadoModulo` → tarjeta con barra de herramientas (búsqueda + filtros + limpiar), barra de acciones en lote (solo con selección), `TablaUsuarios`, pie con rango y paginación. «Agregar usuario» y «Editar» abren `FormularioUsuario` en panel lateral; al guardar, un aviso confirma con «Deshacer» cuando se puede revertir.

Pruébalo: busca, filtra por estado, selecciona filas, abre «Agregar usuario» y envía con un correo sin dominio. Ver la sección «Módulos» del manual para las reglas.
