# Fruti Squad · logotipo y tarjetas

Tipografía elegida (2026-10-08): **Sora** (SIL Open Font License). Nombre en peso 700, «for Kiro» en 500.

En los SVG el texto está convertido a trazos: se ven igual aunque Sora no esté instalada. Generador: `../ronda-3/logotipo.py`, que necesita fontTools, uharfbuzz y el archivo `Sora[wght].ttf` de google/fonts.

| Archivo | Uso |
|---|---|
| `fruti-squad-logotipo-oscuro.svg` | Icono + nombre, sobre fondo oscuro (núcleo lima) |
| `fruti-squad-logotipo-tinta.svg` | Igual, en una tinta (`currentColor`), para fondo claro |
| `fruti-squad-logotipo-kiro-{oscuro,tinta}.svg` | Con «for Kiro» debajo del nombre |
| `simbolo-oscuro.svg` | Solo el símbolo, sin cuadro, para fondo oscuro |
| `tarjeta-redes-1280x640.png` | Vista previa social de GitHub (Settings → Social preview) |
| `tarjeta-og-1200x630.png` | Open Graph para docs o web |

Evidencia: `evidencia-logotipos.png` muestra los logotipos en oscuro y en claro, a 80 y 28 px.

Para texto en la web:

```html
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;700&display=swap" rel="stylesheet">
```
