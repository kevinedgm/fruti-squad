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

### Benchmark A/B

Usa la misma tarea, commit, modelo y reasoning effort.

```bash
fruti semilla off
fruti semilla benchmark start locate-status --variant control
# ejecuta la tarea con el agente
fruti semilla benchmark end --input-tokens 30000 --output-tokens 2000 --tool-calls 25

fruti semilla on
fruti semilla benchmark start locate-status --variant semilla
# ejecuta exactamente la misma tarea en una sesión limpia
fruti semilla benchmark end --input-tokens 9000 --output-tokens 1800 --tool-calls 8

fruti semilla benchmark report
```

El cronómetro lo registra Semilla automáticamente. Los tokens y tool calls se pasan al cerrar porque cada host/modelo expone esas métricas de forma diferente.

Solo puede haber un benchmark abierto a la vez: `start` sobre uno activo falla en vez de pisarlo (`--force` lo descarta a propósito), y `end` cierra el activo y lo borra, de modo que un segundo `end` no duplica la corrida.

## Qué significa orphan

El mapper calcula relaciones entrantes/salientes y reachability desde raíces conocidas. También detecta **subgrafos desconectados**: archivos que se importan entre ellos pero a los que no llega ningún camino desde una raíz.

Esto es evidencia para revisión, no permiso automático para borrar archivos. Cargas dinámicas, auto-imports, registries y convenciones de framework pueden requerir verificación adicional.
