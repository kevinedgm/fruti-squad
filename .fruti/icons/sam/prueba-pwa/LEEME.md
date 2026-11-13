# SAM · página de prueba instalable

PWA mínima para validar en dispositivos reales los iconos de la marca (`../final/`): pestaña, instalación, icono en la pantalla de inicio, pantalla de carga y notificación push. No es la aplicación.

Contenido: `index.html`, `manifest.webmanifest`, `sw.js` (service worker mínimo: instalación y notificación de prueba) e `iconos/` (copias de `../final/`; si cambian los finales, volver a copiarlos).

## Cómo abrirla
- **Computadora:** `python3 -m http.server 8765` dentro de esta carpeta y abrir `http://localhost:8765` (localhost cuenta como seguro, se puede instalar).
- **Celular:** necesita HTTPS con certificado válido. Cualquier hosting estático sirve (por ejemplo GitHub Pages o Netlify). Un artifact de claude.ai no sirve: no admite service workers ni instalación.

## Verificado (2026-11-13, Chromium de Playwright en localhost)
Service worker activo, manifest sin errores, `Page.getInstallabilityErrors` vacío, sin errores de JavaScript.

## No verificado
Instalación real en Android e iPhone, máscara circular del icono adaptable, icono pequeño de la notificación y favicon SVG en Safari.
