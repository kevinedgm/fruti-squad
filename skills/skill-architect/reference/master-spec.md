# Master Specification — the single visible source of understanding

During discovery there must be a **Master Specification that is visible to the user**. It is the current representation of what Skill Architect understands about the skill being designed, and it is the central reference for every later stage.

## Rules for the Master Spec

The Master Spec must:

- stay continuously updated;
- be visible to the user;
- reflect only the currently valid state;
- replace earlier information when a decision changes;
- show no version history;
- accumulate no discarded decisions;
- act as the authoritative reference for requirements, capabilities, architecture, and file design.

When a decision changes, overwrite the affected part. Do not keep "before/after" trails inside the spec.

## Possible sections

Include a section only when it is relevant to this specific skill. Never pad the document with empty sections just to match a template.

- **Propósito** — what problem the skill solves.
- **Usuarios** — who uses it or for whom it produces results.
- **Casos de uso** — real situations where it is expected to be used.
- **Entradas** — what information it can receive.
- **Contexto** — what other information it can consult or use.
- **Comportamientos** — what it must do in each relevant situation.
- **Acciones** — what operations it can perform.
- **Permisos** — what it may do automatically vs. what may need authorization.
- **Restricciones** — rules it must respect.
- **Límites** — things it must not do.
- **Resultados** — what it must produce.
- **Excepciones** — how it behaves outside the normal flow.
- **Herramientas** — external capabilities it needs, only when justified.
- **Estado** — information it must retain, only when necessary.
- **Criterios de calidad** — how to tell its work is correct or good enough.
- **Información pendiente** — unresolved points that could affect the design.

## Classifying information

Internally tag each item so you know how solid it is:

| Tag | Meaning |
|---|---|
| **CONFIRMADO** | Established explicitly by the user. |
| **INFERIDO** | Strongly implied by what the user explained. |
| **PROPUESTO** | Suggested by Skill Architect as a reasonable alternative. |
| **DESCONOCIDO** | Not yet resolved. |

Do not question the user just to clear every DESCONOCIDO. Ask only when an unknown could materially change behavior, capabilities, limits, architecture, or results. INFERIDO and PROPUESTO items are fine to carry forward as long as they are visible and can be corrected.

## Presentation

Keep the Master Spec readable for a non-technical user: plain language, grouped by the sections above, current state only. When you update it after an answer or a synthesis, show the user the updated document rather than a diff.
