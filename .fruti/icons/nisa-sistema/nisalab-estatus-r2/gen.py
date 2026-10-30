# NisaLab · indicadores de estatus, ronda 2.
# Cambios: Cancelada sale de Pago y pasa a Proceso (aplica a una muestra o a toda la orden de análisis).
# Colores elegidos por presupuesto: cada color tiene UN dueño. Las áreas ya ocupan 8 tonos del círculo cromático
# y el resultado del análisis ocupa verde, rojo y ámbar; por eso:
#   proceso = rampa del azul real (es un orden: más oscuro = más avanzado), cancelada en gris;
#   pago = sin color, el grado lo dice la moneda (vacía, media, llena) y cortesía su regalo;
#   urgente = pera, el único color libre.
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
B16 = '<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
def etapa(n, check='#fff'):
    if n == 0: return B16 + '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75" stroke-dasharray="2.6 2.1"/></svg>'
    if n == 3: return B16 + f'<circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M4.8 8.2 7 10.4 11.2 5.9" fill="none" stroke="{check}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    arc = 'M8 8 V2.5 A5.5 5.5 0 0 1 8 13.5 Z' if n == 1 else 'M8 8 V2.5 A5.5 5.5 0 1 1 2.5 8 Z'
    return B16 + f'<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75"/><path d="{arc}" fill="currentColor"/></svg>'
def moneda(n):
    s = '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75"/>'
    if n == 1: return B16 + s + '<path d="M8 1.5 A6.5 6.5 0 0 0 8 14.5 Z" fill="currentColor"/></svg>'
    if n == 2: s = '<circle cx="8" cy="8" r="7.5" fill="currentColor"/>'
    sg = '#fff' if n == 2 else 'currentColor'
    return B16 + s + f'<path d="M10 5.6 H7.1 a1.3 1.3 0 0 0 0 2.6 h1.8 a1.3 1.3 0 0 1 0 2.6 H6 M8 4.2 v7.6" fill="none" stroke="{sg}" stroke-width="1.3" stroke-linecap="round"/></svg>'
AZ, TINTA = '#052A76', '#141B33'
# clave, nombre, ícono, fondo, texto, borde, cuándo
PROCESO = [
    ('no-ingresada', 'No ingresada', etapa(0), '#FFFFFF', '#344054', '1.5px dashed #858DA3', 'Recibida en ventanilla, sin folio interno.'),
    ('en-proceso', 'En proceso', etapa(1), '#E8EDF7', AZ, '1.5px solid #E8EDF7', 'Se le asignó folio interno de laboratorio.'),
    ('generando-informe', 'Generando informe', etapa(2), '#C7D3EE', AZ, '1.5px solid #C7D3EE', 'Todos los parámetros requeridos capturados.'),
    ('terminada', 'Terminada', etapa(3, AZ), AZ, '#FFFFFF', f'1.5px solid {AZ}', 'Informe generado y enviado.'),
    ('cancelada', 'Cancelada', lucide('ban'), '#EEF1F6', '#475467', '1.5px solid #EEF1F6', 'Se canceló la muestra o toda su orden. Etapa final: no avanza más.'),
]
PAGO = [
    ('no-pagada', 'No pagada', moneda(0), 'Sin pagos registrados.'),
    ('parcial', 'Pago parcial', moneda(1), 'Pagó una parte; queda saldo.'),
    ('pagada', 'Pagada', moneda(2), 'Saldo en cero.'),
    ('cortesia', 'Cortesía', lucide('gift'), 'Se procesa sin cobro, por decisión del laboratorio.'),
]
P = {k: v for k, *v in PROCESO}; G = {k: v for k, *v in PAGO}
def pastilla(k):
    n, ic, bg, tx, bd, _ = P[k]
    return f'<span class="ps{" tc" if k == "cancelada" else ""}" style="background:{bg};color:{tx};border:{bd}">{ic}{n}</span>'
