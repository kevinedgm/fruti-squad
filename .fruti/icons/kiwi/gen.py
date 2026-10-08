# Generador de Kiwi (interfaz + avatares). Uso: python3 gen.py
import math
CX=CY=12
def geo(rx,ry,inset=.35):
    ey=lambda x: ry*math.sqrt(1-((x-CX)/rx)**2); ex=lambda y: rx*math.sqrt(1-((y-CY)/ry)**2)
    xv,yh,x2=9,11,15
    return dict(rx=rx,ry=ry,eje=f'M{xv} {CY-ey(xv)+inset:.2f}V{CY+ey(xv)-inset:.2f}',
                fila=f'M{xv} {yh}H{CX+ex(yh)-inset:.2f}', sec=f'M{x2} {yh}V{CY+ey(x2)-inset:.2f}')
CSS = ('.uva-kiwi{{stroke-width:var(--uva-stroke,{sw})}}'
       '.uva-kiwi:dir(rtl){{transform:scaleX(-1)}}'
       # «organizar»: al entrar en el estado «Kiwi está estructurando» se dibuja el contorno, cae el eje y se traza la fila
       '.uva-kiwi--organizar{{--uva-kiwi-contorno:uva-kiwi-trazar;--uva-kiwi-eje:uva-kiwi-trazar;--uva-kiwi-fila:uva-kiwi-trazar;--uva-kiwi-secundaria:uva-kiwi-trazar}}'
       '.uva-kiwi__contorno{{stroke-dasharray:1 1.1;animation:var(--uva-kiwi-contorno,none) 380ms cubic-bezier(.2,.6,.3,1) 0ms 1 both}}'
       '.uva-kiwi__eje{{stroke-dasharray:1 1.1;animation:var(--uva-kiwi-eje,none) 240ms cubic-bezier(.3,0,.2,1) 320ms 1 both}}'
       '.uva-kiwi__fila{{stroke-dasharray:1 1.1;animation:var(--uva-kiwi-fila,none) 220ms cubic-bezier(.3,0,.2,1) 540ms 1 both}}'
       '.uva-kiwi__secundaria{{stroke-dasharray:1 1.1;animation:var(--uva-kiwi-secundaria,none) 180ms cubic-bezier(.3,0,.2,1) 740ms 1 both}}'
       '@keyframes uva-kiwi-trazar{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}'
       '@media (prefers-reduced-motion:reduce){{.uva-kiwi--organizar{{--uva-kiwi-contorno:none;--uva-kiwi-eje:none;--uva-kiwi-fila:none;--uva-kiwi-secundaria:none}}}}')
def svg(g,piezas,sw=2,color='currentColor',a11y='aria-hidden="true"',extra_cls='',tile=False,escala=1):
    cuerpo=(f'  <ellipse class="uva-kiwi__contorno" pathLength="1" cx="{CX}" cy="{CY}" rx="{g["rx"]}" ry="{g["ry"]}"/>\n'
            + ''.join(f'  <path class="uva-kiwi__{p}" pathLength="1" d="{g[p]}"/>\n' for p in piezas))
    css=CSS.format(sw=sw)
    if tile:
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="uva-icon uva-kiwi{extra_cls}" {a11y}>\n'
                f'  <!-- kiwi · avatar del agente Kiwi (estructura): óvalo + eje + fila; organiza el espacio antes de construirlo -->\n'
                f'  <style>{css}</style>\n  <rect width="24" height="24" rx="5.25" fill="#161616"/>\n'
                f'  <g transform="translate(12 12) scale({escala}) translate(-12 -12)" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">\n{cuerpo}  </g>\n</svg>\n')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" class="uva-icon uva-kiwi{extra_cls}" {a11y}>\n'
            f'  <!-- kiwi · avatar del agente Kiwi (estructura): óvalo + eje + fila; organiza el espacio antes de construirlo -->\n'
            f'  <style>{css}</style>\n{cuerpo}</svg>\n')
UI=geo(9,7.25)            # trazo 2, margen 2
AV=geo(8.75,7.05)         # trazo 2.5, margen 2 (avatares)
w=lambda p,s: open(p,'w').write(s)
w('kiwi.small.svg', svg(UI,['eje']))
w('kiwi.svg',       svg(UI,['eje','fila']))
w('kiwi.large.svg', svg(UI,['eje','fila','sec']).replace('uva-kiwi__sec"','uva-kiwi__secundaria"'))
lbl='role="img" aria-label="Kiwi"'
w('avatar/kiwi-oscuro.svg', svg(AV,['eje','fila'],2.5,'#7FCF5B',lbl))
w('avatar/kiwi-claro.svg',  svg(AV,['eje','fila'],2.5,'#448427',lbl))
auto=svg(AV,['eje','fila'],2.5,'#448427',lbl).replace('</style>','.uva-kiwi{stroke:#448427}@media (prefers-color-scheme:dark){.uva-kiwi{stroke:#7FCF5B}}</style>')
w('avatar/kiwi-auto.svg', auto)
tl=lambda cls='': svg(AV,['eje','fila','sec'],2.75,'#7FCF5B',lbl,cls,tile=True,escala=.82).replace('uva-kiwi__sec"','uva-kiwi__secundaria"')
w('avatar/kiwi-tile.svg', tl())
w('avatar/kiwi-tile-animado.svg', tl(' uva-kiwi--organizar'))
w('kiwi-animado-ejemplo.svg', svg(UI,['eje','fila'],extra_cls=' uva-kiwi--organizar'))
