import { persona, objeto, ilustracion } from '../scripts/kit.mjs';
import { writeFileSync } from 'node:fs';
const suelo = 292;
const p = persona({ x: 150, y: suelo, pose: 'senala', pelo: 'largo', piel: 'piel', ropa: 'acento' });
const svg = ilustracion({ id: 'ayuda-informa', titulo: 'Una persona señala un panel con una gráfica mientras explica', partes: [
  objeto.mancha({ x: 40, y: 40, w: 400, h: 250 }),
  objeto.puntos({ x: 66, y: 238 }),
  objeto.suelo({ x: 30, y: suelo + 2, w: 420 }),
  objeto.pizarra({ x: 222, y: 70, w: 196, h: 136 }),
  objeto.planta({ x: 430, y: suelo }),
  p.svg,
  objeto.burbuja({ x: 30, y: 40, w: 88, h: 50, cola: "der" }),
]});
writeFileSync('ayuda-informa.svg', svg); console.log(svg.length, 'bytes');
