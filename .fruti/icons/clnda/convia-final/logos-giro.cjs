// Convia · logotipo de giro en un color («Convia | Hoteles»), pedido del usuario 2026-10-31 para los perfiles por giro.
// Parte de sellos/<giro>-logotipo.svg (ya trazado) y conserva solo la primera palabra del giro (corta en el primer hueco ancho entre letras).
// Uso: NODE_PATH=$(npm root -g) node logos-giro.cjs → sellos/<giro>-logotipo-giro.svg
const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
const D=__dirname;const T=JSON.parse(fs.readFileSync(path.join(D,'tema.json')));
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.setContent('<svg xmlns="http://www.w3.org/2000/svg" id="s"></svg>');
for(const [k,c] of Object.entries(T.categorias)){const s=fs.readFileSync(path.join(D,'sellos',k+'-logotipo.svg'),'utf8');
 const paths=s.match(/<path[^>]*\/>/g);const d=paths[2].match(/ d="([^"]+)"/)[1];const subs=d.match(/M[^M]+/g);
 const bb=await p.evaluate(subs=>subs.map(d=>{const e=document.createElementNS('http://www.w3.org/2000/svg','path');e.setAttribute('d',d);document.getElementById('s').appendChild(e);const r=e.getBBox();e.remove();return [r.x,r.x+r.width]}),subs);
 const order=bb.map((r,i)=>[r,i]).sort((a,b)=>a[0][0]-b[0][0]);let end=order[0][0][1],cut=Infinity;
 for(const [r] of order.slice(1)){if(r[0]-end>8){cut=end;break}end=Math.max(end,r[1])}
 const keep=subs.filter((_,i)=>bb[i][1]<=cut+0.5).join('');const W=Math.ceil((cut===Infinity?end:cut)+4);const nombre=c.nombre.split(' ')[0];const col=c.texto;
 const out=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} 68" role="img" aria-label="Convia ${nombre}">`+paths[0].replace(/fill="[^"]*"/,`fill="${col}"`)+paths[1].replace(/fill="[^"]*"/,`fill="${col}"`)
  +s.match(/<rect[^>]*\/>/)[0].replace(/fill="[^"]*"/,`fill="${col}"`)+`<path d="${keep}" fill="${col}"/></svg>`;
 fs.writeFileSync(path.join(D,'sellos',k+'-logotipo-giro.svg'),out);console.log(k,nombre,W)}
await b.close()})();
