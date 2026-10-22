# Calificación en flores

Imágenes de la calificación de Laranda: cinco lóbulos en vez de cinco estrellas. `calificacion-N` muestra N lóbulos llenos (0 a 5); el quinto, el lóbulo separado, solo se enciende con 5 y va en `accent`. Siempre acompañada del número escrito («4 de 5», «4.9 · 128 reseñas»).

- `svg/calificacion-N.svg`: una sola versión con variables CSS (`--brand`, `--accent`, `--surface`) y fallback claro; toma el tema del contexto.
- `svg/calificacion-N-claro.svg` y `-oscuro.svg`: colores fijos (claro: brand #5B3BB5, accent #E0611A, garganta #FFFFFF; oscuro: #C4B5F0, #F2A074, #1A191D).
- `png/calificacion-N-{claro|oscuro}-{24|48|96|256}.png`: fondo transparente. 16–24 px en listas, 24 en la tarjeta, 36–48 en la entrada de calificación.
- Regenerar: `python3 gen.py` y el script de captura.

![Lámina](lamina.png)
