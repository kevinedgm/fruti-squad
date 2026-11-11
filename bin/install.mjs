#!/usr/bin/env node
// Fruti Squad installer/setup — kiwi → lima → coco → bruno → mora, for Kiro, Claude Code, Codex.
// Zero dependencies.
//   npx github:kevinedgm/fruti-squad setup   --target kiro --intake my-intake.yaml
//   npx github:kevinedgm/fruti-squad install --target kiro
//
// Commands:
//   setup    install + init (lima) + append coco:/mora: blocks to the profile   (one shot)
//   install  copy the squad into a project (or --global)
//   update   like install, but renews what belongs to the squad and keeps yours (profiles, state,
//            handoffs). With --dry-run it lists every file as new / changes / same / obsolete.
//   list     show installable members and per-target paths
//   help     show help
//
// Targets (where each member lands):
//   kiro    members -> .kiro/skills/<n>/ (agents get a SKILL.md bridge)
//           + .kiro/agents/<n>.md (one Kiro agent per member, least privilege) + .kiro/agents/fruti.md
//           (orchestrator, delegates with the subagent tool) + .kiro/steering/fruti-squad.md
//   claude  skills -> .claude/skills/<n>/     agents -> .claude/skills/<n>/  (as skills)
//           + CLAUDE.md block (imports .fruti/policy.md) + .fruti/paths.yaml
//   codex   skills -> .codex/skills/<n>/      agents -> .codex/skills/<n>/   + AGENTS.md block
//
// Flags:
//   --target <env>  kiro | claude | codex  (default: autodetect, else kiro)
//   --intake <f>    (setup) intake YAML for lima's init -> a COMPLETE profile
//   --qa <runner>   (setup) passed to lima init, e.g. playwright | none
//   --global        install user-wide (~ instead of the project root)
//   --dest <dir>    target project root (default: current working directory)
//   --only <names>  comma list (default: kiwi,lima,coco,bruno,mora). Extra: impeccable,
//                   improve-animations, skill-architect
//   --force         overwrite existing destinations
//   --dry-run       print actions, change nothing

import { cpSync, existsSync, mkdirSync, readFileSync, writeFileSync, appendFileSync, readdirSync, statSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, resolve } from 'node:path';
import { homedir, tmpdir } from 'node:os';
import { spawnSync } from 'node:child_process';
import { createInterface } from 'node:readline';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PKG_ROOT = resolve(__dirname, '..');

const MEMBERS = {
  lima:                 { from: 'skills/lima',               kind: 'skill', blurb: 'gobierna: clasifica, reutiliza, registra y decide el estado de cada pieza' },
  impeccable:           { from: 'skills/impeccable',         kind: 'skill', blurb: 'playbooks de refinamiento de UI' },
  'improve-animations': { from: 'skills/improve-animations', kind: 'skill', blurb: 'micro-interacciones y animación' },
  'skill-architect':    { from: 'skills/skill-architect',    kind: 'skill', blurb: 'creación de nuevas skills' },
  kiwi:                 { from: 'agentes/kiwi',              kind: 'agent', blurb: 'estructura: brief, user flow y wireframes F0–F2 adaptativos con traspaso a lima' },
  coco:                 { from: 'agentes/coco',              kind: 'agent', blurb: 'capa visual: alta fidelidad (F3) con el sistema real y su CSS; auditoría canónica (R0)' },
  bruno:                { from: 'agentes/bruno',             kind: 'agent', blurb: 'implementa el comportamiento (R3): API, eventos, estado, teclado, foco y ARIA' },
  mora:                 { from: 'agentes/mora',              kind: 'agent', blurb: 'documenta lo implementado y sincroniza el Design Hub (último paso del flujo)' },
  mango:                { from: 'agentes/mango',             kind: 'agent', blurb: 'compone y corrige pantallas reales: alineación, ayudas, separadores, adaptación e integración de las piezas con lo que ya había (fuera de la ronda)' },
};
const DEFAULT = ['kiwi', 'lima', 'coco', 'bruno', 'mora', 'mango'];
// Members that work directly in the conversation and are not stages of a design round.
const OUTSIDE_ROUND = ['mango'];
const TARGETS = ['kiro', 'claude', 'codex'];

const C = {
  reset: '\x1b[0m', bold: '\x1b[1m', dim: '\x1b[2m',
  green: '\x1b[32m', yellow: '\x1b[33m', red: '\x1b[31m', cyan: '\x1b[36m',
};
const log = (...a) => console.log(...a);
const ok = (s) => `${C.green}${s}${C.reset}`;
const warn = (s) => `${C.yellow}${s}${C.reset}`;
const err = (s) => `${C.red}${s}${C.reset}`;

// WCAG relative-luminance contrast, used to warn when text on the action color would fail AA.
function contrastRatio(a, b) {
  const lum = (h) => {
    const c = [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16) / 255)
      .map((v) => (v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4));
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  };
  const [x, y] = [lum(a), lum(b)];
  return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
}

function parseArgs(argv) {
  const args = { _: [], target: null, intake: null, qa: null, global: false, force: false, dryRun: false, update: false, dest: null, only: null };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--global') args.global = true;
    else if (a === '--force') args.force = true;
    else if (a === '--dry-run') args.dryRun = true;
    else if (a === '--target') args.target = argv[++i];
    else if (a === '--intake') args.intake = argv[++i];
    else if (a === '--qa') args.qa = argv[++i];
    else if (a === '--dest') args.dest = argv[++i];
    else if (a === '--only') args.only = argv[++i];
    else if (a === '-h' || a === '--help') args._.push('help');
    else args._.push(a);
  }
  return args;
}

