# Fruti Squad · ronda 4: otra marca constante (usuario: «no me gusta, dame otra propuesta de símbolos»). Mismo método (sello + rasgo + color).
# La marca constante se pinta en el color de la marca del sello; lo que en la marca es negro (#000) se cala con el color del sello.
import os, re
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, 'base.py')).read())
def sello2(k, color, mc, uid, fm):
    cut, draw = R[k]
    back = ''
    if k == 'mora':
        back = (f'<mask id="b{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/>'
                f'<rect x="5" y="5" width="54" height="54" rx="16" fill="#000"/></mask><rect x="15" y="1" width="46" height="46" rx="13" fill="{color}" mask="url(#b{uid})"/>')
    tm = f'<mask id="t{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/><g fill="#000">{cut}</g></mask>'
    d = draw.replace('§', color).replace('¤', mc)
    mk = fm(mc).replace('stroke="#000"', f'stroke="{color}"').replace('fill="#000"', f'fill="{color}"')
    return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{back}{tm}<g mask="url(#t{uid})" fill="{color}">{TILE}</g><g fill="{color}">{d}</g>{mk}</svg>'
u = [0]
def S2(k, c, mc, fm):
    u[0] += 1; return sello2(k, c, mc, u[0], fm)
def card(key):
    t, i, a, r, fm = MARCAS[key]
    fila = ''.join(f'<figure class="p">{S2(k, c, mc, fm)}<figcaption><b>{n}</b></figcaption></figure>' for k, n, rr, v, c, mc in P)
    peq = ''.join(f'<span class="pq">{S2(k, c, mc, fm)}</span>' for k, n, rr, v, c, mc in P)
    dk = ''.join(f'<span class="ti">{S2(k, c if k != "squad" else "#f5f5f2", mc if k != "squad" else INK, fm)}</span>' for k, n, rr, v, c, mc in P)
    k0, n0, r0, v0, c0, m0 = P[3]
    lock = f'<div class="lk">{S2(k0, c0, m0, fm)}<span><b>{n0}</b><i>{r0}</i><small>de Fruti Squad</small></span></div>'
    return (f'<section class="c"><header><span class="k">{key}</span><h2>{t}</h2></header><p class="id">{i}</p><div class="fila">{fila}</div>'
            f'<div class="row"><span class="lb">16 px</span>{peq}<span class="lb">Oscuro</span><span class="dkb">{dk}</span></div>{lock}'
            f'<p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.c{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:22px;display:grid;gap:12px;min-width:0;align-content:start}}.c header{{display:flex;gap:10px;align-items:center}}
.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font-size:18px;margin:0}}.id{{margin:0;font-weight:600}}
.fila{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:6px}}.p{{margin:0;display:grid;justify-items:center;gap:4px;text-align:center}}.p svg{{width:100%;max-width:72px;height:auto}}.p b{{font-size:12px}}
.row{{display:flex;flex-wrap:wrap;gap:8px;align-items:center}}.lb{{font-size:12px;font-weight:700;color:#6b6b66}}.pq{{display:inline-grid;place-items:center;width:28px;height:28px;border:1px solid #ececE6;border-radius:7px}}.pq svg{{width:16px;height:16px}}
.dkb{{display:inline-flex;gap:6px;background:{INK};border-radius:10px;padding:6px}}.ti svg{{width:28px;height:28px}}
.lk{{display:flex;align-items:center;gap:14px;border:1px solid #ececE6;border-radius:14px;padding:12px 16px}}.lk svg{{width:52px;height:52px;flex:none}}.lk span{{display:grid;line-height:1.15}}.lk b{{font-size:22px}}.lk i{{font-style:normal;color:#3f3f3c}}.lk small{{font-size:12px;color:#6b6b66}}
.pr{{margin:0;font-size:14px;color:#4b4b47}}.pr b{{color:{INK}}}
@media (max-width:980px){{.g{{grid-template-columns:1fr}}}}@media (max-width:480px){{.fila{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · símbolos ronda 4</title>'
        f'<style>{css}</style></head><body><main><h1>Fruti Squad · otra marca para el centro (ronda 4)</h1>'
        '<p class="lead">Cambia solo la marca blanca del centro: es la pieza constante que hace familia. Lo demás (sello, rasgo en el borde y color de cada producto) se queda igual que en la ronda 3 para comparar solo el símbolo. Cada propuesta aplicada a los seis, a 16 px, sobre oscuro y como producto.</p>'
        f'<div class="g">{"".join(card(k) for k in "ABCD")}</div></main></body></html>')
open(os.path.join(H, 'simbolos.html'), 'w').write(html); print('ok')
