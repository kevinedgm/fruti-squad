# Convia · QR de mesa r1

Pedido del usuario (2026-10-31): identidad de los QR que el restaurante (o café) pone en sus mesas para ver el menú en Convia, con cámara o NFC. El establecimiento es el protagonista; Convia aparece discreto.

## Jerarquía
1. **El establecimiento**: cabecera con su nombre (o logo) y **su color** (no el de Convia).
2. **Qué hacer**: «Escanea · Scan» y «Acerca tu teléfono · Tap your phone» (NFC), en español e inglés.
3. **El QR**: grande, sin nada encima (ni la estrella), oscuro sobre blanco, con su dirección corta debajo.
4. **Convia**: estrellita + «Menú en Convia» / «Carta en Convia» en el pie, pequeño.

## Piezas (medidas reales, botón «Imprimir a tamaño real»)
- **A · Tarjeta de mesa** 10 × 14 cm (carpa o atril), QR de 5.6 cm, número de mesa al pie.
- **B · Calca redonda** 8 cm para la mesa: nombre en el arco superior, «MENÚ · MENU · ESCANEA · SCAN · NFC» en el inferior.
- **C · Tarjeta de barra** 5.5 × 8.5 cm (bloque de acrílico).

## Reglas
- El color del establecimiento va en la cabecera; **el QR solo lo toma si contrasta 7:1 o más con el blanco**; si no, se imprime en negro y se avisa.
- El texto sobre la cabecera cambia a negro si el color es claro (contraste 4.5:1).
- Un solo QR por establecimiento (el número de mesa es solo impreso): un cambio de menú no obliga a reimprimir.
- NFC: etiqueta pegada detrás del ícono del teléfono, grabada con la misma dirección.
- QR: corrección de errores M, zona de silencio de 4 módulos, módulos cuadrados; generado en el navegador con qrcode-generator 1.4.4 (MIT) desde cdnjs.

## Pendiente / supuestos
- La dirección corta «convia.mx/m/…» es provisional (dominio sin confirmar). En la demo el QR abre el menú publicado en vista de mesa (#qr) del restaurante o café de ejemplo.
- **Escaneo sin verificar en esta sesión**: no se pudo ejecutar aquí un lector de QR (código externo bloqueado). Verificar con un teléfono antes de imprimir.
- Logo propio del establecimiento: la demo usa monograma; en producción el negocio sube su logo.
- Publicado: https://claude.ai/artifact/9p4DZJEucazvmtx5ycK3gX. Uso: `python3 gen.py <carpeta de salida>`.
