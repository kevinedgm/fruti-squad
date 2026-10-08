import math
CX,CY,RX,RY=12,12,9,7.25
def ey(x): return RY*math.sqrt(1-((x-CX)/RX)**2)
def ex(y): return RX*math.sqrt(1-((y-CY)/RY)**2)
inset=.35
def svg(id_,body,extra=''):
  return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="uva-icon uva-{id_}" aria-hidden="true">\n'
          f'  <style>.uva-{id_}{{stroke-width:var(--uva-stroke,2)}}</style>\n'
          f'  <ellipse class="uva-{id_}__contorno" cx="{CX}" cy="{CY}" rx="{RX}" ry="{RY}"/>\n{body}{extra}</svg>\n')
V={}
xv=9; top=CY-ey(xv)+inset; bot=CY+ey(xv)-inset; yh=11; rgt=CX+ex(yh)-inset
V['v1-columna']=f'  <path class="uva-v1-columna__eje" d="M{xv} {top:.2f}V{bot:.2f}"/>\n  <path class="uva-v1-columna__fila" d="M{xv} {yh}H{rgt:.2f}"/>\n'
V['v2-cruz']=f'  <path class="uva-v2-cruz__eje" d="M12 {CY-RY+inset:.2f}V{CY+RY-inset:.2f}"/>\n  <path class="uva-v2-cruz__fila" d="M{CX-RX+inset:.2f} 12H{CX+RX-inset:.2f}"/>\n'
V['v3-flotante']='  <path class="uva-v3-flotante__eje" d="M9.5 9V15"/>\n  <path class="uva-v3-flotante__fila" d="M9.5 12H15.5"/>\n'
for k,body in V.items(): open(f'{k}.svg','w').write(svg(k,body))
open('v1-columna.small.svg','w').write(svg('v1-columna',f'  <path class="uva-v1-columna__eje" d="M{xv} {top:.2f}V{bot:.2f}"/>\n'))
x2=15; b2=CY+ey(x2)-inset
open('v1-columna.large.svg','w').write(svg('v1-columna',V['v1-columna'],f'  <path class="uva-v1-columna__secundaria" d="M{x2} {yh}V{b2:.2f}"/>\n'))
