# Nexa Squad · ronda 1 · dos sistemas de símbolos en tinta. python3 gen.py -> simbolos.html
import os, math
D = os.path.dirname(os.path.abspath(__file__))
AG = [('squad','Nexa Squad','El squad'),('orka','Orka','Conductor'),('inqa','Inqa','Product Analyst'),('arko','Arko','Systems Architect'),
      ('fluxa','Fluxa','Flow Designer'),('kompa','Kompa','Layout Composer'),('kura','Kura','Component Curator'),('forja','Forja','Build Engineer'),('vera','Vera','QA Auditor')]

# A · Retícula: 3x3; contorno = lo que ya existe, lleno = lo que el agente decide
def cell(r, c, rs=1, cs=1, k='s'):
    x, y = 3 + c*15, 3 + r*15; w, h = cs*12 + (cs-1)*3, rs*12 + (rs-1)*3
    if k == 's': return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2.5" fill="currentColor"/>'
    return f'<rect x="{x+1.1}" y="{y+1.1}" width="{w-2.2}" height="{h-2.2}" rx="1.8" fill="none" stroke="currentColor" stroke-width="2.2"/>'
A = {
 'squad': [cell(0,0,1,2), cell(0,2,1,1,'o'), cell(1,0,1,1,'o'), cell(1,1,2,2), cell(2,0)],
 'orka':  [cell(r,c,1,1,'o') for r in range(3) for c in range(3) if (r,c)!=(1,1)] + [cell(1,1)],
 'inqa':  sum([[cell(r,0), cell(r,1,1,2,'o')] for r in range(3)], []),
 'arko':  [cell(0,c,1,1,'o') for c in range(3)] + [cell(1,0,1,3,'o'), cell(2,0,1,3)],
 'fluxa': [cell(0,0,1,1,'o'), cell(0,1,1,1,'o'), cell(1,1,1,1,'o'), cell(2,1,1,1,'o'), cell(2,2)],
 'kompa': [cell(0,0,1,3,'o'), cell(1,0,2,1,'o'), cell(1,1,2,2)],
 'kura':  [cell(0,c,1,1,'o') for c in range(3)] + [cell(1,0,2,3)],
 'forja': [cell(2,0), cell(1,0,1,1,'o'), cell(0,0,1,1,'o'), cell(1,1,2,1), cell(0,1,1,1,'o'), cell(0,2,3,1)],
 'vera':  [cell(1,0), cell(2,1), cell(1,2), cell(0,2)],
}
A_TXT = {
 'squad':'Un módulo completo: piezas de tamaños distintos que encajan sin huecos.',
 'orka':'Ocho piezas disponibles y una activa: quién trabaja ahora.',
 'inqa':'Una lista de criterios: cada requisito con su punto de comprobación.',
 'arko':'Lo que no se ve: la base llena sostiene las capas de arriba.',
 'fluxa':'Un recorrido de pantalla en pantalla que termina en el resultado.',
 'kompa':'Encabezado, lateral y contenido: el acomodo de una vista.',
 'kura':'Tres usos que se vuelven un componente (su regla de 3).',
 'forja':'Se construye fase por fase: cada columna sube un nivel.',
 'vera':'El visto bueno hecho de piezas: pasa o regresa.',
}
# B · Hilo: un trazo continuo con nodos (mismo grosor 3.5 que Fruti Squad)
S = 'fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"'
def n(x, y, r=4.6): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="currentColor"/>'
def p(d): return f'<path d="{d}" {S}/>'
B = {
 'squad': [p('M11 38 V10 L37 38 V10'), n(11,38), n(37,10)],
 'orka':  [p('M24 24 L24 9 M24 24 L11 33 M24 24 L37 33'), n(24,24,6), n(24,9,3.4), n(11,33,3.4), n(37,33,3.4)],
 'inqa':  [p('M9 24 H22 L28 31 L39 15'), n(9,24)],
 'arko':  [p('M9 39 H39 M13 39 V26 A11 11 0 0 1 35 26 V39'), n(24,15)],
 'fluxa': [p('M8 30 C14 14 20 14 24 24 S34 34 40 18'), n(8,30), n(24,24), n(40,18)],
 'kompa': [p('M24 13 L13 39 M24 13 L35 39 M17 30 A12 12 0 0 0 31 30'), n(24,11)],
 'kura':  [p('M9 10 C9 22 24 20 24 30 M24 10 V30 M39 10 C39 22 24 20 24 30 V39'), n(24,39)],
 'forja': [p('M8 39 H17 V30 H26 V21 H35 V12'), n(35,12)],
 'vera':  [p('M10 25 L20 35 L38 14'), n(20,35)],
}
B_TXT = {
 'squad':'Una N de un solo trazo: Nexa, el nexo que une a los ocho.',
 'orka':'Un centro que reparte el turno a tres direcciones.',
 'inqa':'Del requisito a su comprobación: una línea que termina en palomita.',
 'arko':'Un arco sobre su base: Arko, la estructura que sostiene.',
 'fluxa':'Un flujo con tres paradas: las vistas en orden.',
 'kompa':'Un compás: mide y acomoda cada sección.',
 'kura':'Tres caminos que se juntan en uno: reutilizar antes que crear.',
 'forja':'Escalones: se construye fase por fase hasta llegar.',
 'vera':'La palomita con el nodo en el vértice: el veredicto.',
}
def svg(parts, size, label):
    return f'<svg viewBox="0 0 48 48" width="{size}" height="{size}" role="img" aria-label="{label}">{"".join(parts)}</svg>'

