# Profile — Tallerio / Brezo (EXAMPLE)

Example of a complete, filled-in profile for a **fictional** project (Tallerio: a public directory of independent repair workshops with online booking; Brezo design system, Tallerio Design Hub, Vue 3 + Tailwind). It is **not** an active profile for any repo — it lives under `profiles/examples/` to show the level of detail a finished profile reaches. To start a project, copy `profiles/_TEMPLATE.md` to `profiles/<your-project>.md` and fill it by inspecting your repo (see `references/first-run.md`).

```yaml
name: Tallerio / Brezo
design_system: Brezo
truth_sources:
  - docs/brezo-mockup.html           # canonical mockup
  - frontend/tailwind.config.js      # tokens
  - Tallerio Design Hub/brezo.css    # Hub stylesheet
color_law: >
  canvas #F4F3F0, paper #FFFFFF, ink #1A1C1E.
  ámbar #FFB020 ONLY for the booking action / active state.
  azul #2F5BEA for categories, verified, focus, accents.
  rojo #E5484D ONLY for save/favorite. success #1E7F4F. rating star #F2A900.
  If an element is neither action nor favorite, it is ink on paper.
  Shadow means elevation, never decoration.
type_law: >
  Inter Tight across the system. Fraunces only for logo/brand
  and workshop names over photography.
hub_root: Tallerio Design Hub
hub_layout:
  - Design System/{Botones,Colores,Componentes,Estados,Iconos,Inputs,Tipografía}
  - Responsive/{Desktop,Tablet,Phone,Wide}
  - Patrones UX
  - Flujos
  - Wireframes
registry_path: Tallerio Design Hub/system/registry.json
production:
  detect: true
  known_stack: >
    Vue 3 <script setup lang="ts"> + TypeScript + TailwindCSS + PWA (Vite),
    icons via lucide-vue-next, no heavy UI framework. Confirm by inspection each time.
  token_binding: Map Brezo tokens to frontend/tailwind.config.js; never hardcode values.
  component_layout: frontend/src/components/ (+ packages/* for shared), match existing naming.
impeccable_path: .agents/skills/impeccable
runtime_qa:
  enabled: true
  runner: playwright
  harness_root: Tallerio Design Hub/qa    # owns package.json, playwright.config.js, tests/
  hub:
    start_command: "python3 -m http.server 4321 --directory ."   # from harness cwd; serves the Hub root
    base_url: "http://localhost:4321"
  tests_root: Tallerio Design Hub/qa/tests
  evidence_root: Tallerio Design Hub/qa/evidence
  viewports: [1440, 1024, 768, 390]
```

Notes:
- WCAG AA is a project requirement (PRODUCT.md): contrast, visible focus, keyboard, touch targets ≥44px on mobile, meaning never carried by color alone.
- Deprecated aesthetics (verde neón/Poppins, gris pizarra/Roboto) are anti-references; never reintroduce them.
