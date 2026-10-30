"""Nabi → NisaLab. Tercer paso de la cadena: modulos.py → marca-nisa.py → marca-nisalab.py.

Uso: python3 marca-nisalab.py <carpeta-project>
Aplica la marca aprobada (2026-10-30): nombre NisaLab, símbolo Colonia (nisalab-final), áreas con paleta e íconos propios
(nisalab-areas-final) en lugar de los colores e íconos de división del manual. Los assets ya están subidos al artifact:
blobs-nisalab.json guarda sus ids.
"""
import json, os, re, shutil, sys

P = sys.argv[1]
H = os.path.dirname(os.path.abspath(__file__))
NS = os.path.join(H, '..')
AREAS_F = os.path.join(NS, 'nisalab-areas-final')
FINAL = os.path.join(NS, 'nisalab-final')
BL = json.load(open(os.path.join(H, 'blobs-nisalab.json')))
TEMA = json.load(open(os.path.join(AREAS_F, 'tema.json')))['paleta']['areas']
blob = lambda n: f'/_blob/{BL["marca"][n]}'

def sv(ruta, h, extra=''):
    s = open(ruta).read().strip()
    s = re.sub(r'<title>.*?</title>', '', s)
    s = s.replace(' role="img"', ' aria-hidden="true"')
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block;flex:none{extra}" ', 1)
_u = [0]
def uniq(s):
    _u[0] += 1; u = f'-n{_u[0]}'
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="{m.group(1)}{u}"', s)
    return re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{m.group(1)}{u})', s)
icono = lambda k, h: uniq(sv(os.path.join(AREAS_F, 'svg', k, 'icono.svg'), h))
marca_area = lambda k, h: uniq(sv(os.path.join(AREAS_F, 'svg', k, 'marca.svg'), h))
POR_NOMBRE = {v['nombre']: k for k, v in TEMA.items()}

# ---------- tokens ----------
t = json.load(open(f'{P}/tokens.json'))
t['name'] = 'NisaLab'
toks = t['color']['tokens']
toks[:] = [c for c in toks if not c['name'].startswith('div-')]
for c in toks:
    if c['name'] == 'pera':
        c['usage'] = 'La célula que creció del símbolo Colonia y lo que está en curso: la muestra activa, el registro que se edita. Una sola cosa pera por pantalla. Nunca texto (1.7:1 sobre blanco).'
for k, v in TEMA.items():
    toks.append({'name': v['token'], 'value': v['hex'],
                 'usage': f'{v["nombre"]}: color del área en NisaLab (paleta OKLCH 0.54 · 0.12). Solo identifica el área, en su ícono y su marca; nunca estado. Blanco encima {v["blanco_encima"]}:1.'})
for grupo in ('sizing', 'motion'):
    for c in t.get(grupo, {}).get('tokens', []):
        if c['name'] == 'pozo':
            c['usage'] = 'Punto de estado de 10 px en tablas, del color del estado y junto a su texto.'
        if c['name'] == 'paso-carga':
            c['usage'] = 'Cada paso de la carga: las células de Colonia aparecen una tras otra y la pera crece al final.'
json.dump(t, open(f'{P}/tokens.json', 'w'), ensure_ascii=False, indent=1)

# ---------- componentes ----------
def lee(c): return open(f'{P}/components/{c}/preview.html').read()
def escribe(c, s): open(f'{P}/components/{c}/preview.html', 'w').write(s)
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">'

# textos de ejemplo
for c in ('EncabezadoModulo', 'ModuloUsuarios'):
    escribe(c, lee(c).replace('Quién entra a Nabi', 'Quién entra a NisaLab'))

# columna Divisiones: íconos de área en lugar de los azulejos del manual
def cambia_dv(m):
    nombre = m.group(2).strip()
    k = POR_NOMBRE.get(nombre)
    return f'<span class="dv">{icono(k, 16)}{m.group(2)}</span>' if k else m.group(0)
for c in ('TablaUsuarios', 'ModuloUsuarios'):
    s = re.sub(r'<span class="dv">(<svg.*?</svg>)([^<]+)</span>', cambia_dv, lee(c), flags=re.S)
    escribe(c, s)

