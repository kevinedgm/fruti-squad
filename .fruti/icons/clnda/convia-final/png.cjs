// Exporta PNG desde los SVG del paquete. Uso: node png.cjs
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
const jobs=[['app-icon',512,512],['app-icon',192,192],['app-icon',180,180],['simbolo',512,512],['og',1200,630]];
for(const [n,w,h] of jobs){const s=fs.readFileSync(path.join(__dirname,'svg',n+'.svg'),'utf8');
await p.setViewportSize({width:w,height:h});await p.setContent(`<html><body style="margin:0;background:transparent">${s.replace('<svg ',`<svg width="${w}" height="${h}" `)}</body></html>`);
await p.screenshot({path:path.join(__dirname,'png',`${n}-${w===h?w:w+'x'+h}.png`),omitBackground:true,clip:{x:0,y:0,width:w,height:h}});}
await b.close()})();
