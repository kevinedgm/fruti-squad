# GEMA · Gestión de Muestras y Análisis · identidad, ronda 2 (2026-11-17): formas abstractas del análisis.
# Referencia de estilo: SAM (contorno de tinta 2.6, acento como relleno que siempre toca tinta). Acento provisional (cian); el color se decide en otra ronda.
AC = 'var(--g-color-brand,#38bdf8)'; T = 'currentColor'
def svg(k, body, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="GEMA" class="gema-{k}">\n'
            f'  <!-- GEMA · {desc} -->\n{body}</svg>\n')
V = {}
# A · INTERSECCIÓN: la muestra (círculo) se cruza con el método (cuadrado); donde se encuentran, en acento, ocurre el análisis.
V['a-interseccion'] = ((
 '  <defs><clipPath id="gema-a-q"><rect x="6" y="12" width="24" height="24" rx="6"/></clipPath></defs>\n'
 f'  <circle cx="30" cy="24" r="12" fill="{AC}" clip-path="url(#gema-a-q)"/>\n'
 f'  <rect x="6" y="12" width="24" height="24" rx="6" fill="none" stroke="{T}" stroke-width="2.6"/>\n'
 f'  <circle cx="30" cy="24" r="12" fill="none" stroke="{T}" stroke-width="2.6"/>\n'),
 'intersección: muestra y método se cruzan; el cruce en acento es el análisis')
# B · CRISTAL: un hexágono en seis piezas, como una red cristalina; una pieza, en acento, se desprende: la fracción que se analiza.
V['b-cristal'] = ((
 f'  <path d="M26.99 18.82 L26.99 5.38 L38.63 12.10Z" fill="{AC}" stroke-linejoin="round"/>\n'
 f'  <path d="M25.48 24.00 L37.12 17.28 L37.12 30.72Z" fill="{T}" stroke-linejoin="round"/>\n'
 f'  <path d="M24.74 25.28 L36.38 32.00 L24.74 38.72Z" fill="{T}" stroke-linejoin="round"/>\n'
 f'  <path d="M23.26 25.28 L23.26 38.72 L11.62 32.00Z" fill="{T}" stroke-linejoin="round"/>\n'
 f'  <path d="M22.52 24.00 L10.88 30.72 L10.88 17.28Z" fill="{T}" stroke-linejoin="round"/>\n'
 f'  <path d="M23.26 22.72 L11.62 16.00 L23.26 9.28Z" fill="{T}" stroke-linejoin="round"/>\n'
 ),
 'cristal: hexágono en seis piezas; la pieza en acento se desprende para analizarse')
# C · ESTRATOS: un círculo cortado en cuatro franjas desplazadas, como un núcleo de muestra o un espectro; una franja en acento.
V['c-estratos'] = ((
 '  <defs><clipPath id="gema-c-o"><circle cx="24" cy="24" r="16"/></clipPath></defs>\n'
 f'  <g clip-path="url(#gema-c-o)"><rect x="0" y="8" width="48" height="7" fill="{T}"/></g>\n'
 f'  <g clip-path="url(#gema-c-o)" transform="translate(-4 0)"><rect x="4" y="16.5" width="48" height="7" fill="{T}"/></g>\n'
 f'  <g transform="translate(5 0)"><g clip-path="url(#gema-c-o)"><rect x="-5" y="25" width="48" height="7" fill="{AC}"/></g></g>\n'
 f'  <g clip-path="url(#gema-c-o)"><rect x="0" y="33.5" width="48" height="7" fill="{T}"/></g>\n'),
 'estratos: círculo en franjas desplazadas; la franja en acento es la que se mide')
# D · MÓDULOS: cuatro cuartos de una retícula; tres en tinta y uno en acento giran sobre el centro y dejan un hueco: proceso en marcha.
V['d-modulos'] = ((
 f'  <path d="M8 23A15 15 0 0 1 23 8V23Z" fill="{T}"/>\n'
 f'  <rect x="25" y="8" width="15" height="15" rx="3" fill="none" stroke="{T}" stroke-width="2.6"/>\n'
 f'  <path d="M8 25H23V40H11Q8 40 8 37Z" fill="{T}"/>\n'
 f'  <path d="M25 25H40A15 15 0 0 1 25 40Z" fill="{AC}"/>\n'),
 'módulos: cuatro cuartos de retícula; el cuarto en acento completa el proceso')
for k, (b, d) in V.items(): open(f'{k}.svg', 'w').write(svg(k, b, d))
INFO = {
 'a-interseccion': ('A · Intersección', 'Un círculo (la muestra) cruza un cuadrado (el método); donde se encuentran, en color, ocurre el análisis. Dos geometrías puras, sin dibujar nada del laboratorio.', 'Riesgo: los diagramas de Venn son comunes; aquí lo distingue mezclar círculo y cuadrado.'),
 'b-cristal': ('B · Cristal', 'Un hexágono armado con seis piezas, como una red cristalina; una pieza en color se desprende hacia fuera: la fracción que se toma para analizar. Además, una gema es un cristal.', 'Riesgo: los hexágonos se usan mucho en ciencia y tecnología; lo propio es la pieza que se separa.'),
 'c-estratos': ('C · Estratos', 'Un círculo cortado en franjas que se desplazan, como el núcleo de una muestra o las bandas de un espectro; una franja en color es la que se mide.', 'Riesgo: el desplazamiento puede leerse como «falla» o efecto glitch.'),
 'd-modulos': ('D · Módulos', 'Cuatro cuartos de una retícula: macizos, redondeados y uno abierto. El cuarto en color cierra el ciclo: muestra que entra, se analiza y sale como resultado.', 'Riesgo: abstracto puro; su significado hay que contarlo, no se ve solo.'),
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
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GEMA · ronda 3</title>
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
</style></head><body><main><h1>GEMA · identidad, ronda 3 · geometrías nuevas</h1>
<p class="sub">GEMA · Gestión de Muestras y Análisis. Cuatro geometrías construidas, sin dibujar objetos ni gráficas: superposición, cristal, estratos y módulos. Un solo acento por símbolo. El cian es provisional (el color se decide después) y el nombre va en Onest 700, también provisional.</p>
{cards}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
