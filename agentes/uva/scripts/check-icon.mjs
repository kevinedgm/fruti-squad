#!/usr/bin/env node
// Uva · verificador determinista del contrato técnico de un icono SVG (fase E3).
// Uso: node check-icon.mjs <icono.svg> [más.svg…] [--json]
// Los iconos de librería (clase "lucide" o atributo data-referencia) se verifican como referencia: solo
// construcción, color y accesibilidad; no se les exigen las convenciones propias de Uva (uva-<id>, --uva-stroke).
// Sale con código 1 si algún criterio bloqueante falla. Las comprobaciones visuales
// (reconocimiento, confusiones, peso óptico, separación) se hacen en el banco de prueba.

import { readFileSync } from 'node:fs';
import { basename } from 'node:path';

const MAX_MOTION_S = 5; // WCAG 2.2.2

function rootTag(src) {
  const m = src.match(/<svg\b[^>]*>/);
  return m ? m[0] : '';
}
const attr = (tag, name) => {
  const m = tag.match(new RegExp(`\\s${name}\\s*=\\s*"([^"]*)"`));
  return m ? m[1] : null;
};
const styleText = (src) => [...src.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map((m) => m[1]).join('\n');

// Separa por comas de primer nivel (ignora las de cubic-bezier(...), var(...), etc.).
function splitTop(s) {
  const out = []; let depth = 0; let cur = '';
  for (const ch of s) {
    if (ch === '(') depth++;
    if (ch === ')') depth--;
    if (ch === ',' && depth === 0) { out.push(cur); cur = ''; } else cur += ch;
  }
  if (cur.trim()) out.push(cur);
  return out.map((x) => x.trim());
}
const toSeconds = (t) => (t.endsWith('ms') ? parseFloat(t) / 1000 : parseFloat(t));

// Duración total de cada animación del shorthand `animation:` = retraso positivo + duración × repeticiones.
function motionTotals(css) {
  const totals = []; let infinite = false;
  for (const m of css.matchAll(/(?:^|[;{\s])animation\s*:\s*([^;}]+)/g)) {
    if (/^\s*none\b/.test(m[1])) continue;
    for (const one of splitTop(m[1])) {
      const tokens = one.replace(/[\w-]+\([^)]*\)/g, ' ').split(/\s+/).filter(Boolean);
      const times = tokens.filter((t) => /^-?[\d.]+m?s$/.test(t)).map(toSeconds);
      if (tokens.includes('infinite')) infinite = true;
      const countTok = tokens.find((t) => /^[\d.]+$/.test(t));
      const count = countTok ? parseFloat(countTok) : 1;
      const dur = times[0] ?? 0;
      const delay = Math.max(0, times[1] ?? 0);
      totals.push(delay + dur * count);
    }
  }
  if (/animation-iteration-count\s*:\s*infinite/.test(css)) infinite = true;
  const longDelays = [...css.matchAll(/animation-delay\s*:\s*([^;}]+)/g)]
    .flatMap((m) => splitTop(m[1])).map(toSeconds).filter((x) => x > 0);
  const extra = longDelays.length ? Math.max(...longDelays) : 0; // estimación conservadora
  return { animated: totals.length > 0, infinite, total: totals.length ? Math.max(...totals) + extra : 0 };
}

