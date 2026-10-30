# NisaData · color C aprobado (grafito + mandarina): los tres símbolos en su color, para elegir forma.
# Uso: python3 simbolos-c.py <carpeta de fuentes> → simbolos-c.html
import importlib.util, os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = sys.argv[1]
spec = importlib.util.spec_from_file_location('r1', os.path.join(H, 'gen.py')); R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
B, A = '#1F2532', '#FF8A1F'
def lock(sv): return f'<div class="lk"><div class="sm">{sv}</div><div><div class="wm"><b>Nisa</b>Data</div><div class="rs">de <b>Nisa Nabani</b></div></div></div>'
def tams(fn): return ''.join(f'<div style="width:{px}px;height:{px}px">{fn(B, A)}</div>' for px in (48, 32, 24, 16))
cards = ''.join(f'<div class="c"><h3>{k} · {n}</h3>{lock(fn(B, A))}<div class="row"><div class="app">{fn("#FFFFFF", A)}</div><div class="tam">{tams(fn)}</div></div>'
                f'<div class="osc">{lock(fn("#FFFFFF", A)).replace("<b>Nisa</b>Data", "<b>Nisa</b>Data")}</div><p>{i}</p></div>' for k, n, fn, i in R.SIM)
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700))
css = ff + f'''
*{{box-sizing:border-box}}body{{margin:0;background:#F2F4F8;color:{B};font:400 14px/1.5 Poppins,sans-serif;padding:32px}}
h1{{font:700 26px/1.2 Poppins;margin:0 0 4px}}.lead{{color:#535B70;max-width:860px;margin:0 0 24px}}
.g{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}.c{{background:#fff;border:1px solid #DFE3EC;border-radius:14px;padding:20px;display:flex;flex-direction:column;gap:16px;min-width:0}}
.c h3{{font:600 15px/1.3 Poppins;margin:0}}.c p{{margin:0;color:#535B70;font-size:13px}}
.lk{{display:flex;align-items:center;gap:12px}}.sm{{width:48px;height:48px;flex:none}}svg{{width:100%;height:100%;display:block}}
.wm{{font:400 32px/1 Poppins;letter-spacing:-.01em;color:{B}}}.wm b{{font-weight:700}}.rs{{font:500 11px/1 Poppins;color:#535B70;margin-top:4px}}.rs b{{color:{B}}}
.row{{display:flex;gap:18px;align-items:flex-end;flex-wrap:wrap}}.app{{width:64px;height:64px;border-radius:16px;background:{B};padding:12px}}.tam{{display:flex;gap:12px;align-items:flex-end}}
.osc{{background:{B};border-radius:10px;padding:16px}}.osc .wm,.osc .rs,.osc .rs b{{color:#fff}}
@media (max-width:1000px){{.g{{grid-template-columns:1fr}}}}@media (max-width:480px){{body{{padding:16px}}}}
'''
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaData símbolos</title><style>{css}</style><body>'
        '<h1>NisaData · símbolos en grafito y mandarina</h1><p class="lead">Color C aprobado. Cada símbolo con logotipo, ícono de app, tamaños de 48 a 16 px y sobre fondo oscuro. La célula mandarina es el acento: una sola por símbolo.</p>'
        f'<div class="g">{cards}</div></body></html>')
open(os.path.join(H, 'simbolos-c.html'), 'w').write(html); print('ok')
