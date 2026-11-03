# Escudo de Oaxaca · propuestas r1 (ejercicio propio del usuario, 2026-11-03). Tres direcciones:
# A heráldica depurada (conserva composición y cruz), B sello circular, C greca de las ocho regiones.
# Paleta: los tintes históricos de Oaxaca: grana (cochinilla) y añil, más oro y cal. Uso: python3 gen.py → svg/, revision.html
import os, math, json
D = os.path.dirname(os.path.abspath(__file__)); SV = os.path.join(D, 'svg'); os.makedirs(SV, exist_ok=True)
GRANA, ANIL, ORO, CAL, TINTA = '#8E1B2E', '#1F3A68', '#E2A428', '#F7F1E6', '#231A1C'
FONT = "Archivo, 'Archivo', sans-serif"
def star(cx, cy, R, r=None, rot=0):
    r = r or R * .42; p = []
    for k in range(10):
        a = math.radians(rot - 90 + k * 36); rr = R if k % 2 == 0 else r
        p.append(f'{cx + rr*math.cos(a):.2f},{cy + rr*math.sin(a):.2f}')
    return 'M' + ' L'.join(p) + 'Z'
def greca(x, y, s, n=1):
    # Greca escalonada de Mitla: escalones + gancho en espiral. Módulo de 10×8 unidades, trazo de 1 unidad.
    pts = []
    for i in range(n):
        o = i * 10
        pts += [(o+0,8),(o+0,6),(o+2,6),(o+2,4),(o+4,4),(o+4,2),(o+6,2),(o+6,0),(o+10,0)]
    d = 'M' + ' L'.join(f'{x+px*s:.1f},{y+py*s:.1f}' for px, py in pts)
    hooks = ''.join(f'M{x+(i*10+10)*s:.1f},{y:.1f} L{x+(i*10+10)*s:.1f},{y+8*s:.1f} L{x+(i*10+6.5)*s:.1f},{y+8*s:.1f} L{x+(i*10+6.5)*s:.1f},{y+4.5*s:.1f} L{x+(i*10+8.2)*s:.1f},{y+4.5*s:.1f}' for i in range(n))
    return f'<path d="{d} {hooks}" fill="none" stroke-width="{s*1.15:.1f}" stroke-linecap="square" stroke-linejoin="miter"/>'
def _qb(p0, p1, p2, t): return tuple((1-t)**2*a + 2*(1-t)*t*b + t*t*c for a, b, c in zip(p0, p1, p2))
def huaje(cx, cy, s, hoja=TINTA, vaina=GRANA, semilla=CAL):
    # Huaje (guaje): rama con hojas pinnadas y tres vainas planas colgando con sus semillas. Caja ~100 con s=1.
    T = lambda x, y: (cx + x*s, cy + y*s); f = lambda q: f'{q[0]:.1f},{q[1]:.1f}'
    out = []
    for ang in (-60, 0, 60):  # tres hojas pinnadas
        a = math.radians(ang - 90); L = 40 if ang == 0 else 36
        x1, y1 = 0 + L*math.cos(a), -14 + L*math.sin(a)
        out.append(f'<path d="M{f(T(0,-14))} L{f(T(x1,y1))}" stroke="{hoja}" stroke-width="{2.6*s:.1f}" stroke-linecap="round"/>')
        for k in range(1, 6):
            t = k / 6; px, py = 0 + (x1)*t, -14 + (y1+14)*t
            for sg in (-1, 1):
                ang2 = ang - 90 + sg*55; b = math.radians(ang2); lx, ly = px + 6.5*math.cos(b), py + 6.5*math.sin(b)
                X, Y = T(lx, ly); out.append(f'<ellipse cx="{X:.1f}" cy="{Y:.1f}" rx="{5.6*s:.1f}" ry="{2.5*s:.1f}" transform="rotate({ang2:.0f} {X:.1f} {Y:.1f})" fill="{hoja}"/>')
    for x0, bend, L in ((-14, -8, 48), (0, 2, 56), (14, 10, 48)):  # vainas
        p0, p1, p2 = T(x0*.4, -12), T(x0, 14), T(x0 + bend, -12 + L)
        out.append(f'<path d="M{f(p0)} Q{f(p1)} {f(p2)}" fill="none" stroke="{vaina}" stroke-width="{10*s:.1f}" stroke-linecap="round"/>')
        for t in (.35, .55, .75, .92):
            q = _qb(p0, p1, p2, t); out.append(f'<circle cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="{2.1*s:.1f}" fill="{semilla}"/>')
    return ''.join(out)
