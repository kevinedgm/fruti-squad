# Fruti Squad · roles y fronteras

Fuente única de los roles del squad. Cada miembro describe en su manual solo su propia frontera y remite aquí para el resto. La política de ejecución (rutear primero, fuentes aprobadas, handoffs) está en `.fruti/policy.md`.

## Flujo

```text
🥝 kiwi  → estructura: brief, flujo, wireframes F0–F2
🟢 lima  → gobierno: clasifica, reutiliza, registra, fija contrato y decide estados
🥥 coco  → construcción: alta fidelidad con el sistema real (F3), implementación (R3), auditoría (R0)
🫐 mora  → documentación: publica lo implementado y verificado
🍇 uva   → lateral: iconos SVG a medida; entrega SVG verificados a coco
🥭 mango → lateral: ilustraciones de línea para secciones; entrega SVG verificados a coco
```

Orden: **kiwi estructura → lima gobierna → coco construye/verifica → mora documenta.** Uva no forma parte de la cadena: se invoca cuando hace falta un icono que no existe. Entrega SVG verificados a coco, que los consume sin redibujarlos; lima decide si su ADN base se vuelve token (`icon.*`) y registra el icono si el proyecto lleva registry de iconos; mora lo documenta si el proyecto documenta iconos.

Mango tampoco forma parte de la cadena: se invoca cuando una sección necesita una ilustración. Compone con su kit, prueba en la sección real y entrega SVG verificados a coco, que los coloca sin redibujarlos; lima decide si sus roles de color se vuelven tokens (`illustration.*`); mora los documenta si el proyecto documenta ilustraciones.

**Un auditor, un gestor del ciclo de vida:** coco es el único auditor (R0 de interfaz y auditoría de arquitectura de componentes) y lima la única dueña del lifecycle y del registry. No hay dos. Cuando el Stable Gate de lima necesita `audit`, se lo pide a coco y consume su declaración de cumplimiento como evidencia; lima conserva `harden` (refinamiento) y todo el ciclo de vida. Lima y coco comparten el mismo perfil de proyecto.

**Registry y mora:** el registry es de lima. Mora solo escribe en él el campo documental `documentation` (ruta de la página del Hub) y `updated` cuando lo cambia; nunca `status`, `version`, owner, `qa`, `refinement`, `production`, `replacedBy`, `dependencies` ni `profileDependencies`. Cualquier otro desajuste lo reporta y lo deriva a lima.

**Modo revisión de impeccable:** los pases de impeccable (critique, distill, adapt, polish, harden) corren sobre la salida de coco: lima los ejecuta, registra los hallazgos y coco aplica los cambios.

**Perfil compartido y vivo:** un solo perfil por proyecto (`skills/lima/profiles/<proyecto>.md`, resuelto con `.fruti/paths.yaml` o `fruti path`). Lima escribe los campos del sistema (`design_system`, `color_law`, `type_law`, `truth_sources`, `production.*`, `breakpoints`, `anti_references`), coco escribe el bloque `coco:` y mora el bloque `mora:`. Cuando el usuario cambia un dato en lenguaje natural, su dueño lo actualiza y lo confirma en una línea; nunca hace falta reinstalar ni repetir el asistente. El intake del perfil es único y vive en lima (`references/intake.md`); coco y mora solo piden sus bloques.

**Modo autónomo:** si kiwi o coco no están instalados, lima ejecuta el pipeline completo y lo dice en una línea. Coco tiene su propio modo autónomo cuando no hay ronda de kiwi.

## ¿A quién llamo?

| Pide… | Lo hace | Por qué |
|---|---|---|
| Brief, user flow, "¿cómo debería funcionar?" | 🥝 kiwi | Estructura antes que apariencia |
| Wireframe, boceto, estructura, A/B/C estructural | 🥝 kiwi (F0–F2) | La pregunta es de estructura |
| "¿Cómo se vería?" con el design system real, mockup, hi-fi | 🥥 coco (F3) | Requiere el sistema real |
| Implementar lo aprobado | 🥥 coco (R3) | Modifica producción |
| Revisar/auditar UI existente | 🥥 coco (R0) | Un solo auditor en el squad |
| Patrón reutilizable → registro y estado | 🟢 lima | Ciclo de vida |
| Documentar lo implementado | 🫐 mora | Solo lo que existe |
| Estructura nueva del Design Hub | 🥝 kiwi con el **encargo documental** de mora | mora es dueña del contenido y del estándar |
| Icono que no existe en la librería, icono animado | 🍇 uva | Iconografía a medida |
| Ilustración para una sección (personas, escenas, objetos, estados vacíos) | 🥭 mango | Ilustración compuesta con el kit y coloreada por tokens |

## Qué hace lima con un traspaso de kiwi

Cuando el usuario aprueba una estructura, la ronda pasa a lima, no directo a coco. Lima clasifica cada pieza (primitive, patrón, product-application), revisa qué existe en el registry para reutilizarlo, registra lo nuevo como `draft`, fija el contrato de cada artefacto y entrega a coco la orden de construcción. Al aprobarse, la estructura queda congelada: coco aplica el sistema, no rediseña.

## Retornos

| Detecta | Quién | Vuelve a |
|---|---|---|
| Defecto de estructura o de flujo | lima, coco o mora | 🥝 kiwi, que abre `rNN+1` |
| Rechazo de un F2 en el contrato | lima (indica reglas fallidas, restricciones a conservar y qué reconsiderar; no reescribe geometría, no mueve acciones ni reagrupa regiones) | 🥝 kiwi, que crea la siguiente revisión estructural |
| Hueco de gobierno, contrato o tokens | kiwi, coco, mora, uva o mango | 🟢 lima |
| Decisión de estado, versión o taxonomía | mora (u otro) | 🟢 lima |
| Decisión solo de implementación dentro de un contrato aprobado | cualquiera | 🥥 coco |
| Hueco de documentación | cualquiera | 🫐 mora |
| Problema de diseño o de arquitectura, código o evidencia de QA faltante | mora (u otro) | 🥥 coco |
