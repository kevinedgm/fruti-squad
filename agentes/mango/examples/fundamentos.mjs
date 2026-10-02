// Mango · hoja de fundamentos (Fase 1 de la especificación): trazo, caras a–d, 10 expresiones, 7 peinados,
// proporciones, manos y poses. Genera fundamentos.html (una ilustración por celda, con rótulo HTML).
// Uso: node fundamentos.mjs [dir-salida]
import { semilla, cabeza, figura, mano, linea, ilustracion, CARAS, EXPRESIONES, PEINADOS, CANON } from '../scripts/kit.mjs';
import { writeFileSync } from 'node:fs';
import { join } from 'node:path';

const salida = process.argv[2] || '.';
let n = 0;
const celda = (rotulo, w, h, partes, z = 1.5) => `<figure style="width:${w * z}px">${ilustracion({ id: `f${n++}`, w, h, decorativa: true, partes })}<figcaption>${rotulo}</figcaption></figure>`;
const busto = (o) => { const c = cabeza({ x: 60, y: 118, s: 0.8, ...o }); return [c.atras, c.cuello, c.svg]; };

semilla(11);
const trazo = celda('trazo · peso estable', 300, 130, [
  linea([[20, 40], [90, 22], [170, 50], [280, 30]]), linea([[20, 80], [140, 96], [280, 76]], { fina: true }),
  linea([[60, 110], [80, 100], [100, 112], [120, 100]], { fina: true })]);
const caras = Object.keys(CARAS).map((c, i) => celda(`cara ${c}`, 130, 150, busto({ cara: c, pelo: ['crop', 'bob', 'curls', 'short-wave'][i], expresion: 'neutral' })));
const expres = Object.keys(EXPRESIONES).map((e, i) => celda(e, 130, 150, busto({ cara: 'a', pelo: 'short-wave', expresion: e })));
const pelos = Object.keys(PEINADOS).filter((p) => p !== 'ninguno').map((p, i) => celda(p, 130, 150, busto({ cara: 'abcd'[i % 4], pelo: p, expresion: 'happy' })));

// proporciones: 4 personas de pie con la guía de cabezas
const H = 46, suelo = 320;
const guia = []; for (let k = 0; k <= 6; k++) guia.push(linea([[8, suelo - k * H], [24, suelo - k * H]], { fina: true }));
const gente = [
  { cara: 'a', pelo: 'short-wave', complexion: 'average' }, { cara: 'b', pelo: 'ponytail', complexion: 'slim', camisa: 'acento' },
  { cara: 'c', pelo: 'curls', complexion: 'broad' }, { cara: 'd', pelo: 'bun', complexion: 'average', dir: -1 }];
const prop = celda(`proporciones · cabeza/torso = ${(1 / CANON.torso).toFixed(2)} · ~5,6 cabezas`, 640, 340,
  [...guia, ...gente.map((g, i) => figura({ x: 110 + i * 150, y: suelo, H, expresion: 'neutral', ...g }).svg)]);

const gestos = ['manopla', 'pulgar', 'senala', 'cuenco', 'abierta'];
const manos = gestos.map((g) => celda(`mano · ${g}`, 130, 110, [mano({ x: 20, y: 70, s: 0.75, gesto: g }).svg]));

const poses = [['de-pie', 'neutral'], ['camina', 'happy'], ['senala', 'curious'], ['sostiene', 'focused'], ['sentado', 'relieved'], ['pulgar', 'proud']];
const fila = poses.map(([p, e], i) => celda(`${p} · ${e}`, 200, 300, [figura({ x: 80, y: 285, H: 42, pose: p, expresion: e, cara: 'abcd'[i % 4],
  pelo: ['crop', 'long', 'short-wave', 'bob', 'curls', 'bun'][i], gestos: p === 'pulgar' ? { cerca: 'pulgar', lejos: 'manopla' } : p === 'senala' ? { cerca: 'senala', lejos: 'manopla' } : undefined,
  enfasis: p === 'pulgar' || p === 'senala' ? CANON.enfasis.comunicativo : 1 }).svg]));

const sec = (t, cosas) => `<h2>${t}</h2><div class="g">${cosas.join('')}</div>`;
writeFileSync(join(salida, 'fundamentos.html'), `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Mango · fundamentos</title><style>
body{margin:0;padding:24px;background:#FFFDF5;font:13px/1.4 system-ui,sans-serif;color:#111;width:1100px}h2{font-size:14px;margin:18px 0 6px}
.g{display:flex;flex-wrap:wrap;gap:6px 10px}figure{margin:0}figcaption{text-align:center;color:#555}svg{display:block;width:100%;height:auto}
</style></head><body><h1 style="font-size:18px">Mango · fundamentos (Fase 1)</h1>
${sec('Trazo', [trazo])}${sec('Caras a–d', caras)}${sec('10 expresiones', expres)}${sec('7 peinados', pelos)}${sec('Proporciones', [prop])}${sec('Manos', manos)}${sec('Poses + expresión', fila)}
</body></html>`);
console.log('ok');
