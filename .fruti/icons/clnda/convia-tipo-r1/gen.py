# Convia · tipografía ronda 1: logotipo con el símbolo E1b y la paleta B. Uso: python3 gen.py <carpeta de fuentes>
import sys, os, re, pathlib
F = sys.argv[1] if len(sys.argv) > 1 else '.'
D = os.path.dirname(os.path.abspath(__file__))
path = re.search(r'<path d="([^"]+)"', open(os.path.join(D, '..', 'convia-r7', 'E1b.svg')).read()).group(1)
B = dict(fondo='#1f4d3a', principal='#d42a66', acento='#ffc53d', papel='#f6f3ea', tinta='#15241d')
def sym(c, s): return f'<svg viewBox="0 0 200 200" width="{s}" height="{s}" aria-hidden="true"><path d="{path}" fill="{c}"/></svg>'
T = [  # id, nombre, archivo, peso, ajustes de ejes, carácter
 ('T1', 'Fraunces', 'Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf', 600, '"SOFT" 100, "WONK" 1, "opsz" 72', 'Serif suave y algo irregular: cálida y hecha a mano, como el trazo de la estrella.'),
 ('T2', 'Instrument Sans', 'InstrumentSans[wdth,wght].ttf', 600, 'normal', 'Sans limpia y neutra: deja todo el carácter al símbolo.'),
 ('T3', 'Syne', 'Syne[wght].ttf', 700, 'normal', 'Sans expresiva y ancha: moderna, con un toque de cartel de fiesta.'),
 ('T4', 'Onest', 'Onest.ttf', 700, 'normal', 'Sans redondeada y amable: cercana, muy legible en pantalla.'),
]
faces = ''.join(f'@font-face{{font-family:"{n}";src:url("{pathlib.Path(os.path.join(F, f)).resolve().as_uri()}");font-weight:100 900}}' for _, n, f, *_ in T)
cards = ''.join(f'''<article style="--ff:'{n}';--fw:{w};--fv:{v}">
<div class="lk claro">{sym(B['principal'], 52)}<b>Convia</b></div>
<div class="lk oscuro">{sym(B['acento'], 52)}<b>Convia</b></div>
<div class="ui"><h3>Talleres para ir solo este fin</h3><p>Cerámica, cocina y grabado en el Centro y Jalatlaco.</p></div>
<h2>{k} · {n}</h2><p class="d">{d}</p></article>''' for k, n, f, w, v, d in T)
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Convia · tipografía r1</title><style>{faces}
body{{margin:0;padding:32px;background:#efeee9;color:#1b1b1d;font:15px/1.45 "Instrument Sans",system-ui,sans-serif}}h1{{margin:0 0 4px;font-size:26px}}.lead{{margin:0 0 24px;color:#55555a}}
main{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}article{{background:#fff;border:1px solid #e3e3de;border-radius:16px;overflow:hidden;display:grid;align-content:start;gap:12px;padding-bottom:18px}}
article>h2,article>.d,article>.ui{{margin:0 18px}}
.lk{{display:flex;align-items:center;gap:10px;padding:22px 18px}}.lk b{{font-family:var(--ff);font-weight:var(--fw);font-variation-settings:var(--fv);font-size:44px;letter-spacing:-.01em;line-height:1}}
.claro{{background:{B['papel']};color:{B['tinta']}}}.oscuro{{background:{B['fondo']};color:#fff}}
.ui h3{{font-family:var(--ff);font-weight:var(--fw);font-variation-settings:var(--fv);font-size:20px;margin:0;color:{B['tinta']}}}.ui p{{margin:4px 0 0;color:#55555a}}
h2{{font-size:16px}}.d{{color:#55555a}}</style></head><body><h1>Convia · tipografía, ronda 1</h1><p class="lead">Logotipo con el símbolo E1b y la paleta B. Las cuatro son de Google Fonts (licencia OFL). El texto corrido de la app irá en una sans legible.</p><main>{cards}</main></body></html>'''
open(os.path.join(D, 'lamina.html'), 'w').write(html)
