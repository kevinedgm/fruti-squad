# NisaLab · encabezado de página, ronda 1: actual + A/B/C aplicados a páginas globales y por área.
# Pregunta de diseño: ¿cómo sabe quien captura, sin dudar, en qué área está (no registrar un agua en Alimentos)?
# Uso: python3 gen.py <carpeta de fuentes> <carpeta de íconos lucide> → encabezados.html
import json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..')
F, LU = sys.argv[1], sys.argv[2]
T = json.load(open(os.path.join(NS, 'nabi-design-system', 'tokens.json')))
V = ''.join(f"--{c['name']}:{c['value']};" for k in ('color', 'shadow', 'radius', 'spacing') for c in T[k]['tokens'] if not c['value'].startswith('{'))
def lucide(n, px=16):
    s = open(os.path.join(LU, n + '.svg')).read(); s = s[s.index('<svg'):]
    return re.sub(r'\s+', ' ', s).replace('width="24"', f'width="{px}"').replace('height="24"', f'height="{px}"').replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
_n = iter(range(100000))
def area_svg(a, var, px):
    s = open(os.path.join(NS, 'nisalab-areas-final', 'svg', a, var + '.svg')).read().strip()
    s = re.sub(r'<title>.*?</title>', '', s); u = next(_n)
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="{m.group(1)}-{u}"', s); s = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{m.group(1)}-{u})', s)
    return s.replace('<svg ', f'<svg width="{px}" height="{px}" aria-hidden="true" focusable="false" style="display:block;flex:none" ', 1)
AREA = {'aguas': ('Aguas', '#007CA3'), 'alimentos': ('Alimentos', '#A6552D'), 'bebidas': ('Bebidas alcohólicas', '#7A5DA9')}
# página: (clave, sección, título, área|None, entradilla|None, conteo, secundaria(ícono, texto), primaria(ícono, texto))
PAG = [
    ('usuarios', 'Administración', 'Usuarios', None, 'Quién entra a NisaLab y qué puede hacer.', '<b>24</b> usuarios · <b>3</b> invitaciones pendientes', ('download', 'Exportar'), ('user-plus', 'Agregar usuario')),
    ('rec-aguas', 'Recepción', 'Recepción de muestras', 'aguas', None, '<b>12</b> muestras hoy · <b>3</b> por etiquetar', ('printer', 'Imprimir etiquetas'), ('plus', 'Registrar muestra')),
    ('bit-bebidas', 'Bitácoras', 'Bitácora', 'bebidas', None, 'Turno matutino · <b>8</b> registros · <b>1</b> sin firmar', ('file-down', 'Exportar PDF'), ('plus', 'Nuevo registro')),
    ('cat-normas', 'Catálogos', 'Normas', None, 'Normas y métodos contra los que se evalúa cada parámetro.', '<b>64</b> normas · <b>5</b> por vencer', ('upload', 'Importar'), ('plus', 'Agregar norma')),
]
def acciones(sec, pri, movil):
    s = f'<button class="btn btn-s">{lucide(sec[0])}<span>{sec[1]}</span></button>'
    if movil: s = f'<button class="btn btn-s btn-i" aria-label="Más acciones">{lucide("ellipsis")}</button>'
    return f'<div class="acc">{s}<button class="btn btn-p">{lucide(pri[0])}<span>{pri[1]}</span></button></div>'
def chip(a):
    n, c = AREA[a]; return f'<span class="ach">{area_svg(a, "icono", 18)}{n}</span>'
def ruta(sec, ult):
    return f'<nav class="ruta" aria-label="Ruta"><a href="#">{sec}</a><span aria-hidden="true">/</span><span aria-current="page">{ult}</span></nav>'
def actual(p, m):
    k, sec, tit, a, ent, cnt, s2, s1 = p
    t = tit if not a else f'{tit} · {AREA[a][0]}'
    return (f'<header class="eh">{ruta(sec, AREA[a][0] if a else tit)}<div class="fila"><div class="tx"><h1>{t}</h1>'
            f'{f"<p class=ent>{ent}</p>" if ent else ""}<p class="cnt">{cnt}</p></div>{acciones(s2, s1, m)}</div></header>')
