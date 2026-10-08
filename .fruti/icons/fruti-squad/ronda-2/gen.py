import math
INK='#261818'; CREAM='#fff4e0'; LEAF='#7dd258'; LEAFD='#4fa83a'; SPARK='#fcc22a'
def P(cx,cy,r,a): a=math.radians(a); return (cx+r*math.cos(a), cy+r*math.sin(a))
def f(p): return '%.1f %.1f'%p
def wedge_d(cx,cy,r,a0,a1,g):
  m=(a0+a1)/2; half=math.radians((a1-a0)/2); off=g/2/math.sin(half)
  ap=P(cx,cy,off,m); da=math.degrees(g/2/r)
  return f'M{f(ap)}L{f(P(cx,cy,r,a0+da))}A{r} {r} 0 0 1 {f(P(cx,cy,r,a1-da))}Z'
def leaf(cx,cy,ang,L,Wd,col,cls=''):
  a=math.radians(ang); ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux
  q=lambda t,w:(cx+ux*L*t+px*w,cy+uy*L*t+py*w)
  return f'<path class="{cls}" fill="{col}" d="M{f((cx,cy))}C{f(q(.3,Wd))} {f(q(.75,Wd*.8))} {f(q(1,0))}C{f(q(.75,-Wd*.8))} {f(q(.3,-Wd))} {f((cx,cy))}Z"/>'
def paw(x,y,s,col):
  t=''.join(f'<ellipse cx="{x+dx*s:.1f}" cy="{y+dy*s:.1f}" rx="{5*s:.1f}" ry="{6.5*s:.1f}" fill="{col}"/>' for dx,dy in ((-11,-8),(-4,-15),(4,-15),(11,-8)))
  return t+f'<ellipse cx="{x}" cy="{y+5*s:.1f}" rx="{10*s:.1f}" ry="{8.5*s:.1f}" fill="{col}"/>'
