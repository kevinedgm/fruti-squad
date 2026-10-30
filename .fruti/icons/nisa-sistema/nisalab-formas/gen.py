# NisaLab · catálogo de formas: diez contenedores para la N, sin cuadro, sin matraz.
# Uso: python3 gen.py [carpeta-fuentes] → formas.html y svg/
import os, re, sys

H = os.path.dirname(os.path.abspath(__file__))
MARCA = os.path.join(H, '..', 'nabi-design-system', 'marca-nisa')
AZ, PE, W = '#052A76', '#C2D225', '#FFFFFF'
_s = open(os.path.join(MARCA, 'nisa-nabani-n.svg')).read()
NV = [float(v) for v in re.search(r'viewBox="([^"]*)"', _s).group(1).split()]
NP = [(m.group(1), m.group(2)) for m in re.finditer(r'<path[^>]*fill="([^"]*)"[^>]*d="([^"]*)"', _s)]
def N(cx, cy, w):
    k = w / NV[2]
    t = f'translate({cx} {cy}) scale({k:.4f}) translate({-(NV[0] + NV[2] / 2):.2f} {-(NV[1] + NV[3] / 2):.2f})'
    return f'<g transform="{t}">' + ''.join(f'<path d="{d}" fill="{PE if f.startswith("rgb(76") else W}"/>' for f, d in NP) + '</g>'

def poly(pts, r=12):  # polígono con esquinas redondeadas (trazo del mismo color)
    p = ' '.join(f'{x},{y}' for x, y in pts)
    return f'<polygon points="{p}" fill="{AZ}" stroke="{AZ}" stroke-width="{r}" stroke-linejoin="round"/>'
def path(d, r=0):
    return f'<path d="{d}" fill="{AZ}"' + (f' stroke="{AZ}" stroke-width="{r}" stroke-linejoin="round"' if r else '') + '/>'

FORMAS = [  # nombre, forma, (cx, cy, ancho N), idea
    ('Círculo', '<circle cx="50" cy="50" r="50" fill="#052A76"/>', (50, 52, 70), 'El pocillo visto desde arriba.'),
    ('Hexágono', poly([(27, 6), (73, 6), (95, 50), (73, 94), (27, 94), (5, 50)], 12), (50, 52, 68), 'La molécula: química y estructura.'),
    ('Cápsula', '<rect x="0" y="20" width="100" height="60" rx="30" fill="#052A76"/>', (50, 51, 66), 'Horizontal y suave, como una píldora o un botón.'),
    ('Escudo', path('M10 8 H90 V46 C90 74 70 90 50 98 C30 90 10 74 10 46 Z', 10), (50, 46, 62), 'Garantía y calidad certificada.'),
    ('Rombo', poly([(50, 4), (96, 50), (50, 96), (4, 50)], 14), (50, 52, 56), 'Una señal: precisa y alerta.'),
    ('Arco', path('M6 98 V48 A44 44 0 0 1 94 48 V98 Z', 10), (50, 64, 66), 'Una puerta o ventana: entrar al laboratorio.'),
    ('Ojo', path('M2 50 Q50 -8 98 50 Q50 108 2 50 Z'), (50, 52, 60), 'Observar y revisar.'),
    ('Octágono', poly([(30, 4), (70, 4), (96, 30), (96, 70), (70, 96), (30, 96), (4, 70), (4, 30)], 10), (50, 52, 70), 'Sólido, institucional, como un sello.'),
    ('Paralelogramo', poly([(24, 10), (96, 10), (76, 90), (4, 90)], 12), (50, 52, 66), 'Inclinado: movimiento y avance.'),
    ('Orgánica', path('M54 3 C84 6 99 28 96 56 C93 84 70 99 44 96 C17 93 1 72 4 46 C7 19 26 0 54 3 Z'), (50, 52, 70), 'Una forma libre, como una gota de muestra vista al microscopio.'),
]
def svg(forma, n):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-6 -6 112 112">{forma}{N(*n)}</svg>'
def inl(s, h):
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block" aria-hidden="true" ', 1)

os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
cards = ''
for i, (nom, f, n, idea) in enumerate(FORMAS, 1):
    s = svg(f, n)
    open(os.path.join(H, 'svg', f'{i:02d}-{nom.lower()}.svg'), 'w').write(s)
    cards += (f'<article><span class="n">{i}</span><div class="big">{inl(s, 120)}</div><h2>{nom}</h2><p>{idea}</p>'
              f'<div class="sm">{inl(s, 40)}{inl(s, 24)}<span class="wm"><b>Nisa</b>Lab</span></div></article>')

F = sys.argv[1] if len(sys.argv) > 1 else None
fuentes = ('<style>' + ''.join(f"@font-face{{font-family:Poppins;src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 600, 700)) + '</style>'
           if F else '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap">')
html = f'''<title>NisaLab · formas</title>
<meta name="claude:viewport-fit-sides" content="cover">
{fuentes}
<style>
/* Catálogo para elegir una forma: blanco, tinta y azul real; Poppins como en el manual. */
:root{{--az:{AZ};--fg:#141B33;--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:16px/1.5 Poppins,system-ui,sans-serif;padding-block:0 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1180px;margin:0 auto}} header{{padding:40px 0 22px;display:grid;gap:8px}} h1{{margin:0;font:700 clamp(28px,5vw,42px)/1.1 Poppins,sans-serif;letter-spacing:-.02em}} header p{{margin:0;color:var(--muted);max-width:70ch}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}}
article{{position:relative;border:1px solid var(--line);border-radius:18px;padding:16px;display:grid;gap:6px;align-content:start}}
.n{{position:absolute;top:12px;left:12px;font:700 13px Poppins,sans-serif;color:var(--muted)}} .big{{display:grid;place-items:center;background:var(--sunk);border-radius:14px;height:160px}}
h2{{margin:6px 0 0;font:700 18px/1.2 Poppins,sans-serif}} article p{{margin:0;font-size:14px;color:var(--muted);line-height:1.4;min-height:40px}}
.sm{{display:flex;align-items:center;gap:10px;margin-top:4px}} .wm{{font-size:18px;color:var(--az)}} .wm b{{font-weight:700}}
</style>
<main><header><h1>¿Qué forma tiene NisaLab?</h1><p>Diez contenedores para la misma N, sin cuadro y sin matraz. Solo cambia la forma. Elige una o dos y las desarrollo.</p></header>
<div class="g">{cards}</div></main>'''
open(os.path.join(H, 'formas.html'), 'w').write(html)
print('ok')
