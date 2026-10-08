# PULZ · paquete final: la Z del trasiego, añil + Unbounded. Uso: python gen.py <carpeta de fuentes>
import sys, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
FD=sys.argv[1]
INK='#121217'; ANIL='#3346e0'; FONDO='#f2f2f6'; INK_N='#f2f2f6'; ANIL_N='#7d8bff'; FONDO_N='#121217'
C='var(--pulz-color,#3346e0)'; CUR='currentColor'
def marca(uid,anim=False,lote=True):
    diag='38,21 56,21 26,43 8,43'
    b=f'<rect x="8" y="9" width="48" height="12" rx="3" fill="{CUR}"/><rect x="8" y="43" width="48" height="12" rx="3" fill="{CUR}"/>'
    if not anim:
        return b+f'<polygon points="{diag}" fill="{C}"/>'+(f'<rect x="11.5" y="46.5" width="41" height="5" rx="2.5" fill="{C}"/>' if lote else '')
    return b+(f'<rect class="pz-arriba" x="11.5" y="12.5" width="41" height="5" rx="2.5" fill="{C}"/><clipPath id="d{uid}"><polygon points="{diag}"/></clipPath>'
              f'<path class="pz-trasiego" clip-path="url(#d{uid})" d="M50 19.5 14 44.5" pathLength="1" stroke="{C}" stroke-width="30" fill="none"/>'
              f'<rect class="pz-abajo" x="11.5" y="46.5" width="41" height="5" rx="2.5" fill="{C}"/>')
CSS=('<style>.pz-arriba,.pz-abajo{transform-box:fill-box}.pz-arriba{transform-origin:right center;animation:pz-vacia 700ms cubic-bezier(.5,0,.75,0) 500ms both}'
     '.pz-trasiego{stroke-dasharray:1 1.1;animation:pz-corre 700ms cubic-bezier(.4,0,.2,1) 900ms both}'
     '.pz-abajo{transform-origin:left center;animation:pz-llena 800ms cubic-bezier(.2,.8,.3,1) 1400ms both}'
     '@keyframes pz-vacia{from{transform:scaleX(1)}to{transform:scaleX(0)}}@keyframes pz-corre{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}@keyframes pz-llena{from{transform:scaleX(0)}to{transform:scaleX(1)}}'
     '@media (prefers-reduced-motion:reduce){.pz-arriba{animation:none;transform:scaleX(0)}.pz-trasiego,.pz-abajo{animation:none}}</style>')
