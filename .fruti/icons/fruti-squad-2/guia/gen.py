# Fruti Squad · guía de marca + kit de marketplace. Usa el paquete de ../final (símbolos y tema).
# Uso: python3 gen.py <carpeta de fuentes> && node kit.cjs → kit/*.png, guia.html, textos.md
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); FIN = os.path.join(H, '..', 'final'); FD = sys.argv[1]
exec(open(os.path.join(H, 'textos.py')).read())
tema = json.load(open(os.path.join(FIN, 'tema.json')))
P = tema['productos']; ORDER = ['squad', 'kiwi', 'lima', 'coco', 'bruno', 'mora']
DARK, INK, PAPER = tema['color']['oscuro'], tema['color']['tinta'], tema['color']['papel']
def sv(k, n): return open(os.path.join(FIN, k, 'svg', n + '.svg')).read()
FONT_LOCAL = f"@font-face{{font-family:'Bricolage Grotesque';src:url('file://{FD}/BricolageGrotesque[opsz,wdth,wght].ttf');font-weight:200 800}}"
# ---- portadas (HTML para capturar) ----
os.makedirs(os.path.join(H, 'kit', 'src'), exist_ok=True)
def portada(k, w, h):
    n, p = P[k]['nombre'], P[k]['producto']; tag = T[k]['en'][0]
    acc = P[k]['color_oscuro'] or '#d4ff3a'
    fam = '' if k != 'squad' else '<div class="fam">' + ''.join(sv(x, 'simbolo-oscuro') for x in ORDER[1:]) + '</div>'
    sub = 'Fruti Squad · for Codex, Kiro and Claude Code' if k != 'squad' else 'for Codex, Kiro and Claude Code'
    return f'''<!doctype html><meta charset=utf-8><style>{FONT_LOCAL}*{{margin:0;box-sizing:border-box}}body{{width:{w}px;height:{h}px;background:{DARK};color:#fff;font-family:'Bricolage Grotesque';overflow:hidden;position:relative}}
.s{{position:absolute;left:{int(w*.07)}px;top:50%;transform:translateY(-50%);width:{int(h*.36)}px;height:{int(h*.36)}px}}.s svg{{width:100%;height:100%}}
.t{{position:absolute;left:{int(w*.07+h*.36+w*.05)}px;right:{int(w*.06)}px;top:50%;transform:translateY(-50%)}}
h1{{font-weight:700;font-size:{int(h*.12)}px;line-height:1;letter-spacing:-.02em}}h2{{font-weight:400;font-size:{int(h*.055)}px;color:#cfcfca;margin-top:{int(h*.02)}px}}
p{{font-weight:400;font-size:{int(h*.045)}px;color:#fff;margin-top:{int(h*.06)}px;max-width:{int(w*.5)}px;line-height:1.3}}
.k{{position:absolute;left:{int(w*.07)}px;bottom:{int(h*.07)}px;font-size:{int(h*.032)}px;color:#a1a1a1;letter-spacing:.02em}}
.bar{{position:absolute;left:0;top:0;height:{int(h*.018)}px;width:100%;background:{acc}}}
.fam{{position:absolute;right:{int(w*.06)}px;bottom:{int(h*.07)}px;display:flex;gap:{int(h*.025)}px}}.fam svg{{width:{int(h*.07)}px;height:{int(h*.07)}px}}</style>
<div class="bar"></div><div class="s">{sv(k, "simbolo-oscuro")}</div><div class="t"><h1>{n}</h1><h2>{p}</h2><p>{tag}</p></div><div class="k">{sub}</div>{fam}'''
jobs = []
for k in ORDER:
    for nm, w, h in (('og', 1200, 630), ('social', 1280, 640)):
        f = os.path.join(H, 'kit', 'src', f'{k}-{nm}.html'); open(f, 'w').write(portada(k, w, h).replace('<div class="bar"></div>', '' if k == 'squad' else '<div class="bar"></div>'))
        jobs.append([f, os.path.join(H, 'kit', f'{k}-{nm}-{w}x{h}.png'), w, h])
