# Proposal and global approval

After architecture and module design are complete, build a **complete representation of the project** and present it for a single global approval. This is the one mandatory approval gate, and it happens before any real file is created.

## Build the full project design

### 1. Project tree

Present the real structure the skill will have. The example below is illustrative only — the actual shape depends on the project's needs:

```text
nombre-skill/
├── SKILL.md
├── README.md
├── reference/
│   ├── workflows/
│   ├── policies/
│   └── evaluators/
├── schemas/
├── examples/
└── tests/
```

Include only the files and folders the requirements justify. A simple skill may be just `SKILL.md` and `README.md`.

### 2. Complete file content

Present the **full proposed content of every file** — not names, not descriptions, not summaries, not placeholders. What you show for approval must be the actual skill that will be generated. If a file is worth existing, its real content is worth showing.

## The approval gate

The user must be able to evaluate: structure, architecture, files, content, responsibilities, flows, rules, and documentation.

- Approval is **global for the whole project**.
- There is never a state where some files are approved and others are not.
- Do not create any real file until you have explicit global approval.

Ask plainly, e.g.: "Here is the complete project. Do you approve it as a whole, or do you want changes first?"

## Handling revision requests

If the user asks for changes:

1. update the affected parts;
2. check the repercussions on the rest of the system (references, sources of truth, module boundaries, flows);
3. update the complete proposal;
4. re-present the project as one coherent unit.

The project stays **not approved** until global approval exists. Never treat prior partial agreement as approval of the whole.

## After approval

Once global approval is explicit, proceed to generation exactly as approved. See [generation-validation.md](generation-validation.md).
