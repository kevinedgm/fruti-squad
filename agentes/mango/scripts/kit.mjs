// Mango · kit de piezas en estilo línea de rotulador.
// Contorno de tinta con un temblor suave y determinista, rellenos planos (a veces desplazados del contorno,
// como una impresión mal registrada), fondo de un color. El color nunca es fijo: cada forma usa una clase de
// rol (mango-<id>__<rol>) y el <style> de la ilustración traduce los roles a tokens del proyecto.
// Uso: import { semilla, linea, relleno, brazo, mano, cabeza, torso, agujero, rayitas, objeto, ilustracion } from './kit.mjs'

const f = (v) => Math.round(v * 10) / 10;
const rad = (g) => (g * Math.PI) / 180;

// Roles de color: nombre → [token del proyecto, valor por defecto]. DARK: valores por defecto en modo oscuro.
export const ROLES = {
  fondo:      ['--mango-fondo',    '#f4b54a'],
  tinta:      ['--mango-tinta',    '#1d1b1a'],
  papel:      ['--mango-papel',    '#fbf3e4'],
  acento:     ['--mango-acento',   '#b3123f'],
  'acento-2': ['--mango-acento-2', '#9ccf6a'],
};
const DARK = { fondo: '#1f1d1b', tinta: '#f3ece0', papel: '#2d2a27' };
export const GROSOR = { linea: 4.8, fina: 2.8 };   // en unidades de un lienzo de 480 de ancho

// ---------- trazo con temblor ----------
let seed = 7;
const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
/** Fija la semilla del temblor: el mismo valor da siempre el mismo dibujo. */
export const semilla = (s) => { seed = Math.max(1, Math.floor(s)); };

function catmull(pts, cerrado) {
  const P = cerrado ? [pts[pts.length - 1], ...pts, pts[0], pts[1]] : [pts[0], ...pts, pts[pts.length - 1]];
  let d = `M${f(pts[0][0])} ${f(pts[0][1])}`;
  for (let i = 1; i < P.length - 2; i++) {
    const [p0, p1, p2, p3] = [P[i - 1], P[i], P[i + 1], P[i + 2]];
    d += `C${f(p1[0] + (p2[0] - p0[0]) / 6)} ${f(p1[1] + (p2[1] - p0[1]) / 6)} ${f(p2[0] - (p3[0] - p1[0]) / 6)} ${f(p2[1] - (p3[1] - p1[1]) / 6)} ${f(p2[0])} ${f(p2[1])}`;
  }
  return d + (cerrado ? 'Z' : '');
}
/** Camino suave por los puntos de control, remuestreado y con un temblor lento (la mano tiembla despacio, no a saltos). */
export function trazo(pts, { cerrado = false, temblor = 0.8, paso = 14 } = {}) {
  const out = []; const n = pts.length; const segs = cerrado ? n : n - 1;
  for (let i = 0; i < segs; i++) {
    const a = pts[i], b = pts[(i + 1) % n]; const k = Math.max(1, Math.round(Math.hypot(b[0] - a[0], b[1] - a[1]) / paso));
    for (let j = 0; j < k; j++) out.push([a[0] + (b[0] - a[0]) * j / k, a[1] + (b[1] - a[1]) * j / k]);
  }
  if (!cerrado) out.push(pts[n - 1]);
  const ph1 = rnd() * 6.28, ph2 = rnd() * 6.28;
  const q = out.map(([x, y], i) => {
    if (!cerrado && (i === 0 || i === out.length - 1)) return [x, y];   // los extremos no se mueven: las uniones encajan
    const t = (i / out.length) * 6.28; return [x + temblor * Math.sin(t * 2.3 + ph1), y + temblor * Math.sin(t * 3.1 + ph2)];
  });
  return catmull(q, cerrado);
}

