# Kiwi · UX Architect

**By Fruti Squad** · Part of the Fruti Squad workflow (Kiwi → Lima → Coco → Mora)

> Structure before appearance: functional brief, user flow and grayscale wireframes for every screen size, before anyone picks a color.

**Price:** _set in the marketplace_ · **Works with:** Claude Code · Codex · Kiro

---

## Gallery

1. `agentes/kiwi/assets/wireframe-base-preview.png`: the wireframe workbench (space selector, state panel, decision notes).
2. Dashboard pattern at expanded 1440 px.
3. Same dashboard at compact 393 px: the attention block moves up, the primary action moves to the bottom bar.

---

## Example session

**User**

> Design the dashboard for my online store. I want to see how sales are going and what needs my attention today.

**Kiwi worked**

- Read the project profile and existing routes.
- Wrote the functional brief.
- Chose route R1 and fidelity F2 (structure, content and states, no visual design).
- Built the wireframe and ran `check_artifact.py`.

**Output (excerpt)**

```
FUNCTIONAL BRIEF
User:       store owner, checks the dashboard several times a day
Design question: what needs my attention now, and how are we doing?
Main verb:  review pending issues
Dominant:   "Needs attention" list (the only block that asks for a decision)
States:     loading · empty (new account) · empty (no data in period)
            partial error (one widget) · error · no permission · offline · long content
Spaces:     expanded 1440 · medium 834 · compact 393 (declared reference)

WIREFRAME F2 · dashboard · r01
expanded  KPIs 4 cols · chart 2/3 + attention 1/3 · latest orders table
medium    KPIs 2 cols · attention above the chart
compact   attention first after KPIs · table stacks as cards · primary in bottom bar

CHECK  0 errors · one primary action per view · no color
NEXT   handoff to Lima (contracts and tokens)
```

---

## About this skill

### The problem

Ask an AI agent for a screen and it jumps straight to colors, cards and gradients. The structure underneath (what the user needs to decide, which states exist, what happens on a phone) gets decided by accident, and you find out when it is expensive to change.

### What it does

- Writes a **functional brief** first: user, task, design question, main verb, dominant data, states, permissions and risk per action.
- Draws the **user flow** when there is more than one screen: entry, decisions, error paths and recovery.
- Picks the **lowest fidelity that answers the question** (F0 flow, F1 lo-fi, F2 mid-fi) and says why.
- Builds **grayscale HTML wireframes** with a space selector (compact, medium, expanded), a state panel and decision notes.
- Designs **every required state**: loading, empty, filtered empty, error, no permission, offline and long content.
- Offers **A/B/C alternatives** that differ in structure, hierarchy or interaction, never just in color.
- Verifies the result with `check_artifact.py` (grays only, one font family, one primary action, states present) and hands a **geometry contract** to Lima.

### Why this beats prompting it yourself

A prompt asks for a screen; Kiwi runs a protocol. Each phase produces something the next one needs, and a wireframe without a brief is invalid by rule. Color is kept out on purpose, so the conversation stays on structure. Responsive behavior is decided per space (what moves, collapses or hides), not by shrinking the desktop.

### Use cases

- Planning a new feature or screen before visual design.
- Restructuring an existing view that grew messy.
- Making a desktop flow work on mobile, as a PWA or offline.
- Comparing three structural directions with a client or team.

### Known limitations

- Does not do visual design, branding or final UI (that is Coco, with your real design system).
- Does not write production code.
- Wireframes are HTML for review in a browser, not Figma files.
- Works best with a Lima project profile; without one it uses declared reference sizes (393 / 834 / 1440).
- Product decisions stay with you: when a business rule is missing, Kiwi asks or marks it as unknown instead of inventing it.

`ux` `wireframes` `user-flow` `responsive` `accessibility` `design-process`

---

## How to use

1. **Install** in your project:
   ```bash
   npx github:kevinedgm/fruti-squad setup --target claude   # or codex, kiro
   ```
2. **Ask in plain language**: "sketch the signup flow", "how would this screen work on mobile?", "give me A/B/C options for the checkout".
3. **Review and approve**: open the wireframe in your browser, switch spaces and states, then approve one direction. Kiwi hands it to Lima.

---

## FAQ

**What exactly do I get?**
A functional brief (Markdown), a user flow when needed, an HTML wireframe with all required states and three space modes, a compliance statement and a handoff file for the next agent.

**Does it design the final look of my app?**
No. Kiwi stops at structure. Colors, typography and final components come later, from your real design system.

**Can I use Kiwi without the rest of the squad?**
Yes. Kiwi works alone; the handoff is simply ready if you add Lima, Coco and Mora later.

**Does it guarantee accessibility?**
No. It designs for WCAG 2.2 AA (focus order, target sizes, states that do not rely on color) and checks what can be checked in a wireframe. Final accessibility is verified on the built interface.

**Which agents does it work with?**
Claude Code, Codex and Kiro, through the Fruti Squad installer.

**Will it ask me a lot of questions?**
Only what changes the structure (task, data, states, permissions), in a single message. It reads your repository first and does not ask what the code already answers.

---

## What's inside

```
kiwi/
├── AGENT.md                     protocol (6 phases)
├── assets/
│   ├── wireframe-base.html      workbench template
│   ├── wireframe-kit.css        grayscale kit
│   ├── patterns/dashboard.html  ready-made dashboard pattern
│   └── plantillas/              brief · flow · findings · statement · handoff
├── references/                  brief · flow · fidelity · wireframing · validation · geometry contract · web/PWA · vue-adaptive
└── scripts/check_artifact.py    wireframe checker
```

---

## Creator

_Fruti Squad · bio to be provided by the author._
