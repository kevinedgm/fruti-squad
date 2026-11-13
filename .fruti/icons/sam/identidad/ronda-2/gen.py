# SAM · identidad, ronda 2: más moderna, tecnológica y disruptiva (usuario, 2026-11-13: «no me gusta, quiero una propuesta más moderna, tecnológica, disruptiva»).
# Estructura en currentColor; acento en --g-color-brand. Acento provisional: lima eléctrica en oscuro, oliva en claro (el color se decide en otra ronda).
COLOR = 'var(--g-color-brand,#c6f432)'
def svg(k, body, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="SAM" class="sam-{k}">\n'
            f'  <!-- SAM · {desc} -->\n{body}</svg>\n')
V = {}
# A · CORTE: una S sólida rebanada en diagonal; la mitad superior se desliza hacia delante sobre el corte.
S = 'M33.5 12.6C31.2 10.2 28 9 24 9C18 9 13.8 12 13.8 16.8C13.8 26.4 34.2 21.8 34.2 31.6C34.2 36.4 30 39.4 24 39.4C19.6 39.4 16.4 38 13.6 35.2'
V['a-corte'] = ((
 '  <defs><clipPath id="sam-a-arr"><path d="M0 0H48V18L0 30Z"/></clipPath><clipPath id="sam-a-aba"><path d="M0 30L48 18V48H0Z"/></clipPath></defs>\n'
 f'  <g fill="none" stroke-width="8.4">\n'
 f'    <path d="{S}" stroke="currentColor" clip-path="url(#sam-a-arr)" transform="translate(2.6 -1.9)"/>\n'
 f'    <path d="{S}" stroke="{COLOR}" clip-path="url(#sam-a-aba)"/>\n  </g>\n'),
 'corte: S sólida rebanada en diagonal; la parte de arriba se adelanta sobre el corte')
# B · MATRIZ: S de módulos en retícula 4 × 5; la fila central se desplaza hacia delante y un módulo va en color (la tarea en movimiento).
P = ['.XXX', 'X...', '.XX.', '...X', 'XXX.']
m, g, x0, y0 = 7, 2, 7, 2.5
B = ''
for r, fila in enumerate(P):
    for c, v in enumerate(fila):
        if v != 'X': continue
        dx = 4.5 if r == 2 else 0
        col = COLOR if (r, c) == (2, 2) else 'currentColor'
        B += f'  <rect x="{x0 + c*(m+g) + dx:g}" y="{y0 + r*(m+g):g}" width="{m}" height="{m}" rx="1.4" fill="{col}"/>\n'
V['b-matriz'] = (B, 'matriz: S de módulos; la fila central se desplaza y un módulo en color es la tarea que avanza')
# C · TERMINAL: «s» minúscula de trazo monoespaciado y un cursor de bloque en color: SAM habla el idioma del equipo que lo usa.
V['c-terminal'] = ((
 '  <path d="M24.5 19.6C23 17.6 20.6 16.5 17.6 16.5C13.4 16.5 10.6 18.6 10.6 21.8C10.6 28.8 25.4 25.4 25.4 32.6C25.4 36.2 22.4 38.4 17.8 38.4C14.2 38.4 11.4 37 9.6 34.6" fill="none" stroke="currentColor" stroke-width="4.6" stroke-linecap="square"/>\n'
 f'  <rect x="29.5" y="33.6" width="13" height="5" fill="{COLOR}"/>\n'),
 'terminal: «s» monoespaciada y cursor de subrayado en color')
for k, (b, d) in V.items(): open(f'{k}.svg', 'w').write(svg(k, b, d))

