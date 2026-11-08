# Interaction contract — triggers, rules, feedback and modes per state

Owner: lima, as part of the `contract` operation. Consumer: bruno (R3), who implements it and must not invent it; coco audits it (R0).

The states vocabulary (`ui-artifact-contract.md`) says **which** states a piece has. This file says **how the piece moves between them**. Without it, "the autocomplete has a loading state" leaves open when loading starts, what the user sees meanwhile and what happens on failure, and the implementer ends up deciding product behavior.

Adapted from Dan Saffer's *Microinteractions* via wondelai/skills (`microinteractions`, MIT, © 2025 Wondel.ai).

## The four parts

| Part | Question it answers | Example (autocomplete) |
|---|---|---|
| Trigger | What starts the transition: a user action or a system condition? | User types ≥ 2 characters, after 300 ms without typing |
| Rules | What happens, in what order, with which limits, and when does it end? | Query runs; earlier pending query is discarded; at most 8 results; ends on results, empty or error |
| Feedback | What does the user perceive, and through which channel (visual, text, ARIA live, focus)? | Spinner in the field; list announced as "8 results" via `aria-live="polite"` |
| Loops and modes | Does it repeat, expire or change meaning in another mode? | Results expire if the text changes; in read-only mode the field never triggers |

## Transition table (required for every interactive piece)

One row per transition, not per state:

```yaml
transitions:
  - from: idle
    to: loading
    trigger: "input length >= 2 and 300 ms without typing"
    rules: ["cancel the previous pending request", "keep the typed text"]
    feedback: ["spinner inside the field", "aria-busy=true on the listbox"]
    source: rule | product-context | inference
  - from: loading
    to: error
    trigger: "request fails or exceeds 8 s"
    rules: ["preserve the typed text", "offer retry"]
    feedback: ["inline error text with the cause", "focus stays in the field"]
    source: product-context
```

`source` follows the geometry contract convention: a `rule` cites its standard, `product-context` cites the user or brief, and `inference` is an assumption that must be confirmed before stable.

## Rules for writing it

- Derive the rules from the user's goal, not from the widget. State the goal in one sentence first.
- Match rule complexity to frequency: a many-times-a-day action gets no configuration and instant feedback; a once-ever setup can explain itself.
- Every transition that can fail has an error row that preserves the user's input.
- Feedback never relies on color alone and is announced when it changes content out of focus.
- A disabled state says why (text or accessible description), not just that it is disabled.
- Durations and delays that are visual (motion) come from motion tokens; delays that are behavioral (debounce, timeout) are part of the rules and live here.

## What bruno does with it

Bruno implements each row literally. A transition the table does not cover is `unresolved` and returns to lima; bruno does not pick a debounce, a timeout or an error message on its own.
