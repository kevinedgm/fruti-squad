// Mide la simetría bilateral de cada emblema en el render: % de píxeles de tinta que coinciden con su reflejo.
const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage();
const dir=process.argv[2];const out={};
for(const k of ['a','b','c']){const svg=fs.readFileSync(`${dir}/svg/oaxaca-${k}-negro.svg`,'utf8');
 const r=await p.evaluate(async(svg)=>{const img=new Image();img.src='data:image/svg+xml;base64,'+btoa(unescape(encodeURIComponent(svg)));await img.decode();
  const N=600,c=document.createElement('canvas');c.width=c.height=N;const x=c.getContext('2d');x.drawImage(img,0,0,N,N);const d=x.getImageData(0,0,N,N).data;
  const vb=svg.match(/viewBox="([^"]+)"/)[1].split(' ').map(Number);const axis=(120-vb[0])/vb[2]*N;  // eje x=120 en píxeles
  const ink=(i,j)=>d[(j*N+i)*4+3]>128;let tot=0,ok=0,tot2=0,ok2=0;const headY=(40-vb[1])/vb[3]*N;
  for(let j=0;j<N;j++)for(let i=0;i<N;i++){if(!ink(i,j))continue;const m=Math.round(2*axis-i-1);const s=m>=0&&m<N&&ink(m,j);tot++;if(s)ok++;if(j>headY){tot2++;if(s)ok2++;}}
  return {sim:+(100*ok/tot).toFixed(1),sim2:+(100*ok2/tot2).toFixed(1)}},svg);
 out[k]=k==='a'?{sim:r.sim,simSinCabeza:r.sim2}:{sim:r.sim};}
console.log(JSON.stringify(out));fs.writeFileSync(`${dir}/qa.json`,JSON.stringify(out));await b.close()})();
