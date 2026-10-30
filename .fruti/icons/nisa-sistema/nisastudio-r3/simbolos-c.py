# NisaStudio · color C aprobado (índigo → turquesa): los tres símbolos en su color, para elegir forma.
# Uso: python3 simbolos-c.py <carpeta de fuentes> → simbolos-c.html
import importlib.util, os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = sys.argv[1]
_a = sys.argv; sys.argv = [_a[0], F]
spec = importlib.util.spec_from_file_location('r1', os.path.join(H, '..', 'nisastudio-r1', 'gen.py')); R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
sys.argv = _a
C1, C2, W, AC = '#4F46E5', '#14B8A6', '#3730A3', '#FDE68A'
G = f'linear-gradient(135deg,{C1},{C2})'
def lock(sv, dark=False): return f'<div class="lk{" dk" if dark else ""}"><div class="sm">{sv}</div><div><div class="wm"><b>Nisa</b>Studio</div><div class="rs">de <b>Nisa Nabani</b></div></div></div>'
def tams(fn): return ''.join(f'<div style="width:{px}px;height:{px}px">{fn(W, C2)}</div>' for px in (48, 32, 24, 16))
cards = ''.join(f'<div class="c"><h3>{k} · {n}</h3>{lock(fn(W, C2))}<div class="row"><div class="app" style="background:{G}">{fn("#FFFFFF", AC)}</div><div class="tam">{tams(fn)}</div></div>'
                f'<div class="osc">{lock(fn("#FFFFFF", AC), True)}</div><p>{i}</p></div>' for k, n, fn, i in R.SIM)
css = R.css.replace('.big{', '.row{display:flex;gap:18px;align-items:flex-end;flex-wrap:wrap}.app{width:64px!important;height:64px!important;border-radius:16px!important;padding:11px!important}.tam{display:flex;gap:12px;align-items:flex-end}.osc{background:' + G + ';border-radius:10px;padding:16px}.dk{border-color:transparent!important}.dk .wm,.dk .rs,.dk .rs b{color:#fff!important}.wm{color:' + W + '}.rs b{color:' + W + '}.big{')
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaStudio símbolos</title><style>{css}</style><body>'
        '<h1>NisaStudio · símbolos en índigo y turquesa</h1><p class="lead">Color C aprobado. Cada símbolo con logotipo, ícono de app en degradado, tamaños de 48 a 16 px y sobre el degradado. El acento es una sola pieza en turquesa (o amarillo claro sobre el degradado).</p>'
        f'<div class="g">{cards}</div></body></html>')
open(os.path.join(H, 'simbolos-c.html'), 'w').write(html); print('ok')
