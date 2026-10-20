# Conectti · paquete C: la ligadura tt. Símbolo, app icon, favicon, logotipo en minúsculas (IBM Plex Sans 600 en trazados) y pantalla de acceso según el DS.
# Uso: python gen.py <carpeta de fuentes con IBMPlexSans.ttf>
import sys,os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
S=sys.argv[1]; OUT='svg'
INK='#111820'; BG='#F4F7FA'; COB='#1D52BB'; COBS='#0439A1'; TEAL='#057F7D'; TEAL_INV='#5FD6CF'; WHITE='#FFFFFF'
src=S+'/fuentes/IBMPlexSans.ttf'; inst='/tmp/conectti-plex600.ttf'
if not os.path.exists(inst): instancer.instantiateVariableFont(TTFont(src),{'wght':600,'wdth':100}).save(inst)
FONT=TTFont(inst); UPM=FONT['head'].unitsPerEm
def palabra(s,size,x0,y0):
    hf=hb.Font(hb.Face(hb.Blob.from_file_path(inst))); b=hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    gs=FONT.getGlyphSet(); order=FONT.getGlyphOrder(); k=size/UPM; x=x0; d=''
    for i,ps in zip(b.glyph_infos,b.glyph_positions):
        g=gs[order[i.codepoint]]; pen=SVGPathPen(gs); g.draw(TransformPen(pen,(k,0,0,-k,x,y0))); d+=pen.getCommands(); x+=ps.x_advance*k
    return d,x
def svg(body,vb): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
# --- símbolo: dos t que comparten la barra; proporciones de la t de IBM Plex Sans 600 (fuste 128, barra 101 por 1000)
def tt(k,a,sw=7.5,bw=6):
    return f'<path d="M22 12 V42 a9 9 0 0 0 9 9 H34" stroke="{k}" stroke-width="{sw}"/><path d="M42 12 V42 a9 9 0 0 0 9 9 H54" stroke="{k}" stroke-width="{sw}"/><path d="M14 27 H60" stroke="{a}" stroke-width="{bw}"/>'
def tt16(k,a): # versión 16 px: trazos más gruesos, sin cola en la segunda t para no cerrar el hueco
    return f'<path d="M20 10 V40 a10 10 0 0 0 10 10 H32" stroke="{k}" stroke-width="9"/><path d="M42 10 V40 a10 10 0 0 0 10 10 H54" stroke="{k}" stroke-width="9"/><path d="M11 26 H60" stroke="{a}" stroke-width="8"/>'
W={}
W['simbolo']=svg(tt(COB,TEAL),'0 0 64 64')
W['simbolo-tinta']=svg(tt(INK,INK),'0 0 64 64')
W['simbolo-16']=svg(tt16(COB,TEAL),'0 0 64 64')
W['simbolo-inverso']=svg(tt(WHITE,TEAL_INV),'0 0 64 64')
# --- app icon: bloque cobalto, tt blanca con barra verde azulada clara; el bloque ocupa todo (las plataformas recortan la máscara)
def appicon(r):
    g=f'<g transform="translate(96 96) scale(5)">{tt(WHITE,TEAL_INV,7.5,6)}</g>'
    return svg(f'<rect width="512" height="512" rx="{r}" fill="{COB}"/>{g}','0 0 512 512')
W['app-icon']=appicon(0); W['app-icon-redondeado']=appicon(112)
# --- favicon: tt gruesa, cobalto sobre transparente; en esquema oscuro, blanca
W['favicon']=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" stroke-linecap="round" stroke-linejoin="round"><style>:root{{--k:{COB};--a:{TEAL}}}@media(prefers-color-scheme:dark){{:root{{--k:{WHITE};--a:{TEAL_INV}}}}}</style>{tt16("var(--k)","var(--a)")}</svg>'
# --- logotipo: "conectti" en minúsculas; barra compartida que sobresale; punto de la i en acento
def wordmark(k,a,size=100):
    y0=size*1.0; u=size/UPM
    d1,x=palabra('conec',size,0,y0); dt1,x1=palabra('t',size,x,y0); dt2,x2=palabra('t',size,x1,y0); di,x3=palabra('ı',size,x2,y0)
    bx=x+25*u; bw=(x2+90*u)-bx; by=y0-522*u; bh=101*u
    bar=f'<rect x="{bx:.2f}" y="{by:.2f}" width="{bw:.2f}" height="{bh:.2f}" rx="{bh/2:.2f}" fill="{a}"/>'
    dot=f'<circle cx="{x2+138*u:.2f}" cy="{y0-690*u:.2f}" r="{60*u:.2f}" fill="{a}"/>'
    return svg(f'<path d="{d1}{dt1}{dt2}{di}" fill="{k}"/>{bar}{dot}', f'0 0 {x3:.0f} {size*1.22:.0f}'), x3
W['wordmark'],WW=wordmark(COB,TEAL); W['wordmark-tinta'],_=wordmark(INK,INK); W['wordmark-inverso'],_=wordmark(WHITE,TEAL_INV)
# --- lockup horizontal: símbolo + nombre
def lockup(k,a):
    wm,w=wordmark(k,a,100); body=wm.split('>',1)[1].rsplit('</svg>',1)[0]
    return svg(f'<g transform="translate(0 10) scale(1.5)">{tt(k,a)}</g><g transform="translate(112 0)">{body}</g>',f'0 0 {112+w:.0f} 122')
W['lockup']=lockup(COB,TEAL); W['lockup-inverso']=lockup(WHITE,TEAL_INV)
os.makedirs(OUT,exist_ok=True)
for n,s in W.items(): open(f'{OUT}/{n}.svg','w').write(s)
print('ok',list(W))
