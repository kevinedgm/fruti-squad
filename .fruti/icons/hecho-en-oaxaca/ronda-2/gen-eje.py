# Variantes sin «paleta»: sin mástil, o con el eje atravesando la esfera (discos arriba y abajo).
import sys, re
exec(open('gen.py').read())
OUT={}
def eje(cx,cy,R,sw,color=TINTA,sobresale=.32):
    t=cy-R-R*sobresale; b=cy+R+R*sobresale
    return (f'<path d="M{cx} {t:.2f}V{b:.2f}" stroke="{color}" stroke-width="{sw:.2f}" stroke-linecap="round"/>'
            f'<rect x="{cx-R*.2:.2f}" y="{cy-R-sw*.55:.2f}" width="{R*.4:.2f}" height="{sw*1.1:.2f}" rx="{sw*.55:.2f}" fill="{color}"/>'
            f'<rect x="{cx-R*.2:.2f}" y="{cy+R-sw*.55:.2f}" width="{R*.4:.2f}" height="{sw*1.1:.2f}" rx="{sw*.55:.2f}" fill="{color}"/>')
# K
def k(cx,cy,R): return f'<clipPath id="kc{cx}"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath><g clip-path="url(#kc{cx})">{gajos(cx,cy,R,7.5,K_COL)}</g><circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{TINTA}" stroke-width="{R*.06:.2f}"/>'
OUT['k-sin']=svg(100,100,k(50,50,44))
OUT['k-eje']=svg(100,130,k(50,65,44)+eje(50,65,44,4.6))
# O (solo el icono)
def o(cx,cy,R,sw): return (f'<circle cx="{cx}" cy="{cy}" r="{R-sw/2:.2f}" fill="none" stroke="{TINTA}" stroke-width="{sw:.2f}"/>'
                          f'<ellipse cx="{cx}" cy="{cy}" rx="{(R-sw/2)*.42:.2f}" ry="{R-sw/2:.2f}" fill="none" stroke="{ROSA}" stroke-width="{sw*.42:.2f}"/>')
OUT['o-sin']=svg(100,100,o(50,50,44,12))
OUT['o-eje']=svg(100,130,o(50,65,44,12)+f'<path d="M50 9V21M50 109V121" stroke="{ROSA}" stroke-width="5.2" stroke-linecap="round"/>')
# T
def t(cx,cy,R): return picado(cx,cy,R,15,1.6).replace('id="tc"',f'id="tc{cx}{cy}"').replace('url(#tc)',f'url(#tc{cx}{cy})')
OUT['t-sin']=svg(100,100,t(50,50,44))
OUT['t-eje']=svg(100,130,t(50,65,44)+eje(50,65,44,4.6))
for kk,s in OUT.items(): open(f'{kk}.svg','w').write(s)
def r(f,h,style=''): return f'<span style="display:inline-flex;{style}">'+open(f).read().replace('<svg ',f'<svg height="{h}" ',1)+'</span>'
rows=''
for base in ('k','o','t'):
    rows+=f'<section style="display:flex;gap:22px;align-items:center;padding:14px 20px;border-bottom:1px solid #eadfce"><b style="width:40px;font:600 13px sans-serif;color:#7a6650">{base.upper()}</b>'
    rows+=r(f'{"k-icono" if base=="k" else base+"-icono"}.svg',96,'opacity:.35')
    for v in ('sin','eje'): rows+=r(f'{base}-{v}.svg',96)+r(f'{base}-{v}.svg',32)
    rows+='</section>'
open('banco-eje.html','w').write(f'<html><body style="margin:0;background:#fbf5ea;font:11px sans-serif"><p style="padding:8px 20px;margin:0;color:#7a6650">gris: ronda 2 (paleta) · luego sin mástil (96 y 32) · luego eje que atraviesa (96 y 32)</p>{rows}</body></html>')
