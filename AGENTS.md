# Fruti Squad runtime policy

Context-efficient execution model for coding agents (Claude Code, Codex, Kiro); Claude Code loads it through `CLAUDE.md`. The user's natural language is the interface: never require the user to name phases, reference files, loading rules, or internal state.

## Core rule: route first, read second

Do not preload agent/skill reference directories, and do not recursively read `references/`, `reference/`, `examples/`, `templates/`, `assets/`, or long standards merely because an AGENT/SKILL file links them.

For every request:
1. Identify the active artifact/surface and requested operation from natural language.
2. Read `.fruti/state/current.json` when present, then the active Lima project profile and relevant registry entry.
3. Select the owning agent and phase using `.fruti/runtime/<agent>.yaml` (kiwi, lima, coco, mora, uva, mango); read only the active owner's contract, and open the full AGENT/SKILL manual only if that contract cannot resolve the operation.
4. Read ONLY the references the runtime contract lists for that operation. A filename mentioned in an AGENT/SKILL document is not an instruction to load it.
5. Prefer machine-readable contracts/manifests and targeted searches over rereading prose standards.
6. Execute the work.
7. Persist a compact handoff/state delta so the next request starts from current truth.

Deep AGENT/SKILL/reference prose remains normative when a rule is ambiguous, disputed, changed, or cannot be evaluated from the compact contract. Runtime contracts are indexes, not replacement sources of truth.

## Approved sources only

Distinguish normative authority from implementation evidence. Inspect the code needed to execute or verify a change, but use nothing else as a source of design rules.

**Normative authority order** (use the narrowest approved source that owns the decision):
1. Active user instruction for the current request.
2. Approved structural lock / current handoff for frozen architecture, anatomy, geometry, states, and adaptive behavior.
3. Component or pattern contract for semantics, variants, API, accessibility obligations, and allowed behavior.
4. `.fruti/tokens.json` (when present) for visual-system values and semantic tokens; generated token outputs are derivatives.
5. Active project profile for implementation target, framework/language, styling strategy, breakpoints, and configuration.
6. Registry for lifecycle, ownership, canonical identity, reuse/extend/new/local disposition, and promotion status.
7. Audit manifest and verified compliance evidence for QA criteria/results.
8. Deep AGENT/SKILL/reference prose only when the compact sources require it or a rule remains unresolved.

When two approved sources conflict, do not silently pick the convenient one: prefer the source that canonically owns the decision; if ownership itself is ambiguous, mark it `unresolved` and route it to the owning agent.

**Forbidden inference.** Agents MUST NOT:
- infer a design rule from unrelated or neighboring components, or by scanning the repository broadly when the relevant approved contract/token already exists;
- copy raw colors, font sizes, spacing, radii, shadows, motion values, breakpoints, or other visual values from existing code when an approved token/contract owns that decision;
- treat an implementation accident, legacy value, screenshot, demo, example, or historical artifact as design-system truth;
- reinterpret a frozen lock without routing the structural change back to Kiwi/Lima.

**Code inspection boundary.** Existing code is implementation evidence, not design authority. An agent MAY inspect the exact files it must modify, direct dependencies needed to edit them safely, generated outputs to regenerate or verify, and targeted implementation/API evidence required by the current contract or audit rule.

**Missing decisions.** If no approved source defines a required decision:
1. Do not infer it from unrelated code or invent a value to keep execution moving.
2. Record it as `unresolved` in the active handoff/state delta.
3. Route it to its owner: Kiwi for structure/UX geometry, Lima for governance/contracts/token ownership, Coco for implementation-only choices inside an approved contract, Mora only for documentation gaps.
4. Ask the user only for a genuine product/identity choice that no approved default covers.

A missing configured normative reference (including a project-specific interface guideline) is reported as missing evidence; never reconstruct a missing standard from memory.

**Token discipline.** When `.fruti/tokens.json` exists, it is the canonical editable source for global visual tokens; components consume semantic tokens rather than owning duplicated raw values. A request such as `cambia la fuente principal`, `cambia el color de acción`, or `haz los radios menos redondeados` updates the owning semantic token/configuration and regenerates affected derivatives; it never triggers component-by-component visual reinterpretation. Typography ownership: `authority` block of `.fruti/contracts/typography.yaml`.

## Situational contracts (read only when they apply)

- **Redesign** — when redesign intent is detected or `.fruti/redesign/scope.yaml` exists, read `.fruti/contracts/rediseno.md` before touching any surface (`excluded` surfaces are never modified as a side effect).
- **Test round** — while executing a `fruti test` round, read `.fruti/contracts/ronda-prueba.md`.
- **Breakpoints** — layout modes vs verification viewports: `.fruti/contracts/adaptativo.md`.
- **NEW foundations** — with `design_system: NEW`, run `fruti foundations` before expecting a valid F3 visual PASS. It creates a proposal, not truth: Lima materializes it only after explicit user approval (`lima.yaml` → `foundations_new`), and Coco never uses an unapproved proposal.

## Squad, audit and documentation

Roles, «who to call» and returns: `.fruti/contracts/squad.md` (single source). Coco is the only auditor and writes `.fruti/reports/compliance-current.json`; Lima and Mora consume it and never rerun the audit. `.fruti/contracts/documentation.yaml` is the single normative source for Design Hub pages; on conflict with any guidance file, the contract wins.

## Handoff contract

Each stage passes a compact handoff at `.fruti/handoffs/current.json` (or an artifact-specific equivalent) containing only: artifact id and round; source agent and next owner; decisions frozen in this stage; pieces and their reuse/extend/new/local disposition when known; required states and adaptive behavior; unresolved questions/blockers; evidence paths produced; fields changed since the previous handoff.

Never copy whole reference documents into a handoff. The receiver treats it as an index to canonical artifacts, not as permission to reopen every upstream document.

## Persistent state

`.fruti/state/current.json` is an operational cache, not a second source of truth. Canonical ownership remains: profile for configuration, registry for lifecycle/status, real code/types for implementation/API evidence, approved locks/contracts/tokens for design decisions, audit evidence for QA. Update it with pointers + compact decisions; if it conflicts with a canonical source, canonical truth wins and state is repaired.

## User experience

The user should be able to say `rediseña este formulario`, `ahora haz el de registro`, `audítalo`, `promuévelo`, `cambia la fuente principal` or `cambia el color de acción` without internal flags. Infer routing from current state and the request. Ask only for product decisions that materially change the experience.

## Path resolution

Runtime contracts cite package-relative paths (`skills/lima/...`, `agentes/kiwi/...`). In an installed project, resolve them through `.fruti/paths.yaml` (written by the installer) or `fruti path`; when absent (this repo itself), the paths are literal.
