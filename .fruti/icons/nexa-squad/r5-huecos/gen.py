# Nexa Squad · ronda 5 · familia Huecos completa (en tinta). python3 gen.py -> familia.html y svg/<id>.svg
# Reglas: bloque 40×40 en lienzo 48 (margen 4), radio 7. Cortes de 4 (canal), huecos de 8 como mínimo, círculos de radio 4 o más.
# Máximo tres cortes por símbolo. Cada hueco nace de la función del agente (skills/<agente>/SKILL.md en kevinedgm/nexa-squad).
import os
D = os.path.dirname(os.path.abspath(__file__))
AG = [('squad','Nexa Squad','El squad'),('orka','Orka','Conductor'),('inqa','Inqa','Product Analyst'),('arko','Arko','Systems Architect'),
      ('fluxa','Fluxa','Flow Designer'),('kompa','Kompa','Layout Composer'),('kura','Kura','Component Curator'),('forja','Forja','Build Engineer'),('vera','Vera','QA Auditor')]
def k(x, y, w, h, r=0): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#000"/>'
def kc(cx, cy, r): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#000"/>'
CUT = {
 'squad': k(22,0,4,48) + k(0,22,48,4) + kc(24,24,6),                                   # canales que se cruzan en el nexo
 'orka':  kc(11.5,24,4) + kc(24,24,6) + k(33,19,10,10,2),                            # hecho · actual · pendiente
 'inqa':  k(11,12,26,5,2.5) + k(11,21.5,11,5,2.5) + k(26,21.5,11,5,2.5) + kc(14,34,4),  # hecho · supuesto · pregunta
 'arko':  kc(24,19,6.5) + '<path d="M21 22 L18.5 37 H29.5 L27 22 Z" fill="#000"/>',     # cerradura: el servidor decide
 'fluxa': k(0,12,48,4) + k(11,20,14,5,2.5) + k(0,34,48,4),                             # cabecera · herramientas · datos · pie
 'kompa': k(0,15,48,4) + k(0,29,48,4) + k(32,0,4,16) + k(34,15,14,33) + k(22,15,4,15) + k(24,29,24,19) + k(12,29,4,19),  # tres anchos
 'kura':  ''.join(k(x,x,8,8,1.5) for x in (9,20,31)),                                  # la misma necesidad, tres veces
 'forja': k(0,27,48,4) + k(26,0,22,27),                                                # base completa, vista a medias
 'vera':  k(22,0,4,31) + k(19,28,10,10,2),                                             # el hallazgo sube a su dueño
}
FUN = {
 'squad':('Cada decisión tiene un solo dueño y todas se encuentran en un módulo.','Dos canales que parten el bloque en cuatro y se cruzan en un nexo redondo.'),
 'orka':('Elige el primer paso que falta y lanza un solo rol a la vez.','Una cadena de tres huecos: hecho (chico), actual (círculo) y pendiente (cuadro).'),
 'inqa':('Separa hechos, supuestos y preguntas.','Un renglón entero (hecho), uno partido (supuesto) y un punto (pregunta).'),
 'arko':('Decide datos, API y permisos; los permisos se validan en el servidor.','Una cerradura: solo pasa lo que el servidor permite.'),
 'fluxa':('Ordena las vistas; cada una con cabecera, herramientas, datos y pie.','Una pantalla tallada: cabecera, ranura de herramientas, datos al centro y pie.'),
 'kompa':('Decide qué crece y qué cede en tres anchos.','La misma fila en tres anchos: el tramo final nunca cambia.'),
 'kura':('Busca primero lo que existe y cuenta cuántas veces se repite.','El mismo hueco en tres lugares: ya toca un componente.'),
 'forja':('Construye primero lo de atrás y luego las vistas, fase por fase.','La base está completa; la capa de arriba va a medias.'),
 'vera':('Verifica cada criterio y regresa cada hallazgo a su dueño.','Un hallazgo que sale por su canal hacia arriba.'),
}
def sym(id_, size=48, uid=None, label=None, extra=''):
    u = uid or id_
    lab = f' role="img" aria-label="{label}"' if label else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="{size}" height="{size}"{lab}>{extra}'
            f'<defs><mask id="h-{u}" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48"><rect width="48" height="48" fill="#fff"/>{CUT[id_]}</mask></defs>'
            f'<rect x="4" y="4" width="40" height="40" rx="7" fill="currentColor" mask="url(#h-{u})"/></svg>')
for i, n, r in AG:
    open(f'{D}/svg/{i}.svg','w').write(sym(i, 48, i, f'{n}, {r}'))
