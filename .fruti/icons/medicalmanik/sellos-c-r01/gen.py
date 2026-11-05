# Sellos · opción C · r01 (punto medio): pictograma de B + un latido (tramo corto de la línea de pulso) en cada producto.
# Pedido (2026-11-05): «sí, prepara el punto medio». Reutiliza la construcción de la opción B (../sellos-b-r01/gen.py, importada).
# Uso: python3 gen.py → svg/ y comparacion.html (A, B y C lado a lado)
import os, importlib.util, base64
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
s = importlib.util.spec_from_file_location('ob', os.path.join(M, 'sellos-b-r01/gen.py')); B = importlib.util.module_from_spec(s); s.loader.exec_module(B)
def latido(x0, x1, y, a=12):
    """Tramo plano, subida, bajada profunda y regreso: el mismo gesto de la M, en pequeño."""
    w = x1 - x0; p = lambda f: x0 + w * f
    return f'M{x0} {y} H{p(.30):.1f} L{p(.42):.1f} {y - a} L{p(.58):.1f} {y + a * .8:.1f} L{p(.70):.1f} {y} H{x1}'
C = {
 'Expediente': ('M24 36 A5 5 0 0 1 29 31 H42 L47 37 H71 A5 5 0 0 1 76 42 V69 A5 5 0 0 1 71 74 H29 A5 5 0 0 1 24 69 Z ' + latido(33, 67, 57, 9), ''),
 'Agenda': ('M29 33 H71 A5 5 0 0 1 76 38 V70 A5 5 0 0 1 71 75 H29 A5 5 0 0 1 24 70 V38 A5 5 0 0 1 29 33 Z M38 25 V39 M62 25 V39 ' + latido(33, 67, 59, 9), ''),
 'Compras': ('M32 24 H68 V77 L62 72 L56 77 L50 72 L44 77 L38 72 L32 77 Z M41 37 H59 ' + latido(40, 60, 54, 8), ''),
 'Farmacia': ('M50 26 V40 M50 60 V74 ' + latido(24, 76, 50, 11), ''),
 'Impulsa': ('M24 62 H34 L39 54 L45 68 L51 58 L74 37 M60 36 H75 V51', ''),
 'Grupos': ('M37 25 H70 A5 5 0 0 1 75 30 V58 M30 37 H58 A5 5 0 0 1 63 42 V70 A5 5 0 0 1 58 75 H30 A5 5 0 0 1 25 70 V42 A5 5 0 0 1 30 37 Z ' + latido(31, 57, 57, 8), ''),
 'Administración': (latido(26, 74, 51, 12), ''),
}
B.PICTO = C; B.GROSOR = {'Farmacia': 9}  # el latido pide el mismo trazo en todos; Farmacia baja de 14 a 9
ORDEN, ARCH = B.ORDEN, B.ARCH
if __name__ == '__main__':
    for p in ORDEN:
        open(os.path.join(D, 'svg', ARCH[p] + '.svg'), 'w').write(B.sello(p).replace('id="b-', 'id="c-').replace('#b-', '#c-'))
        open(os.path.join(D, 'svg', ARCH[p] + '-1tinta.svg'), 'w').write(B.sello(p, True).replace('id="b-', 'id="c-').replace('#b-', '#c-'))
    u = lambda path: 'data:image/svg+xml;base64,' + base64.b64encode(open(path, 'rb').read()).decode()
    F = {'A': lambda p: os.path.join(M, 'final/svg', ARCH[p] + '.svg'), 'B': lambda p: os.path.join(M, 'sellos-b-r01/svg', ARCH[p] + '.svg'), 'C': lambda p: os.path.join(D, 'svg', ARCH[p] + '.svg')}
    MADRE = u(os.path.join(M, 'final/svg/medicalmanik.svg')); tam = [80, 40, 24, 16]
    tira = lambda path: (lambda d: '<div class="t">' + ''.join(f'<img src="{d}" width="{z}" height="{z}" alt="">' for z in tam) + '</div>')(u(path))
    filas = ''.join(f'<tr><th scope="row"><b>{p}</b> Manik</th>' + ''.join(f'<td>{tira(F[k](p))}</td>' for k in 'ABC') + '</tr>' for p in ORDEN)
    barra = lambda k: '<div class="bar">' + f'<img src="{MADRE}" alt="" width="32" height="32"><span class="sep"></span>' + ''.join(f'<img src="{u(F[k](p))}" alt="{p}" width="28" height="28">' for p in ORDEN[:6]) + '</div>'
    sel = lambda k: '<div class="sel">' + ''.join(f'<div class="ti"><img src="{u(F[k](p))}" alt=""><span>{p}</span></div>' for p in ORDEN[:6]) + '</div>'
    mono = '<div class="mono">' + ''.join(f'<img src="{u(os.path.join(D, "svg", ARCH[p] + "-1tinta.svg"))}" alt="" width="44" height="44">' for p in ORDEN) + '</div>'
    EV = [('¿Cuántas M?', 'Siete (una por sello)', 'Una (el sello madre)', 'Una; en cada producto, un latido'),
          ('¿Se ve que son familia?', 'Muy claro: la misma M', 'Solo por cuadro y color', 'Sí: el latido se repite'),
          ('¿Dice qué hace cada producto?', 'Por el borde, pequeño', 'Muy claro: el dibujo', 'Claro: el dibujo'),
          ('A 16 px', 'El rasgo del borde casi no se ve', 'Se lee bien', 'El latido se pierde; queda el dibujo'),
          ('Riesgo', 'Repetición de la M', 'Íconos genéricos', 'Más detalle; Administración pierde el engrane')]
    ev = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in EV)
    HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sellos A, B y C</title>
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;600;700&display=swap" rel="stylesheet">
<style>:root{{--tinta:#14213D;--muted:#4A5674;--linea:#E1E6F0;--papel:#F7F8FB;--suave:#EEF1F7;color-scheme:light}}*{{box-sizing:border-box}}
body{{margin:0;background:var(--papel);color:var(--tinta);font:400 16px/1.55 "Atkinson Hyperlegible Next",system-ui,sans-serif;padding:0 16px}}h1,h2,h3{{font-family:Urbanist,sans-serif;margin:0}}h1{{font-size:clamp(28px,4.4vw,42px);font-weight:300;line-height:1.1}}h1 b{{font-weight:600}}h2{{font-size:22px;font-weight:600}}h3{{font-size:17px;font-weight:600}}p{{margin:0}}
.wrap{{max-width:1240px;margin:0 auto;padding:36px 0 80px;display:grid;gap:32px;grid-template-columns:minmax(0,1fr)}}.nota{{font-size:14px;line-height:20px;color:var(--muted)}}.cab{{display:grid;gap:12px;max-width:84ch}}
.tw{{overflow-x:auto;border:1px solid var(--linea);border-radius:18px;background:#fff}}table{{border-collapse:collapse;width:100%;min-width:900px}}th,td{{padding:12px 14px;border-bottom:1px solid var(--linea);text-align:left;vertical-align:middle}}thead th{{font:700 12px/16px "Atkinson Hyperlegible Next";letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:var(--suave)}}tbody th{{font:400 16px Urbanist;color:var(--muted);white-space:nowrap}}tbody th b{{color:var(--tinta);font-weight:600}}
.ev th{{font:600 15px "Atkinson Hyperlegible Next";color:var(--tinta);white-space:normal}}.ev td{{font-size:15px;line-height:22px}}
.t{{display:flex;align-items:flex-end;gap:10px}}
.tres{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}}.lam{{background:#fff;border:1px solid var(--linea);border-radius:18px;padding:16px;display:grid;gap:12px;min-width:0}}
.sel{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}}.ti{{display:grid;justify-items:center;gap:6px;padding:10px 4px;border-radius:12px;background:var(--papel);font:600 12px/16px "Atkinson Hyperlegible Next"}}.ti img{{width:40px;height:40px}}
.bar{{display:flex;align-items:center;gap:8px;padding:8px 10px;border:1px solid var(--linea);border-radius:12px;flex-wrap:wrap}}.sep{{width:1px;height:22px;background:var(--linea)}}
.mono{{display:flex;gap:14px;flex-wrap:wrap}}@media(max-width:900px){{.tres{{grid-template-columns:1fr}}}}</style></head><body><main class="wrap">
<header class="cab"><span class="nota">Sellos · opción C (punto medio) · propuesta</span><h1>A, B y el <b>punto medio</b></h1>
<p>C toma el dibujo de producto de B y convierte una de sus piezas en un latido: un tramo corto de la línea de pulso (plano, sube, baja hondo y regresa), el mismo gesto de la M en pequeño. La M completa solo vive en el sello madre; el latido recuerda de dónde viene cada producto.</p>
<p class="nota">Expediente y Agenda: el latido reemplaza las líneas y la palomita. Compras: una línea del ticket. Farmacia: el brazo horizontal de la cruz. Impulsa: la línea de tendencia empieza con un latido. Grupos: dentro de la tarjeta de enfrente. Administración: solo el latido (sin engrane), una propuesta a discutir.</p></header>
<section aria-labelledby="s1"><h2 id="s1">Los tres, producto por producto</h2><p class="nota">A 80, 40, 24 y 16 px. A es la vigente (con la M original).</p><div class="tw" tabindex="0" role="region" aria-label="A, B y C"><table><thead><tr><th scope="col">Producto</th><th scope="col">A · con la M</th><th scope="col">B · sin la M</th><th scope="col">C · con latido</th></tr></thead><tbody>{filas}</tbody></table></div></section>
<section aria-labelledby="s2"><h2 id="s2">En el selector y en la barra</h2><div class="tres">{"".join(f'<div class="lam"><h3>{t}</h3>{sel(k)}{barra(k)}</div>' for k, t in (("A", "A · con la M"), ("B", "B · sin la M"), ("C", "C · con latido")))}</div></section>
<section aria-labelledby="s3"><h2 id="s3">C a una tinta</h2><div class="lam">{mono}</div></section>
<section aria-labelledby="s4"><h2 id="s4">Comparación</h2><div class="tw" tabindex="0" role="region" aria-label="Comparación"><table class="ev"><thead><tr><th scope="col">Pregunta</th><th scope="col">A</th><th scope="col">B</th><th scope="col">C</th></tr></thead><tbody>{ev}</tbody></table></div>
<p class="nota">Lectura [inferencia]: C es la que mejor responde al comentario sin romper la familia. Su punto débil es el tamaño mínimo: a 16 px el latido se vuelve una raya y solo queda el dibujo, que sigue siendo legible. Conviene probar las tres con quien hizo el comentario y con dos o tres usuarios del selector.</p></section>
</main></body></html>'''
    open(os.path.join(D, 'comparacion.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
