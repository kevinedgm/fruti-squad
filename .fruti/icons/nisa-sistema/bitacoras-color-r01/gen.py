# Bitácoras · propuesta de color r01. Uso: python3 gen.py → propuesta.html
# Insumo: CSS de producción de bitácoras que pegó el usuario (no se guarda en el repo; aquí solo el inventario de valores).
# Base normativa: design system NisaLab v3 (../nabi-design-system/tokens.json). Es PROPUESTA: no cambia tokens.json hasta aprobarse.
import os, html
D = os.path.dirname(os.path.abspath(__file__))
e = html.escape

def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + .05) / (lb + .05)
def crt(a, b): return f'{cr(a, b):.1f}:1'

# ---------- Inventario: variantes encontradas por concepto (hechos, leídos del CSS)
VAR = [
 ('Éxito / completo', ['#52660a', '#1a7a4a', '#16803a', '#166534', '#28a745', '#25a868', '#156040', '#3d7a2a']),
 ('Error / rechazo', ['#c43b26', '#c42b1c', '#b42318', '#dc2626', '#dc3545', '#e04030', '#b91c1c', '#9f1d2c', '#912018', '#9d2f1e', '#7e1f2a']),
 ('Advertencia / destiempo', ['#9a6400', '#9a5f00', '#92400e', '#b45309', '#d08820', '#c99722', '#c08820', '#704600']),
 ('Azul de marca y sus tonos', ['#052a76', '#041d55', '#03193d', '#020f26', '#0a3aa0', '#073dab', '#3058b0', '#3d67ae', '#24366b', '#1f4765', '#1e40af']),
 ('Texto principal', ['#0d1526', '#111827', '#18181a', '#0f1f2e', '#122845']),
 ('Texto secundario', ['#5b6478', '#52606d', '#587083', '#5b6577', '#69758b', '#516174', '#59647a', '#697386', '#667085', '#6b7280']),
 ('Fondos claros', ['#dde3ec', '#f2f4f7', '#f4f8fb', '#f8fafd', '#f8fafc', '#fafbfe', '#fafbfd', '#fbfcfe', '#f6f8fb', '#f2f5fa', '#eef2f6', '#eef4fa', '#f1f3f7', '#f6f6fc']),
]
def chip(h): return f'<span class="vc" style="background:{h}" title="{h}"></span>'
INV = ''.join(f'<div class="inv"><b>{n}</b><span class="vcs">{"".join(chip(h) for h in hs)}</span><span class="n">{len(hs)} valores</span></div>' for n, hs in VAR)

FALLAS = [
 ('Borde de campos y buscador', '#d5dce8', '#ffffff', 3.0, 'El contorno es lo que dice «aquí se escribe» (WCAG 1.4.11).'),
 ('Borde de campos (capa anterior)', '#9eacba', '#ffffff', 3.0, 'Tampoco llega.'),
 ('Encabezado de lista de resultados', '#69758b', '#f6f8fb', 4.5, 'Texto de 9 px en mayúsculas.'),
 ('Botón Validar con errores (fin del degradado)', '#ffffff', '#e04030', 4.5, 'El texto cae sobre la parte clara.'),
 ('Botón Validar correcto (fin del degradado)', '#ffffff', '#25a868', 4.5, 'Blanco sobre verde claro.'),
 ('Consola: etapa del registro', '#64748b', '#0f172a', 4.5, 'Texto gris sobre fondo oscuro.'),
]
FALLAS_T = ''.join(f'<tr><td>{n}</td><td><span class="pair" style="background:{b};color:{a};border-color:{a if a != "#ffffff" else b}">Aa</span> <code>{a}</code> / <code>{b}</code></td>'
                   f'<td class="num bad">{crt(a, b)}</td><td class="num">{m}:1</td><td>{t}</td></tr>' for n, a, b, m, t in FALLAS)

