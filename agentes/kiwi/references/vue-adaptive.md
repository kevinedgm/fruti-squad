# vue-adaptive (solo si el proyecto lo usa)

Reglas de kiwi específicas del paquete `vue-adaptive`. Si el proyecto no lo usa, este archivo no se lee.

## Fase 1 — Investigar

Lee el **paquete instalado y su API real**; nunca supongas que el README coincide con el código.

## Fase 3 — Estándares

`vue-adaptive` (si existe): la API real instalada es la referencia.

## Fase 4 — Técnica prevista (se declara, no se implementa)

- `Adaptive`/`useAdaptive` cuando cambian comportamiento o coordinación; `router.meta.adaptive` si el paquete lo permite. Para cambios locales, CSS intrínseco y container queries (técnica genérica de la Fase 4).
- Si `AdaptiveSwitch` monta ramas distintas, identifica qué estado o foco se perdería y cómo preservarlo.

## Fase 6 — Traspaso

Incluye el **mapeo tentativo a la API real de `vue-adaptive`, con límites conocidos** (punto 4 de la plantilla de traspaso).
