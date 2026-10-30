# NisaResults · ronda 2 (colores institucionales): color propio (A/B/C) y símbolo (1/2/3), decisiones separadas.
# Portal de clientes con sus resultados e informes; la página pública (QR) lleva la marca del hotel y el sello «Analizada por Nisa Nabani».
# Restricción de color: ni verde ni rojo (en el portal significan Óptimo / No óptimo), ni azul real (NisaLab) ni grafito+mandarina (NisaData).
# Uso: python3 gen.py <carpeta de fuentes> → nisaresults.html
import os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..'); F = sys.argv[1]
def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)
COL = [('A', 'Azul real + pera', '#052A76', '#C2D225', 'Los dos colores institucionales tal cual. El cliente nunca ve NisaLab (es interno), así que compartirlos no confunde: aquí distingue el símbolo.'),
       ('B', 'Azul real + cian', '#052A76', '#00B4D8', 'Azul real con el cian secundario del manual de Nisa Nabani: institucional y con aire de agua y análisis.'),
       ('C', 'Azul secundario + pera', '#3D67AE', '#C2D225', 'El azul secundario del manual, más claro y amable, con la pera institucional.')]
def s1(b, a):  # banda de control: dos límites y células dentro; la del centro en acento
    return (f'<svg viewBox="0 0 100 100"><rect x="6" y="22" width="88" height="7" rx="3.5" fill="{b}"/><rect x="6" y="71" width="88" height="7" rx="3.5" fill="{b}"/>'
            f'<circle cx="22" cy="56" r="9" fill="{b}"/><circle cx="50" cy="46" r="11" fill="{a}"/><circle cx="78" cy="53" r="9" fill="{b}"/></svg>')
def s2(b, a):  # palomita de células
    pts = [(14, 52, 8), (30, 66, 9), (48, 76, 10), (66, 54, 11), (84, 28, 12)]
    return '<svg viewBox="0 0 100 100">' + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{a if i == 4 else b}"/>' for i, (x, y, r) in enumerate(pts)) + '</svg>'
def s3(b, a):  # hoja de resultados: renglones de células (3, 2, 1) dentro de una hoja; la última en acento
    c = f'<rect x="14" y="6" width="72" height="88" rx="12" fill="none" stroke="{b}" stroke-width="7"/>'
    for j, n in enumerate((3, 2, 1)):
        for i in range(n): c += f'<circle cx="{34 + i * 16}" cy="{30 + j * 20}" r="6.5" fill="{a if (j == 2) else b}"/>'
    return f'<svg viewBox="0 0 100 100">{c}</svg>'
SIM = [('1', 'Banda de control', s1, 'Células dentro de dos límites, como la gráfica de monitoreo con su zona aceptable: «el resultado está dentro». El más propio del producto.'),
       ('2', 'Palomita de células', s2, 'Cinco células que dibujan una palomita: resultado revisado. Riesgo: promete «todo bien» aunque haya resultados no óptimos.'),
       ('3', 'Hoja de resultados', s3, 'Un informe con renglones de células: tus resultados en un documento. Claro, pero el contorno lo aleja de Colonia.')]
def lock(sv, base): return f'<div class="lk"><div class="sm">{sv}</div><div><div class="wm" style="color:{base}"><b>Nisa</b>Results</div><div class="rs">de <b style="color:{base}">Nisa Nabani</b></div></div></div>'
_li = lambda n: re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(NS, n)).read().strip())
FAM = f'<div class="app lab">{_li("nisalab-final/svg/app-icon.svg")}</div><div class="app lab">{_li("nisadata-final/svg/app-icon.svg")}</div>'
colh = ''.join(f'<div class="c"><h3>{k} · {n}</h3><div class="sws"><span><i style="background:{b}"></i>{b}</span><span><i style="background:{a}"></i>{a}</span></div>{lock(s1(b, a), b)}'
               f'<div class="apps">{FAM}<div class="app" style="background:{b}">{s1("#FFFFFF", a)}</div><span class="mut">NisaLab · NisaData · NisaResults</span></div><p>{i}</p>'
               f'<p class="m">Blanco sobre base {cr("#FFFFFF", b)}:1 · acento sobre base {cr(a, b)}:1</p></div>' for k, n, b, a, i in COL)
G1, G2 = '#1F2532', '#8A93A8'
def tams(fn): return ''.join(f'<div style="width:{px}px;height:{px}px">{fn(G1, G2)}</div>' for px in (48, 24, 16))
simh = ''.join(f'<div class="c"><h3>{k} · {n}</h3><div class="big">{fn(G1, G2)}</div><div class="tam">{tams(fn)}</div><p>{i}</p></div>' for k, n, fn, i in SIM)
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700))
css = ff + '''
*{box-sizing:border-box}body{margin:0;background:#F2F4F8;color:#141B33;font:400 14px/1.5 Poppins,sans-serif;padding:32px}
h1{font:700 26px/1.2 Poppins;margin:0 0 4px}.lead{color:#535B70;max-width:900px;margin:0 0 24px}h2{font:600 19px/1.3 Poppins;margin:28px 0 4px}.sub{color:#535B70;margin:0 0 14px}
.g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.c{background:#fff;border:1px solid #DFE3EC;border-radius:14px;padding:20px;display:flex;flex-direction:column;gap:12px;min-width:0}
.c h3{font:600 15px/1.3 Poppins;margin:0}.c p{margin:0;color:#535B70;font-size:13px}.m{font-size:12px!important}
.sws{display:flex;gap:14px;font-size:12px;color:#535B70}.sws span{display:inline-flex;gap:6px;align-items:center}.sws i{width:18px;height:18px;border-radius:5px;display:inline-block}
.lk{display:flex;align-items:center;gap:10px;padding:10px 0;border-top:1px solid #EEF1F6;border-bottom:1px solid #EEF1F6}.sm{width:44px;height:44px;flex:none}svg{width:100%;height:100%;display:block}
.wm{font:400 28px/1 Poppins;letter-spacing:-.01em}.wm b{font-weight:700}.rs{font:500 11px/1 Poppins;color:#535B70;margin-top:3px}
.apps{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.app{width:48px;height:48px;border-radius:12px;padding:9px;overflow:hidden}.app.lab{padding:0}.mut{font-size:12px;color:#535B70}
.big{width:120px;height:120px}.tam{display:flex;gap:14px;align-items:flex-end}
@media (max-width:1000px){.g{grid-template-columns:1fr}}@media (max-width:480px){body{padding:16px}}
'''
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaResults ronda 1</title><style>{css}</style><body>'
        '<h1>NisaResults · ronda 2: colores institucionales</h1><p class="lead">Portal donde el cliente consulta sus resultados e informes y publica su página de calidad con QR. Dos decisiones separadas: color (mostrado con el símbolo 1 solo como referencia) y símbolo (en gris, para juzgar la forma). Ronda 2: como lo verá el cliente, el color sale del manual de Nisa Nabani (azul real, azul secundario, cian y pera). Sigue sin usar verde ni rojo, que en el portal significan Óptimo y No óptimo.</p>'
        f'<h2>Color de NisaResults</h2><p class="sub">Junto a NisaLab y NisaData, para ver la familia.</p><div class="g">{colh}</div>'
        f'<h2>Símbolo</h2><p class="sub">Hechos de células, como Colonia. A 48, 24 y 16 px.</p><div class="g">{simh}</div></body></html>')
open(os.path.join(H, 'nisaresults.html'), 'w').write(html)
for k, n, b, a, _ in COL: print(k, n, cr('#FFFFFF', b), cr(a, b))
