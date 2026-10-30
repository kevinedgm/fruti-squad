# Manual de marca Fruti Squad v0.1 (fase 1: secciones 1-4). Identidad visual: ../final (decisión B).
# Estrategia y voz: brief estratégico del usuario (2026-10-30). Uso: python3 gen.py
import base64, json, os, html, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'guia'))
from textos import T
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'final')
tema = json.load(open(os.path.join(F, 'tema.json')))
def uri(i, n):
    return 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(F, i, 'svg', n + '.svg'), 'rb').read()).decode()
def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + .05) / (lb + .05)
e = html.escape
PAPER, WHITE, DARK, INK = '#f5f5f2', '#ffffff', '#0f0f12', '#18181b'
IDS = ['kiwi', 'lima', 'coco', 'bruno', 'mora']
VERBO = {'kiwi': ('Organizar', 'Organize'), 'lima': ('Validar', 'Validate'), 'coco': ('Inspeccionar', 'Inspect'),
         'bruno': ('Conectar', 'Connect'), 'mora': ('Catalogar', 'Catalog')}
RESP = {'kiwi': 'Arquitectura UX', 'lima': 'Gobernanza del design system', 'coco': 'Construcción visual y auditoría',
        'bruno': 'Implementación funcional', 'mora': 'Documentación verificada'}
SIMB = {'kiwi': ('Tres tamaños', 'Tres marcos anidados: compact, medium y expanded. La misma pantalla resuelta en cada tamaño.'),
        'lima': ('Biblioteca', 'Marcos apilados: una sola fuente de la que salen muchas piezas coherentes.'),
        'coco': ('Visor', 'Esquinas que encuadran la pieza: mirar contra el contrato antes de dar un PASS.'),
        'bruno': ('Cierre', 'Diagonal de código que convierte el plano punteado en pieza sólida.'),
        'mora': ('Red de conocimiento', 'Nodos enlazados dentro del marco: lo que existe, conectado y catalogado.')}
NO = {'kiwi': 'No entrega la capa visual final: su salida son estructura y estados.',
      'lima': 'No dibuja pantallas ni reabre una estructura congelada.',
      'coco': 'No rediseña la estructura aprobada; si falla, la devuelve con evidencia.',
      'bruno': 'No reinterpreta la estructura, el contrato ni el CSS aprobados.',
      'mora': 'No documenta lo que no existe ni repite la auditoría.'}

def sec(n, id_, t, en, body):
    return f'<section id="{id_}" class="sec"><header class="sh"><span class="num">{n:02d}</span><div><h2>{t}</h2><p class="en">{en}</p></div></header>{body}</section>'

# 1 · Brand Strategy
principios = [('Especialización', 'Specialization', 'Cada agente tiene una responsabilidad definida.'),
              ('Colaboración', 'Collaboration', 'El resultado depende de la continuidad entre especialistas.'),
              ('Trazabilidad', 'Traceability', 'Las decisiones importantes deben poder justificarse.'),
              ('Consistencia', 'Consistency', 'Los resultados respetan contratos y decisiones anteriores.'),
              ('Verificación', 'Verification', 'Ninguna afirmación de calidad sustituye a la evidencia.'),
              ('Control humano', 'Human control', 'Las decisiones que requieren aprobación quedan en manos del usuario.')]
atributos = [('Inteligente', 'sin ser pretenciosa'), ('Moderna', 'sin depender de modas visuales'), ('Cercana', 'sin resultar infantil'),
             ('Técnica', 'sin ser innecesariamente compleja'), ('Creativa', 'sin sacrificar consistencia'), ('Confiable', 'sin prometer resultados imposibles')]
