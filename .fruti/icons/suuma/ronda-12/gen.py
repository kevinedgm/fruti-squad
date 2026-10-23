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

def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]; c=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in c]; return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def cr(a,b): la,lb=lum(a),lum(b); return round((max(la,lb)+0.05)/(min(la,lb)+0.05),1)
f=F(S+'/fuentes/BricolageGrotesque[opsz,wdth,wght].ttf',{'wght':600,'opsz':96,'wdth':100},'bric600')
PAL={
 'R1':('Bermellón y mostaza','#C8102E','#E9B824'),'R2':('Índigo noche y mandarina','#2A2A72','#FF7A1A'),'R3':('Naranja quemado y botella','#D4541A','#0B4F3F'),
 'R4':('Lila eléctrico y limón','#6A4CFF','#FFD23F'),'R5':('Frambuesa y menta','#B5174E','#2EC4A6'),'R6':('Cadmio y tinta','#121212','#FFD400')}
def word_c(ink,inner):
    body,x3=f.word(inner_c=inner,track=-SIZE*0.01)
    return body.replace(f'fill="{INK}"',f'fill="{ink}"').replace(f'stroke="{INK}"',f'stroke="{ink}"'),x3
def app(bg,glyph,inner,size=96):
    uu,w=f.nested(0,inner); uu=uu.replace(f'stroke="{INK}"',f'stroke="{glyph}"'); pad=w*0.22; side=w+2*pad; y0=Y-f.xh-pad-(w-f.xh)/2
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {y0} {side:.0f} {side:.0f}" width="{size}" height="{size}"><rect x="{-pad}" y="{y0}" width="{side:.0f}" height="{side:.0f}" rx="{side*0.22:.0f}" fill="{bg}"/>{uu}</svg>'
rows=''
for k,(name,crom,acc) in PAL.items():
    wm,x3=word_c(INK,crom); W=x3+8; wd,_=word_c(BG,acc)
    svg=lambda b,bg,w=300: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 20 {W:.0f} 130" width="{w}" style="background:{bg};border-radius:10px;padding:14px 18px;box-sizing:content-box">{b}</svg>'
    sw=''.join(f'<i style="background:{v}"></i>' for v in (crom,acc,BG,INK))
    rows+=f'<div class="c"><h2>{k} · {name}</h2><div class="sw">{sw}</div><div class="row">{svg(wm,BG)}{svg(wd,INK)}{app(crom,BG,acc)}{app(BG,INK,crom)}{app(INK,BG,acc)}</div><p>cromático/blanco {cr(crom,BG)} · acento/blanco {cr(acc,BG)} · blanco/cromático {cr(BG,crom)} · acento/cromático {cr(acc,crom)} · acento/tinta {cr(acc,INK)}</p></div>'
    open(f'{k}.svg','w').write(svg(wm,BG,W))
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#FFFFFF;color:#121212;font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 20px;color:#5B5750}}
.c{{padding:18px 0;border-top:1px solid #E6E1D8;display:grid;gap:10px}}.c h2{{font:600 16px sans-serif;margin:0}}.sw{{display:flex;gap:6px}}.sw i{{display:block;width:40px;height:22px;border-radius:5px;border:1px solid rgba(0,0,0,.08)}}
.row{{display:flex;gap:18px;align-items:center;flex-wrap:wrap}}.c p{{margin:0;color:#5B5750;font-size:12px}}
</style></head><body><h1>SUUMA · ronda 12 · color sobre Bricolage Grotesque 600</h1><p class="i">Las seis familias de la ronda 10 sobre el wordmark definitivo. Por fila: wordmark claro y oscuro; icono sobre el cromático, sobre blanco y sobre tinta; contrastes WCAG.</p>{rows}</body></html>""")
print('ok')
