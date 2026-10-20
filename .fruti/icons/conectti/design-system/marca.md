# Marca

La identidad de Conectti nace del nombre: las dos t de «conectti» se unen en una sola barra. Esa barra es a la vez el enlace (conectar) y la marca de un instrumento calibrado (medir con precisión). No hay matraces ni gotas: el laboratorio se dice con exactitud, no con ilustración.

![Lámina: app icon, favicon y logotipo](/_blob/008d331d28d584ca1b2bb26a1c994749)

## Piezas

| Pieza | Uso | Archivo |
|---|---|---|
| Símbolo | Avatares, favicon grande, cabeceras compactas, 32px o más. | `simbolo.svg` · `simbolo-tinta.svg` (una tinta, `text`) · `simbolo-inverso.svg` (sobre `brand` o `brand-strong`) |
| Símbolo 16 | De 16 a 24px: trazos más gruesos y cola corta. Nunca escalar el símbolo normal por debajo de 32px. | `simbolo-16.svg` |
| Favicon | Cambia solo con `prefers-color-scheme`: cobalto sobre claro, blanco sobre oscuro. | `favicon.svg` |
| App icon | Bloque `brand` con la tt blanca y la barra en `#5FD6CF` (el `accent` no contrasta sobre cobalto). La versión cuadrada es la maestra; las plataformas aplican su máscara. | `app-icon.svg` · `app-icon-redondeado.svg` · `icon-512.png` · `icon-192.png` |
| Logotipo | Cabecera de la pantalla de acceso, documentos, informes. | `wordmark.svg` · `wordmark-tinta.svg` · `wordmark-inverso.svg` |
| Lockup | Símbolo + logotipo en horizontal; es la forma preferida cuando hay espacio. | `lockup.svg` · `lockup-inverso.svg` |

## Color

- Letras y fustes de la tt en `brand` (#1D52BB); barra y punto de la i en `accent` (#057F7D).
- Sobre fondos `brand` o `brand-strong`: letras en `on-brand` (blanco) y barra en `#5FD6CF`. Es el único valor de la marca que no es un token del sistema; existe porque `accent` sobre cobalto queda en 1.5:1.
- Una tinta: todo en `text`. Nunca en gris, nunca en degradado, nunca sobre fotografía sin un bloque de `surface` detrás.

## Espacio y tamaño

- Área de protección: la altura de la barra (el grosor del trazo de la t) alrededor de todas las piezas.
- Mínimos: logotipo 96px de ancho; lockup 120px; símbolo 32px; símbolo 16 de 16 a 24px.
- No se dibujan versiones nuevas de la tt: se usan los archivos. Cambiar el grosor, separar las t o quitar la barra rompe la marca.

## Dónde aparece

- Pantalla de acceso: lockup arriba a la izquierda, 34px de alto; el título sigue diciendo «Entra a Conectti» en texto.
- Barra superior de la aplicación: símbolo a 24px (`simbolo-16.svg`) junto al nombre en `title-2`, o el lockup a 28px si hay ancho.
- Informes y PDF: logotipo o lockup en `text` o en `brand`; nunca el app icon.
- Pestaña del navegador: `favicon.svg`; `icon-192.png` e `icon-512.png` en el manifest de la PWA.

![Pantalla de acceso con el lockup](/_blob/d50a84556a610a9793ede643a86c3291)
