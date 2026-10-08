import math
INK='#261818'; R_='#f93e3d'; O='#fc8816'; Y='#fcc22a'; G='#7dd258'; P='#9d56dc'; CREAM='#fff4e0'; GD='#4fa83a'
def leaf(cx,cy,ang,L,Wd,col):
  # almond leaf from base (cx,cy) along angle
  a=math.radians(ang); ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux
  tip=(cx+ux*L,cy+uy*L)
  c1=(cx+ux*L*.3+px*Wd,cy+uy*L*.3+py*Wd); c2=(cx+ux*L*.75+px*Wd*.8,cy+uy*L*.75+py*Wd*.8)
  d1=(cx+ux*L*.3-px*Wd,cy+uy*L*.3-py*Wd); d2=(cx+ux*L*.75-px*Wd*.8,cy+uy*L*.75-py*Wd*.8)
  f=lambda p:'%.1f %.1f'%p
  return f'<path fill="{col}" d="M{f((cx,cy))}C{f(c1)} {f(c2)} {f(tip)}C{f(d2)} {f(d1)} {f((cx,cy))}Z"/>'
def wedge(cx,cy,r,a0,a1,g,col):
  m=(a0+a1)/2; half=math.radians((a1-a0)/2)
  off=g/2/math.sin(half)
  ax,ay=cx+off*math.cos(math.radians(m)),cy+off*math.sin(math.radians(m))
  # arc endpoints shifted inward by gap
  da=math.degrees(g/2/r)
  b0,b1=math.radians(a0+da),math.radians(a1-da)
  p0=(cx+r*math.cos(b0),cy+r*math.sin(b0)); p1=(cx+r*math.cos(b1),cy+r*math.sin(b1))
  return f'<path fill="{col}" d="M{ax:.1f} {ay:.1f}L{p0[0]:.1f} {p0[1]:.1f}A{r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}Z"/>'
V={}
# A · Gajos: citrus slice of 5 agents around the orchestrator
cx,cy,r=256,284,172
s=''.join(wedge(cx,cy,r,-90+i*72-36,-90+i*72+36,22,c) for i,c in enumerate([R_,O,Y,G,P]))
s+=f'<circle cx="{cx}" cy="{cy}" r="40" fill="{CREAM}"/>'
s+=f'<path d="M256 112V84" stroke="{CREAM}" stroke-width="18" stroke-linecap="round" fill="none"/>'+leaf(262,96,-28,120,34,G)
V['a-gajos']=s
# B · Racimo: five fruits held by one stem (orchestrator)
r=68; top=[(108,232,R_),(256,232,O),(404,232,Y)]; bot=[(182,366,G),(330,366,P)]
s=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x,y,c in top+bot)
s+=f'<path d="M256 164V96" stroke="{CREAM}" stroke-width="20" stroke-linecap="round" fill="none"/>'+leaf(264,112,-24,130,36,G)
V['b-racimo']=s
# C · Hoja-red: shared leaf (steering) whose veins connect the agents
s=leaf(96,420,-45,430,150,G)
vein=f'<path d="M110 406 L382 134" stroke="{GD}" stroke-width="16" stroke-linecap="round" fill="none"/>'
pts=[(190,326,248,206,R_),(258,258,330,330,O),(320,196,214,190,Y)]
for x0,y0,x1,y1,c in pts: vein+=f'<path d="M{x0} {y0}L{x1} {y1}" stroke="{GD}" stroke-width="12" stroke-linecap="round" fill="none"/>'
dots=''.join(f'<circle cx="{x1}" cy="{y1}" r="30" fill="{c}" stroke="{G}" stroke-width="0"/>' for x0,y0,x1,y1,c in pts)
dots+=f'<circle cx="382" cy="134" r="30" fill="{P}"/><circle cx="110" cy="406" r="30" fill="{CREAM}"/>'
V['c-hoja']=s+vein+dots
for k,body in V.items():
  open(f'{k}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="112" fill="{INK}"/>{body}</svg>')
  open(f'{k}-simbolo.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">{body}</svg>')
# bench
rows=''
for k in V:
  cells=''.join(f'<img src="{k}.svg" style="width:{z}px;height:{z}px">' for z in (16,24,32,48,96,192))
  cells+=f'<span style="background:#fff;padding:8px;display:inline-flex;gap:8px"><img src="{k}-simbolo.svg" style="width:32px"><img src="{k}-simbolo.svg" style="width:96px"></span>'
  rows+=f'<div style="display:flex;align-items:center;gap:14px;padding:10px"><b style="width:90px">{k}</b>{cells}</div>'
open('banco.html','w').write(f'<html><body style="margin:0;background:#eceef2;font:13px sans-serif">{rows}</body></html>')
# A2 · Gajos con cáscara: anillo exterior para leerse como rodaja, no como gráfico de pastel
cx,cy=256,286
s=f'<circle cx="{cx}" cy="{cy}" r="186" fill="{CREAM}"/><circle cx="{cx}" cy="{cy}" r="170" fill="{INK}"/>'
s+=''.join(wedge(cx,cy,156,-90+i*72-36,-90+i*72+36,20,c) for i,c in enumerate([R_,O,Y,G,P]))
s+=f'<circle cx="{cx}" cy="{cy}" r="34" fill="{CREAM}"/>'
s+=f'<path d="M256 100V70" stroke="{CREAM}" stroke-width="18" stroke-linecap="round" fill="none"/>'+leaf(262,84,-28,116,32,G)
V2={'a2-rodaja':s}
# B2 · Racimo unido: el tallo se ramifica hasta cada fruta (orquestador que delega)
r=64; top=[(112,250,R_),(256,250,O),(400,250,Y)]; bot=[(184,382,G),(328,382,P)]
br=f'<path d="M256 186V92M256 150C256 170 160 160 130 196M256 150C256 170 352 160 382 196" stroke="{CREAM}" stroke-width="16" stroke-linecap="round" fill="none"/>'
s=br+''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x,y,c in top+bot)+leaf(264,108,-24,120,34,G)
V2['b2-racimo']=s
for k,body in V2.items():
  open(f'{k}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="112" fill="{INK}"/>{body}</svg>')
  open(f'{k}-simbolo.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">{body}</svg>')
rows=''
for k in ['a-gajos','a2-rodaja','b-racimo','b2-racimo','c-hoja']:
  cells=''.join(f'<img src="{k}.svg" style="width:{z}px;height:{z}px">' for z in (16,24,32,48,96,192))
  cells+=f'<span style="background:#fff;padding:8px;display:inline-flex;gap:8px;align-items:center"><img src="{k}-simbolo.svg" style="width:32px"><img src="{k}-simbolo.svg" style="width:96px"></span>'
  rows+=f'<div style="display:flex;align-items:center;gap:14px;padding:8px"><b style="width:90px">{k}</b>{cells}</div>'
open('banco.html','w').write(f'<html><body style="margin:0;background:#eceef2;font:13px sans-serif">{rows}</body></html>')
