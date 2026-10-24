# Nabi · avatar unisex: la cara de la ronda 4 (A), fiel a la referencia de Notion, sin pelo ni género.
# Lienzo propio del avatar (128): el círculo de color lo pone el componente; la figura va en currentColor.
import re, sys
S = sys.argv[1]
def T(d):  # hornea translate(64 66) scale(1.22) translate(-63 -69) en las coordenadas
    it = iter(re.findall(r'-?\d+\.?\d*', d)); out = []
    for x, y in zip(it, it): out += [f'{(float(x)-63)*1.22+64:.2f}', f'{(float(y)-69)*1.22+66:.2f}']
    v = iter(out); return re.sub(r'-?\d+\.?\d*', lambda m: next(v), d)
def C(x, y): return f'{(x-63)*1.22+64:.2f}', f'{(y-69)*1.22+66:.2f}'
(ex1, ey1), (ex2, ey2) = C(47, 58), C(78, 58)
SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" fill="none" stroke="currentColor" stroke-width="5.1" '
       'stroke-linecap="round" stroke-linejoin="round" class="uva-icon uva-user-avatar" aria-hidden="true">'
       '<style>.uva-user-avatar__ojo{fill:currentColor;stroke:none}</style>'
       f'<path d="{T("M38 51 Q46 43 55 49")}"/>'
       f'<circle class="uva-user-avatar__ojo" cx="{ex1}" cy="{ey1}" r="4.15"/><circle class="uva-user-avatar__ojo" cx="{ex2}" cy="{ey2}" r="4.15"/>'
       f'<path d="{T("M88 50 C82 44 72 45 68 52 L59 80 L68 81.5")}"/>'
       f'<path d="{T("M57 93 L71 92")}"/></svg>')
open('user-avatar.svg', 'w').write(SVG)

W, INKL, INK = '#FFFFFF', '#121826', '#052A76'
FONDOS = [('Gris','#D9DCE3'),('Azul real',INK),('Azul medio','#3D67AE'),('Cian','#00B4D8'),('Verde','#006D53'),('Verde claro','#38B000'),('Pera','#C2D225'),('Naranja','#F48C06'),('Café','#553739'),('Morado','#3D0066'),('Niebla','#E8EDF7')]
def lum(h):
    c = [int(h[i:i+2], 16)/255 for i in (1, 3, 5)]; c = [x/12.92 if x <= .03928 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a, b): la, lb = sorted([lum(a), lum(b)], reverse=True); return (la+.05)/(lb+.05)
def col(bg): return W if cr(W, bg) >= cr(INKL, bg) else INKL
def av(bg, z):
    s = SVG.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
    return f'<span class="av" style="width:{z}px;height:{z}px;background:{bg};color:{col(bg)}">{s}</span>'
sizes = ''.join(f'<figure>{av("#D9DCE3", z)}<figcaption>{z}</figcaption></figure>' for z in (128, 64, 40, 32, 24))
sws = ''.join(f'<figure>{av(bg, 56)}<figcaption>{n}</figcaption></figure>' for n, bg in FONDOS)
ctx = ''.join(f'<div class="li">{av(FONDOS[i][1], 32)}<span><b>{n}</b> {a}</span></div>' for n, a, i in [('Jorge Hernández', 'capturó <span class="m">0.0124 mg/L</span> · Plomo', 4), ('Óscar Zárate', 'envió el lote <span class="m">L-2026-10-147</span> a revisión', 9), ('Mariana Ruiz', 'liberó <span class="m">NN-26-00417</span>', 0)])
open('vista.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo';src:url('file://{S}/fuentes/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}@font-face{{font-family:'Plex';src:url('file://{S}/fuentes/IBMPlexMono.ttf')}}
body{{margin:0;background:#fff;color:#141B33;font:14px/1.45 Archivo,sans-serif;padding:32px;width:980px}}h1{{font-size:24px;font-stretch:125%;color:{INK};margin:0 0 4px}}.i{{margin:0 0 18px;color:#535B70}}
.row{{display:flex;gap:18px;align-items:end;flex-wrap:wrap;margin-bottom:22px}}figure{{margin:0;display:grid;justify-items:center;gap:6px;font-size:12px;color:#535B70}}
.av{{border-radius:50%;display:inline-flex;overflow:hidden}}.av svg{{display:block}}.li{{display:flex;gap:12px;align-items:center;margin:8px 0}}.m{{font-family:Plex,monospace;font-feature-settings:"zero"}}
</style></head><body><h1>Nabi · avatar unisex</h1><p class="i">Una sola cara para todas las personas, fiel a la de Notion. Solo cambia el fondo; la línea pasa sola a blanco o tinta.</p>
<div class="row">{sizes}</div><div class="row">{sws}</div><div>{ctx}</div></body></html>""")
print('ok')
