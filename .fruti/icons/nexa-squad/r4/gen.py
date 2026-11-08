# Nexa Squad · ronda 4 · símbolos desde la función real de cada agente (fuente: skills/<agente>/SKILL.md de nexa-squad),
# dibujados en los tres idiomas de la ronda 3. python3 gen.py -> funcion.html
import os
D = os.path.dirname(os.path.abspath(__file__))
AG = [('squad','Nexa Squad','El squad'),('orka','Orka','Conductor'),('inqa','Inqa','Product Analyst'),('arko','Arko','Systems Architect'),
      ('fluxa','Fluxa','Flow Designer'),('kompa','Kompa','Layout Composer'),('kura','Kura','Component Curator'),('forja','Forja','Build Engineer'),('vera','Vera','QA Auditor')]
FUN = {  # (lo que hace, según su SKILL.md) · (el gesto que se abstrae)
 'squad': ('Ocho roles en cadena; cada decisión tiene un solo dueño.', 'Ocho piezas distintas que forman un solo módulo.'),
 'orka':  ('Lee el estado, elige el primer paso que falta o no está aprobado y lanza un solo rol a la vez.', 'Una cadena: lo aprobado, el paso actual y lo pendiente.'),
 'inqa':  ('Separa siempre hechos (vistos en código), supuestos (marcados) y preguntas; de ahí salen los requisitos.', 'Tres clases de cosa: lo firme, lo supuesto y lo que falta preguntar.'),
 'arko':  ('Decide datos, API y permisos; los permisos se validan en el servidor, no en la pantalla.', 'Una base que solo deja pasar por una entrada controlada.'),
 'fluxa': ('Inventario de vistas en el orden real de la tarea; cada vista de gestión: cabecera, herramientas, datos y pie.', 'Cuatro franjas fijas donde los datos mandan.'),
 'kompa': ('En cada fila decide qué control crece, cuáles conservan su ancho y en qué orden ceden en tres anchos.', 'La misma fila en escritorio, tableta y teléfono: el campo cede, el botón no.'),
 'kura':  ('Para cada hueco busca primero lo que existe y cuenta cuántas veces aparece: reutilizar, variante, nuevo o local.', 'La misma necesidad repetida: lo que ya existe llena el hueco.'),
 'forja': ('Construye primero lo de atrás (datos, API, permisos), luego las vistas; fase por fase y probando cada criterio.', 'Capas de abajo hacia arriba: la base terminada, la vista a medias, la siguiente fase pendiente.'),
 'vera':  ('Verifica cada criterio y regresa cada hallazgo al rol dueño de la decisión que falló.', 'Un hallazgo que sube por su canal hasta su dueño.'),
}
def svg(parts, size, label): return f'<svg viewBox="0 0 48 48" width="{size}" height="{size}" role="img" aria-label="{label}">{"".join(parts)}</svg>'
def s_(x, y, w, h, r=3): return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{r}" fill="currentColor"/>'
def o_(x, y, w, h): return f'<rect x="{x+1.4:.2f}" y="{y+1.4:.2f}" width="{w-2.8:.2f}" height="{h-2.8:.2f}" rx="2" fill="none" stroke="currentColor" stroke-width="2.8"/>'
W3 = 40/3 - 2; T3 = [4, 4+W3+3, 4+2*(W3+3)]; W4 = 7.75; T4 = [4 + i*(W4+3) for i in range(4)]

