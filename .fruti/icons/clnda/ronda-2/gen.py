# CLNDA · ronda 2: abstracto, con programación y ciencia de datos (la calenda queda como capa oculta)
import sys,math,glob,random
S=sys.argv[1]; INK='#17141a'; PAPEL='#f6f1e8'; ROSA='#e4007c'; TURQ='#00a3a8'; AMAR='#ffd400'
def svg(body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{body}</svg>'
# A · el grafo en ronda: 5 nodos (las 5 letras) unidos en círculo = pipeline y comparsa que da la vuelta al pueblo
def grafo(color=True):
    pts=[(32+22*math.cos(math.radians(-90+72*i)),32+22*math.sin(math.radians(-90+72*i))) for i in range(5)]
    e=''.join(f'<line x1="{pts[i][0]:.1f}" y1="{pts[i][1]:.1f}" x2="{pts[(i+1)%5][0]:.1f}" y2="{pts[(i+1)%5][1]:.1f}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>' for i in range(5))
    e+=f'<line x1="{pts[0][0]:.1f}" y1="{pts[0][1]:.1f}" x2="{pts[2][0]:.1f}" y2="{pts[2][1]:.1f}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
    n=''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{7 if i==0 else 5}" fill="{(ROSA if i==0 else INK) if color else INK}"/>' for i,(x,y) in enumerate(pts))
    return svg(e+n)
# B · la distribución que suena: 5 barras (histograma, ecualizador de la banda, 5 letras); la moda en color
def barras(color=True):
    h=[18,34,48,30,22]; b=''
    for i,v in enumerate(h):
        x=6+i*11; b+=f'<rect x="{x}" y="{56-v}" width="8" height="{v}" rx="4" fill="{(ROSA if i==2 else INK) if color else INK}"/>'
    return svg(b)
# C · la intersección: el bit (cuadrado) y el dato (círculo); donde se cruzan está el estudio
def interseccion(color=True):
    lens=f'<clipPath id="ci"><rect x="8" y="14" width="34" height="34" rx="6"/></clipPath>'
    return svg(f'{lens}<rect x="8" y="14" width="34" height="34" rx="6" fill="none" stroke="{INK}" stroke-width="3"/><circle cx="40" cy="36" r="18" fill="none" stroke="{INK}" stroke-width="3"/><circle cx="40" cy="36" r="18" fill="{ROSA if color else INK}" clip-path="url(#ci)" opacity="{1 if color else .35}"/>')
# D · la C de puntos: una nube de datos que forma la inicial; un punto en color es el hallazgo; la curva, el ajuste
def cpuntos(color=True):
    random.seed(3); d=''
    for i in range(14):
        a=math.radians(40+i*20); r=20+random.uniform(-3,3); x,y=32+r*math.cos(a),32+r*math.sin(a)
        d+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.choice([2.6,3.2,3.8])}" fill="{INK}"/>'
    d+=f'<path d="M48 16 A22 22 0 1 0 48 48" fill="none" stroke="{INK}" stroke-width="1.6" opacity=".35"/>'
    d+=f'<circle cx="46" cy="22" r="5" fill="{ROSA if color else INK}"/>'
    return svg(d)
C={'A · grafo en ronda':grafo,'B · la distribución que suena':barras,'C · la intersección':interseccion,'D · la C de puntos':cpuntos}
fonts=glob.glob(S+'/fuentes/Syne*')[0]
css=f'''@font-face{{font-family:Syne;src:url("file://{fonts}");font-weight:400 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:800 18px Syne;margin:0 0 6px}} .sub{{color:#666;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-bottom:26px}}
.celda{{display:grid;gap:10px;align-content:start}} .celda svg{{display:block}} .big svg{{width:120px;height:120px}}
.s{{display:flex;gap:14px;align-items:center}} .s svg{{width:24px;height:24px}} .s .x svg{{width:16px;height:16px}}
.dark{{background:{INK};padding:10px;border-radius:10px;display:inline-flex;gap:10px}}
.lock{{display:flex;align-items:center;gap:12px}} .lock svg{{width:40px;height:40px}} .lock b{{font:800 30px Syne;letter-spacing:-.02em}} .lock span{{font:400 18px Syne;margin-left:.3em}}
.tag{{font:400 12px system-ui;color:#666}}'''
cells=''
for name,fn in C.items():
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big">{fn(True)}</div><div class="s">{fn(True)}<span class="x">{fn(True)}</span><span class="dark">{fn(True).replace(INK,PAPEL)}{fn(False).replace(INK,PAPEL)}</span></div><div class="big" style="opacity:.9">{fn(False)}</div><div class="lock">{fn(True)}<b>CLNDA</b><span>Studio</span></div><span class="tag">una tinta · con el nombre</span></div>'
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">CLNDA Studio · ronda 2 · abstracto: programación y ciencia de datos; la calenda como capa oculta. Colores y letra provisionales.</p><div class="fila">{cells}</div>')
print('ok')