# ---------- Propuesta: tokens (nombre, valor, uso, reemplaza)
P = {
 'primary': '#052A76', 'primary-hover': '#021C52', 'primary-ink': '#041D55', 'primary-soft': '#E8EDF7', 'primary-line': '#C3CFE6',
 'pera': '#C2D225', 'pera-soft': '#F2F6CF',
 'bg': '#F2F4F8', 'surface': '#FFFFFF', 'surface-2': '#F7F9FC', 'surface-sunken': '#EEF1F6',
 'text': '#141B33', 'text-muted': '#535B70', 'text-subtle': '#646B80',
 'border': '#DFE3EC', 'border-strong': '#CDD3DF', 'border-control': '#858DA3',
 'conforme': '#2E7D32', 'conforme-soft': '#E3F1E4', 'on-conforme-soft': '#1E5A22', 'conforme-line': '#A8D1AB',
 'alerta': '#8A6100', 'alerta-soft': '#FBF0CC', 'on-alerta-soft': '#664700', 'alerta-line': '#E3C567', 'alerta-fill': '#E9B10A',
 'fuera': '#B42318', 'fuera-hover': '#8A1A12', 'fuera-soft': '#FDE7E5', 'on-fuera-soft': '#8A1A12', 'fuera-line': '#F0B4AD',
 'pendiente': '#475467', 'pendiente-soft': '#E4E8F0', 'on-pendiente-soft': '#344054',
 'log-bg': '#0E1630', 'log-panel': '#1A2440', 'log-text': '#CBD5E1', 'log-muted': '#94A3B8', 'log-info': '#93C5FD', 'log-warn': '#FDE68A', 'log-err': '#FCA5A5',
}
G = [
 ('Marca', 'El azul ordena; el pera es una sola cosa por pantalla.', [
  ('primary', 'surface', 'Acción principal, enlaces, foco, folio activo.', '#052a76 (5 nombres de variable)'),
  ('primary-hover', 'surface', 'Hover y presionado: más oscuro, no más claro.', '#0a3aa0, #073dab, #03193d'),
  ('primary-ink', None, 'Fin del degradado del encabezado y de los modales.', '#041d55, #020f26'),
  ('primary-soft', None, 'Selección, unidad de medida, reapertura, chips azules.', '#eef2fb, #e6ecf7, #e9f0fb, #dbe6f8'),
  ('primary-line', None, 'Borde de los chips azules.', '#c0d0e8, #c8d3e7, #bfd4e4'),
  ('pera', None, 'Célula del símbolo, selección de texto, «Urgente», registro en curso.', '#c2d225, #c1d324'),
  ('pera-soft', None, 'Fondo del registro que se está capturando.', '#f2f8e0 (hoy usado para «completo»)')]),
 ('Lienzo, texto y bordes', 'Tres niveles de texto y tres de borde. El borde de control es el único que debe medir 3:1.', [
  ('bg', None, 'Fondo de la página.', '#dde3ec, #f2f4f7, #f4f8fb'),
  ('surface', None, 'Tarjetas, tablas, campos.', '#ffffff'),
  ('surface-2', None, 'Encabezado de panel y filas alternas.', '#f8fafd, #f8fafc, #fafbfe, #fafbfd, #fbfcfe, #f6f8fb'),
  ('surface-sunken', None, 'Encabezado de tabla, deshabilitado y solo lectura.', '#f2f5fa, #eef2f6, #eef4fa, #f1f3f7, #f6f6fc'),
  ('text', 'surface', 'Texto principal y valores.', '#0d1526, #111827, #18181a, #0f1f2e, #122845, #2b3346'),
  ('text-muted', 'surface-2', 'Etiquetas, encabezados de columna, ayudas.', '#5b6478, #52606d, #587083, #69758b, #516174'),
  ('text-subtle', 'surface', 'Placeholders, hora, metadatos.', '#59647a, #697386, #667085, #6b7280'),
  ('border', None, 'Separa filas y tarjetas (decorativo).', '#e6ebf3, #e6e9ef, #e2e8f0, #dfe4ee, #eef1f7'),
  ('border-strong', None, 'Divisores sobre fondo hundido.', '#d5dce8 en divisores, #c5cfda, #d8dee8'),
  ('border-control', 'surface', 'Contorno de campos, buscador y casillas.', '#d5dce8 y #9eacba en campos (fallan)')]),
 ('Estado del resultado', 'Un color por significado, siempre con icono y texto. Cada uno con fondo, texto y borde.', [
  ('conforme', 'surface', 'Conforme, completo, firmado.', '#52660a, #1a7a4a, #16803a, #166534, #28a745, #25a868, #3d7a2a'),
  ('conforme-soft', None, 'Fondo de pastilla y de folio completo.', '#f2f8e0, #e8f5ee, #eefbf1, #f0fff4'),
  ('on-conforme-soft', 'conforme-soft', 'Texto sobre el fondo conforme.', ''),
  ('alerta', 'surface', 'Pendiente de firma, destiempo, fuera de tendencia.', '#9a6400, #9a5f00, #92400e, #b45309, #d08820'),
  ('alerta-soft', None, 'Fondo de alerta.', '#fff8e8, #fff5e0, #ffedd5'),
  ('on-alerta-soft', 'alerta-soft', 'Texto sobre el fondo de alerta.', ''),
  ('fuera', 'surface', 'Rechazo, fuera de especificación, botón destructivo.', '#c43b26, #c42b1c, #dc2626, #dc3545, #e04030, #b91c1c'),
  ('fuera-soft', None, 'Fondo de rechazo.', '#fef3f1, #fde8e6, #fee2e2, #fff5f5, #fff7f8'),
  ('on-fuera-soft', 'fuera-soft', 'Texto sobre el fondo de rechazo.', ''),
  ('pendiente', 'surface', 'Sin capturar, en espera. No compite con el azul.', '(no existe: hoy se usa el ámbar)')]),
 ('Consola de importación de PDF', 'Único bloque oscuro. Se tiñe de azul para que pertenezca a la marca.', [
  ('log-bg', None, 'Fondo de la consola.', '#0f172a'),
  ('log-panel', None, 'Detalle y etiquetas de nivel.', '#1e293b, #1e40af, #92400e, #7f1d1d'),
  ('log-text', 'log-bg', 'Texto del registro.', '#cbd5e1'),
  ('log-muted', 'log-bg', 'Etapa y depuración.', '#64748b (falla), #94a3b8'),
  ('log-info', 'log-panel', 'Nivel INFO.', '#bfdbfe, #7dd3fc'),
  ('log-warn', 'log-panel', 'Nivel WARN.', '#fde68a'),
  ('log-err', 'log-panel', 'Nivel ERROR.', '#fca5a5')]),
]
def sw(n, sobre, uso, rem):
    v = P[n]; osc = lum(v) < .3
    ra = f'{crt(v, P[sobre])} sobre {sobre}' if sobre else (f'Texto encima {crt(P["text"], v)}' if not osc else f'Blanco encima {crt("#FFFFFF", v)}')
    if n == 'pera': ra = f'Sobre azul {crt(v, P["primary"])} · nunca texto sobre blanco'
    if n == 'log-bg' or n == 'log-panel': ra = f'Texto de consola encima {crt(P["log-text"], v)}'
    return (f'<figure class="sw"><span class="chip" style="background:{v};color:{"#fff" if osc else P["text"]}"><b>{n}</b><code>{v}</code></span>'
            f'<figcaption>{uso}<span class="ra">{ra}</span>{f"<span class=rem>Reemplaza: {rem}</span>" if rem else ""}</figcaption></figure>')
