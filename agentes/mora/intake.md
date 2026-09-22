# Intake — los datos exactos que mora pide en el primer uso

mora cura el Design Hub de un proyecto. Antes de tocarlo, mora necesita un **perfil**. mora **no** ronda el repo adivinando estructura ni inventa rutas — pide un conjunto fijo de datos en un formato específico y los mapea 1:1 al perfil.

mora comparte el perfil con `lima` y coco, así que el intake es: **el intake del architect, más un pequeño bloque `mora:`.**

## Cómo usa esto mora

1. En el primer uso en un repo, busca un perfil activo en `profiles/<project>.md` de la skill architect.
   - **Si existe**: reúsalo. Pide solo las adiciones `mora:` de abajo si faltan.
   - **Si no existe**: presenta el intake completo (campos del architect + bloque `mora:`), un solo mensaje, y espera.
2. Valida cada campo. Vuelve a pedir solo los campos que fallen. Los campos marcados `AUTO` pueden rellenarse inspeccionando el repo — muestra lo que encontraste para confirmar.
3. Mapea todo al perfil (los campos del architect vía el mapeo de su `reference/intake.md`; los campos `mora:` vía la tabla de abajo).
4. Confirma el perfil terminado con el usuario antes de tocar el Hub.

## Los campos del architect (reusar literalmente)

Usa el formulario exacto de `lima/reference/intake.md`. mora se apoya específicamente en: `hub_root`, `hub_language`, `registry_path` (derivado), `component_dir` (→ `production.component_layout`), `breakpoints`, `a11y_target`. También se beneficia de `design_system_name`.

## Las adiciones de mora (presentar esto literalmente)

```yaml
# === mora · documentation additions (append to the project intake) ===
doc_standard:      # OPTIONAL. Ruta al spec del estándar de doc (orden de secciones + regla de honestidad).
                   # Vacío => mora usa su orden canónico interno.
                   # p. ej. ".../lima/reference/component-documentation.md"

doc_shell:         # REQUIRED (o AUTO). La(s) hoja(s)/script(s) cuyas clases reales reutilizan las páginas.
                   # p. ej. ["design-hub/Design System/docs.css", "design-hub/Design System/docs.js"]

serve_command:     # OPTIONAL o AUTO. Cómo servir el Hub estáticamente para validar.
                   # Vacío => "python3 -m http.server 4321 --directory ."

coverage_script:   # OPTIONAL. Check de censo de que todo componente está documentado. AUTO | vacío.
                   # p. ej. "python3 design-hub/lab/scripts/coverage.py"

hub_preview:       # OPTIONAL. Cómo la Preview viva embebe el componente REAL (iframe a un harness).
                   # Vacío => espeja el CSS del componente, etiquetado como espejo.
                   # p. ej. "iframe http://localhost:5175/qa/<component>?raw=1"
```

## Formatos de campo (estrictos)

| Campo | Formato / valores permitidos | Si falta/es inválido |
|---|---|---|
| `doc_standard` | ruta del repo, o vacío | vacío → orden canónico interno de secciones (declarado) |
| `doc_shell` | lista de rutas reales del repo, o `AUTO` | `AUTO` → detecta el shell css/js del Hub + muestra; si no encuentra ninguno, mora señala que las páginas no tienen shell que reutilizar |
| `serve_command` | string de shell, `AUTO`, o vacío | vacío → `python3 -m http.server` |
| `coverage_script` | comando de shell, `AUTO`, o vacío | `AUTO` → detecta; vacío → cobertura reportada `manual` |
| `hub_preview` | string que describe el embed del harness, o vacío | vacío → espejo de CSS, etiquetado |

Ejemplos completos del bloque `mora:` (completo / sencillo / mínimo): [`examples/mora-block.example.md`](examples/mora-block.example.md).

## Mapeo Campo → perfil (bloque mora)

Estos aterrizan bajo una clave `mora:` en el mismo `profiles/<project>.md`:

| Campo del intake | Campo del perfil |
|---|---|
| `doc_standard` | `mora.doc_standard` |
| `doc_shell` | `mora.doc_shell` |
| `serve_command` | `mora.serve_command` |
| `coverage_script` | `mora.coverage_script` |
| `hub_preview` | `mora.hub_preview` |

Ver [profile-additions.md](profile-additions.md) para cómo se consume cada campo en el protocolo.

## Por qué un intake fijo

- Los campos del perfil son el contrato real de mora; pedirlos directo significa cero adivinanzas y cero deriva.
- Compartir el perfil del architect significa que un proyecto se describe **una vez** y la skill de diseño, coco y mora leen todos la misma verdad.
- `AUTO` deja que el repo responda las preguntas mecánicas (shell/rutas) mientras el humano posee las de juicio (estándar de doc, estrategia de preview).
