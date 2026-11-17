# GEMA · ronda 8: color azul navy (usuario, 2026-11-17: «algo más como un azul navy, como el azul de Nisa Nabani, o un degradado»).
# Hecho: el navy del laboratorio (#052A76) mide 1.5:1 sobre fondo negro; en modo oscuro no se ve. Cada opción resuelve el oscuro de una forma.
import re
def lum(h):
    h = h.lstrip('#'); r, g, b = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    f = lambda c: c/12.92 if c <= .04045 else ((c+.055)/1.055)**2.4
    return .2126*f(r) + .7152*f(g) + .0722*f(b)
def cr(a, b): A, B = sorted([lum(a), lum(b)], reverse=True); return (A+.05)/(B+.05)
NAVY, AZUL, CIAN, CLA, BL, NOCHE_NAVY, CELESTE_OSC = '#052A76', '#3D67AE', '#00B4D8', '#f2f2ee', '#ffffff', '#071633', '#8fb3ff'
r1 = open('../ronda-5/r1-pantalla.svg').read()
inner = r1[r1.index('>', r1.index('<svg')) + 1: r1.rindex('</svg>')]
def simb(z, tinta, pico, grad=None, gid='g'):
    body = inner.replace('currentColor', tinta)
    defs = ''
    if grad:
        defs = f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{grad[1]}"/><stop offset="1" stop-color="{grad[0]}"/></linearGradient></defs>'
        pico = f'url(#{gid})'
    body = body.replace('var(--g-color-brand,#38bdf8)', pico)
    return f'<svg viewBox="0 0 48 48" width="{z}" height="{z}" aria-hidden="true">{defs}{body}</svg>'
n = [0]
def gid(): n[0] += 1; return f'gr{n[0]}'
OP = [
 dict(t='N1 · Navy del laboratorio', idea='El azul real de Nisa Nabani como color de marca. En claro: botones navy con texto blanco. En oscuro, el navy no se ve sobre negro, así que el fondo oscuro se vuelve «noche navy» y el color de marca pasa a un azul claro con texto navy.',
      riesgo='El color cambia de valor entre claro y oscuro (como pasó con el oliva en SAM), aunque aquí es el mismo azul, más claro.',
      L=dict(fondo=CLA, sup=BL, tinta=NAVY, sec='#4a5674', btn=NAVY, btxt=BL, pico=NAVY, grad=None, icon=NAVY, itinta=BL, ipico=CELESTE_OSC),
      D=dict(fondo=NOCHE_NAVY, sup='#0d2150', tinta=CLA, sec='#a9b6d6', btn=CELESTE_OSC, btxt=NOCHE_NAVY, pico=CELESTE_OSC, grad=None)),
 dict(t='N2 · Degradado navy', idea='Un degradado del navy del laboratorio al azul medio (#052A76 → #3D67AE) en las superficies de marca: el pico del símbolo, el icono de la app y el panel de inicio de sesión. Los botones van en un solo tono (navy en claro, azul medio en oscuro), porque un degradado en un botón se lee como adorno.',
      riesgo='El degradado solo vive en la marca; en la interfaz el color es plano. En oscuro, el azul medio mide 3.5:1 sobre negro: suficiente para un botón, no para texto.',
      L=dict(fondo=CLA, sup=BL, tinta='#0a0a0b', sec='#55555c', btn=NAVY, btxt=BL, pico=None, grad=(NAVY, AZUL), icon=None, itinta=BL, ipico=CELESTE_OSC),
      D=dict(fondo='#0a0a0b', sup='#16161a', tinta=CLA, sec='#a3a3a8', btn=AZUL, btxt=BL, pico=None, grad=(AZUL, '#7aa2f0'))),
 dict(t='N3 · Navy + celeste', idea='Navy como color de marca (icono, botones, títulos) y el pico del resultado en el celeste del propio laboratorio (#00B4D8). Dos colores, los dos de la paleta de Nisa Nabani: el navy da la base y el celeste marca el resultado.',
      riesgo='Dos colores de marca piden más reglas: el celeste solo para el resultado y el estado activo, nunca para botones.',
      L=dict(fondo=CLA, sup=BL, tinta='#0a0a0b', sec='#55555c', btn=NAVY, btxt=BL, pico=CIAN, grad=None, icon=NAVY, itinta=BL, ipico=CIAN),
      D=dict(fondo=NOCHE_NAVY, sup='#0d2150', tinta=CLA, sec='#a9b6d6', btn=CIAN, btxt=NOCHE_NAVY, pico=CIAN, grad=None)),
]
def ui(m, chip_bg, chip_txt):
    s = simb(24, m['tinta'], m['pico'], m['grad'], gid())
    return (f'<div class="ui" style="background:{m["fondo"]};color:{m["tinta"]}"><div class="bar">{s}<b>GEMA</b><span class="sp"></span><span style="color:{m["sec"]};font-size:12px">Recepción · Oaxaca</span></div>'
            f'<div class="m" style="background:{m["sup"]}"><span class="fol" style="color:{m["sec"]}">M-2026-1184</span><b>Agua residual · planta norte</b>'
            f'<span class="pie"><span class="chip" style="background:{chip_bg};color:{chip_txt}">En análisis</span><span style="color:{m["sec"]}">DBO₅, SST, pH</span></span></div>'
            f'<div class="acts"><button style="background:{m["btn"]};color:{m["btxt"]}">Registrar muestra</button><a style="color:{m["tinta"]}">Ver resultados</a></div></div>')
