// Captura las portadas del kit: node kit.cjs
const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const [src,out,w,h] of JSON.parse(fs.readFileSync(__dirname+'/kit/src/jobs.json','utf8'))){await p.setViewportSize({width:w,height:h});await p.goto('file://'+src);await p.waitForTimeout(200);await p.screenshot({path:out});}
await b.close();console.log('ok')})();
