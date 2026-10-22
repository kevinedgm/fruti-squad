# Laranda · paquete final. Flor B2 (línea de tinta a mano, mancha violeta desfasada, lóbulo que se separa en naranja),
# paleta intensa aprobada, wordmark Fraunces 600 en trazados. Uso: python gen.py <carpeta de fuentes>
import sys,os,json,math
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
S=sys.argv[1]; OUT='svg'
INK='#15121C'; HUESO='#F6F4EF'; ARENA='#EAE6DE'; VIO='#5B3BB5'; VIO2='#4A2DA8'; LILA='#C4B5F0'; NIEBLA='#ECE7FA'; NAR='#E0611A'; NAR_T='#F2C9B2'; NAR_D='#F2A074'; ORO='#D9A400'; VERDE='#0E8F5E'; ROJO='#A8202F'; SUAVE='#4F4B57'; OSC_SURF='#221E2E'
src=S+'/fuentes/BricolageGrotesque[opsz,wdth,wght].ttf'; inst='/tmp/laranda-bricolage.ttf'
if not os.path.exists(inst): instancer.instantiateVariableFont(TTFont(src),{'wght':600,'opsz':96,'wdth':100}).save(inst)
FONT=TTFont(inst); UPM=FONT['head'].unitsPerEm
def palabra(s,size,x0,y0,track=0):
    hf=hb.Font(hb.Face(hb.Blob.from_file_path(inst))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True,'liga':True})
    gs=FONT.getGlyphSet(); order=FONT.getGlyphOrder(); k=size/UPM; x=x0; d=''
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        g=gs[order[i.codepoint]]; pen=SVGPathPen(gs); g.draw(TransformPen(pen,(k,0,0,-k,x,y0))); d+=pen.getCommands(); x+=ps.x_advance*k+track
    return d,x