PROP = ''.join(f'<div class="grupo"><h3>{t}</h3><p class="pie">{d}</p><div class="sws">{"".join(sw(*x) for x in xs)}</div></div>' for t, d, xs in G)

# ---------- Muestras: el mismo marcado con dos juegos de variables
A = dict(primary='#052a76', hover='#0a3aa0', soft='#eef2fb', line='#c0d0e8', ink='#041d55', pera='#c2d225', perasoft='#f2f8e0', peraink='#52660a',
         bg='#dde3ec', surf='#ffffff', surf2='#f8fafd', sunk='#f2f5fa', text='#0d1526', muted='#5b6478', subtle='#697386', head='#69758b',
         border='#e6ebf3', ctrl='#d5dce8', ro='#f6f6fc', roline='#d8d8ee', ok='#52660a', okbg='#f2f8e0', okline='#cbd88a', okbtn='#111827',
         warn='#9a6400', warnbg='#fff8e8', warnline='#e5c46d', err='#c43b26', errbg='#fef3f1', errline='#e9aaa0', danger='#dc2626',
         countbg='#f2f8e0', counttx='#52660a', countline='#d4de8f', logbg='#0f172a', logpanel='#1e293b', logtx='#cbd5e1', logmuted='#64748b',
         loginfo='#bfdbfe', loginfobg='#1e40af', logwarn='#fde68a', logwarnbg='#92400e', logerr='#fca5a5', logerrbg='#7f1d1d',
         val1='#052a76', val2='#0a3aa0', valok1='#1a7a4a', valok2='#25a868')
B = dict(primary=P['primary'], hover=P['primary-hover'], soft=P['primary-soft'], line=P['primary-line'], ink=P['primary-ink'], pera=P['pera'], perasoft=P['pera-soft'], peraink=P['primary'],
         bg=P['bg'], surf=P['surface'], surf2=P['surface-2'], sunk=P['surface-sunken'], text=P['text'], muted=P['text-muted'], subtle=P['text-subtle'], head=P['text-muted'],
         border=P['border'], ctrl=P['border-control'], ro=P['surface-sunken'], roline=P['border-strong'], ok=P['on-conforme-soft'], okbg=P['conforme-soft'], okline=P['conforme-line'], okbtn=P['primary'],
         warn=P['on-alerta-soft'], warnbg=P['alerta-soft'], warnline=P['alerta-line'], err=P['on-fuera-soft'], errbg=P['fuera-soft'], errline=P['fuera-line'], danger=P['fuera'],
         countbg=P['primary-soft'], counttx=P['primary'], countline=P['primary-line'], logbg=P['log-bg'], logpanel=P['log-panel'], logtx=P['log-text'], logmuted=P['log-muted'],
         loginfo=P['log-info'], loginfobg=P['log-panel'], logwarn=P['log-warn'], logwarnbg=P['log-panel'], logerr=P['log-err'], logerrbg=P['log-panel'],
         val1=P['primary'], val2=P['primary'], valok1=P['primary'], valok2=P['primary'])
vars_ = lambda d: ';'.join(f'--{k}:{v}' for k, v in d.items())

