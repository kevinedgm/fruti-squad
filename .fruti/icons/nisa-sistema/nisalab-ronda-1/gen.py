# NisaLab · ronda 1 de identidad: símbolo y logotipo del sistema de laboratorio de Nisa Nabani.
# Uso: python3 gen.py [carpeta-fuentes] → lamina.html y svg/
# La N de onda y la N con matraz son vectores del manual (marca-nisa/): nunca se redibujan.
import os, re, sys

H = os.path.dirname(os.path.abspath(__file__))
MARCA = os.path.join(H, '..', 'nabi-design-system', 'marca-nisa')
AZ, PE, W, TINTA = '#052A76', '#C2D225', '#FFFFFF', '#141B33'

def carga(nombre):
    s = open(os.path.join(MARCA, nombre)).read()
    vb = [float(v) for v in re.search(r'viewBox="([^"]*)"', s).group(1).split()]
    ps = [(m.group(1), m.group(2)) for m in re.finditer(r'<path[^>]*fill="([^"]*)"[^>]*d="([^"]*)"', s)]
    return vb, ps
NV, NP = carga('nisa-nabani-n.svg')
MV, MP = carga('nisa-nabani-matraz.svg')
def pinta(vb, ps, cx, cy, w, azul, pera):
    k = w / vb[2]
    t = f'translate({cx} {cy}) scale({k:.4f}) translate({-(vb[0] + vb[2] / 2):.2f} {-(vb[1] + vb[3] / 2):.2f})'
    return f'<g transform="{t}">' + ''.join(f'<path d="{d}" fill="{pera if f.startswith("rgb(76") else azul}"/>' for f, d in ps) + '</g>'
N = lambda cx, cy, w, a, p: pinta(NV, NP, cx, cy, w, a, p)
M = lambda cx, cy, w, a, p: pinta(MV, MP, cx, cy, w, a, p)

R = 21
CUADRO = f'M{R} 0 H{100-R} A{R} {R} 0 0 1 100 {R} V{100-R} A{R} {R} 0 0 1 {100-R} 100 H{R} A{R} {R} 0 0 1 0 {100-R} V{R} A{R} {R} 0 0 1 {R} 0 Z'
MATRAZ = 'M33 0 H67 A4 4 0 0 1 67 8 H62 V30 L96 84 A11 11 0 0 1 86 100 H14 A11 11 0 0 1 4 84 L38 30 V8 H33 A4 4 0 0 1 33 0 Z'

# símbolo de cada dirección; tono: 'color' | 'inverso' (sobre azul)
def simbolo(d, tono='color'):
    inv = tono == 'inverso'
    if d == 'a':
        f, a = (W, AZ) if inv else (AZ, W)
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 104 104"><path d="{CUADRO}" fill="{f}"/>{N(50, 52, 72, a, PE)}</svg>'
    if d == 'b':
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 104 84">{M(50, 40, 100, W if inv else AZ, PE)}</svg>'
    f, a = (W, AZ) if inv else (AZ, W)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 104 104"><path d="{MATRAZ}" fill="{f}"/>{N(50, 73, 54, a, PE)}</svg>'

FUENTE_LOGO = {'a': ('Poppins', 'normal'), 'b': ('Archivo', '125%'), 'c': ('Archivo', '125%')}
def palabra(d, tono='color', tam=44):
    col = W if tono == 'inverso' else AZ
    fam, ancho = FUENTE_LOGO[d]
    if d == 'a':
        return f'<span class="wm" style="font-family:Poppins;font-size:{tam}px;color:{col}"><b style="font-weight:700">Nisa</b><span style="font-weight:400">Lab</span></span>'
    if d == 'b':
        return f'<span class="wm st" style="font-size:{tam * .62:.0f}px;color:{col}">NISA<br>LAB</span>'
    return f'<span class="wm st" style="font-size:{tam * .78:.0f}px;color:{col}">NISALAB</span>'

def inl(svg, h):
    return svg.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block" aria-hidden="true" ', 1)
def tile(d, z):
    if d == 'a':
        return inl(simbolo('a'), z)
    return f'<span class="app" style="width:{z}px;height:{z}px;border-radius:{z * .22:.0f}px">{inl(simbolo(d), z * .7)}</span>'

