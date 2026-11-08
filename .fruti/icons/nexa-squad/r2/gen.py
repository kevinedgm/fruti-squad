# Nexa Squad · ronda 2 · Retícula simplificada (máx. 4 piezas). python3 gen.py -> simbolos.html
import os, importlib.util
D = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r1', os.path.join(D, '../r1/gen.py'))
src = open(os.path.join(D, '../r1/gen.py')).read().split("open(os.path.join(D, 'simbolos.html')")[0]
ns = {'__file__': os.path.join(D, '../r1/gen.py')}; exec(src, ns)
AG, A1, svg = ns['AG'], ns['A'], ns['svg']
W = 40/3 - 2  # tercio con 3 px de separación
def s_(x, y, w, h): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="currentColor"/>'
def o_(x, y, w, h): return f'<rect x="{x+1.3}" y="{y+1.3}" width="{w-2.6}" height="{h-2.6}" rx="2" fill="none" stroke="currentColor" stroke-width="2.6"/>'
T3 = [4, 4+W+3, 4+2*(W+3)]
A2 = {
 'squad': [s_(4,4,18,40), s_(26,4,18,18), o_(26,26,18,18)],
 'orka':  [s_(17,4,14,14)] + [o_(x,30,W,14) for x in T3],
 'inqa':  [s_(4,7,12,12), o_(20,7,24,12), s_(4,29,12,12), o_(20,29,24,12)],
 'arko':  [o_(4,4,40,18), s_(4,26,40,18)],
 'fluxa': [o_(4,4,18,18), o_(26,4,18,18), s_(26,26,18,18)],
 'kompa': [o_(4,4,40,12), o_(4,20,12,24), s_(20,20,24,24)],
 'kura':  [o_(x,4,W,12) for x in T3] + [s_(4,22,40,22)],
 'forja': [s_(T3[0],30,W,14), s_(T3[1],18,W,26), s_(T3[2],4,W,40)],
 'vera':  [s_(4,T3[0],40,W), s_(4,T3[1],40,W), o_(4,T3[2],40,W)],
}
TXT = {
 'squad':'Tres piezas que encajan: un módulo completo.',
 'orka':'Uno dirige, tres trabajan.',
 'inqa':'Dos requisitos, cada uno con su punto de comprobación.',
 'arko':'La base llena sostiene la capa que se ve.',
 'fluxa':'Dos pantallas y el resultado al final del recorrido.',
 'kompa':'Encabezado, lateral y contenido.',
 'kura':'Tres usos que se vuelven un componente.',
 'forja':'Fase por fase, cada columna más alta.',
 'vera':'Dos pasan; la vacía regresa a su dueño.',
}
def cuenta(m): return len(m)
filas = ''.join(f'''<article class="ag{' madre' if i=='squad' else ''}">
<div class="lienzo claro">{svg(A2[i],96,f'{n}, {r}')}</div><div class="lienzo oscuro">{svg(A2[i],96,f'{n}, {r}')}</div>
<div class="chicos"><span>{svg(A2[i],32,n)}</span><span>{svg(A2[i],16,n)}</span><span class="osc">{svg(A2[i],16,n)}</span>
<span class="antes" title="Ronda 1">{svg(A1[i],32,n+' ronda 1')}</span></div>
<h3>{n} <small>{r}</small></h3><p>{TXT[i]} <span class="pz">{cuenta(A1[i])} → {cuenta(A2[i])} piezas</span></p></article>''' for i,n,r in AG)
fam = lambda M, sz: ''.join(f'<figure>{svg(M[i],sz,n)}<figcaption>{n}</figcaption></figure>' for i,n,_ in AG)
f16 = ''.join(f'<span>{svg(A2[i],16,n)}</span>' for i,n,_ in AG)
tot1, tot2 = sum(map(len, A1.values())), sum(map(len, A2.values()))
css = open(os.path.join(D,'../r1/simbolos.html')).read().split('<style>')[1].split('</style>')[0]
HTML = f'''<title>Nexa Squad · Símbolos r2</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&display=swap">
<style>{css}
.antes{{opacity:.45;margin-left:auto}} .pz{{display:block;margin-top:4px;font-size:13px;font-variant-numeric:tabular-nums}}
.dos{{display:grid;gap:12px}} .dos .familia{{align-items:end}} .et{{font-size:13px;color:var(--muted);margin:0}}
</style>
<div class="w">
<div class="intro"><p class="ojo">Ronda 2 · Retícula simplificada · en tinta</p><h1>Nexa Squad: menos piezas</h1>
<p>Misma regla que la A (contorno = lo que ya existe, lleno = lo que decide el agente), pero con la rejilla de 3 × 3 abierta: cada símbolo usa de 2 a 4 piezas más grandes en lugar de 4 a 9. En total pasan de {tot1} a {tot2} piezas.</p></div>
<section class="dos"><p class="et">Ronda 1</p><div class="familia">{fam(A1,28)}</div>
<p class="et">Ronda 2</p><div class="familia">{fam(A2,28)}</div>
<div class="prueba"><b>Prueba a 16 px</b><div class="f16">{f16}</div><div class="f16 osc">{f16}</div></div></section>
<div class="rejilla">{filas}</div>
<section class="cmp"><h2>Qué cambió</h2><ul>
<li><b>Orka:</b> ya no son ocho casillas con una llena; ahora uno arriba dirige a tres.</li>
<li><b>Vera:</b> deja la palomita; ahora es la revisión misma: tres filas, dos pasan y la vacía regresa.</li>
<li><b>Arko:</b> dos capas en lugar de cinco piezas.</li>
<li><b>Riesgo:</b> Arko y Kura comparten la base llena; se separan por la fila de arriba (una barra contra tres piezas). Forja se parece al icono de señal del celular. Orka es el más fino a 16 px.</li></ul></section>
</div>'''
open(os.path.join(D, 'simbolos.html'), 'w').write(HTML); print('ok', tot1, tot2)
