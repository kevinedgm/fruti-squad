# AppShell

Esqueleto de las apps con 4 o más secciones: barra superior (EncabezadoApp), barra lateral (BarraLateral), contenido y pie. Aprobado 2026-11-05 (`../../shell-r02/`).

- **Rejilla:** barra superior de `header-height` a todo el ancho; debajo, `sidebar-width` (264 px) o `rail-width` (72 px) y la columna de contenido, que se desplaza sola.
- **Contenido:** migas «Módulo › Submódulo» cuando hay submódulo; encabezado de página (`title-1`, una línea de contexto en «muted», acciones a la derecha: secundaria y luego la principal); área de trabajo en «surface» con borde «line» y `radius-2xl`.
- **Pie** (`footer-height`, 44 px) dentro de la columna de contenido: app y versión, estado del sistema, aviso de privacidad, soporte; 13 px en «muted».
- **Tableta** (< `bp-cajon`): la barra lateral es un cajón desde la izquierda con botón de menú en la barra superior; velo `scrim`; se cierra con X, Esc o tocando fuera y el foco vuelve al botón.
- **Celular** (< `bp-celular`): búsqueda como icono, sello sin nombre, acciones de página a todo el ancho, tablas en filas de dos líneas.
- **Enlace «Saltar al contenido»** como primer elemento enfocable.
- **¿Qué navegación?** Se cuentan destinos, no acciones: 2 o 3 → AppPequena (pestañas); 4 a 7 → BarraLateral plana; módulos con submódulos → BarraLateral por módulos. Nunca tres niveles.
