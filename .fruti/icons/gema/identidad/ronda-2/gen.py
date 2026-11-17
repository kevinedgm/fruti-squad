# GEMA · Gestión de Muestras y Análisis · identidad, ronda 2 (2026-11-17): formas abstractas del análisis.
# Referencia de estilo: SAM (contorno de tinta 2.6, acento como relleno que siempre toca tinta). Acento provisional (cian); el color se decide en otra ronda.
AC = 'var(--g-color-brand,#38bdf8)'; T = 'currentColor'
def svg(k, body, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="GEMA" class="gema-{k}">\n'
            f'  <!-- GEMA · {desc} -->\n{body}</svg>\n')
V = {}
# A · PICO: la señal de un instrumento (cromatograma): sobre la línea base aparece un pico; su área, en acento, es el resultado.
V['a-pico'] = ((
 f'  <path d="M14.5 37C19 37 20.5 11 24 11C27.5 11 29 37 33.5 37Z" fill="{AC}"/>\n'
 f'  <path d="M6 37H14.5C19 37 20.5 11 24 11C27.5 11 29 37 33.5 37H42" fill="none" stroke="{T}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>\n'),
 'pico: señal de un instrumento; el área del pico en acento es el resultado')
# B · CAPAS: una muestra separada en sus componentes; tres capas que se angostan, la del centro en acento es lo que se mide.
V['b-capas'] = ((
 f'  <rect x="8" y="10" width="32" height="7" rx="3.5" fill="none" stroke="{T}" stroke-width="2.6"/>\n'
 f'  <rect x="13" y="21" width="22" height="7" rx="3.5" fill="{AC}" stroke="{T}" stroke-width="2.6"/>\n'
 f'  <rect x="18" y="32" width="12" height="7" rx="3.5" fill="{T}"/>\n'),
 'capas: la muestra separada en sus componentes; la capa central en acento es lo que se mide')
# C · MIRA: el encuadre de la medición; cuatro esquinas de tinta y, al centro, la muestra en acento.
V['c-mira'] = ((
 f'  <g fill="none" stroke="{T}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">\n'
 '    <path d="M8 17V11Q8 8 11 8H17M31 8H37Q40 8 40 11V17M40 31V37Q40 40 37 40H31M17 40H11Q8 40 8 37V31"/>\n  </g>\n'
 f'  <circle cx="24" cy="24" r="7.5" fill="{AC}" stroke="{T}" stroke-width="2.6"/>\n'),
 'mira: el encuadre de la medición con la muestra en acento al centro')
for k, (b, d) in V.items(): open(f'{k}.svg', 'w').write(svg(k, b, d))
INFO = {
 'a-pico': ('A · Pico', 'La señal que entrega un instrumento de análisis: sobre la línea base aparece un pico, y su área en color es el resultado. Es lo que el laboratorio ve todos los días en un cromatograma o un espectro.', 'Riesgo: también parece una gráfica de «tendencia» o un pulso; el contexto lo aclara.'),
 'b-capas': ('B · Capas', 'Una muestra separada en sus componentes, como en una destilación o una decantación: tres capas que se van angostando; la del centro, en color, es lo que se mide.', 'Riesgo: también se lee como embudo de ventas o filtro.'),
 'c-mira': ('C · Mira', 'El encuadre de una medición: cuatro esquinas que enfocan y, al centro, la muestra en color. Precisión y control, sin dibujar ningún instrumento.', 'Riesgo: se parece al icono de «escanear» o «enfocar» de las cámaras.'),
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
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GEMA · ronda 2</title>
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
</style></head><body><main><h1>GEMA · identidad, ronda 2 · formas abstractas</h1>
<p class="sub">GEMA · Gestión de Muestras y Análisis. Ronda 1 rechazada: los objetos no hablaban del laboratorio. Tres formas abstractas que salen del análisis: la señal, la separación y la medición. Estilo de SAM: contorno de tinta y un solo acento como relleno. El cian es provisional (el color se decide después) y el nombre va en Onest 700, también provisional.</p>
{cards}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
