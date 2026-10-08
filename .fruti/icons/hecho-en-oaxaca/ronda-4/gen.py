# Hecho en Oaxaca · ronda 4: K2 en un solo color de tema (--oaxaca-color) + juegos bilingües con un solo OAXACA.
import sys, math
exec(open('../ronda-2/gen.py').read().split("OUT={}")[0])
C='var(--oaxaca-color,#e4007c)'; INK='currentColor'; M='var(--oaxaca-manta,#fff8ee)'
def k2(cx,cy,R,uid):
    sw=R*.07; out=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{M}"/>'
    out+=f'<clipPath id="c{uid}"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath><g clip-path="url(#c{uid})" fill="none" stroke="{C}" stroke-width="{R*.045:.2f}" stroke-opacity=".55">'
    for k in range(12):
        a=math.radians(k*15+7.5-90)
        if abs(a)>=math.pi/2: continue
        x=R*math.sin(a); s=1 if x>=0 else 0
        out+=f'<path d="M{cx} {cy-R}A{abs(x):.3f} {R} 0 0 {s} {cx} {cy+R}"/>'
    out+=f'</g><rect clip-path="url(#c{uid})" x="{cx-R}" y="{cy-R*.17:.2f}" width="{2*R}" height="{R*.34:.2f}" fill="{C}"/>'
    out+=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="{sw:.2f}"/>'
    sob=.3; s2=sw*1.2
    out+=(f'<path d="M{cx} {cy-R-R*sob:.2f}V{cy-R:.2f}M{cx} {cy+R:.2f}V{cy+R+R*sob:.2f}" stroke="{INK}" stroke-width="{s2:.2f}" stroke-linecap="round"/>'
          + ''.join(f'<rect x="{cx-R*.22:.2f}" y="{y-s2*.6:.2f}" width="{R*.44:.2f}" height="{s2*1.2:.2f}" rx="{s2*.6:.2f}" fill="{INK}"/>' for y in (cy-R,cy+R)))
    return out
def svg2(w,h,body,label): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" role="img" aria-label="{label}" style="color:#1a1210">{body}</svg>\n'
OUT={}
X=122
# L1 · barra: HECHO / MADE   EN / IN   OAXACA (una línea compacta encima de OAXACA)
d1,w1=texto('HECHO',20,X,60,800,78,48,1); dsl,wsl=texto('/',20,X+w1+5,60,500,78,48,0); d2,w2=texto('MADE',20,X+w1+5+wsl+5,60,800,78,48,1)
x3=X+w1+5+wsl+5+w2+12; d3,w3=texto('EN',20,x3,60,800,78,48,1); d4,w4=texto('/',20,x3+w3+5,60,500,78,48,0); d5,w5=texto('IN',20,x3+w3+5+w4+5,60,800,78,48,1)
do,wo=texto('OAXACA',48,X-2,108,850,75,48,0.5)
L1=f'<path fill="{INK}" d="{d1}{d3}"/><path fill="{INK}" fill-opacity=".38" d="{dsl}{d4}"/><path fill="{C}" d="{d2}{d5}"/><path fill="{INK}" d="{do}"/>'
OUT['l1-barra']=svg2(X+max(wo,x3+w3+5+w4+5+w5-X)+6,140,k2(55,70,44,'l1')+L1,'Hecho en Oaxaca / Made in Oaxaca')
# L2 · apilado: HECHO EN arriba (tinta), MADE IN debajo (color), ambos apuntan a un solo OAXACA
da,wa=texto('HECHO EN',19,X,44,800,78,48,1.4); db,wb=texto('MADE IN',19,X,66,800,78,48,1.4)
llave=f'<path d="M{X+max(wa,wb)+6:.1f} 30q6 0 6 6v8q0 4 4 6q-4 2-4 6v8q0 6-6 6" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" opacity=".5"/>'
do,wo=texto('OAXACA',48,X-2,114,850,75,48,0.5)
OUT['l2-apilado']=svg2(X+max(wo,max(wa,wb)+24)+6,140,k2(55,70,44,'l2')+f'<path fill="{INK}" d="{da}"/><path fill="{C}" d="{db}"/>'+llave+f'<path fill="{INK}" d="{do}"/>','Hecho en Oaxaca / Made in Oaxaca')
# L3 · giro: HECHO EN ↔ MADE IN se alternan como las caras de la marmota; OAXACA no se mueve. Quieto = L2.
gir=(f'<style>.g1,.g2{{transform-box:fill-box;transform-origin:center;animation:6s infinite}}.g1{{animation-name:ga}}.g2{{animation-name:gb}}'
     '@keyframes ga{0%,42%{transform:scaleY(1);opacity:1}50%,92%{transform:scaleY(0);opacity:0}100%{transform:scaleY(1);opacity:1}}'
     '@keyframes gb{0%,42%{transform:scaleY(0);opacity:0}50%,92%{transform:scaleY(1);opacity:1}100%{transform:scaleY(0);opacity:0}}'
     '@media (prefers-reduced-motion:reduce){.g1,.g2{animation:none}.g2{transform:none;opacity:1}}</style>')
dA,wA=texto('HECHO EN',26,X,62,800,78,48,1.4); dB,wB=texto('MADE IN',26,X,62,800,78,48,1.4)
OUT['l3-giro']=svg2(X+max(wo,wA)+6,140,gir+k2(55,70,44,'l3')+f'<path class="g1" fill="{INK}" d="{dA}"/><path class="g2" fill="{C}" d="{dB}"/><path fill="{INK}" d="{do}"/>','Hecho en Oaxaca / Made in Oaxaca')
OUT['icono']=svg2(110,140,k2(55,70,44,'ic'),'Hecho en Oaxaca')
for k,s in OUT.items(): open(f'{k}.svg','w').write(s)
TEMAS=[('rosa mexicano','#e4007c'),('grana','#a3123a'),('turquesa','#00838a'),('añil','#2f4bb7'),('cempasúchil','#d97a00')]
def inl(f,h,var): return f'<span style="display:inline-flex;--oaxaca-color:{var}">'+open(f).read().replace('<svg ',f'<svg height="{h}" ',1)+'</span>'
rows=''.join(f'<section style="display:flex;gap:22px;align-items:center;padding:14px 20px;border-bottom:1px solid #eadfce"><b style="width:90px;font:600 12px sans-serif;color:#7a6650">{k}</b>{inl(k+".svg",110,"#e4007c")}{inl(k+".svg",48,"#e4007c")}</section>' for k in ('l1-barra','l2-apilado','l3-giro'))
rows+='<section style="display:flex;gap:14px;align-items:center;padding:14px 20px;flex-wrap:wrap"><b style="width:90px;font:600 12px sans-serif;color:#7a6650">color del tema</b>'+''.join(f'<span style="display:inline-flex;flex-direction:column;align-items:center;font:11px sans-serif;color:#7a6650">{inl("icono.svg",80,c)}{n}</span>' for n,c in TEMAS)+'</section>'
open('banco.html','w').write(f'<html><body style="margin:0;background:#fbf5ea">{rows}</body></html>')
print('ok')
