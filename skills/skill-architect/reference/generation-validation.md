# Generation, validation, and final documentation

This stage runs only after explicit global approval. It creates the real files, validates the result, fixes safe defects, escalates substantial ones, and produces final documentation.

## 1. Generate the real files

Create the actual files of the skill. Generation must respect exactly:

- the approved structure;
- the approved content;
- the approved relationships;
- the approved limits and permissions.

Do not add, drop, or reshape anything that was not in the approved proposal.

## 2. Validate

After the files exist, run a complete validation. At minimum check:

- requirements coverage;
- architectural coherence;
- every referenced file actually exists;
- internal references are valid;
- every workflow has a defined ending;
- responsibilities do not conflict;
- inputs and outputs are defined;
- sources of truth are clear (no duplicated authority);
- failure behavior is defined;
- no unnecessary complexity;
- correspondence with the user's original examples.

## 3. Safe auto-correction

You may fix a defect automatically **only** when the fix does not:

- change approved behavior;
- substantially change the architecture;
- add important new capabilities;
- alter limits or permissions;
- change fundamental decisions.

Examples of safe auto-fixes:

- repairing a broken reference;
- adding a file that was approved but not generated;
- fixing an incorrect path;
- correcting a minor terminology inconsistency;
- repairing an obvious internal connection.

## 4. Substantial changes → re-approve

If fixing a defect requires materially changing behavior, architecture, responsibilities, permissions, restrictions, capabilities, or fundamental structure, **stop the automatic modification**. Rebuild the affected proposal completely and present it again for a **new global approval** (see [proposal-approval.md](proposal-approval.md)). Do not quietly push the change through.

## 5. Final documentation

Once the skill is validated, produce documentation that lets the project be understood **without the original conversation**. Depending on the project, explain: purpose, how it works, usage, capabilities, limits, structure, architecture, files, flows, configuration, tools, examples, extensibility, and troubleshooting.

Do not create ceremonial documentation with no practical value. Document what a future reader actually needs.

## Delivery

Report to the user what was created, where, what validation found, what was auto-fixed, and anything that still needs their decision. If any criterion could not be verified, say so explicitly rather than claiming completion.
