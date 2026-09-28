#!/usr/bin/env node
import { existsSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { resolve, join } from 'node:path';
import { createInterface } from 'node:readline';

const argv=process.argv.slice(2);
let dest=process.cwd(), yes=false;
for(let i=0;i<argv.length;i++){ if(argv[i]==='--dest') dest=argv[++i]||dest; else if(argv[i]==='--yes') yes=true; }
dest=resolve(dest);

const candidates=[
  join(dest,'.codex','skills','lima','profiles','pulz.md'),
  join(dest,'.claude','skills','lima','profiles','pulz.md'),
  join(dest,'.agents','skills','lima','profiles','pulz.md')
];
const profile=candidates.find(existsSync);
if(!profile){ console.error('No encuentro un perfil activo pulz.md. Ejecuta setup primero.'); process.exit(2); }
const raw=readFileSync(profile,'utf8');
const isNew=/design_system:\s*NEW\b/.test(raw);
if(!isNew){ console.log('El perfil ya tiene design_system definido. Foundations no necesita bootstrap NEW.'); process.exit(0); }

const ask=async()=>{
 const rl=createInterface({input:process.stdin,output:process.stdout});
 const q=(t,d='')=>new Promise(r=>rl.question('? '+t+(d?' ['+d+']':'')+' ',a=>r((a||'').trim()||d)));
 console.log('\n🍓 Fruti Squad · foundations NEW\n');
 console.log('Esto establece la ley mínima que Coco podrá consumir. No genera componentes todavía.\n');
 const intent=await q('Describe en una frase cómo debe sentirse el producto:','claro, contemporáneo, pulido y fácil de operar');
 const primary=await q('Color primario (hex):','#5B4BFF');
 const secondary=await q('Color secundario (hex):','#FF7664');
 const surface=await q('Superficie base (hex):','#F8F8FA');
 const ink=await q('Tinta/texto principal (hex):','#17171B');
 const danger=await q('Peligro/error (hex):','#C84655');
 const body=await q('Tipografía primaria/interfaz:','Inter');
 const display=await q('Tipografía secundaria/display:','');
 const radius=await q('Radio base de controles (px):','10');
 const spacing=await q('Paso base de spacing (px):','4');
 const motion=await q('Motion base:','fast 140ms; standard 220ms; emphasis 320ms; ease cubic-bezier(.2,.8,.2,1)');
 rl.close();
 return {intent,primary,secondary,surface,ink,danger,body,display,radius,spacing,motion};
};
if(!process.stdin.isTTY && !yes){ console.error('Foundations necesita terminal interactiva.'); process.exit(2); }
const v=await ask();
const proposal=[
'# PULZ foundations proposal','',
'status: proposed',
'design_intent: '+v.intent,'',
'color:',
'  surface: '+v.surface,
'  ink: '+v.ink,
'  primary: '+v.primary,
'  secondary: '+v.secondary,
'  danger: '+v.danger,
'  rule: primary owns primary action/active selection; secondary is expressive support; semantic states keep independent roles.','',
'typography:',
'  primary: '+v.body,
'  secondary: '+(v.display||'none'),
'  rule: primary owns UI/data; secondary, when present, is display/editorial only.','',
'geometry:',
'  spacing_base_px: '+v.spacing,
'  control_radius_px: '+v.radius,
'  touch_min_px: 44','',
'iconography:',
'  library: lucide',
'  rule: one stroke set; icons support labels and never carry state alone.','',
'motion:',
'  law: '+v.motion,
'  reduced_motion: required','',
'approval: pending',''
].join('\n');
const dir=join(dest,'.fruti','foundations'); mkdirSync(dir,{recursive:true});
const file=join(dir,'proposal.yaml'); writeFileSync(file,proposal);
console.log('\nPropuesta escrita en '+file);
console.log('Revísala. Si la apruebas, dile a Codex:');
console.log('"Usa Lima para aprobar .fruti/foundations/proposal.yaml, materializar tokens/foundations en el Design Hub y actualizar el perfil PULZ como fuente normativa. No diseñes componentes todavía."');
