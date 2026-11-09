# Xila · paquete de marca del rediseño (decidido con el usuario el 2026-11-09; rondas en ../rediseno-r1 a ../rediseno-r8).
# Símbolo: la x bordada en el rombo del huipil, con un dibujo por tamaño (grande ≥64, mediano 32–48, chico 20–28, favicon 16).
# Nombre: «xila» en punto de cruz, el punto de la i en añil claro. Color: Añil. Letra: Familjen Grotesk (primaria) + Instrument Sans (secundaria).
# Uso: python3 gen.py <carpeta con FamiljenGrotesk-SemiBold.ttf> && node png.cjs
import os, sys, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
H = os.path.dirname(os.path.abspath(__file__)); FD = sys.argv[1]
src = open(os.path.join(H,'..','rediseno-r5','gen.py')).read().split('PAL = [')[0]
ns = {'__file__': os.path.join(H,'..','rediseno-r5','gen.py')}; exec(src, ns)
niveles, cr, GL, x = ns['niveles'], ns['cr'], ns['GL'], ns['x']
AN, AN2, AN3, AN4, MANTA, TXT2 = '#16255C', '#2F4FA8', '#7FA0E0', '#C9D6F2', '#F4F1EA', '#4A5274'
OSC = dict(fondo=AN, x=MANTA, rombo=AN3, centro=AN3)                 # emblema principal: añil
CLA = dict(fondo=MANTA, x=AN, rombo=AN2, centro=AN2, borde='#DCD6CA')   # alternativa sobre fondos oscuros o de color
NOMBRES = ['grande', 'mediano', 'chico', 'favicon']
_niv = niveles
def niveles(P):  # el favicon lleva un anillo del color del fondo alrededor del punto, para que el dato se separe de la X
    lv = _niv(P); F_, X_, C_ = P['fondo'], P['x'], P['centro']; b = P.get('borde')
    tile = f'<rect x=".75" y=".75" width="62.5" height="62.5" rx="12" fill="{F_}"' + (f' stroke="{b}" stroke-width="1.5"/>' if b else '/>')
    lv[3] = tile + x(32, 32, 34, X_, 11) + f'<circle cx="32" cy="32" r="12" fill="{F_}"/><circle cx="32" cy="32" r="8.5" fill="{C_}"/>'
    return lv
def svg(inner, vb='0 0 64 64', label='xila'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">{inner}</svg>'
def bordado(h, col, dot):
    g = h/7; s = ''; ox = 0
    for ch in 'xila':
        rows = GL[ch]; cols = [j for row in rows for j, c in enumerate(row) if c in 'Xo']; a, b = min(cols), max(cols)
        for i, row in enumerate(rows):
            for j, c in enumerate(row):
                if c in 'Xo': s += x(ox + (j-a)*g + g/2, i*g + g/2, g*.78, dot if c == 'o' else col, g*.3)
        ox += (b - a + 1)*g + g*.9
    return s, ox - g*.9
FT = os.path.join(FD, 'FamiljenGrotesk-SemiBold.ttf'); TT = TTFont(FT)
def texto(s, size, x0, y0):
    upm = TT['head'].unitsPerEm; hf = hb.Font(hb.Face(hb.Blob.from_file_path(FT))); b = hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf, b, {'kern': True})
    gs = TT.getGlyphSet(); order = TT.getGlyphOrder(); k = size/upm; xx = x0; dd = ''
    for i, ps in zip(b.glyph_infos, b.glyph_positions):
        pen = SVGPathPen(gs); gs[order[i.codepoint]].draw(TransformPen(pen, (k, 0, 0, -k, xx, y0))); dd += pen.getCommands(); xx += ps.x_advance*k
    return dd, xx
def wordmark(oscuro):
    col, dot = (MANTA, AN3) if oscuro else (AN, AN2)
    s, w = bordado(56, col, dot)
    return svg(s, f'-4 -4 {w+12:.0f} 64')
def lockup(oscuro):
    col, dot = (MANTA, AN3) if oscuro else (AN, AN2)
    s, w = bordado(46, col, dot); emb = niveles(OSC if not oscuro else CLA)[0]
    return svg(f'<g transform="scale(.97)">{emb}</g><g transform="translate(80 9)">{s}</g>', f'0 0 {80+w+12:.0f} 64')