// Selectores con combinadores (descendencia, hijo, hermano) fuera de @keyframes: no sobreviven a <use>.
function compoundSelectors(css) {
  const sinKeyframes = css
    .replace(/\/\*[\s\S]*?\*\//g, '')                                   // comentarios
    .replace(/@keyframes[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}/g, '')        // bloques @keyframes
    .replace(/@[^{;]+\{/g, '');                                          // preludios @media/@supports
  const out = [];
  for (const m of sinKeyframes.matchAll(/([^{}@;]+)\{/g)) {
    for (const sel of m[1].split(',').map((x) => x.trim()).filter(Boolean)) {
      if (/^@|^(from|to|\d+%)$/.test(sel)) continue;
      if (/[\s>+~]/.test(sel.replace(/\([^)]*\)/g, ''))) out.push(sel);
    }
  }
  return out;
}

function check(file) {
  const src = readFileSync(file, 'utf8');
  const root = rootTag(src);
  const css = styleText(src);
  const body = src.replace(/<style[\s\S]*?<\/style>/g, '');
  const cls = attr(root, 'class') || '';
  const id = (cls.match(/\buva-(?!icon\b)([\w-]+)/) || [])[1];
  const referencia = /\blucide\b/.test(cls) || attr(root, 'data-referencia') !== null;
  const motion = motionTotals(css);
  const r = [];
  const add = (code, ok, level, msg) => r.push({ code, ok, level, msg });

  // XML prohíbe «--» dentro de un comentario: inline en HTML pasa, pero como <img>, favicon o archivo no se abre.
  const badComments = [...src.matchAll(/<!--([\s\S]*?)-->/g)].filter((m) => /--|-$/.test(m[1])).length;
  add('X1', badComments === 0, 'bloqueante', `comentarios XML válidos, sin «--» dentro${badComments ? ` (${badComments} con «--»: el archivo no abre como <img> ni favicon)` : ''}`);
  add('A1', attr(root, 'viewBox') === '0 0 24 24', 'bloqueante', 'viewBox="0 0 24 24"');
  add('A1b', !attr(root, 'width') && !attr(root, 'height'), 'recomendado', 'sin width/height fijos en la raíz');
  add('A3', attr(root, 'stroke-width') !== null && !/<(?!svg\b)[a-z]+\b[^>]*\sstroke-width=/.test(body), 'bloqueante', 'un solo stroke-width, en la raíz');
  add('A4', attr(root, 'stroke-linecap') === 'round' && attr(root, 'stroke-linejoin') === 'round', 'bloqueante', 'stroke-linecap y stroke-linejoin = round');
  add('COL1', attr(root, 'stroke') === 'currentColor' && attr(root, 'fill') === 'none', 'bloqueante', 'raíz con stroke="currentColor" fill="none"');
  const fixedAttr = [...body.matchAll(/\s(?:fill|stroke|stop-color|color)\s*=\s*"([^"]*)"/g)]
    .map((m) => m[1]).filter((v) => !/^(none|currentColor|inherit|transparent)$/i.test(v));
  const fixedCss = (css.match(/#[0-9a-f]{3,8}\b|rgba?\(|hsla?\(/gi) || []);
  add('COL2', fixedAttr.length === 0 && fixedCss.length === 0, 'bloqueante', `sin colores fijos${fixedAttr.length + fixedCss.length ? ` (encontrados: ${[...fixedAttr, ...fixedCss].join(', ')})` : ''}`);
  if (!referencia) add('COL3', /var\(--uva-stroke/.test(css), 'recomendado', 'grosor ajustable con --uva-stroke');
  // Lucide: oculto por defecto; nombre accesible solo si el icono informa por sí solo.
  const named = !!attr(root, 'aria-label') || /<title\b[^>]*>[^<]+<\/title>/.test(body);
  const labelled = attr(root, 'role') === 'img' && named;
  const hidden = attr(root, 'aria-hidden') === 'true';
  add('C2', (labelled || hidden) && !(hidden && named), 'bloqueante',
    hidden && named ? 'aria-hidden="true" y nombre accesible a la vez: elige uno'
      : 'oculto (aria-hidden="true") o, si informa solo, role="img" + aria-label/<title>');
  if (labelled && !hidden) add('C2b', false, 'recomendado', 'expuesto con nombre: confirma que comunica algo esencial sin etiqueta (si no, aria-hidden="true")');
  if (referencia) add('REF', true, 'info', 'icono de librería verificado como referencia (sin convenciones uva-*)');
  else add('ID', !!id && /\buva-icon\b/.test(cls), 'bloqueante', 'clases "uva-icon uva-<id>"');
  if (!referencia) {
    const comp = compoundSelectors(css);
    add('SEL', comp.length === 0, 'bloqueante', `una clase por regla, sin combinadores${comp.length ? ` (encontrados: ${comp.join(' | ')})` : ''}`);
  }
  if (id && !referencia) {
    const unprefixed = [...css.matchAll(/@keyframes\s+([\w-]+)/g)].map((m) => m[1]).filter((k) => !k.startsWith(`uva-${id}-`));
    add('ID2', unprefixed.length === 0, 'bloqueante', `@keyframes con prefijo uva-${id}-${unprefixed.length ? ` (sin prefijo: ${unprefixed.join(', ')})` : ''}`);
  }
  if (motion.animated) {
    add('D1', !motion.infinite && motion.total <= MAX_MOTION_S, 'bloqueante',
      motion.infinite ? 'movimiento infinito: debe terminar en ≤5 s o tener control para pausar (WCAG 2.2.2)'
        : `movimiento total ≈ ${motion.total.toFixed(2)} s (máx. ${MAX_MOTION_S} s, WCAG 2.2.2)`);
    add('D2', /prefers-reduced-motion\s*:\s*reduce/.test(css), 'bloqueante', 'bloque @media (prefers-reduced-motion: reduce)');
    if (/stroke-dashoffset/.test(css)) add('D5', /pathLength=/.test(body), 'bloqueante', 'pathLength explícito en trazos animados con stroke-dashoffset');
  } else {
    add('D0', true, 'info', 'icono estático');
  }
  return { file: basename(file), id: id || null, referencia, motion, results: r, ok: r.every((x) => x.ok || x.level !== 'bloqueante') };
}

const args = process.argv.slice(2);
const json = args.includes('--json');
const files = args.filter((a) => a !== '--json');
if (!files.length) { console.error('Uso: node check-icon.mjs <icono.svg> [...] [--json]'); process.exit(2); }
const reports = files.map(check);
if (json) console.log(JSON.stringify(reports, null, 2));
else for (const rep of reports) {
  console.log(`\n${rep.ok ? '✅' : '❌'} ${rep.file}${rep.id ? ` (uva-${rep.id})` : ''}${rep.referencia ? ' (referencia de librería)' : ''}`);
  for (const x of rep.results) console.log(`  ${x.ok ? '✅' : x.level === 'bloqueante' ? '❌' : '⚠️ '} ${x.code.padEnd(4)} ${x.msg}${x.ok || x.level === 'bloqueante' ? '' : ' (recomendado)'}`);
}
process.exit(reports.every((x) => x.ok) ? 0 : 1);
