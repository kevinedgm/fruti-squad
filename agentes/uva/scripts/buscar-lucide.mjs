#!/usr/bin/env node
// Uva · busca en el catálogo de Lucide antes de diseñar un icono nuevo (estándar §4, etapa E1).
// Uso:
//   node buscar-lucide.mjs <término> [término…]   → iconos que coinciden por nombre o etiqueta (etiquetas en inglés)
//   node buscar-lucide.mjs --svg <nombre> [--stroke 1.5]   → SVG real del icono (para banco de prueba / propuesta)
// Catálogo (primera ruta que exista): --catalog <dir> · $UVA_LUCIDE_DIR · node_modules/lucide-static del proyecto
//   · caché ~/.cache/fruti-uva/lucide-static (si falta, se descarga con `npm pack lucide-static`).

import { existsSync, mkdirSync, readFileSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { homedir } from 'node:os';
import { spawnSync } from 'node:child_process';

const args = process.argv.slice(2);
const opt = (name) => { const i = args.indexOf(name); return i >= 0 ? args.splice(i, 2)[1] : null; };
const catalogArg = opt('--catalog');
const svgName = opt('--svg');
const stroke = opt('--stroke');

function catalogDir() {
  const candidates = [catalogArg, process.env.UVA_LUCIDE_DIR, resolve('node_modules/lucide-static')].filter(Boolean);
  for (const c of candidates) if (existsSync(join(c, 'tags.json'))) return c;
  const cache = join(homedir(), '.cache', 'fruti-uva');
  const dir = join(cache, 'package');
  if (existsSync(join(dir, 'tags.json'))) return dir;
  mkdirSync(cache, { recursive: true });
  console.error('Descargando lucide-static (npm pack)…');
  const pack = spawnSync('npm', ['pack', 'lucide-static', '--silent', '--pack-destination', cache], { encoding: 'utf8' });
  const tgz = readdirSync(cache).find((f) => /^lucide-static-.*\.tgz$/.test(f));
  if (pack.status !== 0 || !tgz) {
    console.error('No pude obtener el catálogo de Lucide (npm pack falló). Instala lucide-static en el proyecto o usa --catalog <dir>.');
    process.exit(2);
  }
  const tar = spawnSync('tar', ['-xzf', join(cache, tgz), '-C', cache, 'package/tags.json', 'package/icons', 'package/package.json']);
  if (tar.status !== 0) { console.error('No pude extraer el catálogo (tar).'); process.exit(2); }
  return dir;
}

const dir = catalogDir();
const version = (() => { try { return JSON.parse(readFileSync(join(dir, 'package.json'), 'utf8')).version; } catch { return '?'; } })();

if (svgName) {
  const file = join(dir, 'icons', `${svgName}.svg`);
  if (!existsSync(file)) { console.error(`No existe el icono "${svgName}" en lucide-static ${version}.`); process.exit(1); }
  let svg = readFileSync(file, 'utf8').replace(/<!--[\s\S]*?-->\s*/g, '').replace(/\s+(width|height)="24"/g, '');
  // Con --stroke, el grosor sigue además a --uva-stroke (misma variable que los iconos de Uva).
  if (stroke) svg = svg.replace(/stroke-width="[^"]*"/, `stroke-width="${stroke}" style="stroke-width:var(--uva-stroke,${stroke})"`);
  svg = svg.replace('<svg', `<svg data-nombre="${svgName}" aria-hidden="true"`);
  console.log(svg.replace(/\n\s*/g, ' ').replace(/\s+>/g, '>').trim());
  process.exit(0);
}

const terms = args.map((t) => t.toLowerCase()).filter(Boolean);
if (!terms.length) { console.error('Uso: node buscar-lucide.mjs <término> [...] | --svg <nombre> [--stroke 1.5]'); process.exit(2); }

const tags = JSON.parse(readFileSync(join(dir, 'tags.json'), 'utf8'));
const results = [];
for (const [name, list] of Object.entries(tags)) {
  const words = name.split('-');
  let score = 0; const hits = new Set();
  for (const t of terms) {
    if (name === t) { score += 6; hits.add(t); }
    else if (words.includes(t)) { score += 4; hits.add(t); }
    else if (t.length >= 4 && name.includes(t)) { score += 2; hits.add(t); }
    for (const tag of list) {
      if (tag === t) { score += 3; hits.add(t); }
      else if (tag.split(/\s+/).includes(t)) { score += 2; hits.add(t); }
      else if (t.length >= 4 && tag.includes(t)) { score += 1; hits.add(t); }
    }
  }
  if (score) results.push({ name, score: score + hits.size * 2, hits: [...hits], tags: list });
}
results.sort((a, b) => b.score - a.score || a.name.localeCompare(b.name));

console.log(`lucide-static ${version} · ${Object.keys(tags).length} iconos · términos: ${terms.join(', ')}\n`);
if (!results.length) console.log('Sin coincidencias: probablemente hace falta un icono propio (registra la búsqueda en el brief).');
for (const r of results.slice(0, 15)) {
  console.log(`${String(r.score).padStart(3)}  ${r.name.padEnd(24)} [${r.hits.join(', ')}]  ${r.tags.slice(0, 8).join(', ')}`);
}
