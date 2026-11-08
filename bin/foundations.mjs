#!/usr/bin/env node
import { existsSync, readFileSync, writeFileSync, mkdirSync, readdirSync } from 'node:fs';
import { resolve, join } from 'node:path';
import { createInterface } from 'node:readline';

const argv=process.argv.slice(2);
let dest=process.cwd();
// Short inputs: a handful of decisions; everything else is derived or defaulted and recorded as such.
const SHORT={marca:'brand',brand:'brand',acento:'accent',accent:'accent',fuente:'font',font:'font',
  'fuente-display':'fontDisplay','font-display':'fontDisplay',radio:'radius',radius:'radius',
  densidad:'density',density:'density',sentir:'feeling',evitar:'avoid'};
const short={}; let preguntar=false, rapido=false;
for(let i=0;i<argv.length;i++){
  const a=argv[i];
  if(a==='--dest'){ dest=argv[++i]||dest; continue; }
  if(a==='--preguntar'){ preguntar=true; continue; }
  if(a==='--rapido'||a==='--quick'){ rapido=true; continue; }
  const m=/^--([a-z-]+)(?:=(.*))?$/.exec(a);
  if(m&&SHORT[m[1]]){ const v=m[2]!==undefined?m[2]:argv[++i]; if(v===undefined||v.startsWith('--')){ console.error('Falta el valor de --'+m[1]+'.'); process.exit(2); } short[SHORT[m[1]]]=v; continue; }
  console.error('Opción desconocida: '+a+'\nEntradas cortas: --marca #HEX --acento #HEX --fuente NOMBRE --fuente-display NOMBRE --radio PX --densidad compacta|equilibrada|amplia --sentir "..." --evitar "..."');
  process.exit(2);
}
dest=resolve(dest);
const isHex=v=>/^#[0-9a-fA-F]{6}$/.test(v);
const DENSITY_HEIGHT={compacta:44,equilibrada:48,amplia:56};
const bad=[];
if(short.brand!==undefined&&!isHex(short.brand)) bad.push('--marca debe ser un hex de 6 dígitos, por ejemplo #5B4BFF.');
if(short.accent!==undefined&&!isHex(short.accent)) bad.push('--acento debe ser un hex de 6 dígitos.');
if(short.radius!==undefined&&!(Number.isInteger(Number(short.radius))&&Number(short.radius)>=0&&Number(short.radius)<=24)) bad.push('--radio debe ser un entero entre 0 y 24.');
if(short.density!==undefined&&!DENSITY_HEIGHT[short.density]) bad.push('--densidad debe ser compacta, equilibrada o amplia.');
if(bad.length){ console.error(bad.join('\n')); process.exit(2); }
// Without --preguntar, any short input (or --rapido) skips the questions.
const quick=!preguntar&&(rapido||Object.keys(short).length>0);

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
if(!quick&&!process.stdin.isTTY){ console.error('fruti foundations necesita una terminal interactiva, o entradas cortas, por ejemplo:\n  fruti foundations --marca #5B4BFF --fuente Inter --radio 8'); process.exit(2); }

// Where each value came from: input (you said it), derived (computed from an input), default.
const origin={};
const pick=(key,input,derivedValue,def)=>{
  if(input!==undefined){ origin[key]='input'; return input; }
  if(derivedValue!==undefined){ origin[key]='derived'; return derivedValue; }
  origin[key]='default'; return def;
};
const radiusIn=short.radius!==undefined?Number(short.radius):undefined;
const pre={
  feeling:pick('identity.feeling',short.feeling,undefined,'contemporáneo, altamente pulido, expresivo, distintivo, claro y fácil de operar'),
  avoid:pick('identity.avoid',short.avoid,undefined,'estética SaaS genérica, clichés del sector, ruido visual, apariencia improvisada'),
  primary:pick('color.primary',short.brand&&short.brand.toUpperCase(),undefined,'#6654F6'),
  secondary:pick('color.secondary',short.accent&&short.accent.toUpperCase(),undefined,'#FF7866'),
  body:pick('typography.primary',short.font,undefined,'Inter'),
  // Display falls back to NONE (one family) unless you name one.
  display:pick('typography.secondary',short.fontDisplay,undefined,'NONE'),
  controlRadius:pick('geometry.control_radius_px',radiusIn,undefined,10),
  // Panels keep the default 10→16 relation: panel radius = control radius + 6, capped at 32.
  surfaceRadius:pick('geometry.surface_radius_px',undefined,radiusIn!==undefined?Math.min(32,radiusIn+6):undefined,16),
  density:pick('geometry.density',short.density,undefined,'equilibrada'),
  controlHeight:pick('geometry.control_height_px',undefined,short.density?DENSITY_HEIGHT[short.density]:undefined,48)
};

