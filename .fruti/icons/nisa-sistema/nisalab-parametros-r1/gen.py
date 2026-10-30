# NisaLab · tipos de parámetro, ronda 1: dos sistemas de marca que no usan el tono.
# A: pictograma en pocillo (cuadrado redondeado, contorno azul real). B: ficha de elemento (letras sobre azul real).
# El círculo de color queda reservado a las áreas; el color semántico, a los estados.
# Uso: python3 gen.py <carpeta-fuentes> → parametros.html
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
F = sys.argv[1] if len(sys.argv) > 1 else ''
AZ, TINTA, GRIS = '#052A76', '#141B33', '#535B70'
S = f'fill="none" stroke="{AZ}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"'
GLIFO = {
    'micro': f'<g transform="rotate(-40 20 20)"><rect x="4" y="9" width="20" height="10" rx="5" fill="{AZ}"/><rect x="16" y="22" width="20" height="10" rx="5" fill="{AZ}"/></g>',
    'fisico': f'<path d="M6 29 A14 14 0 0 1 34 29" {S}/><path d="M20 29 L27.5 17" {S}/><circle cx="20" cy="29" r="3.4" fill="{AZ}"/>',
    'metales': f'<path d="M6 33 L10.5 25 H29.5 L34 33 Z" fill="{AZ}" stroke="{AZ}" stroke-width="2" stroke-linejoin="round"/><path d="M12.5 20.5 L16 13 H24 L27.5 20.5 Z" fill="{AZ}" stroke="{AZ}" stroke-width="2" stroke-linejoin="round"/>',
    'organicos': f'<path d="M20 5 L33 12.5 V27.5 L20 35 L7 27.5 V12.5 Z" {S}/><circle cx="20" cy="20" r="6" {S}/>',
    'nutri': f'<circle cx="20" cy="20" r="14" {S}/><path d="M20 20 V6 A14 14 0 0 1 32.1 27 Z" fill="{AZ}"/>',
}
TIPOS = [  # clave, nombre, letras, confirmado por el usuario
    ('micro', 'Microbiológicos', 'Mb', True), ('fisico', 'Fisicoquímicos', 'Fq', True), ('metales', 'Metales', 'Me', True),
    ('organicos', 'Orgánicos', 'Or', False), ('nutri', 'Nutrimentales', 'Nu', False),
]
def pocillo(k, px):
    return (f'<svg width="{px}" height="{px}" viewBox="0 0 48 48" aria-hidden="true"><rect x="2" y="2" width="44" height="44" rx="11" fill="#fff" stroke="{AZ}" stroke-width="3"/>'
            f'<g transform="translate(8 8) scale(.8)">{GLIFO[k]}</g></svg>')
def ficha(l, px):
    fs = round(px * .5)
    return f'<span class="fi" style="width:{px}px;height:{px}px;font-size:{fs}px;border-radius:{max(3, round(px * .22))}px">{l}</span>'
def fila(sistema, tipo, nombre_tipo, param, area, ac, res, est, ec):
    marca = pocillo(tipo, 20) if sistema == 'A' else ficha(dict((t[0], t[2]) for t in TIPOS)[tipo], 20)
    return (f'<tr><td>{param}</td><td><span class="tp">{marca}{nombre_tipo}</span></td>'
            f'<td><span class="ar"><i style="background:{ac}"></i>{area}</span></td><td class="m">{res}</td><td><span class="st {ec}">{est}</span></td></tr>')
def tabla(s):
    rows = [('micro', 'Microbiológicos', 'Coliformes totales', 'Aguas', '#007CA3', '&lt;1.1 NMP/100 mL', 'Conforme', 'ok'),
            ('fisico', 'Fisicoquímicos', 'pH', 'Aguas', '#007CA3', '7.42', 'Conforme', 'ok'),
            ('metales', 'Metales', 'Plomo', 'Alimentos', '#A6552D', '0.031 mg/kg', 'Fuera de límite', 'er'),
            ('organicos', 'Orgánicos', 'Clorpirifos', 'Agrícolas', '#946400', 'En proceso', 'Pendiente', 'av')]
    return '<div class="tw"><table><thead><tr><th>Parámetro</th><th>Tipo</th><th>Área</th><th>Resultado</th><th>Estado</th></tr></thead><tbody>' + ''.join(fila(s, *r) for r in rows) + '</tbody></table></div>'
