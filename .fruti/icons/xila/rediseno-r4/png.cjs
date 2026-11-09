const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:1});
for(const [k,t] of JSON.parse(fs.readFileSync(__dirname+'/svg/jobs.json','utf8'))){const s=fs.readFileSync(`${__dirname}/svg/${k}.svg`,'utf8');
await p.setViewportSize({width:t,height:t});await p.setContent(`<style>*{margin:0}svg{width:${t}px;height:${t}px;display:block}</style>${s}`);await p.screenshot({path:`${__dirname}/png/${k}-${t}.png`,omitBackground:true});}
await b.close();console.log('png ok')})();
