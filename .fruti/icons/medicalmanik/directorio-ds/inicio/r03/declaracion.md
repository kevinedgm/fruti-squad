# Declaración de cumplimiento · Inicio Manik · r03

- **Ruta / fidelidad:** R1 · F0 (flujo.md) + F2 (kit neutral).
- **Estándares leídos:** brief r01 + delta r03, wireframing (kit), `.fruti/contracts/adaptativo.md`, WCAG 2.2 AA.
- **Artefactos:** `propuestas/index.html` (kit enlazado), `propuestas/publicar.html` (kit en línea + flujo).

## Comprobaciones ejecutadas
- `check_artifact.py index.html --fidelidad F2`: 0 errores, 0 avisos.
- Playwright, 393 / 834 / 1440 × 9 estados (primera visita, Guatemala, buscador, ubicación denegada, pocos médicos, carga, vacío, error, sin conexión): 0 desbordes, 0 controles menores de 24 px, 0 errores JS; máximo 1 acción primaria visible por vista.
- Revisión visual de «Resuelve tus dudas» a 393 y 1440 px.

## Comprobaciones NO ejecutadas
- Texto ampliado al 200 % y navegación con teclado completa.
- Lector de pantalla.
- Revisión visual completa a 834 y 1440 px (solo métricas automáticas).
- Términos de registro profesional y formato de moneda por país: no verificados con fuente oficial.

## Desviaciones
- Las cédulas con número cambian la anatomía de FichaMedico r03 C (aprobada): pendiente de aprobación antes de tocar DS y prototipo.
