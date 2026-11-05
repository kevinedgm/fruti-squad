# EncabezadoApp

Barra superior que comparten todas las apps: sello y nombre de la app a la izquierda; búsqueda, avisos, el botón del ecosistema y el avatar a la derecha.

- 64 px (`header-height`), fondo «surface», borde «line». La navegación es clara en todo el ecosistema.
- El botón del ecosistema (mosaico de seis cuadros, 24 px en un área de 44) va siempre en el mismo lugar: justo antes del avatar. Su nombre accesible: «Ecosistema Manik: cambiar de app».
- El sello de la app a 32–36 px. Clic en el sello o el nombre: inicio de esa app.
- El consumidor provee: la app, la búsqueda propia de la app y el usuario.

- **Por ancho (2026-11-05):** por debajo de `bp-cajon` aparece a la izquierda el botón de menú que abre el cajón de la barra lateral (`aria-expanded`, `aria-controls`); por debajo de `bp-celular` la búsqueda pasa a botón con lupa y el sello va sin nombre. El nombre y el rol del usuario se ocultan por debajo de `bp-cajon`; el avatar queda.
