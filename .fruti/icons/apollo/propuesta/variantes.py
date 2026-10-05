import math
W=.75
R='xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'
def svg(i, nota, piezas):
    css=f'.uva-{i}{{stroke-width:var(--uva-stroke,1.5)}}.uva-{i}__senal{{fill:var(--uva-accent,currentColor);stroke:none}}'
    return f'<svg {R} class="uva-icon uva-{i}">\n  <style>{css}</style>\n  <!-- {nota} -->\n'+''.join(f'  {p}\n' for p in piezas)+'</svg>\n'
# A · cohete en vertical; el neón es el punto de ignición (dónde actuar: Lanzar)
A=svg('apollo-a','A · cohete: el neón es la ignición',[
 '<path class="uva-apollo-a__cohete" d="M12 2.5C14.5 4.5 15 7.5 15 10.5V16H9V10.5C9 7.5 9.5 4.5 12 2.5Z"/>',
 '<circle class="uva-apollo-a__ventana" cx="12" cy="9" r="1.5"/>',
 '<path class="uva-apollo-a__aleta" d="M9 12.75 7 15.25V17.5L9 16.5M15 12.75l2 2.5V17.5L15 16.5"/>',
 '<circle class="uva-apollo-a__senal" cx="12" cy="19.55" r="1.25"/>'])
# B · prompt en órbita: el neón es el satélite (En órbita = en ejecución)
cx,cy,rx,ry,rot=12,12,9.6,6.1,-22
def elip(t):
    x,y=rx*math.cos(t),ry*math.sin(t); a=math.radians(rot)
    return (cx+x*math.cos(a)-y*math.sin(a), cy+x*math.sin(a)+y*math.cos(a))
sat=elip(math.radians(-55))
prompt=[(9.7,10.3),(11.5,11.8),(9.7,13.3),(12.7,13.7),(14.7,13.7)]
seg=[(prompt[0],prompt[1]),(prompt[1],prompt[2]),(prompt[3],prompt[4])]
pts=[(a[0]+(b[0]-a[0])*k/20,a[1]+(b[1]-a[1])*k/20) for a,b in seg for k in range(21)]
dmin=min(math.dist(p,elip(t/400*2*math.pi)) for p in pts for t in range(400))
marg=min(min(elip(t/400*2*math.pi)[0],elip(t/400*2*math.pi)[1],24-elip(t/400*2*math.pi)[0],24-elip(t/400*2*math.pi)[1]) for t in range(400))-.75
print('B margen órbita',round(marg,2))
B=svg('apollo-b','B · prompt en órbita: el neón es el satélite',[
 f'<ellipse class="uva-apollo-b__orbita" cx="12" cy="12" rx="{rx}" ry="{ry}" transform="rotate({rot} 12 12)"/>',
 '<path class="uva-apollo-b__prompt" d="M9.7 10.3 11.5 11.8 9.7 13.3M12.7 13.7h2"/>',
 f'<circle class="uva-apollo-b__senal" cx="{sat[0]:.2f}" cy="{sat[1]:.2f}" r="1.6"/>'])
# C · trayectoria: plataforma + arco de ascenso; el neón es la cápsula en la punta
C=svg('apollo-c','C · trayectoria de lanzamiento: el neón es la cápsula',[
 '<path class="uva-apollo-c__trayectoria" d="M3.5 20.5h3.5C8.5 13 12 7.75 17.3 5.6"/>',
 '<circle class="uva-apollo-c__senal" cx="20.4" cy="3.8" r="1.3"/>'])
for v,s in zip('abc',[A,B,C]): open(f'apollo-{v}.svg','w').write(s)
print('B: distancia mínima prompt-órbita (ejes)',round(dmin,2),'→ hueco entre bordes',round(dmin-1.5,2))
print('A: cuerpo (borde 16.75) - ignición (borde', round(19.55-1.25,2),') =', round(19.55-1.25-16.75,2))
print('C: fin del arco - punto', round(math.dist((17.3,5.6),(20.4,3.8))-0.75-1.3,2))