const say=t=>{ if(!quick) console.log(t); };
const rl=quick?null:createInterface({input:process.stdin,output:process.stdout});
const q=(text,def='')=>quick?Promise.resolve(def):new Promise(res=>rl.question('? '+text+(def?' ['+def+']':'')+'\n> ',a=>res((a||'').trim()||def)));
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

if(!quick) console.log('\n🍓 Fruti Squad · Foundations Lab\n');
if(!quick) console.log('Construiremos una PROPUESTA. Nada se vuelve canónico hasta tu aprobación explícita.\n');

say('1/8 · Identidad');
const feeling=await q('¿Cómo debe sentirse el producto?',pre.feeling);
const avoid=await q('¿Qué debe evitar visualmente?',pre.avoid);
const refs=await q('Referencias de calidad/dirección (separadas por coma):','Notion, Apple, Stripe');
const audience=await q('Contexto principal de uso:','80% móvil; trabajadores jóvenes de campo; sesiones operativas cortas');

say('\n2/8 · Color');
const primary=await hex('Color primario de identidad',pre.primary);
const secondary=await hex('Color secundario de identidad',pre.secondary);
const surface=await hex('Superficie base','#F8F8FA');
const ink=await hex('Tinta principal','#17171B');
const danger=await hex('Danger/error','#C84655');
const success=await hex('Success','#187A5B');
const warning=await hex('Warning','#9A6715');

say('\n3/8 · Tipografía');
const body=await q('Familia primaria para interfaz/datos:',pre.body);
const display=await q('Familia secundaria para display/editorial (NONE si no quieres):',pre.display);
const typeCharacter=await q('Carácter tipográfico deseado:','alta legibilidad, jerarquía fuerte, números claros, display con personalidad sin afectar operación');

say('\n4/8 · Geometría');
const spacing=await integer('Paso base de spacing en px',4,2,8);
const controlRadius=await integer('Radio base de controles en px',pre.controlRadius,0,24);
const surfaceRadius=await integer('Radio de superficies/paneles en px',pre.surfaceRadius,0,32);
const density=await q('Densidad operativa: compacta | equilibrada | amplia',pre.density);
const controlHeight=await integer('Altura operativa recomendada en px',pre.controlHeight,44,64);

say('\n5/8 · Iconografía');
const icons=await q('Librería de iconos:','lucide');
const iconRule=await q('Regla de iconografía:','trazo coherente; icono + texto en acciones ambiguas; estado nunca solo por icono o color');

say('\n6/8 · Motion');
const motion=await q('Carácter del movimiento:','rápido, físico y contenido; continuidad y feedback, nunca decoración');
const fast=await integer('Duración fast ms',140,80,220);
const standard=await integer('Duración standard ms',220,140,360);
const emphasis=await integer('Duración emphasis ms',320,220,500);
const easing=await q('Easing estándar:','cubic-bezier(.2,.8,.2,1)');

say('\n7/8 · Adaptividad');
const compact=await q('Compact (<600):','una columna; bottom navigation; acción primaria en zona alcanzable; progressive disclosure');
const medium=await q('Medium (600–1023):','navigation rail; 8 columnas; detalle contextual cuando aporte');
const expanded=await q('Expanded (>=1024):','sidebar persistente; 12 columnas; master-detail cuando mejore comparación');
const touch=await integer('Target táctil mínimo px',44,44,64);

say('\n8/8 · Accesibilidad');
const a11y=await q('Objetivo:','WCAG 2.2 AA');
const accessibility=await q('Reglas adicionales:','foco visible; significado nunca solo por color; zoom 200%; reduced motion; forced-colors; teclado');

if(rl) rl.close();

const displayValue=/^none$/i.test(display)?'none':display;

