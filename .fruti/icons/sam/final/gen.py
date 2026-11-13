# SAM · archivos finales de identidad (2026-11-13). Congelado: símbolo Tarjetas C2 + C4, color Voltaje (regla de relleno), Onest 700/500.
# Uso: python3 -I gen.py <carpeta-con-onest-500.ttf-y-onest-700.ttf>   (Onest, OFL; el texto se convierte a trazos, la fuente no se incluye)
import sys, os, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FD = sys.argv[1]
OSC, CLA, VO = '#0a0a0b', '#f2f2ee', '#c6f432'
R8 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'identidad', 'ronda-8')
def cuerpo(nombre):  # interior del SVG congelado (sin la etiqueta <svg>)
    s = open(os.path.join(R8, nombre)).read()
    return s[s.index('>', s.index('<svg')) + 1: s.rindex('</svg>')].strip('\n')
C2, C4 = cuerpo('c2-contorno.svg'), cuerpo('c4-16px.svg')
def texto(fuente, txt, tam, x, y, track=0.0):
    f = TTFont(os.path.join(FD, fuente)); gs = f.getGlyphSet(); cmap = f.getBestCmap(); hm = f['hmtx']; esc = tam / f['head'].unitsPerEm
    d, cx = [], x
    for ch in txt:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (esc, 0, 0, -esc, cx, y)))
        d.append(pen.getCommands()); cx += hm[g][0] * esc + track * tam
    return ' '.join(d), cx - track * tam - x
