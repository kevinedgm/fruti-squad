# NisaLab · ronda 1 de áreas: cómo se identifica cada división de Nisa Nabani dentro de NisaLab.
# Uso: python3 gen.py [carpeta-fuentes] → areas.html y svg/
# Colonia es el símbolo aprobado (nisalab-final). Los azulejos de división son los vectores del manual (marca-nisa/division-*.svg).
import os, re, sys

H = os.path.dirname(os.path.abspath(__file__))
NS = os.path.join(H, '..')
MARCA = os.path.join(NS, 'nabi-design-system', 'marca-nisa')
AZ, PE, W, TINTA = '#052A76', '#C2D225', '#FFFFFF', '#141B33'

_s = open(os.path.join(NS, 'nisalab-final', 'svg', 'simbolo.svg')).read()
CEL = [(float(x), float(y), float(r), c) for x, y, r, c in re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)" fill="([^"]+)"', _s)]
GROW = next(c for c in CEL if c[3] == PE)  # la célula que creció

AREAS = [  # clave, nombre del manual, color del manual
    ('aguas', 'Aguas', '#00B4D8'), ('agricolas', 'Agrícolas', '#553739'), ('ambiental', 'Ambiental', '#38B000'),
    ('alimentos', 'Alimentos', '#F48C06'), ('bebidas', 'Bebidas', '#3D67AE'), ('agave', 'Bebidas de agave', '#006D53'),
    ('farmacia', 'Farmacia', '#3D0066'), ('consultoria', 'Consultoría', '#052A76'),
]
_n = [0]
def azulejo(k, x, y, size):
    """El azulejo de división del manual, colocado como <svg> anidado con ids únicos."""
    _n[0] += 1; u = f'd{_n[0]}'
    s = open(os.path.join(MARCA, f'division-{k}.svg')).read()
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="{m.group(1)}{u}"', s)
    s = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{m.group(1)}{u})', s)
    s = re.sub(r' width="[^"]*" height="[^"]*"', '', s, 1)
    return s.replace('<svg ', f'<svg x="{x:.2f}" y="{y:.2f}" width="{size:.2f}" height="{size:.2f}" ', 1)

def base(sin_grow=False, az=AZ):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{az}"/>' for x, y, r, c in CEL if not (sin_grow and c == PE))

def dir_a(k, color):  # la célula que creció toma el color de la división
    x, y, r, _ = GROW
    borde = f' stroke="{W}" stroke-width="0"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 104 104">{base(True)}<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/></svg>'
def dir_b(k, color):  # la célula que creció es el azulejo de la división, recortado en círculo
    x, y, r, _ = GROW
    _n[0] += 1; u = f'c{_n[0]}'
    s = 2 * r * 1.12
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 104 104"><defs><clipPath id="{u}"><circle cx="{x}" cy="{y}" r="{r}"/></clipPath></defs>'
            f'{base(True)}<g clip-path="url(#{u})">{azulejo(k, x - s / 2, y - s / 2, s)}</g></svg>')
def dir_c(k, color):  # Colonia sin cambios + el azulejo de la división al lado
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 176 104">{base()}'
            + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{PE}"/>' for x, y, r, c in CEL if c == PE)
            + f'{azulejo(k, 110, 20, 60)}</svg>')

D = [
    ('A', 'Color', 'La célula que creció deja el pera y toma el color de la división. El resto del racimo sigue azul.', dir_a,
     ['Un solo cambio, como los productos de Manik.', 'El color del manual hace el trabajo.'],
     ['Consultoría es azul real: su célula desaparece en el racimo.', 'Agrícolas (café) y Farmacia (morado) son oscuros: a 24 px se confunden con el azul.']),
    ('B', 'Azulejo', 'La célula que creció es el azulejo de la división del manual, recortado en círculo: su color y su ícono.', dir_b,
     ['Las ocho se distinguen, incluida Consultoría, por el ícono.', 'Usa el ícono oficial de cada división: nada nuevo.'],
     ['A 24 px el ícono dentro de la célula es diminuto: ahí manda el color.', 'Más detalle que la versión A.']),
    ('C', 'Etiqueta', 'Colonia no cambia; el azulejo de la división va a su lado, como una etiqueta.', dir_c,
     ['El símbolo de NisaLab queda intacto.', 'Cada división se ve exactamente como en el manual.'],
     ['Son dos piezas, no una: no sirve como ícono de app.', 'Ocupa el doble de ancho.']),
]

def inl(s, h):
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block" aria-hidden="true" ', 1)

