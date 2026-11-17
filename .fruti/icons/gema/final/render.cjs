// Renderiza los PNG de render.json con el Chromium de Playwright (fondo transparente).
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const P=JSON.parse(fs.readFileSync('render.json','utf8'));const b=await chromium.launch();
for(const [k,s] of Object.entries(P)){const z=+s.match(/width="(\d+)"/)[1];const p=await b.newPage({viewport:{width:z,height:z},deviceScaleFactor:1});
await p.setContent(`<html><body style="margin:0;background:transparent">${s}</body></html>`);await p.screenshot({path:k+'.png',omitBackground:true,clip:{x:0,y:0,width:z,height:z}});await p.close();}
await b.close();console.log('png ok');})();
