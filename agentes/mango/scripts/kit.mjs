// Mango · kit de piezas en estilo línea de rotulador (especificación «Vector Illustrator Skill», Fase 1).
// Trazo de peso estable con irregularidades sutiles y deliberadas (sin textura de lápiz), rellenos planos
// (a veces desplazados del contorno, como una impresión mal registrada), fondo transparente por defecto. El color nunca es fijo: cada forma usa una clase de
// rol (mango-<id>__<rol>) y el <style> de la ilustración traduce los roles a tokens del proyecto.
// Uso: import { semilla, linea, relleno, brazo, mano, cabeza, torso, agujero, rayitas, objeto, ilustracion } from './kit.mjs'

const f = (v) => Math.round(v * 10) / 10;
const rad = (g) => (g * Math.PI) / 180;

// Roles de color: nombre → [token del proyecto, valor por defecto]. DARK: valores por defecto en modo oscuro.
export const ROLES = {
  fondo:      ['--mango-fondo',    '#FFFDF5'],   // superficie de la hoja (solo si la ilustración pide fondo)
  tinta:      ['--mango-tinta',    '#111111'],
  papel:      ['--mango-papel',    '#FFFDF5'],
  acento:     ['--mango-acento',   '#F8BC32'],   // máx. 3 acentos simultáneos
  'acento-2': ['--mango-acento-2', '#9ccf6a'],
};
const DARK = { fondo: '#1f1d1b', tinta: '#f3ece0', papel: '#2d2a27' };
export const GROSOR = { linea: 4.4, fina: 2.6 };
let escalaTrazo = 1;   // figura() la ajusta a su tamaño: una figura pequeña lleva línea más fina   // en unidades de un lienzo de 480 de ancho

// ---------- trazo con temblor ----------
let seed = 7;
const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
/** Fija la semilla del temblor: el mismo valor da siempre el mismo dibujo. */
export const semilla = (s) => { seed = Math.max(1, Math.floor(s)); };