# Retícula: contorno = lo que ya existe o está pendiente; lleno = lo decidido
R = {
 'squad': sum([[s_(4, T4[i], a, W4, 2), s_(4+a+3, T4[i], 40-a-3, W4, 2)] for i, a in enumerate([26, 11, 18.5, 31])], []),
 'orka':  [s_(T4[0],18,W4,26,2), s_(T4[1],18,W4,26,2), o_(T4[2],18,W4,26), o_(T4[3],18,W4,26), s_(T4[2],4,W4,W4,2)],
 'inqa':  [s_(4,6,40,9), o_(4,19.5,28,9), s_(4,33,9,9,4.5)],
 'arko':  [o_(4,4,40,15), s_(4,29,40,15), s_(19,17,10,14,1.5)],
 'fluxa': [o_(4,4,40,6.4), o_(4,13,40,6.4), s_(4,22,40,13), o_(4,37.6,40,6.4)],
 'kompa': sum([[s_(4,y,t-11,10,2.5), o_(4+t-8,y,8,10)] for y, t in [(4,40),(19,30),(34,20)]], []),
 'kura':  [s_(4,4,18,18), s_(26,4,18,18), o_(4,26,18,18)],
 'forja': [o_(4,4,40,10), s_(4,17,26,10), s_(4,30,40,14)],
 'vera':  [o_(T3[0],4,W3,18), s_(T3[1],4,W3,18), o_(T3[2],4,W3,18), s_(T3[0],26,W3,18), o_(T3[1],26,W3,18), s_(T3[2],26,W3,18)],
}
# Huecos: un solo bloque; el agente es lo que se le quita
def masa(id_, cuts):
    return [f'<defs><mask id="m-{id_}"><rect width="48" height="48" fill="#fff"/>{cuts}</mask></defs>',
            f'<rect x="4" y="4" width="40" height="40" rx="7" fill="currentColor" mask="url(#m-{id_})"/>']
def k(x, y, w, h, r=0): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#000"/>'
def kc(cx, cy, r): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#000"/>'
H = {
 'squad': masa('squad', k(0,22.5,48,3) + ''.join(k(x,0,3,24) for x in (13,23,33)) + ''.join(k(x,24,3,24) for x in (18,28,38))),
 'orka':  masa('orka', kc(10,24,2.2) + kc(18.5,24,2.2) + kc(28,24,5) + k(35,20,8,8,1.5)),
 'inqa':  masa('inqa', k(10,11,28,5,2.5) + k(10,21.5,11,5,2.5) + k(25,21.5,13,5,2.5) + kc(12.5,34.5,3.6)),
 'arko':  masa('arko', kc(24,19,6.5) + '<path d="M21 22 L18.5 37 H29.5 L27 22 Z" fill="#000"/>'),
 'fluxa': masa('fluxa', k(0,11.5,48,3) + k(0,19,48,3) + k(0,36,48,3)),
 'kompa': masa('kompa', k(0,15,48,3.5) + k(0,29.5,48,3.5) + k(32,0,3.5,16) + k(34,15,14,33) + k(22,15,3.5,16) + k(24,29.5,24,19) + k(12,29,3.5,19)),
 'kura':  masa('kura', ''.join(k(x,x,8,8,1.5) for x in (9,20,31))),
 'forja': masa('forja', k(22,9.5,26,9.5,0) + k(0,26.5,48,3)),
 'vera':  masa('vera', k(22.5,0,3,31) + k(19,28,10,10,1.5)),
}
# Cuadrantes: mosaico 2 × 2 (tl, tr, bl, br): cuadro, cuarto de círculo, punto o vacío
def cuad(q):
    out = []; P = [(4,4),(25,4),(4,25),(25,25)]; L = 19
    for (x, y), t in zip(P, q):
        if t == 'S': out.append(s_(x, y, L, L, 2.5))
        elif t == 'D': out.append(f'<circle cx="{x+L/2}" cy="{y+L/2}" r="6.5" fill="currentColor"/>')
        elif t[0] == 'C':
            c = t[1:]; ox = x + (L if 'r' in c else 0); oy = y + (L if 'b' in c else 0)
            sx = x + (0 if 'r' in c else L); sy = y + (0 if 'b' in c else L)
            sweep = 1 if c in ('br','tl') else 0
            out.append(f'<path d="M{ox} {oy} L{sx} {oy} A{L} {L} 0 0 {sweep} {ox} {sy} Z" fill="currentColor"/>')
    return out
