# Mesanda · ronda 6 de color. Usuario: blanco + negro + UN acento vivo; psicología según el tipo de producto (comandero: rapidez,
# atención, servicio), nada «mexicano», nada opaco, nada naranja. Uso: python3 gen.py → color.html
import os
H = os.path.dirname(os.path.abspath(__file__))
NEG, BLA, GRIS = '#0b0b0c', '#ffffff', '#f4f4f5'
def lum(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def cr(a, b): x, y = sorted((lum(a), lum(b))); return (y + .05) / (x + .05)
MESA = '<circle cx="38" cy="32" r="14" fill="§"/><rect x="30" y="7" width="16" height="7" rx="3.5" fill="§"/><rect x="30" y="50" width="16" height="7" rx="3.5" fill="§"/><rect x="56" y="24" width="7" height="16" rx="3.5" fill="§"/>'
EST = '<path d="M6 26h8M3 32h11M6 38h8" stroke="#" stroke-width="4.5"/>'
def sim(m, e): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round">{MESA.replace("§", m)}{EST.replace("#", e)}</svg>'
A = [  # clave, nombre, acento, psicología para un comandero, evidencia, riesgo
 ('1', 'Amarillo señal', '#facc15',
  'Rapidez y atención: es el color que el ojo detecta primero; negro + amarillo es el código de la señalización y de lo urgente-pero-no-peligroso. En un comandero dice «esto necesita al mesero».',
  'Sólida para visibilidad y atención (luminosidad alta, uso en señalización).', 'Nunca como texto sobre blanco: siempre como fondo con texto negro.'),
 ('2', 'Rojo tomate', '#ef2b2d',
  'Apetito, energía y urgencia: el color más usado por marcas de comida y servicio rápido.',
  'Asociación aprendida fuerte con comida rápida; el efecto «abre el apetito» como fisiología tiene evidencia débil.', 'En la interfaz el rojo también significa error y cancelar: el acento y los errores competirían.'),
 ('3', 'Verde vivo', '#22c55e',
  'Fluidez y «listo»: verde es seguir, completado, todo bien. Dice que el servicio avanza sin trabas.',
  'Sólida como convención de interfaz (verde = correcto, adelante).', 'En el plano, verde suele significar «mesa libre»: hay que decidir si la marca y ese estado comparten color a propósito.'),
 ('4', 'Azul eléctrico', '#2f5bff',
  'Eficiencia y confianza: el color de la tecnología y de lo que funciona.',
  'Asociación sólida con tecnología y confianza; que «quita el apetito» tiene evidencia débil.', 'El más visto en software: menos distintivo frente a otros sistemas.'),
]
def plano(ac, tx):
    def m(n, st, label):
        return f'<div class="m" style="{st}"><b>{n}</b><span>{label}</span></div>'
    return ('<div class="plano">' + m('1', f'background:{BLA};color:{NEG};border:2px dashed #c4c4c8', 'Libre') + m('2', f'background:{NEG};color:{BLA}', 'Ocupada · 3') +
            m('3', f'background:{ac};color:{tx}', 'Cuenta pedida') + m('4', f'background:{NEG};color:{BLA}', 'Ocupada · 2') + '</div>')
def card(k, n, ac, ps, ev, rg):
    tx = NEG if cr(ac, NEG) >= cr(ac, BLA) else BLA
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{n}</h2><span class="sw" style="background:{ac}"></span><code>{ac}</code></header>'
            f'<div class="row"><div class="cell" style="background:{BLA}">{sim(NEG, ac)}<span class="nm" style="color:{NEG}">Mesanda</span></div>'
            f'<div class="cell" style="background:{NEG}">{sim(BLA, ac)}<span class="nm" style="color:{BLA}">Mesanda</span></div></div>'
            f'<div class="mini"><span class="ap" style="background:{NEG}">{sim(BLA, ac)}</span><span class="ap" style="background:{ac}">{sim(tx, tx)}</span>'
            f'<span class="btn" style="background:{ac};color:{tx}">Enviar a cocina</span><span class="ct">{"negro" if tx == NEG else "blanco"} sobre acento {cr(ac, tx):.1f}:1 · acento sobre negro {cr(ac, NEG):.1f}:1 · sobre blanco {cr(ac, BLA):.1f}:1</span></div>'
            f'{plano(ac, tx)}<p class="pr"><b>Psicología:</b> {ps}</p><p class="pr"><b>Evidencia:</b> {ev}</p><p class="pr"><b>Riesgo:</b> {rg}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{GRIS};color:{NEG};font:400 15px/1.55 'Manrope',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto}}h1{{font:800 28px/1.2 'Manrope';margin:0 0 6px}}.lead{{color:#52525b;max-width:900px;margin:0 0 22px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.c{{background:#fff;border:1px solid #e4e4e7;border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:12px;min-width:0}}
.c header{{display:flex;gap:10px;align-items:center}}.k{{width:28px;height:28px;border-radius:8px;background:{NEG};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font:700 18px 'Manrope';margin:0}}
.sw{{width:16px;height:16px;border-radius:4px}}header code{{font-size:12px;color:#52525b}}
.row{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}.cell{{border:1px solid #e4e4e7;border-radius:12px;padding:14px;display:flex;align-items:center;gap:8px;min-width:0}}
.cell svg{{width:38px;height:38px;flex:none}}.nm{{font:800 24px/1 'Manrope';letter-spacing:-.025em;white-space:nowrap}}
.mini{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}.ap{{width:52px;height:52px;border-radius:13px;display:grid;place-items:center}}.ap svg{{width:34px;height:34px}}
.btn{{border-radius:10px;padding:10px 16px;font-weight:700;font-size:14px}}.ct{{font:600 12px ui-monospace,monospace;color:#52525b}}
.plano{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;background:{GRIS};border-radius:12px;padding:12px}}
.m{{border-radius:12px;padding:10px;min-height:66px;display:flex;flex-direction:column;justify-content:space-between;font-size:12.5px;font-weight:600}}.m b{{font-size:18px}}
.pr{{margin:0;font-size:14px;color:#52525b}}.pr b{{color:{NEG}}}
@media (max-width:980px){{.g{{grid-template-columns:1fr}}}}@media (max-width:520px){{.row{{grid-template-columns:1fr}}.plano{{grid-template-columns:1fr 1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Color de Mesanda · acento vivo</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>Mesanda · blanco, negro y un acento vivo</h1>'
        '<p class="lead">Blanco y negro hacen el trabajo; un solo acento vivo marca lo importante: el botón principal y la mesa que necesita al mesero. Cuatro acentos elegidos por lo que hace el producto (rapidez, atención, servicio), sin naranja. Cada uno con su evidencia y su riesgo.</p>'
        f'<div class="g">{"".join(card(*a) for a in A)}</div></main></body></html>')
open(os.path.join(H, 'color.html'), 'w').write(html); print('ok')
