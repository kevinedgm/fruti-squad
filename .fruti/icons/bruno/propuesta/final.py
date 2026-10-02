import perro
C = True
def cuerpo(boca):
    nariz, labio, comisura, menton, mandibula = boca
    return [(5.4,10.8),(9.0,10.9),(12.4,10.4),(13.4,8.8),(13.8,6.9),(13.7,4.7),(14.8,3.1),(16.4,3.4),(17.2,4.7,C),(17.5,5.5),(18.5,6.0),(20.0,6.9),
            (*nariz, C), labio, (*comisura, C), menton, mandibula,(16.0,10.6),(16.0,12.6),(15.6,14.4),(15.8,20.4,C),(13.6,20.4,C),(13.4,15.6),(11.8,15.0),(9.3,14.8),(8.6,15.7),
            (8.6,20.4,C),(6.4,20.4,C),(6.0,17.6),(4.4,14.8),(4.3,12.2)]
CERRADA = [(20.4,7.8),(19.8,8.5),(18.5,8.9),(19.2,9.2),(17.3,9.6)]
ABIERTA = [(20.5,7.4),(19.7,8.1),(18.2,8.7),(19.6,10.3),(17.5,10.5)]
cola = [(5.1,10.9),(3.6,10.3),(2.9,9.0),(2.9,7.3)]
linea = [(8.6,15.7),(8.2,13.8),(7.0,12.9)]
dC = perro.camino(cuerpo(CERRADA)); dA = perro.camino(cuerpo(ABIERTA))
assert dC.count('C') == dA.count('C')
R = 'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"'
k = lambda d: f'd:path("{d}")'
css = f'''
    .uva-bruno{{stroke-width:var(--uva-stroke,1.5);overflow:visible;transform-origin:50% 85%}}
    .uva-bruno__ojo{{fill:currentColor;stroke:none}}
    /* Dos movimientos, cada uno con su significado y su modificador (el componente lo añade y lo quita en animationend):
       uva-bruno (modificador contento) · feedback, «Bruno respondió»: mueve la cola dos veces (640 ms).
       uva-bruno (modificador avisar) · attention, «Bruno tiene un aviso»: ladra dos veces, la mandíbula se abre y se cierra (600 ms). Con moderación. */
    .uva-bruno--contento{{--uva-bruno-cola:uva-bruno-menear}}
    .uva-bruno--avisar{{--uva-bruno-cuerpo:uva-bruno-ladrar}}
    .uva-bruno__cola{{transform-box:view-box;transform-origin:5.1px 10.9px;animation:var(--uva-bruno-cola,none) 640ms cubic-bezier(.4,0,.6,1) 0s 1}}
    .uva-bruno__cuerpo{{animation:var(--uva-bruno-cuerpo,none) 300ms cubic-bezier(.3,0,.4,1) 0s 2}}
    @keyframes uva-bruno-menear{{0%{{transform:rotate(0)}}15%{{transform:rotate(32deg)}}35%{{transform:rotate(-15deg)}}55%{{transform:rotate(32deg)}}75%{{transform:rotate(-15deg)}}100%{{transform:rotate(0)}}}}
    @keyframes uva-bruno-ladrar{{0%{{{k(dC)}}}35%{{{k(dA)}}}100%{{{k(dC)}}}}}
    /* Navegadores que no animan la forma (propiedad d): el ladrido se reduce a un leve impulso del icono entero */
    @supports not (d: path("M0 0")) {{
      .uva-bruno--avisar{{animation:uva-bruno-impulso 300ms cubic-bezier(.3,0,.4,1) 0s 2}}
    }}
    @keyframes uva-bruno-impulso{{0%{{transform:none}}35%{{transform:translateY(-4%) rotate(-3deg)}}100%{{transform:none}}}}
    @media (prefers-reduced-motion:reduce){{
      .uva-bruno--contento{{--uva-bruno-cola:none}}
      .uva-bruno--avisar{{--uva-bruno-cuerpo:none;animation:none}}
    }}
  '''
svg = (f'<svg {R} class="uva-icon uva-bruno" aria-hidden="true">\n  <style>{css}</style>\n'
       '  <!-- bruno · perro de perfil · cola (modificador contento) y ladrido (modificador avisar) -->\n'
       f'  <path class="uva-bruno__cuerpo" d="{dC}"/>\n  <path class="uva-bruno__cola" d="{perro.camino(cola, False)}"/>\n'
       f'  <path class="uva-bruno__linea" d="{perro.camino(linea, False)}"/>\n  <circle class="uva-bruno__ojo" cx="17.2" cy="7.4" r="0.75"/>\n</svg>\n')
open('bruno.svg', 'w').write(svg)
open('bruno-abierta.svg', 'w').write(svg.replace(f'class="uva-bruno__cuerpo" d="{dC}"', f'class="uva-bruno__cuerpo" d="{dA}"'))
print('margen cerrada', perro.margen(cuerpo(CERRADA) + cola), 'abierta', perro.margen(cuerpo(ABIERTA)))
