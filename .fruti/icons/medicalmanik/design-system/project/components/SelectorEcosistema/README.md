# SelectorEcosistema

Panel que abre el botón del ecosistema: las apps a las que la persona tiene acceso, con la actual marcada.

- Se abre bajo el botón, alineado a la derecha; 380 px de ancho; sombra `shadow-pop`. Cierra con Escape, clic fuera o al elegir una app; el foco vuelve al botón.
- Rejilla de 3 columnas: sello a 44 px y nombre del producto (sin «Manik»: el panel ya lo dice). La app actual: fondo «manik-soft», «Aquí estás» y `aria-current="page"`.
- Solo muestra las apps con acceso. Al pie, «Ir al inicio del ecosistema».
- Orden fijo en todo el sistema: Expediente, Agenda, Compras, Farmacia, Impulsa, Grupos.
- El consumidor provee: la lista de apps con acceso y la app actual.
