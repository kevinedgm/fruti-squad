# Xila · paquete final: J (greca bordada en punto de cruz), paleta Cobalto, Instrument Sans 700 en trazados.
# Uso: python gen.py <carpeta de fuentes con InstrumentSans[wdth,wght].ttf>
import sys,glob,os,json
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import uharfbuzz as hb
FD=sys.argv[1]; OUT='svg'
MANTA,INK,COB,HILO='#f6f1e8','#15171f','#1f4bd8','#d14e0a'; DBG,DINK,COBD,HILOD='#15171f','#f6f1e8','#7a9bff','#ff8a3d'
src=glob.glob(FD+'/InstrumentSans*')[0]; inst='/tmp/xila-isans.ttf'
if not os.path.exists(inst): instancer.instantiateVariableFont(TTFont(src),{'wght':700,'wdth':100}).save(inst)
FONT=TTFont(inst)
def palabra(s,size,x0,y0,track=0):
    hf=hb.Font(hb.Face(hb.Blob.from_file_path(inst))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    gs=FONT.getGlyphSet(); order=FONT.getGlyphOrder(); k=size/FONT['head'].unitsPerEm; x=x0; d=''; bp=BoundsPen(gs)
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        g=gs[order[i.codepoint]]; m=(k,0,0,-k,x,y0); pen=SVGPathPen(gs); g.draw(TransformPen(pen,m)); g.draw(TransformPen(bp,m)); d+=pen.getCommands(); x+=ps.x_advance*k+track
    return d,bp.bounds
GRECA=[(0,8),(1,8),(2,8),(2,7),(2,6),(3,6),(4,6),(4,5),(4,4),(5,4),(6,4),(6,3),(6,2),(7,2),(8,2),(8,1),(8,0)]
G16=[(0,4),(1,4),(1,3),(2,3),(2,2),(3,2),(3,1),(4,1),(4,0)]   # 5×5: menos puntadas para 16–24 px
def cruz(x,y,c,s,w):
    sw=f' stroke-width="{w}"' if w else ''
    return f'<path d="M{x-s:.2f} {y-s:.2f}L{x+s:.2f} {y+s:.2f}M{x+s:.2f} {y-s:.2f}L{x-s:.2f} {y+s:.2f}" stroke="{c}"{sw}/>'
def greca(ink='currentColor',acc='var(--xila-color,#1f4bd8)',cells=GRECA,pitch=6,x0=8,y0=8,s=2.4,w=1.9,ox=0,oy=0,last=(8,0)):
    return ''.join(cruz(ox+x0+i*pitch,oy+y0+j*pitch,acc if (i,j)==last else ink,s,None) for (i,j) in cells)
def doc(w,h,body,label='xila',dark=False,style='',extra=''):
    col=f'{DINK};--xila-color:{COBD}' if dark else f'{INK};--xila-color:{COB}'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" role="img" aria-label="{label}" fill="none" stroke-width="1.9" stroke-linecap="round" style="color:{col}{extra}">{style}{body}</svg>\n'
O={}
O['simbolo']=doc(64,64,greca()); O['simbolo-oscuro']=doc(64,64,greca(),dark=True)
O['simbolo-16']=doc(64,64,greca(cells=G16,pitch=11,x0=10,y0=10,s=4,last=(4,0))).replace('stroke-width="1.9"','stroke-width="3.2"')
# favicon: cambia solo con el tema
O['favicon']=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="xila" fill="none" stroke-width="3.2" stroke-linecap="round"><style>svg{{color:{INK};--xila-color:{COB}}}@media (prefers-color-scheme:dark){{svg{{color:{DINK};--xila-color:{COBD}}}}}</style>{greca(cells=G16,pitch=11,x0=10,y0=10,s=4,last=(4,0))}</svg>\n'
# icono de app / avatar: azulejo cobalto, puntadas en manta, la última en hilo
def tile(pad,rx):
    s=1-2*pad; return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="xila" fill="none" stroke-width="2.2" stroke-linecap="round"><rect width="64" height="64" rx="{rx}" fill="{COB}"/><g transform="translate({64*pad:.2f} {64*pad:.2f}) scale({s:.4f})">{greca(ink=MANTA,acc=HILOD)}</g></svg>\n'
O['app-icon']=tile(.14,0); O['app-icon-redondeado']=tile(.14,14); O['avatar']=tile(.18,32)
# wordmark: greca + «xila»
d,bb=palabra('xila',50,76,58); W=bb[2]+8
wm=lambda: f'<g transform="translate(2 4)">{greca()}</g><path fill="currentColor" d="{d}"/>'
O['wordmark']=doc(W,72,wm()); O['wordmark-oscuro']=doc(W,72,wm(),dark=True)
# banda: la greca corriendo como en un huipil (patrón repetible, 4 baldosas)
O['banda']=doc(256,64,''.join(greca(ox=i*64) for i in range(4)),label='banda bordada de xila')
# tarjeta de redes 1200×630
d2,b2=palabra('xila',150,330,290); dl,_=palabra('Gráficas que salen de la línea y la barra.',30,120,400); dl2,_=palabra('Librería de gráficos en TypeScript para dashboards y datos científicos.',22,120,442)
inst_r=instancer.instantiateVariableFont(TTFont(src),{'wght':500,'wdth':100}); inst_r.save('/tmp/xila-isans-500.ttf')
O['tarjeta-redes']=doc(1200,630,f'<rect width="1200" height="630" fill="{MANTA}"/><g transform="translate(120 160) scale(2.5)">{greca(ink=INK,acc=COB)}</g><path fill="{INK}" d="{d2}"/><path fill="{INK}" d="{dl}"/><path fill="#5b5f6e" d="{dl2}"/><g transform="translate(800 500) scale(1.4)" opacity=".16">{"".join(greca(ink=INK,acc=INK,ox=(i%3)*64,oy=(i//3)*64) for i in range(3))}</g>',label='xila · gráficas que salen de la línea y la barra')
import xml.dom.minidom as m
for n,s in O.items():
    m.parseString(s); open(f'{OUT}/{n}.svg','w').write(s)
print(len(O))
