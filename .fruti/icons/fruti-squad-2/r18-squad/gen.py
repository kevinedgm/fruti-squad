# Fruti Squad · ronda 18 (usuario: «no me gusta, otra ronda más disruptiva y moderna») · el orquestador (Fruti Squad Workflow Pack). Mora elegida: «Red de conocimiento» (usuario: «vamos con la 1»).
# El sello madre tiene que reunir a los cinco sin copiar a ninguno: delega cada etapa y la evidencia (el punto) pasa de uno a otro.
import os, math
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
import re, itertools
_n = itertools.count()
def svg(b, c=INK):
    k = next(_n); b = re.sub(r'(id="|url\(#)([sc]\d+)', lambda m: f'{m.group(1)}{m.group(2)}_{k}', b)
    return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b.replace("§", c).replace("¤", "#fff" if c == INK else INK)}</svg>'
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
def solido(uid):
    holes = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#000"/>' for x, y, r in [(16, 48, 2.6), (23, 41, 3.4), (31, 33, 4.4), (40, 24, 5.6), (47, 16, 3)])
    return (f'<mask id="s{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="#fff"/>{holes}</mask>'
            f'<rect x="4" y="4" width="56" height="56" rx="16" fill="§" mask="url(#s{uid})"/>')
def espiral():
    o = ''
    for i, (sz, rx) in enumerate([(54, 14), (43, 11), (33, 9), (24, 7), (16, 5)]):
        o += f'<rect x="{32 - sz / 2}" y="{32 - sz / 2}" width="{sz}" height="{sz}" rx="{rx}" stroke="§" stroke-width="3" transform="rotate({i * 11} 32 32)"/>'
    return o + d(32, 32, 4)
def eslabones(uid):
    A = '<rect x="4" y="4" width="36" height="36" rx="11"/>'; B = '<rect x="24" y="24" width="36" height="36" rx="11"/>'
    return (f'<g stroke="§" stroke-width="4.5" fill="none">{B}</g>'
            f'<g stroke="¤" stroke-width="9" fill="none">{A}</g><g stroke="§" stroke-width="4.5" fill="none">{A}</g>'
            f'<clipPath id="c{uid}"><rect x="36" y="18" width="10" height="12"/></clipPath>'
            f'<g clip-path="url(#c{uid})"><g stroke="¤" stroke-width="9" fill="none">{B}</g><g stroke="§" stroke-width="4.5" fill="none">{B}</g></g>' + d(32, 32, 5))
S = [
 ('Sólido', 'El único bloque lleno de la familia (los cinco son de trazo): el orquestador pesa más. Una estela de perforaciones lo cruza en diagonal: la evidencia que viaja y acelera.',
  'Disruptivo por contraste: sólido frente a cinco lineales; silueta de app moderna; la estela da dirección y velocidad.', 'Las perforaciones chicas desaparecen a 16 px; queda un cuadro con puntos.',
  solido(1)),
 ('Espiral', 'Los marcos de la familia anidados y girando: cada especialista entra en su turno y el conjunto se mueve. Al centro, la evidencia.',
  'Moderna y con movimiento implícito; hereda el marco de Kiwi y lo pone a girar (orquestar). Se anima de forma muy natural.', 'Puede recordar el icono de «cargando» o un efecto hipnótico si gira demasiado.',
  espiral()),
 ('Eslabones', 'Dos marcos enlazados como cadena, entrelazados de verdad (uno pasa por encima y luego por debajo). El punto vive en el cruce: el traspaso entre especialistas.',
  'Cuenta el handoff y la coordinación en una forma; el entrelazado le da profundidad y oficio.', 'Dos cuadros enlazados recuerdan iconos de «vincular» o «unir».',
  eslabones(2)),
 ('Entrega', 'Un marco que se abre en una esquina y deja salir la evidencia: el paquete no se queda adentro, entrega.',
  'Simple, con dirección y energía; dice «workflow con resultado».', 'Se parece mucho al icono de «editar» o «redactar» (lápiz sobre un cuadro).',
  '<path d="M38 4H16A12 12 0 0 0 4 16v32a12 12 0 0 0 12 12h32a12 12 0 0 0 12-12V26" stroke="§" stroke-width="4.5" stroke-linecap="round"/>' + ln('M30 34L50 14', 4.5) + d(53, 11, 7)),
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
        '<p class="lead">El último símbolo es el sello madre: tiene que reunir a los cinco sin copiar a ninguno. El orquestador delega cada etapa y la evidencia pasa de uno a otro. Ronda 2, más disruptiva: formas con peso, movimiento o profundidad, no solo puntos en un marco. Cada una encabeza la fila de la familia completa.</p>'
        f'<div class="fam">{fam}</div><div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'squad.html'), 'w').write(html); print('ok')
