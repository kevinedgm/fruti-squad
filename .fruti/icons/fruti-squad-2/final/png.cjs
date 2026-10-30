// PNG: node png.cjs (NODE_PATH con playwright)
const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const k of ['squad','kiwi','lima','coco','bruno','mora']){fs.mkdirSync(`${__dirname}/${k}/png`,{recursive:true});
for(const [n,s] of [['app-icon',512],['app-icon',192],['simbolo',512],['simbolo-oscuro',512]]){
const svg=fs.readFileSync(`${__dirname}/${k}/svg/${n}.svg`,'utf8');await p.setViewportSize({width:s,height:s});
await p.setContent(`<style>*{margin:0}svg{width:${s}px;height:${s}px;display:block}</style>${svg}`);
await p.screenshot({path:`${__dirname}/${k}/png/${n}-${s}.png`,omitBackground:true});}}await b.close();console.log('ok')})();
