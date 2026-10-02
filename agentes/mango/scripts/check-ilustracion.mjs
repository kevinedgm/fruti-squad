#!/usr/bin/env node
// Mango · comprueba el contrato técnico de una ilustración SVG (references/contrato-svg.md).
// Uso: node check-ilustracion.mjs <ilustracion.svg...>   · sale con 1 si algún bloqueante falla.
import { readFileSync, statSync } from 'node:fs';
import { basename } from 'node:path';

const attr = (tag, n) => { const m = tag.match(new RegExp(`\\s${n}\\s*=\\s*"([^"]*)"`)); return m ? m[1] : null; };

function check(file) {
  const src = readFileSync(file, 'utf8');
  const root = (src.match(/<svg\b[^>]*>/) || [''])[0];
  const css = [...src.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map((m) => m[1]).join('\n');
  const body = src.replace(/<style[\s\S]*?<\/style>/g, '');
  const visible = body.replace(/<mask\b[\s\S]*?<\/mask>/g, ''); // en una máscara el color es luminancia, no color visible
  const cls = attr(root, 'class') || '';
  const id = (cls.match(/\bmango-(?!ilu\b)([\w-]+)/) || [])[1];
  const r = []; const add = (code, ok, level, msg) => r.push({ code, ok, level, msg });

  const badComments = [...src.matchAll(/<!--([\s\S]*?)-->/g)].filter((m) => /--|-$/.test(m[1])).length;
  add('X1', badComments === 0, 'bloqueante', `comentarios XML válidos, sin «--» dentro${badComments ? ` (${badComments})` : ''}`);
  const vb = (attr(root, 'viewBox') || '').split(/\s+/).map(Number);
  add('A1', vb.length === 4 && vb[0] === 0 && vb[1] === 0 && vb[2] > 0 && vb[3] > 0, 'bloqueante', `viewBox "0 0 w h"${vb.length === 4 ? ` (${vb[2]}×${vb[3]})` : ''}`);
  add('A2', !attr(root, 'width') && !attr(root, 'height'), 'bloqueante', 'sin width/height en la raíz: la sección decide el tamaño');
  add('ID', /\bmango-ilu\b/.test(cls) && !!id, 'bloqueante', 'clases "mango-ilu mango-<id>"');
  // Color: ningún color fijo fuera de los valores por defecto de var(--mango-…, valor)
  const fixedAttr = [...visible.matchAll(/\s(?:fill|stroke|stop-color|color)\s*=\s*"([^"]*)"/g)].map((m) => m[1]).filter((v) => !/^(none|currentColor|inherit|transparent)$/i.test(v));
  const cssSinDefecto = css.replace(/var\(--mango-[\w-]+\s*,\s*[^)]*\)/g, '');
  const fixedCss = cssSinDefecto.match(/#[0-9a-f]{3,8}\b|rgba?\(|hsla?\(/gi) || [];
  add('COL1', fixedAttr.length === 0 && fixedCss.length === 0, 'bloqueante', `color solo por roles (var(--mango-…)); sin colores fijos${fixedAttr.length + fixedCss.length ? ` (encontrados: ${[...fixedAttr, ...fixedCss].slice(0, 5).join(', ')})` : ''}`);
  const roles = new Set([...css.matchAll(/var\((--mango-[\w-]+)/g)].map((m) => m[1]));
  add('COL2', roles.size >= 2 && roles.size <= 8, 'recomendado', `paleta de 2–8 roles (usa ${roles.size}: ${[...roles].map((x) => x.replace('--mango-', '')).join(', ')})`);
  // Clases y selectores
  const sel = css.replace(/@media[^{]*\{/g, '').split('}').map((b) => b.split('{')[0].trim()).filter((s) => s && !s.startsWith('@'));
  const compuestos = sel.filter((s) => s.split(',').some((p) => /[\s>+~]/.test(p.trim())));
  add('SEL', compuestos.length === 0, 'bloqueante', `una clase por regla, sin combinadores${compuestos.length ? ` (${compuestos.slice(0, 3).join(' | ')})` : ''}`);
  const ajenas = [...body.matchAll(/class="([^"]*)"/g)].flatMap((m) => m[1].split(/\s+/)).filter((k) => k && !k.startsWith(`mango-${id}`) && k !== 'mango-ilu');
  add('ID2', ajenas.length === 0, 'bloqueante', `clases con prefijo mango-${id}${ajenas.length ? ` (sin prefijo: ${[...new Set(ajenas)].slice(0, 4).join(', ')})` : ''}`);
  const ids = [...body.matchAll(/\sid="([^"]*)"/g)].map((m) => m[1]).filter((v) => !v.startsWith(`mango-${id}`));
  add('ID3', ids.length === 0, 'bloqueante', `ids con prefijo mango-${id} (dos ilustraciones en la misma página no chocan)${ids.length ? ` (${ids.join(', ')})` : ''}`);
  // Accesibilidad: decorativa u informativa, nunca las dos
  const hidden = attr(root, 'aria-hidden') === 'true';
  const titled = attr(root, 'role') === 'img' && (/<title\b[^>]*>[^<]{8,}<\/title>/.test(body) || !!attr(root, 'aria-label'));
  add('C1', hidden !== titled, 'bloqueante', hidden && titled ? 'aria-hidden y título a la vez: elige uno' : 'decorativa (aria-hidden="true") o informativa (role="img" + <title> que describe la escena)');
  // Peso y técnica
  const kb = statSync(file).size / 1024;
  add('P1', kb <= 30, kb <= 60 ? 'recomendado' : 'bloqueante', `peso ${kb.toFixed(1)} KB (≤30 recomendado, ≤60 máximo)`);
  add('P2', !/<image\b|data:image\//.test(src), 'bloqueante', 'sin imágenes incrustadas (todo vectorial)');
  add('P3', !/<filter\b|<foreignObject\b/.test(src), 'recomendado', 'sin filtros ni foreignObject (plano, ligero, predecible)');
  add('M1', !/animation|@keyframes/.test(css) || /prefers-reduced-motion/.test(css), 'bloqueante', 'si se mueve, respeta prefers-reduced-motion');
  return r;
}

let fail = false;
for (const f of process.argv.slice(2)) {
  const r = check(f); const blk = r.some((x) => !x.ok && x.level === 'bloqueante'); fail ||= blk;
  console.log(`${blk ? '❌' : '✅'} ${basename(f)}`);
  for (const x of r) console.log(`  ${x.ok ? '✅' : x.level === 'bloqueante' ? '❌' : '⚠️ '} ${x.code.padEnd(4)} ${x.msg}`);
}
if (!process.argv[2]) { console.log('Uso: node check-ilustracion.mjs <ilustracion.svg...>'); process.exit(2); }
process.exit(fail ? 1 : 0);
