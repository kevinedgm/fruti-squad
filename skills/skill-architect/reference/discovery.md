# Discovery — conversational understanding

Goal of this stage: understand the idea well enough that architecture can later be derived from it. You are talking to someone who wants an outcome, not someone designing a system.

## Talk in behavior, not in jargon

The user does not need to know prompt engineering, agent architecture, workflows, contracts, state, schemas, routers, evaluators, or orchestration. Ask only about behavior and real needs:

- what they want to achieve;
- what they would give the skill;
- what they expect it to do with that;
- what result they expect;
- what unusual situations might appear;
- what it should never do.

## Do not run a form

Discovery is not a fixed sequence of predetermined questions. For every answer:

1. analyze it;
2. extract every relevant piece of information it contains;
3. update your understanding (and the Master Spec);
4. detect only the important gaps;
5. ask the next question based on those gaps.

A single answer can resolve several design aspects at once. Never re-ask something already answered, and never ask a question whose answer would not change behavior, capabilities, limits, architecture, or results.

## Ask through examples

Whenever useful, ask the user for real usage examples: "Show me a concrete moment where you'd use this. What did you have, what did you do, what came out?"

From an example you internally identify triggers, inputs, expected behavior, results, constraints, exceptions, permissions, and dependencies. The user never has to classify these technically — you do.

## Periodic synthesis

In longer conversations, periodically present a short synthesis of your current understanding so the user can catch misreadings, correct decisions, add information, redefine limits, or confirm direction. Each synthesis updates the Master Spec directly. These are **not** mandatory approval checkpoints — they keep understanding aligned, nothing more.

## Finish criterion

Discovery is complete enough when you can explain, without material gaps:

1. what the future skill receives;
2. what context it can use;
3. what it must do;
4. under what rules;
5. what actions it can take;
6. what it must not do;
7. what it must produce;
8. what exceptional situations it must handle;
9. what criteria make its output acceptable.

You do not need every detail — you need the absence of unknowns that would materially change behavior or architecture.

When this criterion is met, do **not** ask for approval. Continue automatically into Master Spec → Requirements → Capabilities → Architecture → Module design. Return to the user only if a later stage surfaces an ambiguity you cannot resolve reasonably.

## Managing uncertainty during discovery

Classify everything you learn (see [master-spec.md](master-spec.md)) as CONFIRMADO, INFERIDO, PROPUESTO, or DESCONOCIDO. Do not interrogate the user just to eliminate all DESCONOCIDO items. Ask only when an unknown could materially change behavior, capabilities, limits, architecture, or results.
