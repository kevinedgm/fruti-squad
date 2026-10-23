import os,sys,math
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import uharfbuzz as hb
S=sys.argv[1]; INK='#121212'; BG='#FFFFFF'
SIZE=120; Y=110
class F:
    def __init__(s,src,axes,tag):
        inst=f'/tmp/suuma-{tag}.ttf'
        if not os.path.exists(inst):
            f=TTFont(src)
            if 'fvar' in f: instancer.instantiateVariableFont(f,axes).save(inst)
            else: f.save(inst)
        s.inst=inst; s.font=TTFont(inst); s.UPM=s.font['head'].unitsPerEm; s.GS=s.font.getGlyphSet()
        bp=BoundsPen(s.GS); s.GS['x'].draw(bp); s.XH=bp.bounds[3]
        bp=BoundsPen(s.GS); s.GS['l'].draw(bp); s.STEM=bp.bounds[2]-bp.bounds[0]
        bp=BoundsPen(s.GS); s.GS['u'].draw(bp); s.UW=bp.bounds[2]-bp.bounds[0]
        k=SIZE/s.UPM; s.xh=s.XH*k; s.st=s.STEM*k; s.uw=s.UW*k
    def palabra(s,txt,x0,track=0):
        hf=hb.Font(hb.Face(hb.Blob.from_file_path(s.inst))); b=hb.Buffer(); b.add_str(txt); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
        order=s.font.getGlyphOrder(); k=SIZE/s.UPM; x=x0; d=''
        for i,ps in zip(b.glyph_infos,b.glyph_positions):
            g=s.GS[order[i.codepoint]]; pen=SVGPathPen(s.GS); g.draw(TransformPen(pen,(k,0,0,-k,x,Y))); d+=pen.getCommands(); x+=ps.x_advance*k+track
        return d,x
    def U(s,x,w,top=None,depth=None,sw=None):
        sw=sw or s.st; rr=w/2-sw/2; top=Y-s.xh+sw/2 if top is None else top; yb=(depth or Y)-sw/2; x0=x+sw/2; x1=x+w-sw/2
        return f'<path d="M{x0:.1f} {top:.1f} V{yb-rr:.1f} A{rr:.1f} {rr:.1f} 0 0 0 {x1:.1f} {yb-rr:.1f} V{top:.1f}" fill="none" stroke="{INK}" stroke-width="{sw:.1f}"/>'
    def nested(s,x,inner_c=INK):
        bw=s.uw*1.3; big=s.U(x,bw); iw=bw-2*s.st-s.st*0.9; ix=x+(bw-iw)/2
        small=s.U(ix,iw,top=Y-s.xh*0.60+s.st*0.3,depth=Y-s.st*1.45,sw=s.st*0.6).replace(f'stroke="{INK}"',f'stroke="{inner_c}"')
        return big+small,x+bw
    def word(s,inner_c=INK,track=0):
        gap=s.st*0.9; d_s,x=s.palabra('s',0,track); x+=gap*0.3+track; uu,x2=s.nested(x,inner_c); d_ma,x3=s.palabra('ma',x2+gap*0.3+track,track)
        return f'<path d="{d_s}" fill="{INK}"/>{uu}<path d="{d_ma}" fill="{INK}"/>',x3

import json
TINTA='#121212'; BLANCO='#FFFFFF'; CADMIO='#FFD400'; PAPEL='#F5F4F0'
f=F(S+'/fuentes/BricolageGrotesque[opsz,wdth,wght].ttf',{'wght':600,'opsz':96,'wdth':100},'bric600')
def recolor(s,outer,inner):
    # f.nested/f.word pintan todo en INK; el interior lleva inner_c
    return s.replace(f'stroke="{INK}"',f'stroke="{outer}"').replace(f'fill="{INK}"',f'fill="{outer}"')
def simbolo(outer,inner,pad=10):
    uu,w=f.nested(0,inner); uu=recolor(uu,outer,inner); h=f.xh
    vb=f'{-pad} {Y-h-pad:.1f} {w+2*pad:.1f} {h+2*pad:.1f}'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{uu}</svg>',w,h
def wordmark(outer,inner):
    body,x3=f.word(inner_c=inner,track=-SIZE*0.01); body=recolor(body,outer,inner)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 {Y-f.xh*1.02-14:.1f} {x3+4:.1f} {f.xh*1.02+28:.1f}">{body}</svg>'
def lockup_h(outer,inner):
    body,x3=f.word(inner_c=inner,track=-SIZE*0.01); uu,w=f.nested(0,inner)
    k=1.0; g=f'<g transform="translate(0 0)">{uu}</g><g transform="translate({w+f.st*2.2:.1f} 0)">{body}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 {Y-f.xh*1.02-14:.1f} {w+f.st*2.2+x3+4:.1f} {f.xh*1.02+28:.1f}">{recolor(g,outer,inner)}</svg>'
