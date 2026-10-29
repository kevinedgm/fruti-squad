"""Aplica el manual de Nisa Nabani (2026) al design system de Nabi.

Uso: python3 marca-nisa.py <carpeta-project> <carpeta-marca-nisa>
Corre después de modulos.py. Decisiones del usuario (2026-10-29):
Poppins + IBM Plex Mono (sale Newsreader), estados separados de los colores
de división, Nabi conserva su símbolo de placa.
"""
import json, os, re, sys

P, A = sys.argv[1], sys.argv[2]
POP = '"Poppins", system-ui, -apple-system, "Segoe UI", sans-serif'

# ---------- tokens ----------
t = json.load(open(f'{P}/tokens.json'))
t['version'] = 3
fam = t['type']['families']
fam['display'] = POP
fam['sans'] = POP
fam.pop('editorial', None)
t['type']['groups'] = [g for g in t['type']['groups'] if g.get('family') != 'editorial']
SIZES = {  # Poppins tiene x-height alta: un punto menos que Archivo en cuerpo
    'display': ('28px', '36px', 700, '-0.01em', 'Una por pantalla: encabezado de lote o de certificado.'),
    'title-1': ('22px', '30px', 600, '-0.005em', 'Título de módulo y de sección.'),
    'title-2': ('16px', '24px', 600, None, 'Título de tarjeta, panel y diálogo.'),
    'body': ('14px', '22px', 400, None, None),
    'label': ('13px', '18px', 500, None, None),
    'button': ('14px', '20px', 600, None, None),
    'caption': ('12px', '18px', 400, None, None),
    'overline': ('11px', '16px', 600, '0.06em', None),
}
for g in t['type']['groups']:
    if g['name'] == 'Títulos':
        g['note'] = 'Poppins, la tipografía del manual de Nisa Nabani para títulos, subtítulos y textos. 700 solo en «display»; 600 en los demás títulos.'
    if g.get('family') == 'sans':
        g['note'] = 'Poppins. 14 px de cuerpo: su x-height alta lee como 15 px de otras familias. Google Fonts: Poppins:wght@400;500;600;700.'
    for s in g['styles']:
        if s['name'] in SIZES:
            fs, lh, fw, ls, us = SIZES[s['name']]
            s.update(fontSize=fs, lineHeight=lh, fontWeight=fw)
            if ls: s['letterSpacing'] = ls
            if us: s['usage'] = us
        if 'usage' in s:
            s['usage'] = s['usage'].replace(' font-stretch 125%.', '').replace('Archivo', 'Poppins')

STATE = {
    'conforme': ('#2E7D32', 'Resultado dentro de especificación, muestra liberada, usuario activo. 5.1:1 sobre blanco, 4.7:1 sobre «bg». Verde propio de estado: no es el verde de ninguna división (ΔE00 13.5 con Bebidas de agave, 18.6 con Ambiental). Siempre con icono y texto.'),
    'conforme-soft': ('#E3F1E4', 'Fondo de estado conforme.'),
    'on-conforme-soft': ('#1E5A22', 'Texto sobre «conforme-soft»: 7.1:1.'),
    'alerta': ('#8A6100', 'Cerca del límite, en revisión, suspendido. Ámbar de estado: 5.5:1 sobre blanco; ΔE00 25 con el naranja de Alimentos.'),
    'alerta-fill': ('#E9B10A', 'Ámbar de relleno para marcadores e indicadores. Nunca texto (2.0:1). Sustituye al naranja de Alimentos.'),
    'alerta-soft': ('#FBF0CC', 'Fondo de alerta.'),
    'on-alerta-soft': ('#664700', 'Texto sobre «alerta-soft»: 7.5:1.'),
    'pendiente': ('#475467', 'Pendiente, en análisis, invitación enviada. Gris pizarra: lo pendiente no es urgente y no compite con el azul de Bebidas ni con el azul real. 7.7:1.'),
    'pendiente-soft': ('#E4E8F0', 'Fondo de estado pendiente.'),
    'on-pendiente-soft': ('#344054', 'Texto sobre «pendiente-soft»: 8.5:1.'),
}
DIV = [
    ('aguas', 'Aguas', '#00B4D8'), ('agricolas', 'Agrícolas', '#553739'), ('ambiental', 'Ambiental', '#38B000'),
    ('alimentos', 'Alimentos', '#F48C06'), ('bebidas', 'Bebidas', '#3D67AE'), ('agave', 'Bebidas de agave', '#006D53'),
    ('farmacia', 'Farmacia', '#3D0066'), ('consultoria', 'Consultoría', '#052A76'),
]
toks = t['color']['tokens']
for c in toks:
    if c['name'] in STATE:
        c['value'], c['usage'] = STATE[c['name']]
