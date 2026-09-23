#!/usr/bin/env node
/**
 * Semilla PostToolUse hook — cuenta la exploración de una sesión.
 *
 * Lo instala `fruti semilla hook install`. Recibe el payload del harness por
 * stdin y acumula contadores en `.fruti/.counters.json`, que `fruti semilla
 * test end` lee para medir una condición del A/B.
 *
 * Regla de oro: este hook NUNCA falla ni imprime nada. Un benchmark roto es
 * molesto; un hook que rompe la sesión del agente es inaceptable.
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';

const SEARCH_TOOLS=new Set(['Grep','Glob','WebSearch']);
const READ_TOOLS=new Set(['Read','NotebookRead']);
const SEARCH_CMD=/(^|[\s|;&(])(rg|grep|egrep|fgrep|ag|ack|find|fd)\b/;
// Leer un archivo por shell (cat/head/sed -n) cuenta igual que la herramienta Read:
// en modo auto el agente trabaja por Bash, y sin esto files_read y
// verification_reads se quedan en cero para siempre.
const READ_CMD=/(^|[\s|;&(])(cat|bat|head|tail|less|more|nl)\b/;
const SED_READ=/(^|[\s|;&(])sed\s+[^|;&]*-n\b/;
const KNOWLEDGE=/(?:^|[^\w.])\.fruti[\\/]knowledge[\\/]/;
// La contabilidad del propio benchmark no es exploracion del proyecto.
const SELF_CMD=/(^|[\s|;&(=])(semilla|[^\s]*semilla\.mjs|fruti)\b/;
const FRUTI_STATE=/(?:^|[^\w.])\.fruti[\\/](?!knowledge[\\/])/;

const read=p=>{try{return JSON.parse(readFileSync(p,'utf8'))}catch{return null}};
const paths=cmd=>cmd.split(/\s+/).filter(t=>!t.startsWith('-')&&/^[^\s'"]*[\w)\]]\.[A-Za-z0-9]{1,8}$/.test(t)).map(t=>t.replace(/^['"]|['"]$/g,''));

function main(raw){
 const ev=JSON.parse(raw||'{}');
 const root=ev.cwd||process.cwd();
 // Sin una medicion abierta el hook no hace nada. Contar siempre ensuciaba el
 // archivo con la exploracion de sesiones que no se estaban midiendo y hacia
 // una escritura por cada tool call de cada sesion, para siempre.
 if(!existsSync(join(root,'.fruti','.test-active.json'))&&!existsSync(join(root,'.fruti','.benchmark-active.json')))return;
 const file=join(root,'.fruti','.counters.json');
 const c=read(file)||{since:new Date().toISOString(),tool_calls:0,searches:0,by_tool:{},files_read:[],reads_after_map:[],map_consulted:false};

 const tool=ev.tool_name||'unknown';
 const input=ev.tool_input||{};
 const cmd=String(input.command||'');
 const path=input.file_path||input.notebook_path||input.path||'';

 const touchedMap=KNOWLEDGE.test(path)||KNOWLEDGE.test(String(input.pattern||''))||KNOWLEDGE.test(cmd);
 const touchedState=FRUTI_STATE.test(path)||(tool==='Bash'&&FRUTI_STATE.test(cmd));
 // Invocaciones del propio CLI y lecturas de su estado (benchmarks.json, tests.json,
 // contadores) son contabilidad del experimento, no exploracion: ni siquiera suman
 // un tool call. El mapa si cuenta, porque consultarlo es lo que se esta midiendo.
 if((tool==='Bash'&&SELF_CMD.test(cmd))||(touchedState&&!touchedMap))return;

 c.tool_calls++;
 c.by_tool[tool]=(c.by_tool[tool]||0)+1;

 const note=p=>{
  if(!p||KNOWLEDGE.test(p)||FRUTI_STATE.test(p))return;
  if(!c.files_read.includes(p))c.files_read.push(p);
  if(c.map_consulted&&!c.reads_after_map.includes(p))c.reads_after_map.push(p);
 };

 if(touchedMap){
  // Consultar el mapa es el atajo que se mide, no exploracion del repo.
  // A partir de aqui, cada lectura de codigo es verificacion.
  c.map_consulted=true;
 } else {
  if(SEARCH_TOOLS.has(tool))c.searches++;
  else if(tool==='Bash'&&SEARCH_CMD.test(cmd))c.searches++;
  if(READ_TOOLS.has(tool))note(path);
  else if(tool==='Bash'&&(READ_CMD.test(cmd)||SED_READ.test(cmd)))for(const p of paths(cmd))note(p);
 }

 mkdirSync(dirname(file),{recursive:true});
 writeFileSync(file,JSON.stringify(c,null,2)+'\n');
}

let raw='';
process.stdin.on('data',d=>{raw+=d});
process.stdin.on('end',()=>{try{main(raw)}catch{}process.exit(0)});
process.stdin.on('error',()=>process.exit(0));
setTimeout(()=>process.exit(0),3000).unref();
