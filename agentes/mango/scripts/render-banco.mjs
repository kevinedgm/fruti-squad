#!/usr/bin/env node
// Mango · banco de prueba: pone la ilustración en una sección real (escritorio, móvil, oscuro, 3 temas)
// y comprueba que el SVG abre como imagen. Genera <nombre>-banco.html y <nombre>-banco.png.
// Uso: node render-banco.mjs <ilustracion.svg> [--titulo "Texto del titular"] [--salida <dir>]
// Navegador: $CHROMIUM, Chromium de Playwright ($PLAYWRIGHT_BROWSERS_PATH o /opt/pw-browsers) o el del PATH.
import { existsSync, readdirSync, readFileSync, writeFileSync, copyFileSync } from 'node:fs';
import { basename, dirname, join, resolve } from 'node:path';
import { spawnSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const opt = (n, d) => { const i = args.indexOf(n); return i >= 0 ? args.splice(i, 2)[1] : d; };
const titulo = opt('--titulo', 'Te explicamos cada paso');
const salidaArg = opt('--salida', null);
const svgPath = args[0];
if (!svgPath || !existsSync(svgPath)) { console.error('Uso: node render-banco.mjs <ilustracion.svg> [--titulo "…"] [--salida <dir>]'); process.exit(2); }

const svg = readFileSync(svgPath, 'utf8').replace(/<\?xml[^>]*>/, '');
const salida = resolve(salidaArg || dirname(resolve(svgPath)));
const base = basename(svgPath).replace(/\.svg$/, '');
copyFileSync(svgPath, join(salida, basename(svgPath)));
const temas = [
  ['claro (por defecto)', ''],
  ['tema verde', '--mango-acento:#0f8a5f;--mango-acento-2:#e76f51;--mango-forma:#e3f1ea;--mango-linea:#b9dccb'],
  ['tema coral', '--mango-acento:#e5484d;--mango-acento-2:#3e63dd;--mango-forma:#fde8e8;--mango-linea:#f3c2c2;--mango-piel:#8d5a3c'],
];
const oscuro = '--mango-superficie:#23243a;--mango-forma:#2e3050;--mango-linea:#4b4e78;--mango-tinta:#0e0f1c';
const texto = (c) => `<div class="tx"><span class="eti" style="color:${c}">Ayuda</span><h2>${titulo}</h2><p>Texto de ejemplo de la sección: dos líneas que acompañan a la ilustración para juzgar el equilibrio.</p><span class="btn">Empezar</span></div>`;
const html = `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Mango · banco</title><style>
body{margin:0;padding:20px;background:#eceef3;font:15px/1.5 system-ui,sans-serif;color:#1b1c2b}h1{font-size:15px;margin:0 0 8px;color:#555}
.sec{display:grid;grid-template-columns:1fr 1.15fr;gap:28px;align-items:center;background:#fff;border-radius:16px;padding:28px 32px;margin-bottom:18px;width:900px;box-sizing:border-box}
.sec svg{width:100%;height:auto;display:block}.tx h2{font-size:30px;line-height:1.15;margin:6px 0 10px}.tx p{margin:0 0 16px;color:#5c5f73}
.eti{font-weight:600;font-size:13px}.btn{display:inline-block;background:#1b1c2b;color:#fff;border-radius:10px;padding:10px 16px;font-weight:600}
.fila{display:flex;gap:18px;align-items:flex-start}.movil{width:360px;background:#fff;border-radius:22px;padding:20px;box-sizing:border-box}.movil svg{width:100%;height:auto;display:block;margin-bottom:12px}.movil h2{font-size:24px}
.osc{background:#15162a;color:#f2f2f7}.osc .tx p{color:#a7a9c0}.osc .btn{background:#fff;color:#15162a}
.temas{display:flex;gap:14px}.tema{background:#fff;border-radius:14px;padding:12px;width:290px;box-sizing:border-box;font-size:12px;color:#666}.tema svg{width:100%;height:auto;display:block}
.img{background:#fff;border-radius:14px;padding:12px 16px;margin-top:18px;font-size:13px;width:900px;box-sizing:border-box}
</style></head><body>
<h1>Escritorio · 900 px</h1><div class="sec">${texto('#5b5bd6')}<div>${svg}</div></div>
<div class="fila"><div><h1>Móvil · 360 px</h1><div class="movil">${svg}${texto('#5b5bd6')}</div></div>
<div><h1>Oscuro (tokens oscuros del proyecto)</h1><div class="sec osc" style="width:520px;grid-template-columns:1fr;${oscuro}"><div>${svg}</div></div></div></div>
<h1>El tema pone el color</h1><div class="temas">${temas.map(([n, v]) => `<div class="tema" style="${v}">${svg}<div>${n}</div></div>`).join('')}</div>
<div class="img" id="img">Como imagen (&lt;img&gt;): comprobando…</div>
<script>const i=new Image();i.src=${JSON.stringify(basename(svgPath))};i.decode().then(()=>{document.getElementById('img').textContent='✅ Abre como imagen (<img>, CSS background, favicon): XML válido.'}).catch(()=>{document.getElementById('img').textContent='❌ NO abre como imagen: XML inválido (revisa X1 en check-ilustracion).'})</script>
</body></html>`;
const out = join(salida, `${base}-banco.html`); writeFileSync(out, html);

function chromium() {
  const c = [];
  if (process.env.CHROMIUM) c.push(process.env.CHROMIUM);
  for (const raiz of [process.env.PLAYWRIGHT_BROWSERS_PATH, '/opt/pw-browsers', join(process.env.HOME || '', '.cache/ms-playwright')].filter(Boolean)) {
    if (!existsSync(raiz)) continue;
    for (const d of readdirSync(raiz).filter((x) => /^chromium-\d+/.test(x)).sort().reverse()) c.push(join(raiz, d, 'chrome-linux', 'chrome'), join(raiz, d, 'chrome-mac', 'Chromium.app', 'Contents', 'MacOS', 'Chromium'));
    if (existsSync(join(raiz, 'chromium'))) c.push(join(raiz, 'chromium'));
  }
  for (const b of ['chromium', 'chromium-browser', 'google-chrome']) { const w = spawnSync('which', [b], { encoding: 'utf8' }); if (w.status === 0 && w.stdout.trim()) c.push(w.stdout.trim()); }
  return c.find((x) => existsSync(x)) || null;
}
const png = join(salida, `${base}-banco.png`);
const bin = chromium();
if (!bin) { console.log(`Banco: ${out}\n(no hay Chromium: ábrelo en el navegador)`); process.exit(0); }
const r = spawnSync(bin, ['--headless', '--no-sandbox', '--hide-scrollbars', '--allow-file-access-from-files', '--force-device-scale-factor=1.5', '--window-size=960,1400', '--virtual-time-budget=2000', `--screenshot=${png}`, pathToFileURL(out).href], { encoding: 'utf8' });
console.log(r.status === 0 && existsSync(png) ? `✅ ${png}` : `❌ Chromium falló: ${(r.stderr || '').slice(0, 300)}`);
