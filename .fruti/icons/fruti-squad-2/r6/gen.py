# Fruti Squad · ronda 6: tres sistemas ABSTRACTOS (usuario: «me gustarían más abstractas, no literales»).
# La fruta queda solo como pista (color, suavidad); el rol de cada agente se dice con geometría. Squad + cinco integrantes.
import os, math
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
COL = {'squad': INK, 'kiwi': '#2f9e4f', 'lima': '#a8c81e', 'coco': '#c97a3a', 'bruno': '#2f6fe0', 'mora': '#7b3fa0'}
N = [('squad', 'Fruti Squad', 'Workflow Pack', 'orquestar'), ('kiwi', 'Kiwi', 'UX Architect', 'organizar'), ('lima', 'Lima', 'Design System Governance', 'validar'),
     ('coco', 'Coco', 'UI Audit', 'inspeccionar'), ('bruno', 'Bruno', 'Implementation', 'conectar'), ('mora', 'Mora', 'Documentation', 'catalogar')]
def svg(b): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b}</svg>'
# A · Átomos: el mismo punto (la evidencia), distinta molécula por rol
def dot(x, y, r, c): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
def A(k, c):
    if k == 'squad': return ''.join(dot(32 + 20 * math.cos(math.radians(-90 + i * 72)), 32 + 20 * math.sin(math.radians(-90 + i * 72)), 6.5, c) for i in range(5)) + dot(32, 32, 8, c)
    if k == 'kiwi': return ''.join(dot(x, y, 9, c) for x in (20, 44) for y in (20, 44))
    if k == 'lima': return dot(12, 32, 6.5, c) + dot(27, 32, 6.5, c) + f'<circle cx="48" cy="32" r="11" stroke="{c}" stroke-width="6"/>' + dot(48, 32, 4, c)
    if k == 'coco': return f'<circle cx="32" cy="32" r="23" stroke="{c}" stroke-width="6.5"/>' + dot(39, 26, 7, c)
    if k == 'bruno': return f'<path d="M19 45L45 19" stroke="{c}" stroke-width="7" stroke-linecap="round"/>' + dot(17, 47, 10, c) + dot(47, 17, 10, c)
    if k == 'mora': return dot(32, 13, 8.5, c) + dot(32, 32, 7.5, c) + dot(32, 49, 6.5, c) + dot(16, 32, 4.5, c) + dot(48, 32, 4.5, c)
# B · Una línea: cada agente es un solo trazo, mismo grosor, puntas redondas
def B(k, c):
    st = f'stroke="{c}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
    d = {'squad': 'M10 32c0-8 6-13 12-13 11 0 9 26 20 26 6 0 12-5 12-13s-6-13-12-13c-11 0-9 26-20 26-6 0-12-5-12-13z',
         'kiwi': 'M13 16h38v16H13v16h38',
         'lima': 'M14 52V28a18 18 0 0 1 36 0v24M14 40h36',
         'coco': 'M33.4 28.3 L33.9 28.2 L34.4 28.3 L34.8 28.4 L35.3 28.5 L35.8 28.7 L36.3 29.0 L36.8 29.3 L37.2 29.7 L37.6 30.1 L37.9 30.6 L38.3 31.2 L38.5 31.8 L38.7 32.4 L38.8 33.1 L38.9 33.8 L38.9 34.6 L38.8 35.3 L38.6 36.1 L38.4 36.8 L38.0 37.6 L37.6 38.3 L37.1 39.0 L36.5 39.6 L35.8 40.2 L35.1 40.7 L34.2 41.2 L33.4 41.6 L32.4 41.9 L31.5 42.1 L30.5 42.2 L29.4 42.2 L28.4 42.1 L27.3 41.9 L26.3 41.6 L25.2 41.1 L24.2 40.6 L23.3 39.9 L22.4 39.2 L21.6 38.3 L20.8 37.3 L20.1 36.3 L19.6 35.2 L19.1 34.0 L18.8 32.7 L18.6 31.4 L18.5 30.1 L18.5 28.8 L18.7 27.4 L19.0 26.0 L19.5 24.7 L20.1 23.4 L20.8 22.1 L21.7 20.9 L22.7 19.8 L23.8 18.8 L25.0 17.9 L26.4 17.1 L27.8 16.4 L29.3 15.8 L30.9 15.4 L32.5 15.2 L34.1 15.1 L35.8 15.2 L37.5 15.4 L39.2 15.9 L40.8 16.5 L42.4 17.2 L43.9 18.1 L45.4 19.2 L46.7 20.4 L47.9 21.8 L49.0 23.3 L50.0 24.9 L50.8 26.7 L51.4 28.5 L51.9 30.4 L52.2 32.3 L52.2 34.3 L52.1 36.3 L51.8 38.3 L51.3 40.3 L50.6 42.2 L49.7 44.1 L48.6 45.9 L47.3 47.6 L45.8 49.2 L44.2 50.6 L42.5 51.9 L40.5 53.0 L38.5 54.0 L36.4 54.7 L34.2 55.2 L31.9 55.5 L29.6 55.6 L27.3 55.5 L25.0 55.1 L22.7 54.5 L20.4 53.7 L18.3 52.6 L16.2 51.4',
         'bruno': 'M12 50c0-16 14-18 20-18s20-2 20-18',
         'mora': 'M12 16h36a8 8 0 0 1 0 16H20a8 8 0 0 0 0 16h32'}[k]
    extra = f'<circle cx="12" cy="50" r="6" fill="{c}"/><circle cx="52" cy="14" r="6" fill="{c}"/>' if k == 'bruno' else ''
    return f'<path d="{d}" {st}/>' + extra
