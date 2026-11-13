# SAM · identidad, ronda 1: tres conceptos de símbolo (lienzo 48). Marca independiente; carácter «ágil».
# Estructura en tinta (currentColor); el acento lee --g-color-brand de Grana (provisional naranja: el color se decide en otra ronda).
COLOR = 'var(--g-color-brand,#c2410c)'
def svg(k, body, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="SAM" class="sam-{k}">\n'
            f'  <!-- SAM · {desc} -->\n{body}</svg>\n')
V = {}
# A · RELEVO: la S partida en dos mitades desplazadas; el tramo central (el testigo) pasa de una a otra en color.
V['a-relevo'] = ((
 '  <g fill="none" stroke-width="5.2" stroke-linecap="round">\n'
 '    <path d="M32 12.5C29.4 9.6 26.4 8.4 22.6 8.4C17 8.4 12.6 11.4 12.6 16C12.6 19 14.4 20.8 17 21.9" stroke="currentColor"/>\n'
 '    <path d="M31 26.1C33.6 27.2 35.4 29 35.4 32C35.4 36.6 31 39.6 25.4 39.6C21.6 39.6 18.6 38.4 16 35.5" stroke="currentColor"/>\n'
 f'    <path d="M21.6 23.4L26.4 24.6" stroke="{COLOR}" stroke-width="6"/>\n  </g>\n'),
 'relevo: la S partida; el testigo en color pasa de una mitad a la otra')
# B · RECORRIDO: la S como un camino por etapas (tramos rectos y vueltas cortas); la tarea, un punto en color, va en camino.
V['b-recorrido'] = ((
 '  <path d="M35 9.5H18.5Q13 9.5 13 15V18.5Q13 24 18.5 24H29.5Q35 24 35 29.5V33Q35 38.5 29.5 38.5H18" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>\n'
 f'  <circle cx="10.5" cy="38.5" r="3.6" fill="{COLOR}"/>\n'),
 'recorrido: la S es el camino entre etapas y la tarea, en color, avanza al frente')
# C · PULSO: S continua e inclinada hacia delante; su remate superior se suelta como un aviso en color.
V['c-pulso'] = ((
 '  <g transform="skewX(-10) translate(4 0)">\n'
 '    <path d="M29.5 12.2C27.4 10 25 9.2 22 9.2C16.6 9.2 12.8 12 12.8 16.4C12.8 26 34.8 21.6 34.8 31.6C34.8 36.6 30.6 39.6 24.6 39.6C20.4 39.6 17.2 38.2 14.6 35.4" fill="none" stroke="currentColor" stroke-width="5.2" stroke-linecap="round"/>\n'
 f'    <circle cx="35.6" cy="9.4" r="4.4" fill="{COLOR}"/>\n  </g>\n'),
 'pulso: S en marcha (inclinada) y su remate suelto como aviso en color')
for k, (b, d) in V.items(): open(f'{k}.svg', 'w').write(svg(k, b, d))

INFO = {
 'a-relevo': ('A · Relevo', 'La S se parte en dos mitades desplazadas. El tramo central, en color, es el testigo: el trabajo pasa de una persona o fase a la siguiente sin detenerse.', 'Función 3 del brief: mover el trabajo entre personas o fases.'),
 'b-recorrido': ('B · Recorrido', 'La S es un camino de tramos rectos y vueltas cortas, como un tablero de etapas. El punto en color es la tarea que va avanzando.', 'Funciones 1 y 3: controlar la tarea y su paso por etapas.'),
 'c-pulso': ('C · Pulso', 'Una S continua, inclinada hacia delante. Su remate superior se suelta como un aviso: el trabajo te llama a tiempo.', 'Función 7: avisar a tiempo (push, Discord, correo).'),
}
TEMAS = [('naranja', '#c2410c'), ('azul', '#1d4ed8'), ('verde', '#15803d'), ('magenta', '#a21caf')]
TINTA, PAPEL = '#16181d', '#f4f3ef'
def at(s, z, extra=''): return s.replace('<svg ', f'<svg width="{z}" height="{z}" {extra}', 1)
cards = ''
for k in V:
    s = open(f'{k}.svg').read(); t, idea, fn = INFO[k]
    tam = ''.join(f'<figure><div class="z" style="height:128px">{at(s, z)}</div><figcaption>{z} px</figcaption></figure>' for z in (16, 24, 32, 48, 128))
    lock = f'<div class="lock">{at(s, 56)}<span class="wm">SAM</span></div>'
    app = (f'<div class="app" style="background:{TINTA};color:{PAPEL}">{at(s, 60)}</div>'
           f'<div class="app" style="background:#c2410c;color:{PAPEL};--g-color-brand:{TINTA}">{at(s, 60)}</div>')
    tab = f'<div class="tab">{at(s, 16)}<span>Mis pendientes · SAM</span></div>'
    th = ''.join(f'<span class="th" style="--g-color-brand:{c}">{at(s, 32)}<small>{n}</small></span>' for n, c in TEMAS)
    dk = f'<span class="th dk" style="--g-color-brand:#fb923c">{at(s, 32)}<small>oscuro</small></span>'
    mono = f'<span class="th" style="--g-color-brand:currentColor">{at(s, 32)}<small>una tinta</small></span>'
    cards += (f'<section><header><h2>{t}</h2><p>{idea}</p><p class="fn">Nace de: {fn}</p></header>'
              f'<div class="row tams">{tam}</div><div class="row">{lock}{app}{tab}</div><div class="row">{th}{dk}{mono}</div></section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAM · ronda 1</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{PAPEL};color:{TINTA};font:15px/1.5 "Space Grotesk",system-ui,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:32px;line-height:1.1;margin:0 0 8px}} .sub{{margin:0 0 34px;color:#4a4d55;max-width:70ch}}
section{{background:#fbfaf7;border:1px solid #d9d6cf;border-radius:4px;padding:21px;margin-bottom:21px}}
h2{{margin:0;font-size:22px}} header p{{margin:4px 0 0;max-width:80ch}} .fn{{color:#4a4d55;font-size:13px}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:21px}}
.tams{{align-items:flex-end}} figure{{margin:0;text-align:center}} .z{{display:flex;align-items:flex-end;justify-content:center;min-width:56px}}
figcaption,small{{font-size:12px;color:#4a4d55}}
.lock{{display:flex;align-items:center;gap:8px;padding:8px 21px 8px 13px;border:1px solid #d9d6cf;border-radius:4px}}
.wm{{font:700 44px/1 "Space Grotesk";letter-spacing:-.02em}}
.app{{width:88px;height:88px;border-radius:21px;display:flex;align-items:center;justify-content:center}}
.tab{{display:flex;gap:8px;align-items:center;background:#e6e3dc;border-radius:8px 8px 0 0;padding:8px 13px;font-size:13px}}
.th{{display:inline-flex;gap:6px;align-items:center;padding:6px 10px;border:1px solid #d9d6cf;border-radius:4px}}
.th.dk{{background:#121317;color:#f1efe9;border-color:#121317}} .th.dk small{{color:#c9c6be}}
</style></head><body><main><h1>SAM · identidad, ronda 1</h1>
<p class="sub">Tres conceptos de símbolo, en tinta con un acento. El naranja es provisional: el color se decide en otra ronda y en la app lo pone <code>--g-color-brand</code> de Grana. La tipografía del nombre (Space Grotesk 700) también es provisional.</p>
{cards}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
