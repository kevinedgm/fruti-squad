# Manual de marca · NisaLab (consolida nisalab-final, nisalab-areas-final, nisalab-parametros-final y el design system NisaLab v3).
# Uso: python3 gen.py → manual.html. Símbolo, logotipos, áreas y fichas: archivos reales embebidos. Folios y clientes: de ejemplo.
# No usa ni reproduce el manual de Nisa Nabani (material del cliente).
import os, re, json, base64, html
D = os.path.dirname(os.path.abspath(__file__)); N = os.path.join(D, '..')
TOK = json.load(open(os.path.join(N, 'nabi-design-system/tokens.json')))
C = {t['name']: t['value'] for t in TOK['color']['tokens']}
USO = {t['name']: t.get('usage', '') for t in TOK['color']['tokens']}
for _ in range(4):
    C = {k: (C[v[1:-1]] if isinstance(v, str) and v.startswith('{') else v) for k, v in C.items()}
RET = {'surface-sunken':'bg','border-strong':'border','pera-soft':'primary-soft','on-pera':'primary','on-alerta-soft':'alerta','pendiente-soft':'bg','on-pendiente-soft':'text-muted','pendiente':'text-muted',
 'muestra-no-ingresada':'alerta-soft','on-muestra-no-ingresada':'alerta','muestra-en-proceso':'primary-soft','on-muestra-en-proceso':'primary','muestra-generando-informe':'primary-soft','on-muestra-generando-informe':'primary',
 'muestra-terminada':'conforme-soft','on-muestra-terminada':'on-conforme-soft','muestra-cancelada':'fuera-soft','on-muestra-cancelada':'fuera','pago-no-pagada':'fuera','pago-parcial':'alerta','pago-pagada':'conforme','pago-cortesia':'primary','on-fuera-soft':'fuera'}
C.update({k: C[v] for k, v in RET.items() if k not in C})
CUANDO = {'no-ingresada': 'Recibida en ventanilla, sin folio interno.', 'en-proceso': 'Con folio interno; se capturan parámetros.', 'generando-informe': 'Parámetros capturados; falta el informe.',
          'terminada': 'Informe generado y enviado.', 'cancelada': 'Se canceló la muestra o toda su orden.'}
AREAS = json.load(open(os.path.join(N, 'nisalab-areas-final/tema.json')))['paleta']['areas']
PARAM = json.load(open(os.path.join(N, 'nisalab-parametros-final/tema.json')))['tipos']
uri = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(N, p), 'rb').read()).decode()
F = {k: uri(f'nisalab-final/svg/{k}.svg') for k in ['simbolo', 'simbolo-1tinta', 'simbolo-blanco', 'logotipo', 'logotipo-blanco', 'logotipo-1tinta',
                                                    'logotipo-respaldo', 'logotipo-vertical', 'app-icon', 'favicon']}
HER = {p: uri(f'{p}-final/svg/simbolo.svg') for p in ['nisadata', 'nisaresults', 'nisastudio']}
L = '/root/.cache/fruti-uva/package/icons/'
def ico(n, size=18, color='currentColor', sw=1.75):
    inner = ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse|polygon)[^>]*/>', open(L + n + '.svg').read()))
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{inner}</svg>'
def frase(t, i=0):
    p = re.split(r'(?<=\.)\s', t); return p[i] if len(p) > i else ''
def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return f'{(la + .05) / (lb + .05):.1f}'
e = html.escape
W = '#FFFFFF'

# ---------- Color
GRUPOS = [
 ('Marca', 'Los dos colores del laboratorio. El azul ordena; el pera es una sola cosa: lo que creció, lo que está en curso.',
  [('primary', 'surface'), ('primary-hover', 'surface'), ('primary-soft', None), ('pera', None)]),
 ('Lienzo y lectura', 'Tema claro: lienzo gris de laboratorio y superficies blancas, nunca blanco sobre blanco.',
  [('bg', None), ('surface', None), ('text', 'bg'), ('text-muted', 'bg'), ('border', None), ('border-control', 'surface')]),
 ('Estados', 'Tres colores de estado, siempre con ícono y texto. Sirven al resultado, al proceso de la muestra y al pago. Pendiente va en gris.',
  [('conforme', 'surface'), ('conforme-soft', None), ('on-conforme-soft', 'conforme-soft'), ('alerta', 'alerta-soft'), ('alerta-soft', None), ('fuera', 'fuera-soft'), ('fuera-soft', None)]),
]
def swatch(n, sobre):
    v = C[n]; oscuro = lum(v) < .3
    if sobre: ra = f'{cr(v, C[sobre])}:1 sobre {sobre}'
    elif n.startswith('pera') and n == 'pera': ra = f'Azul encima {cr(C["primary"], v)}:1 · sobre blanco {cr(v, W)}:1 (nunca texto)'
    elif n == 'alerta-fill': ra = f'Sobre blanco {cr(v, W)}:1 (nunca texto)'
    else: ra = f'Texto encima {cr(C["text"], v)}:1'
    uso = frase(USO.get(n, ''))
    return (f'<figure class="sw"><span class="chip" style="background:{v};color:{W if oscuro else C["text"]}"><b>{n}</b><code>{v.upper()}</code></span>'
            f'<figcaption>{e(uso)}<span class="ra">{ra}</span></figcaption></figure>')
COLOR = ''.join(f'<div class="grupo"><h3>{g}</h3><p class="pie">{d}</p><div class="sws">{"".join(swatch(n, s) for n, s in it)}</div></div>' for g, d, it in GRUPOS)

