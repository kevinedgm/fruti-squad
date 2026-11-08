# Nexa Squad · ronda 3 · tres propuestas: Retícula afinada, Huecos, Cuadrantes. python3 gen.py -> propuestas.html
import os
D = os.path.dirname(os.path.abspath(__file__))
AG = [('squad','Nexa Squad','El squad'),('orka','Orka','Conductor'),('inqa','Inqa','Product Analyst'),('arko','Arko','Systems Architect'),
      ('fluxa','Fluxa','Flow Designer'),('kompa','Kompa','Layout Composer'),('kura','Kura','Component Curator'),('forja','Forja','Build Engineer'),('vera','Vera','QA Auditor')]
def svg(parts, size, label, defs=''):
    return f'<svg viewBox="0 0 48 48" width="{size}" height="{size}" role="img" aria-label="{label}">{defs}{"".join(parts)}</svg>'

# 1 · Retícula afinada (ronda 2 corregida)
W = 40/3 - 2; T3 = [4, 4+W+3, 4+2*(W+3)]
def s_(x, y, w, h, r=3): return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{r}" fill="currentColor"/>'
def o_(x, y, w, h): return f'<rect x="{x+1.4:.2f}" y="{y+1.4:.2f}" width="{w-2.8:.2f}" height="{h-2.8:.2f}" rx="2" fill="none" stroke="currentColor" stroke-width="2.8"/>'
R = {
 'squad': [s_(4,4,18,40), s_(26,4,18,18), o_(26,26,18,18)],
 'orka':  [s_(15,4,18,18)] + [o_(x,28,W,16) for x in T3],
 'inqa':  [s_(4,7,12,12), o_(20,7,24,12), s_(4,29,12,12), o_(20,29,24,12)],
 'arko':  [o_(4,4,40,18), s_(4,26,40,18)],
 'fluxa': [o_(4,4,18,18), o_(26,4,18,18), s_(26,26,18,18)],
 'kompa': [o_(4,4,40,12), o_(4,20,12,24), s_(20,20,24,24)],
 'kura':  [o_(4,y,W,W) for y in T3] + [s_(4+W+3,4,40-W-3,40)],
 'forja': [s_(4,32,40,12), s_(17,18,27,12), s_(30,4,14,12)],
 'vera':  [s_(4,T3[0],40,W), s_(4,T3[1],40,W), o_(4,T3[2],40,W)],
}
R_T = {'squad':'Tres piezas que encajan: un módulo completo.','orka':'Uno dirige, tres trabajan (piezas más gruesas que en la ronda 2).',
 'inqa':'Dos requisitos, cada uno con su comprobación.','arko':'La base llena sostiene la capa que se ve.','fluxa':'Dos pantallas y el resultado al final.',
 'kompa':'Encabezado, lateral y contenido.','kura':'Tres usos a la izquierda se vuelven un componente (ya no comparte base con Arko).',
 'forja':'Escalones apilados: se construye por fases (ya no parece el icono de señal).','vera':'Dos filas pasan; la vacía regresa a su dueño.'}

# 2 · Huecos: una sola masa; el agente es el hueco. Nexa acomoda la pieza justa en el lugar que le toca.
def masa(id_, cuts):
    m = f'<defs><mask id="m-{id_}"><rect width="48" height="48" fill="#fff"/>{cuts}</mask></defs>'
    return [m, f'<rect x="4" y="4" width="40" height="40" rx="7" fill="currentColor" mask="url(#m-{id_})"/>']
