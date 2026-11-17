# GEMA · Gestión de Muestras y Análisis · archivos finales (2026-11-17).
# Congelado: símbolo R1 (Pantalla + Resultado) + versión chica + silueta; color N2 (degradado navy); letra Onest 700/500.
# Uso: python3 -I gen.py <carpeta con onest-500.ttf y onest-700.ttf>  y luego  node render.cjs
import sys, os, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FD = sys.argv[1]
NAVY, AZUL, AZUL_CLARO, CELESTE, OSC, CLA = '#052A76', '#3D67AE', '#7aa2f0', '#8fb3ff', '#0a0a0b', '#f2f2ee'
# Símbolo grande (R1). Tinta = currentColor. Pico = degradado vertical de --gema-pico-b (arriba) a --gema-pico-a (abajo).
MARCO = '<rect x="5" y="8" width="38" height="32" rx="7" fill="none" stroke="{t}" stroke-width="2.6"/>'
AREA = '<path d="M21.76 33C25.12 33 26.24 14 28.48 14C30.72 14 31.84 33 36.32 33Z" fill="url(#{g})"/>'
SENAL = '<path d="M10 33H13.92C15.88 33 16.44 24.45 17.56 24.45C18.68 24.45 19.24 33 21.76 33C25.12 33 26.24 14 28.48 14C30.72 14 31.84 33 36.32 33H38" fill="none" stroke="{t}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
# Chico (16–24 px): marco grueso y solo el pico del resultado.
C_AREA = '<path d="M14 34C19 34 20.5 13 24 13C27.5 13 29 34 34 34Z" fill="url(#{g})"/>'
C_MARCO = '<rect x="5" y="7" width="38" height="34" rx="8" fill="none" stroke="{t}" stroke-width="3.6"/>'
C_SENAL = '<path d="M10 34H14C19 34 20.5 13 24 13C27.5 13 29 34 34 34H38" fill="none" stroke="{t}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>'
def grad(g, a, b): return f'<defs><linearGradient id="{g}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{b}"/><stop offset="1" stop-color="{a}"/></linearGradient></defs>'
VAR_A, VAR_B = 'var(--gema-pico-a,#052A76)', 'var(--gema-pico-b,#3D67AE)'
def simbolo(g, t='currentColor', a=VAR_A, b=VAR_B, chico=False):
    if chico: return grad(g, a, b) + C_AREA.format(g=g) + C_MARCO.format(t=t) + C_SENAL.format(t=t)
    return grad(g, a, b) + MARCO.format(t=t) + AREA.format(g=g) + SENAL.format(t=t)
def svg(w, h, body, titulo):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" role="img" aria-label="{titulo}">\n<title>{titulo}</title>\n{body}\n</svg>\n'
def texto(fuente, txt, tam, track=0.0):
    f = TTFont(os.path.join(FD, fuente)); gs = f.getGlyphSet(); cmap = f.getBestCmap(); hm = f['hmtx']; e = tam / f['head'].unitsPerEm
    d, cx = [], 0
    for ch in txt:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs); gs[g].draw(TransformPen(pen, (e, 0, 0, -e, cx, 0))); d.append(pen.getCommands()); cx += hm[g][0]*e + track*tam
    return ' '.join(d), cx - track*tam
def esc(body, x, y, s): return f'<g transform="translate({x:g} {y:g}) scale({s/48:g})">{body}</g>'
NOMBRE = 'GEMA, Gestión de Muestras y Análisis'
gm, wG = texto('onest-700.ttf', 'GEMA', 44, -0.01); ds, wD = texto('onest-500.ttf', 'Gestión de Muestras y Análisis', 12.5)
gc, wGc = texto('onest-700.ttf', 'GEMA', 30, -0.01)
def lockups(t, a, b, sufijo):
    g = 'gema-pico' + sufijo
    xT = 78; W = xT + max(wG, wD) + 2; Wv = max(wG, wD, 80) + 8
    return {
     'horizontal': (W, 64, esc(simbolo(g+'h', t, a, b), 0, 0, 64) + f'<path transform="translate({xT} 41)" d="{gm}" fill="{t}"/><path transform="translate({xT+1} 59)" d="{ds}" fill="{t}"/>'),
     'compacto': (50 + wGc + 2, 40, esc(simbolo(g+'c', t, a, b), 0, 0, 40) + f'<path transform="translate(50 31.3)" d="{gc}" fill="{t}"/>'),
     'vertical': (Wv, 152, esc(simbolo(g+'v', t, a, b), (Wv-80)/2, 0, 80) + f'<path transform="translate({(Wv-wG)/2:.2f} 124)" d="{gm}" fill="{t}"/><path transform="translate({(Wv-wD)/2:.2f} 146)" d="{ds}" fill="{t}"/>'),
    }