# C · Formas suaves: siluetas orgánicas distintas; el squad es la superposición (colaborar = mezclar colores)
def blob(k, c, op=''):
    s = {'kiwi': f'<ellipse cx="32" cy="32" rx="27" ry="20" fill="{c}"{op}/>',
         'lima': f'<path d="M32 7c4 0 7 2 9 6l15 27c4 8-1 16-10 16H18c-9 0-14-8-10-16l15-27c2-4 5-6 9-6z" fill="{c}"{op}/>',
         'coco': f'<path d="M32 6c20 0 26 6 26 26s-6 26-26 26S6 52 6 32 12 6 32 6z" fill="{c}"{op}/>',
         'bruno': f'<rect x="18" y="1" width="28" height="62" rx="14" transform="rotate(45 32 32)" fill="{c}"{op}/>',
         'mora': ''.join(f'<circle cx="{32+13*math.cos(math.radians(a))}" cy="{32+13*math.sin(math.radians(a))}" r="15" fill="{c}"{op}/>' for a in (0, 90, 180, 270))}
    return s[k]
def C(k, c):
    if k == 'squad':
        op = ' style="mix-blend-mode:multiply"'
        return (f'<g transform="translate(6 8) scale(.55)">{blob("kiwi", COL["kiwi"], op)}</g><g transform="translate(23 5) scale(.55)">{blob("lima", COL["lima"], op)}</g>'
                f'<g transform="translate(8 24) scale(.55)">{blob("coco", COL["coco"], op)}</g><g transform="translate(23 23) scale(.55)">{blob("mora", COL["mora"], op)}</g>')
    return blob(k, c)
