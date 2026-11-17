# GEMA · Gestión de Muestras y Análisis · identidad, ronda 1 (2026-11-17).
# Referencia de estilo: SAM (contorno de tinta 2.6, acento como relleno que siempre toca tinta). Acento provisional (cian); el color se decide en otra ronda.
AC = 'var(--g-color-brand,#38bdf8)'; T = 'currentColor'
def svg(k, body, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="GEMA" class="gema-{k}">\n'
            f'  <!-- GEMA · {desc} -->\n{body}</svg>\n')
V = {}
# A · MUESTRA: frasco de muestra con tapa; el líquido en acento es la muestra que entra al laboratorio.
V['a-muestra'] = ((
 '  <defs><clipPath id="gema-a-c"><rect x="13" y="13" width="22" height="29" rx="6"/></clipPath></defs>\n'
 f'  <rect x="13" y="25" width="22" height="18" fill="{AC}" clip-path="url(#gema-a-c)"/>\n'
 f'  <rect x="13" y="13" width="22" height="29" rx="6" fill="none" stroke="{T}" stroke-width="2.6"/>\n'
 f'  <path d="M13.5 25H34.5" stroke="{T}" stroke-width="2.6"/>\n'
 f'  <rect x="17" y="5" width="14" height="7" rx="2" fill="{T}"/>\n'),
 'muestra: frasco con tapa; el líquido en acento es la muestra')
# B · GEMA: la piedra tallada; su parte inferior, en acento, es la gota de muestra. Une el nombre con el trabajo.
V['b-gema'] = ((
 f'  <path d="M11 18H37L24 41Z" fill="{AC}"/>\n'
 f'  <g fill="none" stroke="{T}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round">\n'
 '    <path d="M17.5 8H30.5L37 18L24 41L11 18Z"/>\n    <path d="M11 18H37M20.5 18L24 8L27.5 18"/>\n  </g>\n'),
 'gema: piedra tallada; el pabellón en acento es la gota de muestra')
# C · G CON GOTA: la G de GEMA; su barra termina en una gota de muestra en acento.
V['c-g-gota'] = ((
 f'  <path d="M35.5 14.5A14.5 14.5 0 1 0 38.5 25.5H28" fill="none" stroke="{T}" stroke-width="5" stroke-linecap="round"/>\n'
 f'  <path d="M24 19.5C24 19.5 19 25.5 19 28.5A5 5 0 0 0 29 28.5C29 25.5 24 19.5 24 19.5Z" fill="{AC}" stroke="{T}" stroke-width="2.6" stroke-linejoin="round"/>\n'),
 'G con gota: la barra de la G desemboca en una gota de muestra')
for k, (b, d) in V.items(): open(f'{k}.svg', 'w').write(svg(k, b, d))
INFO = {
 'a-muestra': ('A · Muestra', 'Un frasco de muestra con su tapa; el líquido en color es la muestra que entra al laboratorio. Es el objeto con el que empieza todo en GEMA.', 'Riesgo: se lee como «frasco» o «bebida» si el contexto no ayuda; es el más literal.'),
 'b-gema': ('B · Gema', 'La piedra tallada del nombre; su parte de abajo, en color, tiene forma de gota: la muestra. Une el nombre con lo que hace el sistema.', 'Riesgo: fuera de contexto puede leerse como joyería o «premium».'),
 'c-g-gota': ('C · G con gota', 'La G de GEMA; su barra termina en una gota de muestra en color. Letra y oficio en un solo trazo.', 'Riesgo: a 16 px la gota y la barra se juntan; necesitaría versión chica.'),
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
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GEMA · ronda 1</title>
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
</style></head><body><main><h1>GEMA · identidad, ronda 1 · símbolo</h1>
<p class="sub">GEMA · Gestión de Muestras y Análisis. Tres conceptos con el estilo de SAM: contorno de tinta y un solo acento como relleno. El cian es provisional (el color se decide después) y el nombre va en Onest 700, también provisional.</p>
{cards}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
