# Fruti Squad · ronda 17 · el orquestador (Fruti Squad Workflow Pack). Mora elegida: «Red de conocimiento» (usuario: «vamos con la 1»).
# El sello madre tiene que reunir a los cinco sin copiar a ninguno: delega cada etapa y la evidencia (el punto) pasa de uno a otro.
import os, math
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
def svg(b, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b.replace("§", c).replace("¤", "#fff" if c == INK else INK)}</svg>'
def d(x, y, r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="§"/>'
def o(x, y, r, w=3.5): return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="§" stroke-width="{w}"/>'
def fr(x, y, w, h, r, fill='none'): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" stroke="§" stroke-width="3.5" fill="{fill}"/>'
def ln(p, w=3.5): return f'<path d="{p}" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
KIWI = fr(4, 4, 56, 56, 12) + fr(13, 13, 38, 38, 9) + fr(21, 21, 22, 22, 6) + d(32, 32, 5.5)
LIMA = fr(20, 4, 40, 34, 9) + fr(12, 13, 40, 34, 9, '¤') + fr(4, 22, 40, 36, 9, '¤') + d(24, 40, 6)
COCO = ln('M4 18V12a8 8 0 0 1 8-8h6M46 4h6a8 8 0 0 1 8 8v6M60 46v6a8 8 0 0 1-8 8h-6M18 60h-6a8 8 0 0 1-8-8v-6') + fr(18, 18, 28, 28, 7) + d(32, 32, 5.5)
BRUNO = ('<path d="M27 4H16A12 12 0 0 0 4 16v32a12 12 0 0 0 12 12h3" stroke="§" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="5 5"/>'
         '<path d="M37 60h11a12 12 0 0 0 12-12V16A12 12 0 0 0 48 4h-3" stroke="§" stroke-width="3.5" stroke-linecap="round"/>' + ln('M38 6L26 58', 4) + d(44, 32, 5.5))
MORA = fr(4, 4, 56, 56, 12) + ln('M19 19L44 21M44 21L45 45M44 21L20 44', 3) + d(19, 19, 6) + d(44, 21, 4.5) + d(45, 45, 4.5) + d(20, 44, 4.5)
FAM = [('Kiwi', KIWI), ('Lima', LIMA), ('Coco', COCO), ('Bruno', BRUNO), ('Mora', MORA)]
def pent(r, cy=32):
    return [(32 + r * math.cos(math.radians(-90 + i * 72)), cy + r * math.sin(math.radians(-90 + i * 72))) for i in range(5)]
P5 = pent(18)
S = [
 ('Núcleo', 'El orquestador al centro, dentro del marco de la familia, con los cinco especialistas alrededor y unidos a él: delega cada etapa.',
  'La lectura más clara de «orquestador»; cinco puntos = cinco integrantes, sin copiar a ninguno.', 'Un centro con radios puede recordar iconos de «red» o «hub».',
  fr(4, 4, 56, 56, 14) + ''.join(ln(f'M32 32L{x:.1f} {y:.1f}', 2.6) for x, y in P5) + ''.join(d(round(x, 1), round(y, 1), 4.2) for x, y in P5) + d(32, 32, 7)),
 ('Ronda', 'Los cinco en un anillo y uno resaltado: el turno activo. La evidencia da la vuelta de especialista en especialista.',
  'Cuenta el flujo por turnos (handoffs) con movimiento; se anima muy bien (el punto grande recorre la ronda).', 'Sin el marco, cinco puntos en círculo son un patrón común; el resaltado es lo que lo vuelve propio.',
  fr(4, 4, 56, 56, 14) + o(32, 32, 18, 2.4) + ''.join(d(round(x, 1), round(y, 1), 7 if i == 0 else 4.2) for i, (x, y) in enumerate(P5))),
 ('Quinteto', 'Un marco con cinco puntos como la cara de un dado: cinco especialistas, un solo sistema.',
  'La silueta más simple y fuerte a 16 px; sello muy fácil de recordar.', 'Es literalmente un dado: puede sonar a juego o azar.',
  fr(4, 4, 56, 56, 14) + d(19, 19, 5.5) + d(45, 19, 5.5) + d(32, 32, 6.5) + d(19, 45, 5.5) + d(45, 45, 5.5)),
 ('Secuencia', 'Una cápsula con cinco puntos unidos en orden; el último, mayor: lo entregado al final del flujo.',
  'Cuenta el Workflow Pack (etapas en orden con un resultado); horizontal, buena para banners.', 'Puede leerse como barra de progreso o carrusel.',
  fr(2, 18, 60, 28, 14) + ln('M12 32h40', 2.6) + d(12, 32, 3.6) + d(22, 32, 3.6) + d(32, 32, 3.6) + d(42, 32, 3.6) + d(52, 32, 6.5)),
]
fam = ''.join(f'<span>{svg(b)}<b>{n}</b></span>' for n, b in FAM)
cards = ''.join(f'''<section class="c"><span class="n">{i+1}</span>{svg(b)}<div><h2>{t}</h2><p>{idea}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p>
<div class="sm"><span class="pq">{svg(b)}</span><span class="pq p24">{svg(b)}</span><span class="pq dk">{svg(b, "#fff")}</span></div>
<div class="row">{svg(b)}<i></i>{"".join(svg(x) for _, x in FAM)}</div></div></section>''' for i, (t, idea, a, r, b) in enumerate(S))
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.fam{{display:flex;gap:18px;align-items:center;background:#fff;border:1px solid #e3e3de;border-radius:14px;padding:12px 16px;flex-wrap:wrap}}.fam svg{{width:44px;height:44px}}.fam span{{display:flex;gap:8px;align-items:center}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.c{{position:relative;background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;grid-template-columns:124px minmax(0,1fr);gap:18px;align-items:start}}
.c>svg{{width:124px;height:124px}}.n{{position:absolute;top:12px;left:14px;font-size:12px;font-weight:800;color:#8a8a84}}h2{{font-size:20px;margin:0 0 4px}}
.c p{{margin:0 0 6px;font-size:14px;color:#3a3a37}}.c p.pr{{color:#5b5b56}}.pr b{{color:{INK}}}
.sm{{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px;align-items:center}}.pq{{display:inline-grid;place-items:center;width:30px;height:30px;border:1px solid #ececE6;border-radius:8px}}.pq svg{{width:16px;height:16px}}.pq.p24{{width:38px;height:38px}}.pq.p24 svg{{width:24px;height:24px}}.pq.dk{{background:{INK};border-color:{INK}}}
.row{{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:10px;border:1px solid #ececE6;border-radius:12px;padding:8px 12px}}.row svg{{width:30px;height:30px}}.row svg:first-child{{width:40px;height:40px}}.row i{{width:1px;height:28px;background:#dcdcd6}}
@media (max-width:860px){{.g{{grid-template-columns:1fr}}}}@media (max-width:440px){{.c{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · orquestador</title>'
        f'<style>{css}</style></head><body><main><h1>Fruti Squad · el orquestador (Workflow Pack)</h1>'
        '<p class="lead">El último símbolo es el sello madre: tiene que reunir a los cinco sin copiar a ninguno. El orquestador delega cada etapa y la evidencia pasa de uno a otro. Cuatro opciones; cada una encabeza la fila de la familia completa.</p>'
        f'<div class="fam">{fam}</div><div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'squad.html'), 'w').write(html); print('ok')