def etiqueta(k):
    n, ic, _ = G[k]; return f'<span class="et{" deuda" if k == "no-pagada" else ""}">{ic}{n}</span>'
def urgente(): return f'<span class="ur">{lucide("zap")}Urgente</span>'
ORDENES = [
    ('OA-2610-031', 'Hotel Las Palmas', None, [('AG-2610-0147', 'Aguas', '#007CA3', 'en-proceso', 'pagada', True), ('AG-2610-0148', 'Aguas', '#007CA3', 'generando-informe', 'pagada', True), ('AG-2610-0149', 'Aguas', '#007CA3', 'cancelada', 'pagada', False)]),
    ('OA-2610-032', 'Destilería Santa Fe', None, [('BE-2610-0088', 'Bebidas alcohólicas', '#7A5DA9', 'no-ingresada', 'parcial', False), ('AL-2610-0152', 'Alimentos', '#A6552D', 'terminada', 'cortesia', False)]),
    ('OA-2610-029', 'Purificadora El Manantial', 'cancelada', [('AG-2610-0139', 'Aguas', '#007CA3', 'cancelada', 'no-pagada', False), ('AG-2610-0140', 'Aguas', '#007CA3', 'cancelada', 'no-pagada', False)]),
]
def lista():
    r = ''
    for oa, cli, est, ms in ORDENES:
        canc = sum(1 for m in ms if m[3] == 'cancelada')
        res = pastilla('cancelada') if est == 'cancelada' else (f'<span class="nota">{canc} de {len(ms)} muestras cancelada{"s" if canc > 1 else ""}</span>' if canc else '')
        r += f'<tr class="oa"><th colspan="5" scope="rowgroup"><span class="m">{oa}</span> · {cli} · {len(ms)} muestras {res}</th></tr>'
        for fol, a, ac, p, g, urg in ms:
            r += (f'<tr class="{"urg " if urg else ""}{"off" if p == "cancelada" else ""}"><td class="m fol">{fol}</td><td>{urgente() if urg else ""}</td><td><span class="ar"><i style="background:{ac}"></i>{a}</span></td>'
                  f'<td>{pastilla(p)}</td><td>{etiqueta(g)}</td></tr>')
    return f'<div class="tw"><table class="ls"><thead><tr><th>Folio</th><th><span class="vh">Prioridad</span></th><th>Área</th><th>Proceso</th><th>Pago</th></tr></thead><tbody>{r}</tbody></table></div>'
def ref_p():
    rows = ''.join(f'<tr><td>{pastilla(k)}</td><td>{c}</td><td class="m">{tx} / {bg} · {cr(tx, bg)}:1</td></tr>' for k, n, ic, bg, tx, bd, c in PROCESO)
    return f'<div class="tw"><table class="ref"><thead><tr><th>Indicador</th><th>Cuándo</th><th>Texto / fondo · contraste</th></tr></thead><tbody>{rows}</tbody></table></div>'
def ref_g():
    rows = ''.join(f'<tr><td>{etiqueta(k)}</td><td>{c}</td><td class="m">{TINTA} / #FFFFFF · {cr(TINTA, "#FFFFFF")}:1</td></tr>' for k, n, ic, c in PAGO)
    return f'<div class="tw"><table class="ref"><thead><tr><th>Indicador</th><th>Cuándo</th><th>Texto / fondo · contraste</th></tr></thead><tbody>{rows}</tbody></table></div>'
