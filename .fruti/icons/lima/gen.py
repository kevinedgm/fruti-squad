# Generador de Lima (interfaz + avatares). Uso: python3 gen.py
import math
def hexd(R,c=12): return 'M'+' L'.join('%.2f %.2f'%(c+R*math.sin(math.radians(a)), c-R*math.cos(math.radians(a))) for a in range(0,360,60))+'Z'
def hexpts(R,c=12): return [(c+R*math.sin(math.radians(a)), c-R*math.cos(math.radians(a))) for a in range(0,360,60)]
def segdist(p,a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]; t=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/(dx*dx+dy*dy))); return math.hypot(p[0]-a[0]-t*dx,p[1]-a[1]-t*dy)
def gap(R,half,y,sw):
    P=hexpts(R); E=list(zip(P,P[1:]+P[:1]))
    pts=[(12-half+2*half*i/40,yy) for i in range(41) for yy in (12-y,12+y)]
    return min(segdist(p,a,b) for p in pts for a,b in E)-sw
CSS=('.uva-lima{{stroke-width:var(--uva-stroke,{sw})}}'
     # «validar»: al entrar en el estado «Lima está evaluando» se traza el contenedor, se abre la entrada, baja el eje y la salida cierra la compuerta
     '.uva-lima--validar{{--uva-lima-contenedor:uva-lima-trazar;--uva-lima-entrada:uva-lima-trazar;--uva-lima-eje:uva-lima-trazar;--uva-lima-salida:uva-lima-trazar}}'
     '.uva-lima__contenedor{{stroke-dasharray:1 1.1;animation:var(--uva-lima-contenedor,none) 360ms cubic-bezier(.2,.6,.3,1) 0ms 1 both}}'
     '.uva-lima__entrada{{stroke-dasharray:1 1.1;animation:var(--uva-lima-entrada,none) 160ms cubic-bezier(.3,0,.2,1) 300ms 1 both}}'
     '.uva-lima__eje{{stroke-dasharray:1 1.1;animation:var(--uva-lima-eje,none) 220ms cubic-bezier(.3,0,.2,1) 440ms 1 both}}'
     '.uva-lima__salida{{stroke-dasharray:1 1.1;animation:var(--uva-lima-salida,none) 160ms cubic-bezier(.3,0,.2,1) 640ms 1 both}}'
     '@keyframes uva-lima-trazar{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}'
     '@media (prefers-reduced-motion:reduce){{.uva-lima--validar{{--uva-lima-contenedor:none;--uva-lima-entrada:none;--uva-lima-eje:none;--uva-lima-salida:none}}}}')
def cuerpo(R,half,y,piezas):
    d={'entrada':f'M{12-half:g} {12-y:g}H{12+half:g}','eje':f'M12 {12-y:g}V{12+y:g}','salida':f'M{12-half:g} {12+y:g}H{12+half:g}'}
    return (f'  <path class="uva-lima__contenedor" pathLength="1" d="{hexd(R)}"/>\n'
            + ''.join(f'  <path class="uva-lima__{p}" pathLength="1" d="{d[p]}"/>\n' for p in piezas))
COM='  <!-- lima · avatar del agente Lima (gobernanza): hexágono + entrada, eje y salida; cada pieza tiene un contrato y un lugar -->\n'
def svg(g,piezas,sw=2,color='currentColor',a11y='aria-hidden="true"',cls='',tile=False,escala=1):
    c=cuerpo(*g,piezas); css=CSS.format(sw=sw)
    if tile:
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="uva-icon uva-lima{cls}" {a11y}>\n{COM}  <style>{css}</style>\n'
                f'  <rect width="24" height="24" rx="5.25" fill="#161616"/>\n  <g transform="translate(12 12) scale({escala}) translate(-12 -12)" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">\n{c}  </g>\n</svg>\n')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" class="uva-icon uva-lima{cls}" {a11y}>\n{COM}  <style>{css}</style>\n{c}</svg>\n')
UI=(9,2.25,3)          # R, media barra, distancia de las barras al centro · trazo 2
AV=(8.85,2.4,2.25)     # trazo 2.25: máximo que admite la «I» dentro del hexágono con hueco ≥ trazo (2.5 es geométricamente imposible)
TL=AV                  # cuadro: mismo dibujo, escala 0.92
if __name__=='__main__':
    for n,g,sw in (('UI',UI,2),('AV',AV,2.25)):
        print(n,'hueco barra–contenedor %.2f (≥ %s)'%(gap(*g,sw),sw),'hueco entre barras %.2f'%(2*g[2]-sw),'margen %.2f'%(12-g[0]-sw/2))
    w=lambda p,s: open(p,'w').write(s)
    w('lima.small.svg', svg(UI,['eje']))
    w('lima.svg',       svg(UI,['entrada','eje','salida']))
    w('lima.large.svg', svg(UI,['entrada','eje','salida']))
    w('lima-animado-ejemplo.svg', svg(UI,['entrada','eje','salida'],cls=' uva-lima--validar'))
    lbl='role="img" aria-label="Lima"'
    w('avatar/lima-oscuro.svg', svg(AV,['entrada','eje','salida'],2.25,'#C9F36B',lbl))
    w('avatar/lima-claro.svg',  svg(AV,['entrada','eje','salida'],2.25,'#5D820B',lbl))
    w('avatar/lima-auto.svg',   svg(AV,['entrada','eje','salida'],2.25,'#5D820B',lbl).replace('</style>','.uva-lima{stroke:#5D820B}@media (prefers-color-scheme:dark){.uva-lima{stroke:#C9F36B}}</style>'))
    w('avatar/lima-tile.svg',         svg(TL,['entrada','eje','salida'],2.25,'#C9F36B',lbl,tile=True,escala=.92))
    w('avatar/lima-tile-animado.svg', svg(TL,['entrada','eje','salida'],2.25,'#C9F36B',lbl,' uva-lima--validar',tile=True,escala=.92))
