# NisaLab · ronda 2: variaciones de la dirección A (cuadro con la N). Sin matraz y sin parecerse al logo de la empresa.
# Uso: python3 gen.py [carpeta-fuentes] → lamina.html y svg/
# La N de onda es el vector del manual (marca-nisa/nisa-nabani-n.svg): se recolorea, nunca se redibuja.
import os, re, sys

H = os.path.dirname(os.path.abspath(__file__))
NS = os.path.join(H, '..')
MARCA = os.path.join(NS, 'nabi-design-system', 'marca-nisa')
AZ, PE, W, TINTA = '#052A76', '#C2D225', '#FFFFFF', '#141B33'

_s = open(os.path.join(MARCA, 'nisa-nabani-n.svg')).read()
NV = [float(v) for v in re.search(r'viewBox="([^"]*)"', _s).group(1).split()]
NP = [(m.group(1), m.group(2)) for m in re.finditer(r'<path[^>]*fill="([^"]*)"[^>]*d="([^"]*)"', _s)]
def N(cx, cy, w, azul, pera):
    k = w / NV[2]
    t = f'translate({cx} {cy}) scale({k:.4f}) translate({-(NV[0] + NV[2] / 2):.2f} {-(NV[1] + NV[3] / 2):.2f})'
    return f'<g transform="{t}">' + ''.join(f'<path d="{d}" fill="{pera if f.startswith("rgb(76") else azul}"/>' for f, d in NP) + '</g>'

def rr(x, y, w, h, r):
    return f'M{x+r} {y} H{x+w-r} A{r} {r} 0 0 1 {x+w} {y+r} V{y+h-r} A{r} {r} 0 0 1 {x+w-r} {y+h} H{x+r} A{r} {r} 0 0 1 {x} {y+h-r} V{y+r} A{r} {r} 0 0 1 {x+r} {y} Z'
Q = rr(0, 0, 100, 100, 21)
_u = [0]
def uid():
    _u[0] += 1; return f'q{_u[0]}'

def v1(inv=False):  # Pera: el único cuadro pera del ecosistema
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 104 104"><path d="{Q}" fill="{PE}"/>{N(50, 52, 72, AZ, AZ)}</svg>'
def v2(inv=False):  # Nivel: cuadro azul con un nivel pera, como una muestra
    u = uid()
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 104 104"><defs><clipPath id="{u}"><path d="{Q}"/></clipPath></defs>'
            f'<path d="{Q}" fill="{AZ}"/><g clip-path="url(#{u})"><path d="M-2 74 C20 66 36 82 58 74 S88 66 102 72 V104 H-2 Z" fill="{PE}"/></g>{N(50, 44, 70, W, W)}</svg>')
def v3(inv=False):  # Desborde: la onda cruza el cuadro
    u = uid()
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-30 -2 160 104"><defs><clipPath id="{u}"><path d="{Q}"/></clipPath></defs>'
            f'{N(50, 52, 150, AZ, PE)}<path d="{Q}" fill="{AZ}"/><g clip-path="url(#{u})">{N(50, 52, 150, W, PE)}</g></svg>')
def v4(inv=False):  # Mosaico: cuatro cuadros, uno pera; la N los cruza
    u = uid()
    tiles = [(0, 0, AZ), (52, 0, AZ), (0, 52, AZ), (52, 52, PE)]
    clip = ''.join(f'<path d="{rr(x, y, 48, 48, 12)}"/>' for x, y, _ in tiles)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 104 104"><defs><clipPath id="{u}">{clip}</clipPath></defs>'
            + ''.join(f'<path d="{rr(x, y, 48, 48, 12)}" fill="{c}"/>' for x, y, c in tiles)
            + f'<g clip-path="url(#{u})">{N(50, 50, 84, W, W)}</g></svg>')
def v5(inv=False):  # Palabra: el ícono de app es el cuadro base; la identidad la carga el logotipo
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 104 104"><path d="{Q}" fill="{AZ}"/>{N(50, 52, 72, W, PE)}</svg>'

