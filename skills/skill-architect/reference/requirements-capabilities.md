# Requirements and capabilities

This stage runs after discovery is complete enough and before any architecture decision. Requirements come first; capabilities second; architecture only after both.

## Requirements before architecture

Strictly respect this order:

```text
User need → Discovery → Specification → Requirements → Capabilities → Architecture
```

Never start from a known architecture and bend the need to fit it. Architecture is a consequence of requirements.

## Extracting requirements

Convert the Master Spec, the conversation, and the user's examples into explicit requirements. A good requirement is behavioral and checkable. Model, for each relevant situation:

- **Entradas** — what the skill receives.
- **Contexto** — what else it can use.
- **Comportamiento** — what it must do.
- **Reglas** — under what constraints it acts.
- **Acciones / Permisos** — what it may do, and what needs authorization.
- **Salidas** — what it produces.
- **Excepciones** — how it behaves outside the normal flow.
- **Criterios de aceptación** — what makes the output acceptable.

Trace each requirement back to something the user said or to a clearly inferred need. If a requirement has no source, it is probably invented complexity — drop it or confirm it.

## Modeling capabilities

Once requirements are set, determine what the future skill must be **able to do**. A capability is an ability of the system — not necessarily a file or module.

Examples of capabilities:

```text
comparar documentos
detectar inconsistencias
buscar información
clasificar hallazgos
generar un informe
pedir aprobación
modificar archivos
mantener estado
```

Only after capabilities are modeled do you decide how each one is implemented. Do not attach files, agents, or components to capabilities yet — that is the architecture stage.

## Checkpoints

Before moving to architecture, confirm you can answer, per requirement:

- Which capability (or capabilities) satisfies it?
- Is every capability traceable to a real requirement?
- Is any capability present only because a familiar architecture "usually has it"? If so, remove it.

Keep the Master Spec updated with the resolved requirements and capabilities. Continue automatically to [architecture.md](architecture.md) unless a material ambiguity requires asking the user.