I = {  # iconos de trazo simples
 'ok': '<svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true"><path d="M3.5 8.5l3 3 6-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'x': '<svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
 'warn': '<svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true"><path d="M8 2l6.5 11.5h-13z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M8 6.5v3M8 11.6v.1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
 'lock': '<svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true"><rect x="3.5" y="7" width="9" height="6.5" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M5.5 7V5a2.5 2.5 0 015 0v2" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>',
}
def muestra(modo):
    d = A if modo == 'a' else B
    titulo = 'Actual' if modo == 'a' else 'Propuesta'
    validar = ('<span class="b val" style="background:linear-gradient(135deg,var(--valok1),var(--valok2))">Validado</span>' if modo == 'a'
               else '<span class="b val">Validar bitácora</span>')
    aprobar = '<span class="b okbtn">Aprobar</span>'
    botones = (f'<span class="b pri">Guardar</span><span class="b sec">Cancelar</span>{validar}{aprobar}<span class="b dng">Eliminar</span>' if modo == 'a' else
               f'{validar}<span class="b sec">Guardar</span><span class="b sec">Cancelar</span><span class="b dng" style="margin-left:auto">Eliminar</span><span class="pie" style="flex-basis:100%">Aprobar va en la vista del supervisor; ahí es la única primaria.</span>')
    return f'''<div class="lado {'actual' if modo == 'a' else 'nueva'}" style="{vars_(d)}"><span class="lt">{titulo}</span>
<div class="m"><div class="mh"><b>Folios del día</b><span class="count">12 folios</span></div>
<div class="fol"><span class="fb ok"><b>AG-0147</b><small>Completo</small></span><span class="fb pend"><b>AG-0148</b><small>Pendiente</small></span><span class="fb act"><b>AG-0149</b><small>Abierto</small></span><span class="fb ok"><b>AG-0150</b><small>Completo</small></span></div></div>
<div class="m"><div class="lh"><span>Parámetro</span><span>Resultado</span><span></span></div>
<div class="ri"><span><b>Alcohol vol. a 20 °C</b><span class="pill ok">{I['ok']}Conforme</span></span><span class="v">38.4 <small>% Alc. Vol.</small></span><span class="b pri sm">Abrir</span></div>
<div class="ri"><span><b>Metanol</b><span class="pill err">{I['x']}Fuera de especificación</span></span><span class="v">312 <small>mg/100 mL A.A.</small></span><span class="b pri sm">Abrir</span></div>
<div class="ri"><span><b>Extracto seco</b><span class="pill warn">{I['warn']}Firma pendiente</span></span><span class="v">0.84 <small>g/L</small></span><span class="b pri sm">Abrir</span></div></div>
<div class="m"><label class="fl">Peso de la cápsula</label><span class="campo"><span class="in">42.3175</span><span class="u">g</span></span>
<label class="fl">Temperatura (solo lectura)</label><span class="campo ro"><span class="lk">{I['lock']}</span><span class="in">20.0</span><span class="u">°C</span></span></div>
<div class="m"><div class="al err"><b>Rechazada por el validador</b><span>El duplicado difiere 0.6 %; el método admite 0.3 %. Repite la lectura 2.</span></div>
<div class="al pri"><b>Reabierta por supervisión</b><span>Corrige la temperatura y vuelve a validar.</span></div>
<div class="al warn"><b>Captura a destiempo</b><span>Se registró 26 h después del análisis.</span></div></div>
<div class="m"><div class="btns">{botones}</div></div>
<div class="m log"><div class="lr"><span class="lb info">INFO</span><span class="le">LECTURA</span><span>PDF recibido, 3 páginas.</span></div>
<div class="lr"><span class="lb warn">WARN</span><span class="le">TABLAS</span><span>Columna «LC» vacía en la página 2.</span></div>
<div class="lr"><span class="lb err">ERROR</span><span class="le">VALIDACIÓN</span><span>Metanol fuera de intervalo.</span></div></div>
</div>'''
MUESTRAS = muestra('a') + muestra('b')

# ---------- Capa de compatibilidad (va al FINAL del archivo, para ganar a las capas anteriores)
ALIAS = [
 ('--navy', 'primary'), ('--navy-deep', 'primary-ink'), ('--navy-mid', 'primary-hover'), ('--navy-lt', 'primary-soft'),
 ('--lime', 'pera'), ('--lime-soft', 'pera-soft'), ('--lime-ink', 'text'),
 ('--surf', 'surface'), ('--surf-2', 'surface-2'), ('--surf-3', 'surface-sunken'), ('--surf-4', 'border'), ('--page-bg', 'bg'),
 ('--bdr', 'border'), ('--bdr-2', 'border-control'), ('--bdr-3', 'text-subtle'),
 ('--tx', 'text'), ('--tx-2', 'text'), ('--tx-3', 'text-muted'), ('--tx-4', 'text-subtle'), ('--placeholder', 'text-subtle'),
 ('--ok', 'on-conforme-soft'), ('--ok-bg', 'conforme-soft'), ('--ok-bdr', 'conforme-line'),
 ('--warn', 'on-alerta-soft'), ('--warn-bg', 'alerta-soft'), ('--warn-bdr', 'alerta-line'),
 ('--err', 'fuera'), ('--err-bg', 'fuera-soft'), ('--err-bdr', 'fuera-line'),
 ('--dis-bg', 'surface-sunken'), ('--dis-bdr', 'border-strong'), ('--dis-tx', 'text-subtle'),
 ('--nn-bit-navy', 'primary'), ('--nn-bit-navy-lt', 'primary-soft'), ('--nn-bit-navy-mid', 'primary-hover'),
 ('--nn-bit-bg', 'bg'), ('--nn-bit-surf', 'surface'), ('--nn-bit-surf-2', 'surface-2'), ('--nn-bit-surf-3', 'surface-sunken'), ('--nn-bit-surf-4', 'border'),
 ('--nn-bit-bdr', 'border'), ('--nn-bit-bdr-2', 'border-control'), ('--nn-bit-bdr-3', 'text-subtle'),
 ('--nn-bit-tx', 'text'), ('--nn-bit-tx-2', 'text'), ('--nn-bit-tx-3', 'text-muted'), ('--nn-bit-tx-4', 'text-subtle'),
 ('--nn-bit-ok', 'on-conforme-soft'), ('--nn-bit-ok-bg', 'conforme-soft'), ('--nn-bit-ok-bdr', 'conforme-line'),
 ('--nn-bit-warn', 'on-alerta-soft'), ('--nn-bit-warn-bg', 'alerta-soft'), ('--nn-bit-warn-bdr', 'alerta-line'),
 ('--nn-bit-err', 'fuera'), ('--nn-bit-err-bg', 'fuera-soft'), ('--nn-bit-err-bdr', 'fuera-line'),
 ('--nn-bit-dis-bg', 'surface-sunken'), ('--nn-bit-dis-bdr', 'border-strong'), ('--nn-bit-dis-tx', 'text-subtle'),
 ('--v3-ink', 'text'), ('--v3-muted', 'text-muted'), ('--v3-border', 'border'), ('--v3-navy', 'primary'),
 ('--nn-primary-light', 'primary-hover'), ('--nn-primary-dark', 'primary-hover'), ('--nn-primary-darker', 'primary-ink'), ('--nn-secondary', 'pera'),
 ('--nn-text-light', 'text-muted'), ('--nn-bg-alt', 'surface-2'),
 ('--nn-color-text-muted', 'text-muted'), ('--nn-color-success-dark', 'on-conforme-soft'), ('--nn-color-warning-dark', 'on-alerta-soft'), ('--nn-color-error-dark', 'fuera'), ('--nn-color-info-dark', 'primary'),
 ('--info', 'primary'), ('--info-bg', 'primary-soft'), ('--info-bdr', 'primary-line'),
 ('--nn-color-success-soft', 'conforme-soft'), ('--nn-color-warning-soft', 'alerta-soft'), ('--nn-color-error-soft', 'fuera-soft'), ('--nn-color-info-soft', 'primary-soft'),
]
CSS_PROP = ('/* NisaLab · bitácoras · capa de color única (aprobada 2026-11-05). Pegar AL FINAL del archivo. */\n.bitacoras-page-wrap,\n.bit-history-layer,\n.bit-history-control {\n'
            + ''.join(f'  --nn-{k}: {v};\n' for k, v in P.items())
            + '  /* Compatibilidad: los nombres viejos apuntan a la capa nueva */\n'
            + ''.join(f'  {a}: var(--nn-{b});\n' for a, b in ALIAS)
            + '  --focus-ring: 0 0 0 3px rgba(5, 42, 118, 0.18);\n  --nn-bit-focus: var(--focus-ring);\n}\n'
            + '.bitacoras-page-wrap ::selection { background: var(--nn-pera); color: var(--nn-primary); }\n')

