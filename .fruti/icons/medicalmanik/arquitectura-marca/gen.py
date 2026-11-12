# MedicalManik · arquitectura de marca explicada (por qué se renombraron los productos).
# Pedido (2026-11-05): «un artifact aparte, documentado, explicando toda la lógica y concepto detrás de MedicalManik:
# por qué renombramos los productos para diferenciar la marca de sus productos».
# Fuentes: ../ronda-1-nombres … ../ronda-5-seis, ../final/ (tema.json, LEEME), ../manik-final/, ../manual-marca/,
# ../design-system/project/README.md, ../manik-ia/LEEME.md, ../directorio-nombre-r02/. Uso: python3 gen.py → arquitectura.html
import os, base64, json
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
uri = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
T = json.load(open(os.path.join(M, 'final/tema.json')))
P = T['productos']
S = {k: uri(f'final/svg/{k}.svg') for k in ['medicalmanik', 'expediente', 'agenda', 'compras', 'farmacia', 'impulsa', 'grupos', 'administracion', 'ecosistema']}
PIN = uri('manik-final/svg/simbolo.svg'); LOGO = uri('final/svg/medicalmanik-logotipo.svg')
IA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 3.5c.45 4.2 3.8 7.55 8 8-4.2.45-7.55 3.8-8 8-.45-4.2-3.8-7.55-8-8 4.2-.45 7.55-3.8 8-8z" fill="#5FD3E2"/><path d="M19 2c.2 1.6 1.4 2.8 3 3-1.6.2-2.8 1.4-3 3-.2-1.6-1.4-2.8-3-3 1.6-.2 2.8-1.4 3-3z" fill="#5FD3E2"/></svg>'

# Fondos de las apps (2026-11-12): valores leídos del sistema de diseño del Ecosistema (fuente única), no copiados.
TK = {t['name']: t['value'] for t in json.load(open(os.path.join(M, 'design-system/project/tokens.json')))['color']['tokens']}
def _rgb(h): return [int(h[i:i+2], 16) for i in (1, 3, 5)]
def _lum(h):
    c = [x / 255 for x in _rgb(h)]; c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]; return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b): a, b = _lum(a), _lum(b); return (max(a, b) + .05) / (min(a, b) + .05)
def _lab(h):
    f = lambda c: c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4
    r, g, b = [f(x / 255) for x in _rgb(h)]
    l = (.4122214708*r + .5363325363*g + .0514459929*b) ** (1/3); m = (.2119034982*r + .6806995451*g + .1073969566*b) ** (1/3); q = (.0883024619*r + .2817188376*g + .6299787005*b) ** (1/3)
    return (.2104542553*l + .7936177850*m - .0040720468*q, 1.9779984951*l - 2.4285922050*m + .4505937099*q, .0259040371*l + .7827717662*m - .8086757660*q)
def dE(a, b): A, B = _lab(a), _lab(b); return 100 * sum((A[i] - B[i]) ** 2 for i in range(3)) ** .5
f1 = lambda x: f'{x:.1f}'.replace('.', '.')
CAPAS = [('canvas', 'Página', 'El fondo detrás de todo, en las siete apps.'), ('surface', 'Tarjeta y paneles', 'Tarjetas, tablas, barra superior y barra lateral.'),
 ('surface-soft', 'Agrupación', 'Encabezados de tabla, filas agrupadas, hover y campos de solo lectura.'), ('surface-pressed', 'Presionado', 'Lo que se está tocando o arrastrando.')]
capas_filas = ''.join(f'<tr><th scope="row"><span class="mu" style="background:{TK[k]}"></span>{n}</th><td><code>{k}</code></td><td class="num">{TK[k]}</td><td>{u}</td><td class="num">{f1(cr(TK["ink"], TK[k]))}:1 · {f1(cr(TK["muted"], TK[k]))}:1</td></tr>' for k, n, u in CAPAS)
ENOM = {'info': 'información', 'exito': 'éxito', 'aviso': 'atención', 'error': 'error'}
ESTADO = {'expediente': ('info', 'Sincronizando'), 'farmacia': ('exito', 'Receta surtida'), 'compras': ('aviso', 'Existencias bajas'), 'grupos': ('error', 'Pago rechazado')}
def mock(k, n, op):
    tb = TK[f'app-{k}-soft'] if op == 'C' else TK['surface']; pg = TK[f'app-{k}-soft'] if op == 'B' else TK['canvas']; e, et = ESTADO[k]
    return (f'<figure class="mkf"><div class="mk" role="img" aria-label="Pantalla de {n} Manik, opción {op}" style="--tb:{tb};--pg:{pg}"><div class="tb"><img src="{S[k]}" alt=""><span><b>{n}</b> Manik</span></div>'
            f'<div class="cu"><div class="lat"><i class="on"></i><i></i><i></i><i></i></div><div class="pg"><span class="ban" style="background:{TK[e + "-soft"]};color:{TK["on-" + e + "-soft"]}">{et}</span>'
            f'<div class="card"><b>Pendientes de hoy</b><span class="row"></span><span class="row c"></span><span class="bt" style="background:{TK["manik"]}">Guardar</span></div></div></div></div>'
            f'<figcaption><b>{n}</b> · fondo {pg} · aviso de {ENOM[e]}: ΔE {f1(dE(pg, TK[e + "-soft"]))}</figcaption></figure>')
MK = [('expediente', 'Expediente'), ('farmacia', 'Farmacia'), ('compras', 'Compras'), ('grupos', 'Grupos')]
mocks = {op: ''.join(mock(k, n, op) for k, n in MK) for op in 'ABC'}
_soft = {k: TK[f'app-{k}-soft'] for k, _ in [('expediente',0),('agenda',0),('compras',0),('farmacia',0),('impulsa',0),('grupos',0)]}
_ks = list(_soft); par_min = min(((dE(_soft[a], _soft[b]), a, b) for i, a in enumerate(_ks) for b in _ks[i+1:]))
PN = {'expediente': 'Expediente', 'agenda': 'Agenda', 'compras': 'Compras', 'farmacia': 'Farmacia', 'impulsa': 'Impulsa', 'grupos': 'Grupos'}

# Propuesta «pulcra» (2026-11-12): superficies con menos tinte, borde fino sin sombra; pesos máximos 500. Familias aprobadas: Outfit + Lexend.
HOY_S = {'canvas': TK['canvas'], 'surface': TK['surface'], 'soft': TK['surface-soft'], 'pressed': TK['surface-pressed'], 'line': TK['line'], 'line-control': TK['line-control']}
PUL_S = {'canvas': '#F4F2EE', 'surface': '#FFFFFF', 'soft': '#FAF9F6', 'pressed': '#EDEAE4', 'line': '#E8E5DF', 'line-control': '#7B849A'}  # 2026-11-12 r3: perla
PUL_NOTA = {'canvas': 'Página color perla: blanco roto con un matiz cálido leve. Las tarjetas blancas resaltan solas.', 'surface': 'Tarjetas, tablas, barras. Sin sombra; el contraste con la página ya las separa.',
 'soft': 'Dentro de una tarjeta: encabezados de tabla, hover y solo lectura.', 'pressed': 'Presionado y fila seleccionada junto con el azul de selección.', 'line': 'Bordes y divisores de 1 px.', 'line-control': 'Borde de campos. Se oscurece un poco para pasar 3:1 también sobre la página perla y las demás capas.'}