s1 = f'''<div class="hero-q"><p class="big">Five specialists. One coordinated workflow.</p><p class="sub">Cinco especialistas. Un proceso coordinado.</p></div>
<div class="g3">
<div class="card"><h3>Propósito</h3><p>Hacer que el desarrollo de software asistido por IA sea más estructurado, consistente, verificable y fácil de mantener.</p></div>
<div class="card"><h3>Misión</h3><p>Proporcionar agentes especializados, protocolos y flujos coordinados para diseñar, desarrollar, verificar y documentar interfaces con responsabilidades claras.</p></div>
<div class="card"><h3>Visión</h3><p>Ser referencia para equipos y desarrolladores que usan agentes de IA dentro de procesos de ingeniería disciplinados, reutilizables y auditables.</p></div></div>
<h3 class="h3">Principios</h3><div class="g3">{''.join(f'<div class="pr"><b>{a}</b><span class="en">{b}</span><p>{c}</p></div>' for a,b,c in principios)}</div>
<h3 class="h3">Posicionamiento</h3>
<div class="card"><p class="cat">Coordinated AI Agent Workflow for UX, Design Systems and Frontend Engineering.</p>
<p>Fruti Squad es un sistema de trabajo multiagente para desarrolladores y equipos de producto que necesitan construir interfaces con IA sin perder consistencia, trazabilidad ni control. A diferencia de una colección de prompts sueltos, define especialistas, responsabilidades, contratos, traspasos y puntos de validación que conectan las etapas.</p>
<p class="prom"><span>Promesa</span> From requirements to verified implementation, through a coordinated team of AI specialists.</p></div>
<h3 class="h3">Público</h3><div class="tbl"><table><thead><tr><th>Segmento</th><th>Quiénes</th><th>Necesidad</th></tr></thead><tbody>
<tr><td>Principal</td><td>Desarrolladores frontend, full-stack e independientes que programan con asistentes de IA</td><td>Resultados consistentes sin reconstruir el contexto en cada tarea</td></tr>
<tr><td>Secundario</td><td>Equipos de producto pequeños, agencias, responsables de design systems</td><td>Estandarizar decisiones para que personas y agentes trabajen sobre la misma arquitectura</td></tr>
<tr><td>Especializado</td><td>Arquitectos frontend, diseñadores de producto, ingenieros UX, creadores de herramientas</td><td>Procedimientos reutilizables de gobernanza, verificación y documentación</td></tr>
<tr class="no"><td>No prioritario</td><td>Quien solo quiere generar una pantalla</td><td>No es a quien hablamos primero; la marca es accesible, pero no es un generador instantáneo</td></tr>
</tbody></table></div>
<h3 class="h3">Personalidad</h3><div class="attrs">{''.join(f'<span><b>{a}</b> {b}</span>' for a,b in atributos)}</div>
<div class="avoid"><b>Evitar</b><ul><li>Robots, cerebros digitales e ilustración futurista sin relación con el producto.</li><li>Presentar a los agentes como seres autónomos que garantizan resultados perfectos.</li><li>Lenguaje corporativo o mensajes que son solo una cadena de términos técnicos.</li></ul></div>'''

# 2 · Visual Identity
def sw(nombre, hexv, fondo):
    return f'<div class="sw"><i style="background:{hexv}"></i><span><b>{nombre}</b><code>{hexv}</code><small>{cr(hexv, fondo):.1f}:1 sobre {fondo}</small></span></div>'
filas = ''
for i in IDS:
    p = tema['productos'][i]; v, c = p['color_oscuro'], p['color_claro']
    a, b, w = cr(v, DARK), cr(c, PAPER), cr(c, WHITE)
    ok = lambda x: f'<td class="{"ok" if x >= 3 else "bad"}">{x:.2f}</td>'
    filas += f'<tr><td><b>{p["nombre"]}</b></td><td><i class="dot" style="background:{v}"></i>{v}</td>{ok(a)}<td><i class="dot" style="background:{c}"></i>{c}</td>{ok(w)}{ok(b)}</tr>'
cambios = [('Isotipo', 'Cinco módulos alrededor de un núcleo', 'Espiral: cinco marcos que giran sobre un punto en degradado', 'El usuario rehízo la familia desde cero; la espiral conserva la idea de «cinco alrededor de un centro» del isotipo anterior'),
           ('Especialistas', 'Personajes', 'Símbolos abstractos, uno por función', 'Reconocibles a 16 px y sin desplazar al producto (criterio 15 del brief)'),
           ('Paleta base', '#161616 · #F8F8F5 · acento #B7F34D', 'Tinta #18181b · oscuro #0f0f12 · papel #f5f5f2; sin acento único', 'El color lo aportan los cinco puntos; el acento #B7F34D mide 1.2:1 sobre la superficie clara'),
           ('Color de agentes', '#7FCF5B #C9F36B #C89A68 #E5A447 #8468E8', 'Duotono: vivo en oscuro, claro en fondo claro', 'Los del brief bajan de 3:1 sobre claro y Kiwi y Bruno se confunden con deuteranopía (ΔE 2.3)'),
           ('Tipografía', 'Sora', 'Bricolage Grotesque', 'Elegida en la ronda 20; ejes de tamaño óptico para titular y texto')]
