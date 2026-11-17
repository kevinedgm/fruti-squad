# GEMA · Gestión de Muestras y Análisis · identidad, ronda 2 (2026-11-17): formas abstractas del análisis.
# Referencia de estilo: SAM (contorno de tinta 2.6, acento como relleno que siempre toca tinta). Acento provisional (cian); el color se decide en otra ronda.
AC = 'var(--g-color-brand,#38bdf8)'; T = 'currentColor'
def svg(k, body, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="GEMA" class="gema-{k}">\n'
            f'  <!-- GEMA · {desc} -->\n{body}</svg>\n')
V = {}
PK = 'C{a} 37 {b} {t} 24 {t}C{c} {t} {d} 37'
# A1 · PICO SÓLIDO: el pico de la ronda 2 con más peso: trazo grueso, base corta, área del resultado en acento.
V['a1-pico'] = ((
 f'  <path d="M13 38C18.5 38 20 9 24 9C28 9 29.5 38 35 38Z" fill="{AC}"/>\n'
 f'  <path d="M6 38H13C18.5 38 20 9 24 9C28 9 29.5 38 35 38H42" fill="none" stroke="{T}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>\n'),
 'pico sólido: la señal del análisis con el área del resultado en acento')
# A2 · PICO EN PANTALLA: el pico dentro del marco de un instrumento; funciona como icono de app.
V['a2-pantalla'] = ((
 f'  <rect x="6" y="8" width="36" height="32" rx="7" fill="none" stroke="{T}" stroke-width="2.6"/>\n'
 f'  <path d="M15.5 33C19.5 33 21 15 24 15C27 15 28.5 33 32.5 33Z" fill="{AC}"/>\n'
 f'  <path d="M11 33H15.5C19.5 33 21 15 24 15C27 15 28.5 33 32.5 33H37" fill="none" stroke="{T}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>\n'),
 'pico en pantalla: la señal dentro del marco de un instrumento')
# B · MIRA CON PICO: las esquinas de la medición encuadran el pico; el análisis enfocado en su resultado.
V['b-mira-pico'] = ((
 f'  <g fill="none" stroke="{T}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">\n'
 '    <path d="M7 16V10Q7 7 10 7H16M32 7H38Q41 7 41 10V16M41 32V38Q41 41 38 41H32M16 41H10Q7 41 7 38V32"/>\n  </g>\n'
 f'  <path d="M17 33C20 33 21.5 16 24 16C26.5 16 28 33 31 33Z" fill="{AC}"/>\n'
 f'  <path d="M13 33H17C20 33 21.5 16 24 16C26.5 16 28 33 31 33H35" fill="none" stroke="{T}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>\n'),
 'mira con pico: la medición enfocada en el resultado')
# C · RESULTADO: la señal con un pico menor en tinta y el pico del resultado, mayor, en acento: lo que se busca destaca.
V['c-resultado'] = ((
 f'  <path d="M23 38C27.5 38 29 8 32.5 8C36 8 37.5 38 42 38Z" fill="{AC}"/>\n'
 f'  <path d="M5 38H8.5C11.5 38 12.5 25 14.5 25C16.5 25 17.5 38 20.5 38H23C27.5 38 29 8 32.5 8C36 8 37.5 38 42 38H43" fill="none" stroke="{T}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>\n'),
 'resultado: un pico menor en tinta y el del resultado, mayor, en acento')
# D · CAPAS DE SEÑAL: las capas de la ronda 2 como bandas de lectura; la central, en acento, es el resultado.
V['d-capas'] = ((
 f'  <rect x="7" y="9" width="34" height="8" rx="4" fill="{T}"/>\n'
 f'  <rect x="7" y="20" width="26" height="8" rx="4" fill="{AC}" stroke="{T}" stroke-width="2.6"/>\n'
 f'  <rect x="7" y="31" width="18" height="8" rx="4" fill="none" stroke="{T}" stroke-width="2.6"/>\n'),
 'capas de señal: bandas de lectura alineadas; la central en acento es el resultado')
