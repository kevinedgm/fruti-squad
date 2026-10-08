# Ronda 5: «en oscuro parece cebolla». Variantes de la espiga.
import math
C='var(--oaxaca-color,#e4007c)'; INK='currentColor'; M='var(--oaxaca-manta,#fff8ee)'
def esfera(cx,cy,R,uid):
    sw=R*.07; out=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{M}"/><clipPath id="c{uid}"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath><g clip-path="url(#c{uid})" fill="none" stroke="{C}" stroke-width="{R*.045:.2f}" stroke-opacity=".55">'
    for k in range(12):
        a=math.radians(k*15+7.5-90)
        if abs(a)>=math.pi/2: continue
        x=R*math.sin(a); s=1 if x>=0 else 0
        out+=f'<path d="M{cx} {cy-R}A{abs(x):.3f} {R} 0 0 {s} {cx} {cy+R}"/>'
    out+=f'</g><rect clip-path="url(#c{uid})" x="{cx-R}" y="{cy-R*.17:.2f}" width="{2*R}" height="{R*.34:.2f}" fill="{C}"/><circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="{sw:.2f}"/>'
    return out,sw
def espiga(cx,cy,R,sw,color,grosor=1.2,largo=.3,disco=.22,hueco=0):
    s2=sw*grosor; g=hueco*R
    top=f'M{cx} {cy-R-g-R*largo:.2f}V{cy-R-g:.2f}'; bot=f'M{cx} {cy+R+g:.2f}V{cy+R+g+R*largo:.2f}'
    discos=''.join(f'<rect x="{cx-R*disco:.2f}" y="{y-s2*.6:.2f}" width="{2*R*disco:.2f}" height="{s2*1.2:.2f}" rx="{s2*.6:.2f}" fill="{color}"/>' for y in (cy-R-g,cy+R+g))
    return f'<path d="{top}{bot}" stroke="{color}" stroke-width="{s2:.2f}" stroke-linecap="round"/>'+discos
V={}
def mk(n,**k):
    b,sw=esfera(55,72,44,n); V[n]=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 110 144" role="img" aria-label="Hecho en Oaxaca">{b}{espiga(55,72,44,sw,**k)}</svg>\n'
mk('d0-actual',color=INK)
mk('d1-color',color=C)
mk('d2-estructura',color=INK,grosor=1.9,largo=.42,disco=.34,hueco=.05)
mk('d3-estructura-color',color=C,grosor=1.9,largo=.42,disco=.34,hueco=.05)
for k,s in V.items(): open(f'{k}.svg','w').write(s)
def r(f,h,bg,col): return f'<span style="display:inline-flex;padding:10px;background:{bg};color:{col};border-radius:10px">'+open(f).read().replace('<svg ',f'<svg height="{h}" ',1)+'</span>'
rows=''.join(f'<section style="display:flex;gap:14px;align-items:center;padding:12px 18px;border-bottom:1px solid #33261f"><b style="width:150px;font:600 12px sans-serif;color:#bfae9f">{k}</b>{r(k+".svg",120,"#1a1210","#fff8ee")}{r(k+".svg",48,"#1a1210","#fff8ee")}{r(k+".svg",28,"#1a1210","#fff8ee")}{r(k+".svg",48,"#fbf5ea","#1a1210")}</section>' for k in V)
open('banco.html','w').write(f'<html><body style="margin:0;background:#120c0a">{rows}</body></html>')
