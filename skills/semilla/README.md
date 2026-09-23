# 🌱 Semilla

**Project Mapper de Fruti Squad.**

Semilla construye y mantiene un mapa técnico persistente del proyecto para evitar que los agentes tengan que explorar todo el repositorio cada vez.

- `INIT`: reconocimiento inicial y grafo alcanzable.
- `QUERY`: recupera contexto pequeño para una tarea.
- `SYNC`: actualiza solo lo afectado por cambios.
- `DEAD-CODE`: reporta candidatos huérfanos con evidencia, sin borrar nada.

La base generada vive por defecto en `.fruti/knowledge/`.

Semilla distingue entre **existir** y **estar en uso**. Un archivo sin referencias se marca `orphan`, no `unused`, hasta contar con evidencia suficiente.
