# icon-forge · uso

Icono de la skill Uva: «forja / construcción precisa de iconos». Monocromo, `currentColor`, trazo 1.5, 24×24, margen ≥2.

- **Decorativo (por defecto):** `aria-hidden="true"`; el texto de al lado da el nombre.
- **Botón solo con icono:** el nombre accesible va en el botón, no en el SVG (área mínima 44×44):
  ```html
  <button type="button" aria-label="Abrir Uva" class="btn-icono">
    <svg …icon-forge… aria-hidden="true" focusable="false"></svg>
  </button>
  ```
  El nombre describe el propósito («Abrir Uva»), no el dibujo («icono de racimo»).
- **Color:** se hereda solo inline o vía `<use>`. Como `<img>`, favicon o avatar, `currentColor` no se hereda y se pinta negro: para fondo oscuro, exporta una copia con `stroke="#fff"` (o PNG) solo para ese uso.
- **GitHub (avatar):** GitHub no acepta SVG como avatar; exporta PNG cuadrado (p. ej. 512×512) con margen.
- **Grosor:** `--uva-stroke` ajusta el trazo (familia a 1.5).
