import { semilla, cabezaPerfil as cabeza, torso, brazo, mano, agujero, rayitas, objeto, ilustracion, linea } from '../scripts/kit.mjs';
import { writeFileSync } from 'node:fs';
semilla(23);
const cuello = [372, 214], s = 1.15;
const t = torso({ x: cuello[0], y: cuello[1], s, flip: true });
const c = cabeza({ x: cuello[0], y: cuello[1], s, flip: true, pelo: 'corto' });
const b = brazo({ desde: t.hombro, hasta: [236, 214], ancho: 46, curva: -0.08 });
const m = mano({ x: b.muneca[0], y: b.muneca[1], rot: b.angulo - 180, flip: true, gesto: 'cuenco', s: 1.05 });
const g = objeto.grana({ cx: m.apoyo[0], base: m.apoyo[1] + 4, t: 5 });
writeFileSync('presenta.svg', ilustracion({ id: 'presenta', titulo: 'Una persona se asoma por la derecha y presenta una gran cochinilla', partes: [
  t.svg, c.svg, b.svg, g, m.svg, rayitas({ cx: m.apoyo[0], cy: m.apoyo[1] - 60, r: 70 }) ] }));
semilla(5);
const h = (x, y, gesto, ang, flip = false) => { const ag = agujero({ x, y, rx: 16, ry: 44 }); const bb = brazo({ desde: [x, y], hasta: [x + (flip ? -1 : 1) * 110 * Math.cos(ang * Math.PI / 180), y + 110 * Math.sin(ang * Math.PI / 180)], ancho: 44, curva: 0.06 });
  const mm = mano({ x: bb.muneca[0], y: bb.muneca[1], rot: flip ? bb.angulo - 180 : bb.angulo, flip, gesto }); return ag + bb.svg + mm.svg; };
writeFileSync('manos.svg', ilustracion({ id: 'manos', w: 600, h: 320, decorativa: true, partes: [h(40, 90, 'cuenco', -10), h(40, 230, 'senala', 8), h(560, 160, 'abierta', -20, true)] }));
