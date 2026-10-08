# Uva · iconos de dominio de PULZ (trazo 2, familia Lucide). Escribe <id>/variantes/<id>-<v>.svg
import os,math
R=os.path.dirname(os.path.abspath(__file__))
def svg(id,v,body,hyp):
    c=f'uva-{id}-{v}'
    s=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="uva-icon {c}" aria-hidden="true">\n'
       f'  <!-- {id} · {v}: {hyp} -->\n  <style>.{c}{{stroke-width:var(--uva-stroke,2)}}</style>\n{body}\n</svg>\n')
    d=os.path.join(R,id,'variantes'); os.makedirs(d,exist_ok=True); open(os.path.join(d,f'{id}-{v}.svg'),'w').write(s)
def lens(b,t,w):
    (bx,by),(tx,ty)=b,t; mx,my=(bx+tx)/2,(by+ty)/2; L=math.hypot(tx-bx,ty-by); px,py=-(ty-by)/L,(tx-bx)/L
    return f'M{bx:.2f} {by:.2f}Q{mx+px*2*w:.2f} {my+py*2*w:.2f} {tx:.2f} {ty:.2f}Q{mx-px*2*w:.2f} {my-py*2*w:.2f} {bx:.2f} {by:.2f}Z'
P=lambda d:f'  <path d="{d}"/>'
# ---------- agave ----------
G='M3 21H21'
svg('agave','a',P(G)+'\n'+P('M4.5 21L2.5 14L7.5 18L5.5 6L10 14.5L12 2.5L14 14.5L18.5 6L16.5 18L21.5 14L19.5 21'),
    'un solo contorno en zigzag: cinco pencas rectas y punzantes de alturas distintas, sin manchas en la base')
svg('agave','b',P(G)+'\n'+P('M10.5 21L12 4L13.5 21')+'\n'+P('M9.5 21L3 11L11 19')+'\n'+P('M14.5 21L21 11L13 19'),
    'tres pencas rectas muy abiertas: la roseta ancha y baja del espadín')
svg('agave','c',P(G)+'\n'+P('M5 21C4 19 3 17.5 2 16.5C4.5 16.5 6.5 17.5 8 18.5L5.5 6L10 14.5L12 2.5L14 14.5L18.5 6L16 18.5C17.5 17.5 19.5 16.5 22 16.5C21 17.5 20 19 19 21'),
    'como a, con las pencas bajas arqueadas hacia afuera: la roseta madura del espadín')
# ---------- horno cónico de tierra ----------
svg('earth-oven','a',P('M2 11.5H22')+'\n'+P('M4.5 11.5L9.5 21H14.5L19.5 11.5')+'\n'+P('M5.5 11.5C5.5 2.5 18.5 2.5 18.5 11.5')+'\n'+P('M12 19c-1.4-1-1.4-2.9 0-4c1.4 1.1 1.4 3 0 4z'),
    'corte a toda la altura: el cono bajo el suelo con el fuego al fondo y el montículo de piñas tapadas encima')
svg('earth-oven','b',P('M2 9H22')+'\n'+P('M5 9L11 21H13L19 9')+'\n'+P('M6.5 9C7 6 17 6 17.5 9')+'\n'+P('M12 19c-1.3-.9-1.3-2.6 0-3.6c1.3 1 1.3 2.7 0 3.6z'),
    'cono hondo y montículo bajo: lo «cónico» domina')
svg('earth-oven','c',P('M2 14H22')+'\n'+P('M5.5 14L10 21H14L18.5 14')+'\n'+P('M5 14C5 7 19 7 19 14')+'\n'+P('M9.5 5.5c-.8-1 .8-2 0-3')+'\n'+P('M14.5 5.5c-.8-1 .8-2 0-3'),
    'el montículo cociendo, con humo, sobre un cono más bajo: lo que se ve en el palenque')
# ---------- horno de mampostería ----------
svg('masonry-oven','a',P('M2 20H22')+'\n'+P('M4 20V14a8 8 0 0 1 16 0V20')+'\n'+P('M9 20v-3a3 3 0 0 1 6 0v3'),
    'bóveda de piedra sobre el suelo con boca en arco: la forma clásica de un horno')
svg('masonry-oven','b',P('M2 20H22')+'\n'+P('M4 20V9h16V20')+'\n'+P('M9 20v-3a3 3 0 0 1 6 0v3')+'\n'+P('M4 13.5H9')+'\n'+P('M15 13.5H20')+'\n'+P('M12 9V13.5')+'\n'+P('M16 9V5h2.5V9'),
    'cuarto de mampostería con juntas de piedra, boca y chimenea')
svg('masonry-oven','c',P('M2 20H22')+'\n'+P('M4 20V12a2 2 0 0 1 2-2H18a2 2 0 0 1 2 2V20')+'\n'+P('M9 20v-3a3 3 0 0 1 6 0v3')+'\n'+P('M9 7c-.8-1 .8-2 0-3')+'\n'+P('M12 7c-.8-1 .8-2 0-3')+'\n'+P('M15 7c-.8-1 .8-2 0-3'),
    'horno de obra sobre el suelo cociendo a vapor: el vapor lo separa de una casa')
# ---------- tahona ----------
svg('stone-mill','a',P('M2 21H22')+'\n'+P('M5 7V21')+'\n'+P('M5 15H9')+'\n'+P('M19 15H22')+'\n'+'  <circle cx="14" cy="15" r="5"/>\n  <circle cx="14" cy="15" r="2"/>',
    'de lado: la rueda de piedra en la fosa, unida por la vara al poste del centro')
svg('stone-mill','b',P('M2 21H22')+'\n'+P('M4 3V21')+'\n'+P('M4 13H22')+'\n'+'  <circle cx="14" cy="14" r="6"/>',
    'como a, con el poste alto y la vara saliendo de la rueda: la vara de la que tira el animal')
svg('stone-mill','c',P('M2 21H22')+'\n'+'  <circle cx="12" cy="13" r="6.5"/>\n  <circle cx="12" cy="13" r="1.5"/>\n'+P('M2 13H9')+'\n'+P('M15 13H22'),
    'la rueda grande sola con su eje: lo mínimo, la piedra que muele')
print('ok')
