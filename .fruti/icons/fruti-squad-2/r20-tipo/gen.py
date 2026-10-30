# Fruti Squad · ronda 20: tipografía. Color aprobado: C duotono (usuario: «apruebo C»).
# Fuentes nuevas (no Sora: identidad anterior; no Space Grotesk ni Manrope: ya son CLNDA y Mesanda). Todas con licencia OFL (Google Fonts).
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'r19-color'))
src = open(os.path.join(H, '..', 'r19-color', 'gen.py')).read()
ns = {'__file__': os.path.join(H, '..', 'r19-color', 'gen.py')}
exec(src.split('SIS = [')[0], ns)
C, NOM, INK, PAPER, DARK = ns['C'], ns['NOM'], ns['INK'], ns['PAPER'], ns['DARK']
F = [
 ('A', 'Bricolage Grotesque', "'Bricolage Grotesque'", 700, 400, 'Grotesca con carácter: trazos con contraste sutil y remates suaves. Moderna y con personalidad, sin ser decorativa.',
  'La más distintiva: se reconoce en un marketplace lleno de sans genéricas; cálida, como las frutas.', 'Su personalidad puede competir con la de los símbolos si se usa en títulos muy grandes.'),
 ('B', 'Instrument Sans', "'Instrument Sans'", 600, 400, 'Sans limpia y precisa, de las que usan productos de software actuales.',
  'La más legible en interfaces y documentación; deja que los símbolos lleven la identidad.', 'La menos memorable: se parece a muchas otras.'),
 ('C', 'Unbounded', "'Unbounded'", 700, 400, 'Ancha, redondeada y tecnológica: presencia fuerte en portadas y banners.',
  'La más disruptiva; en una portada de marketplace se impone.', 'Ocupa mucho a lo ancho: «Documentation & Knowledge Engineer» no cabe en una línea; cansa en textos largos.'),
]
def lock(k, n, p, fam, w1, w2, dark):
    return (f'<div class="lk{" dk" if dark else ""}">{C(k, dark)}<span style="font-family:{fam}"><b style="font-weight:{w1}">{n}</b><i style="font-weight:{w2}">{p}</i></span></div>')
def card(k, nom, fam, w1, w2, idea, a, r):
    claro = ''.join(lock(i, n, p, fam, w1, w2, False) for i, n, p in NOM)
    osc = ''.join(lock(i, n, p, fam, w1, w2, True) for i, n, p in (NOM[0], NOM[3]))
    portada = (f'<div class="port" style="font-family:{fam}">{C("squad", True)}<div><b style="font-weight:{w1}">Fruti Squad</b><p style="font-weight:{w2}">Agentes especialistas que diseñan, gobiernan, implementan, auditan y documentan interfaces. Para Codex, Kiro y Claude Code.</p></div></div>')
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{nom}</h2></header><p class="id">{idea}</p>'
            f'<div class="g">{claro}</div><div class="g2">{osc}</div>{portada}'
            f'<p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{PAPER};color:{INK};font:400 15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto;display:grid;gap:16px}}h1{{font-size:28px;line-height:1.2;margin:0}}.lead{{margin:0;color:#4b4b47;max-width:900px}}
.c{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:22px;display:grid;gap:14px;min-width:0}}.c header{{display:flex;gap:10px;align-items:center}}
.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:800}}h2{{font-size:19px;margin:0}}.id{{margin:0;color:#3a3a37}}
.g{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}}.g2{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}}
.lk{{display:flex;align-items:center;gap:12px;border:1px solid #ececE6;border-radius:14px;padding:12px 14px;min-width:0}}.lk.dk{{background:{DARK};border-color:{DARK};color:#fff}}.lk svg{{width:46px;height:46px;flex:none}}
.lk span{{display:grid;line-height:1.15;min-width:0}}.lk b{{font-size:21px;letter-spacing:-.01em}}.lk i{{font-style:normal;font-size:14px;opacity:.75;overflow-wrap:anywhere}}
.port{{display:flex;align-items:center;gap:22px;background:{DARK};color:#fff;border-radius:16px;padding:26px 28px}}.port svg{{width:96px;height:96px;flex:none}}.port b{{font-size:40px;line-height:1.05;letter-spacing:-.02em;display:block}}.port p{{margin:8px 0 0;color:#c9c9c4;max-width:560px}}
.pr{{margin:0;font-size:14px;color:#4b4b47}}.pr b{{color:{INK}}}
@media (max-width:900px){{.g{{grid-template-columns:1fr 1fr}}.g2{{grid-template-columns:1fr}}.port{{flex-direction:column;align-items:flex-start}}.port b{{font-size:30px}}}}@media (max-width:520px){{.g{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Fruti Squad · tipografía</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@400;700&family=Instrument+Sans:wght@400;600&family=Unbounded:wght@400;700&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main><h1>Fruti Squad · tipografía (ronda 20)</h1>'
        '<p class="lead">Color aprobado: duotono. Ahora la letra. Tres fuentes nuevas (ninguna es la de la identidad anterior ni las de CLNDA o Mesanda), todas libres para uso comercial. Cada una con los seis nombres de producto, en oscuro y en una portada de marketplace.</p>'
        f'{"".join(card(*x) for x in F)}</main></body></html>')
open(os.path.join(H, 'tipografia.html'), 'w').write(html); print('ok')
