---
name: skill-architect
description: Use when the user wants to create, design, build, or scaffold a NEW skill for an AI agent starting from a plain-language idea. The user describes what they want to achieve, how they imagine using the skill, and what results they need; this skill turns that into a full skill project (spec, requirements, capabilities, architecture, files, validation, docs). Use for requests like "create a skill that...", "I want a skill for...", "help me build an agent skill", "design a new skill", or "turn this idea into a skill". Not for editing existing non-skill code or for using an already-built skill.
license: MIT
metadata:
  author: skill-architect
  version: "1.0"
---

# Skill Architect

Skill Architect is a meta-skill. It turns a plain-language idea into a complete, working project for a **new** AI-agent skill. The user explains what they want; Skill Architect handles the design, structure, files, validation, and documentation.

**The user never has to design a skill technically.** They speak in terms of goals, behavior, and outcomes. You translate that into specification, requirements, capabilities, architecture, and files.

## Guiding principle

**Architecture emerges from required behavior.** Never decide up front that the new skill needs multiple files, sub-agents, routers, workflows, scripts, tools, persistent state, evaluators, schemas, policies, databases, or external integrations. Introduce each element only when the requirements of the future skill justify it. Use the minimum architecture that correctly satisfies the requirements.

You must follow this sequence and never invert it:

```text
User need → Discovery → Specification → Requirements → Capabilities → Architecture → Module design
```

Never do: `Idea → known architecture → bend the need to fit it.` Architecture is a consequence of requirements, not a starting template.

## The flow

```text
IDEA → DISCOVERY → VISIBLE MASTER SPEC → REQUIREMENTS → CAPABILITIES
→ ARCHITECTURE → MODULE DESIGN → FULL PROJECT TREE → FULL FILE CONTENT
→ GLOBAL APPROVAL → REAL FILE GENERATION → VALIDATION
→ (auto-fix if approved design unchanged / re-approve if substantial change)
→ FINAL DOCUMENTATION → DELIVERY
```

## Stages and their references

Work through these stages in order. Load the reference for the stage you are in.

| Stage | What you do | Reference |
|---|---|---|
| 1. Discovery | Understand the idea through natural conversation, not a form. Ask via examples. Detect only material gaps. | [reference/discovery.md](reference/discovery.md) |
| 2. Master Spec | Maintain a single, visible, always-current specification. Classify info as CONFIRMADO / INFERIDO / PROPUESTO / DESCONOCIDO. | [reference/master-spec.md](reference/master-spec.md) |
| 3. Requirements + Capabilities | Turn conversation and examples into explicit requirements, then model what the future skill must be able to do. | [reference/requirements-capabilities.md](reference/requirements-capabilities.md) |
| 4. Architecture + Modules | Choose the minimum architecture. Give each module a clear responsibility. Establish sources of truth. | [reference/architecture.md](reference/architecture.md) |
| 5. Proposal + Approval | Present the complete project tree and full file content. Get one global approval before creating anything. | [reference/proposal-approval.md](reference/proposal-approval.md) |
| 6. Generation + Validation + Docs | Create real files only after approval, validate, auto-fix safe defects, re-approve substantial changes, write final docs. | [reference/generation-validation.md](reference/generation-validation.md) |

## Continuation rules

- **Discovery has no mandatory approval gate.** When discovery is complete enough (see the finish criterion in [reference/discovery.md](reference/discovery.md)), continue automatically through Master Spec → Requirements → Capabilities → Architecture → Module design. Only stop to ask the user if you hit an ambiguity you cannot reasonably resolve from what you already know.
- **There is exactly one mandatory approval gate:** after the full design (tree + complete file content) and before creating any real file. Approval is **global for the whole project** — never a state where some files are approved and others are not. See [reference/proposal-approval.md](reference/proposal-approval.md).
- **After generation, validate.** Auto-fix only defects that do not change approved behavior, architecture, responsibilities, permissions, restrictions, capabilities, or fundamental structure. Anything larger forces a rebuild of the affected proposal and a **new global approval**. See [reference/generation-validation.md](reference/generation-validation.md).

## Global restrictions

Skill Architect must never:

- force the user to design the skill technically;
- pick architecture before understanding requirements;
- introduce complexity without justification;
- create real files before global approval;
- treat a project as partially approved;
- silently change fundamental approved decisions;
- ask about irrelevant details just to fill a template;
- duplicate important rules without need;
- declare a skill finished without validating it.

## Quality bar for a run

A run is successful when: the user expressed their need without technical knowledge; the spec faithfully represents that need; questions were relevant, not bureaucratic; architecture derived from real requirements; every component has a reason to exist; the pre-approval proposal was complete; generated files match the approved proposal; validation caught real inconsistencies; auto-fixes never altered approved decisions; and the final documentation lets someone understand the skill without reading the original conversation.

## Where to put the new skill

Create new skills under `.agents/skills/<skill-name>/` unless the user names another location. Match the conventions of skills already in this workspace: a `SKILL.md` with YAML front-matter (`name`, `description`, optional `license`, `metadata`) plus a `reference/` folder for detailed playbooks, and other folders (`schemas/`, `examples/`, `tests/`, `scripts/`) only when the requirements justify them.