def alt_a(p, m):
    k, sec, tit, a, ent, cnt, s2, s1 = p
    return (f'<header class="eh">{ruta(sec, AREA[a][0] if a else tit)}<div class="fila"><div class="tx"><div class="tt"><h1>{tit}</h1>{chip(a) if a else ""}</div>'
            f'{f"<p class=ent>{ent}</p>" if ent else ""}<p class="cnt">{cnt}</p></div>{acciones(s2, s1, m)}</div></header>')
def alt_b(p, m):
    k, sec, tit, a, ent, cnt, s2, s1 = p
    if not a: return alt_a(p, m)
    n, c = AREA[a]
    return (f'<header class="eh ehb" style="--ac:{c}"><div class="fila"><div class="mb">{area_svg(a, "marca", 52 if not m else 44)}<div class="tx">'
            f'<p class="ceja">{sec} · {n}</p><h1>{tit} <span class="an">{n}</span></h1><p class="cnt">{cnt}</p></div></div>{acciones(s2, s1, m)}</div></header>')
def alt_c(p, m):
    k, sec, tit, a, ent, cnt, s2, s1 = p
    if not a: return alt_a(p, m)
    n, c = AREA[a]; act = 'Recepción' if sec == 'Recepción' else 'Bitácora'
    tabs = ''.join(f'<a href="#" class="tab"{" aria-current=page" if x == act else ""}>{x}</a>' for x in ('Recepción', 'Bitácora', 'Resultados'))
    return (f'<div class="ctx" style="--ac:{c}"><button class="sel" aria-haspopup="listbox">{area_svg(a, "icono", 24)}<span><small>Área</small>{n}</span>{lucide("chevron-down")}</button>'
            f'<nav class="tabs" aria-label="Secciones del área">{tabs}</nav></div>'
            f'<header class="eh"><div class="fila"><div class="tx"><h1>{tit}</h1>{f"<p class=ent>{ent}</p>" if ent else ""}<p class="cnt">{cnt}</p></div>{acciones(s2, s1, m)}</div></header>')
