# Project Knowledge Map — esquema v1

Semilla escribe JSON legible y estable. El objetivo es recuperación barata, no reproducir una base de grafos completa.

## index.json

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
    "orphans": "orphans.json"
  },
  "counts": {},
  "aliases": {}
}
```

## Regla de tamaño

Si un archivo especializado crece demasiado, particiónalo por módulo y actualiza `files`/índice. No existe premio por conseguir un JSON de 4 MB.
