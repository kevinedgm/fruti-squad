#!/usr/bin/env node
import { existsSync, readFileSync, writeFileSync, mkdirSync, readdirSync } from 'node:fs';
import { resolve, join } from 'node:path';
import { createInterface } from 'node:readline';

const argv=process.argv.slice(2);
let dest=process.cwd();
for(let i=0;i<argv.length;i++) if(argv[i]==='--dest') dest=argv[++i]||dest;
dest=resolve(dest);

const profilesDirs=['.codex','.claude','.agents'].map(d=>join(dest,d,'skills','lima','profiles'));
const profiles=profilesDirs.filter(existsSync).flatMap(d=>readdirSync(d).filter(f=>f.endsWith('.md')&&f!=='_TEMPLATE.md').map(f=>join(d,f)));
if(!profiles.length){ console.error('No encuentro un perfil de proyecto de lima. Ejecuta setup primero.'); process.exit(2); }
// Prefer the profile that is still NEW; otherwise any profile (reported as already defined below).
const profile=profiles.find(f=>/design_system:\s*NEW\b/.test(readFileSync(f,'utf8')))||profiles[0];
const raw=readFileSync(profile,'utf8');
if(!/design_system:\s*NEW\b/.test(raw)){
  console.log('El perfil ya tiene un design system definido; NEW foundations no aplica.');
  process.exit(0);
}
if(!process.stdin.isTTY){ console.error('fruti foundations necesita una terminal interactiva.'); process.exit(2); }