function catmull(pts, cerrado) {
  const P = cerrado ? [pts[pts.length - 1], ...pts, pts[0], pts[1]] : [pts[0], ...pts, pts[pts.length - 1]];
  // curvas en coordenadas relativas (c): mismo dibujo, menos bytes
  const n = (v) => { const t = f(v); return (t >= 0 ? ' ' : '') + t; };
  let d = `M${f(pts[0][0])} ${f(pts[0][1])}`;
  for (let i = 1; i < P.length - 2; i++) {
    const [p0, p1, p2, p3] = [P[i - 1], P[i], P[i + 1], P[i + 2]];
    const o = [f(p1[0]), f(p1[1])];
    d += 'c' + [p1[0] + (p2[0] - p0[0]) / 6 - o[0], p1[1] + (p2[1] - p0[1]) / 6 - o[1], p2[0] - (p3[0] - p1[0]) / 6 - o[0], p2[1] - (p3[1] - p1[1]) / 6 - o[1], f(p2[0]) - o[0], f(p2[1]) - o[1]].map(n).join('').trimStart();
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
function curva(pts, cerrado, paso = 5.5) {
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
/** Trazo orgánico: una cinta rellena de peso estable que afina un poco en los extremos, con un temblor lento
 *  de la línea central y los extremos que se pasan apenas. Devuelve el «d» de una forma rellena. */
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
  if (cerrado) c = [...c, ...c.slice(1, 3).map(([x, y]) => [x + 0.5, y + 0.5])];
  else { c = [ext(c[1], c[0], 0.5 + rnd()), ...c, ext(c[c.length - 2], c[c.length - 1], 0.5 + rnd() * 1.2)]; }
  const n = c.length, L = [], R = [];
  const acum = [0]; for (let i = 1; i < n; i++) acum.push(acum[i - 1] + Math.hypot(c[i][0] - c[i - 1][0], c[i][1] - c[i - 1][1]));
  const total = acum[n - 1] || 1;
  const fase = rnd() * 6.28, ataque = 5 + rnd() * 3, cola = 7 + rnd() * 4;   // en unidades: la mano afina igual en un trazo corto que en uno largo
  const onda = Math.min(1, total / 60);                                     // los trazos cortos no ondulan su grosor
  for (let i = 0; i < n; i++) {
    const a = c[Math.max(0, i - 1)], b = c[Math.min(n - 1, i + 1)]; const dx = b[0] - a[0], dy = b[1] - a[1]; const d = Math.hypot(dx, dy) || 1;
    const nx = -dy / d, ny = dx / d; const s0 = acum[i];
    // peso estable: solo afina un poco al entrar y salir, y apenas ondula (±5 %) a lo largo del trazo
    const entrada = cerrado ? 1 : Math.min(1, s0 / ataque), salida = cerrado ? 1 : Math.min(1, (total - s0) / cola);
    const presion = (0.42 + 0.58 * Math.min(entrada, salida)) * (1 + onda * 0.05 * Math.sin((s0 / 45) * 6.28 + fase));
    const h = (ancho / 2) * presion;
    const grano = () => (rnd() - 0.5) * 0.06;   // borde limpio: sin textura de lápiz
    L.push([c[i][0] + nx * (h + grano()), c[i][1] + ny * (h + grano())]);
    R.push([c[i][0] - nx * (h + grano()), c[i][1] - ny * (h + grano())]);
  }
  // coordenadas relativas redondeadas: el mismo dibujo en bastantes menos bytes
  const p = [...L, ...R.reverse()].map(([x, y]) => [f(x), f(y)]);
  let d = `M${p[0][0]} ${p[0][1]}l`;
  for (let i = 1; i < p.length; i++) { const dx = f(p[i][0] - p[i - 1][0]), dy = f(p[i][1] - p[i - 1][1]); d += `${i > 1 && dx >= 0 ? ' ' : ''}${dx}${dy >= 0 ? ' ' : ''}${dy}`; }
  return d + 'Z';
}

// ---------- geometría ----------
/** Transforma puntos: escala s, rotación rot (grados), espejo horizontal flip, y los lleva a (x, y). */
export function tf(pts, { x = 0, y = 0, s = 1, rot = 0, flip = false } = {}) {
  const c = Math.cos(rad(rot)), si = Math.sin(rad(rot));
  return pts.map(([px, py]) => { const X = (flip ? -px : px) * s, Y = py * s; return [x + X * c - Y * si, y + X * si + Y * c]; });
}
/** Línea de tinta (gruesa o fina). */
export const linea = (pts, o = {}) => `<path class="{c}__trazo" d="${trazoOrganico(pts, { ancho: (o.fina ? GROSOR.fina : GROSOR.linea) * escalaTrazo, temblor: (o.fina ? 0.3 : 0.6) * escalaTrazo, ...o })}"/>`;
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
  // manopla: la mano simple del doodle para figuras enteras (palma + pulgar)
  manopla: { contorno: [[0, -20], [22, -22], [30, -36], [40, -38], [44, -26], [60, -20], [74, -8], [72, 8], [56, 18], [24, 20], [0, 20]], pliegues: [], apoyo: [52, -14] },
  // mano abierta, dedos hacia delante (saludo, chocar)
  abierta: { contorno: [[0, -22], [20, -30], [30, -44], [40, -50], [44, -44], [38, -30], [60, -34], [96, -34], [102, -28], [96, -22], [64, -20], [100, -16], [106, -10], [100, -4], [66, -6], [96, 2], [100, 8], [94, 12], [62, 10], [84, 18], [86, 24], [78, 26], [40, 26], [0, 22]],
    pliegues: [], apoyo: [100, -30] },
  // pulgar arriba: puño cerrado con el pulgar hacia arriba (thumbs-up)
  pulgar: { contorno: [[0, -20], [28, -24], [32, -42], [38, -58], [46, -60], [51, -52], [48, -28], [64, -24], [72, -10], [70, 8], [60, 20], [24, 22], [0, 20]],
    pliegues: [[[50, -6], [64, -6]], [[48, 7], [62, 7]]], apoyo: [44, -60] },
};
/** Mano en la muñeca (x, y), girada «rot» grados (usa el ángulo que devuelve brazo), escala s, espejo flip.
 *  Devuelve { svg, apoyo } (apoyo = dónde se coloca lo que sostiene o señala). */
export function mano({ x, y, rot = 0, s = 1, flip = false, gesto = 'cuenco' }) {
  const g = MANOS[gesto] || MANOS.cuenco; const T = (p) => tf(p, { x, y, s, rot, flip });
  const c = T(g.contorno);
  return { svg: [relleno('papel', c, { temblor: 0.5 }), linea(c, { cerrado: true }), ...g.pliegues.map((p) => linea(T(p), { fina: true }))].join(''), apoyo: T([g.apoyo])[0] };
}

// ---------- rostro (ADN facial de la hoja) ----------
// Cabeza 3/4 mirando a la derecha, en unidades de cabeza: alto 100, origen en la barbilla (0, 0), coronilla en y = -100.
// Firma: nariz lineal angular + oreja simplificada + cabello sólido; ojos con marcas simples y boca con una curva breve.
// Variantes de cara a–d: forma del cráneo y de la mandíbula, tipo de ojo y largo de nariz (población coherente, no el mismo personaje).
export const CARAS = {
  a: { ancho: 1,    alto: 1,    mandibula: 1,    ojo: 'punto', nariz: 1 },
  b: { ancho: 0.92, alto: 1.07, mandibula: 0.94, ojo: 'raya',  nariz: 1.08 },
  c: { ancho: 1.08, alto: 0.97, mandibula: 1.04, ojo: 'punto', nariz: 1.18 },
  d: { ancho: 1,    alto: 1.02, mandibula: 1.16, ojo: 'punto', nariz: 0.95, cejas: true },
};
const CRANEO = [[-2, -100], [20, -96], [33, -82], [37, -62], [37, -44], [32, -24], [22, -8], [8, 0], [-8, -2], [-22, -14], [-32, -34], [-38, -58], [-34, -82], [-20, -96]];
// Cabello: masas negras sólidas. «frente» va sobre la cabeza; «atras» (si hay) va detrás del cuello y del cuerpo.
const GORRA = [[-39, -54], [-41, -80], [-28, -98], [-4, -107], [20, -103], [34, -90], [35, -78], [22, -83], [6, -82], [-8, -76], [-18, -66], [-24, -54]];
const rizos = () => { const o = []; for (let i = 0; i <= 13; i++) { const g = rad(-18 - i * 13.5), r = 47 + (i % 2 ? 6 : 0); o.push([-2 + r * Math.cos(g), -62 + r * Math.sin(g)]); }
  return [...o, [-26, -50], [-18, -66], [-4, -76], [12, -81], [28, -80]]; };
const MELENA = [[34, -72], [38, -90], [24, -105], [-2, -109], [-28, -99], [-43, -76], [-45, -44], [-41, -14], [-30, -8], [-22, -12], [-20, -36], [-14, -56], [-2, -70], [14, -75], [26, -70]];
export const PEINADOS = {
  'short-wave': { frente: [[-39, -52], [-42, -80], [-30, -101], [-6, -113], [18, -111], [35, -101], [41, -86], [34, -77], [26, -87], [17, -78], [7, -85], [-7, -76], [-18, -66], [-25, -54]] },
  crop:   { frente: GORRA },
  curls:  { frente: rizos() },
  bob:    { frente: MELENA },
  long:   { frente: [[34, -72], [38, -90], [24, -105], [-2, -109], [-28, -99], [-43, -76], [-45, -42], [-32, -32], [-22, -42], [-14, -58], [-2, -70], [14, -75], [26, -70]],
            atras: [[-30, -82], [-50, -60], [-52, -10], [-48, 46], [-18, 52], [-6, 34], [-12, 0]] },
  bun:    { frente: GORRA, extra: [[-22, -96], [-38, -100], [-42, -116], [-30, -128], [-12, -124], [-8, -108]] },
  ponytail: { frente: GORRA, extra: [[-34, -82], [-50, -88], [-62, -74], [-64, -44], [-56, -18], [-50, -38], [-48, -62], [-36, -64]] },
  ninguno: { frente: null },
};
// Expresiones: ojo, cejas [cerca, lejos] ({ dy: subir < 0, t: extremo interior abajo > 0 }), boca y giro de cabeza (grados, + = hacia delante/abajo).
// La emoción se lee primero en el giro de cabeza y la postura; la cara solo la confirma.
export const EXPRESIONES = {
  neutral:   { ojo: 'base',    cejas: null,                                    boca: 'neutra',   giro: 0 },
  happy:     { ojo: 'base',    cejas: [{ dy: -2, t: -0.5 }, { dy: -2, t: -0.5 }], boca: 'sonrisa',  giro: -3 },
  focused:   { ojo: 'base',    cejas: [{ dy: 3, t: 2 }, { dy: 3, t: 2 }],      boca: 'plana',    giro: 7 },
  curious:   { ojo: 'base',    cejas: [{ dy: -5, t: -1 }, { dy: 0, t: 0.5 }],   boca: 'neutra',   giro: 9 },
  surprised: { ojo: 'grande',  cejas: [{ dy: -7, t: 0 }, { dy: -7, t: 0 }],     boca: 'o',        giro: -6 },
  confused:  { ojo: 'base',    cejas: [{ dy: -5, t: -1.5 }, { dy: 2, t: 2 }],   boca: 'ondulada', giro: -9 },
  concerned: { ojo: 'base',    cejas: [{ dy: -2, t: -2.5 }, { dy: -2, t: -2.5 }], boca: 'triste', giro: 5 },
  relieved:  { ojo: 'cerrado', cejas: [{ dy: -3, t: -1.5 }, { dy: -3, t: -1.5 }], boca: 'sonrisa', giro: -4 },
  proud:     { ojo: 'base',    cejas: [{ dy: -1, t: 0.5 }, { dy: -1, t: 0.5 }],  boca: 'ladeada',  giro: -11 },
  excited:   { ojo: 'feliz',   cejas: [{ dy: -6, t: 0 }, { dy: -6, t: 0 }],     boca: 'grande',   giro: -5 },
};
const BOCAS = {
  neutra: [[12, -21], [18, -20], [24, -21]], sonrisa: [[10, -24], [17, -18], [25, -24]], plana: [[13, -21], [23, -21]],
  ondulada: [[10, -21], [14, -23], [18, -20], [22, -22], [26, -20]], triste: [[11, -18], [18, -22], [25, -18]], ladeada: [[11, -21], [19, -20], [26, -25]],
};
/** Cabeza 3/4 con cuello. (x, y) = barbilla; s = alto de la cabeza / 100. cara: a–d (CARAS); pelo: PEINADOS; expresion: EXPRESIONES.
 *  Devuelve { atras, cuello, svg }: el pelo de detrás, el cuello (va detrás del torso) y la cabeza (va delante). */
export function cabeza({ x, y, s = 1, flip = false, rot = 0, cara = 'a', pelo = 'crop', expresion = 'neutral', cuelloLargo = 30 }) {
  const V = CARAS[cara] || CARAS.a, E = EXPRESIONES[expresion] || EXPRESIONES.neutral, P = PEINADOS[pelo] || PEINADOS.crop;
  const T = (p) => tf(p, { x, y, s, flip, rot: rot + (E.giro || 0) * (flip ? -1 : 1) });
  const forma = (p) => p.map(([a, b]) => [a * V.ancho * (b > -30 ? V.mandibula : 1), b * V.alto]);   // la mandíbula ensancha solo la parte baja
  const pt = (a, b) => T(forma([[a, b]]))[0];
  const craneo = T(forma(CRANEO));
  const cuelloPts = T([[-16, -22], [-15, cuelloLargo], [8, cuelloLargo], [7, -12]]);
  const cuello = relleno('papel', cuelloPts, { temblor: 0.3 }) + linea([cuelloPts[0], cuelloPts[1]]) + linea([cuelloPts[3], cuelloPts[2]]);
  const atras = P.atras ? relleno('tinta', T(forma(P.atras)), { temblor: 0.5 }) : '';
  const o = [relleno('papel', craneo, { temblor: 0.4 }), linea(craneo, { cerrado: true })];
  o.push(linea(T(forma([[-14, -56], [-24, -60], [-28, -48], [-22, -38], [-14, -38]])), { fina: true }), linea(T(forma([[-20, -52], [-22, -46]])), { fina: true, temblor: 0.1 }));   // oreja
  if (P.frente) o.push(relleno('tinta', T(forma(P.frente)), { temblor: 0.5 }));
  if (P.extra) o.push(relleno('tinta', T(forma(P.extra)), { temblor: 0.5 }));
  // ojos: cerca (6, -55) y lejos (31, -57), algo más pequeño; la nariz baja entre los dos
  const ojos = [[6, -55, 1], [31, -57, 0.85]];
  for (const [ex, ey, k] of ojos) {
    const tipo = E.ojo === 'base' ? V.ojo : E.ojo;
    const c = pt(ex, ey);
    if (tipo === 'punto' || tipo === 'grande') o.push(`<circle class="{c}__punto" cx="${f(c[0])}" cy="${f(c[1])}" r="${f((tipo === 'grande' ? 4.6 : 3.4) * k * s)}"/>`);
    else if (tipo === 'raya') o.push(linea(T(forma([[ex, ey - 4.5 * k], [ex + 0.4, ey + 3.5 * k]])), { fina: true, temblor: 0 }));
    else if (tipo === 'feliz') o.push(linea(T(forma([[ex - 5 * k, ey + 2], [ex, ey - 3], [ex + 5 * k, ey + 2]])), { fina: true, temblor: 0 }));
    else if (tipo === 'cerrado') o.push(linea(T(forma([[ex - 5 * k, ey - 1], [ex, ey + 3], [ex + 5 * k, ey - 1]])), { fina: true, temblor: 0 }));
  }
  const cejas = E.cejas || (V.cejas ? [{ dy: 0, t: 0.5 }, { dy: 0, t: 0.5 }] : null);
  if (cejas) cejas.forEach((cj, i) => { const [ex, ey, k] = ojos[i]; const by = ey - 11 + cj.dy, w = 5.5 * k;
    o.push(linea(T(forma(i === 0 ? [[ex - w, by - cj.t], [ex + w, by + cj.t]] : [[ex - w, by + cj.t], [ex + w, by - cj.t]])), { fina: true, temblor: 0 })); });
  // nariz lineal angular: baja desde el entrecejo hacia delante y vuelve en ángulo (sobresale apenas del contorno)
  const n = V.nariz;
  o.push(linea(T(forma([[25, -50], [25 + 13 * n, -50 + 15 * n], [29, -50 + 18 * n]])), { fina: true, temblor: 0.1 }));
  if (E.boca === 'grande') o.push(relleno('tinta', T(forma([[9, -26], [27, -26], [24, -18], [17, -13], [11, -18]])), { temblor: 0.2 }));
  else if (E.boca === 'o') o.push(relleno('tinta', T(forma([[18, -25], [21.5, -21], [18, -16], [14.5, -21]])), { temblor: 0.1 }));
  else o.push(linea(T(forma(BOCAS[E.boca] || BOCAS.neutra)), { fina: true, temblor: 0 }));
  return { atras, cuello, svg: o.join('') };
}

/** Cabeza de perfil (estilo anterior a la especificación; se conserva para las escenas existentes).
 *  (x, y) = base del cuello por delante. pelo: corto | largo | barba | ninguno. Devuelve { svg }. */
export function cabezaPerfil({ x, y, s = 1, flip = false, rot = 0, pelo = 'corto', cara = 'sonrie' }) {
  const T = (p) => tf(p, { x, y, s, flip, rot });
  const contorno = T([[-24, 0], [-26, -30], [-34, -58], [-32, -84], [-18, -98], [2, -100], [18, -92], [24, -76], [26, -64], [36, -52], [26, -48], [26, -40], [24, -30], [12, -24], [0, -22], [0, 0]]);
  const o = [relleno('papel', [...contorno, ...T([[0, 10], [-24, 10]])], { temblor: 0.5 }), linea(contorno)];
  if (pelo === 'corto' || pelo === 'barba') o.push(relleno('tinta', T([[-34, -58], [-34, -82], [-20, -98], [4, -102], [20, -94], [16, -82], [4, -84], [-6, -78], [-14, -66], [-22, -54]]), { temblor: 0.6 }));
  if (pelo === 'largo') o.push(relleno('tinta', T([[-26, -20], [-38, -50], [-36, -82], [-20, -100], [4, -104], [22, -94], [18, -82], [2, -86], [-10, -74], [-16, -52], [-14, -24]]), { temblor: 0.6 }));
  if (pelo === 'barba') o.push(relleno('tinta', T([[-6, -52], [0, -38], [12, -26], [24, -30], [26, -40], [16, -42], [8, -50]]), { temblor: 0.5 }));
  o.push(`<circle class="{c}__punto" cx="${f(T([[14, -68]])[0][0])}" cy="${f(T([[14, -68]])[0][1])}" r="${f(3.4 * s)}"/>`);
  if (cara === 'sonrie') o.push(linea(T([[16, -40], [20, -37], [24, -40]]), { fina: true, temblor: 0.2 }));
  o.push(linea(T([[-6, -40], [-11, -45], [-9, -51], [-3, -50]]), { fina: true, temblor: 0.2 }));
  return { svg: o.join('') };
}

/** Torso de perfil (hombros y pecho) que sale del lienzo por abajo. (x, y) = base del cuello por delante, como cabezaPerfil.
 *  Devuelve { svg, hombro } (hombro = de dónde sale el brazo). */
export function torso({ x, y, s = 1, flip = false, rol = 'papel', alto = 200 }) {
  const T = (p) => tf(p, { x, y, s, flip });
  const espalda = [[-24, 0], [-40, 10], [-62, 26], [-72, 60], [-76, alto]], pecho = [[0, 0], [16, 14], [30, 40], [36, 80], [40, alto]];
  return { svg: [relleno(rol, T([...espalda, ...pecho.slice().reverse()]), { temblor: 0.5 }), linea(T(espalda)), linea(T(pecho))].join(''), hombro: T([[-30, 34]])[0] };
}

// ---------- figura humana: canon de la hoja + esqueleto + carne ----------
// Canon en cabezas (H = alto de la cabeza). head_to_torso = 1 / torso ≈ 0.65 (rango 0.55–0.75); hombros compactos;
// extremidades alargadas y suaves; ~5,6 cabezas de alto. Anatomía caricaturizada pero comprensible.
export const CANON = {
  cuello: 0.26, torso: 1.55, hombroAncho: 0.33, hombroBajo: 0.19, caderaAncho: 0.22,
  brazo: 1.05, antebrazo: 0.95, mano: 0.62, muslo: 1.45, pierna: 1.4, pie: 0.66,
  grosor: { hombro: 0.36, codo: 0.28, muneca: 0.22, cadera: 0.48, rodilla: 0.34, tobillo: 0.22 },
  // contorno del torso 3/4 (x adelante, y arriba = negativo), en cabezas, de la cadera a los hombros
  torsoForma: [[-0.46, 0.12], [-0.4, -0.55], [-0.5, -1.12], [-0.47, -1.43], [-0.28, -1.55], [0.28, -1.55], [0.45, -1.42], [0.52, -1.1], [0.4, -0.55], [0.46, 0.12], [0, 0.2]],
  enfasis: { neutral: 1, comunicativo: 1.25 },   // manos: 1.0 neutras, 1.15–1.35 cuando hacen la acción importante
};
export const COMPLEXION = { slim: 0.88, average: 1, broad: 1.16 };
// Poses: ángulos en grados con la figura mirando a la derecha (0 = adelante, 90 = abajo, -90 = arriba).
// brazo: [hombro→codo, codo→muñeca]; pierna: [cadera→rodilla, rodilla→tobillo]. cerca = el lado que ve el espectador.
export const POSES = {
  'de-pie':   { inclina: 0,  cabeza: 0,  brazoCerca: [103, 94],  brazoLejos: [78, 82],   piernaCerca: [92, 90],  piernaLejos: [88, 90] },
  'camina':   { inclina: 4,  cabeza: 0,  brazoCerca: [66, 50],   brazoLejos: [114, 100], piernaCerca: [68, 98],  piernaLejos: [112, 82] },
  'senala':   { inclina: 2,  cabeza: -4, brazoCerca: [-6, -12],  brazoLejos: [94, 88],   piernaCerca: [94, 90],  piernaLejos: [86, 90] },
  'sostiene': { inclina: 0,  cabeza: 6,  brazoCerca: [80, -2],   brazoLejos: [76, -6],   piernaCerca: [92, 90],  piernaLejos: [88, 90] },
  'sentado':  { inclina: -6, cabeza: 0,  brazoCerca: [76, 14],   brazoLejos: [84, 20],   piernaCerca: [-4, 92],  piernaLejos: [4, 88] },
  'pulgar':   { inclina: -2, cabeza: -4, brazoCerca: [70, -42],  brazoLejos: [96, 88],   piernaCerca: [92, 90],  piernaLejos: [86, 90] },
};
const gesto0 = { cerca: 'manopla', lejos: 'manopla' };
/** Tubo que se adelgaza a lo largo de una cadena de articulaciones: relleno + dos contornos orgánicos abiertos
 *  (los extremos quedan ocultos bajo el torso y la mano/pie, así no aparecen costuras). */
function tubo(js, ws, rol) {
  const L = [], R = [];
  for (let i = 0; i < js.length; i++) {
    const a = js[Math.max(0, i - 1)], b = js[Math.min(js.length - 1, i + 1)];
    const dx = b[0] - a[0], dy = b[1] - a[1], d = Math.hypot(dx, dy) || 1, nx = -dy / d, ny = dx / d;
    L.push([js[i][0] + nx * ws[i] / 2, js[i][1] + ny * ws[i] / 2]); R.push([js[i][0] - nx * ws[i] / 2, js[i][1] - ny * ws[i] / 2]);
  }
  return relleno(rol, [...L, ...R.slice().reverse()], { temblor: 0.4 }) + linea(L) + linea(R);
}
const ir = (p, len, ang, dir) => [p[0] + dir * len * Math.cos(rad(ang)), p[1] + len * Math.sin(rad(ang))];
/** Figura humana 3/4 (dir 1 mira a la derecha, -1 a la izquierda). (x, y) = suelo bajo la cadera. H = alto de cabeza.
 *  pose: nombre de POSES o un objeto con sus ángulos. cara/pelo/expresion: como cabeza(). complexion: slim | average | broad.
 *  enfasis: escala de las manos (CANON.enfasis). Devuelve { svg, manoCerca, manoLejos } (puntos de apoyo de las manos). */
export function figura({ x, y, H = 40, dir = 1, pose = 'de-pie', cara = 'a', pelo = 'crop', expresion = 'neutral', complexion = 'average',
  camisa = 'papel', pantalon = 'papel', zapato = 'tinta', gestos = gesto0, enfasis = 1 }) {
  const antes = escalaTrazo; escalaTrazo = Math.min(1, H / 54);   // la línea escala con la figura
  const P = typeof pose === 'string' ? POSES[pose] : pose; const C = CANON, g = C.grosor, k = COMPLEXION[complexion] || 1;
  const sentado = P === POSES.sentado || pose === 'sentado';
  const altoPierna = (C.muslo + C.pierna) * H * 0.98;
  const cadera = [x, sentado ? y - C.pierna * H * 1.02 : y - altoPierna];
  const inc = (px, py) => { const a = rad(P.inclina); return [cadera[0] + dir * (px * Math.cos(a) - py * Math.sin(a)), cadera[1] + px * Math.sin(a) + py * Math.cos(a)]; };
  const t = C.torso * H;
  const torsoPts = C.torsoForma.map(([a, b]) => inc(a * H * k, b * H));
  // 3/4 mirando a la derecha: el hombro cercano al espectador queda atrás (izquierda), el lejano asoma por delante
  const hombroC = inc(-C.hombroAncho * H * k, -t + C.hombroBajo * H), hombroL = inc(C.hombroAncho * H * k * 0.8, -t + C.hombroBajo * H);
  const caderaC = inc(-C.caderaAncho * H * k, 0), caderaL = inc(C.caderaAncho * H * k, 0);
  const cuelloBase = inc(0.02 * H, -t + 0.1 * H);
  const brazo = (hombro, ang, gesto) => { const e = ir(hombro, C.brazo * H, ang[0], dir), w = ir(e, C.antebrazo * H, ang[1], dir);
    const largo = Math.max(...MANOS[gesto].contorno.map((p) => p[0]));
    const m = mano({ x: w[0], y: w[1], rot: dir === 1 ? ang[1] : -ang[1], flip: dir === -1, s: (C.mano * H * enfasis) / largo, gesto });
    return { svg: tubo([hombro, e, w], [g.hombro * H * k, g.codo * H * k, g.muneca * H * k], camisa) + m.svg, apoyo: m.apoyo }; };
  const pierna = (cad, ang) => { const kn = ir(cad, C.muslo * H, ang[0], dir), a = ir(kn, C.pierna * H, ang[1], dir);
    const pl = C.pie * H, ph = 0.24 * H;
    const pie = [[-0.25 * pl, -ph * 0.6], [0.35 * pl, -ph * 0.7], [0.85 * pl, -ph * 0.35], [1.0 * pl, 0], [0.9 * pl, ph * 0.3], [-0.3 * pl, ph * 0.3]].map(([px, py]) => [a[0] + dir * px, a[1] + py]);
    return tubo([cad, kn, a], [g.cadera * H * k, g.rodilla * H * k, g.tobillo * H * k], pantalon) + relleno(zapato, pie, { temblor: 0.3 }) + linea(pie, { cerrado: true }); };
  const gL = gestos.lejos || 'manopla', gC = gestos.cerca || 'manopla';
  const bL = brazo(hombroL, P.brazoLejos, gL), bC = brazo(hombroC, P.brazoCerca, gC);
  const torsoSvg = relleno(camisa, torsoPts, { temblor: 0.4 }) + linea(torsoPts, { cerrado: true });
  const s = H / 100, cuelloLargo = 30;
  const cab = cabeza({ x: cuelloBase[0] + dir * 4 * s, y: cuelloBase[1] - (C.cuello * H + 10 * s), s, flip: dir === -1, rot: ((P.cabeza || 0) + P.inclina) * dir, cara, pelo, expresion, cuelloLargo: C.cuello * 100 + 14 });
  // orden: pelo de detrás, brazo y pierna lejanos, pierna cercana, cuello, torso, cabeza, brazo cercano
  const svg = `<g class="{c}__persona">${cab.atras}${bL.svg}${pierna(caderaL, P.piernaLejos)}${pierna(caderaC, P.piernaCerca)}${cab.cuello}${torsoSvg}${cab.svg}${bC.svg}</g>`;
  escalaTrazo = antes;
  return { svg, manoCerca: bC.apoyo, manoLejos: bL.apoyo };
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
export function ilustracion({ id, w = 480, h = 320, titulo, decorativa = false, fondo = false, partes }) {
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
