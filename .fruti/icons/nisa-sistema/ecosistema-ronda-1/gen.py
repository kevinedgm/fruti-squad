# Ecosistema Nisa · ronda 1 de identidad: tres sistemas de sello para los productos de Nisa Nabani.
# Uso: python3 gen.py [carpeta-fuentes]  → lamina.html y svg/
# Sin argumento usa Google Fonts; con carpeta usa @font-face locales para capturar sin red.
# La N de onda es el vector del manual (marca-nisa/nisa-nabani-n.svg): nunca se redibuja.
import os, re, sys

H = os.path.dirname(os.path.abspath(__file__))
MARCA = os.path.join(H, '..', 'nabi-design-system', 'marca-nisa')
AZ, PE, PAPEL, TINTA, LT = '#052A76', '#C2D225', '#FFFFFF', '#141B33', '#768AB4'

_n = open(os.path.join(MARCA, 'nisa-nabani-n.svg')).read()
NVB = [float(v) for v in re.search(r'viewBox="([^"]*)"', _n).group(1).split()]
NP = [(m.group(1), m.group(2)) for m in re.finditer(r'<path[^>]*fill="([^"]*)"[^>]*d="([^"]*)"', _n)]
def N(cx, cy, w, azul, pera):
    """La N de onda centrada en (cx, cy) con ancho w; azul y pera recoloreables."""
    k = w / NVB[2]
    tx, ty = -(NVB[0] + NVB[2] / 2), -(NVB[1] + NVB[3] / 2)
    ps = ''.join(f'<path d="{d}" fill="{pera if f.startswith("rgb(76") else azul}"/>' for f, d in NP)
    return f'<g transform="translate({cx} {cy}) scale({k:.4f}) translate({tx:.2f} {ty:.2f})">{ps}</g>'

R = 21
Q = f'M{R} 0 H{100-R} A{R} {R} 0 0 1 100 {R} V{100-R} A{R} {R} 0 0 1 {100-R} 100 H{R} A{R} {R} 0 0 1 0 {100-R} V{R} A{R} {R} 0 0 1 {R} 0 Z'
VB = '-14 -16 128 128'

PROD = [  # clave, nombre, para quién, rasgo
    ('madre', 'Nisa Nabani', 'La empresa', 'cuadro limpio'),
    ('recepcion', 'Recepción', 'Personal de recepción', 'etiqueta colgante'),
    ('analisis', 'Análisis', 'Analistas', 'tres pocillos'),
    ('calidad', 'Calidad', 'Supervisores de calidad', 'borde de sello'),
    ('clientes', 'Clientes', 'Clientes del laboratorio', 'esquina doblada'),
    ('admin', 'Administración', 'Administradores', 'tarjeta detrás'),
]

# ---------- A · Contenedor ----------
TAG = 'M-8 -5 L0 -14 L8 -5 V11 A3 3 0 0 1 5 14 H-5 A3 3 0 0 1 -8 11 Z'
def piezas(k):
    """Piezas separadas del cuadro (se recortan del cuadro con un corte)."""
    if k == 'recepcion':
        return [f'<g transform="translate(93 7) rotate(45)"><path d="{TAG}"/></g>'], [f'<circle cx="97" cy="-3" r="0"/>']
    if k == 'analisis':
        return [f'<circle cx="{x}" cy="100" r="7"/>' for x in (30, 50, 70)], []
    return [], []
