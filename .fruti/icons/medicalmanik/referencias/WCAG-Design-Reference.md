# A11Y Experience Guide — WCAG Design Reference

## Purpose

This document is a design-focused accessibility reference for designers, AI agents, LLMs, and human reviewers. It documents all 10 WCAG experience themes used in this application, including every success criterion with its ID, compliance level, WCAG version, plain-language description, and a direct link to the official W3C specification.

**How to use this document:**

- Before finalising any design decision, check each theme that applies to the component or flow being designed.
- Every criterion marked Level A or AA is a legal and functional requirement. Flag any that are not met.
- Criteria marked Level AAA are the gold standard; they are aspirational but should be documented and pursued where feasible.
- Criteria marked **[New in 2.2]** were introduced in WCAG 2.2 (2023) and reflect the current modern standard.

**For AI agents:** When assessing a design, reviewing code, or generating a recommendation from this guide, follow each criterion's Reference link and pull from the official W3C Understanding guidance found there. The descriptions in this file are plain-language summaries; the linked specs contain the normative definitions, exceptions, sufficient techniques, and failure examples that your assessment should be grounded in. Cite the specific criterion (e.g. 1.4.3) in every finding or recommendation.

---

## Compliance Levels

| Level | Name | Requirement |
|-------|------|-------------|
| **A** | Essential | Must be met. Without this, the site is unusable for many people. |
| **AA** | The Standard | The widely adopted legal benchmark. Referenced by laws such as the ADA (USA), AODA (Canada), and EN 301 549 (EU); exact obligations depend on the jurisdiction and the version of the law that applies. |
| **AAA** | Enhanced | The gold standard. Not categorically required by law; pursue wherever feasible, especially for specialized audiences. Aspirational for general consumer products. |

---

## Explore the Guidelines

Click any rule's WCAG number to explore W3C's official examples. All links route to the latest WCAG 2.2 directory, ensuring you always get the most current techniques and modern browser context.

---

## WCAG Versions

| Version | Year | Significance |
|---------|------|-------------|
| **2.0** | 2008 | Foundational standard. Established the core four principles: Perceivable, Operable, Understandable, Robust (POUR). |
| **2.1** | 2018 | Extended 2.0 with 17 new criteria covering mobile, low vision, and cognitive accessibility. |
| **2.2** | 2023 | Current standard. Added 9 new criteria focused on focus appearance, touch targets, and authentication. |

---

## The 10 Experience Themes

---

### 1. Color & Appearance

**Design imperative:** Ensure sufficient contrast and redundant visual cues.

**Beneficiaries:** Users with Color Blindness and Low Vision.

**Why it matters:** Designers often use color to show status (e.g., red for "error"). However, 1 in 12 people are color blind. The design rule is "Redundancy": if color conveys meaning, you must also use a shape, icon, or text label. Additionally, text must have strong contrast against its background.

**Applies to:** All components, Buttons, Status indicators, Text.

#### Rules

| Criterion | Level | Version | Title | Description | Reference |
|-----------|-------|---------|-------|-------------|-----------|
| 1.4.1 | A | 2.0 | Use of Color | Color cannot be the only visual means of conveying information. Do not rely solely on red text to mark an error; add an icon or thick border. | [Understanding 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color) |
| 1.4.3 | AA | 2.0 | Text Contrast | Standard text needs a 4.5:1 contrast ratio against the background. Large text (at least 18pt/24px, or 14pt/18.66px if bold) needs a 3:1 ratio. | [Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum) |
| 1.4.11 | AA | 2.1 | UI Component Contrast | Buttons, input borders, and icons must have a 3:1 contrast ratio against adjacent colors. | [Understanding 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast) |
| 1.4.6 | AAA | 2.0 | Contrast (Enhanced) | For enhanced accessibility, standard text needs a 7:1 contrast ratio, and large text needs 4.5:1. | [Understanding 1.4.6](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced) |

---

### 2. Typography & Reading

**Design imperative:** Support text resizing and avoid sensory-only instructions.

**Beneficiaries:** Users with Low Vision and Dyslexia.

**Why it matters:** Users often increase text size or line spacing to improve readability. If a design uses fixed-height boxes, expanding text will be cut off. The design rule: Allow containers to grow vertically with their content. Never assume a paragraph will stay "3 lines tall".