def cadena(cx, cy, s, c=GRANA, chispa=ORO):
    # Cadena rota: dos eslabones entrelazados a cada lado y el del centro abierto, con chispas.
    w = 4.6 * s; o = []
    E = lambda x, y, rot: f'<rect x="{x-15*s:.1f}" y="{y-8.5*s:.1f}" width="{30*s:.1f}" height="{17*s:.1f}" rx="{8.5*s:.1f}" transform="rotate({rot} {x:.1f} {y:.1f})" fill="none" stroke="{c}" stroke-width="{w:.1f}"/>'
    for sg in (-1, 1):
        o.append(E(cx + sg*58*s, cy + 8*s, sg*-20)); o.append(E(cx + sg*34*s, cy - 1*s, sg*-20))
        x = cx + sg*14*s  # medio eslabón abierto
        o.append(f'<path d="M{x - sg*1*s:.1f},{cy - 9*s:.1f} Q{x + sg*8*s:.1f},{cy - 8*s:.1f} {x + sg*9*s:.1f},{cy - 2*s:.1f}" transform="rotate({sg*-20} {x:.1f} {cy:.1f})" fill="none" stroke="{c}" stroke-width="{w:.1f}" stroke-linecap="round"/>')
    for dx, dy, l in ((0, -16, 9), (-7, -13, 6), (7, -13, 6), (0, 14, 7)):
        a = math.atan2(dy, dx); o.append(f'<path d="M{cx + dx*s:.1f},{cy + dy*s:.1f} l{l*math.cos(a)*s:.1f},{l*math.sin(a)*s:.1f}" stroke="{chispa}" stroke-width="{2.8*s:.1f}" stroke-linecap="round"/>')
    return ''.join(o)
def cruz(cx, cy, s, c=CAL):
    # Cruz dominicana (flordelisada) simplificada: brazos iguales con remate de tres lóbulos.
    out = f'<path d="M{cx},{cy-16*s} V{cy+16*s} M{cx-16*s},{cy} H{cx+16*s}" stroke="{c}" stroke-width="{5*s}" />'
    for a in range(4):
        r = math.radians(a * 90); ex, ey = cx + 18*s*math.sin(r), cy - 18*s*math.cos(r)
        for d in (-1, 0, 1):
            rr = r + d * .6; out += f'<circle cx="{ex + (3 if d else 0)*s*math.sin(rr):.1f}" cy="{ey - (3 if d else 0)*s*math.cos(rr):.1f}" r="{3.6*s:.1f}" fill="{c}"/>'
    return out
def textpath(pid, d, txt, size, fill, ls=1.5, w=700):
    return (f'<path id="{pid}" d="{d}" fill="none"/><text font-family="{FONT}" font-size="{size}" font-weight="{w}" letter-spacing="{ls}" fill="{fill}">'
            f'<textPath href="#{pid}" startOffset="50%" text-anchor="middle">{txt}</textPath></text>')
SVG = lambda vb, body, t: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{t}"><title>{t}</title>{body}</svg>'

