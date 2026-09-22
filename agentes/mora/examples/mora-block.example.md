# Ejemplo — el bloque `mora:` del perfil

El bloque `mora:` le dice a mora **cómo documentar el Hub de tu proyecto**: qué estándar de secciones seguir, qué shell (css/js) reutilizan las páginas, cómo servir el Hub para validarlo, cómo censar cobertura y cómo mostrar una preview real del componente.

**Todos los campos son opcionales.** Lo que dejes vacío, mora lo resuelve con un default y lo marca como "manual" en su reporte — nunca lo pasa en silencio.

| Campo | Qué es | Si lo dejas vacío |
|---|---|---|
| `doc_standard` | ruta al spec de orden de secciones + regla de honestidad | mora usa su orden canónico interno |
| `doc_shell` | css/js del Hub cuyas clases reales reutilizan las páginas | mora avisa que no hay shell (riesgo de páginas sin estilo) |
| `serve_command` | cómo servir el Hub estáticamente para validar | `python3 -m http.server` |
| `coverage_script` | censo: que todo componente esté documentado | cobertura reportada como `manual` |
| `hub_preview` | cómo la Preview embebe el componente REAL | espeja el CSS del componente, etiquetado como espejo |

---

## Ejemplo A — proyecto con Hub propio y harness de QA (lo más completo)

```yaml
mora:
  doc_standard: skills/lima/reference/component-documentation.md
  doc_shell:
    - design-hub/docs.css
    - design-hub/docs.js
  serve_command: "python3 -m http.server 4321 --directory ."
  coverage_script: "python3 design-hub/lab/scripts/coverage.py"
  hub_preview: "iframe http://localhost:5173/qa/<component>?raw=1"
```

**Qué haría mora con este bloque** (documentación de máxima fidelidad):
- ✅ Ordena cada página con el estándar de `doc_standard` (Overview→Preview→…→History) — todas se ven parte del mismo set.
- ✅ Reutiliza las clases reales de `docs.css`/`docs.js`; las páginas salen **con estilo** y en el paso de verificación comprueba que ninguna clase usada sea inventada.
- ✅ En la sección **Preview** embebe el **componente REAL** vía iframe al harness (`/qa/<component>`), no una maqueta.
- ✅ Sirve el Hub con `serve_command` para validar HTTP 200 + que el shell resuelve; corre `coverage_script` y reporta cobertura como **verificada**, no "manual".
- 🟡 Si el harness no está corriendo, la Preview aparece vacía y mora lo dice (no finge que el componente se renderizó).

## Ejemplo B — Hub sencillo, sin scripts de gobernanza

```yaml
mora:
  doc_shell:
    - design-hub/styles.css
  serve_command: "python3 -m http.server 8080 --directory ."
  # doc_standard, coverage_script, hub_preview → vacíos:
  #   mora usa su orden interno, reporta cobertura "manual" y espeja el CSS del componente.
```

**Qué haría mora con este bloque** (documentación sólida, con caveats honestos):
- ✅ Reutiliza las clases de `styles.css` (tiene shell) → páginas con estilo.
- ✅ Sirve el Hub en el puerto 8080 para validar las páginas.
- 🟡 Como no hay `doc_standard`, ordena las páginas con **su orden canónico interno** y lo declara.
- 🟡 Como no hay `hub_preview`, la Preview **espeja el CSS del componente** y lo etiqueta como "espejo", no como el componente real (no hay harness al que apuntar).
- 🟡 Como no hay `coverage_script`, reporta la cobertura como **"manual"** (revisó a mano que los componentes tengan página, pero sin censo automático).
- 🚫 No inventa un harness ni finge una preview en vivo que no existe.

## Ejemplo C — mínimo (arrancar ya, afinar después)

```yaml
mora:
  doc_shell:
    - design-hub/docs.css
  # todo lo demás vacío. mora documenta y avisa qué chequeos quedaron "manual".
```

**Qué haría mora con este bloque** (lo mínimo para arrancar):
- ✅ Usa `docs.css` para que las páginas tengan estilo (el único campo que de verdad conviene no dejar vacío).
- 🟡 Orden interno de secciones, preview por espejo de CSS, cobertura "manual", servidor por defecto (`python3 -m http.server`).
- ✅ **Igual documenta y sincroniza** — solo que su declaración de cumplimiento dirá claramente qué quedó "manual". Afinas los campos después sin rehacer nada.

### Y si dejas `doc_shell` también vacío…

```yaml
mora:
  # (todo vacío)
```
- 🚫 mora **avisa que no hay shell que reutilizar**: es el único caso peligroso, porque las páginas podrían quedar "sin estilo" (usar clases que no existen). Aun así no inventa un shell; te pide que apuntes a los css/js reales de tu Hub antes de generar páginas.

---

## Notas por campo

- **`doc_shell` es el más importante.** Son los archivos cuyas clases reales reutilizan las páginas del Hub. Si mora no los conoce, puede generar páginas que "se ven sin estilo" (usar clases inexistentes). Apunta a los css/js reales de tu Hub.
- **`hub_preview`** es cómo se muestra el componente REAL en la doc: normalmente un `iframe` a un harness que monta el SFC (p. ej. tu dev server en `/qa/<component>`). Si no tienes harness, déjalo vacío y mora espejará el CSS del componente (y lo etiqueta como espejo, no como el componente real).
- **`coverage_script`** confirma que todo componente esté censado/documentado. `AUTO` para que mora intente detectarlo; vacío para que lo haga a mano.
- **`doc_standard`** define el orden fijo de secciones de cada página (Overview→Preview→Usage→…→History). Vacío = mora usa su orden canónico interno.

> Regla de honestidad: mora documenta **lo que existe**. Ningún campo de este bloque la autoriza a inventar props/estados/APIs que el código no tiene.
