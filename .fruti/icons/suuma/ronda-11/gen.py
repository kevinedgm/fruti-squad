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
FONTS=[('Bricolage Grotesque 600 · opsz 96',S+'/fuentes/BricolageGrotesque[opsz,wdth,wght].ttf',{'wght':600,'opsz':96,'wdth':100},'bric600'),
       ('Bricolage Grotesque 700 · opsz 96',S+'/fuentes/BricolageGrotesque[opsz,wdth,wght].ttf',{'wght':700,'opsz':96,'wdth':100},'bric700'),
       ('Onest 600',S+'/fuentes/Onest.ttf',{'wght':600},'onest600'),
       ('Onest 700',S+'/fuentes/Onest.ttf',{'wght':700},'onest700'),
       ('Manrope 700 (referencia, rondas 4–10)',S+'/fuentes/Manrope[wght].ttf',{'wght':700},'manrope700')]
rows=''; out={}
for name,src,axes,tag in FONTS:
    f=F(src,axes,tag); body,x3=f.word(track=-SIZE*0.01); W=x3+8
    svg=lambda b,w,h=None: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 20 {W:.0f} 130" width="{w}" height="{h or int(w*130/W)}">{b}</svg>'
    inv=body.replace(INK,'@@').replace(BG,INK).replace('@@',BG)
    rows+=f'<div class="c"><h2>{name}</h2><div class="row">{svg(body,420)}<div class="dk">{svg(inv,300)}</div><span>{svg(body,80)}<small>80 px</small></span></div></div>'
    open(f'{tag}.svg','w').write(svg(body,W,130))
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:{BG};color:{INK};font:14px/1.4 sans-serif;padding:32px}}h1{{font:600 22px sans-serif;margin:0 0 4px}}p.i{{margin:0 0 16px;color:#5B5750}}
.c{{padding:16px 0;border-top:1px solid #E6E1D8;display:grid;gap:8px}}.c h2{{font:600 15px sans-serif;margin:0}}.row{{display:flex;gap:28px;align-items:center;flex-wrap:wrap}}.dk{{background:{INK};padding:10px 16px;border-radius:10px}}.row span{{display:grid;gap:4px;justify-items:center;font-size:11px;color:#5B5750}}
</style></head><body><h1>SUUMA · ronda 11 · tipografía</h1><p class="i">B1 reconstruida con el tallo y el cuenco de cada fuente. Bricolage Grotesque y Onest frente a Manrope. En blanco y negro para juzgar solo la letra.</p>{rows}</body></html>""")
print('ok')
