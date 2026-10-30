# Fruti Squad · ronda 3: el método de Manik y Nisa Nabani aplicado a la squad (usuario 2026-10-30).
# Sello madre = cuadro de color con una marca blanca CONSTANTE; cada producto = mismo sello + un RASGO en el borde (silueta o pieza separada por un corte)
# + color propio. El color nunca es la única señal. Identificador del ecosistema: retícula de seis cuadros.
# Marca constante: la fruta (círculo con hoja) con la semilla calada: «Fruti» + la evidencia que cada agente entrega.
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
P = [  # id, nombre, rol (producto), verbo, color, color de la marca, rasgo
 ('squad', 'Fruti Squad', 'Workflow Pack', 'orquestar', '#18181b', '#ffffff'),
 ('kiwi', 'Kiwi', 'UX Architect', 'organizar', '#4f8a2b', '#ffffff'),
 ('lima', 'Lima', 'Design System Governance', 'validar', '#c5e04b', INK),
 ('coco', 'Coco', 'UI Audit', 'inspeccionar', '#8a5a3b', '#ffffff'),
 ('bruno', 'Bruno', 'Implementation', 'conectar', '#2563eb', '#ffffff'),
 ('mora', 'Mora', 'Documentation', 'catalogar', '#7e2e8c', '#ffffff'),
]
def lum(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def cr(a, b): x, y = sorted((lum(a), lum(b))); return (y + .05) / (x + .05)
TILE = '<rect x="8" y="8" width="48" height="48" rx="13"/>'
# rasgos: (forma que se recorta del cuadro con un margen, forma que se dibuja)
R = {
 'squad': ('', ''),
 'kiwi': ('<rect x="40" y="2" width="22" height="22" rx="7"/>', '<rect x="43" y="5" width="16" height="16" rx="5"/>'),
 'lima': ('<circle cx="51" cy="13" r="12"/>', '<circle cx="51" cy="13" r="9"/><path d="M46.5 13l3 3 5.5-6" stroke="¤" stroke-width="2.6" fill="none"/>'),
 'coco': ('<path d="M44 44l16 16" stroke-width="13" stroke="#000"/>', '<path d="M47 47l12 12" stroke-width="7" stroke="§" stroke-linecap="round"/>'),
 'bruno': ('<rect x="52" y="24" width="12" height="16" rx="4"/>', '<rect x="55" y="26" width="7" height="12" rx="2.5"/><path d="M62 29h2M62 35h2" stroke="§" stroke-width="2.5"/>'),
 'mora': ('', ''),
}
def marca(c):  # fruta con hoja y semilla calada
    return (f'<circle cx="30" cy="36" r="12.5" fill="{c}"/><path d="M33 24.5c0-6.5 5.5-11 12.5-11 0 6.5-5.5 11-12.5 11z" fill="{c}"/>'
            f'<circle cx="30" cy="36" r="3.8" fill="#000"/>')
def sello(k, color, mc, uid, tinta=False):
    cut, draw = R[k]
    if tinta: color, mc = 'currentColor', None
    m = (f'<mask id="m{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/>'
         f'<g fill="#000">{cut}</g>' + marca('#000').replace('fill="#000"/>', 'fill="#000"/>', 1) + '</mask>')
    # la marca se cala en la versión a una tinta; en color se pinta encima
    mk = '' if tinta else marca(mc).replace('<circle cx="30" cy="36" r="3.8" fill="#000"/>', f'<circle cx="30" cy="36" r="3.8" fill="{color}"/>')
    tile_mask = (f'<mask id="t{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/><g fill="#000">{cut}</g>'
                 + (marca('#000') if tinta else '') + '</mask>')
    if tinta:
        tile_mask = tile_mask.replace('<circle cx="30" cy="36" r="3.8" fill="#000"/>', '<circle cx="30" cy="36" r="3.8" fill="#fff"/>')
    d = draw.replace('§', color).replace('¤', mc if mc else '#fff')
    if tinta: d = draw.replace('§', 'currentColor').replace('¤', '#fff')
    back = ''
    if k == 'mora':
        back = (f'<mask id="b{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/>'
                f'<rect x="5" y="5" width="54" height="54" rx="16" fill="#000"/></mask><rect x="15" y="1" width="46" height="46" rx="13" fill="{color}" mask="url(#b{uid})"/>')
    return (f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{back}{tile_mask}<g mask="url(#t{uid})" fill="{color}">{TILE}</g>'
            f'<g fill="{color}">{d}</g>{mk}</svg>')
u = [0]
def S(k, c, mc, t=False):
    u[0] += 1; return sello(k, c, mc, u[0], t)
def nombre(n, r): return f'<span class="nm"><b>{n}</b> {r}</span>'
fila = ''.join(f'<figure class="p">{S(k, c, mc)}<figcaption><b>{n}</b><span>{r}</span><code>{c}</code></figcaption></figure>' for k, n, r, v, c, mc in P)
tinta = ''.join(f'<span class="ti">{S(k, c, mc, True)}</span>' for k, n, r, v, c, mc in P)
oscuro = ''.join(f'<span class="ti">{S(k, c if k != "squad" else "#f5f5f2", mc if k != "squad" else INK)}</span>' for k, n, r, v, c, mc in P)
peq = ''.join(f'<span class="pq">{S(k, c, mc)}</span>' for k, n, r, v, c, mc in P)
eco = '<svg viewBox="0 0 64 44" class="eco" aria-hidden="true">' + ''.join(f'<rect x="{4+(i%3)*20}" y="{4+(i//3)*20}" width="16" height="16" rx="5" fill="{c}"/>' for i, (k, n, r, v, c, mc) in enumerate(P)) + '</svg>'
eco1 = '<svg viewBox="0 0 64 44" class="eco" aria-hidden="true">' + ''.join(f'<rect x="{4+(i%3)*20}" y="{4+(i//3)*20}" width="16" height="16" rx="5" fill="{INK}"/>' for i in range(6)) + '</svg>'
locks = ''.join(f'<div class="lk">{S(k, c, mc)}<span><b>{n}</b><i>{r}</i>{"" if k == "squad" else "<small>de Fruti Squad</small>"}</span></div>' for k, n, r, v, c, mc in P[:4])
rows = ''.join(f'<tr><td><span class="sw" style="background:{c}"></span></td><td><b>{n}</b> {r}</td><td>{v}</td><td>{"blanca" if mc == "#ffffff" else "tinta"} sobre color {cr(c, mc):.1f}:1</td></tr>' for k, n, r, v, c, mc in P)
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.c{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:22px;display:grid;gap:14px;min-width:0}}.c.dk{{background:{INK};color:#fff;border-color:{INK}}}h2{{font-size:17px;margin:0}}
.fila{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px}}.p{{margin:0;display:grid;justify-items:center;gap:8px;text-align:center}}.p svg{{width:100px;height:100px}}
.p figcaption{{display:grid;line-height:1.25}}.p b{{font-size:15px}}.p span{{font-size:13px;color:#4b4b47}}.p code{{font-size:11.5px;color:#6b6b66}}
.ti svg{{width:64px;height:64px;color:{INK}}}.dk .ti svg{{color:#fff}}.row{{display:flex;flex-wrap:wrap;gap:18px;align-items:center}}.pq svg{{width:16px;height:16px}}.pq{{display:inline-grid;place-items:center;width:30px;height:30px;border:1px solid #ececE6;border-radius:8px}}
.eco{{width:96px;height:66px}}.ecot{{font-size:30px;letter-spacing:-.02em}}.ecot b{{font-weight:800}}
.lks{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}}.lk{{display:flex;align-items:center;gap:14px;border:1px solid #ececE6;border-radius:14px;padding:14px 18px;min-width:0}}.lk svg{{width:56px;height:56px;flex:none}}
.lk span{{display:grid;line-height:1.15;min-width:0}}.lk b{{font-size:24px;letter-spacing:-.02em;font-weight:700}}.lk i{{font-style:normal;font-size:16px;color:#3f3f3c}}.lk small{{font-size:12px;color:#6b6b66;margin-top:3px}}
table{{border-collapse:collapse;width:100%;font-size:14px}}td,th{{padding:8px 6px;border-bottom:1px solid #ececE6;text-align:left;vertical-align:middle}}th{{font-size:12px;color:#6b6b66;text-transform:uppercase;letter-spacing:.05em}}.sw{{display:block;width:20px;height:20px;border-radius:6px}}
ol{{margin:0;padding-left:20px;color:#3a3a37}}li{{margin:3px 0}}
@media (max-width:900px){{.fila{{grid-template-columns:repeat(3,minmax(0,1fr))}}.lks{{grid-template-columns:1fr}}}}@media (max-width:440px){{.fila{{grid-template-columns:repeat(2,minmax(0,1fr))}}.p svg{{width:84px;height:84px}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Ecosistema Fruti Squad</title>'
        f'<style>{css}</style></head><body><main><h1>Ecosistema Fruti Squad · propuesta (ronda 3)</h1>'
        '<p class="lead">El mismo método que Manik y Nisa Nabani: un sello madre y, por cada producto, el mismo sello con un rasgo propio en el borde y su color. La marca blanca del centro es constante: una fruta con la semilla calada, que es «Fruti» y es la evidencia que cada agente entrega al siguiente. Nombres de Bruno y Mora como producto: provisionales. Tipografía provisional.</p>'
        f'<section class="c"><h2>Sello madre y productos</h2><div class="fila">{fila}</div></section>'
        f'<section class="c"><h2>A una tinta · a 16 px</h2><div class="row">{tinta}</div><div class="row">{peq}</div></section>'
        f'<section class="c dk"><h2>Sobre fondo oscuro</h2><div class="row">{oscuro}</div></section>'
        f'<section class="c"><h2>Como producto en un marketplace</h2><div class="lks">{locks}</div></section>'
        f'<section class="c"><h2>Identificador del ecosistema</h2><div class="row">{eco}{eco1}<span class="ecot"><b>Fruti</b> Squad</span></div></section>'
        f'<section class="c"><h2>Rasgo, verbo y contraste</h2><table><thead><tr><th></th><th>Producto</th><th>Verbo</th><th>Marca sobre su color</th></tr></thead><tbody>{rows}</tbody></table>'
        '<ol><li>La fruta del centro es idéntica en todos; nunca se redibuja por producto.</li><li>El rasgo vive en el borde: pieza separada por un corte (casilla de Kiwi, insignia de Lima, mango de lupa de Coco, conector de Bruno) o silueta (la ficha detrás de Mora: una colección).</li><li>El color acompaña al nombre; nunca es la única señal.</li><li>Lima es el único color claro: su marca va en tinta.</li></ol></section>'
        '</main></body></html>')
open(os.path.join(H, 'ecosistema.html'), 'w').write(html); print('ok')
