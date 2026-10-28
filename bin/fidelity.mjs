#!/usr/bin/env node
// FID-GEOMETRY-001 · Structural fidelity F2 → F3.
//
// Kiwi marks every piece of the approved F2 with `data-piece="<id>"`. Coco keeps the
// same markers in F3. This script renders both at every verification viewport and
// compares the geometry of the marked pieces. It does not compare pixels or style:
// it checks that the decisions Kiwi froze (grouping, order, rows, spacing, size)
// survived construction.
//
// Usage:
//   fruti fidelity --f2 .fruti/tests/r01/kiwi-f2.html --f3 http://localhost:5173/usuarios
//                  [--viewports 1440,1024,768,390] [--height 900] [--tolerance 2]
//                  [--slack 16] [--round r01] [--out .fruti/tests/r01/fidelity.json]
//
// Exit codes: 0 pass · 1 fail · 2 usage error · 3 blocked (no browser / no markers / not loadable).
// A blocked run is never a pass.
//
// Optional per-piece attributes (in F2, they declare an approved freedom):
//   data-piece-free="size"  width/height may change freely
//   data-piece-free="gap"   spacing to siblings may change freely
//   data-piece-free="all"   only presence, grouping and order are checked

import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, join, resolve } from 'node:path';
import { pathToFileURL, fileURLToPath } from 'node:url';

const RULE = 'FID-GEOMETRY-001';
const here = dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const o = { viewports: [1440, 1024, 768, 390], height: 900, tolerance: 2, slack: 16, round: null, out: null, f2: null, f3: null };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    const v = () => argv[++i];
    if (a === '--f2') o.f2 = v();
    else if (a === '--f3') o.f3 = v();
    else if (a === '--viewports') o.viewports = String(v()).split(',').map(Number).filter(n => n > 0);
    else if (a === '--height') o.height = Number(v());
    else if (a === '--tolerance') o.tolerance = Number(v());
    else if (a === '--slack') o.slack = Number(v());
    else if (a === '--round') o.round = v();
    else if (a === '--out') o.out = v();
    else if (a === '-h' || a === '--help') o.help = true;
  }
  return o;
}

const USAGE = 'Uso: fruti fidelity --f2 <kiwi-f2.html> --f3 <archivo.html|URL> [--viewports 1440,1024,768,390] [--round rNN] [--out ruta.json]';

function toUrl(target) {
  if (/^https?:\/\//i.test(target) || /^file:\/\//i.test(target)) return target;
  const abs = resolve(process.cwd(), target);
  if (!existsSync(abs)) return null;
  return pathToFileURL(abs).href;
}

function loadPlaywright() {
  const bases = [join(process.cwd(), 'package.json'), join(here, '..', 'package.json')];
  for (const base of bases) {
    try { return createRequire(base)('playwright'); } catch {}
  }
  return null;
}

// Runs in the page: collects every marked piece with its box, visibility and parent piece.
function collect() {
  const out = [];
  for (const el of document.querySelectorAll('[data-piece]')) {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    const visible = r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none' && Number(cs.opacity) > 0;
    const parentEl = el.parentElement ? el.parentElement.closest('[data-piece]') : null;
    out.push({
      id: el.getAttribute('data-piece'),
      parent: parentEl ? parentEl.getAttribute('data-piece') : null,
      free: (el.getAttribute('data-piece-free') || '').split(/[\s,]+/).filter(Boolean),
      visible,
      display: cs.display,
      x: r.left + window.scrollX, y: r.top + window.scrollY, w: r.width, h: r.height,
    });
  }
  return out;
}

const round1 = n => Math.round(n * 10) / 10;

function relation(a, b) {
  const ix = Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x);
  const iy = Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y);
  if (ix > 1 && iy > 1) return 'overlap';
  const vOverlap = iy / Math.min(a.h, b.h);
  if (vOverlap >= 0.5) return a.x <= b.x ? 'left-of' : 'right-of';
  return a.y <= b.y ? 'above' : 'below';
}

function gap(a, b, rel) {
  if (rel === 'left-of') return b.x - (a.x + a.w);
  if (rel === 'right-of') return a.x - (b.x + b.w);
  if (rel === 'above') return b.y - (a.y + a.h);
  if (rel === 'below') return a.y - (b.y + b.h);
  return 0;
}

const outOfBand = (v2, v3, tol, slack) =>
  (v3 > Math.max(v2 * tol, v2 + slack)) || (v3 < Math.min(v2 / tol, v2 - slack));

// Adjacent pairs: siblings in the same direction with no other sibling between them.
function adjacent(siblings, a, b, rel) {
  const between = s => {
    if (s.id === a.id || s.id === b.id) return false;
    if (rel === 'left-of' || rel === 'right-of') {
      const [l, r] = rel === 'left-of' ? [a, b] : [b, a];
      return relation(l, s) === 'left-of' && relation(s, r) === 'left-of';
    }
    const [t, d] = rel === 'above' ? [a, b] : [b, a];
    return relation(t, s) === 'above' && relation(s, d) === 'above';
  };
  return !siblings.some(between);
}

