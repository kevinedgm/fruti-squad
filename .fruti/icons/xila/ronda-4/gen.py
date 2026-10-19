# Xila · ronda 4: bordado. El punto de cruz es una X (la inicial) y una cuadrícula de puntos es una matriz de datos.
import sys,glob
S=sys.argv[1]; INK='#15171f'; PAPEL='#f7f5f0'; COB='#1f4bd8'; COB_D='#7a9bff'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round">{body}</svg>'
def cruz(x,y,c,s=2.4,w=1.9): return f'<path d="M{x-s} {y-s} L{x+s} {y+s} M{x+s} {y-s} L{x-s} {y+s}" stroke="{c}" stroke-width="{w}"/>'
def grid(cells,acc,ox=0,oy=0,pitch=6,dark=False,x0=5,y0=5):
    ink=PAPEL if dark else INK; cob=COB_D if dark else COB; b=''
    for (i,j) in cells: b+=cruz(ox+x0+i*pitch,oy+y0+j*pitch,cob if (i,j) in acc else ink)
    return b
# H · rombo en punto de cruz: el motivo mínimo del huipil hecho de X; una X en cobalto es el dato
ROMBO={(i,j) for i in range(9) for j in range(9) if abs(i-4)+abs(j-4) in (4,) } | {(i,j) for i in range(9) for j in range(9) if abs(i-4)+abs(j-4)==1} | {(4,4)}
def rombo(dark=False,ox=0,oy=0): return grid(ROMBO,{(4,4)},ox,oy,6,dark,8,8)
# I · flor bordada: flor de ocho puntas en punto de cruz (San Antonino / Istmo, estilizada); el centro en cobalto
FLOR=set()
for i in range(9):
    for j in range(9):
        d=abs(i-4)+abs(j-4); e=max(abs(i-4),abs(j-4))
        if d<=2 or (e==3 and (i==4 or j==4)) or (abs(i-4)==abs(j-4)==3) or (e==4 and (i==4 or j==4)): FLOR.add((i,j))
def flor(dark=False,ox=0,oy=0): return grid(FLOR,{(4,4)},ox,oy,6,dark,8,8)
# J · greca bordada: la greca escalonada de Mitla en punto de cruz; la última X, en cobalto, es el último valor (anatomía de Xila)
GRECA={(0,8),(1,8),(2,8),(2,7),(2,6),(3,6),(4,6),(4,5),(4,4),(5,4),(6,4),(6,3),(6,2),(7,2),(8,2),(8,1),(8,0)}
def greca(dark=False,ox=0,oy=0): return grid(GRECA,{(8,0)},ox,oy,6,dark,8,8)
# K · cadenilla: el hilo de cadeneta del Istmo es una línea que termina en una flor de puntos (el hallazgo)
def cadenilla(dark=False,ox=0,oy=0):
    ink=PAPEL if dark else INK; cob=COB_D if dark else COB; b=''
    pts=[(8,48),(16,40),(24,44),(32,30),(40,34),(48,20)]
    for k in range(len(pts)-1):
        (x0,y0),(x1,y1)=pts[k],pts[k+1]; mx,my=(x0+x1)/2,(y0+y1)/2
        b+=f'<ellipse cx="{ox+mx}" cy="{oy+my}" rx="5.2" ry="2.6" transform="rotate({-45 if y1<y0 else 30} {ox+mx} {oy+my})" stroke="{ink}" stroke-width="1.9"/>'
    for (i,j) in [(0,0),(1,0),(-1,0),(0,1),(0,-1)]: b+=cruz(ox+50+i*5,oy+18+j*5,cob if (i,j)==(0,0) else ink,2,1.8)
    return b
C={'H · rombo en punto de cruz':rombo,'I · flor bordada':flor,'J · greca bordada':greca,'K · cadenilla':cadenilla}
sg=glob.glob(S+'/fuentes/SpaceGrotesk*')[0]
css=f'''@font-face{{font-family:SG;src:url("file://{sg}");font-weight:300 700}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 18px SG;margin:0 0 6px}} .sub{{color:#666;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-bottom:26px}}
.celda{{display:grid;gap:10px;align-content:start}} .celda svg{{display:block}} .big svg{{width:120px;height:120px}} .pat svg{{width:220px;height:110px;border-radius:12px;background:{PAPEL}}}
.s{{display:flex;gap:14px;align-items:center}} .s svg{{width:24px;height:24px}} .s .x svg{{width:16px;height:16px}}
.dark{{background:{INK};padding:10px;border-radius:10px;display:inline-flex;gap:10px}}
.lock{{display:flex;align-items:center;gap:12px}} .lock svg{{width:40px;height:40px}} .lock b{{font:700 32px SG;letter-spacing:-.02em}}
.tag{{font:400 12px system-ui;color:#666}}'''
def tile(fn,dark=False): return svg(fn(dark))
def banda(fn): return svg(''.join(fn(False,i*64,0) for i in range(4)),'0 0 256 64')
cells=''
for name,fn in C.items():
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big">{tile(fn)}</div><div class="s">{tile(fn)}<span class="x">{tile(fn)}</span><span class="dark">{tile(fn,True)}</span></div><div class="pat">{banda(fn)}</div><div class="lock">{tile(fn)}<b>xila</b></div><span class="tag">baldosa · 24 · 16 · oscuro · banda bordada · con el nombre</span></div>'
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Xila · ronda 4 · bordado. El punto de cruz es una X (la inicial de Xila) y una cuadrícula de puntos es una matriz de datos. Cada motivo también corre como banda, igual que en un huipil.</p><div class="fila">{cells}</div>')
print('ok')
