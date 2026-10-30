# NisaLab · indicadores de estatus, ronda 1.
# Tres dimensiones independientes de una muestra: proceso (4 etapas), pago (5 estados) y urgencia (marca).
# Cada dimensión usa una FORMA distinta para que el color pueda repetirse sin confundir:
#   proceso = pastilla rellena + círculo que se llena por etapa; pago = etiqueta con contorno + moneda; urgente = ficha sólida pera + rayo.
# Uso: python3 gen.py <carpeta de fuentes> <carpeta de íconos lucide> → estatus.html
import os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); F, LU = sys.argv[1], sys.argv[2]
def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)
def lucide(n, px=14):
    s = open(os.path.join(LU, n + '.svg')).read(); s = s[s.index('<svg'):]
    return re.sub(r'\s+', ' ', s).replace('width="24"', f'width="{px}"').replace('height="24"', f'height="{px}"').replace('stroke-width="2"', 'stroke-width="2.25"').replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
def etapa(n):  # círculo que se llena: 0 punteado, 1 mitad, 2 tres cuartos, 3 lleno con palomita
    b = '<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    if n == 0: return b + '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75" stroke-dasharray="2.6 2.1"/></svg>'
    if n == 3: return b + '<circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M4.8 8.2 7 10.4 11.2 5.9" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    arc = 'M8 8 V2.5 A5.5 5.5 0 0 1 8 13.5 Z' if n == 1 else 'M8 8 V2.5 A5.5 5.5 0 1 1 2.5 8 Z'
    return b + f'<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75"/><path d="{arc}" fill="currentColor"/></svg>'
def moneda(n):  # moneda que se llena: 0 vacía, 1 media, 2 llena
    b = '<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    s = '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75"/>'
    if n == 1: s += '<path d="M8 1.5 A6.5 6.5 0 0 0 8 14.5 Z" fill="currentColor"/>'
    if n == 2: s = '<circle cx="8" cy="8" r="7.5" fill="currentColor"/>'
    sign = '#fff' if n == 2 else 'currentColor'
    if n == 1: return b + s + '</svg>'
    return b + s + f'<path d="M10 5.6 H7.1 a1.3 1.3 0 0 0 0 2.6 h1.8 a1.3 1.3 0 0 1 0 2.6 H6 M8 4.2 v7.6" fill="none" stroke="{sign}" stroke-width="1.3" stroke-linecap="round"/></svg>'
# clave, nombre, ícono, fondo, texto, borde, qué lo dispara, decidido por
PROCESO = [
    ('no-ingresada', 'No ingresada', etapa(0), '#FBF0CC', '#664700', 'Recibida en ventanilla, sin folio interno.', 'usuario'),
    ('en-proceso', 'En proceso', etapa(1), '#E0F2FE', '#075985', 'Se le asignó folio interno de laboratorio.', 'usuario'),
    ('generando-informe', 'Generando informe', etapa(2), '#EDE9FE', '#5B21B6', 'Todos los parámetros requeridos capturados.', 'usuario'),
    ('terminada', 'Terminada', etapa(3), '#E3F1E4', '#1E5A22', 'Informe generado y enviado.', 'usuario'),
]
PAGO = [
    ('no-pagada', 'No pagada', moneda(0), '#FFFFFF', '#B42318', 'Sin pagos registrados.', 'usuario'),
    ('parcial', 'Pago parcial', moneda(1), '#FFFFFF', '#B54708', 'Pagó una parte; queda saldo.', 'usuario'),
    ('pagada', 'Pagada', moneda(2), '#FFFFFF', '#1E6B34', 'Saldo en cero.', 'usuario'),
    ('cancelada', 'Cancelada', lucide('ban'), '#FFFFFF', '#475467', 'Se anuló el cobro; no se cobra ni se debe.', 'propuesta'),
    ('cortesia', 'Cortesía', lucide('gift'), '#FFFFFF', '#052A76', 'Se procesa sin cobro, por decisión del laboratorio.', 'propuesta'),
]
def pastilla(n, ic, bg, tx): return f'<span class="ps" style="background:{bg};color:{tx}">{ic}{n}</span>'
def etiqueta(n, ic, tx): return f'<span class="et" style="color:{tx};border-color:{tx}">{ic}{n}</span>'
URG = {'U1': ('#C2D225', '#052A76', 'Pera + rayo (recomendada)', 'El único color del sistema que no significa nada más: hoy solo vive en la célula de Colonia. Salta a la vista sin parecer error.'),
       'U2': ('#141B33', '#FFFFFF', 'Tinta + rayo', 'Máximo contraste y sobria; se nota por peso, no por color. Menos llamativa entre muchas filas.')}