const rl=createInterface({input:process.stdin,output:process.stdout});
const q=(text,def='')=>new Promise(res=>rl.question('? '+text+(def?' ['+def+']':'')+'\n> ',a=>res((a||'').trim()||def)));
const hex=async(text,def)=>{
  while(true){
    const v=await q(text,def);
    if(/^#[0-9a-fA-F]{6}$/.test(v)) return v.toUpperCase();
    console.log('  Usa un hex de 6 dígitos, por ejemplo #5B4BFF.');
  }
};
const integer=async(text,def,min,max)=>{
  while(true){
    const v=Number(await q(text,String(def)));
    if(Number.isInteger(v)&&v>=min&&v<=max) return v;
    console.log('  Ingresa un entero entre '+min+' y '+max+'.');
  }
};

console.log('\n🍓 Fruti Squad · Foundations Lab\n');
console.log('Construiremos una PROPUESTA. Nada se vuelve canónico hasta tu aprobación explícita.\n');

console.log('1/8 · Identidad');
const feeling=await q('¿Cómo debe sentirse el producto?','contemporáneo, altamente pulido, expresivo, distintivo, claro y fácil de operar');
const avoid=await q('¿Qué debe evitar visualmente?','estética SaaS genérica, clichés del sector, ruido visual, apariencia improvisada');
const refs=await q('Referencias de calidad/dirección (separadas por coma):','Notion, Apple, Stripe');
const audience=await q('Contexto principal de uso:','80% móvil; trabajadores jóvenes de campo; sesiones operativas cortas');

console.log('\n2/8 · Color');
const primary=await hex('Color primario de identidad','#6654F6');
const secondary=await hex('Color secundario de identidad','#FF7866');
const surface=await hex('Superficie base','#F8F8FA');
const ink=await hex('Tinta principal','#17171B');
const danger=await hex('Danger/error','#C84655');
const success=await hex('Success','#187A5B');
const warning=await hex('Warning','#9A6715');

console.log('\n3/8 · Tipografía');
const body=await q('Familia primaria para interfaz/datos:','Inter');
const display=await q('Familia secundaria para display/editorial (NONE si no quieres):','NONE');
const typeCharacter=await q('Carácter tipográfico deseado:','alta legibilidad, jerarquía fuerte, números claros, display con personalidad sin afectar operación');

console.log('\n4/8 · Geometría');
const spacing=await integer('Paso base de spacing en px',4,2,8);
const controlRadius=await integer('Radio base de controles en px',10,0,24);
const surfaceRadius=await integer('Radio de superficies/paneles en px',16,0,32);
const density=await q('Densidad operativa: compacta | equilibrada | amplia','equilibrada');
const controlHeight=await integer('Altura operativa recomendada en px',48,44,64);

console.log('\n5/8 · Iconografía');
const icons=await q('Librería de iconos:','lucide');
const iconRule=await q('Regla de iconografía:','trazo coherente; icono + texto en acciones ambiguas; estado nunca solo por icono o color');

console.log('\n6/8 · Motion');
const motion=await q('Carácter del movimiento:','rápido, físico y contenido; continuidad y feedback, nunca decoración');
const fast=await integer('Duración fast ms',140,80,220);
const standard=await integer('Duración standard ms',220,140,360);
const emphasis=await integer('Duración emphasis ms',320,220,500);
const easing=await q('Easing estándar:','cubic-bezier(.2,.8,.2,1)');

console.log('\n7/8 · Adaptividad');
const compact=await q('Compact (<600):','una columna; bottom navigation; acción primaria en zona alcanzable; progressive disclosure');
const medium=await q('Medium (600–1023):','navigation rail; 8 columnas; detalle contextual cuando aporte');
const expanded=await q('Expanded (>=1024):','sidebar persistente; 12 columnas; master-detail cuando mejore comparación');
const touch=await integer('Target táctil mínimo px',44,44,64);

console.log('\n8/8 · Accesibilidad');
const a11y=await q('Objetivo:','WCAG 2.2 AA');
const accessibility=await q('Reglas adicionales:','foco visible; significado nunca solo por color; zoom 200%; reduced motion; forced-colors; teclado');

rl.close();

const displayValue=/^none$/i.test(display)?'none':display;
const proposal={
  version:2,status:'proposed',approval:'pending',
  identity:{feeling,avoid,references:refs,audience},
  color:{surface,ink,primary,secondary,danger,success,warning},
  typography:{primary:body,secondary:displayValue,character:typeCharacter},
  geometry:{spacing_base_px:spacing,control_radius_px:controlRadius,surface_radius_px:surfaceRadius,density,control_height_px:controlHeight,touch_min_px:touch},
  iconography:{library:icons,rule:iconRule},
  motion:{character:motion,fast_ms:fast,standard_ms:standard,emphasis_ms:emphasis,easing,reduced_motion:'required'},
  adaptive:{compact,medium,expanded},
  accessibility:{target:a11y,rule:accessibility}
};
const yaml=[
'# PULZ foundations proposal v2','',
'status: proposed','approval: pending','',
'identity:',
'  feeling: '+JSON.stringify(feeling),
'  avoid: '+JSON.stringify(avoid),
'  references: '+JSON.stringify(refs),
'  audience: '+JSON.stringify(audience),'',
'color:',
'  surface: '+surface,'  ink: '+ink,'  primary: '+primary,'  secondary: '+secondary,
'  danger: '+danger,'  success: '+success,'  warning: '+warning,
'  law: "primary = acción primaria/selección activa; secondary = expresión/acento; semantic roles son independientes; contenido ordinario = ink sobre surface"','',
'typography:',
'  primary: '+JSON.stringify(body),'  secondary: '+JSON.stringify(displayValue),
'  character: '+JSON.stringify(typeCharacter),
'  law: "primary gobierna UI y datos; secondary solo display/editorial; números comparables usan tabular figures"','',
'geometry:',
'  spacing_base_px: '+spacing,'  control_radius_px: '+controlRadius,'  surface_radius_px: '+surfaceRadius,
'  density: '+JSON.stringify(density),'  control_height_px: '+controlHeight,'  touch_min_px: '+touch,'',
'iconography:',
'  library: '+JSON.stringify(icons),'  rule: '+JSON.stringify(iconRule),'',
'motion:',
'  character: '+JSON.stringify(motion),'  fast_ms: '+fast,'  standard_ms: '+standard,'  emphasis_ms: '+emphasis,
'  easing: '+JSON.stringify(easing),'  reduced_motion: required','',
'adaptive:',
'  compact: '+JSON.stringify(compact),'  medium: '+JSON.stringify(medium),'  expanded: '+JSON.stringify(expanded),'',
'accessibility:',
'  target: '+JSON.stringify(a11y),'  rule: '+JSON.stringify(accessibility),'',
'derived_tokens:',
'  status: not-materialized',
'  note: "Lima derives scales/semantic tokens only after explicit approval; this proposal is not truth."',''
].join('\n');

const dir=join(dest,'.fruti','foundations'); mkdirSync(dir,{recursive:true});
const file=join(dir,'proposal.yaml'); writeFileSync(file,yaml);
writeFileSync(join(dir,'proposal.json'),JSON.stringify(proposal,null,2)+'\n');
console.log('\n✓ Propuesta creada: '+file);
console.log('✓ JSON espejo: '+join(dir,'proposal.json'));
console.log('\nNO está aprobada. Revísala primero.');
console.log('Para verla: cat .fruti/foundations/proposal.yaml');
console.log('Si la apruebas, díselo a tu agente (Claude Code, Codex…):');
console.log('"Usa Lima foundations_new para aprobar .fruti/foundations/proposal.yaml, materializar tokens y páginas Foundations, actualizar el perfil PULZ y detenerte antes de diseñar componentes."');
