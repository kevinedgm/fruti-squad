import math
cx,cy,rx,ry,rot=12,12,9.6,6.1,-22
def elip(t):
    x,y=rx*math.cos(t),ry*math.sin(t); a=math.radians(rot)
    return (cx+x*math.cos(a)-y*math.sin(a), cy+x*math.sin(a)+y*math.cos(a))
t0=math.radians(-55); rest=elip(t0); N=36
# una vuelta completa en el sentido de la órbita; fotogramas sobre la elipse, relativos al punto de reposo
kf=''.join(f'{k*100/N:.2f}%{{transform:translate({elip(t0+2*math.pi*k/N)[0]-rest[0]:.2f}px,{elip(t0+2*math.pi*k/N)[1]-rest[1]:.2f}px)}}' for k in range(N+1))
css=f'''
    .uva-apollo{{stroke-width:var(--uva-stroke,1.5)}}
    .uva-apollo__senal{{fill:var(--uva-accent,currentColor);stroke:none}}
    /* Estado Ignición → En órbita: al arrancar un entorno, el satélite da una vuelta completa a la órbita (900 ms,
       una vez) y queda en su sitio. Sin brillo ni movimiento en reposo. El componente añade uva-apollo (modificador
       ignicion) al empezar el arranque y la quita en animationend. */
    .uva-apollo--ignicion{{--uva-apollo-senal:uva-apollo-orbitar}}
    .uva-apollo__senal{{animation:var(--uva-apollo-senal,none) 900ms cubic-bezier(.45,0,.25,1) 0s 1}}
    @keyframes uva-apollo-orbitar{{{kf}}}
    @media (prefers-reduced-motion:reduce){{
      .uva-apollo--ignicion{{--uva-apollo-senal:none}}
    }}
  '''
R='xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"'
svg=(f'<svg {R} class="uva-icon uva-apollo" aria-hidden="true">\n  <style>{css}</style>\n'
 '  <!-- apollo · prompt en órbita; un solo neón (el satélite) · ignición con la clase uva-apollo (modificador ignicion) -->\n'
 f'  <ellipse class="uva-apollo__orbita" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" transform="rotate({rot} {cx} {cy})"/>\n'
 '  <path class="uva-apollo__prompt" d="M9.7 10.3 11.5 11.8 9.7 13.3M12.7 13.7h2"/>\n'
 f'  <circle class="uva-apollo__senal" cx="{rest[0]:.2f}" cy="{rest[1]:.2f}" r="1.6"/>\n</svg>\n')
open('apollo.svg','w').write(svg)
open('apollo-anim.svg','w').write(svg.replace('class="uva-icon uva-apollo"','class="uva-icon uva-apollo uva-apollo--ignicion"'))