# ---------- A · Heráldica depurada ----------
def prop_a(p='a'):
    cx, cy, rx, ry = 200, 250, 116, 140
    b = []
    sil = f'M70,64 H330 V300 C330,392 270,436 200,452 C130,436 70,392 70,300 Z'
    b.append(f'<path d="{sil}" fill="{GRANA}"/>')
    for x in (70, 330):  # lienzo enrollado: dos rollos arriba
        b.append(f'<circle cx="{x}" cy="64" r="20" fill="{GRANA}"/><circle cx="{x}" cy="64" r="9" fill="none" stroke="{CAL}" stroke-opacity=".55" stroke-width="3"/>')
    b.append(f'<rect x="70" y="44" width="260" height="10" fill="{GRANA}"/>')
    # 8 estrellas alrededor del óvalo
    for k in range(8):
        a = math.radians(-90 + 22.5 + k * 45)
        sx, sy = cx + 140 * math.cos(a), cy + 166 * math.sin(a)
        if sy > 400: sy -= 18
        b.append(f'<path d="{star(sx, sy, 11)}" fill="{ORO}"/>')
    # óvalo con lema
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{CAL}" stroke="{ORO}" stroke-width="5"/>')
    b.append(f'<clipPath id="{p}-in"><ellipse cx="{cx}" cy="{cy}" rx="{rx-24}" ry="{ry-24}"/></clipPath>')
    g = [f'<rect x="80" y="100" width="120" height="152" fill="{ORO}"/>', f'<rect x="200" y="100" width="120" height="152" fill="{ANIL}"/>',
         f'<rect x="80" y="252" width="240" height="160" fill="{CAL}"/>',
         huaje(140, 186, .78, hoja=TINTA, vaina=GRANA),
         f'<g stroke="{CAL}">{greca(212, 206, 3.2, 3)}</g>', cruz(236, 172, .72),
         cadena(200, 318, 1.05)]
    b.append(f'<g clip-path="url(#{p}-in)">{"".join(g)}</g>')
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx-24}" ry="{ry-24}" fill="none" stroke="{ORO}" stroke-width="2"/>')
    rr = (rx + rx - 24) / 2; ry2 = (ry + ry - 24) / 2
    t0, t1 = math.radians(152), math.radians(28)
    arc = f'M{cx + rr*math.cos(t0):.1f},{cy + ry2*math.sin(t0):.1f} A{rr},{ry2} 0 1 1 {cx + rr*math.cos(t1):.1f},{cy + ry2*math.sin(t1):.1f}'
    b.append(textpath(f'{p}-lema', arc, 'EL RESPETO AL DERECHO AJENO ES LA PAZ', 13.5, GRANA, 1.2))
    # cinta
    b.append(f'<path d="M52,404 L82,396 V430 L52,438 L64,421 Z M348,404 L318,396 V430 L348,438 L336,421 Z" fill="#6A1322"/>'
             f'<rect x="78" y="392" width="244" height="34" rx="3" fill="{CAL}" stroke="{ORO}" stroke-width="2"/>'
             f'<text x="200" y="414" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" letter-spacing=".8" fill="{GRANA}">ESTADO LIBRE Y SOBERANO DE OAXACA</text>')
    return SVG('10 20 380 440', ''.join(b), 'Escudo de Oaxaca, propuesta A')
def reducido_a(p='ar'):
    b = [f'<path d="M14,10 H86 V62 C86,84 70,96 50,100 C30,96 14,84 14,62 Z" fill="{GRANA}"/>',
         f'<clipPath id="{p}-c"><ellipse cx="50" cy="55" rx="27" ry="33"/></clipPath>',
         f'<g clip-path="url(#{p}-c)"><rect x="20" y="20" width="30" height="35" fill="{ORO}"/><rect x="50" y="20" width="30" height="35" fill="{ANIL}"/><rect x="20" y="55" width="60" height="40" fill="{CAL}"/>'
         f'{huaje(35, 40, .3)}<g stroke="{CAL}">{greca(52, 40, 1.1, 2)}</g>{cadena(50, 72, .36)}</g>',
         f'<ellipse cx="50" cy="55" rx="29" ry="35" fill="none" stroke="{ORO}" stroke-width="4"/>']
    for k in range(8):
        a = math.radians(-90 + 22.5 + k * 45); b.append(f'<path d="{star(50 + 33*math.cos(a)*1.0, 55 + 39*math.sin(a), 4.2)}" fill="{ORO}"/>')
    return SVG('0 0 100 104', ''.join(b), 'Sello reducido de Oaxaca, propuesta A')