s2 = f'''<p class="lead">Un sistema, dos piezas: un <b>marco redondeado</b> en trazo neutro y un <b>punto</b>, la evidencia que cada agente produce y entrega. El marco es de la marca; el punto lleva el color de quien firma.</p>
<div class="anat"><img src="{uri('squad','simbolo')}" alt="Símbolo de Fruti Squad"><ol><li><b>Marco</b> trazo 3.5 en una caja de 64, esquinas redondeadas, siempre tinta o blanco.</li><li><b>Silueta</b> lo que cambia entre integrantes: así se distinguen sin color.</li><li><b>Punto</b> único elemento con color. En el orquestador reúne los cinco en degradado.</li></ol></div>
<h3 class="h3">Logotipo principal</h3>
<div class="g2"><div class="lk"><img src="{uri('squad','lockup')}" alt="Fruti Squad Workflow Pack"></div><div class="lk dk"><img src="{uri('squad','lockup-oscuro')}" alt="Fruti Squad Workflow Pack, versión oscura"></div></div>
<div class="g3 small"><div class="card"><h4>Área de seguridad</h4><p>Alrededor del símbolo, ¼ de su alto (16 de 64 unidades). Nada entra en esa zona.</p></div>
<div class="card"><h4>Tamaño mínimo</h4><p>Símbolo 16 px (existe un favicon dibujado para ese tamaño). Logotipo con descriptor: 32 px de alto.</p></div>
<div class="card"><h4>Una tinta</h4><p><code>simbolo-tinta.svg</code> usa currentColor: para grabado, sellos, monocromo y fondos de color.</p></div></div>
<div class="row ink"><img src="{uri('squad','simbolo-tinta')}" alt="" class="t"><img src="{uri('squad','app-icon')}" alt="App icon Fruti Squad" class="a"><img src="{uri('squad','favicon')}" alt="Favicon" class="f"><span class="cap">una tinta · app icon · favicon</span></div>
<h3 class="h3">Color</h3>
<div class="pal">{sw('Tinta', INK, PAPER)}{sw('Oscuro', DARK, PAPER)}{sw('Papel', PAPER, INK)}{sw('Texto secundario claro', '#52525b', PAPER)}{sw('Texto secundario oscuro', '#b9b9b4', DARK)}</div>
<div class="tbl"><table><caption>Contraste del punto como elemento gráfico (mínimo WCAG 1.4.11: 3:1). Calculado al generar esta página.</caption>
<thead><tr><th>Integrante</th><th>Vivo</th><th>sobre #0f0f12</th><th>Claro</th><th>sobre blanco</th><th>sobre #f5f5f2</th></tr></thead><tbody>{filas}</tbody></table></div>
<p class="note">El color de integrante es señal gráfica, no color de texto. Para texto se usa tinta o blanco; el color nunca es la única forma de identificar a un agente: la silueta y el nombre siempre lo acompañan.</p>
<h3 class="h3">Tipografía · Bricolage Grotesque</h3>
<div class="type"><div><span class="lbl">Display · 700 · 48/1.05</span><p style="font:700 48px/1.05 var(--f);letter-spacing:-.02em;margin:0">Structure first.</p></div>
<div><span class="lbl">Titular · 700 · 30/1.15</span><p style="font:700 30px/1.15 var(--f);margin:0">Five specialists, one workflow</p></div>
<div><span class="lbl">Subtítulo · 600 · 20/1.3</span><p style="font:600 20px/1.3 var(--f);margin:0">Kiwi defines the structure before appearance</p></div>
<div><span class="lbl">Cuerpo · 400 · 16/1.55</span><p style="font:400 16px/1.55 var(--f);margin:0;max-width:62ch">Each agent does one kind of work and hands verified evidence to the next, so decisions are not reinterpreted along the way.</p></div>
<div><span class="lbl">Etiqueta · 600 · 12/1.2 · versalitas +0.06em</span><p style="font:600 12px/1.2 var(--f);letter-spacing:.06em;text-transform:uppercase;margin:0">UX Architect · Handoff</p></div>
<div><span class="lbl">Código · monoespaciada del sistema · 14/1.5</span><p style="font:400 14px/1.5 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;margin:0">npx fruti install --target claude</p></div></div>
<p class="note">Alternativa si Bricolage no está disponible: <code>system-ui, -apple-system, "Segoe UI", Roboto, sans-serif</code>. En logotipos nunca se sustituye: los SVG llevan la letra convertida a trazos. La monoespaciada de marca está <b>sin decidir</b>; mientras tanto se usa la del sistema.</p>
<h3 class="h3">Cambios respecto a la identidad anterior</h3><p class="note">El brief pide documentar cualquier cambio. Decisión del usuario: manda la identidad nueva.</p>
<div class="tbl"><table><thead><tr><th>Elemento</th><th>Antes (brief)</th><th>Ahora</th><th>Por qué</th></tr></thead><tbody>{''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in cambios)}</tbody></table></div>'''