# ---------- Áreas
AREA_T = ''.join(
    f'<tr><td><span class="ar"><img src="{uri(f"nisalab-areas-final/svg/{k}/marca.svg")}" alt="" width="40" height="40"><b>{v["nombre"]} NisaLab</b></span></td>'
    f'<td><img src="{uri(f"nisalab-areas-final/svg/{k}/icono.svg")}" alt="" width="32" height="32"></td>'
    f'<td><span class="dot" style="background:{v["hex"]}"></span><code>{v["hex"]}</code></td><td><code>{v["token"]}</code></td><td class="num">{cr(v["hex"], W)}:1</td></tr>'
    for k, v in AREAS.items())
AREA_LOGOS = ''.join(f'<div class="lienzo claro"><img src="{uri(f"nisalab-areas-final/svg/{k}/logotipo.svg")}" alt="Logotipo {AREAS[k]["nombre"]} NisaLab"></div>' for k in ('aguas', 'agave', 'farmacia'))

# ---------- Parámetros
FICHA = lambda c: uri('nisalab-parametros-final/svg/' + c + '/ficha.svg')
PARAM_H = ''.join('<div class="pm"><img src="' + FICHA(p['clave']) + '" alt="" width="40" height="40"><span><b>' + p['nombre'] + '</b><small>' + p['ejemplos'] + '</small></span></div>' for p in PARAM)

# ---------- Estados de la muestra y pago: usan los colores de estado (RET)
B16 = '<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true">'
def etapa(n):
    if n == 0: return B16 + '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75" stroke-dasharray="2.6 2.1"/></svg>'
    if n == 3: return B16 + '<circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M4.8 8.2 7 10.4 11.2 5.9" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    arc = 'M8 8 V2.5 A5.5 5.5 0 0 1 8 13.5 Z' if n == 1 else 'M8 8 V2.5 A5.5 5.5 0 1 1 2.5 8 Z'
    return B16 + f'<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75"/><path d="{arc}" fill="currentColor"/></svg>'
PROC = [('no-ingresada', 'No ingresada', etapa(0)), ('en-proceso', 'En proceso', etapa(1)), ('generando-informe', 'Generando informe', etapa(2)),
        ('terminada', 'Terminada', etapa(3)), ('cancelada', 'Cancelada', ico('ban', 14, sw=2.25))]
PAGO = [('no-pagada', 'No pagada', 'circle'), ('parcial', 'Pago parcial', 'circle-dashed'), ('pagada', 'Pagada', 'circle-check'), ('cortesia', 'Cortesía', 'gift')]
PILLS = ''.join(f'<span class="ps" style="background:{C["muestra-" + k]};color:{C["on-muestra-" + k]}">{i}{t}</span>' for k, t, i in PROC)
PILLS_R = ''.join(f'<tr><td><span class="ps" style="background:{C["muestra-" + k]};color:{C["on-muestra-" + k]}">{i}{t}</span></td><td class="num">{cr(C["on-muestra-" + k], C["muestra-" + k])}:1</td><td>{CUANDO[k]}</td></tr>' for k, t, i in PROC)
ETQ = ''.join(f'<span class="et2" style="color:{C["pago-" + k]};border-color:{C["pago-" + k]}">{ico(i, 14, sw=2.25)}{t}</span>' for k, t, i in PAGO)
URG = f'<span class="ur">{ico("zap", 14, sw=2.25)}Urgente</span>'
RES = [('conforme', 'circle-check', 'Conforme'), ('fuera', 'circle-x', 'Fuera de especificación'), ('alerta', 'triangle-alert', 'Cerca del límite'), ('pendiente', 'clock', 'Pendiente')]
RES_H = ''.join(f'<span class="rs" style="background:{C[k + "-soft"]};color:{C["on-" + k + "-soft"]}">{ico(i, 14, sw=2.25)}{t}</span>' for k, i, t in RES)

# ---------- Símbolo animado (carga): las células aparecen una tras otra, la pera crece al final
SIM = re.sub(r'<title>.*?</title>', '', open(os.path.join(N, 'nisalab-final/svg/simbolo.svg')).read()).replace('role="img" aria-label="NisaLab"', 'class="carga" aria-hidden="true" width="96" height="96"')

VOZ = [('«Registrar muestra»', '«Nuevo»'), ('«Capturar resultado»', '«Guardar datos»'),
       ('«El resultado está fuera del intervalo del método (0.005–10 mg/L). Revisa la dilución.»', '«Error de validación»'),
       ('«Liberar lote 2026-10-147»', '«Procesar»'), ('«LD», «LC», «alícuota», «método»', 'Traducir o explicar términos que el laboratorio ya usa'),
       ('«Aguas NisaLab»', '«NisaLab Aguas», «Nisalab», «Nisa Lab»')]
VOZ_T = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in VOZ)

NAV = [('esencia', 'Esencia'), ('marca', 'Marca'), ('color', 'Color'), ('areas', 'Áreas'), ('tipografia', 'Tipografía'), ('forma', 'Forma y elevación'),
       ('iconos', 'Iconos y parámetros'), ('estados', 'Estados'), ('movimiento', 'Movimiento'), ('voz', 'Voz'), ('componentes', 'Componentes'), ('accesibilidad', 'Accesibilidad'), ('pendientes', 'Pendientes')]
NAVH = ''.join(f'<li><a href="#{a}">{t}</a></li>' for a, t in NAV)

TY = {s['name']: s for g in TOK['type']['groups'] for s in g['styles']}
FAM = TOK['type']['families']; FQ = {k: v.replace('"', "'") for k, v in FAM.items()}; ZERO = 'font-feature-settings:"zero";'
def tline(n, txt, fam):
    s = TY[n]
    return (f'<div><span>{n}<br><small>{s["fontSize"]} / {s["fontWeight"]}</small></span><span style="font:{s["fontWeight"]} {s["fontSize"]}/{s["lineHeight"]} {FQ[fam]};'
            f'{"letter-spacing:" + s["letterSpacing"] + ";" if s.get("letterSpacing") else ""}{ZERO if fam == "datos" else ""}{"text-transform:uppercase;letter-spacing:.08em;" if n == "overline" else ""}">{txt}</span></div>')
