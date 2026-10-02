import perro, r3
dC = perro.camino(r3.cuerpo_a(r3.CERR)); dA = perro.camino(r3.cuerpo_a(r3.ABIE)); assert dC.count('C') == dA.count('C')
src = open('final.py').read()
# reutiliza la plantilla de estilos/animación de la ronda anterior con la geometría nueva
ns = {}
exec(src.split("svg = (")[0].replace("dC = perro.camino(cuerpo(CERRADA)); dA = perro.camino(cuerpo(ABIERTA))", "").replace("assert dC.count('C') == dA.count('C')", ""), {**ns, 'perro': perro, 'dC': dC, 'dA': dA}, ns)
css = ns['css'].replace('transform-origin:5.1px 10.9px', 'transform-origin:5.0px 11.2px')
R = ns['R']
svg = (f'<svg {R} class="uva-icon uva-bruno" aria-hidden="true">\n  <style>{css}</style>\n'
       '  <!-- bruno · perro de perfil, familia de rabbit y turtle · cola (modificador contento) y ladrido (modificador avisar) -->\n'
       f'  <path class="uva-bruno__cuerpo" d="{dC}"/>\n  <path class="uva-bruno__cola" d="{perro.camino(r3.colaA, False)}"/>\n'
       f'  <path class="uva-bruno__oreja" d="{perro.camino(r3.orejaA, False)}"/>\n  <circle class="uva-bruno__ojo" cx="18.6" cy="7.2" r="0.75"/>\n</svg>\n')
open('bruno3.svg', 'w').write(svg)
open('bruno3-abierta.svg', 'w').write(svg.replace(f'class="uva-bruno__cuerpo" d="{dC}"', f'class="uva-bruno__cuerpo" d="{dA}"'))
