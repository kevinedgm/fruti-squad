# Hecho en Oaxaca · ronda 3: K con eje, banda y manta blanca; con y sin texto.
import sys, math
exec(open('../ronda-2/gen.py').read().split("OUT={}")[0])
K_COL=[ROSA,MANTA,'#00a3a3',MANTA,'#f2b200',MANTA,'#7b3fb3',MANTA,'#f26419',MANTA,ROSA,MANTA]
def gajos2(cx,cy,R,rot,colores):
    out=''
    for k in range(-1,13):
        a=math.radians(k*15+rot-90); b=math.radians((k+1)*15+rot-90); a=max(a,-math.pi/2); b=min(b,math.pi/2)
        if b<=a: continue
        xa,xb=R*math.sin(a),R*math.sin(b); sa=1 if xa>=0 else 0; sb=0 if xb>=0 else 1
        out+=f'<path d="M{cx} {cy-R}A{abs(xa):.3f} {R} 0 0 {sa} {cx} {cy+R}A{abs(xb):.3f} {R} 0 0 {sb} {cx} {cy-R}Z" fill="{colores[k%len(colores)]}"/>'
    return out
def meridianos(cx,cy,R,rot,sw,color):
    out=''
    for k in range(0,12):
        a=math.radians(k*15+rot-90)
        if abs(a)>=math.pi/2: continue
        x=R*math.sin(a); s=1 if x>=0 else 0
        out+=f'<path d="M{cx} {cy-R}A{abs(x):.3f} {R} 0 0 {s} {cx} {cy+R}"/>'
    return f'<g fill="none" stroke="{color}" stroke-width="{sw:.2f}">{out}</g>'
def eje(cx,cy,R,sw,color=TINTA,sob=.3):
    return (f'<path d="M{cx} {cy-R-R*sob:.2f}V{cy-R:.2f}M{cx} {cy+R:.2f}V{cy+R+R*sob:.2f}" stroke="{color}" stroke-width="{sw:.2f}" stroke-linecap="round"/>'
            + ''.join(f'<rect x="{cx-R*.22:.2f}" y="{y-sw*.6:.2f}" width="{R*.44:.2f}" height="{sw*1.2:.2f}" rx="{sw*.6:.2f}" fill="{color}"/>' for y in (cy-R,cy+R)))
def banda(cx,cy,R,h,color,uid):
    return f'<clipPath id="b{uid}"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath><rect clip-path="url(#b{uid})" x="{cx-R}" y="{cy-h/2:.2f}" width="{2*R}" height="{h:.2f}" fill="{color}"/>'
def picados(cx,y,R,n,t):
    # guirnalda bajo la banda: n triángulos de papel picado
    out=''; xs=[cx-R*.62+i*(R*1.24)/(n-1) for i in range(n)]
    for i,x in enumerate(xs): out+=f'<path d="M{x-t:.2f} {y:.2f}H{x+t:.2f}L{x:.2f} {y+t*1.25:.2f}Z" fill="{PICADO[i%5]}"/>'
    return out
def marca(v,cx,cy,R,uid):
    sw=R*.07
    if v=='k1':   # husos de color + banda tinta + eje
        b=f'<clipPath id="c{uid}"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath><g clip-path="url(#c{uid})">{gajos2(cx,cy,R,7.5,K_COL)}</g>'
        b+=banda(cx,cy,R,R*.34,TINTA,uid)
    elif v=='k2': # manta blanca, costillas de color finas, banda rosa
        b=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{MANTA}"/>'
        b+=f'<clipPath id="c{uid}"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath><g clip-path="url(#c{uid})">'
        for i,col in enumerate(PICADO+PICADO[:1]):
            b+=meridianos(cx,cy,R,7.5+i*0,R*.11,col).replace('<g ',f'<g opacity="1" ') if False else ''
        # 12 costillas, cada una de un color del papel picado
        for k in range(12):
            a=math.radians(k*15+7.5-90)
            if abs(a)>=math.pi/2: continue
            x=R*math.sin(a); s=1 if x>=0 else 0
            b+=f'<path d="M{cx} {cy-R}A{abs(x):.3f} {R} 0 0 {s} {cx} {cy+R}" fill="none" stroke="{PICADO[k%5]}" stroke-width="{R*.045:.2f}"/>'
        b+='</g>'+banda(cx,cy,R,R*.34,ROSA,uid)
    else:         # k3 = k2 + guirnalda de papel picado bajo la banda
        b=marca('k2',cx,cy,R,uid+'x')[0]
        b+=picados(cx,cy+R*.17,R,5,R*.13)
        return b,sw
    return b,sw
def completa(v,cx,cy,R,uid):
    b,sw=marca(v,cx,cy,R,uid)
    return b+f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{TINTA}" stroke-width="{sw:.2f}"/>'+eje(cx,cy,R,sw*1.2)
OUT={}
for v in ('k1','k2','k3'):
    OUT[f'{v}-icono']=svg(110,140,completa(v,55,70,44,v))
    dh,wh=texto('HECHO EN',22,124,60,800,78,48,1.2); do,wo=texto('OAXACA',46,122,104,850,75,48,0.5); dm,wm=texto('MADE IN OAXACA',12.5,124,124,650,90,14,1.6)
    OUT[f'{v}-sello']=svg(128+max(wh,wo,wm),140,completa(v,55,70,44,v+'s')+f'<path fill="{TINTA}" d="{dh}"/><path fill="{ROSA}" d="{do}"/><path fill="{TINTA}" fill-opacity=".7" d="{dm}"/>')
for k,s in OUT.items(): open(f'{k}.svg','w').write(s)
def r(f,h): return f'<img src="{f}" style="height:{h}px">'
rows=''.join(f'<section style="display:flex;gap:22px;align-items:center;padding:14px 20px;border-bottom:1px solid #eadfce"><b style="width:30px;font:600 13px sans-serif;color:#7a6650">{v.upper()}</b>{r(v+"-icono.svg",120)}{r(v+"-icono.svg",48)}{r(v+"-icono.svg",24)}{r(v+"-sello.svg",96)}<span style="background:#1a1210;padding:8px;border-radius:8px;display:inline-flex">{r(v+"-icono.svg",64)}</span></section>' for v in ('k1','k2','k3'))
open('banco.html','w').write(f'<html><body style="margin:0;background:#fbf5ea">{rows}</body></html>')
print('ok')
