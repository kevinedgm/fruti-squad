# Fruti Squad · ronda 5: tres propuestas originales completas (usuario: «no, preséntame 3 propuestas originales»).
# Cada una es un sistema entero (squad + cinco integrantes), con color, y evita los motivos genéricos de las rondas anteriores (palomita, hoja, F, flechas).
import os, math
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
N = [('squad', 'Fruti Squad', 'Workflow Pack'), ('kiwi', 'Kiwi', 'UX Architect'), ('lima', 'Lima', 'Design System Governance'),
     ('coco', 'Coco', 'UI Audit'), ('bruno', 'Bruno', 'Implementation'), ('mora', 'Mora', 'Documentation')]
def svg(b): return f'<svg viewBox="0 0 64 64" aria-hidden="true">{b}</svg>'
# ---------- A · personajes: cada agente es su fruta con cara mínima ----------
EYES = '<circle cx="26.5" cy="33" r="2.8" fill="{e}"/><circle cx="37.5" cy="33" r="2.8" fill="{e}"/><path d="M27.5 40q4.5 3.6 9 0" stroke="{e}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
def cara(e=INK, dy=0): return f'<g transform="translate(0 {dy})">' + EYES.format(e=e) + '</g>'
A = {
 'kiwi': '<circle cx="32" cy="33" r="25" fill="#6b4f2c"/><circle cx="32" cy="33" r="20.5" fill="#8cc63f"/>' + ''.join(f'<circle cx="{32+14*math.cos(math.radians(a)):.1f}" cy="{33+14*math.sin(math.radians(a)):.1f}" r="1.6" fill="#2b2b1f"/>' for a in range(-60, 241, 30) if not 30 < a < 150) + cara(),
 'lima': '<path d="M44 12c5-4 11-4 14-1-3 4-8 6-14 4z" fill="#3f7d20"/><circle cx="32" cy="35" r="24" fill="#b5d334"/><circle cx="32" cy="35" r="19" fill="#e4f08a"/>' + cara(dy=2),
 'coco': '<path d="M7 34a25 25 0 0 1 50 0z" fill="#5b3a1e"/><path d="M7 34h50a25 25 0 0 1-50 0z" fill="#5b3a1e"/><circle cx="32" cy="34" r="19" fill="#fbf6ec"/>' + cara(),
 'bruno': '<path d="M32 7c13 9 20 20 20 30a20 20 0 0 1-40 0c0-10 7-21 20-30z" fill="#c98a43"/><path d="M32 16c-6 7-9 14-9 21" stroke="#a96c2c" stroke-width="2.5" fill="none" stroke-linecap="round"/>' + cara(dy=4),
 'mora': ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#6d2a7a"/>' for x, y in [(22, 24), (32, 19), (42, 24), (17, 35), (27, 31), (37, 31), (47, 35), (22, 45), (32, 43), (42, 45), (32, 53)]) + '<path d="M28 9l4 6 4-6" stroke="#3f7d20" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' + cara('#fff', 1),
}
A['squad'] = ('<rect x="2" y="2" width="60" height="60" rx="16" fill="' + INK + '"/>' +
             ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="{c}"/>' for x, y, c in [(20, 22, '#8cc63f'), (44, 22, '#b5d334'), (32, 33, '#fbf6ec'), (20, 44, '#c98a43'), (44, 44, '#6d2a7a')]) +
             '<circle cx="29" cy="32" r="1.6" fill="#18181b"/><circle cx="35" cy="32" r="1.6" fill="#18181b"/><path d="M29.5 36q2.5 2 5 0" stroke="#18181b" stroke-width="1.6" fill="none" stroke-linecap="round"/>')
