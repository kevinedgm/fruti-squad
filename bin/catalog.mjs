#!/usr/bin/env node
// fruti catalog: une el registro de Lima (estado, versión, rutas) con .fruti/catalog.json
// (propósito, punto de entrada, API, variantes, tamaños, estados; lo escribe Mora) y genera
// .fruti/catalog.md, la guía rápida que leen Fruti y Mango antes de abrir el Design Hub.
// El estado nunca se copia al catálogo: sale siempre del registro.
//   fruti catalog [--dest <proyecto>] [--registry <ruta>] [--check]
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve, join } from 'node:path';

const argv = process.argv.slice(2);
let dest = process.cwd(), registryArg = null, check = false;
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--dest') dest = argv[++i];
  else if (a === '--registry') registryArg = argv[++i];
  else if (a === '--check') check = true;
  else { console.error(`Opción desconocida: ${a}\nUso: fruti catalog [--dest <proyecto>] [--registry <ruta>] [--check]`); process.exit(2); }
}
dest = resolve(dest);
const catPath = join(dest, '.fruti', 'catalog.json');
const mdPath = join(dest, '.fruti', 'catalog.md');
const readJson = (p, what) => {
  try { return JSON.parse(readFileSync(p, 'utf8')); }
  catch (e) { console.error(`No pude leer ${what} (${p}): ${e.message}`); process.exit(2); }
};

const catalog = existsSync(catPath) ? readJson(catPath, 'el catálogo') : { registry: null, components: {} };
catalog.components ||= {};
const regRel = registryArg || catalog.registry;
if (!regRel) { console.error('Falta la ruta del registro: pasa --registry <ruta> (el registry_path del perfil de Lima) o ponla en "registry" de .fruti/catalog.json.'); process.exit(2); }
const regPath = resolve(dest, regRel);
const registry = existsSync(regPath) ? readJson(regPath, 'el registro') : {};
if (!existsSync(regPath)) console.warn(`Aviso: no existe el registro ${regRel}; solo se listan los componentes del proyecto.`);

// Lo que se elige al componer una pantalla. Los tokens y superficies viven en tokens.json.
const PIECES = new Set(['component', 'pattern', 'navigation', 'template']);
const REQUIRED = ['purpose', 'entry'];
const problems = [], rows = [];

for (const [id, r] of Object.entries(registry)) {
  if (!PIECES.has(r.kind) || r.status === 'deprecated') continue;
  if (!catalog.components[id]) problems.push(`${id}: está en el registro (${r.status}) y no tiene entrada en el catálogo`);
}
for (const [id, c] of Object.entries(catalog.components)) {
  const origin = c.origin || 'fruti';
  const r = registry[id];
  if (origin === 'fruti' && !r) { problems.push(`${id}: origin fruti y no existe en el registro`); continue; }
  for (const f of REQUIRED) if (c[f] == null || c[f] === '') problems.push(`${id}: falta ${f}`);
  if ('status' in c) problems.push(`${id}: el estado no va en el catálogo; sale del registro`);
  rows.push({ id, c, r, origin });
}

const order = { stable: 0, candidate: 1, draft: 2, deprecated: 3 };
rows.sort((x, y) => (x.origin === y.origin ? 0 : x.origin === 'fruti' ? -1 : 1)
  || (order[x.r?.status] ?? 9) - (order[y.r?.status] ?? 9) || x.id.localeCompare(y.id));

const list = (v) => Array.isArray(v) ? (v.length ? v.map((x) => typeof x === 'string' ? x : x.name).join(', ') : '—') : (v || '—');
const entry = (e) => typeof e === 'string' ? e : [e?.import, e?.markup].filter(Boolean).join(' · ') || '—';
const cell = (s) => String(s).replace(/\|/g, '\\|').replace(/\n/g, ' ');
const lines = [
  '<!-- Generado por `fruti catalog`. No lo edites: cambia .fruti/catalog.json (Mora) o el registro (Lima). -->',
  '# Catálogo de componentes',
  '',
  `Registro: \`${regRel}\`. Estado y versión salen del registro; lo demás, de \`.fruti/catalog.json\`. Si un dato falta aquí, abre la página del Hub solo de ese componente.`,
  '',
  '| Id | Origen | Estado | Para qué | Entrada | Variantes | Tamaños | Ancho | Estados |',
  '|---|---|---|---|---|---|---|---|---|',
  ...rows.map(({ id, c, r, origin }) => `| ${cell(id)} | ${origin} | ${r ? `${r.status} ${r.version || ''}`.trim() : 'sin registrar'} | ${cell(c.purpose || '—')} | ${cell(entry(c.entry))} | ${cell(list(c.variants))} | ${cell(list(c.sizes))} | ${cell(c.width || '—')} | ${cell(list(c.states))} |`),
  '',
];
for (const { id, c, r } of rows) {
  lines.push(`## ${id}`, '');
  if (c.use_when) lines.push(`- Úsalo cuando: ${c.use_when}`);
  if (c.avoid_when) lines.push(`- No lo uses cuando: ${c.avoid_when}`);
  const api = c.api || {};
  for (const [k, label] of [['props', 'Props'], ['slots', 'Slots'], ['events', 'Eventos']]) {
    if (!api[k]?.length) continue;
    lines.push(`- ${label}: ${api[k].map((p) => typeof p === 'string' ? `\`${p}\`` : `\`${p.name}\`${p.type ? ` (${p.type}${p.default !== undefined ? `, por defecto ${p.default}` : ''})` : ''}${p.values ? `: ${p.values.join(' | ')}` : ''}`).join('; ')}`);
  }
  const docs = c.docs || r?.documentation;
  if (docs) lines.push(`- Hub: \`${docs}\``);
  if (r?.source) lines.push(`- Código: \`${r.source}\`${r.behavior ? ` + \`${r.behavior}\`` : ''}`);
  if (c.missing?.length) lines.push(`- Sin evidencia (no inventar): ${c.missing.join(', ')}`);
  lines.push('');
}
const md = lines.join('\n');

if (check) {
  const current = existsSync(mdPath) ? readFileSync(mdPath, 'utf8') : null;
  if (current !== md) problems.push('.fruti/catalog.md no está al día: corre `fruti catalog`');
  if (problems.length) { console.error(`Catálogo con ${problems.length} problema(s):\n- ${problems.join('\n- ')}`); process.exit(1); }
  console.log(`✓ catálogo al día: ${rows.length} componente(s)`);
} else {
  if (!catalog.registry) { catalog.registry = regRel; writeFileSync(catPath, JSON.stringify(catalog, null, 2) + '\n'); }
  writeFileSync(mdPath, md);
  console.log(`✓ .fruti/catalog.md: ${rows.length} componente(s)`);
  if (problems.length) { console.warn(`Pendientes (${problems.length}):\n- ${problems.join('\n- ')}`); }
}
