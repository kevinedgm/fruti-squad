# CLNDA Studio · ronda 1: tres conceptos desde la calenda (sin marmota: ya es el sello de Oaxaca)
import sys,math,glob
S=sys.argv[1]
INK='#17141a'; PAPEL='#f6f1e8'
ACC=['#e4007c','#ff8a00','#00a3a8','#6a3fb5','#ffd400']   # rosa mexicano, naranja, turquesa, morado, amarillo (provisional, ronda 1)
def svg(vb,body,cls=''): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" class="{cls}">{body}</svg>'
# A · el globo de calenda: esfera de papel en un palo; las franjas son series de datos; la luz adentro
def globo(color=True):
    cx,cy,r=32,26,19
    franjas=''
    for i,(y0,y1) in enumerate([(-19,-11),(-11,-3),(-3,5),(5,13),(13,19)]):
        c=ACC[i] if color else INK
        franjas+=f'<path d="M{cx-math.sqrt(r*r-y0*y0):.2f} {cy+y0} A{r} {r} 0 0 1 {cx+math.sqrt(r*r-y0*y0):.2f} {cy+y0} L{cx+math.sqrt(r*r-y1*y1):.2f} {cy+y1} A{r} {r} 0 0 1 {cx-math.sqrt(r*r-y1*y1):.2f} {cy+y1} Z" fill="{c}" opacity="{1 if color else 1-0.18*i}"/>'
    return svg('0 0 64 64',f'{franjas}<rect x="30" y="45" width="4" height="17" rx="2" fill="{INK}"/><circle cx="32" cy="26" r="5" fill="{PAPEL}"/>')
# B · las vocales que faltan: C·L·ND·A — los huecos de CALENDA se llenan de color (tipográfico; aquí con rects)
def vocales(color=True):
    # bloques de letras aproximados a 64 de alto: se renderiza con fuente real en el banco; aquí un símbolo: dos huecos de color
    return svg('0 0 64 64',f'<rect x="4" y="18" width="12" height="28" rx="3" fill="{INK}"/><rect x="20" y="18" width="9" height="28" rx="3" fill="{ACC[0] if color else INK}" opacity="{1 if color else .35}"/><rect x="33" y="18" width="12" height="28" rx="3" fill="{INK}"/><rect x="49" y="18" width="9" height="28" rx="3" fill="{ACC[2] if color else INK}" opacity="{1 if color else .35}"/>')
# C · papel picado como matriz de datos: una bandera con huecos; los huecos son datos
def picado(color=True):
    pts=''
    import random; random.seed(7)
    for i in range(5):
        for j in range(4):
            x,y=12+i*10,14+j*9
            if (i,j) in [(1,1),(3,1),(2,2),(1,3),(3,3),(2,0)]: continue
            pts+=f'<circle cx="{x}" cy="{y}" r="2.6" fill="{PAPEL}"/>'
    fill=ACC[0] if color else INK
    return svg('0 0 64 64',f'<path d="M4 4H60V48L52 42 44 48 36 42 28 48 20 42 12 48 4 42Z" fill="{fill}"/><path d="M4 4H60" stroke="{INK}" stroke-width="2"/>{pts}')
# D · la comparsa: puntos que caminan y forman una línea (datos que se vuelven camino)
def comparsa(color=True):
    body=''
    xs=[6,16,26,36,46,56]; ys=[46,40,34,30,24,16]
    body+=f'<path d="M{xs[0]} {ys[0]} C 20 46 18 30 {xs[2]} {ys[2]} S 44 30 {xs[4]} {ys[4]} S 54 12 {xs[5]} {ys[5]}" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>'
    for k,(x,y) in enumerate(zip(xs,ys)):
        body+=f'<circle cx="{x}" cy="{y}" r="{4.5 if k==5 else 3.5}" fill="{ACC[k%5] if color else INK}"/>'
    return svg('0 0 64 64',body)
C={'A · globo de calenda':globo,'B · las vocales que faltan':vocales,'C · papel picado':picado,'D · la comparsa':comparsa}
fonts=glob.glob(S+'/fuentes/Syne*')[0]
css=f'''@font-face{{font-family:Syne;src:url("file://{fonts}");font-weight:400 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:800 18px Syne;margin:0 0 6px}} .sub{{color:#666;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-bottom:26px}}
.celda{{display:grid;gap:10px;align-content:start}} .celda svg{{display:block}} .big svg{{width:120px;height:120px}}
.s{{display:flex;gap:14px;align-items:center}} .s svg{{width:24px;height:24px}} .s .x{{width:16px;height:16px}}
.dark{{background:{INK};color:{PAPEL};padding:10px;border-radius:10px}}
.wm{{font:800 44px Syne;letter-spacing:-.02em;display:flex;align-items:baseline;gap:0}}
.wm i{{display:inline-block;width:.42em;height:.72em;border-radius:.08em;transform:translateY(.02em);margin:0 .05em}}
.tag{{font:400 12px system-ui;color:#666}}'''
cells=''
for name,fn in C.items():
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big">{fn(True)}</div><div class="s">{fn(True)}<span class="x">{fn(True)}</span><span class="dark" style="display:inline-flex;gap:10px">{fn(True)}{fn(False).replace(INK,PAPEL)}</span></div><div class="big" style="opacity:.9">{fn(False)}</div><span class="tag">una tinta</span></div>'
wm=f'''<div class="fila" style="grid-template-columns:1fr 1fr"><div class="celda"><h2>Nombre · B aplicado al wordmark</h2><div class="wm">C<i style="background:{ACC[0]}"></i>L<i style="background:{ACC[2]}"></i>NDA</div><div class="wm" style="font-size:28px">C<i style="background:{ACC[0]}"></i>L<i style="background:{ACC[2]}"></i>NDA <span style="font-weight:400;margin-left:.3em">Studio</span></div><span class="tag">las vocales que faltan (A, E) son color; la A final se queda porque CLNDA la conserva</span></div>
<div class="celda"><h2>Nombre · plano, para A, C y D</h2><div class="wm">CLNDA</div><div class="wm" style="font-size:28px">CLNDA <span style="font-weight:400;margin-left:.3em">Studio</span></div><span class="tag">Syne 800 (provisional)</span></div></div>'''
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">CLNDA Studio · ronda 1 · cuatro conceptos desde la calenda (sin la marmota, que ya es el sello). Colores provisionales.</p><div class="fila">{cells}</div>{wm}')
print('ok')