SIS = [
 ('A', 'Átomos', 'Todos están hechos del mismo átomo: el punto, que es la evidencia que cada agente entrega. Cambia la molécula: cuatro en retícula (organiza), una fila que pasa por un anillo (valida), un punto dentro de un lente (inspecciona), dos puntos unidos (conecta), una columna que decrece (cataloga). El squad es el núcleo con sus cinco.', A,
  'Muy coherente como sistema y fácil de extender (Mango y Uva serían otra molécula). Abstracto pero con significado.', 'Los puntos son un recurso visto en marcas de tecnología; el valor está en las combinaciones, que hay que cuidar.'),
 ('B', 'Una línea', 'Cada agente es un solo trazo con el mismo grosor: una serpentina de filas (organiza), un arco con barra como compuerta (valida), una espiral hacia el centro (inspecciona), una curva que une dos extremos (conecta), una cinta doblada como páginas (cataloga). El squad es un lazo continuo: todo el flujo sin cortes.', B,
  'Elegante y de firma, como un monograma dibujado a mano; se ve muy bien en una sola tinta y en animación (el trazo se dibuja).', 'Los trazos finos pierden fuerza a 16 px; hay que probar el grosor.'),
 ('C', 'Formas suaves', 'Siluetas orgánicas y redondeadas que evocan fruta sin dibujarla: óvalo, triángulo suave, cuadro redondo, cápsula y trébol. El squad es la superposición de varias formas, que al cruzarse mezclan color: colaborar es mezclar.', C,
  'La más cálida y contemporánea; muy reconocible por silueta y color; el squad cuenta la colaboración de forma visual.', 'Las formas solas no dicen el rol; el significado se apoya en el nombre del producto.'),
]
def card(k, t, i, F, a, r):
    fila = ''.join(f'<figure class="p">{svg(F(id_, COL[id_]))}<figcaption><b>{n}</b><span>{v}</span></figcaption></figure>' for id_, n, rol, v in N)
    tinta = ''.join(f'<span class="pq">{svg(F(id_, INK) if id_ != "squad" or k != "C" else F(id_, INK))}</span>' for id_, n, rol, v in N)
    dk = ''.join(svg(F(id_, "#f5f5f2" if id_ == "squad" else COL[id_])) for id_, n, rol, v in N)
    lk = ''.join(f'<div class="lk">{svg(F(id_, COL[id_]))}<span><b>{n}</b><i>{rol}</i><small>{"de Fruti Squad" if id_ != "squad" else "Kiwi · Lima · Coco · Bruno · Mora"}</small></span></div>' for id_, n, rol, v in (N[3], N[0]))
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{t}</h2></header><p class="id">{i}</p><div class="fila">{fila}</div>'
            f'<div class="row"><span class="lb">A 16 px</span>{tinta}<span class="dkb">{dk}</span></div><div class="lks">{lk}</div>'
            f'<p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.c{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:22px;display:grid;gap:14px;min-width:0}}.c header{{display:flex;gap:10px;align-items:center}}
.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font-size:19px;margin:0}}.id{{margin:0;color:#3a3a37}}
.fila{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px}}.p{{margin:0;display:grid;justify-items:center;gap:8px;text-align:center}}.p svg{{width:100%;max-width:96px;height:auto}}
.p figcaption{{display:grid;line-height:1.25}}.p b{{font-size:15px}}.p span{{font-size:12.5px;color:#4b4b47}}
.row{{display:flex;flex-wrap:wrap;gap:8px;align-items:center}}.lb{{font-size:12px;font-weight:700;color:#6b6b66}}.pq{{display:inline-grid;place-items:center;width:28px;height:28px;border:1px solid #ececE6;border-radius:7px}}.pq svg{{width:16px;height:16px}}
.dkb{{display:inline-flex;gap:8px;background:{INK};border-radius:10px;padding:8px;margin-left:8px}}.dkb svg{{width:30px;height:30px}}
.lks{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}}.lk{{display:flex;align-items:center;gap:14px;border:1px solid #ececE6;border-radius:14px;padding:12px 16px;min-width:0}}.lk svg{{width:56px;height:56px;flex:none}}
.lk span{{display:grid;line-height:1.15;min-width:0}}.lk b{{font-size:22px}}.lk i{{font-style:normal;color:#3f3f3c}}.lk small{{font-size:12px;color:#6b6b66}}
.pr{{margin:0;font-size:14px;color:#4b4b47}}.pr b{{color:{INK}}}
@media (max-width:900px){{.fila{{grid-template-columns:repeat(3,minmax(0,1fr))}}.lks{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · abstractas</title>'
        f'<style>{css}</style></head><body><main><h1>Fruti Squad · tres sistemas abstractos (ronda 6)</h1>'
        '<p class="lead">Nada literal: la fruta queda solo como pista en el color y en lo redondeado. El rol de cada agente lo dice la geometría. Cada sistema con el squad y sus cinco integrantes, a 16 px en una tinta, sobre oscuro y como producto.</p>'
        f'{"".join(card(*x) for x in SIS)}</main></body></html>')
open(os.path.join(H, 'abstractas.html'), 'w').write(html); print('ok')
