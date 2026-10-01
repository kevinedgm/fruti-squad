# Modo autónomo (kiwi o coco no instalados)

Se carga **solo** si kiwi o coco no están instalados en el proyecto. Entonces lima ejecuta el pipeline completo por sí misma y lo dice en una línea. Con el squad completo, lima solo gobierna: la estructura es de kiwi y la construcción, de coco (`.fruti/contracts/squad.md`).

Si coco está instalado pero no hay ronda de kiwi, coco tiene su propio modo autónomo (`agentes/coco/references/modo-autonomo.md`, descubrimiento funcional y R2 estructural); no lo dupliques aquí.

## Pipeline de diseño (fase DRAFT)

```text
DRAFT
  diseña la experiencia primero (propósito → tarea → jerarquía → principios UX)   (design-process.md)
  diseño → critique → distill → adapt → polish                                    (impeccable-bridge.md)
  → revisión arquitectónica (esta skill)
  → Candidate Gate y transición a candidate (gobierno, como en el SKILL.md)
```

Después de `candidate`, el ciclo de vida es el mismo del SKILL.md (harden, audit delegado a coco si está instalado, Stable Gate, aprobación explícita). En modo autónomo sin coco, lima ejecuta el audit con los playbooks de impeccable y lo declara como evidencia propia, no de coco.

## Reglas del modo autónomo

- Diseña propósito, comportamiento, contexto y experiencia antes que la apariencia; una petición nunca salta directo a variantes visuales (`design-process.md`). La skill es agnóstica del dominio: los dominios son contexto de entrada, nunca reglas.
- Nunca des por terminada la primera versión: ejecuta siempre el pipeline de refinamiento.
- La adaptación por breakpoint es un replanteo real, no un encogimiento (`adaptive-design.md`).
- Las demos viven en el Design Hub (`design-hub.md`), la página de referencia sigue `component-documentation.md` y la QA en navegador real sigue `runtime-qa.md`.
- La implementación en producción sigue `promotion.md` y `component-api.md`, solo con aprobación explícita.

## Referencias que se cargan en este modo

| Archivo | Cuándo |
|---|---|
| `design-process.md` | Diseñar la experiencia antes que la apariencia |
| `adaptive-design.md` | Diseñar la composición por breakpoint (en el squad, solo para fijar el contrato adaptativo) |
| `design-hub.md` | Construir demos y la comparación responsive |
| `component-documentation.md` | Documentar la pieza como página viva (en el squad lo hace mora) |
| `runtime-qa.md` | Ejecutar la QA en navegador (en el squad la ejecuta coco) |
| `promotion.md` | Implementar en producción (en el squad lo hace coco) |