def sello_a(k, uid, inv=False):
    fondo, linea, pera, pieza = (PAPEL, AZ, PE, PAPEL) if inv else (AZ, PAPEL, PE, AZ)
    m = f'm{uid}'
    shapes, _ = piezas(k)
    cuadro = Q
    extra_back = extra_front = ''
    mask = ''
    if k == 'calidad':  # silueta de sello: bordes festoneados
        bumps = ''.join(f'<circle cx="{x}" cy="{y}" r="8"/>' for x in (30, 50, 70) for y in (0, 100)) + ''.join(f'<circle cx="{x}" cy="{y}" r="8"/>' for y in (30, 50, 70) for x in (0, 100))
        extra_back = f'<g fill="{fondo}">{bumps}</g>'
    if k == 'clientes':
        cuadro = f'M{R} 0 H70 L100 30 V{100-R} A{R} {R} 0 0 1 {100-R} 100 H{R} A{R} {R} 0 0 1 0 {100-R} V{R} A{R} {R} 0 0 1 {R} 0 Z'
        extra_front = f'<path d="M76 2 L98 24 H82 A6 6 0 0 1 76 18 Z" fill="{PE}"/>'
    if k == 'recepcion':
        extra_front = f'<g transform="translate(93 7) rotate(45)"><circle cx="0" cy="-4" r="3" fill="{PAPEL}"/></g>'
    if k == 'admin':
        mask = (f'<mask id="{m}b" maskUnits="userSpaceOnUse" x="-14" y="-16" width="128" height="128"><rect x="-14" y="-16" width="128" height="128" fill="#fff"/>'
                f'<path d="{Q}" fill="#000" stroke="#000" stroke-width="10"/></mask>')
        extra_back = f'<g mask="url(#{m}b)"><path d="{Q}" transform="translate(11 -11)" fill="{LT if not inv else PAPEL}"/></g>'
    if shapes:
        mask += (f'<mask id="{m}" maskUnits="userSpaceOnUse" x="-14" y="-16" width="128" height="128"><rect x="-14" y="-16" width="128" height="128" fill="#fff"/>'
                 f'<g fill="#000" stroke="#000" stroke-width="10">{"".join(shapes)}</g></mask>')
        body = f'<g mask="url(#{m})"><path d="{cuadro}" fill="{fondo}"/>{extra_back}</g><g fill="{pieza}">{"".join(shapes)}</g>'
    else:
        body = f'{extra_back}<path d="{cuadro}" fill="{fondo}"/>'
    stroke = f' stroke="{AZ}" stroke-width="2"' if inv else ''
    if inv:
        body = body.replace(f'<path d="{cuadro}" fill="{fondo}"/>', f'<path d="{cuadro}" fill="{fondo}"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}"><defs>{mask}</defs>{body}{N(50, 52, 72, linea, pera)}{extra_front}</svg>'

# ---------- B · Variación del manual (N + ícono) ----------
def icono_b(k):
    if k == 'recepcion':
        return f'<g transform="translate(20 22) scale(1.25)"><path d="{TAG}" fill="{AZ}"/><circle cx="0" cy="-5" r="2.6" fill="{PAPEL}"/></g>'
    if k == 'analisis':
        return f'<rect x="2" y="9" width="36" height="24" rx="6" fill="{AZ}"/>' + ''.join(f'<circle cx="{x}" cy="21" r="4.2" fill="{PAPEL}"/>' for x in (11, 20, 29))
    if k == 'calidad':
        b = ''.join(f'<circle cx="{20 + 14 * __import__("math").cos(a * 0.6283):.2f}" cy="{21 + 14 * __import__("math").sin(a * 0.6283):.2f}" r="5.5"/>' for a in range(10))
        return f'<g fill="{AZ}"><circle cx="20" cy="21" r="14"/>{b}</g><circle cx="20" cy="21" r="7" fill="{PE}"/>'
    if k == 'clientes':
        return f'<path d="M6 4 H26 L36 14 V36 A3 3 0 0 1 33 39 H6 A3 3 0 0 1 3 36 V7 A3 3 0 0 1 6 4 Z" fill="{AZ}"/><path d="M26 4 V12 A2 2 0 0 0 28 14 H36 Z" fill="{PE}"/><path d="M9 22 H29 M9 29 H24" stroke="{PAPEL}" stroke-width="3" stroke-linecap="round"/>'
    if k == 'admin':
        return f'<rect x="10" y="3" width="28" height="24" rx="5" fill="{LT}"/><rect x="2" y="12" width="28" height="26" rx="5" fill="{AZ}" stroke="{PAPEL}" stroke-width="3"/>'
    return ''
def sello_b(k):
    if k == 'madre':
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 110 60">{N(55, 30, 96, AZ, PE)}</svg>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 110 60">{N(36, 32, 64, AZ, PE)}<g transform="translate(66 10)">{icono_b(k)}</g></svg>'

# ---------- C · Insignia ----------
POS = {'recepcion': (50, 0), 'analisis': (100, 50), 'calidad': (50, 100), 'clientes': (0, 50), 'admin': (85.4, 14.6)}
def sello_c(k, uid):
    dot = ''
    mask = ''
    if k in POS:
        x, y = POS[k]
        mask = (f'<mask id="c{uid}" maskUnits="userSpaceOnUse" x="-14" y="-16" width="128" height="128"><rect x="-14" y="-16" width="128" height="128" fill="#fff"/>'
                f'<circle cx="{x}" cy="{y}" r="14" fill="#000"/></mask>')
        dot = f'<circle cx="{x}" cy="{y}" r="9" fill="{PE}"/>'
    c = f'<circle cx="50" cy="50" r="50" fill="{AZ}"' + (f' mask="url(#c{uid})"' if mask else '') + '/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}"><defs>{mask}</defs>{c}{dot}{N(50, 52, 70, PAPEL, PE)}</svg>'

os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
for k, *_ in PROD:
    for d, s in (('a', sello_a(k, 'f' + k)), ('b', sello_b(k)), ('c', sello_c(k, 'f' + k))):
        open(os.path.join(H, 'svg', f'{d}-{k}.svg'), 'w').write(s)

_c = [0]
def uid():
    _c[0] += 1; return f'u{_c[0]}'
def inl(svg, h, cls=''):
    return svg.replace('<svg ', f'<svg class="{cls}" style="height:{h}px;width:auto" aria-hidden="true" ', 1)
def nombre(n):
    return f'<span class="pn"><b>{n}</b>{"" if n == "Nisa Nabani" else " Nisa"}</span>'

AGUAS = re.sub(r' width="[^"]*" height="[^"]*"', '', open(os.path.join(MARCA, 'division-aguas.svg')).read(), 1)

AGUAS_40 = AGUAS.replace('<svg ', '<svg style="height:40px;width:auto" aria-hidden="true" ', 1)
def bloque(letra, titulo, idea, gen, pros, contras, ancho=96):
    fila = ''.join(f'<figure>{inl(gen(k), ancho)}{nombre(n)}<figcaption>{q} · {t}</figcaption></figure>' for k, n, q, t in PROD)
    peq = ''.join(inl(gen('recepcion' if i % 3 == 0 else ('analisis' if i % 3 == 1 else 'calidad')), z) for i, z in enumerate((48, 48, 48, 24, 24, 24)))
    barra = f'<div class="bar">{inl(gen("analisis"), 32)}{nombre("Análisis")}<span class="sp"></span><span class="mos">{"".join(f"<i style=background:{c}></i>" for c in (AZ, AZ, AZ, AZ, AZ, PE))}</span></div>'
    junto = f'<div class="jun"><div>{AGUAS_40}<span>Aguas</span><small>división</small></div><div>{inl(gen("recepcion"), 44)}<span>Recepción Nisa</span><small>producto</small></div></div>'
    return f'''<section><span class="num">{letra}</span><h2>{titulo}</h2><p class="idea">{idea}</p>
<div class="fila">{fila}</div>
<div class="tres"><div><h3>Tamaños 48 y 24 px</h3><div class="peq">{peq}</div></div><div><h3>Barra de una app</h3>{barra}</div><div><h3>Junto a una división</h3>{junto}</div></div>
<div class="pc"><div class="si"><b>A favor</b><ul>{"".join(f"<li>{x}</li>" for x in pros)}</ul></div><div class="nosi"><b>En contra</b><ul>{"".join(f"<li>{x}</li>" for x in contras)}</ul></div></div></section>'''

FUENTES = sys.argv[1] if len(sys.argv) > 1 else None
fonts = (f"<style>@font-face{{font-family:Poppins;src:url('file://{FUENTES}/Poppins-400.woff2');font-weight:400}}@font-face{{font-family:Poppins;src:url('file://{FUENTES}/Poppins-600.woff2');font-weight:600}}@font-face{{font-family:Poppins;src:url('file://{FUENTES}/Poppins-700.woff2');font-weight:700}}</style>"
         if FUENTES else '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap">')

A = bloque('A', 'Contenedor', 'Como Manik: la N de Nisa dentro de un cuadro azul real; el rasgo de cada producto vive en el borde y nunca toca la N. El color queda reservado a las divisiones: todos los productos son azul real.', lambda k: sello_a(k, uid()),
           ['Se distingue de inmediato de una división: cuadro contra ícono suelto.', 'Funciona como ícono de app y a 24 px.', 'Es el mismo sistema que Manik: una sola lógica para las dos empresas.'],
           ['Los seis sellos son del mismo azul: el rasgo y el nombre cargan toda la diferencia.', 'A 24 px el borde de sello de Calidad se lee como un cuadro rugoso.'])
B = bloque('B', 'Variación del manual', 'La regla que el manual ya usa para las divisiones: la N de onda con un ícono al lado. Cada producto suma su ícono en azul real.', sello_b,
           ['Sale directo del manual: cero reglas nuevas.', 'La N conserva su forma y sus colores originales.'],
           ['Un producto se ve igual que una división: «Recepción» y «Aguas» son el mismo tipo de pieza.', 'Es horizontal: no sirve como ícono de app cuadrado.', 'A 24 px el ícono queda de 10 px y desaparece.'], ancho=58)
C = bloque('C', 'Insignia', 'Un círculo azul con la N; cada producto se marca con un pocillo pera en una posición del borde, como un reloj.', lambda k: sello_c(k, uid()),
           ['Muy limpio y reconocible como familia.', 'El círculo recuerda la insignia del manual.'],
           ['La diferencia entre productos es solo la posición de un punto: se aprende, no se entiende.', 'Es fácil confundir Recepción con Administración a 24 px.'])

html = f'''<title>Ecosistema Nisa · ronda 1</title>
<meta name="claude:viewport-fit-sides" content="cover">
{fonts}
<style>
/* Lámina de decisión: blanco, tinta y azul real de Nisa Nabani; Poppins como en el manual. */
:root{{--bg:#FFFFFF;--fg:{TINTA};--az:{AZ};--pe:{PE};--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{background:var(--bg);color:var(--fg);font:16px/1.6 Poppins,system-ui,sans-serif;margin:0;padding-block:0 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1120px;margin:0 auto}} h1,h2,h3{{margin:0;text-wrap:balance}} h1{{font:700 clamp(30px,5vw,48px)/1.1 Poppins,sans-serif;letter-spacing:-.02em}} h2{{font:700 26px/1.2 Poppins,sans-serif;margin-bottom:4px}} h3{{font:600 14px/1.4 Poppins,sans-serif;color:var(--muted);margin:0 0 8px}}
p{{max-width:72ch;margin:0 0 10px}} .muted{{color:var(--muted)}} .num{{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--az);color:#fff;font:700 16px Poppins,sans-serif;margin-bottom:8px}}
header{{padding:44px 0 28px;border-bottom:1px solid var(--line);display:grid;gap:12px}}
.arq{{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}} .arq div{{background:var(--sunk);border-radius:14px;padding:12px 14px;font-size:14px;line-height:1.4}} .arq b{{display:block;font-size:15px}}
section{{padding:36px 0;border-bottom:1px solid var(--line)}} .idea{{color:var(--muted)}}
.fila{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));margin:16px 0}} .fila figure{{margin:0;border:1px solid var(--line);border-radius:16px;padding:16px 10px;display:grid;justify-items:center;gap:6px;text-align:center}}
.fila figcaption{{font-size:12px;line-height:1.35;color:var(--muted)}} .pn{{font-size:15px;line-height:1.3}} .pn b{{font-weight:600}}
.tres{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));margin:8px 0 16px}} .peq{{display:flex;gap:14px;align-items:center;flex-wrap:wrap;background:var(--sunk);border-radius:14px;padding:14px}}
.bar{{display:flex;align-items:center;gap:10px;height:56px;padding:0 12px;border:1px solid var(--line);border-radius:14px;background:#fff}} .sp{{flex:1}} .mos{{display:grid;grid-template-columns:repeat(3,6px);gap:3px}} .mos i{{width:6px;height:6px;border-radius:2px;display:block}}
.jun{{display:flex;gap:20px;flex-wrap:wrap}} .jun div{{display:grid;justify-items:center;gap:2px;font-size:14px;font-weight:600}} .jun small{{font-weight:400;color:var(--muted);font-size:12px}}
.pc{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}} .si,.nosi{{border-radius:14px;padding:14px 16px;font-size:15px}} .si{{background:#EEF4D6}} .nosi{{background:#FBEDEE}} .si b,.nosi b{{display:block;margin-bottom:4px}} .si ul,.nosi ul{{margin:0;padding-left:20px}}
.rec{{background:var(--sunk);border-radius:18px;padding:20px 22px;margin-top:28px}}
</style>
<main>
<header><span class="muted" style="font-size:13px;letter-spacing:.08em;text-transform:uppercase">Ecosistema Nisa · ronda 1 de identidad</span>
<h1>Un sello para cada producto de Nisa Nabani</h1>
<p class="muted">El sistema de laboratorio (antes «Nabi») se vuelve un ecosistema: productos con el patrón «Producto Nisa» bajo el sello de Nisa Nabani, como el Ecosistema Manik. Tres maneras de construir los sellos; la N de onda es el vector del manual en las tres.</p>
<div class="arq"><div><b>Nisa Nabani</b>La empresa y el sello madre.</div><div><b>Producto Nisa</b>Recepción, Análisis, Calidad, Clientes y Administración (propuesta por confirmar).</div><div><b>Divisiones</b>Aguas, Alimentos… Siguen como están: N + ícono, con su color.</div><div><b>Regla clave</b>Un producto no puede parecer una división.</div></div></header>
{A}{B}{C}
<div class="rec"><b>Recomendación: A · Contenedor</b>, con confianza media. Es la única que separa a simple vista un producto de una división y la única que funciona como ícono de app. Su punto débil es que todos los sellos son azules; se compensa con el rasgo y el nombre, igual que en Manik. Es criterio de diseño, no está probado con usuarios.</div>
</main>'''
open(os.path.join(H, 'lamina.html'), 'w').write(html)
print('ok')
