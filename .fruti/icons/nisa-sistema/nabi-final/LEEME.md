# Nabi · paquete final

Sistema de laboratorio de Nisa Nabani (antes «Conectti»). Símbolo: placa de 4×4 pocillos redondos; los llenos dibujan la N, los vacíos son puntos y la muestra pera ocupa el pocillo superior derecho. Wordmark «nabi» en Archivo 700, ancho 125 %, con pocillo pera como punto de la i. Color: azul real #052A76 y pera #C2D225 del laboratorio. Manual: https://claude.ai/artifact/SpJUaBTY9zUURYgy8NGk5A

- `gen.py <scratchpad>`: regenera `svg/`, `tema.json` y `pruebas.md` (usa las funciones de `../nabi-ronda-4/gen.py`).
- `svg/`: simbolo (-tinta, -blanco, -blanco-una), wordmark (-blanco, -tinta), lockup-h (-blanco, -tinta), lockup-familia (-blanco), lockup-v, favicon (cambia con el esquema), favicon-tinta, app-icon (-claro, -maskable), avatar, carga (-blanco; animado con CSS y reducir movimiento), tarjeta-redes.
- `png/`: icon 1024/512/192, maskable, claro, avatar, símbolos 512, favicon 16/32/48 + .ico, wordmark y lockups a 240 px, tarjeta 1200×630, carga.gif.
- Pendiente: conciliar azul/pera con el acento esmeralda de Verdant en la UI; búsqueda de marca «Nabi».
