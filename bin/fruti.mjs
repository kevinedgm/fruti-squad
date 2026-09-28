#!/usr/bin/env node
// Fruti Squad command router.
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
const here=dirname(fileURLToPath(import.meta.url));
const a=process.argv.slice(2);
const entry=a[0]==='test'?'test.mjs':'install.mjs';
const pass=a[0]==='test'?a.slice(1):a;
const r=spawnSync(process.execPath,[resolve(here,entry),...pass],{stdio:'inherit',cwd:process.cwd()});
process.exit(r.status??1);
