# Sellos con la M original · r01 (propuesta)

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
