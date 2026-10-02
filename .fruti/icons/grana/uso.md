# Grana · logo

**Concepto:** una gota de tinte que es la cochinilla (cuerpo con bandas, antenas en la punta, patitas). La forma es fija; el color lo pone el tema, como en la librería.

## Archivos

| Archivo | Para qué |
|---|---|
| `grana.svg` | Logo completo (≥ 32 px): docs, README, cabecera, redes |
| `grana-favicon.svg` | Favicon y tamaños ≤ 24 px: sin patitas (a 16 px son ruido) |
| `favicon-32.png` | Respaldo para navegadores sin favicon SVG |
| `icon-192.png`, `icon-512.png` | Manifest de PWA (fondo transparente) |
| `apple-touch-icon.png` | iOS (180 px, fondo blanco: iOS no admite transparencia) |
| `muestra.html` | El logo con el nombre y el lema, en claro, oscuro y en varios temas |

## Color: lo pone el tema

El logo lee `--grana-color`. Si no está definido, usa el carmín de la grana: en pantallas Display P3 `color(display-p3 .62 .05 .2)` y en las demás `#a3123a`.

```css
:root { --grana-color: var(--gr-color-brand); }   /* el mismo token que colorea tus componentes */
```

Así el logo y los componentes cambian de color juntos: si un proyecto pone su marca en azul, el logo de Grana en su documentación sale azul.

## En Vue

Inline (hereda `--grana-color` del tema):

```vue
<template>
  <span class="gr-logo" v-html="granaSvg" />
</template>
<script setup>
import granaSvg from './grana.svg?raw'
</script>
```

Como `<img src="grana.svg">` también funciona, pero **no hereda** `--grana-color` (una imagen no ve el CSS de la página): sale siempre en carmín.

## Favicon

```html
<link rel="icon" href="/grana-favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

## Accesibilidad

El SVG lleva `role="img"` y `aria-label="Grana"`. Junto al nombre escrito («grana»), ponle `aria-hidden="true"` para que no se lea dos veces.

## Reglas de la marca

- No cambies la forma ni el número de bandas; cambia solo el color (`--grana-color`).
- Debajo de 32 px usa `grana-favicon.svg`.
- Deja un margen libre alrededor de al menos ¼ del tamaño del logo.
