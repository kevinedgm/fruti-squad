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
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';

const SEARCH_TOOLS=new Set(['Grep','Glob','WebSearch']);
const READ_TOOLS=new Set(['Read','NotebookRead']);
const SEARCH_CMD=/\b(rg|grep|egrep|fgrep|ag|ack|find|fd|ls)\b/;

const read=p=>{try{return JSON.parse(readFileSync(p,'utf8'))}catch{return null}};

function main(raw){
 const ev=JSON.parse(raw||'{}');
 const root=ev.cwd||process.cwd();
 const file=join(root,'.fruti','.counters.json');
 const c=read(file)||{since:new Date().toISOString(),tool_calls:0,searches:0,by_tool:{},files_read:[],reads_after_map:[],map_consulted:false};

 const tool=ev.tool_name||'unknown';
 const input=ev.tool_input||{};
 const path=input.file_path||input.notebook_path||input.path||'';
 const looksLikeMap=/(^|[\\/])\.fruti[\\/]/.test(path)||/\.fruti[\\/]knowledge/.test(input.pattern||'')||/\.fruti/.test(input.command||'');

 c.tool_calls++;
 c.by_tool[tool]=(c.by_tool[tool]||0)+1;

 if(looksLikeMap){
  // Consultar el mapa no cuenta como exploración del repo: es el atajo que
  // estamos midiendo. A partir de aquí, cada lectura es verificación.
  c.map_consulted=true;
 } else {
  if(SEARCH_TOOLS.has(tool))c.searches++;
  else if(tool==='Bash'&&SEARCH_CMD.test(input.command||''))c.searches++;
  if(READ_TOOLS.has(tool)&&path){
   if(!c.files_read.includes(path))c.files_read.push(path);
   if(c.map_consulted&&!c.reads_after_map.includes(path))c.reads_after_map.push(path);
  }
 }

 mkdirSync(dirname(file),{recursive:true});
 writeFileSync(file,JSON.stringify(c,null,2)+'\n');
}

let raw='';
process.stdin.on('data',d=>{raw+=d});
process.stdin.on('end',()=>{try{main(raw)}catch{}process.exit(0)});
process.stdin.on('error',()=>process.exit(0));
setTimeout(()=>process.exit(0),3000).unref();
