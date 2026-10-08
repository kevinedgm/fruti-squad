# Grana · ronda 2b: color con tinte sólido (como A1) en proporción intermedia + versión de una tinta con el tinte como segundo contorno.
from gen import oval, bandas
COLOR='var(--g-color-brand,#a3123a)'
def color(cx,cy,rx,ry,top,ys,curva,sw,off,ant,sw_b=None):
    body=oval(cx,cy,rx,ry,top); b=bandas(cx,cy,rx,ry,ys,curva)
    return (f'  <path class="grana__tinte" d="{body}" transform="translate({off} {off})" fill="{COLOR}"/>\n'
            f'  <g class="grana__armazon" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="{body}"/><path d="{b}"' + (f' stroke-width="{sw_b}"' if sw_b else '') + '/>' + (f'<path d="{ant}"/>' if ant else '') + '</g>\n')
def mono(cx,cy,rx,ry,top,ys,curva,sw,off,ant,sw_b=None):
    body=oval(cx,cy,rx,ry,top); b=bandas(cx,cy,rx,ry,ys,curva)
    return (f'  <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">'
            f'<path class="grana__tinte" d="{body}" transform="translate({off} {off})" stroke-width="{sw*0.6:.2f}" stroke-dasharray="0.1 {sw*1.2:.2f}"/>'
            f'<path d="{body}" stroke-width="{sw}"/><path d="{b}" stroke-width="{sw_b or sw}"/>' + (f'<path d="{ant}" stroke-width="{sw}"/>' if ant else '') + '</g>\n')
def mono_linea(cx,cy,rx,ry,top,ys,curva,sw,off,ant,sw_b=None):
    body=oval(cx,cy,rx,ry,top); b=bandas(cx,cy,rx,ry,ys,curva)
    return (f'  <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">'
            f'<path class="grana__tinte" d="{body}" transform="translate({off} {off})" stroke-width="{sw*0.55:.2f}"/>'
            f'<path d="{body}" stroke-width="{sw}"/><path d="{b}" stroke-width="{sw_b or sw}"/>' + (f'<path d="{ant}" stroke-width="{sw}"/>' if ant else '') + '</g>\n')
def svg(id_,body,desc): return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Grana" class="grana-{id_}">\n  <!-- Grana · {desc} -->\n{body}</svg>\n')
P=dict(cx=23.2,cy=25,rx=13.5,ry=15,top=.8,ys=[20.5,27.5,33.8],curva=2.4,sw=3,off=3,ant='M20.4 10.8 18.6 7.2M26 10.8 27.8 7.2',sw_b=2.6)
P16=dict(cx=23,cy=24.5,rx=16,ry=17,top=.85,ys=[25.5],curva=3,sw=4.6,off=3.6,ant=None)
open('a5-color.svg','w').write(svg('a5',color(**P),'armazón: tinte sólido del tema desplazado detrás; estructura en tinta (proporción intermedia, antenas cortas)'))
open('a5-tinta-puntos.svg','w').write(svg('a5p',mono(**P),'una tinta: el tinte es un contorno punteado desplazado'))
open('a5-tinta-linea.svg','w').write(svg('a5l',mono_linea(**P),'una tinta: el tinte es un segundo contorno fino desplazado'))
open('a5-16.svg','w').write(svg('a516',color(**P16),'16 px: óvalo, una banda, trazo grueso, sin antenas'))
open('a5-16-tinta.svg','w').write(svg('a516t',mono_linea(**P16),'16 px en una tinta'))
TEMAS=[('#a3123a'),('#2563eb'),('#0f8a5f'),('#7c3aed')]
def r(f,z,style=''): return f'<span style="display:inline-flex;{style}">'+open(f).read().replace('<svg ',f'<svg width={z} height={z} ',1)+'</span>'
rows=''
for name,fc,f16 in (('a1-original','../ronda-1/a-armazon.svg','../ronda-1/a-armazon.svg'),('a5-color','a5-color.svg','a5-16.svg')):
    sz=r(f16,16,'width:28px;justify-content:center')+''.join(r(fc,z,f'width:{max(z,36)+8}px;justify-content:center') for z in (24,32,48,64,128))
    th=''.join(r(fc,36,f'padding:6px;border:1px solid #e5e5e5;border-radius:10px;--g-color-brand:{c};color:#1a1a1a') for c in TEMAS)+r(fc,36,'padding:6px;border-radius:10px;background:#141414;color:#f5f5f5;--g-color-brand:#ff4d7a')
    rows+=f'<section style="padding:10px 16px;border-bottom:1px solid #eee"><b style="font:600 13px sans-serif">{name}</b><div style="display:flex;align-items:flex-end;gap:4px;margin:6px 0;color:#1a1a1a">{sz}</div><div style="display:flex;gap:8px">{th}</div></section>'
for name,fm,f16 in (('una tinta · contorno fino','a5-tinta-linea.svg','a5-16-tinta.svg'),('una tinta · punteado','a5-tinta-puntos.svg','a5-16-tinta.svg')):
    sz=r(f16,16,'width:28px;justify-content:center')+''.join(r(fm,z,f'width:{max(z,36)+8}px;justify-content:center') for z in (24,32,48,64,128))
    rows+=f'<section style="padding:10px 16px;border-bottom:1px solid #eee"><b style="font:600 13px sans-serif">{name}</b><div style="display:flex;align-items:flex-end;gap:4px;margin:6px 0;color:#1a1a1a">{sz}{r(fm,48,"padding:8px;background:#141414;color:#f5f5f5;border-radius:10px;margin-left:10px")}</div></section>'
open('banco2.html','w').write(f'<html><body style="margin:0;background:#fafaf9">{rows}</body></html>')
