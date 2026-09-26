# Fruti Squad runtime policy

This repository uses a context-efficient execution model for Codex. The user's natural language is the interface; never require the user to name phases, reference files, loading rules, or internal state.

## Core rule: route first, read second

Do not preload agent/skill reference directories. Do not recursively read `references/`, `reference/`, `examples/`, `templates/`, `assets/`, or long standards merely because they are linked from an AGENT/SKILL file.

For every request:
1. Identify the active artifact/surface and requested operation from natural language.
2. Read `.fruti/state/current.json` when present, then the active Lima project profile and relevant registry entry.
3. Select the owning agent and phase using `.fruti/runtime/<agent>.yaml`; do not open the full AGENT/SKILL manual unless the compact runtime contract cannot resolve the operation.
4. Read ONLY the references listed for that operation by the runtime contract. A filename mentioned in an AGENT/SKILL document is not an instruction to load it unless the current phase requires its rules.
5. Prefer machine-readable contracts/manifests and targeted searches over rereading prose standards.
6. Execute the work.
7. Persist a compact handoff/state delta so the next request starts from current truth rather than reconstructing history.

Deep AGENT/SKILL/reference prose remains normative when a rule is ambiguous, disputed, changed, or cannot be evaluated from the compact contract. Runtime contracts are indexes, not replacement sources of truth.

## Approved Sources Only

All agents MUST distinguish between normative authority and implementation evidence. Agents may inspect the code required to execute or verify a change, but MUST NOT mine unrelated project code, neighboring components, screenshots, examples, or historical artifacts to invent design rules.

### Normative authority order

Use the narrowest approved source that owns the decision:
1. Active user instruction for the current request.
2. Approved structural lock / current handoff for frozen architecture, anatomy, geometry, states, and adaptive behavior.
3. Component or pattern contract for component semantics, variants, API, accessibility obligations, and allowed behavior.
4. `.fruti/tokens.json` (when present) for visual-system values and semantic design tokens; generated token outputs are derivatives, not independent authority.
5. Active project profile for implementation target, framework/language, styling strategy, breakpoints, and project configuration.
6. Registry for lifecycle, ownership, canonical identity, reuse/extend/new/local disposition, and promotion status.
7. Audit manifest and verified compliance evidence for QA criteria/results.
8. Deep AGENT/SKILL/reference prose only when the compact approved sources explicitly require it or a rule remains unresolved/ambiguous.

When two approved sources conflict, do not silently choose whichever is convenient. Prefer the source that canonically owns that decision; if ownership itself is ambiguous, mark the decision `unresolved` and route it to the owning agent.

### Forbidden inference

Agents MUST NOT:
- infer a design rule by inspecting unrelated or neighboring components;
- copy raw colors, font sizes, spacing, radii, shadows, motion values, breakpoints, or other visual values from existing code when an approved token/contract owns that decision;
- treat an implementation accident, legacy value, screenshot, demo, or example as design-system truth;
- scan the repository broadly to discover styling conventions when the relevant approved contract/token already exists;
- invent a missing value merely to keep execution moving;
- reinterpret a frozen lock without routing the structural change back to Kiwi/Lima as appropriate.

### Code inspection boundary

Existing code is implementation evidence, not design authority. An agent MAY inspect:
- the exact files it must modify;
- direct dependencies/imports needed to understand or safely edit those files;
- generated outputs that must be regenerated or verified;
- targeted implementation/API evidence required by the current contract or audit rule.

That permission does not allow exploratory repository-wide inspection for design inspiration or convention discovery.

### Missing decisions

If an approved source does not define a required decision:
1. Do not infer it from unrelated code.
2. Record it as `unresolved` in the active handoff/state delta.
3. Route it to the agent that owns the decision (Kiwi for structure/UX geometry, Lima for governance/contracts/tokens ownership, Coco for implementation-only choices inside an approved contract, Mora only for documentation gaps).
4. Ask the user only when the missing decision is genuinely a product/identity choice that cannot be derived from an approved default.