toks[:] = [c for c in toks if not c['name'].startswith('div-')]
for k, n, v in DIV:
    toks.append({'name': f'div-{k}', 'value': v, 'usage': f'{n}: color de división del manual de Nisa Nabani. Solo identifica la división (azulejo del icono, filete o marca de documento). Nunca estado ni texto: el nombre de la división va en «text».'})
json.dump(t, open(f'{P}/tokens.json', 'w'), ensure_ascii=False, indent=1)

# ---------- vistas previas ----------
NEW = {k: v for k, (v, _) in STATE.items()}
def html(s):
    s = s.replace('family=Archivo:wdth,wght@62..125,100..900', 'family=Poppins:wght@400;500;600;700')
    s = s.replace('&family=Newsreader:ital,opsz,wght@1,6..72,400;1,6..72,500', '')
    s = s.replace('"Archivo"', '"Poppins"')
    s = s.replace('Archivo,sans-serif', 'var(--font-sans)')  # v1 escribía la familia a mano
    s = s.replace('.t1{margin:0;font:700 26px/32px var(--font-display);font-stretch:125%;letter-spacing:-.015em;',
                  '.t1{margin:0;font:600 24px/32px var(--font-display);letter-spacing:-.005em;')
    s = s.replace('font:italic 400 17px/24px var(--font-editorial)', 'font:400 15px/22px var(--font-sans)')
    s = s.replace('font:italic 400 22px/30px var(--font-editorial)', 'font:600 18px/26px var(--font-display)')
    # neutro y «dado de baja»: contorno, sin relleno, para no confundirse con «pendiente»
    s = s.replace('.e-baja{background:var(--surface-sunken);color:var(--text-muted)}',
                  '.e-baja{background:var(--surface);box-shadow:inset 0 0 0 1px var(--border-strong);color:var(--text-muted)}')
    s = s.replace('.e-neu{background:var(--surface-sunken,#F4F6FA);color:var(--text-muted,#535B70)}',
                  '.e-neu{background:var(--surface,#FFFFFF);box-shadow:inset 0 0 0 1px var(--border-strong,#CDD3DF);color:var(--text-muted,#535B70)}')
    for k, v in NEW.items():
        s = re.sub(r'var\(--' + k + r',\s*#[0-9A-Fa-f]{3,6}\)', f'var(--{k},{v})', s)
    return s

for d in sorted(os.listdir(f'{P}/components')):
    f = f'{P}/components/{d}/preview.html'
    s = open(f).read(); n = html(s)
    assert 'font-editorial' not in n and 'font-stretch' not in n and 'Archivo' not in n, d
    open(f, 'w').write(n)

# Poppins ocupa más que Archivo: tarjetas que crecen
for d, a, b in [('Campo', 'height=190 -->', 'height=240 -->'),
                ('TablaResultados', 'height=300 -->', 'height=320 width=860 -->'),
                ('TablaUsuarios', 'height=560 width=1100', 'height=580 width=1100')]:
    f = f'{P}/components/{d}/preview.html'; s = open(f).read()
    assert a in s.split('\n', 1)[0], d
    s = s.replace(a, b, 1)
    if d == 'TablaResultados':
        s = s.replace('<td style="padding:9px 12px;font-size:13px" class="mut">', '<td style="padding:9px 12px;font-size:13px;white-space:nowrap" class="mut">')
    open(f, 'w').write(s)

# ---------- documentos ----------
def md(path, pairs):
    f = f'{P}/{path}'; s = open(f).read()
    for a, b in pairs:
        assert a in s, (path, a); s = s.replace(a, b)
    open(f, 'w').write(s)

