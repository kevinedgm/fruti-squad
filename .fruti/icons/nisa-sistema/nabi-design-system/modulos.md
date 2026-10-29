# Módulos

Cómo se arma una pantalla de módulo en Nabi (Usuarios, Clientes, Métodos, Equipos): qué color va en cada zona, qué voz tipográfica, dónde viven las acciones, cómo se muestran los estados y cómo responden las interacciones. El ejemplo vivo es el componente `ModuloUsuarios`.

## Anatomía

1. **Encabezado** (`EncabezadoModulo`): ruta · título · entradilla opcional · conteo · acciones. Sin fondo propio.
2. **Tarjeta de trabajo**: barra de herramientas, tabla y pie, en una sola tarjeta elevada (`shadow-1`).
3. **Capas** que aparecen solo cuando hacen falta: barra de acciones en lote, panel lateral del formulario, aviso con «Deshacer».

## Color por zona

| Zona | Fondo | Texto | Borde y sombra |
|---|---|---|---|
| Página | `bg` | — | — |
| Encabezado | (sobre `bg`) | título `text`; ruta, entradilla y conteo `text-muted` | — |
| Acción primaria | `primary` | `on-primary` | `shadow-primary`; hover `primary-hover` + `shadow-primary-hover` |
| Acción secundaria | `surface` | `primary` | `border-control` + `shadow-1` |
| Tarjeta de trabajo | `surface` | `text` | `border` + `shadow-1` |
| Encabezado de tabla | `surface-sunken` | `text-muted` | `border` abajo |
| Fila en hover | `surface-hover` | `text` | — |
| Fila seleccionada | `primary-soft` | `text` | casilla marcada |
| Registro en curso | — | — | un pocillo `pera` junto al nombre (uno por pantalla) |
| Campos | `surface` | `text`; placeholder `text-subtle` | `border-control` + `shadow-inset`; foco `primary` + anillo `primary-soft` |
| Filtro activo | `primary-soft` | `primary` | — |
| Estados | `*-soft` | `on-*-soft` + icono | — |
| Barra de lote, aviso | `text` (tinta) | blanco | `shadow-overlay` |
| Panel lateral | `surface` | `text` | `shadow-overlay`, `radius-lg` |
| Destructiva | `surface` | `fuera` | borde `fuera`; separada por un filete |

Proporción: casi todo es `bg`, `surface` y tinta; el azul aparece en la acción primaria, los enlaces y la selección; los colores de estado solo en la columna de estado; el pera, una vez.

## Tipografía por zona

| Elemento | Estilo |
|---|---|
| Ruta | `label` (Poppins 500 13/18) |
| Título del módulo | Poppins 600 24/32 (`title-1` ampliado) |
| Entradilla | `body` ampliado (Poppins 400 15/22, `text-muted`) |
| Conteo, último acceso, correos, folios | Plex Mono (`valor-sm`, `folio`) con cero con barra |
| Encabezados de columna | `label` |
| Nombre en tabla | Poppins 600 14/20 |
| Botones | `button` |
| Título del panel | `title-2` |
| Ayudas y errores | `caption` |

## Encabezado: reglas

- **Título sin icono.** El icono del módulo vive en el menú lateral; junto al título repite información y compite con la acción primaria.
- **Una sola acción primaria**, arriba a la derecha, con verbo + objeto: «Agregar usuario», «Registrar cliente». Las demás, secundarias o en «Más».
- **Entradilla** solo en módulos de configuración o poco frecuentes; nunca en pantallas de captura diaria.
- **Conteos** que ayudan a decidir («3 invitaciones pendientes»), en Plex Mono.

## Tabla de personas

- Columnas en este orden: casilla · Usuario (iniciales o foto, nombre, correo) · Rol · Divisiones · Último acceso · Estado · acciones.
- Filas de 56 px (dos líneas); 40 px si solo hay una.
- Lo que se compara o copia (fechas, correos, folios) en Plex Mono; lo que se lee, en Poppins.
- Acciones por fila: «Editar» y «Más», visibles al pasar o enfocar la fila y siempre en táctil. Nunca más de dos iconos por fila.

## Estados

El color sigue al significado y es el mismo en todos los módulos:

| Significado | Tokens | Ejemplos |
|---|---|---|
| Está bien | `conforme-soft` / `on-conforme-soft` | Activo · Conforme · Liberada |
| Pendiente | `pendiente-soft` / `on-pendiente-soft` | Invitación enviada · En análisis |
| Requiere atención | `alerta-soft` / `on-alerta-soft` | Suspendido · En revisión |
| Impedido | `fuera-soft` / `on-fuera-soft` | Bloqueado · Fuera · Rechazada |
| Fuera de uso o neutro | contorno `border-strong` sobre `surface` / `text-muted` | Dado de baja · Recibida |

Siempre icono + palabra. El pera no es un estado, y ningún color de división (`div-*`) se usa como estado.

La columna **Divisiones** muestra el azulejo de 16 px de cada división y su nombre en `text`; el color identifica la división, nunca su estado.

## Interacciones

| Interacción | Respuesta |
|---|---|
| Pasar sobre una fila | `surface-hover` en 150 ms (`quick`); aparecen sus acciones |
| Seleccionar | `primary-soft`; aparece la barra de lote con el conteo |
| Filtrar | El chip pasa a `primary-soft`; el conteo y el pie se actualizan; si no hay resultados, estado vacío con «Limpiar filtros» |
| Ordenar | Flecha en la columna activa y `aria-sort` |
| Abrir formulario | Panel lateral con `shadow-overlay`; el registro en curso recibe el pocillo pera; Esc o «Cerrar» devuelven el foco |
| Guardar | Botón ocupado (sin doble envío); al terminar, aviso con «Deshacer» si se puede revertir |
| Botón primario | Hover: 1 px hacia arriba y sombra mayor; presionado: vuelve a su lugar |

Con `prefers-reduced-motion`: sin desplazamientos, solo cambios de color.

## Formularios

- En **panel lateral** de 440 px para altas y ediciones cortas; en página propia si pasan de ~12 campos o tienen secciones.
- Etiqueta arriba, ayuda abajo, error en lugar de la ayuda; validación al salir del campo; al enviar con errores, foco al primero.
- Opciones excluyentes con descripción → tarjetas de opción; múltiples cortas → casillas en chip.
- Pie fijo: «Cancelar» (secundario) a la izquierda de la primaria. Lo destructivo, en «Zona de riesgo», separado y con su consecuencia escrita.

## Estados de la pantalla

- **Carga:** esqueleto con la huella de la tabla (filas de 56 px); el encabezado ya visible.
- **Vacío inicial:** frase editorial («Aún no hay usuarios») + qué hacer + acción primaria.
- **Vacío por filtros:** «Ningún usuario coincide» + filtros activos + «Limpiar filtros».
- **Error:** causa + «Reintentar»; si había datos, se conservan y se marcan como no actualizados.
- **Sin permiso:** el módulo no aparece en el menú; si se llega por enlace, explicación y a quién pedir acceso.

## Por espacio

- **Escritorio (≥ 1024):** todo visible; panel lateral junto a la tabla.
- **Tableta (600–1023):** Divisiones y Último acceso pasan al detalle; el panel cubre la tabla.
- **Móvil (< 600):** cada usuario es un bloque (nombre, correo, estado); acciones en el menú «Más»; «Agregar usuario» como botón fijo abajo; el formulario a pantalla completa.
