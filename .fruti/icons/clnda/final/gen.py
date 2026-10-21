# CLNDA Studio · paquete final: la llave (C1) con índigo y lima. Logotipo Space Grotesk 700 en trazados con cursor de bloque.
# Uso: python gen.py <carpeta de fuentes con SpaceGrotesk[wght].ttf>
import sys,os,json
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
S=sys.argv[1]; OUT='svg'
BG='#f5f6fb'; INK='#0e0f1c'; IND='#4338ca'; INDD='#8b8cf8'; LIMA='#c6f23d'; OLIVA='#4d7c0f'
src=S+'/fuentes/SpaceGrotesk[wght].ttf'; inst='/tmp/clnda-sg700.ttf'
if not os.path.exists(inst): instancer.instantiateVariableFont(TTFont(src),{'wght':700}).save(inst)
FONT=TTFont(inst); UPM=FONT['head'].unitsPerEm
def palabra(s,size,x0,y0,track=0):
    hf=hb.Font(hb.Face(hb.Blob.from_file_path(inst))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    gs=FONT.getGlyphSet(); order=FONT.getGlyphOrder(); k=size/UPM; x=x0; d=''
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        g=gs[order[i.codepoint]]; pen=SVGPathPen(gs); g.draw(TransformPen(pen,(k,0,0,-k,x,y0))); d+=pen.getCommands(); x+=ps.x_advance*k+track
    return d,x
def svg(body,vb): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
BR='M40 10 H36 a8 8 0 0 0 -8 8 V26 a6 6 0 0 1 -6 6 a6 6 0 0 1 6 6 V46 a8 8 0 0 0 8 8 H40'
BR16='M38 10 H36 a9 9 0 0 0 -9 9 V25 a7 7 0 0 1 -7 7 a7 7 0 0 1 7 7 V45 a9 9 0 0 0 9 9 H38'
def symb(ll,pt): return f'<path d="{BR}" stroke="{ll}" stroke-width="7" transform="translate(-3 0)"/><circle cx="46" cy="32" r="6.5" fill="{pt}"/>'
def symb16(ll,pt): return f'<path d="{BR16}" stroke="{ll}" stroke-width="9" transform="translate(-3 0)"/><circle cx="46" cy="32" r="8" fill="{pt}"/>'
W={}
W['simbolo']=svg(symb(IND,INK),'0 0 64 64')                 # claro
W['simbolo-oscuro']=svg(symb(INDD,BG),'0 0 64 64')          # sobre tinta, índigo claro (regla C)
W['simbolo-lima']=svg(symb(LIMA,BG),'0 0 64 64')            # sobre tinta, lima (excepción B)
W['simbolo-tinta']=svg(symb(INK,INK),'0 0 64 64')
W['simbolo-16']=svg(symb16(IND,INK),'0 0 64 64'); W['simbolo-16-oscuro']=svg(symb16(INDD,BG),'0 0 64 64'); W['simbolo-16-lima']=svg(symb16(LIMA,BG),'0 0 64 64')
W['favicon']=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke-linecap="round" stroke-linejoin="round"><style>:root{{--l:{IND};--p:{INK}}}@media(prefers-color-scheme:dark){{:root{{--l:{LIMA};--p:{BG}}}}}</style>{symb16("var(--l)","var(--p)")}</svg>'
def app(bg,ll,pt,r=0): return svg(f'<rect width="512" height="512" rx="{r}" fill="{bg}"/><g transform="translate(80 80) scale(5.5)">{symb(ll,pt)}</g>','0 0 512 512')
W['app-icon']=app(INK,LIMA,BG); W['app-icon-redondeado']=app(INK,LIMA,BG,112); W['app-icon-claro']=app(BG,IND,INK); W['avatar']=app(INK,LIMA,BG,256)
# logotipo: CLNDA + cursor de bloque
def wordmark(k,cur,size=100):
    y0=size*.98; u=size/UPM
    d,x=palabra('CLNDA',size,0,y0,track=-size*.015)
    cw=size*.44; ch=size*.72; cx=x+size*.08
    return svg(f'<path d="{d}" fill="{k}"/><rect x="{cx:.2f}" y="{y0-ch:.2f}" width="{cw:.2f}" height="{ch:.2f}" rx="{size*.05:.2f}" fill="{cur}"/>', f'0 0 {cx+cw:.0f} {size*1.2:.0f}'), cx+cw
W['wordmark'],WW=wordmark(INK,OLIVA); W['wordmark-oscuro'],_=wordmark(BG,LIMA); W['wordmark-tinta'],_=wordmark(INK,INK)
def lockup(k,cur,ll,pt):
    wm,w=wordmark(k,cur); body=wm.split('>',1)[1].rsplit('</svg>',1)[0]
    return svg(f'<g transform="translate(-6 -4) scale(1.95)">{symb(ll,pt)}</g><g transform="translate(118 0)">{body}</g>',f'0 0 {118+w:.0f} 120')
W['lockup']=lockup(INK,OLIVA,IND,INK); W['lockup-oscuro']=lockup(BG,LIMA,INDD,BG); W['lockup-lima']=lockup(BG,LIMA,LIMA,BG)
# firma de producto: símbolo + "hecho por CLNDA Studio" en Space Grotesk 500 (texto vivo en HTML; aquí en trazados a 700 para SVG)
def firma(k,ll,pt):
    d,x=palabra('hecho por CLNDA Studio',22,34,22)
    return svg(f'<g transform="scale(0.45)">{symb(ll,pt)}</g><path d="{d}" fill="{k}" opacity=".85"/>',f'0 0 {x+4:.0f} 30')
W['firma']=firma(INK,IND,INK); W['firma-oscuro']=firma(BG,INDD,BG)
# tarjeta de redes 1200x630 oscura con lima
wm,w=wordmark(BG,LIMA,140); body=wm.split('>',1)[1].rsplit('</svg>',1)[0]
W['tarjeta-redes']=svg(f'<rect width="1200" height="630" fill="{INK}"/><g transform="translate(120 180) scale(4.2)">{symb(LIMA,BG)}</g><g transform="translate(420 240)">{body}</g>',"0 0 1200 630")
os.makedirs(OUT,exist_ok=True)
for n,s in W.items(): open(f'{OUT}/{n}.svg','w').write(s)
json.dump({'nombre':'CLNDA Studio','simbolo':'la llave: { en color de marca y el dato en tinta','color':{'tinta':INK,'fondo':BG,'indigo':IND,'indigo-oscuro':INDD,'lima':LIMA,'lima-claro':OLIVA},
 'reglas':{'simbolo':'índigo en claro (#4338ca) e índigo claro sobre tinta (#8b8cf8); lima (#c6f23d) permitida solo sobre tinta como variante de pantalla: avatar, app icon, portadas','dato':'siempre tinta en claro y fondo en oscuro','cursor':'lima en oscuro, oliva #4d7c0f en claro','interfaz':'índigo = acción primaria en claro; lima = acción primaria en oscuro; enlaces índigo/lima'},
 'tipografia':{'marca':'Space Grotesk 700 (trazados)','interfaz':'Space Grotesk 400/500','codigo':'JetBrains Mono 500'},
 'contraste':{'indigo/fondo':7.3,'indigo-oscuro/tinta':6.5,'lima/tinta':14.6,'oliva/fondo':4.6,'tinta/fondo':17.6}},open('tema.json','w'),indent=2,ensure_ascii=False)
print('ok',list(W))