def svg(body,vb='0 0 128 128'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
LOBOS=[('M60 46 C54 30 40 26 34 36 C28 46 38 56 50 56',0,0),('M68 44 C72 30 88 26 94 36 C100 46 90 56 78 58',4,-4),('M80 66 C96 64 104 76 98 86 C92 94 78 92 72 80',0,0),('M66 86 C70 100 60 110 50 104 C42 98 46 88 56 84',0,0),('M48 76 C34 82 22 74 26 62 C30 52 44 54 52 62',0,0)]
MANCHA='M62 36 C50 26 36 34 40 50 C28 54 24 70 34 78 C42 86 54 84 60 76 C62 92 78 100 88 90 C96 82 92 70 84 64 C98 58 100 42 88 36 C80 30 70 32 62 36Z'
LOBULO='M70 20 C78 14 92 18 96 30 C98 40 90 48 80 46 C72 44 66 32 70 20Z'
def flor(k=INK,f=HUESO,m=VIO,a=NAR,sw=3.2,off=(8,7),mancha=True,cls=False):
    dx,dy=off; b=''
    cm=' class="m"' if cls else ''; ca=' class="a"' if cls else ''; cc=' class="c"' if cls else ''
    if mancha: b+=f'<path d="{MANCHA}" fill="{m}" transform="translate({dx} {dy})"{cm}/><path d="{LOBULO}" fill="{a}" transform="translate({dx+1} {dy-1})"{ca}/>'
    for i,(d,lx,ly) in enumerate(LOBOS):
        cl=f' class="l l{i}"' if cls else ''
        b+=f'<path d="{d}" stroke="{k}" stroke-width="{sw}" transform="translate({lx} {ly})"{cl}/>'
    b+=f'<circle cx="64" cy="68" r="4.5" fill="{f}" stroke="{k}" stroke-width="{sw*.8:.1f}"{cc}/>'
    return b
def silueta(k=VIO,f=HUESO,a=None):
    b=''
    for i in range(5):
        ang=math.radians(-126+i*72); cx,cy=64+20*math.cos(ang),66+20*math.sin(ang)
        if i==1: cx+=5; cy-=5
        b+=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="15" fill="{a if (i==1 and a) else k}"/>'
    return b+f'<circle cx="64" cy="66" r="7" fill="{f}"/>'
W={}
W['simbolo']=svg(flor()); W['simbolo-oscuro']=svg(flor(HUESO,INK,LILA,NAR_D)); W['simbolo-tinta']=svg(flor(INK,HUESO,mancha=False)); W['simbolo-blanco']=svg(flor(HUESO,INK,mancha=False))
W['silueta']=svg(silueta()); W['silueta-tinta']=svg(silueta(INK)); W['silueta-oscuro']=svg(silueta(LILA,INK)); W['silueta-acento']=svg(silueta(VIO,HUESO,NAR))
W['favicon']=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128"><style>:root{{--k:{VIO};--f:{HUESO};--a:{NAR}}}@media(prefers-color-scheme:dark){{:root{{--k:{LILA};--f:{INK};--a:{NAR_D}}}}}</style>{silueta("var(--k)","var(--f)","var(--a)")}</svg>'
def app(r=0,margen=32,bg=VIO,k=HUESO,m=LILA,a=NAR_D):
    sc=(512-2*margen)/128
    return svg(f'<rect width="512" height="512" rx="{r}" fill="{bg}"/><g transform="translate({margen} {margen}) scale({sc:.3f})">{flor(k,bg,m,a)}</g>','0 0 512 512')
W['app-icon']=app(0,32); W['app-icon-redondeado']=app(112,32); W['app-icon-maskable']=app(0,102); W['avatar']=app(256,40)
W['app-icon-claro']=app(0,32,HUESO,INK,VIO,NAR)
# wordmark: caja baja, Bricolage Grotesque 600 opsz 96
def wordmark(k,size=100):
    y0=size*.88; d,x=palabra('laranda',size,2,y0,track=-size*.012); return svg(f'<path d="{d}" fill="{k}"/>',f'0 0 {x+2:.0f} {size*1.15:.0f}'),x+2
W['wordmark'],WW=wordmark(INK); W['wordmark-oscuro'],_=wordmark(HUESO); W['wordmark-violeta'],_=wordmark(VIO)
def lockup_h(k,f,m,a):
    wm,w=wordmark(k); body=wm.split('>',1)[1].rsplit('</svg>',1)[0]
    return svg(f'<g transform="translate(-10 -6) scale(1.1)">{flor(k,f,m,a)}</g><g transform="translate(122 -4)">{body}</g>',f'0 0 {122+w:.0f} 118')
def lockup_v(k,f,m,a):
    wm,w=wordmark(k,80); body=wm.split('>',1)[1].rsplit('</svg>',1)[0]; W_=max(w,140); 
    return svg(f'<g transform="translate({(W_-140)/2:.0f} 0) scale(1.1)">{flor(k,f,m,a)}</g><g transform="translate({(W_-w)/2:.0f} 134)">{body}</g>',f'0 0 {W_:.0f} 230')
W['lockup-h']=lockup_h(INK,HUESO,VIO,NAR); W['lockup-h-oscuro']=lockup_h(HUESO,INK,LILA,NAR_D); W['lockup-h-tinta']=svg(lockup_h(INK,HUESO,INK,INK).split('>',1)[1].rsplit('</svg>',1)[0].replace(f'fill="{INK}" transform','fill="none" transform'),f'0 0 {122+WW:.0f} 118')
W['lockup-v']=lockup_v(INK,HUESO,VIO,NAR); W['lockup-v-oscuro']=lockup_v(HUESO,INK,LILA,NAR_D)
W['sello']=svg(flor(INK,HUESO,mancha=False,sw=2.6)); W['sello-emitido']=svg(f'<circle cx="64" cy="64" r="60" stroke="{INK}" stroke-width="2.2"/><g transform="translate(14 12) scale(0.78)">{flor(INK,HUESO,mancha=False,sw=3)}</g>')
# tarjeta de redes 1200x630
wm,w=wordmark(HUESO,150); body=wm.split('>',1)[1].rsplit('</svg>',1)[0]
W['tarjeta-redes']=svg(f'<rect width="1200" height="630" fill="{VIO}"/><g transform="translate(110 130) scale(2.9)">{flor(HUESO,VIO,LILA,NAR_D)}</g><g transform="translate(520 235)">{body}</g><text x="524" y="440" font-family="Onest, system-ui, sans-serif" font-size="34" font-weight="500" fill="{LILA}">Tu oficio, en flor. · Your craft, in bloom.</text>','0 0 1200 630')
# bloom: 500 ms; los lóbulos crecen desde la garganta y el lóbulo naranja se separa al final; con reducir movimiento, abierta
anim=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" fill="none" stroke-linecap="round" stroke-linejoin="round"><style>
.m,.a,.l,.c{{transform-box:fill-box;transform-origin:center}}
@media (prefers-reduced-motion:no-preference){{
.m{{transform-origin:64px 68px;animation:crece .5s cubic-bezier(.2,.8,.2,1) both}}
.l{{transform-origin:64px 68px;animation:crece .45s cubic-bezier(.2,.8,.2,1) both;animation-delay:.05s}}
.l1,.a{{animation-name:crece-sep}} .a{{transform-origin:64px 68px;animation-duration:.55s}}
.c{{animation:punto .3s ease-out both;animation-delay:.3s}}
@keyframes crece{{from{{transform:scale(.2);opacity:0}}to{{transform:scale(1);opacity:1}}}}
@keyframes crece-sep{{from{{transform:scale(.2) translate(-4px,4px);opacity:0}}70%{{transform:scale(1) translate(-4px,4px);opacity:1}}to{{transform:scale(1) translate(0,0);opacity:1}}}}
@keyframes punto{{from{{transform:scale(0)}}to{{transform:scale(1)}}}}}}
</style>{flor(cls=True)}</svg>'''
W['simbolo-bloom']=anim
os.makedirs(OUT,exist_ok=True)
for n,s in W.items(): open(f'{OUT}/{n}.svg','w').write(s)
json.dump({'nombre':'laranda','historia':'la jacaranda sin la jota: el instante de florecer','simbolo':'flor dibujada a mano: línea de tinta, mancha violeta desfasada (8,7), el lóbulo superior derecho separado en naranja, garganta vacía',
 'color':{'violeta':VIO,'violeta-presionado':VIO2,'lila':LILA,'niebla':NIEBLA,'naranja':NAR,'naranja-tinte':NAR_T,'naranja-oscuro':NAR_D,'oro-reservar':ORO,'verde-exito':VERDE,'rojo-error':ROJO,'tinta':INK,'tinta-suave':SUAVE,'hueso':HUESO,'arena':ARENA,'superficie-oscura':OSC_SURF},
 'reglas':{'oro':'solo botón Reservar y confirmación de cita; texto en tinta','estados':'siempre color + icono + texto','naranja':'acento de marca: lóbulo separado, enlaces, destacados, ilustración; como texto solo en tamaño grande (3.2:1)','oscuro':'violeta sube a lila, naranja a naranja-oscuro, mancha en lila'},
 'tipografia':{'primaria':'Bricolage Grotesque 600, opsz 96 (wordmark en trazados; títulos)','secundaria':'Onest 400/500/700 (interfaz y cuerpo)','mono':'IBM Plex Mono 500 (folios)'},
 'tamanos_minimos':{'simbolo':'40 px; de 16 a 32 px, la silueta','lockup-h':'120 px','lockup-v':'80 px','wordmark':'80 px'},
 'area_de_respeto':'la altura del punto central de la flor (r = 4.5 en 128)',
 'contraste':{'violeta/hueso':7.0,'naranja/hueso':3.2,'verde/hueso':3.7,'rojo/hueso':6.6,'tinta/oro':8.2,'lila/tinta':10.4,'naranja-oscuro/tinta':7.7}},open('tema.json','w'),indent=2,ensure_ascii=False)
print('ok',list(W))
