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

const cwd=process.cwd(), root=resolve(cwd), fruti=join(root,'.fruti');
const cfgPath=join(fruti,'semilla.json'), benchPath=join(fruti,'benchmarks.json'), activePath=join(fruti,'.benchmark-active.json');
const SCHEMA='fruti-semilla/v1';
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
function roots(files){
 const rs=new Set();
 for(const f of files){const b=f.split('/').pop();if(/^(main|index|app|server|bootstrap)\.(js|mjs|cjs|ts|tsx|jsx|vue|java|py|php|dart)$/i.test(b))rs.add(f);if(/router|routes/i.test(f))rs.add(f)}
 try{const pkg=JSON.parse(readFileSync(join(root,'package.json'),'utf8'));for(const k of ['main','module','browser'])if(pkg[k])rs.add(slash(pkg[k]))}catch{}
 return [...rs].filter(x=>files.includes(x))
}
function classify(path){if(/test|spec|__tests__/i.test(path))return'test';if(/route|router/i.test(path))return'route';if(/component|\.vue$|\.svelte$/i.test(path))return'ui';if(/store|state/i.test(path))return'state';if(/service|api|client/i.test(path))return'service';return'code'}
function build(scope='.'){
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
 writeJson(indexPath,{...prev,schema:prev.schema||SCHEMA,updated_at:result.generated_at,
  files:{...(prev.files||{}),graph:'graph.json',graph_orphans:'graph-orphans.json'},
  graph:{generated_at:result.generated_at,verified_commit:result.verified_commit,scope:result.scope,roots:rs,counts}});
 return {ms:performance.now()-started,files:files.length,counts,roots:rs.length}
}
function graph(){const g=readJson(graphPath,null);if(g)return g;throw new Error(`No hay grafo del CLI en ${rel(graphPath)}. Ejecuta: fruti semilla init [--scope src]`)}
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
function help(){console.log(`
🌱 Semilla
  fruti semilla init [--scope src]
  fruti semilla map <path>
  fruti semilla sync
  fruti semilla on | off | status
  fruti semilla relations <file>
  fruti semilla impact <file>
  fruti semilla why <file>
  fruti semilla orphans [--scope text]
  fruti semilla graph [--scope text]
  fruti semilla benchmark start <name> --variant control|semilla [--force]
  fruti semilla benchmark end [--input-tokens N --output-tokens N --tool-calls N]
  fruti semilla benchmark report
`)}

try{
 if(cmd==='init'||cmd==='map'){const scope=cmd==='map'?(args[1]||'.'):(str('--scope','.')||'.');const r=build(scope);console.log(`🌱 mapa listo · ${r.files} archivos · ${r.roots} raíces · ${r.ms.toFixed(0)} ms`);console.log(r.counts)}
 else if(cmd==='sync'){const c=changed();const old=readJson(indexPath,{});const scope=old.graph?.scope||old.scope||'.';const r=build(scope);console.log(`🌱 sync · ${c.length} archivos cambiados · grafo reconstruido sobre "${scope}" en ${r.ms.toFixed(0)} ms`)}
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
   else console.log('  grafo CLI: NO CONSTRUIDO — ejecuta "fruti semilla init --scope src"')
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
   const a=readJson(activePath,null);if(!a)throw new Error('No hay benchmark activo. Ábrelo con: fruti semilla benchmark start <name> --variant control|semilla');
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
 else help();
}catch(e){console.error('Semilla:',e.message);process.exit(1)}
