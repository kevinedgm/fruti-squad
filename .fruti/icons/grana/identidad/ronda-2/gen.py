# Grana · ronda 2: afinado de Armazón. Lienzo 48. Tinte = --g-color-brand (carmín por defecto); estructura = currentColor.
# Hueco recortado: la capa de tinte se enmascara con la estructura engrosada, así tinta y tinte nunca se tocan (sirve en una tinta).
import math
COLOR='var(--g-color-brand,#a3123a)'
def oval(cx,cy,rx,ry,top=1.0):
    # óvalo de grano: algo más estrecho arriba (top<1)
    k=0.5523
    return (f'M{cx} {cy-ry}C{cx+rx*k*top:.2f} {cy-ry} {cx+rx:.2f} {cy-ry*k:.2f} {cx+rx:.2f} {cy:.2f}'
            f'C{cx+rx:.2f} {cy+ry*k:.2f} {cx+rx*k:.2f} {cy+ry} {cx} {cy+ry}'
            f'C{cx-rx*k:.2f} {cy+ry} {cx-rx:.2f} {cy+ry*k:.2f} {cx-rx:.2f} {cy:.2f}'
            f'C{cx-rx:.2f} {cy-ry*k:.2f} {cx-rx*k*top:.2f} {cy-ry} {cx} {cy-ry}Z')
def bandas(cx,cy,rx,ry,ys,curva):
    out=''
    for y in ys:
        dy=y-cy; w=rx*math.sqrt(max(0,1-(dy/ry)**2))-0.3
        out+=f'M{cx-w:.2f} {y:.2f}Q{cx} {y+curva:.2f} {cx+w:.2f} {y:.2f}'
    return out
def simbolo(id_,cx,cy,rx,ry,top,ys,curva,sw,off,gap,antenas):
    body=oval(cx,cy,rx,ry,top); b=bandas(cx,cy,rx,ry,ys,curva)
    est=f'<path d="{body}"/><path d="{b}"/>'+(f'<path d="{antenas}"/>' if antenas else '')
    return (f'  <defs><mask id="{id_}-hueco" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48"><rect width="48" height="48" fill="#fff"/>'
            f'<g fill="none" stroke="#000" stroke-width="{sw+2*gap}" stroke-linecap="round" stroke-linejoin="round">{est}</g></mask></defs>\n'
            f'  <g mask="url(#{id_}-hueco)"><path class="grana__tinte" d="{body}" transform="translate({off} {off})" fill="{COLOR}"/></g>\n'
            f'  <g class="grana__armazon" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{est}</g>\n')
def svg(id_,body,desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Grana" class="grana-{id_}">\n'
            f'  <!-- Grana · {desc} -->\n{body}</svg>\n')
V={}
V['a1-original']=open('../ronda-1/a-armazon.svg').read()
# A2 · grano con antenas cortas
V['a2-grano']=svg('a2',simbolo('a2',23.5,26,15.5,13.5,.85,[21.5,28.5],2.6,3,2.8,1.4,'M19.8 13.4 18 10.2M27.2 13.4 29 10.2'),'armazón afinado: grano ancho, dos bandas, antenas cortas, hueco recortado entre tinta y tinte')
# A3 · grano sin antenas, tres bandas finas: más semilla que bicho
V['a3-semilla']=svg('a3',simbolo('a3',23.5,24.5,15.5,13.5,.85,[19.5,25,30.5],2.2,3,2.8,1.4,None),'armazón afinado: grano sin antenas, tres bandas; se lee como semilla de grana')
# A4 · grano con cabeza (segmento pequeño delante) en vez de antenas
V['a4-oval']=svg('a4',simbolo('a4',23.5,25.5,13.5,15,.8,[21.5,28.5,34.5],2.4,3,2.8,1.3,'M20.6 11.3 18.6 7.6M26.4 11.3 28.4 7.6'),'armazón afinado: óvalo algo más alto que ancho (entre el original y el grano), tres bandas, antenas cortas, hueco recortado')
# 16 px: versión mínima (sobre la que mejor funcione)
V['a2-16']=svg('a216',simbolo('a216',23,25.5,17,15,.85,[25.5],3,4.5,3.4,1.8,None),'versión de 16 px: grano, una banda, trazo grueso')
for k,s in V.items(): open(f'{k}.svg','w').write(s)
TEMAS=[('carmín','#a3123a'),('azul','#2563eb'),('verde','#0f8a5f'),('violeta','#7c3aed')]
rows=''
for k in ['a1-original','a4-oval','a2-grano','a3-semilla']:
    s=open(f'{k}.svg').read(); s16=open('a2-16.svg').read() if k!='a1-original' else s
    sz=f'<span style="display:inline-flex;width:30px;justify-content:center;flex-direction:column;align-items:center">{s16.replace("<svg ","<svg width=16 height=16 ",1)}<small style="font:9px sans-serif;color:#999">16</small></span>'
    sz+=''.join(f'<span style="display:inline-flex;width:{max(z,36)+8}px;justify-content:center">{s.replace("<svg ",f"<svg width={z} height={z} ",1)}</span>' for z in (24,32,48,64,128))
    th=''.join(f'<span style="display:inline-flex;padding:6px;border:1px solid #e5e5e5;border-radius:10px;--g-color-brand:{c};color:#1a1a1a">{s.replace("<svg ","<svg width=36 height=36 ",1)}</span>' for n,c in TEMAS)
    dk=f'<span style="display:inline-flex;padding:6px;border-radius:10px;background:#141414;color:#f5f5f5;--g-color-brand:#ff4d7a">{s.replace("<svg ","<svg width=36 height=36 ",1)}</span>'
    mono=f'<span style="display:inline-flex;padding:6px;border:1px solid #e5e5e5;border-radius:10px;--g-color-brand:currentColor;color:#1a1a1a">{s.replace("<svg ","<svg width=36 height=36 ",1)}</span>'
    monod=f'<span style="display:inline-flex;padding:6px;border-radius:10px;background:#141414;--g-color-brand:currentColor;color:#f5f5f5">{s.replace("<svg ","<svg width=36 height=36 ",1)}</span>'
    rows+=f'<section style="padding:10px 16px;border-bottom:1px solid #eee"><b style="font:600 13px sans-serif">{k}</b><div style="display:flex;align-items:flex-end;gap:4px;margin:6px 0;color:#1a1a1a">{sz}</div><div style="display:flex;gap:8px;align-items:center">{th}{dk}<span style="width:12px"></span>{mono}{monod}<small style="font:11px sans-serif;color:#666">temas · oscuro · una tinta</small></div></section>'
open('banco.html','w').write(f'<html><body style="margin:0;background:#fafaf9">{rows}</body></html>')