pul_filas = ''.join(f'<tr><th scope="row"><code>{"surface-" + k if k in ("soft", "pressed") else k}</code></th><td class="num"><span class="mu" style="background:{HOY_S[k]}"></span>{HOY_S[k]}</td><td class="num"><span class="mu" style="background:{PUL_S[k]}"></span><b>{PUL_S[k]}</b></td><td>{PUL_NOTA[k]}</td><td class="num">{"—" if k == "line" else (f1(min(cr(PUL_S[k], PUL_S[b]) for b in ("canvas", "surface", "soft", "pressed"))) + ":1 mín.") if k == "line-control" else f1(cr(TK["ink"], PUL_S[k])) + ":1 · " + f1(cr(TK["muted"], PUL_S[k])) + ":1"}</td></tr>' for k in PUL_S)
# Escala tipográfica: (estilo, familia, hoy, propuesta [px, alto, peso, extra], uso, muestra)
TIPO = [
 ('title-1', 'Outfit', '24/32 · 600', (22, 30, 500, ''), 'Título de página', 'Pacientes de hoy'),
 ('title-2', 'Outfit', '18/26 · 600', (17, 24, 500, ''), 'Título de tarjeta, panel y diálogo', 'Signos vitales'),
 ('app-name', 'Outfit', '16/24 · 600 + 400', (15, 22, 500, ''), 'Producto en 500, «Manik» en 400 y en color secundario', 'Expediente <span style="font-weight:400;color:#4A5674">Manik</span>'),
 ('body', 'Lexend', '16/24 · 400', (16, 24, 400, ''), 'Texto corrido y notas clínicas (sin cambio)', 'Refiere dolor leve desde hace dos días.'),
 ('body-sm', 'Lexend', '14/20 · 400', (14, 20, 400, ''), 'Tablas y listas densas (sin cambio)', 'Consulta de seguimiento'),
 ('label', 'Lexend', '14/20 · 600', (13, 18, 500, ''), 'Etiquetas de campo y encabezados de columna, en secundario', 'Motivo de consulta'),
 ('dato', 'Lexend', '16/24 · 500', (15, 22, 500, 'tnum'), 'Valores clínicos con cifras tabulares', '120/80 mmHg'),
 ('dato-xl', 'Lexend', '28/32 · 600', (26, 32, 400, 'tnum'), 'Valor protagonista: el tamaño ya lo destaca', '98 mg/dL'),
 ('button', 'Lexend', 'Outfit 15/20 · 600', (14, 20, 500, ''), 'Botones: misma letra que la interfaz', 'Guardar'),
 ('caption', 'Lexend', '13/18 · 400', (13, 18, 400, ''), 'Metadatos y ayudas; piso de 13 px (sin cambio)', 'Actualizado hace 5 min'),
 ('overline', 'Lexend', '12/16 · 700 MAYÚSCULAS', None, 'Se retira: lo cubre «label» en secundario', '—'),
]
def _ts(t):
    if not t[3]: return '<td class="num">se retira</td><td>—</td>'
    px, lh, w, x = t[3]; fam = '"Outfit"' if t[1] == 'Outfit' else '"Lexend"'
    st = f'font:{w} {px}px/{lh}px {fam},system-ui,sans-serif;{"font-variant-numeric:tabular-nums;" if x else ""}color:{"#4A5674" if t[0] in ("label", "caption") else "#14213D"}'
    return f'<td class="num"><b>{px}/{lh} · {w}</b></td><td><span style="{st}">{t[5]}</span></td>'
tipo_filas = ''.join(f'<tr><th scope="row"><code>{t[0]}</code><small>{t[1]}</small></th><td class="num">{t[2]}</td>{_ts(t)}<td>{t[4]}</td></tr>' for t in TIPO)
def app2(v):
    P = v == 'p'; S_ = PUL_S if P else HOY_S
    css = (f'--cv:{S_["canvas"]};--sf:{S_["surface"]};--so:{S_["soft"]};--ln:{S_["line"]};--lc:{S_["line-control"]};--rc:{"6px" if P else "24px"};--rb:{"4px" if P else "14px"};--sh:{"none" if P else TK["shadow-card"] if "shadow-card" in TK else "0 1px 2px rgba(20,33,61,.05),0 5px 14px rgba(20,33,61,.05)"};'
           f'--wt:{500 if P else 600};--wl:{500 if P else 600};--wx:{400 if P else 600};--t1:{22 if P else 24}px;--t2:{17 if P else 18}px;--lb:{13 if P else 14}px;--bf:{"Lexend" if P else "Outfit"};--bw:{500 if P else 600}')
    est = lambda e, t: f'<span class="ax-ch" style="background:{TK[e + "-soft"]};color:{TK["on-" + e + "-soft"]}">{t}</span>'
    rows = [('9:00', 'Ana Pérez Ruiz', 'Control de presión', est('exito', 'Atendida')), ('9:30', 'Luis Gómez Soto', 'Dolor de garganta', est('info', 'En consulta')),
            ('10:00', 'María Torres Vela', 'Resultados de laboratorio', est('aviso', 'Retrasada')), ('10:30', 'Jorge Díaz León', 'Primera vez', '<span class="ax-ch ax-n">Por llegar</span>')]
    ov = (lambda t: f'<span class="ax-ov">{t}</span>') if not P else (lambda t: f'<span class="ax-lb">{t}</span>')
    stats = ''.join(f'<div class="ax-st">{ov(a)}<b>{b}</b></div>' for a, b in [('Citas de hoy', '14'), ('Atendidas', '6'), ('Glucosa promedio', '98 <small>mg/dL</small>')])
    return (f'<div class="ax" style="{css}" role="img" aria-label="Pantalla de Expediente Manik, {"propuesta" if P else "hoy"}"><div class="ax-tb"><img src="{S["expediente"]}" alt=""><span class="ax-an"><b>Expediente</b> <span>Manik</span></span><span class="ax-bus">Buscar paciente</span></div>'
            f'<div class="ax-cu"><div class="ax-la"><span class="on">Hoy</span><span>Pacientes</span><span>Agenda</span><span>Recetas</span></div><div class="ax-pg"><div class="ax-hd"><div><h4>Pacientes de hoy</h4><small>Martes 12 de noviembre</small></div><span class="ax-bt">Nueva consulta</span></div>'
            f'<div class="ax-sts">{stats}</div><div class="ax-cd"><table><thead><tr><th>Hora</th><th>Paciente</th><th>Motivo</th><th>Estado</th></tr></thead><tbody>{"".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows)}</tbody></table></div></div></div></div>')

