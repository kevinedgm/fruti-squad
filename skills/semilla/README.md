# 🌱 Semilla

**Project Mapper de Fruti Squad.**

Semilla construye y mantiene un mapa técnico persistente del proyecto para evitar que los agentes tengan que explorar todo el repositorio cada vez.

- `INIT`: reconocimiento inicial y grafo alcanzable.
- `QUERY`: recupera contexto pequeño para una tarea.
- `SYNC`: actualiza solo lo afectado por cambios.
- `DEAD-CODE`: reporta candidatos huérfanos con evidencia, sin borrar nada.

La base generada vive por defecto en `.fruti/knowledge/`.

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

## Qué significa orphan

El mapper calcula relaciones entrantes/salientes y reachability desde raíces conocidas. También detecta **subgrafos desconectados**: archivos que se importan entre ellos pero a los que no llega ningún camino desde una raíz.

Esto es evidencia para revisión, no permiso automático para borrar archivos. Cargas dinámicas, auto-imports, registries y convenciones de framework pueden requerir verificación adicional.