ESCALA = ''.join([tline('display', 'Lote 2026-10-147', 'display'), tline('title-1', 'Resultados del análisis', 'display'), tline('title-2', 'Parámetros fisicoquímicos', 'display'),
                  tline('body', 'Muestra recibida en ventanilla por la mañana.', 'sans'), tline('label', 'Fecha de muestreo', 'sans'), tline('overline', 'Resultado', 'sans'),
                  tline('valor-xl', '0.012 mg/L', 'datos'), tline('valor', '7.40 ± 0.05', 'datos'), tline('valor-sm', 'LD 0.005 · LC 0.010', 'datos'), tline('folio', 'AG-2610-0147', 'datos')])

CSS = f'''
/* Manual NisaLab: índice fijo a la izquierda en escritorio, arriba en celular. Tema claro único (decisión del sistema). Valores tomados de tokens.json. */
:root{{--bg:{C['bg']};--surface:#fff;--sunken:{C['surface-sunken']};--text:{C['text']};--muted:{C['text-muted']};--border:{C['border']};--border-strong:{C['border-strong']};
--primary:{C['primary']};--primary-soft:{C['primary-soft']};--pera:{C['pera']};--pera-soft:{C['pera-soft']};--shadow-1:{TOK['shadow']['tokens'][0]['value']};--shadow-2:{TOK['shadow']['tokens'][1]['value']};
--sans:{FAM['sans']};--datos:{FAM['datos']};color-scheme:light}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
body{{margin:0;background:var(--bg);color:var(--text);font:15px/1.65 var(--sans)}}
a{{color:var(--primary)}}a:focus-visible{{outline:2px solid var(--primary);outline-offset:2px;border-radius:4px}}
h1,h2,h3,h4{{margin:0;text-wrap:balance}}p{{margin:0}}code,.num{{font:500 13px var(--datos);font-feature-settings:"zero";overflow-wrap:anywhere}}
.nw{{white-space:nowrap}}
.wrap{{max-width:1240px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.portada{{background:var(--primary);color:#fff;position:relative;overflow:hidden}}
.portada .wrap{{padding-block:28px 56px;display:grid;gap:24px;position:relative}}
.portada .logo{{height:40px;width:auto}}.portada h1{{font:700 clamp(38px,8vw,80px)/1.02 var(--sans);letter-spacing:-.03em;max-width:13ch}}.portada h1 span{{font-weight:400}}
.portada .lead{{font-size:18px;color:#DCE3F2;max-width:58ch}}.portada .meta{{display:flex;flex-wrap:wrap;gap:8px}}.portada .meta span{{border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:3px 12px;font-size:13px}}
.portada .fondo{{position:absolute;right:-60px;bottom:-80px;width:340px;height:340px;opacity:.14;pointer-events:none}}
.cuerpo{{display:grid;grid-template-columns:minmax(0,1fr);padding-block:8px 64px}}.cuerpo>*{{min-width:0}}
@media (min-width:1024px){{.cuerpo{{grid-template-columns:200px minmax(0,1fr);gap:48px}}}}
nav.indice{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);border-bottom:1px solid var(--border);margin:0 calc(-1 * max(16px,env(safe-area-inset-left,0px)));padding:8px max(16px,env(safe-area-inset-left,0px))}}
nav.indice ul{{list-style:none;margin:0;padding:0;display:flex;gap:6px;overflow-x:auto;scrollbar-width:none}}
nav.indice a{{display:inline-flex;align-items:center;min-height:36px;padding:0 12px;border-radius:8px;background:#fff;border:1px solid var(--border);color:var(--text);text-decoration:none;font-size:14px;white-space:nowrap}}
@media (min-width:1024px){{nav.indice{{margin:0;padding:24px 0;border:0;align-self:start;max-height:100vh;overflow:auto}}nav.indice ul{{flex-direction:column;overflow:visible}}nav.indice a{{background:none;border:0;padding:0 8px;min-height:32px}}nav.indice a:hover{{background:#fff}}}}
section.s{{display:grid;grid-template-columns:minmax(0,1fr);gap:20px;padding-block:40px;border-bottom:1px solid var(--border);scroll-margin-top:64px;min-width:0}}
.s>h2{{font:700 clamp(28px,4.4vw,40px)/1.1 var(--sans);letter-spacing:-.02em}}.s>h2 span{{font-weight:400}}
.s .intro{{font-size:17px;color:var(--muted);max-width:64ch}}.s h3{{font:600 18px/1.3 var(--sans)}}
.ey{{font:600 11px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--primary)}}
.grid2{{display:grid;gap:16px}}@media (min-width:760px){{.grid2{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
.grid3{{display:grid;gap:16px}}@media (min-width:760px){{.grid3{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}
.card{{background:#fff;border:1px solid var(--border);border-radius:12px;padding:20px;display:grid;gap:10px;min-width:0;box-shadow:var(--shadow-1);align-content:start}}.card p{{color:var(--muted)}}
.lista{{margin:0;padding-left:20px;display:grid;gap:6px;max-width:70ch}}.lista b{{font-weight:600}}
.arq{{display:grid;gap:10px}}@media (min-width:760px){{.arq{{grid-template-columns:1fr auto 1fr auto 1fr;align-items:center}}}}
.arq .card{{text-align:center;justify-items:center}}.arq .fl{{text-align:center;color:var(--muted);font-size:20px}}@media (max-width:759px){{.arq .fl{{transform:rotate(90deg)}}}}
.fam{{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(180px,1fr))}}.fam img{{width:40px;height:40px}}
/* Marca */
.lienzo{{border-radius:12px;display:grid;place-items:center;padding:28px;min-height:150px;border:1px solid var(--border)}}.lienzo img{{max-height:64px;width:auto;max-width:100%}}
.lienzo.claro{{background:#fff}}.lienzo.gris{{background:var(--bg)}}.lienzo.azul{{background:var(--primary);border-color:var(--primary)}}
.pie{{font-size:13px;color:var(--muted);margin-top:6px}}
.respeto{{display:inline-grid;place-items:center;padding:26px;background:repeating-linear-gradient(45deg,var(--pera-soft) 0 6px,#fff 6px 12px);border-radius:8px}}.respeto img{{height:90px;display:block;background:#fff}}
.mal{{display:grid;gap:12px}}@media (min-width:640px){{.mal{{grid-template-columns:repeat(4,minmax(0,1fr))}}}}
.mal figure{{margin:0;overflow:hidden;background:#fff;border:1px solid var(--border);border-radius:12px;padding:16px;display:grid;gap:8px;justify-items:center;text-align:center;font-size:13px;color:var(--muted)}}.mal img{{height:44px;width:auto}}
.mal .x{{font:700 12px var(--sans);color:{C['fuera']};letter-spacing:.06em}}
/* Color */
.grupo{{display:grid;gap:10px}}.sws{{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(190px,1fr))}}
.sw{{margin:0;display:grid;gap:6px;align-content:start}}.sw .chip{{border-radius:12px;min-height:92px;padding:12px 14px;display:flex;flex-direction:column;justify-content:flex-end;gap:2px;border:1px solid rgba(20,27,51,.08)}}.sw .chip b{{font:600 14px var(--sans)}}
.sw figcaption{{font-size:13px;line-height:18px;color:var(--muted);display:grid;gap:4px}}.sw .ra{{font-weight:600;color:var(--text);font-variant-numeric:tabular-nums}}
.prop{{display:flex;height:44px;border-radius:12px;overflow:hidden;border:1px solid var(--border)}}.prop span{{display:grid;place-items:center;font-size:12px;font-weight:600}}
/* Tablas */
.tw{{overflow-x:auto;background:#fff;border:1px solid var(--border);border-radius:12px;box-shadow:var(--shadow-1)}}
table{{border-collapse:collapse;width:100%;font-size:14px}}th{{background:var(--sunken);color:var(--muted);font:500 13px var(--sans);text-align:left;padding:10px 12px}}td{{padding:10px 12px;border-top:1px solid var(--border);vertical-align:middle}}
.ar{{display:inline-flex;align-items:center;gap:10px;white-space:nowrap}}.dot{{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:8px;vertical-align:-1px}}
/* Tipografía */
.esp-d{{font:700 clamp(34px,6vw,60px)/1.05 var(--sans);letter-spacing:-.025em}}.esp-d span{{font-weight:400}}
.esp-m{{font:500 clamp(26px,4.5vw,40px)/1.1 var(--datos);font-feature-settings:"zero"}}
.escala{{display:grid;gap:0}}.escala div{{display:grid;grid-template-columns:110px minmax(0,1fr);gap:12px;align-items:baseline;border-top:1px solid var(--border);padding:10px 0}}.escala div>span:first-child{{font-size:13px;color:var(--muted);line-height:1.3}}
/* Forma */
.radios{{display:flex;flex-wrap:wrap;gap:16px;align-items:end}}.radios figure{{margin:0;display:grid;gap:6px;justify-items:center;font-size:13px;color:var(--muted)}}.radios span{{display:block;width:72px;height:72px;background:var(--primary-soft);border:1.5px solid var(--primary)}}
.esp{{display:grid;gap:8px}}.esp div{{display:grid;grid-template-columns:80px minmax(0,1fr) 1.4fr;gap:12px;align-items:center;font-size:14px}}.esp i{{display:block;height:14px;background:var(--primary);border-radius:3px}}.esp small{{color:var(--muted)}}
@media (max-width:639px){{.esp div{{grid-template-columns:72px minmax(0,1fr)}}.esp small{{grid-column:1/-1}}}}
.sombras{{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(180px,1fr))}}.sombras figure{{margin:0;background:#fff;border-radius:12px;min-height:110px;padding:14px;display:grid;align-content:end;gap:2px;font-size:13px;color:var(--muted)}}.sombras b{{color:var(--text);font-size:14px}}
/* Iconos y parámetros */
.ics{{display:flex;flex-wrap:wrap;gap:10px}}.ics span{{display:inline-flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--border);border-radius:8px;padding:6px 12px;font-size:14px}}
.pms{{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}}.pm{{display:flex;gap:12px;align-items:center;background:#fff;border:1px solid var(--border);border-radius:12px;padding:12px}}.pm img{{flex:none}}.pm small{{display:block;color:var(--muted);font-size:13px;line-height:18px}}
.canales{{display:grid;gap:12px}}@media (min-width:760px){{.canales{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}
/* Estados */
.ps,.et2,.ur,.rs{{display:inline-flex;align-items:center;gap:6px;font:500 13px/18px var(--sans);border-radius:999px;padding:3px 10px;white-space:nowrap}}
.et2{{border:1.5px solid;background:#fff;border-radius:6px}}.ur{{background:var(--pera);color:{C['on-pera']};font-weight:600;border-radius:6px}}.rs{{border-radius:6px}}
.fila{{display:flex;flex-wrap:wrap;gap:8px}}
/* Movimiento */
.carga circle{{transform-box:fill-box;transform-origin:center;animation:cel 2.4s cubic-bezier(.2,.8,.2,1) infinite}}
.carga circle:nth-of-type(4){{animation-delay:0s}}.carga circle:nth-of-type(1){{animation-delay:.2s}}.carga circle:nth-of-type(3){{animation-delay:.4s}}.carga circle:nth-of-type(2){{animation-delay:.6s}}
@keyframes cel{{0%{{transform:scale(0);opacity:0}}12%,80%{{transform:scale(1);opacity:1}}100%{{transform:scale(1);opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.carga circle{{animation:none}}}}
.mov{{display:flex;flex-wrap:wrap;gap:24px;align-items:center}}
/* Voz */
.voz td:first-child{{color:{C['on-conforme-soft']}}}.voz td:last-child{{color:var(--muted)}}
/* Componentes */
.muestra{{background:#fff;border:1px solid var(--border);border-radius:12px;padding:20px;display:grid;gap:14px;box-shadow:var(--shadow-1);min-width:0}}
.muestra>.et{{font:600 11px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}}
.btnrow{{display:flex;flex-wrap:wrap;gap:10px}}.btn{{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:0 16px;border-radius:6px;font:600 14px var(--sans)}}
.btn.pri{{background:var(--primary);color:#fff;box-shadow:{TOK['shadow']['tokens'][4]['value']}}}.btn.sec{{background:#fff;color:var(--text);border:1px solid var(--border-strong);box-shadow:var(--shadow-1)}}.btn.txt{{color:var(--primary);padding:0 8px}}.btn.des{{background:#fff;color:{C['fuera']};border:1px solid {C['fuera']}}}
.campo{{display:grid;gap:6px;max-width:320px}}.campo label{{font:500 13px var(--sans)}}.campo span{{min-height:40px;border:1px solid {C['border-control']};border-radius:8px;padding:8px 12px;box-shadow:inset 0 1px 1px rgba(20,27,51,.05);font:500 14px var(--datos);font-feature-settings:"zero"}}.campo small{{color:var(--muted);font-size:12px}}
.res{{width:100%;min-width:560px}}.res td.num,.res th.num{{text-align:right;white-space:nowrap}}.res th{{white-space:nowrap}}.res tr.curso td{{background:var(--pera-soft)}}.res tr.curso td:first-child{{box-shadow:inset 3px 0 0 var(--pera)}}
.pozo{{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px}}
footer{{padding-block:28px 48px;color:var(--muted);font-size:14px;display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center}}footer img{{height:26px}}
'''

