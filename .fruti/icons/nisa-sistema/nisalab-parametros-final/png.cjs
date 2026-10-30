// NisaLab · tipos de parámetro · exporta PNG con transparencia. Uso: node png.cjs (con NODE_PATH apuntando a playwright)
const {chromium} = require('playwright'); const fs = require('fs'); const path = require('path');
const D = __dirname;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const t of fs.readdirSync(path.join(D, 'svg'))) {
    const out = path.join(D, 'png', t); fs.mkdirSync(out, {recursive: true});
    for (const n of ['ficha', 'ficha-blanco', 'ficha-1tinta'])
      for (const z of [16, 24, 32, 64, 128, 512]) {
        await p.setViewportSize({width: z, height: z});
        const s = fs.readFileSync(path.join(D, 'svg', t, n + '.svg'), 'utf8').replace('<svg ', `<svg width="${z}" height="${z}" style="color:#141B33;display:block" `);
        await p.setContent(`<html><body style="margin:0;background:transparent">${s}</body></html>`);
        await p.screenshot({path: path.join(out, `${n}-${z}.png`), omitBackground: true, clip: {x: 0, y: 0, width: z, height: z}});
      }
  }
  await b.close();
})();
