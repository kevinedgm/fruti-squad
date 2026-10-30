# NisaData · ronda 1: color propio (A/B/C) y símbolo (1/2/3), decisiones separadas.
# El color de producto vive en marca, ícono de app, acceso y navegación; nunca en tablas (ahí todo color es estatus).
# Uso: python3 gen.py <carpeta de fuentes> → nisadata.html
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = sys.argv[1]
def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)
AZ, PE = '#052A76', '#C2D225'
COL = [  # clave, nombre, base, acento, idea
    ('A', 'Petróleo + menta', '#0B4F5C', '#5FD4B8', 'Verde azulado profundo: serio y técnico, se separa del azul real sin pelearse con él.'),
    ('B', 'Ciruela + coral', '#4E1B4A', '#FF8B75', 'Cálido y distinto; el más diferente de NisaLab. Ojo: el coral no debe usarse como alerta.'),
    ('C', 'Grafito + mandarina', '#1F2532', '#FF8A1F', 'Oscuro de panel de datos, con un acento vivo. El grafito casi no tiene tono: el acento lo es todo.'),
]
def s1(b, a):  # barras de células: columnas de 1, 2 y 3 células; la última célula en acento
    c = ''; r = 9.5
    for i, n in enumerate((1, 2, 3)):
        x = 18 + i * 32
        for j in range(n):
            y = 88 - j * 26; col = a if (i == 2 and j == n - 1) else b
            c += f'<circle cx="{x}" cy="{y}" r="{r + i * 1.2}" fill="{col}"/>'
    return f'<svg viewBox="0 0 100 100">{c}</svg>'
def s2(b, a):  # tendencia: puntos que crecen unidos por una línea; el último en acento
    pts = [(14, 80, 7), (38, 64, 9), (62, 52, 11), (84, 24, 13)]
    l = 'M' + ' L'.join(f'{x} {y}' for x, y, _ in pts)
    c = f'<path d="{l}" fill="none" stroke="{b}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    c += ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{a if i == 3 else b}"/>' for i, (x, y, r) in enumerate(pts))
    return f'<svg viewBox="0 0 100 100">{c}</svg>'
def s3(b, a):  # matriz: 3×3 puntos cuyo tamaño crece hacia arriba a la derecha (mapa de calor); uno en acento
    c = ''
    for i in range(3):
        for j in range(3):
            r = 6 + (i + (2 - j)) * 2.6; col = a if (i, j) == (2, 0) else b
            c += f'<circle cx="{20 + i * 30}" cy="{20 + j * 30}" r="{r:.1f}" fill="{col}"/>'
    return f'<svg viewBox="0 0 100 100">{c}</svg>'
SIM = [('1', 'Columnas de células', s1, 'Una gráfica de barras hecha de células, como las de Colonia: dato que crece. Parentesco claro con NisaLab sin copiarla.'),
       ('2', 'Tendencia', s2, 'Puntos que crecen unidos por una línea: el comportamiento en el tiempo. Riesgo: se parece a íconos genéricos de gráfica.'),
       ('3', 'Matriz de calor', s3, 'Nueve puntos que crecen hacia una esquina, como un mapa de calor: muchos datos que forman un patrón. El más propio.')]
import re as _re
_li = _re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(H, '..', 'nisalab-final', 'svg', 'app-icon.svg')).read().strip())
LAB_APP = f'<div class="app lab">{_li}</div>'
def app(sv, base): return f'<div class="app" style="background:{base}">{sv}</div>'
def lock(sv, base): return f'<div class="lk"><div class="sm">{sv}</div><div><div class="wm" style="color:{base}"><b>Nisa</b>Data</div><div class="rs">de <b style="color:{base}">Nisa Nabani</b></div></div></div>'
colh = ''
for k, n, b, a, idea in COL:
    sv = s3(b, a)
    colh += (f'<div class="c"><h3>{k} · {n}</h3><div class="sws"><span><i style="background:{b}"></i>{b}</span><span><i style="background:{a}"></i>{a}</span></div>'
             f'<div class="fam"><div class="lk"><div class="wm" style="color:{AZ}"><b>Nisa</b>Lab</div></div>{lock(sv, b)}</div>'
             f'<div class="apps">{LAB_APP}{app(s3("#FFFFFF", a), b)}<span class="mut">NisaLab · NisaData</span></div>'
             f'<p>{idea}</p><p class="m">Blanco sobre base {cr("#FFFFFF", b)}:1 · acento sobre base {cr(a, b)}:1</p></div>')
