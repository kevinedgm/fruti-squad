# NisaLab · áreas, ronda 2: íconos y colores propios (no los del manual), unidos a Colonia.
# Colores: OKLCH con L 0.54 y C 0.12 iguales; solo cambia el tono, sin tocar el rango del pera (100–125°).
# Íconos: dibujados en una retícula de 40, formas redondas y blancas, como las células de Colonia.
# Uso: python3 gen.py [carpeta-fuentes] → areas.html y svg/
import math, os, re, sys

H = os.path.dirname(os.path.abspath(__file__))
NS = os.path.join(H, '..')
AZ, PE, W, TINTA = '#052A76', '#C2D225', '#FFFFFF', '#141B33'
L_, C_ = 0.54, 0.12

def oklch(h):
    a, b = C_ * math.cos(math.radians(h)), C_ * math.sin(math.radians(h))
    l_ = L_ + 0.3963377774 * a + 0.2158037573 * b; m_ = L_ - 0.1055613458 * a - 0.0638541728 * b; s_ = L_ - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    rgb = [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s]
    f = lambda x: (lambda x: 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055)(max(0, min(1, x)))
    return '#' + ''.join(f'{round(f(v) * 255):02X}' for v in rgb)
def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)

S4 = 'fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"'
S35 = S4.replace('stroke-width="4"', 'stroke-width="3.5"')
def hoja(rot):
    return f'<path d="M20 34 L17 15 L20 5 L23 15 Z" fill="#fff" transform="rotate({rot} 20 34)"/>'
ICON = {
    'aguas': lambda c: f'<path d="M6 15 q3.5 -5 7 0 t7 0 t7 0 t7 0" {S4}/><path d="M6 25 q3.5 -5 7 0 t7 0 t7 0 t7 0" {S4}/><path d="M10 34 H30" {S4}/>',
    'agricolas': lambda c: (f'<path d="M20 38 V10" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' + ''.join(f'<ellipse cx="{20 + dx}" cy="{y}" rx="2.6" ry="5.6" fill="#fff" transform="rotate({ang} {20 + dx} {y})"/>' for y in (14, 21, 28) for dx, ang in ((-4.6, -38), (4.6, 38))) + '<ellipse cx="20" cy="6.5" rx="2.6" ry="5" fill="#fff"/>'),
    'ambiental': lambda c: f'<path d="M7 33 C7 15 19 6 34 6 C34 22 25 34 7 33 Z" fill="#fff"/><path d="M8 32 L25 15" stroke="{c}" stroke-width="2.8" stroke-linecap="round"/>',
    'alimentos': lambda c: '<circle cx="15" cy="24" r="10" fill="#fff"/><circle cx="25" cy="24" r="10" fill="#fff"/><path d="M20 15 V8" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><ellipse cx="25.5" cy="9" rx="5" ry="2.8" fill="#fff" transform="rotate(-25 25.5 9)"/>',
    'bebidas': lambda c: f'<path d="M10 7 H30 L27 34 H13 Z" {S35}/><path d="M11.4 19 H28.6 L27 34 H13 Z" fill="#fff"/>',
    'agave': lambda c: ''.join(hoja(r) for r in (-52, -26, 0, 26, 52)) + '<path d="M11 36 H29" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/>',
    'farmacia': lambda c: f'<g transform="rotate(-45 20 20)"><rect x="5" y="13" width="30" height="14" rx="7" fill="none" stroke="#fff" stroke-width="3.5"/><path d="M12 13 H20 V27 H12 A7 7 0 0 1 12 13 Z" fill="#fff"/></g>',
    'consultoria': lambda c: f'<path d="M12 6 H28 A8 8 0 0 1 36 14 V21 A8 8 0 0 1 28 29 H19 L11 36 V29 A8 8 0 0 1 4 21 V14 A8 8 0 0 1 12 6 Z" fill="#fff"/>' + ''.join(f'<circle cx="{x}" cy="17.5" r="2.6" fill="{c}"/>' for x in (13, 20, 27)),
}
AREAS = [  # clave, nombre, tono
    ('aguas', 'Aguas', 225), ('agricolas', 'Agrícolas', 78), ('ambiental', 'Ambiental', 150), ('alimentos', 'Alimentos', 45),
    ('bebidas', 'Bebidas', 300), ('agave', 'Bebidas de agave', 185), ('farmacia', 'Farmacia', 350), ('consultoria', 'Consultoría', 265),
]
AREAS = [(k, n, oklch(h)) for k, n, h in AREAS]

