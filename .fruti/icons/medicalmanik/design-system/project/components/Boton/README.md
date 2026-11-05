# Boton

Botón: la acción principal es azul Manik en TODAS las apps, sin importar el color del producto. Aprobado 2026-11-05 (`../../controles-r01/`).

- **Variantes.** `primario` («manik» / «on-manik»), una por vista. `secundario` («surface», borde «line-control», texto «manik»). `terciario` (solo texto). `destructivo` (contorno y texto «error») para iniciar una acción que borra. `destructivo-confirmación` (relleno «error», blanco encima 5.07:1) SOLO dentro del diálogo que confirma. `icono` (44 × 44, «muted», con `aria-label`).
- **Estados.** Hover: «manik-hover» en el primario; «surface-soft» en secundario, terciario e icono; «error-soft» en el destructivo. Presionado: «surface-pressed» o sombra interior. Foco: anillo «focus» 2 px con 2 px de separación. Cargando: icono girando a la izquierda, mismo ancho, `aria-busy`, no se puede pulsar dos veces. Deshabilitado: «surface-soft», borde «line», texto «muted» (5.98:1), sin color de acción, `aria-disabled`.
- **Tamaños.** `control-height` 44 px en todo. `control-height-compact` 36 px solo en filas de tabla y barras de filtros.
- **El botón principal de un formulario nunca se deshabilita:** se pulsa y el formulario dice qué falta.
- Por qué no el color del producto: Farmacia, Compras y Grupos se parecen a éxito, aviso y error; un botón verde o rojo diría otra cosa. El mismo botón en todas las apps evita reaprender al cambiar de app.
- El consumidor provee: verbo + objeto, estado de carga y `aria-disabled`.
