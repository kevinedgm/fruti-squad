# Ecosistema Manik · ronda 1: el identificador que abre el selector de aplicaciones (como el «waffle» de otras suites)
# Retícula 24 (botón de interfaz). A · mosaico de los seis · B · retícula cruzada por el pulso · C · sello en órbita
import sys
S = sys.argv[1]; F = f'file://{S}/fuentes'
AZ, PAPEL, TINTA = '#234899', '#F6F8FC', '#14213D'
APPS = [('Expediente', '#234899'), ('Agenda', '#007C8C'), ('Compras', '#A15C07'), ('Farmacia', '#1B7F52'), ('Impulsa', '#6B3FB8'), ('Grupos', '#C73A55')]
SVGD = '../ronda-5-seis/svg/'
def app_svg(p): return open(SVGD + p.lower() + '.svg').read()

def A(color=True):  # 3×2 tarjetas: una por producto
    c, g, x0 = 5.6, 1.6, 2.8; y0 = 12 - c - g / 2; out = ''
    for i, (_, col) in enumerate(APPS):
        x = x0 + (i % 3) * (c + g); y = y0 + (i // 3) * (c + g)
        out += f'<rect x="{x:.2f}" y="{y:.2f}" width="{c}" height="{c}" rx="1.6" fill="{col if color else "currentColor"}"/>'
    return out
def B(color=True):  # 3×3 tarjetas cruzadas por la línea de pulso (calada)
    c, g = 5.6, 1.6; out = '<defs><mask id="mB"><rect width="24" height="24" fill="#fff"/>'
    out += '<path d="M1 14.6 L4.4 14.6 L7.4 4.8 L11.8 19.4 L16.2 7.2 L18.8 14.6 L23 14.6" fill="none" stroke="#000" stroke-width="2.2" stroke-linejoin="round"/></mask></defs><g mask="url(#mB)">'
    for i in range(9):
        x = 2.8 + (i % 3) * (c + g); y = 2.8 + (i // 3) * (c + g)
        out += f'<rect x="{x:.2f}" y="{y:.2f}" width="{c}" height="{c}" rx="1.6" fill="{AZ if color else "currentColor"}"/>'
    return out + '</g>'
def C(color=True):  # el sello al centro y los seis productos alrededor
    import math
    out = f'<rect x="7" y="7" width="10" height="10" rx="2.6" fill="{AZ if color else "currentColor"}"/>'
    out += f'<path d="M6 13.4 L8.6 13.4 L10.2 8.8 L12.2 15.6 L14.2 9.8 L15.4 13.4 L18 13.4" fill="none" stroke="{PAPEL if color else "var(--fondo,#fff)"}" stroke-width="1.5" stroke-linejoin="round"/>'
    for i, (_, col) in enumerate(APPS):
        a = -math.pi / 2 + i * math.pi / 3
        out += f'<circle cx="{12 + 9.6 * math.cos(a):.2f}" cy="{12 + 9.6 * math.sin(a):.2f}" r="1.7" fill="{col if color else "currentColor"}"/>'
    return out
V = [('A', 'Mosaico', 'Seis tarjetas, una por producto y en su color. Dice literalmente «estas son las apps». Si mañana hay un séptimo producto, cambia el dibujo.', A),
     ('B', 'Retícula con pulso', 'La retícula de 3×3 que la gente ya reconoce como «aplicaciones», cruzada por la línea de Manik. Estable aunque cambie el número de productos.', B),
     ('C', 'Órbita', 'El sello al centro y los seis productos girando alrededor. Es la imagen más literal de «ecosistema», pero a 20 px los puntos se vuelven ruido.', C)]
def ic(fn, z, color=True, cls=''):
    return f'<svg class="{cls}" viewBox="0 0 24 24" width="{z}" height="{z}">{fn(color)}</svg>'
filas = ''
for k, n, t, fn in V:
    tam = ''.join(f'<figure>{ic(fn, z)}<figcaption>{z}</figcaption></figure>' for z in (16, 20, 24, 32, 64))
    mono = f'<figure>{ic(fn, 24, False)}<figcaption>1 tinta</figcaption></figure><figure class="dk">{ic(fn, 24)}<figcaption>oscuro</figcaption></figure>'
    filas += f'<div class="fila"><div class="k"><b>{k} · {n}</b><small>{t}</small></div><div class="tam">{tam}{mono}</div></div>'

# El selector abierto dentro de un módulo (Farmacia), con B como botón
tiles = ''.join(f'<a class="tile{" on" if p == "Farmacia" else ""}"><span class="ai">{app_svg(p)}</span><span>{p}</span>{"<em>Aquí estás</em>" if p == "Farmacia" else ""}</a>' for p, _ in APPS)
panel = f"""<div class="mock"><div class="bar"><span class="ai sm">{app_svg('Farmacia')}</span><b>Farmacia</b>&nbsp;Manik<span class="sp"></span><span class="srch">Buscar producto, receta o lote</span><button class="eco on" aria-label="Ecosistema Manik" aria-expanded="true">{ic(A, 22)}</button><span class="av">MR</span></div>
<div class="body"><div class="pn" role="dialog" aria-label="Ecosistema Manik"><div class="ph">{ic(A, 18)}<b>Ecosistema</b>&nbsp;Manik</div><div class="grid">{tiles}</div><div class="pf">MedicalManik · un solo inicio de sesión para todas las apps</div></div>
<div class="ghost"><div class="gl"></div><div class="gl w"></div><div class="gl"></div><div class="gl w2"></div></div></div></div>"""
lk = f'<div class="lock">{ic(A, 44)}<span><b>Ecosistema</b> Manik</span></div>'
open('lamina.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
body{{margin:0;background:{PAPEL};color:{TINTA};font:14px/1.45 Inst,sans-serif;padding:36px;width:1140px}}h1{{font:600 26px Sora;color:{AZ};margin:0}}.i{{margin:2px 0 20px;color:#4A5674;max-width:1000px}}h2{{font:600 17px Sora;color:{AZ};margin:24px 0 10px}}
svg{{display:block}}.fila{{display:grid;grid-template-columns:400px 1fr;gap:20px;align-items:center;background:#fff;border:1px solid #E1E6F0;border-radius:16px;padding:16px 18px;margin-bottom:10px;color:{TINTA}}}
.k{{display:grid;gap:4px}}.k small{{color:#4A5674;font-size:12.5px}}.tam{{display:flex;gap:18px;align-items:end}}figure{{margin:0;display:grid;justify-items:center;gap:6px;font-size:11px;color:#4A5674}}.dk{{background:#0F1C3F;--fondo:#0F1C3F;padding:8px;border-radius:8px;color:#C9D3EA}}
.lock{{display:flex;gap:12px;align-items:center;font:26px Sora}}.lock b{{font-weight:600}}.lock span{{color:#4A5674}}.lock b{{color:{TINTA}}}
.mock{{background:#fff;border:1px solid #E1E6F0;border-radius:16px;overflow:hidden}}.bar{{display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid #E1E6F0;font:16px Sora;color:#4A5674}}.bar b{{color:{TINTA};font-weight:600}}
.ai{{display:inline-block;width:40px;height:40px}}.ai svg{{width:100%;height:100%}}.ai.sm{{width:30px;height:30px}}.sp{{flex:1}}.srch{{font:14px Inst;color:#8A93A8;border:1px solid #E1E6F0;border-radius:10px;padding:8px 14px;width:300px}}
.eco{{width:40px;height:40px;border-radius:10px;border:0;background:transparent;display:grid;place-items:center;cursor:pointer}}.eco.on{{background:#E8EDF8;outline:2px solid {AZ};outline-offset:1px}}.av{{width:34px;height:34px;border-radius:50%;background:#D9DCE3;display:grid;place-items:center;font:600 12px Inst}}
.body{{position:relative;height:430px;background:#FAFBFD}}.pn{{position:absolute;right:58px;top:8px;width:400px;background:#fff;border:1px solid #E1E6F0;border-radius:16px;box-shadow:0 18px 40px rgba(20,33,61,.16);padding:16px}}
.ph{{display:flex;align-items:center;gap:8px;font:15px Sora;color:#4A5674;margin-bottom:12px}}.ph b{{color:{TINTA};font-weight:600}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}}
.tile{{display:grid;justify-items:center;gap:6px;padding:14px 6px 12px;border-radius:12px;font:600 13px Inst;color:{TINTA};position:relative}}.tile.on{{background:#EEF2FB}}.tile em{{font-style:normal;font-weight:500;font-size:11px;color:{AZ}}}
.pf{{border-top:1px solid #E1E6F0;margin-top:10px;padding-top:10px;font-size:12px;color:#4A5674;text-align:center}}.ghost{{padding:24px;display:grid;gap:12px;width:560px}}.gl{{height:14px;background:#EDF0F5;border-radius:6px;width:70%}}.gl.w{{width:90%}}.gl.w2{{width:50%}}
</style></head><body><h1>Ecosistema Manik · el identificador</h1><p class="i">Un botón que vive en la barra superior de cada módulo y abre el selector con las seis apps. Está en la retícula de 24 de los iconos de interfaz: es un icono, no un logotipo, así que debe leerse a 20 px junto a la campana y el avatar.</p>
{filas}<h2>Con la palabra · y en uso dentro de Farmacia Manik (con A)</h2>{lk}<div style="height:14px"></div>{panel}</body></html>""")
print('ok')