def urgente(k, px=14): bg, tx, *_ = URG[k]; return f'<span class="ur" style="background:{bg};color:{tx}">{lucide("zap", px)}Urgente</span>'
def tabla_dim(lista, kind):
    rows = ''
    for k, n, ic, bg, tx, cuando, por in lista:
        chip = pastilla(n, ic, bg, tx) if kind == 'p' else etiqueta(n, ic, tx)
        c = cr(tx, bg); tag = '' if por == 'usuario' else '<em>propuesta</em>'
        rows += f'<tr><td>{chip}</td><td>{cuando}</td><td class="m">{tx} sobre {bg} · {c}:1</td><td>{tag or "tuyo"}</td></tr>'
    return f'<div class="tw"><table class="ref"><thead><tr><th>Indicador</th><th>Cuándo</th><th>Color y contraste</th><th>Origen</th></tr></thead><tbody>{rows}</tbody></table></div>'
P = {k: (n, ic, bg, tx) for k, n, ic, bg, tx, *_ in PROCESO}; G = {k: (n, ic, bg, tx) for k, n, ic, bg, tx, *_ in PAGO}
MUESTRAS = [('AG-2610-0147', 'Aguas', '#007CA3', 'en-proceso', 'pagada', True), ('AL-2610-0152', 'Alimentos', '#A6552D', 'no-ingresada', 'no-pagada', False),
            ('BE-2610-0088', 'Bebidas alcohólicas', '#7A5DA9', 'generando-informe', 'parcial', True), ('AG-2610-0139', 'Aguas', '#007CA3', 'terminada', 'pagada', False),
            ('AL-2610-0131', 'Alimentos', '#A6552D', 'terminada', 'cortesia', False), ('AG-2610-0150', 'Aguas', '#007CA3', 'no-ingresada', 'cancelada', False)]
