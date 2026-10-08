import math
BG='#161616'; FG='#F8F8F5'; AC='#B7F34D'
C=256
def pol(r,a): a=math.radians(a); return (C+r*math.cos(a), C+r*math.sin(a))
def svg(cls,mods,core,css,desc,ink=False):
  fg='currentColor' if ink else f'var(--fs-claro,{FG})'
  ac='currentColor' if ink else f'var(--fs-acento,{AC})'
  tile='' if ink else f'<rect width="512" height="512" rx="112" fill="var(--fs-fondo,{BG})"/>'
  body=mods.replace('FGC',fg)+core.replace('ACC',ac)
  return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="Fruti Squad" class="fs3 fs3--{cls}">\n'
          f'  <!-- Fruti Squad · «{cls}»: {desc} -->\n'
          f'  <style>{css}@media (prefers-reduced-motion:reduce){{.fs3--{cls} *{{animation:none!important}}}}</style>\n  {tile}{body}\n</svg>\n')
OUT={}
# ---- 1 ÓRBITA: núcleo + 5 semillas tangenciales (ligero giro = flujo)
mods=''; css=''
for i in range(5):
  a=-90+i*72; x,y=pol(162,a)
  mods+=(f'<g class="m m{i}"><rect x="{x-68:.1f}" y="{y-42:.1f}" width="136" height="84" rx="42" fill="FGC" '
         f'transform="rotate({a+90+28:.1f} {x:.1f} {y:.1f})"/></g>')
  css+=f'.fs3--orbita .m{i}{{animation:fs3-orb-{i} 560ms {i*90}ms cubic-bezier(.3,1.4,.5,1) both}}'
  css+=f'@keyframes fs3-orb-{i}{{from{{transform:rotate(-72deg) scale(.2);opacity:0}}to{{transform:none;opacity:1}}}}'
css+=f'.fs3--orbita .m{{transform-origin:{C}px {C}px}}.fs3--orbita .n{{transform-origin:{C}px {C}px;animation:fs3-nucleo 520ms 640ms cubic-bezier(.3,1.8,.5,1) both}}'
css+='@keyframes fs3-nucleo{from{transform:scale(0)}to{transform:scale(1)}}'
OUT['orbita']=(mods,f'<circle class="n" cx="{C}" cy="{C}" r="64" fill="ACC"/>',css,'núcleo (orquestador) y cinco semillas (agentes) en órbita, giradas para sugerir flujo. Las semillas salen del centro en orden y el núcleo se enciende al final (1.16 s, una vez).')
# ---- 2 ESPIRAL: 5 cápsulas curvas que se abren en espiral alrededor del núcleo
mods=''; css=''
for i in range(5):
  a0=-90+i*72+6; a1=a0+54
  p=[pol(118+ (t/10)*72, a0+(a1-a0)*t/10) for t in range(11)]
  d='M'+' L'.join('%.1f %.1f'%q for q in p)
  mods+=f'<g class="m m{i}"><path d="{d}" fill="none" stroke="FGC" stroke-width="66" stroke-linecap="round" stroke-linejoin="round"/></g>'
  css+=f'.fs3--espiral .m{i}{{animation:fs3-esp 700ms {i*70}ms cubic-bezier(.25,1.3,.5,1) both}}'
css+=(f'.fs3--espiral .m{{transform-origin:{C}px {C}px}}@keyframes fs3-esp{{from{{transform:rotate(-150deg) scale(.35);opacity:0}}to{{transform:none;opacity:1}}}}'
      f'.fs3--espiral .n{{transform-origin:{C}px {C}px;animation:fs3-nucleo2 480ms 720ms cubic-bezier(.3,1.8,.5,1) both}}@keyframes fs3-nucleo2{{from{{transform:scale(0)}}to{{transform:scale(1)}}}}')
OUT['espiral']=(mods,f'<circle class="n" cx="{C}" cy="{C}" r="52" fill="ACC"/>',css,'cinco cápsulas que se abren en espiral alrededor del núcleo: piezas distintas, un solo flujo. Se despliegan girando y el núcleo se enciende (1.2 s, una vez).')
# ---- 3 MONOGRAMA F modular: la F hecha de 4 módulos redondeados + el núcleo como quinto
W=76
mods=''.join([
 f'<g class="m m0"><rect x="118" y="96" width="{W}" height="150" rx="38" fill="FGC"/></g>',
 f'<g class="m m1"><rect x="118" y="266" width="{W}" height="150" rx="38" fill="FGC"/></g>',
 f'<g class="m m2"><rect x="214" y="96" width="180" height="{W}" rx="38" fill="FGC"/></g>',
 f'<g class="m m3"><rect x="214" y="218" width="104" height="{W}" rx="38" fill="FGC"/></g>'])
css=''
for i,(dx,dy) in enumerate(((0,-120),(0,120),(140,0),(110,0))):
  css+=f'.fs3--monograma .m{i}{{animation:fs3-mon-{i} 460ms {i*90}ms cubic-bezier(.3,1.5,.5,1) both}}@keyframes fs3-mon-{i}{{from{{transform:translate({dx}px,{dy}px);opacity:0}}to{{transform:none;opacity:1}}}}'
css+='.fs3--monograma .n{transform-origin:376px 382px;animation:fs3-nucleo3 460ms 520ms cubic-bezier(.3,1.8,.5,1) both}@keyframes fs3-nucleo3{from{transform:scale(0)}to{transform:scale(1)}}'
OUT['monograma']=(mods,'<circle class="n" cx="376" cy="382" r="42" fill="ACC"/>',css,'una F construida con cuatro módulos redondeados; el quinto es el punto lima, el orquestador que completa la marca. Los módulos llegan desde fuera y encajan (1 s, una vez).')
import xml.dom.minidom as mm
for k,(m,c,css,d) in OUT.items():
  for ink in (False,True):
    s=svg(k,m,c,css,d,ink); mm.parseString(s)
    open(f'fs-{k}{"-tinta" if ink else ""}.svg','w').write(s)
print('ok')