function helpText() {
  return `
${C.bold}🍓 Fruti Squad${C.reset} — kiwi → lima → coco → bruno → mora  (Kiro · Claude Code · Codex)

${C.bold}Commands${C.reset}
  ${C.bold}setup${C.reset}          One shot: install + init (lima) + append coco:/mora: to the profile
  install        Copy the squad into a project (or --global)
  update         Renew the squad's files, keep yours; with --dry-run list new / changes / same / obsolete
  list           Show installable members and per-target paths
  path <p>       Resolve a package-relative path (skills/..., agentes/...) via .fruti/paths.yaml
  fidelity       FID-GEOMETRY-001: compare Kiwi F2 vs Coco F3 geometry (--f2 <html> --f3 <html|URL>)
  help           Show this help

${C.bold}Options${C.reset}
  --target <env>   kiro | claude | codex   (default: autodetect, else kiro)
  --intake <file>  (setup) intake YAML -> lima writes a COMPLETE profile
  --qa <runner>    (setup) playwright | none   (default: playwright)
  --global         Install user-wide (home dir instead of project root)
  --dest <dir>     Target project root (default: current directory)
  --only <names>   Comma list (default: kiwi,lima,coco,bruno,mora). Extra: impeccable,
                   improve-animations, skill-architect
  --force          Overwrite existing destinations
  --dry-run        Show actions without changing anything

${C.bold}Recommended (one command)${C.reset}
  npx github:kevinedgm/fruti-squad setup --target kiro --intake my-intake.yaml
  npx github:kevinedgm/fruti-squad setup --target claude          # intake conversacional después

${C.bold}Manual (step by step)${C.reset}
  npx github:kevinedgm/fruti-squad install --target codex
  npx github:kevinedgm/fruti-squad list
  npx github:kevinedgm/fruti-squad update --target kiro --dry-run
`;
}

function autodetectTarget(dest) {
  const home = homedir();
  const has = (p) => existsSync(p);
  if (has(join(dest, '.kiro')) || has(join(dest, '.agents'))) return 'kiro';
  if (has(join(dest, '.claude')) || has(join(home, '.claude'))) return 'claude';
  if (has(join(dest, '.codex')) || has(join(home, '.codex')) || has(join(dest, 'AGENTS.md'))) return 'codex';
  if (has(join(home, '.kiro'))) return 'kiro';
  return 'kiro';
}

function resolveRoot(target, kind, base) {
  switch (target) {
    case 'kiro':
      // Kiro guide: procedures (with references/) are skills; .kiro/agents holds only agent definitions.
      return join(base, '.kiro', 'skills');
    case 'claude':
      return join(base, '.claude', 'skills');
    case 'codex':
      return join(base, '.codex', 'skills');
    default:
      return join(base, '.agents', 'skills');
  }
}

function selectedMembers(args) {
  if (!args.only) return DEFAULT.slice();
  const names = args.only.split(',').map((s) => s.trim()).filter(Boolean);
  const unknown = names.filter((n) => !MEMBERS[n]);
  if (unknown.length) {
    log(err(`Unknown member(s): ${unknown.join(', ')}`));
    log(`Known: ${Object.keys(MEMBERS).join(', ')}`);
    process.exit(2);
  }
  return names;
}

function installedMemberName(name, target) {
  // `mora` is also the name of an unrelated Verdant governance skill.
  // Keep the Kiro agent command for compatibility, but avoid skill-name collisions.
  return name === 'mora' && (target === 'claude' || target === 'codex') ? 'mora-docs' : name;
}