Q = {
 'squad': cuad(['Cbr','Cbl','Ctr','Ctl']), 'orka': cuad(['S','S','E','D']), 'inqa': cuad(['S','Cbl','E','D']),
 'arko': cuad(['E','E','Ctr','Ctl']), 'fluxa': cuad(['Cbl','E','E','Ctr']), 'kompa': cuad(['S','Cbl','S','E']),
 'kura': cuad(['D','D','D','S']), 'forja': cuad(['Cbr','E','S','S']), 'vera': cuad(['S','D','S','S']),
}
LEE = {  # cómo se lee cada símbolo, por idioma
 'squad': ('Ocho piezas de tamaños distintos que llenan un módulo.', 'Ocho bloques trabados como ladrillos.', 'Cuatro cuartos que se juntan en el centro.'),
 'orka':  ('Dos aprobados, el pendiente con el marcador encima, otro detrás.', 'Hechos, el actual (círculo) y el pendiente (cuadro).', 'En el sentido del reloj: dos hechos, el punto actual y uno vacío.'),
 'inqa':  ('Hecho (lleno), supuesto (contorno), pregunta (punto).', 'Un renglón entero, uno partido y uno que falta.', 'Lo firme, una parte supuesta y la pregunta.'),
 'arko':  ('La interfaz arriba, el servidor abajo y una sola columna que los une.', 'Una cerradura: el servidor decide quién pasa.', 'Un cuenco que sostiene desde abajo.'),
 'fluxa': ('Cabecera, herramientas, datos (lleno) y pie.', 'Los mismos cuatro tramos, como cortes.', 'El recorrido de la tarea en diagonal.'),
 'kompa': ('Tres anchos: el campo se encoge, el botón conserva sus 8 unidades.', 'La fila se acorta; el último tramo nunca cambia.', 'Arriba, campo y botón que cede; abajo, el campo solo.'),
 'kura':  ('Dos que ya existen y el hueco del mismo tamaño.', 'El mismo hueco en tres lugares: es momento de un componente.', 'Tres usos y un componente.'),
 'forja': ('Base terminada, vista a medias, siguiente fase en contorno.', 'La capa de arriba aún sin terminar.', 'Base construida; la vista empieza a subir.'),
 'vera':  ('Abajo, un criterio falla; arriba se enciende su dueño.', 'El hallazgo sale por su canal hacia arriba.', 'Tres pasan; el punto está en manos de su dueño.'),
}
SIS = [('Retícula', R), ('Huecos', H), ('Cuadrantes', Q)]
def rm(parts, pre): return [x.replace('id="m-', f'id="{pre}-').replace('#m-', f'#{pre}-') for x in parts]

filas = []
for i, n, r in AG:
    celdas = ''.join(f'<div class="cel"><div class="par"><span class="cl">{svg(rm(M[i],f"a{j}{i}"),72,n+", "+nom)}</span><span class="os">{svg(rm(M[i],f"b{j}{i}"),72,n+", "+nom)}</span></div>'
                     f'<div class="mini"><span class="cl">{svg(rm(M[i],f"c{j}{i}"),16,n)}</span><span class="os">{svg(rm(M[i],f"d{j}{i}"),16,n)}</span><b>{nom}</b></div><p>{LEE[i][j]}</p></div>'
                     for j, (nom, M) in enumerate(SIS))
    filas.append(f'''<article class="fila{' madre' if i=='squad' else ''}"><header><h3>{n} <small>{r}</small></h3>
<p><span class="et">Qué hace</span>{FUN[i][0]}</p><p><span class="et">El gesto</span>{FUN[i][1]}</p></header><div class="tres">{celdas}</div></article>''')
tiras = ''.join(f'<div class="tira"><b>{nom}</b><div class="f16 cl">{"".join(svg(rm(M[i],f"t{j}{i}"),16,n) for i,n,_ in AG)}</div>'
                f'<div class="f16 os">{"".join(svg(rm(M[i],f"u{j}{i}"),16,n) for i,n,_ in AG)}</div>'
                f'<div class="f30">{"".join(svg(rm(M[i],f"v{j}{i}"),30,n) for i,n,_ in AG)}</div></div>' for j,(nom,M) in enumerate(SIS))

