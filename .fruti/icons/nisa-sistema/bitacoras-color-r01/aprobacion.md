# Bitácoras · color · aprobación r01

Fecha: 2026-11-05. Aprobó: usuario («aplica tus recomendaciones»).

Decisiones congeladas
1. «Completo» y «firmado» = `conforme` (#2E7D32 / soft #E3F1E4 / texto #1E5A22). El olivo #52660a queda descartado; el pera solo dice «en curso» o «urgente».
2. Lienzo = `bg` #F2F4F8 (sustituye #DDE3EC); las tarjetas se separan con borde y sombra.
3. Solo lectura = `surface-sunken` + `border-strong` + candado, igual que deshabilitado en color (sale el lila #F6F6FC).

Derivados de la regla (ya estaban en la propuesta)
- Botones de éxito (btn-success, btn-nn-success, nnd-btn-ok, iub-btn.success) pasan a `primary`: una sola acción primaria.
- Botón destructivo = `fuera` / `fuera-hover`. Validar sin degradado.
- Borde de campos = `border-control` (3.3:1).

Aplicado
- Design system NisaLab v3, versión 17 del artefacto FzzBwrjsBqAm4gdgcTduiV: tokens nuevos surface-2, primary-ink, primary-line, conforme-line, alerta-line, fuera-hover, fuera-line, log-*; README y lastChange.
- `bitacoras-color.css`: capa de variables + compatibilidad + 2.º paso (reglas con color fijo). Se pega al final del CSS de bitácoras.

Verificado: todas las variables usadas están definidas; Chromium resuelve los colores esperados en 8 elementos de prueba.
No verificado: el archivo dentro de la aplicación real (no tengo el repositorio de producción). Pendiente: revisión visual en bitácoras, en especial reglas con mayor especificidad o `!important` no listadas.
Fuera de alcance: fuente de datos (Google Sans Code vs IBM Plex Mono).
