# Estelar · paquete de marca (decidido con el usuario el 2026-11-09; rondas en ../ronda-1 a ../ronda-6).
# Símbolo: C1 «urdimbre de 7» (marca) + C3 «estrella de 5» (16–24 px). Color: Caracol, la estrella en color, sobre la manta y la tinta de Xila.
# Letra: combinación 3 (nombre y etiquetas en Big Shoulders Display 800; lema y titulares en Instrument Serif cursiva; texto en Instrument Sans).
# Uso: python3 gen.py <carpeta con BigShouldersDisplay-ExtraBold.ttf e InstrumentSerif-Italic.ttf> && node png.cjs
import os, sys, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
H = os.path.dirname(os.path.abspath(__file__)); FD = sys.argv[1]
src = open(os.path.join(H,'..','ronda-3','gen.py')).read().split('def svg(')[0]
ns = {'__file__': os.path.join(H,'..','ronda-3','gen.py')}; exec(src, ns); tejido, P7, P5, cr = ns['tejido'], ns['P7'], ns['P5'], ns['cr']
MANTA, SUP, TINTA, TINTA2, NOCHE, NOCHE_SUP, CLARO, CLARO2 = '#F6F1E8', '#FFFDF9', '#15171F', '#5B5F6E', '#15171F', '#1E2130', '#F6F1E8', '#A9ADBD'
CAR, CAR_O = '#7B2D8E', '#C98BDB'
def C1(t, f): return tejido(P7, 8, 4, t, f, t)
def C3(t, f): return tejido(P5, 11.2, 4, t, f, t, hilos=False, alto=.74)
def svg(inner, vb='0 0 64 64', label='Estelar'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">{inner}</svg>'
FT = {'nombre': os.path.join(FD,'BigShouldersDisplay-ExtraBold.ttf'), 'lema': os.path.join(FD,'InstrumentSerif-Italic.ttf')}
TT = {k: TTFont(p) for k, p in FT.items()}
def palabra(s, size, x0, y0, k, track=0):
    font = TT[k]; upm = font['head'].unitsPerEm
    hf = hb.Font(hb.Face(hb.Blob.from_file_path(FT[k]))); b = hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf, b, {'kern': True})
    gs = font.getGlyphSet(); order = font.getGlyphOrder(); sc = size/upm; x = x0; dd = ''
    for i, ps in zip(b.glyph_infos, b.glyph_positions):
        pen = SVGPathPen(gs); gs[order[i.codepoint]].draw(TransformPen(pen, (sc, 0, 0, -sc, x, y0))); dd += pen.getCommands(); x += ps.x_advance*sc + track
    return dd, x
def wordmark(oscuro):
    t, a, sub = (CLARO, CAR_O, CLARO2) if oscuro else (TINTA, CAR, TINTA2)
    d1, x1 = palabra('Estelar', 50, 0, 44, 'nombre'); d2, x2 = palabra('Del hilo suelto a la estrella', 19, 1, 70, 'lema')
    w = 84 + max(x1, x2) + 12
    return svg(f'<g transform="scale(1.19)">{C1(t, a)}</g><g transform="translate(86 0)"><path d="{d1}" fill="{t}"/><path d="{d2}" fill="{sub}"/></g>', f'0 0 {w:.0f} 78', 'Estelar · Del hilo suelto a la estrella')
def favicon():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><style>.t{fill:%s}.a{fill:%s}@media(prefers-color-scheme:dark){.t{fill:%s}.a{fill:%s}}</style>' % (TINTA, CAR, CLARO, CAR_O)
            + C3('T', 'A').replace('fill="T"', 'class="t"').replace('fill="A"', 'class="a"').replace('stroke="T"', 'stroke="currentColor"') + '</svg>')
def app(r=0):
    return svg(f'<rect width="512" height="512" rx="{r}" fill="{NOCHE}"/><g transform="translate(64 64) scale(6)">{C1(CLARO, CAR_O)}</g>', '0 0 512 512')
