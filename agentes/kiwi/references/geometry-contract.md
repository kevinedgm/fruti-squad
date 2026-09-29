# Kiwi F2 geometry contract

Kiwi owns structural certainty, not final visual styling. A F2 artifact is not complete until geometry is explicit enough that Coco can build F3 without re-deciding information architecture.

## Required geometry

For every major region record:
- role and dominant information;
- min/max or reference size when size affects usability;
- grid span / placement;
- spacing relationship to adjacent regions;
- density and expected content range;
- primary/secondary hierarchy;
- interactive target size;
- overflow/truncation/wrapping behavior.

## Adaptive matrix

Always describe compact (<600), medium (600–1023), expanded (>=1024):
- what is preserved;
- what changes structure;
- what is hidden or progressively disclosed;
- navigation form;
- primary-action placement;
- list/detail relationship.

Do not merely scale the same layout.

## Piece contract (per piece, not per region)

Decompose each screen into pieces: a piece is a group of data plus an interaction boundary that could stand alone (a widget, a card with a domain object, a list row). For every piece record, for each size it can receive (reference container sizes, not only the three layout modes):
- dominant value and the type role it uses (semantic role from the typography contract, never an invented px value);
- secondary values, each marked kept | demoted (smaller role) | disclosed on demand | hidden;
- spacing role and reference dimensions (w×h, min/max) derived from the content range, the 44 px target and one-hand use; Coco verifies them at the profile viewports;
- states the piece must support and its overflow/long-text behavior;
- candidate disposition for Lima (reuse | extend | new | local) with the reason.

Recompose, don't restack: every size must state which value is promoted and which is demoted. Only moving blocks into rows or columns does not count as adaptation.

- Every piece classified new or extend gets its own per-size table, not only the first one you think of.
- If the dominant value is the same at every size, justify it (`because`); do not copy it by default. Ask whether a different value should lead when the space is much larger or smaller.
- State what each dimension derives from (content range, 44 px target, one-hand use); an unexplained number is not a dimension.
- A pattern that repeats (for example the same section header three times) is one piece, listed once with its count.

## Decision provenance

Important structural decisions use a compact record:
- id
- choice
- source: rule | product-context | inference
- because
- alternatives_rejected (when useful)
- affects: compact | medium | expanded
- status: proposed | frozen | unresolved

Never attribute an inference to a standard.

## Neutrality

F2 uses grayscale/system type. No final brand colors, decorative shadows, brand illustration or F3 motion. Geometry and hierarchy must work without color.

## Grouping rule

Do not introduce a card merely because a UI library has cards. Use a surface only when it communicates a real independent group, interaction boundary, selectable object, or elevation/layer. Prefer spacing, alignment and dividers for ordinary grouping.

## Interface standards

Configured interface guidelines (for example a project-supplied Apple HIG reference) are normative only when the actual source is available through the active profile/contracts. If the source is missing, record the gap. Do not reconstruct or paraphrase a missing normative document from memory.
