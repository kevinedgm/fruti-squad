#!/usr/bin/env node
/**
 * Semilla local CLI — deterministic project map for Fruti Squad.
 * Zero dependencies. Node >=16.
 *
 * Este CLI produce SOLO la capa determinista del mapa: el grafo de imports
 * y la reachability desde raíces (`graph.json` + `graph-orphans.json`).
 * Las capas semánticas (modules/ui/data/api/flows) las escribe el agente.
 * Ambas conviven en el mismo `index.json`: este CLI mezcla su sección, nunca
 * reemplaza el archivo completo.
 */
import { existsSync, mkdirSync, readFileSync, writeFileSync, readdirSync, statSync, rmSync } from 'node:fs';
import { resolve, join, relative, extname, dirname } from 'node:path';
import { spawnSync } from 'node:child_process';
import { performance } from 'node:perf_hooks';
import { fileURLToPath } from 'node:url';

const cwd=process.cwd(), root=resolve(cwd), fruti=join(root,'.fruti');
const cfgPath=join(fruti,'semilla.json'), benchPath=join(fruti,'benchmarks.json'), activePath=join(fruti,'.benchmark-active.json');
const SCHEMA='fruti-semilla/v1';
// Como citar el comando: `fruti semilla` solo existe si se instalo el paquete;
// si no, se cita la ruta real con la que nos acaban de ejecutar.
const SELF=process.env.SEMILLA_INVOCATION||(()=>{const abs=process.argv[1]||'',r=relative(process.cwd(),abs);return `node ${r&&r.length<abs.length?r:abs}`})();
const countersPath=join(fruti,'.counters.json'), testActivePath=join(fruti,'.test-active.json'), testsPath=join(fruti,'tests.json');
const settingsPath=join(root,'.claude','settings.local.json');
const hookScript=fileURLToPath(new URL('semilla-hook.mjs',import.meta.url));
const IGNORE=new Set(['node_modules','.git','.fruti','dist','build','coverage','.next','.nuxt','.output','vendor']);
const CODE=new Set(['.js','.mjs','.cjs','.ts','.tsx','.jsx','.vue','.svelte','.java','.py','.php','.dart']);
const args=process.argv.slice(2), cmd=args[0]||'help';
const flag=(n,d=null)=>{const i=args.indexOf(n); return i>=0 ? (args[i+1]&&!args[i+1].startsWith('--')?args[i+1]:true):d};
const str=(n,d)=>{const v=flag(n,d);if(v===true)throw new Error(`Falta el valor de ${n}`);return v};
const num=n=>{const v=flag(n,0);if(v===true)throw new Error(`Falta el valor de ${n}`);const x=Number(v);if(!Number.isFinite(x))throw new Error(`${n} debe ser un número, recibí "${v}"`);return x};
const readJson=(p,d)=>{try{return JSON.parse(readFileSync(p,'utf8'))}catch{return d}};
const writeJson=(p,v)=>{mkdirSync(dirname(p),{recursive:true});writeFileSync(p,JSON.stringify(v,null,2)+'\n')};
const slash=p=>p.split('\\').join('/');
function config(){return readJson(cfgPath,{enabled:true,knowledge_path:'.fruti/knowledge'})}
const knowledge=resolve(root,config().knowledge_path||'.fruti/knowledge');
const indexPath=join(knowledge,'index.json'), graphPath=join(knowledge,'graph.json'), graphOrphansPath=join(knowledge,'graph-orphans.json');
const ensure=()=>{mkdirSync(knowledge,{recursive:true});};
const rel=p=>slash(relative(root,p))||'.';
function gitSha(){const r=spawnSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8'});return r.status===0?r.stdout.trim():null}
function walk(dir,out=[]){for(const e of readdirSync(dir)){if(IGNORE.has(e))continue;const p=join(dir,e);let s;try{s=statSync(p)}catch{continue}if(s.isDirectory())walk(p,out);else if(CODE.has(extname(e)))out.push(p)}return out}
function imports(text,file){
 const found=[]; const patterns=[/\b(?:import|export)\s+(?:[^'"]*?\s+from\s+)?['"]([^'"]+)['"]/g,/\brequire\(\s*['"]([^'"]+)['"]\s*\)/g,/\bimport\(\s*['"]([^'"]+)['"]\s*\)/g];
 for(const re of patterns){let m;while((m=re.exec(text)))found.push(m[1])}
 return [...new Set(found)].filter(x=>x.startsWith('.')).map(x=>resolveImport(file,x)).filter(Boolean)
}
function resolveImport(file,spec){
 const base=resolve(dirname(file),spec); const tries=[base,...[...CODE].map(e=>base+e)];
 for(const e of CODE)tries.push(join(base,'index'+e));
 for(const p of tries)if(existsSync(p)&&statSync(p).isFile())return slash(relative(root,p));
 return null
}
const EXT='js|mjs|cjs|ts|tsx|jsx|vue|java|py|php|dart';
function htmlRoots(files){
 // Entradas declaradas en HTML (<script src="/src/main.js">). Vite y compania
 // arrancan desde ahi, no desde un import, asi que sin esto salen huerfanos falsos.
 const out=new Set();
 let pages=[];try{pages=readdirSync(root).filter(f=>/\.html?$/i.test(f))}catch{}
 for(const page of pages){
  let text='';try{text=readFileSync(join(root,page),'utf8')}catch{continue}
  for(const m of text.matchAll(/\b(?:src|href)\s*=\s*["']([^"']+)["']/g)){
   const spec=m[1];
   if(/^(?:[a-z]+:)?\/\//i.test(spec)||spec.startsWith('data:'))continue;
   const p=slash(relative(root,resolve(root,spec.replace(/^\//,''))));
   if(files.includes(p))out.add(p)
  }
 }
 return [...out]
}
function roots(files){
 const rs=new Set();
 for(const f of files){
  const b=f.split('/').pop(), depth=f.split('/').length;
  if(new RegExp(`^(main|app|server|bootstrap)\\.(${EXT})$`,'i').test(b))rs.add(f);
  // `index` solo cuenta como raiz en la cima del arbol: un src/utils/index.js es
  // un barrel, no un entry point, y tratarlo como raiz oculta huerfanos reales.
  if(new RegExp(`^index\\.(${EXT})$`,'i').test(b)&&depth<=2)rs.add(f);
  // Los service workers son entry points aunque nadie los importe.
  if(new RegExp(`^(sw|service-worker)\\.(${EXT})$`,'i').test(b))rs.add(f);
  if(/router|routes/i.test(f))rs.add(f)
 }
 for(const h of htmlRoots(files))rs.add(h);
 try{const pkg=JSON.parse(readFileSync(join(root,'package.json'),'utf8'));for(const k of ['main','module','browser'])if(pkg[k])rs.add(slash(pkg[k]))}catch{}
 return [...rs].filter(x=>files.includes(x))
}
function classify(path){if(/test|spec|__tests__/i.test(path))return'test';if(/route|router/i.test(path))return'route';if(/component|\.vue$|\.svelte$/i.test(path))return'ui';if(/store|state/i.test(path))return'state';if(/service|api|client/i.test(path))return'service';return'code'}
function build(scope='.',isInit=true){
 const started=performance.now(), abs=resolve(root,scope);if(!existsSync(abs))throw new Error('Scope no existe: '+scope);
 const files=walk(abs).map(p=>slash(relative(root,p))), nodes={};
 for(const f of files){let text='';try{text=readFileSync(join(root,f),'utf8')}catch{}nodes[f]={path:f,kind:classify(f),outgoing:imports(text,join(root,f)),incoming:[],status:'unknown',confidence:'medium'}}
 for(const n of Object.values(nodes))for(const t of n.outgoing)if(nodes[t])nodes[t].incoming.push(n.path);
 const rs=roots(files), seen=new Set(), q=[...rs];while(q.length){const f=q.shift();if(seen.has(f)||!nodes[f])continue;seen.add(f);for(const t of nodes[f].outgoing)q.push(t)}
 for(const n of Object.values(nodes)){if(seen.has(n.path)){n.status='active';n.confidence='high'}else if(n.incoming.length===0){n.status='orphan';n.confidence='medium'}else{n.status='unreachable';n.confidence='medium'}}
 const result={schema:SCHEMA,generated_at:new Date().toISOString(),verified_commit:gitSha(),scope:rel(abs),roots:rs,nodes};
 ensure();writeJson(graphPath,result);
 const orphans=Object.values(nodes).filter(n=>n.status==='orphan'||n.status==='unreachable');writeJson(graphOrphansPath,{generated_at:result.generated_at,items:orphans});
 const counts={};for(const n of Object.values(nodes))counts[n.status]=(counts[n.status]||0)+1;
 const prev=readJson(indexPath,null)||{};
 // `files` solo se mezcla si es un objeto plano. Si el agente lo escribio como
 // array (u otra forma), spreadearlo lo convertiria en {"0":..,"1":..}: se deja
 // intacto y la seccion `graph` basta para localizar lo del CLI.
 const plain=v=>!!v&&typeof v==='object'&&!Array.isArray(v);
 const filesKey=(plain(prev.files)||prev.files===undefined)
  ?{files:{...(plain(prev.files)?prev.files:{}),graph:'graph.json',graph_orphans:'graph-orphans.json'}}
  :{};
 writeJson(indexPath,{...prev,schema:prev.schema||SCHEMA,updated_at:result.generated_at,...filesKey,
  graph:{generated_at:result.generated_at,verified_commit:result.verified_commit,scope:result.scope,
   // `init_scope` recuerda el alcance completo para que un `map` acotado no deje
   // a `sync` reconstruyendo para siempre sobre un subarbol.
   init_scope:isInit?result.scope:(prev.graph?.init_scope||prev.graph?.scope||result.scope),
   roots:rs,counts}});
 return {ms:performance.now()-started,files:files.length,counts,roots:rs.length}
}
function graph(){const g=readJson(graphPath,null);if(g)return g;throw new Error(`No hay grafo del CLI en ${rel(graphPath)}. Ejecuta: ${SELF} init [--scope src]`)}
function nodeFor(q){
 if(!q)throw new Error('Falta archivo');
 const g=graph(), exact=g.nodes[slash(q)];if(exact)return exact;
 const hits=Object.values(g.nodes).filter(n=>n.path.toLowerCase().includes(q.toLowerCase()));
 if(!hits.length)throw new Error(`Sin coincidencias para "${q}" (${Object.keys(g.nodes).length} archivos mapeados, scope ${g.scope}).`);
 return hits.length===1?hits[0]:hits
}
function pathFromRoot(g,target){
 const parent={},q=[...(g.roots||[])],seen=new Set(q);
 while(q.length){
  const f=q.shift();
  if(f===target){const out=[f];let c=f;while(parent[c]){c=parent[c];out.unshift(c)}return out}
  for(const t of g.nodes[f]?.outgoing||[])if(!seen.has(t)){seen.add(t);parent[t]=f;q.push(t)}
 }
 return null
}
function printNode(n){console.log('\n🌱 '+n.path);console.log('status:',n.status,'| confidence:',n.confidence);console.log('incoming:',n.incoming.length?n.incoming.join(', '):'—');console.log('outgoing:',n.outgoing.length?n.outgoing.join(', '):'—')}
function changed(){
 const out=[];
 for(const a of [['diff','--name-only','HEAD'],['ls-files','--others','--exclude-standard']]){
  const r=spawnSync('git',a,{cwd:root,encoding:'utf8'});
  if(r.status===0)out.push(...r.stdout.trim().split(/\r?\n/).filter(Boolean))
 }
 return [...new Set(out)].filter(f=>!f.split('/').some(seg=>IGNORE.has(seg)))
}
// ---------- hook ----------
function hookCmd(){return `node ${JSON.stringify(hookScript)}`}
function hasHook(s){return (s?.hooks?.PostToolUse||[]).some(m=>(m.hooks||[]).some(h=>String(h.command||'').includes('semilla-hook.mjs')))}
function hookInstall(){
 const s=readJson(settingsPath,null)||{};
 if(hasHook(s))return 'El hook ya estaba instalado.';
 s.hooks??={};s.hooks.PostToolUse??=[];
 s.hooks.PostToolUse.push({matcher:'*',hooks:[{type:'command',command:hookCmd()}]});
 writeJson(settingsPath,s);
 return `Hook instalado en ${rel(settingsPath)}. Reinicia la sesion del agente para que lo cargue.`
}
function hookUninstall(){
 const s=readJson(settingsPath,null);
 if(!s||!hasHook(s))return 'No habia hook de Semilla instalado.';
 s.hooks.PostToolUse=s.hooks.PostToolUse.map(m=>({...m,hooks:(m.hooks||[]).filter(h=>!String(h.command||'').includes('semilla-hook.mjs'))})).filter(m=>(m.hooks||[]).length);
 writeJson(settingsPath,s);
 return 'Hook desinstalado.'
}

// ---------- test A/B ----------
function tests(){const t=readJson(testsPath,null);return t&&Array.isArray(t.runs)?t:{runs:[],overhead:{}}}
const nfmt=n=>Number.isFinite(n)?n.toLocaleString('en-US'):'—';
function pct(a,b){if(!Number.isFinite(a)||!Number.isFinite(b)||a===0)return '—';const d=(b-a)/a*100;return (d>0?'+':'')+d.toFixed(1)+'%'}
function row(label,a,b,fmt=nfmt){console.log(label.padEnd(20)+String(fmt(a)).padStart(10)+String(fmt(b)).padStart(11)+String(pct(a,b)).padStart(11))}
function pair(runs,name){
 const of_=[...runs].reverse().find(r=>r.name===name&&r.variant==='control');
 const on=[...runs].reverse().find(r=>r.name===name&&r.variant==='semilla');
 return {of_,on}
}
function printPair(name,of_,on){
 console.log('\nTask: '+name);
 if(of_?.task||on?.task)console.log('"'+(of_?.task||on?.task)+'"');
 console.log(''.padEnd(20)+'OFF'.padStart(10)+'ON'.padStart(11)+'Δ'.padStart(11));
 console.log('─'.repeat(52));
 row('Tiempo',of_?.duration_ms/1000,on?.duration_ms/1000,n=>Number.isFinite(n)?n.toFixed(1)+' s':'—');
 row('Archivos leidos',of_?.files_read,on?.files_read);
 row('Busquedas',of_?.searches,on?.searches);
 row('Tool calls',of_?.tool_calls,on?.tool_calls);
 row('Input tokens',of_?.input_tokens,on?.input_tokens);
 console.log('Verification reads'.padEnd(20)+String(of_?.verification_reads??'—').padStart(10)+String(on?.verification_reads??'—').padStart(11));
 console.log('Respuesta correcta'.padEnd(20)+(of_?of_.correct?'✓':'✗':'—').padStart(10)+(on?on.correct?'✓':'✗':'—').padStart(11));
 if(!of_||!on)console.log('\n(falta la condicion '+(of_?'ON':'OFF')+'; corre la otra mitad para comparar)')
}
function help(){console.log(`
🌱 Semilla
  ${SELF} init [--scope src]
  ${SELF} map <path>
  ${SELF} sync
  ${SELF} on | off | status
  ${SELF} relations <file>
  ${SELF} impact <file>
  ${SELF} why <file>
  ${SELF} orphans [--scope text]
  ${SELF} graph [--scope text]
  ${SELF} benchmark start <name> --variant control|semilla [--force]
  ${SELF} benchmark end [--input-tokens N --output-tokens N --tool-calls N]
  ${SELF} benchmark report

  ${SELF} hook install | uninstall | status
  ${SELF} test start <name> --task "..." --variant control|semilla
  ${SELF} test end --correct|--wrong [--input-tokens N --output-tokens N] [--note "..."]
  ${SELF} test report [<name>]
  ${SELF} test overhead --init-tokens N [--sync-tokens N]
  ${SELF} test status
`)}

try{
 if(cmd==='init'||cmd==='map'){
  const isInit=cmd==='init', scope=isInit?(str('--scope','.')||'.'):(args[1]||'.');
  const before=readJson(indexPath,null)?.graph?.init_scope;
  const r=build(scope,isInit);
  console.log(`🌱 mapa listo · ${r.files} archivos · ${r.roots} raíces · ${r.ms.toFixed(0)} ms`);console.log(r.counts);
  if(!isInit&&before&&before!==scope)console.log(`\n⚠️  el grafo quedó acotado a "${scope}". "${SELF} init --scope ${before}" lo restaura; "sync" ya vuelve solo a "${before}".`);
 }
 else if(cmd==='sync'){const c=changed();const old=readJson(indexPath,{});const scope=old.graph?.init_scope||old.graph?.scope||old.scope||'.';const r=build(scope);console.log(`🌱 sync · ${c.length} archivos cambiados · grafo reconstruido sobre "${scope}" en ${r.ms.toFixed(0)} ms`)}
 else if(cmd==='on'||cmd==='off'){ensure();const c=config();c.enabled=cmd==='on';c.updated_at=new Date().toISOString();writeJson(cfgPath,c);console.log('🌱 Semilla',c.enabled?'ON':'OFF')}
 else if(cmd==='status'){
  const c=config(),i=readJson(indexPath,null);
  console.log('🌱 Semilla',c.enabled?'ON':'OFF');
  console.log('Knowledge:',rel(knowledge));
  if(!i)console.log('Map: NOT INITIALIZED');
  else{
   console.log('Map:',i.schema||'(sin schema)');
   if(i.counts||i.scope){console.log('  agente · scope:',i.scope||'—');if(i.counts)console.log('  agente · counts:',i.counts)}
   if(i.graph&&existsSync(graphPath))console.log('  grafo CLI · scope:',i.graph.scope,'· commit:',i.graph.verified_commit||'unknown','· counts:',JSON.stringify(i.graph.counts));
   else console.log(`  grafo CLI: NO CONSTRUIDO — ejecuta "${SELF} init --scope src"`)
  }
 }
 else if(cmd==='relations'||cmd==='why'){const n=nodeFor(args[1]);if(Array.isArray(n)){console.log(n.map(x=>x.path).join('\n'))}else{printNode(n);if(cmd==='why'){const chain=pathFromRoot(graph(),n.path);console.log('reachable from root:',chain?'yes':'no');if(chain)console.log('path:',chain.join('\n   -> '));console.log('reason:',n.status==='orphan'?'sin referencias entrantes conocidas':n.status==='unreachable'?'tiene relaciones internas pero no es alcanzable desde una raíz conocida':'alcanzable desde una raíz conocida')}}}
 else if(cmd==='impact'){const g=graph(),n=nodeFor(args[1]);if(Array.isArray(n)){console.log(n.map(x=>x.path).join('\n'))}else{const seen=new Set(),queue=[n.path];while(queue.length){const p=queue.shift();if(seen.has(p))continue;seen.add(p);for(const s of g.nodes[p]?.incoming||[])queue.push(s)}console.log([...seen].join('\n'))}}
 else if(cmd==='orphans'){const s=str('--scope',''),g=graph();const a=Object.values(g.nodes).filter(n=>(n.status==='orphan'||n.status==='unreachable')&&(!s||n.path.includes(s)));console.log(a.map(n=>`${n.status.padEnd(11)} ${n.path}  in:${n.incoming.length} out:${n.outgoing.length}`).join('\n')||'Sin candidatos')}
 else if(cmd==='graph'){const s=str('--scope',''),g=graph();for(const n of Object.values(g.nodes).filter(n=>!s||n.path.includes(s)))console.log(`${n.path} -> ${n.outgoing.join(', ')||'—'}`)}
 else if(cmd==='benchmark'){
  const sub=args[1],all=readJson(benchPath,[]);
  if(sub==='start'){
   const prev=readJson(activePath,null);
   if(prev&&!flag('--force',false))throw new Error(`Ya hay un benchmark activo: "${prev.name}" (${prev.variant}, desde ${prev.started_at}). Ciérralo con "benchmark end" o repite con --force para descartarlo.`);
   const name=args[2]&&!args[2].startsWith('--')?args[2]:'unnamed', variant=str('--variant','semilla');
   writeJson(activePath,{name,variant,started_at:new Date().toISOString(),started_ms:Date.now()});
   console.log('⏱ benchmark started:',name,variant)
  }
  else if(sub==='end'){
   const a=readJson(activePath,null);if(!a)throw new Error(`No hay benchmark activo. Ábrelo con: ${SELF} benchmark start <name> --variant control|semilla`);
   const run={...a,ended_at:new Date().toISOString(),duration_ms:Date.now()-a.started_ms,input_tokens:num('--input-tokens'),output_tokens:num('--output-tokens'),tool_calls:num('--tool-calls')};
   all.push(run);writeJson(benchPath,all);rmSync(activePath,{force:true});console.log(run)
  }
  else if(sub==='report'){
   const by={};for(const r of all)(by[r.name]??=[]).push(r);
   if(!Object.keys(by).length){console.log('Sin corridas registradas.')}
   for(const [n,rs] of Object.entries(by)){console.log('\n'+n);for(const r of rs){const d=Number.isFinite(r.duration_ms)?(r.duration_ms/1000).toFixed(2)+'s':'—';console.log(`  ${String(r.variant||'?').padEnd(8)} ${d} input:${r.input_tokens??0} output:${r.output_tokens??0} tools:${r.tool_calls??0}`)}}
  }
  else help()
 }
 else if(cmd==='hook'){
  const sub=args[1]||'status';
  if(sub==='install')console.log('🌱 '+hookInstall());
  else if(sub==='uninstall')console.log('🌱 '+hookUninstall());
  else{
   const s=readJson(settingsPath,null);
   console.log('🌱 Hook:',hasHook(s)?'INSTALADO':'NO INSTALADO');
   console.log('Settings:',rel(settingsPath));
   console.log('Script:',hookScript);
   const c=readJson(countersPath,null);
   console.log('Contadores:',c?`${c.tool_calls} tool calls · ${c.files_read.length} archivos · ${c.searches} busquedas (desde ${c.since})`:'sin actividad registrada');
  }
 }
 else if(cmd==='test'){
  const sub=args[1]||'status', t=tests();
  if(sub==='start'){
   const prev=readJson(testActivePath,null);
   if(prev&&!flag('--force',false))throw new Error(`Ya hay un test activo: "${prev.name}" (${prev.variant}). Cierralo con "test end" o repite con --force.`);
   const name=args[2]&&!args[2].startsWith('--')?args[2]:null;
   if(!name)throw new Error(`Falta el nombre del test: ${SELF} test start <name> --task "..." --variant control|semilla`);
   const variant=str('--variant',null);
   if(variant!=='control'&&variant!=='semilla')throw new Error('--variant debe ser control o semilla');
   const task=str('--task',null)||(t.runs.find(r=>r.name===name)?.task);
   if(!task)throw new Error('Falta --task "..." la primera vez que corres este test');
   ensure();const c=config();c.enabled=variant==='semilla';c.updated_at=new Date().toISOString();writeJson(cfgPath,c);
   rmSync(countersPath,{force:true});
   writeJson(testActivePath,{name,task,variant,started_at:new Date().toISOString(),started_ms:Date.now()});
   console.log(`\n🌱 test "${name}" · ${variant.toUpperCase()} · Semilla ${c.enabled?'ON':'OFF'}`);
   console.log('─'.repeat(52));
   console.log('Abre una sesion LIMPIA del agente y pega exactamente esto:\n');
   console.log(variant==='control'
    ?`Ignora por completo .fruti/knowledge/. Responde usando el repositorio directamente.\n\n${task}`
    :`Consulta .fruti/knowledge/ primero. Abre codigo solo para verificar o completar lo que el mapa no responda.\n\n${task}`);
   console.log(`\nAl terminar: ${SELF} test end --correct|--wrong [--input-tokens N]`);
  }
  else if(sub==='end'){
   const a=readJson(testActivePath,null);if(!a)throw new Error(`No hay test activo. Abrelo con: ${SELF} test start <name> --task "..." --variant control|semilla`);
   const ok=flag('--correct',false)===true, bad=flag('--wrong',false)===true;
   if(ok===bad)throw new Error('Marca el resultado con --correct o --wrong (exactamente uno).');
   const c=readJson(countersPath,null);
   if(!c)console.error(`Semilla: aviso · sin contadores del hook; se registra solo el tiempo. Revisa "${SELF} hook status".`);
   const run={...a,ended_at:new Date().toISOString(),duration_ms:Date.now()-a.started_ms,
    tool_calls:c?.tool_calls??null,files_read:c?.files_read?.length??null,searches:c?.searches??null,
    verification_reads:c?.reads_after_map?.length??null,map_consulted:c?.map_consulted??null,
    input_tokens:flag('--input-tokens',null)===null?null:num('--input-tokens'),
    output_tokens:flag('--output-tokens',null)===null?null:num('--output-tokens'),
    correct:ok,note:flag('--note',null)===true?null:flag('--note',null)};
   t.runs.push(run);writeJson(testsPath,t);
   rmSync(testActivePath,{force:true});rmSync(countersPath,{force:true});
   console.log(`🌱 registrado · ${run.name} · ${run.variant} · ${(run.duration_ms/1000).toFixed(1)}s · ${run.files_read??'—'} archivos · ${run.searches??'—'} busquedas · ${run.tool_calls??'—'} tool calls · ${ok?'✓':'✗'}`);
   const {of_,on}=pair(t.runs,run.name);if(of_&&on)printPair(run.name,of_,on);
  }
  else if(sub==='report'){
   const only=args[2]&&!args[2].startsWith('--')?args[2]:null;
   const names=[...new Set(t.runs.map(r=>r.name))].filter(n=>!only||n===only);
   if(!names.length){console.log('Sin tests registrados.')}
   else{console.log('\n🌱 SEMILLA BENCHMARK');for(const n of names){const {of_,on}=pair(t.runs,n);printPair(n,of_,on)}}
  }
  else if(sub==='overhead'){
   t.overhead={...t.overhead,init_tokens:num('--init-tokens'),...(flag('--sync-tokens',null)===null?{}:{sync_tokens:num('--sync-tokens')})};
   writeJson(testsPath,t);console.log('🌱 overhead registrado:',t.overhead);
  }
  else if(sub==='status'){
   const names=[...new Set(t.runs.map(r=>r.name))];
   const pairs=names.map(n=>pair(t.runs,n)).filter(p=>p.of_&&p.on);
   console.log('\n🌱 Semilla effectiveness');
   console.log('Experiments'.padEnd(20)+String(pairs.length).padStart(8)+`  (de ${names.length} tareas registradas)`);
   if(!pairs.length){console.log('\nNingun test tiene todavia sus dos condiciones. Corre la mitad que falte.')}
   else{
    const avg=k=>{const v=pairs.map(p=>{const a=k(p.of_),b=k(p.on);return Number.isFinite(a)&&Number.isFinite(b)&&a!==0?(b-a)/a*100:null}).filter(x=>x!==null);return v.length?(v.reduce((s,x)=>s+x,0)/v.length):null};
    const line=(l,v)=>console.log('  '+l.padEnd(18)+(v===null?'sin datos':(v>0?'+':'')+v.toFixed(0)+'%').padStart(10));
    console.log('\nAverage');line('Tiempo',avg(r=>r.duration_ms));line('Input tokens',avg(r=>r.input_tokens));line('Archivos leidos',avg(r=>r.files_read));line('Busquedas',avg(r=>r.searches));
    const acc=v=>{const rs=t.runs.filter(r=>r.variant===v);return rs.length?(rs.filter(r=>r.correct).length/rs.length*100).toFixed(1)+'%':'sin datos'};
    console.log('\nAccuracy');console.log('  OFF'.padEnd(20)+acc('control').padStart(10));console.log('  ON'.padEnd(20)+acc('semilla').padStart(10));
    console.log('\nSemilla overhead');
    console.log('  INIT'.padEnd(20)+(t.overhead?.init_tokens?nfmt(t.overhead.init_tokens)+' tokens':'sin datos').padStart(10));
    console.log('  SYNC'.padEnd(20)+(t.overhead?.sync_tokens?nfmt(t.overhead.sync_tokens)+' tokens':'sin datos').padStart(10));
    const saved=pairs.map(p=>Number.isFinite(p.of_.input_tokens)&&Number.isFinite(p.on.input_tokens)?p.of_.input_tokens-p.on.input_tokens:null).filter(x=>x!==null);
    const mean=saved.length?saved.reduce((s,x)=>s+x,0)/saved.length:null;
    console.log('\nBreak-even'.padEnd(20)+((t.overhead?.init_tokens&&mean&&mean>0)?(t.overhead.init_tokens/mean).toFixed(1)+' tareas':'sin datos (falta overhead o input tokens)').padStart(10));
   }
  }
  else help()
 }
 else help();
}catch(e){console.error('Semilla:',e.message);process.exit(1)}