# ---------- B · cortes: la sección transversal de cada fruta, plana y geométrica ----------
B = {
 'kiwi': '<circle cx="32" cy="32" r="27" fill="#4f8a2b"/><ellipse cx="32" cy="32" rx="7" ry="9" fill="#e9f5c9"/>' + ''.join(f'<ellipse cx="{32+15*math.cos(math.radians(a)):.1f}" cy="{32+15*math.sin(math.radians(a)):.1f}" rx="1.7" ry="3.4" transform="rotate({a+90} {32+15*math.cos(math.radians(a)):.1f} {32+15*math.sin(math.radians(a)):.1f})" fill="#141414"/>' for a in range(0, 360, 30)),
 'lima': '<circle cx="32" cy="32" r="27" fill="#9cc83a"/><circle cx="32" cy="32" r="22" fill="#d8ec7a"/>' + ''.join(f'<path d="M32 32L{32+22*math.cos(math.radians(a)):.1f} {32+22*math.sin(math.radians(a)):.1f}" stroke="#9cc83a" stroke-width="3"/>' for a in range(0, 360, 45)) + '<circle cx="32" cy="32" r="4" fill="#9cc83a"/>',
 'coco': '<circle cx="32" cy="32" r="27" fill="#4a2f17"/><circle cx="32" cy="32" r="19" fill="#fbf6ec"/><circle cx="32" cy="32" r="11" fill="#d9ecf2"/>',
 'bruno': '<path d="M32 5c16 10 23 22 23 31a23 23 0 0 1-46 0c0-9 7-21 23-31z" fill="#b8762f"/><path d="M32 13c9 8 13 16 13 23a13 13 0 0 1-26 0c0-7 4-15 13-23z" fill="#f2dcb8"/>',
 'mora': ''.join(f'<circle cx="{32+r*math.cos(math.radians(a)):.1f}" cy="{32+r*math.sin(math.radians(a)):.1f}" r="8.6" fill="#6d2a7a"/>' for r, a in [(0, 0)] + [(17, x) for x in range(0, 360, 60)]) + ''.join(f'<circle cx="{32+r*math.cos(math.radians(a)):.1f}" cy="{32+r*math.sin(math.radians(a)):.1f}" r="3" fill="#b05bbf"/>' for r, a in [(0, 0)] + [(17, x) for x in range(0, 360, 60)]),
}
B['squad'] = ''.join(f'<circle cx="32" cy="32" r="{r}" fill="{c}"/>' for r, c in [(28, '#18181b'), (23, '#6d2a7a'), (18.5, '#b8762f'), (14, '#4a2f17'), (9.5, '#9cc83a'), (5, '#4f8a2b')])
# ---------- C · etiquetas: la calcomanía de la fruta del súper, con su código (registro y trazabilidad) ----------
def etq(shape, color, letra, cod, tx='#fff'):
    return (f'<g>{shape.format(f=color, s="none")}{shape.format(f="none", s=tx).replace("<", "<", 1)}'
            f'<text x="32" y="36" text-anchor="middle" font-family="system-ui,Segoe UI,sans-serif" font-weight="800" font-size="22" fill="{tx}">{letra}</text>'
            f'<text x="32" y="47" text-anchor="middle" font-family="ui-monospace,monospace" font-weight="700" font-size="7" fill="{tx}" letter-spacing=".5">{cod}</text></g>')
SH = {
 'oval': '<ellipse cx="32" cy="32" rx="29" ry="22" fill="{f}" stroke="{s}" stroke-width="2.4" transform-origin="32 32"/>',
 'circ': '<circle cx="32" cy="32" r="27" fill="{f}" stroke="{s}" stroke-width="2.4"/>',
 'cuad': '<rect x="6" y="6" width="52" height="52" rx="14" fill="{f}" stroke="{s}" stroke-width="2.4"/>',
 'hex': '<path d="M32 4l25 14v28L32 60 7 46V18z" fill="{f}" stroke="{s}" stroke-width="2.4" stroke-linejoin="round"/>',
 'flor': '<path d="' + 'M'.join([''] ) + '"/>',
}
def flor(f, s):
    pts = []
    for i in range(24):
        a = math.radians(i * 15); r = 28 if i % 2 == 0 else 24.5
        pts.append(f'{32+r*math.cos(a):.1f} {32+r*math.sin(a):.1f}')
    return f'<path d="M{" L".join(pts)}Z" fill="{f}" stroke="{s}" stroke-width="2.4" stroke-linejoin="round"/>'
def etq2(kind, color, letra, cod, tx='#fff'):
    if kind == 'flor':
        base, ring = flor(color, 'none'), ''
        inner = flor('none', tx).replace('<path', '<path transform="translate(32 32) scale(.84) translate(-32 -32)"')
    else:
        base = SH[kind].format(f=color, s='none'); inner = SH[kind].format(f='none', s=tx).replace('<', '<g transform="translate(32 32) scale(.86) translate(-32 -32)"><', 1) + '</g>'
    return (base + inner + f'<text x="32" y="{37 if kind != "oval" else 36}" text-anchor="middle" font-family="system-ui,Segoe UI,sans-serif" font-weight="800" font-size="21" fill="{tx}">{letra}</text>'
            f'<text x="32" y="47" text-anchor="middle" font-family="ui-monospace,monospace" font-weight="700" font-size="6.5" fill="{tx}">{cod}</text>')
