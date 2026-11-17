# GEMA · Gestión de Muestras y Análisis · identidad, ronda 2 (2026-11-17): formas abstractas del análisis.
# Referencia de estilo: SAM (contorno de tinta 2.6, acento como relleno que siempre toca tinta). Acento provisional (cian); el color se decide en otra ronda.
AC = 'var(--g-color-brand,#38bdf8)'; T = 'currentColor'
def svg(k, body, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="GEMA" class="gema-{k}">\n'
            f'  <!-- GEMA · {desc} -->\n{body}</svg>\n')
V = {}
def picos(x0, x1, base, alto, sw):
    # Señal: pico menor en tinta y pico del resultado, mayor, en acento.
    w = x1 - x0; p1 = x0 + w*0.27; p2 = x0 + w*0.66; ch = base - (base - alto)*0.45
    a = f'M{x0+w*0.42:.2f} {base}C{p2-w*0.12:.2f} {base} {p2-w*0.08:.2f} {alto} {p2:.2f} {alto}C{p2+w*0.08:.2f} {alto} {p2+w*0.12:.2f} {base} {x1-w*0.06:.2f} {base}Z'
    l = (f'M{x0:.2f} {base}H{p1-w*0.13:.2f}C{p1-w*0.06:.2f} {base} {p1-w*0.04:.2f} {ch:.2f} {p1:.2f} {ch:.2f}C{p1+w*0.04:.2f} {ch:.2f} {p1+w*0.06:.2f} {base} {x0+w*0.42:.2f} {base}'
         f'C{p2-w*0.12:.2f} {base} {p2-w*0.08:.2f} {alto} {p2:.2f} {alto}C{p2+w*0.08:.2f} {alto} {p2+w*0.12:.2f} {base} {x1-w*0.06:.2f} {base}H{x1:.2f}')
    return (f'  <path d="{a}" fill="{AC}"/>\n'
            f'  <path d="{l}" fill="none" stroke="{T}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>\n')
ESQ = '    <path d="M7 16V10Q7 7 10 7H16M32 7H38Q41 7 41 10V16M41 32V38Q41 41 38 41H32M16 41H10Q7 41 7 38V32"/>\n'
V['r1-pantalla'] = ((f'  <rect x="5" y="8" width="38" height="32" rx="7" fill="none" stroke="{T}" stroke-width="2.6"/>\n' + picos(10, 38, 33, 14, 2.6)),
 'pantalla + resultado: el doble pico dentro del marco del instrumento')
V['r2-mira'] = ((f'  <g fill="none" stroke="{T}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">\n' + ESQ + '  </g>\n' + picos(12, 36, 33, 15, 2.6)),
 'mira + resultado: el doble pico encuadrado por las esquinas de la medición')
V['r3-resultado'] = (picos(4, 44, 38, 9, 3.2), 'resultado: pico menor en tinta y pico del resultado en acento')
for k, (b, d) in V.items(): open(f'{k}.svg', 'w').write(svg(k, b, d))
INFO = {
 'r1-pantalla': ('R1 · Pantalla + Resultado', 'A2 + C. El doble pico dentro del marco de un instrumento: el resultado de un análisis tal como aparece en el equipo. El marco le da cuerpo de icono.', 'Riesgo: dentro del marco, a 16 px el pico menor casi desaparece.'),
 'r2-mira': ('R2 · Mira + Resultado', 'B + C. Las esquinas de la medición encuadran el doble pico: el análisis enfocado en el resultado que se busca.', 'Riesgo: es el más fino de los tres; necesita versión chica.'),
 'r3-resultado': ('R3 · Resultado', 'C sola, más equilibrada: la señal con un pico menor y el pico del resultado, mayor, en color. Sin marco: la forma más simple.', 'Riesgo: sin marco es ancha y baja; en un icono cuadrado deja aire arriba.'),
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
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GEMA · ronda 5</title>
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
</style></head><body><main><h1>GEMA · identidad, ronda 5 · B + A2 + C</h1>
<p class="sub">GEMA · Gestión de Muestras y Análisis. El usuario eligió B (Mira con pico), A2 (Pico en pantalla) y C (Resultado). Tres combinaciones: el doble pico del resultado en el marco del instrumento, en las esquinas de la medición y solo. El cian es provisional (el color se decide después) y el nombre va en Onest 700, también provisional.</p>
{cards}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
