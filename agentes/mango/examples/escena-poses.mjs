import { semilla, figura, ilustracion, linea, POSES } from '../scripts/kit.mjs';
import { writeFileSync } from 'node:fs';
semilla(3);
const H = 38, suelo = 300, poses = ['de-pie', 'camina', 'senala', 'sostiene', 'sentado'];
const partes = [linea([[10, suelo + 2], [890, suelo + 2]], { fina: true })];
poses.forEach((p, i) => { partes.push(figura({ x: 90 + i * 175, y: suelo, H, pose: p, pelo: ['corto', 'largo', 'barba', 'corto', 'largo'][i] }).svg); });
// guía del canon: 7 cabezas
for (let k = 0; k <= 7; k++) partes.push(linea([[20, suelo - k * H], [40, suelo - k * H]], { fina: true }));
writeFileSync('poses.svg', ilustracion({ id: 'poses', w: 900, h: 330, decorativa: true, partes }));
