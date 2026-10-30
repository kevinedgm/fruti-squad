# NisaLab · desarrollo del símbolo Colonia: construcción, variantes y sistema de marca.
# Uso: python3 gen.py [carpeta-fuentes] → colonia.html y svg/
import math, os, sys

H = os.path.dirname(os.path.abspath(__file__))
AZ, PE, W, TINTA = '#052A76', '#C2D225', '#FFFFFF', '#141B33'
G = 4  # separación constante entre células

def tangente(c1, r1, c2, r2, r, lado):
    """Centro de un círculo de radio r a distancia (r1+r+G) de c1 y (r2+r+G) de c2."""
    d1, d2 = r1 + r + G, r2 + r + G
    dx, dy = c2[0] - c1[0], c2[1] - c1[1]
    d = math.hypot(dx, dy)
    a = (d1 * d1 - d2 * d2 + d * d) / (2 * d)
    h = math.sqrt(max(d1 * d1 - a * a, 0))
    mx, my = c1[0] + a * dx / d, c1[1] + a * dy / d
    return (mx - lado * h * dy / d, my + lado * h * dx / d)

def construida(n=4):
    A, rA = (0.0, 0.0), 26
    rB = 20
    ang = math.radians(-40)
    B = (A[0] + (rA + rB + G) * math.cos(ang), A[1] + (rA + rB + G) * math.sin(ang))
    C, rC = tangente(A, rA, B, rB, 12, 1), 12
    cel = [(A, rA, 'az'), (B, rB, 'pe'), (C, rC, 'az')]
    if n == 4:
        D = tangente(A, rA, B, rB, 7, -1)
        cel.append((D, 7, 'az'))
    return cel

def original():
    return [((34, 62), 24, 'az'), ((68, 36), 22, 'pe'), ((72, 76), 14, 'az'), ((32, 22), 11, 'az')]
def mitosis():
    A, rA = (0.0, 0.0), 26
    B = (A[0] + 50 * math.cos(math.radians(-40)), A[1] + 50 * math.sin(math.radians(-40)))
    return [(A, rA, 'az'), (B, 20, 'pe'), ((B[0] + 14, B[1] - 12), 13, 'pe2'), (tangente(A, rA, B, 20, 12, 1), 12, 'az')]

def encaja(cel, caja=100, margen=0):
    xs = [c[0] - r for c, r, _ in cel] + [c[0] + r for c, r, _ in cel]
    ys = [c[1] - r for c, r, _ in cel] + [c[1] + r for c, r, _ in cel]
    w, h = max(xs) - min(xs), max(ys) - min(ys)
    k = (caja - 2 * margen) / max(w, h)
    ox = margen + (caja - 2 * margen - w * k) / 2 - min(xs) * k
    oy = margen + (caja - 2 * margen - h * k) / 2 - min(ys) * k
    return [((c[0] * k + ox, c[1] * k + oy), r * k, t) for c, r, t in cel]

def dibuja(cel, az=AZ, pe=PE):
    col = {'az': az, 'pe': pe, 'pe2': pe}
    out = ''
    for (x, y), r, t in cel:
        extra = f' fill-opacity="{.85 if az != pe else 1}"' if t == 'pe2' else ''
        out += f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{col[t]}"{extra}/>'
    return out
def svg(cel, az=AZ, pe=PE, vb='-2 -2 104 104'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{dibuja(cel, az, pe)}</svg>'
def inl(s, h):
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block" aria-hidden="true" ', 1)

VAR = [
    ('1', 'Original', encaja(original()), 'La de la ronda anterior: cuatro células colocadas a ojo.'),
    ('2', 'Construida', encaja(construida(4)), 'Las mismas cuatro, pero todas tangentes con la misma separación. Se ve diseñada, no casual.'),
    ('3', 'Tres células', encaja(construida(3)), 'Sin la célula más chica: más simple y más clara a 16 px.'),
    ('4', 'Crece', encaja(mitosis()), 'La célula pera se está dividiendo: el laboratorio detecta lo que crece.'),
]
REC = VAR[1][2]

# ---------- construcción ----------
def construccion():
    cel = REC
    guias = ''.join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r + G * 100 / 104 / 2:.2f}" fill="none" stroke="#9AA6C0" stroke-width=".6" stroke-dasharray="2 2"/>' for (x, y), r, _ in cel)
    centros = ''.join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.2" fill="#9AA6C0"/>' for (x, y), _, _ in cel)
    lineas = ''
    for i in range(len(cel)):
        for j in range(i + 1, len(cel)):
            (x1, y1), r1, _ = cel[i]; (x2, y2), r2, _ = cel[j]
            if math.hypot(x2 - x1, y2 - y1) < r1 + r2 + 8:
                lineas += f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#9AA6C0" stroke-width=".6"/>'
    radios = [r for _, r, _ in cel]
    base = radios[-1]
    rot = ''.join(f'<text x="{x:.1f}" y="{y + 3:.1f}" font-size="8" text-anchor="middle" fill="#141B33" font-family="Poppins,sans-serif" font-weight="600">{r / base:.1f}</text>' for (x, y), r, _ in cel)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-8 -8 116 116">{dibuja(cel, "#C9D2E6", "#E3EBA8")}{guias}{lineas}{centros}{rot}</svg>'