# portada
logo = sv(os.path.join(FINAL, 'svg', 'logotipo-respaldo.svg'), 64)
sim = sv(os.path.join(FINAL, 'svg', 'simbolo.svg'), 232)
escribe('Cover', f'''<!-- @dsCard height=288 -->
<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>
html,body{{margin:0;height:100%}} body{{background:var(--bg,#F2F4F8);color:var(--text,#141B33);font-family:var(--font-sans,"Poppins",system-ui,sans-serif);overflow:hidden}}
.c{{position:relative;height:288px;padding:0 var(--space-6,24px);display:flex;align-items:center;justify-content:space-between;gap:24px;overflow:hidden}}
.w{{display:grid;gap:14px;max-width:440px}} .tag{{margin:0;font-size:14px;line-height:20px;color:var(--text-muted,#535B70)}} .tag .d{{font-family:var(--font-datos,"IBM Plex Mono",monospace);font-feature-settings:"zero";color:var(--text,#141B33)}}
.s{{flex:none;margin-right:12px}}
</style></head><body><div class="c"><div class="w">{logo}<p class="tag">Sistema de laboratorio · muestras, lotes, resultados, certificados · <span class="d">pH 7.42 ± 0.05</span></p></div><div class="s">{sim}</div></div></body></html>''')