K = 'fill="#000"'; KS = 'fill="none" stroke="#000" stroke-linecap="round" stroke-linejoin="round"'
H = {
 'squad': masa('squad', f'<rect x="26" y="26" width="22" height="22" rx="4" {K}/>'),
 'orka':  masa('orka', f'<circle cx="24" cy="24" r="8.5" {K}/>'),
 'inqa':  masa('inqa', f'<rect x="12" y="15" width="24" height="5" rx="2.5" {K}/><rect x="12" y="28" width="15" height="5" rx="2.5" {K}/>'),
 'arko':  masa('arko', f'<path d="M15 48 V30 A9 9 0 0 1 33 30 V48 Z" {K}/>'),
 'fluxa': masa('fluxa', f'<path d="M4 31 C14 31 14 17 24 17 S34 31 44 31" {KS} stroke-width="5.5"/>'),
 'kompa': masa('kompa', f'<rect x="0" y="16" width="48" height="4.5" {K}/><rect x="17" y="16" width="4.5" height="32" {K}/>'),
 'kura':  masa('kura', ''.join(f'<rect x="{x}" y="15" width="7" height="7" rx="1.5" {K}/>' for x in (11,20.5,30)) + f'<rect x="11" y="27" width="26" height="7" rx="1.5" {K}/>'),
 'forja': masa('forja', f'<path d="M24 0 H48 V30 H38 V20 H31 V10 H24 Z" {K}/>'),
 'vera':  masa('vera', f'<path d="M13 24.5 L21 32 L35 16" {KS} stroke-width="5.5"/>'),
}
H_T = {'squad':'La masa con su pieza faltante: el lugar exacto donde algo encaja.','orka':'El foco al centro: a quién le toca ahora.',
 'inqa':'Dos renglones calados: lo que debe hacer, escrito.','arko':'Un arco abierto en la base: la estructura de abajo.',
 'fluxa':'Un cauce que atraviesa la masa: el flujo entre pantallas.','kompa':'Los canales (gutters) que dividen encabezado, lateral y contenido.',
 'kura':'Tres huecos chicos sobre uno ancho: tres usos, un componente.','forja':'La esquina tallada en escalones: se construye por fases.',
 'vera':'La palomita calada en el bloque: el veredicto.'}

# 3 · Cuadrantes: un mosaico 2 × 2; cada cuadrante es cuadro, cuarto de círculo, punto o vacío.
def cuad(q):
    out = []; P = [(4,4),(25,4),(4,25),(25,25)]; L = 19
    for (x, y), t in zip(P, q):
        if t == 'S': out.append(s_(x, y, L, L, 2.5))
        elif t == 'D': out.append(f'<circle cx="{x+L/2}" cy="{y+L/2}" r="6.5" fill="currentColor"/>')
        elif t[0] == 'C':  # cuarto de círculo con el centro en la esquina indicada
            c = t[1:]; ox = x + (L if 'r' in c else 0); oy = y + (L if 'b' in c else 0)
            sx = x + (0 if 'r' in c else L); sy = y + (0 if 'b' in c else L)
            ex, ey = sx, oy; fx, fy = ox, sy
            sweep = 1 if c in ('br','tl') else 0
            out.append(f'<path d="M{ox} {oy} L{ex} {ey} A{L} {L} 0 0 {sweep} {fx} {fy} Z" fill="currentColor"/>')
    return out
Q = {
 'squad': cuad(['Cbr','Cbl','Ctr','Ctl']), 'orka': cuad(['Cbr','E','E','Ctl']), 'inqa': cuad(['S','D','S','D']),
 'arko': cuad(['Cbr','Cbl','S','S']), 'fluxa': cuad(['Cbl','E','E','Ctr']), 'kompa': cuad(['S','E','E','S']),
 'kura': cuad(['D','D','S','S']), 'forja': cuad(['E','S','S','S']), 'vera': cuad(['S','S','S','D']),
}
Q_T = {'squad':'Cuatro cuartos que se encuentran en el centro: el nexo.','orka':'Dos cuartos que se pasan el turno en diagonal.',
 'inqa':'Requisito y comprobación, dos veces.','arko':'Una cúpula sobre su base.','fluxa':'Una onda que cruza en diagonal: el flujo.',
 'kompa':'Lleno y vacío en equilibrio: el acomodo.','kura':'Dos usos sobre una pieza ancha: se vuelve componente.',
 'forja':'Un escalón construido: tres bloques, uno por fase.','vera':'Tres pasan; el punto es lo que se está revisando.'}