def S(id_, ey, titulo, intro, cuerpo):
    return f'<section class="s" id="{id_}" aria-labelledby="h-{id_}"><span class="ey">{ey}</span><h2 id="h-{id_}">{titulo}</h2>{f"<p class=intro>{intro}</p>" if intro else ""}{cuerpo}</section>'

TABLA_RES = f'''<div class="tw"><table class="res"><caption class="sr" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Resultados de la muestra AG-2610-0147 (ejemplo)</caption>
<thead><tr><th>Parámetro</th><th>Tipo</th><th class="num">Resultado</th><th class="num">Especificación</th><th>Estado</th></tr></thead><tbody>
<tr><td>pH</td><td><img src="{uri('nisalab-parametros-final/svg/fisicoquimicos/ficha.svg')}" alt="Fisicoquímicos" width="22" height="22" style="vertical-align:middle"></td><td class="num">7.40</td><td class="num">6.5–8.5</td><td><span class="pozo" style="background:{C['conforme']}"></span>Conforme</td></tr>
<tr><td>Plomo</td><td><img src="{uri('nisalab-parametros-final/svg/metales/ficha.svg')}" alt="Metales" width="22" height="22" style="vertical-align:middle"></td><td class="num">0.012 mg/L</td><td class="num">≤ 0.010</td><td><span class="pozo" style="background:{C['fuera']}"></span>Fuera de especificación</td></tr>
<tr class="curso"><td>Coliformes totales</td><td><img src="{uri('nisalab-parametros-final/svg/microbiologicos/ficha.svg')}" alt="Microbiológicos" width="22" height="22" style="vertical-align:middle"></td><td class="num">—</td><td class="num">&lt; 1.1 NMP/100 mL</td><td><span class="pozo" style="background:{C['pendiente']}"></span>Pendiente · en captura</td></tr>
</tbody></table></div>'''

