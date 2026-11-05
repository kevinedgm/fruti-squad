# Ecosistema Manik · botones, campos y controles · r01 (aprobada 2026-11-05)

Pedido (2026-11-05): «la familia de botones, inputs y de control para todas las aplicaciones del ecosistema Manik para que se homogenicen todas».
`python3 gen.py` → `controles.html`. Valores leídos de `../design-system/project/tokens.json`; ningún color nuevo.

## Brief
- Usuario: quien diseña o programa cualquiera de las 7 apps (Expediente, Agenda, Compras, Farmacia, Impulsa, Grupos, Administración).
- Pregunta de diseño: ¿qué controles comparten todas, en qué estados, y qué cambia por app? Respuesta: solo el sello y el nombre.
- Supuesto: el directorio para pacientes queda fuera (tiene su familia en píldora).
- Ruta R1, fidelidad F3 con el sistema real.

## Contenido
Ejemplo «Nueva receta» que cambia de app; botones (principal, secundario, terciario, destructivo, confirmación destructiva, solo icono) × 6 estados y tamaño compacto; campos (texto, número con unidad, lista) × 6 estados; casilla, opción única, interruptor, control segmentado, chip de filtro, buscador, área de texto.

## Decisiones nuevas [propuesta, sin aprobar]
Compacto 36 px solo en tablas y filtros · deshabilitado = surface-soft + line + muted (sin color de acción) · hover/presionado con surface-soft/surface-pressed/manik-hover/error-soft · cargando con icono girando y aria-busy · destructivo en contorno, sólido solo al confirmar · marcar «(opcional)» y no lo obligatorio · hover de campo con borde muted · casilla/opción/interruptor de 20 px en fila de 44.

## Verificación
Playwright 1300 y 390 px: sin desbordes ni errores JS; sin IDs duplicados; todo control con etiqueta; aria-describedby válidos; ningún control < 24 px. Interacción: error de dosis > 100 con aria-invalid, cambio de app, botón cargando. No ejecutado: lector de pantalla real, zoom 200 %.

## Pendiente tras aprobación
Llevar al sistema de diseño (Boton, Campo y componentes nuevos), al manual (Superficies e interfaz) y decidir si el directorio adopta deshabilitado y semánticos.

## Aprobación (2026-11-05)
Aprobada por el usuario («sí, apruébalas y llévalas al design system y al manual»). Integrada al sistema de diseño del Ecosistema (versión 8) con `../design-system/controles_formularios.py` y resumida en el manual (`../manual-marca/`, sección Superficies e interfaz).
