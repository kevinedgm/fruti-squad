// PNG: node png.cjs
const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const [n,w,h,out] of [['simbolo',512,512,'simbolo-512'],['simbolo-oscuro',512,512,'simbolo-oscuro-512'],['app-icon',512,512,'icon-512'],['app-icon',192,192,'icon-192'],['app-icon-redondeado',512,512,'icon-redondeado-512'],['simbolo-16',32,32,'favicon-32'],['tarjeta-redes',1200,630,'tarjeta-redes'],['wordmark',1200,0,'wordmark'],['wordmark-oscuro',1200,0,'wordmark-oscuro']]){
const svg=fs.readFileSync(`${__dirname}/svg/${n}.svg`,'utf8');const vb=svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);const H=h||Math.round(w*vb[2]/vb[1]);
await p.setViewportSize({width:w,height:H});await p.setContent(`<style>*{margin:0}svg{width:${w}px;height:${H}px;display:block}</style>${svg}`);
await p.screenshot({path:`${__dirname}/png/${out}.png`,omitBackground:true});}await b.close();console.log('ok')})();
