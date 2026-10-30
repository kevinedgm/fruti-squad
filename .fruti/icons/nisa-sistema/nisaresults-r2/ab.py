# NisaResults · A (azul real + pera) contra B (azul real + cian) en uso: encabezado del portal y página pública con gráfica de monitoreo.
# Uso: python3 ab.py <carpeta de fuentes> → ab.html
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = sys.argv[1]
AZ = '#052A76'
def sim(b, a):
    return (f'<svg viewBox="0 0 100 100" aria-hidden="true"><rect x="6" y="22" width="88" height="7" rx="3.5" fill="{b}"/><rect x="6" y="71" width="88" height="7" rx="3.5" fill="{b}"/>'
            f'<circle cx="22" cy="56" r="9" fill="{b}"/><circle cx="50" cy="46" r="11" fill="{a}"/><circle cx="78" cy="53" r="9" fill="{b}"/></svg>')
V = [6.9, 7.1, 7.4, 7.2, 7.0, 7.6, 7.3, 7.1, 8.7, 7.2, 7.4, 7.3]  # pH de ejemplo; óptimo 6.5–8.5
def graf(acc):
    W, Hh, L, T, B = 520, 200, 34, 12, 26; lo, hi = 6.0, 9.0
    y = lambda v: T + (hi - v) * (Hh - T - B) / (hi - lo); x = lambda i: L + i * (W - L - 12) / (len(V) - 1)
    s = f'<rect x="{L}" y="{y(8.5):.1f}" width="{W - L - 12}" height="{y(6.5) - y(8.5):.1f}" fill="#E3F1E4"/>'
    s += f'<rect x="{L}" y="{T}" width="{W - L - 12}" height="{y(8.5) - T:.1f}" fill="#FDE7E5"/><rect x="{L}" y="{y(6.5):.1f}" width="{W - L - 12}" height="{Hh - B - y(6.5):.1f}" fill="#FDE7E5"/>'
    s += ''.join(f'<text x="{L - 6}" y="{y(v) + 4:.1f}" text-anchor="end" font-size="11" fill="#646B80">{v}</text>' for v in (6.5, 8.5))
    s += '<path d="M' + ' L'.join(f'{x(i):.1f} {y(v):.1f}' for i, v in enumerate(V)) + f'" fill="none" stroke="{AZ}" stroke-width="2"/>'
    s += ''.join(f'<circle cx="{x(i):.1f}" cy="{y(v):.1f}" r="4.5" fill="{"#B42318" if v > 8.5 else (acc if i == len(V) - 1 else AZ)}" stroke="#fff" stroke-width="1.5"/>' for i, v in enumerate(V))
    return f'<svg viewBox="0 0 {W} {Hh}" style="width:100%;height:auto;display:block" role="img" aria-label="pH por mes; un punto fuera de rango">{s}</svg>'
def panel(k, n, acc):
    return (f'<div class="col"><h2>{k} · {n}</h2>'
            f'<div class="top" style="--acc:{acc}"><div class="lg"><div class="sm">{sim("#FFFFFF", acc)}</div><span><b>Nisa</b>Results</span></div><nav><a aria-current="page">Resultados</a><a>Informes</a><a>Página pública</a></nav></div>'
            f'<div class="pub"><span class="hotel">Hotel Las Palmas</span><h3>Alberca principal</h3><p class="cat">Agua de uso y consumo humano · última muestra 28 oct 2026</p>'
            f'<div class="par"><div><b>pH</b><span>Qué tan ácida o alcalina es el agua.</span></div><span class="ok">Óptimo · 7.3</span></div>{graf(acc)}'
            f'<p class="ley"><i style="background:#E3F1E4"></i>Rango óptimo 6.5–8.5 <i style="background:#FDE7E5"></i>Fuera de rango <i style="background:{acc};border-radius:50%"></i>Último análisis</p>'
            f'<div class="sello"><div class="sm2">{sim(AZ, acc)}</div><span>Analizada por <b>Nisa Nabani</b> · laboratorio</span></div></div></div>')
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700))
css = ff + f'''
*{{box-sizing:border-box}}body{{margin:0;background:#F2F4F8;color:#141B33;font:400 14px/1.5 Poppins,sans-serif;padding:32px}}
h1{{font:700 24px/1.2 Poppins;margin:0 0 4px}}.lead{{color:#535B70;margin:0 0 20px;max-width:860px}}.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}}.col{{min-width:0;display:grid;gap:12px}}
h2{{font:600 16px Poppins;margin:0}}.top{{background:{AZ};border-radius:12px;padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}}
.lg{{display:flex;align-items:center;gap:10px;color:#fff;font:400 20px Poppins}}.lg b{{font-weight:700}}.sm{{width:30px;height:30px}}.sm svg,.sm2 svg{{width:100%;height:100%;display:block}}
nav{{display:flex;gap:4px}}nav a{{color:#C9D3EA;font:500 13px Poppins;padding:6px 10px;border-radius:8px;position:relative}}nav a[aria-current]{{color:#fff;background:rgba(255,255,255,.1)}}nav a[aria-current]::after{{content:"";position:absolute;left:10px;right:10px;bottom:-1px;height:3px;border-radius:3px;background:var(--acc)}}
.pub{{background:#fff;border:1px solid #DFE3EC;border-radius:16px;padding:20px;display:grid;gap:10px}}.hotel{{font:600 13px Poppins;color:#535B70;letter-spacing:.04em;text-transform:uppercase}}h3{{font:600 22px Poppins;margin:0}}.cat{{margin:0;color:#535B70;font-size:13px}}
.par{{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;border-top:1px solid #EEF1F6;padding-top:10px}}.par b{{display:block}}.par span{{font-size:13px;color:#535B70}}
.ok{{background:#E3F1E4;color:#1E5A22!important;font-weight:600;border-radius:999px;padding:3px 10px;white-space:nowrap}}
.ley{{display:flex;gap:10px;align-items:center;font-size:12px;color:#535B70;margin:0;flex-wrap:wrap}}.ley i{{width:12px;height:12px;display:inline-block;border-radius:3px}}
.sello{{display:flex;align-items:center;gap:10px;border-top:1px solid #EEF1F6;padding-top:12px;font-size:13px;color:#535B70}}.sello b{{color:{AZ}}}.sm2{{width:26px;height:26px}}
@media (max-width:900px){{.g{{grid-template-columns:1fr}}}}@media (max-width:480px){{body{{padding:16px}}}}
'''
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaResults A contra B</title><style>{css}</style><body>'
        '<h1>NisaResults · A contra B en uso</h1><p class="lead">Arriba, el encabezado del portal del cliente. Abajo, la página pública del QR con la gráfica de monitoreo (zona verde = óptimo, roja = fuera). Fíjate en el acento junto al verde: ahí está la diferencia. Datos de ejemplo.</p>'
        f'<div class="g">{panel("A", "Azul real + pera", "#C2D225")}{panel("B", "Azul real + cian", "#00B4D8")}</div></body></html>')
open(os.path.join(H, 'ab.html'), 'w').write(html); print('ok')