// Deterministic contrast checks (WCAG 2.x relative luminance). They warn; Lima decides on approval.
const lum=h=>{ const c=[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)/255).map(v=>v<=0.03928?v/12.92:((v+0.055)/1.055)**2.4); return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]; };
const ratio=(a,b)=>{ const [x,y]=[lum(a),lum(b)].sort((m,n)=>n-m); return Math.round(((x+0.05)/(y+0.05))*100)/100; };
const checks=[
  {id:'primary-vs-surface',what:'primario como borde/control sobre la superficie',ratio:ratio(primary,surface),min:3},
  {id:'text-on-primary',what:'texto blanco sobre el primario (botón principal)',ratio:ratio('#FFFFFF',primary),min:4.5},
  {id:'ink-vs-surface',what:'tinta sobre la superficie',ratio:ratio(ink,surface),min:4.5}
].map(c=>({...c,status:c.ratio>=c.min?'ok':'warn'}));
// Interactive answers are all yours; origin is only meaningful for short inputs.
if(!quick) for(const k in origin) delete origin[k];
if(quick) for(const k of ['color.surface','color.ink','color.danger','color.success','color.warning','typography.character','geometry.spacing_base_px','geometry.touch_min_px','iconography','motion','adaptive','accessibility']) origin[k]??='default';

const proposal={
  version:2,status:'proposed',approval:'pending',
  identity:{feeling,avoid,references:refs,audience},
  color:{surface,ink,primary,secondary,danger,success,warning},
  typography:{primary:body,secondary:displayValue,character:typeCharacter},
  geometry:{spacing_base_px:spacing,control_radius_px:controlRadius,surface_radius_px:surfaceRadius,density,control_height_px:controlHeight,touch_min_px:touch},
  iconography:{library:icons,rule:iconRule},
  motion:{character:motion,fast_ms:fast,standard_ms:standard,emphasis_ms:emphasis,easing,reduced_motion:'required'},
  adaptive:{compact,medium,expanded},
  accessibility:{target:a11y,rule:accessibility},
  mode:quick?'short-inputs':'interactive', short_inputs:short, origin, checks
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
'  surface: '+JSON.stringify(surface),'  ink: '+JSON.stringify(ink),'  primary: '+JSON.stringify(primary),'  secondary: '+JSON.stringify(secondary),
'  danger: '+JSON.stringify(danger),'  success: '+JSON.stringify(success),'  warning: '+JSON.stringify(warning),
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
'short_inputs:'+(Object.keys(short).length?'':' {}'),
...Object.entries(short).map(([k,v])=>'  '+k+': '+JSON.stringify(v)),'',
'# input = lo dijiste tú · derived = calculado de una entrada · default = valor por omisión, revísalo',
'mode: '+(quick?'short-inputs':'interactive'),
'origin:'+(Object.keys(origin).length?'':' {}'),
...Object.entries(origin).map(([k,v])=>'  '+JSON.stringify(k)+': '+v),'',
'checks:',
...checks.flatMap(c=>['  - id: '+c.id,'    what: '+JSON.stringify(c.what),'    ratio: '+c.ratio,'    min: '+c.min,'    status: '+c.status]),'',
'derived_tokens:',
'  status: not-materialized',
'  note: "Lima derives scales/semantic tokens only after explicit approval; this proposal is not truth."',''
].join('\n');

const dir=join(dest,'.fruti','foundations'); mkdirSync(dir,{recursive:true});
const file=join(dir,'proposal.yaml'); writeFileSync(file,yaml);
writeFileSync(join(dir,'proposal.json'),JSON.stringify(proposal,null,2)+'\n');
console.log('\n✓ Propuesta creada: '+file);
console.log('✓ JSON espejo: '+join(dir,'proposal.json'));
const warns=checks.filter(c=>c.status==='warn');
for(const c of warns) console.log('⚠ Contraste bajo: '+c.what+' = '+c.ratio+':1 (mínimo '+c.min+':1).');
if(quick){
  const defs=Object.entries(origin).filter(([,v])=>v==='default').map(([k])=>k);
  console.log('Tomé de tus entradas: '+(Object.keys(short).join(', ')||'nada')+'. Quedaron por omisión: '+defs.length+' decisiones (ver origin en la propuesta).');
}
console.log('\nNO está aprobada. Revísala primero.');
console.log('Para verla: cat .fruti/foundations/proposal.yaml');
console.log('Si la apruebas, díselo a tu agente (Claude Code, Codex…):');
console.log('"Usa Lima foundations_new para aprobar .fruti/foundations/proposal.yaml, materializar tokens y páginas Foundations, actualizar el perfil PULZ y detenerte antes de diseñar componentes."');
