# App shell común · NisaLab, NisaData, NisaStudio (r1)

Prototipo: `shell.html` (regenerar con `python3 gen.py <íconos lucide>`).

## Fijo en todas las apps
- **Barra superior (60 px, blanca):** menú lateral · selector de aplicaciones (rejilla) · logo de la app · búsqueda (Ctrl K) · ayuda · avisos · usuario. Línea inferior de 2 px con el degradado base → acento de la app.
- **Selector de aplicaciones:** lista de apps a las que la persona tiene acceso (ícono, nombre, para qué sirve) y «Ir a todas las aplicaciones» (hub.nisanabani.com).
- **Menú del usuario:** nombre, correo, Mi cuenta, Preferencias, Cerrar sesión.
- **Menú lateral (240 px; 72 px plegado):** nombre de la app, secciones, y abajo Ayuda y Configuración. En pantallas de 860 px o menos se vuelve cajón con fondo oscurecido.
- **Área de trabajo:** fondo #F2F4F8; encabezado (ruta, título, conteo, acción principal) y contenido.

## Cambia por app (tokens)
| App | `--side` | `--side2` | `--acc` (sección activa) | Logo |
|---|---|---|---|---|
| NisaLab | #052A76 | #0A3487 | #C2D225 | nisalab-final/logotipo |
| NisaData | #1F2532 | #2A3142 | #FF8A1F | nisadata-final/logotipo |
| NisaStudio | #3730A3 | #4038B5 | #14B8A6 | nisastudio-final/logotipo |

La acción principal del área de trabajo usa `--side`.

## Encabezado de página en NisaLab
El área de trabajo usa EncabezadoModulo (design system de NisaLab):
- **Por área (opción B aprobada):** Recepción (Aguas), Muestras (Alimentos), Captura (Aguas), Bitácoras (Bebidas alcohólicas), Informes (Aguas): marca del área, nombre del área junto al título y línea de 3 px en su color.
- **Global:** Catálogos (Normas) y Usuarios: sin marca ni línea, con entradilla.
NisaData y NisaStudio usan solo la variante global.

## Pendiente
- Contenido real de cada pantalla (aquí son marcadores).
- Comportamiento de la búsqueda global y de los avisos.
