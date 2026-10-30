// NisaLab · exporta los PNG con transparencia. Uso: node png.cjs (con NODE_PATH apuntando a playwright)
const {chromium} = require('playwright'); const fs = require('fs'); const path = require('path');
const D = __dirname; const out = path.join(D, 'png'); fs.mkdirSync(out, {recursive: true});
const cuadrados = ['simbolo', 'simbolo-blanco', 'app-icon', 'app-icon-maskable', 'favicon'];
const anchos = ['logotipo', 'logotipo-blanco', 'logotipo-respaldo', 'logotipo-vertical'];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  async function shot(n, w, h, file) {
    await p.setViewportSize({width: w, height: h});
    const s = fs.readFileSync(path.join(D, 'svg', n + '.svg'), 'utf8').replace('<svg ', `<svg width="${w}" height="${h}" `);
    await p.setContent(`<html><body style="margin:0;background:transparent">${s}</body></html>`);
    await p.screenshot({path: path.join(out, file), omitBackground: true, clip: {x: 0, y: 0, width: w, height: h}});
  }
  for (const n of cuadrados) for (const z of [16, 32, 64, 128, 512]) await shot(n, z, z, `${n}-${z}.png`);
  for (const n of anchos) {
    const vb = fs.readFileSync(path.join(D, 'svg', n + '.svg'), 'utf8').match(/viewBox="([^"]+)"/)[1].split(' ').map(Number);
    for (const w of [512, 1024]) await shot(n, w, Math.round(w * vb[3] / vb[2]), `${n}-${w}.png`);
  }
  await b.close(); console.log('ok');
})();
