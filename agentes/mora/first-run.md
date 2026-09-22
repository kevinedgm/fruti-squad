# Primer uso — usar mora en un proyecto nuevo

mora es agnóstica del proyecto. En un repo que nunca ha curado no hay perfil activo, así que lo primero — antes de cualquier inventario, reestructura o documentación — es enlazar mora al proyecto. mora comparte su perfil con la skill `lima` y con coco, así que esto es rápido cuando cualquiera de los dos ya está configurado.

## Orden de resolución (compuerta 0)

1. **Busca un perfil existente** en `profiles/<project>.md` de la skill architect.
   - Si existe y resuelve → **reúsalo**. Luego verifica el bloque `mora:` ([profile-additions.md](profile-additions.md)); si falta, pide solo esas adiciones ([intake.md](intake.md), la parte `mora:`) y añádelas.
2. **Aún no hay perfil** → inicializa pidiendo el intake completo ([intake.md](intake.md)): los campos del architect + el bloque `mora:`, en un solo mensaje. Mapea las respuestas a `profiles/<project>.md` y confirma.
3. **Override del usuario** → una instrucción explícita en la conversación gana sobre el perfil; obedécela y anota la desviación en una línea.

Nunca hagas inventario ni reestructures contra una taxonomía de Hub asumida. Si no hay perfil y el usuario no ha dado el intake, pídelo primero. Y aun con un perfil, mora siempre empieza el trabajo real con el **inventario (paso 1)** — nunca reordena ni reescribe antes de saber qué está desincronizado.

## Dos formas de enlazar

### A. Guiada (por defecto, con el usuario presente)
Presenta el/los formulario(s) de intake literalmente, valida cada campo, resuelve `AUTO` inspeccionando el repo y mostrando hallazgos, luego escribe/extiende el perfil y confirma.

### B. Reusar el bootstrap compartido (lo más rápido al arrancar desde cero)
Si el proyecto es totalmente nuevo, corre primero el bootstrap de la skill architect — crea `profiles/<project>.md`, el Hub y el registry:

```bash
# desde la raíz del repo
bash mis-agentes/skills/lima/scripts/init-project.sh \
  --intake my-intake.yaml --qa playwright
```

Luego añade el bloque `mora:` de mora (desde [intake.md](intake.md)) a ese perfil generado. mora lee el mismo archivo.

## Qué necesita mora para estar a plena potencia

Incluso con un perfil, algunas capacidades dependen del tooling del proyecto. mora degrada honestamente — sigue curando, pero etiqueta lo que no pudo correr:

| Capacidad | Necesita | Si falta |
|---|---|---|
| Inventariar registry + páginas | `registry_path`, `hub_root` en el perfil | no puede arrancar — pide el perfil |
| Contrastar páginas vs código real | `production.component_layout` | anota que no puede confirmar deriva del código |
| Censo de cobertura | `mora.coverage_script` | reporta cobertura como `manual` |
| Servir + validar páginas | `mora.serve_command` (o python3) | reporta el check de HTTP/shell como no ejecutado |
| Reusar el shell de doc real | `mora.doc_shell` | señala que las páginas no tienen shell que reutilizar (riesgo de páginas sin estilo) |
| Preview viva del componente | `mora.hub_preview` / un harness corriendo | espeja el CSS del componente, etiquetado como espejo |
| Orden de secciones + spec de honestidad | `mora.doc_standard` | usa el orden canónico interno de mora, declarado |

Ninguna de estas impide que mora *cure*; solo cambian qué checks son verificables vs manuales. La declaración de cumplimiento (paso 5) siempre dice la verdad sobre cuáles corrieron.

## Resultado

- mora queda enlazada a `profiles/<project>.md` (compartido con la skill architect y coco), incluyendo un bloque `mora:`.
- Desde aquí aplica el protocolo de 5 pasos (AGENT.md): inventario → alcance → leer estándar → estructura canónica del Hub → verificar + declaración de cumplimiento.
