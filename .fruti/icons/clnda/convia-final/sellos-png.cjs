// Exporta los sellos a PNG 512. Uso: node sellos-png.cjs
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:512,height:512}});
for(const f of fs.readdirSync(path.join(__dirname,'sellos')).filter(f=>f.endsWith('-sello.svg')||f.endsWith('-sello-solido.svg'))){
const s=fs.readFileSync(path.join(__dirname,'sellos',f),'utf8').replace('<svg ','<svg width="512" height="512" ');
await p.setContent(`<html><body style="margin:0;background:transparent">${s}</body></html>`);
await p.screenshot({path:path.join(__dirname,'png',f.replace('.svg','-512.png')),omitBackground:true,clip:{x:0,y:0,width:512,height:512}});}
await b.close()})();