for k, (b, d) in V.items(): open(f'{k}.svg', 'w').write(svg(k, b, d))
INFO = {
 'a1-pico': ('A1 · Pico sólido', 'El pico de la ronda 2 con más peso: trazo grueso y el área del resultado en color. La señal que entrega todo análisis.', 'Riesgo: sigue siendo ligero en la parte alta; a 16 px se lee como «^».'),
 'a2-pantalla': ('A2 · Pico en pantalla', 'El pico dentro del marco de un instrumento. Se lee como «resultado de un equipo» y funciona como icono de app.', 'Riesgo: el marco lo acerca a un icono de «monitor» o «estadísticas».'),
 'b-mira-pico': ('B · Mira con pico', 'Las esquinas de la medición encuadran el pico: el análisis enfocado en su resultado. Une la Mira y el Pico de la ronda 2.', 'Riesgo: dos ideas juntas; a 16 px el pico se pierde dentro de las esquinas.'),
 'c-resultado': ('C · Resultado', 'Una señal con un pico menor y el pico del resultado, mayor, en color: lo que el análisis busca destaca sobre todo lo demás.', 'Riesgo: asimétrico; necesita su espacio a la izquierda en el logotipo.'),
 'd-capas': ('D · Capas de señal', 'Las capas de la ronda 2, alineadas a la izquierda como bandas de lectura: de la medición completa al resultado. La central, en color, es el resultado.', 'Riesgo: alineadas parecen un menú o una gráfica de barras.'),
}
OSC, CLA, AV, SEC = '#0a0a0b', '#f2f2ee', '#38bdf8', '#a3a3a8'
def at(s, z): return s.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
cards = ''
for k in V:
    s = open(f'{k}.svg').read(); t, idea, r = INFO[k]
    tam = ''.join(f'<figure><div class="z">{at(s, z)}</div><figcaption>{z} px</figcaption></figure>' for z in (16, 24, 32, 48, 128))
    lock = ''.join(f'<div class="lock" style="background:{f};color:{c}">{at(s, 60)}<span><span class="wm">GEMA</span><span class="desc" style="color:{dc}">Gestión de Muestras y Análisis</span></span></div>' for f, c, dc in ((OSC, CLA, SEC), (CLA, OSC, '#3a3a40')))
    apps = (f'<div class="app" style="background:{OSC};color:{CLA}">{at(s, 60)}</div><div class="app" style="background:{CLA};color:{OSC}">{at(s, 60)}</div>'
            f'<span class="th" style="--g-color-brand:transparent">{at(s, 32)}<small>una tinta</small></span>'
            f'<div class="tab" style="background:#e4e4de;color:{OSC}">{at(s, 16)}<span>Recepción · GEMA</span></div><div class="tab">{at(s, 16)}<span>Recepción · GEMA</span></div>')
    cards += f'<section><header><h2>{t}</h2><p>{idea}</p><p class="fn">{r}</p></header><div class="row tams">{tam}</div><div class="row">{lock}</div><div class="row">{apps}</div></section>'
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GEMA · ronda 4</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;700&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 'Onest',system-ui,sans-serif;--g-color-brand:{AV}}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:{SEC};max-width:78ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px}} header p{{margin:4px 0 0;max-width:86ch}} .fn{{color:{SEC};font-size:13px}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:16px}}
.tams{{align-items:flex-end}} figure{{margin:0;text-align:center}} .z{{display:flex;align-items:flex-end;justify-content:center;min-width:56px;height:128px}}
figcaption,small{{font-size:12px;color:{SEC}}}
.lock{{display:flex;align-items:center;gap:13px;padding:16px 26px 16px 16px;border:1px solid #26262b;border-radius:2px}}
.wm{{display:block;font-weight:700;font-size:44px;line-height:1;letter-spacing:-.01em}} .desc{{display:block;font-size:14px;font-weight:500;margin-top:4px}}
.app{{width:88px;height:88px;border-radius:20px;display:flex;align-items:center;justify-content:center;border:1px solid #26262b}}
.tab{{display:flex;gap:8px;align-items:center;background:#1c1c20;border-radius:8px 8px 0 0;padding:8px 13px;font-size:13px}}
.th{{display:inline-flex;gap:6px;align-items:center;padding:6px 10px;border:1px solid #26262b;border-radius:2px}}
</style></head><body><main><h1>GEMA · identidad, ronda 4 · análisis y resultado</h1>
<p class="sub">GEMA · Gestión de Muestras y Análisis. Desarrollo de la ronda 2 (Pico, Capas y Mira), que fue la que tuvo sentido: cinco variantes que hablan del análisis de muestras y de su resultado. Estilo de SAM: tinta y un solo acento como relleno. El cian es provisional (el color se decide después) y el nombre va en Onest 700, también provisional.</p>
{cards}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
