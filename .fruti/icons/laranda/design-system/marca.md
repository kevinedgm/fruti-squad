# Marca

La jacaranda sin la jota: misma floración, mismo violeta, nombre propio. El logo no ilustra un árbol: captura el instante de florecer.

![Lockup](/_blob/9cabaca099c454bb0284a894cb38bee7)

## Piezas

| Pieza | Uso | Archivo |
|---|---|---|
| Símbolo | 40 px o más: cabeceras, portadas, sellos grandes | `simbolo.svg` · `simbolo-oscuro.svg` (línea hueso, mancha lila) · `simbolo-tinta.svg` (una tinta) |
| Silueta | 16 a 32 px: favicon, avatar chico, chips de categoría, sello pequeño | `silueta.svg` · `silueta-oscuro.svg` · `favicon.svg` (cambia con el esquema) |
| App icon | PWA e iOS; `app-icon-maskable` con margen del 20 % para Android adaptativo | `app-icon.svg` · `app-icon-maskable.svg` · `icon-512.png` · `icon-192.png` |
| Avatar | Redes, recortado en círculo | `avatar.svg` |
| Wordmark | Documentos, folios, firmas; mínimo 80 px | `wordmark.svg` · `wordmark-oscuro.svg` |
| Lockup horizontal | Web, correo, cabecera de perfil; mínimo 120 px | `lockup-h.svg` · `lockup-h-oscuro.svg` |
| Lockup vertical | Social, stickers, carteles; mínimo 80 px | `lockup-v.svg` |
| Sello | La flor como estado: folio emitido, verificado | `sello.svg` · `sello-emitido.svg` |
| Bloom | Animación de 500 ms | `simbolo-bloom.svg` · `simbolo-bloom.gif` |
| Tarjeta de redes | 1200×630 | `tarjeta-redes.svg` |

## Anatomía

- Línea de tinta a mano (`ink-draw`), cinco lóbulos abiertos, grosor 3.2 en una caja de 128.
- Mancha plana en `brand`, desfasada 8 a la derecha y 7 hacia abajo. El desfase es fijo en todas las piezas y no se «corrige».
- El lóbulo superior derecho está separado 4 unidades y es el único en `accent`. Sin ese lóbulo, no es Laranda.
- Garganta vacía con anillo: el punto que se llena.

## Reglas

- Área de respeto: la altura del punto central, alrededor de toda pieza.
- Fondos permitidos: `bg`, `surface`, `surface-sunken`, `text` (oscuro) y `brand`. Sobre fotografía, con un bloque de `bg` detrás.
- Una tinta: todo en `text` (o en `bg` sobre oscuro). Nunca en gris, nunca en degradado.
- No cerrar los lóbulos, no quitar el separado, no rellenar la garganta, no la J de jacaranda, no explicar el nombre, no oro fuera de Reservar.

## Dónde aparece

- Cabecera de perfil público: lockup horizontal a 32 px de alto, arriba a la izquierda.
- Barra superior de la app: silueta a 24 px junto al nombre en `title-2`.
- Folio: wordmark en una tinta y la flor como sello; papel crema, tinta negra.
- Estados: la silueta en `brand` junto a «Perfil publicado», «Folio emitido», «Verificado».
