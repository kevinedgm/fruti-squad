#!/usr/bin/env node
// Fruti Squad installer/setup — coco · lima · mora, for Kiro, Claude Code, Codex.
// Zero dependencies.
//   npx github:kevinedgm/fruti-squad setup   --target kiro --intake my-intake.yaml
//   npx github:kevinedgm/fruti-squad install --target kiro
//
// Commands:
//   setup    install + init (lima) + append coco:/mora: blocks to the profile   (one shot)
//   install  copy the squad into a project (or --global)
//   list     show installable members and per-target paths
//   help     show help
//
// Targets (where each member lands):
//   kiro    skills -> .agents/skills/<n>/     agents -> .kiro/agents/<n>/
//   claude  skills -> .claude/skills/<n>/     agents -> .claude/skills/<n>/  (as skills)
//   codex   skills -> .codex/skills/<n>/      agents -> .codex/skills/<n>/   + AGENTS.md block
//
// Flags:
//   --target <env>  kiro | claude | codex  (default: autodetect, else kiro)
//   --intake <f>    (setup) intake YAML for lima's init -> a COMPLETE profile
//   --qa <runner>   (setup) passed to lima init, e.g. playwright | none
//   --global        install user-wide (~ instead of the project root)
//   --dest <dir>    target project root (default: current working directory)
//   --only <names>  comma list (default: coco,lima,mora). Extra: impeccable,
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
  lima:                 { from: 'skills/lima',               kind: 'skill', blurb: 'gobierna el ciclo de vida y refina el design system' },
  impeccable:           { from: 'skills/impeccable',         kind: 'skill', blurb: 'playbooks de refinamiento de UI' },
  'improve-animations': { from: 'skills/improve-animations', kind: 'skill', blurb: 'micro-interacciones y animación' },
  'skill-architect':    { from: 'skills/skill-architect',    kind: 'skill', blurb: 'creación de nuevas skills' },
  coco:                 { from: 'agentes/coco',              kind: 'agent', blurb: 'diseña, implementa y audita interfaz (protocolo R0–R3)' },
  mora:                 { from: 'agentes/mora',              kind: 'agent', blurb: 'documenta y sincroniza el Design Hub' },
};
const DEFAULT = ['coco', 'lima', 'mora'];
const TARGETS = ['kiro', 'claude', 'codex'];

const C = {
  reset: '\x1b[0m', bold: '\x1b[1m', dim: '\x1b[2m',
  green: '\x1b[32m', yellow: '\x1b[33m', red: '\x1b[31m', cyan: '\x1b[36m',
};
const log = (...a) => console.log(...a);
const ok = (s) => `${C.green}${s}${C.reset}`;
const warn = (s) => `${C.yellow}${s}${C.reset}`;
const err = (s) => `${C.red}${s}${C.reset}`;