C = {
 'squad': etq2('oval', INK, 'FS', 'SQUAD', '#f5f5f2'),
 'kiwi': etq2('oval', '#4f8a2b', 'K', 'UX·01'),
 'lima': etq2('circ', '#c5e04b', 'L', 'DS·02', INK),
 'coco': etq2('cuad', '#6b4226', 'C', 'QA·03'),
 'bruno': etq2('hex', '#2563eb', 'B', 'IM·04'),
 'mora': etq2('flor', '#7e2e8c', 'M', 'DOC·05'),
}
P = [
 ('A', 'Personajes', 'Cada agente es su fruta con una cara mínima (dos puntos y una sonrisa). Bruno, que no es fruta, es una semilla. El squad es el grupo reunido.', A,
  'La más memorable y la más fácil de querer: en un marketplace lleno de iconos abstractos, una cara se recuerda. Sirve para avatares, stickers y mensajes de bienvenida.', 'Puede sentirse infantil para un producto de gobernanza; hay que mantener las caras mínimas y el tono de los textos serio.'),
 ('B', 'Cortes', 'La sección transversal real de cada fruta, reducida a geometría plana: las semillas del kiwi, los gajos de la lima, la pulpa del coco, las drupas de la mora, la almendra de Bruno. El squad es un corte de anillos con los colores de todos.', B,
  'Muy gráfica y propia (estilo afiche); la fruta se reconoce sin ser caricatura. El squad en anillos se ve como un sello.', 'Todos son círculos: a 16 px se distinguen sobre todo por color y patrón, menos por silueta.'),
 ('C', 'Etiquetas', 'La calcomanía que traen las frutas del súper, con su código. Cada agente tiene su forma de etiqueta, su letra y un código (UX·01, DS·02…): fruta y, a la vez, registro y trazabilidad, que es lo que hace la squad.', C,
  'La más original del sector y la que mejor une las dos mitades: lo fresco de la fruta y el rigor del registro. Cada forma de etiqueta es distinta, así que se reconocen por silueta.', 'El código no se lee a 16 px (solo la letra); la referencia a la etiqueta del súper hay que explicarla una vez para que se aprecie.'),
]
def card(k, t, i, D, a, r):
    fila = ''.join(f'<figure class="p">{svg(D[id_])}<figcaption><b>{n}</b><span>{rol}</span></figcaption></figure>' for id_, n, rol in N)
    peq = ''.join(f'<span class="pq">{svg(D[id_])}</span>' for id_, n, rol in N)
    lk = ''.join(f'<div class="lk">{svg(D[id_])}<span><b>{n}</b><i>{rol}</i><small>{"de Fruti Squad" if id_ != "squad" else "Kiwi · Lima · Coco · Bruno · Mora"}</small></span></div>' for id_, n, rol in (N[3], N[0]))
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{t}</h2></header><p class="id">{i}</p><div class="fila">{fila}</div>'
            f'<div class="row"><span class="lb">A 16 px</span>{peq}<span class="dkb">{"".join(svg(D[x]) for x, _, _ in N)}</span></div><div class="lks">{lk}</div>'
            f'<p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.c{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:22px;display:grid;gap:14px;min-width:0}}.c header{{display:flex;gap:10px;align-items:center}}
.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font-size:19px;margin:0}}.id{{margin:0;color:#3a3a37}}
.fila{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px}}.p{{margin:0;display:grid;justify-items:center;gap:8px;text-align:center}}.p svg{{width:100%;max-width:104px;height:auto}}
.p figcaption{{display:grid;line-height:1.25}}.p b{{font-size:15px}}.p span{{font-size:12.5px;color:#4b4b47}}
.row{{display:flex;flex-wrap:wrap;gap:8px;align-items:center}}.lb{{font-size:12px;font-weight:700;color:#6b6b66}}.pq{{display:inline-grid;place-items:center;width:28px;height:28px;border:1px solid #ececE6;border-radius:7px}}.pq svg{{width:16px;height:16px}}
.dkb{{display:inline-flex;gap:8px;background:{INK};border-radius:10px;padding:8px;margin-left:8px}}.dkb svg{{width:30px;height:30px}}
.lks{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}}.lk{{display:flex;align-items:center;gap:14px;border:1px solid #ececE6;border-radius:14px;padding:12px 16px;min-width:0}}.lk svg{{width:56px;height:56px;flex:none}}
.lk span{{display:grid;line-height:1.15;min-width:0}}.lk b{{font-size:22px}}.lk i{{font-style:normal;color:#3f3f3c}}.lk small{{font-size:12px;color:#6b6b66}}
.pr{{margin:0;font-size:14px;color:#4b4b47}}.pr b{{color:{INK}}}
@media (max-width:900px){{.fila{{grid-template-columns:repeat(3,minmax(0,1fr))}}.lks{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · tres propuestas</title>'
        f'<style>{css}</style></head><body><main><h1>Fruti Squad · tres propuestas originales (ronda 5)</h1>'
        '<p class="lead">Tres sistemas completos, con color, para el squad y sus cinco integrantes. Dejé fuera los motivos genéricos de las rondas anteriores (palomita, hoja, letra F, flechas y el mismo cuadro para todos). Cada uno se ve en grande, a 16 px, sobre oscuro y como producto. Nombres de Bruno y Mora como producto: provisionales.</p>'
        f'{"".join(card(*x) for x in P)}</main></body></html>')
open(os.path.join(H, 'propuestas.html'), 'w').write(html); print('ok')