# texture of each squad member inside a sector (angles a0..a1, centre cx,cy)
def miembro(n,cx,cy,a0,a1,R,g,cid):
  m=(a0+a1)/2; out=[]
  clip=f'<clipPath id="{cid}"><path d="{wedge_d(cx,cy,R,a0,a1,g)}"/></clipPath>'
  if n=='kiwi':
    out=[f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#8a5a2b"/>',f'<circle cx="{cx}" cy="{cy}" r="{R*.88}" fill="#8cc63f"/>',f'<circle cx="{cx}" cy="{cy}" r="{R*.42}" fill="#eef3c4"/>']
    for k in (-.28,0,.28):
      x,y=P(cx,cy,R*.6,m+(a1-a0)*k); out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{R*.035:.1f}" ry="{R*.07:.1f}" fill="{INK}" transform="rotate({m+(a1-a0)*k+90:.1f} {x:.1f} {y:.1f})"/>')
  elif n=='lima':
    out=[f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#3f9b2f"/>',f'<circle cx="{cx}" cy="{cy}" r="{R*.9}" fill="#f1f7cf"/>',f'<circle cx="{cx}" cy="{cy}" r="{R*.82}" fill="#b5e04a"/>']
    x0,y0=P(cx,cy,R*.2,m); x1,y1=P(cx,cy,R*.72,m); out.append(f'<path d="M{x0:.1f} {y0:.1f}L{x1:.1f} {y1:.1f}" stroke="#e3f3a0" stroke-width="{R*.04:.1f}" stroke-linecap="round"/>')
  elif n=='coco':
    out=[f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#6e4126"/>',f'<circle cx="{cx}" cy="{cy}" r="{R*.84}" fill="{CREAM}"/>',f'<circle cx="{cx}" cy="{cy}" r="{R*.5}" fill="#f3e6cc"/>']
  elif n=='mora':
    out=[f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#3d1660"/>',f'<circle cx="{cx}" cy="{cy}" r="{R*.9}" fill="#6b2fa0"/>']
    for rr,k in ((.72,-.25),(.72,.25),(.45,0),(.9*.85,0)):
      x,y=P(cx,cy,R*rr,m+(a1-a0)*k); out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{R*.1:.1f}" fill="#9a5fdc"/>')
  elif n=='bruno':
    out=[f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#b8742f"/>',f'<circle cx="{cx}" cy="{cy}" r="{R*.88}" fill="#f0b45e"/>']
    x,y=P(cx,cy,R*.6,m); out.append(paw(round(x,1),round(y,1),R/180*1.5,'#7a4a1f'))
  return clip, f'<g clip-path="url(#{cid})">{"".join(out)}</g>'
ORDEN=['kiwi','lima','coco','mora','bruno']
def svg(cls,body,css,desc,vb='0 0 512 512',tile=True):
  bg=f'<rect class="fs-fondo" width="512" height="512" rx="112" fill="{INK}"/>' if tile else ''
  return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="Fruti Squad" class="fs fs--{cls}">\n'
          f'  <!-- Fruti Squad · {desc} -->\n  <style>{css}@media (prefers-reduced-motion:reduce){{.fs--{cls} *{{animation:none!important}}}}</style>\n{bg}{body}\n</svg>\n')
OUT={}
# ===== V1 · LA FRUTA DEL EQUIPO: una fruta hecha de los cinco miembros; se ensambla en el orden de la cadena
cx,cy,R,g=256,282,178,16
defs=''; grupos=''; css=''
for i,n in enumerate(ORDEN):
  a0=-90-36+i*72; a1=a0+72; m=a0+36
  clip,g_=miembro(n,cx,cy,a0,a1,R,g,f'v1-{n}')
  defs+=clip
  dx,dy=[v*150 for v in (math.cos(math.radians(m)),math.sin(math.radians(m)))]
  grupos+=f'<g class="g{i}">{g_}</g>'
  css+=(f'.fs--equipo .g{i}{{animation:fs-eq-{i} 520ms {120+i*110}ms cubic-bezier(.3,1.5,.55,1) both}}'
        f'@keyframes fs-eq-{i}{{from{{transform:translate({dx:.0f}px,{dy:.0f}px) rotate({-40 if i%2 else 40}deg);opacity:0;transform-origin:{cx}px {cy}px}}to{{transform:none;opacity:1;transform-origin:{cx}px {cy}px}}}}')
hub=f'<circle class="hub" cx="{cx}" cy="{cy}" r="30" fill="{CREAM}"/>'
css+=(f'.fs--equipo .hub{{transform-origin:{cx}px {cy}px;animation:fs-pop 420ms 760ms cubic-bezier(.3,1.8,.5,1) both}}'
      f'.fs--equipo .hoja{{transform-origin:262px 92px;animation:fs-brota 460ms 900ms cubic-bezier(.3,1.6,.5,1) both}}'
      '@keyframes fs-pop{from{transform:scale(0)}to{transform:scale(1)}}@keyframes fs-brota{from{transform:scale(0) rotate(-60deg)}to{transform:none}}')
stem=f'<g class="hoja"><path d="M256 104V78" stroke="{CREAM}" stroke-width="16" stroke-linecap="round"/>{leaf(262,92,-28,112,32,LEAF)}</g>'
OUT['equipo']=svg('equipo',f'<defs>{defs}</defs>{grupos}{hub}{stem}',css,'«La fruta del equipo»: una sola fruta hecha de Kiwi, Lima, Coco, Mora y Bruno; al aparecer, cada gajo llega en el orden de la cadena y el orquestador (centro) los une.')
# ===== V2 · RELEVO: el orquestador pasa el trabajo; la chispa recorre a los miembros en orden
cx,cy,RR,r=256,268,150,62
defs=''; nodos=''; css=''
pos=[P(cx,cy,RR,-90+i*72) for i in range(5)]
arco=' '.join(('M' if i==0 else 'L')+f(pos[i]) for i in range(5))+'Z'
pista=f'<path d="{arco}" fill="none" stroke="#4a3434" stroke-width="10" stroke-linejoin="round"/>'
for i,n in enumerate(ORDEN):
  x,y=pos[i]
  clip,g_=miembro(n,x,y,0,359.99,r,0.001,f'v2-{n}')
  # full circle: use simple circle clip instead of wedge
  clip=f'<clipPath id="v2-{n}"><circle cx="{x:.1f}" cy="{y:.1f}" r="{r}"/></clipPath>'
  inner=g_.replace(f'clip-path="url(#v2-{n})"',f'clip-path="url(#v2-{n})"')
  defs+=clip; nodos+=f'<g class="n{i}" style="transform-origin:{x:.1f}px {y:.1f}px">{inner}</g>'
  css+=f'.fs--relevo .n{i}{{animation:fs-rel-bote 2400ms {i*380+260}ms infinite}}'
# make member textures circular: miembro() draws circles centred on (x,y) when a0..a1 full -> textures centred, fine
hub=f'<circle cx="{cx}" cy="{cy}" r="38" fill="{CREAM}"/>'+leaf(cx+6,cy-30,-30,70,20,LEAF)
pts=[(cx,cy)]+pos+[(cx,cy)]
kf=[]; tot=2400
for j,p in enumerate(pts):
  pct=min(100,j*380*100/tot); kf.append(f'{pct:.1f}%{{transform:translate({p[0]-cx:.1f}px,{p[1]-cy:.1f}px)}}')
css+=('.fs--relevo .chispa{animation:fs-rel-chispa 2400ms cubic-bezier(.6,0,.4,1) infinite}'
      '@keyframes fs-rel-chispa{'+''.join(kf)+'100%{transform:none}}'
      '@keyframes fs-rel-bote{0%,100%{transform:scale(1)}6%{transform:scale(1.16)}14%{transform:scale(1)}}')
chispa=f'<circle class="chispa" cx="{cx}" cy="{cy}" r="16" fill="{SPARK}"/>'
OUT['relevo']=svg('relevo',f'<defs>{defs}</defs>{pista}{nodos}{hub}{chispa}',css,'«Relevo»: el orquestador (centro) entrega el trabajo y la chispa pasa por Kiwi → Lima → Coco → Mora → Bruno; cada miembro rebota al recibirlo. Bucle de 2.4 s (para cargas); estático es el icono.')
# ===== V3 · </> FRUTAL: dos hojas forman los corchetes de código y dentro gira la rodaja del equipo
cx,cy,R=256,256,92
defs=''; gaj=''
for i,n in enumerate(ORDEN):
  a0=-90-36+i*72; a1=a0+72
  clip,g_=miembro(n,cx,cy,a0,a1,R,9,f'v3-{n}'); defs+=clip; gaj+=g_
def chev(sx,col,cls):
  # chevron made of two leaves meeting at the tip
  tipx=256-sx*196; a=45 if sx>0 else 135
  return f'<g class="{cls}">'+leaf(tipx,256,-a,124,26,col)+leaf(tipx,256,a,124,26,col)+'</g>'
css=(f'.fs--codigo .rodaja{{transform-origin:{cx}px {cy}px;animation:fs-cod-gira 900ms 250ms cubic-bezier(.3,1.3,.5,1) both}}'
     '.fs--codigo .izq{animation:fs-cod-izq 600ms cubic-bezier(.3,1.5,.5,1) both}.fs--codigo .der{animation:fs-cod-der 600ms cubic-bezier(.3,1.5,.5,1) both}'
     '@keyframes fs-cod-gira{from{transform:rotate(-200deg) scale(.2);opacity:0}to{transform:none;opacity:1}}'
     '@keyframes fs-cod-izq{from{transform:translateX(90px);opacity:0}to{transform:none;opacity:1}}@keyframes fs-cod-der{from{transform:translateX(-90px);opacity:0}to{transform:none;opacity:1}}')
OUT['codigo']=svg('codigo',f'<defs>{defs}</defs>{chev(1,LEAF,"izq")}{chev(-1,LEAF,"der")}<g class="rodaja">{gaj}<circle cx="{cx}" cy="{cy}" r="16" fill="{CREAM}"/></g>',css,'«&lt;/&gt; frutal»: dos hojas forman los corchetes de código y dentro llega girando la rodaja del equipo: frutas que diseñan y construyen interfaces.')
import xml.dom.minidom as mm
for k,s in OUT.items(): mm.parseString(s); open(f'fs-{k}.svg','w').write(s); print(k,len(s))