LITERALES = [('#c0d0e8 (borde de chips azules)', 'var(--nn-primary-line)', '≈ 14 reglas'), ('#dc2626 / #b91c1c (botón eliminar)', 'var(--nn-fuera) / var(--nn-fuera-hover)', '4 reglas'),
             ('#f6f6fc, #d8d8ee, #eeeef8, #8080b0 (solo lectura lila)', 'var(--nn-sunken), var(--nn-border-strong), var(--nn-text-subtle)', '8 reglas'),
             ('#111827 (botón success negro)', 'var(--nn-primary)', '2 reglas'), ('#073dab, #156040 (hovers)', 'var(--nn-primary-hover)', '3 reglas'),
             ('Degradados de .btn-validate', 'Color sólido; el estado lo dicen icono y texto', '3 reglas'),
             ('Colores fijos de .nn-gc-*, .nn-gl-table, .pdf-dropzone', 'var(--nn-conforme-*), var(--nn-fuera-*)', '≈ 10 reglas'),
             ('Bloque .bit-history-* (fuera del contenedor)', 'Mover dentro de .bitacoras-page-wrap o declarar las variables en :root', '≈ 30 valores')]
LIT_T = ''.join(f'<tr><td><code>{a}</code></td><td><code>{b}</code></td><td>{c}</td></tr>' for a, b, c in LITERALES)