def sistema(key, nombre, sub, M, T):
    filas = []
    for i, (id_, nom, rol) in enumerate(AG):
        lab = f'{nom}, {rol}'
        filas.append(f'''<article class="ag{' madre' if id_=='squad' else ''}">
<div class="lienzo claro">{svg(M[id_],96,lab)}</div><div class="lienzo oscuro">{svg(M[id_],96,lab)}</div>
<div class="chicos"><span>{svg(M[id_],32,lab)}</span><span>{svg(M[id_],16,lab)}</span><span class="osc">{svg(M[id_],16,lab)}</span></div>
<h3>{nom} <small>{rol}</small></h3><p>{T[id_]}</p></article>''')
    fila16 = ''.join(f'<span title="{nom}">{svg(M[i],16,nom)}</span>' for i, nom, _ in AG)
    fila24 = ''.join(f'<figure>{svg(M[i],28,nom)}<figcaption>{nom}</figcaption></figure>' for i, nom, _ in AG)
    return f'''<section class="sis" id="{key}"><header><p class="ojo">Sistema {key.upper()}</p><h2>{nombre}</h2><p>{sub}</p></header>
<div class="familia">{fila24}</div><div class="prueba"><b>Prueba a 16 px</b><div class="f16">{fila16}</div><div class="f16 osc">{fila16}</div></div>
<div class="rejilla">{''.join(filas)}</div></section>'''