for k, (w, h, b) in lockups('currentColor', VAR_A, VAR_B, '').items(): open(f'gema-logotipo-{k}.svg', 'w').write(svg(w, h, b, NOMBRE))
for modo, t, a, b in (('sobre-claro', OSC, NAVY, AZUL), ('sobre-oscuro', CLA, AZUL, AZUL_CLARO)):
    for k, (w, h, body) in lockups(t, a, b, '-' + modo).items(): open(f'gema-logotipo-{k}-{modo}.svg', 'w').write(svg(w, h, body, NOMBRE))
open('gema-simbolo.svg', 'w').write(svg(48, 48, simbolo('gema-s'), 'GEMA'))
open('gema-simbolo-chico.svg', 'w').write(svg(48, 48, simbolo('gema-sc', chico=True), 'GEMA'))
# Favicon: chico con tinta según el tema del navegador.
fav = f'<style>:root{{--t:{OSC};--a:{NAVY};--b:{AZUL}}}@media (prefers-color-scheme:dark){{:root{{--t:{CLA};--a:{AZUL};--b:{AZUL_CLARO}}}}}</style>' + simbolo('gema-f', 'var(--t)', 'var(--a)', 'var(--b)', chico=True)
open('favicon.svg', 'w').write(svg(48, 48, fav, 'GEMA'))
# Notificación: silueta de una tinta, marco y pico calado (solo contorno), blanco sobre transparente.
sil = ('<rect x="5" y="7" width="38" height="34" rx="8" fill="none" stroke="#ffffff" stroke-width="4"/>'
       '<path d="M10 34H14C19 34 20.5 13 24 13C27.5 13 29 34 34 34H38" fill="none" stroke="#ffffff" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round"/>')
open('gema-notificacion.svg', 'w').write(svg(48, 48, sil, 'GEMA'))
# Tokens.
open('gema-marca.css', 'w').write(f'''/* GEMA · Gestión de Muestras y Análisis · marca (congelada 2026-11-17) */
/* Degradado navy SOLO en superficies de marca (pico del símbolo, icono de la app, panel de inicio de sesión).
   En la interfaz el color es plano: navy en tema claro, azul medio en oscuro, siempre con texto blanco. */
:root {{
  --g-color-brand: {NAVY};          /* Grana, tema claro. Blanco sobre navy: 13.1:1. Navy sobre papel: 11.7:1 */
  --g-color-on-brand: #ffffff;
  --gema-pico-a: {NAVY};            /* degradado del pico: abajo */
  --gema-pico-b: {AZUL};            /* degradado del pico: arriba */
  --gema-degradado: linear-gradient(160deg, {AZUL}, {NAVY});
  --gema-tinta: {OSC}; --gema-papel: {CLA};
  --gema-font: "Onest", ui-sans-serif, system-ui, sans-serif;            /* marca e interfaz */
  --gema-font-mono: "JetBrains Mono", ui-monospace, monospace;           /* folios, valores y unidades */
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --g-color-brand: {AZUL};        /* blanco sobre azul medio: 5.6:1; sobre negro: 3.5:1 (botón, no texto) */
    --gema-pico-a: {AZUL}; --gema-pico-b: {AZUL_CLARO};
  }}
}}
:root[data-theme="dark"] {{ --g-color-brand: {AZUL}; --gema-pico-a: {AZUL}; --gema-pico-b: {AZUL_CLARO}; }}
''')
json.dump({'name': 'GEMA · Gestión de Muestras y Análisis', 'short_name': 'GEMA', 'theme_color': NAVY, 'background_color': NAVY,
           'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png', 'purpose': 'any'},
                     {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any'},
                     {'src': 'maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}]},
          open('manifest.fragmento.json', 'w'), ensure_ascii=False, indent=2)
# PNG: icono sobre degradado navy, símbolo blanco con pico celeste.
def tile(z, chico, rad, sym):
    p = (z - sym) / 2
    body = simbolo('t', '#ffffff', AZUL_CLARO, CELESTE, chico=chico)
    bg = f'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{AZUL}"/><stop offset="1" stop-color="{NAVY}"/></linearGradient></defs><rect width="{z}" height="{z}" rx="{rad}" fill="url(#bg)"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{z}" height="{z}" viewBox="0 0 {z} {z}">{bg}{esc(body, p, p, sym)}</svg>'
PNG = {'favicon-32': tile(32, True, 7, 30), 'icon-192': tile(192, False, 42, 150), 'icon-512': tile(512, False, 112, 400),
       'maskable-512': tile(512, False, 0, 300), 'apple-touch-icon': tile(180, False, 0, 130),
       'notificacion-96': svg(48, 48, sil, 'GEMA').replace('<svg ', '<svg width="96" height="96" ', 1)}
open('render.json', 'w').write(json.dumps(PNG)); print('ok', round(wG), round(wD))
