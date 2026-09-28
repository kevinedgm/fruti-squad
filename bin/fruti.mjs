#!/usr/bin/env node
// Fruti Squad command router.
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
const here=dirname(fileURLToPath(import.meta.url));
const a=process.argv.slice(2);
const command=a[0];
const entry=command==='test'?'test.mjs':command==='foundations'?'foundations.mjs':'install.mjs';
const pass=(command==='test'||command==='foundations')?a.slice(1):a;
const r=spawnSync(process.execPath,[resolve(here,entry),...pass],{stdio:'inherit',cwd:process.cwd()});
process.exit(r.status??1);
