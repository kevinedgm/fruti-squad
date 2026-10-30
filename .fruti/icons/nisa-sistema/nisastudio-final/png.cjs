// NisaStudio · exporta PNG con transparencia. Uso: node png.cjs (con NODE_PATH apuntando a playwright)
const {chromium} = require('playwright'); const fs = require('fs'); const path = require('path');
const D = __dirname;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage(); const out = path.join(D, 'png'); fs.mkdirSync(out, {recursive: true});
  async function shot(n, w, h) {
    await p.setViewportSize({width: w, height: h});
    const s = fs.readFileSync(path.join(D, 'svg', n + '.svg'), 'utf8').replace('<svg ', `<svg width="${w}" height="${h}" style="color:#3730A3;display:block" `);
    await p.setContent(`<html><body style="margin:0;background:transparent">${s}</body></html>`);
    await p.screenshot({path: path.join(out, `${n}-${w}.png`), omitBackground: true, clip: {x: 0, y: 0, width: w, height: h}});
  }
  for (const n of ['app-icon', 'app-icon-maskable', 'favicon']) for (const z of [16, 32, 64, 128, 180, 192, 512]) await shot(n, z, z);
  for (const n of ['simbolo', 'simbolo-blanco']) for (const z of [64, 128, 512]) await shot(n, z, z);
  
  for (const n of ['logotipo', 'logotipo-blanco', 'logotipo-respaldo', 'logotipo-respaldo-blanco', 'logotipo-vertical']) {
    const vb = fs.readFileSync(path.join(D, 'svg', n + '.svg'), 'utf8').match(/viewBox="([^"]+)"/)[1].split(' ').map(Number);
    for (const w of [512, 1024]) await shot(n, w, Math.round(w * vb[3] / vb[2]));
  }
  await b.close();
})();