/** Puntos de una curva Catmull-Rom evaluada cada «paso» unidades (la línea central del trazo). */
function curva(pts, cerrado, paso = 3.5) {
  const P = cerrado ? [pts[pts.length - 1], ...pts, pts[0], pts[1]] : [pts[0], ...pts, pts[pts.length - 1]];
  const out = [];
  for (let i = 1; i < P.length - 2; i++) {
    const [p0, p1, p2, p3] = [P[i - 1], P[i], P[i + 1], P[i + 2]];
    const n = Math.max(2, Math.ceil(Math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / paso));
    for (let k = 0; k < n; k++) { const t = k / n, t2 = t * t, t3 = t2 * t;
      out.push([0, 1].map((d) => 0.5 * (2 * p1[d] + (-p0[d] + p2[d]) * t + (2 * p0[d] - 5 * p1[d] + 4 * p2[d] - p3[d]) * t2 + (-p0[d] + 3 * p1[d] - 3 * p2[d] + p3[d]) * t3))); }
  }
  out.push(cerrado ? pts[0] : pts[pts.length - 1]);
  return out;
}
/** Trazo orgánico: una cinta rellena cuyo ancho sigue la presión de la mano (entra y sale fino, varía en medio),
 *  con el borde áspero (grano) y los extremos que se pasan un poco. Devuelve el «d» de una forma rellena. */
export function trazoOrganico(pts, { cerrado = false, ancho = 4.2, temblor = 0.8 } = {}) {
  let c = curva(pts, cerrado);
  // un gesto corto tiembla menos: temblor y grano se escalan con la longitud del trazo
  let largo = 0; for (let i = 1; i < c.length; i++) largo += Math.hypot(c[i][0] - c[i - 1][0], c[i][1] - c[i - 1][1]);
  const escala = Math.min(1, largo / 70);
  // temblor lento de la línea central
  const ph1 = rnd() * 6.28, ph2 = rnd() * 6.28, tb = temblor * escala;
  c = c.map(([x, y], i) => { const t = (i / c.length) * 6.28; return [x + tb * Math.sin(t * 2.3 + ph1), y + tb * Math.sin(t * 3.1 + ph2)]; });
  // la mano no cierra exacto: una forma cerrada se solapa al terminar; un trazo abierto se pasa un poco
  const ext = (a, b, l) => { const d = Math.hypot(b[0] - a[0], b[1] - a[1]) || 1; return [b[0] + ((b[0] - a[0]) / d) * l, b[1] + ((b[1] - a[1]) / d) * l]; };
  if (cerrado) c = [...c, ...c.slice(1, 4).map(([x, y]) => [x + 0.8, y + 0.8])];
  else { c = [ext(c[1], c[0], 1 + rnd() * 2.5), ...c, ext(c[c.length - 2], c[c.length - 1], 1 + rnd() * 3)]; }
  const n = c.length, L = [], R = [];
  const acum = [0]; for (let i = 1; i < n; i++) acum.push(acum[i - 1] + Math.hypot(c[i][0] - c[i - 1][0], c[i][1] - c[i - 1][1]));
  const total = acum[n - 1] || 1;
  const fase = rnd() * 6.28, ataque = 5 + rnd() * 3, cola = 7 + rnd() * 4;   // en unidades: la mano afina igual en un trazo corto que en uno largo
  const onda = Math.min(1, total / 60);                                     // los trazos cortos no ondulan su grosor
  for (let i = 0; i < n; i++) {
    const a = c[Math.max(0, i - 1)], b = c[Math.min(n - 1, i + 1)]; const dx = b[0] - a[0], dy = b[1] - a[1]; const d = Math.hypot(dx, dy) || 1;
    const nx = -dy / d, ny = dx / d; const s0 = acum[i];
    // presión: entra y sale fino (salida más larga que la entrada) y ondula despacio a lo largo del trazo
    const entrada = cerrado ? 1 : Math.min(1, s0 / ataque), salida = cerrado ? 1 : Math.min(1, (total - s0) / cola);
    const presion = (0.4 + 0.6 * Math.min(entrada, salida)) * (1 + onda * 0.16 * Math.sin((s0 / 38) * 6.28 + fase));
    const h = (ancho / 2) * presion;
    const grano = () => (rnd() - 0.5) * (0.12 + 0.33 * escala);   // borde áspero
    L.push([c[i][0] + nx * (h + grano()), c[i][1] + ny * (h + grano())]);
    R.push([c[i][0] - nx * (h + grano()), c[i][1] - ny * (h + grano())]);
  }
  const p = [...L, ...R.reverse()];
  return 'M' + p.map(([x, y]) => `${f(x)} ${f(y)}`).join('L') + 'Z';
}

