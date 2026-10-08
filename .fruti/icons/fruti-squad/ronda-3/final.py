import math, sys
C=256; BG='#161616'; FG='#F8F8F5'; AC='#B7F34D'
def pol(r,a): a=math.radians(a); return (C+r*math.cos(a), C+r*math.sin(a))
def simbolo(w,span,r0,r1,core,n=12):
  ps=[]
  for i in range(5):
    p=[pol(r0+(t/n)*(r1-r0), -90+i*72+span*t/n) for t in range(n+1)]
    ps.append('M'+' '.join('%.1f %.1f'%q for q in p))
  return ps,core,w
def svg(params,escala,modo,anim=True,fondo=True,name='fs'):
  ps,core,w=simbolo(**params)
  fg={'tile':f'var(--fs-claro,{FG})','tinta':'currentColor'}[modo]
  ac={'tile':f'var(--fs-acento,{AC})','tinta':'currentColor'}[modo]
  mods=''.join(f'<path class="fs-esp__modulo fs-esp__modulo--{i}" d="{d}"/>' for i,d in enumerate(ps))
  css=(f'.fs-esp__modulo{{fill:none;stroke:{fg};stroke-width:{w};stroke-linecap:round;stroke-linejoin:round}}'
       f'.fs-esp__nucleo{{fill:{ac}}}')
  if anim:
    css+=(f'.fs-esp__modulo,.fs-esp__nucleo{{transform-origin:{C}px {C}px}}'
          '.fs-esp--entrada .fs-esp__modulo{animation:fs-esp-abre 700ms cubic-bezier(.25,1.3,.5,1) both}'
          + ''.join(f'.fs-esp--entrada .fs-esp__modulo--{i}{{animation-delay:{i*70}ms}}' for i in range(5)) +
          '.fs-esp--entrada .fs-esp__nucleo{animation:fs-esp-nucleo 480ms 720ms cubic-bezier(.3,1.8,.5,1) both}'
          '@keyframes fs-esp-abre{from{transform:rotate(-150deg) scale(.35);opacity:0}to{transform:none;opacity:1}}'
          '@keyframes fs-esp-nucleo{from{transform:scale(0)}to{transform:scale(1)}}'
          '@media (prefers-reduced-motion:reduce){.fs-esp--entrada *{animation:none!important}}')
  tile=f'<rect width="512" height="512" rx="112" fill="var(--fs-fondo,{BG})"/>' if fondo else ''
  cls='fs-esp'+(' fs-esp--entrada' if anim else '')
  aria='role="img" aria-label="Fruti Squad"'
  return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" {aria} class="{cls}">'
          f'<style>{css}</style>{tile}<g transform="translate({C} {C}) scale({escala}) translate(-{C} -{C})">{mods}'
          f'<circle class="fs-esp__nucleo" cx="{C}" cy="{C}" r="{core}"/></g></svg>\n')
ANTES=dict(w=66,span=54,r0=118,r1=190,core=52)
AHORA=dict(w=68,span=40,r0=130,r1=200,core=46)
