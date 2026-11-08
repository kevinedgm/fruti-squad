// Installer smoke tests: each target installs into a clean project, writes what its runtime
// needs, and reinstalling never overwrites live project state. Zero dependencies: `npm test`.
import { spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
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
  for (const n of ['kiwi', 'lima', 'coco', 'mora-docs']) has(d, '.claude', 'skills', n, 'SKILL.md');
  has(d, '.fruti', 'policy.md'); has(d, '.fruti', 'paths.yaml'); has(d, '.fruti', 'runtime', 'coco.yaml');
  assert.match(readFileSync(join(d, 'CLAUDE.md'), 'utf8'), /\.fruti\/policy\.md/);
});

test('codex: skills and AGENTS.md block', () => {
  const d = fresh();
  run('install', '--target', 'codex', '--dest', d);
  for (const n of ['kiwi', 'lima', 'coco', 'mora-docs']) has(d, '.codex', 'skills', n, 'SKILL.md');
  has(d, 'AGENTS.md');
});

test('kiro: steering and one custom agent per member, with permissions', () => {
  const d = fresh();
  run('install', '--target', 'kiro', '--dest', d);
  has(d, '.kiro', 'steering', 'fruti-squad.md');
  has(d, '.agents', 'skills', 'lima', 'SKILL.md');
  for (const n of ['kiwi', 'lima', 'coco', 'mora']) {
    has(d, '.kiro', 'agents', `${n}.md`);
    const def = readFileSync(join(d, '.kiro', 'agents', `${n}.md`), 'utf8');
    assert.match(def, new RegExp(`^---\\nname: ${n}\\n`), `${n}: frontmatter name`);
    assert.match(def, /effect: deny/, `${n}: destructive commands denied`);
    assert.match(def, /"git push\*"/, `${n}: git push denied`);
    // Every file:// or skill:// resource it points at must exist after install.
    for (const [, r] of def.matchAll(/^  - (?:file|skill):\/\/(.+)$/gm)) has(d, r);
  }
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

console.log(`\n${passed} tests passed`);
