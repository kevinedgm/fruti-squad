#!/usr/bin/env node
/**
 * Semilla local CLI — deterministic project map for Fruti Squad.
 * Zero dependencies. Node >=16.
 */
import { existsSync, mkdirSync, readFileSync, writeFileSync, readdirSync, statSync, rmSync } from 'node:fs';
import { resolve, join, relative, extname, dirname, normalize } from 'node:path';
import { spawnSync } from 'node:child_process';
import { performance } from 'node:perf_hooks';

const cwd=process.cwd(), root=resolve(cwd), fruti=join(root,'.fruti'), knowledge=join(fruti,'knowledge');
const cfgPath=join(fruti,'semilla.json'), benchPath=join(fruti,'benchmarks.json'), activePath=join(fruti,'.benchmark-active.json');
const SCHEMA='fruti-semilla/v1';
const IGNORE=new Set(['node_modules','.git','.fruti','dist','build','coverage','.next','.nuxt','.output','vendor']);
const CODE=new Set(['.js','.mjs','.cjs','.ts','.tsx','.jsx','.vue','.svelte','.java','.py','.php','.dart']);
const args=process.argv.slice(2), cmd=args[0]||'help';
const flag=(n,d=null)=>{const i=args.indexOf(n); return i>=0 ? (args[i+1]&&!args[i+1].startsWith('--')?args[i+1]:true):d};
const ensure=()=>{mkdirSync(knowledge,{recursive:true});};
const readJson=(p,d)=>{try{return JSON.parse(readFileSync(p,'utf8'))}catch{return d}};
const writeJson=(p,v)=>{mkdirSync(dirname(p),{recursive:true});writeFileSync(p,JSON.stringify(v,null,2)+'\n')};
const slash=p=>p.split('\\').join('/');
function gitSha(){const r=spawnSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8'});return r.status===0?r.stdout.trim():null}
function config(){return readJson(cfgPath,{enabled:true,knowledge_path:'.fruti/knowledge'})}
function walk(dir,out=[]){for(const e of readdirSync(dir)){if(IGNORE.has(e))continue;const p=join(dir,e);let s;try{s=statSync(p)}catch{continue}if(s.isDirectory())walk(p,out);else if(CODE.has(extname(e)))out.push(p)}return out}
function imports(text,file){
 const found=[]; const patterns=[/\b(?:import|export)\s+(?:[^'"]*?\s+from\s+)?['"]([^'"]+)['"]/g,/\brequire\(\s*['"]([^'"]+)['"]\s*\)/g,/\bimport\(\s*['"]([^'"]+)['"]\s*\)/g];
 for(const re of patterns){let m;while((m=re.exec(text)))found.push(m[1])}
 return [...new Set(found)].filter(x=>x.startsWith('.')).map(x=>resolveImport(file,x)).filter(Boolean)
}
function resolveImport(file,spec){
 const base=resolve(dirname(file),spec); const tries=[base,...CODE].map((x,i)=>i?base+x:x);
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
function build(scope='.',force=false){
 const started=performance.now(), abs=resolve(root,scope);if(!existsSync(abs))throw new Error('Scope no existe: '+scope);
 const prev=mapState();if(prev.kind==='foreign'&&!force)throw new Error(`El mapa existente usa el schema "${prev.index.schema}": lo generó el agente, no este CLI. init/sync sobrescribirían index.json y orphans.json. Usa --force si de verdad quieres reemplazarlo.`);
 const files=walk(abs).map(p=>slash(relative(root,p))), nodes={};
 for(const f of files){let text='';try{text=readFileSync(join(root,f),'utf8')}catch{};nodes[f]={path:f,kind:classify(f),outgoing:imports(text,join(root,f)),incoming:[],status:'unknown',confidence:'medium'}}
 for(const n of Object.values(nodes))for(const t of n.outgoing)if(nodes[t])nodes[t].incoming.push(n.path);
 const rs=roots(files), seen=new Set(), q=[...rs];while(q.length){const f=q.shift();if(seen.has(f)||!nodes[f])continue;seen.add(f);for(const t of nodes[f].outgoing)q.push(t)}
 for(const n of Object.values(nodes)){if(seen.has(n.path)){n.status='active';n.confidence='high'}else if(n.incoming.length===0){n.status='orphan';n.confidence='medium'}else{n.status='unreachable';n.confidence='medium'}}
 const result={schema:SCHEMA,generated_at:new Date().toISOString(),verified_commit:gitSha(),scope:slash(relative(root,abs))||'.',roots:rs,nodes};
 ensure();writeJson(join(knowledge,'graph.json'),result);
 const orphans=Object.values(nodes).filter(n=>n.status==='orphan'||n.status==='unreachable');writeJson(join(knowledge,'orphans.json'),{generated_at:result.generated_at,items:orphans});
 const counts={};for(const n of Object.values(nodes))counts[n.status]=(counts[n.status]||0)+1;
 writeJson(join(knowledge,'index.json'),{schema:result.schema,updated_at:result.generated_at,verified_commit:result.verified_commit,scope:result.scope,roots:rs,counts,files:{graph:'graph.json',orphans:'orphans.json'}});
 return {ms:performance.now()-started,files:files.length,counts,roots:rs.length}
}
function mapState(){const i=readJson(join(knowledge,'index.json'),null);if(!i)return{kind:'none',index:null};return{kind:i.schema&&i.schema!==SCHEMA?'foreign':'cli',index:i}}
function graph(){const g=readJson(join(knowledge,'graph.json'),null);if(g)return g;const st=mapState();throw new Error(st.kind==='foreign'?`Hay un mapa con schema "${st.index.schema}" pero sin graph.json: lo construyó el agente, no este CLI. Ejecuta "fruti semilla init --force" para generar el grafo del CLI (sobrescribe index.json y orphans.json).`:'No hay mapa. Ejecuta: fruti semilla init')}
function nodeFor(q){const g=graph(), exact=g.nodes[slash(q)];if(exact)return exact;const hits=Object.values(g.nodes).filter(n=>n.path.toLowerCase().includes(q.toLowerCase()));return hits}
function printNode(n){console.log('\n🌱 '+n.path);console.log('status:',n.status,'| confidence:',n.confidence);console.log('incoming:',n.incoming.length?n.incoming.join(', '):'—');console.log('outgoing:',n.outgoing.length?n.outgoing.join(', '):'—')}
function changed(){const r=spawnSync('git',['diff','--name-only','HEAD'],{cwd:root,encoding:'utf8'});return r.status===0?r.stdout.trim().split(/\r?\n/).filter(Boolean):[]}
function help(){console.log(`
🌱 Semilla
  fruti semilla init [--scope src] [--force]
  fruti semilla map <path>
  fruti semilla sync
  fruti semilla on | off | status
  fruti semilla relations <file>
  fruti semilla impact <file>
  fruti semilla why <file>
  fruti semilla orphans [--scope text]
  fruti semilla graph [--scope text]
  fruti semilla benchmark start <name> --variant control|semilla
  fruti semilla benchmark end [--input-tokens N --output-tokens N --tool-calls N]
  fruti semilla benchmark report
`)}

try{
 if(cmd==='init'||cmd==='map'){const scope=cmd==='map'?(args[1]||'.'):(flag('--scope','.')||'.');const r=build(scope,!!flag('--force',false));console.log(`🌱 mapa listo · ${r.files} archivos · ${r.roots} raíces · ${r.ms.toFixed(0)} ms`);console.log(r.counts)}
 else if(cmd==='sync'){const c=changed();const old=readJson(join(knowledge,'index.json'),{});const scope=old.scope||'.';const r=build(scope,!!flag('--force',false));console.log(`🌱 sync · ${c.length} archivos cambiados detectados · mapa verificado en ${r.ms.toFixed(0)} ms`)}
 else if(cmd==='on'||cmd==='off'){ensure();const c=config();c.enabled=cmd==='on';c.updated_at=new Date().toISOString();writeJson(cfgPath,c);console.log('🌱 Semilla',c.enabled?'ON':'OFF')}
 else if(cmd==='status'){const c=config(),st=mapState(),i=st.index;console.log('🌱 Semilla',c.enabled?'ON':'OFF');if(!i)console.log('Map: NOT INITIALIZED');else if(st.kind==='foreign'){console.log('Map: EXTERNO (schema '+i.schema+')');console.log('Scope:',i.scope||'—');console.log('Nota: lo construyó el agente, no este CLI; relations/impact/why/orphans/graph necesitan "fruti semilla init --force".')}else{console.log('Map: READY');console.log('Commit:',i.verified_commit||'unknown');console.log('Scope:',i.scope);console.log('Counts:',i.counts)}}
 else if(cmd==='relations'||cmd==='why'){const q=args[1];if(!q)throw new Error('Falta archivo');const n=nodeFor(q);if(Array.isArray(n)){console.log(n.map(x=>x.path).join('\n'))}else{printNode(n);if(cmd==='why'){console.log('reachable from root:',n.status==='active'?'yes':'no');console.log('reason:',n.status==='orphan'?'sin referencias entrantes conocidas':n.status==='unreachable'?'tiene relaciones internas pero no es alcanzable desde una raíz conocida':'alcanzable desde una raíz conocida')}}}
 else if(cmd==='impact'){const q=args[1],g=graph(),n=nodeFor(q);if(Array.isArray(n)){console.log(n.map(x=>x.path).join('\n'))}else{const seen=new Set(),queue=[n.path];while(queue.length){const p=queue.shift();if(seen.has(p))continue;seen.add(p);for(const s of g.nodes[p]?.incoming||[])queue.push(s)}console.log([...seen].join('\n'))}}
 else if(cmd==='orphans'){const s=flag('--scope',''),g=graph();const a=Object.values(g.nodes).filter(n=>(n.status==='orphan'||n.status==='unreachable')&&(!s||n.path.includes(s)));console.log(a.map(n=>`${n.status.padEnd(11)} ${n.path}  in:${n.incoming.length} out:${n.outgoing.length}`).join('\n')||'Sin candidatos')}
 else if(cmd==='graph'){const s=flag('--scope',''),g=graph();for(const n of Object.values(g.nodes).filter(n=>!s||n.path.includes(s)))console.log(`${n.path} -> ${n.outgoing.join(', ')||'—'}`)}
 else if(cmd==='benchmark'){const sub=args[1],all=readJson(benchPath,[]);if(sub==='start'){const name=args[2]||'unnamed',variant=flag('--variant','semilla');writeJson(activePath,{name,variant,started_at:new Date().toISOString(),started_ms:Date.now()});console.log('⏱ benchmark started:',name,variant)}else if(sub==='end'){const a=readJson(activePath,null);if(!a)throw new Error('No benchmark activo');const run={...a,ended_at:new Date().toISOString(),duration_ms:Date.now()-a.started_ms,input_tokens:Number(flag('--input-tokens',0)),output_tokens:Number(flag('--output-tokens',0)),tool_calls:Number(flag('--tool-calls',0))};all.push(run);writeJson(benchPath,all);rmSync(activePath,{force:true});console.log(run)}else if(sub==='report'){const by={};for(const r of all)(by[r.name]??=[]).push(r);for(const [n,rs] of Object.entries(by)){console.log('\n'+n);for(const r of rs)console.log(`  ${r.variant.padEnd(8)} ${(r.duration_ms/1000).toFixed(2)}s input:${r.input_tokens} output:${r.output_tokens} tools:${r.tool_calls}`)}}else help()}
 else help();
}catch(e){console.error('Semilla:',e.message);process.exit(1)}
