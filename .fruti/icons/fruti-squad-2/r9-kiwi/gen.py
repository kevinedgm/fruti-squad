# Fruti Squad · ronda 9 · Kiwi. Usuario: «siento que no representa Kiwi UX Architect». Lectura: faltaba el oficio de ARQUITECTO
# (plano, estructura que sostiene, distribución de espacios, medidas por tamaño). Mismo sistema Átomos: punto (evidencia), enlace, anillo.
import os, math
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
def svg(b, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b.replace("§", c)}</svg>'
def d(x, y, r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="§"/>'
def o(x, y, r, w=4): return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="§" stroke-width="{w}"/>'
def ln(p, w=4.5, extra=''): return f'<path d="{p}" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{extra}/>'
def arco():
    out = ''
    for i in range(5):
        a = math.radians(180 + i * 45); x, y = 32 + 24 * math.cos(a), 48 + 24 * math.sin(a)
        out += d(round(x, 1), round(y, 1), 9 if i == 2 else 6)
    return out + ln('M8 55v6M56 55v6', 6)
K = [
 ('Clave', 'La piedra clave de un arco: la pieza que sostiene toda la estructura. Kiwi define la estructura que sostiene a los demás.',
  'Arquitectura pura, reconocible y propia del sistema de puntos; el punto mayor es la decisión que todo sostiene.', 'Fuera de contexto puede leerse como un arcoíris o un semicírculo de puntos; la base y el punto mayor arriba son lo que lo hacen «arco».', arco()),
 ('Plano', 'Puntos sobre los ejes de un plano: el arquitecto ubica cada pieza en su retícula antes de construir.',
  'Dice «plano», «retícula» y «ubicar» sin ser un icono común; los ejes son el guiño de arquitecto.', 'Las líneas finas pierden fuerza en tamaños pequeños.',
  ln('M6 20h52M6 44h52M20 6v52M44 6v52', 2.6, ' stroke-dasharray="3 4"') + d(20, 20, 7) + d(44, 20, 4.5) + d(20, 44, 4.5) + o(44, 44, 7)),
 ('Planta', 'La planta de un espacio: muros con sus aberturas y un punto en la entrada. La arquitectura de una pantalla, vista desde arriba.',
  'La metáfora más directa de «arquitectura de información»: espacios, recorridos y por dónde se entra.', 'En pequeño se parece a una puerta o un armario.',
  ln('M8 8h20M36 8h20v48H36M28 56H8V8M32 8v22M32 38v18') + d(20, 56, 5.5) + d(44, 30, 5)),
 ('Tres tamaños', 'El mismo contenido en tres marcos: compact, medium y expanded. El punto se queda en su lugar: la estructura que Kiwi decide sobrevive a cada tamaño.',
  'El único que cuenta lo adaptativo, que es lo más específico de un UX Architect.', 'Los marcos anidados recuerdan a una diana o a iconos de «capas»; el punto fijo es lo que lo diferencia.',
  '<rect x="4" y="4" width="56" height="56" rx="12" stroke="§" stroke-width="3.5"/><rect x="13" y="13" width="38" height="38" rx="9" stroke="§" stroke-width="3.5"/><rect x="21" y="21" width="22" height="22" rx="6" stroke="§" stroke-width="3.5"/>' + d(32, 32, 5.5)),
]
cards = ''.join(f'''<section class="c"><span class="n">{i+1}</span>{svg(b)}<div><h2>{t}</h2><p>{idea}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p>
<div class="sm"><span class="pq">{svg(b)}</span><span class="pq p24">{svg(b)}</span><span class="pq dk">{svg(b, "#fff")}</span><span class="lk">{svg(b)}<b>Kiwi</b> UX Architect</span></div></div></section>''' for i, (t, idea, a, r, b) in enumerate(K))
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.c{{position:relative;background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;grid-template-columns:132px minmax(0,1fr);gap:18px;align-items:start}}
.c>svg{{width:132px;height:132px}}.n{{position:absolute;top:12px;left:14px;font-size:12px;font-weight:800;color:#8a8a84}}h2{{font-size:20px;margin:0 0 4px}}
.c p{{margin:0 0 6px;font-size:14px;color:#3a3a37}}.c p.pr{{color:#5b5b56}}.pr b{{color:{INK}}}
.sm{{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px;align-items:center}}.pq{{display:inline-grid;place-items:center;width:30px;height:30px;border:1px solid #ececE6;border-radius:8px}}.pq svg{{width:16px;height:16px}}.pq.p24{{width:38px;height:38px}}.pq.p24 svg{{width:24px;height:24px}}.pq.dk{{background:{INK};border-color:{INK}}}
.lk{{display:inline-flex;align-items:center;gap:8px;border:1px solid #ececE6;border-radius:10px;padding:6px 12px;font-size:16px}}.lk svg{{width:28px;height:28px}}
@media (max-width:860px){{.g{{grid-template-columns:1fr}}}}@media (max-width:440px){{.c{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Kiwi UX Architect · símbolo</title>'
        f'<style>{css}</style></head><body><main><h1>Kiwi · UX Architect · ronda 2</h1>'
        '<p class="lead">Lo que faltaba era el oficio: arquitecto. Estas cuatro opciones hablan el lenguaje de la arquitectura (la clave que sostiene, el plano, la planta, las medidas por tamaño) con las mismas piezas del sistema: punto, enlace y anillo. En tinta.</p>'
        f'<div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'kiwi.html'), 'w').write(html); print('ok')
