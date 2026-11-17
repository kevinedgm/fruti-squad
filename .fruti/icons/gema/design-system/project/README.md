GEMA (Gestión de Muestras y Análisis) es el sistema interno del laboratorio: registra las muestras que llegan, sus análisis, sus resultados, los informes y el cobro. La marca se resume en tres decisiones: el símbolo es la pantalla de un instrumento con el pico del resultado; el azul viene del navy de Nisa Nabani y su degradado solo vive en la marca; y la letra es Onest, la misma de SAM. La interfaz se construye con Grana; este sistema es la capa de marca y de dominio encima.

## Voz y contenido

- Español, segunda persona, frases cortas y verbos concretos: «Registrar muestra», «Asignar análisis», «Emitir informe».
- Mayúscula solo al inicio: «Resultados del día».
- Escribe valores y unidades como en el informe: `18.4 mg/L`, `7.21`, `196 mg/100 mL A.A.`; subíndices reales (DBO₅); punto decimal.
- Folios tal cual en `folio`: `M-2026-1184`.
- Los resultados se dicen como se dictaminan: «Cumple», «No cumple», «En análisis».
- Errores con causa y salida: «No se pudo emitir el informe: falta el resultado de pH. Captúralo y vuelve a intentar.»
- Sin emojis.

## Color

- Página en `surface`, tablas y tarjetas en `surface-raised`, hovers en `surface-sunken`; texto en `ink`, metadatos en `ink-muted`.
- `brand` es el color plano de la interfaz, siempre con `on-brand` (blanco): navy en claro, azul medio en oscuro. Una acción principal por vista.
- El degradado (`brand-grad-start` → `brand-grad-end`) solo va en superficies de marca: el pico del símbolo, el icono de la app y el panel de inicio de sesión. Nunca en botones, estados ni texto.
- Navy nunca en tema oscuro: mide 1.5:1 sobre negro.
- «Cumple» va en `ink` con ✓: no lleva color. «No cumple» va en `danger` con ✕. Así los dos dictámenes nunca se distinguen solo por tono (un verde y un rojo se confunden con daltonismo).
- `warning` marca muestras «Por vencer». Todo estado lleva palabra.
- En la app, `brand` entra en `--g-color-brand` de Grana y `on-brand` en `--g-color-on-brand`. El resto de la equivalencia con Grana está pendiente.

## Tipografía

- Onest (`sans`) en todo: `display` o `title` para la pantalla, `subtitle` para secciones, `body` para texto, `item-title` para el nombre de una muestra.
- Folios en `folio` y valores con unidad en `value` (JetBrains Mono, números tabulares, alineados a la derecha).

## Espacio, forma y profundidad

- Pasos de 4 px (`space-1` a `space-8`), radios `radius-sm`, `radius-md` y `radius-pill`, controles de `control-height`: todo heredado de SAM.
- Sin sombras: profundidad por superficies y `line`.

## Movimiento

- Solo para cambios de estado: un resultado nuevo aparece con un fundido de 150 ms. Con `prefers-reduced-motion`, sin animación.

## Símbolo y logotipo

- Símbolo «Pantalla + Resultado»: marco y señal en tinta; el pico del resultado en el degradado.
- Desde `symbol-min` (32 px) el grande; por debajo el chico (marco grueso, solo el pico del resultado).
- Logotipo: «GEMA» arriba y «Gestión de Muestras y Análisis» abajo. Horizontal en la barra de la app y documentos; vertical en portadas e inicio; compacto donde no cabe la definición.
- Como `<img>` usa las versiones «sobre-claro» o «sobre-oscuro».
- No deformar, no recolorear el pico, no usar degradado en botones.

## Iconografía

- Los iconos de interfaz los pone Grana; pendiente confirmar su familia.
- Notificaciones push: silueta blanca de una tinta con el pico calado (`notificacion-96.png`).

## Componentes

Botón, Estado, Fila de resultado y Barra de la app son componentes de dominio sobre Grana, con guía y vista previa en ambos temas.
