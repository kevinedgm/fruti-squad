# Fruti Squad · ronda 2: la identidad como SISTEMA de familia (usuario 2026-10-30: rediseñar al orquestador y a todos los integrantes,
# que se venderán también por separado: Kiwi UX Architect, Lima Design System Governance, Coco UI Audit, Fruti Squad Workflow Pack).
# Cada concepto de la ronda 1 se lleva a 6 piezas: un elemento CONSTANTE dice «familia», uno VARIABLE dice «quién».
# Verbos de cada integrante (README del paquete): Kiwi organizar · Lima validar · Coco inspeccionar · Bruno conectar · Mora catalogar · Squad orquestar.
import os, math
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#131313', '#f5f5f2'
def svg(b, c=INK, bg='#fff'): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round">{b.replace("§", c).replace("¤", bg)}</svg>'
M = ['Fruti Squad', 'Kiwi', 'Lima', 'Coco', 'Bruno', 'Mora']
V = ['orquestar', 'organizar', 'validar', 'inspeccionar', 'conectar', 'catalogar']
# A · forma + punto: el punto (la evidencia) es la constante; la forma, el rol
DOT = '<circle cx="32" cy="32" r="6" fill="§"/>'
def arcos():
    o = ''
    for i in range(5):
        a0, a1 = math.radians(-90 + i * 72 + 12), math.radians(-90 + (i + 1) * 72 - 12)
        o += f'<path d="M{32+23*math.cos(a0):.1f} {32+23*math.sin(a0):.1f}A23 23 0 0 1 {32+23*math.cos(a1):.1f} {32+23*math.sin(a1):.1f}" stroke="§" stroke-width="6"/>'
    return o
A = [arcos() + '<circle cx="32" cy="32" r="8" fill="§"/>',
     '<rect x="9" y="9" width="46" height="46" rx="11" stroke="§" stroke-width="6"/>' + DOT,
     '<path d="M32 7l22 8v16c0 14-9 23-22 27C19 54 10 45 10 31V15z" stroke="§" stroke-width="6"/>' + DOT,
     '<circle cx="28" cy="28" r="19" stroke="§" stroke-width="6"/><path d="M42 42l14 14" stroke="§" stroke-width="7"/><circle cx="28" cy="28" r="6" fill="§"/>',
     '<path d="M32 7l22 12.5v25L32 57 10 44.5v-25z" stroke="§" stroke-width="6"/>' + DOT,
     '<path d="M15 8h34v48L32 45 15 56z" stroke="§" stroke-width="6"/><circle cx="32" cy="25" r="6" fill="§"/>']
# B · el cajón: la casilla es la constante; la marca interior, el rol
CAJ = '<rect x="7" y="7" width="50" height="50" rx="13" stroke="§" stroke-width="5.5"/>'
def cajon6():
    o = ''
    for r in range(2):
        for c in range(3):
            x, y = 6 + c * 18, 15 + r * 18
            o += f'<rect x="{x}" y="{y}" width="15" height="15" rx="4.5" ' + ('fill="§"/>' if (r, c) == (0, 0) else 'stroke="§" stroke-width="4"/>')
    return o
B = [cajon6(),
     CAJ + '<path d="M20 32h24M32 20v24" stroke="§" stroke-width="5"/>',
     CAJ + '<path d="M20 33l8 8 16-17" stroke="§" stroke-width="6"/>',
     CAJ + '<circle cx="29" cy="29" r="9" stroke="§" stroke-width="5"/><path d="M36 36l8 8" stroke="§" stroke-width="5.5"/>',
     CAJ + '<circle cx="21" cy="32" r="5" fill="§"/><circle cx="43" cy="32" r="5" fill="§"/><path d="M26 32h12" stroke="§" stroke-width="5"/>',
     CAJ + '<path d="M20 23h24M20 32h24M20 41h14" stroke="§" stroke-width="5"/>']
# C · los gajos: la fruta es la constante; el gajo que sale es el integrante
def gajos(act):
    o = ''
    for i in range(5):
        a0, a1 = math.radians(-90 + i * 72 + 9), math.radians(-90 + (i + 1) * 72 - 9)
        am = (a0 + a1) / 2; d = 5 if i == act else 0
        cx, cy = 32 + d * math.cos(am), 33 + d * math.sin(am); r = 25
        hx, hy = cx + 5 * math.cos(am), cy + 5 * math.sin(am)
        p = f'M{hx:.1f} {hy:.1f}L{cx+r*math.cos(a0):.1f} {cy+r*math.sin(a0):.1f}A{r} {r} 0 0 1 {cx+r*math.cos(a1):.1f} {cy+r*math.sin(a1):.1f}Z'
        o += f'<path d="{p}" ' + ('fill="§" stroke="§" stroke-width="3"/>' if act < 0 or i == act else 'stroke="§" stroke-width="3"/>')
    return o
