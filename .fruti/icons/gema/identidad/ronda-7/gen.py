# GEMA · ronda 7: color de marca para R1 (congelado por el usuario el 2026-11-17).
# Regla heredada de SAM: el acento es RELLENO (mismo valor en claro y oscuro), con texto de tinta encima y contorno de tinta en claro.
def lum(h):
    h = h.lstrip('#'); r, g, b = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    f = lambda c: c/12.92 if c <= .04045 else ((c+.055)/1.055)**2.4
    return .2126*f(r) + .7152*f(g) + .0722*f(b)
def cr(a, b): A, B = sorted([lum(a), lum(b)], reverse=True); return (A+.05)/(B+.05)
OSC, SUP, CLA, BL, SEC = '#0a0a0b', '#16161a', '#f2f2ee', '#ffffff', '#a3a3a8'
COL = [
 ('Celeste', '#38bdf8', 'Agua, limpieza y precisión de laboratorio. Pariente del celeste secundario del laboratorio Nisa Nabani (#00B4D8). Se distingue bien del lima de SAM.', 'El azul claro es común en software de salud y ciencia; lo propio lo pone el pico.'),
 ('Ámbar', '#f5b52e', 'Industrial y cálido, como la luz de un instrumento encendido. Muy legible y distinto de todo lo que hemos hecho.', 'En un laboratorio el ámbar se asocia a «precaución»: las alertas tendrían que ir en otro tono.'),
 ('Coral', '#ff8466', 'Energía y cercanía; resalta mucho el pico del resultado. Rompe con el azul habitual de los laboratorios.', 'Cerca del rojo de «error»: el estado de error tendría que ser un rojo más oscuro y siempre con palabra.'),
]
r1 = open('../ronda-5/r1-pantalla.svg').read()
def at(s, z): return s.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
def ui(fondo, sup, tinta, sec, ac, claro, linea):
    borde = f';box-shadow:inset 0 0 0 {2 if claro else 0}px {OSC}'
    chip = f'background:{ac};color:{OSC}' + (f';box-shadow:inset 0 0 0 1.5px {OSC}' if claro else '')
    return (f'<div class="ui" style="background:{fondo};color:{tinta};--g-color-brand:{ac};border-color:{linea}">'
            f'<div class="bar" style="border-color:{linea}">{at(r1, 24)}<b>GEMA</b><span class="sp"></span><span style="color:{sec};font-size:12px">Recepción · Oaxaca</span></div>'
            f'<div class="m" style="background:{sup};border-color:{linea}"><span class="fol" style="color:{sec}">M-2026-1184</span><b>Agua residual · planta norte</b>'
            f'<span class="pie"><span class="chip" style="{chip}">En análisis</span><span style="color:{sec}">DBO₅, SST, pH</span></span></div>'
            f'<div class="acts"><button style="background:{ac};color:{OSC}{borde}">Registrar muestra</button><a style="color:{tinta}">Ver resultados</a><span class="foco" style="outline-color:{tinta}">Foco</span></div></div>')
secs = ''
for n, ac, idea, riesgo in COL:
    m = (f'<ul class="mt"><li>Texto de tinta sobre {n.lower()}: <b>{cr(OSC, ac):.1f}:1</b></li><li>{n} sobre fondo oscuro: <b>{cr(ac, OSC):.1f}:1</b></li>'
         f'<li>{n} sobre fondo claro: <b>{cr(ac, CLA):.1f}:1</b>, por eso en claro lleva contorno de tinta</li></ul>')
    lk = ''.join(f'<div class="lock" style="background:{f};color:{c};--g-color-brand:{ac}">{at(r1, 56)}<span><span class="wm">GEMA</span><span class="desc" style="color:{dc}">Gestión de Muestras y Análisis</span></span></div>' for f, c, dc in ((OSC, CLA, SEC), (CLA, OSC, '#3a3a40')))
    apps = (f'<div class="app" style="background:{OSC};color:{CLA};--g-color-brand:{ac}">{at(r1, 58)}</div>'
            f'<div class="app" style="background:{ac};color:{OSC};--g-color-brand:{CLA}">{at(r1, 58)}</div>'
            f'<div class="app" style="background:{CLA};color:{OSC};--g-color-brand:{ac}">{at(r1, 58)}</div>')
    secs += (f'<section><header><h2>{n} <small><code>{ac}</code></small></h2><p>{idea}</p><p class="fn">Riesgo: {riesgo}</p></header>'
             f'<div class="row">{lk}{apps}</div><div class="row al">{ui(OSC, SUP, CLA, SEC, ac, False, "#2a2a30")}{ui(CLA, BL, OSC, "#55555c", ac, True, "#d6d6d0")}{m}</div></section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GEMA · ronda 7</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 'Onest',system-ui,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:{SEC};max-width:80ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px}} h2 small{{font-size:14px;font-weight:400;color:{SEC}}} header p{{margin:4px 0 0;max-width:86ch}} .fn{{color:{SEC};font-size:13px}}
code{{font-family:'JetBrains Mono',monospace;font-size:13px;color:#e6e6e1}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:16px}} .row.al{{align-items:flex-start}}
.lock{{display:flex;align-items:center;gap:12px;padding:14px 24px 14px 14px;border:1px solid #26262b;border-radius:2px}}
.wm{{display:block;font-weight:700;font-size:38px;line-height:1}} .desc{{display:block;font-size:13px;font-weight:500;margin-top:4px}}
.app{{width:84px;height:84px;border-radius:19px;display:flex;align-items:center;justify-content:center;border:1px solid #26262b}}
.ui{{width:340px;border:1px solid;border-radius:10px;overflow:hidden;display:grid;gap:12px;padding-bottom:14px}}
.bar{{display:flex;gap:8px;align-items:center;padding:10px 13px;border-bottom:1px solid}} .bar b{{font-size:17px}} .sp{{flex:1}}
.m{{margin:0 13px;border:1px solid;border-radius:6px;padding:10px 12px;display:grid;gap:3px}} .m b{{font-weight:600}}
.fol{{font:500 12px 'JetBrains Mono',monospace}} .pie{{display:flex;gap:8px;align-items:center;font-size:13px;margin-top:3px}} .chip{{font-size:12px;font-weight:600;padding:2px 9px;border-radius:999px}}
.acts{{display:flex;gap:12px;align-items:center;flex-wrap:wrap;padding:0 13px}} .acts button{{font:600 14px 'Onest';border:0;border-radius:6px;padding:0 16px;min-height:44px}}
.acts a{{font-weight:600;font-size:14px;text-decoration:underline;text-underline-offset:3px}} .foco{{font-size:13px;padding:6px 10px;border-radius:4px;outline:3px solid;outline-offset:2px}}
.mt{{margin:0;padding-left:18px;font-size:13px;color:#cfcfca;max-width:280px}}
</style></head><body><main><h1>GEMA · identidad, ronda 7 · color</h1>
<p class="sub">Símbolo R1 congelado. Tres colores de marca con la regla de SAM desde el inicio: el color es relleno (mismo valor en claro y oscuro), lleva texto de tinta encima y contorno de tinta en claro; texto, enlaces y foco van en tinta. Quedan fuera el lima (SAM), el carmín (Grana) y el teal (MedicalManik). Onest provisional. Datos ficticios.</p>
{secs}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
