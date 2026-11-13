# SAM · identidad, ronda 4: color de marca para A1 + L3 (elegidos por el usuario, 2026-11-13).
# Cada color tiene valor para oscuro y para claro; en la app entra en --g-color-brand de Grana. Contrastes WCAG calculados aquí.
def lum(h):
    h = h.lstrip('#'); r, g, b = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    f = lambda c: c/12.92 if c <= .04045 else ((c+.055)/1.055)**2.4
    return .2126*f(r) + .7152*f(g) + .0722*f(b)
def cr(a, b):
    A, B = sorted([lum(a), lum(b)], reverse=True); return (A+.05)/(B+.05)
OSC, CLA, BL = '#0a0a0b', '#f2f2ee', '#ffffff'
COL = [
 ('Voltaje', 'lima eléctrica', '#c6f432', '#3f6b0a', 'La más disruptiva y la menos vista en herramientas de trabajo. En claro tiene que oscurecerse mucho (pasa a verde oliva) para leerse: son casi dos colores distintos.'),
 ('Señal', 'naranja', '#ff8a3d', '#b93a06', 'Energía y urgencia, color de aviso. Riesgo: en una herramienta de incidencias se confunde con «advertencia», así que los estados de alerta tendrían que ir en otro tono.'),
 ('Cobalto', 'azul eléctrico', '#7d93ff', '#3348d1', 'Tecnológico y estable, el que mejor pasa contraste en claro y oscuro. Riesgo: el azul es el color más usado en software; la diferencia la tendría que poner el corte.'),
]
a1 = open('../ronda-3/a1-depurada.svg').read()
def at(s, z): return s.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
def cortado(fondo, tinta, acento, tam=72):
    up = 'polygon(0 0,100% 0,100% 38%,0 62%)'; dn = 'polygon(0 62%,100% 38%,100% 100%,0 100%)'
    return (f'<span class="cw" style="font-size:{tam}px"><span style="color:{acento};clip-path:{dn}">SAM</span>'
            f'<span style="color:{tinta};clip-path:{up};transform:translate(.055em,-.04em)">SAM</span></span>')
def ui(fondo, sup, tinta, sec, ac, txtbtn):
    return (f'<div class="ui" style="background:{fondo};color:{tinta};--ac:{ac};--sup:{sup};--sec:{sec}">'
            f'<div class="bar" style="--g-color-brand:{ac}">{at(a1, 22)}<b>Mis pendientes</b></div>'
            f'<div class="tk"><span class="id">INC-2041</span><b>El reporte diario de atrasos no llegó a Discord</b><span class="st">En curso · Soporte técnico</span></div>'
            f'<div class="acts"><button style="background:{ac};color:{txtbtn}">Avanzar etapa</button><a>Adjuntar evidencia</a><span class="foco">Foco</span></div></div>')
secs = ''
for n, d, vo, vc, nota in COL:
    m = (f'<ul class="m"><li>Acento sobre fondo oscuro: <b>{cr(vo, OSC):.1f}:1</b></li><li>Texto oscuro sobre botón: <b>{cr(OSC, vo):.1f}:1</b></li>'
         f'<li>Acento sobre fondo claro: <b>{cr(vc, CLA):.1f}:1</b></li><li>Texto blanco sobre botón: <b>{cr(BL, vc):.1f}:1</b></li></ul>')
    logos = (f'<div class="lock" style="background:{OSC}">{cortado(OSC, CLA, vo)}</div>'
             f'<div class="lock" style="background:{CLA}">{cortado(CLA, OSC, vc)}</div>'
             f'<div class="app" style="background:{OSC};color:{CLA};--g-color-brand:{vo}">{at(a1, 60)}</div>'
             f'<div class="app" style="background:{vo};color:{OSC};--g-color-brand:{OSC}">{at(a1, 60)}</div>'
             f'<div class="app" style="background:{CLA};color:{OSC};--g-color-brand:{vc}">{at(a1, 60)}</div>')
    uis = ui(OSC, '#16161a', CLA, '#a3a3a8', vo, OSC) + ui(CLA, BL, OSC, '#55555c', vc, BL)
    secs += (f'<section><header><h2>{n} <small>· {d} · oscuro <code>{vo}</code> · claro <code>{vc}</code></small></h2><p>{nota}</p></header>'
             f'<div class="row">{logos}</div><div class="row">{uis}{m}</div></section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAM · ronda 4</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 "Geist",system-ui,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:#a3a3a8;max-width:74ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px}} h2 small{{font-size:14px;font-weight:400;color:#a3a3a8}} header p{{margin:4px 0 0;max-width:84ch}}
code{{font-family:"JetBrains Mono",monospace;font-size:13px;color:#e6e6e1}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:16px}}
.lock{{display:flex;align-items:center;padding:13px 26px;border:1px solid #26262b;border-radius:2px;height:96px;box-sizing:border-box}}
.cw{{display:inline-grid;font-weight:800;line-height:1;letter-spacing:-.035em}} .cw>span{{grid-area:1/1}}
.app{{width:88px;height:88px;border-radius:20px;display:flex;align-items:center;justify-content:center;border:1px solid #26262b}}
.ui{{width:340px;border:1px solid #26262b;border-radius:4px;padding:13px;display:grid;gap:13px}}
.bar{{display:flex;gap:8px;align-items:center;font-size:14px}}
.tk{{background:var(--sup);border-radius:4px;padding:13px;display:grid;gap:2px;border-left:3px solid var(--ac)}}
.tk .id{{font:500 12px "JetBrains Mono",monospace;color:var(--sec)}} .tk b{{font-weight:600;line-height:1.3}} .tk .st{{font-size:13px;color:var(--sec)}}
.acts{{display:flex;gap:13px;align-items:center;flex-wrap:wrap}}
.acts button{{font:600 14px "Geist";border:0;border-radius:4px;padding:10px 16px;min-height:44px}}
.acts a{{color:var(--ac);font-weight:600;font-size:14px;text-decoration:underline;text-underline-offset:3px}}
.foco{{font-size:13px;padding:6px 10px;border-radius:4px;outline:3px solid var(--ac);outline-offset:2px}}
.m{{margin:0;padding-left:18px;font-size:13px;color:#cfcfca}}
</style></head><body><main><h1>SAM · identidad, ronda 4 · color</h1>
<p class="sub">Símbolo A1 y logotipo L3 (elegidos). Tres colores de marca, cada uno con su valor para oscuro y para claro. En la app, el color entra en <code>--g-color-brand</code> de Grana y tiñe botón principal, enlaces y foco. Contrastes calculados (WCAG 2.2: texto 4.5:1, controles y foco 3:1). Quedan fuera el carmín (de Grana) y el teal (de MedicalManik). Tipografía del nombre provisional (Geist 800).</p>
{secs}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
