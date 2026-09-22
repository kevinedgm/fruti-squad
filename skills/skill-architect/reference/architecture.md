# Architecture and module design

Run this stage only after requirements and capabilities are set. The output is the minimum architecture that cleanly satisfies them, plus a clear responsibility for every module.

## Choose the minimum architecture

Select the smallest architecture that satisfies the requirements and capabilities cleanly. The following components are available but **none is mandatory by default** — introduce each only when a requirement or capability justifies it:

- Router
- Workflow
- Playbook
- Policy
- Evaluator
- Specialized Agent
- Schema
- Utility
- State
- Script
- Tool integration

For each component you propose, be able to state which capability forced it into existence. If you cannot, remove it.

## Module responsibility

When the architecture has several modules, each must have one clear responsibility. For every module you must be able to answer:

```text
Quién lo invoca
↓
Qué información necesita
↓
Qué responsabilidad posee
↓
Qué otros elementos puede invocar
↓
Qué resultado produce
↓
Dónde continúa el flujo
```

If any of these cannot be answered clearly, reconsider whether the module should exist or where its boundary lies.

## Sources of truth

Every important rule has one authoritative owner. Do not duplicate critical information across files.

```text
Reglas de fuentes      → source-policy.md
Convenciones globales  → PROJECT.md
```

Other components reference the authoritative source instead of keeping their own copies. When you notice the same rule stated in two places, pick an owner and make the other a reference.

## Module scope

A module must not silently widen its responsibility. When, during a task, a need appears outside a module's scope, the module should:

1. identify it;
2. keep the finding if it is relevant;
3. route it to the appropriate component;
4. request additional intent when the new action requires it.

## Every workflow must terminate

Any workflow you design must have a defined ending. There should be no path that loops forever or leaves the flow undefined. Define behavior on failure as explicitly as behavior on success.

## Handing off

Keep the Master Spec updated with the chosen architecture and module map. Continue automatically to project design and the proposal in [proposal-approval.md](proposal-approval.md). Only stop to ask the user if a material ambiguity cannot be resolved from what you already know.