md('README.md', [
    ('- **Dos voces tipográficas.** Archivo habla (títulos, etiquetas, texto)', '- **Dos voces tipográficas.** Poppins habla (títulos, etiquetas, texto), como en el manual de Nisa Nabani'),
    ('- **Nada depende solo del color.**', '- **División no es estado.** Los colores secundarios del manual identifican divisiones; los estados tienen colores propios que no se confunden con ninguna.\n- **Nada depende solo del color.**'),
    ('- Estados de resultado: `conforme` (verde del laboratorio #006D53), `fuera` (#B42318), `alerta` (texto #8A4B00; el naranja del laboratorio #F48C06 solo como relleno) y `pendiente` (azul secundario #3D67AE). Cada uno con su fondo `*-soft` y su texto `on-*-soft`.',
     '- Estados: `conforme` (#2E7D32), `fuera` (#B42318), `alerta` (texto #8A6100, relleno #E9B10A) y `pendiente` (pizarra #475467). Cada uno con su fondo `*-soft` y su texto `on-*-soft`. Ninguno reutiliza un color de división.\n- Divisiones (`div-*`): los ocho secundarios del manual, uno por división (Aguas #00B4D8, Agrícolas #553739, Ambiental #38B000, Alimentos #F48C06, Bebidas #3D67AE, Bebidas de agave #006D53, Farmacia #3D0066, Consultoría #052A76). Solo en el azulejo del icono y en marcas de documento; el nombre siempre en `text`, porque cuatro de ellos no llegan a 4.5:1 como texto. Ver el componente «Divisiones».'),
    ('- **Archivo** (`display`, `sans`). Una sola familia variable en dos anchos: 125 % y 700 en `display` y `title-1`, la misma voz del wordmark; ancho normal en todo lo demás. 15 px de cuerpo para pantallas densas.',
     '- **Poppins** (`display`, `sans`). La tipografía del manual de Nisa Nabani para títulos, subtítulos y textos. 700 solo en `display`; 600 en títulos y botones; 400 en texto. 14 px de cuerpo: su x-height alta lee como 15 px de otras familias.'),
    ('- **Newsreader itálica** (`editorial`). La voz editorial: entradillas y lemas cortos (`entradilla` 17/24, `lema` 22/31). Nunca en controles, tablas ni datos; como máximo una por pantalla.\n', ''),
    ('- Se cargan de Google Fonts: `Archivo:wdth,wght@62..125,100..900`, `IBM Plex Mono:wght@400;500;600` y `Newsreader:ital,opsz,wght@1,6..72,400..500`.',
     '- **IBM Plex Mono** se conserva aunque el manual no la incluye: el manual no cubre datos tabulares y Poppins no alinea cifras en columna.\n- Se cargan de Google Fonts: `Poppins:wght@400;500;600;700` e `IBM Plex Mono:wght@400;500;600`.'),
])
md('valores.md', [('y el texto corrido van en Archivo.', 'y el texto corrido van en Poppins.')])
md('marca.md', [
    ('| Wordmark | «nabi» en Archivo 700 al 125 %, pocillo pera en la i |', '| Wordmark | «nabi» dibujado en trazos anchos (afín a la versal ancha del logo de Nisa Nabani), pocillo pera en la i. Es dibujo, no fuente de interfaz |'),
])
with open(f'{P}/marca.md', 'a') as f:
    f.write('''
## Nisa Nabani

Nabi es producto de Nisa Nabani y conserva su símbolo propio. La marca madre se rige por su manual (2026):

- **Logo:** la N en onda con el matraz, en azul real y pera, junto a «NISA NABANI» en versal ancha. Va en certificados, membretes y documentos para clientes, nunca dentro de la interfaz de trabajo.
- **Lema:** «Calidad para el desarrollo empresarial.» con el punto en pera.
- **Divisiones:** Aguas, Agrícolas, Ambiental, Alimentos, Bebidas, Bebidas de agave, Farmacia y Consultoría. Cada una tiene color e icono propios (tokens `div-*`, componente «Divisiones»). En el azulejo de Bebidas de agave el pera es fondo de marca, no la muestra en curso.
- **Membrete:** folio con prefijo NN + código de división (ejemplo del manual: NNAG-1254) y fecha en mayúsculas.

Pendiente: el manual no da la tabla completa de códigos de división para los folios (el ejemplo NNAG aparece en Aguas y en Agrícolas).
''')
md('modulos.md', [
    ('| Ruta | `label` (Archivo 500 13/18) |', '| Ruta | `label` (Poppins 500 13/18) |'),
    ('| Título del módulo | Archivo 700 al 125 %, 26/32 (`title-1` ampliado) |', '| Título del módulo | Poppins 600 24/32 (`title-1` ampliado) |'),
    ('| Entradilla | `entradilla` (Newsreader itálica 17/24) |', '| Entradilla | `body` ampliado (Poppins 400 15/22, `text-muted`) |'),
    ('| Nombre en tabla | Archivo 600 15/22 |', '| Nombre en tabla | Poppins 600 14/20 |'),
    ('lo que se lee, en Archivo.', 'lo que se lee, en Poppins.'),
    ('| Fuera de uso | `surface-sunken` / `text-muted` | Dado de baja · Recibida |', '| Fuera de uso o neutro | contorno `border-strong` sobre `surface` / `text-muted` | Dado de baja · Recibida |'),
    ('Siempre icono + palabra. El pera no es un estado.', 'Siempre icono + palabra. El pera no es un estado, y ningún color de división (`div-*`) se usa como estado.\n\nLa columna **Divisiones** muestra el azulejo de 16 px de cada división y su nombre en `text`; el color identifica la división, nunca su estado.'),
])
for path, pairs in {
    'components/Boton/README.md': [('Texto `button` en Archivo.', 'Texto `button` en Poppins.')],
    'components/Campo/README.md': [('El texto va en Archivo;', 'El texto va en Poppins;')],
    'components/IdMuestra/README.md': [('versalitas (Archivo)', 'versalitas (Poppins)')],
    'components/ResultadoAnalisis/README.md': [('`title-2` (Archivo)', '`title-2` (Poppins)')],
    'components/TablaResultados/README.md': [('nombres en Archivo,', 'nombres en Poppins,')],
    'components/TablaUsuarios/README.md': [('nombre en Archivo 600,', 'nombre en Poppins 600,')],
    'components/EncabezadoModulo/README.md': [
        ('(`title-1` ampliado: Archivo 700 al 125 %, 26/32)', '(`title-1` ampliado: Poppins 600, 24/32)'),
        ('(`entradilla`, Newsreader itálica, «text-muted»)', '(Poppins 400 15/22, «text-muted»)')],
    'components/EstadoUsuario/README.md': [
        ('verde = está bien, azul = pendiente, naranja = requiere atención, rojo = impedido, gris = fuera de uso.',
         'verde = está bien, pizarra = pendiente, ámbar = requiere atención, rojo = impedido, contorno sin relleno = fuera de uso. Ninguno es color de división.')],
}.items():
    md(path, pairs)

