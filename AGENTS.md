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

## Runtime contracts

- `.fruti/runtime/kiwi.yaml`: route structural work, define minimum inputs and handoff output.
- `.fruti/runtime/lima.yaml`: route governance operations and registry/lifecycle reads.
- `.fruti/runtime/coco.yaml`: route F3/R3/R0 and audit-manifest execution.
- `.fruti/runtime/mora.yaml`: route documentation work from verified deltas.

Read one runtime contract for the active owner. Do not read all four just because a full squad pipeline may eventually run; each stage reads its own contract when control reaches it.

## Squad routing

- Kiwi: structure and UX, brief/flow/wireframes F0-F2. Read only structural references needed for the selected fidelity.
- Lima: governance, classification, reuse, registry, contracts and lifecycle. Read only the reference for the current governance operation/gate.
- Coco: F3 construction, implementation and canonical UI audit. For audits, use `.fruti/audit-manifest.yaml` plus automated evidence first; open prose standards only for failed/ambiguous/non-deterministic checks.
- Mora: documentation of implemented/verified truth. Work from registry + Coco compliance report + code/diff; document the delta. Do not reconstruct the whole design history.

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

`.fruti/state/current.json` is an operational cache, not a second source of truth. Canonical ownership remains: project profile for configuration, registry for lifecycle/status, real code/types for implementation/API, audit evidence for QA.

Update state with pointers + compact decisions. If cached state conflicts with a canonical source, canonical truth wins and state is repaired.

## Audit policy

Deterministic checks should be executed by scripts/tools where available: DOM validity, duplicate IDs, broken links, horizontal overflow, token usage, forbidden raw values, interactive semantics, required states, target sizes, focus hooks and registry consistency.

Coco spends model reasoning on non-deterministic review: hierarchy, clarity, density, affordance, consistency, adaptive composition, misleading interaction, visual regressions and exceptions. Report rule IDs and evidence; do not reread an entire standard to rediscover a known criterion.

Coco writes `.fruti/reports/compliance-current.json` (or artifact-specific equivalent). Lima consumes that report for gates; Mora consumes it as QA evidence. Neither should rerun Coco's audit merely to understand the result.

## Documentation policy

Mora reads only the affected artifact, registry entry, public API/code, compliance report, active documentation contract and affected navigation/shell. Expand scope only for global audit/synchronization requests.

## User experience

The user should be able to say things like `rediseña este formulario`, `ahora haz el de registro`, `audítalo`, or `promuévelo` without internal flags. Infer routing from current state and the request. Ask only for product decisions that materially change the experience.
