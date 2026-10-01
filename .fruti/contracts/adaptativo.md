# Adaptive contract: layout modes vs verification viewports

Read by kiwi (wireframes, F2), lima (adaptive contract, `lima init`) and coco (F3, audit). Moved out of the always-loaded policy; the rules are unchanged.

Two different things share the word "breakpoint":
- **Layout modes** — fixed by the adaptive contract: compact `<600`, medium `600–1023`, expanded `>=1024`. Kiwi and Coco design with these.
- **Verification viewports** — the profile's `breakpoints` / `runtime_qa.viewports`: the widths every piece is verified at (default `[1440, 1024, 768, 390]`). They are not layout thresholds.

A viewport set must cover every mode (at least one `<600`, one in `600–1023`, one `>=1024`); `lima init` warns otherwise. The generated Playwright config derives its projects from the profile viewports.