def palabra(k, tam=44, color=AZ):
    if k == 5:  # la N de onda es la N del nombre
        return (f'<span class="wm" style="font-size:{tam}px;color:{color}">'
                f'<svg viewBox="{NV[0]} {NV[1]} {NV[2]} {NV[3]}" style="height:{tam * .78:.0f}px;width:auto;margin-right:2px" aria-hidden="true">'
                + ''.join(f'<path d="{d}" fill="{PE if f.startswith("rgb(76") else color}"/>' for f, d in NP)
                + f'</svg><b style="font-weight:700">isa</b><span style="font-weight:400">Lab</span></span>')
    return f'<span class="wm" style="font-size:{tam}px;color:{color}"><b style="font-weight:700">Nisa</b><span style="font-weight:400">Lab</span></span>'

V = [
    (1, v1, 'Pera', 'El mismo cuadro, pero en pera: NisaLab es el único cuadro pera del ecosistema; todos los productos son azules. La N va en azul, a una tinta.',
     ['Se distingue de cualquier producto a primera vista.', 'Usa los dos colores del manual sin agregar nada.'],
     ['El pera domina: sobre fondos claros pierde presencia (el pera sobre blanco es 1.7:1 como contorno).']),
    (2, v2, 'Nivel', 'Cuadro azul con un nivel pera en la parte baja, como una muestra en un tubo, sin dibujar el tubo. La N va en blanco.',
     ['Cuenta «laboratorio» sin matraz.', 'Funciona a 24 px: se ve el nivel.'],
     ['La N pierde su pera para no fundirse con el nivel.', 'El nivel puede leerse como «carga» o «progreso».']),
    (3, v3, 'Desborde', 'La onda de la N es más grande que el cuadro y lo cruza: fuera del cuadro es azul y pera, dentro es blanca y pera.',
     ['El más dinámico: la onda «sale» del sistema.', 'Ningún producto lo hace: es exclusivo de NisaLab.'],
     ['Es horizontal: como ícono de app se usa solo el cuadro.', 'A 24 px la parte que desborda se pierde.']),
    (4, v4, 'Mosaico', 'Cuatro cuadros, uno pera, y la N los cruza en blanco: el sistema hecho de partes, como el mosaico del Ecosistema Manik.',
     ['Dice «sistema de varios productos».', 'Encaja con la regla de Manik: el sistema tiene un emblema distinto a las apps.'],
     ['La N queda partida por las separaciones.', 'Es el más cargado de los cinco.']),
    (5, v5, 'Palabra', 'El ícono es el cuadro base, igual al de los productos sin rasgo; la identidad la carga el logotipo, donde la N de onda es la N de «NisaLab».',
     ['El logotipo es único y se lee como palabra.', 'El ícono es el más simple del ecosistema.'],
     ['En el ícono de app, NisaLab y un producto se distinguen solo por el rasgo.']),
]

_PROD = open(os.path.join(NS, 'ecosistema-ronda-1', 'svg', 'a-recepcion.svg')).read()
def prod():
    u = uid()
    return re.sub(r'(id="|url\(#)([^")]+)', lambda m: m.group(1) + m.group(2) + u, _PROD)
def inl(svg, h):
    return svg.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block" aria-hidden="true" ', 1)

def tarjeta(k, fn, nom, idea, pros, contras):
    s = fn()
    logo = f'<div class="lg">{inl(fn(), 56)}{palabra(k, 38)}</div>' if k != 5 else f'<div class="lg">{palabra(5, 46)}</div>'
    app = inl(v5() if k == 3 else fn(), 48)
    tam = ''.join(f'<span>{inl(v5() if k == 3 else fn(), z)}</span>' for z in (48, 32, 24, 16))
    jun = f'<div class="jun"><div>{app}<span>NisaLab</span></div><div>{inl(prod(), 48)}<span>Recepción NisaLab</span></div></div>'
    return f'''<article><div class="hd"><span class="num">{k}</span><h2>{nom}</h2></div><div class="big">{inl(s, 120)}</div>
<p class="idea">{idea}</p><h3>Logotipo</h3>{logo}<h3>Ícono de app · 48, 32, 24 y 16</h3><div class="tam">{tam}</div>
<h3>Junto a un producto</h3>{jun}
<ul class="pro">{"".join(f"<li>{x}</li>" for x in pros)}</ul><ul class="con">{"".join(f"<li>{x}</li>" for x in contras)}</ul></article>'''