HTML = f'''<title>Nexa Squad · Símbolos r1</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&display=swap">
<style>
/* Hoja de evaluación: dos sistemas completos lado a lado, cada símbolo en grande, en claro y oscuro, y a 32/16 px */
:root{{--bg:#f6f6f4;--fg:#17171c;--muted:#5b5b66;--line:#dcdcd6;--card:#fff;--ink:#17171c;--paper:#fff;--night:#111115;--nightfg:#f4f4f0;
--f:'Bricolage Grotesque',ui-sans-serif,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#141418;--fg:#eeeeea;--muted:#a3a3ad;--line:#2c2c33;--card:#1b1b20;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#141418;--fg:#eeeeea;--muted:#a3a3ad;--line:#2c2c33;--card:#1b1b20;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 64px}}
.w{{max-width:1180px;margin:0 auto;display:grid;gap:56px}}
h1{{font-size:clamp(30px,5vw,48px);line-height:1.05;margin:0;font-weight:700;text-wrap:balance}}
.intro{{display:grid;gap:12px;max-width:68ch}} .intro p{{margin:0;color:var(--muted)}}
.ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.sis{{display:grid;gap:24px}} .sis header{{display:grid;gap:6px;max-width:70ch}} .sis h2{{margin:0;font-size:30px;line-height:1.1}} .sis header p{{margin:0}}
.sis header p:last-child{{color:var(--muted)}}
.familia{{display:flex;flex-wrap:wrap;gap:20px 28px;padding:24px;background:var(--card);border:1px solid var(--line);border-radius:14px}}
.familia figure{{margin:0;display:grid;justify-items:center;gap:6px;color:var(--fg)}} .familia figcaption{{font-size:13px;color:var(--muted)}}
.prueba{{display:flex;flex-wrap:wrap;align-items:center;gap:12px 20px;font-size:14px}}
.f16{{display:flex;gap:14px;padding:10px 14px;border-radius:10px;background:var(--paper);color:var(--ink);border:1px solid var(--line)}}
.f16.osc,.osc{{background:var(--night);color:var(--nightfg)}}
.rejilla{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}}
.ag{{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:12px;background:var(--card);border:1px solid var(--line);border-radius:14px;align-content:start}}
.ag.madre{{border-color:var(--fg)}}
.lienzo{{display:grid;place-items:center;aspect-ratio:1;border-radius:10px;max-width:100%}}
.claro{{background:var(--paper);color:var(--ink);border:1px solid var(--line)}} .oscuro{{background:var(--night);color:var(--nightfg)}}
.chicos{{grid-column:1/-1;display:flex;gap:8px;align-items:center}}
.chicos span{{display:grid;place-items:center;width:44px;height:44px;border-radius:8px;background:var(--paper);color:var(--ink);border:1px solid var(--line)}}
.chicos span.osc{{border-color:transparent}}
.ag h3{{grid-column:1/-1;margin:4px 0 0;font-size:19px;line-height:1.2}} .ag h3 small{{font-weight:400;color:var(--muted);font-size:14px}}
.ag p{{grid-column:1/-1;margin:0;font-size:14px;color:var(--muted)}}
.cmp{{display:grid;gap:12px;max-width:72ch}} .cmp h2{{margin:0;font-size:26px}} .cmp ul{{margin:0;padding-left:20px;display:grid;gap:6px}}
</style>
<div class="w">
<div class="intro"><p class="ojo">Ronda 1 · en tinta, sin color ni tipografía final</p><h1>Nexa Squad: dos sistemas de símbolos</h1>
<p>Nexa compone módulos con los componentes que ya existen. Cada sistema dibuja al squad y a sus ocho agentes con una misma regla, para que se reconozcan como familia y se distingan entre sí a 16 px. El color y la tipografía van en la ronda siguiente, sobre el sistema que elijas.</p></div>
{sistema('a','A · Retícula','Todo vive en una rejilla de 3 × 3. Contorno = lo que ya existe; lleno = lo que decide el agente. Es la idea de Nexa (acomodar piezas) dibujada literalmente, y se separa de Fruti Squad, que es de trazo.',A,A_TXT)}
{sistema('b','B · Hilo','Un solo trazo continuo con nodos, del mismo grosor que los símbolos de Fruti Squad: se lee como marca hermana. Varios símbolos juegan con el nombre: Arko es un arco, Kompa un compás, Fluxa un flujo.',B,B_TXT)}
<section class="cmp"><h2>Cómo comparar</h2><ul>
<li><b>Prueba a 16 px:</b> ¿distingues a los nueve sin leer el nombre?</li>
<li><b>Relación con Fruti Squad:</b> A se separa (bloques llenos); B se emparienta (mismo trazo y nodos).</li>
<li><b>Riesgo de A:</b> Orka y Kompa usan muchos contornos; a 16 px pesan menos que el resto.</li>
<li><b>Riesgo de B:</b> Vera e Inqa comparten la palomita; si eliges B, Inqa cambiaría de rasgo. Kompa (compás) se puede leer como la letra A.</li></ul></section>
</div>'''
open(os.path.join(D, 'simbolos.html'), 'w').write(HTML)
print('ok')
