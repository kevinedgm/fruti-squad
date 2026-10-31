// Convia · silueta sólida de la estrella E1b (contorno exterior), para rellenarla (p. ej. degradado del QR de mesa).
// La estrella es un solo trazo con hueco; aquí se muestrea el trazo y, en cada dirección desde el centro, se toma el punto más lejano.
// Uso: NODE_PATH=$(npm root -g) node silueta.cjs → svg/simbolo-silueta.svg
const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
const D=__dirname;const svg=fs.readFileSync(path.join(D,'svg/simbolo.svg'),'utf8');const d=svg.match(/ d="([^"]+)"/)[1];
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.setContent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"><path id="s"/></svg>');
const pts=await p.evaluate(d=>{const e=document.getElementById('s');e.setAttribute('d',d);const L=e.getTotalLength();const bb=e.getBBox();const cx=bb.x+bb.width/2,cy=bb.y+bb.height/2;
 const N=720,best=new Array(N).fill(null);for(let i=0;i<6000;i++){const q=e.getPointAtLength(L*i/6000);const a=Math.atan2(q.y-cy,q.x-cx);const k=Math.floor(((a+Math.PI)/(2*Math.PI))*N)%N;const r=Math.hypot(q.x-cx,q.y-cy);if(!best[k]||r>best[k].r)best[k]={x:q.x,y:q.y,r}}
 const out=best.filter(Boolean);return {cx,cy,pts:out.map(o=>[+o.x.toFixed(2),+o.y.toFixed(2)])}},d);
const P=pts.pts;let s=`M${P[0][0]} ${P[0][1]}`;for(let i=1;i<P.length;i++)s+=`L${P[i][0]} ${P[i][1]}`;s+='Z';
fs.writeFileSync(path.join(D,'svg/simbolo-silueta.svg'),`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" role="img" aria-label="Convia"><path d="${s}" fill="#2f5a45"/></svg>`);
console.log('ok',P.length,'puntos; centro',pts.cx.toFixed(1),pts.cy.toFixed(1));
await p.setContent(`<div style="display:flex;gap:20px;padding:20px">${svg.replace('<svg ','<svg width="300" height="300" ')}<svg width="300" height="300" viewBox="0 0 200 200"><path d="${s}" fill="#2f5a45" opacity=".35"/><path d="${d}" fill="#2f5a45"/></svg></div>`);
await p.screenshot({path:process.argv[2]||'/dev/null'});await b.close()})();