SECCIONES = [
S('esencia', '01 · Esencia', 'Calidad que se <span>puede comprobar</span>', 'NisaLab es el sistema de laboratorio de Nisa Nabani: recepción de muestras, lotes, captura y revisión de resultados, e informes. Lo usan analistas, supervisores de calidad y recepción, casi siempre en escritorio y durante toda la jornada.',
  f'''<div class="grid2"><div class="card"><h3>Cómo se nombra</h3><p>«NisaLab», junto y con dos mayúsculas. Respaldo: «de Nisa Nabani». Nunca «Nisalab», «Nisa Lab» ni «NISALAB».</p></div>
  <div class="card"><h3>Qué dice el símbolo</h3><p>Colonia: cuatro células que casi se tocan; una creció y es pera. Lo vivo que el laboratorio detecta, cuenta y certifica.</p></div></div>
  <h3>Arquitectura</h3><div class="arq"><div class="card"><b>Nisa Nabani</b><p>La empresa. Su marca y su manual mandan sobre todo.</p></div><span class="fl" aria-hidden="true">→</span>
  <div class="card"><img src="{F['simbolo']}" alt="" width="40" height="40"><b>NisaLab</b><p>El sistema de laboratorio. Este manual.</p></div><span class="fl" aria-hidden="true">→</span>
  <div class="card"><b>«Área NisaLab»</b><p>Aguas, Alimentos, Farmacia… La célula que creció toma el color del área.</p></div></div>
  <h3>Fundamentos</h3><ul class="lista"><li><b>El dato manda.</b> Cada pantalla tiene un valor o estado protagonista; la marca vive en el encabezado, la carga y los documentos, no en las tablas.</li>
  <li><b>Una sola cosa pera.</b> Si hay dos cosas en pera, una sobra.</li><li><b>Área no es estado.</b> El color del área identifica la división; el estado tiene colores propios.</li>
  <li><b>Nada depende solo del color.</b> Todo estado lleva icono y texto.</li><li><b>Dos voces.</b> Poppins habla; IBM Plex Mono mide.</li></ul>
  <h3>Productos hermanos</h3><div class="fam"><div class="card"><img src="{HER['nisadata']}" alt=""><b>NisaData</b><p>Analítica. Lee los datos de NisaLab.</p></div>
  <div class="card"><img src="{HER['nisaresults']}" alt=""><b>NisaResults</b><p>Portal de clientes: resultados e informes.</p></div><div class="card"><img src="{HER['nisastudio']}" alt=""><b>NisaStudio</b><p>Piezas de redes y avisos.</p></div></div>
  <p class="pie">Mismo patrón «Nisa» + palabra, mismo respaldo y células como átomo gráfico; cada uno con su símbolo y su color. Tienen manual propio.</p>'''),
S('marca', '02 · Marca', 'Símbolo y <span>logotipo</span>', 'Se usan siempre los archivos del paquete final; nunca se redibuja el racimo ni se reescribe el nombre con una fuente.',
  f'''<div class="grid3"><div><div class="lienzo claro"><img src="{F['logotipo']}" alt="Logotipo NisaLab"></div><p class="pie">Horizontal · uso principal</p></div>
  <div><div class="lienzo gris"><img src="{F['logotipo-vertical']}" alt="Logotipo NisaLab vertical" style="max-height:120px"></div><p class="pie">Vertical · pantalla de acceso</p></div>
  <div><div class="lienzo claro"><img src="{F['logotipo-respaldo']}" alt="Logotipo NisaLab de Nisa Nabani"></div><p class="pie">Con respaldo · informes, documentos para clientes, portada</p></div>
  <div><div class="lienzo azul"><img src="{F['logotipo-blanco']}" alt="Logotipo NisaLab en blanco"></div><p class="pie">Blanco · sobre azul real</p></div>
  <div><div class="lienzo claro"><img src="{F['logotipo-1tinta']}" alt="Logotipo NisaLab a una tinta" style="color:{C['text']}"></div><p class="pie">Una tinta · documentos impresos</p></div>
  <div><div class="lienzo gris" style="gap:18px;grid-auto-flow:column"><img src="{F['simbolo']}" alt="Símbolo Colonia" style="max-height:56px"><img src="{F['app-icon']}" alt="Ícono de app" style="max-height:56px;border-radius:12px"><img src="{F['favicon']}" alt="Favicon" style="max-height:32px"></div><p class="pie">Símbolo · ícono de app · favicon</p></div></div>
  <div class="grid2"><div class="card"><h3>Área de respeto y tamaño mínimo</h3><div><span class="respeto"><img src="{F['simbolo']}" alt=""></span></div><p>El ancho de la célula grande libre alrededor de toda la pieza. Mínimo 16 px en pantalla y 6 mm impreso.</p></div>
  <div class="card"><h3>Construcción</h3><p>Cuatro células tangentes con la misma separación y proporción fija 1.0 · 1.7 · 2.9 · 3.7. La pera, arriba a la derecha. «Nisa» en Poppins 700 y «Lab» en Poppins 400, convertidos a trazos: el peso separa las dos palabras sin espacio.</p>
  <p>Sobre azul se usa la versión blanca; en documentos a una tinta, la versión a una tinta.</p></div></div>
  <h3>Así no</h3><div class="mal"><figure><img src="{F['simbolo']}" alt="" style="transform:rotate(90deg)"><span class="x">NO</span>Rotar o reacomodar el racimo</figure>
  <figure><span style="display:flex;gap:4px"><img src="{F['simbolo']}" alt="" style="filter:hue-rotate(60deg)"></span><span class="x">NO</span>Cambiar colores o poner dos peras</figure>
  <figure><span style="font:600 22px Poppins,sans-serif;color:{C['pera']};background:#fff">NisaLab</span><span class="x">NO</span>Texto en pera ({cr(C['pera'], W)}:1)</figure>
  <figure><img src="{F['logotipo']}" alt="" style="transform:scaleX(1.4);height:32px"><span class="x">NO</span>Estirar, o juntarlo con el logo de Nisa Nabani en una pieza</figure></div>'''),
S('color', '03 · Color', 'Azul real y <span>una célula pera</span>', '25 colores en total: 6 básicos, 4 de marca, 7 de estado y las 8 áreas. Un módulo no crea colores propios. Contrastes calculados con los valores de <code>tokens.json</code>.',
  f'''{COLOR}<div><h3>Proporción</h3><div class="prop" aria-hidden="true"><span style="flex:46;background:var(--bg)">lienzo</span><span style="flex:30;background:#fff">superficie</span><span style="flex:14;background:var(--text);color:#fff">texto</span><span style="flex:8;background:var(--primary);color:#fff">azul</span><span style="flex:2;background:var(--pera)"></span></div>
  <p class="pie">Aproximada: el pera ocupa un punto, nunca un área.</p></div>
  <ul class="lista"><li><b>Tema claro único.</b> Los campos van sobre <code>surface</code>: sobre <code>bg</code> su borde baja a {cr(C['border-control'], C['bg'])}:1.</li><li><b>Foco:</b> anillo de 2 px en azul, desplazado 2 px; sobre azul, el anillo va en pera.</li>
  <li><b>Solo lectura y deshabilitado:</b> sobre <code>bg</code> con candado (borde {cr(C['border-control'], C['bg'])}:1).</li><li><b>Pendiente:</b> gris de texto sobre el lienzo, con reloj: no es urgente.</li></ul>'''),
S('areas', '04 · Áreas', '«Área <span>NisaLab</span>»', 'Cada división es «Área NisaLab» y la célula que creció toma su color y su ícono. Los ocho colores tienen la misma luminosidad e intensidad (OKLCH 0.54 · 0.12): solo cambia el tono, fuera del rango del pera.',
  f'''<div class="tw"><table><thead><tr><th>Área</th><th>Ícono</th><th>Color</th><th>Token</th><th>Blanco encima</th></tr></thead><tbody>{AREA_T}</tbody></table></div>
  <div class="grid3">{AREA_LOGOS}</div>
  <ul class="lista"><li>El color del área va en su marca, el encabezado de su página y los filtros. <b>Nunca en tablas</b>: ahí el área va con su ícono a una tinta y su nombre.</li>
  <li>Íconos dibujados en retícula de 40, formas redondas y blancas, trazo 3–4. Mínimo 16 px.</li><li>Un color de área nunca indica un estado.</li></ul>'''),
S('tipografia', '05 · Tipografía', 'Poppins habla, <span>Plex Mono mide</span>', 'Poppins es la tipografía de Nisa Nabani para títulos y textos. IBM Plex Mono lleva lo que se mide, se compara o se copia: resultados, límites, unidades y folios.',
  f'''<div class="grid2"><div class="card"><span class="ey">Poppins 400 · 500 · 600 · 700</span><p class="esp-d" style="color:var(--text)">Resultados <span>del análisis</span></p><p class="pie">700 solo en display; 600 en títulos y botones; 400 en texto. Cuerpo de 14 px.</p></div>
  <div class="card"><span class="ey">IBM Plex Mono 400 · 500 · 600</span><p class="esp-m" style="color:var(--text)">0.012 mg/L</p><p class="pie">Cifras de ancho fijo para alinear columnas; cero con barra (<code>font-feature-settings:"zero"</code>) para no confundir 0 con O; tiene µ, ±, ≤, ≥ y °.</p></div></div>
  <div class="escala">{ESCALA}</div>
  <p class="pie">Carga: <code>Poppins:wght@400;500;600;700</code> e <code>IBM+Plex+Mono:wght@400;500;600</code> de Google Fonts.</p>'''),
S('forma', '06 · Forma y elevación', 'Contenido, <span>no plano</span>', 'Escala de 4 px; radios contenidos; sombras teñidas de azul, no negras. Las superficies blancas se separan del lienzo con borde y una sombra mínima.',
  '<div class="radios">' + ''.join(f'<figure><span style="border-radius:{t["value"]}"></span>{t["name"].replace("radius-", "")} · {t["value"]}</figure>' for t in TOK['radius']['tokens']) + '</div>'
  + '<div class="esp">' + ''.join(f'<div><code>{t["name"]}</code><span><i style="width:{int(t["value"][:-2]) * 3}px"></i></span><small>{t["value"]} · {e(t["usage"])}</small></div>' for t in TOK['spacing']['tokens']) + '</div>'
  + '<div class="sombras">' + ''.join(f'<figure style="box-shadow:{t["value"]}{";border:1px solid var(--border)" if t["name"] == "shadow-1" else ""}"><b>{t["name"]}</b>{e(frase(t["usage"]))}</figure>' for t in TOK['shadow']['tokens'][:4]) + '</div>'
  + '<p class="pie">Controles de 40 px en escritorio y 44 px en táctil; filas de tabla de 40 px. La píldora solo para puntos de estado, etiquetas de área y avatares.</p>'),
S('iconos', '07 · Iconos y parámetros', 'Tres canales, <span>tres significados</span>', 'Iconos de trazo de 1.75 px a 18 px, en el color del texto que acompañan. El tipo de parámetro es una ficha de elemento: cuadrado azul con dos letras blancas.',
  f'''<div class="ics">{"".join(f"<span>{ico(n)}{t}</span>" for n, t in [("test-tube", "Muestra"), ("flask-conical", "Ensayo"), ("microscope", "Análisis"), ("file-text", "Informe"), ("search", "Buscar"), ("circle-check", "Conforme")])}</div>
  <div class="pms">{PARAM_H}</div>
  <div class="canales"><div class="card"><h3>Área = color</h3><p>Círculo del color del área, con su ícono. Dice de qué división es.</p></div><div class="card"><h3>Parámetro = ficha</h3><p>Siempre azul ({cr(W, C['primary'])}:1 con blanco). Nunca toma tono. Va con su nombre al lado, salvo en columnas angostas con encabezado «Tipo».</p></div>
  <div class="card"><h3>Estado = semántico</h3><p>Color del estado, con icono y texto. Ver «Estados».</p></div></div>'''),
S('estados', '08 · Estados', 'Cada color, <span>un dueño</span>', 'Verde, ámbar y rojo dicen lo mismo en todo el sistema: el resultado, el proceso de la muestra y el pago usan esos tres colores. Pendiente va en gris; urgente es pera.',
  f'''<div><h3>Resultado del análisis</h3><div class="fila">{RES_H}</div></div>
  <div><h3>Proceso de la muestra</h3><p class="pie">Pastilla con fondo de color de estado. «En proceso» y «Generando informe» comparten el azul de selección; los separa el ícono, que avanza como la etapa: vacío, un cuarto, tres cuartos, lleno.</p><div class="tw" style="margin-top:10px"><table><thead><tr><th>Pastilla</th><th>Contraste</th><th>Cuándo</th></tr></thead><tbody>{PILLS_R}</tbody></table></div></div>
  <div class="grid2"><div><h3>Pago</h3><p class="pie">Etiqueta con contorno, para no competir con la pastilla de proceso.</p><div class="fila" style="margin-top:10px">{ETQ}</div></div>
  <div><h3>Prioridad</h3><p class="pie">Marca aparte; texto azul sobre pera ({cr(C['on-pera'], C['pera'])}:1).</p><div class="fila" style="margin-top:10px">{URG}</div></div></div>'''),
S('movimiento', '09 · Movimiento', 'La carga <span>es el símbolo</span>', 'Las células de Colonia aparecen una tras otra, 200 ms por paso, y la pera crece al final. Con «reducir movimiento», el símbolo queda quieto. Todo lo demás dura 150 ms.',
  f'''<div class="mov"><div class="card" style="place-items:center;min-width:180px">{SIM}<span class="pie">Cargando resultados…</span></div>
  <ul class="lista"><li><code>quick</code> 150 ms: hover y foco.</li><li><code>paso-carga</code> 200 ms: cada célula.</li><li><code>ease-out</code> <code>cubic-bezier(0.2, 0.8, 0.2, 1)</code>: entrada de paneles.</li><li>El botón primario sube 1 px al pasar el cursor.</li></ul></div>'''),
S('voz', '10 · Voz', 'Precisa, breve, <span>sin adornos</span>', 'Los botones dicen la acción y el objeto. Los errores dicen qué pasó y cómo corregirlo. Los términos del laboratorio no se traducen.',
  f'<div class="tw"><table class="voz"><thead><tr><th>Así sí</th><th>Así no</th></tr></thead><tbody>{VOZ_T}</tbody></table></div>'),
S('componentes', '11 · Componentes', 'Las piezas <span>clave</span>', 'Muestras estáticas. El design system NisaLab tiene las versiones vivas, sus estados y sus reglas. Folios y valores: de ejemplo.',
  f'''<div class="muestra"><span class="et">Botones</span><div class="btnrow"><span class="btn pri">Registrar muestra</span><span class="btn sec">Exportar</span><span class="btn txt">Ver historial</span><span class="btn des">Cancelar orden</span></div><p class="pie">Una sola acción primaria por vista; la destructiva va separada y pide confirmación.</p></div>
  <div class="grid2"><div class="muestra"><span class="et">Campo con valor</span><div class="campo"><label>Resultado (mg/L)</label><span>0.012</span><small>Intervalo del método: 0.005–10 mg/L</small></div></div>
  <div class="muestra"><span class="et">Folio y estado</span><p style="display:flex;flex-wrap:wrap;gap:10px;align-items:center"><code style="font-size:14px">AG-2610-0147</code>{PILLS.split('</span>')[1]}</span>{URG}</p><p class="pie">El folio siempre en Plex Mono; la fila en curso, en pera suave.</p></div></div>
  <div class="muestra"><span class="et">Tabla de resultados</span>{TABLA_RES}<p class="pie">Valores alineados a la derecha; estado con punto de 10 px y texto; la fila que se edita, con filete pera.</p></div>'''),
S('accesibilidad', '12 · Accesibilidad', 'WCAG 2.2 <span>AA</span>', None,
  f'<ul class="lista"><li>Texto 4.5:1 sobre su fondo (<code>text-muted</code> {cr(C["text-muted"], C["bg"])}:1 sobre <code>bg</code>); bordes de control 3:1.</li><li>Controles de 40 px en escritorio y 44 px en táctil; nada interactivo bajo 24 px.</li><li>Foco visible de 2 px; sobre azul, en pera.</li><li>Estados con icono y texto, nunca solo color; el área en tablas va con nombre.</li><li>Sobre su fondo suave, el verde necesita texto oscuro (<code>on-conforme-soft</code>); ámbar y rojo se leen con su propio color.</li><li>El pera nunca es texto ({cr(C["pera"], W)}:1 sobre blanco).</li><li>Se respeta «reducir movimiento».</li></ul>'),
S('pendientes', '13 · Pendientes', 'Por <span>decidir</span>', None,
  '<ul class="lista"><li>Registro de «NisaLab» en el IMPI y disponibilidad del dominio.</li><li>Productos «Producto NisaLab» (por ejemplo, «Recepción NisaLab») y su sello.</li><li>Convivencia con Verdant WebKit: si el azul y pera sustituyen al acento esmeralda de la interfaz actual o conviven con él.</li><li>Íconos de estatus dentro del informe (rondas A/B/C/D): sin elegir.</li><li>Confirmar nombres de estado con el flujo real del laboratorio.</li></ul>'),
]