# carga: las células aparecen una tras otra y la pera crece al final
sim_s = open(os.path.join(FINAL, 'svg', 'simbolo.svg')).read()
cel = re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)" fill="([^"]+)"', sim_s)
orden = sorted(range(len(cel)), key=lambda i: (cel[i][3] == '#C2D225', float(cel[i][2])))  # de la más chica a la grande; la pera al final
circ = ''.join(f'<circle class="k k{orden.index(i)}" cx="{x}" cy="{y}" r="{r}" fill="{f}"/>' for i, (x, y, r, f) in enumerate(cel))
carga_svg = (f'<svg viewBox="-2 -2 104 104" width="56" height="56" aria-hidden="true"><style>.k{{transform-box:fill-box;transform-origin:center;animation:cg 1.6s var(--ease-out,cubic-bezier(.2,.8,.2,1)) infinite}}'
             + ''.join(f'.k{i}{{animation-delay:{i * 0.2:.1f}s}}' for i in range(len(cel)))
             + '@keyframes cg{0%{transform:scale(.4);opacity:.25}25%,70%{transform:scale(1);opacity:1}100%{transform:scale(.4);opacity:.25}}'
             + '@media (prefers-reduced-motion:reduce){.k{animation:none}}</style>' + circ + '</svg>')
s = lee('Carga')
s = re.sub(r'<svg width="56".*?</svg>', lambda m: carga_svg, s, count=1, flags=re.S)
escribe('Carga', s)

# áreas (sustituye a Divisiones)
os.makedirs(f'{P}/components/Areas', exist_ok=True)
filas = ''.join(f'<li>{marca_area(k, 40)}<span><b>{v["nombre"]}</b> NisaLab<small>{v["hex"]} · {v["token"]}</small></span></li>' for k, v in TEMA.items())
chips = ''.join(f'<span class="dv">{icono(k, 16)}{v["nombre"]}</span>' for k, v in list(TEMA.items())[:4])
open(f'{P}/components/Areas/preview.html', 'w').write(f'''<!-- @dsCard group="Marca" height=560 width=1000 -->
<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>
body{{margin:0;background:var(--bg,#F2F4F8);color:var(--text,#141B33);font:400 14px/22px var(--font-sans,"Poppins",sans-serif);padding:var(--space-6,24px)}}
.top{{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;padding-bottom:var(--space-5,20px);border-bottom:1px solid var(--border,#DFE3EC)}}
h2{{font:600 11px/16px var(--font-sans,"Poppins",sans-serif);letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted,#535B70);margin:var(--space-5,20px) 0 var(--space-3,12px)}}
ul{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:var(--space-3,12px)}}
li{{display:flex;align-items:center;gap:var(--space-3,12px);background:var(--surface,#fff);border:1px solid var(--border,#DFE3EC);border-radius:var(--radius-md,8px);box-shadow:var(--shadow-1,none);padding:10px 12px;color:var(--text-muted,#535B70)}}
li b{{color:var(--text,#141B33);font-weight:600}} li small{{display:block;font:500 11px/16px var(--font-datos,"IBM Plex Mono",monospace);color:var(--text-muted,#535B70)}}
.row{{display:flex;flex-wrap:wrap;gap:var(--space-2,8px);align-items:center;background:var(--surface,#fff);border:1px solid var(--border,#DFE3EC);border-radius:var(--radius-md,8px);padding:12px}}
.dv{{display:inline-flex;align-items:center;gap:6px;font:500 13px/18px var(--font-sans,"Poppins",sans-serif);padding:3px 10px 3px 4px;border-radius:999px;background:var(--surface-sunken,#EEF1F6)}}
.note{{color:var(--text-muted,#535B70);font-size:13px;margin:var(--space-2,8px) 0 0}}
</style></head><body><div class="top">{sv(os.path.join(FINAL, 'svg', 'logotipo-respaldo.svg'), 48)}<span class="note" style="margin:0">Cada área: la célula que creció toma su color y su ícono.</span></div>
<h2>Áreas</h2><ul>{filas}</ul><h2>En la interfaz</h2><div class="row">{chips}</div>
<p class="note">Ícono de 16 px + nombre. El color identifica el área; nunca indica estado.</p></body></html>''')
open(f'{P}/components/Areas/README.md', 'w').write('''# Areas

Las ocho áreas (divisiones) de Nisa Nabani dentro de NisaLab: «Área NisaLab». La célula que creció de Colonia toma el color y el ícono del área; el resto del racimo sigue azul real.

- **Color:** tokens `area-*`. Paleta OKLCH con la misma luminosidad (0.54) e intensidad (0.12); solo cambia el tono, fuera del rango del pera. Blanco encima de 4.6 a 5.4:1.
- **Ícono:** dibujado en retícula de 40, formas redondas y blancas. 16 px junto al nombre en tablas y filtros; 40 px en listas y encabezados de área.
- **Nombre:** siempre acompaña a la marca o al ícono; a 24 px lo que se lee es el color.
- **Nunca estado:** los estados usan `conforme`, `alerta`, `pendiente` y `fuera`.
- **Archivos:** grupo de assets «Áreas» (marca e ícono por área). El paquete completo vive en `nisalab-areas-final/`.
''')
shutil.rmtree(f'{P}/components/Divisiones', ignore_errors=True)

# ---------- documentos ----------
def md(path, pares):
    f = f'{P}/{path}'; s = open(f).read()
    for a, b in pares:
        assert a in s, (path, a[:60]); s = s.replace(a, b)
    open(f, 'w').write(s)

md('README.md', [
    ('# Nabi\n\nNabi es el sistema de laboratorio de Nisa Nabani', '# NisaLab\n\nNisaLab es el sistema de laboratorio de Nisa Nabani'),
    ('![Lockup de Nabi](/_blob/3534ef111e16fe05c60c372a3d61e030)', f'![NisaLab de Nisa Nabani]({blob("logotipo-respaldo.svg")})'),
    ('- **Una sola muestra pera.** El pera marca lo que está en curso: la muestra activa, la fila seleccionada, el pocillo del símbolo. Si hay dos cosas en pera, una sobra.',
     '- **Una sola cosa pera.** El pera marca lo que está en curso: la muestra activa, el registro que se edita, la célula que creció del símbolo. Si hay dos cosas en pera, una sobra.'),
    ('- **División no es estado.** Los colores secundarios del manual identifican divisiones; los estados tienen colores propios que no se confunden con ninguna.',
     '- **Área no es estado.** Los colores de área identifican cada división dentro de NisaLab; los estados tienen colores propios.'),
    ('- `pera` (#C2D225) es la muestra: el pocillo del símbolo y la muestra activa.', '- `pera` (#C2D225) es lo que está en curso: la célula que creció del símbolo y la muestra activa.'),
    ('Ninguno reutiliza un color de división.', 'Ninguno es color de área.'),
    ('- Divisiones (`div-*`): los ocho secundarios del manual, uno por división (Aguas #00B4D8, Agrícolas #553739, Ambiental #38B000, Alimentos #F48C06, Bebidas #3D67AE, Bebidas de agave #006D53, Farmacia #3D0066, Consultoría #052A76). Solo en el azulejo del icono y en marcas de documento; el nombre siempre en `text`, porque cuatro de ellos no llegan a 4.5:1 como texto. Ver el componente «Divisiones».',
     '- Áreas (`area-*`): ocho colores propios de NisaLab con la misma luminosidad e intensidad (OKLCH 0.54 · 0.12), uno por área: ' + ', '.join(f'{v["nombre"]} {v["hex"]}' for v in TEMA.values()) + '. Solo en el ícono y la marca del área; blanco encima de 4.6 a 5.4:1. Ver el componente «Areas».'),
    ('Radios contenidos: 6, 8 y 12 px; la píldora solo para pocillos y puntos de estado.', 'Radios contenidos: 6, 8 y 12 px; la píldora solo para puntos de estado, etiquetas de área y avatares.'),
    ('La carga es el símbolo: la muestra pera recorre la N, 200 ms por paso (`paso-carga`). Con `prefers-reduced-motion` se detiene en el pocillo final. Todo lo demás es `quick` (150 ms).\n\n![Carga](/_blob/6358d06d47e59e7d479475ad1ab7587b)',
     'La carga es el símbolo: las células de Colonia aparecen una tras otra, 200 ms por paso (`paso-carga`), y la pera crece al final. Con `prefers-reduced-motion` el símbolo queda quieto. Todo lo demás es `quick` (150 ms).'),
    ('- El pocillo es el átomo gráfico: los estados en tablas se marcan con un pocillo de 10 px (`pozo`) del color del estado, junto al texto.\n- Símbolo, wordmark y lockups en la sección «Marca» y en el grupo de assets «Marca».',
     '- La célula es el átomo gráfico: los estados en tablas se marcan con un punto de 10 px (`pozo`) del color del estado, junto al texto.\n- Símbolo, logotipos e íconos en la sección «Marca» y en los grupos de assets «Marca» y «Áreas».'),
])
md('modulos.md', [
    ('ma una pantalla de módulo en Nabi', 'ma una pantalla de módulo en NisaLab'),
    ('un pocillo `pera` junto al nombre', 'un punto `pera` junto al nombre'),
    ('el registro en curso recibe el pocillo pera', 'el registro en curso recibe el punto pera'),
    ('y ningún color de división (`div-*`) se usa como estado.', 'y ningún color de área (`area-*`) se usa como estado.'),
    ('La columna **Divisiones** muestra el azulejo de 16 px de cada división y su nombre en `text`; el color identifica la división, nunca su estado.',
     'La columna **Divisiones** muestra el ícono de área de 16 px y su nombre en `text`; el color identifica el área, nunca su estado.'),
])
md('components/ModuloUsuarios/README.md', [('módulo de administración de Nabi', 'módulo de administración de NisaLab')])
md('components/TablaResultados/README.md', [('lleva fondo «pera-soft» y pocillo pera', 'lleva fondo «pera-soft» y punto pera')])
open(f'{P}/components/Carga/README.md', 'w').write('''# Carga

Indicador de carga y proceso: el símbolo Colonia de NisaLab, con sus células apareciendo una tras otra y la pera al final.

- Un paso de 200 ms por célula (`paso-carga`), en bucle. Con `prefers-reduced-motion` el símbolo queda quieto.
- A 56 px en estados de carga de página o de proceso largo, con texto de qué se procesa y el avance en `datos`. A 16–20 px dentro de botones.
- No usar un spinner genérico en el sistema.
- El consumidor provee: el texto de la tarea y, si se conoce, el avance.
''')
open(f'{P}/marca.md', 'w').write(f'''# Marca

NisaLab es el sistema de laboratorio de Nisa Nabani. Se escribe «NisaLab», junto y con dos mayúsculas; como respaldo, «de Nisa Nabani».

![NisaLab]({blob("logotipo.svg")})

## Símbolo: Colonia

Cuatro células que casi se tocan, con la misma separación entre ellas y una proporción fija (1.0 · 1.7 · 2.9 · 3.7). Una sola en pera, arriba a la derecha: la que creció. Lo vivo que el laboratorio detecta, cuenta y certifica.

## Piezas

| Pieza | Uso | Archivo |
|---|---|---|
| Símbolo | Encabezado, carga, sellos | `simbolo.svg` · `simbolo-1tinta.svg` · `simbolo-blanco.svg` |
| Logotipo | «Nisa» en Poppins 700 y «Lab» en 400, a trazos | `logotipo.svg` · `logotipo-blanco.svg` |
| Con respaldo | Certificados, documentos para clientes, portada | `logotipo-respaldo.svg` |
| Vertical | Pantalla de acceso | `logotipo-vertical.svg` |
| Ícono de app | PWA | `app-icon.svg` · `app-icon-maskable.svg` · `app-icon-512.png` |
| Favicon | 16–32 px | `favicon.svg` |

## Áreas

Cada división es «Área NisaLab» (por ejemplo, «Aguas NisaLab»): la célula que creció toma el color y el ícono del área. Ver el componente «Areas» y el grupo de assets «Áreas».

## Reglas

- El racimo es fijo: no se rota, no se reacomoda, no se le quitan ni agregan células.
- Una sola célula pera. El pera nunca es texto.
- Área de respeto: el ancho de la célula grande. Mínimo 16 px en pantalla y 6 mm impreso.
- El logo de Nisa Nabani y el de NisaLab no se unen en una sola pieza: NisaLab lleva «de Nisa Nabani».
''')
print('ok')
