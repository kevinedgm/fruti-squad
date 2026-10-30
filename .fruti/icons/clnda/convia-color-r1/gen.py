# Convia · color ronda 1, sobre el símbolo aprobado E1b (../convia-r7/E1b.svg). Uso: python3 gen.py <carpeta de fuentes>
import sys, os, re
F = sys.argv[1] if len(sys.argv) > 1 else '.'
D = os.path.dirname(os.path.abspath(__file__))
star = open(os.path.join(D, '..', 'convia-r7', 'E1b.svg')).read()
path = re.search(r'<path d="([^"]+)"', star).group(1)
def sym(c, size): return f'<svg viewBox="0 0 200 200" width="{size}" height="{size}" aria-hidden="true"><path d="{path}" fill="{c}"/></svg>'
def lum(h):
    c = [int(h[i:i+2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b):
    x, y = sorted([lum(a), lum(b)], reverse=True); return (x + .05) / (y + .05)
PAL = [
 ('A', 'Convite', 'Las flores y el papel del convite: magenta, naranja y amarillo sobre un morado de noche de fiesta.',
  dict(fondo='#2a1a5e', principal='#d42a66', acento='#ffb627', apoyo='#f2711c', papel='#fff8f0', tinta='#1d1530')),
 ('B', 'Convite + cantera', 'El verde cantera de la ciudad como base, con el magenta y el amarillo de la fiesta como acentos.',
  dict(fondo='#1f4d3a', principal='#d42a66', acento='#ffc53d', apoyo='#3f8f6b', papel='#f6f3ea', tinta='#15241d')),
 ('C', 'Verde y coral', 'Verde cantera y un solo acento coral: más sobria, la fiesta queda en el símbolo.',
  dict(fondo='#1f4d3a', principal='#d4392c', acento='#ff5a4e', apoyo='#9cc5b0', papel='#f4f2ec', tinta='#15241d')),
]
font = os.path.join(F, 'InstrumentSans[wdth,wght].ttf')
cards = ''
for k, n, desc, p in PAL:
    sw = ''.join(f'<span class="sw"><i style="background:{v}"></i><b>{nm}</b><code>{v}</code></span>' for nm, v in p.items())
    checks = [('Acento sobre fondo (gráfico ≥ 3)', cr(p['acento'], p['fondo'])), ('Principal sobre papel (gráfico ≥ 3)', cr(p['principal'], p['papel'])),
              ('Tinta sobre papel (texto ≥ 4.5)', cr(p['tinta'], p['papel'])), ('Blanco sobre principal (botón ≥ 4.5)', cr('#ffffff', p['principal']))]
    ck = ''.join(f'<li class="{"ok" if v >= (4.5 if "texto" in t or "botón" in t else 3) else "bad"}">{t}: <b>{v:.1f}</b></li>' for t, v in checks)
    cards += f'''<article style="--f:{p['fondo']};--p:{p['principal']};--a:{p['acento']};--pa:{p['papel']};--t:{p['tinta']};--ap:{p['apoyo']}">
<div class="hero"><div class="app">{sym(p['acento'], 76)}</div><div class="lk">{sym(p['principal'], 46)}<b>Convia</b></div></div>
<div class="ui"><span class="chip">Hoy · Centro</span><h3>Taller de cerámica para ir solo</h3><p>Sáb 11:00 · 4 lugares</p><button>Ver plan</button></div>
<div class="sws">{sw}</div><ul class="ck">{ck}</ul><h2>{k} · {n}</h2><p class="d">{desc}</p></article>'''
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Convia · color r1</title><style>
@font-face{{font-family:IS;src:url("file://{font}")}}
body{{margin:0;padding:32px;background:#efeee9;color:#1b1b1d;font:15px/1.45 IS,system-ui,sans-serif}}h1{{margin:0 0 4px;font-size:26px}}.lead{{margin:0 0 24px;color:#55555a}}
main{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
article{{background:#fff;border-radius:16px;overflow:hidden;display:grid;gap:14px;padding-bottom:20px;border:1px solid #e3e3de}}
article>*:not(.hero){{margin:0 20px}}
.hero{{background:var(--pa);padding:22px;display:flex;align-items:center;gap:20px}}.app{{width:96px;height:96px;border-radius:22px;background:var(--f);display:grid;place-items:center}}
.lk{{display:flex;align-items:center;gap:8px}}.lk b{{font:600 34px IS;color:var(--t);letter-spacing:-.01em}}
.ui{{background:var(--pa);border-radius:14px;padding:14px;display:grid;gap:4px;justify-items:start}}.ui h3{{margin:4px 0 0;font-size:17px;color:var(--t)}}.ui p{{margin:0;color:var(--t);opacity:.75}}
.chip{{background:var(--f);color:#fff;border-radius:999px;padding:2px 10px;font-size:12px;font-weight:600}}
.ui button{{margin-top:8px;background:var(--p);color:#fff;border:0;border-radius:999px;padding:9px 16px;font:600 14px IS}}
.sws{{display:grid;grid-template-columns:1fr 1fr;gap:6px}}.sw{{display:flex;gap:6px;align-items:center;font-size:12.5px}}.sw i{{width:22px;height:22px;border-radius:6px;border:1px solid #0001}}.sw code{{color:#6b6b66;font-size:11px}}
.ck{{margin:0 20px;padding-left:18px;font-size:13px}}.ck .ok{{color:#0f7a4f}}.ck .bad{{color:#b42318}}h2{{font-size:16px}}.d{{color:#55555a}}
</style></head><body><h1>Convia · color, ronda 1</h1><p class="lead">Sobre el símbolo aprobado (E1b). Contraste calculado al generar (WCAG 2.2: 3:1 gráficos, 4.5:1 texto).</p><main>{cards}</main></body></html>'''
open(os.path.join(D, 'lamina.html'), 'w').write(html)
