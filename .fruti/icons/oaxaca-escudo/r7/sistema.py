# Escudo de Oaxaca · r7 · lámina de sistema. Uso: python3 sistema.py [qa.json] → revision.html, svg/
import os, sys, json; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emblemas import *
D = os.path.dirname(os.path.abspath(__file__))
def em(k, cls='em'): return f'<svg class="{cls}" viewBox="{VB}" aria-hidden="true">{E[k]()}</svg>'
def mini(body, vb): return f'<svg class="ic" viewBox="{vb}" aria-hidden="true">{grupo(body)}</svg>'
PZ = {
 'aguila': (mini(aguila(0), '20 -4 200 124'), 'Águila', 'La cimera del escudo actual: soberanía.'),
 'mitla': (mini(f'<path d="{mitla(176)}"/>', '50 118 140 68'), 'Mitla', 'Plataforma escalonada: historia y patrimonio.'),
 'huaje': (mini(huaje(124), '56 50 128 128'), 'Huaje', 'Topónimo: el origen del nombre «Oaxaca».'),
 'cadena': (mini(cadena(30), '40 10 160 40'), 'Cadena rota', 'Libertad: el fin de la opresión.'),
 'puntos': (mini(''.join(f'<path d="{punto(64 + 16*k, 20)}"/>' for k in range(8)), '50 4 140 32'), 'Ocho puntos', 'Las ocho regiones, como las estrellas del escudo actual.'),
 'ovalo': (mini('<ellipse cx="120" cy="60" rx="40" ry="52"/><ellipse cx="120" cy="60" rx="20" ry="32"/>', '70 0 100 120'), 'Óvalo doble', 'El óvalo del lema de Juárez, ahora con las ocho regiones.'),
 'estrella': (mini(octagrama(120, 60, 50), '60 0 120 120'), 'Estrella de ocho puntas', 'Las ocho regiones alrededor de un centro común.'),
}
PROP = {
 'a': ('Escudo con cimera', 'La evolución más directa: águila de cimera, Mitla arriba, la cadena rota abajo y ocho puntos en la base, uno por región.', ['aguila', 'mitla', 'cadena', 'puntos']),
 'b': ('Óvalo', 'El óvalo del lema de Juárez se vuelve el escudo: doble anillo con ocho puntos y, al centro, el huaje que da nombre a Oaxaca sobre Mitla.', ['ovalo', 'huaje', 'mitla', 'puntos']),
 'c': ('Estrella de ocho regiones', 'Escudo en punta con una estrella de ocho puntas (dos cuadrados) y un centro común; abajo, la cadena rota.', ['estrella', 'cadena']),
}
def wm(cls=''): return f'<span class="wm {cls}"><b>OAXACA</b><i>GOBIERNO DEL ESTADO</i></span>'
def h(k, cls=''): return f'<div class="h {cls}">{em(k)}<span class="div"></span>{wm()}</div>'
def v(k): return f'<div class="v">{em(k)}{wm("c")}</div>'
cards = []
for k, (nom, desc, pzs) in PROP.items():
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
qa = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else None
qa_txt = ' '.join(f'{k.upper()}: simetría {v["sim"]}%{" (sin la cabeza del águila: " + str(v["simSinCabeza"]) + "%)" if "simSinCabeza" in v else ""}.' for k, v in qa.items()) + ' Un solo grosor de trazo en las tres.' if qa else 'Pendiente.'
html = open(os.path.join(D, 'plantilla.html')).read().replace('{{CARDS}}', ''.join(cards)).replace('{{QA}}', qa_txt)
html = html.replace('{{NEG}}', f'<div class="neg">{em("a", "em")}</div>').replace('{{ADM}}', f'<div class="adm">{h("a")}<span class="div"></span><span class="admt">Administración<br>2028 – 2034</span></div>')
open(os.path.join(D, 'revision.html'), 'w').write(html)
for k in E:
    for nom, fg in (('negro', '#111111'), ('blanco', '#FFFFFF')):
        open(os.path.join(D, 'svg', f'oaxaca-{k}-{nom}.svg'), 'w').write(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" color="{fg}" role="img" aria-label="Escudo de Oaxaca, propuesta {k.upper()}"><title>Escudo de Oaxaca, propuesta {k.upper()}</title>{E[k]()}</svg>')
# Regla 1 (estática): un único stroke-width y ningún relleno en los emblemas
for k in E:
    body = E[k](); sw = set(re.findall(r'stroke-width="([^"]+)"', body)); fills = re.findall(r'fill="(?!none)[^"]*"', body)
    assert sw == {str(W)} and not fills, (k, sw, fills)
print('ok · grosor único', W)