_s = open(os.path.join(NS, 'nisalab-final', 'svg', 'simbolo.svg')).read()
CEL = [(float(x), float(y), float(r), c) for x, y, r, c in re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)" fill="([^"]+)"', _s)]
gx, gy, gr, _ = next(c for c in CEL if c[3] == PE)

def marca(k, color):
    base = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{AZ}"/>' for x, y, r, c in CEL if c != PE)
    s = gr * 2 * 0.62 / 40
    ico = f'<g transform="translate({gx - 20 * s:.2f} {gy - 20 * s:.2f}) scale({s:.3f})">{ICON[k](color)}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 104 104">{base}<circle cx="{gx}" cy="{gy}" r="{gr}" fill="{color}"/>{ico}</svg>'
def chip(k, color):  # el ícono solo, en círculo: listas, filtros y etiquetas
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="24" fill="{color}"/><g transform="translate(6.5 6.5) scale(.875)">{ICON[k](color)}</g></svg>'
def inl(s, h):
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block;flex:none" aria-hidden="true" ', 1)

os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
for k, n, c in AREAS:
    open(os.path.join(H, 'svg', f'marca-{k}.svg'), 'w').write(marca(k, c))
    open(os.path.join(H, 'svg', f'icono-{k}.svg'), 'w').write(chip(k, c))

paleta = ''.join(f'<div class="sw" style="background:{c}"><b>{n}</b><span>{c}</span><span>Blanco encima {cr(W, c)}:1</span></div>' for k, n, c in AREAS)
marcas = ''.join(f'<figure>{inl(marca(k, c), 96)}<div class="sm">{inl(marca(k, c), 32)}{inl(marca(k, c), 24)}</div><figcaption><b>{n}</b> NisaLab</figcaption></figure>' for k, n, c in AREAS)
iconos = ''.join(f'<figure class="ic">{inl(chip(k, c), 56)}<figcaption>{n}</figcaption></figure>' for k, n, c in AREAS)
chips = ''.join(f'<span class="tag">{inl(chip(k, c), 20)}{n}</span>' for k, n, c in AREAS)
ak, an, ac = AREAS[0]

F = sys.argv[1] if len(sys.argv) > 1 else None
fuentes = ('<style>' + ''.join(f"@font-face{{font-family:Poppins;src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 600, 700)) + '</style>'
           if F else '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap">')
logo = open(os.path.join(NS, 'nisalab-final', 'svg', 'logotipo.svg')).read().replace('<svg ', '<svg style="height:44px;width:auto;display:block" ', 1)
html = f'''<title>NisaLab · áreas 2</title>
<meta name="claude:viewport-fit-sides" content="cover">
{fuentes}
<style>
/* Lámina de áreas: blanco, tinta y azul real de Nisa Nabani; Poppins como en el manual. */
:root{{--az:{AZ};--fg:{TINTA};--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:16px/1.55 Poppins,system-ui,sans-serif;padding-block:0 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1180px;margin:0 auto}} header{{padding:40px 0 24px;display:grid;gap:12px;border-bottom:1px solid var(--line)}}
h1{{margin:0;font:700 clamp(28px,5vw,42px)/1.1 Poppins,sans-serif;letter-spacing:-.02em}} h2{{margin:0 0 6px;font:700 22px/1.2 Poppins,sans-serif}} p{{margin:0;max-width:72ch}} .muted{{color:var(--muted)}}
section{{padding:30px 0;border-bottom:1px solid var(--line)}}
.pal{{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));margin-top:12px}} .sw{{border-radius:14px;padding:12px;min-height:96px;color:#fff;display:grid;align-content:end;gap:1px;font-size:12px}} .sw b{{font-size:14px}}
.fila{{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));margin-top:12px}} figure{{margin:0;border:1px solid var(--line);border-radius:16px;padding:14px 8px;display:grid;justify-items:center;gap:8px;text-align:center}}
.sm{{display:flex;gap:10px;align-items:center;background:var(--sunk);border-radius:8px;padding:6px 10px}} figcaption{{font-size:13px;line-height:1.3;color:var(--muted)}} figcaption b{{color:var(--fg);font-weight:600}}
.ic{{border:0;padding:6px}} .tags{{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}} .tag{{display:inline-flex;align-items:center;gap:6px;background:var(--sunk);border-radius:999px;padding:4px 12px 4px 4px;font-size:14px;font-weight:500}}
.bar{{display:flex;align-items:center;gap:12px;height:60px;padding:0 14px;border:1px solid var(--line);border-radius:14px;margin-top:12px;max-width:640px}} .nm{{font-size:17px;color:var(--muted)}} .nm b{{color:var(--fg);font-weight:600}} .sp{{flex:1}}
</style>
<main><header>{logo}<h1>Áreas con íconos y colores propios</h1>
<p class="muted">Íconos nuevos, dibujados con las formas redondas de Colonia, y una paleta nueva: los ocho colores tienen la misma luminosidad y la misma intensidad, solo cambia el tono, para que ninguno pese más que otro y ninguno se acerque al pera de NisaLab. Cada área se nombra «Área NisaLab».</p></header>
<section><h2>Paleta de áreas</h2><p class="muted">El blanco sobre los ocho colores pasa 4.5:1: los íconos y textos blancos encima se leen.</p><div class="pal">{paleta}</div></section>
<section><h2>Marca de cada área</h2><p class="muted">La célula que creció toma el color y el ícono del área; el resto del racimo sigue azul.</p><div class="fila">{marcas}</div></section>
<section><h2>Íconos</h2><p class="muted">El ícono solo, en círculo, para listas, filtros y etiquetas dentro de NisaLab.</p><div class="fila">{iconos}</div><div class="tags">{chips}</div>
<div class="bar">{inl(marca(ak, ac), 34)}<span class="nm"><b>{an}</b> NisaLab</span><span class="sp"></span></div></section>
</main>'''
open(os.path.join(H, 'areas.html'), 'w').write(html)
print('ok', [(n, c, cr(W, c)) for k, n, c in AREAS])