C = [gajos(-1)] + [gajos(i) for i in range(5)]
SIS = [
 ('A', 'Forma + evidencia', 'El punto es la evidencia que todos producen y entregan: es lo constante. La forma dice quién es: casilla (organiza), escudo (valida), lupa (inspecciona), tuerca (conecta), separador (cataloga). El orquestador es el punto rodeado por los cinco.', A,
  'Cada integrante se reconoce por silueta, sin color: funciona solo en un marketplace y junto a los demás. La constante (el punto) cuenta la idea del producto.', 'Lupa y escudo son formas muy usadas; el dibujo tiene que ser propio en el detalle (proporción, esquinas).'),
 ('B', 'El cajón', 'La casilla es lo constante; la marca interior dice el rol. El orquestador es el cajón completo.', B,
  'El más ordenado y fácil de extender a nuevos integrantes (Mango, Uva).', 'Silueta igual para todos (un cuadrado): de lejos o a 16 px solo los distingue la marca interior.'),
 ('C', 'Los gajos', 'La fruta es lo constante; cada integrante es su gajo, que sale de la fruta. El orquestador es la fruta completa.', C,
  'La más «fruta» y la más poética: todos son parte del mismo cítrico.', 'Los integrantes solo se distinguen por la posición del gajo: separados, sin el resto, se parecen demasiado.'),
]
def cel(b, n, v, dk=False):
    return f'<figure class="m{" dk" if dk else ""}">{svg(b, "#fff" if dk else INK)}<figcaption><b>{n}</b><span>{v}</span></figcaption></figure>'
def card(k, t, i, S, a, r):
    fila = ''.join(cel(b, n, v, j == 0) for j, (b, n, v) in enumerate(zip(S, M, V)))
    peq = ''.join(f'<span class="t">{svg(b)}</span>' for b in S)
    lock = (f'<div class="lk">{svg(S[3])}<span><b>Coco</b><i>UI Audit</i><small>de Fruti Squad</small></span></div>'
            f'<div class="lk">{svg(S[0])}<span><b>Fruti Squad</b><i>Workflow Pack</i></span></div>')
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{t}</h2></header><p class="id">{i}</p><div class="fam">{fila}</div>'
            f'<p class="lb">A 16 px:</p><div class="peq">{peq}</div><p class="lb">Como producto en un marketplace:</p><div class="lks">{lock}</div>'
            f'<p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{color:#4b4b47;max-width:900px;margin:0}}
.c{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:12px;min-width:0}}
.c header{{display:flex;gap:10px;align-items:center}}.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font-size:18px;margin:0}}.id{{margin:0;color:#3a3a37}}
.fam{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px}}.m{{margin:0;border:1px solid #ececE6;border-radius:14px;padding:14px 8px;display:grid;justify-items:center;gap:8px;text-align:center}}
.m svg{{width:56px;height:56px}}.m.dk{{background:{INK};color:#fff;border-color:{INK}}}.m figcaption{{display:grid;line-height:1.2}}.m b{{font-size:14px}}.m span{{font-size:12px;opacity:.75}}
.lb{{margin:0;font-weight:700;font-size:13px}}.peq{{display:flex;gap:10px}}.t{{width:34px;height:34px;border:1px solid #ececE6;border-radius:9px;display:grid;place-items:center}}.t svg{{width:16px;height:16px}}
.lks{{display:flex;flex-wrap:wrap;gap:12px}}.lk{{display:flex;align-items:center;gap:12px;border:1px solid #ececE6;border-radius:14px;padding:14px 18px}}.lk svg{{width:48px;height:48px;flex:none}}
.lk span{{display:grid;line-height:1.1}}.lk b{{font-size:24px;letter-spacing:-.02em}}.lk i{{font-style:normal;font-size:16px;font-weight:600;color:#4b4b47}}.lk small{{font-size:12px;color:#6b6b66;margin-top:3px}}
.pr{{margin:0;font-size:14px;color:#4b4b47}}.pr b{{color:{INK}}}
@media (max-width:900px){{.fam{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}@media (max-width:420px){{.fam{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · familia</title>'
        f'<style>{css}</style></head><body><main><h1>Fruti Squad · la identidad como familia (ronda 2)</h1>'
        '<p class="lead">Ahora cada integrante también se vende solo (Kiwi UX Architect, Lima Design System Governance, Coco UI Audit) y el squad se vende como paquete. Así que el símbolo ya no se elige solo: se elige el sistema que genera seis símbolos coherentes. Regla de cada sistema: un elemento constante dice «es de Fruti Squad» y uno variable dice «quién es». En tinta: el color va en la siguiente ronda.</p>'
        f'{"".join(card(*x) for x in SIS)}</main></body></html>')
open(os.path.join(H, 'familia.html'), 'w').write(html); print('ok')
