// Installer smoke tests: each target installs into a clean project, writes what its runtime
// needs, and reinstalling never overwrites live project state. Zero dependencies: `npm test`.
import { spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const run = (...args) => {
  const r = spawnSync(process.execPath, [join(ROOT, 'bin', 'install.mjs'), ...args], { encoding: 'utf8' });
  assert.equal(r.status, 0, `install ${args.join(' ')} failed:\n${r.stdout}\n${r.stderr}`);
  return r.stdout;
};
const fresh = () => mkdtempSync(join(tmpdir(), 'fruti-test-'));
const has = (base, ...p) => assert.ok(existsSync(join(base, ...p)), `expected ${p.join('/')}`);
let passed = 0;
const test = (name, fn) => { fn(); passed++; console.log(`✓ ${name}`); };

test('claude: skills, SKILL.md bridges, CLAUDE.md block, runtime', () => {
  const d = fresh();
  run('install', '--target', 'claude', '--dest', d);
  for (const n of ['kiwi', 'lima', 'coco', 'bruno', 'mora-docs', 'mango']) has(d, '.claude', 'skills', n, 'SKILL.md');
  has(d, '.fruti', 'runtime', 'mango.yaml');
  has(d, '.fruti', 'policy.md'); has(d, '.fruti', 'paths.yaml'); has(d, '.fruti', 'runtime', 'coco.yaml'); has(d, '.fruti', 'runtime', 'bruno.yaml');
  assert.match(readFileSync(join(d, 'CLAUDE.md'), 'utf8'), /\.fruti\/policy\.md/);
});

test('codex: skills and AGENTS.md block', () => {
  const d = fresh();
  run('install', '--target', 'codex', '--dest', d);
  for (const n of ['kiwi', 'lima', 'coco', 'bruno', 'mora-docs']) has(d, '.codex', 'skills', n, 'SKILL.md');
  has(d, 'AGENTS.md');
});

test('kiro: members as skills, one least-privilege agent per member, orchestrator', () => {
  const d = fresh();
  run('install', '--target', 'kiro', '--dest', d);
  has(d, '.kiro', 'steering', 'fruti-squad.md');
  for (const n of ['kiwi', 'lima', 'coco', 'bruno', 'mora', 'mango']) {
    has(d, '.kiro', 'skills', n, 'SKILL.md');
    assert.ok(!existsSync(join(d, '.kiro', 'agents', n)), `${n}: no procedure folder inside .kiro/agents`);
    const def = readFileSync(join(d, '.kiro', 'agents', `${n}.md`), 'utf8');
    assert.match(def, new RegExp(`^---\\nname: ${n}\\n`), `${n}: frontmatter name`);
    assert.match(def, /effect: deny/, `${n}: destructive commands denied`);
    assert.match(def, /"git push\*"/, `${n}: git push denied`);
    // Every file:// or skill:// resource it points at must exist after install.
    for (const [, r] of def.matchAll(/^  - (?:file|skill):\/\/(.+)$/gm)) has(d, r);
  }
  assert.doesNotMatch(readFileSync(join(d, '.kiro', 'agents', 'mora.md'), 'utf8'), /"web"/, 'mora has no web tool');
  const orq = readFileSync(join(d, '.kiro', 'agents', 'fruti.md'), 'utf8');
  assert.match(orq, /"subagent"/);
  assert.match(orq, /availableAgents: \["kiwi", "lima", "coco", "bruno", "mora"\]/);
  assert.doesNotMatch(orq.match(/trustedAgents: .*/)[0], /coco|bruno|mango/, 'agents that write product code are not trusted');
  assert.doesNotMatch(orq, /"mango"/, 'mango works outside the round');
  assert.match(readFileSync(join(d, '.fruti', 'paths.yaml'), 'utf8'), /agentes\/kiwi: \.kiro\/skills\/kiwi/);
});

test('update --dry-run: same after install, migrates old Kiro layout without deleting it', () => {
  const d = fresh();
  run('install', '--target', 'kiro', '--dest', d);
  assert.match(run('update', '--target', 'kiro', '--dest', d, '--dry-run'), / 0 nuevo · 0 cambiaría · \d+ igual · 0 omitido · 0 obsoleto/);
  // Old layout: lima in .agents/skills with a user profile, kiwi as a folder in .kiro/agents.
  spawnSync('mkdir', ['-p', join(d, '.agents', 'skills', 'lima', 'profiles'), join(d, '.kiro', 'agents', 'kiwi')]);
  writeFileSync(join(d, '.agents', 'skills', 'lima', 'SKILL.md'), '---\nname: lima\n---\n');
  writeFileSync(join(d, '.agents', 'skills', 'lima', 'profiles', 'demo.md'), 'impeccable_path: .agents/skills/lima/vendor/impeccable\n');
  writeFileSync(join(d, '.kiro', 'agents', 'kiwi', 'AGENT.md'), '---\nname: kiwi\n---\n');
  const dry = run('update', '--target', 'kiro', '--dest', d, '--dry-run');
  assert.match(dry, /2 obsoleto · 1 migraría/);
  assert.match(dry, /revisa.*demo\.md/);
  assert.ok(!existsSync(join(d, '.kiro', 'skills', 'lima', 'profiles', 'demo.md')), 'dry-run migrated');
  run('update', '--target', 'kiro', '--dest', d);
  has(d, '.kiro', 'skills', 'lima', 'profiles', 'demo.md');
  has(d, '.agents', 'skills', 'lima', 'profiles', 'demo.md');
});

test('reinstall with --force keeps live state and handoffs', () => {
  const d = fresh();
  run('install', '--target', 'claude', '--dest', d);
  const state = join(d, '.fruti', 'state', 'current.json');
  writeFileSync(state, '{"round":"r07"}\n');
  run('install', '--target', 'claude', '--dest', d, '--force');
  assert.equal(readFileSync(state, 'utf8'), '{"round":"r07"}\n');
});

test('dry-run changes nothing', () => {
  const d = fresh();
  run('install', '--target', 'kiro', '--dest', d, '--dry-run');
  assert.ok(!existsSync(join(d, '.kiro')) && !existsSync(join(d, '.fruti')), 'dry-run wrote files');
});

test('fruti test --case marks the round with its case', () => {
  const d = fresh();
  const r = spawnSync(process.execPath, [join(ROOT, 'bin', 'fruti.mjs'), 'test', '--dest', d, '--case', 'evals/casos/01-tarjeta-de-resumen.md'], { encoding: 'utf8' });
  assert.equal(r.status, 0, r.stderr);
  assert.match(readFileSync(join(d, '.fruti', 'tests', 'r01', 'request.md'), 'utf8'), /^case: 01-tarjeta-de-resumen$/m);
});

test('fruti foundations with short inputs: no questions, origin and contrast recorded', () => {
  const d = fresh();
  run('install', '--target', 'claude', '--dest', d);
  writeFileSync(join(d, '.claude', 'skills', 'lima', 'profiles', 'demo.md'), '---\ndesign_system: NEW\n---\n');
  const f = (...a) => spawnSync(process.execPath, [join(ROOT, 'bin', 'fruti.mjs'), 'foundations', '--dest', d, ...a], { encoding: 'utf8', input: '' });
  assert.equal(f().status, 2, 'without a terminal and without inputs it must refuse');
  assert.equal(f('--marca', 'azul').status, 2, 'a non-hex brand must be rejected');
  const r = f('--marca', '#F5C400', '--radio', '4', '--densidad', 'compacta');
  assert.equal(r.status, 0, r.stderr);
  const p = JSON.parse(readFileSync(join(d, '.fruti', 'foundations', 'proposal.json'), 'utf8'));
  assert.equal(p.status, 'proposed');
  assert.equal(p.color.primary, '#F5C400');
  assert.equal(p.geometry.surface_radius_px, 10);
  assert.equal(p.geometry.control_height_px, 44);
  assert.equal(p.origin['color.primary'], 'input');
  assert.equal(p.origin['geometry.surface_radius_px'], 'derived');
  assert.equal(p.origin['color.secondary'], 'default');
  assert.equal(p.checks.find(c => c.id === 'text-on-primary').status, 'warn');
  assert.match(readFileSync(join(d, '.fruti', 'foundations', 'proposal.yaml'), 'utf8'), /^  primary: "#F5C400"$/m);
});

test('every reference cited by a runtime contract exists in the package', () => {
  const dir = join(ROOT, '.fruti', 'runtime');
  for (const f of readdirSync(dir).filter((x) => x.endsWith('.yaml'))) {
    const text = readFileSync(join(dir, f), 'utf8');
    for (const [p] of text.matchAll(/(?:agentes|skills)\/[A-Za-z0-9_./-]+\.md/g)) assert.ok(existsSync(join(ROOT, p)), `${f} cites missing ${p}`);
  }
});

test('fruti catalog: joins registry, flags gaps, regenerates catalog.md', () => {
  const d = fresh();
  const cat = (...args) => spawnSync(process.execPath, [join(ROOT, 'bin', 'fruti.mjs'), 'catalog', '--dest', d, ...args], { encoding: 'utf8' });
  writeFileSync(join(d, 'registry.json'), JSON.stringify({
    button: { kind: 'component', status: 'stable', version: '1.0.0', documentation: 'hub/button.html', source: 'ui/button.css' },
    'date-field': { kind: 'component', status: 'candidate', version: '0.2.0' },
    old: { kind: 'component', status: 'deprecated' },
    'color-primary': { kind: 'token', status: 'stable' },
  }));
  spawnSync('mkdir', ['-p', join(d, '.fruti')]);
  writeFileSync(join(d, '.fruti', 'catalog.json'), JSON.stringify({ registry: 'registry.json', components: {
    button: { purpose: 'Acción', entry: { import: "import Button from '@/ui/Button.vue'" }, variants: ['primary', 'secondary'], width: 'content', api: { props: [{ name: 'variant', type: 'string', default: 'primary', values: ['primary', 'secondary'] }] } },
    'sneat-select': { origin: 'proyecto', purpose: 'Selector de la librería', entry: '<select class="form-select">' },
  } }));
  let r = cat();
  assert.equal(r.status, 0, r.stderr);
  const md = readFileSync(join(d, '.fruti', 'catalog.md'), 'utf8');
  assert.match(md, /\| button \| fruti \| stable 1\.0\.0 \|/);
  assert.match(md, /sneat-select \| proyecto \| sin registrar/);
  assert.doesNotMatch(md, /color-primary|\| old \|/);
  r = cat('--check');
  assert.equal(r.status, 1, 'date-field has no entry, so --check must fail');
  assert.match(r.stderr, /date-field: está en el registro/);
});

console.log(`\n${passed} tests passed`);
