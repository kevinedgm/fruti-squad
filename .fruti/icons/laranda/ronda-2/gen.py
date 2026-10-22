# Laranda · ronda 2 · abstracta (usuario: «disruptivos, no literales, modernos»). Florecer sin dibujar flores:
# algo cerrado que se abre, una pieza que se separa (el rasgo obligatorio del brief) y un centro vacío (el punto que se llena).
import sys,math
S=sys.argv[1]; INK='#1C1917'; CREMA='#FAF8F5'; VIO='#6B4FA0'; LILA='#B8A9E0'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
def arc(cx,cy,r,a0,a1,sw,k):
    p=lambda a:(cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a)))
    x0,y0=p(a0); x1,y1=p(a1); big=1 if (a1-a0)%360>180 else 0
    return f'<path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f}" stroke="{k}" stroke-width="{sw}"/>'
# A · el disco que se abre: un disco sólido con un sector que se desprende y gira; centro vacío
def disco(k=INK,f=CREMA):
    cx,cy=32,34; r=22
    def sector(a0,a1,dx=0,dy=0,rot=0):
        p=lambda a:(cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a)))
        x0,y0=p(a0); x1,y1=p(a1); big=1 if (a1-a0)>180 else 0
        return f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {big} 1 {x1:.1f} {y1:.1f}Z" fill="{k}" transform="translate({dx} {dy}) rotate({rot} {cx} {cy})"/>'
    return svg(sector(-20,290)+sector(-70,-20,3.5,-4,10)+f'<circle cx="{cx}" cy="{cy}" r="6" fill="{f}"/>')
# B · el anillo que se abre: anillo grueso con un segmento que se separa hacia fuera; el hueco es el centro
def anillo(k=INK,f=CREMA):
    return svg(arc(32,34,19,10,300,9,k)+f'<g transform="translate(3 -4)">{arc(32,34,19,-50,0,9,k)}</g>')
# C · cuadrantes: cuatro pastillas alrededor de un centro vacío; una se desplaza en diagonal (se abre)
def cuadrantes(k=INK,f=CREMA):
    b=''
    for i,(x,y) in enumerate(((14,16),(34,16),(14,36),(34,36))):
        dx,dy=(3,-3) if i==1 else (0,0)
        b+=f'<rect x="{x+dx}" y="{y+dy}" width="16" height="16" rx="7" fill="{k}"/>'
    return svg(b)
# D · la l que brota: el asta de la l y, separado, un brote redondo que se eleva; el punto negativo va en el brote
def ele(k=INK,f=CREMA):
    return svg(f'<rect x="25" y="22" width="11" height="34" rx="5.5" fill="{k}"/><circle cx="38" cy="14" r="8" fill="{k}"/><circle cx="38" cy="14" r="2.6" fill="{f}"/>')
# E · dos arcos: una forma cerrada (paréntesis) que se abre: el arco derecho se separa; punto al centro
def arcos(k=INK,f=CREMA):
    return svg(arc(32,34,16,110,250,8,k)+f'<g transform="translate(5 -3)">{arc(32,34,16,-70,70,8,k)}</g><circle cx="33" cy="33" r="3.2" fill="{k}"/>')
T={'A · el disco que se abre':disco,'B · el anillo que se abre':anillo,'C · cuadrantes':cuadrantes,'D · la l que brota':ele,'E · dos arcos':arcos}
fr=S+'/fuentes/Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf'; mr=S+'/fuentes/Manrope[wght].ttf'
css=f'''@font-face{{font-family:FR;src:url("file://{fr}");font-weight:100 900}} @font-face{{font-family:MR;src:url("file://{mr}");font-weight:200 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 MR,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 16px MR;margin:0 0 8px}} .sub{{color:#57534E;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-bottom:20px}}
.celda{{background:{CREMA};padding:14px;border-radius:12px;border:1px solid #F0EBE3;display:grid;gap:10px;align-content:start}} svg{{display:block}}
.big svg{{width:140px;height:140px}} .s{{display:flex;gap:10px;align-items:flex-end}} .s span{{display:block}} .s svg{{width:100%;height:100%}}
.dark{{background:{INK};padding:8px;border-radius:8px;display:inline-flex;gap:8px;align-items:flex-end}} .vio{{background:{VIO};padding:8px;border-radius:8px;display:inline-flex;gap:8px;align-items:flex-end}}
.lock{{display:flex;align-items:center;gap:10px}} .lock svg{{width:40px;height:40px}} .f1{{font:600 34px/1 FR;font-variation-settings:"opsz" 72,"SOFT" 60}} .f2{{font:600 32px/1 MR;letter-spacing:-.02em}}
.tag{{font:400 12px MR;color:#57534E}}
.app{{display:flex;gap:16px;align-items:flex-end}} .app span{{display:block;overflow:hidden}} .app svg{{width:100%;height:100%}}'''
def inv(s,bg=INK): return s.replace(f'fill="{CREMA}"','fill="@F@"').replace(INK,CREMA).replace('@F@',bg)
def app(fn,r=112): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="{r}" fill="{VIO}"/><g fill="none" stroke-linecap="round" stroke-linejoin="round" transform="translate(64 64) scale(6)">{fn(CREMA,VIO).split(">",1)[1].rsplit("</svg>",1)[0]}</g></svg>'
cells=''
for name,fn in T.items():
    s=fn()
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big">{s}</div><div class="s"><span style="width:48px;height:48px">{s}</span><span style="width:32px;height:32px">{s}</span><span style="width:16px;height:16px">{s}</span><span class="dark"><span style="width:40px;height:40px">{inv(s)}</span><span style="width:16px;height:16px">{inv(s)}</span></span></div><div class="app"><span style="width:64px;height:64px">{app(fn)}</span><span style="width:48px;height:48px">{app(fn)}</span><span style="width:40px;height:40px;border-radius:50%">{app(fn,256)}</span></div><div class="lock">{s}<span class="f1">laranda</span></div><div class="lock">{s}<span class="f2">laranda</span></div></div>'
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Laranda · ronda 2 · abstracta. Florecer sin flor: algo cerrado que se abre, una pieza que se separa, un centro vacío. Tinta sobre crema; crema sobre tinta; app icon en Violeta Laranda; lockup con Fraunces y con Manrope.</p><div class="fila">{cells}</div>')
print('ok')
