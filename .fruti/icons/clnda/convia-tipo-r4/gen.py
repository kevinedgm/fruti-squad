# Convia · tipografía ronda 4: primarias elegantes + Instrument Sans, en una pantalla real de la app.
# Uso: python3 gen.py <fuentes> <fuentes2>  (fuentes2: Gloock.woff2; fuentes: Fraunces, Newsreader, InstrumentSans)
import sys, os, re, pathlib
F, F2 = sys.argv[1], sys.argv[2]
D = os.path.dirname(os.path.abspath(__file__))
path = re.search(r'<path d="([^"]+)"', open(os.path.join(D, '..', 'convia-r7', 'E1b.svg')).read()).group(1)
B = dict(fondo='#1f4d3a', principal='#d42a66', acento='#ffc53d', apoyo='#3f8f6b', papel='#f6f3ea', tinta='#15241d')
def sym(c, s): return f'<svg viewBox="0 0 200 200" width="{s}" height="{s}" aria-hidden="true"><path d="{path}" fill="{c}"/></svg>'
u = lambda d, f: pathlib.Path(os.path.join(d, f)).resolve().as_uri()
faces = (f'@font-face{{font-family:Gloock;src:url("{u(F2, "Gloock.woff2")}")}}'
         f'@font-face{{font-family:Fraunces;src:url("{u(F, "Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf")}");font-weight:100 900}}'
         f'@font-face{{font-family:Newsreader;src:url("{u(F, "Newsreader%5Bopsz,wght%5D.ttf")}");font-weight:200 800}}'
         f'@font-face{{font-family:"Instrument Sans";src:url("{u(F, "InstrumentSans[wdth,wght].ttf")}");font-weight:400 700}}')
PARES = [('A', 'Gloock', 400, 'normal', 'Serif de alto contraste: elegante y editorial, con curvas que le dan carácter propio.'),
         ('B', 'Fraunces', 500, '"SOFT" 0, "WONK" 0, "opsz" 72', 'Serif clásica, sobria y precisa: pulcritud de buena revista.'),
         ('C', 'Newsreader', 500, '"opsz" 72', 'Serif de lectura, fina y tranquila: elegancia discreta.')]
ITEMS = [('Taller de barro bruñido', 'Taller · para ir solo', 'Sáb 11:00', '$650', '4 lugares'),
         ('Café Tres Patios', 'Café · Jalatlaco', 'Abierto hasta 21:00', '$$', '350 m'),
         ('Hotel Patio de Luz', 'Hotel boutique · Centro', 'Desde', '$2,480', 'por noche')]
def screen(pri, w, v):
    cards = ''.join(f'''<div class="card"><div class="img"></div><div><p class="cat">{c}</p><h3>{n}</h3>
<p class="meta"><span>{h}</span><b class="num">{pr}</b><span>{x}</span></p></div></div>''' for n, c, h, pr, x in ITEMS)
    return f'''<div class="phone" style="--pri:'{pri}';--pw:{w};--pv:{v};--sec:'Instrument Sans'"><header>{sym(B['acento'], 26)}<b class="logo">Convia</b></header>
<div class="body"><h1>¿Qué hacemos hoy?</h1><p class="sub">Lo que vale la pena en Oaxaca, escogido por gente de aquí.</p>
<div class="chips"><span class="on">Hoy</span><span>Para ir solo</span><span>Talleres</span><span>Cafés</span></div>{cards}
<button>Ver todos los planes</button></div></div>'''
cols = ''.join(f'<section><h2>{k} · {p} + Instrument Sans</h2><p class="d">{d}</p>{screen(p, w, v)}</section>' for k, p, w, v, d in PARES)
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Convia · tipografía r3</title><style>{faces}
body{{margin:0;padding:32px;background:#e9e8e3;color:#1b1b1d;font:15px/1.45 "Instrument Sans",system-ui,sans-serif}}h1.t{{margin:0 0 4px;font-size:26px}}.lead{{margin:0 0 20px;color:#55555a}}
main{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}section h2{{font-size:16px;margin:0}}.d{{margin:4px 0 12px;color:#55555a;min-height:42px}}
.phone{{width:360px;background:{B['papel']};border-radius:28px;overflow:hidden;border:1px solid #d9d6cc;font-family:var(--sec),sans-serif;color:{B['tinta']}}}
.phone header{{background:{B['fondo']};padding:16px 18px;display:flex;align-items:center;gap:8px}}.logo{{font-family:var(--pri);font-weight:var(--pw);font-variation-settings:var(--pv);font-size:25px;color:#fff;letter-spacing:.005em}}
.body{{padding:18px;display:grid;gap:12px}}.body h1{{font-family:var(--pri);font-weight:var(--pw);font-variation-settings:var(--pv);font-size:32px;line-height:1.08;margin:0;letter-spacing:-.01em}}.sub{{margin:0;font-size:15px;color:#3d4a43}}
.chips{{display:flex;gap:6px;flex-wrap:wrap}}.chips span{{border:1px solid {B['tinta']};border-radius:999px;padding:4px 11px;font-size:13px;font-weight:600}}.chips .on{{background:{B['tinta']};color:#fff}}
.card{{background:#fff;border-radius:16px;padding:10px;display:grid;grid-template-columns:76px 1fr;gap:12px;align-items:center}}.img{{height:76px;border-radius:12px;background:linear-gradient(135deg,{B['apoyo']},{B['fondo']})}}
.cat{{margin:0;font-size:11.5px;font-weight:600;color:{B['principal']};text-transform:uppercase;letter-spacing:.04em}}.card h3{{margin:2px 0;font-size:16.5px;font-weight:600}}
.meta{{margin:0;font-size:13px;display:flex;gap:8px;color:#3d4a43}}.num{{font-variant-numeric:tabular-nums;color:{B['tinta']}}}
.body button{{background:{B['principal']};color:#fff;border:0;border-radius:999px;padding:13px;font-family:"Instrument Sans",sans-serif;font-weight:600;font-size:15px}}
</style></head><body><h1 class="t">Convia · primarias elegantes</h1><p class="lead">Tres primarias con más elegancia y pulcritud, todas con Instrument Sans como secundaria (más seria que Figtree). Misma pantalla, mismos colores. Nombres de negocios de ejemplo (ficticios).</p><main>{cols}</main></body></html>'''
open(os.path.join(D, 'lamina.html'), 'w').write(html)