**Applies to:** All text, Cards, Layout containers.

#### Rules

| Criterion | Level | Version | Title | Description | Reference |
|-----------|-------|---------|-------|-------------|-----------|
| 1.3.3 | A | 2.0 | Sensory Characteristics | Do not rely solely on shape, size, or visual location for instructions (e.g. avoid saying "Click the round button"). | [Understanding 1.3.3](https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics) |
| 1.4.4 | AA | 2.0 | Resize Text | The design must support zooming text up to 200% without overlapping other elements or disappearing off-screen. | [Understanding 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text) |
| 1.4.5 | AA | 2.0 | Images of Text | Use real text code, not images of text, so content can be resized and read by assistive technology. | [Understanding 1.4.5](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text) |
| 1.4.12 | AA | 2.1 | Text Spacing | The layout must not break if the user manually increases line height, paragraph spacing, or letter spacing. | [Understanding 1.4.12](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing) |

---

### 3. Interactive Focus

**Design imperative:** Design visible, controllable states for all interactive and hover elements.

**Beneficiaries:** Keyboard users, Switch Device users, and users with motor disabilities.

**Why it matters:** Keyboard and switch users navigate entirely through interactive states. Designers must ensure every control is reachable and operable without a mouse, never traps focus inside a component, and shows a high-contrast focus indicator that is never hidden by floating headers or banners. Custom tooltips and popovers must also stay stable and dismissible.

**Applies to:** Buttons, Forms, Navigation, Inputs.

#### Rules