# ---------- componente Divisiones ----------
def svg(name, pref, h=None):
    s = open(f'{A}/{name}.svg').read()
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="{pref}-{m.group(1)}"', s)
    s = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{pref}-{m.group(1)})', s)
    s = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{pref}-{m.group(1)}"', s)
    s = re.sub(r' width="[^"]*" height="[^"]*"', '', s, 1)
    return s.replace('<svg', f'<svg aria-hidden="true" focusable="false"' + (f' style="height:{h}px;width:auto;display:block"' if h else ''), 1)

tiles = ''.join(f'<li><span class="tile">{svg("division-" + k, "d" + k)}</span>{n}</li>' for k, n, _ in DIV)
chips = ''.join(f'<span class="dv"><span class="tile s">{svg("division-" + k, "c" + k)}</span>{n}</span>' for k, n, _ in DIV[:3])
body = f'''<!-- @dsCard group="Marca" height=560 width=1000 -->
<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap"><style>
body{{margin:0;background:var(--bg);color:var(--text);font:400 14px/22px var(--font-sans);padding:var(--space-6)}}
.top{{display:flex;flex-wrap:wrap;align-items:center;gap:var(--space-6);padding-bottom:var(--space-5);border-bottom:1px solid var(--border)}}
.lema{{font:600 18px/26px var(--font-display);color:var(--primary);margin:0}} .lema b{{color:var(--pera)}}
h2{{font:600 11px/16px var(--font-sans);letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted);margin:var(--space-5) 0 var(--space-3)}}
ul{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:var(--space-3)}}
li{{display:flex;align-items:center;gap:var(--space-3);font:600 14px/20px var(--font-sans);background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-md);box-shadow:var(--shadow-1);padding:10px 12px}}
.tile{{width:36px;height:36px;flex:none;display:block}} .tile svg{{width:100%;height:100%;display:block}}
.tile.s{{width:16px;height:16px}}
.row{{display:flex;flex-wrap:wrap;gap:var(--space-2);align-items:center;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-md);padding:12px}}
.dv{{display:inline-flex;align-items:center;gap:6px;font:500 13px/18px var(--font-sans);color:var(--text);padding:3px 8px 3px 4px;border-radius:var(--radius-sm);background:var(--surface-sunken)}}
.note{{color:var(--text-muted);font-size:13px;margin:var(--space-2) 0 0}}
</style></head><body>
<div class="top">{svg("nisa-nabani-logo", "lg", 52)}<p class="lema">Calidad para el desarrollo empresarial<b>.</b></p></div>
<h2>Divisiones</h2><ul>{tiles}</ul>
<h2>En la interfaz</h2><div class="row">{chips}</div>
<p class="note">Azulejo de 16 px + nombre en «text». El color identifica la división; nunca indica estado.</p>
</body></html>'''
os.makedirs(f'{P}/components/Divisiones', exist_ok=True)
open(f'{P}/components/Divisiones/preview.html', 'w').write(body)
open(f'{P}/components/Divisiones/README.md', 'w').write('''# Divisiones

Las ocho divisiones de Nisa Nabani con el icono y el color de su manual (2026), y cómo aparecen dentro de Nabi.

- **Azulejo:** el icono del manual tal cual, en vector. 36 px en listas y encabezados de división; 16 px junto al nombre en tablas y filtros.
- **Nombre:** siempre en «text», nunca en el color de la división (Aguas, Ambiental, Alimentos y Bebidas de agave no llegan a 4.5:1 como texto sobre blanco).
- **Color:** tokens `div-*`. Identifica la división; nunca indica estado. Los estados usan `conforme`, `alerta`, `pendiente` y `fuera`.
- **Accesibilidad:** el azulejo es decorativo (`aria-hidden`) porque el nombre siempre lo acompaña. Por eso el glifo blanco sobre cian o naranja del manual se conserva aunque baje de 3:1.
- **Marca:** el logo de Nisa Nabani y el lema van en documentos para clientes, membretes y certificados, no dentro de las pantallas de trabajo.
''')

# ---------- columna Divisiones en las tablas de usuarios ----------
KEY = {n: k for k, n, _ in DIV}
CSS = ('.dvs{display:flex;flex-wrap:wrap;gap:4px 10px}.dv{display:inline-flex;align-items:center;gap:6px;white-space:nowrap}'
       '.dv svg{width:16px;height:16px;flex:none;display:block}\n')
n_ = [0]
def cell(m):
    names = m.group(1).split(' · ')
    if not all(x in KEY for x in names):
        return m.group(0)
    out = []
    for x in names:
        n_[0] += 1
        out.append(f'<span class="dv">{svg("division-" + KEY[x], f"t{n_[0]}")}{x}</span>')
    return '<td><span class="dvs">' + ''.join(out) + '</span></td><td class="dt">'
for d in ('TablaUsuarios', 'ModuloUsuarios'):
    f = f'{P}/components/{d}/preview.html'; s = open(f).read()
    s, k = re.subn(r'<td>([^<]+)</td><td class="dt">', cell, s)
    assert '.dvs{' not in s and '</style>' in s, d
    s = s.replace('</style>', CSS + '</style>', 1)
    open(f, 'w').write(s)
print('ok')
