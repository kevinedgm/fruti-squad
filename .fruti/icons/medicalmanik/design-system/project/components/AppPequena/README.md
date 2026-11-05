# AppPequena

La alternativa para apps de 2 o 3 secciones (por ejemplo, Impulsa: Campañas y Resultados). Aprobada 2026-11-05.

- **Sin barra lateral:** 264 px para dos enlaces harían ver la app más grande de lo que es.
- **Pestañas bajo la barra superior,** a todo el ancho en «surface» con borde «line»: icono de 18 px y texto 15 px 600; la actual en «manik» con subrayado de 3 px. Son destinos: `<nav>` con enlaces y `aria-current="page"`, no `role="tab"`.
- **Las acciones no son pestañas:** «Nueva campaña» es el botón principal del encabezado de página.
- **Contenido centrado** a `content-narrow` (1120 px); mismo encabezado de página, área de trabajo y pie que AppShell.
- **Celular:** las pestañas se reparten el ancho; no hay cajón ni barra inferior.
- **Si la app crece** a 4 secciones o más, pasa a BarraLateral plana; no se suman pestañas.