FUENTES = sys.argv[1] if len(sys.argv) > 1 else None
fuentes = ('<style>' + ''.join(f"@font-face{{font-family:Poppins;src:url('file://{FUENTES}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 600, 700)) + '</style>'
           if FUENTES else '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap">')

S = svg(REC)
S1 = svg(REC, TINTA, TINTA)
SB = svg(REC, W, PE)
os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
for nom, s in (('simbolo', S), ('simbolo-1tinta', svg(REC, 'currentColor', 'currentColor')), ('simbolo-blanco', SB)):
    open(os.path.join(H, 'svg', nom + '.svg'), 'w').write(s)
for n, nom, cel, _ in VAR:
    open(os.path.join(H, 'svg', f'variante-{n}.svg'), 'w').write(svg(cel))
open(os.path.join(H, 'svg', 'construccion.svg'), 'w').write(construccion())

wm = lambda t, c=AZ: f'<span class="wm" style="font-size:{t}px;color:{c}"><b>Nisa</b>Lab</span>'
var_html = ''.join(f'<figure class="{"on" if n == "2" else ""}"><div class="vb">{inl(svg(cel), 110)}</div><div class="vs">{inl(svg(cel), 32)}{inl(svg(cel), 16)}</div><b>{n} · {nom}</b><figcaption>{t}</figcaption></figure>' for n, nom, cel, t in VAR)

html = f'''<title>NisaLab · Colonia</title>
<meta name="claude:viewport-fit-sides" content="cover">
{fuentes}
<style>
/* Desarrollo de un símbolo: blanco, tinta y azul real de Nisa Nabani; Poppins como en el manual. */
:root{{--az:{AZ};--pe:{PE};--fg:{TINTA};--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:16px/1.55 Poppins,system-ui,sans-serif;padding-block:0 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1120px;margin:0 auto}} header{{padding:40px 0 26px;display:grid;gap:14px;border-bottom:1px solid var(--line)}}
h1{{margin:0;font:700 clamp(28px,5vw,44px)/1.1 Poppins,sans-serif;letter-spacing:-.02em}} h2{{margin:0 0 6px;font:700 24px/1.2 Poppins,sans-serif}} h3{{margin:0 0 10px;font:600 13px/1.4 Poppins,sans-serif;color:var(--muted)}}
p{{margin:0 0 10px;max-width:70ch}} .muted{{color:var(--muted)}} section{{padding:34px 0;border-bottom:1px solid var(--line)}} .num{{font:700 14px Poppins,sans-serif;color:var(--az);display:block;margin-bottom:4px}}
.hero{{display:flex;align-items:center;gap:22px;flex-wrap:wrap}} .wm{{line-height:1;letter-spacing:-.015em;white-space:nowrap;display:inline-block}} .wm b{{font-weight:700}}
.vars{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}} figure{{margin:0;border:1px solid var(--line);border-radius:18px;padding:16px;display:grid;gap:8px}} figure.on{{border:2px solid var(--az);box-shadow:inset 0 4px 0 var(--pe)}}
.vb{{display:grid;place-items:center;background:var(--sunk);border-radius:14px;height:150px}} .vs{{display:flex;gap:12px;align-items:center}} figcaption{{font-size:14px;color:var(--muted);line-height:1.45}}
.two{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));align-items:center}} .fig{{background:var(--sunk);border-radius:18px;padding:22px;display:grid;place-items:center}} .fig svg{{max-width:320px;width:100%;height:auto}}
.g3{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}} .c{{border:1px solid var(--line);border-radius:18px;padding:20px;display:grid;gap:12px;align-content:start;min-width:0}} .c.az{{background:var(--az);border-color:var(--az)}} .c.az h3{{color:#C9D3EA}}
.lg{{display:flex;align-items:center;gap:14px}} .lv{{display:grid;justify-items:center;gap:10px}} .de{{font-size:13px;color:var(--muted);margin-top:4px}} .de b{{color:var(--fg)}}
.tam{{display:flex;gap:16px;align-items:flex-end;flex-wrap:wrap}} .app{{display:grid;place-items:center;background:var(--az)}}
.resp{{display:inline-grid;place-items:center;outline:2px dashed var(--az);padding:24px;border-radius:4px}}
.tab{{display:flex;align-items:center;gap:8px;background:#E8EBF2;border-radius:10px 10px 0 0;padding:8px 12px;width:max-content;font-size:13px}} .tab span{{color:var(--muted)}}
.bar{{display:flex;align-items:center;gap:12px;height:60px;padding:0 16px;border:1px solid var(--line);border-radius:14px;background:#fff}} .sp{{flex:1}} .srch{{border:1px solid #858DA3;border-radius:10px;padding:6px 12px;font-size:13px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:45%}}
.login{{border:1px solid var(--line);border-radius:22px;padding:26px;display:grid;gap:12px;max-width:340px;background:#fff;box-shadow:0 10px 30px rgba(20,27,51,.08)}} .login .f{{height:42px;border:1px solid #858DA3;border-radius:10px;padding:0 12px;display:flex;align-items:center;color:var(--muted);font-size:14px}} .login .b{{height:44px;border-radius:10px;background:var(--az);color:#fff;display:grid;place-items:center;font-weight:600}}
.rules li{{margin:6px 0}} .wide{{grid-column:span 2}} @media (max-width:700px){{.wide{{grid-column:auto}} .hero .wm{{font-size:44px !important}} .bar .srch{{display:none}}}} .rec{{background:var(--sunk);border-radius:18px;padding:18px 20px;margin-top:6px}}
</style>
<main>
<header><span class="muted" style="font-size:13px;letter-spacing:.08em;text-transform:uppercase">NisaLab · desarrollo del símbolo</span>
<div class="hero">{inl(S, 96)}<div><span class="wm" style="font-size:60px;color:var(--az)"><b>Nisa</b>Lab</span><div class="de" style="font-size:15px">de <b>Nisa Nabani</b></div></div></div>
<p class="muted">Colonia: células agrupadas, una en pera. Lo vivo que el laboratorio detecta, cuenta y certifica.</p></header>

<section><span class="num">01</span><h2>La forma</h2><p class="muted">Cuatro maneras de construir el mismo racimo. La marcada es la recomendada y es la que usa el resto de la página.</p>
<div class="vars">{var_html}</div>
<p class="rec"><b>Recomendación: 2 · Construida.</b> Conserva lo que elegiste y le da una regla: todas las células se tocan casi, con la misma separación, y sus tamaños siguen una proporción. Esa regla es lo que hace que no parezca un dibujo cualquiera. Si a 16 px te importa más la claridad, la 3 es la alternativa.</p></section>

<section><span class="num">02</span><h2>Construcción</h2>
<div class="two"><div class="fig">{construccion()}</div><div><ul class="rules"><li><b>Separación constante.</b> Entre células siempre hay el mismo espacio; las líneas grises unen centros de células vecinas.</li><li><b>Proporción.</b> Los números son el tamaño de cada célula comparado con la más chica.</li><li><b>Una sola célula pera</b>, arriba a la derecha: la que creció. Nunca dos.</li><li><b>No se rota ni se reacomoda:</b> el racimo es fijo, como una firma.</li></ul></div></div></section>

<section><span class="num">03</span><h2>Logotipo</h2>
<div class="g3"><div class="c"><h3>Horizontal</h3><div class="lg">{inl(S, 56)}{wm(44)}</div></div>
<div class="c"><h3>Vertical</h3><div class="lv">{inl(S, 72)}{wm(34)}</div></div>
<div class="c"><h3>Con respaldo</h3><div class="lg">{inl(S, 52)}<div>{wm(34)}<div class="de">de <b>Nisa Nabani</b></div></div></div></div>
<div class="c az"><h3>Sobre azul</h3><div class="lg">{inl(SB, 56)}{wm(44, W)}</div></div>
<div class="c"><h3>Una tinta</h3><div class="lg">{inl(S1, 56)}{wm(44, TINTA)}</div></div>
<div class="c"><h3>Solo el nombre</h3>{wm(44)}<p class="muted" style="font-size:14px;margin:0">«Nisa» en Poppins 700 y «Lab» en 400: el sistema y lo que hace.</p></div></div></section>

<section><span class="num">04</span><h2>Ícono, tamaños y respeto</h2>
<div class="g3"><div class="c"><h3>Ícono de app · 96, 60, 40 px</h3><div class="tam">{"".join(f'<span class="app" style="width:{z}px;height:{z}px;border-radius:{z * .22:.0f}px">{inl(SB, z * .62)}</span>' for z in (96, 60, 40))}</div></div>
<div class="c"><h3>Favicon · 32, 24 y 16 px</h3><div class="tam">{inl(S, 32)}{inl(S, 24)}{inl(S, 16)}</div><div class="tab">{inl(S, 16)}NisaLab <span>· Recepción</span></div></div>
<div class="c"><h3>Área de respeto</h3><div class="resp">{inl(S, 64)}</div><p class="muted" style="font-size:14px;margin:0">Libre alrededor: el ancho de la célula grande. Mínimo 16 px en pantalla y 6 mm impreso.</p></div></div></section>

<section><span class="num">05</span><h2>Aplicado</h2>
<div class="g3"><div class="c wide"><h3>Barra superior</h3><div class="bar">{inl(S, 32)}{wm(20)}<span class="sp"></span><span class="srch">Buscar muestra, lote o cliente</span></div></div>
<div class="c"><h3>Inicio de sesión</h3><div class="login"><div class="lg">{inl(S, 40)}<div>{wm(26)}<div class="de">de <b>Nisa Nabani</b></div></div></div><div class="f">Correo</div><div class="f">Contraseña</div><div class="b">Entrar</div></div></div></div></section>
</main>'''
open(os.path.join(H, 'colonia.html'), 'w').write(html)
print('ok', [round(r, 1) for _, r, _ in REC])
