# SAM · identidad, ronda 7: replanteo de logo y color (usuario, 2026-11-13).
# Logo: el corte es «demasiado agresivo» y «no dice actividad». Color: el lima se queda; lo que falla es el oliva del modo claro.
# Regla de color nueva: el lima nunca se oscurece. Es relleno, siempre tocando tinta (contorno o fondo). En claro, texto, enlaces y foco van en tinta.
LIMA = 'var(--g-color-brand,#c6f432)'
def svg(k, body, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="SAM" class="sam-{k}">\n'
            f'  <!-- SAM · {desc} -->\n{body}</svg>\n')
V = {}
# A · ETAPAS: dos etapas cumplidas (círculos en tinta) y la actividad en curso (píldora lima con contorno en tinta).
V['a-etapas'] = ((
 '  <circle cx="9" cy="24" r="5.5" fill="currentColor"/>\n  <circle cx="22" cy="24" r="5.5" fill="currentColor"/>\n'
 f'  <rect x="30" y="17.5" width="15" height="13" rx="6.5" fill="{LIMA}" stroke="currentColor" stroke-width="2.6"/>\n'),
 'etapas: dos cumplidas y la actividad en curso')
# B · RUTA: una S amable de trazo redondo con tres paradas; la última, en lima, es donde va la actividad.
V['b-ruta'] = ((
 '  <path d="M33 11.5C30.8 9.6 27.8 8.6 24.4 8.6C18.6 8.6 14.6 11.6 14.6 16.2C14.6 25.6 33.4 21.8 33.4 31.6C33.4 36.4 29.4 39.4 23.6 39.4C20.2 39.4 17.2 38.4 15 36.5" fill="none" stroke="currentColor" stroke-width="4.6" stroke-linecap="round"/>\n'
 '  <circle cx="24" cy="24" r="4.2" fill="currentColor"/>\n'
 f'  <circle cx="35.4" cy="11.4" r="5.6" fill="{LIMA}" stroke="currentColor" stroke-width="2.6"/>\n'),
 'ruta: la S es el camino de la actividad; la parada en lima es donde va')
# C · TARJETAS: la actividad es una tarjeta que pasa adelante; detrás queda la anterior.
V['c-tarjetas'] = ((
 '  <rect x="6" y="9" width="26" height="22" rx="5" fill="currentColor"/>\n'
 f'  <rect x="16" y="17" width="26" height="22" rx="5" fill="{LIMA}" stroke="currentColor" stroke-width="2.6"/>\n'
 '  <path d="M22.5 28.2L26.5 32L35 23.8" fill="none" stroke="var(--sam-tinta,#0a0a0b)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>\n'),
 'tarjetas: la actividad pasa adelante y se completa; detrás queda la anterior')
for k, (b, d) in V.items(): open(f'{k}.svg', 'w').write(svg(k, b, d))
INFO = {
 'a-etapas': ('A · Etapas', 'Dos etapas cumplidas y la actividad en curso, que se estira hacia delante. Es un indicador de progreso convertido en marca: dice «actividad que avanza» sin letra.', 'Riesgo: fuera de contexto puede leerse como «escribiendo…» o un indicador de carga.'),
 'b-ruta': ('B · Ruta', 'La S de SAM es el camino; la parada en lima es la actividad. Trazo redondo y amable, sin corte. Une el nombre con la idea de flujo entre etapas.', 'Riesgo: a 16 px la parada intermedia se pierde (queda S + punto).'),
 'c-tarjetas': ('C · Tarjetas', 'Una tarjeta de actividad pasa adelante y queda completada; la anterior queda detrás. Es lo que el equipo hace todo el día en SAM.', 'Riesgo: tarjetas y palomita son comunes en apps de tareas; lo propio lo pone el lima con contorno.'),
}
OSC, SUP, CLA, BL, VO, SEC = '#0a0a0b', '#16161a', '#f2f2ee', '#ffffff', '#c6f432', '#a3a3a8'
def at(s, z): return s.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
def barra(s, fondo, tinta, linea):
    return (f'<div class="tel" style="background:{fondo};color:{tinta};border-color:{linea}"><div class="top">{at(s, 30)}<span class="wm">SAM</span></div>'
            f'<h3>Mis actividades</h3><div class="it" style="border-color:{linea}"><span class="fol">INC-2041</span><b>El reporte diario de atrasos no llegó a Discord</b>'
            f'<span class="chip" style="background:{VO};color:{OSC};box-shadow:inset 0 0 0 1.5px {OSC if fondo == CLA else VO}">En curso</span></div>'
            f'<button style="background:{VO};color:{OSC};box-shadow:inset 0 0 0 2px {OSC if fondo == CLA else VO}">Nueva actividad</button>'
            f'<a style="color:{tinta}">Adjuntar evidencia</a></div>')
