# Escudo de Oaxaca · r6 · lámina de sistema por propuesta (en el formato de las láminas del usuario). Uso: python3 sistema.py
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emblemas import *
D = os.path.dirname(os.path.abspath(__file__))
VB = '-14 -22 228 262'
def em(k, cls='em'): return f'<svg class="{cls}" viewBox="{VB}" aria-hidden="true">{E[k]()}</svg>'
def mini(body, vb): return f'<svg class="ic" viewBox="{vb}" aria-hidden="true">{body}</svg>'
PZ = {
 'aguila': (mini(aguila(0, 0, 1), '-4 -2 70 66'), 'Águila', 'La cimera del escudo actual: soberanía.'),
 'mitla': (mini(mitla(30, 44, 56, 3), '0 0 60 48'), 'Mitla', 'Plataforma escalonada: historia y patrimonio.'),
 'huaje': (mini(huaje(0, 0, 1), '-26 0 52 56'), 'Huaje', 'Topónimo: el origen del nombre «Oaxaca».'),
 'cadena': (mini(cadena(0, 0, 1), '-62 -26 124 50'), 'Cadena rota', 'Libertad: el fin de la opresión.'),
 'estrella': (mini(estrella8(20, 20, 18, 8), '0 0 40 40'), 'Ocho puntas', 'Las ocho regiones en una estrella.'),
 'greca': (mini('<path d="M-17,5 V-5 H-7 V3 H1 V-5 H17 V5 H9 V-1" fill="none" stroke="currentColor" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>', '-21 -9 42 18'), 'Greca', 'Marco de ocho lados: una región por lado.'),
 'petalos': (mini(''.join(f'<circle cx="{20 + 13*math.cos(math.radians(45*k))}" cy="{20 + 13*math.sin(math.radians(45*k))}" r="5" fill="none" stroke="currentColor" stroke-width="2.4"/>' for k in range(8)), '0 0 40 40'), 'Ocho pétalos', 'Cada región con su pictograma, alrededor del centro.'),
 'estrellas': (mini(''.join(estrella8(8 + 12*k, 10, 5.5, 2.4) for k in range(3)), '0 0 40 20'), 'Ocho estrellas', 'En la bordura, como las estrellas del escudo actual, ahora ocho.'),
 'lienzo': (mini('<path d="M8,14 H48 M8,14 H2 a7,7 0 1 1 7,-7 M48,14 h6 a7,7 0 1 0 -7,-7" fill="none" stroke="currentColor" stroke-width="3.6" stroke-linecap="round"/>', '-8 -4 72 24'), 'Lienzo enrollado', 'La silueta del escudo actual: las luchas por la libertad.'),
}
PROP = {
 'a': ('Escudo de las ocho regiones', 'La evolución más directa del escudo actual: la misma estructura (cimera, lienzo, cuarteles) dibujada en trazo grueso y parejo, con una bordura de ocho estrellas.', ['aguila', 'lienzo', 'mitla', 'huaje', 'cadena', 'estrellas']),
 'b': ('Greca', 'El escudo dentro de un marco octagonal de grecas: cada lado es una región y el marco las une. Al centro, Mitla, la estrella de ocho puntas y la cadena rota.', ['aguila', 'greca', 'mitla', 'estrella', 'cadena']),
 'c': ('Ocho pétalos', 'Ocho regiones alrededor de un centro común, cada una con su pictograma. Al centro, el escudo con el águila sobre Mitla.', ['aguila', 'mitla', 'petalos']),
}
def wm(cls=''): return f'<span class="wm {cls}"><b>OAXACA</b><i>GOBIERNO DEL ESTADO</i></span>'
def h(k, cls=''): return f'<div class="h {cls}">{em(k)}<span class="div"></span>{wm()}</div>'
def v(k): return f'<div class="v">{em(k)}{wm("c")}</div>'
cards = []
for i, (k, (nom, desc, pzs)) in enumerate(PROP.items()):
    reco = ' reco' if k == 'a' else ''
    ley = ''.join(f'<li>{PZ[p][0]}<div><b>{PZ[p][1]}</b><span>{PZ[p][2]}</span></div></li>' for p in pzs)
    cards.append(f'''<article class="prop{reco}"><div class="tit"><span class="tag">Propuesta {k.upper()}</span>{'<span class="chip">Recomendada</span>' if reco else ''}</div>
<h2>{nom}</h2><p class="desc">{desc}</p>
<div class="hero"><div class="principal">{v(k)}</div><div><h3>Elementos clave</h3><ul class="ley">{ley}</ul></div></div>
<h3>Versiones del logotipo</h3>
<div class="fila vers"><figure>{v(k)}<figcaption>Vertical<br><small>uso preferente</small></figcaption></figure><figure>{h(k)}<figcaption>Horizontal<br><small>uso general</small></figcaption></figure><figure>{em(k, 'em iso')}<figcaption>Isotipo<br><small>institucional</small></figcaption></figure></div>
<h3>Escalas y uso mínimo</h3>
<div class="fila esc"><figure>{h(k, 'g')}<figcaption>Grande<br><small>señalética, fachadas</small></figcaption></figure><figure>{h(k, 'm')}<figcaption>Mediana<br><small>documentos, medios</small></figcaption></figure><figure>{em(k, 'em min')}<figcaption>Mínima<br><small>12 mm / 48 px</small></figcaption></figure></div>
<h3>Área de protección</h3>
<div class="prot"><span class="x tl">x</span><span class="x tr">x</span><span class="x bl">x</span><span class="x br">x</span>{h(k)}</div>
</article>''')
html = open(os.path.join(D, 'plantilla.html')).read().replace('{{CARDS}}', ''.join(cards))
html = html.replace('{{NEG}}', f'<div class="neg">{em("a", "em")}</div>').replace('{{ADM}}', f'<div class="adm">{h("a")}<span class="div"></span><span class="admt">Administración<br>2028 – 2034</span></div>')
open(os.path.join(D, 'revision.html'), 'w').write(html)
for k in E:
    for nom, fg, bg in (('negro', '#111111', '#FFFFFF'), ('blanco', '#FFFFFF', '#111111')):
        open(os.path.join(D, 'svg', f'oaxaca-{k}-{nom}.svg'), 'w').write(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" color="{fg}" role="img" aria-label="Escudo de Oaxaca, propuesta {k.upper()}"><title>Escudo de Oaxaca, propuesta {k.upper()}</title><style>.cut{{fill:{bg}}}.cuts{{stroke:{bg}}}</style>{E[k]()}</svg>')
print('ok')
