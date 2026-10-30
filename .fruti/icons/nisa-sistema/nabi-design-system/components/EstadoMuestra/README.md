# EstadoMuestra

Los tres datos de estado de una muestra, que cambian por separado. El personal de recepción se guía por el color: cada color de proceso ya está asociado a una acción, por eso se respeta. Lo que separa los grupos es la forma.

## Proceso · pastilla rellena
El círculo se llena por etapa (punteado, mitad, tres cuartos, lleno con palomita) como apoyo cuando no se distingue el color.

| Estado | Tokens | Cuándo |
|---|---|---|
| No ingresada | `muestra-no-ingresada` / `on-muestra-no-ingresada` | Recibida en ventanilla, sin folio interno. Acción: ingresarla. |
| En proceso | `muestra-en-proceso` / `on-muestra-en-proceso` | Con folio interno de laboratorio. Acción: capturar parámetros. |
| Generando informe | `muestra-generando-informe` / `on-muestra-generando-informe` | Parámetros requeridos capturados. Acción: generar el informe. |
| Terminada | `muestra-terminada` / `on-muestra-terminada` | Informe generado y enviado. |
| Cancelada | `muestra-cancelada` / `on-muestra-cancelada` | Muestra cancelada, sola o con toda su orden. Etapa final. |

Cancelada aplica a una muestra o a toda la orden de análisis. Si se cancela la orden, la orden y todas sus muestras llevan Cancelada; si se cancela una muestra, la orden dice «1 de N muestras cancelada» y sigue su curso. En la lista, el folio de una muestra cancelada va tachado y su pago se apaga a gris.

## Pago · etiqueta con contorno
Sin relleno; la moneda se llena (vacía, media, llena). Cortesía lleva regalo.

| Estado | Token | Cuándo |
|---|---|---|
| No pagada | `pago-no-pagada` | Sin pagos registrados. |
| Pago parcial | `pago-parcial` | Pagó una parte; queda saldo. |
| Pagada | `pago-pagada` | Saldo en cero. |
| Cortesía | `pago-cortesia` | Se procesa sin cobro, por decisión del laboratorio. |

## Prioridad · Urgente
Ficha `pera` con rayo junto al folio y franja `pera` de 4 px a la izquierda de la fila. No usa rojo (ya es Cancelada y No pagada). Texto `on-pera` 7.8:1.

## Reglas
1. Proceso, pago y urgencia nunca comparten forma: pastilla rellena, etiqueta con contorno, ficha sólida.
2. Un color de estado significa la misma acción en toda la aplicación.
3. Siempre ícono + palabra; el color nunca es la única señal.
4. Los colores de área (`area-*`) nunca aparecen en tablas.
5. El consumidor provee: estado de proceso, estado de pago, si es urgente y, si aplica, quién y cuándo cambió el estado.

## Incógnitas
- ¿Una orden cancelada se puede reabrir?
- ¿Qué pasa con lo ya pagado de una muestra cancelada?