### Token discipline

When `.fruti/tokens.json` exists, it is the canonical editable source for global visual tokens. Components consume semantic tokens rather than owning duplicated raw values. Generated CSS/TS/framework token files are regenerated derivatives and MUST NOT become competing sources of truth.

A request such as `cambia la fuente principal`, `cambia el color de acción`, or `haz los radios menos redondeados` should update the owning semantic token/configuration and regenerate affected derivatives. It should not trigger component-by-component visual reinterpretation.

## Runtime contracts

- `.fruti/runtime/kiwi.yaml`: route structural work, define minimum inputs and handoff output.
- `.fruti/runtime/lima.yaml`: route governance operations and registry/lifecycle reads.
- `.fruti/runtime/coco.yaml`: route F3/R3/R0 and audit-manifest execution.
- `.fruti/runtime/mora.yaml`: route documentation work from verified deltas.

Read one runtime contract for the active owner. Do not read all four just because a full squad pipeline may eventually run; each stage reads its own contract when control reaches it.

## Squad routing

- Kiwi: structure and UX, brief/flow/wireframes F0-F2. Read only structural references needed for the selected fidelity. Kiwi defines functional geometry and adaptive composition but does not invent visual styling.
- Lima: governance, classification, reuse, registry, contracts, token ownership and lifecycle. Read only the reference for the current governance operation/gate.
- Coco: F3 construction, implementation and canonical UI audit. Consume approved locks/contracts/tokens. For audits, use `.fruti/audit-manifest.yaml` plus automated evidence first; open prose standards only for failed/ambiguous/non-deterministic checks.
- Mora: documentation of implemented/verified truth. Work from registry + approved contracts/tokens + Coco compliance report + targeted code/diff; document the delta. Do not reconstruct the whole design history or infer rules from the implementation.

## Handoff contract

Each stage passes a compact handoff at `.fruti/handoffs/current.json` (or an artifact-specific equivalent) containing only:
- artifact id and round
- source agent and next owner
- decisions frozen in this stage
- pieces and their reuse/extend/new/local disposition when known
- required states and adaptive behavior
- unresolved questions/blockers
- evidence paths produced
- changed fields since the previous handoff

Never copy whole reference documents into a handoff. The receiving agent treats the handoff as an index to canonical artifacts, not as permission to reopen every upstream document.

## Persistent state

`.fruti/state/current.json` is an operational cache, not a second source of truth. Canonical ownership remains: project profile for configuration, registry for lifecycle/status, real code/types for implementation/API evidence, approved locks/contracts/tokens for design decisions, and audit evidence for QA.

Update state with pointers + compact decisions. If cached state conflicts with a canonical source, canonical truth wins and state is repaired.

## Audit policy

Deterministic checks should be executed by scripts/tools where available: DOM validity, duplicate IDs, broken links, horizontal overflow, token usage, forbidden raw values, interactive semantics, required states, target sizes, focus hooks and registry consistency.

Coco spends model reasoning on non-deterministic review: hierarchy, clarity, density, affordance, consistency, adaptive composition, misleading interaction, visual regressions and exceptions. Report rule IDs and evidence; do not reread an entire standard to rediscover a known criterion.

Coco writes `.fruti/reports/compliance-current.json` (or artifact-specific equivalent). Lima consumes that report for gates; Mora consumes it as QA evidence. Neither should rerun Coco's audit merely to understand the result.

## Documentation policy

Mora reads only the affected artifact, registry entry, public API/code, approved token/contract sources, compliance report, active documentation contract and affected navigation/shell. Expand scope only for global audit/synchronization requests. The Design Hub documents approved truth; it does not derive new design rules from the product implementation.

## User experience

The user should be able to say things like `rediseña este formulario`, `ahora haz el de registro`, `audítalo`, `promuévelo`, `cambia la fuente principal`, or `cambia el color de acción` without internal flags. Infer routing from current state and the request. Ask only for product decisions that materially change the experience.
