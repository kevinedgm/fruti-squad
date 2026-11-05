# Bitácoras · propuesta de color · r01

`python3 gen.py` → `propuesta.html`. Artefacto: https://claude.ai/artifact/FAPBW5p3TcAL686anyRhqj
Insumo: CSS de producción de bitácoras pegado por el usuario (no se guarda en el repo; gen.py conserva solo el inventario de valores).
Base: design system NisaLab v3. Aprobada el 2026-11-05 (ver aprobacion.md); tokens ya aplicados al DS (versión 17).

Hallazgos: 5 capas de variables con valores distintos; éxito en olivo derivado del pera (#52660a); borde de campos 1.4:1 (pide 3:1); encabezado de lista 4.4:1; extremos claros del degradado de Validar; etapa de consola 3.8:1.
Propuesta: una capa `--nn-*` con nombres de v3 + borde de píldoras, hover destructivo y consola oscura; capa de compatibilidad para nombres viejos.
Decisiones abiertas: (1) completo verde vs olivo, (2) lienzo #F2F4F8 vs #dde3ec, (3) solo lectura gris con candado vs lila.
Fuera de alcance: fuente de datos Google Sans Code vs IBM Plex Mono en v3.
Entregable: `bitacoras-color.css` (generado por gen.py desde la capa + `overrides.css`).