# ---------- B · Sello circular ----------
def prop_b(p='b', reducido=False):
    c, R = 200, 190
    b = [f'<circle cx="{c}" cy="{c}" r="{R}" fill="{GRANA}"/>', f'<circle cx="{c}" cy="{c}" r="{R-8}" fill="none" stroke="{ORO}" stroke-width="2"/>']
    if not reducido:
        b.append(textpath(f'{p}-t1', f'M{c-158},{c} A158,158 0 0 1 {c+158},{c}', 'ESTADO LIBRE Y SOBERANO DE OAXACA', 19, CAL, 2.4))
        b.append(textpath(f'{p}-t2', f'M{c-172},{c} A172,172 0 0 0 {c+172},{c}', 'EL RESPETO AL DERECHO AJENO ES LA PAZ', 15, CAL, 1.6, 600))
    rin = 128 if not reducido else 150
    for k in range(8):
        a = math.radians(-90 + k * 45) if reducido else math.radians(180 + (k + .5) * 180 / 8) if False else None
    # 8 estrellas: arco de estrellas en la franja interior, una por región
    rs = rin + 13 if not reducido else rin + 22
    for k in range(8):
        a = math.radians(-90 + k * 45 + 22.5)
        b.append(f'<path d="{star(c + rs*math.cos(a), c + rs*math.sin(a), 8 if not reducido else 13)}" fill="{ORO}"/>')
    b.append(f'<circle cx="{c}" cy="{c}" r="{rin}" fill="{CAL}"/><clipPath id="{p}-c"><circle cx="{c}" cy="{c}" r="{rin}"/></clipPath>')
    s = rin / 128
    g = [f'<rect x="0" y="{c - 6*s}" width="400" height="{50*s}" fill="{ANIL}"/>',
         f'<g stroke="{CAL}">{greca(c - 135*s, c + 3*s, 3.2*s, 9)}</g>',
         huaje(c, c - 66*s, 1.05*s), cadena(c, c + 80*s, 1.25*s)]
    b.append(f'<g clip-path="url(#{p}-c)">{"".join(g)}</g>')
    return SVG('0 0 400 400', ''.join(b), 'Escudo de Oaxaca, propuesta B' + (' reducida' if reducido else ''))

