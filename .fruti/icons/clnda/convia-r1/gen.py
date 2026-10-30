# Convia · símbolos ronda 1 (forma en tinta; el color se decide después). Uso: python3 gen.py <carpeta de fuentes>
import sys, os
F = sys.argv[1] if len(sys.argv) > 1 else '.'
INK = '#1b1b1d'
S = 'fill="none" stroke="{c}" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"'
P = {
 'A': ('Camino', 'Una vía que da la vuelta y llega: la C de Convia termina en el lugar al que te invitan.',
       '<path d="M47 15 A21 21 0 1 0 47 49" {s}/><circle cx="47" cy="49" r="5.5" fill="{c}"/>'),
 'B': ('Portal', 'El arco de cantera de las casonas: una puerta abierta, la invitación a entrar.',
       '<path d="M15 56 V31 A17 17 0 0 1 49 31 V56" {s}/><circle cx="32" cy="44" r="5.5" fill="{c}"/>'),
 'C': ('Encuentro', 'Dos caminos que se juntan en un punto: el convite, gente que llega al mismo plan.',
       '<path d="M13 56 C13 38 32 36 32 22 M51 56 C51 38 32 36 32 22" {s}/><circle cx="32" cy="14" r="5.5" fill="{c}"/>'),
 'D': ('Pin abierto', 'Un marcador de lugar que no se cierra: siempre hay un sitio más por descubrir.',
       '<path d="M32 58 C23 47 14 39 14 28 A18 18 0 0 1 48 20" {s}/><circle cx="32" cy="28" r="5.5" fill="{c}"/>'),
}
def svg(k, c=INK, size=None):
    body = P[k][2].format(s=S.format(c=c), c=c)
    wh = f' width="{size}" height="{size}"' if size else ''
    return f'<svg viewBox="0 0 64 64"{wh} role="img" aria-label="Convia, {P[k][0]}">{body}</svg>'
for k in P:
    open(f'{k}.svg', 'w').write(svg(k))
font = os.path.join(F, 'InstrumentSans[wdth,wght].ttf')
cards = ''.join(f'''<article><div class="big">{svg(k)}</div>
<div class="row"><span class="s">{svg(k,size=24)}</span><span class="s">{svg(k,size=16)}</span><span class="dk">{svg(k,'#ffffff',40)}</span></div>
<div class="lk">{svg(k,size=40)}<b>Convia</b></div>
<h2>{k} · {P[k][0]}</h2><p>{P[k][1]}</p></article>''' for k in P)
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Convia · símbolos r1</title><style>
@font-face{{font-family:IS;src:url("file://{font}")}}
body{{margin:0;padding:32px;background:#f4f4f1;color:{INK};font:15px/1.45 IS,system-ui,sans-serif}}
h1{{margin:0 0 4px;font-size:26px}}.lead{{margin:0 0 24px;color:#55555a}}
main{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}
article{{background:#fff;border:1px solid #e3e3de;border-radius:16px;padding:20px;display:grid;gap:14px;align-content:start}}
.big svg{{width:100%;max-width:180px;display:block;margin:8px auto}}
.row{{display:flex;gap:14px;align-items:center}}.dk{{background:#1b1b1d;border-radius:10px;padding:6px;display:inline-flex}}
.lk{{display:flex;align-items:center;gap:10px;border-top:1px solid #ececE8;padding-top:14px}}.lk b{{font:600 30px IS;letter-spacing:-.01em}}
h2{{margin:0;font-size:16px}}p{{margin:0;color:#55555a}}
</style></head><body><h1>Convia · símbolos, ronda 1</h1><p class="lead">Convite + vía. Solo forma, en tinta: el color se decide cuando haya símbolo. Tamaños: grande, 24 px, 16 px y sobre oscuro.</p><main>{cards}</main></body></html>'''
open('lamina.html', 'w').write(html)
