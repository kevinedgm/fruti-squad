// Mango · kit de piezas para ilustraciones planas geométricas.
// Cada pieza devuelve SVG como texto. El color nunca es fijo: cada forma usa una clase de rol
// (mango-<id>__<rol>) y el <style> de la ilustración traduce los roles a tokens del proyecto.
// Uso: import { persona, objeto, ilustracion } from './kit.mjs'

const r1 = (v) => Math.round(v * 10) / 10;
const rad = (g) => (g * Math.PI) / 180;
const pt = (x, y, len, ang) => [x + len * Math.cos(rad(ang)), y + len * Math.sin(rad(ang))];

// Roles de color (nombre del rol → token del proyecto y valor por defecto si el token no existe).
export const ROLES = {
  acento:     ['--mango-acento',     '#5b5bd6'],
  'acento-2': ['--mango-acento-2',   '#f5a524'],
  tinta:      ['--mango-tinta',      '#2b2d42'],
  'tinta-2':  ['--mango-tinta-2',    '#4a4e69'],
  piel:       ['--mango-piel',       '#c98e6b'],
  'piel-2':   ['--mango-piel-2',     '#8d5a3c'],
  'piel-3':   ['--mango-piel-3',     '#f1c9a5'],
  superficie: ['--mango-superficie', '#ffffff'],
  forma:      ['--mango-forma',      '#e8e9f7'],
  linea:      ['--mango-linea',      '#c7c9e0'],
};
const DARK = { superficie: '#23243a', forma: '#2e3050', linea: '#4b4e78', tinta: '#11121f' };

// Poses: ángulos en grados (0 = derecha, 90 = abajo) para brazo [hombro→codo, codo→mano] y piernas.
export const POSES = {
  'de-pie':    { bi: [100, 95],  bd: [80, 85],   pi: [94, 91],  pd: [86, 89] },
  'senala':    { bi: [100, 92],  bd: [-40, -28], pi: [94, 91],  pd: [86, 89] },
  'saluda':    { bi: [100, 95],  bd: [-60, -100], pi: [94, 91], pd: [86, 89] },
  'sostiene':  { bi: [110, 10],  bd: [70, 170],  pi: [94, 91],  pd: [86, 89] },
  'explica':   { bi: [102, 92],  bd: [35, -20],  pi: [94, 91],  pd: [86, 89] },
};

const PELO = {
  corto: (cx, cy) => `M${r1(cx - 18.8)} ${r1(cy)}A18.8 18.8 0 0 1 ${r1(cx + 18.8)} ${r1(cy)}Q${r1(cx + 9)} ${r1(cy - 7)} ${r1(cx - 4)} ${r1(cy - 8.5)}Q${r1(cx - 13)} ${r1(cy - 6.5)} ${r1(cx - 18.8)} ${r1(cy)}Z`,
  largo: (cx, cy) => `M${r1(cx - 21)} ${r1(cy + 30)}V${r1(cy - 2)}A21 21 0 0 1 ${r1(cx + 21)} ${r1(cy - 2)}V${r1(cy + 30)}Q${r1(cx)} ${r1(cy + 36)} ${r1(cx - 21)} ${r1(cy + 30)}Z`,
  rizado: (cx, cy) => [[-15, -6, 9], [-6, -14, 10], [6, -14, 10], [15, -6, 9], [-18, 4, 7], [18, 4, 7]]
    .map(([dx, dy, r]) => `M${r1(cx + dx + r)} ${r1(cy + dy)}A${r} ${r} 0 1 0 ${r1(cx + dx - r)} ${r1(cy + dy)}A${r} ${r} 0 1 0 ${r1(cx + dx + r)} ${r1(cy + dy)}Z`).join(''),
};

