# Apollo · icono de app y favicon

Derivados de exportación de `../apollo.svg` con los hex de `project/tokens.json` del design system de Apollo (Órbita: void #070a14, ink #e8edf7, signal #22e4f5 · Día: void #f4f6fb, ink #0b1020, signal #00707f). Llevan colores fijos a propósito: fuera de la página no hay variables CSS. En la interfaz usa `../apollo.svg` (currentColor + `--uva-accent`).

| Archivo | Uso |
|---|---|
| `apollo-app-orbita.svg`, `apollo-app-1024.png`, `apollo-app-512.png` | icono de app (dock, instalador), tema Órbita, esquinas redondeadas |
| `apollo-app-dia.svg`, `apollo-app-dia-512.png` | variante Día, para fondos claros |
| `apollo-app-*-cuadrado.svg`, `apollo-pwa-512.png`, `apollo-pwa-192.png` | sin esquinas: iOS, Android y PWA las recortan (el icono está a 60 %, dentro de la zona segura de máscara) |
| `apple-touch-icon.png` | 180×180 para iOS |
| `favicon.svg` | pestaña del navegador: sigue el tema del sistema; nítido a cualquier tamaño (recomendado) |
| `favicon.ico`, `favicon-32.png`, `favicon-16.png` | respaldo para navegadores sin favicon SVG; a 16 px el satélite casi desaparece |

```html
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
```

```json
{ "name": "Apollo", "icons": [
  { "src": "/apollo-pwa-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable" },
  { "src": "/apollo-pwa-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" } ],
  "background_color": "#070a14", "theme_color": "#070a14" }
```

Estáticos: la ignición (el satélite que da la vuelta) solo existe en el SVG de interfaz.