AREAS = [('Aguas', '#007CA3'), ('Agrícolas', '#946400'), ('Ambiental', '#2F8247'), ('Alimentos', '#A6552D'), ('Bebidas', '#7A5DA9'), ('Agave', '#008478'), ('Farmacia', '#A14E78'), ('Consultoría', '#4C6BB4')]
def dueño(t, sw): return f'<div class="du"><b>{t}</b><div class="sws">{sw}</div></div>'
sw = lambda c, n: f'<span class="sw"><i style="background:{c}"></i>{n}</span>'
pres = (dueño('Áreas · círculo sólido', ''.join(sw(c, n) for n, c in AREAS))
        + dueño('Resultado del análisis · pastilla', sw('#2E7D32', 'Conforme') + sw('#B42318', 'Fuera de límite') + sw('#E9B10A', 'Alerta'))
        + dueño('Proceso · rampa del azul real', ''.join(sw(c, n) for c, n in (('#FFFFFF', 'No ingresada'), ('#E8EDF7', 'En proceso'), ('#C7D3EE', 'Generando informe'), (AZ, 'Terminada'), ('#EEF1F6', 'Cancelada'))))
        + dueño('Pago · sin color', sw('#FFFFFF', 'contorno tinta + moneda'))
        + dueño('Urgente · pera', sw('#C2D225', 'Urgente')))
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700)) + f"@font-face{{font-family:'IBM Plex Mono';src:url('file://{F}/IBMPlexMono.ttf')}}"
css = ff + f'''
:root{{--az:{AZ};--tinta:{TINTA};--gris:#535B70;--borde:#DFE3EC}}
*{{box-sizing:border-box}}body{{margin:0;background:#E6E9F0;color:var(--tinta);font:400 14px/1.5 Poppins,sans-serif;padding:32px}}
h1{{font:700 26px/1.2 Poppins;color:var(--az);margin:0 0 4px}}.lead{{color:var(--gris);max-width:880px;margin:0 0 24px}}
section{{background:#fff;border-radius:14px;padding:24px;margin-bottom:20px;box-shadow:0 1px 2px rgba(20,27,51,.06)}}
h2{{font:600 19px/1.3 Poppins;margin:0}}.id{{color:var(--gris);margin:4px 0 16px;max-width:920px}}
h3{{font:600 11px/1 Poppins;letter-spacing:.06em;text-transform:uppercase;color:var(--gris);margin:18px 0 10px}}
.ps,.et,.ur{{display:inline-flex;align-items:center;gap:6px;font:500 13px/18px Poppins;white-space:nowrap}}
.ps{{border-radius:999px;padding:2px 10px 2px 7px}}.et{{border:1.5px solid #858DA3;color:var(--tinta);border-radius:6px;padding:2px 8px 2px 6px;background:#fff}}.et.deuda{{font-weight:600;border-color:var(--tinta)}}
.ur{{font-weight:600;border-radius:6px;padding:3px 8px 3px 6px;background:#C2D225;color:var(--az)}}
.flujo{{display:flex;align-items:center;gap:8px;flex-wrap:wrap}}.flujo b{{color:var(--gris);font-weight:400}}
.tw{{overflow-x:auto}}table{{width:100%;border-collapse:collapse;font-size:13px}}th{{text-align:left;font-weight:500;color:var(--gris);background:#EEF1F6;padding:8px 10px}}td{{padding:9px 10px;border-top:1px solid var(--borde)}}
.ref td:nth-child(2){{color:var(--gris)}}.m{{font-family:'IBM Plex Mono',monospace;font-size:12px}}
.ls td{{white-space:nowrap}}.ls tr.urg td:first-child{{box-shadow:inset 4px 0 0 #C2D225}}.fol{{font-weight:600}}.ls tr.off td{{color:#646B80}}.ls tr.off .fol{{text-decoration:line-through}}
.ls tr.oa th{{background:#fff;color:var(--tinta);font-weight:600;border-top:1px solid #CDD3DF;padding-top:14px;white-space:nowrap}}.ls tr.oa th .ps{{margin-left:8px}}
tr.off .et.deuda{{font-weight:500;border-color:#858DA3}}.nota{{font-weight:400;color:var(--gris);margin-left:8px}}
.ar{{display:inline-flex;align-items:center;gap:6px}}.ar i{{width:12px;height:12px;border-radius:50%;display:inline-block}}
.du{{display:grid;grid-template-columns:240px 1fr;gap:12px;padding:10px 0;border-top:1px solid var(--borde);align-items:center}}.sws{{display:flex;flex-wrap:wrap;gap:6px 14px}}
.sw{{display:inline-flex;align-items:center;gap:6px;font-size:13px}}.sw i{{width:16px;height:16px;border-radius:4px;display:inline-block;box-shadow:inset 0 0 0 1px rgba(20,27,51,.18)}}
.gris{{filter:grayscale(1)}}.reg{{margin:0;padding-left:20px}}.reg li{{margin:4px 0}}
.vh{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
@media (max-width:700px){{.du{{grid-template-columns:1fr}}}}@media (max-width:480px){{body{{padding:12px}}section{{padding:16px}}}}
'''
flujo = '<b>→</b>'.join(pastilla(k) for k in ('no-ingresada', 'en-proceso', 'generando-informe', 'terminada')) + '<b>·</b>' + pastilla('cancelada')
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Indicadores de estatus</title><style>{css}</style><body>'
 '<h1>Indicadores de estatus · ronda 2</h1><p class="lead">Cada color tiene un solo dueño. Las ocho áreas ya ocupan casi todo el círculo cromático y el resultado del análisis ya usa verde, rojo y ámbar. Si el proceso y el pago también usaran tonos, alguno chocaría siempre. Por eso el proceso usa un solo tono que se oscurece al avanzar, el pago no usa color y la urgencia usa el único color libre.</p>'
 f'<section><h2>Quién es dueño de cada color</h2><p class="id">Regla: un color nuevo solo entra si su dueño no existe ya en esta lista.</p>{pres}</section>'
 f'<section><h2>1 · Proceso de la muestra</h2><p class="id">Es un orden (va de una etapa a la siguiente), así que se codifica con claridad, no con tonos: más oscuro = más avanzado, y el círculo se llena. Cancelada sale del orden: gris, ícono de prohibido y el folio tachado en la lista.</p><div class="flujo">{flujo}</div><h3>Referencia</h3>{ref_p()}</section>'
 f'<section><h2>2 · Pago</h2><p class="id">Sin color: contorno en tinta y una moneda que se llena. «No pagada» va en negritas y con contorno más oscuro porque es lo único que pide acción. Cortesía usa su regalo.</p><div class="flujo">{"".join(etiqueta(k) for k, *_ in PAGO)}</div><h3>Referencia</h3>{ref_g()}</section>'
 f'<section><h2>3 · Urgente</h2><p class="id">Ficha pera con rayo junto al folio y franja pera a la izquierda de la fila. Texto azul real sobre pera: 7.8:1.</p><div class="flujo">{urgente()}</div></section>'
 f'<section><h2>En la lista, agrupada por orden de análisis</h2><p class="id">Si se cancela toda la orden, la orden lleva la pastilla Cancelada y todas sus muestras también. Si se cancela una muestra, la orden dice «1 de 3 muestras cancelada» y sigue su curso.</p>{lista()}<h3>Sin color</h3><div class="gris">{lista()}</div></section>'
 '<section><h2>Reglas</h2><ol class="reg"><li>Proceso, pago y urgencia nunca comparten forma: pastilla, etiqueta con contorno y ficha sólida.</li><li>Ningún estado usa el tono de un área ni el verde, rojo o ámbar del resultado.</li><li>Siempre ícono + texto; el color nunca es la única señal.</li><li>En una muestra cancelada, «No pagada» pierde el énfasis: ya no pide cobrar (incógnita: ¿qué pasa con lo ya pagado, se reembolsa?).</li><li>Cancelada es final: no se regresa a otra etapa sin reabrir la orden (incógnita: ¿se puede reabrir?).</li></ol></section>'
 '</body></html>')
open(os.path.join(H, 'estatus.html'), 'w').write(html); print('ok')
