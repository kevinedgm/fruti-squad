#!/usr/bin/env node
import { existsSync, mkdirSync, writeFileSync, cpSync, readdirSync } from 'node:fs';
import { resolve, join, extname } from 'node:path';

const argv=process.argv.slice(2);
let prompt='', file=null, dest=process.cwd();
for(let i=0;i<argv.length;i++){
  const a=argv[i];
  if(a==='--prompt') prompt=argv[++i]||'';
  else if(a==='--file') file=argv[++i]||null;
  else if(a==='--dest') dest=argv[++i]||dest;
  else if(!a.startsWith('--')) prompt+=(prompt?' ':'')+a;
}
dest=resolve(dest);
const source=file?resolve(dest,file):null;
if(!prompt && !source){
  console.error('Uso: fruti test --prompt "Diseña un card..." [--file ./actual.html]');
  process.exit(2);
}
if(source && !existsSync(source)){
  console.error('No encuentro --file: '+source);
  process.exit(2);
}
const testsRoot=join(dest,'.fruti','tests');
mkdirSync(testsRoot,{recursive:true});
const rounds=readdirSync(testsRoot,{withFileTypes:true})
  .filter(d=>d.isDirectory() && /^r\\d{2}$/.test(d.name))
  .map(d=>Number(d.name.slice(1)));
const next=(rounds.length?Math.max(...rounds):0)+1;
const round='r'+String(next).padStart(2,'0');
const dir=join(testsRoot,round);
mkdirSync(dir,{recursive:true});
const current=join(testsRoot,'current');
mkdirSync(current,{recursive:true});
const request=[
'# Fruti Squad Design Test · '+round,'',
'status: ready','mode: full-squad-test','round: '+round,'',
'## User request',prompt||'(redesign the supplied source artifact)','',
'## Source artifact',source||'none','',
'## Required pipeline',
'1. Kiwi: load runtime and the required brief/wireframe/validation references. Produce a neutral grayscale F2, geometry contract, adaptive matrix, states and compact decision records. No visual styling.',
'2. Lima: classify reuse/extend/new/local and validate the frozen structure against approved contracts, project profile and configured interface standards. Report missing normative sources; never invent them.',
'3. Coco: build F3 from approved structure + real tokens/design direction, implement in the configured target, then audit and emit compliance evidence.',
'4. Lima: consume Coco compliance evidence for lifecycle/gate; do not rerun the audit.',
'5. Mora: generate/update the canonical Design Hub page from verified evidence. Preview MUST render the real implemented component or a verified preview artifact.','',
'## Required deliverables',
'- .fruti/tests/'+round+'/kiwi-f2.html',
'- .fruti/tests/'+round+'/kiwi-decisions.yaml',
'- .fruti/tests/'+round+'/lima-contract.yaml',
'- Coco implementation/component',
'- .fruti/reports/compliance-current.json',
'- Mora Design Hub documentation page with verified Preview',
'- result dimensions: technical, structural, visual, accessibility, design_system, documentation',
'- .fruti/tests/'+round+'/result.md with PASS/PARTIAL/FAIL per stage','',
'## Invariants',
'- Existing HTML/code is current-state evidence, not target visual authority.',
'- F2 is grayscale/neutral; no branding, final color, shadow or decorative motion.',
'- compact/medium/expanded must declare what is preserved, changed and hidden.',
'- Main touch controls >= 44 CSS px.',
'- Important geometry records size, spacing, hierarchy and source: rule | product-context | inference.',
'- Do not introduce a card merely as a generic visual container; grouping requires a functional reason.',
'- Missing standards/references are blockers or explicit gaps, never silently reconstructed.',
'- Mora Preview corresponds to Coco verified output.',
'- Overall PASS is forbidden unless every mandatory quality dimension passes.',
'- No-overflow is not evidence of collision-free or well-composed layout.',
'- If design_system is NEW and minimum foundations are missing, F3 visual PASS is BLOCKED until foundations are approved.',''
].join('\n');
writeFileSync(join(dir,'request.md'),request);
writeFileSync(join(current,'request.md'),request);
if(source){
  const ext=extname(source)||'.txt';
  cpSync(source,join(dir,'input'+ext));
  cpSync(source,join(current,'input'+ext));
}
console.log('🍓 Fruti Squad test preparado');
console.log('round: '+round);
console.log('request: '+join(dir,'request.md'));
console.log('');
console.log('Ahora pide a tu agente:');
console.log('"Ejecuta '+join('.fruti','tests',round,'request.md')+' completo de Kiwi a Mora. No uses artefactos de rondas anteriores como salida de esta ronda. Muéstrame result.md y solo la página del Design Hub generada válidamente en esta ronda."');
