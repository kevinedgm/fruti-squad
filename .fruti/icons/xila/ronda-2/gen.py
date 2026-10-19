# Xila · ronda 2: patrón de hilos. El brocado se construye con hileras horizontales de hilo de distinto largo; una barra horizontal es lo mismo.
import sys,glob
S=sys.argv[1]; INK='#15171f'; PAPEL='#f7f5f0'; COB='#1f4bd8'; COB_D='#7a9bff'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
# A · rombo de hilos: 9 hileras horizontales (la trama) cuyos largos forman el rombo; la del centro en cobalto. Es también una gráfica de barras horizontales
def rombo(c=True,ox=0,oy=0):
    a=COB if c else INK; b=''
    L=[6,14,22,30,38,30,22,14,6]
    for i,l in enumerate(L):
        y=oy+12+i*5; b+=f'<path d="M{ox+32-l/2} {y} H{ox+32+l/2}" stroke="{a if i==4 else INK}" stroke-width="3"/>'
    return b
# B · trama y urdimbre: hilos verticales (urdimbre) e hileras horizontales; donde el hilo pasa «por encima» se tiñe: un mapa de calor tejido que dibuja el rombo
def trama(c=True,ox=0,oy=0):
    a=COB if c else INK; b=''
    for i in range(7):
        x=ox+11+i*7; b+=f'<path d="M{x} {oy+8} V{oy+56}" stroke="{INK}" stroke-width="1.5" opacity=".35"/>'
    cells={(3,0),(2,1),(3,1),(4,1),(1,2),(2,2),(3,2),(4,2),(5,2),(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(1,4),(2,4),(3,4),(4,4),(5,4),(2,5),(3,5),(4,5),(3,6)}
    for (i,j) in cells:
        x=ox+11+i*7; y=oy+11+j*7; b+=f'<path d="M{x-2.5} {y} H{x+2.5}" stroke="{a if (i,j)==(3,3) else INK}" stroke-width="4"/>'
    return b
# C · greca de hileras: la franja inferior del brocado (chevrones) hecha de hileras; el patrón corre en banda
def greca(c=True,ox=0,oy=0):
    a=COB if c else INK; b=''
    rows=[(0,[(32,8)]),(1,[(28,8),(36,8)]),(2,[(24,8),(40,8)]),(3,[(20,8),(44,8)]),(4,[(16,8),(32,6),(48,8)]),(5,[(28,8),(36,8)]),(6,[(32,8)])]
    for j,segs in rows:
        y=oy+16+j*5
        for (cx,l) in segs: b+=f'<path d="M{ox+cx-l/2} {y} H{ox+cx+l/2}" stroke="{a if (j,cx)==(4,32) else INK}" stroke-width="3"/>'
    return b
# D · retícula de rombos: los hilos en zigzag que al cruzarse hacen la red de rombos del brocado; un rombo lleno es el dato
def red(c=True,ox=0,oy=0):
    a=COB if c else INK
    z1=f'M{ox+4} {oy+20} L{ox+18} {oy+6} L{ox+32} {oy+20} L{ox+46} {oy+6} L{ox+60} {oy+20}'
    z2=f'M{ox+4} {oy+20} L{ox+18} {oy+34} L{ox+32} {oy+20} L{ox+46} {oy+34} L{ox+60} {oy+20}'
    z3=f'M{ox+4} {oy+48} L{ox+18} {oy+34} L{ox+32} {oy+48} L{ox+46} {oy+34} L{ox+60} {oy+48}'
    return f'<path d="{z1}" stroke="{INK}" stroke-width="2.5"/><path d="{z2}" stroke="{INK}" stroke-width="2.5"/><path d="{z3}" stroke="{INK}" stroke-width="2.5"/><path d="M{ox+32} {oy+23} L{ox+39} {oy+34} L{ox+32} {oy+45} L{ox+25} {oy+34} Z" fill="{a}"/>'
C={'A · rombo de hilos':rombo,'B · trama y urdimbre':trama,'C · greca de hileras':greca,'D · retícula de rombos':red}
def tile(fn,c=True): return svg(fn(c))
def patron(fn):  # 3×3 baldosas
    return svg(''.join(fn(i==1 and j==1, i*64, j*64) for i in range(3) for j in range(3)),'0 0 192 192')
sg=glob.glob(S+'/fuentes/SpaceGrotesk*')[0]
css=f'''@font-face{{font-family:SG;src:url("file://{sg}");font-weight:300 700}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 18px SG;margin:0 0 6px}} .sub{{color:#666;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-bottom:26px}}
.celda{{display:grid;gap:10px;align-content:start}} .celda svg{{display:block}} .big svg{{width:120px;height:120px}} .pat svg{{width:220px;height:220px;border-radius:12px;background:{PAPEL}}}
.s{{display:flex;gap:14px;align-items:center}} .s svg{{width:24px;height:24px}} .s .x svg{{width:16px;height:16px}}
.dark{{background:{INK};padding:10px;border-radius:10px;display:inline-flex;gap:10px}}
.lock{{display:flex;align-items:center;gap:12px}} .lock svg{{width:40px;height:40px}} .lock b{{font:700 32px SG;letter-spacing:-.02em}}
.tag{{font:400 12px system-ui;color:#666}}'''
def dark(s): return s.replace(f'stroke="{PAPEL}"','stroke="@A@"').replace(INK,PAPEL).replace('@A@',INK).replace(COB,COB_D)
cells=''
for name,fn in C.items():
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big">{tile(fn)}</div><div class="s">{tile(fn)}<span class="x">{tile(fn)}</span><span class="dark">{dark(tile(fn))}{dark(tile(fn,False))}</span></div><div class="pat">{patron(fn)}</div><div class="lock">{tile(fn)}<b>xila</b></div><span class="tag">baldosa · pequeño · oscuro · patrón 3×3 · con el nombre</span></div>'
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Xila · ronda 2 · patrón de hilos. El brocado se teje con hileras horizontales de distinto largo; una barra horizontal es exactamente eso. Cada concepto es una baldosa que se repite como patrón.</p><div class="fila">{cells}</div>')
print('ok')