HTML = f'''<title>Nexa Squad · Símbolos r4</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&display=swap">
<style>
/* Una fila por agente: su función real arriba y el mismo gesto en los tres idiomas */
:root{{--bg:#f6f6f4;--fg:#17171c;--muted:#5b5b66;--line:#dcdcd6;--card:#fff;--ink:#17171c;--paper:#fff;--night:#111115;--nightfg:#f4f4f0;
--f:'Bricolage Grotesque',ui-sans-serif,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#141418;--fg:#eeeeea;--muted:#a3a3ad;--line:#2c2c33;--card:#1b1b20;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#141418;--fg:#eeeeea;--muted:#a3a3ad;--line:#2c2c33;--card:#1b1b20;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 64px}}
.w{{max-width:1180px;margin:0 auto;display:grid;gap:40px}}
h1{{font-size:clamp(30px,5vw,48px);line-height:1.05;margin:0;text-wrap:balance}}
.intro{{display:grid;gap:12px;max-width:70ch}} .intro p{{margin:0;color:var(--muted)}}
.ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.cl{{background:var(--paper);color:var(--ink);border:1px solid var(--line)}} .os{{background:var(--night);color:var(--nightfg);border:1px solid transparent}}
.tiras{{display:grid;gap:14px;padding:20px;background:var(--card);border:1px solid var(--line);border-radius:14px}}
.tira{{display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px}} .tira b{{width:110px;font-size:15px}}
.f16{{display:flex;gap:12px;padding:9px 12px;border-radius:9px}} .f30{{display:flex;gap:14px;color:var(--fg)}}
.fila{{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);gap:20px;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:14px}}
.fila.madre{{border-color:var(--fg)}}
.fila header{{display:grid;gap:8px;align-content:start}} .fila h3{{margin:0;font-size:22px;line-height:1.15}} .fila h3 small{{font-weight:400;font-size:14px;color:var(--muted)}}
.fila header p{{margin:0;font-size:15px}} .et{{display:block;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.tres{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}}
.cel{{display:grid;gap:8px;align-content:start}} .par{{display:flex;gap:6px}} .par span{{display:grid;place-items:center;flex:1;aspect-ratio:1;border-radius:10px;max-width:100%}}
.mini{{display:flex;gap:6px;align-items:center}} .mini span{{display:grid;place-items:center;width:30px;height:30px;border-radius:7px}} .mini b{{font-size:13px;margin-left:4px}}
.cel p{{margin:0;font-size:13.5px;color:var(--muted)}}
.cmp{{display:grid;gap:10px;max-width:72ch}} .cmp h2{{margin:0;font-size:26px}} .cmp ul{{margin:0;padding-left:20px;display:grid;gap:6px}}
@media (max-width:820px){{.fila{{grid-template-columns:1fr}}}}
@media (max-width:520px){{.tres{{grid-template-columns:1fr}} .par span{{max-width:120px}}}}
</style>
<div class="w">
<div class="intro"><p class="ojo">Ronda 4 · en tinta · desde lo que cada agente hace</p><h1>Nexa Squad: el símbolo sale de la función</h1>
<p>Leí el proceso de cada agente en su SKILL.md del repositorio de Nexa y saqué un solo gesto: la operación que más lo define. Ese gesto se dibuja igual en los tres idiomas de la ronda 3, así puedes juzgar por separado la idea (el gesto) y el dibujo (el idioma).</p></div>
<section class="tiras" aria-label="Las tres familias a 16 y 30 px">{tiras}</section>
{''.join(filas)}
<section class="cmp"><h2>Riesgos que veo</h2><ul>
<li><b>Retícula:</b> Inqa, Arko y Fluxa son franjas horizontales; se separan por el contenido de cada franja, no por la silueta.</li>
<li><b>Huecos:</b> Squad y Fluxa son cortes rectos; a 16 px Squad se lee como textura. Arko (cerradura) es el más claro de toda la ronda.</li>
<li><b>Cuadrantes:</b> sigue siendo la más abstracta; Orka, Vera y Kompa comparten cuadros y punto y se distinguen por la posición.</li>
<li><b>Kompa en Retícula</b> es el gesto más fiel a la función (tres anchos, el botón no cede), pero también el más cargado.</li></ul></section>
</div>'''
open(os.path.join(D,'funcion.html'),'w').write(HTML); print('ok')