# ---------- C · Greca de las ocho regiones ----------
REGIONES = ['Cañada', 'Papaloapan', 'Sierra Norte', 'Istmo', 'Costa', 'Sierra Sur', 'Valles Centrales', 'Mixteca']
def emblema_c(p='c', mono=None):
    # Ocho lados, ocho regiones: cada lado del octágono es un tramo de greca de Mitla. Centro: el huaje.
    Ro, Ri = 150, 100; b = ['<g transform="translate(200 200)">']
    for k in range(8):
        a0, a1 = math.radians(-112.5 + 45*k), math.radians(-67.5 + 45*k)
        pts = [(Ro*math.cos(a0), Ro*math.sin(a0)), (Ro*math.cos(a1), Ro*math.sin(a1)), (Ri*math.cos(a1), Ri*math.sin(a1)), (Ri*math.cos(a0), Ri*math.sin(a0))]
        col = mono or (GRANA if k % 2 == 0 else ANIL)
        b.append(f'<path d="M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + f'Z" fill="{col}"/>')
        gc = CAL if not mono else (TINTA if mono == '#ffffff' else '#fff')
        ap = (Ro + Ri) / 2 * math.cos(math.radians(22.5)); sc = 3.3
        b.append(f'<g transform="rotate({45*k}) translate({-10*sc:.1f} {-ap - 4*sc:.1f})" stroke="{gc}">{greca(0, 0, sc, 2)}</g>')
    b.append(f'<circle r="74" fill="{mono or ORO}" opacity="{1 if not mono else 0}"/>')
    b.append(huaje(0, -4, 1.05, hoja=(mono or TINTA), vaina=(mono or GRANA), semilla=gc) + '</g>')
    return SVG('40 40 320 320', ''.join(b), 'Emblema de Oaxaca, propuesta C')
def lockup_c():
    _e = emblema_c('cl'); e = _e[_e.index('<g'):-6]
    t = (f'<text x="380" y="190" font-family="{FONT}" font-size="86" font-weight="800" letter-spacing="6" fill="{TINTA}">OAXACA</text>'
         f'<text x="384" y="226" font-family="{FONT}" font-size="20" font-weight="600" letter-spacing="3" fill="{GRANA}">ESTADO LIBRE Y SOBERANO</text>'
         f'<text x="384" y="256" font-family="{FONT}" font-size="16" font-weight="400" letter-spacing=".5" fill="{TINTA}">El respeto al derecho ajeno es la paz</text>')
    return SVG('40 40 800 320', e + t, 'Oaxaca, Estado Libre y Soberano, propuesta C')

P = {'a': prop_a(), 'a-reducido': reducido_a(), 'b': prop_b(), 'b-reducido': prop_b('br', True), 'c': emblema_c(), 'c-1tinta': emblema_c('cm', '#231A1C'), 'c-horizontal': lockup_c()}
for k, s in P.items(): open(os.path.join(SV, f'oaxaca-{k}.svg'), 'w').write(s)
json.dump({'regiones': REGIONES}, open(os.path.join(D, 'datos.json'), 'w'), ensure_ascii=False)
print('ok', list(P))

# ---------- Página de revisión ----------
import base64
def uri(s): return 'data:image/svg+xml;base64,' + base64.b64encode(s.encode()).decode()
def lum(h):
    c = [int(h[i:i+2], 16)/255 for i in (1, 3, 5)]; c = [x/12.92 if x <= .04045 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0] + .7152*c[1] + .0722*c[2]
cr = lambda a, b: f'{(max(lum(a), lum(b))+.05)/(min(lum(a), lum(b))+.05):.1f}'
def tam(s, oscura):
    f = ''.join(f'<figure><img src="{uri(s)}" width="{n}" height="{n}" alt=""><figcaption>{n}</figcaption></figure>' for n in (64, 32, 16))
    return f + f'<figure><span class="osc"><img src="{uri(oscura)}" width="44" height="44" alt=""></span><figcaption>sobre oscuro</figcaption></figure>'
P2 = {'b-oscura': prop_b('bo', True), 'c-blanco': emblema_c('cw', '#ffffff')}
P2['b-oscura'] = P2['b-oscura']  # el sello ya tiene su propio fondo grana
def regiones_c():
    s = emblema_c('cr'); body = s[s.index('<g'):-6]; t = []
    for k, n in enumerate(REGIONES):
        a = math.radians(-90 + 45*k); x, y = 200 + 176*math.cos(a), 200 + 176*math.sin(a)
        anc = 'middle' if abs(math.cos(a)) < .3 else ('start' if math.cos(a) > 0 else 'end')
        t.append(f'<text x="{x:.0f}" y="{y + 5:.0f}" text-anchor="{anc}" font-family="{FONT}" font-size="15" font-weight="600" fill="{TINTA}">{n}</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-120 -10 640 420" role="img" aria-label="Emblema C con el nombre de cada región en su lado">{body}{"".join(t)}</svg>'
html = open(os.path.join(D, 'plantilla.html')).read()
rep = {'A': P['a'], 'B': P['b'], 'C': P['c'], 'CH': P['c-horizontal'], 'CR': regiones_c(),
       'TA': tam(P['a-reducido'], P['a-reducido']), 'TB': tam(P['b-reducido'], P['b-reducido']), 'TC': tam(P['c'], P2['c-blanco']),
       'REG': ''.join(f'<li>{n}</li>' for n in REGIONES), 'K1': cr(CAL, GRANA), 'K2': cr(CAL, ANIL), 'K3': cr(GRANA, CAL)}
for k, v in rep.items(): html = html.replace('{{' + k + '}}', v)
assert '{{' not in html
open(os.path.join(SV, 'oaxaca-c-blanco.svg'), 'w').write(P2['c-blanco'])
open(os.path.join(D, 'revision.html'), 'w').write(html); print('revision ok', len(html))