// SKILL.md generated from an agent's AGENT.md so every target can load it as a skill.
function bridgeFor(agentText, name) {
  const fm = agentText.match(/^---\n([\s\S]*?)\n---\n?/);
  let description = `Fruti Squad member ${name}.`;
  if (fm) {
    const dm = fm[1].match(/^description:\s*(.*)$/m);
    if (dm) description = dm[1].trim().replace(/^["']|["']$/g, '');
  }
  const body = fm ? agentText.slice(fm[0].length) : agentText;
  return `---\nname: ${name}\ndescription: ${JSON.stringify(description)}\n---\n\n<!-- Generated by fruti-squad installer as a SKILL.md bridge. Source of truth: AGENT.md in this folder. -->\n${body}`;
}

function ensureSkillBridge(dest, name) {
  const agentPath = join(dest, 'AGENT.md');
  if (!existsSync(agentPath)) return;
  writeFileSync(join(dest, 'SKILL.md'), bridgeFor(readFileSync(agentPath, 'utf8'), name));
}

// ---- Tracked writes: every file is reported as new / changes / same, so update --dry-run is a real diff ----
const tally = { nuevo: 0, cambia: 0, igual: 0, omitido: 0, obsoleto: 0, migrado: 0 };
function report(kind, label, path, dryRun) {
  tally[kind]++;
  const word = { nuevo: dryRun ? 'nuevo' : 'ok', cambia: dryRun ? 'cambia' : 'renovado', igual: 'igual', omitido: 'omitido', obsoleto: 'obsoleto', migrado: dryRun ? 'migraría' : 'migrado' }[kind];
  const color = kind === 'igual' ? C.dim : kind === 'omitido' || kind === 'obsoleto' ? C.yellow : kind === 'nuevo' ? C.green : C.cyan;
  log(`  ${color}${word.padEnd(9)}${C.reset}${label} ${C.dim}${path}${C.reset}`);
}
function filesOf(p) {
  if (!existsSync(p)) return [];
  if (!statSync(p).isDirectory()) return [''];
  const out = [];
  for (const e of readdirSync(p)) for (const f of filesOf(join(p, e))) out.push(f ? join(e, f) : e);
  return out;
}
// Same when every file of the package copy exists in the project with equal bytes. Files the project
// added (lima profiles, registry) do not count: they are the user's and are never touched.
function sameContent(src, dest, extra = {}) {
  if (!existsSync(dest)) return false;
  if (!statSync(src).isDirectory()) return readFileSync(src).equals(readFileSync(dest));
  const okFiles = filesOf(src).every((f) => existsSync(join(dest, f)) && readFileSync(join(src, f)).equals(readFileSync(join(dest, f))));
  return okFiles && Object.entries(extra).every(([f, c]) => existsSync(join(dest, f)) && readFileSync(join(dest, f), 'utf8') === c);
}
// renew: the file is the squad's (runtime contracts, policy) and is always refreshed.
function trackedCopy(src, dest, args, label, { renew = false, extra = {}, after } = {}) {
  const existe = existsSync(dest);
  const kind = !existe ? 'nuevo' : sameContent(src, dest, extra) ? 'igual' : 'cambia';
  if (kind === 'igual') { report('igual', label, dest, args.dryRun); return true; }
  if (kind === 'cambia' && !renew && !args.force && !args.update) { report('omitido', `${label} — ya existe con otro contenido (usa update)`, dest, args.dryRun); return false; }
  if (!args.dryRun) { mkdirSync(dirname(dest), { recursive: true }); cpSync(src, dest, { recursive: true, force: true }); if (after) after(); }
  report(kind, label, dest, args.dryRun);
  return true;
}
function trackedWrite(dest, content, args, label, { renew = false } = {}) {
  const existe = existsSync(dest);
  const kind = !existe ? 'nuevo' : readFileSync(dest, 'utf8') === content ? 'igual' : 'cambia';
  if (kind === 'igual') { report('igual', label, dest, args.dryRun); return; }
  if (kind === 'cambia' && !renew && !args.force && !args.update) { report('omitido', `${label} — ya existe con otro contenido (usa update)`, dest, args.dryRun); return; }
  if (!args.dryRun) { mkdirSync(dirname(dest), { recursive: true }); writeFileSync(dest, content); }
  report(kind, label, dest, args.dryRun);
}

// Writes/refreshes a fenced fruti-squad block in a project instruction file
// (AGENTS.md for Codex, CLAUDE.md for Claude Code), preserving everything else.
function writeInstructionBlock(base, fileName, lines, dryRun) {
  const file = join(base, fileName);
  const start = '<!-- fruti-squad:start -->';
  const end = '<!-- fruti-squad:end -->';
  const block = [start, ...lines, end].join('\n');
  if (dryRun) { log(`  ${C.cyan}would update${C.reset} ${fileName} ${C.dim}(fruti-squad block)${C.reset}`); return; }
  let content = existsSync(file) ? readFileSync(file, 'utf8') : '';
  if (content.includes(start) && content.includes(end)) {
    content = content.replace(new RegExp(start + '[\\s\\S]*?' + end), () => block);
    writeFileSync(file, content);
  } else {
    const sep = content && !content.endsWith('\n') ? '\n\n' : (content ? '\n' : '');
    appendFileSync(file, sep + block + '\n');
  }
  log(`  ${ok('ok')}    ${fileName} ${C.dim}(fruti-squad block written)${C.reset}`);
}

function squadLines(members, target, skillsRootRel) {
  return [
    '## Fruti Squad (kiwi → lima → coco → bruno → mora)',
    '',
    'Este proyecto incluye el Fruti Squad en `' + skillsRootRel + '`. Cada carpeta tiene su `SKILL.md`/`AGENT.md`; léelos cuando la tarea lo pida:',
    '',
    ...members.map((n) => {
      const installed = installedMemberName(n, target);
      return `- **${installed}** — ${MEMBERS[n].blurb} → \`${skillsRootRel}/${installed}/\``;
    }),
    '',
    'Flujo: **kiwi estructura → lima gobierna → coco construye la capa visual → bruno implementa el comportamiento → coco audita → mora documenta.** Cada uno se dedica a una actividad y todos usan el perfil de proyecto de lima (`' + skillsRootRel + '/lima/profiles/<proyecto>.md`).',
    ...(members.includes('mango') ? ['Fuera de la ronda: **mango** compone y corrige pantallas reales del producto directamente en la conversación ("usa mango: agrega separadores al formulario de alta").'] : []),
    // Claude imports the policy with @; Codex has no import syntax, so it gets an explicit read instruction.
    ...(target === 'codex' ? ['', 'Antes de la primera tarea de diseño/UI lee `.fruti/policy.md` (política de ruteo: rutea primero, lee después; fuentes aprobadas; handoffs compactos). Rutas reales de skills/agentes: `.fruti/paths.yaml`.'] : []),
  ];
}

function writeCodexAgentsMd(base, members, skillsRootRel, dryRun) {
  writeInstructionBlock(base, 'AGENTS.md', squadLines(members, 'codex', skillsRootRel), dryRun);
}

// Kiro reads .kiro/steering/*.md; `always` keeps it working in the CLI, which ignores inclusion modes.
// The file is only a pointer so the always-on cost stays a few lines; custom agents get the policy via resources.
function kiroSteering() {
  return [
    '---',
    'inclusion: always',
    '---',
    '',
    '# Fruti Squad (kiwi → lima → coco → bruno → mora)',
    '',
    'Antes de la primera tarea de diseño/UI lee `.fruti/policy.md` (política de ruteo: rutea primero, lee después; fuentes aprobadas; handoffs compactos). Rutas reales de skills/agentes: `.fruti/paths.yaml`.',
    'Para una ronda completa usa el agente `fruti`, que lanza a cada miembro como subagente; para un solo paso, el agente del miembro.',
    'Para corregir o integrar una pantalla real del producto, usa el agente `mango` directamente (no es parte de la ronda).',
    '',
  ].join('\n');
}

// Kiro custom agents (guide "Kiro — Agents, Skills & Steering"): one agent per member with only the
// tools its job needs (least privilege), its own skill via skill://, the shared policy/state via file://.
// Design-system work lives in .fruti/; coco and bruno also write the product's CSS and components.
const KIRO_READ = ['ls *', 'cat *', 'head *', 'tail *', 'grep *', 'rg *', 'find *', 'wc *', 'git status', 'git log*', 'git diff*', 'git show*'];
const KIRO_RUN = ['npm test*', 'npm run *', 'node *', 'npx fruti*', 'npx playwright*', 'python3 *', 'bash *'];
const KIRO_SHELL_DENY = ['rm -rf *', 'sudo *', 'git push*', 'git reset --hard*', 'git clean*', 'git checkout -- *'];
const KIRO_AGENTS = {
  kiwi: { description: 'Fruti Squad structure and UX agent (F0-F2).', welcome: 'Kiwi · Structure — structure, flow and adaptation come first (F0-F2).', tools: ['read', 'write', 'shell', 'web'], writes: ['.fruti/**'], shell: [...KIRO_READ, 'npx fruti*', 'node *'] },
  lima: { description: 'Fruti Squad governance agent: classification, contracts, tokens, registry, gates and lifecycle.', welcome: 'Lima · Governance — I classify and set contracts, tokens, registry and gates.', extraSkills: ['impeccable'], tools: ['read', 'write', 'shell'], writes: ['.fruti/**', '.kiro/skills/lima/profiles/**', '**/registry.json', 'design-hub/**'], shell: [...KIRO_READ, 'npx fruti*', 'node *', 'bash *'] },
  coco: { description: 'Fruti Squad visual layer (F3/CSS) and canonical audit (R0) agent.', welcome: 'Coco · UI Audit — I build the visual layer and audit it against the contract.', tools: ['read', 'write', 'shell', 'web'], writes: ['**'], shell: [...KIRO_READ, ...KIRO_RUN] },
  bruno: { description: 'Fruti Squad frontend implementation agent (R3): API, events, state, keyboard, focus and functional ARIA.', welcome: 'Bruno · Implementation — I turn the approved piece into real frontend behavior.', tools: ['read', 'write', 'shell'], writes: ['**'], shell: [...KIRO_READ, ...KIRO_RUN] },
  mango: { description: 'Fruti Squad screen composer: integrates and corrects real product screens (alignment, helper text, separators, adaptation, integration with existing code). Works directly, outside the design round.', welcome: 'Mango · Composer — tell me the screen and what is wrong; I fix it in the code.', tools: ['read', 'write', 'shell', 'web'], writes: ['**'], shell: [...KIRO_READ, ...KIRO_RUN, 'date*', 'printf *', 'mkdir -p .fruti/logs*'] },
  mora: { description: 'Fruti Squad documentation agent; publishes implemented, verified truth.', welcome: 'Mora · Docs — I document only what is implemented and verified.', tools: ['read', 'write', 'shell'], writes: ['.fruti/**', 'design-hub/**', 'docs/**'], shell: [...KIRO_READ, 'npx fruti*', 'node *'] },
};
// Members that only write design-system files run as subagents without an approval prompt; coco and
// bruno write product code, so the user approves them.
const KIRO_TRUSTED = ['kiwi', 'lima', 'mora'];

function kiroPermissions(spec) {
  const q = (x) => JSON.stringify(x);
  const list = (xs) => `[${xs.map(q).join(', ')}]`;
  return [
    'permissions:',
    '  rules:',
    '    - capability: fs_read',
    '      match: ["**"]',
    '      effect: allow',
    '    - capability: fs_write',
    `      match: ${list(spec.writes)}`,
    '      effect: allow',
    '    - capability: fs_write',
    '      match: [".env*", "**/.env*", ".git/**"]',
    '      effect: deny',
    '    - capability: shell',
    `      match: ${list(spec.shell)}`,
    '      effect: allow',
    '    - capability: shell',
    `      match: ${list(KIRO_SHELL_DENY)}`,
    '      effect: deny',
  ];
}

function kiroAgentDefinition(name, base, members, target = 'kiro') {
  const spec = KIRO_AGENTS[name];
  const rel = (p) => (p.startsWith(base) ? p.slice(base.length + 1) : p).replace(/\\/g, '/');
  const own = join(resolveRoot(target, MEMBERS[name].kind, base), installedMemberName(name, target), 'SKILL.md');
  const resources = ['file://.kiro/steering/fruti-squad.md', 'file://.fruti/policy.md', 'file://.fruti/state/current.json', 'file://.fruti/handoffs/current.json',
    'skill://' + rel(own)];
  for (const extra of spec.extraSkills || []) if (members.includes(extra)) resources.push('skill://' + rel(join(resolveRoot(target, 'skill', base), extra, 'SKILL.md')));
  return [
    '---',
    `name: ${name}`,
    `description: ${JSON.stringify(spec.description)}`,
    `welcomeMessage: ${JSON.stringify(spec.welcome)}`,
    `tools: [${spec.tools.map((t) => JSON.stringify(t)).join(', ')}]`,
    'resources:',
    ...resources.map((r) => `  - ${r}`),
    ...kiroPermissions(spec),
    '---',
    '',
    `# ${name}`,
    '',
    `Use \`${rel(own)}\` as the normative procedure and \`.fruti/runtime/${name}.yaml\` as the compact router. Read only the references needed for the active operation. Respect the current handoff and do not take on responsibilities that belong to another squad member.`,
    '',
  ].join('\n');
}

// Orchestrator: runs a full round by delegating each stage to the member's agent with the subagent tool.
function kiroOrchestrator(members) {
  const agents = members.filter((n) => KIRO_AGENTS[n] && !OUTSIDE_ROUND.includes(n));
  const list = (xs) => `[${xs.map((x) => JSON.stringify(x)).join(', ')}]`;
  return [
    '---',
    'name: fruti',
    'description: "Fruti Squad orchestrator: runs a design round (kiwi → lima → coco → bruno → coco R0 → lima gate → mora) by delegating each stage to its member as a subagent."',
    'welcomeMessage: "Fruti · Squad — tell me the piece; I route it through kiwi, lima, coco, bruno and mora."',
    'tools: ["read", "write", "shell", "subagent"]',
    'resources:',
    '  - file://.kiro/steering/fruti-squad.md',
    '  - file://.fruti/policy.md',
    '  - file://.fruti/state/current.json',
    '  - file://.fruti/handoffs/current.json',
    'toolsSettings:',
    '  subagent:',
    `    availableAgents: ${list(agents)}`,
    `    trustedAgents: ${list(KIRO_TRUSTED.filter((n) => agents.includes(n)))}`,
    ...kiroPermissions({ writes: ['.fruti/**'], shell: [...KIRO_READ, 'npx fruti*', 'node *'] }),
    '---',
    '',
    '# fruti',
    '',
    'You route; the members do the work. Follow `.fruti/policy.md`:',
    '',
    '- Read `.fruti/state/current.json`, pick the owner and launch that member with the subagent tool, one stage at a time, in pipeline order. Each stage writes its handoff and round copy.',
    '- Skip bruno (and report SKIPPED) when the piece has no behavior beyond native markup.',
    '- Ask the user only for product or identity decisions; everything else follows the policy\'s "Missing decisions" rules.',
    '- You only write under `.fruti/`. Product code is written by coco and bruno.',
    '',
  ].join('\n');
}

function writeKiroAgents(base, members, args) {
  for (const name of members.filter((n) => KIRO_AGENTS[n]))
    trackedWrite(join(base, '.kiro', 'agents', `${name}.md`), kiroAgentDefinition(name, base, members), args, `agente ${name}`);
  if (members.filter((n) => KIRO_AGENTS[n]).length > 1)
    trackedWrite(join(base, '.kiro', 'agents', 'fruti.md'), kiroOrchestrator(members), args, 'agente fruti (orquestador)');
}

// Before this version Kiro got skills in .agents/skills/ and agent folders in .kiro/agents/<n>/.
// Nothing is deleted: leftovers are reported, and lima profiles are copied to the new place.
function migrateKiro(base, members, args) {
  for (const name of members) {
    const old = MEMBERS[name].kind === 'skill' ? join(base, '.agents', 'skills', name) : join(base, '.kiro', 'agents', name);
    const marker = join(old, MEMBERS[name].kind === 'skill' ? 'SKILL.md' : 'AGENT.md');
    if (!existsSync(marker)) continue;
    if (name === 'lima') {
      const oldProfiles = join(old, 'profiles');
      const newProfiles = join(resolveRoot('kiro', 'skill', base), 'lima', 'profiles');
      for (const f of filesOf(oldProfiles)) {
        const dst = join(newProfiles, f);
        if (f.startsWith('examples') || f === '_TEMPLATE.md' || existsSync(dst)) continue;
        if (!args.dryRun) { mkdirSync(dirname(dst), { recursive: true }); cpSync(join(oldProfiles, f), dst); }
        report('migrado', `perfil de lima ${f} → .kiro/skills/lima/profiles/`, join(oldProfiles, f), args.dryRun);
      }
    }
    report('obsoleto', `${name} (ahora vive en .kiro/skills; bórralo a mano)`, old, args.dryRun);
  }
  // Profiles written by the old layout may still cite it (e.g. impeccable_path). Warn on every run until fixed.
  const seen = new Set();
  for (const dir of [join(base, '.kiro', 'skills', 'lima', 'profiles'), join(base, '.agents', 'skills', 'lima', 'profiles')]) {
    for (const f of filesOf(dir)) {
      if (f.startsWith('examples') || f === '_TEMPLATE.md' || seen.has(f) || !f.endsWith('.md')) continue;
      seen.add(f);
      if (/\.agents\/skills\/lima|\.kiro\/agents\/(kiwi|coco|bruno|mora)\//.test(readFileSync(join(dir, f), 'utf8')))
        log(`  ${warn('revisa'.padEnd(9))}el perfil ${f} cita rutas viejas (.agents/skills/lima o .kiro/agents/<miembro>/): cámbialas a .kiro/skills/`);
    }
  }
}

function writeClaudeMd(base, members, skillsRootRel, dryRun, global = false) {
  // Global installs have no project .fruti/, so user-level memory gets only the squad list.
  if (global) { writeInstructionBlock(base, join('.claude', 'CLAUDE.md'), squadLines(members, 'claude', skillsRootRel), dryRun); return; }
  writeInstructionBlock(base, 'CLAUDE.md', [
    ...squadLines(members, 'claude', skillsRootRel),
    '',
    'Política de ejecución (rutea primero, lee después; fuentes aprobadas; handoffs compactos):',
    '',
    '@.fruti/policy.md',
    '',
    'Rutas reales de skills/agentes: `.fruti/paths.yaml`. Los contratos `.fruti/runtime/*.yaml` citan rutas relativas al paquete (`skills/...`, `agentes/...`); resuélvelas con ese mapa o con `fruti path <ruta>` (imprime la ruta real). Invoca cada miembro con la herramienta Skill (`kiwi`, `lima`, `coco`, `bruno`, `mora-docs`, `mango`) y haz las preguntas de producto con AskUserQuestion.',
  ], dryRun);
}

// Maps package-relative paths used by .fruti/runtime/*.yaml to real install locations.
function pathsMap(base, members, target) {
  const rel = (p) => (p.startsWith(base) ? p.slice(base.length + 1) : p).replace(/\\/g, '/');
  const lines = ['# Generated by fruti-squad installer. Resolves package-relative paths in .fruti/runtime/*.yaml.', '# Longest-prefix match: skills/lima/reference/x.md -> <skills/lima value>/reference/x.md. Script: fruti path <package-relative path>.', `target: ${target}`, 'roots:'];
  for (const n of members) {
    const m = MEMBERS[n];
    lines.push(`  ${m.from}: ${rel(join(resolveRoot(target, m.kind, base), installedMemberName(n, target)))}`);
  }
  return lines.join('\n') + '\n';
}

// `fruti path <package-relative path>` -> real location in this project, via .fruti/paths.yaml.
// Longest-prefix match, so `skills/lima/reference/x.md` resolves through the `skills/lima` root.
function doPath(args) {
  const rel = (args._[1] || '').replace(/\\/g, '/').replace(/^\.\//, '');
  if (!rel) { log(err('Uso: fruti path <ruta relativa al paquete>  (p. ej. skills/lima/reference/quality-gates.md)')); process.exit(2); }
  const base = resolve(args.dest || process.cwd());
  const mapFile = join(base, '.fruti', 'paths.yaml');
  if (!existsSync(mapFile)) {
    // Package checkout (no install map): paths are literal.
    if (existsSync(join(base, rel))) { console.log(join(base, rel)); return; }
    log(err(`No encuentro ${mapFile} ni ${rel}. Ejecuta install/setup primero.`)); process.exit(2);
  }
  const roots = {};
  for (const line of readFileSync(mapFile, 'utf8').split('\n')) {
    const m = line.match(/^  ([^\s#][^:]*):\s*(\S+)\s*$/);
    if (m) roots[m[1]] = m[2];
  }
  const key = Object.keys(roots).filter((k) => rel === k || rel.startsWith(k + '/')).sort((a, b) => b.length - a.length)[0];
  if (!key) { log(err(`Sin raíz para "${rel}" en .fruti/paths.yaml (raíces: ${Object.keys(roots).join(', ') || 'ninguna'}). ¿El miembro se instaló con --only?`)); process.exit(2); }
  const out = join(base, roots[key], rel.slice(key.length));
  if (!existsSync(out)) { log(err(`Resuelve a ${out}, que no existe.`)); process.exit(2); }
  console.log(out);
}

// Runs the install, returns { target, base, skillsRoot } for chaining (setup).
function doInstall(args) {
  const base = args.global ? homedir() : resolve(args.dest || process.cwd());
  const target = (args.target || autodetectTarget(base)).toLowerCase();
  if (!TARGETS.includes(target)) {
    log(err(`Unknown --target "${target}". Use: ${TARGETS.join(', ')}`));
    process.exit(2);
  }
  const members = selectedMembers(args);

  log(`${C.bold}🍓 Fruti Squad installer${C.reset}`);
  log(`${C.dim}target env:${C.reset} ${C.bold}${target}${C.reset}${args.target ? '' : C.dim + ' (autodetected)' + C.reset}`);
  log(`${C.dim}base:${C.reset} ${base}${args.global ? warn('  (global)') : ''}`);
  log(`${C.dim}members:${C.reset} ${members.join(', ')}${args.dryRun ? warn('   (dry-run)') : ''}\n`);

  if (target === 'kiro' && args.global) { log(err('Kiro: install per project (agents read .fruti/ from the project).')); process.exit(2); }
  let skillsRoot = resolveRoot(target, 'skill', base);
  for (const name of members) {
    const m = MEMBERS[name];
    const installedName = installedMemberName(name, target);
    const src = join(PKG_ROOT, m.from);
    if (!existsSync(src)) { log(err(`  missing in package: ${m.from} — skipped`)); continue; }
    const dest = join(resolveRoot(target, m.kind, base), installedName);
    const extra = m.kind === 'agent' ? { 'SKILL.md': bridgeFor(readFileSync(join(src, 'AGENT.md'), 'utf8'), installedName) } : {};
    trackedCopy(src, dest, args, installedName, { extra, after: m.kind === 'agent' ? () => ensureSkillBridge(dest, installedName) : undefined });
  }

  // Compact runtime contracts, policy and guides belong to the squad: always renewed. State and handoffs
  // belong to the project: created once, never overwritten.
  if (!args.global) {
    const own = { renew: true };
    const fr = (...p) => join(PKG_ROOT, '.fruti', ...p);
    const to = (...p) => join(base, '.fruti', ...p);
    if (existsSync(fr('runtime'))) trackedCopy(fr('runtime'), to('runtime'), args, 'runtime contracts', own);
    if (existsSync(fr('contracts'))) trackedCopy(fr('contracts'), to('contracts'), args, 'contracts', own);
    if (existsSync(fr('audit-manifest.yaml'))) trackedCopy(fr('audit-manifest.yaml'), to('audit-manifest.yaml'), args, 'audit manifest', own);
    for (const rel of [['state', 'current.json'], ['handoffs', 'current.json']]) {
      if (existsSync(fr(...rel)) && !existsSync(to(...rel))) trackedCopy(fr(...rel), to(...rel), args, rel.join('/'));
    }
    if (existsSync(join(PKG_ROOT, 'AGENTS.md'))) trackedCopy(join(PKG_ROOT, 'AGENTS.md'), to('policy.md'), args, 'policy', own);
    trackedWrite(to('paths.yaml'), pathsMap(base, members, target), args, 'path map', own);
  }

  if (target === 'kiro') {
    trackedWrite(join(base, '.kiro', 'steering', 'fruti-squad.md'), kiroSteering(), args, 'steering');
    writeKiroAgents(base, members, args);
    migrateKiro(base, members, args);
  }

  if (target === 'codex' || target === 'claude') {
    const rel = (skillsRoot.startsWith(base) ? '.' + skillsRoot.slice(base.length) : skillsRoot).replace(/\\/g, '/');
    if (target === 'codex') writeCodexAgentsMd(base, members, rel, args.dryRun);
    else writeClaudeMd(base, members, rel, args.dryRun, args.global);
  }

  log(`\n  ${tally.nuevo} nuevo · ${tally.cambia} ${args.dryRun ? 'cambiaría' : 'renovado'} · ${tally.igual} igual · ${tally.omitido} omitido · ${tally.obsoleto} obsoleto${tally.migrado ? ` · ${tally.migrado} ${args.dryRun ? 'migraría' : 'migrado'}` : ''}`);
  if (args.dryRun) log(`\n${warn('Dry-run:')} no se cambió nada. Quita --dry-run para aplicarlo.`);
  else {
    if (tally.omitido) log(`  ${C.dim}Lo omitido ya existía con otro contenido: usa ${C.bold}update${C.reset}${C.dim} para renovarlo.${C.reset}`);
    log(`${ok('Install done.')}`);
  }
  return { target, base, skillsRoot };
}

// --- setup: install + init + append coco:/mora: blocks -----------------------

const COCO_BLOCK = `
coco:
  # data_contract = las entidades/campos REALES que coco puede dibujar.
  # NO lo llenas tú: arranca en 'none-yet' y coco lo va escribiendo SOLO cada vez
  # que diseñas una pantalla (registra ahí la entidad que descubre). Crece solo.
  # Puedes revisarlo/ajustarlo cuando quieras; ver examples/data_contract.example.md.
  data_contract: none-yet
  # Scripts de auditoría del proyecto. Si no los tienes, deja VACÍO (coco audita a
  # mano y lo marca) o pon AUTO para autodetectar.
  governance_scripts:
    scaffold_round:    # p. ej. "python3 <hub>/lab/scripts/scaffold_round.py" | AUTO |
    check_prototype:   # | AUTO |
    audit_component:   # p. ej. "python3 <hub>/lab/scripts/audit_component.py" | AUTO |
    coverage:          # | AUTO |
  governance_policy:   # ruta a tu policy de arquitectura, o VACÍO
  component_doc_standard: # orden de secciones de la página de componente, o VACÍO
`;

const MORA_BLOCK = `
mora:
  doc_standard:        # ruta al estándar de documentación, o VACÍO (usa el interno de mora)
  doc_shell:           # css/js del Hub cuyas clases reutilizan las páginas
    # - design-hub/assets/hub-shell.css
    # - design-hub/assets/hub-navigation.js
  serve_command:       # cómo servir el Hub, o VACÍO ("python3 -m http.server" por defecto)
  coverage_script:     # censo de cobertura | AUTO | VACÍO
  hub_preview:         # cómo la Preview embebe el componente real, o VACÍO (no disponible/no verificada)
`;

function findNewestProfile(profilesDir) {
  if (!existsSync(profilesDir)) return null;
  let best = null, bestMtime = -1;
  for (const name of readdirSync(profilesDir)) {
    if (!name.endsWith('.md')) continue;
    if (name === '_TEMPLATE.md') continue;
    const p = join(profilesDir, name);
    try {
      const st = statSync(p);
      if (st.isFile() && st.mtimeMs > bestMtime) { best = p; bestMtime = st.mtimeMs; }
    } catch {}
  }
  return best;
}

function appendBlockOnce(profilePath, key, block, dryRun) {
  const content = existsSync(profilePath) ? readFileSync(profilePath, 'utf8') : '';
  const has = new RegExp(`(^|\\n)${key}:\\s*(\\n|$)`).test(content);
  if (has) { log(`  ${warn('skip')}  bloque ${C.bold}${key}:${C.reset} ya existe en el perfil`); return; }
  if (dryRun) { log(`  ${C.cyan}would append${C.reset} bloque ${C.bold}${key}:${C.reset} al perfil`); return; }
  const sep = content && !content.endsWith('\n') ? '\n' : '';
  appendFileSync(profilePath, sep + block);
  log(`  ${ok('ok')}    bloque ${C.bold}${key}:${C.reset} añadido al perfil`);
}

// Interactive wizard: asks the project facts in the terminal and writes an intake
// YAML. Returns the path to that file, or null if it can't/shouldn't run.
async function runWizard(base) {
  if (!process.stdin.isTTY || !process.stdout.isTTY) return null; // no TTY -> skip
  const rl = createInterface({ input: process.stdin, output: process.stdout });
  const ask = (q, def = '') =>
    new Promise((res) => rl.question(`${C.cyan}?${C.reset} ${q}${def ? C.dim + ' [' + def + ']' + C.reset : ''} `, (a) => res((a || '').trim() || def)));
  const yes = (v) => /^(s|si|sí|y|yes)$/i.test(v);

  log(`\n${C.bold}🧭 Configuremos tu proyecto${C.reset} ${C.dim}(Enter = valor por defecto)${C.reset}\n`);

  const projectName = await ask('Nombre del proyecto:', base.split('/').pop() || 'mi-proyecto');
  const hasDS = yes(await ask('¿Ya tienes un design system definido (colores, tipografía)? (s/N):', 'n'));

  let designSystem, colorLaw, typeLaw;
  if (hasDS) {
    designSystem = await ask('  Nombre del design system:', projectName);
    const action = await ask('  Color de ACCIÓN principal (hex):', '#2A62F0');
    const danger = await ask('  Color de PELIGRO/error (hex):', '#C0392B');
    const surface = await ask('  Color de SUPERFICIE/fondo (hex):', '#FFFFFF');
    const ink = await ask('  Color de TEXTO/tinta (hex):', '#14161A');
    if (/^#[0-9a-f]{6}$/i.test(action) && /^#[0-9a-f]{6}$/i.test(surface)) {
      const cr = contrastRatio(action, surface);
      if (cr < 4.5) log(`  ${warn('!')} el texto ${surface} sobre la acción ${action} da ${cr.toFixed(2)}:1 (< 4.5:1 de WCAG AA para texto normal). Considera oscurecer la acción.`);
    }
    const bodyFont = await ask('  Fuente base:', 'Inter');
    colorLaw = `surface ${surface}\nink ${ink}\naction ${action}   # solo la acción primaria\ndanger ${danger}   # solo errores/destructivo\nrule: si un elemento no es acción ni estado, es ink sobre surface.`;
    typeLaw = `body: "${bodyFont}"`;
  } else {
    designSystem = 'NEW';
    colorLaw = 'NEW';
    typeLaw = 'NEW';
    log(`  ${C.dim}Sin problema: lima te ayudará a definir un sistema mínimo cuando diseñes lo primero.${C.reset}`);
  }

  const framework = await ask('Framework (react-ts, vue3-ts, svelte… o AUTO):', 'AUTO');
  const styling = await ask('Styling (tailwind, css-modules… o AUTO):', 'AUTO');
  const icons = await ask('Iconos (lucide, heroicons… o AUTO):', 'AUTO');
  const hub = await ask('Carpeta del Design Hub:', 'design-hub');
  const breakpoints = await ask('Breakpoints (px, coma-separados):', '1440, 1024, 768, 390');
  const a11y = await ask('Objetivo de accesibilidad:', 'WCAG 2.2 AA');
  const wantQa = yes(await ask('¿Configurar QA con Playwright? (S/n):', 's'));
  rl.close();

  const bpArr = '[' + breakpoints.split(',').map((s) => s.trim()).filter(Boolean).join(', ') + ']';
  const yaml = [
    `# Generado por el wizard de fruti-squad setup`,
    `project_name: ${JSON.stringify(projectName)}`,
    `design_system_name: ${JSON.stringify(designSystem)}`,
    `color_law: |`,
    ...colorLaw.split('\n').map((l) => '  ' + l),
    `type_law: |`,
    ...typeLaw.split('\n').map((l) => '  ' + l),
    `framework: ${framework}`,
    `styling: ${styling}`,
    `icon_library: ${icons}`,
    `hub_root: ${hub}`,
    `a11y_target: ${JSON.stringify(a11y)}`,
    `breakpoints: ${bpArr}`,
    `qa_runner: ${wantQa ? 'playwright' : 'none'}`,
    '',
  ].join('\n');

  const file = join(tmpdir(), `fruti-intake-${Date.now()}.yaml`);
  writeFileSync(file, yaml);
  log(`\n  ${ok('ok')} intake preparado ${C.dim}(${file})${C.reset}`);
  return { file, qa: wantQa ? 'playwright' : 'none' };
}

async function doSetup(args) {
  log(`${C.bold}🍓 Fruti Squad · setup (todo en uno)${C.reset}\n`);

  // 1) install
  const { target, base, skillsRoot } = doInstall(args);
  if (args.dryRun) {
    log(`\n${C.dim}dry-run: setup también correría el wizard, el init y añadiría los bloques coco:/mora:.${C.reset}`);
    return;
  }

  // 1.5) wizard — si no pasaron --intake y hay terminal interactiva, preguntamos aquí.
  let intakePath = args.intake ? resolve(args.intake) : null;
  let wizardQa = null;
  if (!intakePath) {
    const wiz = await runWizard(base);
    if (wiz) { intakePath = wiz.file; wizardQa = wiz.qa; }
    else log(`\n${C.dim}Sin terminal interactiva y sin --intake: lima hará el intake conversacional.${C.reset}`);
  }

  // 2) init (lima) — needs bash + the init script
  const initScript = join(skillsRoot, 'lima', 'scripts', 'init-project.sh');
  const qa = args.qa || wizardQa || 'playwright';
  log(`\n${C.bold}› init (lima)${C.reset}`);
  if (!existsSync(initScript)) {
    log(err(`  no encuentro ${initScript} — ¿se instaló lima? Omitiendo init.`));
    return;
  }
  const hasBash = spawnSync('bash', ['-c', 'true'], { stdio: 'ignore' }).status === 0;
  if (!hasBash) {
    log(warn('  bash no disponible en este entorno; no puedo correr el init automáticamente.'));
    log(`  Córrelo tú:`);
    log(`    ${C.cyan}bash ${initScript}${intakePath ? ' --intake ' + intakePath : ''} --qa ${qa}${C.reset}`);
    log(`  Luego re-ejecuta ${C.bold}setup${C.reset} para añadir los bloques, o añádelos a mano.`);
    return;
  }
  const initArgs = [initScript];
  if (intakePath) initArgs.push('--intake', intakePath);
  initArgs.push('--qa', qa);
  const r = spawnSync('bash', initArgs, { cwd: base, stdio: 'inherit' });
  if (r.status !== 0) {
    log(err(`  el init de lima terminó con código ${r.status}. Revisa el output de arriba.`));
    return;
  }

  // 3) append coco:/mora: to the profile lima just created
  log(`\n${C.bold}› completar (coco: + mora:)${C.reset}`);
  const profilesDir = join(skillsRoot, 'lima', 'profiles');
  const profile = findNewestProfile(profilesDir);
  if (!profile) {
    log(warn(`  no encontré un perfil en ${profilesDir}. Añade los bloques coco:/mora: a mano (ver README).`));
    return;
  }
  log(`  ${C.dim}perfil:${C.reset} ${profile}`);
  appendBlockOnce(profile, 'coco', COCO_BLOCK, false);
  appendBlockOnce(profile, 'mora', MORA_BLOCK, false);

  // done
  log(`\n${ok('Setup completo.')}`);
  log(`\n${C.bold}Falta solo lo tuyo:${C.reset}`);
  log(`  · ${C.bold}No tienes que llenar nada más.${C.reset} coco irá escribiendo ${C.dim}data_contract${C.reset} solo, mientras diseñas.`);
  log(`  · Opcional: rutas de ${C.dim}governance_scripts / doc_shell${C.reset} en el perfil (o déjalas vacías; funcionan igual).`);
  log(`  · Perfil: ${C.cyan}${profile}${C.reset}`);
  printUse(target);
}

function printUse(target) {
  log(`\n${C.bold}Usar:${C.reset}`);
  if (target === 'kiro')   log(`  En Kiro elige el agente ${C.bold}fruti${C.reset} para una ronda completa, o ${C.bold}kiwi${C.reset}, ${C.bold}lima${C.reset}, ${C.bold}coco${C.reset}, ${C.bold}bruno${C.reset} o ${C.bold}mora${C.reset} para un solo paso.`);
  if (target === 'claude') log(`  En Claude Code aparecen como skills en ${C.bold}.claude/skills/${C.reset} y la política se carga vía ${C.bold}CLAUDE.md${C.reset}; pídele "usa kiwi/lima/coco/bruno/mora-docs/mango" o rediseña en lenguaje natural.`);
  if (target === 'codex')  log(`  Codex las conoce por el bloque en ${C.bold}AGENTS.md${C.reset}; pídele "usa kiwi/lima/coco/bruno/mora-docs/mango".`);
}

function doList() {
  log(`${C.bold}🍓 Fruti Squad — installable members${C.reset}\n`);
  for (const [name, m] of Object.entries(MEMBERS)) {
    const def = DEFAULT.includes(name) ? ok(' (default)') : `${C.dim} (optional)${C.reset}`;
    log(`  ${C.bold}${name}${C.reset}${def}  ${C.dim}${m.kind} — ${m.blurb}${C.reset}`);
  }
  log(`\n${C.bold}Per-target destination${C.reset}`);
  log(`  ${C.dim}kiro  ${C.reset} members→.kiro/skills/  agents→.kiro/agents/<n>.md + fruti.md (orchestrator)`);
  log(`  ${C.dim}claude${C.reset} everything→.claude/skills/  + CLAUDE.md block`);
  log(`  ${C.dim}codex ${C.reset} everything→.codex/skills/  + AGENTS.md block`);
  log(`\n${C.dim}Default squad: ${DEFAULT.join(', ')}. impeccable ships bundled inside lima (vendor/).${C.reset}`);
}

const args = parseArgs(process.argv.slice(2));
const cmd = args._[0] || 'help';
switch (cmd) {
  case 'setup': doSetup(args).catch((e) => { log(err('setup falló: ' + (e && e.message))); process.exit(1); }); break;
  case 'install': doInstall(args); break;
  case 'update': args.update = true; doInstall(args); break;
  case 'list': doList(); break;
  case 'path': doPath(args); break;
  case 'test': {
    const tr = spawnSync(process.execPath, [resolve(__dirname, 'test.mjs'), ...process.argv.slice(3)], { stdio: 'inherit', cwd: process.cwd() });
    process.exit(tr.status ?? 1);
    break;
  }
  case 'fidelity': {
    const vr = spawnSync(process.execPath, [resolve(__dirname, 'fidelity.mjs'), ...process.argv.slice(3)], { stdio: 'inherit', cwd: process.cwd() });
    process.exit(vr.status ?? 1);
    break;
  }
  case 'foundations': {
    const fr = spawnSync(process.execPath, [resolve(__dirname, 'foundations.mjs'), ...process.argv.slice(3)], { stdio: 'inherit', cwd: process.cwd() });
    process.exit(fr.status ?? 1);
    break;
  }
  case 'help':
  default: log(helpText());
}