json.dump(jobs, open(os.path.join(H, 'kit', 'src', 'jobs.json'), 'w'))
# ---- textos.md ----
md = ['# Fruti Squad · textos de marketplace', '', 'Fuente de las responsabilidades: README del paquete. Lema corto + descripción, en español e inglés.', '']
for k in ORDER:
    md += [f"## {P[k]['nombre']} · {P[k]['producto']}", '', f"**ES** — {T[k]['es'][0]}", '', T[k]['es'][1], '', f"**EN** — {T[k]['en'][0]}", '', T[k]['en'][1], '']
open(os.path.join(H, 'textos.md'), 'w').write('\n'.join(md))
# ---- guía ----
def esc(s): return s.replace('&', '&amp;')
prods = ''.join(f'''<article class="pr"><div class="pv">{sv(k, "simbolo")}</div><div><h3>{esc(P[k]["nombre"])} <span>{esc(P[k]["producto"])}</span></h3><p class="tag">{esc(T[k]["es"][0])}</p><p>{esc(T[k]["es"][1])}</p>
<p class="meta"><b>Símbolo:</b> {["Espiral: los marcos de la familia girando; cada especialista entra en su turno","Tres tamaños: compact, medium y expanded; la estructura se mantiene","Biblioteca: marcos apilados, el de enfrente es el aprobado","Visor: esquinas que encuadran la pieza para revisarla","Cierre: la barra de &lt;/&gt; parte el marco; de plano punteado a pieza sólida","Red de conocimiento: piezas documentadas conectadas"][ORDER.index(k)]}{"" if k == "squad" else f' · <b>Color:</b> <i style="background:{P[k]["color_oscuro"]}"></i>{P[k]["color_oscuro"]} <i style="background:{P[k]["color_claro"]}"></i>{P[k]["color_claro"]}'}</p></div></article>''' for k in ORDER)
kitimgs = ''.join(f'<figure><img src="kit/{k}-og-1200x630.png" alt="Portada de {esc(P[k]["nombre"])}"><figcaption>{esc(P[k]["nombre"])} · 1200×630</figcaption></figure>' for k in ORDER)
mal = [('Pintar el trazo de color', sv('coco', 'simbolo').replace('stroke="#18181b"', 'stroke="#ff9f1c"')),
       ('Usar el color vivo sobre fondo claro', sv('lima', 'simbolo').replace('#6f8c00', '#d4ff3a')),
       ('Deformar o girar el símbolo', sv('kiwi', 'simbolo').replace('<svg ', '<svg style="transform:scaleX(1.5) rotate(12deg)" ')),
       ('Cambiar el color del punto entre integrantes', sv('mora', 'simbolo').replace('#d0156e', '#0f9e6e'))]