html_out = f'''<title>Manual de marca NisaLab</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>{CSS}</style>
<script>document.documentElement.lang='es'</script>
<header class="portada"><img class="fondo" src="{F['simbolo-blanco']}" alt=""><div class="wrap"><img class="logo" src="{F['logotipo-blanco']}" alt="NisaLab"><h1>Manual de marca <span>de NisaLab</span></h1>
<p class="lead">Cómo se ve, cómo habla y cómo se usa NisaLab, el sistema de laboratorio de Nisa Nabani. Reúne el paquete final de marca, las áreas, los parámetros y el design system aprobados al 5 de noviembre de 2026.</p>
<div class="meta"><span>Design system v3 · noviembre 2026</span><span>Escritorio primero</span><span>Tema claro</span><span>WCAG 2.2 AA</span></div></div></header>
<div class="wrap cuerpo"><nav class="indice" aria-label="Secciones del manual"><ul>{NAVH}</ul></nav><main>{"".join(SECCIONES)}</main></div>
<footer class="wrap"><img src="{F['logotipo-respaldo']}" alt="NisaLab de Nisa Nabani"><span>Fuentes: paquetes nisalab-final, nisalab-areas-final, nisalab-parametros-final y design system NisaLab v3.</span></footer>'''
open(os.path.join(D, 'manual.html'), 'w').write(html_out)
print('ok', len(html_out) // 1024, 'KB')