// ---------- geometría ----------
/** Transforma puntos: escala s, rotación rot (grados), espejo horizontal flip, y los lleva a (x, y). */
export function tf(pts, { x = 0, y = 0, s = 1, rot = 0, flip = false } = {}) {
  const c = Math.cos(rad(rot)), si = Math.sin(rad(rot));
  return pts.map(([px, py]) => { const X = (flip ? -px : px) * s, Y = py * s; return [x + X * c - Y * si, y + X * si + Y * c]; });
}
/** Línea de tinta (gruesa o fina). */
export const linea = (pts, o = {}) => `<path class="{c}__trazo" d="${trazoOrganico(pts, { ancho: o.fina ? GROSOR.fina : GROSOR.linea, temblor: o.fina ? 0.4 : 0.8, ...o })}"/>`;
/** Forma rellena de un rol; desplaza = [dx, dy] para el efecto de impresión mal registrada. */
export const relleno = (rol, pts, o = {}) => { const [dx, dy] = o.desplaza || [0, 0];
  return `<path class="{c}__${rol}" d="${trazo(pts.map(([x, y]) => [x + dx, y + dy]), { cerrado: true, temblor: 1, ...o })}"/>`; };

// ---------- piezas ----------
/** Agujero oscuro (pared, suelo, techo) del que sale o al que entra algo. */
export const agujero = ({ x, y, rx, ry }) => relleno('tinta', [[0, -1], [0.7, -0.7], [1, 0], [0.7, 0.7], [0, 1], [-0.7, 0.7], [-1, 0], [-0.7, -0.7]].map(([a, b]) => [x + a * rx, y + b * ry]), { temblor: 1 });

/** Rayitas de «¡ta-dá!» alrededor de (cx, cy), en un arco de «de» a «a» grados. */
export function rayitas({ cx, cy, r, n = 5, de = -150, a = -30, largo = 18 }) {
  return Array.from({ length: n }, (_, i) => { const g = rad(de + ((a - de) * i) / Math.max(1, n - 1)); const l = largo * (i % 2 ? 0.8 : 1);
    return linea([[cx + r * Math.cos(g), cy + r * Math.sin(g)], [cx + (r + l) * Math.cos(g), cy + (r + l) * Math.sin(g)]], { temblor: 0.2 }); }).join('');
}

/** Brazo (manga de papel) desde «desde» hasta la muñeca «hasta». Devuelve { svg, muneca, angulo }. */
export function brazo({ desde, hasta, ancho = 44, curva = 0.12, puno = true }) {
  const [x1, y1] = desde, [x2, y2] = hasta; const L = Math.hypot(x2 - x1, y2 - y1); const ux = (x2 - x1) / L, uy = (y2 - y1) / L; const nx = -uy, ny = ux;
  const h = ancho / 2, mid = [(x1 + x2) / 2 + nx * L * curva, (y1 + y2) / 2 + ny * L * curva];
  const lado = (s, w0, w1) => [[x1 + nx * w0 * s, y1 + ny * w0 * s], [mid[0] + nx * ((w0 + w1) / 2) * s, mid[1] + ny * ((w0 + w1) / 2) * s], [x2 + nx * w1 * s, y2 + ny * w1 * s]];
  const a = lado(-1, h * 1.08, h), b = lado(1, h * 1.08, h);
  const svg = [relleno('papel', [...a, ...b.slice().reverse()], { temblor: 0.5 }), linea(a), linea(b)];
  if (puno) { const p = 0.84; const c = [x1 + (x2 - x1) * p + nx * L * curva * 0.5, y1 + (y2 - y1) * p + ny * L * curva * 0.5];
    svg.push(linea([[c[0] - nx * h * 1.05, c[1] - ny * h * 1.05], [c[0] + nx * h * 1.05, c[1] + ny * h * 1.05]], { temblor: 0.5 })); }
  return { svg: svg.join(''), muneca: hasta, angulo: (Math.atan2(uy, ux) * 180) / Math.PI };
}

