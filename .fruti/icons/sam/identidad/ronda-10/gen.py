# SAM · identidad, ronda 10: tipografía con el símbolo congelado (C2 + C4, Voltaje con regla de relleno; congelado por el usuario el 2026-11-13).
# Criterio: la misma letra en marca e interfaz; legible a 13–15 px en celular; números claros; que acompañe las esquinas redondas de las tarjetas.
OSC, SUP, CLA, BL, VO, SEC = '#0a0a0b', '#16161a', '#f2f2ee', '#ffffff', '#c6f432', '#a3a3a8'
c2 = open('../ronda-8/c2-contorno.svg').read()
def at(s, z): return s.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
F = [
 ('A · Instrument Sans', 'Instrument Sans', 'La letra de Grana: SAM y su librería de interfaz con la misma voz, sin sumar otra familia. Compacta y un poco condensada; sus terminales rectos contrastan con las esquinas redondas del símbolo.'),
 ('B · Figtree', 'Figtree', 'Geométrica y abierta, con curvas amplias que repiten las esquinas redondas de las tarjetas. La más amable y la que más se siente «simple». Ocupa algo más de ancho.'),
 ('C · Onest', 'Onest', 'Diseñada para interfaces: formas simples, letras bien diferenciadas y números claros. Punto medio entre A y B: más cálida que Instrument, más compacta que Figtree.'),
]
ACT = [('INC-2041', 'El reporte diario de atrasos no llegó a Discord', 'En curso', 'hoy, 18:00', True),
       ('TAR-0187', 'Migrar plantillas de alta de usuario al editor visual', 'Revisión', '15 nov', False),
       ('INC-2039', 'Ticket de WhatsApp sin evidencia adjunta', 'Nuevo', '18 nov', False)]
def tel(fam, fondo, sup, tinta, sec, linea):
    claro = fondo == CLA
    items = ''.join(
        f'<li style="background:{sup};border-color:{linea}"><span class="fol" style="color:{sec}">{f}</span><b>{t}</b>'
        f'<span class="pie"><span class="chip" style="{"background:"+VO+";color:"+OSC+(";box-shadow:inset 0 0 0 1.5px "+OSC if claro else "") if hot else "border:1px solid "+linea+";color:"+tinta}">{e}</span><span style="color:{sec}">Vence {v}</span></span></li>'
        for f, t, e, v, hot in ACT)
    return (f'<div class="tel" style="background:{fondo};color:{tinta};font-family:\'{fam}\';border-color:{linea}">'
            f'<div class="top">{at(c2, 28)}<b class="wm">SAM</b></div>'
            f'<h3>Mis actividades</h3><p class="res" style="color:{sec}">3 abiertas · 1 vence hoy</p><ul>{items}</ul>'
            f'<button style="background:{VO};color:{OSC}{";box-shadow:inset 0 0 0 2px "+OSC if claro else ""}">Nueva actividad</button></div>')
secs = ''
for t, fam, nota in F:
    lk = ''
    for f, c, dc in ((OSC, CLA, SEC), (CLA, OSC, '#3a3a40')):
        lk += (f'<div class="lock" style="background:{f};color:{c};font-family:\'{fam}\'">{at(c2, 60)}<span><span class="wm g">SAM</span><span class="desc" style="color:{dc}">Simple Activity Manager</span></span></div>')
    lk += f'<div class="lock v" style="background:{OSC};color:{CLA};font-family:\'{fam}\'">{at(c2, 72)}<span class="wm g">SAM</span><span class="desc" style="color:{SEC}">Simple Activity Manager</span></div>'
    prueba = f'<p class="prueba" style="font-family:\'{fam}\'">Il1 · O0 · rn m · 14:05 · 2041 · ñ á é</p>'
    secs += (f'<section><header><h2 style="font-family:\'{fam}\'">{t}</h2><p>{nota}</p></header><div class="row">{lk}</div><div class="row al">'
             f'{tel(fam, OSC, SUP, CLA, SEC, "#2a2a30")}{tel(fam, CLA, BL, OSC, "#55555c", "#d6d6d0")}'
             f'<div class="nota">{prueba}<p class="fn">Prueba de confusión a 15 px: I mayúscula, l minúscula y 1; O y 0; «rn» y «m». Folios en JetBrains Mono en las tres.</p></div></div></section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAM · ronda 10</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=Figtree:wght@400;500;600;700&family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 'Instrument Sans',system-ui,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:{SEC};max-width:78ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:24px}} header p{{margin:4px 0 0;max-width:86ch}} .fn{{color:{SEC};font-size:13px;margin:4px 0 0}}
.row{{display:flex;flex-wrap:wrap;gap:16px;align-items:center;margin-top:16px}} .row.al{{align-items:flex-start}}
.lock{{display:flex;align-items:center;gap:13px;padding:16px 26px 16px 16px;border:1px solid #26262b;border-radius:2px}}
.lock.v{{flex-direction:column;gap:8px;padding:16px 26px;text-align:center}}
.wm{{font-weight:700;font-size:20px;letter-spacing:-.01em}} .wm.g{{display:block;font-size:44px;line-height:1}} .desc{{display:block;font-size:14px;font-weight:500;margin-top:4px}}
.tel{{width:320px;border:1px solid;border-radius:21px;padding:16px 13px;box-sizing:border-box}}
.top{{display:flex;gap:8px;align-items:center;padding:0 3px}}
.tel h3{{font-size:23px;font-weight:700;line-height:1.1;margin:21px 3px 2px;letter-spacing:-.01em}} .res{{margin:0 3px 13px;font-size:14px}}
.tel ul{{list-style:none;margin:0;padding:0;display:grid;gap:8px}}
.tel li{{border:1px solid;border-radius:6px;padding:10px 12px;display:grid;gap:3px}}
.fol{{font:500 12px 'JetBrains Mono',monospace}} .tel li b{{font-weight:600;font-size:15px;line-height:1.3}}
.pie{{display:flex;gap:8px;align-items:center;font-size:13px;margin-top:4px}} .chip{{font-size:12px;font-weight:600;padding:2px 9px;border-radius:999px}}
.tel button{{margin-top:13px;width:100%;min-height:44px;border:0;border-radius:6px;font:inherit;font-weight:600;font-size:15px}}
.nota{{max-width:260px}} .prueba{{font-size:15px;margin:0}}
</style></head><body><main><h1>SAM · identidad, ronda 10 · tipografía</h1>
<p class="sub">Símbolo y color congelados (Tarjetas C2 + C4, lima Voltaje como relleno). Tres letras para el nombre y la interfaz, probadas en el logotipo y en «Mis actividades» en celular. IBM Plex Sans (ronda 6) sale: sus formas angulosas chocan con las esquinas redondas del símbolo. Datos ficticios.</p>
{secs}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
