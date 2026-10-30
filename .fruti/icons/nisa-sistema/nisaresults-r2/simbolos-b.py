# NisaResults · color B aprobado (azul real + cian): los tres símbolos en su color, para elegir forma.
# Uso: python3 simbolos-b.py <carpeta de fuentes> → simbolos-b.html
import importlib.util, os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = sys.argv[1]
spec = importlib.util.spec_from_file_location('r1', os.path.join(H, '..', 'nisaresults-r1', 'gen.py')); R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
B, A = '#052A76', '#00B4D8'
def lock(sv, dark=False): return f'<div class="lk{" dk" if dark else ""}"><div class="sm">{sv}</div><div><div class="wm"><b>Nisa</b>Results</div><div class="rs">de <b>Nisa Nabani</b></div></div></div>'
def tams(fn): return ''.join(f'<div style="width:{px}px;height:{px}px">{fn(B, A)}</div>' for px in (48, 32, 24, 16))
cards = ''.join(f'<div class="c"><h3>{k} · {n}</h3>{lock(fn(B, A))}<div class="row"><div class="app">{fn("#FFFFFF", A)}</div><div class="tam">{tams(fn)}</div></div>'
                f'<div class="osc">{lock(fn("#FFFFFF", A), True)}</div><div class="sello"><div class="s2">{fn(B, A)}</div><span>Analizada por <b>Nisa Nabani</b> · laboratorio</span></div><p>{i}</p></div>' for k, n, fn, i in R.SIM)
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700))
css = ff + f'''
*{{box-sizing:border-box}}body{{margin:0;background:#F2F4F8;color:#141B33;font:400 14px/1.5 Poppins,sans-serif;padding:32px}}
h1{{font:700 26px/1.2 Poppins;margin:0 0 4px;color:{B}}}.lead{{color:#535B70;max-width:880px;margin:0 0 24px}}
.g{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}.c{{background:#fff;border:1px solid #DFE3EC;border-radius:14px;padding:20px;display:flex;flex-direction:column;gap:16px;min-width:0}}
.c h3{{font:600 15px/1.3 Poppins;margin:0}}.c p{{margin:0;color:#535B70;font-size:13px}}
.lk{{display:flex;align-items:center;gap:12px}}.sm{{width:48px;height:48px;flex:none}}svg{{width:100%;height:100%;display:block}}
.wm{{font:400 30px/1 Poppins;letter-spacing:-.01em;color:{B}}}.wm b{{font-weight:700}}.rs{{font:500 11px/1 Poppins;color:#535B70;margin-top:4px}}.rs b{{color:{B}}}
.row{{display:flex;gap:18px;align-items:flex-end;flex-wrap:wrap}}.app{{width:64px;height:64px;border-radius:16px;background:{B};padding:11px}}.tam{{display:flex;gap:12px;align-items:flex-end}}
.osc{{background:{B};border-radius:10px;padding:16px}}.dk .wm,.dk .rs,.dk .rs b{{color:#fff}}
.sello{{display:flex;align-items:center;gap:10px;border:1px dashed #C9CED8;border-radius:10px;padding:10px 12px;font-size:13px;color:#535B70}}.sello b{{color:{B}}}.s2{{width:26px;height:26px;flex:none}}
@media (max-width:1000px){{.g{{grid-template-columns:1fr}}}}@media (max-width:480px){{body{{padding:16px}}}}
'''
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaResults símbolos</title><style>{css}</style><body>'
        '<h1>NisaResults · símbolos en azul real y cian</h1><p class="lead">Color B aprobado. Cada símbolo con logotipo, ícono de app, tamaños de 48 a 16 px, sobre azul real y como sello en la página pública. La célula cian es el acento: una sola por símbolo.</p>'
        f'<div class="g">{cards}</div></body></html>')
open(os.path.join(H, 'simbolos-b.html'), 'w').write(html); print('ok')