// persona({ x, y (suelo), escala, pose, piel: 'piel'|'piel-2'|'piel-3', pelo: 'corto'|'largo'|'rizado'|'moño', ropa: rol, pantalon: rol })
export function persona({ x = 0, y = 0, escala = 1, pose = 'de-pie', piel = 'piel', pelo = 'corto', ropa = 'acento', pantalon = 'tinta', zapato = 'tinta-2' } = {}) {
  const P = POSES[pose] || POSES['de-pie'];
  const ys = -144, yh = -82;                  // hombros y caderas (origen en el suelo, centro de la figura)
  const sI = [-21, ys + 9], sD = [21, ys + 9];
  const brazo = (s, [a1, a2]) => {
    const c = pt(s[0], s[1], 33, a1), m = pt(c[0], c[1], 29, a2);
    return { d: `M${r1(s[0])} ${r1(s[1])}L${r1(c[0])} ${r1(c[1])}L${r1(m[0])} ${r1(m[1])}`, mano: m };
  };
  const pierna = (h, [a1, a2]) => {
    const k = pt(h[0], h[1], 40, a1), p = pt(k[0], k[1], 38, a2);
    return { d: `M${r1(h[0])} ${r1(h[1])}L${r1(k[0])} ${r1(k[1])}L${r1(p[0])} ${r1(p[1])}`, pie: p };
  };
  const bI = brazo(sI, P.bi), bD = brazo(sD, P.bd);
  const pI = pierna([-10, yh], P.pi), pD = pierna([10, yh], P.pd);
  const cx = 0, cy = ys - 25;
  const o = [];
  if (pelo === 'largo') o.push(`<path class="{c}__${'tinta'}" d="${PELO.largo(cx, cy)}"/>`);
  // piernas y zapatos
  for (const [p, dir] of [[pI, -1], [pD, 1]]) {
    o.push(`<path class="{c}__trazo-${pantalon}" stroke-width="18" d="${p.d}"/>`);
    o.push(`<path class="{c}__trazo-${zapato}" stroke-width="10" d="M${r1(p.pie[0])} ${r1(p.pie[1] + 3)}H${r1(p.pie[0] + dir * 11)}"/>`);
  }
  // brazo de atrás (izquierdo) primero
  o.push(`<path class="{c}__trazo-${ropa}" stroke-width="13" d="${bI.d}"/>`);
  o.push(`<circle class="{c}__${piel}" cx="${r1(bI.mano[0])}" cy="${r1(bI.mano[1])}" r="6.5"/>`);
  // torso
  o.push(`<path class="{c}__${ropa}" d="M-23 ${ys + 14}Q-23 ${ys} -9 ${ys}H9Q23 ${ys} 23 ${ys + 14}L19 ${yh + 6}Q19 ${yh + 10} 15 ${yh + 10}H-15Q-19 ${yh + 10} -19 ${yh + 6}Z"/>`);
  // cuello y cabeza
  o.push(`<rect class="{c}__${piel}" x="-6" y="${ys - 9}" width="12" height="12" rx="3"/>`);
  o.push(`<circle class="{c}__${piel}" cx="${cx}" cy="${cy}" r="18"/>`);
  if (pelo === 'corto' || pelo === 'moño') o.push(`<path class="{c}__tinta" d="${PELO.corto(cx, cy)}"/>`);
  if (pelo === 'moño') o.push(`<circle class="{c}__tinta" cx="${cx}" cy="${cy - 22}" r="8"/>`);
  if (pelo === 'largo') o.push(`<path class="{c}__tinta" d="${PELO.corto(cx, cy)}"/>`);
  if (pelo === 'rizado') o.push(`<path class="{c}__tinta" d="${PELO.rizado(cx, cy)}"/>`);
  // brazo de delante (derecho) al final
  o.push(`<path class="{c}__trazo-${ropa}" stroke-width="13" d="${bD.d}"/>`);
  o.push(`<circle class="{c}__${piel}" cx="${r1(bD.mano[0])}" cy="${r1(bD.mano[1])}" r="6.5"/>`);
  const t = `translate(${r1(x)} ${r1(y)})${escala !== 1 ? ` scale(${escala})` : ''}`;
  return { svg: `<g class="{c}__persona" transform="${t}">${o.join('')}</g>`,
    manoD: [x + bD.mano[0] * escala, y + bD.mano[1] * escala], manoI: [x + bI.mano[0] * escala, y + bI.mano[1] * escala] };
}

