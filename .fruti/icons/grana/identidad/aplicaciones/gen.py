# Grana · aplicaciones de marca. Uso: python gen.py <InstrumentSans[wdth,wght].ttf>
import sys, re, json, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
SRC=sys.argv[1]
P=json.load(open('../color/paleta.json'))
C={m:{k:P[m][k]['hex'] for k in ('carmin','nopal','cera','tinta')} for m in ('claro','oscuro')}
_c={}
def texto(s,size,x0,y0,wght,wdth=100,track=0):
    k=(wght,wdth)
    if k not in _c:
        f=TTFont(SRC); instantiateVariableFont(f,{'wght':wght,'wdth':wdth},inplace=True); p=f'/tmp/is-{wght}-{wdth}.ttf'; f.save(p); _c[k]=(TTFont(p),p)
    f,p=_c[k]; upm=f['head'].unitsPerEm
    font=hb.Font(hb.Face(hb.Blob.from_file_path(p))); buf=hb.Buffer(); buf.add_str(s); buf.guess_segment_properties(); hb.shape(font,buf,{'kern':True})
    gs=f.getGlyphSet(); order=f.getGlyphOrder(); kk=size/upm; x=0; d=''
    for info,pos in zip(buf.glyph_infos,buf.glyph_positions):
        pen=SVGPathPen(gs); gs[order[info.codepoint]].draw(TransformPen(pen,(kk,0,0,-kk,x0+x*kk,y0))); d+=pen.getCommands(); x+=pos.x_advance+track*upm
    return d, x*kk
sym=open('../ronda-2/a5-color.svg').read(); SYM=re.search(r'-->\n(.*)</svg>',sym,re.S).group(1)
s16=open('../ronda-2/a5-16.svg').read(); SYM16=re.search(r'-->\n(.*)</svg>',s16,re.S).group(1)
anim=open('../movimiento/grana-simbolo-animado.svg').read(); CSS=re.search(r'<style>(.*?)</style>',anim,re.S).group(1)
SYM_A=SYM.replace('<path d="M','<path pathLength="1" d="M')
def colorea(body,modo): return body.replace('var(--g-color-brand,#a3123a)',C[modo]['carmin']).replace('currentColor',C[modo]['tinta'])
w=lambda p,s: open(p,'w').write(s)
# 1 · FAVICON: versión de 16 px; tinta y tinte cambian con el tema del navegador
fav=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Grana"><style>'
     f'.t{{fill:{C["claro"]["carmin"]}}}.a{{stroke:{C["claro"]["tinta"]}}}'
     f'@media (prefers-color-scheme:dark){{.t{{fill:{C["oscuro"]["carmin"]}}}.a{{stroke:{C["oscuro"]["tinta"]}}}}}</style>'
     + SYM16.replace('fill="var(--g-color-brand,#a3123a)"','class="t"').replace('class="grana__tinte" ','').replace('stroke="currentColor"','class="a"').replace('class="grana__armazon" ','') + '</svg>\n')
w('favicon.svg',fav)
def tile(modo,sym_body,pad=.16,bg=None,r=0):
    bg=bg or C[modo]['cera']; s=48*(1-2*pad)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Grana"><rect width="48" height="48" rx="{r}" fill="{bg}"/>'
            f'<g transform="translate({48*pad:.2f} {48*pad:.2f}) scale({s/48:.4f})">{colorea(sym_body,modo)}</g></svg>\n')
w('avatar-claro.svg',tile('claro',SYM,.17)); w('avatar-oscuro.svg',tile('oscuro',SYM,.17))
w('app-icon.svg',tile('claro',SYM,.2)); w('app-icon-maskable.svg',tile('claro',SYM,.26))
# 3 · CABECERA DEL README: W2 + lema, en claro y en oscuro, con «la impresión» una vez
def cabecera(modo):
    c=C[modo]
    dn,wn=texto('grana',96,118,82,700,100,-0.015)
    dl,wl=texto("The only bug you'll want in your UI.",26,121,142,450)
    W=max(118+wn,121+wl)+10
    body=(f'<g class="grana-mov"><g transform="translate(0 6) scale(2)">{colorea(SYM_A,modo)}</g>'
          f'<path class="grana__nombre-tinte" fill="{c["carmin"]}" transform="translate(3.4 3.4)" d="{dn}"/><path fill="{c["tinta"]}" d="{dn}"/>'
          f'<path fill="{c["tinta"]}" fill-opacity=".74" d="{dl}"/></g>')
    css=CSS+'.grana-mov .grana__nombre-tinte{animation:grana-tenir 240ms ease-out 700ms both,grana-registro2 520ms var(--grana-mov-ease) 860ms both}@keyframes grana-registro2{from{translate:-3.4px -3.4px}to{translate:0 0}}'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 0 {W+4:.0f} 158" role="img" aria-label="Grana: the only bug you\'ll want in your UI."><style>{css}</style>{body}</svg>\n'
w('readme-cabecera-claro.svg',cabecera('claro')); w('readme-cabecera-oscuro.svg',cabecera('oscuro'))
# 4 · TARJETA PARA REDES 1280×640 (SVG; el PNG se renderiza aparte)
def tarjeta(modo,W=1280,H=640):
    c=C[modo]
    dn,wn=texto('grana',230,300,330,700,100,-0.015)
    dl,_=texto("The only bug you'll want in your UI.",44,108,450,450)
    dd,_=texto('Componentes Vue 3 · tema por tokens · accesible por diseño',28,108,520,500)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Grana"><rect width="{W}" height="{H}" fill="{c["cera"]}"/>'
            f'<g transform="translate(100 150) scale(4.2)">{colorea(SYM,modo)}</g>'
            f'<path fill="{c["carmin"]}" transform="translate(8 8)" d="{dn}"/><path fill="{c["tinta"]}" d="{dn}"/>'
            f'<path fill="{c["tinta"]}" fill-opacity=".8" d="{dl}"/><path fill="{c["nopal"]}" d="{dd}"/></svg>\n')
w('tarjeta-redes-claro.svg',tarjeta('claro')); w('tarjeta-redes-oscuro.svg',tarjeta('oscuro'))
print('ok')