def app(r=0): return svg(f'<rect width="512" height="512" rx="{r}" fill="{AN}"/><g transform="translate(56 56) scale(6.25)">{niveles(OSC)[0]}</g>', '0 0 512 512')
def favicon():
    v = niveles(OSC)[3]; c = niveles(CLA)[3]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><style>.o{{display:none}}@media(prefers-color-scheme:dark){{.c{{display:none}}.o{{display:inline}}}}</style>'
            f'<g class="c">{v}</g><g class="o">{c}</g></svg>')
def tarjeta():
    l1, _ = texto('Primero la pregunta,', 70, 96, 330); l2, _ = texto('después la gráfica.', 70, 96, 410)
    sub, _ = texto('Gráficas que responden lo que quiere saber quien mira', 28, 98, 480)
    s, w = bordado(70, MANTA, AN3)
    return svg(f'<rect width="1200" height="630" fill="{AN}"/><g transform="translate(96 150)">{s}</g><path d="{l1}{l2}" fill="{MANTA}"/><path d="{sub}" fill="{AN4}"/>'
               f'<g transform="translate(860 170) scale(4.4)">{niveles(OSC)[0].replace(AN, "#1B2D6E", 1)}</g>', '0 0 1200 630', 'xila · Primero la pregunta, después la gráfica.')
F = {}
for nom, s in zip(NOMBRES, niveles(OSC)): F[f'simbolo-{nom}'] = svg(s)
for nom, s in zip(NOMBRES, niveles(CLA)): F[f'simbolo-{nom}-claro'] = svg(s)
F.update({'wordmark': wordmark(False), 'wordmark-oscuro': wordmark(True), 'lockup': lockup(False), 'lockup-oscuro': lockup(True),
          'app-icon': app(), 'app-icon-redondeado': app(112), 'favicon': favicon(), 'tarjeta-redes': tarjeta()})
for n, s in F.items(): open(f'{H}/svg/{n}.svg', 'w').write(s)
tema = {'nombre': 'xila', 'version': '2.0.0', 'fuente': '.fruti/icons/xila/LEEME.md (rediseño aprobado 2026-11-09)',
 'concepto': 'La x bordada en el rombo del huipil; el centro es el dato. El nombre se escribe en punto de cruz y el punto de la i es el dato.',
 'simbolo': {'grande': '9 × 9 puntadas, desde 64 px', 'mediano': '5 × 5, de 32 a 48 px', 'chico': '3 × 3, de 20 a 28 px', 'favicon': 'una X gruesa con su punto, 16 px',
             'regla': 'cada dibujo solo en su rango; no se escala uno para cubrir otro'},
 'color': {'anil': {'valor': AN, 'uso': f'marca, fondo del emblema, el dato en las gráficas; {cr(AN, MANTA):.1f}:1 sobre manta'},
           'anil_medio': {'valor': AN2, 'uso': f'rombo del emblema claro, enlaces, cambios positivos; {cr(AN2, MANTA):.1f}:1 sobre manta'},
           'anil_claro': {'valor': AN3, 'uso': f'rombo del emblema y punto de la i sobre añil; {cr(AN3, AN):.1f}:1 sobre añil'},
           'anil_bruma': {'valor': AN4, 'uso': f'texto secundario sobre añil; {cr(AN4, AN):.1f}:1'},
           'manta': {'valor': MANTA, 'uso': 'fondo claro y la x del emblema'}, 'texto2': {'valor': TXT2, 'uso': f'texto secundario sobre manta; {cr(TXT2, MANTA):.1f}:1'},
           'contexto': {'valor': '#C4C6CF', 'uso': 'series de contexto en las gráficas (gris)'}},
 'tipografia': {'primaria': {'familia': 'Familjen Grotesk', 'peso': 600, 'uso': 'lema, títulos de sección, título de gráfica (el hallazgo)'},
                'secundaria': {'familia': 'Instrument Sans', 'pesos': [400, 600], 'uso': 'texto, ejes, etiquetas, tablas, botones; cifras tabulares'},
                'nombre': 'siempre bordado (svg/wordmark.svg); nunca escrito con una fuente'},
 'reglas': ['En las gráficas, el dato que importa va en añil y el resto en gris: la misma regla que el centro del emblema.',
            'Desde 64 px el emblema grande; de 32 a 48 el mediano; de 20 a 28 el chico; a 16 px el favicon.',
            'Sobre fondos oscuros o de color se usa el emblema claro (manta).',
            'El nombre bordado se usa desde 24 px de alto; más chico, «xila» en Familjen Grotesk junto al símbolo.',
            'La metáfora textil va en la marca; los botones y mensajes hablan claro («Quitar filtros»).']}
json.dump(tema, open(f'{H}/tema.json','w'), indent=2, ensure_ascii=False); print('ok')