def tarjeta():
    e, _ = palabra('ESTELAR', 30, 96, 214, 'nombre', track=4)
    l1, _ = palabra('Diseña en copo de nieve.', 74, 96, 300, 'lema'); l2, _ = palabra('Publica en estrella.', 74, 96, 380, 'lema')
    s, _ = palabra('Del hilo suelto a la estrella', 34, 96, 460, 'lema')
    return svg(f'<rect width="1200" height="630" fill="{NOCHE}"/><path d="{e}" fill="{CAR_O}"/><path d="{l1}{l2}" fill="{CLARO}"/><path d="{s}" fill="{CLARO2}"/>'
               f'<g transform="translate(760 125) scale(6)">{C1(CLARO, CAR_O)}</g>', '0 0 1200 630', 'Estelar · Diseña en copo de nieve. Publica en estrella.')
F = {'simbolo': svg(C1(TINTA, CAR)), 'simbolo-oscuro': svg(C1(CLARO, CAR_O)), 'simbolo-tinta': svg(C1('currentColor', 'currentColor')),
     'simbolo-16': svg(C3(TINTA, CAR)), 'simbolo-16-oscuro': svg(C3(CLARO, CAR_O)), 'favicon': favicon(),
     'app-icon': app(), 'app-icon-redondeado': app(112), 'wordmark': wordmark(False), 'wordmark-oscuro': wordmark(True), 'tarjeta-redes': tarjeta()}
for n, s in F.items(): open(f'{H}/svg/{n}.svg', 'w').write(s)
tema = {'nombre': 'Estelar', 'fuente': '.fruti/icons/estelar/LEEME.md (decidido 2026-11-09)',
 'concepto': 'Estrella + telar: la estrella de ocho puntas del telar de cintura, tejida con flotes (tramos de trama sobre la urdimbre). Grana es el tinte, Estelar el telar, Xila el bordado.',
 'color': {'manta': {'claro': MANTA, 'oscuro': NOCHE, 'uso': 'fondo (compartido con Xila)'}, 'superficie': {'claro': SUP, 'oscuro': NOCHE_SUP},
           'tinta': {'claro': TINTA, 'oscuro': CLARO, 'uso': f'texto, urdimbre y centro del símbolo; {cr(TINTA, MANTA):.1f}:1'},
           'tinta2': {'claro': TINTA2, 'oscuro': CLARO2, 'uso': f'texto secundario; {cr(TINTA2, MANTA):.1f}:1 · {cr(CLARO2, NOCHE):.1f}:1'},
           'caracol': {'claro': CAR, 'oscuro': CAR_O, 'uso': f'la estrella (flotes), acento y etiquetas; {cr(CAR, MANTA):.1f}:1 · {cr(CAR_O, NOCHE):.1f}:1'}},
 'tipografia': {'nombre': {'familia': 'Big Shoulders Display', 'peso': 800, 'uso': 'el nombre Estelar y etiquetas cortas en mayúsculas'},
                'lema': {'familia': 'Instrument Serif', 'estilo': 'italic', 'uso': 'lema y titulares de portada'},
                'texto': {'familia': 'Instrument Sans', 'peso': 400, 'uso': 'texto corrido e interfaz (la de Xila)'}},
 'simbolo': {'marca': 'C1: estrella de 7 × 7 con urdimbre; desde 32 px', 'chico': 'C3: estrella de 5 × 5 sin urdimbre; 16 a 24 px', 'centro': 'el hecho del modelo; siempre en tinta'},
 'reglas': ['La estrella va en caracol; la urdimbre y el centro, en tinta.', 'Por debajo de 32 px se usa la estrella de 5 (simbolo-16).',
            'Caracol claro sobre manta; caracol oscuro (#C98BDB) sobre fondo oscuro. Nunca al revés.',
            'La metáfora del telar va en lo que se lee una vez (nombre, portada, README); nunca en botones ni mensajes de error.',
            'Nunca «IA», «mágico» ni «inteligente» junto a la marca.']}
json.dump(tema, open(f'{H}/tema.json','w'), indent=2, ensure_ascii=False); print('ok', {k: v['uso'] for k, v in tema['color'].items() if 'uso' in v})
