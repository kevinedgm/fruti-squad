// NisaLab · áreas · exporta PNG con transparencia. Uso: node png.cjs (con NODE_PATH apuntando a playwright)
const {chromium} = require('playwright'); const fs = require('fs'); const path = require('path');
const D = __dirname;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  async function shot(file, w, h, dest) {
    await p.setViewportSize({width: w, height: h});
    const s = fs.readFileSync(file, 'utf8').replace('<svg ', `<svg width="${w}" height="${h}" style="color:#141B33" `);
    await p.setContent(`<html><body style="margin:0;background:transparent">${s}</body></html>`);
    await p.screenshot({path: dest, omitBackground: true, clip: {x: 0, y: 0, width: w, height: h}});
  }
  for (const area of fs.readdirSync(path.join(D, 'svg'))) {
    const out = path.join(D, 'png', area); fs.mkdirSync(out, {recursive: true});
    for (const n of ['marca', 'marca-blanco', 'icono'])
      for (const z of [16, 32, 64, 128, 512]) await shot(path.join(D, 'svg', area, n + '.svg'), z, z, path.join(out, `${n}-${z}.png`));
    for (const n of ['logotipo', 'logotipo-blanco']) {
      const f = path.join(D, 'svg', area, n + '.svg');
      const vb = fs.readFileSync(f, 'utf8').match(/viewBox="([^"]+)"/)[1].split(' ').map(Number);
      for (const w of [512, 1024]) await shot(f, w, Math.round(w * vb[3] / vb[2]), path.join(out, `${n}-${w}.png`));
    }
  }
  await b.close(); console.log('ok');
})();
