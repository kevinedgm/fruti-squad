# SAM · plantillas de correo

HTML de tablas con estilos en línea (Gmail, Outlook, Apple Mail), tema claro, ancho máximo 560 px. Generadas con `gen.py`.

| Plantilla | Uso | Variables |
|---|---|---|
| `asignacion.html` | Te asignaron una actividad | folio, titulo, asignador, etapa, chip, meta, actividad_url |
| `etapa.html` | La actividad avanzó de etapa y te toca | folio, titulo, autor, etapa_anterior, etapa, chip, meta, actividad_url |
| `comentario.html` | Comentario nuevo | folio, titulo, autor, comentario, comentario_corto, chip, meta, actividad_url |
| `por-vencer.html` | Por vencer | folio, titulo, vence_corto, vence_largo, etapa, chip, meta, actividad_url |
| `vencida.html` | Vencida | folio, titulo, vencio_corto, vencio_largo, etapa, chip, meta, actividad_url |
| `reporte.html` | Reportes de atrasos diario (OR), semanal (WR) y mensual (MR) | titulo_reporte, resumen, n_atrasadas, n_nuevas, etiqueta_nuevas, n_personas, filas, reporte_url, rol |
| `invitacion.html` | Invitación al equipo | invitador, correo, enlace, vigencia |
| `recuperar.html` | Restablecer contraseña | correo, enlace, vigencia |

Todas: `logo_url` (PNG `sam-logo-correo@2x.png`, mostrado a 140 × 40; Gmail y Outlook no muestran SVG) y `preferencias_url`.
`chip` y `filas` son fragmentos HTML que arma el código (ver `chip()` y `fila()` en `gen.py`); el resto es texto y debe escaparse.
`muestras.json`: 10 muestras con datos ficticios.

Supuestos por confirmar: vigencia del enlace de invitación (72 h) y de recuperación (1 h); los reportes muestran las 4 actividades más atrasadas.
No verificado: render en clientes de correo reales (Outlook de escritorio, Gmail en Android).
