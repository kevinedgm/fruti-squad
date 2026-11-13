# SAM · identidad, ronda 6: tipografía pensada desde la app (usuario, 2026-11-13: «no me gusta ninguna, debe estar pensada en el contexto
# de la aplicación; SAM es Simple Activity Manager»). Criterio: la marca usa la misma letra que la interfaz.
OSC, SUP, CLA, BL, VO, VC = '#0a0a0b', '#16161a', '#f2f2ee', '#ffffff', '#c6f432', '#3f6b0a'
F = [
 ('A · Instrument Sans', 'Instrument Sans', 'JetBrains Mono', 'Es la letra de Grana (sus docs y su logotipo). SAM y su librería de interfaz hablarían con la misma voz. Compacta: caben más actividades por pantalla.'),
 ('B · Figtree', 'Figtree', 'JetBrains Mono', 'Geométrica, abierta y amable: la más «simple» de las tres. Formas redondas y amplias; se lee rápido en celular. Algo menos densa.'),
 ('C · IBM Plex Sans', 'IBM Plex Sans', 'IBM Plex Mono', 'Hecha para herramientas técnicas: distingue I, l y 1, y tiene su monoespaciada para folios. La más «manager»; un poco más seria.'),
]
ACT = [('INC-2041', 'El reporte diario de atrasos no llegó a Discord', 'En curso', 'hoy, 18:00', True),
       ('TAR-0187', 'Migrar plantillas de alta de usuario al editor visual', 'Revisión', '15 nov', False),
       ('INC-2039', 'Ticket de WhatsApp sin evidencia adjunta', 'Nuevo', '18 nov', False)]
def cortado(fam, color_t, color_a, tam):
    up = 'polygon(0 0,100% 0,100% 38%,0 62%)'; dn = 'polygon(0 62%,100% 38%,100% 100%,0 100%)'
    return (f'<span class="cw" style="font-family:\'{fam}\';font-size:{tam}px"><span style="color:{color_a};clip-path:{dn}">SAM</span>'
            f'<span style="color:{color_t};clip-path:{up};transform:translate(.055em,-.04em)">SAM</span></span>')
def tel(fam, mono, fondo, sup, tinta, sec, ac, txtbtn, linea):
    items = ''.join(
        f'<li style="background:{sup};border-color:{linea}"><span class="fol" style="font-family:\'{mono}\';color:{sec}">{f}</span><b>{t}</b>'
        f'<span class="pie"><span class="chip" style="{"background:"+ac+";color:"+txtbtn if hot else "border:1px solid "+linea+";color:"+tinta}">{e}</span><span style="color:{sec}">Vence {v}</span></span></li>'
        for f, t, e, v, hot in ACT)
    return (f'<div class="tel" style="background:{fondo};color:{tinta};font-family:\'{fam}\';border-color:{linea}">'
            f'<div class="top">{cortado(fam, tinta, ac, 28)}<span class="av" style="border-color:{linea}">KR</span></div>'
            f'<h3>Mis actividades</h3><p class="res" style="color:{sec}">3 abiertas · 1 vence hoy</p><ul>{items}</ul>'
            f'<button style="background:{ac};color:{txtbtn}">Nueva actividad</button></div>')
secs = ''
for t, fam, mono, nota in F:
    marca = (f'<div class="marca" style="background:{OSC};color:{CLA}">{cortado(fam, CLA, VO, 88)}<span class="desc" style="font-family:\'{fam}\'">Simple Activity Manager</span></div>'
             f'<div class="marca" style="background:{CLA};color:{OSC}">{cortado(fam, OSC, VC, 88)}<span class="desc" style="font-family:\'{fam}\';color:#3a3a40">Simple Activity Manager</span></div>')
    prueba = f'<p class="prueba" style="font-family:\'{fam}\'">Il1 · O0 · rn m · 14:05 · 2041 · ñ á é</p>'
    secs += (f'<section><header><h2>{t}</h2><p>{nota}</p></header><div class="row">{marca}</div><div class="row al">'
             f'{tel(fam, mono, OSC, SUP, CLA, "#a3a3a8", VO, OSC, "#2a2a30")}{tel(fam, mono, CLA, BL, OSC, "#55555c", VC, BL, "#d6d6d0")}'
             f'<div class="nota">{prueba}<p class="fn">Prueba de confusión a 15 px: I mayúscula, l minúscula y 1; O y 0; «rn» y «m».</p></div></div></section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAM · ronda 6</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;700&family=Figtree:wght@400;500;700&family=IBM+Plex+Sans:wght@400;500;700&family=IBM+Plex+Mono:wght@500&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 'Instrument Sans',system-ui,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:#a3a3a8;max-width:76ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px}} header p{{margin:4px 0 0;max-width:84ch}} .fn{{color:#a3a3a8;font-size:13px;margin:4px 0 0}}
.row{{display:flex;flex-wrap:wrap;gap:16px;align-items:center;margin-top:16px}} .row.al{{align-items:flex-start}}
.marca{{display:flex;flex-direction:column;gap:6px;padding:21px 34px;border:1px solid #26262b;border-radius:2px}}
.desc{{font-size:15px;font-weight:500;letter-spacing:.01em}}
.cw{{display:inline-grid;font-weight:700;line-height:1;letter-spacing:-.03em}} .cw>span{{grid-area:1/1}}
.tel{{width:320px;border:1px solid;border-radius:21px;padding:16px 13px;box-sizing:border-box}}
.top{{display:flex;justify-content:space-between;align-items:center;padding:0 3px}} .av{{width:32px;height:32px;border-radius:50%;border:1px solid;display:grid;place-items:center;font-size:12px;font-weight:600}}
.tel h3{{font-size:23px;font-weight:700;line-height:1.1;margin:21px 3px 2px;letter-spacing:-.01em}} .res{{margin:0 3px 13px;font-size:14px}}
.tel ul{{list-style:none;margin:0;padding:0;display:grid;gap:8px}}
.tel li{{border:1px solid;border-radius:6px;padding:10px 12px;display:grid;gap:3px}}
.fol{{font-size:12px;font-variant-numeric:tabular-nums}} .tel li b{{font-weight:600;font-size:15px;line-height:1.3}}
.pie{{display:flex;gap:8px;align-items:center;font-size:13px;margin-top:4px}} .chip{{font-size:12px;font-weight:600;padding:2px 8px;border-radius:999px}}
.tel button{{margin-top:13px;width:100%;min-height:44px;border:0;border-radius:6px;font:inherit;font-weight:600;font-size:15px}}
.nota{{max-width:260px}} .prueba{{font-size:15px;margin:0;color:{CLA}}}
</style></head><body><main><h1>SAM · identidad, ronda 6 · tipografía desde la app</h1>
<p class="sub">SAM es <b>Simple Activity Manager</b>: una herramienta que el equipo abre todo el día para ver y mover actividades. Criterio de esta ronda: la marca usa la misma letra que la interfaz, legible a 13–15 px en celular, con números claros para folios, horas y fechas. Logotipo L3 en Voltaje, con el nombre completo como descriptor. Datos de ejemplo ficticios.</p>
{secs}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