DIR = [
    ('a', 'Sello', 'La N de Nisa dentro del cuadro azul: el mismo sello que llevarán los productos, sin rasgo. El nombre en Poppins, la letra del manual: «Nisa» en 700 y «Lab» en 400.',
     ['Es a la vez ícono de app: no necesita adaptación.', 'Sistema y productos comparten una sola forma, como Manik.', 'Poppins es la letra del manual: cero fuentes nuevas.'],
     ['Si los productos también son cuadros azules, NisaLab se distingue de ellos solo porque no lleva rasgo.']),
    ('b', 'Familia del logo', 'El ícono del manual (N con matraz) y el nombre apilado en versal ancha, como «NISA NABANI». Es el logo de la empresa con otra palabra.',
     ['Nadie duda que es de Nisa Nabani.', 'Usa el ícono que ya existe: no hay símbolo nuevo.'],
     ['Se confunde con el logo de la empresa: en un documento habría dos logos casi iguales.', 'El matraz es de línea fina: a 24 px desaparece.', 'Como ícono de app necesita un cuadro blanco alrededor.']),
    ('c', 'Matraz', 'La silueta del matraz del logo se vuelve el contenedor: azul, con la N dentro. El matraz dice «laboratorio» sin palabras; el nombre, en versal ancha.',
     ['Forma propia: no se confunde con la empresa ni con los productos (cuadros).', 'Se reconoce a 24 px por la silueta.', 'El «Lab» del nombre y el matraz cuentan lo mismo.'],
     ['Como ícono de app va dentro de un cuadro blanco; el matraz queda más chico.', 'La N se achica para caber en el cuerpo del matraz.']),
]

def bloque(d, titulo, idea, pros, contras):
    logo = f'<div class="lg">{inl(simbolo(d), 64)}{palabra(d)}</div>'
    resp = f'<div class="lg">{inl(simbolo(d), 44)}<div>{palabra(d, tam=30)}<div class="de">de <b>Nisa Nabani</b></div></div></div>'
    inv = f'<div class="lg inv">{inl(simbolo(d, "inverso"), 56)}{palabra(d, "inverso", 38)}</div>'
    tam = ''.join(f'<span>{tile(d, z)}</span>' for z in (96, 48, 32, 16))
    barra = f'<div class="bar">{tile(d, 32)}<span class="nm"><b>NisaLab</b></span><span class="sp"></span><span class="srch">Buscar muestra, lote o cliente</span></div>'
    return f'''<section><span class="num">{d.upper()}</span><h2>{titulo}</h2><p class="idea">{idea}</p>
<div class="g2"><div class="c"><h3>Logotipo</h3>{logo}</div><div class="c"><h3>Con respaldo</h3>{resp}</div><div class="c az"><h3>Sobre azul</h3>{inv}</div></div>
<div class="g2"><div class="c"><h3>Ícono de app · 96, 48, 32 y 16 px</h3><div class="tam">{tam}</div></div><div class="c" style="grid-column:span 2"><h3>Barra superior</h3>{barra}</div></div>
<div class="pc"><div class="si"><b>A favor</b><ul>{"".join(f"<li>{x}</li>" for x in pros)}</ul></div><div class="nosi"><b>En contra</b><ul>{"".join(f"<li>{x}</li>" for x in contras)}</ul></div></div></section>'''

os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
for d, *_ in DIR:
    for t in ('color', 'inverso'):
        open(os.path.join(H, 'svg', f'{d}-simbolo-{t}.svg'), 'w').write(simbolo(d, t))