def doc(w,h,body,oscuro=False,label='PULZ',style='',extra=''):
    col=f'{INK_N};--pulz-color:{ANIL_N}' if oscuro else INK
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" role="img" aria-label="{label}" style="color:{col}{extra}">{style}{body}</svg>\n'
f=TTFont(FD+'/Unbounded[wght].ttf'); instantiateVariableFont(f,{'wght':800},inplace=True); f.save('/tmp/pz-unb.ttf'); F=TTFont('/tmp/pz-unb.ttf')
def palabra(s,size,x0,y0,font=F,path='/tmp/pz-unb.ttf',track=0):
    hf=hb.Font(hb.Face(hb.Blob.from_file_path(path))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    gs=font.getGlyphSet(); order=font.getGlyphOrder(); kk=size/font['head'].unitsPerEm; x=x0; d=''; bp=BoundsPen(gs)
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        g=gs[order[i.codepoint]]; m=(kk,0,0,-kk,x,y0); pen=SVGPathPen(gs); g.draw(TransformPen(pen,m)); g.draw(TransformPen(bp,m)); d+=pen.getCommands(); x+=ps.x_advance*kk+track
    return d,bp.bounds,font['OS/2'].sCapHeight*kk
OUT={}
OUT['simbolo']=doc(64,64,marca('s')); OUT['simbolo-oscuro']=doc(64,64,marca('s'),True)
OUT['simbolo-animado']=doc(64,64,marca('a',True),style=CSS)
OUT['simbolo-16']=doc(64,64,marca('p',lote=False))
d,bb,cap=palabra('PUL',64,0,64); esc=cap/46; zx=bb[2]+cap*.08-8*esc; W=zx+56*esc+2
wm=lambda anim,uid: f'<path fill="{CUR}" d="{d}"/><g transform="translate({zx:.2f} {64-cap-9*esc:.2f}) scale({esc:.4f})">{marca(uid,anim)}</g>'
OUT['wordmark']=doc(W,72,wm(False,'w')); OUT['wordmark-oscuro']=doc(W,72,wm(False,'w'),True); OUT['wordmark-animado']=doc(W,72,wm(True,'wa'),style=CSS)
OUT['wordmark-animado-oscuro']=doc(W,72,wm(True,'wao'),True,style=CSS)
# favicon: versión de 16 px, sigue el tema del navegador
OUT['favicon']=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="PULZ"><style>svg{{color:{INK};--pulz-color:{ANIL}}}@media (prefers-color-scheme:dark){{svg{{color:{INK_N};--pulz-color:{ANIL_N}}}}}</style>{marca("f",lote=False)}</svg>\n')
# icono de app: tile añil, Z en cal (6.08:1) y lote en tinta; la diagonal en tinta daba 2.75:1
# en una tinta la Z es un solo trazado: sin costura entre piezas y con esquinas vivas donde la diagonal toca cada barra
ZMONO='M11 9H53a3 3 0 0 1 3 3V21L26 43H53a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3H11a3 3 0 0 1-3-3V43L38 21H11a3 3 0 0 1-3-3v-6a3 3 0 0 1 3-3Z'
def tile(pad,rx):
    s=64*(1-2*pad)/64
    m=f'<path d="{ZMONO}" fill="{FONDO}"/><rect x="11.5" y="46.5" width="41" height="5" rx="2.5" fill="{INK}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="PULZ"><rect width="64" height="64" rx="{rx}" fill="{ANIL}"/><g transform="translate({64*pad:.2f} {64*pad:.2f}) scale({s:.4f})">{m}</g></svg>\n'
OUT['app-icon']=tile(.18,0); OUT['app-icon-maskable']=tile(.26,0); OUT['app-icon-redondeado']=tile(.18,14)
# firma «hecho con PULZ»: toma el color de cada palenque por --pulz-color
dh,bh,caph=palabra('hecho con',13,26,21,track=.2)
dp,bpz,_=palabra('PULZ',13,bh[2]+5,21)
OUT['firma']=doc(bpz[2]+8,30,f'<g transform="translate(2 3) scale(.375)">{marca("h")}</g><path fill="{CUR}" fill-opacity=".72" d="{dh}"/><path fill="{CUR}" d="{dp}"/>',label='hecho con PULZ')
OUT['firma-oscuro']=doc(bpz[2]+8,30,f'<g transform="translate(2 3) scale(.375)">{marca("h")}</g><path fill="{CUR}" fill-opacity=".72" d="{dh}"/><path fill="{CUR}" d="{dp}"/>',True,label='hecho con PULZ')
# tarjeta para WhatsApp y redes (1200×630)
d2,b2,cap2=palabra('PUL',150,96,330); e2=cap2/46; zx2=b2[2]+cap2*.08-8*e2
dl,_,_=palabra('Del maguey al granel.',38,100,430,F)
dl2,_,_=palabra('Producción de mezcal, trazada.',38,100,482,F)
OUT['tarjeta-redes']=doc(1200,630,f'<rect width="1200" height="630" fill="{FONDO}"/><path fill="{CUR}" d="{d2}"/><g transform="translate({zx2:.2f} {330-cap2-9*e2:.2f}) scale({e2:.4f})">{marca("og")}</g><path fill="{CUR}" d="{dl}"/><path fill="{C}" d="{dl2}"/>')
for k,s in OUT.items(): open(f'svg/{k}.svg','w').write(s)
print(len(OUT))
