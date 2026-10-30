# Mesanda (de CLNDA Studio) · ronda 2 de símbolo. Ronda 2: A y D elegidos por el usuario + híbridos H1–H3.
# Símbolos en tinta a propósito: se decide la forma sin que el color la secuestre; el color va en la ronda 2 (evitar el naranja del competidor).
# Uso: python3 gen.py → simbolos.html
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#14161f', '#f6f6f3'
def s(body, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round">{body.replace("§", c)}</svg>'
CAP_T = '<rect x="24" y="7" width="16" height="7" rx="3.5" fill="§"/>'
CAP_B = '<rect x="24" y="50" width="16" height="7" rx="3.5" fill="§"/>'
CAP_L = '<rect x="7" y="24" width="7" height="16" rx="3.5" fill="§"/>'
CAP_R = '<rect x="50" y="24" width="7" height="16" rx="3.5" fill="§"/>'
MESA = '<circle cx="32" cy="32" r="14" fill="§"/>'
S = [
 ('A', 'La mesa en el plano', 'La ronda 1 tal cual: mesa redonda y cuatro sillas.',
  'La más clara y la más fiel a la interfaz.', 'Quieta: no cuenta la rapidez.', MESA + CAP_T + CAP_B + CAP_L + CAP_R),
 ('D', 'La mesa que anda', 'La ronda 1 tal cual: mesa con líneas de velocidad.',
  'Cuenta la promesa de rapidez.', 'Sin sillas, puede leerse como un punto en movimiento cualquiera.', '<circle cx="39" cy="32" r="15" fill="§"/><path d="M8 24h12M5 32h12M8 40h12" stroke="§" stroke-width="5.5"/>'),
 ('H1', 'Mesa con estela', 'Tres sillas se quedan; la cuarta se vuelve estela de velocidad.',
  'Se lee «mesa» y «rápido» a la vez: une A y D sin perder claridad.', 'A 16 px la estela se vuelve una sola raya: hay que comprobarla en tamaño real.',
  '<g transform="translate(6 0)">' + MESA + CAP_T + CAP_B + CAP_R + '</g><path d="M6 26h8M3 32h11M6 38h8" stroke="§" stroke-width="4.5"/>'),
 ('H2', 'Sillas que se quedan atrás', 'La mesa avanza y sus sillas de la izquierda quedan como rastro, cada vez más cortas.',
  'La más propia: la estela está hecha con las mismas piezas que la mesa (sillas).', 'Más abstracta: sin explicación se lee movimiento antes que mesa.',
  '<circle cx="40" cy="32" r="14" fill="§"/><rect x="32" y="7" width="16" height="7" rx="3.5" fill="§"/><rect x="32" y="50" width="16" height="7" rx="3.5" fill="§"/><rect x="14" y="25" width="12" height="6" rx="3" fill="§"/><rect x="6" y="34" width="20" height="6" rx="3" fill="§" opacity=".55"/>'),
 ('H3', 'La mesa gira', 'Mesa y sillas giradas, con un arco que sugiere movimiento circular: la ronda del mesero.',
  'Movimiento sin las líneas de velocidad típicas de apps de entrega.', 'El arco agrega una pieza más; a 16 px puede perderse.',
  '<g transform="rotate(20 32 32)">' + MESA + CAP_T + CAP_B + CAP_L + CAP_R + '</g><path d="M50 12a28 28 0 0 1 9 14" stroke="§" stroke-width="4.5"/>'),
]
def card(k, t, i, a, r, b):
    big = s(b); inv = s(b, '#ffffff')
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{t}</h2></header>'
            f'<div class="lk"><span class="sym">{big}</span><span class="nm">Mesanda</span></div><span class="by">de <b>CLNDA</b> Studio</span>'
            f'<div class="mini"><span class="t">{big}</span><span class="t s24">{big}</span><span class="t s16">{big}</span><span class="t ap">{inv}</span></div>'
            f'<p class="id">{i}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.55 'Manrope',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto}}h1{{font:800 28px/1.2 'Manrope';margin:0 0 6px}}.lead{{color:#4b4e5a;max-width:860px;margin:0 0 22px}}
.g{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.c{{background:#fff;border:1px solid #e3e3dc;border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:10px;min-width:0}}
.c header{{display:flex;gap:10px;align-items:center}}.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font:700 18px 'Manrope';margin:0}}
.lk{{display:flex;align-items:center;gap:12px;margin-top:6px;min-width:0}}.sym svg{{width:56px;height:56px;display:block}}.nm{{font:800 34px/1 'Manrope';letter-spacing:-.025em}}
.by{{font-size:13px;color:#5d606b;margin:-4px 0 0 68px}}.by b{{color:{INK}}}
.mini{{display:flex;gap:8px;align-items:center}}.t{{width:40px;height:40px;border-radius:10px;border:1px solid #ecece6;display:grid;place-items:center}}.t svg{{width:32px;height:32px}}.t.s24 svg{{width:24px;height:24px}}.t.s16 svg{{width:16px;height:16px}}
.t.ap{{background:{INK};border-color:{INK}}}.t.ap svg{{width:24px;height:24px}}
.id{{margin:0;font-weight:600}}.pr{{margin:0;font-size:14px;color:#4b4e5a}}.pr b{{color:{INK}}}
@media (max-width:1000px){{.g{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}@media (max-width:700px){{.g{{grid-template-columns:1fr}}.nm{{font-size:32px}}.by{{margin-left:0}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Símbolo de Mesanda · ronda 2</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>Mesanda · ronda 2 de símbolo</h1>'
        '<p class="lead">Te gustaron A (la mesa en el plano) y D (la mesa que anda). Aquí están las dos tal cual y tres híbridos que intentan decir «mesa» y «rápido» en un solo símbolo. Sigue en tinta: el color va en la ronda siguiente. Cada una en grande, a 32, 24 y 16 px, y como app icon. Tipografía provisional.</p>'
        f'<div class="g">{"".join(card(*x) for x in S)}</div></main></body></html>')
open(os.path.join(H, 'simbolos.html'), 'w').write(html); print('ok')