def rm(parts, pre): return [x.replace('id="m-', 'id="'+pre+'-').replace('#m-', '#'+pre+'-') for x in parts]
def sistema(key, nombre, tipo, sub, M, T):
    def tarj(i, n, r):
        k = key + i
        return (f'<article class="ag{" madre" if i=="squad" else ""}"><div class="lienzo claro">{svg(rm(M[i],k+"1"),96,n+", "+r)}</div>'
                f'<div class="lienzo oscuro">{svg(rm(M[i],k+"2"),96,n+", "+r)}</div><div class="chicos"><span>{svg(rm(M[i],k+"3"),32,n)}</span>'
                f'<span>{svg(rm(M[i],k+"4"),16,n)}</span></div><h3>{n} <small>{r}</small></h3><p>{T[i]}</p></article>')
    tarjetas = ''.join(tarj(i, n, r) for i, n, r in AG)
    def tira(pre, sz, cap):
        return ''.join('<figure>' + svg(rm(M[i], pre+i), sz, n) + (('<figcaption>'+n+'</figcaption>') if cap else '') + '</figure>' for i, n, _ in AG)
    return f'''<section class="sis" id="{key}"><header><p class="ojo">{tipo}</p><h2>{nombre}</h2><p>{sub}</p></header>
<div class="familia">{tira(key+'f',30,True)}</div>
<div class="prueba"><b>16 px</b><div class="f16">{tira(key+'a',16,False)}</div><div class="f16 osc">{tira(key+'b',16,False)}</div></div>
<div class="rejilla">{tarjetas}</div></section>'''

css = open(os.path.join(D,'../r1/simbolos.html')).read().split('<style>')[1].split('</style>')[0]
HTML = f'''<title>Nexa Squad · Símbolos r3</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&display=swap">
<style>{css}
.f16 figure,.familia figure{{margin:0}} .f16{{gap:12px}}
.idx{{display:flex;flex-wrap:wrap;gap:8px}} .idx a{{color:var(--fg);border:1px solid var(--line);border-radius:999px;padding:6px 14px;text-decoration:none;font-weight:600;background:var(--card)}}
.idx a:focus-visible{{outline:3px solid var(--fg);outline-offset:2px}}
</style>
<div class="w">
<div class="intro"><p class="ojo">Ronda 3 · tres propuestas en tinta</p><h1>Nexa Squad: tres caminos</h1>
<p>La primera corrige la Retícula de la ronda 2. Las otras dos son más abstractas: dejan de dibujar pantallas y trabajan con masa y geometría. Las tres usan solo formas llenas, sin el trazo con nodos que descartaste.</p>
<nav class="idx" aria-label="Propuestas"><a href="#p1">1 · Retícula afinada</a><a href="#p2">2 · Huecos</a><a href="#p3">3 · Cuadrantes</a></nav></div>
{sistema('p1','1 · Retícula afinada','Continuidad','La ronda 2 con sus tres riesgos corregidos: Forja ya no parece el icono de señal, Kura ya no comparte base con Arko y Orka tiene piezas más gruesas.',R,R_T)}
{sistema('p2','2 · Huecos','Más disruptiva','Todos los símbolos son el mismo bloque; lo que cambia es el hueco. Es la idea de Nexa al revés: no dibuja la pieza, dibuja el lugar donde la pieza encaja. A 16 px pesa mucho porque casi todo es masa.',H,H_T)}
{sistema('p3','3 · Cuadrantes','Más abstracta','Un mosaico de 2 × 2 en el que cada cuadrante es un cuadro, un cuarto de círculo, un punto o un vacío. Geométrica, de lectura suizo-Bauhaus; el significado está en la combinación, no en un dibujo.',Q,Q_T)}
<section class="cmp"><h2>Riesgos por propuesta</h2><ul>
<li><b>1 · Retícula afinada:</b> sigue dibujando pantallas; es la más clara y la menos sorprendente.</li>
<li><b>2 · Huecos:</b> la familia se reconoce de inmediato, pero en el bloque oscuro los nueve pesan igual; distinguirlos depende solo del hueco. Vera se parece a una casilla marcada y Orka a un botón de opción: dos iconos de interfaz que ya existen.</li>
<li><b>3 · Cuadrantes:</b> es la más abstracta; el significado necesita su texto la primera vez. Inqa y Kura usan los mismos elementos (punto y cuadro) en otro orden.</li></ul></section>
</div>'''
open(os.path.join(D,'propuestas.html'),'w').write(HTML); print('ok')
