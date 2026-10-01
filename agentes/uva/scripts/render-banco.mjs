#!/usr/bin/env node
// Uva · renderiza las capturas del banco de prueba (etapa E3) sin escribir el comando de Chromium a mano.
// Uso: node render-banco.mjs <banco.html> [--modo final|medio|reducido|todos] [--salida <dir>]
//   Genera banco-<modo>.png junto al banco (o en --salida), escala 2, ventana 900×1100, virtual-time-budget 1500.
//   Modos: final (fotograma tras la animación) · medio (instante común a mitad del ciclo, R4) · reducido (D2).
// Navegador: $CHROMIUM, Chromium de Playwright ($PLAYWRIGHT_BROWSERS_PATH o /opt/pw-browsers), chromium /
// chromium-browser / google-chrome en el PATH; si no hay ninguno, el paquete `playwright` de Node.

import { existsSync, readdirSync } from 'node:fs';
import { basename, dirname, join, resolve } from 'node:path';
import { spawnSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const opt = (name, def) => { const i = args.indexOf(name); return i >= 0 ? args.splice(i, 2)[1] : def; };
const modo = opt('--modo', 'todos');
const salidaArg = opt('--salida', null);
const banco = args[0];
const MODOS = ['final', 'medio', 'reducido'];

if (!banco) { console.error('Uso: node render-banco.mjs <banco.html> [--modo final|medio|reducido|todos] [--salida <dir>]'); process.exit(2); }
if (!existsSync(banco)) { console.error(`No existe ${banco}.`); process.exit(2); }
const modos = modo === 'todos' ? MODOS : [modo];
if (modos.some((m) => !MODOS.includes(m))) { console.error(`Modo desconocido: ${modo}. Usa final, medio, reducido o todos.`); process.exit(2); }

const ruta = resolve(banco);
const salida = resolve(salidaArg || dirname(ruta));
const base = basename(ruta).replace(/\.html?$/, '');
const VENTANA = [900, 1100];

function buscarChromium() {
  const candidatos = [];
  if (process.env.CHROMIUM) candidatos.push(process.env.CHROMIUM);
  for (const raiz of [process.env.PLAYWRIGHT_BROWSERS_PATH, '/opt/pw-browsers', join(process.env.HOME || '', '.cache/ms-playwright')].filter(Boolean)) {
    if (!existsSync(raiz)) continue;
    for (const d of readdirSync(raiz).filter((x) => /^chromium-\d+/.test(x)).sort().reverse()) {
      candidatos.push(join(raiz, d, 'chrome-linux', 'chrome'), join(raiz, d, 'chrome-mac', 'Chromium.app', 'Contents', 'MacOS', 'Chromium'));
    }
  }
  for (const bin of ['chromium', 'chromium-browser', 'google-chrome', 'google-chrome-stable']) {
    const w = spawnSync('which', [bin], { encoding: 'utf8' });
    if (w.status === 0 && w.stdout.trim()) candidatos.push(w.stdout.trim());
  }
  return candidatos.find((c) => existsSync(c)) || null;
}

async function conPlaywright() {
  let pw;
  try { pw = await import('playwright'); } catch { return false; }
  const navegador = await pw.chromium.launch();
  for (const m of modos) {
    const pagina = await navegador.newPage({ viewport: { width: VENTANA[0], height: VENTANA[1] }, deviceScaleFactor: 2 });
    await pagina.goto(`${pathToFileURL(ruta).href}#${m}`);
    await pagina.waitForTimeout(1500);
    const png = join(salida, `${base}-${m}.png`);
    await pagina.screenshot({ path: png });
    console.log(`✅ ${png}`);
    await pagina.close();
  }
  await navegador.close();
  return true;
}

const chrome = buscarChromium();
if (chrome) {
  let ok = true;
  for (const m of modos) {
    const png = join(salida, `${base}-${m}.png`);
    const r = spawnSync(chrome, [
      '--headless', '--no-sandbox', '--hide-scrollbars', '--force-device-scale-factor=2',
      '--disable-background-networking', '--disable-component-update', '--no-first-run',
      `--window-size=${VENTANA.join(',')}`, '--virtual-time-budget=1500',
      `--screenshot=${png}`, `${pathToFileURL(ruta).href}#${m}`,
    ], { encoding: 'utf8' });
    if (r.status === 0 && existsSync(png)) console.log(`✅ ${png}`);
    else { ok = false; console.error(`❌ ${m}: Chromium falló (${r.status}). ${(r.stderr || '').split('\n').filter((l) => !/dbus|bus\.cc/.test(l)).slice(-3).join(' ')}`); }
  }
  process.exit(ok ? 0 : 1);
} else if (!(await conPlaywright())) {
  console.error('No encontré Chromium ni el paquete playwright. Define CHROMIUM=/ruta/al/navegador o instala playwright en el proyecto.');
  process.exit(2);
}
