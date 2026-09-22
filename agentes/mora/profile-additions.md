# Adiciones al perfil para mora

mora reutiliza el **mismo perfil de proyecto** que la skill `lima` y coco (`profiles/<project>.md`: `name`, `design_system`, `hub_root`, `hub_layout`, `registry_path`, `production.*`, `breakpoints`, `a11y_target`). **No** los duplica.

Encima de ese perfil, mora lee un pequeño bloque `mora:` para las cosas que una *curadora de documentación* necesita. Si un campo está ausente, mora cae a un default razonable y lo dice en su declaración de cumplimiento.

## El bloque `mora:` (añadir al perfil activo)

```yaml
mora:
  # El estándar de documentación: orden de secciones + regla de honestidad para una página
  # viva de componente. Apunta a un archivo de spec, o déjalo vacío para usar el orden interno de mora.
  doc_standard:     # p. ej. ".../lima/reference/component-documentation.md" | vacío

  # El shell del Hub: la(s) hoja(s)/script(s) cuyas clases reales toda página debe
  # reutilizar (nunca inventar un sistema de estilos paralelo). Lista los archivos.
  doc_shell:        # p. ej. [ "design-hub/Design System/docs.css", "design-hub/Design System/docs.js" ] | vacío

  # Cómo se sirve el Hub estáticamente para validar (una página abierta con file:// pierde el shell).
  serve_command:    # p. ej. "python3 -m http.server 4321 --directory ." | vacío (default: python3 http.server)

  # Check de cobertura/censo: confirma que todo componente está documentado en el Hub.
  coverage_script:  # p. ej. "python3 design-hub/lab/scripts/coverage.py" | AUTO | vacío

  # Cómo la Preview viva embebe el componente REAL (iframe a un harness corriendo), si lo hay.
  hub_preview:      # p. ej. "iframe a http://localhost:5175/qa/<component>?raw=1" | vacío (usa espejo de CSS)
```

## Qué activa cada adición en el protocolo

| Campo de mora | Se usa en | Efecto |
|---|---|---|
| `doc_standard` | Paso 3 + Paso 4 | Orden de secciones, shell de 3 zonas, regla de honestidad, primitivas de doc. Vacío → orden canónico interno de mora. |
| `doc_shell` | Paso 3 + Paso 5.1 | Las clases reales que toda página reutiliza; el paso 5 verifica que las clases usadas existen en estos archivos. |
| `serve_command` | Paso 5.1 | Sirve el Hub para verificar HTTP 200 + que el shell resuelve. Vacío → `python3 -m http.server`. |
| `coverage_script` | Paso 1.4 + Paso 5.2 | Corre el censo (todo componente documentado). Vacío → mora reporta cobertura como `manual`. |
| `hub_preview` | Paso 4 (Preview/Playground) | Cómo una página muestra el componente real. Vacío → espeja el CSS del componente, etiquetado como espejo. |

## Verdad compartida (del perfil base)

- `hub_root` + `hub_layout` → dónde vive el Hub y su taxonomía.
- `registry_path` → la fuente de `status/version/props/events/consumers/QA` que refleja una página.
- `production.component_layout` → el código real contra el que mora contrasta las páginas.
- `breakpoints` → los viewports que documenta la sección Responsive.
- `a11y_target` → la barra de accesibilidad que refleja la sección Accessibility.

## Regla de honestidad

Todo check que mora no pueda correr (sin `coverage_script`, Hub no servible, harness ausente) se reporta como `manual` o `no se ejecutó` en la declaración de cumplimiento — nunca se pasa en silencio. mora refleja el sistema; nunca inventa documentación para rellenar un hueco.