CSS = r'''
/* Propuesta de color: lectura vertical; muestras lado a lado (actual | propuesta) desde 1024 px. Tema claro único, como el sistema. */
:root{--bg:#F2F4F8;--surface:#fff;--text:#141B33;--muted:#535B70;--border:#DFE3EC;--primary:#052A76;--pera:#C2D225;--bad:#B42318;
--sans:"Poppins",system-ui,sans-serif;--mono:"Google Sans Code","IBM Plex Mono",ui-monospace,monospace;color-scheme:light}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 var(--sans)}
h1,h2,h3{margin:0;text-wrap:balance}p{margin:0}code,.num{font:500 12.5px var(--mono);overflow-wrap:anywhere}
.wrap{max-width:1240px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
header{background:linear-gradient(135deg,#052A76,#041D55);color:#fff}header .wrap{padding-block:28px 36px;display:grid;gap:12px}
header h1{font:700 clamp(28px,5vw,44px)/1.1 var(--sans);letter-spacing:-.02em}header h1 span{font-weight:400}
header p{color:#C3CBE4;max-width:64ch}.tags{display:flex;flex-wrap:wrap;gap:8px}.tags span{border:1px solid rgba(255,255,255,.3);border-radius:6px;padding:2px 10px;font-size:13px}
.tags .p{border-color:var(--pera);color:var(--pera)}
main{display:grid;padding-block:8px 56px}
section{display:grid;grid-template-columns:minmax(0,1fr);gap:16px;padding-block:32px;border-bottom:1px solid var(--border);min-width:0}
section>h2{font:700 26px/1.2 var(--sans);letter-spacing:-.015em}section>h2 span{font-weight:400}.ey{font:600 11px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--primary)}
.intro{color:var(--muted);max-width:68ch}.pie{font-size:13px;color:var(--muted)}
.tres{display:grid;gap:12px}@media(min-width:860px){.tres{grid-template-columns:repeat(3,minmax(0,1fr))}}
.card{background:#fff;border:1px solid var(--border);border-radius:12px;padding:18px;display:grid;gap:6px;align-content:start;box-shadow:0 1px 2px rgba(20,27,51,.06)}.card p{color:var(--muted);font-size:14px}
.card .k{font:600 11px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.inv{display:grid;grid-template-columns:minmax(0,190px) minmax(0,1fr) auto;gap:12px;align-items:center;padding:10px 0;border-top:1px solid var(--border)}
@media(max-width:639px){.inv{grid-template-columns:minmax(0,1fr) auto}.inv .vcs{grid-column:1/-1;order:3}}
.vcs{display:flex;flex-wrap:wrap;gap:4px}.vc{width:26px;height:26px;border-radius:6px;border:1px solid rgba(20,27,51,.12)}.inv .n{font-size:13px;color:var(--muted);white-space:nowrap}
.tw{overflow-x:auto;background:#fff;border:1px solid var(--border);border-radius:12px}
table{border-collapse:collapse;width:100%;font-size:14px}th{background:#EEF1F6;color:var(--muted);font:500 13px var(--sans);text-align:left;padding:10px 12px;white-space:nowrap}
td{padding:10px 12px;border-top:1px solid var(--border);vertical-align:middle}td.num{white-space:nowrap}.bad{color:var(--bad);font-weight:600}
.pair{display:inline-grid;place-items:center;width:34px;height:26px;border-radius:6px;border:1.5px solid;font-weight:600;font-size:13px}
.lista{margin:0;padding-left:20px;display:grid;gap:6px;max-width:70ch}
.grupo{display:grid;gap:8px}.grupo h3{font:600 17px var(--sans)}.sws{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}
.sw{margin:0;display:grid;gap:6px;align-content:start}.sw .chip{border-radius:10px;min-height:78px;padding:10px 12px;display:flex;flex-direction:column;justify-content:flex-end;border:1px solid rgba(20,27,51,.08)}
.sw .chip b{font:600 14px var(--sans)}.sw .chip code{font-size:12px}.sw figcaption{font-size:13px;line-height:18px;color:var(--muted);display:grid;gap:3px}.sw .ra{font-weight:600;color:var(--text)}.sw .rem{font-size:12px}
/* Muestras */
.duo{display:grid;gap:16px}@media(min-width:1024px){.duo{grid-template-columns:repeat(2,minmax(0,1fr))}}
.lado{background:var(--bg);border-radius:16px;padding:16px;display:grid;gap:12px;align-content:start;color:var(--text);font-size:13px;min-width:0}
.lt{font:700 12px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.lado .m{background:var(--surf);border-radius:14px;padding:14px;display:grid;gap:10px;box-shadow:0 8px 22px rgba(5,42,118,.06);min-width:0}
.mh{display:flex;align-items:center;justify-content:space-between;gap:8px}.count{font:600 11px var(--mono);padding:3px 9px;border-radius:7px;background:var(--countbg);color:var(--counttx);border:1px solid var(--countline)}
.fol{display:flex;flex-wrap:wrap;gap:6px}.fb{display:grid;justify-items:center;gap:2px;min-width:72px;padding:7px 10px;border-radius:9px;border:1px solid;font-family:var(--mono)}
.fb b{font-size:12px}.fb small{font:700 9px var(--sans);letter-spacing:.05em;text-transform:uppercase}
.fb.ok{background:var(--okbg);border-color:var(--okline);color:var(--ok)}.fb.pend{background:var(--warnbg);border-color:var(--warnline);color:var(--warn)}.fb.act{background:var(--primary);border-color:var(--primary);color:#fff}
.lh{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr) auto;gap:10px;font:700 9px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--head);background:var(--surf2);margin:-14px -14px 0;padding:8px 14px;border-radius:14px 14px 0 0;border-bottom:1px solid var(--border)}
.ri{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr) auto;gap:10px;align-items:center;padding-bottom:10px;border-bottom:1px solid var(--border)}.ri:last-child{border:0;padding:0}
.ri>span:first-child{display:grid;gap:4px;justify-items:start}.ri b{font-weight:600}
.pill{display:inline-flex;align-items:center;gap:4px;padding:2px 8px;border-radius:7px;font-size:10.5px;font-weight:600;border:1px solid}
.pill.ok{background:var(--okbg);color:var(--ok);border-color:var(--okline)}.pill.err{background:var(--errbg);color:var(--err);border-color:var(--errline)}.pill.warn{background:var(--warnbg);color:var(--warn);border-color:var(--warnline)}
.v{font:600 14px var(--mono);text-align:right}.v small{display:block;font:500 10px var(--mono);color:var(--muted)}
.fl{font-size:11px;font-weight:600;color:var(--muted)}.campo{display:flex;min-height:42px;border:1px solid var(--ctrl);border-radius:10px;overflow:hidden;background:var(--surf)}
.campo .in{flex:1;padding:10px 12px;text-align:right;font:500 13.5px var(--mono)}.campo .u{display:flex;align-items:center;padding:0 10px;background:var(--soft);border-left:1px solid var(--line);color:var(--primary);font:700 10.5px var(--mono)}
.campo.ro{background:var(--ro);border-color:var(--roline)}.campo.ro .in{color:var(--muted)}.campo .lk{display:grid;place-items:center;width:32px;border-right:1px solid var(--roline);color:var(--muted)}
.al{display:grid;gap:2px;padding:10px 12px;border-radius:10px;border:1px solid}.al b{font-size:12.5px}.al span{color:var(--text);font-size:12px}
.al.err{background:var(--errbg);border-color:var(--errline);color:var(--err)}.al.pri{background:var(--soft);border-color:var(--line);color:var(--primary)}.al.warn{background:var(--warnbg);border-color:var(--warnline);color:var(--warn)}
.btns{display:flex;flex-wrap:wrap;gap:8px}.b{display:inline-flex;align-items:center;min-height:40px;padding:0 14px;border-radius:9px;font-weight:600;font-size:12.5px;border:1px solid transparent}
.b.sm{min-height:34px;padding:0 12px}.b.pri{background:var(--primary);color:#fff}.b.sec{background:var(--surf);border-color:var(--ctrl);color:var(--text)}
.b.val{background:var(--primary);color:#fff}.b.okbtn{background:var(--okbtn);color:#fff}.b.dng{background:var(--danger);color:#fff}
.log{background:var(--logbg)!important;font:12px/1.5 var(--mono);color:var(--logtx)}.lr{display:grid;grid-template-columns:auto auto minmax(0,1fr);gap:8px;align-items:baseline}
.lb{font:700 9.5px var(--sans);padding:1px 5px;border-radius:3px}.lb.info{background:var(--loginfobg);color:var(--loginfo)}.lb.warn{background:var(--logwarnbg);color:var(--logwarn)}.lb.err{background:var(--logerrbg);color:var(--logerr)}
.le{font:600 10px var(--sans);letter-spacing:.05em;color:var(--logmuted)}
.lado.nueva .lb{border:1px solid currentColor}
/* Código */
.code{position:relative}.code pre{margin:0;max-height:420px;overflow:auto;background:#0E1630;color:#CBD5E1;border-radius:12px;padding:16px;font:12.5px/1.55 var(--mono)}
.copy{position:absolute;top:10px;right:10px;min-height:40px;padding:0 14px;border-radius:8px;border:1px solid #C3CFE6;background:#E8EDF7;color:#052A76;font:600 13px var(--sans);cursor:pointer}
.copy:focus-visible,a:focus-visible{outline:2px solid var(--pera);outline-offset:2px}
.dec{display:grid;gap:12px}.dec .card h3{font:600 16px var(--sans)}.rec{font-size:13px;font-weight:600;color:#1E5A22;background:#E3F1E4;border-radius:6px;padding:2px 8px;justify-self:start}
footer{padding-block:24px 40px;color:var(--muted);font-size:13px}
'''