os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
secciones = ''
for letra, nom, idea, fn, pros, contras in D:
    fila = ''
    for k, n, c in AREAS:
        s = fn(k, c)
        open(os.path.join(H, 'svg', f'{letra.lower()}-{k}.svg'), 'w').write(s)
        fila += f'<figure>{inl(fn(k, c), 72)}<div class="sm">{inl(fn(k, c), 24)}</div><figcaption><b>{n}</b> NisaLab</figcaption></figure>'
    barra = f'<div class="bar">{inl(fn("aguas", "#00B4D8"), 34)}<span class="nm"><b>Aguas</b> NisaLab</span><span class="sp"></span><span class="chip">Cambiar de área</span></div>'
    secciones += f'''<section><span class="num">{letra}</span><h2>{nom}</h2><p class="idea">{idea}</p><div class="fila">{fila}</div>
<div class="two"><div><h3>En la barra superior</h3>{barra}</div><div class="pc"><div class="si"><b>A favor</b><ul>{"".join(f"<li>{x}</li>" for x in pros)}</ul></div><div class="nosi"><b>En contra</b><ul>{"".join(f"<li>{x}</li>" for x in contras)}</ul></div></div></div></section>'''

F = sys.argv[1] if len(sys.argv) > 1 else None
fuentes = ('<style>' + ''.join(f"@font-face{{font-family:Poppins;src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 600, 700)) + '</style>'
           if F else '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap">')
logo = open(os.path.join(NS, 'nisalab-final', 'svg', 'logotipo.svg')).read().replace('<svg ', '<svg style="height:48px;width:auto;display:block" ', 1)
html = f'''<title>NisaLab · áreas</title>
<meta name="claude:viewport-fit-sides" content="cover">
{fuentes}
<style>
/* Lámina de decisión: blanco, tinta y azul real de Nisa Nabani; Poppins como en el manual. */
:root{{--az:{AZ};--fg:{TINTA};--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:16px/1.55 Poppins,system-ui,sans-serif;padding-block:0 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1180px;margin:0 auto}} header{{padding:40px 0 24px;display:grid;gap:12px;border-bottom:1px solid var(--line)}}
h1{{margin:0;font:700 clamp(28px,5vw,42px)/1.1 Poppins,sans-serif;letter-spacing:-.02em}} h2{{margin:0 0 4px;font:700 24px/1.2 Poppins,sans-serif}} h3{{margin:0 0 10px;font:600 13px/1.4 Poppins,sans-serif;color:var(--muted)}}
p{{margin:0;max-width:72ch}} .idea{{color:var(--muted);margin-bottom:14px}} section{{padding:32px 0;border-bottom:1px solid var(--line)}}
.num{{display:inline-grid;place-items:center;width:32px;height:32px;border-radius:50%;background:var(--az);color:#fff;font:700 15px Poppins,sans-serif;margin-bottom:8px}}
.fila{{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));margin-bottom:16px}} figure{{margin:0;border:1px solid var(--line);border-radius:16px;padding:14px 8px;display:grid;justify-items:center;gap:8px;text-align:center}}
.sm{{background:var(--sunk);border-radius:8px;padding:6px 10px}} figcaption{{font-size:13px;line-height:1.3;color:var(--muted)}} figcaption b{{color:var(--fg);font-weight:600}}
.two{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));align-items:start}}
.bar{{display:flex;align-items:center;gap:12px;height:60px;padding:0 14px;border:1px solid var(--line);border-radius:14px}} .nm{{font-size:17px;color:var(--muted)}} .nm b{{color:var(--fg);font-weight:600}} .sp{{flex:1}} .chip{{border:1px solid #858DA3;border-radius:10px;padding:5px 10px;font-size:13px}}
.pc{{display:grid;gap:10px}} .si,.nosi{{border-radius:14px;padding:12px 14px;font-size:14px}} .si{{background:#EEF4D6}} .nosi{{background:#FBEDEE}} .si b,.nosi b{{display:block}} .si ul,.nosi ul{{margin:4px 0 0;padding-left:20px}}
.rec{{background:var(--sunk);border-radius:18px;padding:18px 20px;margin-top:24px;display:grid;gap:8px}}
</style>
<main><header>{logo}<h1>Las áreas dentro de NisaLab</h1>
<p style="color:var(--muted)">Las ocho divisiones del manual de Nisa Nabani, con su color y su ícono oficiales, unidas al símbolo de NisaLab. Cada área se nombra «Área NisaLab», como «Agenda Manik». Tres maneras de hacerlo, aplicadas a las ocho.</p></header>
{secciones}
<div class="rec"><b>Recomendación: B · Azulejo</b><p>Con confianza media. Es la única en la que las ocho áreas se distinguen entre sí, incluida Consultoría, que comparte el azul real con NisaLab. Usa el ícono oficial de cada división, así que no agrega dibujos nuevos, y sigue siendo una sola pieza que sirve como ícono de app. A 24 px el ícono interno se pierde y lo que se lee es el color; es aceptable porque el nombre del área siempre acompaña. Es criterio de diseño, no está probado con usuarios.</p></div>
</main>'''
open(os.path.join(H, 'areas.html'), 'w').write(html)
print('ok')
