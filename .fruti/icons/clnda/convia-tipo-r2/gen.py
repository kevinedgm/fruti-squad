# Convia · tipografía ronda 2 (más personalidad): logotipo con el símbolo E1b y la paleta B. Uso: python3 gen.py <carpeta de fuentes>
# Fuentes: 2.º argumento = carpeta con los .woff2 descargados de Google Fonts (Caprasimo, Shrikhand, YoungSerif, Gloock, InstrumentSerif, Kalnia, CherryBombOne, BagelFatOne).
import sys, os, re, pathlib
F = sys.argv[1] if len(sys.argv) > 1 else '.'
D = os.path.dirname(os.path.abspath(__file__))
path = re.search(r'<path d="([^"]+)"', open(os.path.join(D, '..', 'convia-r7', 'E1b.svg')).read()).group(1)
B = dict(fondo='#1f4d3a', principal='#d42a66', acento='#ffc53d', papel='#f6f3ea', tinta='#15241d')
def sym(c, s): return f'<svg viewBox="0 0 200 200" width="{s}" height="{s}" aria-hidden="true"><path d="{path}" fill="{c}"/></svg>'
T = [  # id, nombre, archivo, peso, ejes, carácter
 ('P1', 'Caprasimo', 'Caprasimo.woff2', 400, 'normal', 'Serif gruesa y blanda, de los años 70: cálida, golosa, muy de cartel de fiesta.'),
 ('P2', 'Shrikhand', 'Shrikhand.woff2', 400, 'normal', 'Cursiva gruesa con mucho movimiento: festiva, parece pintada en una barda.'),
 ('P3', 'Young Serif', 'YoungSerif.woff2', 400, 'normal', 'Serif con remates suaves y algo torpes a propósito: cercana y con oficio.'),
 ('P4', 'Gloock', 'Gloock.woff2', 400, 'normal', 'Serif de alto contraste y curvas marcadas: editorial, elegante, con carácter.'),
 ('P5', 'Instrument Serif', 'InstrumentSerif.woff2', 400, 'normal', 'Serif cursiva condensada: fina, de revista, muy actual.'),
 ('P6', 'Kalnia', 'Kalnia.woff2', 600, 'normal', 'Serif con trazos que se curvan como cinta: decorativa y única.'),
 ('P7', 'Cherry Bomb One', 'CherryBombOne.woff2', 400, 'normal', 'Redonda e inflada: juguetona, juvenil.'),
 ('P8', 'Bagel Fat One', 'BagelFatOne.woff2', 400, 'normal', 'Gruesa, compacta y alegre: contundente, tipo calcomanía.'),
]
F2 = sys.argv[2] if len(sys.argv) > 2 else F
faces = ''.join(f'@font-face{{font-family:"{n}";src:url("{pathlib.Path(os.path.join(F2, f)).resolve().as_uri()}");font-weight:100 900}}' for _, n, f, *_ in T) + f'@font-face{{font-family:"Instrument Sans";src:url("{pathlib.Path(os.path.join(F, "InstrumentSans[wdth,wght].ttf")).resolve().as_uri()}")}}'
cards = ''.join(f'''<article style="--ff:'{n}';--fw:{w};--fv:{v}">
<div class="lk claro">{sym(B['principal'], 52)}<b>Convia</b></div>
<div class="lk oscuro">{sym(B['acento'], 52)}<b>Convia</b></div>
<div class="ui"><h3>Talleres para ir solo este fin</h3><p>Cerámica, cocina y grabado en el Centro y Jalatlaco.</p></div>
<h2>{k} · {n}</h2><p class="d">{d}</p></article>''' for k, n, f, w, v, d in T)
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Convia · tipografía r2</title><style>{faces}
body{{margin:0;padding:32px;background:#efeee9;color:#1b1b1d;font:15px/1.45 "Instrument Sans",system-ui,sans-serif}}h1{{margin:0 0 4px;font-size:26px}}.lead{{margin:0 0 24px;color:#55555a}}
main{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}article{{background:#fff;border:1px solid #e3e3de;border-radius:16px;overflow:hidden;display:grid;align-content:start;gap:12px;padding-bottom:18px}}
article>h2,article>.d,article>.ui{{margin:0 18px}}
.lk{{display:flex;align-items:center;gap:10px;padding:22px 18px}}.lk b{{font-family:var(--ff);font-weight:var(--fw);font-variation-settings:var(--fv);font-size:44px;letter-spacing:-.01em;line-height:1}}
.claro{{background:{B['papel']};color:{B['tinta']}}}.oscuro{{background:{B['fondo']};color:#fff}}
.ui h3{{font-family:var(--ff);font-weight:var(--fw);font-variation-settings:var(--fv);font-size:20px;margin:0;color:{B['tinta']}}}.ui p{{margin:4px 0 0;color:#55555a}}
h2{{font-size:16px}}.d{{color:#55555a}}</style></head><body><h1>Convia · tipografía, ronda 2 · más personalidad</h1><p class="lead">Logotipo con el símbolo E1b y la paleta B. Todas son de Google Fonts (licencia OFL, uso comercial libre). El texto corrido de la app irá en una sans legible.</p><main>{cards}</main></body></html>'''
open(os.path.join(D, 'lamina.html'), 'w').write(html)