function compare(f2, f3, vw, opt, elastic = new Set()) {
  const findings = [];
  const add = (check, pieces, expected, found, message) =>
    findings.push({ rule_id: RULE, check, viewport: vw, pieces, expected, found, message });
  const m3 = new Map(f3.map(p => [p.id, p]));

  for (const p of f2) {
    const q = m3.get(p.id);
    if (!q) { add('presence', [p.id], 'marcada en F3', 'ausente', `La pieza «${p.id}» existe en F2 pero no está marcada en F3.`); continue; }
    if (p.visible && !q.visible && q.display === 'contents') add('grouping', [p.id], 'grupo con caja propia', 'display: contents', `A ${vw}px el grupo «${p.id}» se disolvió (display: contents): sus piezas ya no se mantienen juntas.`);
    else if (p.visible !== q.visible) add('visibility', [p.id], p.visible ? 'visible' : 'oculta', q.visible ? 'visible' : 'oculta', `A ${vw}px la pieza «${p.id}» cambia de visibilidad respecto a F2.`);
    if (p.parent !== q.parent) add('grouping', [p.id], p.parent || '(raíz)', q.parent || '(raíz)', `La pieza «${p.id}» salió de su grupo: en F2 pertenece a «${p.parent || 'raíz'}» y en F3 a «${q.parent || 'raíz'}».`);
  }

  const visible2 = f2.filter(p => p.visible && m3.get(p.id)?.visible);
  const groups = new Map();
  for (const p of visible2) {
    const k = p.parent || '';
    if (!groups.has(k)) groups.set(k, []);
    groups.get(k).push(p);
  }

  for (const siblings of groups.values()) {
    for (let i = 0; i < siblings.length; i++) {
      for (let j = i + 1; j < siblings.length; j++) {
        const a2 = siblings[i], b2 = siblings[j];
        const a3 = m3.get(a2.id), b3 = m3.get(b2.id);
        const r2 = relation(a2, b2), r3 = relation(a3, b3);
        if (r2 !== r3) {
          add('relation', [a2.id, b2.id], r2, r3, `A ${vw}px «${a2.id}» debía estar ${label(r2)} «${b2.id}», y en F3 está ${label(r3)}.`);
          continue;
        }
        if (r2 === 'overlap') continue;
        const free = new Set([...a2.free, ...b2.free]);
        if (free.has('gap') || free.has('all')) continue;
        if (!adjacent(siblings, a2, b2, r2)) continue;
        const g2 = gap(a2, b2, r2), g3 = gap(a3, b3, r3);
        if (elastic.has(pairKey(a2.id, b2.id))) {
          // Elastic gap in F2 (it grows with the space, e.g. space-between): only a collapse is a defect.
          if (g2 >= 8 && g3 < 4) add('gap', [a2.id, b2.id], round1(g2), round1(g3), `A ${vw}px «${a2.id}» y «${b2.id}» quedaron pegadas: en F2 los separa ${round1(g2)}px y en F3 ${round1(g3)}px.`);
        } else if (outOfBand(g2, g3, opt.tolerance, opt.slack)) {
          add('gap', [a2.id, b2.id], round1(g2), round1(g3), `A ${vw}px la separación entre «${a2.id}» y «${b2.id}» pasó de ${round1(g2)}px en F2 a ${round1(g3)}px en F3.`);
        }
      }
    }
  }

  // Intrusion: a piece from outside a group lands inside the area its members occupy
  // (e.g. the action button placed between the title and the subtitle).
  const parentOf = new Map(f2.map(p => [p.id, p.parent]));
  const isInside = (id, groupId) => { for (let c = parentOf.get(id); c; c = parentOf.get(c)) if (c === groupId) return true; return false; };
  const area = list => list.length && ({
    x: Math.min(...list.map(p => p.x)), y: Math.min(...list.map(p => p.y)),
    w: Math.max(...list.map(p => p.x + p.w)) - Math.min(...list.map(p => p.x)),
    h: Math.max(...list.map(p => p.y + p.h)) - Math.min(...list.map(p => p.y)),
  });
  const hits = (a, b) => Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x) > 1 && Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y) > 1;
  for (const g of new Set(f2.map(p => p.parent).filter(Boolean))) {
    const members2 = visible2.filter(p => isInside(p.id, g));
    if (members2.length < 2) continue;
    const zone2 = area(members2), zone3 = area(members2.map(p => m3.get(p.id)));
    for (const o of visible2) {
      if (o.id === g || isInside(o.id, g) || isInside(g, o.id)) continue;
      const o3 = m3.get(o.id);
      if (hits(zone3, o3) && !hits(zone2, o)) add('intrusion', [o.id, g], `fuera de «${g}»`, `dentro de «${g}»`, `A ${vw}px «${o.id}» quedó metida entre las piezas del grupo «${g}».`);
    }
  }

  for (const p of visible2) {
    if (p.free.includes('size') || p.free.includes('all')) continue;
    const q = m3.get(p.id);
    for (const [dim, name] of [['w', 'ancho'], ['h', 'alto']]) {
      if (outOfBand(p[dim], q[dim], opt.tolerance, opt.slack * 1.5)) {
        add('size', [p.id], round1(p[dim]), round1(q[dim]), `A ${vw}px el ${name} de «${p.id}» pasó de ${round1(p[dim])}px en F2 a ${round1(q[dim])}px en F3.`);
      }
    }
  }
  return findings;
}

