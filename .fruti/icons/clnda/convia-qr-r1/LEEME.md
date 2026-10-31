# Convia · QR de mesa r1

Pedido del usuario (2026-10-31): identidad de los QR que el restaurante (o café) pone en sus mesas para ver el menú en Convia, con cámara o NFC. El establecimiento es el protagonista; Convia aparece discreto.

## Ajuste r1.1 (usuario: «se pierde el sello de Convia; que el QR esté integrado en la estrella»)
**La estrella pone la forma; el lugar pone el color.** El QR vive dentro de la estrella E1b de Convia (contorno dibujado a mano, sin deformar), pintada con el color del establecimiento y girada como sello; el QR va en un panel blanco que tapa el centro y deja ver las seis puntas. Medición: el hueco libre de la estrella es solo el 19 % de su ancho, por eso el QR va encima del centro y no dentro del hueco.

## Jerarquía
1. **El establecimiento**: cabecera con su nombre (o logo) y **su color**.
2. **Qué hacer**: «Escanea · Scan» y «Acerca tu teléfono · Tap your phone» (NFC), en español e inglés.
3. **El QR dentro de la estrella**: panel blanco, sin nada sobre los módulos.
4. **Convia** se reconoce por la forma de la estrella; al pie solo «Menú en Convia» / «Carta en Convia».

## Piezas (medidas reales, botón «Imprimir a tamaño real»)
- **A · Tarjeta de mesa** 10 × 14 cm (carpa o atril), QR de 3.3 cm dentro de la estrella, número de mesa al pie.
- **B · Calca estrella** 9.5 cm: el sticker es la estrella (silueta blanca de recorte con el contorno de color), QR y nombre del lugar al centro.
- **C · Tarjeta de barra** 5.5 × 8.5 cm (bloque de acrílico), QR de 2.5 cm (mínimo).
- Tamaños de QR medidos a tamaño real: 3.3 / 3.6 / 2.5 cm.

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
