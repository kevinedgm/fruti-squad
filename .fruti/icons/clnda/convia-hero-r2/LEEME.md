# Convia · hero del directorio r2 (arcos + cielo + temporadas)

El usuario eligió **B (portal de arcos)** y **C (cielo vivo)** de la ronda 1 y pidió **temporadas tipo doodle** (Día de Muertos, Guelaguetza…) que cambien fondo y logo.

## Regla
- **Fijo**: arcos (navegación: Cafés · Restaurantes · Hoteles · Museos · Agenda, igual que las pestañas del directorio r11), buscador, intenciones, la palabra «Convia».
- **Cambia por temporada**: cielo, cerro, papel picado, adorno (pétalos de cempasúchil, listones, rábanos), color de la piedra de los arcos, **la estrella del logo** (como los doodles: el nombre se queda, el símbolo se viste), título, texto y enlace a la agenda de la temporada.
- La portada elige sola por fecha (`desde`/`hasta` en MM-DD, se repite cada año). Fuera de temporada: «cotidiano», con el cielo según la hora (mañana, tarde, noche).
- Cada temporada es un **registro de datos** (ver `TEMPORADAS` en `plantilla.html`); agregar una edición no toca el diseño.
- Crédito al pie: propuesta de encargar cada edición a una ilustradora o un ilustrador de Oaxaca.

## Temporadas de la demo (fechas verificadas)
- Día de Muertos: 31 oct – 2 nov (la demo arranca el sáb 31 oct 2026, así que se ve esta edición).
- Guelaguetza: 12 – 27 jul; los Lunes del Cerro son los dos lunes después del 16 de julio (2027: 19 y 26 jul).
- Noche de Rábanos: 20 – 23 dic (la noche es el 23).
- Pendiente de verificar: si el nombre «Guelaguetza» tiene restricciones de uso comercial antes de usarlo en una campaña.

## Verificación
1440, 820 y 390 px: sin desborde, sin errores, título y texto dentro de la tarjeta en las cuatro variantes; movimiento apagado con «reducir movimiento».
- Publicado: https://claude.ai/artifact/6M4fcSSKyQfYw14wnU2PbA. Uso: `python3 gen.py <carpeta de salida>`.
