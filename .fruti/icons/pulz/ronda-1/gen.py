# PULZ · ronda 1 de símbolo. Lienzo 64. Paleta nueva del palenque.
import math
MAGUEY='#2f5d58'; COBRE='#b4582f'; CAL='#f4efe6'; TIERRA='#2a211c'
def svg(body,label='PULZ'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="{label}">{body}</svg>\n'
def penca(bx,by,ang,L,W,color):
    a=math.radians(ang-90); ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux
    tip=(bx+ux*L,by+uy*L); c1=(bx+ux*L*.35+px*W,by+uy*L*.35+py*W); c2=(bx+ux*L*.35-px*W,by+uy*L*.35-py*W)
    f=lambda p:'%.2f %.2f'%p
    return f'<path d="M{f((bx+px*W*.55,by+py*W*.55))}Q{f(c1)} {f(tip)}Q{f(c2)} {f((bx-px*W*.55,by-py*W*.55))}Z" fill="{color}"/>'
V={}
# A · pencas-datos: roseta de 5 pencas de alturas distintas (como barras), base común; la central lleva punta de cobre
alt=[0.62,0.86,1.0,0.78,0.56]; angs=[-52,-26,0,26,52]
body=''.join(penca(32,54,a,40*h,5.6 if i!=2 else 6.2,MAGUEY) for i,(a,h) in enumerate(zip(angs,alt)))
body+=f'<circle cx="32" cy="{54-40+1.5}" r="2.4" fill="{COBRE}"/>'
body+=f'<rect x="14" y="54" width="36" height="4" rx="2" fill="{TIERRA}"/>'
V['a-pencas']=svg(body)
# B · traza: una «P» dibujada como la ruta de un lote, con paradas
P='M22 56V12H36C45 12 50 17.5 50 25C50 32.5 45 38 36 38H22'
paradas=[(22,56),(22,34),(22,12),(50,25),(36,38)]
body=f'<path d="{P}" fill="none" stroke="{MAGUEY}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
for i,(x,y) in enumerate(paradas):
    last=i==len(paradas)-1
    body+=f'<circle cx="{x}" cy="{y}" r="{5.2 if last else 4}" fill="{COBRE if last else CAL}" stroke="{TIERRA if not last else COBRE}" stroke-width="{2.6 if not last else 0}"/>'
V['b-traza']=svg(body)
# C · piña jimada: óvalo con rombos de las pencas cortadas y tres muñones arriba
clip='<clipPath id="pc"><ellipse cx="32" cy="38" rx="20" ry="18"/></clipPath>'
lat=''
for k in range(-6,7):
    lat+=f'<path d="M{32+k*8-24} 14L{32+k*8+24} 62M{32+k*8+24} 14L{32+k*8-24} 62"/>'
body=(clip+f'<ellipse cx="32" cy="38" rx="20" ry="18" fill="{MAGUEY}"/>'
      f'<g clip-path="url(#pc)" fill="none" stroke="{CAL}" stroke-width="1.6" opacity=".55">{lat}</g>'
      + ''.join(f'<path d="M{x} 21L{x+d} 8" stroke="{MAGUEY}" stroke-width="4.5" stroke-linecap="round"/>' for x,d in ((26,-4),(32,0),(38,4)))
      + f'<path d="M24 22H40" stroke="{COBRE}" stroke-width="3" stroke-linecap="round"/>')
V['c-pina']=svg(body)
for k,s in V.items(): open(f'{k}.svg','w').write(s)
def img(f,h,style=''): return f'<span style="display:inline-flex;{style}"><img src="{f}" style="height:{h}px"></span>'
def tile(f,h,bg): return f'<span style="display:inline-flex;width:{h}px;height:{h}px;border-radius:{h*.22}px;background:{bg};align-items:center;justify-content:center"><img src="{f}" style="height:{h*.7}px"></span>'
rows=''
for k in V:
    rows+=(f'<section style="display:flex;gap:18px;align-items:center;padding:14px 18px;border-bottom:1px solid #e3dccf"><b style="width:80px;font:600 12px sans-serif;color:#6b5d50">{k}</b>'
           +img(k+'.svg',128)+img(k+'.svg',48)+img(k+'.svg',24)+img(k+'.svg',16)+tile(k+'.svg',64,CAL)+tile(k+'.svg',64,'#ffffff')+
           f'<span style="display:inline-flex;gap:6px;align-items:center;font:600 13px sans-serif;color:{TIERRA};border:1px solid #e3dccf;border-radius:999px;padding:4px 10px 4px 6px;background:#fff">{img(k+".svg",18)}hecho con PULZ</span></section>')
open('banco.html','w').write(f'<html><body style="margin:0;background:{CAL}">{rows}</body></html>')