SEC = []
SEC.append(f'''<section aria-labelledby="h1s"><span class="ey">Panorama</span><h2 id="h1s">Qué encontré <span>en el CSS</span></h2>
<div class="tres"><div class="card"><span class="k">Hecho</span><h3>Cinco capas definen lo mismo</h3><p>--v3-*, --nn-color-*, --nn-*, --nn-bit-* y la capa «V3» final. Cada una le da otro valor al mismo concepto; gana la que está más abajo en el archivo.</p></div>
<div class="card"><span class="k">Hecho</span><h3>Éxito usa el pera</h3><p>La capa final pone <code>--ok: #52660a</code>, un olivo sacado del pera. «Completo» y la marca se ven de la misma familia; en NisaLab el pera significa «en curso».</p></div>
<div class="card"><span class="k">Hecho</span><h3>Los campos no se distinguen</h3><p>El contorno de campos y buscador mide {crt("#d5dce8", "#ffffff")} sobre blanco. WCAG pide 3:1 para el borde que identifica un control.</p></div></div>
<p class="intro">La mayoría del texto sí cumple 4.5:1. El problema principal no es de contraste sino de <b>dueño</b>: el mismo significado tiene muchos valores, y un valor (el pera) tiene dos significados.</p></section>''')
SEC.append(f'''<section aria-labelledby="h2s"><span class="ey">Diagnóstico</span><h2 id="h2s">Valores distintos <span>por concepto</span></h2>
<p class="intro">Leídos directamente del archivo, incluidos los valores de respaldo de <code>var(--x, #valor)</code>. Cada cuadro es un color diferente que hoy significa lo mismo.</p><div>{INV}</div>
<h3 style="font:600 17px var(--sans)">Contrastes que no cumplen</h3><div class="tw"><table><thead><tr><th>Dónde</th><th>Par</th><th>Medido</th><th>Mínimo</th><th>Nota</th></tr></thead><tbody>{FALLAS_T}</tbody></table></div>
<p class="pie">Cálculo WCAG 2.x con los valores del archivo. Los textos de la consola, alertas, píldoras y botones principales sí cumplen.</p></section>''')
SEC.append(f'''<section aria-labelledby="h3s"><span class="ey">Propuesta</span><h2 id="h3s">Una sola capa, <span>{len(P)} colores con dueño</span></h2>
<p class="intro">Parte del design system NisaLab v3 (mismos nombres y valores) y agrega solo lo que bitácoras necesita y v3 no tenía: el borde de las píldoras de estado, el hover destructivo y la consola oscura. Cada tarjeta dice qué valores actuales reemplaza.</p>{PROP}</section>''')
SEC.append(f'''<section aria-labelledby="h4s"><span class="ey">Evidencia</span><h2 id="h4s">Mismo marcado, <span>otros colores</span></h2>
<p class="intro">Las dos columnas usan exactamente el mismo HTML y CSS; solo cambian las variables. Lo que ves de diferencia lo produce el color, nada más. Folios, parámetros y valores: de ejemplo.</p><div class="duo">{MUESTRAS}</div>
<ul class="lista"><li><b>Folios:</b> «Completo» pasa de olivo a verde conforme; el contador deja el pera y pasa a azul suave.</li><li><b>Campos:</b> el contorno pasa de {crt("#d5dce8", "#ffffff")} a {crt(P["border-control"], "#ffffff")}; solo lectura deja el lila y usa gris hundido con candado.</li>
<li><b>Botones:</b> «Validar» deja el degradado (el texto fallaba en su extremo claro) y «Aprobar» deja el negro: una sola acción primaria, en azul. Eliminar usa el rojo de «fuera».</li><li><b>Consola:</b> fondo teñido de azul; la etapa sube de {crt("#64748b", "#0f172a")} a {crt(P["log-muted"], P["log-bg"])}; los niveles se leen por texto y borde, sin tres fondos de color.</li></ul></section>''')
SEC.append(f'''<section aria-labelledby="h5s"><span class="ey">Decisiones</span><h2 id="h5s">Lo que tienes <span>que elegir</span></h2>
<div class="dec"><div class="card"><span class="rec">Recomendado: verde conforme</span><h3>1. ¿«Completo» en verde o en olivo?</h3><p>Olivo (actual): se integra con la marca, pero el pera ya marca «Urgente» y «en curso»; la misma familia diría «listo» y «atiéndeme». Verde (propuesta): mismo color que «Terminada» y «Conforme» en el resto de NisaLab.</p></div>
<div class="card"><span class="rec">Recomendado: #F2F4F8</span><h3>2. ¿Lienzo más oscuro o más claro?</h3><p>#dde3ec (actual) separa más las tarjetas (blanco encima {crt("#dde3ec", "#ffffff")}) pero baja el texto gris a {crt("#5b6478", "#dde3ec")} si cae directo sobre él. #F2F4F8 es el de v3; la separación la hacen el borde y la sombra.</p></div>
<div class="card"><span class="rec">Recomendado: gris con candado</span><h3>3. ¿Solo lectura con color propio?</h3><p>Hoy es lila (#f6f6fc), un tono que no existe en ningún otro lado del sistema. La propuesta lo iguala a deshabilitado y lo distingue con el candado: la diferencia la dice el icono, no un color sin dueño.</p></div></div></section>''')
SEC.append(f'''<section aria-labelledby="h6s"><span class="ey">Cómo aplicarla</span><h2 id="h6s">Capa de <span>compatibilidad</span></h2>
<p class="intro">Primer paso reversible: pegar este bloque al final del archivo. Los nombres viejos apuntan a la capa nueva, así que la mayoría de las reglas cambian sin tocarlas. Para deshacer, se borra el bloque.</p>
<div class="code"><button class="copy" type="button" id="copiar">Copiar CSS</button><pre id="css" tabindex="0">{e(CSS_PROP)}</pre></div>
<h3 style="font:600 17px var(--sans)">Segundo paso: valores escritos a mano en las reglas</h3><p class="pie">Estos no los alcanza la capa porque están como color fijo en la regla. Conteo aproximado por lectura.</p>
<div class="tw"><table><thead><tr><th>Hoy</th><th>Cambiar por</th><th>Alcance</th></tr></thead><tbody>{LIT_T}</tbody></table></div></section>''')
SEC.append('''<section aria-labelledby="h7s"><span class="ey">Fuera de alcance</span><h2 id="h7s">Lo que vi <span>y no toqué</span></h2><ul class="lista">
<li>La fuente de datos es Google Sans Code; el design system v3 dice IBM Plex Mono. Es decisión de tipografía, no de color.</li><li>Los colores de área de NisaLab no aparecen en bitácoras; no se tocan.</li><li>Esta propuesta no cambia el design system: si la apruebas, se actualizan sus valores y después el CSS.</li></ul></section>''')

