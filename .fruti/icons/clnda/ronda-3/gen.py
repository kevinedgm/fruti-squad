# CLNDA · ronda 3: la marca nace de cómo se escribe el nombre y del gesto del código; el color de fiesta es el único guiño a la calenda.
import sys,glob,math,random
S=sys.argv[1]; INK='#17141a'; PAPEL='#f6f1e8'; ROSA='#e4007c'; TURQ='#00a3a8'; AMAR='#ffd400'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
# A · C_ : la C y el guion bajo donde iba la vocal. Es un prompt: la terminal espera. Símbolo del wordmark C_L_ND_
def cprompt(c=True):
    a=ROSA if c else INK
    return svg(f'<path d="M44 16 A16 16 0 1 0 44 40" stroke="{INK}" stroke-width="8"/><path d="M38 56 H58" stroke="{a}" stroke-width="8"/>')
# C · la llave: la C dibujada como llave de código { , cerrada por un punto (el dato)
def llave(c=True):
    a=TURQ if c else INK
    return svg(f'<path d="M40 10 H36 a8 8 0 0 0 -8 8 V26 a6 6 0 0 1 -6 6 a6 6 0 0 1 6 6 V46 a8 8 0 0 0 8 8 H40" stroke="{INK}" stroke-width="7"/><circle cx="46" cy="32" r="6" fill="{a}"/>')
# D · confeti con ajuste: siete puntos de colores (confeti de calenda) y la recta de regresión que los atraviesa
def confeti(c=True):
    random.seed(7); pts=[(10,50),(18,40),(26,44),(32,30),(40,26),(48,18),(56,22)]
    cols=[ROSA,TURQ,AMAR,ROSA,TURQ,AMAR,ROSA]
    b=f'<path d="M8 50 L58 16" stroke="{INK}" stroke-width="3.5"/>'
    for (x,y),k in zip(pts,cols): b+=f'<circle cx="{x}" cy="{y}" r="5.5" fill="{k if c else INK}" stroke="{PAPEL}" stroke-width="2"/>'
    return svg(b)
# E · bloque cursor: el wordmark termina en un cursor de bloque en rosa. Símbolo: solo el bloque con una C recortada
def cursor(c=True):
    a=ROSA if c else INK
    return svg(f'<rect x="10" y="8" width="44" height="48" rx="6" fill="{a}"/><path d="M40 24 A11 11 0 1 0 40 40" stroke="{PAPEL}" stroke-width="7"/>')
C={'A · C_ (el prompt)':cprompt,'C · la llave':llave,'D · confeti con ajuste':confeti,'E · bloque cursor':cursor}
jb=S+'/fuentes/JetBrainsMono.ttf'; sg=glob.glob(S+'/fuentes/SpaceGrotesk*')[0]; sy=glob.glob(S+'/fuentes/Syne*')[0]
css=f'''@font-face{{font-family:JB;src:url("file://{jb}");font-weight:100 800}} @font-face{{font-family:SG;src:url("file://{sg}");font-weight:300 700}} @font-face{{font-family:SY;src:url("file://{sy}");font-weight:400 800}}
body{{margin:0;padding:28px;background:{PAPEL};color:{INK};font:14px/1.4 SG,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 18px SG;margin:0 0 6px}} .sub{{color:#5b5560;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-bottom:22px}}
.celda{{display:grid;gap:10px;align-content:start;background:#fff;padding:16px;border-radius:12px;border:1px solid #e3ddd1}} .celda svg{{display:block}} .big svg{{width:120px;height:120px}}
.s{{display:flex;gap:14px;align-items:center}} .s svg{{width:24px;height:24px}} .s .x svg{{width:16px;height:16px}}
.dark{{background:{INK};padding:10px;border-radius:8px;display:inline-flex;gap:10px}}
.wm{{font-size:34px;letter-spacing:-.02em;display:flex;align-items:center;gap:10px;min-height:48px}} .wm svg{{width:40px;height:40px}}
.jb{{font:700 34px JB}} .jb i{{font-style:normal;color:{ROSA}}} .sg{{font:700 34px SG}} .sy{{font:800 34px SY;letter-spacing:.02em}}
.cur{{display:inline-block;width:.62em;height:1em;background:{ROSA};border-radius:3px;vertical-align:-.12em;margin-left:.08em}}
.tag{{font:400 12px SG;color:#5b5560}}
.wms{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}} .wmc{{background:#fff;padding:20px;border-radius:12px;border:1px solid #e3ddd1;display:grid;gap:14px}} .wmc .grande{{font-size:64px}} .wmc .dark{{display:block;padding:18px}}'''
def dark(s): return s.replace(f'stroke="{PAPEL}"','stroke="@P@"').replace(INK,PAPEL).replace('@P@',INK)
cells=''
locks={'A · C_ (el prompt)':f'<span class="jb">C<i>_</i>L<i>_</i>ND<i>_</i></span>','C · la llave':f'<span class="sy">CLNDA</span>','D · confeti con ajuste':f'<span class="sg">CLNDA</span>','E · bloque cursor':f'<span class="sg">CLNDA<span class="cur"></span></span>'}
for name,fn in C.items():
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big">{fn(True)}</div><div class="s">{fn(True)}<span class="x">{fn(True)}</span><span class="dark">{dark(fn(True))}{dark(fn(False))}</span></div><div class="big" style="opacity:.9">{fn(False)}</div><div class="wm">{fn(True)}{locks[name]}</div></div>'
wms=f'''<div class="wms">
<div class="wmc"><h2>A · C_L_ND_ · el nombre con los huecos de las vocales</h2><div class="jb grande">C<i>_</i>L<i>_</i>ND<i>_</i></div><div class="dark"><span class="jb grande" style="color:{PAPEL}">C<i>_</i>L<i>_</i>ND<i>_</i></span></div><span class="tag">JetBrains Mono 700. Los guiones bajos son las vocales que faltan y también el cursor de una terminal: el estudio llena lo que falta. Se lee «CLNDA» igual.</span></div>
<div class="wmc"><h2>E · CLNDA▮ · el nombre con cursor de bloque</h2><div class="sg grande">CLNDA<span class="cur"></span></div><div class="dark"><span class="sg grande" style="color:{PAPEL}">CLNDA<span class="cur"></span></span></div><span class="tag">Space Grotesk 700. El bloque rosa es el cursor que parpadea: algo se está escribiendo. En web puede parpadear de verdad; en impreso queda fijo.</span></div></div>'''
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">CLNDA · ronda 3 · la marca nace del nombre escrito y del gesto del código; el color de fiesta (rosa, turquesa, amarillo) es el único guiño a la calenda.</p><div class="fila">{cells}</div>{wms}')
print('ok')