os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
for k, fn, nom, *_ in V:
    open(os.path.join(H, 'svg', f'v{k}-{nom.lower()}.svg'), 'w').write(fn())

F = sys.argv[1] if len(sys.argv) > 1 else None
fuentes = ('<style>' + ''.join(f"@font-face{{font-family:Poppins;src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 600, 700)) + '</style>'
           if F else '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap">')
html = f'''<title>NisaLab · ronda 2</title>
<meta name="claude:viewport-fit-sides" content="cover">
{fuentes}
<style>
/* Lámina de decisión: blanco, tinta y azul real de Nisa Nabani; Poppins como en el manual. */
:root{{--az:{AZ};--pe:{PE};--fg:{TINTA};--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:16px/1.55 Poppins,system-ui,sans-serif;padding-block:0 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1180px;margin:0 auto}} header{{padding:40px 0 24px;display:grid;gap:10px}}
.ov{{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}} h1{{margin:0;font:700 clamp(28px,5vw,44px)/1.1 Poppins,sans-serif;letter-spacing:-.02em}} p{{margin:0;max-width:72ch}}
.g{{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(330px,1fr))}}
article{{border:1px solid var(--line);border-radius:20px;padding:20px;display:grid;gap:10px;align-content:start;min-width:0}}
.hd{{display:flex;gap:10px;align-items:center}} .num{{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--az);color:#fff;font:700 14px Poppins,sans-serif}} h2{{margin:0;font:700 22px/1.2 Poppins,sans-serif}}
h3{{margin:6px 0 0;font:600 12px/1.4 Poppins,sans-serif;color:var(--muted);letter-spacing:.04em;text-transform:uppercase}}
.big{{background:var(--sunk);border-radius:16px;display:grid;place-items:center;padding:24px;min-height:150px}} .idea{{font-size:14px;color:var(--muted);line-height:1.5}}
.lg{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;min-height:60px}} .wm{{display:inline-flex;align-items:baseline;line-height:1;letter-spacing:-.015em;white-space:nowrap}}
.tam{{display:flex;gap:12px;align-items:flex-end}} .jun{{display:flex;gap:22px}} .jun div{{display:grid;justify-items:center;gap:4px;font-size:13px;font-weight:600}}
.pro,.con{{margin:0;padding-left:20px;font-size:14px;line-height:1.45;border-radius:12px;padding:10px 12px 10px 30px}} .pro{{background:#EEF4D6}} .con{{background:#FBEDEE}}
.rec{{background:var(--sunk);border-radius:18px;padding:20px 22px;margin-top:24px;display:grid;gap:8px}}
</style>
<main><header><span class="ov">NisaLab · ronda 2 · variaciones de A</span><h1>El cuadro con la N, cinco maneras</h1>
<p style="color:var(--muted)">Todas parten del sello A: la N de onda del manual dentro de un cuadro, con el nombre en Poppins. La pregunta es qué hace a NisaLab distinto de sus productos, que también serán cuadros azules (como «Recepción», a la derecha en cada tarjeta).</p></header>
<div class="g">{"".join(tarjeta(*v) for v in V)}</div>
<div class="rec"><b>Recomendación: 1 · Pera</b><p>Con confianza media. Es la diferencia más simple y más visible: un solo cambio de color, con los dos colores del manual, y NisaLab nunca se confunde con un producto. Si buscas más movimiento, la alternativa es <b>3 · Desborde</b>, que usa el cuadro pera o azul como ícono y la onda completa en el logotipo. Es criterio de diseño, no está probado con usuarios.</p></div>
</main>'''
open(os.path.join(H, 'lamina.html'), 'w').write(html)
print('ok')
