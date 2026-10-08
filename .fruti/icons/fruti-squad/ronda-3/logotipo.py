import sys, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
sys.path.insert(0,'.'); from final import simbolo
SRC=sys.argv[1]; OUT=sys.argv[2]
fonts={}
def inst(w):
  if w not in fonts:
    f=TTFont(SRC); instantiateVariableFont(f,{'wght':w},inplace=True); f.save(f'sora-{w}.ttf'); fonts[w]=TTFont(f'sora-{w}.ttf')
  return fonts[w]
def texto(s,w,size,x0,y0):
  f=inst(w); upm=f['head'].unitsPerEm
  blob=hb.Blob.from_file_path(f'sora-{w}.ttf'); face=hb.Face(blob); font=hb.Font(face)
  buf=hb.Buffer(); buf.add_str(s); buf.guess_segment_properties(); hb.shape(font,buf,{'kern':True,'liga':True})
  gs=f.getGlyphSet(); order=f.getGlyphOrder(); k=size/upm; x=0; d=''
  for info,pos in zip(buf.glyph_infos,buf.glyph_positions):
    pen=SVGPathPen(gs); tp=TransformPen(pen,(k,0,0,-k,x0+(x+pos.x_offset)*k,y0-pos.y_offset*k))
    gs[order[info.codepoint]].draw(tp); d+=pen.getCommands(); x+=pos.x_advance
  return d, x*k
def icono(x,y,s,arm,core):
  ps,c,w=simbolo(w=64,span=46,r0=116,r1=212,core=44)
  e=s/512
  g=''.join(f'<path d="{p}"/>' for p in ps)
  return (f'<g transform="translate({x} {y}) scale({e:.5f})"><g transform="translate(256 256) scale(1.04) translate(-256 -256)" fill="none" stroke="{arm}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{g}</g>'
          f'<circle cx="256" cy="256" r="{c*1.04:.1f}" fill="{core}"/></g>')
def lockup(modo,kiro):
  arm,core,tx,kc={'oscuro':('#F8F8F5','#B7F34D','#F8F8F5','#B7F34D'),'tinta':('currentColor',)*4}[modo]
  H=120
  d1,w1=texto('Fruti Squad',700,64 if not kiro else 60,148,82 if not kiro else 66)
  body=icono(0,0,H,arm,core)+f'<path fill="{tx}" d="{d1}"/>'
  W=148+w1
  if kiro:
    d2,w2=texto('for Kiro',500,30,150,108); body+=f'<path fill="{kc}" d="{d2}"/>'; W=max(W,150+w2)
  label='Fruti Squad for Kiro' if kiro else 'Fruti Squad'
  return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 {W+8:.0f} {H+8}" role="img" aria-label="{label}">{body}</svg>\n'
for kiro in (False,True):
  for modo in ('oscuro','tinta'):
    n=f'{OUT}/fruti-squad-logotipo{"-kiro" if kiro else ""}-{modo}.svg'; open(n,'w').write(lockup(modo,kiro)); print(n)