G1, G2 = '#1F2532', '#8A93A8'
def tams(fn): return ''.join(f'<div style="width:{px}px;height:{px}px">{fn(G1, G2)}</div>' for px in (48, 24, 16))
simh = ''.join(f'<div class="c"><h3>{k} · {n}</h3><div class="big">{fn(G1, G2)}</div><div class="tam">{tams(fn)}</div><p>{idea}</p></div>' for k, n, fn, idea in SIM)
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700))
css = ff + '''
*{box-sizing:border-box}body{margin:0;background:#F2F4F8;color:#141B33;font:400 14px/1.5 Poppins,sans-serif;padding:32px}
h1{font:700 26px/1.2 Poppins;color:#141B33;margin:0 0 4px}.lead{color:#535B70;max-width:880px;margin:0 0 24px}h2{font:600 19px/1.3 Poppins;margin:28px 0 4px}.sub{color:#535B70;margin:0 0 14px}
.g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.c{background:#fff;border:1px solid #DFE3EC;border-radius:14px;padding:20px;box-shadow:0 1px 2px rgba(20,27,51,.06);display:flex;flex-direction:column;gap:12px;min-width:0}
.c h3{font:600 15px/1.3 Poppins;margin:0}.c p{margin:0;color:#535B70;font-size:13px}.m{font-size:12px!important}
.sws{display:flex;gap:14px;font-size:12px;color:#535B70}.sws span{display:inline-flex;gap:6px;align-items:center}.sws i{width:18px;height:18px;border-radius:5px;display:inline-block}
.fam{display:flex;flex-direction:column;gap:10px;padding:12px 0;border-top:1px solid #EEF1F6;border-bottom:1px solid #EEF1F6}
.lk{display:flex;align-items:center;gap:10px}.sm{width:40px;height:40px;flex:none}.sm svg,.big svg,.tam svg,.app svg{width:100%;height:100%;display:block}
.wm{font:400 28px/1 Poppins;letter-spacing:-.01em}.wm b{font-weight:700}.rs{font:500 11px/1 Poppins;color:#535B70;margin-top:3px}
.apps{display:flex;gap:10px;align-items:center}.app{width:56px;height:56px;border-radius:14px;padding:11px}.mut{font-size:12px;color:#535B70}.app.lab{padding:0;overflow:hidden;background:none}
.big{width:120px;height:120px}.tam{display:flex;gap:14px;align-items:flex-end}
@media (max-width:1000px){.g{grid-template-columns:1fr}}@media (max-width:480px){body{padding:16px}}
'''
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaData ronda 1</title><style>{css}</style><body>'
        '<h1>NisaData · ronda 1</h1><p class="lead">Dos decisiones separadas. Primero el color propio, que distingue a NisaData de NisaLab dentro de la familia (cada color se muestra con el símbolo 3 solo como referencia). Después el símbolo, en gris neutro para juzgar solo la forma. El color de producto vive en la marca, el ícono de app, el acceso y la navegación; nunca en tablas ni gráficas de estatus.</p>'
        f'<h2>Color de NisaData</h2><p class="sub">Junto a NisaLab (azul real + pera), para ver la familia.</p><div class="g">{colh}</div>'
        f'<h2>Símbolo</h2><p class="sub">Todos hechos de células redondas, como Colonia, para que se note que son familia. A 48, 24 y 16 px.</p><div class="g">{simh}</div></body></html>')
open(os.path.join(H, 'nisadata.html'), 'w').write(html)
for k, n, b, a, _ in COL: print(k, n, cr('#FFFFFF', b), cr(a, b))
