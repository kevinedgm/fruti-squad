# Redesign contract

Loaded when redesign intent is detected or `.fruti/redesign/scope.yaml` exists, **before touching any surface**. Every member that can modify a surface (kiwi, lima, coco, mora, uva) reads it. Moved out of the always-loaded policy; the rules are unchanged.

## Understand before changing

Fruti Squad supports both greenfield design and redesign of an existing product. A redesign is NOT permission to rewrite the application or treat legacy styling as target truth.

When redesign intent is detected, Kiwi runs `understand → inventory → scope (user approval) → redesign_plan` (operations and rules in `.fruti/runtime/kiwi.yaml`), persisting to `.fruti/redesign/scope.yaml`, `.fruti/design/design-direction.yaml` and `.fruti/redesign/plan.yaml`. Only then the normal Kiwi → Lima → Coco → Mora handoffs run, per approved item. References are inspiration (qualities, not specifications).

## Redesign statuses

Use: `not-reviewed`, `proposed`, `approved`, `excluded`, `preserve`, `completed`.

- `excluded`: agents MUST ignore the surface for direct redesign. Do not modify it as a redesign side effect. Approved global-token propagation is tracked separately and must not be misrepresented as a direct redesign.
- `preserve`: current structure/behavior is intentionally frozen. Visual work may only touch what the approved scope explicitly allows.
- `approved`: eligible for the redesign plan and downstream execution.

## Existing-product boundary

In redesign mode, existing code is an authorized source for understanding current functionality, data requirements, routes, interactions and implementation constraints. It is NOT an authorized source for deciding the target visual identity unless the user explicitly marks a current rule as preserved.

Do not copy legacy colors, spacing, typography, radii, shadows, component styling or layout conventions merely because they exist. The target design direction, approved contracts and tokens own the redesigned visual system.

## Design direction

`.fruti/design/design-direction.yaml` is the approved compact source for experiential intent (perception, quality level, composition, device emphasis, anti-patterns). It guides Kiwi's structure and Lima's checks; `.fruti/tokens.json` remains the canonical materialization of visual values.
