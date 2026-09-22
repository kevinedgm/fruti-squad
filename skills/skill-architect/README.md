# Skill Architect

A meta-skill that turns a plain-language idea into a complete, working project for a **new** AI-agent skill. The user describes what they want to achieve; Skill Architect produces the specification, requirements, capabilities, architecture, files, validation, and documentation.

## What it does

You say what you want. Skill Architect does the technical design:

```text
Your idea
  → conversational discovery
  → a visible, always-current Master Spec
  → requirements
  → capabilities
  → architecture
  → module design
  → full project tree + complete file content
  → one global approval
  → real files
  → validation
  → final documentation
```

You never have to think in terms of routers, workflows, schemas, evaluators, or agents. You describe behavior and outcomes; the skill decides the minimum architecture that satisfies them.

## Core principles

- **Architecture emerges from behavior.** No component (files, sub-agents, routers, workflows, scripts, tools, state, evaluators, schemas, policies, databases, integrations) is added unless a requirement justifies it. Minimum architecture that works.
- **Requirements before architecture.** Discovery → Specification → Requirements → Capabilities → Architecture. Never bend the need to fit a familiar design.
- **One global approval gate.** Nothing real is created until you approve the complete project as a whole. There is no partially-approved state.
- **Validate before declaring done.** After generation, the skill checks coverage, references, flows, sources of truth, and correspondence with your examples. Safe defects are auto-fixed; substantial changes go back to you for a new approval.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Entry point: guiding principle, the flow, stage-to-reference map, restrictions, quality bar. |
| `reference/discovery.md` | Conversational discovery: talk in behavior, ask via examples, detect only material gaps, finish criterion. |
| `reference/master-spec.md` | The single visible spec: rules, possible sections, and the CONFIRMADO / INFERIDO / PROPUESTO / DESCONOCIDO classification. |
| `reference/requirements-capabilities.md` | Turning conversation into explicit requirements, then modeling capabilities. |
| `reference/architecture.md` | Choosing minimum architecture, module responsibility, sources of truth, module scope, terminating workflows. |
| `reference/proposal-approval.md` | Full project tree, complete file content, and the single global approval gate. |
| `reference/generation-validation.md` | Generating real files, validation checklist, safe auto-correction, substantial-change re-approval, final docs. |

## How to use it

Just describe the skill you want, for example: "I want a skill that compares two contracts and flags inconsistencies," or "help me build an agent skill for triaging bug reports." Skill Architect starts the discovery conversation and carries the idea all the way to a validated, documented skill project.

## Where new skills are created

By default under `.agents/skills/<skill-name>/`, matching this workspace's convention: a `SKILL.md` with YAML front-matter plus a `reference/` folder, and additional folders (`schemas/`, `examples/`, `tests/`, `scripts/`) only when justified.