PROD = [('expediente', 'Expediente'), ('agenda', 'Agenda'), ('compras', 'Compras'), ('farmacia', 'Farmacia'), ('impulsa', 'Impulsa'), ('grupos', 'Grupos')]
RASGO = {'expediente': 'pestaña de carpeta', 'agenda': 'argollas de calendario', 'compras': 'borde de ticket', 'farmacia': 'cruz', 'impulsa': 'flecha que sale', 'grupos': 'segunda tarjeta detrás'}
sellos = ''.join(f'<figure><img src="{S[k]}" alt="" width="64" height="64"><figcaption><b>{n}</b> Manik<span>{P[n]["para"]}</span><span class="r">{RASGO[k]}</span></figcaption></figure>' for k, n in PROD)

ANTES = [
 ('La empresa', 'MedicalManik', 'MedicalManik', 'Sin cambio: es quien respalda. Su sello es el cuadro limpio con la línea de pulso.', 'hecho'),
 ('El expediente clínico', 'MedicalManik (el producto y la empresa se llamaban igual)', 'Expediente Manik', 'La ronda 1 de nombres partió de aquí: «la empresa sigue siendo MedicalManik; el producto lleva nombre propio».', 'hecho'),
 ('Campañas de prevención', 'Manik Impulsa (en producción)', 'Impulsa Manik', 'Se invierte el orden para seguir el patrón; su sistema en producción conserva su violeta como color de identidad.', 'hecho'),
 ('Agenda, Compras, Farmacia, Grupos', 'Sin nombre de producto', 'Agenda Manik · Compras Manik · Farmacia Manik · Grupos Manik', 'Nacen con el patrón desde el principio.', 'hecho'),
 ('Herramienta interna', 'No existía como producto', 'Administración Manik', 'Solo la ve el equipo de MedicalManik; para una clínica no existe.', 'hecho'),
 ('El directorio para pacientes', 'Mi Médico Manik', 'Manik → nombre nuevo en revisión', '«Manik» solo no se puede registrar; se exploran nombres como MediManik o DocManik.', 'en curso'),
 ('La inteligencia artificial', '«Recomendar tratamientos»', 'Manik IA (una función de Expediente)', 'No es un producto ni un personaje: en pantalla se llama «IA» y siempre sugiere.', 'hecho'),
]
filas = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td><td><b>{c}</b></td><td>{d}</td><td><span class="est {e.replace(" ", "-")}">{e}</span></td></tr>' for a, b, c, d, e in ANTES)

