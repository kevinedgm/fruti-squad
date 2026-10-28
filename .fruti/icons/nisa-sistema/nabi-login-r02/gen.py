# Nabi · login r02. Uso: python3 gen.py [carpeta-fuentes salida-local]
# 1) nabi-tokens.css sale de ../nabi-design-system/tokens.json (fuente única v1).
# 2) nabi-identidad-v2.css es la capa de propuesta (ver identidad-v2.md); solo redefine o agrega tokens.
# 3) login.html = tokens + capa v2 + plantilla, con lockup y carga reales de ../nabi-final/svg.
import json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(H, '..', 'nabi-design-system', 'tokens.json')))
SVG = os.path.join(H, '..', 'nabi-final', 'svg')
v = []
for t in T['color']['tokens']:
    val = t['value']
    if val.startswith('{'): val = 'var(--%s)' % val.strip('{}')
    v.append(f'--{t["name"]}:{val};')
for k, f in T['type']['families'].items(): v.append(f'--font-{k}:{f};')
for g in ('spacing', 'radius', 'sizing', 'shadow', 'motion'):
    for t in T[g]['tokens']: v.append(f'--{t["name"]}:{t["value"]};')
tokens = ':root{' + ''.join(v) + 'color-scheme:light}'
open(os.path.join(H, 'nabi-tokens.css'), 'w').write('/* generado desde ../nabi-design-system/tokens.json · no editar a mano */\n' + tokens + '\n')
capa = open(os.path.join(H, 'nabi-identidad-v2.css')).read()
def svg(n, w=None):
    s = open(os.path.join(SVG, n)).read()
    s = s.replace('<svg ', '<svg aria-hidden="true" focusable="false" ' + (f'width="{w}" ' if w else ''), 1)
    return s
carga = svg('carga-blanco.svg', 18)
carga = re.sub(r'\.w(\d?)(?=[{,\s])', r'.cw\1', carga)
carga = re.sub(r'class="w w(\d)"', r'class="cw cw\1"', carga).replace('@keyframes nb', '@keyframes nbc').replace('animation:nb ', 'animation:nbc ')
GOOGLE = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
  '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=IBM+Plex+Mono:wght@400;500;600'
  '&family=Newsreader:ital,opsz,wght@1,6..72,400;1,6..72,500&display=swap">')
def local(d):
    f = {'Archivo': 'ArchivoVar.ttf', 'IBM Plex Mono': 'IBMPlexMono.ttf', 'Newsreader': 'Newsreader%5Bopsz,wght%5D.ttf'}
    return '<style>' + ''.join("@font-face{font-family:'%s';src:url('file://%s/%s');font-weight:100 900;font-stretch:62%% 125%%%s}" % (k, d, v.replace('%', '%25'), ';font-style:italic' if k == 'Newsreader' else '') for k, v in f.items()) + '</style>'
t = open(os.path.join(H, 'plantilla.html')).read()
t = (t.replace('{{FUENTES}}', local(sys.argv[1]) if len(sys.argv) > 1 else GOOGLE)
      .replace('{{TOKENS}}', tokens).replace('{{CAPA_V2}}', capa)
      .replace('{{LOCKUP}}', svg('lockup-h.svg')).replace('{{CARGA}}', carga))
open(sys.argv[2] if len(sys.argv) > 2 else os.path.join(H, 'login.html'), 'w').write(t)
print('ok')
