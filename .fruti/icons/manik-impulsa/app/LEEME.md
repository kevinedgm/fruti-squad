# Manik Impulsa · iconos grandes (≥48 px)

Símbolo completo (globo + pulso con línea base) en `#6e6eb5` sobre blanco: 4.6:1, por encima del 4.5:1 recomendado. El favicon de 16–32 px es la versión simplificada de `../favicon/`.

| Archivo | Uso | Símbolo |
|---|---|---|
| `apple-touch-icon.png` (180) | pantalla de inicio de iPhone/iPad | 70 % del lienzo |
| `icon-192.png`, `icon-512.png` | PWA, `purpose: any` | 70 % |
| `icon-maskable-192.png`, `icon-maskable-512.png` | PWA en Android, `purpose: maskable` | 59 %, dentro del círculo seguro del 80 % |
| `manik-app.svg`, `manik-app-maskable.svg` | fuentes para reexportar | — |

Por qué fondo blanco opaco: iOS rellena la transparencia con negro, y Android recorta los maskable con la forma del launcher; sin fondo, el globo quedaría flotando sobre un color imprevisible. Comprobación: `evidencia-mascaras.png`.

## Código

```html
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
```

```json
"icons": [
  { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any" },
  { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any" },
  { "src": "/icon-maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable" },
  { "src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
]
```

## Decisiones

- **Aprobado (2026-10-05):** `#6e6eb5` para fondos claros en lugar de `#8f8fc6` (3.04:1).