def svg(w, h, body, titulo, extra=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" role="img" aria-label="{titulo}"{extra}>\n<title>{titulo}</title>\n{body}\n</svg>\n')
def simbolo(body, x, y, tam):
    return f'<g transform="translate({x:g} {y:g}) scale({tam/48:g})">\n{body}\n</g>'
# Logotipos: tinta = currentColor, lima = --g-color-brand, palomita = --sam-tinta (fallbacks incluidos).
def logos():
    out = {}
    sam, wS = texto('onest-700.ttf', 'SAM', 44, 0, 0, -0.01)
    des, wD = texto('onest-500.ttf', 'Simple Activity Manager', 12.5, 0, 0)
    # horizontal: símbolo 64; «SAM» con altura de mayúscula 31; descriptor debajo
    xT = 78; W = xT + max(wS, wD) + 2
    out['horizontal'] = (W, 64, simbolo(C2, 0, 0, 64) + f'\n<path transform="translate({xT} 41)" d="{sam}" fill="currentColor"/>'
                         f'\n<path transform="translate({xT+1} 59)" d="{des}" fill="currentColor"/>')
    # compacto: símbolo 40 + «SAM»
    samc, wSc = texto('onest-700.ttf', 'SAM', 30, 0, 0, -0.01)
    out['compacto'] = (50 + wSc + 2, 40, simbolo(C2, 0, 0, 40) + f'\n<path transform="translate(50 31.3)" d="{samc}" fill="currentColor"/>')
    # vertical: símbolo 80 centrado, «SAM» y descriptor centrados
    Wv = max(wS, wD, 80) + 8
    out['vertical'] = (Wv, 152, simbolo(C2, (Wv-80)/2, 0, 80) + f'\n<path transform="translate({(Wv-wS)/2:.2f} 124)" d="{sam}" fill="currentColor"/>'
                       f'\n<path transform="translate({(Wv-wD)/2:.2f} 146)" d="{des}" fill="currentColor"/>')
    return out
L = logos()
for k, (w, h, b) in L.items():
    open(f'sam-logotipo-{k}.svg', 'w').write(svg(w, h, b, 'SAM, Simple Activity Manager'))
    for modo, tinta in (('sobre-oscuro', CLA), ('sobre-claro', OSC)):
        fijo = b.replace('currentColor', tinta).replace('var(--g-color-brand,#c6f432)', VO).replace('var(--sam-tinta,#0a0a0b)', OSC)
        open(f'sam-logotipo-{k}-{modo}.svg', 'w').write(svg(w, h, fijo, 'SAM, Simple Activity Manager'))
open('sam-simbolo.svg', 'w').write(svg(48, 48, C2, 'SAM'))
open('sam-simbolo-chico.svg', 'w').write(svg(48, 48, C4, 'SAM'))
# Favicon SVG: C4 con colores fijos y cambio de tinta según el tema del navegador.
fav = C4.replace('currentColor', 'var(--t)').replace('var(--g-color-brand,#c6f432)', VO).replace('var(--sam-tinta,#0a0a0b)', OSC)
open('favicon.svg', 'w').write(svg(48, 48, f'<style>:root{{--t:{OSC}}}@media (prefers-color-scheme:dark){{:root{{--t:{CLA}}}}}</style>\n' + fav, 'SAM'))
# Notificación: silueta de una tinta (blanco sobre transparente, como pide Android para el icono pequeño).
sil = open(os.path.join(R8, '..', 'ronda-9', 'notificacion.svg')).read().replace('currentColor', '#ffffff')
open('sam-notificacion.svg', 'w').write(sil)
# Tokens para Grana y la app.
open('sam-marca.css', 'w').write(f'''/* SAM · Simple Activity Manager · marca (congelada 2026-11-13) */
/* Regla del lima: es RELLENO (botón principal, estado activo, acento del símbolo) y siempre toca tinta.
   Nunca es texto ni se oscurece. En tema claro lleva contorno de tinta; texto, enlaces y foco van en tinta. */
:root {{
  --g-color-brand: {VO};          /* Voltaje: tiñe Grana y el símbolo */
  --g-color-on-brand: {OSC};      /* texto sobre lima: 15.4:1 */
  --sam-tinta: {OSC};             /* palomita del símbolo y texto sobre lima */
  --sam-noche: {OSC};             /* fondo oscuro; lima sobre noche: 15.4:1 */
  --sam-papel: {CLA};             /* fondo claro; tinta sobre papel: 17.6:1. Lima sobre papel: 1.1:1, solo con contorno */
  --sam-font: "Onest", ui-sans-serif, system-ui, sans-serif;           /* marca e interfaz: 400, 500, 600, 700 */
  --sam-font-mono: "JetBrains Mono", ui-monospace, monospace;          /* folios, horas y datos */
}}
''')
# Manifest de la PWA (fragmento).
json.dump({'name': 'SAM · Simple Activity Manager', 'short_name': 'SAM', 'theme_color': OSC, 'background_color': OSC,
           'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png', 'purpose': 'any'},
                     {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any'},
                     {'src': 'maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}]},
          open('manifest.fragmento.json', 'w'), ensure_ascii=False, indent=2)
# Página de render para los PNG (la usa render.cjs).
def tile(z, body, bg, rad, sym):
    pad = (z - sym) / 2; fijo = body.replace('currentColor', CLA).replace('var(--g-color-brand,#c6f432)', VO).replace('var(--sam-tinta,#0a0a0b)', OSC)
    bgr = f'<rect width="{z}" height="{z}" rx="{rad}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{z}" height="{z}" viewBox="0 0 {z} {z}">{bgr}{simbolo(fijo, pad, pad, sym)}</svg>'
PNG = {'favicon-32': tile(32, C4, OSC, 7, 30), 'icon-192': tile(192, C2, OSC, 42, 150), 'icon-512': tile(512, C2, OSC, 112, 400),
       'maskable-512': tile(512, C2, OSC, 0, 300), 'apple-touch-icon': tile(180, C2, OSC, 0, 130),
       'notificacion-96': sil.replace('<svg ', '<svg width="96" height="96" ', 1)}
open('render.json', 'w').write(json.dumps(PNG))
print('ok', {k: (round(w), h) for k, (w, h, _) in L.items()})
