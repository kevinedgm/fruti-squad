# Wireframing F1/F2

## Material

- Kit neutral `assets/wireframe-kit.css`: grises, una familia de sistema, radios y espacios fijos.
- Nada del design system del proyecto salvo `breakpoints`.
- Parte de `assets/wireframe-base.html`: cópialo como `index.html` de la ronda y el kit a `vendor/`, o inclúyelo inline si el artefacto debe abrirse suelto. Ya trae selector de espacio (compact/medium/expanded), panel de estados y notas.

## Jerarquía sin color

Solo grises del kit, una familia, formas simples; sin color, sombras decorativas ni ilustraciones. Tamaño, peso, espacio, agrupación y posición. El sólido oscuro (`.wf-btn--primary`) se reserva a **una** acción por vista. Estados de madurez o estado de negocio se distinguen por **forma + texto** (relleno, contorno, discontinuo, tachado), nunca por tono.

## Contenido

- Real o realista en cuanto la jerarquía dependa de él: nombres largos, números con formato, listas de 0, 1 y 200. Lorem ipsum solo donde no cambia nada.
- Cada pantalla responde: ¿qué necesita saber?, ¿qué necesita hacer?, ¿qué acción domina?, ¿qué resultado produce?
- Datos de ejemplo rotulados (`.wf-tag` "ejemplo" / "supuesto").

## Navegación

- Desde los destinos (frecuencia/urgencia), no desde un menú: ¿qué visita más, qué es urgente?
- Las acciones van en la pantalla, no como pestañas.
- Dónde estoy (título + breadcrumb), qué puedo hacer (acciones en contexto), cómo sigo, cómo regreso.
- **Volver** (historial), **Cancelar** (descarta cambios), **Cerrar** (oculta sin decidir) son tres cosas distintas.

## Acciones y estados

- **Una sola acción primaria por vista.** Nunca dos sólidos de igual peso en el mismo bloque; la destructiva, separada.
- Estados del brief (carga, vacío inicial y por filtros, error, sin permiso, sin conexión, contenido largo, destructiva) en el **panel de estados**, no en pantallas duplicadas.

## Por espacio

**Diseño por espacio, no por dispositivo.** Define una política `compact` / `medium` / `expanded` según el espacio disponible. Para cada modo: navegación, jerarquía, composición, densidad, overlays, acciones visibles, detalles que pasan a vista secundaria y teclado/foco. Considera orientación, pantalla dividida, zoom 200 %, área segura y teclado virtual. Tamaños de prueba = `breakpoints` del perfil; si no existen, 393 / 834 / 1440 como **referencia declarada**, nunca como equivalente obligatorio de dispositivos. Muestra **una tarea completa en cada modo**, no una captura estática.

| Modo | Ancho de referencia | Tendencias |
|---|---|---|
| compact | < 600 | Una columna, acción primaria persistente abajo, filtros a pantalla completa, tablas → bloques |
| medium | 600–1023 | Dos columnas cuando aportan, drawers laterales, navegación compacta |
| expanded | ≥ 1024 | Paneles persistentes, detalle junto a lista, densidad mayor |

Declara qué **conserva**, qué **cambia** y qué **se oculta** cada elemento.

**Técnica prevista** (se declara, no se implementa): CSS intrínseco y container queries para cambios locales. Una sola fuente de datos y una instancia de negocio: no dupliques formularios, estados ni operaciones entre teléfono y escritorio. (Con `vue-adaptive`: `references/vue-adaptive.md`.)

**Matriz de adaptación** obligatoria: elemento · compact · medium · expanded · motivo · técnica · impacto en foco y estado.

## Rondas

`<hub_root>/lab/<superficie>/rNN/` (o `docs/adaptive/<superficie>/rNN/` si no hay Hub). R2 va en `propuestas/`. Una ronda rechazada o cambiada materialmente crea `rNN+1`; nunca sobrescribas algo que el usuario ya evaluó. Durante el wireframe no se cambian reglas de negocio, rutas productivas ni dependencias.

## Anotaciones

`.wf-note` para decisiones, supuestos y referencias a la spec. Nunca uses color para anotar.
