# Reseñas, calificación y guardados

Lo propio de Laranda no es el dibujo sino qué se mide y en qué orden se pregunta.

## Tres piezas

- **La flor como calificación.** Cinco lóbulos; el quinto, el que se abre, solo se enciende con 5. Número siempre escrito. Componente `Calificacion`.
- **«Vuelven», la métrica propia.** Clientes con dos o más folios entre todos los clientes de los últimos 12 meses. Se calcula sola, no se infla con reseñas. Sin dato hasta 10 clientes distintos. Componente `Vuelven`.
- **Guardar es el lóbulo suelto.** Contorno / relleno `accent`. Los guardados viven en «Mis oficios» y su acción es volver a reservar. Componente `Guardar`.

## El flujo

Solo con folio. Paso 1 «¿Volverías?» con un toque; paso 2 etiquetas; paso 3 texto opcional. La calificación de 1 a 5 se deriva (sí + 3 etiquetas = 5, sí = 4, no + etiquetas = 2, no = 1) y se puede afinar tocando las flores. Componentes `FlujoResena` y `Resena`.

## Reglas

- Sin promedio hasta 3 reseñas; sin «vuelven» hasta 10 clientes. Nunca un 0 ni un 5.0 con una sola reseña.
- Toda reseña lleva el sello «con folio»; la línea de meta dice si el cliente volvió a reservar.
- El profesional responde una vez, en público. Las reseñas no se borran: se reportan y pasan a «en revisión».
- En el perfil, las etiquetas agregadas («Puntual · 96») acompañan al promedio: dicen más que el número.
- La primera reseña es un hito: la flor se abre con `bloom` y el perfil empieza a mostrar calificación.
