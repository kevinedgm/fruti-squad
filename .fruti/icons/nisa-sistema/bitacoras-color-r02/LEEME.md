# Bitácoras · color · r02 (sustituye a r01)

`python3 gen.py` → `propuesta.html` y `bitacoras-color.css` (capa + `overrides.css`).
Artefacto: https://claude.ai/artifact/FAPBW5p3TcAL686anyRhqj (misma URL que r01, ahora con r02).

Pedido: «solo los esenciales, básicos y semánticos; no generar colores de más».
Resultado: 17 colores, todos existentes en NisaLab v3; cero nuevos. Se retiraron del DS los 14 que r01 había agregado (versión 18 del artefacto FzzBwrjsBqAm4gdgcTduiV).
- Básicos (6): bg, surface, text, text-muted, border, border-control.
- Marca (4): primary, primary-hover, primary-soft, pera.
- Semánticos (7): conforme, conforme-soft, on-conforme-soft, alerta, alerta-soft, fuera, fuera-soft.
Única excepción con tono extra: on-conforme-soft, porque conforme sobre conforme-soft mide 4.4:1.
Se mantienen las decisiones aprobadas en r01: completo en verde, lienzo #F2F4F8, solo lectura gris con candado (ahora sobre bg: borde 3.0:1; sobre surface-sunken medía 2.9:1).
Cambios de forma: consola clara; encabezado y modales en azul sólido; píldoras sin borde; hover destructivo con anillo fuera-soft.
Verificado: variables definidas; Chromium resuelve los colores esperados. No verificado: dentro de la aplicación real.