F = sys.argv[1] if len(sys.argv) > 1 else None
if F:
    fuentes = ('<style>' + ''.join(f"@font-face{{font-family:Poppins;src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 600, 700))
               + f"@font-face{{font-family:Archivo;src:url('file://{F}/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}</style>")
else:
    fuentes = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Archivo:wdth,wght@62..125,100..900&display=swap">'

madre = open(os.path.join(MARCA, 'nisa-nabani-logo.svg')).read()
madre = re.sub(r' width="[^"]*" height="[^"]*"', '', madre, 1).replace('<svg ', '<svg style="height:56px;width:auto;display:block" aria-hidden="true" ', 1)

html = f'''<title>NisaLab · ronda 1</title>
<meta name="claude:viewport-fit-sides" content="cover">
{fuentes}
<style>
/* Lámina de decisión: blanco, tinta y azul real de Nisa Nabani; Poppins como en el manual. */
:root{{--az:{AZ};--pe:{PE};--fg:{TINTA};--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:16px/1.55 Poppins,system-ui,sans-serif;padding-block:0 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1120px;margin:0 auto}} header{{padding:40px 0 24px;border-bottom:1px solid var(--line);display:grid;gap:12px}}
.ov{{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}} h1{{margin:0;font:700 clamp(28px,5vw,44px)/1.1 Poppins,sans-serif;letter-spacing:-.02em}} h2{{margin:0 0 4px;font:700 26px/1.2 Poppins,sans-serif}} h3{{margin:0 0 12px;font:600 13px/1.4 Poppins,sans-serif;color:var(--muted)}}
p{{margin:0;max-width:72ch}} .idea{{color:var(--muted);margin-bottom:16px}}
.arq{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;font-size:15px}} .arq span{{background:var(--sunk);border-radius:999px;padding:6px 14px}} .arq i{{color:var(--muted);font-style:normal}}
section{{padding:34px 0;border-bottom:1px solid var(--line)}} .num{{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--az);color:#fff;font:700 16px Poppins,sans-serif;margin-bottom:8px}}
.g2{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));margin-bottom:14px}} .c{{border:1px solid var(--line);border-radius:18px;padding:18px;min-width:0}} .c.az{{background:var(--az);border-color:var(--az)}} .c.az h3{{color:#C9D3EA}}
.lg{{display:flex;align-items:center;gap:14px;flex-wrap:wrap}} .wm{{line-height:1;letter-spacing:-.01em;white-space:nowrap}} .st{{font-family:Archivo,sans-serif;font-weight:800;font-stretch:125%;letter-spacing:.01em;line-height:.95}}
.de{{font-size:13px;color:var(--muted);margin-top:4px}} .de b{{color:var(--fg)}}
.tam{{display:flex;gap:14px;align-items:flex-end;flex-wrap:wrap}} .app{{display:grid;place-items:center;background:#fff;box-shadow:0 0 0 1px var(--line),0 2px 6px rgba(20,27,51,.10)}}
.bar{{display:flex;align-items:center;gap:12px;height:60px;padding:0 14px;border:1px solid var(--line);border-radius:14px;background:#fff}} .nm{{font-weight:700;font-size:17px}} .sp{{flex:1}} .srch{{border:1px solid #858DA3;border-radius:10px;padding:6px 12px;font-size:13px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:45%}}
.pc{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}} .si,.nosi{{border-radius:14px;padding:14px 16px;font-size:15px}} .si{{background:#EEF4D6}} .nosi{{background:#FBEDEE}} .si b,.nosi b{{display:block;margin-bottom:4px}} .si ul,.nosi ul{{margin:0;padding-left:20px}}
.rec{{background:var(--sunk);border-radius:18px;padding:20px 22px;margin-top:26px;display:grid;gap:8px}}
</style>
<main>
<header><span class="ov">NisaLab · ronda 1 de identidad</span><h1>El símbolo y el logotipo de NisaLab</h1>
<p style="color:var(--muted)">NisaLab es el sistema de laboratorio de Nisa Nabani. Tres maneras de construir su identidad a partir del manual de la empresa. La N de onda y el matraz son los vectores del manual.</p>
<div class="arq"><span><b>Nisa Nabani</b> <i>empresa</i></span>→<span><b>NisaLab</b> <i>sistema</i></span>→<span><b>Recepción NisaLab, Calidad NisaLab…</b> <i>productos</i></span></div>
<div style="display:flex;gap:12px;align-items:center;margin-top:6px">{madre}<span style="font-size:13px;color:var(--muted)">La marca madre, como referencia.</span></div></header>
{"".join(bloque(*d) for d in DIR)}
<div class="rec"><b>Recomendación: C · Matraz</b><p>Con confianza media. Es la única forma que no se confunde con la empresa (B) ni con los productos (A): el sistema es el matraz y cada producto será un cuadro con su rasgo, igual que en Manik el ecosistema tiene un emblema distinto a las apps. Además se reconoce a 24 px por la silueta. Es criterio de diseño, no está probado con usuarios.</p>
<p style="font-size:14px;color:var(--muted)">La versal ancha usa Archivo al 125 % como aproximación a Steppe, la letra del logo de Nisa Nabani (comercial, no disponible aquí). En el paquete final los logotipos se entregan convertidos a trazos.</p></div>
</main>'''
open(os.path.join(H, 'lamina.html'), 'w').write(html)
print('ok')