const pairKey = (a, b) => (a < b ? a + '|' + b : b + '|' + a);

// A sibling gap is elastic when, in F2, it changes with the viewport (space-between, auto margins).
// A gap that stays constant across viewports is a spacing decision and is compared strictly.
function elasticPairs(runs, slack) {
  const seen = new Map();
  for (const { f2 } of runs) {
    const groups = new Map();
    for (const p of f2.filter(p => p.visible)) {
      const k = p.parent || '';
      if (!groups.has(k)) groups.set(k, []);
      groups.get(k).push(p);
    }
    for (const sib of groups.values()) for (let i = 0; i < sib.length; i++) for (let j = i + 1; j < sib.length; j++) {
      const r = relation(sib[i], sib[j]);
      if (r === 'overlap') continue;
      const k = pairKey(sib[i].id, sib[j].id);
      if (!seen.has(k)) seen.set(k, []);
      seen.get(k).push(gap(sib[i], sib[j], r));
    }
  }
  const out = new Set();
  for (const [k, gaps] of seen) if (gaps.length > 1 && Math.max(...gaps) - Math.min(...gaps) > slack) out.add(k);
  return out;
}

function label(rel) {
  return { 'left-of': 'a la izquierda de', 'right-of': 'a la derecha de', above: 'encima de', below: 'debajo de', overlap: 'encimado con' }[rel] || rel;
}

function finish(report, opt) {
  const json = JSON.stringify(report, null, 2) + '\n';
  if (opt.out) {
    const out = resolve(process.cwd(), opt.out);
    mkdirSync(dirname(out), { recursive: true });
    writeFileSync(out, json);
  }
  process.stdout.write(json);
  const tag = { pass: 'PASS', fail: 'FAIL', blocked: 'BLOCKED' }[report.status];
  process.stderr.write(`${RULE} ${tag}` + (report.status === 'fail' ? ` · ${report.findings.length} hallazgo(s)` : report.reason ? ` · ${report.reason}` : '') + '\n');
  process.exit(report.status === 'pass' ? 0 : report.status === 'fail' ? 1 : 3);
}

async function main() {
  const opt = parseArgs(process.argv.slice(2));
  if (opt.help || !opt.f2 || !opt.f3) { console.error(USAGE); process.exit(opt.help ? 0 : 2); }
  const base = { rule_id: RULE, round: opt.round, f2: opt.f2, f3: opt.f3, viewports: opt.viewports, tolerance: opt.tolerance, slack_px: opt.slack };

  const u2 = toUrl(opt.f2), u3 = toUrl(opt.f3);
  if (!u2 || !u3) finish({ ...base, status: 'blocked', reason: `no encuentro ${!u2 ? opt.f2 : opt.f3}`, findings: [] }, opt);

  const pw = loadPlaywright();
  if (!pw) finish({ ...base, status: 'blocked', reason: 'Playwright no está instalado en el proyecto (npm i -D playwright && npx playwright install chromium)', findings: [] }, opt);

  let browser;
  try { browser = await pw.chromium.launch(); }
  catch (e) { finish({ ...base, status: 'blocked', reason: 'no se pudo abrir Chromium: ' + String(e.message).split('\n')[0], findings: [] }, opt); }

  const runs = [];
  try {
    for (const vw of opt.viewports) {
      const page = await browser.newPage({ viewport: { width: vw, height: opt.height } });
      await page.goto(u2, { waitUntil: 'networkidle' });
      // Kiwi's wireframe kit simulates the space with a frame (#wf-frame + container queries).
      // Size that frame to the verification viewport so F2 and F3 are compared in the same mode.
      await page.evaluate(w => {
        /* global S, render */
        if (typeof S === 'object' && S && typeof render === 'function') { S.w = w; render(); }
        else { const f = document.getElementById('wf-frame'); if (f) f.style.setProperty('--wf-w', w + 'px'); }
      }, vw);
      const f2 = await page.evaluate(collect);
      await page.goto(u3, { waitUntil: 'networkidle' });
      const f3 = await page.evaluate(collect);
      await page.close();
      if (!f2.length) { await browser.close(); finish({ ...base, status: 'blocked', reason: 'el F2 no tiene piezas marcadas con data-piece', findings: [] }, opt); }
      runs.push({ vw, f2, f3 });
    }
  } finally { await browser?.close().catch(() => {}); }

  const elastic = elasticPairs(runs, opt.slack);
  const findings = runs.flatMap(r => compare(r.f2, r.f3, r.vw, opt, elastic));
  const measured = runs.map(r => ({ viewport: r.vw, f2_pieces: r.f2.length, f3_pieces: r.f3.length }));

  finish({ ...base, status: findings.length ? 'fail' : 'pass', measured, findings }, opt);
}

main();