| Criterion | Level | Version | Title | Description | Reference |
|-----------|-------|---------|-------|-------------|-----------|
| 2.1.1 | A | 2.0 | Keyboard | Every interactive pattern (menus, modals, date pickers, carousels) must be operable by keyboard alone. Do not design mouse-only interactions. | [Understanding 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard) |
| 2.1.2 | A | 2.0 | No Keyboard Trap | Keyboard focus must never become permanently trapped. Modals need a visible escape: a close button and/or Escape key dismissal. | [Understanding 2.1.2](https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap) |
| 2.4.3 | A | 2.0 | Focus Order | The tab order of interactive elements must match the logical reading order (e.g. left-to-right, top-to-bottom). | [Understanding 2.4.3](https://www.w3.org/WAI/WCAG22/Understanding/focus-order) |
| 2.4.7 | AA | 2.0 | Focus Visible | All interactive elements must have a visible highlight when selected via keyboard. | [Understanding 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible) |
| 1.4.13 | AA | 2.1 | Content on Hover or Focus | Custom tooltips and popovers must be dismissible without moving the mouse, hoverable, and persistent. | [Understanding 1.4.13](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus) |
| 2.4.11 | AA | 2.2 | Focus Not Obscured **[New in 2.2]** | The item receiving focus must not be hidden behind sticky headers, footers, or cookie banners. | [Understanding 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum) |
| 2.4.13 | AAA | 2.2 | Focus Appearance **[New in 2.2]** | The focus indicator needs strong contrast and sufficient thickness to be clearly seen. | [Understanding 2.4.13](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance) |

---

### 4. Touch & Targets

**Design imperative:** Design large clickable areas for finger accuracy.

**Beneficiaries:** Users with tremors or large fingers.

**Why it matters:** Human fingers are imprecise. If a button is visually small (like a standalone icon), the clickable "hotspot" must be larger. New standards require minimum sizes or spacing buffers to prevent users from accidentally tapping the wrong button.

**Applies to:** Mobile interactions, Buttons, Icons, Navigation.

#### Rules

| Criterion | Level | Version | Title | Description | Reference |
|-----------|-------|---------|-------|-------------|-----------|
| 2.5.5 | AAA | 2.1 | Target Size (Enhanced) | The ideal touch target size is at least 44x44 pixels. | [Understanding 2.5.5](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced) |
| 2.5.8 | AA | 2.2 | Target Size (Minimum) **[New in 2.2]** | Targets must be at least 24x24 pixels. If visually smaller, they need spacing so a 24px circle touches nothing else. | [Understanding 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) |

---

### 5. Layout & Structure

**Design imperative:** Ensure visual order matches reading order and supports reflow.

**Beneficiaries:** Screen Reader users and small-screen users.

**Why it matters:** Screen readers read content in the order it appears in the page's code structure, not necessarily the visual arrangement on screen. When elements like navigation or overlapping components could disrupt the intended flow, annotate the correct reading sequence when communicating design intent with development. Also, layouts must reflow vertically on small screens so users don't have to scroll sideways.

**Applies to:** Grids, Layout containers, Responsive breakpoints.

#### Rules

| Criterion | Level | Version | Title | Description | Reference |
|-----------|-------|---------|-------|-------------|-----------|
| 1.3.2 | A | 2.0 | Meaningful Sequence | Visual order must reflect the logical reading order. When page elements like navigation or overlays could introduce a different sequence, the intended reading order must be clearly established. | [Understanding 1.3.2](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence) |
| 1.4.10 | AA | 2.1 | Reflow | Content must reorganize (stack) for small screens (320px width) to avoid horizontal scrolling. | [Understanding 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow) |
| 1.3.4 | AA | 2.1 | Orientation | Do not lock the screen to portrait or landscape mode; support both orientations. | [Understanding 1.3.4](https://www.w3.org/WAI/WCAG22/Understanding/orientation) |

---

### 6. Forms & Friction

**Design imperative:** Provide clear error identification, prevent redundant entry, and design login flows that don't rely on memory alone.

**Beneficiaries:** Users with Memory loss and Cognitive challenges.

**Why it matters:** Forms are high-stress points, including login. Design error messages that clearly identify what went wrong and explain exactly how to fix it. Avoid redundant data entry, and never make cognitive tests the only path into an account. Support alternatives like password managers, pasteable codes, or third-party authentication.

**Applies to:** Forms, Login flows, Inputs, Error states.

#### Rules

| Criterion | Level | Version | Title | Description | Reference |
|-----------|-------|---------|-------|-------------|-----------|
| 3.3.1 | A | 2.0 | Error Identification | If an error is detected, the item must be explicitly identified and the error described in text, not just by color. | [Understanding 3.3.1](https://www.w3.org/WAI/WCAG22/Understanding/error-identification) |
| 3.3.2 | A | 2.0 | Labels or Instructions | Every input needs a visible label or instruction explaining what is required. | [Understanding 3.3.2](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions) |
| 3.3.7 | A | 2.2 | Redundant Entry **[New in 2.2]** | Do not force users to re-type info (like an address) they already entered. Offer a checkbox to copy it or auto-populate it. | [Understanding 3.3.7](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry) |
| 3.3.3 | AA | 2.0 | Error Suggestion | If an input error is detected, suggestions for correction are provided to the user. | [Understanding 3.3.3](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion) |
| 3.3.4 | AA | 2.0 | Error Prevention | For pages that commit data (like deleting or buying), allow users to reverse, check, or confirm the data. | [Understanding 3.3.4](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data) |
| 3.3.8 | AA | 2.2 | Accessible Auth **[New in 2.2]** | Do not make cognitive tests (like memorizing passwords or solving puzzles) the only path to login. Support alternatives such as password managers, pasteable one-time codes, or third-party authentication. | [Understanding 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum) |

---

### 7. Input & Gestures

**Design imperative:** Offer simple tap alternatives for complex gestures and prevent accidental activation.

**Beneficiaries:** Users with limited dexterity.

**Why it matters:** Complex gestures (swiping, dragging, pinching) are impossible for some users. If a design includes a "Drag and Drop" feature or a "Slider", there must also be simple buttons (like Up/Down or +/-) to perform the same action. The one exception: if the gesture is essential to the feature (for example, a freehand drawing or sketching tool), an alternative is not required.

**Applies to:** Sliders, Maps, Carousels, Interactive controls.

#### Rules

| Criterion | Level | Version | Title | Description | Reference |
|-----------|-------|---------|-------|-------------|-----------|
| 2.5.1 | A | 2.1 | Pointer Gestures | Any action requiring a multi-point gesture (pinch) needs a single-tap alternative. | [Understanding 2.5.1](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures) |
| 2.5.7 | AA | 2.2 | Dragging Movements **[New in 2.2]** | Any dragging action (sliders, drag-and-drop) must have a simple click-based alternative. | [Understanding 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements) |
| 2.5.4 | A | 2.1 | Motion Actuation | Functions triggered by moving the device (shaking, tilting) must also be operable by buttons. | [Understanding 2.5.4](https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation) |

---

### 8. Animation & Motion

**Design imperative:** Control time-based content and provide users the ability to pause, extend, or disable it.

**Beneficiaries:** Users with Vestibular Disorders and ADHD.

**Why it matters:** Auto-playing motion can cause severe nausea or distraction, and strict time limits can lock out users who need more time. The golden rules for designers: if content moves automatically beyond 5 seconds, provide a visible Pause or Stop button; if a task has a time limit, let users extend or disable it.

**Applies to:** Video, Animations, Hero sections.

#### Rules

| Criterion | Level | Version | Title | Description | Reference |
|-----------|-------|---------|-------|-------------|-----------|
| 2.2.1 | A | 2.0 | Timing Adjustable | If a time limit exists (session timeout, quiz timer, payment countdown), users must be able to turn it off, adjust it, or extend it via a warning prompt. | [Understanding 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable) |
| 2.2.2 | A | 2.0 | Pause, Stop, Hide | Auto-playing content (carousels, videos) must have user controls to pause or stop it. | [Understanding 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide) |
| 2.3.1 | A | 2.0 | Three Flashes | Content must not flash more than 3 times in any one-second period to avoid seizure risks. | [Understanding 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold) |
| 2.3.3 | AAA | 2.1 | Animation from Interactions | Allow users to disable non-essential cosmetic animations (like parallax scrolling). | [Understanding 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions) |

---

### 9. Navigation & Predictability

**Design imperative:** Keep navigation consistent, prevent unexpected context changes, and give users multiple ways to find what they need.

**Beneficiaries:** Users with Cognitive Disabilities.

**Why it matters:** Users with cognitive challenges rely on predictability. Navigation must stay consistent and offer more than one way to find a page. Interactions must never trigger surprises: focusing or selecting a control should not auto-launch modals, submit forms, or navigate away without warning. If a "Chat" button sits bottom-right on one page, it must be there on all pages.

**Applies to:** Navigation menus, Help mechanisms, Global UI patterns.

#### Rules

| Criterion | Level | Version | Title | Description | Reference |
|-----------|-------|---------|-------|-------------|-----------|
| 2.4.4 | A | 2.0 | Link Purpose | The purpose of each link must be clear. Avoid "Click Here" or "Read More". | [Understanding 2.4.4](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context) |
| 3.2.1 | A | 2.0 | On Focus | Focusing on a component must not trigger an unexpected change of context, such as automatically launching a modal or navigating away. | [Understanding 3.2.1](https://www.w3.org/WAI/WCAG22/Understanding/on-focus) |
| 3.2.2 | A | 2.0 | On Input | Interacting with a UI control must not automatically change the context or submit a form without warning. | [Understanding 3.2.2](https://www.w3.org/WAI/WCAG22/Understanding/on-input) |
| 3.2.6 | A | 2.2 | Consistent Help **[New in 2.2]** | Help mechanisms (Chat, Contact, FAQ) must appear in the same location across all pages. | [Understanding 3.2.6](https://www.w3.org/WAI/WCAG22/Understanding/consistent-help) |
| 2.4.5 | AA | 2.0 | Multiple Ways | Provide more than one way to locate a page (e.g. a navigation menu plus a search bar or robust footer sitemap). | [Understanding 2.4.5](https://www.w3.org/WAI/WCAG22/Understanding/multiple-ways) |
| 2.4.6 | AA | 2.0 | Headings and Labels | Headings and labels must describe the topic or purpose (e.g. "Contact Support" instead of just "Support"). | [Understanding 2.4.6](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels) |
| 3.2.3 | AA | 2.0 | Consistent Navigation | Menus must appear in the same relative order on every page. | [Understanding 3.2.3](https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation) |
| 3.2.4 | AA | 2.0 | Consistent Identification | Components with the same functionality must be identified consistently (e.g. always use the same icon for "Delete"). | [Understanding 3.2.4](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification) |
| 2.4.8 | AAA | 2.0 | Location | Users must be able to determine where they are within a set of pages, through breadcrumbs, a highlighted nav item, or a site map. | [Understanding 2.4.8](https://www.w3.org/WAI/WCAG22/Understanding/location) |

---

### 10. Media & Images

**Design imperative:** Provide text alternatives for images and captions for video.

**Beneficiaries:** Blind users and Deaf users.

**Why it matters:** Blind users cannot see images; Deaf users cannot hear video. Designers must decide: Is this image decorative (eye candy)? If yes, mark it to be ignored. Is it informative? If yes, provide a text description.

**Applies to:** Images, Video, Audio, Icons.

#### Rules

| Criterion | Level | Version | Title | Description | Reference |
|-----------|-------|---------|-------|-------------|-----------|
| 1.1.1 | A | 2.0 | Non-text Content | Images need text descriptions. Decorative images should be hidden from assistive technology. | [Understanding 1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content) |
| 1.2.2 | A | 2.0 | Captions | Videos with audio must have visual captions. | [Understanding 1.2.2](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded) |
| 1.4.2 | A | 2.0 | Audio Control | Any audio that auto-plays for more than 3 seconds must have a mechanism to pause or stop it. | [Understanding 1.4.2](https://www.w3.org/WAI/WCAG22/Understanding/audio-control) |

---

## Future Standards & AI (WCAG 3.0 / Project Silver)

**Design imperative:** Prepare for scoring-based compliance and AI-mediated user experiences.

**Beneficiaries:** Everyone, enhanced by AI agents navigating digital ecosystems on their behalf.

**Why it matters:** The future of accessibility (WCAG 3.0 / Project Silver) is expanding far beyond the browser. Instead of retrofitting web guidelines to fit new technologies, the next generation natively covers mobile apps, digital products, authoring tools, and emerging spaces like VR/XR. It also acknowledges that the legacy pass/fail system is too rigid. The new model proposes scoring experiences (Bronze, Silver, Gold) based on holistic functional user needs. Even as this new paradigm emerges, the established WCAG 2.x standards will remain the baseline for global legal compliance. Simultaneously, AI is reshaping the landscape. Interfaces must be transparent about AI usage, and code must be semantically rich enough for AI agents to navigate on behalf of users.

### Emerging Concepts

**Holistic Scoring (WCAG 3.0)**
Moving away from binary A/AA/AAA checklists to a point-based system. A site might "pass" even with minor failures if the overall functional user journey is successful and robust.

**AI Transparency**
Users must be clearly informed when they are interacting with AI (chatbots, content). This aligns with emerging regulations like the EU AI Act.

**Agent-Ready Semantics**
AI Agents browse the web for humans. Semantic HTML is no longer just for screen readers; it is the API for AI. Clean code = AI Optimization.

**Human Verification**
AI tools can generate Alt Text and fix code, but they hallucinate. A new design principle: "AI-generated accessibility artifacts must be human-verified."

---

## Agent Instructions

When using this document to review or produce a design:

1. **Follow the spec links.** For every criterion you assess, open its Reference link and base your evaluation on the official W3C Understanding guidance found there: normative wording, exceptions, sufficient techniques, and documented failures. Do not rely only on the summaries in this file.

2. **Check every applicable theme.** For each component, flow, or screen being designed, identify which of the 10 themes apply and verify every Level A and Level AA criterion is met.

3. **Flag Level A or AA failures immediately.** These are not optional. A design that fails Level A is not accessible. A design that fails Level AA does not meet legal standards in most jurisdictions. Do not deliver a design with unresolved A or AA failures.

4. **Document AAA gaps.** Where Level AAA criteria are not met, note them explicitly so the team can make an informed decision. Pursue them wherever feasible.

5. **Prioritize WCAG 2.2 criteria.** Criteria marked [New in 2.2] reflect the current 2023 standard. These are increasingly required by updated regulations and should be treated with the same urgency as older AA criteria.

6. **Apply the redundancy principle broadly.** Never rely on a single sensory modality (color alone, shape alone, sound alone) to convey meaning. Always pair it with a second modality (color + icon, color + text, audio + caption).

7. **Design for the pause.** Any animation, motion, or audio that plays automatically must have an immediately visible stop, pause, or mute control. Do not bury it in settings.

8. **Verify with humans.** AI can miss nuances and hallucinate guidance. Cite criteria in every recommendation, and treat automated assessments as a starting point that requires manual testing and human review.
