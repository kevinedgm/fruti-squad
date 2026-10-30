# NisaLab · símbolo propio: ocho conceptos del oficio de laboratorio. Sin matraz, sin la N de onda,
# sin los íconos de las divisiones (gota, surco, hoja, frasco, botella, agave, cápsula, lupa).
# Uso: python3 gen.py [carpeta-fuentes] → simbolos.html y svg/
import os, sys

H = os.path.dirname(os.path.abspath(__file__))
AZ, PE = '#052A76', '#C2D225'
L = f'fill="none" stroke="{AZ}" stroke-linecap="round" stroke-linejoin="round"'

def placa():
    c = ''.join(f'<circle cx="{x}" cy="{y}" r="13" fill="{PE if (x, y) == (82, 18) else AZ}"/>' for x in (18, 50, 82) for y in (18, 50, 82))
    return c
def pico():
    return (f'<path d="M6 86 H94" {L} stroke-width="8"/>'
            f'<path d="M10 86 C30 86 36 80 41 52 C45 28 55 28 59 52 C64 80 70 86 90 86" {L} stroke-width="9"/>'
            f'<circle cx="50" cy="14" r="9" fill="{PE}"/>')
def escala():
    bars = [(14, 40), (32, 62), (50, 76), (68, 62), (86, 40)]
    s = ''.join(f'<rect x="12" y="{y - 5}" width="{w}" height="10" rx="5" fill="{PE if y == 50 else AZ}"/>' for y, w in bars)
    return s + f'<rect x="84" y="6" width="10" height="88" rx="5" fill="{AZ}"/>'
def mira():
    t = ''.join(f'<path d="{d}" {L} stroke-width="9"/>' for d in ('M50 2 V20', 'M50 80 V98', 'M2 50 H20', 'M80 50 H98'))
    return f'<circle cx="50" cy="50" r="34" {L} stroke-width="9"/>{t}<circle cx="50" cy="50" r="11" fill="{PE}"/>'