def lockup_v(outer,inner):
    body,x3=f.word(inner_c=inner,track=-SIZE*0.01); uu,w=f.nested(0,inner); sc=1.6
    g=f'<g transform="translate({(x3-w*sc)/2:.1f} {-(f.xh*sc+f.st*3.2):.1f}) scale({sc})">{uu}</g>{body}'
    top=Y-f.xh*sc-f.st*3.2-f.xh-10
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 {top:.1f} {x3+4:.1f} {Y-top+16:.1f}">{recolor(g,outer,inner)}</svg>'
def app(bg,outer,inner,margin=0.22,rounded=True):
    uu,w=f.nested(0,inner); uu=recolor(uu,outer,inner); h=f.xh; side=w*(1+2*margin); x0=-(side-w)/2; y0=Y-h-(side-h)/2
    rect=f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{side:.1f}" height="{side:.1f}" rx="{side*0.22 if rounded else 0:.1f}" fill="{bg}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.1f} {y0:.1f} {side:.1f} {side:.1f}">{rect}{uu}</svg>'
def avatar(bg,outer,inner):
    uu,w=f.nested(0,inner); uu=recolor(uu,outer,inner); h=f.xh; side=w*1.5; x0=-(side-w)/2; y0=Y-h-(side-h)/2
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.1f} {y0:.1f} {side:.1f} {side:.1f}"><circle cx="{x0+side/2:.1f}" cy="{y0+side/2:.1f}" r="{side/2:.1f}" fill="{bg}"/>{uu}</svg>'
def favicon():
    uu,w=f.nested(0,CADMIO); h=f.xh; pad=6; vb=f'{-pad} {Y-h-pad:.1f} {w+2*pad:.1f} {h+2*pad:.1f}'
    uu=uu.replace(f'stroke="{INK}"','class="o"',1) if False else uu
    outer=recolor(uu,'currentColor',CADMIO)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"><style>svg{{color:{TINTA}}}@media (prefers-color-scheme:dark){{svg{{color:{BLANCO}}}}}</style>{outer}</svg>'
def tarjeta():
    lk=lockup_h(TINTA,CADMIO); inner=lk[lk.index('>')+1:-6]; vb=lk[lk.index('viewBox="')+9:]; vb=vb[:vb.index('"')]; x,y,w,h=map(float,vb.split())
    sc=560/w
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="{BLANCO}"/><rect x="0" y="590" width="1200" height="40" fill="{CADMIO}"/><g transform="translate({600-560/2:.1f} {315-h*sc/2:.1f}) scale({sc:.4f}) translate({-x:.1f} {-y:.1f})">{inner}</g></svg>'
out={
 'simbolo':simbolo(TINTA,CADMIO)[0],'simbolo-tinta':simbolo(TINTA,TINTA)[0],'simbolo-blanco':simbolo(BLANCO,CADMIO)[0],'simbolo-blanco-tinta':simbolo(BLANCO,BLANCO)[0],
 'wordmark':wordmark(TINTA,CADMIO),'wordmark-tinta':wordmark(TINTA,TINTA),'wordmark-oscuro':wordmark(BLANCO,CADMIO),
 'lockup-h':lockup_h(TINTA,CADMIO),'lockup-h-oscuro':lockup_h(BLANCO,CADMIO),'lockup-h-tinta':lockup_h(TINTA,TINTA),
 'lockup-v':lockup_v(TINTA,CADMIO),'lockup-v-oscuro':lockup_v(BLANCO,CADMIO),
 'app-icon':app(TINTA,BLANCO,CADMIO),'app-icon-cadmio':app(CADMIO,TINTA,TINTA),'app-icon-claro':app(BLANCO,TINTA,CADMIO),
 'app-icon-maskable':app(TINTA,BLANCO,CADMIO,margin=0.42,rounded=False),'avatar':avatar(TINTA,BLANCO,CADMIO),
 'favicon':favicon(),'tarjeta-redes':tarjeta()}
for k,v in out.items(): open(f'svg/{k}.svg','w').write(v)
json.dump({'nombre':'SUUMA','simbolo':'la doble U anidada: una u fina dentro de la u de la palabra; el nombre se lee «suma» y la segunda u vive dentro de la primera',
 'tipografia':{'wordmark':'Bricolage Grotesque 600, opsz 96, caja baja, tracking −1 %; en trazados','interfaz':'Onest 400/500/700','datos':'IBM Plex Mono 500 (provisional)'},
 'color':{'tinta':TINTA,'blanco':BLANCO,'papel':PAPEL,'cadmio':CADMIO,'cadmio-suave':'#FFF3B0','texto-secundario':'#5F5E5A','borde':'#E3E2DD','exito':'#0E7C4A','error':'#C8102E'},
 'reglas':['El cadmio nunca es texto: va en la u interior, en fondos con texto en tinta, en chips y en destacados.','La acción primaria va en tinta con texto blanco; el cadmio marca, no ordena.','Nada depende solo del color: estados con icono y texto.','Los estados (éxito/error) son provisionales hasta el design system.'],
 'archivos':sorted(out)},open('tema.json','w'),indent=1,ensure_ascii=False)
print('ok',sorted(out))
