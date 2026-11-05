# Ecosistema Manik · formularios y diálogos · r01 (propuesta)

Pedido (2026-11-05): «las reglas para el diseño de formularios, composición de formularios en dialogs».
`python3 gen.py` → `formularios.html`. Reutiliza CSS, iconos y piezas de `../controles-r01/gen.py` (importado, no copiado); valores de `../design-system/project/tokens.json`.

## Contenido
1. Composición (10 reglas + formulario de ejemplo con resumen de errores).
2. Etiquetas, ayudas y errores (así / así no) y validación (6 reglas).
3. ¿Diálogo, panel o página? (por número de campos y necesidad de contexto).
4. Formularios en diálogos: anatomía, 8 reglas, diálogos reales (nueva cita con descartar, error de servidor y aviso; confirmación destructiva) y hoja inferior en celular.

## Decisiones nuevas [propuesta]
Contenedor por tamaño (confirmación / diálogo ≤ 6 campos / panel 7–12 / página > 12) · anchos 400/560/720 · hoja inferior < 640 px · clic fuera no cierra formularios · botón principal nunca deshabilitado · formulario máx. 640 px · fondo del diálogo tinta 40 % (no es token).
Hereda de controles-r01, sin aprobar: «(opcional)», deshabilitado, compacto.

## Huecos
El panel lateral no existe en el sistema (otra ronda). El fondo del diálogo no es token.

## Verificación
Playwright 1300 y 390 px: sin desbordes ni errores JS; sin IDs duplicados; todo campo con etiqueta; referencias aria válidas. Diálogo: foco al primer campo, Esc con cambios abre «¿Descartar?», error de servidor, cierre con aviso y foco de regreso al botón; confirmación con foco en «Cancelar». Único enlace < 24 px: en línea dentro de un párrafo (excepción de 2.5.8). El campo de fecha se ve en formato del navegador (en la prueba, inglés). No ejecutado: lector de pantalla real, zoom 200 %.
