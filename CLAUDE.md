@AGENTS.md

# Claude Code notes

- The policy above is shared with Codex/Kiro; it is the single source. Do not duplicate it here.
- Squad members are Skills: `kiwi`, `lima`, `coco`, `mora-docs` (installed name of `mora`). Invoke them with the Skill tool; `agentes/*/AGENT.md` and `skills/lima/SKILL.md` are their sources. Load only what the runtime contract for the current operation lists.
- Ask product/identity questions with AskUserQuestion; everything else follows the "Missing decisions" rules.
- Repo checks: `node bin/install.mjs install --target claude --dest <tmp> --dry-run`, `node bin/fruti.mjs list`.
- `skills/impeccable` and `skills/lima/vendor/impeccable` are vendored: the Codex-specific notes in their references are harness-conditional; on Claude Code use Skill/AskUserQuestion/Agent equivalents and leave the files untouched.
