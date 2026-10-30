# Fruti Squad · ronda 10 · Lima (Design System Governance). Kiwi quedó con «Tres tamaños» (usuario: «vamos con el 4»).
# Kiwi fija el lenguaje: marcos redondeados en trazo 3.5 + el punto lleno (la evidencia). Lima habla el mismo idioma con otra silueta.
# Lima: clasifica (reuse/extend/new/local), contratos, tokens, registro, ciclo de vida, quality gates, promoción y deprecación.
import os
H = os.path.dirname(os.path.abspath(__file__))
INK, BG = '#18181b', '#f5f5f2'
def svg(b, c=INK): return f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none">{b.replace("§", c)}</svg>'
def d(x, y, r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="§"/>'
def fr(x, y, w, h, r, extra=''): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" stroke="§" stroke-width="3.5"{extra}/>'
def ln(p, w=3.5): return f'<path d="{p}" stroke="§" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
KIWI = fr(4, 4, 56, 56, 12) + fr(13, 13, 38, 38, 9) + fr(21, 21, 22, 22, 6) + d(32, 32, 5.5)
L = [
 ('Clasificación', 'reuse / extend / new / local · registry',
  'Un marco dividido en cuatro casillas: las cuatro decisiones de Lima. El punto ocupa la que le corresponde.',
  'Cuenta su decisión principal (dónde va cada pieza) con la misma geometría de Kiwi; muy legible a 16 px.', 'Una cuadrícula 2×2 se parece a iconos de «apps» o «galería»; el punto es lo que lo vuelve propio.',
  fr(4, 4, 56, 56, 12) + ln('M32 8v48M8 32h48') + d(45, 19, 6)),
 ('Compuerta', 'quality gates',
  'Un marco con una abertura: solo sale lo que cumple. El punto ya pasó la compuerta.',
  'La idea de «gate» es exacta para gobernanza; silueta abierta, distinta de Kiwi.', 'Se parece al icono de «salir» (puerta con flecha); el punto fuera lo acerca a «exportar».',
  '<path d="M44 14V10a6 6 0 0 0-6-6H10a6 6 0 0 0-6 6v44a6 6 0 0 0 6 6h28a6 6 0 0 0 6-6v-4" stroke="§" stroke-width="3.5" stroke-linecap="round"/>' + ln('M44 26v12', 3.5) + d(24, 32, 5.5) + d(54, 32, 5.5)),
 ('Promoción', 'lifecycle · promoción y deprecación',
  'Tres marcos que suben como escalones: local, reutilizable, sistema. El punto llegó arriba.',
  'Cuenta el ciclo de vida, que es lo más propio de Lima; dinámico.', 'Se parece mucho al icono de «señal» (barras de cobertura) o a una gráfica de crecimiento.',
  fr(4, 40, 18, 18, 5) + fr(23, 25, 18, 33, 5) + fr(42, 6, 18, 52, 5) + d(51, 18, 5.5)),
 ('Contrato', 'contratos · tokens · reglas que no se reinterpretan',
  'El marco de una pieza con su sello en la esquina: lo que está dentro ya tiene contrato.',
  'Dice «aprobado y gobernado» sin palomita; conversa con Kiwi (marco) y añade el sello.', 'El sello en la esquina puede leerse como notificación.',
  fr(4, 10, 46, 50, 10) + d(27, 35, 5.5) + '<circle cx="49" cy="15" r="10" fill="#fff" stroke="§" stroke-width="3.5"/>' + d(49, 15, 4)),
]
cards = ''.join(f'''<section class="c"><span class="n">{i+1}</span>{svg(b)}<div><h2>{t}</h2><p class="sk">{sk}</p><p>{idea}</p><p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p>
<div class="sm"><span class="pq">{svg(b)}</span><span class="pq p24">{svg(b)}</span><span class="pq dk">{svg(b, "#fff").replace('fill="#fff" stroke="#fff"', 'fill="#18181b" stroke="#fff"')}</span><span class="pair">{svg(KIWI)}{svg(b)}<small>junto a Kiwi</small></span></div></div></section>''' for i, (t, sk, idea, a, r, b) in enumerate(L))
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.kiwi{{display:flex;align-items:center;gap:14px;background:#fff;border:1px solid #e3e3de;border-radius:14px;padding:12px 16px;width:max-content;max-width:100%}}.kiwi svg{{width:48px;height:48px}}
.g{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.c{{position:relative;background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;grid-template-columns:124px minmax(0,1fr);gap:18px;align-items:start}}
.c>svg{{width:124px;height:124px}}.n{{position:absolute;top:12px;left:14px;font-size:12px;font-weight:800;color:#8a8a84}}h2{{font-size:20px;margin:0}}
.sk{{margin:2px 0 6px;font:600 12px ui-monospace,monospace;color:#6b6b66}}.c p{{margin:0 0 6px;font-size:14px;color:#3a3a37}}.c p.pr{{color:#5b5b56}}.pr b{{color:{INK}}}
.sm{{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px;align-items:center}}.pq{{display:inline-grid;place-items:center;width:30px;height:30px;border:1px solid #ececE6;border-radius:8px}}.pq svg{{width:16px;height:16px}}.pq.p24{{width:38px;height:38px}}.pq.p24 svg{{width:24px;height:24px}}.pq.dk{{background:{INK};border-color:{INK}}}
.pair{{display:inline-flex;align-items:center;gap:8px;border:1px solid #ececE6;border-radius:10px;padding:6px 10px}}.pair svg{{width:32px;height:32px}}.pair small{{color:#6b6b66}}
@media (max-width:860px){{.g{{grid-template-columns:1fr}}}}@media (max-width:440px){{.c{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Lima · símbolo</title>'
        f'<style>{css}</style></head><body><main><h1>Lima · Design System Governance</h1>'
        f'<p class="lead">Kiwi ya tiene símbolo y marca el idioma de la familia: marcos redondeados con el mismo trazo y el punto lleno de la evidencia. Estas cuatro opciones para Lima hablan ese idioma con otra silueta, cada una desde una de sus habilidades.</p><div class="kiwi">{svg(KIWI)}<span><b>Kiwi</b> UX Architect · elegido</span></div>'
        f'<div class="g">{cards}</div></main></body></html>')
open(os.path.join(H, 'lima.html'), 'w').write(html); print('ok')