out = f'''<title>Bitácoras · propuesta de color</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Google+Sans+Code:wght@400;500;600;700&display=swap">
<style>{CSS}</style><script>document.documentElement.lang='es'</script>
<header><div class="wrap"><h1>Bitácoras NisaLab: <span>propuesta de color</span></h1><p>Revisión del CSS de producción de bitácoras contra el design system NisaLab v3, y una capa de color única para reemplazar las cinco que conviven hoy.</p>
<div class="tags"><span>Ronda 1 · aprobada el 5 de noviembre</span><span>WCAG 2.2 AA</span><span class="p">Una sola cosa pera</span></div></div></header>
<main class="wrap">{"".join(SEC)}</main><footer class="wrap">Fuente: CSS de bitácoras (producción) y tokens del design system NisaLab v3. Contrastes calculados por el generador.</footer>
<script>
document.getElementById('copiar').addEventListener('click',function(){{var b=this,t=document.getElementById('css').textContent;
function sel(){{var r=document.createRange();r.selectNodeContents(document.getElementById('css'));var s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Seleccionado: copia con Ctrl+C';}}
try{{navigator.clipboard.writeText(t).then(function(){{b.textContent='Copiado'}},sel)}}catch(x){{sel()}}}});
</script>'''
open(os.path.join(D, 'propuesta.html'), 'w').write(out)
OVERRIDES = open(os.path.join(D, 'overrides.css')).read()
open(os.path.join(D, 'bitacoras-color.css'), 'w').write(CSS_PROP + '\n' + OVERRIDES)
print('ok', len(out) // 1024, 'KB')
