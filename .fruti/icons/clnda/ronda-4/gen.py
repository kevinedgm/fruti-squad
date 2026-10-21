# CLNDA · ronda 4: desarrollo de C (la llave) y E (bloque cursor), más dos híbridos.
import sys
S=sys.argv[1]; INK='#17141a'; PAPEL='#f6f1e8'; ROSA='#e4007c'; TURQ='#00a3a8'; AMAR='#ffd400'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
BR='M40 10 H36 a8 8 0 0 0 -8 8 V26 a6 6 0 0 1 -6 6 a6 6 0 0 1 6 6 V46 a8 8 0 0 0 8 8 H40'   # llave {
def brace(k,sw=7,dx=0): return f'<path d="{BR}" stroke="{k}" stroke-width="{sw}" transform="translate({dx} 0)"/>'
# --- C: la llave
def c1(c=True):  # llave + punto (ronda 3), llave rosa para que el color esté en el gesto
    return svg(brace(ROSA if c else INK)+f'<circle cx="46" cy="32" r="6" fill="{INK}"/>')
def c2(c=True):  # llave en tinta + punto rosa, punto más grande y pegado: el dato sale de la llave
    return svg(brace(INK,7,-4)+f'<circle cx="46" cy="32" r="7.5" fill="{ROSA if c else INK}"/>')
def c3(c=True):  # par de llaves { } con el punto en medio: un bloque de código que contiene el dato
    return svg(brace(INK,6,-10)+f'<path d="{BR}" stroke="{INK}" stroke-width="6" transform="translate(74 0) scale(-1 1)"/><circle cx="32" cy="32" r="6" fill="{ROSA if c else INK}"/>')
# --- E: bloque cursor
def e1(c=True):  # bloque rosa, C recortada (ronda 3)
    a=ROSA if c else INK
    return svg(f'<rect x="10" y="8" width="44" height="48" rx="6" fill="{a}"/><path d="M40 24 A11 11 0 1 0 40 40" stroke="{PAPEL}" stroke-width="7"/>')
def e2(c=True):  # bloque más alto y estrecho (proporción de cursor real 1:2), C recortada
    a=ROSA if c else INK
    return svg(f'<rect x="16" y="6" width="32" height="52" rx="5" fill="{a}"/><path d="M38 25 A9 9 0 1 0 38 39" stroke="{PAPEL}" stroke-width="6"/>')
def e3(c=True):  # bloque en tinta con la C en rosa: el cursor es el fondo, la letra es el color
    a=ROSA if c else PAPEL
    return svg(f'<rect x="10" y="8" width="44" height="48" rx="6" fill="{INK}"/><path d="M40 24 A11 11 0 1 0 40 40" stroke="{a}" stroke-width="7"/>')
# --- híbridos
def h1(c=True):  # bloque rosa con la llave recortada y el punto en papel
    a=ROSA if c else INK
    return svg(f'<rect x="10" y="8" width="44" height="48" rx="6" fill="{a}"/><g transform="translate(2 9.6) scale(0.7)">{brace(PAPEL,8)}</g><circle cx="41" cy="32" r="5" fill="{PAPEL}"/>')
def h2(c=True):  # bloque rosa con la llave recortada; el punto, en turquesa, es lo único que no es rosa ni papel
    a=ROSA if c else INK; d=TURQ if c else PAPEL
    return svg(f'<rect x="10" y="8" width="44" height="48" rx="6" fill="{a}"/><g transform="translate(2 9.6) scale(0.7)">{brace(PAPEL,8)}</g><circle cx="41" cy="32" r="5.5" fill="{d}"/>')
G=[('C · la llave',[('C1 · llave en color',c1),('C2 · punto grande',c2),('C3 · par de llaves',c3)]),
   ('E · bloque cursor',[('E1 · bloque con C',e1),('E2 · proporción de cursor',e2),('E3 · bloque tinta, C rosa',e3)]),
   ('C + E · la llave dentro del cursor',[('H1 · llave y punto en papel',h1),('H2 · punto turquesa',h2)])]
sg=S+'/fuentes/SpaceGrotesk[wght].ttf'; jb=S+'/fuentes/JetBrainsMono.ttf'
css=f'''@font-face{{font-family:SG;src:url("file://{sg}");font-weight:300 700}} @font-face{{font-family:JB;src:url("file://{jb}");font-weight:100 800}}
body{{margin:0;padding:28px;background:{PAPEL};color:{INK};font:14px/1.4 SG,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 18px SG;margin:0 0 10px}} h3{{font:700 15px SG;margin:0 0 6px}} .sub{{color:#5b5560;margin:0 0 14px}}
.grupo{{margin-bottom:26px}} .fila{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
.celda{{display:grid;gap:10px;align-content:start;background:#fff;padding:16px;border-radius:12px;border:1px solid #e3ddd1}} .celda svg{{display:block}} .big svg{{width:110px;height:110px}}
.s{{display:flex;gap:14px;align-items:center}} .s svg{{width:24px;height:24px}} .s .x svg{{width:16px;height:16px}} .s .t svg{{width:110px;height:110px}}
.dark{{background:{INK};padding:10px;border-radius:8px;display:inline-flex;gap:10px}}
.wm{{font:700 30px SG;letter-spacing:-.02em;display:flex;align-items:center;gap:10px}} .wm svg{{width:36px;height:36px}}
.cur{{display:inline-block;width:.62em;height:1em;background:{ROSA};border-radius:3px;vertical-align:-.12em;margin-left:.08em}}
.firma{{font:500 13px JB;color:#5b5560;display:flex;align-items:center;gap:6px}} .firma svg{{width:16px;height:16px}}'''
def dark(s): return s.replace(f'stroke="{PAPEL}"','stroke="@P@"').replace(f'fill="{PAPEL}"','fill="@F@"').replace(INK,PAPEL).replace('@P@',INK).replace('@F@',INK)
out=''
for gname,items in G:
    cells=''
    for name,fn in items:
        cells+=f'<div class="celda"><h3>{name}</h3><div class="s"><span class="t">{fn(True)}</span><span class="t" style="opacity:.9">{fn(False)}</span></div><div class="s">{fn(True)}<span class="x">{fn(True)}</span><span class="dark">{dark(fn(True))}{dark(fn(False))}</span></div><div class="wm">{fn(True)}CLNDA<span class="cur"></span></div><div class="firma">{fn(True)}hecho por CLNDA Studio</div></div>'
    out+=f'<div class="grupo"><h2>{gname}</h2><div class="fila">{cells}</div></div>'
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">CLNDA · ronda 4 · desarrollo de la llave y del bloque cursor, y dos híbridos. Cada celda: color y una tinta, 24 y 16 px, sobre tinta, lockup con cursor y firma de producto.</p>{out}')
print('ok')