# 3 · Agent Identity System
cards = ''
for i in IDS:
    p = tema['productos'][i]
    cards += f'''<article class="ag"><div class="agh"><img src="{uri(i,'simbolo')}" alt="Símbolo de {p['nombre']}" class="s"><div><h3>{p['nombre']}</h3><p class="desc">{e(p['producto'])}</p></div></div>
<dl><dt>Responsabilidad</dt><dd>{RESP[i]}</dd><dt>Verbo de marca</dt><dd>{VERBO[i][0]} <span class="en">· {VERBO[i][1]}</span></dd>
<dt>Símbolo</dt><dd><b>{SIMB[i][0]}.</b> {SIMB[i][1]}</dd><dt>Hace</dt><dd>{e(T[i]['es'][1])}</dd><dt>Límite</dt><dd>{NO[i]}</dd>
<dt>Color</dt><dd><i class="dot" style="background:{p['color_claro']}"></i>{p['color_claro']} claro · <i class="dot" style="background:{p['color_oscuro']}"></i>{p['color_oscuro']} vivo</dd></dl></article>'''
s3 = f'''<p class="lead">Cinco especialistas, una sola marca. Se distinguen por <b>nombre, silueta, color del punto y función</b>; comparten marco, trazo, letra y voz.</p>
<div class="flowh"><img src="{uri('squad','simbolo')}" alt=""><b>Fruti Squad</b><span>coordina</span></div><div class="flow" role="img" aria-label="Flujo: Kiwi estructura, Lima gobierna, Coco construye y audita, Bruno implementa, Mora documenta; Fruti Squad coordina">{''.join(f'<div class="fs"><img src="{uri(i,"simbolo")}" alt=""><b>{tema["productos"][i]["nombre"]}</b><span>{VERBO[i][0]}</span></div>' for i in IDS)}</div>
<p class="note">El orquestador (Fruti Squad) no es un sexto especialista: no aparece dentro de la fila, la enmarca y la coordina.</p>
<div class="ags">{cards}</div>
<h3 class="h3">Reglas</h3><ol class="rules"><li>Un especialista nunca aparece sin su nombre la primera vez que se menciona.</li><li>En una misma pieza, el color de un integrante solo marca lo que ese integrante produjo.</li><li>Los símbolos no se combinan entre sí ni se reacomodan en un logo nuevo; para el conjunto se usa el de Fruti Squad.</li><li>Los personajes del brief se sustituyen por símbolos; la personalidad la llevan el verbo y la voz, no una cara.</li><li>Ningún especialista se presenta como autónomo: cada uno entrega evidencia y la aprobación queda en el usuario.</li></ol>'''

# 4 · Verbal Identity
msgs = [('Especialización', 'Each agent owns a clearly defined responsibility.', 'Cada agente es dueño de una responsabilidad definida.'),
        ('Coordinación', 'Decisions and deliverables move through a shared workflow.', 'Decisiones y entregables avanzan por un flujo compartido.'),
        ('Control', 'Important approvals remain with the developer.', 'Las aprobaciones importantes quedan en manos de quien desarrolla.'),
        ('Calidad', 'Outputs can be inspected against explicit requirements and evidence.', 'Los resultados se revisan contra requisitos explícitos y evidencia.'),
        ('Continuidad', 'Implementation and documentation inherit the decisions made in earlier stages.', 'Implementación y documentación heredan las decisiones previas.')]
claims = [('We help you keep UX, contracts, code and docs consistent.', 'Garantizamos accesibilidad total.'),
          ('Each stage hands evidence to the next.', 'Cero errores. Funciona en cualquier stack.'),
          ('Approvals stay with you.', 'Agentes autónomos que construyen tu app solos.'),
          ('Works with Codex, Kiro and Claude Code (verified editions).', '10× más rápido (sin una prueba publicada que lo respalde).')]