cards = ''
for k in V:
    s = open(f'{k}.svg').read(); t, idea, riesgo = INFO[k]
    tam = ''.join(f'<figure><div class="z">{at(s, z)}</div><figcaption>{z} px</figcaption></figure>' for z in (16, 24, 32, 48, 128))
    marca = (f'<div class="lock" style="background:{OSC};color:{CLA}">{at(s, 56)}<span><span class="wm g">SAM</span><span class="desc">Simple Activity Manager</span></span></div>'
             f'<div class="lock" style="background:{CLA};color:{OSC}">{at(s, 56)}<span><span class="wm g">SAM</span><span class="desc" style="color:#3a3a40">Simple Activity Manager</span></span></div>')
    apps = (f'<div class="app" style="background:{OSC};color:{CLA}">{at(s, 60)}</div>'
            f'<div class="app" style="background:{CLA};color:{OSC}">{at(s, 60)}</div>'
            f'<div class="app" style="background:{VO};color:{OSC};--g-color-brand:{CLA}">{at(s, 60)}</div>'
            f'<div class="tab" style="background:#e4e4de;color:{OSC}">{at(s, 16)}<span>Mis actividades · SAM</span></div>'
            f'<div class="tab">{at(s, 16)}<span>Mis actividades · SAM</span></div>')
    cards += (f'<section><header><h2>{t}</h2><p>{idea}</p><p class="fn">{riesgo}</p></header><div class="row tams">{tam}</div>'
              f'<div class="row">{marca}</div><div class="row">{apps}</div><div class="row al">{barra(s, OSC, CLA, "#2a2a30")}{barra(s, CLA, OSC, "#d6d6d0")}</div></section>')
regla = ('<section class="regla"><h2>Regla de color nueva: el lima ya no se oscurece</h2>'
         '<p>El oliva aparecía porque usábamos el lima como <b>texto</b> en modo claro, y un lima que se lea sobre blanco tiene que volverse oliva. '
         'Ahora el lima es solo <b>relleno</b> (botón principal, estado activo, el acento del símbolo) y siempre va tocando tinta: texto oscuro encima y contorno oscuro en claro. '
         'En modo claro, el texto, los enlaces y el foco van en tinta.</p>'
         '<ul><li>Texto tinta sobre lima: <b>15.4:1</b></li><li>Lima sobre fondo oscuro: <b>15.4:1</b></li>'
         '<li>Lima sobre fondo claro: <b>1.1:1</b>, por eso en claro nunca va sin contorno de tinta ni como texto</li><li>Foco y enlaces en tinta sobre claro: <b>16.1:1</b></li></ul></section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAM · ronda 7</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 'Instrument Sans',system-ui,sans-serif;--g-color-brand:{VO}}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:{SEC};max-width:76ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px}} header p,.regla p{{margin:4px 0 0;max-width:86ch}} .fn{{color:{SEC};font-size:13px}} .regla ul{{margin:8px 0 0;padding-left:18px;color:#cfcfca}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:16px}} .row.al{{align-items:flex-start}}
.tams{{align-items:flex-end}} figure{{margin:0;text-align:center}} .z{{display:flex;align-items:flex-end;justify-content:center;min-width:56px;height:128px}}
figcaption{{font-size:12px;color:{SEC}}}
.lock{{display:flex;align-items:center;gap:13px;padding:16px 30px 16px 18px;border:1px solid #26262b;border-radius:2px}}
.wm{{font-weight:700;font-size:22px;letter-spacing:-.01em}} .wm.g{{display:block;font-size:44px;line-height:1}} .desc{{display:block;font-size:14px;font-weight:500;margin-top:4px}}
.app{{width:88px;height:88px;border-radius:20px;display:flex;align-items:center;justify-content:center;border:1px solid #26262b}}
.tab{{display:flex;gap:8px;align-items:center;background:#1c1c20;border-radius:8px 8px 0 0;padding:8px 13px;font-size:13px}}
.tel{{width:320px;border:1px solid;border-radius:21px;padding:16px 13px;box-sizing:border-box;display:grid;gap:10px}}
.top{{display:flex;gap:8px;align-items:center}} .tel h3{{font-size:23px;margin:8px 0 0}}
.it{{border:1px solid;border-radius:6px;padding:10px 12px;display:grid;gap:4px;justify-items:start}} .it b{{font-weight:600;line-height:1.3}}
.fol{{font:500 12px 'JetBrains Mono',monospace;opacity:.75}} .chip{{font-size:12px;font-weight:600;padding:2px 9px;border-radius:999px}}
.tel button{{min-height:44px;border:0;border-radius:6px;font:inherit;font-weight:600}} .tel a{{font-weight:600;text-decoration:underline;text-underline-offset:3px;justify-self:start}}
</style></head><body><main><h1>SAM · identidad, ronda 7 · replanteo de logo y color</h1>
<p class="sub">Tres símbolos nuevos que dicen «actividad», sin corte y sin agresividad. El lima Voltaje se queda con una regla nueva para el modo claro. Nombre en Instrument Sans 700 (provisional, la recomendada de la ronda 6), con el descriptor Simple Activity Manager.</p>
{regla}{cards}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
