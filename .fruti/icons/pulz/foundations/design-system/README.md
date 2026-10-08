PULZ registra y traza la producción de mezcal en el palenque: del maguey al granel. Una PWA que se usa 60 % en el teléfono, 30 % en escritorio y 10 % en tablet, muchas veces al sol, con una mano y con prisa. Todo lo que sigue sale de la identidad de 2026-10-08: la Z del trasiego, el añil y Unbounded.

## Principios

1. **Todo es lote, recurso y movimiento.** Un lote pasa de un tanque a otro; la interfaz lo muestra como el logo: algo se vacía de un lado y se llena del otro.
2. **Un color significa una sola cosa.** `anil` es «esto se puede tocar o está seleccionado»; `pericon` es expresión; los estados tienen sus propios tintes.
3. **Se lee al sol.** Contraste mínimo 4.5:1 en texto, cero con raya, cifras alineadas, controles de 48 px con el dedo.
4. **El escritorio tiene diseño propio.** No es el teléfono estirado: tablas completas, maestro y detalle a la vez.

## Voz y texto

- Habla de tú, en presente y en activa: «Registra la medición», «Falta la medición de hoy: regístrala para seguir».
- Nombra las cosas como en el palenque: lote, tina, tanque, horno, tahona, °Brix, trasiego. Nunca «ítem», «registro de entidad» ni jerga de base de datos.
- Un botón dice exactamente lo que pasa: «Registrar medición» y después «Guardado».
- Mayúscula solo al inicio y en nombres propios. Sin emoji.
- Las fechas van en español corto: «martes 8 oct», «07:40».

## Color: Tintes de Oaxaca

Dos colores de identidad y tres de estado, todos tintes naturales de Oaxaca, sobre neutros fríos.

- Pinta el fondo con `canvas` y las tarjetas con `surface`; separa con `line`, no con sombra. `shadow-sheet` solo en hojas y menús que flotan.
- Escribe en `ink`; lo secundario en `muted`. Ambos pasan 4.5:1 sobre `canvas` y `surface` en los dos temas.
- **Marca, `anil`:** acción principal, fila seleccionada, enlace, destino activo de la navegación. Texto encima en `on-anil`. Al pulsar, `anil-strong`. Es también el `focus`.
- **Acento, `pericon`:** solo como relleno con `on-pericon` encima: la franja de «Hoy», la variación de una cifra («−1.4 desde ayer»), un momento destacado. Nunca como texto sobre `canvas`: da 1.6:1. Nunca en iconos.
- **Estados:** `verde` = listo, `cempasuchil` = revisar, `grana` = falta algo o error. Cada uno con su `-soft` de fondo para chips y avisos, y siempre con una palabra: nada depende solo del color. El aviso es naranja para no confundirse con el acento.
- Las etiquetas de estado se prueban en escala de grises: si no se distinguen, les falta texto o icono.
- Los campos llevan borde `control` (≥3:1); `line` es solo decorativa.
- El tema oscuro no invierte: cada tinte tiene su propio valor medido. Se aplica con `prefers-color-scheme: dark` salvo `data-theme="light"`, o manualmente con `data-theme="dark"`.
- Pendiente: paleta para gráficas de varias series.

## Tipografía

- Toda la interfaz en la familia `ui` (Atkinson Hyperlegible Next): `body`, `body-sm`, `label`, `caption`, `data`. Diseñada para baja visión; en el campo, equivale a leer al sol.
- Las cifras comparables (tablas, mediciones) usan `data` con `font-variant-numeric: tabular-nums`. El cero lleva raya: 0 y O no se confunden en una medición.
- La familia `display` (Unbounded, la del logo) solo en `display`, `title-lg`, `title` y `title-sm`: títulos y la cifra protagonista. Nunca en párrafos, controles ni por debajo de 17 px.
- Una sola `display` por pantalla.

## Geometría

- Espaciado en pasos de 4: `space-1` a `space-16`. Margen lateral del teléfono `space-4`.
- **El alto de un control lo decide la entrada, no el ancho.** Con el dedo (`pointer: coarse`): `size-control` 48, chips `size-tag` 32, filas `size-row` 48, acción principal del teléfono `size-field-action` 56. Con ratón (`pointer: fine`): 40, 28 y 40. Una tablet conserva los tamaños del dedo aunque su pantalla sea grande.
- **Radio = ¼ del alto**, como la barra de la Z (12 de alto, radio 3): `radius-control` 12 para 48, `radius-control-fine` 10 para 40, `radius-field` 14 para 56, `radius-tag` 8 para 32.
- Las superficies llevan `radius-surface` 16, fijo y mayor que el de lo que contienen.
- `radius-pill` solo para el interruptor y los avatares de empresa.
- Mínimos: `size-touch-min` 44 con el dedo, `size-pointer-min` 24 con ratón.

## El tanque

La barra de la Z convertida en componente: una barra `ink` de `size-tank` 12 con `radius-tank` 3, y el nivel en `anil` 3.5 px por dentro. Muestra el nivel de una tina o el avance de un lote. Se llena desde la izquierda con la curva «llenar» y nunca rebota. Es donde la identidad aparece dentro de la app, no solo en el logo.

## Marca blanca

En el portal de cada palenque (`pulz.mx/e/<slug>`) manda la marca de la empresa. PULZ aparece solo como la firma «hecho con PULZ» (assets/Marca), cuya diagonal y lote toman el color de la empresa con `--pulz-color`. Si ese color no llega a 3:1 sobre el fondo, la firma se queda en `ink`. El wordmark grande nunca va dentro de un portal.
