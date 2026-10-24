// Mide A2 (margen) y A6 (separación entre bordes) de cada icono: muestrea cada pieza en Chromium.
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module'; const { chromium } = createRequire(import.meta.url)('playwright');
const iconos = JSON.parse(readFileSync(process.argv[2] || 'piezas.json', 'utf8'));
const b = await chromium.launch(); const p = await b.newPage();
for (const [id, svg] of Object.entries(iconos)) {
  await p.setContent(svg);
  const r = await p.evaluate(() => {
    const sw = 1.5, piezas = [...document.querySelectorAll('[data-pieza]')].map(e => {
      const L = e.getTotalLength(), pts = [];
      for (let i = 0; i <= 400; i++) { const q = e.getPointAtLength(L * i / 400); pts.push([q.x, q.y]); }
      return { n: e.dataset.pieza, pts, h: e.getAttribute('class')?.includes('relleno') ? 0 : sw / 2 };
    });
    let margen = 99; for (const q of piezas) for (const [x, y] of q.pts) margen = Math.min(margen, x - q.h, y - q.h, 24 - x - q.h, 24 - y - q.h);
    const gaps = [];
    for (let i = 0; i < piezas.length; i++) for (let j = i + 1; j < piezas.length; j++) {
      let d = 99; for (const a of piezas[i].pts) for (const c of piezas[j].pts) d = Math.min(d, Math.hypot(a[0] - c[0], a[1] - c[1]));
      gaps.push([piezas[i].n + '/' + piezas[j].n, +(d - piezas[i].h - piezas[j].h).toFixed(2)]);
    }
    gaps.sort((x, y) => x[1] - y[1]);
    return { margen: +margen.toFixed(2), gaps: gaps.slice(0, 3) };
  });
  const mal = r.gaps.filter(g => g[1] < 1.5);
  console.log(id.padEnd(22), 'margen', r.margen, mal.length ? 'A6 ❌ ' + JSON.stringify(mal) : 'A6 ✅ min ' + JSON.stringify(r.gaps[0]));
}
await b.close();