s4 = f'''<p class="lead">Voz profesional, directa y centrada en resultados. Inglés como idioma comercial principal, español como secundario; las dos versiones dicen lo mismo, no se traducen palabra por palabra.</p>
<div class="g2"><div class="card big2"><span class="lbl">Tagline</span><p class="t1">Five specialists. One coordinated workflow.</p><p class="t2">Cinco especialistas. Un proceso coordinado.</p></div>
<div class="card big2"><span class="lbl">Mensaje de producto</span><p class="t1">Build with structure. Ship with confidence.</p><p class="t2">Construye con estructura. Publica con confianza.</p></div></div>
<div class="card"><span class="lbl">Descripción breve</span><p>Fruti Squad is a coordinated multi-agent workflow that brings structure, governance, implementation, auditing and documentation into one connected software development process.</p><p class="es">Fruti Squad es un flujo multiagente coordinado que une estructura, gobernanza, implementación, auditoría y documentación en un solo proceso de desarrollo conectado.</p></div>
<h3 class="h3">Mensajes fundamentales</h3><div class="tbl"><table><thead><tr><th>Idea</th><th>EN</th><th>ES</th></tr></thead><tbody>{''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c in msgs)}</tbody></table></div>
<h3 class="h3">Orden de la comunicación</h3><ol class="rules"><li>El problema real de quien desarrolla.</li><li>El beneficio de usar Fruti Squad.</li><li>Cómo funciona la coordinación.</li><li>Quiénes son los especialistas.</li><li>Qué entregables produce.</li><li>Cómo instalarlo, probarlo o comprarlo.</li></ol>
<p class="note">No se abre con la complejidad del runtime. Primero el problema: <i>«AI coding agents can write code quickly, but keeping UX decisions, component contracts, implementation and documentation consistent gets hard when responsibilities are not separated.»</i></p>
<h3 class="h3">Una línea por especialista</h3><div class="tbl"><table><thead><tr><th></th><th>EN</th><th>ES</th></tr></thead><tbody>{''.join(f'<tr><td><b>{tema["productos"][i]["nombre"]}</b></td><td>{e(T[i]["en"][0])}</td><td>{e(T[i]["es"][0])}</td></tr>' for i in ['squad']+IDS)}</tbody></table></div>
<h3 class="h3">Límites de lo que decimos</h3><div class="claims"><div><b class="okt">Sí</b><ul>{''.join(f'<li>{a}</li>' for a,_ in claims)}</ul></div><div><b class="badt">No</b><ul>{''.join(f'<li>{b}</li>' for _,b in claims)}</ul></div></div>
<p class="note">Precios, descuentos y beneficios viven en materiales de venta actualizables, nunca en la identidad. Las funciones públicas no se presentan como exclusivas de pago.</p>'''

pend = '''<aside class="pend" aria-label="Decisiones pendientes"><b>Pendiente de confirmar</b><ul>
<li><b>Nombres.</b> El manual usa los nombres aprobados en las rondas (UX Architect, UI Audit, Frontend Implementation Engineer, Documentation &amp; Knowledge Engineer, Workflow Pack). El brief propone UX Architecture, Visual Engineering &amp; Audit, Frontend Implementation, Verified Documentation y «Fruti Squad Complete». Cambiar es un reemplazo de texto: los símbolos no dependen del nombre.</li>
<li><b>Monoespaciada de marca</b> para código y terminal.</li>
<li>Secciones 5 a 8 (Product Branding, Marketing, Digital Standards, Brand Assets): siguiente fase.</li></ul></aside>'''

toc = [(1, 'estrategia', 'Brand Strategy'), (2, 'visual', 'Visual Identity'), (3, 'agentes', 'Agent Identity System'), (4, 'verbal', 'Verbal Identity')]
CSS = open(os.path.join(D, 'manual.css')).read()
page = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Fruti Squad Manual</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><header class="top"><img src="{uri('squad','lockup-oscuro')}" alt="Fruti Squad" class="tl"><div><p class="ver">Manual de marca · v0.1 · fase 1 de 2</p><h1>Five specialists.<br>One coordinated workflow.</h1><p class="intro">Estrategia y voz del brief estratégico; identidad visual aprobada en las rondas 1 a 20. Para Codex, Kiro y Claude Code.</p></div>
<nav aria-label="Secciones"><ol>{''.join(f'<li><a href="#{a}"><span>{n:02d}</span>{t}</a></li>' for n,a,t in toc)}</ol></nav></header>
<main>{pend}{sec(1,'estrategia','Estrategia de marca','Brand Strategy',s1)}{sec(2,'visual','Identidad visual','Visual Identity',s2)}{sec(3,'agentes','Sistema de especialistas','Agent Identity System',s3)}{sec(4,'verbal','Identidad verbal','Verbal Identity',s4)}</main>
<footer class="foot">Fruti Squad · manual v0.1 · generado desde <code>.fruti/icons/fruti-squad-2/manual/gen.py</code></footer></body></html>'''
open(os.path.join(D, 'index.html'), 'w').write(page)
print('ok', len(page))