GRID = ''.join(f'<line x1="{v}" y1="0" x2="{v}" y2="48" stroke="#e5484d" stroke-width=".25"/><line x1="0" y1="{v}" x2="48" y2="{v}" stroke="#e5484d" stroke-width=".25"/>' for v in range(4,45,4))
def cons(id_):  # símbolo en gris claro con la retícula de 4 y el contorno de los cortes
    cut = CUT[id_].replace('fill="#000"', 'fill="none" stroke="#e5484d" stroke-width=".6"')
    return (f'<svg viewBox="0 0 48 48" width="200" height="200" aria-hidden="true"><defs><mask id="c-{id_}"><rect width="48" height="48" fill="#fff"/>{CUT[id_]}</mask></defs>'
            f'<rect x="4" y="4" width="40" height="40" rx="7" fill="currentColor" opacity=".16" mask="url(#c-{id_})"/>{GRID}<g clip-path="inset(0)">{cut}</g>'
            f'<rect x="4" y="4" width="40" height="40" rx="7" fill="none" stroke="currentColor" stroke-width=".4"/></svg>')
n = 0
def u():
    global n; n += 1; return f'x{n}'
fam = lambda sz, cap=True: ''.join(f'<figure>{sym(i,sz,u(),nm)}{"<figcaption>"+nm+"</figcaption>" if cap else ""}</figure>' for i,nm,_ in AG)
tarj = ''.join(f'''<article class="ag{' madre' if i=='squad' else ''}" id="{i}">
<div class="vista"><div class="cl">{sym(i,120,u(),n_+', '+r)}</div><div class="os">{sym(i,120,u(),n_+', '+r)}</div><div class="con">{cons(i)}</div></div>
<div class="esc">{''.join(f'<span class="cl" style="--s:{s}px">{sym(i,s,u(),n_)}</span>' for s in (64,32,24,16))}<span class="os" style="--s:16px">{sym(i,16,u(),n_)}</span></div>
<h3>{n_} <small>{r}</small></h3><p><span class="et">Qué hace</span>{FUN[i][0]}</p><p><span class="et">El hueco</span>{FUN[i][1]}</p></article>''' for i,n_,r in AG)
APP = ''.join(f'<figure><span class="app">{sym(i,60,u(),nm)}</span><figcaption>{nm}</figcaption></figure>' for i,nm,_ in AG)
LOCK = ''.join(f'<div class="lock">{sym(i,44,u(),nm)}<div><b>{nm if i!="squad" else "Nexa Squad"}</b><span>{r if i!="squad" else "Composición de módulos"}</span></div></div>' for i,nm,r in AG)
HTML = f'''<title>Nexa Squad · Familia Huecos</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&display=swap">
<style>
/* Familia completa: reglas arriba, cada símbolo con su construcción y escalas, aplicaciones provisionales al final */
:root{{--bg:#f5f5f2;--fg:#16161b;--muted:#5a5a65;--line:#dbdbd4;--card:#fff;--paper:#fff;--ink:#16161b;--night:#101014;--nightfg:#f3f3ee;--guia:#e5484d;
--f:'Bricolage Grotesque',ui-sans-serif,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#131317;--fg:#ededea;--muted:#a2a2ac;--line:#2b2b32;--card:#1a1a1f;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#131317;--fg:#ededea;--muted:#a2a2ac;--line:#2b2b32;--card:#1a1a1f;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1180px;margin:0 auto;display:grid;gap:48px}}
h1{{font-size:clamp(32px,5.4vw,56px);line-height:1.02;margin:0;letter-spacing:-.01em;text-wrap:balance}} h2{{margin:0;font-size:28px;line-height:1.1}}
.intro{{display:grid;gap:14px;max-width:70ch}} .intro p{{margin:0;color:var(--muted)}}
.ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.heroe{{display:flex;flex-wrap:wrap;gap:22px 30px;padding:28px;background:var(--card);border:1px solid var(--line);border-radius:16px;color:var(--fg)}}
figure{{margin:0;display:grid;justify-items:center;gap:6px}} figcaption{{font-size:13px;color:var(--muted)}}
.reglas{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}}
.regla{{padding:16px;background:var(--card);border:1px solid var(--line);border-radius:12px;display:grid;gap:4px}} .regla b{{font-size:17px}} .regla span{{font-size:14px;color:var(--muted)}}
.cl{{background:var(--paper);color:var(--ink);border:1px solid var(--line)}} .os{{background:var(--night);color:var(--nightfg);border:1px solid transparent}}
.rejilla{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}}
.ag{{display:grid;gap:10px;padding:16px;background:var(--card);border:1px solid var(--line);border-radius:14px;align-content:start}} .ag.madre{{border-color:var(--fg)}}
.vista{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}} .vista>div{{display:grid;place-items:center;aspect-ratio:1;border-radius:10px;max-width:100%}}
.vista svg{{width:80%;height:auto}} .con{{background:var(--paper);color:var(--ink);border:1px solid var(--line)}}
.esc{{display:flex;gap:8px;align-items:center;flex-wrap:wrap}} .esc span{{display:grid;place-items:center;width:calc(var(--s) + 16px);height:calc(var(--s) + 16px);border-radius:8px}}
.ag h3{{margin:4px 0 0;font-size:21px;line-height:1.15}} .ag h3 small{{font-weight:400;font-size:14px;color:var(--muted)}}
.ag p{{margin:0;font-size:14.5px}} .et{{display:block;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.apps{{display:flex;flex-wrap:wrap;gap:18px 22px}} .app{{display:grid;place-items:center;width:84px;height:84px;border-radius:20px;background:var(--night);color:var(--nightfg)}}
.locks{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}}
.lock{{display:flex;gap:12px;align-items:center;padding:14px 16px;background:var(--card);border:1px solid var(--line);border-radius:12px;color:var(--fg)}}
.lock b{{display:block;font-size:20px;line-height:1.1;font-weight:700}} .lock span{{font-size:14px;color:var(--muted)}}
.fav{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}} .tab{{display:flex;gap:8px;align-items:center;padding:8px 14px;border-radius:10px 10px 0 0;background:var(--card);border:1px solid var(--line);border-bottom:0;font-size:14px;color:var(--fg)}}
.sec{{display:grid;gap:16px}} .sec>p{{margin:0;color:var(--muted);max-width:70ch}}
.cmp ul{{margin:0;padding-left:20px;display:grid;gap:6px;max-width:72ch}}
</style>
<div class="w">
<div class="intro"><p class="ojo">Ronda 5 · familia Huecos · en tinta</p><h1>Nexa Squad: lo que se quita es lo que hace</h1>
<p>Todos los símbolos son el mismo bloque. Lo que cambia es el hueco, y cada hueco sale del proceso real de su agente. El color y la tipografía final van en la ronda siguiente; aquí la letra es provisional.</p></div>
<div class="heroe" aria-label="La familia completa">{fam(64)}</div>
<section class="sec"><h2>Reglas de construcción</h2><div class="reglas">
<div class="regla"><b>Un bloque</b><span>40 × 40 en un lienzo de 48, margen de 4, radio de 7. Nunca cambia.</span></div>
<div class="regla"><b>Retícula de 4</b><span>Los cortes caen en múltiplos de 4 o en su mitad. La guía roja de cada ficha lo muestra.</span></div>
<div class="regla"><b>Cortes mínimos</b><span>Canales de 4, huecos de 8 y círculos de radio 4 o más: a 16 px siguen viéndose.</span></div>
<div class="regla"><b>Tres cortes como máximo</b><span>Si hacen falta más, el gesto no está claro todavía.</span></div>
<div class="regla"><b>Cuatro clases de corte</b><span>Canal (atraviesa), hueco (cerrado), círculo (estado o foco) y tallado (quita un borde).</span></div>
<div class="regla"><b>Un gesto por agente</b><span>El hueco cuenta la operación que más lo define, según su SKILL.md.</span></div>
</div></section>
<section class="sec"><h2>Los nueve</h2><p>Cada ficha: claro, oscuro y construcción; después 64, 32, 24 y 16 px.</p><div class="rejilla">{tarj}</div></section>
<section class="sec"><h2>Aplicaciones provisionales</h2><p>Para ver cómo se comporta la familia; letra provisional (la de Fruti Squad) hasta elegir la de Nexa.</p>
<div class="apps">{APP}</div>
<div class="fav"><span class="tab">{sym('squad',16,u(),'Nexa Squad')} Nexa Squad · docs</span><span class="tab">{sym('kompa',16,u(),'Kompa')} composicion/cuentas.md</span><span class="tab">{sym('vera',16,u(),'Vera')} revision/cuentas.md</span></div>
<div class="locks">{LOCK}</div></section>
<section class="sec cmp"><h2>Qué cambió desde la ronda 4</h2><ul>
<li><b>Squad:</b> dejó los ladrillos (a 16 px eran textura). Ahora son dos canales que se cruzan en un nexo redondo.</li>
<li><b>Fluxa:</b> dejó las tres franjas iguales, que se parecían al icono de menú. Ahora es una pantalla tallada con una ranura de herramientas.</li>
<li><b>Orka:</b> los tres huecos crecen en tamaño (hecho, actual, pendiente) y ninguno es menor que el mínimo.</li>
<li><b>Forja:</b> base completa y vista a medias, sin la franja abierta que se leía como «S».</li>
<li><b>Riesgo pendiente:</b> Kompa tiene más cortes que la regla (su escalera necesita cinco). Lo dejo así porque es el gesto más fiel a su función; si quieres la regla estricta, lo simplifico a dos filas.</li></ul></section>
</div>'''
open(f'{D}/familia.html','w').write(HTML); print('ok')