def lista(u):
    r = ''
    for fol, a, ac, p, g, urg in MUESTRAS:
        r += (f'<tr class="{"urg" if urg else ""}" style="--uc:{URG[u][0]}"><td class="m fol">{fol}</td><td>{urgente(u) if urg else ""}</td><td><span class="ar"><i style="background:{ac}"></i>{a}</span></td>'
              f'<td>{pastilla(*P[p])}</td><td>{etiqueta(G[g][0], G[g][1], G[g][3])}</td></tr>')
    return f'<div class="tw"><table class="ls"><thead><tr><th>Folio</th><th><span class="vh">Prioridad</span></th><th>Área</th><th>Proceso</th><th>Pago</th></tr></thead><tbody>{r}</tbody></table></div>'
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700)) + f"@font-face{{font-family:'IBM Plex Mono';src:url('file://{F}/IBMPlexMono.ttf')}}"
css = ff + '''
:root{--az:#052A76;--tinta:#141B33;--gris:#535B70;--bg:#F2F4F8;--borde:#DFE3EC}
*{box-sizing:border-box}body{margin:0;background:#E6E9F0;color:var(--tinta);font:400 14px/1.5 Poppins,sans-serif;padding:32px}
h1{font:700 26px/1.2 Poppins;color:var(--az);margin:0 0 4px}.lead{color:var(--gris);max-width:860px;margin:0 0 24px}
section{background:#fff;border-radius:14px;padding:24px;margin-bottom:20px;box-shadow:0 1px 2px rgba(20,27,51,.06)}
h2{font:600 19px/1.3 Poppins;margin:0}.id{color:var(--gris);margin:4px 0 16px;max-width:900px}
h3{font:600 11px/1 Poppins;letter-spacing:.06em;text-transform:uppercase;color:var(--gris);margin:18px 0 10px}
.ps,.et,.ur{display:inline-flex;align-items:center;gap:6px;font:500 13px/18px Poppins;white-space:nowrap}
.ps{border-radius:999px;padding:3px 10px 3px 7px}.et{border:1.5px solid;border-radius:6px;padding:2px 8px 2px 6px;background:#fff}
.ur{font-weight:600;border-radius:6px;padding:3px 8px 3px 6px}
.tw{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:13px}th{text-align:left;font-weight:500;color:var(--gris);background:#EEF1F6;padding:8px 10px}td{padding:9px 10px;border-top:1px solid var(--borde)}
.ref td:nth-child(2){color:var(--gris)}.m{font-family:'IBM Plex Mono',monospace;font-size:12px}.ref em{font-style:normal;font-size:11px;color:#664700;background:#FBF0CC;border-radius:6px;padding:1px 6px}
.ls td{white-space:nowrap}.ls tr.urg td:first-child{box-shadow:inset 4px 0 0 var(--uc)}.fol{font-weight:600}
.ar{display:inline-flex;align-items:center;gap:6px}.ar i{width:12px;height:12px;border-radius:50%;display:inline-block}
.dos{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}.dos>div{min-width:0}.gris{filter:grayscale(1)}
.flujo{display:flex;align-items:center;gap:8px;flex-wrap:wrap}.flujo b{color:var(--gris);font-weight:400}
.ad{border-left:4px solid #E9B10A;background:#FFFBEB;border-radius:8px;padding:12px 16px;margin:0}.ad li{margin:4px 0}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (max-width:1000px){.dos{grid-template-columns:1fr}}@media (max-width:480px){body{padding:12px}section{padding:16px}}
'''
flujo = '<b>→</b>'.join(pastilla(*P[k]) for k, *_ in PROCESO)
uopts = ''.join(f'<div><h3>{k} · {URG[k][2]}</h3><p class="id">{URG[k][3]}</p>{lista(k)}</div>' for k in URG)
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Indicadores de estatus</title><style>{css}</style><body>'
 '<h1>Indicadores de estatus · ronda 1</h1><p class="lead">Una muestra tiene tres datos de estado que cambian por separado: en qué etapa va, cómo va su pago y si es urgente. Si los tres se distinguen solo por color, verde «Terminada» y verde «Pagada» se confunden. Por eso cada dimensión tiene su propia forma; el color ayuda, la forma y el texto deciden.</p>'
 f'<section><h2>1 · Proceso de la muestra</h2><p class="id">Pastilla rellena. El círculo se va llenando por etapa: aunque no veas el color, sabes qué tan avanzada va.</p><div class="flujo">{flujo}</div><h3>Referencia</h3>{tabla_dim(PROCESO, "p")}</section>'
 f'<section><h2>2 · Pago</h2><p class="id">Etiqueta con contorno (no rellena) y una moneda que se llena. Cancelada y Cortesía no son grados de pago, por eso cambian de ícono.</p><div class="flujo">{"".join(etiqueta(n, ic, tx) for k, n, ic, bg, tx, *_ in PAGO)}</div><h3>Referencia</h3>{tabla_dim(PAGO, "e")}</section>'
 f'<section><h2>3 · Urgente</h2><p class="id">No es un estado sino una marca de prioridad: ficha sólida con rayo junto al folio y una franja a la izquierda de la fila. No usa rojo, que ya es «No pagada» y «Fuera de límite».</p>{uopts}</section>'
 f'<section><h2>Prueba sin color</h2><p class="id">La lista con U1 en escala de grises: proceso, pago y urgencia se siguen leyendo por forma, ícono y texto.</p><div class="gris">{lista("U1")}</div></section>'
 '<section><h2>Choques que hay que decidir</h2><ul class="ad">'
 '<li><b>Morado</b> de «Generando informe» se parece al área Bebidas (#7A5DA9), y el <b>azul cielo</b> de «En proceso» al área Aguas (#007CA3). No se confunden porque el área es un círculo y el estado una pastilla con texto, pero en la misma fila conviven.</li>'
 '<li><b>Verde y rojo</b> ya significan resultado del análisis (Conforme, Fuera de límite). Pago los repite; lo separa el contorno y la moneda.</li>'
 '<li><b>Cancelada</b>: ¿se cancela el cobro o se cancela la muestra (deja de procesarse)? Si es la muestra, va en Proceso como etapa final, no en Pago.</li></ul></section>'
 '</body></html>')
open(os.path.join(H, 'estatus.html'), 'w').write(html); print('ok')
for k, n, ic, bg, tx, *_ in PROCESO + PAGO: print(n, cr(tx, bg))
