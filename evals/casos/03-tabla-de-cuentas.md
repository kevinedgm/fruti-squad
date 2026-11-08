# Caso 03: tabla de cuentas con acciones

## Petición
`Diseña la tabla de cuentas pendientes de la recepción: muestra, cliente, monto, estado de pago; acciones por fila (pagar, adjuntar voucher, cancelar) y acciones masivas para las seleccionadas`

## Ruta esperada
Kiwi → Lima → Coco → Lima gate → Mora.

## Debe
- [ ] Acciones de fila al final de cada fila; acciones masivas aparecen al seleccionar, con el conteo.
- [ ] Cancelar con tratamiento de peligro y confirmación.
- [ ] Estado de pago con texto, no solo color.
- [ ] En compact, la fila pasa a bloque con dato principal arriba y acciones en menú.
- [ ] Encabezados de columna diferenciados; estados vacío y sin resultados con contenido propio.

## No debe
- [ ] Acciones de una fila en una barra global lejos de la fila.
- [ ] Desbordamiento horizontal en 390 px.