function parseArgs(argv) {
  const args = { _: [], target: null, intake: null, qa: null, global: false, force: false, dryRun: false, dest: null, only: null };
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
${C.bold}🍓 Fruti Squad${C.reset} — coco · lima · mora  (Kiro · Claude Code · Codex)

${C.bold}Commands${C.reset}
  ${C.bold}setup${C.reset}          One shot: install + init (lima) + append coco:/mora: to the profile
  install        Copy the squad into a project (or --global)
  list           Show installable members and per-target paths
  help           Show this help

${C.bold}Options${C.reset}
  --target <env>   kiro | claude | codex   (default: autodetect, else kiro)
  --intake <file>  (setup) intake YAML -> lima writes a COMPLETE profile
  --qa <runner>    (setup) playwright | none   (default: playwright)
  --global         Install user-wide (home dir instead of project root)
  --dest <dir>     Target project root (default: current directory)
  --only <names>   Comma list (default: coco,lima,mora). Extra: impeccable,
                   improve-animations, skill-architect
  --force          Overwrite existing destinations
  --dry-run        Show actions without changing anything

${C.bold}Recommended (one command)${C.reset}
  npx github:kevinedgm/fruti-squad setup --target kiro --intake my-intake.yaml
  npx github:kevinedgm/fruti-squad setup --target claude          # intake conversacional después

${C.bold}Manual (step by step)${C.reset}
  npx github:kevinedgm/fruti-squad install --target codex
  npx github:kevinedgm/fruti-squad list
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
      return kind === 'skill' ? join(base, '.agents', 'skills') : join(base, '.kiro', 'agents');
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

function ensureSkillBridge(dest, name) {
  const skillPath = join(dest, 'SKILL.md');
  const agentPath = join(dest, 'AGENT.md');
  if (existsSync(skillPath) || !existsSync(agentPath)) return;
  const raw = readFileSync(agentPath, 'utf8');
  const fm = raw.match(/^---\n([\s\S]*?)\n---\n?/);
  let description = `Fruti Squad member ${name}.`;
  if (fm) {
    const dm = fm[1].match(/^description:\s*(.*)$/m);
    if (dm) description = dm[1].trim().replace(/^["']|["']$/g, '');
  }
  const body = fm ? raw.slice(fm[0].length) : raw;
  const skill = `---\nname: ${name}\ndescription: ${JSON.stringify(description)}\n---\n\n<!-- Generated by fruti-squad installer as a SKILL.md bridge for Claude/Codex. Source of truth: AGENT.md in this folder. -->\n${body}`;
  writeFileSync(skillPath, skill);
  log(`         ${C.dim}+ SKILL.md bridge (from AGENT.md)${C.reset}`);
}

function writeCodexAgentsMd(base, members, skillsRootRel, dryRun) {
  const file = join(base, 'AGENTS.md');
  const start = '<!-- fruti-squad:start -->';
  const end = '<!-- fruti-squad:end -->';
  const lines = [
    start,
    '## 🍓 Fruti Squad (coco · lima · mora)',
    '',
    'Este proyecto incluye el Fruti Squad en `' + skillsRootRel + '`. Cada carpeta tiene su `SKILL.md`/`AGENT.md`; léelos cuando la tarea lo pida:',
    '',
    ...members.map((n) => `- **${n}** — ${MEMBERS[n].blurb} → \`${skillsRootRel}/${n}/\``),
    '',
    'Frontera: **coco audita · lima gobierna el ciclo y refina · mora documenta.** Coco, lima y mora comparten el perfil de proyecto de lima (`' + skillsRootRel + '/lima/profiles/<proyecto>.md`).',
    end,
  ].join('\n');

  if (dryRun) { log(`  ${C.cyan}would update${C.reset} AGENTS.md ${C.dim}(fruti-squad block)${C.reset}`); return; }

  let content = existsSync(file) ? readFileSync(file, 'utf8') : '';
  if (content.includes(start) && content.includes(end)) {
    content = content.replace(new RegExp(start + '[\\s\\S]*?' + end), lines);
    writeFileSync(file, content);
  } else {
    const sep = content && !content.endsWith('\n') ? '\n\n' : (content ? '\n' : '');
    appendFileSync(file, sep + lines + '\n');
  }
  log(`  ${ok('ok')}    AGENTS.md ${C.dim}(fruti-squad block written)${C.reset}`);
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

  let installed = 0, skipped = 0;
  let skillsRoot = resolveRoot(target, 'skill', base);
  for (const name of members) {
    const m = MEMBERS[name];
    const src = join(PKG_ROOT, m.from);
    if (!existsSync(src)) { log(err(`  missing in package: ${m.from} — skipped`)); continue; }
    const root = resolveRoot(target, m.kind, base);
    const dest = join(root, name);

    if (existsSync(dest) && !args.force) {
      log(`  ${warn('skip')}  ${C.bold}${name}${C.reset} — already exists (use --force) ${C.dim}${dest}${C.reset}`);
      skipped++;
      continue;
    }
    if (args.dryRun) {
      log(`  ${C.cyan}would copy${C.reset}  ${C.bold}${name}${C.reset} → ${C.dim}${dest}${C.reset}`);
      installed++;
      continue;
    }
    mkdirSync(root, { recursive: true });
    cpSync(src, dest, { recursive: true });
    log(`  ${ok('ok')}    ${C.bold}${name}${C.reset} → ${C.dim}${dest}${C.reset}`);
    if (m.kind === 'agent' && (target === 'claude' || target === 'codex')) ensureSkillBridge(dest, name);
    installed++;
  }

  if (target === 'codex') {
    const rel = skillsRoot.startsWith(base) ? '.' + skillsRoot.slice(base.length) : skillsRoot;
    writeCodexAgentsMd(base, members, rel.replace(/\\/g, '/'), args.dryRun);
  }

  log('');
  if (args.dryRun) log(`${C.dim}dry-run: ${installed} would install, ${skipped} skipped. Nothing changed.${C.reset}`);
  else log(`${ok('Install done.')} ${installed} installed, ${skipped} skipped.`);
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
    # - design-hub/docs.css
    # - design-hub/docs.js
  serve_command:       # cómo servir el Hub, o VACÍO ("python3 -m http.server" por defecto)
  coverage_script:     # censo de cobertura | AUTO | VACÍO
  hub_preview:         # cómo la Preview embebe el componente real, o VACÍO (espejo de CSS)
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
    const action = await ask('  Color de ACCIÓN principal (hex):', '#2F6BFF');
    const danger = await ask('  Color de PELIGRO/error (hex):', '#C0392B');
    const surface = await ask('  Color de SUPERFICIE/fondo (hex):', '#FFFFFF');
    const ink = await ask('  Color de TEXTO/tinta (hex):', '#14161A');
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
  if (target === 'kiro')   log(`  Invoca ${C.bold}/coco${C.reset}, ${C.bold}/mora${C.reset} o la skill ${C.bold}lima${C.reset} desde Kiro.`);
  if (target === 'claude') log(`  En Claude Code aparecen como skills en ${C.bold}.claude/skills/${C.reset}; invócalas por nombre.`);
  if (target === 'codex')  log(`  Codex las conoce por el bloque en ${C.bold}AGENTS.md${C.reset}; pídele "usa coco/lima/mora".`);
}

function doList() {
  log(`${C.bold}🍓 Fruti Squad — installable members${C.reset}\n`);
  for (const [name, m] of Object.entries(MEMBERS)) {
    const def = DEFAULT.includes(name) ? ok(' (default)') : `${C.dim} (optional)${C.reset}`;
    log(`  ${C.bold}${name}${C.reset}${def}  ${C.dim}${m.kind} — ${m.blurb}${C.reset}`);
  }
  log(`\n${C.bold}Per-target destination${C.reset}`);
  log(`  ${C.dim}kiro  ${C.reset} skills→.agents/skills/  agents→.kiro/agents/`);
  log(`  ${C.dim}claude${C.reset} everything→.claude/skills/`);
  log(`  ${C.dim}codex ${C.reset} everything→.codex/skills/  + AGENTS.md block`);
  log(`\n${C.dim}Default squad: ${DEFAULT.join(', ')}. impeccable ships bundled inside lima (vendor/).${C.reset}`);
}

const args = parseArgs(process.argv.slice(2));
const cmd = args._[0] || 'help';
switch (cmd) {
  case 'setup': doSetup(args).catch((e) => { log(err('setup falló: ' + (e && e.message))); process.exit(1); }); break;
  case 'install': doInstall(args); break;
  case 'list': doList(); break;
  case 'help':
  default: log(helpText());
}