def sistema(s, titulo, idea):
    tarj = ''
    for k, n, l, ok in TIPOS:
        tam = ''.join((pocillo(k, px) if s == 'A' else ficha(l, px)) for px in (48, 24, 16))
        tarj += f'<div class="tj"><div class="tm">{tam}</div><b>{n}</b>{"" if ok else "<em>supuesto</em>"}</div>'
    return (f'<section><h2>{s} · {titulo}</h2><p class="id">{idea}</p><div class="tjs">{tarj}</div>'
            f'<div class="ctx"><div><h3>En la tabla de resultados</h3>{tabla(s)}</div>'
            f'<div class="gr"><h3>Prueba sin color (escala de grises)</h3>{tabla(s)}</div></div></section>')
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700)) if F else ''
ff += f"@font-face{{font-family:'IBM Plex Mono';src:url('file://{F}/IBMPlexMono.ttf')}}" if F else ''
css = ff + f'''
:root{{--az:{AZ};--tinta:{TINTA};--gris:{GRIS};--bg:#F2F4F8;--sup:#fff;--borde:#DCE1EA}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--tinta);font:400 14px/1.5 Poppins,sans-serif;padding:32px}}
h1{{font:700 26px/1.2 Poppins;margin:0 0 4px;color:var(--az)}} .lead{{color:var(--gris);margin:0 0 24px;max-width:760px}}
section{{background:var(--sup);border:1px solid var(--borde);border-radius:14px;padding:24px;margin-bottom:24px;box-shadow:0 1px 2px rgba(20,27,51,.06)}}
h2{{font:600 19px/1.3 Poppins;margin:0}} .id{{color:var(--gris);margin:4px 0 18px}} h3{{font:600 12px/1 Poppins;letter-spacing:.06em;text-transform:uppercase;color:var(--gris);margin:0 0 10px}}
.tjs{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:22px}} .tj{{border:1px solid var(--borde);border-radius:10px;padding:14px;display:flex;flex-direction:column;gap:8px}}
.tm{{display:flex;align-items:flex-end;gap:12px}} .tj em{{font-style:normal;font-size:11px;color:#8A5A00;background:#FFF4D6;border-radius:6px;padding:1px 6px;align-self:flex-start}}
.fi{{display:inline-grid;place-items:center;background:var(--az);color:#fff;font-family:Poppins;font-weight:600;letter-spacing:-.02em;flex:none}}
.ctx{{display:grid;grid-template-columns:1fr;gap:20px}} .ctx>div{{min-width:0}} .tw{{overflow-x:auto}} .gr table{{filter:grayscale(1)}}
table{{width:100%;border-collapse:collapse;font-size:13px}} th{{text-align:left;font-weight:500;color:var(--gris);background:#EEF1F6;padding:8px 10px}} td{{padding:9px 10px;border-top:1px solid var(--borde);white-space:nowrap}}
.m{{font-family:'IBM Plex Mono',monospace;font-size:12px}} .tp,.ar{{display:inline-flex;align-items:center;gap:6px}} .tp svg,.tp .fi{{flex:none}}
.ar i{{width:12px;height:12px;border-radius:50%;display:inline-block}}
.st{{font-size:12px;font-weight:500;border-radius:6px;padding:2px 8px}} .ok{{background:#E3F2E6;color:#1E6B34}} .er{{background:#FCE4E4;color:#A11D1D}} .av{{background:#FFF1CC;color:#7A5200}}
@media (max-width:900px){{.tjs{{grid-template-columns:repeat(2,1fr)}}}} @media (max-width:480px){{body{{padding:16px}}section{{padding:16px}}.tjs{{grid-template-columns:1fr}}}}
'''
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Tipos de parámetro</title><style>{css}</style><body>'
        '<h1>Tipos de parámetro · ronda 1</h1><p class="lead">Una marca por tipo para agrupar parámetros. No usa el tono: el círculo de color es del área y el color semántico es del estado. El tipo se reconoce por la forma cuadrada y su glifo o sus letras, siempre con el nombre al lado.</p>'
        + sistema('A', 'Pictograma en pocillo', 'Un dibujo por tipo dentro de un cuadrado redondeado (el pocillo de una placa), en azul real. Se entiende sin leer, si el dibujo es claro.')
        + sistema('B', 'Ficha de elemento', 'Dos letras sobre azul real, como una ficha de la tabla periódica. Se lee siempre igual a cualquier tamaño, pero hay que aprender las abreviaturas.')
        + '</body></html>')
open(os.path.join(H, 'parametros.html'), 'w').write(html)
print('ok')