ALTS = [
    ('Actual', 'EncabezadoModulo tal como está', actual, 'El área solo aparece como texto en la ruta y el título. Es correcto, pero «Aguas» y «Alimentos» se ven igual: hay que leer para distinguirlos.'),
    ('A', 'Sello de área junto al título', alt_a, 'Mínimo cambio: el título dice la tarea y un sello (ícono + nombre del área) dice dónde. Las páginas globales quedan iguales.'),
    ('B', 'Marca del área como identidad de la página', alt_b, 'La página por área lleva la marca Colonia del área y una línea de su color. Se reconoce de lejos, sin leer. Cambia la regla actual «título sin ícono» solo para páginas por área.'),
    ('C', 'El área como espacio de trabajo', alt_c, 'El área deja de ser parte del título y pasa a ser un contexto persistente con selector; debajo, pestañas entre Recepción, Bitácora y Resultados del mismo área. Cambia la navegación, no solo el encabezado.'),
]
secs = ''
for L, t, fn, idea in ALTS:
    esc = ''.join(f'<div class="pg"><p class="pn">{p[2]}{" · " + AREA[p[3]][0] if p[3] else ""}</p><div class="lienzo">{fn(p, False)}<div class="tabla"></div></div></div>' for p in PAG)
    mov = f'<div class="pg mv"><p class="pn">Móvil 390 · Recepción · Aguas</p><div class="lienzo movil">{fn(PAG[1], True)}<div class="tabla"></div></div></div>'
    secs += f'<section><h2>{L} · {t}</h2><p class="id">{idea}</p><div class="pgs">{esc}{mov}</div></section>'
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700)) + f"@font-face{{font-family:'IBM Plex Mono';src:url('file://{F}/IBMPlexMono.ttf')}}"
css = ff + ':root{' + V + '}' + '''
*{box-sizing:border-box}body{margin:0;background:#E6E9F0;color:var(--text);font:400 14px/1.5 Poppins,sans-serif;padding:32px}
.top h1{font:700 26px/1.2 Poppins;color:var(--primary);margin:0 0 4px}.lead{color:var(--text-muted);max-width:820px;margin:0 0 8px}.sup{font-size:12px;color:var(--on-alerta-soft);background:var(--alerta-soft);border-radius:6px;padding:2px 8px;display:inline-block;margin-bottom:24px}
section{background:var(--surface);border-radius:14px;padding:24px;margin-bottom:24px;box-shadow:var(--shadow-1)}
section>h2{font:600 19px/1.3 Poppins;margin:0}.id{color:var(--text-muted);margin:4px 0 18px;max-width:900px}
.pgs{display:grid;grid-template-columns:minmax(0,1fr);gap:16px}.pg{min-width:0}.pn{font:600 11px/1 Poppins;letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted);margin:0 0 8px}
.lienzo{background:var(--bg);border:1px solid var(--border);border-radius:12px;padding:20px 24px 0;overflow:hidden}.movil{max-width:390px;padding:16px 16px 0}
.tabla{height:44px;margin-top:16px;background:var(--surface);border-radius:12px 12px 0 0;box-shadow:var(--shadow-1)}
.ruta{font:500 13px/18px Poppins;color:var(--text-muted);display:flex;gap:6px;margin-bottom:6px}.ruta a{color:var(--text-muted);text-decoration:none}.ruta [aria-current]{color:var(--text)}
.fila{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;flex-wrap:wrap}.tx{min-width:0}
h1{font:600 24px/32px Poppins;margin:0;color:var(--text)}.ent{color:var(--text-muted);font-size:15px;line-height:22px;margin:2px 0 0}
.cnt{font:400 13px/18px 'IBM Plex Mono',monospace;color:var(--text-muted);margin:6px 0 0}.cnt b{color:var(--text);font-weight:600}
.tt{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.ach{display:inline-flex;align-items:center;gap:6px;font:500 13px/18px Poppins;background:var(--surface);border:1px solid var(--border);border-radius:999px;padding:3px 12px 3px 4px;box-shadow:var(--shadow-1)}
.acc{display:flex;gap:8px;flex:none}.btn{display:inline-flex;align-items:center;gap:8px;font:600 14px/20px Poppins;border-radius:var(--radius-md);padding:9px 16px;min-height:40px;cursor:pointer}
.btn-s{background:var(--surface);color:var(--primary);border:1px solid var(--border-strong)}.btn-p{background:var(--primary);color:var(--on-primary);border:1px solid var(--primary);box-shadow:var(--shadow-primary)}.btn-i{padding:9px 10px}
.ehb{border-bottom:3px solid var(--ac);padding-bottom:16px}.mb{display:flex;align-items:center;gap:16px;min-width:0}
.ceja{font:500 13px/18px Poppins;color:var(--text-muted);margin:0 0 2px}.an{font-weight:400;color:var(--text-muted)}
.ctx{display:flex;align-items:center;gap:20px;background:var(--surface);border-radius:12px;box-shadow:var(--shadow-1);border-left:4px solid var(--ac);padding:6px 12px 0 8px;margin:-4px 0 16px;flex-wrap:wrap}
.sel{display:inline-flex;align-items:center;gap:10px;background:none;border:0;font:600 15px/20px Poppins;color:var(--text);padding:6px 8px 12px;cursor:pointer;text-align:left}.sel small{display:block;font:500 11px/14px Poppins;color:var(--text-muted)}
.tabs{display:flex;gap:4px;align-self:stretch;align-items:flex-end}.tab{font:500 14px/20px Poppins;color:var(--text-muted);text-decoration:none;padding:12px 12px 13px;border-bottom:3px solid transparent}.tab[aria-current]{color:var(--text);border-bottom-color:var(--ac);font-weight:600}
.movil .fila{align-items:stretch}.movil .acc{width:100%}.movil .btn-p{flex:1;justify-content:center}.movil h1{font-size:22px;line-height:28px}.movil .tabs{width:100%;overflow-x:auto}

@media (max-width:480px){body{padding:12px}section{padding:16px}.lienzo{padding:16px 12px 0}}
'''
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Encabezados de página</title><style>{css}</style><body>'
        '<div class="top"><h1>Encabezado de página · ronda 1</h1><p class="lead">Pregunta de diseño: ¿cómo sabe quien captura, sin dudar, en qué área está, para no registrar una muestra de agua en Alimentos? Cada alternativa se aplica a una página global (Usuarios, Normas) y a dos por área (Recepción, Bitácora).</p>'
        '<span class="sup">Supuesto: «Bebidas alcohólicas» usa el área Bebidas (#7A5DA9) hasta confirmar si sustituye a Bebidas de agave.</span></div>'
        + secs + '</body></html>')
open(os.path.join(H, 'encabezados.html'), 'w').write(html); print('ok')