// Manos: puntos con la muñeca en (0, 0), mirando a la derecha, muñeca de 44 de ancho (de -22 a 22).
const MANOS = {
  // palma arriba en forma de cuenco: el objeto se apoya en «apoyo»
  cuenco: { contorno: [[0, -22], [14, -24], [26, -32], [34, -34], [40, -26], [36, -14], [48, -6], [78, -4], [100, -12], [112, -24], [120, -26], [124, -18], [118, 0], [100, 18], [70, 28], [34, 28], [0, 22]],
    pliegues: [[[90, 4], [108, -10]], [[78, 14], [100, 2]]], apoyo: [66, -6] },
  // índice extendido, el resto del puño cerrado
  senala: { contorno: [[0, -22], [26, -26], [52, -22], [96, -20], [108, -14], [104, -8], [62, -8], [66, 0], [62, 10], [52, 22], [28, 26], [0, 22]],
    pliegues: [[[50, -8], [56, 4]], [[44, 8], [52, 18]]], apoyo: [108, -14] },
  // mano abierta, dedos hacia delante (saludo, chocar)
  abierta: { contorno: [[0, -22], [20, -30], [30, -44], [40, -50], [44, -44], [38, -30], [60, -34], [96, -34], [102, -28], [96, -22], [64, -20], [100, -16], [106, -10], [100, -4], [66, -6], [96, 2], [100, 8], [94, 12], [62, 10], [84, 18], [86, 24], [78, 26], [40, 26], [0, 22]],
    pliegues: [], apoyo: [100, -30] },
};
/** Mano en la muñeca (x, y), girada «rot» grados (usa el ángulo que devuelve brazo), escala s, espejo flip.
 *  Devuelve { svg, apoyo } (apoyo = dónde se coloca lo que sostiene o señala). */
export function mano({ x, y, rot = 0, s = 1, flip = false, gesto = 'cuenco' }) {
  const g = MANOS[gesto] || MANOS.cuenco; const T = (p) => tf(p, { x, y, s, rot, flip });
  const c = T(g.contorno);
  return { svg: [relleno('papel', c, { temblor: 0.5 }), linea(c, { cerrado: true }), ...g.pliegues.map((p) => linea(T(p), { fina: true }))].join(''), apoyo: T([g.apoyo])[0] };
}

/** Cabeza de perfil mirando a la derecha (flip para la izquierda): cara mínima (ojo de punto, sonrisa, nariz angular).
 *  (x, y) = base del cuello por delante. pelo: corto | largo | barba | ninguno. Devuelve { svg }. */
export function cabeza({ x, y, s = 1, flip = false, pelo = 'corto', cara = 'sonrie' }) {
  const T = (p) => tf(p, { x, y, s, flip });
  const contorno = T([[-24, 0], [-26, -30], [-34, -58], [-32, -84], [-18, -98], [2, -100], [18, -92], [24, -76], [26, -64], [36, -52], [26, -48], [26, -40], [24, -30], [12, -24], [0, -22], [0, 0]]);
  // el relleno baja 10 por debajo del cuello para solaparse con el torso (el temblor no deja huecos)
  const o = [relleno('papel', [...contorno, ...T([[0, 10], [-24, 10]])], { temblor: 0.5 }), linea(contorno)];
  if (pelo === 'corto' || pelo === 'barba') o.push(relleno('tinta', T([[-34, -58], [-34, -82], [-20, -98], [4, -102], [20, -94], [16, -82], [4, -84], [-6, -78], [-14, -66], [-22, -54]]), { temblor: 0.6 }));
  if (pelo === 'largo') o.push(relleno('tinta', T([[-26, -20], [-38, -50], [-36, -82], [-20, -100], [4, -104], [22, -94], [18, -82], [2, -86], [-10, -74], [-16, -52], [-14, -24]]), { temblor: 0.6 }));
  if (pelo === 'barba') o.push(relleno('tinta', T([[-6, -52], [0, -38], [12, -26], [24, -30], [26, -40], [16, -42], [8, -50]]), { temblor: 0.5 }));
  o.push(`<circle class="{c}__punto" cx="${f(T([[14, -68]])[0][0])}" cy="${f(T([[14, -68]])[0][1])}" r="${f(3.4 * s)}"/>`);
  if (cara === 'sonrie') o.push(linea(T([[16, -40], [20, -37], [24, -40]]), { fina: true, temblor: 0.2 }));
  o.push(linea(T([[-6, -40], [-11, -45], [-9, -51], [-3, -50]]), { fina: true, temblor: 0.2 }));   // oreja, bajo el pelo
  return { svg: o.join('') };
}

/** Torso de perfil (hombros y pecho) que sale del lienzo por abajo. (x, y) = base del cuello por delante, como cabeza.
 *  Devuelve { svg, hombro } (hombro = de dónde sale el brazo). */
