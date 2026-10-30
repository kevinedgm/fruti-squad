# Fruti Squad · ronda 7: Átomos (A de la ronda 6) desde la habilidad real de cada integrante (README de fruti-squad-kiro).
# Usuario: «trabajemos sobre la A; propuesta en base a lo que cada integrante hace; representemos su habilidad». Colores no gustaron: aquí en tinta.
# Regla: el átomo es el punto (la evidencia). Se permiten «enlaces» (barras) y «anillos». Dos variantes por integrante.
import os, math
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
def svg(b, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b.replace("§", c)}</svg>'
def d(x, y, r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="§"/>'
def ring(x, y, r, w=5): return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="§" stroke-width="{w}"/>'
def bar(x1, y1, x2, y2, w=5): return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="§" stroke-width="{w}" stroke-linecap="round"/>'
M = [
 ('squad', 'Fruti Squad', 'Orquesta: delega cada etapa al especialista y la evidencia pasa de uno a otro.',
  ('Núcleo', 'El orquestador al centro y los cinco alrededor.', ''.join(d(32 + 21 * math.cos(math.radians(-90 + i * 72)), 32 + 21 * math.sin(math.radians(-90 + i * 72)), 6.5) for i in range(5)) + d(32, 32, 9)),
  ('Relevo', 'Cinco etapas en orden; la última, mayor, es lo entregado.', bar(10, 46, 22, 26) + bar(22, 26, 34, 40) + bar(34, 40, 46, 20) + d(10, 46, 5.5) + d(22, 26, 5.5) + d(34, 40, 5.5) + d(46, 20, 5.5) + d(52, 44, 9) + bar(46, 20, 52, 44))),
 ('kiwi', 'Kiwi', 'Estructura antes que apariencia: regiones, jerarquía, qué aparece primero y cómo se reorganiza en compact, medium y expanded.',
  ('Jerarquía', 'Uno grande arriba, dos medianos, tres chicos: qué va primero.', d(32, 13, 9) + d(22, 33, 6.5) + d(42, 33, 6.5) + d(15, 50, 4.5) + d(32, 50, 4.5) + d(49, 50, 4.5)),
  ('Regiones', 'Una región principal y dos secundarias: la arquitectura de una pantalla.', d(22, 32, 14) + d(48, 20, 7.5) + d(48, 44, 7.5))),
 ('lima', 'Lima', 'Gobierna: reutiliza, extiende o crea; contratos, registro, ciclo de vida y quality gates.',
  ('Compuerta', 'Tres llegan, la compuerta deja pasar lo que cumple.', d(9, 32, 4.5) + d(9, 20, 4.5) + d(9, 44, 4.5) + bar(24, 12, 24, 52, 5.5) + bar(34, 12, 34, 52, 5.5) + d(50, 32, 7.5)),
  ('Ciclo de vida', 'Local → reutilizable → sistema: crece y queda certificado en un anillo.', d(10, 32, 4) + d(24, 32, 6) + ring(46, 32, 13, 5) + d(46, 32, 6.5))),
 ('coco', 'Coco', 'Construye lo visual (F3) y después audita (R0): consistencia, accesibilidad, desviaciones del contrato.',
  ('Hallazgo', 'Una retícula pareja; el lente marca el punto que se desvía.', ''.join(d(x, y, 3.6) for x in (14, 26, 38) for y in (14, 26, 38) if (x, y) != (38, 38)) + ring(42, 42, 12, 5) + d(42, 42, 5)),
  ('Medición', 'Puntos alineados sobre una base, con la regla que verifica su altura.', d(14, 36, 5.5) + d(28, 36, 5.5) + d(42, 30, 5.5) + bar(8, 48, 56, 48, 4) + bar(52, 18, 52, 36, 3.5) + bar(48, 18, 56, 18, 3.5))),
 ('bruno', 'Bruno', 'Convierte lo aprobado en comportamiento real: props, eventos, estados, teclado, foco.',
  ('Interruptor', 'Un estado que cambia: el componente ya se comporta.', '<rect x="6" y="20" width="52" height="24" rx="12" stroke="§" stroke-width="5"/>' + d(46, 32, 7.5)),
  ('Foco', 'El punto con su anillo de foco: interacción accesible.', d(30, 34, 10) + '<circle cx="30" cy="34" r="18" stroke="§" stroke-width="4.5" stroke-dasharray="8 6"/>' + d(52, 12, 5))),
 ('mora', 'Mora', 'Documenta solo lo que existe y fue verificado; mantiene la documentación sincronizada con el código.',
  ('Índice', 'Cada punto con su entrada: el catálogo navegable.', ''.join(d(12, y, 4.5) + bar(22, y, 22 + w, y, 5) for y, w in ((14, 30), (26, 22), (38, 26), (50, 16)))),
  ('Espejo', 'Código y documentación, punto por punto, unidos.', ''.join(d(14, y, 5) + d(50, y, 5) + bar(20, y, 44, y, 3.5) for y in (14, 32, 50)))),
]
rows = ''
for k, n, hace, v1, v2 in M:
    rows += (f'<section class="c"><div class="who"><b>{n}</b><p>{hace}</p></div>'
             + ''.join(f'<figure class="op"><span class="lbl">{i}</span>{svg(v[2])}<figcaption><b>{v[0]}</b><span>{v[1]}</span></figcaption><div class="sm"><span class="pq">{svg(v[2])}</span><span class="pq dk">{svg(v[2], "#fff")}</span></div></figure>' for i, v in ((1, v1), (2, v2)))
             + '</section>')
fam1 = ''.join(f'<figure>{svg(v1[2])}<figcaption>{n}</figcaption></figure>' for k, n, h, v1, v2 in M)
fam2 = ''.join(f'<figure>{svg(v2[2])}<figcaption>{n}</figcaption></figure>' for k, n, h, v1, v2 in M)
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:14px}}h1{{font-size:28px;line-height:1.2;margin:0}}h2{{font-size:18px;margin:8px 0 0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.c{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:18px 20px;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr) minmax(0,1fr);gap:18px;align-items:center}}
.who b{{font-size:20px}}.who p{{margin:4px 0 0;color:#4b4b47;font-size:14px}}
.op{{margin:0;display:grid;grid-template-columns:88px minmax(0,1fr);grid-template-areas:"s t" "s m";gap:2px 12px;align-items:center;position:relative;border:1px solid #ececE6;border-radius:14px;padding:12px}}
.op>svg{{grid-area:s;width:88px;height:88px}}.op figcaption{{grid-area:t;display:grid;line-height:1.3}}.op figcaption span{{font-size:13px;color:#4b4b47}}.sm{{grid-area:m;display:flex;gap:6px}}
.lbl{{position:absolute;top:8px;left:10px;font-size:11px;font-weight:800;color:#8a8a84}}
.pq{{display:inline-grid;place-items:center;width:28px;height:28px;border:1px solid #ececE6;border-radius:7px}}.pq svg{{width:16px;height:16px}}.pq.dk{{background:{INK};border-color:{INK}}}
.fam{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:18px}}.fam figure{{margin:0;display:grid;justify-items:center;gap:6px;font-size:13px;font-weight:600}}.fam svg{{width:64px;height:64px}}
@media (max-width:900px){{.c{{grid-template-columns:1fr}}.fam{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · átomos por habilidad</title>'
        f'<style>{css}</style></head><body><main><h1>Fruti Squad · Átomos según lo que hace cada uno (ronda 7)</h1>'
        '<p class="lead">Sobre la A. Cada símbolo sale de la responsabilidad real del integrante (README del paquete). El átomo sigue siendo el punto, la evidencia; se agregan dos piezas: el enlace (barra) y el anillo. Dos variantes por integrante, en tinta: el color va después, con una paleta nueva.</p>'
        f'{rows}<h2>Familia con las variantes 1</h2><div class="fam">{fam1}</div><h2>Familia con las variantes 2</h2><div class="fam">{fam2}</div></main></body></html>')
open(os.path.join(H, 'habilidades.html'), 'w').write(html); print('ok')
