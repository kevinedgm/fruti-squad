# Project Knowledge Map — esquema v1

Semilla escribe JSON legible y estable. El objetivo es recuperación barata, no reproducir una base de grafos completa.

El identificador de schema es la cadena literal `fruti-semilla/v1`.

## index.json

Archivo compartido entre las dos capas. Las claves de nivel superior (`project`, `stack`, `roots`, `counts`, `aliases`) y las entradas semánticas de `files` las escribe el agente. La sección `graph` y las entradas `files.graph` / `files.graph_orphans` las escribe el CLI, **mezclándolas**: quien escriba una capa conserva la otra.

```json
{
  "schema": "fruti-semilla/v1",
  "project": "example",
  "verified_commit": null,
  "stack": [],
  "roots": [],
  "files": {
    "modules": "modules.json",
    "entrypoints": "entrypoints.json",
    "ui": "ui.json",
    "data": "data.json",
    "api": "api.json",
    "flows": "flows.json",
    "orphans": "orphans.json",
    "graph": "graph.json",
    "graph_orphans": "graph-orphans.json"
  },
  "counts": {},
  "aliases": {},
  "graph": {
    "generated_at": "2026-01-01T00:00:00.000Z",
    "verified_commit": "abc123",
    "scope": "src",
    "init_scope": "src",
    "roots": ["src/main.js"],
    "counts": { "active": 68, "orphan": 2 }
  }
}
```

## graph.json — capa determinista

Lo produce el CLI. Un nodo por archivo de código dentro del scope, sin semántica de dominio:

```json
{
  "schema": "fruti-semilla/v1",
  "generated_at": "2026-01-01T00:00:00.000Z",
  "verified_commit": "abc123",
  "scope": "src",
  "roots": ["src/main.js"],
  "nodes": {
    "src/components/AppointmentCard.vue": {
      "path": "src/components/AppointmentCard.vue",
      "kind": "ui",
      "outgoing": ["src/stores/appointments.js"],
      "incoming": ["src/views/AppointmentView.vue"],
      "status": "active",
      "confidence": "high"
    }
  }
}
```

`status` aquí solo admite `active`, `orphan` y `unreachable`: es reachability por imports estáticos, nada más. Los estados ricos del SKILL.md (`dynamic`, `test-only`, `deprecated`…) pertenecen a la capa semántica, que puede corregir al grafo cuando tiene evidencia de carga dinámica.

`scope` es el alcance del grafo actual; `init_scope` es el del último `init`. Se separan para que un `map <subárbol>` acotado no deje a `sync` reconstruyendo sobre ese subárbol para siempre.

`graph-orphans.json` es el subconjunto `orphan` + `unreachable` con el mismo formato de nodo.

## Regla de tamaño

Si un archivo especializado crece demasiado, particiónalo por módulo y actualiza `files`/índice. No existe premio por conseguir un JSON de 4 MB.