INFO = {
 'a-corte': ('A · Corte', 'Una S sólida rebanada en diagonal. La parte de arriba ya se adelantó sobre el corte: el trabajo no espera a que la fase anterior termine de cerrarse. Es la ruptura literal: SAM se parte del sistema viejo.', 'Geist 700', 'SAM'),
 'b-matriz': ('B · Matriz', 'Una S hecha de módulos, como píxeles o celdas de datos. La fila central se desplaza hacia delante y un módulo va en color: la tarea que está avanzando. Puede animarse módulo por módulo.', 'Geist 700', 'SAM'),
 'c-terminal': ('C · Terminal', 'Una «s» monoespaciada y un cursor de subrayado («s_»). SAM habla el idioma del equipo que lo usa (desarrollo y soporte): listo para escribir, siempre activo. El cursor parpadea como movimiento de marca.', 'JetBrains Mono 700', 'sam'),
}
OSC, CLA, LIMA, OLIVA = '#0a0a0b', '#f2f2ee', '#c6f432', '#4d7c0f'
TEMAS = [('lima', LIMA), ('cian', '#22d3ee'), ('naranja', '#ff7a1a'), ('blanco', '#f2f2ee')]
def at(s, z): return s.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
cards = ''
for k in V:
    s = open(f'{k}.svg').read(); t, idea, fuente, nom = INFO[k]
    fam = '"JetBrains Mono",monospace' if 'Mono' in fuente else '"Geist",sans-serif'
    cur = f'<i class="cur" style="background:{LIMA}"></i>' if k == 'c-terminal' else ''
    curc = f'<i class="cur" style="background:{OLIVA}"></i>' if k == 'c-terminal' else ''
    tam = ''.join(f'<figure><div class="z">{at(s, z)}</div><figcaption>{z} px</figcaption></figure>' for z in (16, 24, 32, 48, 128))
    lock_o = f'<div class="lock" style="background:{OSC};color:{CLA}">{at(s, 52)}<span class="wm" style="font-family:{fam}">{nom}{cur}</span></div>'
    lock_c = f'<div class="lock" style="background:{CLA};color:{OSC};--g-color-brand:{OLIVA}">{at(s, 52)}<span class="wm" style="font-family:{fam}">{nom}{curc}</span></div>'
    apps = (f'<div class="app" style="background:{OSC};color:{CLA}">{at(s, 64)}</div>'
            f'<div class="app" style="background:{LIMA};color:{OSC};--g-color-brand:{OSC}">{at(s, 64)}</div>'
            f'<div class="app" style="background:{CLA};color:{OSC};--g-color-brand:{OLIVA}">{at(s, 64)}</div>')
    tab = f'<div class="tab">{at(s, 16)}<span>Mis pendientes · SAM</span></div>'
    th = ''.join(f'<span class="th" style="--g-color-brand:{c}">{at(s, 32)}<small>{n}</small></span>' for n, c in TEMAS)
    mono = f'<span class="th" style="--g-color-brand:currentColor">{at(s, 32)}<small>una tinta</small></span>'
    cards += (f'<section><header><h2>{t}</h2><p>{idea}</p><p class="fn">Nombre provisional en {fuente}</p></header>'
              f'<div class="row tams">{tam}</div><div class="row">{lock_o}{lock_c}</div><div class="row">{apps}{tab}</div><div class="row">{th}{mono}</div></section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAM · ronda 2</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;700&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 "Geist",system-ui,sans-serif;--g-color-brand:{LIMA}}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:#a3a3a8;max-width:72ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px;letter-spacing:-.01em}} header p{{margin:4px 0 0;max-width:80ch}} .fn{{color:#a3a3a8;font-size:13px}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:21px}}
.tams{{align-items:flex-end}} figure{{margin:0;text-align:center}} .z{{display:flex;align-items:flex-end;justify-content:center;min-width:56px;height:128px}}
figcaption,small{{font-size:12px;color:#a3a3a8}}
.lock{{display:flex;align-items:center;gap:10px;padding:13px 26px 13px 16px;border:1px solid #26262b;border-radius:2px}}
.wm{{font-weight:700;font-size:46px;line-height:1;letter-spacing:-.03em}}
.cur{{display:inline-block;width:24px;height:7px;margin-left:4px;vertical-align:baseline}}
.app{{width:96px;height:96px;border-radius:22px;display:flex;align-items:center;justify-content:center;border:1px solid #26262b}}
.tab{{display:flex;gap:8px;align-items:center;background:#1c1c20;border-radius:8px 8px 0 0;padding:8px 13px;font-size:13px}}
.th{{display:inline-flex;gap:6px;align-items:center;padding:6px 10px;border:1px solid #26262b;border-radius:2px}}
code{{font-family:"JetBrains Mono",monospace;font-size:13px}}
</style></head><body><main><h1>SAM · identidad, ronda 2</h1>
<p class="sub">Más moderna, tecnológica y disruptiva. Tres conceptos nuevos (no derivan de la ronda 1). La lima es provisional en oscuro y el oliva en claro: el color se decide en otra ronda y en la app lo pone <code>--g-color-brand</code> de Grana.</p>
{cards}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
