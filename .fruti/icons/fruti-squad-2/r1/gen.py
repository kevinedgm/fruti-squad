# Fruti Squad for Kiro · identidad nueva (usuario 2026-10-30: «empezar de cero»), ronda 1 de símbolo.
# Verdad del producto: cada agente hace una sola clase de trabajo y entrega evidencia al siguiente (Kiwi → Lima → Coco → Bruno → Coco R0 → Lima → Mora).
# Tensión de marca: frutas (cercano, juguetón) + gobernanza (riguroso). Símbolos en tinta; color en la ronda 2. Uso: python3 gen.py → simbolos.html
import os, math
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#131313', '#f5f5f2'
def s(body, c=INK, bg='#fff'): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round">{body.replace("§", c).replace("¤", bg)}</svg>'
def gajos():
    out = ''
    for i in range(6):
        a0, a1 = math.radians(-90 + i * 60 + 8), math.radians(-90 + (i + 1) * 60 - 8)
        r = 25; cx, cy = 32, 33
        if i == 1: cx, cy = 32 + 4.5 * math.cos(math.radians(-60)), 32 + 4.5 * math.sin(math.radians(-60))  # el gajo que trabaja sale
        x0, y0, x1, y1 = cx + r * math.cos(a0), cy + r * math.sin(a0), cx + r * math.cos(a1), cy + r * math.sin(a1)
        hx, hy = cx + 5 * math.cos((a0 + a1) / 2), cy + 5 * math.sin((a0 + a1) / 2)
        out += f'<path d="M{hx:.1f} {hy:.1f}L{x0:.1f} {y0:.1f}A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}Z" fill="§" stroke="§" stroke-width="3" stroke-linejoin="round"/>'
    return out
S = [
 ('A', 'El relevo', 'Tres especialistas en fila; la evidencia (el punto) pasa de uno al siguiente.',
  'Cuenta la idea central del producto (entregar evidencia) en una forma.', 'Puede leerse como «progreso» o «carga» genérica si el punto no se distingue.',
  '<circle cx="12" cy="32" r="8" stroke="§" stroke-width="5"/><rect x="25" y="23" width="18" height="18" rx="5" stroke="§" stroke-width="5"/><path d="M52 23l8 9-8 9-8-9z" stroke="§" stroke-width="5"/><circle cx="34" cy="32" r="3.5" fill="§"/>'),
 ('B', 'El cajón', 'Cuatro casillas, cada fruta en la suya: responsabilidades separadas dentro de un mismo sistema.',
  'Dice «cada uno en su lugar» y «frutas» sin dibujar fruta literal; muy legible pequeño.', 'La rejilla 2×2 es común (apps, dashboards); el detalle interior se pierde a 16 px.',
  '<rect x="6" y="6" width="24" height="24" rx="7" fill="§"/><rect x="34" y="6" width="24" height="24" rx="7" stroke="§" stroke-width="4.5"/><circle cx="46" cy="18" r="4" fill="§"/><rect x="6" y="34" width="24" height="24" rx="7" stroke="§" stroke-width="4.5"/><path d="M12 46h12M18 40v12" stroke="§" stroke-width="4"/><rect x="34" y="34" width="24" height="24" rx="7" stroke="§" stroke-width="4.5"/><circle cx="42" cy="46" r="2.6" fill="§"/><circle cx="50" cy="46" r="2.6" fill="§"/><circle cx="46" cy="40" r="2.6" fill="§"/><circle cx="46" cy="52" r="2.6" fill="§"/>'),
 ('C', 'Los gajos', 'Un corte de cítrico: seis gajos separados forman una sola fruta; el que está trabajando sobresale.',
  'Fruta y sistema a la vez; el gajo que sale cuenta «uno a la vez, con su turno».', 'Cercano a los íconos de cítrico de marcas de bebidas; hay que cuidar que no se lea refresco.',
  gajos()),
 ('D', 'La línea', 'El flujo como línea de metro: cada estación es un agente y la última, con doble anillo, es lo entregado.',
  'El más fiel al proceso (orden, etapas, final verificable).', 'Recuerda a íconos de «flujo de trabajo» de muchas herramientas; menos fruta, más diagrama.',
  '<g transform="translate(-1 2)"><path d="M10 50V30a10 10 0 0 1 10-10h24a10 10 0 0 1 10 10v4" stroke="§" stroke-width="5"/><circle cx="10" cy="50" r="5.5" fill="§"/><circle cx="20" cy="20" r="5.5" fill="§"/><circle cx="44" cy="20" r="5.5" fill="§"/><circle cx="54" cy="44" r="8" stroke="§" stroke-width="4.5"/><circle cx="54" cy="44" r="3" fill="§"/></g>'),
]
def card(k, t, i, a, r, b):
    big = s(b); inv = s(b, '#ffffff', INK)
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{t}</h2></header>'
            f'<div class="lk"><span class="sym">{big}</span><span class="nm"><b>Fruti Squad</b><small>UI multiagente</small></span></div>'
            f'<div class="mini"><span class="t">{big}</span><span class="t s24">{big}</span><span class="t s16">{big}</span><span class="t ap">{inv}</span></div>'
            f'<p class="id">{i}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto}}h1{{font-size:28px;line-height:1.2;margin:0 0 6px}}.lead{{color:#4b4b47;max-width:880px;margin:0 0 22px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.c{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:10px;min-width:0}}
.c header{{display:flex;gap:10px;align-items:center}}.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font-size:18px;margin:0}}
.lk{{display:flex;align-items:center;gap:12px;margin-top:6px;min-width:0}}.sym svg{{width:60px;height:60px;display:block}}
.nm{{display:flex;flex-direction:column;line-height:1}}.nm b{{font-size:34px;letter-spacing:-.025em;font-weight:800}}.nm small{{font-size:15px;color:#4b4b47;margin-top:6px;font-weight:600}}
.mini{{display:flex;gap:8px;align-items:center}}.t{{width:40px;height:40px;border-radius:10px;border:1px solid #ececE6;display:grid;place-items:center}}.t svg{{width:32px;height:32px}}.t.s24 svg{{width:24px;height:24px}}.t.s16 svg{{width:16px;height:16px}}
.t.ap{{background:{INK};border-color:{INK}}}.t.ap svg{{width:26px;height:26px}}
.id{{margin:0;font-weight:600}}.pr{{margin:0;font-size:14px;color:#4b4b47}}.pr b{{color:{INK}}}
@media (max-width:820px){{.g{{grid-template-columns:1fr}}.nm b{{font-size:28px}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · símbolo nuevo</title>'
        f'<style>{css}</style></head><body><main><h1>Fruti Squad · identidad nueva, ronda 1</h1>'
        '<p class="lead">Desde cero. Todas las ideas salen de la frase que define el producto: «cada agente hace una sola clase de trabajo y entrega evidencia al siguiente». Y juegan con la tensión de la marca: frutas (cercano) y gobernanza (riguroso). En tinta a propósito: primero la forma, después el color. Tipografía provisional del sistema. Ya no es solo para Kiro: Codex, Kiro y Claude Code; el descriptor «UI multiagente» es provisional.</p>'
        f'<div class="g">{"".join(card(*x) for x in S)}</div></main></body></html>')
open(os.path.join(H, 'simbolos.html'), 'w').write(html); print('ok')