// Objetos: devuelven SVG en coordenadas absolutas.
export const objeto = {
  pizarra: ({ x, y, w = 170, h = 120 }) => [
    `<rect class="{c}__superficie" x="${x}" y="${y}" width="${w}" height="${h}" rx="10"/>`,
    `<rect class="{c}__trazo-linea" stroke-width="2" fill="none" x="${x}" y="${y}" width="${w}" height="${h}" rx="10"/>`,
    `<rect class="{c}__forma" x="${x + 14}" y="${y + 14}" width="${w * 0.45}" height="10" rx="5"/>`,
    ...[0, 1, 2, 3].map((i) => { const bh = [34, 52, 26, 64][i]; return `<rect class="{c}__${i === 3 ? 'acento' : 'acento-2'}" x="${x + 18 + i * 26}" y="${y + h - 16 - bh}" width="16" height="${bh}" rx="3"/>`; }),
    `<rect class="{c}__forma" x="${x + w - 52}" y="${y + 40}" width="38" height="8" rx="4"/>`,
    `<rect class="{c}__forma" x="${x + w - 52}" y="${y + 56}" width="28" height="8" rx="4"/>`,
  ].join(''),
  burbuja: ({ x, y, w = 96, h = 56, cola = 'izq' }) => {
    // Una sola forma (caja + cola) con borde: una superficie clara puede caer sobre el fondo de la página.
    const r = 14, b = y + h, t = cola === 'izq' ? x + 18 : x + w - 18, s = cola === 'izq' ? -1 : 1;
    const tail = cola === 'izq'
      ? `H${t + 12}L${t + s * 10} ${b + 16}L${t} ${b}`
      : `H${t}L${t + s * 10} ${b + 16}L${t - 12} ${b}`;
    const d = `M${x + r} ${y}H${x + w - r}A${r} ${r} 0 0 1 ${x + w} ${y + r}V${b - r}A${r} ${r} 0 0 1 ${x + w - r} ${b}`
      + (cola === 'izq' ? `H${t + 12}L${t - 10} ${b + 16}L${t} ${b}` : `H${t}L${t + 10} ${b + 16}L${t - 12} ${b}`)
      + `H${x + r}A${r} ${r} 0 0 1 ${x} ${b - r}V${y + r}A${r} ${r} 0 0 1 ${x + r} ${y}Z`;
    return [`<path class="{c}__superficie" d="${d}"/>`, `<path class="{c}__trazo-linea" stroke-width="2" d="${d}"/>`,
      `<rect class="{c}__acento" x="${x + 14}" y="${y + 15}" width="${w - 28}" height="8" rx="4"/>`,
      `<rect class="{c}__forma" x="${x + 14}" y="${y + 31}" width="${(w - 28) * 0.62}" height="8" rx="4"/>`].join('');
  },
  planta: ({ x, y }) => [
    `<path class="{c}__acento" d="M${x} ${y - 30}C${x - 26} ${y - 46} ${x - 30} ${y - 74} ${x - 18} ${y - 86}C${x - 6} ${y - 70} ${x - 2} ${y - 52} ${x} ${y - 30}Z"/>`,
    `<path class="{c}__acento" d="M${x} ${y - 30}C${x + 24} ${y - 52} ${x + 34} ${y - 70} ${x + 22} ${y - 90}C${x + 6} ${y - 76} ${x} ${y - 56} ${x} ${y - 30}Z"/>`,
    `<path class="{c}__tinta-2" d="M${x - 18} ${y - 34}H${x + 18}L${x + 13} ${y}H${x - 13}Z"/>`,
  ].join(''),
  mancha: ({ x, y, w, h }) => `<path class="{c}__forma" d="M${x + w * 0.1} ${y + h * 0.35}C${x + w * 0.05} ${y + h * 0.05} ${x + w * 0.45} ${y - h * 0.04} ${x + w * 0.7} ${y + h * 0.08}C${x + w * 0.98} ${y + h * 0.2} ${x + w * 1.02} ${y + h * 0.62} ${x + w * 0.82} ${y + h * 0.86}C${x + w * 0.6} ${y + h * 1.04} ${x + w * 0.2} ${y + h * 0.98} ${x + w * 0.06} ${y + h * 0.74}C${x - w * 0.02} ${y + h * 0.6} ${x + w * 0.12} ${y + h * 0.5} ${x + w * 0.1} ${y + h * 0.35}Z"/>`,
  suelo: ({ x, y, w }) => `<rect class="{c}__forma" x="${x}" y="${y}" width="${w}" height="6" rx="3"/>`,
  puntos: ({ x, y }) => [[0, 0], [14, 0], [28, 0], [0, 14], [14, 14], [28, 14]].map(([dx, dy]) => `<circle class="{c}__acento-2" cx="${x + dx}" cy="${y + dy}" r="3"/>`).join(''),
};

// Envuelve las piezas en el SVG final: roles → tokens, accesibilidad y modo oscuro de los valores por defecto.
export function ilustracion({ id, w = 480, h = 320, titulo, decorativa = false, partes }) {
  const c = `mango-${id}`;
  const usados = new Set([...partes.join('').matchAll(/\{c\}__(?:trazo-)?([a-z0-9-]+)/g)].map((m) => m[1]).filter((r) => ROLES[r]));
  const vars = [...usados].map((r) => `--m-${r}:var(${ROLES[r][0]},${ROLES[r][1]})`).join(';');
  const varsOsc = [...usados].filter((r) => DARK[r]).map((r) => `--m-${r}:var(${ROLES[r][0]},${DARK[r]})`).join(';');
  const reglas = [...usados].map((r) => `.${c}__${r}{fill:var(--m-${r})}.${c}__trazo-${r}{fill:none;stroke:var(--m-${r});stroke-linecap:round;stroke-linejoin:round}`).join('');
  const css = `.${c}{${vars}}${varsOsc ? `@media (prefers-color-scheme:dark){.${c}{${varsOsc}}}` : ''}${reglas}`;
  const a11y = decorativa ? 'aria-hidden="true"' : `role="img" aria-labelledby="${c}-t"`;
  const tit = decorativa ? '' : `<title id="${c}-t">${titulo}</title>`;
  const body = partes.join('\n  ').replaceAll('{c}', c);
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" class="mango-ilu ${c}" ${a11y}>\n  ${tit}<style>${css}</style>\n  ${body}\n</svg>\n`;
}
