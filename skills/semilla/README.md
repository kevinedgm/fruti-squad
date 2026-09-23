# 🌱 Semilla

**Project Mapper de Fruti Squad.**

Semilla construye y mantiene un mapa técnico persistente del proyecto para evitar que los agentes tengan que explorar todo el repositorio cada vez.

- `INIT`: reconocimiento inicial y grafo alcanzable.
- `QUERY`: recupera contexto pequeño para una tarea.
- `SYNC`: actualiza solo lo afectado por cambios.
- `DEAD-CODE`: reporta candidatos huérfanos con evidencia, sin borrar nada.

La base generada vive por defecto en `.fruti/knowledge/` (configurable con `knowledge_path` en `.fruti/semilla.json`).

Se escribe desde dos lados que conviven en el mismo `index.json`: el **CLI** produce la capa determinista (`graph.json`, `graph-orphans.json` — grafo de imports y reachability) y el **agente** produce la capa semántica (`modules.json`, `ui.json`, `data.json`, `api.json`, `flows.json`…). Cada uno mezcla lo suyo y conserva lo del otro; `init` no destruye un mapa escrito por el agente.

Semilla distingue entre **existir** y **estar en uso**. Un archivo sin referencias se marca `orphan`, no `unused`, hasta contar con evidencia suficiente.


## CLI

Después de instalar Fruti Squad:

```bash
fruti semilla init --scope src
fruti semilla map src/components
fruti semilla sync

fruti semilla on
fruti semilla off
fruti semilla status

fruti semilla relations src/components/AppointmentCard.vue
fruti semilla impact src/components/AppointmentCard.vue
fruti semilla why src/components/OldCard.vue
fruti semilla orphans
fruti semilla graph --scope appointments
```

Los comandos de consulta leen `graph.json`, así que necesitan un `init` previo. Aceptan una ruta exacta o un fragmento; si el fragmento coincide con varios archivos los lista, y si no coincide con ninguno falla con código 1 en vez de callarse.

### Qué pregunta responde cada uno

| Pregunta | Comando |
|---|---|
| ¿Quién usa este archivo? | `relations` → `incoming` |
| ¿Qué usa este archivo? | `relations` → `outgoing` |
| ¿Desde qué ruta es alcanzable? | `why` → imprime la cadena raíz → … → archivo |
| ¿Qué podría romper si lo modifico? | `impact` → cierre transitivo de dependientes |
| ¿Qué archivos están aislados? | `orphans` → `orphan` (sin referencias entrantes) |
| ¿Qué subgrafos están desconectados? | `orphans` → `unreachable` (se importan entre sí, sin camino desde una raíz) |
| ¿Por qué considera algo huérfano? | `why` → línea `reason` |

### Benchmark A/B — ¿de verdad ahorra exploración?

Semilla solo se justifica si reduce la exploración del agente. `fruti semilla test` mide eso con la misma tarea, commit, modelo y reasoning effort en dos condiciones.

**Qué mide quién.** El CLI no puede ejecutar al agente ni ver su sesión: es un script sin dependencias. Reparte así:

| Métrica | Quién la aporta |
|---|---|
| tiempo | el CLI, con su cronómetro |
| tool calls, archivos leídos, búsquedas, verification reads | el hook `PostToolUse` |
| input/output tokens | tú, al cerrar (`--input-tokens N`); el hook no los ve |
| respuesta correcta | tú, al cerrar (`--correct` / `--wrong`) |

Instala el hook una vez por proyecto y reinicia la sesión del agente:

```bash
fruti semilla hook install
fruti semilla hook status
```

Escribe en `.claude/settings.local.json`, que está gitignorado: queda en tu máquina.

**Condición A — Semilla OFF:**

```bash
fruti semilla test start localiza-estado-cita \
  --task "Localiza dónde se almacena el estado de una cita y qué archivos intervienen en su lectura y visualización" \
  --variant control
```

`test start` apaga Semilla, pone los contadores en cero e imprime el prompt exacto para pegar en una sesión limpia. Al terminar:

```bash
fruti semilla test end --correct --input-tokens 31420 --output-tokens 2000
```

**Condición B — Semilla ON:** lo mismo con `--variant semilla` (el `--task` ya queda guardado). El prompt cambia a *consulta el mapa primero, abre código solo para verificar*.

```bash
fruti semilla test report
```

```text
Task: localiza-estado-cita
                           OFF         ON          Δ
────────────────────────────────────────────────────
Tiempo                   48.2 s     11.7 s     -75.7%
Archivos leidos              24          4     -83.3%
Busquedas                    17          2     -88.2%
Tool calls                   31          7     -77.4%
Input tokens             31,420      8,910     -71.6%
Verification reads            0          3
Respuesta correcta            ✓          ✓
```

**Verification reads** es la métrica que más importa. El hook marca cuándo el agente leyó `.fruti/knowledge/` y cuenta los archivos que abrió *después*. Cero significa que Semilla se usó como sustituto de la fuente de verdad, no como índice; el comportamiento sano es mapa → dos o tres archivos concretos → confirmación.

**¿Vale la pena el invento?** Registra lo que costó construir el mapa y pregunta:

```bash
fruti semilla test overhead --init-tokens 82410 --sync-tokens 11204
fruti semilla test status
```

`Break-even` divide el costo del INIT entre el ahorro medio por tarea: cuántas tareas hay que hacer para que Semilla se pague. Si `Accuracy ON` baja respecto a `OFF`, el ahorro no cuenta — significa que el mapa está llevando al agente a respuestas peores.

Tareas sugeridas, de menos a más exigentes: localización simple (`¿dónde se guarda el nombre del usuario?`), valores admitidos, endpoint que modifica, pantalla que lo consume, impacto de cambiar un modelo, y código antiguo sin consumidores. Las primeras miden localización; las últimas miden si el grafo sirve de verdad.

### Benchmark manual

Si no quieres instalar el hook, el primitivo crudo sigue ahí y recibe todas las métricas a mano:

```bash
fruti semilla benchmark start locate-status --variant control
fruti semilla benchmark end --input-tokens 30000 --output-tokens 2000 --tool-calls 25
fruti semilla benchmark report
```

El cronómetro lo registra Semilla automáticamente. Los tokens y tool calls se pasan al cerrar porque cada host/modelo expone esas métricas de forma diferente.

Solo puede haber un benchmark abierto a la vez: `start` sobre uno activo falla en vez de pisarlo (`--force` lo descarta a propósito), y `end` cierra el activo y lo borra, de modo que un segundo `end` no duplica la corrida.

## Qué significa orphan

El mapper calcula relaciones entrantes/salientes y reachability desde raíces conocidas. También detecta **subgrafos desconectados**: archivos que se importan entre ellos pero a los que no llega ningún camino desde una raíz.

Esto es evidencia para revisión, no permiso automático para borrar archivos. Cargas dinámicas, auto-imports, registries y convenciones de framework pueden requerir verificación adicional.
