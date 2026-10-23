import math,random
INK='#1C1917'; BG='#FAF8F5'
J=(44,94)
def wing(L,ang,wmax,bend=0.0,peak=0.62,n=36,seed=None,amp=0):
    # centro: recta desde J en ángulo (grados desde la vertical, + a la derecha) con una curva lateral «bend»
    r=random.Random(seed) if seed is not None else None
    ph1,ph2=(r.random(),r.random()) if r else (0,0)
    a=math.radians(ang); ux,uy=math.sin(a),-math.cos(a); px,py=uy,-ux   # px,py perpendicular
    left=[];right=[]
    for i in range(n+1):
        t=i/n; s=L*t; b=bend*L*math.sin(math.pi*t)
        cx=J[0]+ux*s+px*b; cy=J[1]+uy*s+py*b
        # ancho: estrecho en la base, máximo en peak, punta redondeada
        w=wmax*(math.sin(math.pi*min(t/peak,1)*0.5) if t<peak else math.cos(math.pi*0.5*(t-peak)/(1-peak)))
        w=max(w,0.6)
        j=(amp*(math.sin(2*math.pi*(1.3*t+ph1))+0.3*math.sin(2*math.pi*(2.2*t+ph2))) if r else 0)
        left.append((cx+px*(w+j),cy+py*(w+j))); right.append((cx-px*(w+j),cy-py*(w+j)))
    pts=left+right[::-1]
    return 'M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)+'Z'
W1=wing(82,14,13,bend=0.05)     # ala grande: 82 de largo, 14° a la derecha, ancho máx 13
W2=wing(70,96,9,bend=-0.03)     # ala chica: 70 de largo, casi horizontal cayendo
def svg(body,size=128): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}">{body}</svg>'
dot=lambda r=7: f'<circle cx="{J[0]}" cy="{J[1]}" r="{r}" fill="{BG}"/>'
C={}
C['A']=('Huella',f'<g fill="{INK}"><path d="{W1}"/><path d="{W2}"/></g>{dot(7.5)}','Dos alas sólidas; el punto es el hueco donde se tocan. La más silenciosa.')
C['B']=('Contorno',f'<g fill="none" stroke="{INK}" stroke-width="6.5" stroke-linejoin="round"><path d="{W1}"/><path d="{W2}"/></g>{dot(10)}<circle cx="{J[0]}" cy="{J[1]}" r="5.5" fill="none" stroke="{INK}" stroke-width="5"/>','Alas en línea y anillo en el centro. Más ligera, más «taller».')
C['C']=('Tinta',f'<path d="{wing(82,14,13,bend=0.05,seed=3,amp=0.8)}" fill="none" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/><path d="{wing(70,96,9,bend=-0.03,seed=5,amp=0.6)}" fill="{INK}"/>{dot(9)}<circle cx="{J[0]}" cy="{J[1]}" r="5" fill="none" stroke="{INK}" stroke-width="4.5"/>','Una ala a mano, abierta; la otra llena, la que se posa. Línea y masa como en Laranda.')
C['D']=('Ala mínima',f'<path d="{wing(84,14,13,bend=0.05)}" fill="{INK}"/><path d="M58 100 L118 104" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round" stroke-dasharray="0.1 13"/>{dot(7.5)}<circle cx="{J[0]}" cy="{J[1]}" r="5" fill="none" stroke="{INK}" stroke-width="4.5"/>','Una sola ala y la línea de vuelo punteada como pie de la L. La huella, no el insecto.')
C['E']=('Posada',f'<g fill="{INK}"><path d="{wing(104,18,8,peak=0.6)}" transform="translate({-22*math.sin(math.radians(18)):.1f} {22*math.cos(math.radians(18)):.1f})"/><path d="{wing(92,97,6.5,peak=0.6)}" transform="translate({-20*math.sin(math.radians(97)):.1f} {20*math.cos(math.radians(97)):.1f})"/></g>{dot(7)}','Dos alas finas que se cruzan y pivotan en el punto. La más cercana al insecto sin dibujarlo.')
open('banco.html','w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:{BG};color:{INK};font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 24px;color:#57534E}}
.g{{display:grid;grid-template-columns:repeat(5,1fr);gap:24px}}.c{{display:grid;gap:10px;justify-items:center;text-align:center}}
.big svg{{width:200px;height:200px;display:block}}.sm{{display:flex;gap:14px;align-items:flex-end}}.sm span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#57534E}}
.inv{{background:{INK};border-radius:12px;padding:10px}}.inv svg path{{fill:{BG}}}.inv svg [fill="none"]{{fill:none}}.inv svg [stroke="{INK}"]{{stroke:{BG}}}.inv svg circle[fill="{BG}"]{{fill:{INK}}}
.c h2{{font:600 16px sans-serif;margin:6px 0 0}}.c p{{margin:0;color:#57534E;font-size:13px;max-width:220px}}
</style></head><body><h1>Libela · ronda 1 · símbolo en blanco y negro</h1><p class="i">Dos alas asimétricas que forman una L y un punto negativo. Cada ruta a 200 px, a 16 y 32 px reales, y en negativo.</p><div class="g">'''+''.join(f'<div class="c"><div class="big">{svg(b)}</div><div class="sm"><span>{svg(b,16)}16</span><span>{svg(b,32)}32</span><span class="inv">{svg(b,48)}</span></div><h2>{k} · {n}</h2><p>{t}</p></div>' for k,(n,b,t) in C.items())+'</div></body></html>')
for k,(n,b,t) in C.items(): open(f'{k}.svg','w').write(svg(b))
print('ok')