secs = ''
for o in OP:
    L, D = o['L'], o['D']
    lockL = f'<div class="lock" style="background:{CLA};color:{L["tinta"]}">{simb(56, L["tinta"], L["pico"], L["grad"], gid())}<span><span class="wm">GEMA</span><span class="desc" style="color:{L["sec"]}">Gestión de Muestras y Análisis</span></span></div>'
    lockD = f'<div class="lock" style="background:{D["fondo"]};color:{D["tinta"]}">{simb(56, D["tinta"], D["pico"], D["grad"], gid())}<span><span class="wm">GEMA</span><span class="desc" style="color:{D["sec"]}">Gestión de Muestras y Análisis</span></span></div>'
    if L['grad']:
        ibg = f'linear-gradient(160deg,{AZUL},{NAVY})'; ic = simb(58, BL, CELESTE_OSC)
    else:
        ibg = L['icon']; ic = simb(58, L['itinta'], L['ipico'])
    icon = f'<div class="app" style="background:{ibg}">{ic}</div><div class="app" style="background:{BL}">{simb(58, L["tinta"] if L["tinta"]!="#0a0a0b" else NAVY, L["pico"], L["grad"], gid())}</div>'
    chipL = (CIAN, NAVY) if o['t'].startswith('N3') else ('#dbe5f7', NAVY)
    chipD = (CIAN, NOCHE_NAVY) if o['t'].startswith('N3') else (D['btn'], D['btxt'])
    pares = []
    pares.append(f'Texto en botón (claro): <b>{cr(L["btxt"], L["btn"]):.1f}:1</b>')
    pares.append(f'Botón sobre fondo claro: <b>{cr(L["btn"], L["fondo"]):.1f}:1</b>')
    pares.append(f'Texto en botón (oscuro): <b>{cr(D["btxt"], D["btn"]):.1f}:1</b>')
    pares.append(f'Botón sobre fondo oscuro: <b>{cr(D["btn"], D["fondo"]):.1f}:1</b>')
    secs += (f'<section><h2>{o["t"]}</h2><p>{o["idea"]}</p><p class="fn">Riesgo: {o["riesgo"]}</p>'
             f'<div class="row">{lockL}{lockD}{icon}</div><div class="row al">{ui(L, *chipL)}{ui(D, *chipD)}<ul class="mt">{"".join(f"<li>{p}</li>" for p in pares)}</ul></div></section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GEMA · ronda 8</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:#0a0a0b;color:{CLA};font:15px/1.55 'Onest',system-ui,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:#a3a3a8;max-width:82ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px}} section>p{{margin:4px 0 0;max-width:88ch}} .fn{{color:#a3a3a8;font-size:13px}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:16px}} .row.al{{align-items:flex-start}}
.lock{{display:flex;align-items:center;gap:12px;padding:14px 24px 14px 14px;border:1px solid #26262b;border-radius:2px}}
.wm{{display:block;font-weight:700;font-size:38px;line-height:1}} .desc{{display:block;font-size:13px;font-weight:500;margin-top:4px}}
.app{{width:84px;height:84px;border-radius:19px;display:flex;align-items:center;justify-content:center;border:1px solid #26262b}}
.ui{{width:340px;border:1px solid #2a2a30;border-radius:10px;overflow:hidden;display:grid;gap:12px;padding-bottom:14px}}
.bar{{display:flex;gap:8px;align-items:center;padding:10px 13px;border-bottom:1px solid rgba(127,127,140,.3)}} .bar b{{font-size:17px}} .sp{{flex:1}}
.m{{margin:0 13px;border:1px solid rgba(127,127,140,.3);border-radius:6px;padding:10px 12px;display:grid;gap:3px}} .m b{{font-weight:600}}
.fol{{font:500 12px 'JetBrains Mono',monospace}} .pie{{display:flex;gap:8px;align-items:center;font-size:13px;margin-top:3px}} .chip{{font-size:12px;font-weight:600;padding:2px 9px;border-radius:999px}}
.acts{{display:flex;gap:12px;align-items:center;flex-wrap:wrap;padding:0 13px}} .acts button{{font:600 14px 'Onest';border:0;border-radius:6px;padding:0 16px;min-height:44px}}
.acts a{{font-weight:600;font-size:14px;text-decoration:underline;text-underline-offset:3px}}
.mt{{margin:0;padding-left:18px;font-size:13px;color:#cfcfca;max-width:260px}}
</style></head><body><main><h1>GEMA · identidad, ronda 8 · azul navy</h1>
<p class="sub">El navy de Nisa Nabani (#052A76) en tres formas. Hecho que manda: sobre fondo negro el navy mide 1.5:1 y no se ve, así que cada opción resuelve el modo oscuro de forma distinta. Onest provisional. Datos ficticios.</p>
{secs}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