malh = ''.join(f'<figure class="no"><span>{s}</span><figcaption>✕ {t}</figcaption></figure>' for t, s in mal)
reglas = ''.join(f'<li>{esc(r)}</li>' for r in tema['reglas'])
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{PAPER};color:{INK};font:400 16px/1.6 'Bricolage Grotesque',system-ui,sans-serif;padding:0 max(16px,env(safe-area-inset-left)) 48px}}
main{{max-width:1080px;margin:0 auto;display:grid;gap:28px}}header.hero{{background:{DARK};color:#fff;border-radius:0 0 24px 24px;padding:56px 40px;display:flex;gap:32px;align-items:center;flex-wrap:wrap}}header.hero svg{{width:120px;height:120px}}
h1{{font-size:48px;line-height:1;letter-spacing:-.02em;margin:0}}.hero p{{margin:10px 0 0;color:#cfcfca;max-width:560px}}h2{{font-size:28px;letter-spacing:-.01em;margin:0 0 10px}}section>p{{margin:0 0 12px;max-width:760px;color:#3f3f3c}}
.pr{{display:grid;grid-template-columns:96px minmax(0,1fr);gap:20px;background:#fff;border:1px solid #e3e3de;border-radius:18px;padding:20px;margin-bottom:12px}}.pv svg{{width:96px;height:96px}}
h3{{margin:0;font-size:22px}}h3 span{{font-weight:400;color:#52525b}}.tag{{font-weight:700;margin:4px 0}}.pr p{{margin:4px 0;color:#3f3f3c}}.meta{{font-size:14px}}.meta i{{display:inline-block;width:12px;height:12px;border-radius:3px;margin:0 4px -1px 8px}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}figure{{margin:0}}figure img{{width:100%;border-radius:14px;display:block}}figcaption{{font-size:13px;color:#6b6b66;margin-top:6px}}
.no{{background:#fff;border:1px solid #e3e3de;border-radius:14px;padding:16px;display:grid;justify-items:center;gap:8px}}.no span svg{{width:72px;height:72px}}.no figcaption{{color:#b42318;font-weight:700}}.nos{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}}
.box{{background:#fff;border:1px solid #e3e3de;border-radius:18px;padding:22px}}.type b{{font-size:56px;letter-spacing:-.02em;line-height:1}}.type p{{margin:6px 0 0}}ol{{margin:0;padding-left:22px}}li{{margin:4px 0}}
.cons{{display:flex;gap:24px;align-items:center;flex-wrap:wrap}}.cons svg{{width:160px;height:160px;background-image:linear-gradient(#e7e7e2 1px,transparent 1px),linear-gradient(90deg,#e7e7e2 1px,transparent 1px);background-size:10px 10px;border-radius:8px}}
@media (max-width:760px){{.grid{{grid-template-columns:1fr}}.nos{{grid-template-columns:1fr 1fr}}.pr{{grid-template-columns:1fr}}h1{{font-size:36px}}header.hero{{padding:36px 20px}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · guía de marca</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,700&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><header class="hero">{sv("squad", "simbolo-oscuro")}<div><h1>Fruti Squad</h1><p>Guía de marca y kit de marketplace. Seis especialistas, un mismo idioma: cada agente hace una sola clase de trabajo y entrega evidencia al siguiente. Para Codex, Kiro y Claude Code.</p></div></header><main>'
        '<section><h2>La idea</h2><p>Todo el sistema está hecho de dos piezas: el <b>marco redondeado</b> (la pieza de interfaz) y el <b>punto</b> (la evidencia). Cada símbolo cuenta qué hace su agente con esas dos piezas, y el punto lleva el color de quien firma la evidencia. El orquestador reúne los cinco colores.</p>'
        f'<div class="box cons">{sv("kiwi", "simbolo")}<div><b>Construcción</b><p style="margin:4px 0 0">Cuadro de 64 unidades · trazo 3.5 (3 en la Espiral) · radios 5 a 15 · punto de 4 a 6.5 · margen de respeto: la mitad del símbolo alrededor.</p></div></div></section>'
        f'<section><h2>Los productos</h2>{prods}</section>'
        f'<section><h2>Color</h2><p>Duotono: el trazo siempre es neutro (tinta en claro, blanco en oscuro) y el color vive solo en el punto. Sobre oscuro se usan los tonos vivos; sobre claro, los oscurecidos.</p><div class="box"><ol>{reglas}</ol></div></section>'
        '<section><h2>Tipografía</h2><div class="box type"><b>Bricolage Grotesque</b><p>700 para el nombre, 400 para el producto y el texto. Licencia SIL Open Font (Google Fonts). En los logotipos va convertida a trazos.</p></div></section>'
        f'<section><h2>Usos incorrectos</h2><div class="nos">{malh}</div></section>'
        f'<section><h2>Kit de marketplace</h2><p>Portadas 1200×630 (Open Graph) y 1280×640 (vista previa social de GitHub) para cada producto, app icons de 512 y 192 px, y textos cortos en español e inglés en <code>textos.md</code>.</p><div class="grid">{kitimgs}</div></section>'
        '</main></body></html>')
open(os.path.join(H, 'guia.html'), 'w').write(html); print('ok', len(jobs))
