# Sellos con la M original · r01 (aprobada 2026-11-05)

Pedido (2026-11-05): «respetar la forma de la M: tomar del archivo AI la forma de la M para no redondear sus esquinas y forma».
Fuente: «Logos editables MM.ai» del usuario (Illustrator 29.7, compatible con PDF, 6 mesas de trabajo). **No se versiona.** Solo se guarda la geometría de la M (mesa 5, sello sólido), extraída con `pdftocairo -svg` y normalizada a la retícula de 100 de los sellos (`gen.py`, constante `RAW` → `M_ORIGINAL`).

## Qué cambia
- La M deja de ser una polilínea con trazo de 13 y uniones redondas; pasa a ser el trazado relleno original (grosor variable, picos estrechos).
- Sustitución exacta en 29 archivos (`../final/svg` y `../manik-final/svg`): 16 versiones en color (M en #F6F8FC recortada al contenedor) y 13 máscaras de una tinta. Contenedores, rasgos y colores sin cambio.
- Radio del cuadro original 20.4 % del lado; el de los sellos, 21 % (se conserva el de los sellos).
- `python3 gen.py` → `svg/` (copias nuevas) y `comparacion.html` (antes / después a 120, 64, 32, 24 y 16 px, una tinta, negativo y logotipos).

## Por revisar antes de aprobar
Lectura a 16–24 px (picos más finos) · cercanía del pico alto con la pestaña de Expediente y las argollas de Agenda.

## Al aprobar
Reemplazar en `../final/svg` y `../manik-final/svg` (y los generadores), regenerar PNG, subir los assets al sistema de diseño del Ecosistema y del directorio, y actualizar la lámina de construcción del manual (hoy dibuja la línea con trazo 13).

## Propagación (2026-11-05)
- Canónico: `../final/m_original.py` (M_ORIGINAL + convertir). Los generadores `../final/gen.py`, `../manik-final/gen.py` y `../administracion-r1/gen.py` pasan su SVG por convertir().
- 29 SVG reemplazados en `../final/svg` y `../manik-final/svg`; 80 PNG regenerados (16–512).
- Sistema de diseño del Ecosistema (v10): 8 sellos subidos como assets nuevos, blobs actualizados en design-system.json, previews y build.py; previews del shell regeneradas.
- Sistema de diseño del directorio (v13): 10 assets (Marca y Logotipos) nuevos; previews Cover y Encabezado.
- Manual de identidad (v7, lámina de construcción con la M original), arquitectura de marca (v2), manual del directorio (v3) y prototipo del directorio (v18, https://claude.ai/artifact/EfXbngHaw3pqZ8EbN8egFM) regenerados; fuera de los SVG embebidos no cambió nada.
- Rondas antiguas (ronda-3…5, guías, manik-ronda-*) quedan como historia con la línea anterior.
