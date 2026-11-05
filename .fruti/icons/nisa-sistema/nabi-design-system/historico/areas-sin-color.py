# ── HISTÓRICO (2026-11-05) ──────────────────────────────────────────────
# Este script ya corrió y produjo una versión anterior del design system.
# Hoy escribiría colores retirados o archivos viejos sobre el estado actual.
# Fuente de verdad actual: tokens.json, README.md y components/ (versión 19).
import os as _os, sys as _sys
if _os.environ.get('NISALAB_HISTORICO') != '1':
    _sys.exit('Script histórico: no se corre sobre el design system actual. Ver historico/LEEME.md. '
              'Para ejecutarlo a propósito (por ejemplo, para reproducir el pasado en una copia): NISALAB_HISTORICO=1 python3 ' + _sys.argv[0])
# ─────────────────────────────────────────────────────────────────────────
# NisaLab · regla del usuario: los colores de área nunca aparecen en tablas (en una tabla, todo color es estatus).
# En tablas el área va con su ícono a una tinta en «text-muted» + nombre. El color del área queda para su marca y el encabezado de su página.
# Uso: python3 areas-sin-color.py <project>   (después de encabezado-area.py)
import json, os, re, sys
P = sys.argv[1]; NS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
AF = os.path.join(NS, 'nisalab-areas-final')
TEMA = json.load(open(os.path.join(AF, 'tema.json')))
TEMA = TEMA['paleta']['areas']
POR = {v['nombre']: k for k, v in TEMA.items()}
n = [0]
def tinta(k):
    s = open(os.path.join(AF, 'svg', k, 'icono-1tinta.svg')).read().strip()
    s = re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', s); n[0] += 1; u = f'-t{n[0]}'
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="{m.group(1)}{u}"', s); s = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{m.group(1)}{u})', s)
    return s.replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
def cambia(m):
    k = POR.get(m.group(2).strip()); return f'<span class="dv">{tinta(k)}{m.group(2)}</span>' if k else m.group(0)
for c in ('TablaUsuarios', 'ModuloUsuarios'):
    f = os.path.join(P, 'components', c, 'preview.html'); h = open(f).read()
    h = re.sub(r'<span class="dv">(<svg.*?</svg>)([^<]+)</span>', cambia, h, flags=re.S)
    if '.dv svg{color' not in h: h = h.replace('</style>', '.dv svg{color:var(--text-muted)}</style>', 1)
    open(f, 'w').write(h)
def rep(rel, a, b):
    f = os.path.join(P, rel); s = open(f).read()
    if a in s: open(f, 'w').write(s.replace(a, b))
    elif b not in s: print('NO ENCONTRADO', rel, a[:50])
REGLA = 'Nunca en tablas: en una tabla todo color es estatus; ahí el área va con su ícono a una tinta en «text-muted» y su nombre.'
rep('README.md', 'Solo en el ícono y la marca del área; blanco encima', 'Solo en la marca del área, el encabezado de su página y los filtros; nunca en tablas. Blanco encima')
rep('modulos.md', 'La columna **Divisiones** muestra el ícono de área de 16 px y su nombre en `text`; el color identifica el área, nunca su estado.',
    'La columna **Divisiones** muestra el ícono de área a una tinta (16 px, `text-muted`) y su nombre en `text`. Los colores de área nunca aparecen en tablas: ahí todo color es estatus.')
rep('components/Areas/README.md', '- **Nunca estado:**', f'- **{REGLA}**\n- **Nunca estado:**')
rep('components/Areas/README.md', '16 px junto al nombre en tablas y filtros', '16 px junto al nombre en filtros; en tablas, la versión a una tinta')
t = json.load(open(os.path.join(P, 'tokens.json')))
for c in t['color']['tokens']:
    if c['name'].startswith('area-') and 'Nunca en tablas' not in c['usage']:
        c['usage'] = c['usage'].replace('nunca estado.', 'nunca estado. Nunca en tablas.')
json.dump(t, open(os.path.join(P, 'tokens.json'), 'w'), ensure_ascii=False, indent=1)
print('ok', n[0])
