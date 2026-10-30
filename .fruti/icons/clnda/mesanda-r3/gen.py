# Mesanda · ronda 3: color. Símbolo elegido: H1 «mesa con estela» (tres sillas + estela de velocidad).
# Restricción: nada de naranja (la app vieja que se quiere reemplazar es naranja). Uso: python3 gen.py → color.html
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#14161f', '#f6f6f3'
def lum(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def cr(a, b): x, y = sorted((lum(a), lum(b))); return (y + .05) / (x + .05)
MESA = '<circle cx="38" cy="32" r="14" fill="§"/><rect x="30" y="7" width="16" height="7" rx="3.5" fill="§"/><rect x="30" y="50" width="16" height="7" rx="3.5" fill="§"/><rect x="56" y="24" width="7" height="16" rx="3.5" fill="§"/>'
H1 = MESA + '<path d="M6 26h8M3 32h11M6 38h8" stroke="§" stroke-width="4.5"/>'
H1_16 = MESA + '<path d="M5 26.5h10M5 37.5h10" stroke="§" stroke-width="6"/>'  # 16–24 px: dos líneas gruesas
def s(body, c): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round">{body.replace("§", c)}</svg>'
P = [  # clave, nombre, idea, color, acento, fondo del app icon, color del símbolo en el icon, a favor, riesgo
 ('1', 'Albahaca', 'Verde de hierba fresca: cocina, frescura, «adelante».', '#166534', '#d9f99d', '#166534', '#d9f99d',
  'Se asocia a comida fresca y a «listo».', 'En el plano, verde suele significar «mesa libre»: la marca competiría con ese estado.'),
 ('2', 'Vino', 'Tinto profundo con rosa claro: sobremesa, servicio de mesa.', '#7c2d42', '#fbcfe8', '#7c2d42', '#fbcfe8',
  'Cálido y con carácter; lejos del naranja y del verde de los estados.', 'Puede leerse elegante o de bar; cerca del rojo de error si se usa en botones.'),
 ('3', 'Mostaza', 'Tinta casi negra con mostaza: contraste alto, carta de bistró.', '#1c1917', '#eab308', '#1c1917', '#eab308',
  'La más llamativa y la más legible en pantallas con brillo bajo; el amarillo atrae la mirada sin ser alarma.', 'El amarillo vive cerca del naranja: usar siempre el tono mostaza, nunca uno anaranjado.'),
 ('4', 'Petróleo', 'Azul petróleo con crema: sereno y profesional.', '#0f4c5c', '#fde68a', '#0f4c5c', '#fde68a',
  'Serio y confiable para un sistema de caja; no compite con estados de mesa.', 'La más fría: menos apetito, más oficina.'),
]
def card(k, n, i, c, ac, ib, isc, a, r):
    rows = (f'<p class="ct">Contraste: color sobre blanco {cr(c, "#ffffff"):.1f}:1 · acento sobre su fondo {cr(ac, ib):.1f}:1</p>')
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{n}</h2><span class="sw"><i style="background:{c}"></i>{c}</span><span class="sw"><i style="background:{ac}"></i>{ac}</span></header><p class="id">{i}</p>'
            f'<div class="row"><div class="cell"><span class="sym">{s(H1, c)}</span><span class="nm" style="color:{c if c != "#1c1917" else INK}">Mesanda</span></div>'
            f'<div class="cell dk" style="background:{ib}"><span class="sym">{s(H1, isc)}</span><span class="nm" style="color:#fff">Mesanda</span></div></div>'
            f'<div class="mini"><span class="ap" style="background:{ib}">{s(H1, isc)}</span><span class="t">{s(H1_16, c)}</span><span class="t s16">{s(H1_16, c)}</span>'
            f'<span class="btn" style="background:{c};color:#fff">Enviar a cocina</span></div>{rows}'
            f'<p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.55 'Manrope',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto}}h1{{font:800 28px/1.2 'Manrope';margin:0 0 6px}}.lead{{color:#4b4e5a;max-width:880px;margin:0 0 22px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.c{{background:#fff;border:1px solid #e3e3dc;border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:10px;min-width:0}}
.c header{{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center}}.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font:700 18px 'Manrope';margin:0}}
.sw{{display:inline-flex;gap:6px;align-items:center;font:600 12px ui-monospace,monospace;color:#4b4e5a}}.sw i{{width:14px;height:14px;border-radius:4px;border:1px solid rgba(0,0,0,.08)}}
.id{{margin:0;color:#4b4e5a}}.row{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.cell{{border:1px solid #ecece6;border-radius:12px;padding:14px;display:flex;align-items:center;gap:8px;min-width:0}}.cell.dk{{border:0}}
.sym svg{{width:40px;height:40px;display:block}}.nm{{font:800 26px/1 'Manrope';letter-spacing:-.025em;overflow-wrap:anywhere}}
.mini{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}.ap{{width:52px;height:52px;border-radius:13px;display:grid;place-items:center}}.ap svg{{width:34px;height:34px}}
.t{{width:40px;height:40px;border-radius:10px;border:1px solid #ecece6;display:grid;place-items:center}}.t svg{{width:24px;height:24px}}.t.s16 svg{{width:16px;height:16px}}
.btn{{border-radius:10px;padding:10px 16px;font-weight:700;font-size:14px}}
.ct{{margin:0;font:600 12px ui-monospace,monospace;color:#5d606b}}.pr{{margin:0;font-size:14px;color:#4b4e5a}}.pr b{{color:{INK}}}
@media (max-width:900px){{.g{{grid-template-columns:1fr}}}}@media (max-width:480px){{.row{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Color de Mesanda</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>Mesanda · ronda 3 de color</h1>'
        '<p class="lead">Símbolo elegido: la mesa con estela. Cuatro paletas, ninguna naranja. Cada una en claro, en su fondo de marca, como app icon, a 24 y 16 px (versión pequeña con dos líneas más gruesas) y en el botón principal. Contrastes calculados.</p>'
        f'<div class="g">{"".join(card(*p) for p in P)}</div></main></body></html>')
open(os.path.join(H, 'color.html'), 'w').write(html); print('ok')
