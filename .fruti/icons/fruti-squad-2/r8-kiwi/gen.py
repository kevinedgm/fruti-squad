# Fruti Squad · ronda 8: uno por uno. Kiwi (Structure). Usuario: «vamos uno por uno, iniciemos con Kiwi» + su descripción completa.
# Sistema Átomos: punto (evidencia), enlace (barra), anillo. Seis opciones, cada una ligada a una línea concreta de lo que Kiwi hace.
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
def svg(b, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b.replace("§", c)}</svg>'
def d(x, y, r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="§"/>'
def o(x, y, r, w=4): return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="§" stroke-width="{w}"/>'
def bar(p, w=4.5): return f'<path d="{p}" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
K = [
 ('Esqueleto', '«Estructura antes que apariencia» · hierarchy · what appears first',
  'Kiwi trabaja con huecos, no con relleno: los anillos son las regiones sin estilo todavía (un wireframe). Solo un punto va lleno: lo que aparece primero.',
  'Es el único integrante que usaría anillos vacíos: dice «aún sin apariencia», que es exactamente su límite.',
  d(32, 14, 8.5) + o(21, 34, 6.5) + o(43, 34, 6.5) + o(14, 52, 4.5, 3.5) + o(32, 52, 4.5, 3.5) + o(50, 52, 4.5, 3.5)),
 ('Jerarquía', 'hierarchy · what appears first',
  'Uno grande, dos medianos, tres chicos: el orden de importancia de una pantalla.', 'Muy claro; pero es solo una de sus habilidades.',
  d(32, 13, 9) + d(21, 33, 6.5) + d(43, 33, 6.5) + d(14, 51, 4.5) + d(32, 51, 4.5) + d(50, 51, 4.5)),
 ('Regiones', 'screen architecture · which regions the interface needs',
  'Una región principal y dos secundarias: la arquitectura de una pantalla vista desde arriba.', 'El más simple y fuerte a 16 px; puede leerse como un «●:» genérico.',
  d(22, 32, 14) + d(48, 20, 7.5) + d(48, 44, 7.5)),
 ('Flujo', 'user flow · which actions exist',
  'Puntos unidos con una bifurcación: el recorrido del usuario y la decisión que lo divide.', 'Cuenta el user flow, pero es casi idéntico al icono universal de «compartir»: descartarlo o cambiarle la geometría.',
  bar('M12 32H28M28 32L44 16M28 32L44 48') + d(12, 32, 6.5) + d(28, 32, 6.5) + d(46, 15, 7) + d(46, 49, 7)),
 ('Reacomodo', 'compact, medium, expanded · how the experience reorganizes',
  'Los mismos tres puntos en fila y en columna: el contenido se reorganiza según el tamaño.', 'El más específico de Kiwi (adaptativo); a 16 px pesa más la forma de «L» que la idea.',
  d(12, 14, 6) + d(28, 14, 6) + d(44, 14, 6) + bar('M44 24v4') + d(44, 36, 5) + d(44, 48, 5) + d(44, 60, 3.2)),
 ('Estados', 'required states',
  'Un mismo elemento en sus estados: lleno, vacío, en carga y deshabilitado.', 'Muestra la cobertura de estados; como símbolo de marca se ve técnico.',
  d(18, 18, 9) + o(46, 18, 8) + f'<circle cx="18" cy="46" r="8" stroke="§" stroke-width="4" stroke-dasharray="6 4"/>' + d(46, 46, 4)),
]
cards = ''.join(f'''<section class="c"><span class="n">{i+1}</span>{svg(b)}<div><h2>{t}</h2><p class="sk">{sk}</p><p>{idea}</p><p class="pr">{nota}</p>
<div class="sm"><span class="pq">{svg(b)}</span><span class="pq p24">{svg(b)}</span><span class="pq dk">{svg(b, "#fff")}</span></div></div></section>''' for i, (t, sk, idea, nota, b) in enumerate(K))
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.c{{position:relative;background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;grid-template-columns:120px minmax(0,1fr);gap:18px;align-items:start}}
.c>svg{{width:120px;height:120px}}.n{{position:absolute;top:12px;left:14px;font-size:12px;font-weight:800;color:#8a8a84}}h2{{font-size:19px;margin:0}}
.sk{{margin:2px 0 6px;font:600 12px ui-monospace,monospace;color:#6b6b66}}.c p{{margin:0 0 6px;font-size:14px;color:#3a3a37}}.c p.pr{{color:#6b6b66}}
.sm{{display:flex;gap:8px;margin-top:8px}}.pq{{display:inline-grid;place-items:center;width:30px;height:30px;border:1px solid #ececE6;border-radius:8px}}.pq svg{{width:16px;height:16px}}.pq.p24{{width:38px;height:38px}}.pq.p24 svg{{width:24px;height:24px}}.pq.dk{{background:{INK};border-color:{INK}}}
@media (max-width:860px){{.g{{grid-template-columns:1fr}}}}@media (max-width:440px){{.c{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Kiwi · símbolo</title>'
        f'<style>{css}</style></head><body><main><h1>Kiwi · Structure · seis opciones de símbolo</h1>'
        '<p class="lead">Uno por uno, empezando por Kiwi. Cada opción sale de una línea concreta de lo que Kiwi hace (en gris, la habilidad de su descripción). Todas usan las piezas del sistema Átomos: punto, enlace y anillo. En tinta; el color se define al final, cuando estén los seis.</p>'
        f'<div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'kiwi.html'), 'w').write(html); print('ok')