def molecula():
    import math
    pts = [(50 + 38 * math.cos(math.radians(a)), 50 + 38 * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    p = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    n = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{12 if i == 1 else 8}" fill="{PE if i == 1 else AZ}"/>' for i, (x, y) in enumerate(pts))
    return f'<polygon points="{p}" {L} stroke-width="8"/>{n}'
def balanza():
    return (f'<path d="M50 14 V82 M30 92 H70" {L} stroke-width="9"/><path d="M12 30 H88" {L} stroke-width="9"/>'
            f'<path d="M2 52 A14 14 0 0 0 30 52 Z" fill="{AZ}"/><path d="M70 52 A14 14 0 0 0 98 52 Z" fill="{PE}"/>'
            f'<path d="M16 30 L6 52 M16 30 L26 52 M84 30 L74 52 M84 30 L94 52" {L} stroke-width="5"/><circle cx="50" cy="12" r="8" fill="{AZ}"/>')
def registros():
    return (f'<rect x="6" y="10" width="88" height="22" rx="11" fill="{AZ}"/><rect x="6" y="39" width="88" height="22" rx="11" fill="{PE}"/>'
            f'<rect x="6" y="68" width="88" height="22" rx="11" fill="{AZ}"/>'
            + ''.join(f'<circle cx="22" cy="{y}" r="5" fill="#fff"/>' for y in (21, 79)) + f'<circle cx="22" cy="50" r="5" fill="{AZ}"/>')
def prisma():
    return (f'<path d="M50 10 L90 82 H10 Z" {L} stroke-width="9"/><path d="M2 58 L40 50" {L} stroke-width="7"/>'
            f'<path d="M62 50 L98 40" {L} stroke-width="7"/><path d="M62 54 L98 60" fill="none" stroke="{PE}" stroke-width="7" stroke-linecap="round"/>')

C = [  # nombre, dibujo, qué cuenta, riesgo
    ('Placa', placa, 'Nueve pocillos de una placa de ensayo, uno con muestra. Es la idea del Nabi original, simplificada.', 'Puntos en cuadrícula: lo usan muchas apps (menús, dados).'),
    ('Pico', pico, 'El pico de un cromatograma: el momento en que el análisis encuentra algo.', 'Puede leerse como gráfica de finanzas o una montaña.'),
    ('Escala', escala, 'Las marcas de una probeta graduada, con la lectura en pera: medir con precisión.', 'Se parece a un ícono de alinear texto.'),
    ('Mira', mira, 'La retícula del microscopio centrada en la muestra: precisión y foco.', 'También es la mira de un arma.'),
    ('Molécula', molecula, 'Un anillo de seis átomos, uno destacado: química y estructura.', 'Es el símbolo genérico de «química»: poco propio.'),
    ('Balanza', balanza, 'Una balanza en equilibrio: el resultado fiel y justo.', 'Muy ligada a lo legal (justicia) y muchos trazos para 24 px.'),
    ('Registros', registros, 'Tres registros apilados, el del centro en pera: el sistema que ordena muestras, lotes y certificados.', 'Abstracto: no dice «laboratorio» por sí solo.'),
    ('Prisma', prisma, 'Un prisma que separa la luz, como un espectrofotómetro: analizar es descomponer.', 'Asociado a Pink Floyd y a marcas de tecnología.'),
]
def svg(fn):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 108 108">{fn()}</svg>'
def inl(s, h):
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block" aria-hidden="true" ', 1)
def blanco(s):  # versión sobre azul: todo el azul pasa a blanco
    return s.replace(AZ, '#FFFFFF')

os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
cards = ''
for i, (nom, fn, que, riesgo) in enumerate(C, 1):
    s = svg(fn)
    open(os.path.join(H, 'svg', f'{i:02d}-{nom.lower()}.svg'), 'w').write(s)
    cards += (f'<article><span class="n">{i}</span><div class="big">{inl(s, 110)}</div><h2>{nom}</h2><p>{que}</p><p class="r">Riesgo: {riesgo}</p>'
              f'<div class="lk">{inl(s, 40)}<div><span class="wm"><b>Nisa</b>Lab</span><small>de Nisa Nabani</small></div></div>'
              f'<div class="sm"><span class="tile">{inl(blanco(s), 30)}</span>{inl(s, 24)}{inl(s, 16)}</div></article>')

F = sys.argv[1] if len(sys.argv) > 1 else None
fuentes = ('<style>' + ''.join(f"@font-face{{font-family:Poppins;src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 600, 700)) + '</style>'
           if F else '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap">')
html = f'''<title>NisaLab · símbolos</title>
<meta name="claude:viewport-fit-sides" content="cover">
{fuentes}
<style>
/* Catálogo para elegir un símbolo: blanco, tinta y azul real; Poppins como en el manual. */
:root{{--az:{AZ};--fg:#141B33;--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:16px/1.5 Poppins,system-ui,sans-serif;padding-block:0 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1180px;margin:0 auto}} header{{padding:40px 0 22px;display:grid;gap:8px}} h1{{margin:0;font:700 clamp(28px,5vw,42px)/1.1 Poppins,sans-serif;letter-spacing:-.02em}} header p{{margin:0;color:var(--muted);max-width:72ch}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}}
article{{position:relative;border:1px solid var(--line);border-radius:18px;padding:16px;display:grid;gap:6px;align-content:start}}
.n{{position:absolute;top:12px;left:12px;font:700 13px Poppins,sans-serif;color:var(--muted)}} .big{{display:grid;place-items:center;background:var(--sunk);border-radius:14px;height:150px}}
h2{{margin:6px 0 0;font:700 18px/1.2 Poppins,sans-serif}} article p{{margin:0;font-size:14px;color:var(--muted);line-height:1.45}} .r{{color:#8A1A12 !important}}
.lk{{display:flex;align-items:center;gap:10px;margin-top:6px}} .wm{{font-size:22px;color:var(--az);line-height:1;display:block}} .wm b{{font-weight:700}} .lk small{{font-size:12px;color:var(--muted)}}
.sm{{display:flex;align-items:center;gap:12px;margin-top:4px}} .tile{{display:grid;place-items:center;width:44px;height:44px;border-radius:10px;background:var(--az)}}
</style>
<main><header><h1>Un símbolo propio para NisaLab</h1><p>Ocho conceptos del oficio de laboratorio. Ninguno usa la N de Nisa, el matraz ni los íconos de las divisiones. La relación con Nisa Nabani la dan el azul real, el pera y el «de Nisa Nabani». Cada uno se ve grande, con el nombre, como ícono de app sobre azul y a 24 y 16 px.</p></header>
<div class="g">{cards}</div></main>'''
open(os.path.join(H, 'simbolos.html'), 'w').write(html)
print('ok')
