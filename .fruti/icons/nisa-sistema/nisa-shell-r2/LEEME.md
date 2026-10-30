# App shell común · r2 sobrio (tipo Notion)

Prototipo: `shell.html` (regenerar con `python3 gen.py <íconos lucide>`). Sustituye a r1 (menú lateral de color, descartado por el usuario).

## Fijo en todas las apps
- **Menú lateral (240 px; 68 px plegado):** fondo #F6F7F9 con línea #E6E8EE. Arriba, el **selector de aplicaciones** (ícono, nombre y para qué sirve; abre la lista de apps y «Todas las aplicaciones» → hub.nisanabani.com). Después «Secciones» y abajo Ayuda y Configuración. Sección activa: fondo #E8EAF0, texto en negritas, ícono en el color de la app. En 860 px o menos, cajón.
- **Barra superior (52 px, blanca):** plegar menú · ruta (miga) · búsqueda (Ctrl K) · ayuda · avisos · usuario (menú con Mi cuenta, Preferencias, Cerrar sesión).
- **Área de trabajo:** blanca; tarjetas con borde #E6E8EE (nunca blanco sobre blanco sin borde). Ancho de lectura máximo 1080 px.

## Cambia por app
Solo el ícono y el nombre en el selector, el color del ícono de la sección activa y el del botón principal (`--side`): NisaLab #052A76 · NisaData #1F2532 · NisaStudio #3730A3.

## Encabezado de página
NisaLab usa EncabezadoModulo: por área (opción B) en Recepción, Muestras, Captura, Bitácoras e Informes; global en Catálogos y Usuarios. NisaData y NisaStudio, global. La ruta vive en la barra superior, no se repite en el encabezado.

## Pendiente
- Cómo elige la persona el área de trabajo (selector, menú o fija por puesto).
- Búsqueda global y avisos.