export function torso({ x, y, s = 1, flip = false, rol = 'papel', alto = 200 }) {
  const T = (p) => tf(p, { x, y, s, flip });
  const espalda = [[-24, 0], [-40, 10], [-62, 26], [-72, 60], [-76, alto]], pecho = [[0, 0], [16, 14], [30, 40], [36, 80], [40, alto]];
  return { svg: [relleno(rol, T([...espalda, ...pecho.slice().reverse()]), { temblor: 0.5 }), linea(T(espalda)), linea(T(pecho))].join(''), hombro: T([[-30, 34]])[0] };
}

// ---------- objetos ----------
export const objeto = {
  /** La cochinilla de Grana: gota con bandas (recortadas al contorno), antenas y patitas; relleno de acento desplazado. */
  grana: ({ cx, base, t = 5.6, rol = 'acento', desplaza = [6, 4] }) => {
    const X = (v) => cx + (v - 12) * t, Y = (v) => base + (v - 22.2) * t;
    const G = [[12, 4.2], [14.6, 7.6], [17.6, 11.4], [19, 15.5], [18, 19.4], [15.6, 21.6], [12, 22.2], [8.4, 21.6], [6, 19.4], [5, 15.5], [6.4, 11.4], [9.4, 7.6]];
    const gota = G.map(([x, y]) => [X(x), Y(y)]);
    const der = G.slice(0, 7); const ancho = (v) => { for (let i = 0; i < der.length - 1; i++) { const [x1, y1] = der[i], [x2, y2] = der[i + 1]; if (v >= y1 && v <= y2) return x1 + ((x2 - x1) * (v - y1)) / (y2 - y1) - 12; } return 0; };
    const banda = (v) => { const w = ancho(v) - 0.6; return linea([[X(12 - w), Y(v)], [X(12), Y(v + 1.1)], [X(12 + w), Y(v)]], { temblor: 0.5 }); };
    const pata = (a, b) => linea([[X(a[0]), Y(a[1])], [X(b[0]), Y(b[1])]], { temblor: 0.3 });
    return [relleno(rol, gota, { desplaza, temblor: 1.4 }), linea([...gota, gota[0]]), ...[12.0, 15.4, 18.8].map(banda),
      pata([10.9, 6.3], [8.3, 2.9]), pata([13.1, 6.3], [15.7, 2.9]), pata([5.4, 13.4], [3.2, 12.4]), pata([5.1, 17.4], [2.9, 18]), pata([18.6, 13.4], [20.8, 12.4]), pata([18.9, 17.4], [21.1, 18])].join('');
  },
};

// ---------- envoltorio ----------
/** Envuelve las piezas: roles → tokens, fondo, accesibilidad y modo oscuro de los valores por defecto. */
export function ilustracion({ id, w = 480, h = 320, titulo, decorativa = false, fondo = true, partes }) {
  const c = `mango-${id}`;
  const cuerpo = (fondo ? [`<rect class="{c}__fondo" width="${w}" height="${h}"/>`] : []).concat(partes).join('\n  ');
  const usados = new Set(['tinta', ...[...cuerpo.matchAll(/\{c\}__([a-z0-9-]+)/g)].map((m) => m[1]).filter((r) => ROLES[r])]);
  const vars = [...usados].map((r) => `--m-${r}:var(${ROLES[r][0]},${ROLES[r][1]})`).join(';');
  const osc = [...usados].filter((r) => DARK[r]).map((r) => `--m-${r}:var(${ROLES[r][0]},${DARK[r]})`).join(';');
  const reglas = [...usados].map((r) => `.${c}__${r}{fill:var(--m-${r})}`).join('')
    + `.${c}__trazo{fill:var(--m-tinta)}`   // los trazos son cintas rellenas (grosor variable), no líneas con stroke
    + `.${c}__punto{fill:var(--m-tinta)}`;
  const css = `.${c}{${vars}}${osc ? `@media (prefers-color-scheme:dark){.${c}{${osc}}}` : ''}${reglas}`;
  const a11y = decorativa ? 'aria-hidden="true"' : `role="img" aria-labelledby="${c}-t"`;
  const tit = decorativa ? '' : `<title id="${c}-t">${titulo}</title>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" class="mango-ilu ${c}" ${a11y}>\n  ${tit}<style>${css}</style>\n  ${cuerpo.replaceAll('{c}', c)}\n</svg>\n`;
}