HTML = f'''<title>Arquitectura de MedicalManik</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;600;700&family=Outfit:wght@300..700&family=Lexend:wght@300..700&display=swap" rel="stylesheet">
<style>
/* Una sola luz, como la marca (tema claro único por decisión de marca): fondo papel, columna de lectura y láminas.
   Estructura de explicación: tesis → problema → tres niveles → regla del nombre → cómo se ve → casos → antes/ahora → abierto. */
:root{{--azul:#234899;--azul-osc:#1E3C7D;--cian:#009BB0;--cian-ui:#00788A;--papel:#F7F8FB;--blanco:#FFFFFF;--tinta:#14213D;--muted:#4A5674;--linea:#E1E6F0;--suave:#EEF1F7;
 --noche:#0F1C3F;--luz-cian:#D3F0F4;--luz-calida:#FFEFD2;--ok:#157B4A;--ok-s:#E7F5EE;--curso:#6B4A00;--curso-s:#FFF4E0;
 --display:"Urbanist","Segoe UI",system-ui,sans-serif;--sans:"Atkinson Hyperlegible Next","Atkinson Hyperlegible",system-ui,sans-serif;color-scheme:light}}
*{{box-sizing:border-box}}
body{{background:var(--papel);color:var(--tinta);font:400 17px/1.6 var(--sans);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
h1,h2,h3,h4{{font-family:var(--display);margin:0;text-wrap:balance;color:var(--tinta)}}p{{margin:0}}a{{color:var(--cian-ui)}}:focus-visible{{outline:3px solid var(--azul);outline-offset:2px}}
.hoja{{max-width:1060px;margin:0 auto;padding-block:32px 96px;display:grid;gap:72px;grid-template-columns:minmax(0,1fr)}}
.eti{{font:700 12px/16px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--cian-ui)}}
.texto{{max-width:64ch;display:grid;gap:14px}}.nota{{font-size:15px;line-height:22px;color:var(--muted)}}
section{{display:grid;gap:24px}}section>header{{display:grid;gap:6px}}h2{{font-size:clamp(26px,3.6vw,36px);line-height:1.15;font-weight:600}}h3{{font-size:21px;line-height:1.3;font-weight:600}}
/* portada */
.portada{{border-radius:32px;padding:clamp(28px,6vw,64px);display:grid;gap:22px;background:radial-gradient(ellipse 55% 80% at 0 0,var(--luz-cian),transparent 70%),radial-gradient(ellipse 45% 70% at 100% 10%,var(--luz-calida),transparent 70%),var(--blanco);border:1px solid var(--linea)}}
.portada img.logo{{width:min(300px,70%);height:auto}}
.portada h1{{font-size:clamp(34px,5.6vw,58px);line-height:1.05;font-weight:300;letter-spacing:-.02em;max-width:18ch}}.portada h1 b{{font-weight:600}}
.portada .lead{{font-size:19px;line-height:1.55;max-width:58ch}}
.claves{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}.claves div{{background:var(--blanco);border:1px solid var(--linea);border-radius:18px;padding:16px;display:grid;gap:4px}}.claves b{{font:600 17px/1.3 var(--display)}}.claves span{{font-size:15px;line-height:22px;color:var(--muted)}}
/* problema */
.antes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:12px}}
.ficha{{background:var(--blanco);border:1px solid var(--linea);border-radius:18px;padding:18px;display:grid;gap:8px;align-content:start}}.ficha b{{font:600 18px/1.3 var(--display)}}
.ficha .q{{font:600 22px/1.2 var(--display);color:var(--muted)}}
/* niveles */
.niveles{{display:grid;gap:0;border:1px solid var(--linea);border-radius:24px;overflow:hidden;background:var(--blanco)}}
.niv{{display:grid;grid-template-columns:120px minmax(0,1fr) minmax(0,1.2fr);gap:20px;align-items:center;padding:22px 24px;border-top:1px solid var(--linea)}}.niv:first-child{{border-top:0}}
.niv .k{{font:700 12px/16px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}.niv .k b{{display:block;font:600 34px/1 var(--display);letter-spacing:0;color:var(--azul);text-transform:none}}
.niv .ej{{display:flex;align-items:center;gap:12px;flex-wrap:wrap}}.niv .ej img{{width:44px;height:44px}}.niv .nm{{font:400 24px/1.2 var(--display);color:var(--muted)}}.niv .nm b{{font-weight:600;color:var(--tinta)}}
.niv p{{font-size:16px;line-height:24px}}
.analogia{{background:var(--noche);color:#fff;border-radius:24px;padding:24px 28px;display:grid;gap:10px}}.analogia h3{{color:#fff}}.analogia p{{color:#DCE3F2}}.analogia b{{color:#fff}}
.familia{{display:flex;flex-wrap:wrap;gap:8px 18px;font:400 22px/1.3 var(--display);color:#C9D3EA}}.familia b{{color:#fff;font-weight:600}}.familia span.ap{{color:#7FDCE6}}
/* regla del nombre */
.regla{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}}
.si,.no{{background:var(--blanco);border:1px solid var(--linea);border-radius:20px;padding:20px;display:grid;gap:12px;align-content:start}}.si h4{{color:var(--ok)}}.no h4{{color:#B23A48}}
.si ul,.no ul{{margin:0;padding:0;list-style:none;display:grid;gap:10px}}.si li,.no li{{font:400 22px/1.2 var(--display)}}.si li b{{font-weight:600}}.no li{{color:var(--muted);text-decoration:line-through;text-decoration-color:#B23A48}}.no li small,.si li small{{display:block;font:400 14px/20px var(--sans);text-decoration:none;color:var(--muted)}}
.porque{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:12px}}.porque div{{border-left:3px solid var(--cian);padding:4px 0 4px 16px;display:grid;gap:4px}}.porque b{{font:600 17px/1.35 var(--display)}}
.tag{{display:inline-block;font:700 11px/16px var(--sans);letter-spacing:.06em;text-transform:uppercase;border-radius:999px;padding:2px 8px;margin-left:6px;vertical-align:2px}}.tag.h{{background:var(--ok-s);color:var(--ok)}}.tag.i{{background:var(--suave);color:var(--muted)}}
/* sellos */
.sellos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,150px),1fr));gap:12px}}
.sellos figure{{margin:0;background:var(--blanco);border:1px solid var(--linea);border-radius:18px;padding:16px;display:grid;gap:10px;justify-items:start}}
.sellos figcaption{{display:grid;gap:2px;font:400 17px/1.3 var(--display);color:var(--muted)}}.sellos figcaption b{{font-weight:600;color:var(--tinta)}}.sellos figcaption span{{font:400 14px/20px var(--sans)}}.sellos .r{{color:var(--cian-ui)}}
.madre{{display:flex;flex-wrap:wrap;gap:24px;align-items:center;background:var(--blanco);border:1px solid var(--linea);border-radius:24px;padding:24px}}.madre img{{width:88px;height:88px}}.madre .texto{{flex:1;min-width:min(100%,280px)}}
.dos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:16px}}
.lam{{background:var(--blanco);border:1px solid var(--linea);border-radius:20px;padding:20px;display:grid;gap:12px;align-content:start}}
.chip{{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:6px 14px 6px 8px;font:600 15px/20px var(--sans)}}
.btn{{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:14px;background:var(--azul);color:#fff;font:600 15px/20px var(--sans)}}
.fila{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
/* tres familias */
.fams{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}.fam{{background:var(--blanco);border:1px solid var(--linea);border-radius:20px;padding:20px;display:grid;gap:10px;align-content:start}}
.fam .ic{{width:48px;height:48px;display:grid;place-items:center;border-radius:14px}}.fam .ic img{{width:44px;height:44px}}.fam .ic svg{{width:26px;height:26px}}
.fam dl{{margin:0;display:grid;gap:6px;font-size:15px;line-height:22px}}.fam dt{{font-weight:700;color:var(--muted);font-size:12px;letter-spacing:.06em;text-transform:uppercase}}.fam dd{{margin:0 0 6px}}
/* tabla */
.tw{{overflow-x:auto;border:1px solid var(--linea);border-radius:20px;background:var(--blanco)}}
table{{border-collapse:collapse;width:100%;min-width:760px}}th,td{{text-align:left;vertical-align:top;padding:14px 16px;border-bottom:1px solid var(--linea);font-size:15px;line-height:22px}}thead th{{font:700 12px/16px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:var(--suave)}}tbody tr:last-child>*{{border-bottom:0}}tbody th{{font-weight:700;min-width:150px}}
.est{{display:inline-block;border-radius:999px;padding:2px 10px;font:700 12px/18px var(--sans);white-space:nowrap}}.est.hecho{{background:var(--ok-s);color:var(--ok)}}.est.en-curso{{background:var(--curso-s);color:var(--curso)}}
.capas{{display:grid;grid-template-columns:minmax(0,1fr);gap:16px;align-items:start}}.capas .pila{{max-width:560px}}
.pila{{border-radius:20px;padding:22px;display:grid;gap:10px;border:1px solid var(--linea)}}.pila>span{{font:700 12px/16px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.pila .t1{{background:#fff;border:1px solid var(--linea);border-radius:14px;padding:14px;display:grid;gap:8px}}.pila .t2{{border-radius:10px;padding:10px 12px;display:flex;justify-content:space-between;align-items:center;font-size:14px}}.pila .t3{{border-radius:8px;padding:4px 10px;font-size:13px;font-weight:600}}
.mu{{display:inline-block;width:14px;height:14px;border-radius:4px;border:1px solid var(--linea);vertical-align:-2px;margin-right:8px}}td.num{{font-variant-numeric:tabular-nums;white-space:nowrap}}code{{font:13px ui-monospace,Menlo,monospace;background:var(--suave);border-radius:6px;padding:1px 6px}}
.ops{{display:grid;gap:28px}}.op{{display:grid;gap:12px}}.op>header{{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 12px}}.op>header h3{{font-size:20px}}
.mks{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:12px}}.mkf{{margin:0;display:grid;gap:6px}}.mkf figcaption{{font-size:13px;line-height:18px;color:var(--muted);font-variant-numeric:tabular-nums}}.mkf figcaption b{{color:var(--tinta)}}
.mk{{border:1px solid var(--linea);border-radius:14px;overflow:hidden;display:grid;grid-template-rows:34px 150px;background:#fff}}
.mk .tb{{background:var(--tb);display:flex;align-items:center;gap:6px;padding:0 10px;border-bottom:1px solid var(--linea);font:400 12px var(--display)}}.mk .tb img{{width:22px;height:22px}}.mk .tb b{{font-weight:600}}
.mk .cu{{display:grid;grid-template-columns:52px 1fr}}.mk .lat{{background:#fff;border-right:1px solid var(--linea);padding:10px 8px;display:grid;gap:6px;align-content:start}}.mk .lat i{{height:8px;border-radius:4px;background:#EEF1F7}}.mk .lat i.on{{background:#E9EDF5;box-shadow:inset 3px 0 0 #234899}}
.mk .pg{{background:var(--pg);padding:10px;display:grid;gap:8px;align-content:start}}.mk .ban{{justify-self:stretch;border-radius:6px;padding:4px 8px;font:600 11px var(--sans)}}
.mk .card{{background:#fff;border:1px solid var(--linea);border-radius:8px;padding:8px;display:grid;gap:6px}}.mk .card b{{font:600 12px var(--display)}}.mk .row{{height:6px;border-radius:3px;background:#EEF1F7}}.mk .row.c{{width:60%}}.mk .bt{{justify-self:start;color:#fff;border-radius:6px;padding:2px 8px;font:600 10px var(--sans)}}
.ab2{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}@media (max-width:900px){{.ab2{{grid-template-columns:1fr}}}}.ab2 figure{{margin:0;display:grid;gap:8px}}.ab2 figcaption{{font:600 15px var(--display)}}.ab2 figcaption span{{font:400 14px var(--sans);color:var(--muted)}}
.ax{{border:1px solid var(--ln);border-radius:16px;overflow:hidden;background:var(--cv);font:400 13px/18px "Lexend",system-ui,sans-serif;color:#14213D;display:grid;grid-template-rows:44px auto}}
.ax-tb{{background:var(--sf);border-bottom:1px solid var(--ln);display:flex;align-items:center;gap:8px;padding:0 12px}}.ax-tb img{{width:24px;height:24px}}.ax-an{{font:400 15px "Outfit",sans-serif}}.ax-an b{{font-weight:var(--wt)}}.ax-an span{{color:#4A5674}}.ax-bus{{margin-left:auto;border:1px solid var(--lc);border-radius:var(--rb);padding:3px 10px;color:#4A5674;font-size:12px}}
.ax-cu{{display:grid;grid-template-columns:96px minmax(0,1fr)}}.ax-la{{background:var(--sf);border-right:1px solid var(--ln);padding:10px 8px;display:grid;gap:2px;align-content:start}}.ax-la span{{padding:6px 8px;border-radius:var(--rb);color:#4A5674}}.ax-la .on{{background:#E9EDF5;color:#234899;font-weight:var(--wl)}}
.ax-pg{{padding:14px;display:grid;gap:12px;min-width:0}}.ax-hd{{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}}.ax-hd h4{{font:var(--wt) var(--t1)/1.3 "Outfit",sans-serif;letter-spacing:-.01em}}.ax-hd small{{color:#4A5674}}
.ax-bt{{background:#234899;color:#fff;border-radius:var(--rb);padding:6px 12px;font:var(--bw) 13px var(--bf),sans-serif;white-space:nowrap}}
.ax-sts{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}}.ax-st{{background:var(--sf);border:1px solid var(--ln);border-radius:var(--rc);box-shadow:var(--sh);padding:10px;display:grid;gap:2px;min-width:0}}
.ax-st b{{font:var(--wx) 22px/1.2 "Lexend",sans-serif;font-variant-numeric:tabular-nums}}.ax-st b small{{font-size:12px;font-weight:400;color:#4A5674}}
.ax-ov{{font:700 10px/14px "Lexend",sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#4A5674}}.ax-lb{{font:500 12px/16px "Lexend",sans-serif;color:#4A5674}}
.ax-cd{{background:var(--sf);border:1px solid var(--ln);border-radius:var(--rc);box-shadow:var(--sh);overflow:hidden}}.ax-cd table{{min-width:0;width:100%}}.ax-cd th,.ax-cd td{{padding:7px 10px;font-size:12px;line-height:16px;border-bottom:1px solid var(--ln)}}
.ax-cd thead th{{background:var(--so);font:var(--wl) calc(var(--lb) - 2px)/16px "Lexend",sans-serif;letter-spacing:0;text-transform:none;color:#4A5674}}.ax-cd tbody tr:last-child td{{border-bottom:0}}
.ax-ch{{display:inline-block;border-radius:999px;padding:1px 8px;font-size:11px;font-weight:500;white-space:nowrap}}.ax-n{{background:var(--so);color:#4A5674}}
.tipo th small{{display:block;font:400 12px var(--sans);color:var(--muted)}}
.reco{{border-left:4px solid var(--ok);background:var(--blanco);border-radius:0 16px 16px 0;padding:16px 20px;display:grid;gap:8px;max-width:76ch}}
.abiertos{{margin:0;padding-left:24px;display:grid;gap:10px;max-width:72ch}}
.glos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:12px 28px;margin:0}}.glos div{{display:grid;gap:2px}}.glos dt{{font:600 17px/1.3 var(--display)}}.glos dd{{margin:0;font-size:15px;line-height:22px;color:var(--muted)}}
.pie{{border-top:1px solid var(--linea);padding-top:18px;display:flex;flex-wrap:wrap;gap:8px 24px;justify-content:space-between;font-size:14px;color:var(--muted)}}
@media (max-width:760px){{.claves,.fams,.regla{{grid-template-columns:1fr}}.niv{{grid-template-columns:1fr;gap:10px}}}}
</style>

<main class="hoja">
<header class="portada">
 <img class="logo" src="{LOGO}" alt="MedicalManik">
 <span class="eti">Arquitectura de marca · cómo se nombra todo</span>
 <h1>Una empresa que <b>respalda</b>, una familia que <b>se reconoce</b> y productos que <b>dicen qué hacen</b></h1>
 <p class="lead">MedicalManik dejó de usar un solo nombre para todo. La empresa es quien está detrás; cada producto tiene un nombre que dice para qué sirve, y «Manik» los une como un apellido. Este documento explica esa lógica, por qué se tomó y cómo se aplica.</p>
 <div class="claves"><div><b>MedicalManik</b><span>La empresa y el sello madre. Firma, respalda, no compite con sus productos.</span></div><div><b>Manik</b><span>El apellido de la familia. Une a todo lo que hace la empresa.</span></div><div><b>Expediente, Agenda…</b><span>El nombre de pila: dice qué hace cada producto y para quién.</span></div></div>
</header>

<section aria-labelledby="h-prob"><header><span class="eti">El punto de partida</span><h2 id="h-prob">Un nombre hacía tres trabajos a la vez</h2></header>
 <div class="texto"><p>Antes, «MedicalManik» nombraba a la empresa y también a su producto principal, el expediente clínico. Otros productos tenían nombres armados cada uno a su manera: «Manik Impulsa» ponía la familia primero; «Mi Médico Manik», para pacientes, agregaba un posesivo. Cuando una empresa crece de un producto a varios, ese arreglo deja de funcionar.</p></div>
 <div class="antes">
  <div class="ficha"><span class="q">«¿Uso MedicalManik?»</span><b>No dice cuál</b><p class="nota">Si la empresa y el producto se llaman igual, una clínica que contrata Farmacia no sabe si «ya tiene MedicalManik» o le falta.</p></div>
  <div class="ficha"><span class="q">Manik Impulsa · Mi Médico Manik</span><b>Cada uno con su regla</b><p class="nota">Sin un patrón, cada producto nuevo inventa su forma de nombrarse y la familia deja de verse como familia.</p></div>
  <div class="ficha"><span class="q">Seis productos, un sello</span><b>No se distinguen</b><p class="nota">En un selector de apps, seis cosas llamadas igual con el mismo símbolo obligan a leer cada etiqueta.</p></div>
 </div>
</section>

<section aria-labelledby="h-niv"><header><span class="eti">La lógica</span><h2 id="h-niv">Tres niveles, cada uno con un trabajo</h2></header>
 <div class="niveles">
  <div class="niv"><span class="k">Nivel<b>1</b></span><div class="ej"><img src="{S["medicalmanik"]}" alt=""><span class="nm"><b>MedicalManik</b></span></div><p><b>La empresa.</b> Da confianza: seguridad de la información, cumplimiento normativo, respaldo. Aparece en contratos, facturas, firma institucional y como «de MedicalManik» junto a los productos.</p></div>
  <div class="niv"><span class="k">Nivel<b>2</b></span><div class="ej"><img src="{S["ecosistema"]}" alt=""><span class="nm"><b>Ecosistema</b> Manik</span></div><p><b>La familia.</b> «Manik» es el apellido que comparten todos los productos. Su identificador es el mosaico de seis cuadros, el botón que lleva de una app a otra.</p></div>
  <div class="niv"><span class="k">Nivel<b>3</b></span><div class="ej"><img src="{S["farmacia"]}" alt=""><span class="nm"><b>Farmacia</b> Manik</span></div><p><b>El producto.</b> El nombre dice qué hace y para quién: Farmacia surte recetas y lleva inventario. Su sello cambia solo el borde; su color lo identifica.</p></div>
 </div>
 <div class="analogia"><h3>Funciona como un nombre y un apellido</h3><p>Nadie confunde a dos hermanos porque compartan apellido: el nombre de pila dice quién es cada uno y el apellido dice de qué familia viene. Así se leen los productos:</p>
  <p class="familia">{"".join(f'<span><b>{n}</b> <span class="ap">Manik</span></span>' for _, n in PROD)}</p>
  <p>Y la empresa es como los padres: no tiene que aparecer en cada presentación, pero respalda a todos («de MedicalManik»).</p></div>
 <div class="texto"><p class="nota">En los manuales de marca a este modelo se le llama <b>casa con marcas respaldadas</b>: está entre una marca única para todo (como un banco que llama a todo con su nombre) y una casa de marcas independientes (como una empresa de consumo cuyos productos no se parecen entre sí). Toma lo mejor de ambos: cada producto es claro y la familia se reconoce.</p></div>
</section>

<section aria-labelledby="h-reg"><header><span class="eti">La regla del nombre</span><h2 id="h-reg">Siempre «Producto Manik»</h2></header>
 <div class="regla">
  <div class="si"><h4>Así</h4><ul><li><b>Expediente</b> Manik<small>El producto en negritas, «Manik» en regular.</small></li><li><b>Impulsa</b> Manik</li><li><b>Grupos</b> Manik</li></ul></div>
  <div class="no"><h4>Así no</h4><ul><li>Manik Farmacia<small>El orden invertido rompe la familia.</small></li><li>Farmacia<small>Solo, se pierde de qué familia viene.</small></li><li>MedicalManik Agenda<small>La empresa no se usa como apellido del producto.</small></li></ul></div>
 </div>
 <div class="porque">
  <div><b>El producto va primero <span class="tag i">razón inferida</span></b><p class="nota">En un menú o un selector la vista lee la primera palabra. Si todas empezaran con «Manik», habría que leer hasta la segunda para distinguirlas.</p></div>
  <div><b>«Manik» y no «MedicalManik» <span class="tag i">razón inferida</span></b><p class="nota">Es corto y se puede repetir en seis nombres sin cansar. «MedicalManik» queda reservado para la empresa y su respaldo.</p></div>
  <div><b>Pesos distintos <span class="tag h">regla vigente</span></b><p class="nota">El producto en 600 y «Manik» en 400. La vista se queda en lo que distingue y el apellido acompaña.</p></div>
 </div>
</section>

<section aria-labelledby="h-ver"><header><span class="eti">Cómo se ve</span><h2 id="h-ver">La misma línea de pulso, un borde distinto</h2></header>
 <div class="madre"><img src="{S["medicalmanik"]}" alt="Sello de MedicalManik"><div class="texto"><p>El <b>sello madre</b> es el cuadro limpio con la M dibujada como línea de pulso. Esa línea es idéntica en todos los sellos de la familia y nunca se redibuja. Cada producto cambia solo el <b>borde del cuadro</b> con un rasgo que cuenta qué es, y la línea nunca se corta.</p></div></div>
 <div class="sellos">{sellos}</div>
 <div class="dos">
  <div class="lam"><h3>El color tiene dos trabajos que no se mezclan</h3><p><b>Identidad:</b> cada producto tiene su color, que vive en su sello y en su tarjeta. Dice en qué app estás.</p><p><b>Interfaz:</b> el botón principal es azul MedicalManik en las siete apps, y los estados (éxito, aviso, error) son iguales en todas.</p>
   <div class="fila"><span class="btn">Guardar receta</span><span class="chip" style="background:var(--ok-s);color:var(--ok)">Surtida</span></div>
   <p class="nota">Por qué: Farmacia es verde como «éxito», Compras ámbar como «aviso» y Grupos rojizo como «error». Si fueran color de botón, un «Guardar» rojo en Grupos se leería como peligro.</p></div>
  <div class="lam"><h3>Y en pantalla, solo cambia el sello</h3><p>Barra superior, botones, campos, diálogos y navegación son los mismos en las siete apps. Quien pasa de Agenda a Farmacia no reaprende nada: lo único que cambia es el sello y el nombre arriba a la izquierda.</p>
   <div class="fila">{"".join(f'<img src="{S[k]}" alt="{n} Manik" width="36" height="36">' for k, n in PROD)}</div><p class="nota">Detalle en el sistema de diseño del Ecosistema: <a href="https://claude.ai/artifact/28z6yfie6L8btocL8QBZi9" target="_blank" rel="noopener">AppShell, EncabezadoApp y controles ↗</a>.</p></div>
 </div>
</section>

<section aria-labelledby="h-fon"><header><span class="eti">Los fondos</span><h2 id="h-fon">Los fondos de las apps</h2></header>
 <div class="texto"><p>Una pantalla se arma con capas de fondo. Cada capa tiene un trabajo: separar lo que es página de lo que es contenido, agrupar filas y mostrar qué se está tocando. Las capas son <b>neutras</b>: un gris con un sesgo leve al azul MedicalManik, el mismo en las siete apps.</p></div>
 <div class="capas">
  <div class="pila" style="background:{TK["canvas"]}"><span>Página · canvas</span><div class="t1"><b style="font:600 16px var(--display)">Tarjeta · surface</b><div class="t2" style="background:{TK["surface-soft"]}">Fila agrupada · surface-soft <span class="t3" style="background:{TK["surface-pressed"]}">presionado</span></div><div class="t2" style="background:{TK["surface-soft"]}">Encabezado de tabla</div></div></div>
  <div class="tw"><table style="min-width:620px"><thead><tr><th>Capa</th><th>Token</th><th>Color</th><th>Para qué</th><th>Texto · secundario</th></tr></thead><tbody>{capas_filas}</tbody></table></div>
 </div>
 <div class="dos">
  <div class="lam"><h3>Fuera de las apps, la luz de marca</h3><p>El inicio de sesión, la portada y el inicio del ecosistema usan <code>bruma</code> ({TK["bruma"]}) con los halos <code>luz-cian</code> y <code>luz-calida</code>, igual que el directorio para pacientes. Dentro de una app manda la página neutra: ahí se trabaja, no se presenta.</p></div>
  <div class="lam"><h3>Dónde sí entra el color del producto</h3><p>En el sello, en el nombre arriba a la izquierda y en la tarjeta de cada app en el inicio y el selector, que usa su fondo suave (por ejemplo <code>app-farmacia-soft</code> {TK["app-farmacia-soft"]}). Detrás de diálogos y hojas va el velo <code>scrim</code> (tinta al 40 %), nunca un color de producto.</p></div>
 </div>
 <header><span class="eti">Por decidir</span><h3>¿Y si el fondo de cada app llevara el color de su producto?</h3></header>
 <div class="texto"><p>Tres opciones sobre la misma pantalla, con un aviso de estado arriba, que es donde se nota el problema. Debajo de cada ejemplo está la distancia de color (ΔE) entre el fondo y el aviso: <b>por debajo de 2 el ojo casi no ve la diferencia</b>.</p></div>
 <div class="ops">
  <div class="op"><header><h3>A · Todo neutro</h3><span class="tag h">recomendada</span><span class="nota">Así está hoy el sistema de diseño.</span></header><div class="mks">{mocks["A"]}</div></div>
  <div class="op"><header><h3>B · La página con el tono del producto</h3><span class="tag i">no recomendada</span><span class="nota">La página usa el fondo suave de cada app.</span></header><div class="mks">{mocks["B"]}</div></div>
  <div class="op"><header><h3>C · La barra superior con el tono del producto</h3><span class="tag i">alternativa</span><span class="nota">Solo la barra cambia; la página sigue neutra.</span></header><div class="mks">{mocks["C"]}</div></div>
 </div>
 <div class="reco"><h3>Recomendación: A</h3><p><b>Lo que se midió.</b> Los fondos suaves de producto están demasiado cerca entre sí para orientar: {PN[par_min[1]]} y {PN[par_min[2]]} quedan a ΔE {f1(par_min[0])}. Y quedan encima de los avisos: en la opción B, el fondo de Farmacia está a ΔE {f1(dE(TK["app-farmacia-soft"], TK["exito-soft"]))} del aviso de éxito y el de Compras a {f1(dE(TK["app-compras-soft"], TK["aviso-soft"]))} del aviso de atención, así que el aviso se pierde en la página.</p><p><b>Lo que se infiere.</b> Es el mismo conflicto que separa identidad e interfaz en los botones: el color de producto en un plano grande compite con los colores que avisan algo. Si se quiere más presencia del producto, la opción C es la menos riesgosa, porque la barra no comparte espacio con los avisos.</p><p class="nota">Aun en la opción A, un aviso se separa de la página solo por ΔE {f1(min(dE(TK["canvas"], TK[e + "-soft"]) for e in ENOM))} a {f1(max(dE(TK["canvas"], TK[e + "-soft"]) for e in ENOM))}: se reconoce porque siempre lleva icono y texto, como pide el sistema de diseño, no solo por su color. Ninguna opción afecta la lectura: tinta y texto secundario pasan 4.5:1 sobre todos los fondos mostrados.</p></div>
</section>

<section aria-labelledby="h-pul"><header><span class="eti">Propuesta por aprobar</span><h2 id="h-pul">Superficies más pulcras y una tipografía más discreta</h2></header>
 <div class="texto"><p>En un expediente se trabaja muchas horas y lo importante son los datos del paciente. La propuesta quita peso a todo lo que no es dato: <b>fondos color perla, tarjetas blancas sin sombra, esquinas casi rectas y pesos que no pasan de 500</b>. La jerarquía la dan el tamaño y el color (tinta contra secundario), no el grosor de la letra.</p><p class="nota">Se mantienen las familias aprobadas: Outfit para títulos y Lexend para texto. Cambian solo tamaños, pesos y fondos.</p></div>
 <div class="ab2"><figure><figcaption>Hoy <span>· sistema de diseño actual</span></figcaption>{app2("h")}</figure><figure><figcaption>Propuesta <span>· pulcra y discreta</span></figcaption>{app2("p")}</figure></div>
 <div class="dos">
  <div class="lam"><h3>Cinco reglas</h3><ol class="abiertos" style="padding-left:20px"><li><b>Peso máximo 500.</b> El 600 y el 700 salen de la interfaz.</li><li><b>Jerarquía por tamaño y color.</b> Títulos en tinta; etiquetas, encabezados de columna y metadatos en secundario.</li><li><b>Sin mayúsculas forzadas.</b> El «overline» se retira.</li><li><b>Contraste, no sombra.</b> Tarjetas blancas sobre página perla, con borde de 1 px; la sombra queda solo para lo que flota (menús, diálogos).</li><li><b>Esquinas casi rectas:</b> 6 px en tarjetas y 4 px en botones y campos (hoy 24 y 14). Chips y etiquetas de estado siguen en píldora.</li></ol></div>
  <div class="lam"><h3>Lo que no cambia</h3><p>El azul MedicalManik en la acción principal, los colores de estado, el sello de cada producto, el piso de 13 px y el contraste: todo el texto sigue pasando 4.5:1.</p><p class="nota"><b>Inferencia:</b> la regla «el producto en 600 y Manik en 400» pasa a 500 y 400, y «Manik» además en color secundario, para que la diferencia no dependa solo del peso.</p></div>
 </div>
 <h3>Fondos</h3>
 <div class="tw"><table style="min-width:680px"><thead><tr><th>Token</th><th>Hoy</th><th>Propuesta</th><th>Uso</th><th>Texto · secundario</th></tr></thead><tbody>{pul_filas}</tbody></table></div>
 <h3>Escala tipográfica</h3>
 <div class="tw"><table class="tipo" style="min-width:760px"><thead><tr><th>Estilo</th><th>Hoy</th><th>Propuesta</th><th>Muestra</th><th>Uso</th></tr></thead><tbody>{tipo_filas}</tbody></table></div>
 <p class="nota">Medido: la página propuesta ({PUL_S["canvas"]}) se separa del blanco de las tarjetas por ΔE {f1(dE(PUL_S["canvas"], "#FFFFFF"))} (hoy {f1(dE(HOY_S["canvas"], "#FFFFFF"))}): por eso la tarjeta no necesita sombra. Al ser cálida, queda cerca del fondo del aviso de atención (ΔE {f1(dE(PUL_S["canvas"], TK["aviso-soft"]))}): los avisos van dentro de tarjetas blancas y siempre con icono y texto, nunca sueltos sobre la página. Intensidad del tinte: hoy {f1(100 * (_lab(HOY_S["canvas"])[1] ** 2 + _lab(HOY_S["canvas"])[2] ** 2) ** .5)} hacia el azul; perla {f1(100 * (_lab(PUL_S["canvas"])[1] ** 2 + _lab(PUL_S["canvas"])[2] ** 2) ** .5)} hacia el cálido (croma OKLab ×100): casi la misma cantidad de color, en otra dirección. Si se aprueba, los valores van primero al sistema de diseño del Ecosistema; este documento solo los explica.</p>
</section>

<section aria-labelledby="h-fam"><header><span class="eti">Para quién es cada cosa</span><h2 id="h-fam">Tres familias bajo el mismo respaldo</h2></header>
 <div class="fams">
  <div class="fam"><span class="ic"><img src="{S["ecosistema"]}" alt=""></span><h3>Ecosistema Manik</h3><dl><dt>Para</dt><dd>Clínicas, hospitales, médicos y su equipo.</dd><dt>Qué es</dt><dd>Seis apps de trabajo y Administración, que es interna.</dd><dt>Cómo se nombra</dt><dd>«Producto Manik».</dd></dl></div>
  <div class="fam"><span class="ic"><img src="{PIN}" alt=""></span><h3>El directorio para pacientes</h3><dl><dt>Para</dt><dd>Pacientes que buscan médico.</dd><dt>Qué es</dt><dd>La cara pública: buscar, ver precio y agendar.</dd><dt>Cómo se nombra</dt><dd>Nombre propio con Manik y respaldo «de MedicalManik». En revisión: «Manik» solo no se puede registrar.</dd></dl></div>
  <div class="fam"><span class="ic" style="background:var(--noche)">{IA}</span><h3>Manik IA</h3><dl><dt>Para</dt><dd>Médicos, dentro de Expediente.</dd><dt>Qué es</dt><dd>Una función, no un producto ni un personaje.</dd><dt>Cómo se nombra</dt><dd>En pantalla, solo «IA»: «Resumir con IA». Siempre sugiere; el médico decide.</dd></dl></div>
 </div>
 <div class="texto"><p class="nota">El directorio tiene otra voz (de tú, cercana) y otra paleta (luz cian y cálida) porque habla con pacientes, no con médicos. Conserva la línea de pulso dentro de un pin: se reconoce como parte de la familia.</p></div>
</section>

<section aria-labelledby="h-casos"><header><span class="eti">Casos especiales</span><h2 id="h-casos">Las excepciones también tienen regla</h2></header>
 <div class="dos">
  <div class="lam"><img src="{S["administracion"]}" alt="" width="48" height="48"><h3>Administración Manik es invisible para las clínicas</h3><p>Es la herramienta del equipo de MedicalManik. A diferencia de una app que la clínica no contrató (que se ve apagada, con candado), Administración no aparece en absoluto: mostrarla revelaría una superficie interna y generaría solicitudes imposibles. Por eso queda fuera del mosaico de seis.</p></div>
  <div class="lam"><img src="{S["impulsa"]}" alt="" width="48" height="48"><h3>Impulsa ya existía</h3><p>Se llamaba «Manik Impulsa» y tiene sistema propio en producción. Pasa a «Impulsa Manik» por el patrón, y su violeta se conserva como color de identidad. El 5 de noviembre se aprobó alinearla en lo que le faltaba: tipografía (Urbanist y Atkinson), botones en azul Manik y el lienzo común. Su equipo migra con una guía.</p></div>
 </div>
</section>

<section aria-labelledby="h-tabla"><header><span class="eti">Antes y ahora</span><h2 id="h-tabla">Qué cambió, producto por producto</h2></header>
 <div class="tw" tabindex="0" role="region" aria-label="Antes y ahora, producto por producto"><table><thead><tr><th scope="col">Qué es</th><th scope="col">Antes</th><th scope="col">Ahora</th><th scope="col">Por qué</th><th scope="col">Estado</th></tr></thead><tbody>{filas}</tbody></table></div>
</section>

<section aria-labelledby="h-abi"><header><span class="eti">Lo que sigue abierto</span><h2 id="h-abi">Decisiones pendientes</h2></header>
 <ol class="abiertos"><li><b>Nombre del directorio para pacientes.</b> «Manik» solo no se puede registrar. Hay propuestas con el molde de Doctoralia (MediManik, DocManik, DoctorManik) y la tipografía del logotipo será Sora. Falta saber por qué se rechazó «Manik» y hacer la búsqueda en el registro de marcas.</li>
 <li><b>Migración de Impulsa</b> al sistema común (aprobada; la hace su equipo con la guía).</li>
 <li><b>Fondos por producto.</b> Se recomienda la opción A (fondos neutros iguales en las siete apps); la C (barra superior con el tono del producto) queda como alternativa. Si se elige B o C, el cambio va primero al sistema de diseño del Ecosistema.</li>
 <li><b>Superficies pulcras y tipografía discreta.</b> Propuesta por aprobar: fondos color perla con tarjetas blancas, sin sombra, esquinas de 6 y 4 px y pesos máximos de 500. Si se aprueba, se aplica primero en el sistema de diseño del Ecosistema.</li>
 <li><b>Registro y dominios</b> de los nombres de producto en México y Centroamérica: no se han verificado.</li></ol>
</section>

<section aria-labelledby="h-glos"><header><span class="eti">Glosario</span><h2 id="h-glos">Palabras que usa este documento</h2></header>
 <dl class="glos">
  <div><dt>Arquitectura de marca</dt><dd>Cómo se relacionan y se nombran la empresa y sus productos.</dd></div>
  <div><dt>Marca madre</dt><dd>La marca de la empresa que respalda a las demás: MedicalManik.</dd></div>
  <div><dt>Respaldo</dt><dd>La firma pequeña que dice quién está detrás de un producto: «de MedicalManik».</dd></div>
  <div><dt>Sello</dt><dd>El símbolo de cada producto: la línea de pulso dentro de un cuadro con un rasgo propio en el borde.</dd></div>
  <div><dt>Color de identidad</dt><dd>El color que dice qué producto es. Vive en el sello y la tarjeta; nunca en botones ni estados.</dd></div>
  <div><dt>Mosaico del ecosistema</dt><dd>Los seis cuadros de color que abren el selector de apps. Siempre seis, aunque se sumen productos.</dd></div></dl>
</section>

<footer class="pie"><span>MedicalManik · Arquitectura de marca · noviembre 2026</span><span>Fuente: rondas de nombre y sello (24 de octubre), manual de identidad 2026 y sistema de diseño del Ecosistema</span></footer>
</main>'''
open(os.path.join(D, 'arquitectura.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
