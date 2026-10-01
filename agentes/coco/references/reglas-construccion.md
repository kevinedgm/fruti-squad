# Reglas de construcción (Paso 4) y checklist de aceptación (Paso 5)

Todo valor concreto (colores, tipografía, radios, iconos, stack, targets) sale del **perfil activo**: aquí solo hay reglas, nunca valores.

## Sistema

- **Reutiliza el sistema real.** Consume los tokens (`truth_sources`) y los componentes (`component_layout`) que declara el perfil. En prototipos del Hub, reutiliza la hoja de estilos y el shell del Hub; **nunca** recrees ni «adaptes» el sistema en paralelo.
- Un componente de dominio nuevo se construye **con los tokens del sistema** y se documenta como artefacto en el Hub (página viva + entrada en el registry) según el estándar de documentación.

## Color, tipografía, geometría e iconografía

- **Ley de color (dura) = `color_law` del perfil.** No hay hexes en este agente. Regla universal: un color de acción reservado a su acción; un color de foco/acento; un color de peligro solo para error/destructivo; lo que no es acción ni estado es tinta sobre superficie; la sombra indica elevación, nunca decora. Los roles y hexes concretos los da `color_law`.
- **Tipografía = `type_law` del perfil.** Una familia base en todo el sistema; a lo sumo una de display para marca. Números tabulares donde comparen. Tamaños en `rem` (escalan al 200%).
- **Geometría:** usa la escala de radios del perfil/tokens. Máximo tres radios visibles por pantalla.
- **Iconografía = `icon_library` del perfil.** Un solo set, trazo y viewBox coherentes. Nunca mezclar sets, rellenos o emojis. Un concepto, un icono. (Si hace falta un icono que no existe: uva.)

## NUNCA

`:root` local o paleta paralela; hex/radio/sombra/duración a mano existiendo token; una familia tipográfica extra; iconos fuera del set del perfil o rellenos si el set es de trazo; otro shell/navbar/footer; modo oscuro sin solicitud; gradientes decorativos, glass sin función, sombras de color, bordes gruesos; `!important`; `transition: all`; `outline: none` sin reemplazo; hero/tarjeta gigante con tres datos en pantalla de trabajo; spinner a pantalla completa; scroll horizontal en el cuerpo; volcar campos de la API «porque están».

## Contenido

Botones verbo + sustantivo; **una** primaria por vista; máximo dos acciones visibles por fila/tarjeta (el resto a menú); etiqueta arriba del campo; validación al salir (`blur`); error con causa y solución; estado nunca solo por color (icono + texto); tabla para registros comparables, tarjetas solo para contenido heterogéneo o cuando la imagen aporta; dato derivado antes que dato crudo; vocabulario del dominio; datos de ejemplo realistas e identificados como tales.

## Estados obligatorios en el prototipo

Carga (esqueleto con la misma huella), vacío con acción, error con reintento, sin permiso, éxito con texto, texto largo, 0/`null`.

## Adaptación real por rango (no escalar)

Amplio / medio / compacto / móvil reciben composición propia; se declara qué cambia y por qué. Targets táctiles según `a11y_target`. Prefiere container queries cuando la pieza deba ser correcta en cualquier grid.

## Producción (R3)

El stack real del perfil (`production.known_stack`), consumiendo los tokens reales. Acciones = `<button>`; navegación = `<a>`/enlace del router; nunca anides interactivos. Lo aprobado queda **congelado**: anatomía, orden, densidad, acciones, estados, responsive.

## Accesibilidad frente al mockup

**Cuando el mockup choca con el estándar de accesibilidad, gana el estándar.** Controles con el target mínimo y contraste del perfil aunque el mockup muestre menos; la densidad se recupera en tipografía, interlínea y padding, y se declara en las Notas.

## Checklist de aceptación (Paso 5)

Recorre la checklist de aceptación del estándar: idea principal glanceable · móvil+escritorio · targets del perfil · **todos** los estados · contraste del perfil · estado con texto+ícono · teclado + foco visible · semántica + aria · reduced-motion + forced-colors · copy claro · tokens del sistema · i18n/RTL con propiedades lógicas · reutiliza patrones.

Verifica que **ningún antipatrón** esté presente: info repetida en el mismo bloque; barra de % para conteos pequeños; `aria-label` de contenedor que repite el texto de dentro; dos acciones compitiendo como principal; control sin dato que lo sustente; reglas de negocio en la presentación; tokens inventados existiendo equivalentes.
