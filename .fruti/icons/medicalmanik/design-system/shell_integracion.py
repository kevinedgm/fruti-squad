# Ecosistema Manik · integra al sistema de diseño el app shell r02 aprobado el 2026-11-05 (../shell-r02/).
# Paso idempotente sobre project/ (como controles_formularios.py; no usa build.py). Uso: python3 shell_integracion.py
import json, os, re, importlib.util, datetime
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, 'project'); M = os.path.join(D, '..')

tp = os.path.join(P, 'tokens.json'); T = json.load(open(tp))
def upsert(group, name, value, usage):
    toks = T[group]['tokens']
    for x in toks:
        if x['name'] == name: x.update(value=value, usage=usage); return
    toks.append({'name': name, 'value': value, 'usage': usage})
upsert('layout', 'sidebar-width', '264px', 'Barra lateral desplegada de las apps con 4 o más secciones.')
upsert('layout', 'rail-width', '72px', 'Barra lateral plegada (riel): solo iconos.')
upsert('layout', 'content-narrow', '1120px', 'Ancho máximo del contenido en apps pequeñas (2 o 3 secciones, con pestañas).')
upsert('layout', 'footer-height', '44px', 'Pie de cada app, dentro de la columna de contenido.')
upsert('layout', 'bp-cajon', '1024px', 'Por debajo, la barra lateral se vuelve cajón.')
upsert('layout', 'bp-celular', '640px', 'Por debajo, búsqueda como icono, sello sin nombre y tablas en filas.')
json.dump(T, open(tp, 'w'), indent=1, ensure_ascii=False)

s = importlib.util.spec_from_file_location('shr', os.path.join(M, 'shell-r02/gen.py')); S = importlib.util.module_from_spec(s); s.loader.exec_module(S)
CSS = S.HTML.split('<style>', 1)[1].split('</style>', 1)[0]
JS = S.JS
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700&display=swap">'
FIT = '''<script>(function(){const m=document.getElementById('marco');function fit(){const s=Math.min((innerWidth-32)/1180,(innerHeight-32)/760,1);m.style.zoom=s}fit();addEventListener('resize',fit)})();</script>'''

def preview(grp, h, app, riel=False, after=''):
    js = JS.replace("let app='expediente',riel=false,act=null;", f"let app='{app}',riel={'true' if riel else 'false'},act=null;")
    return (f'<!-- @dsCard group="{grp}" height={h} -->\n<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>{CSS}'
            'body{padding:16px;margin:0;background:var(--canvas)}.sh-marco{width:1180px;max-width:none!important;margin:0 auto}</style></head><body>'
            f'<div class="sh-marco" id="marco" data-ancho="esc"><div class="sh" id="sh"></div></div><script>{js}{after}</script>{FIT}</body></html>')

comps = {
 'AppShell': ('Patrones', 470, preview('Patrones', 470, 'expediente'),
 '''Esqueleto de las apps con 4 o más secciones: barra superior (EncabezadoApp), barra lateral (BarraLateral), contenido y pie. Aprobado 2026-11-05 (`../../shell-r02/`).

- **Rejilla:** barra superior de `header-height` a todo el ancho; debajo, `sidebar-width` (264 px) o `rail-width` (72 px) y la columna de contenido, que se desplaza sola.
- **Contenido:** migas «Módulo › Submódulo» cuando hay submódulo; encabezado de página (`title-1`, una línea de contexto en «muted», acciones a la derecha: secundaria y luego la principal); área de trabajo en «surface» con borde «line» y `radius-2xl`.
- **Pie** (`footer-height`, 44 px) dentro de la columna de contenido: app y versión, estado del sistema, aviso de privacidad, soporte; 13 px en «muted».
- **Tableta** (< `bp-cajon`): la barra lateral es un cajón desde la izquierda con botón de menú en la barra superior; velo `scrim`; se cierra con X, Esc o tocando fuera y el foco vuelve al botón.
- **Celular** (< `bp-celular`): búsqueda como icono, sello sin nombre, acciones de página a todo el ancho, tablas en filas de dos líneas.
- **Enlace «Saltar al contenido»** como primer elemento enfocable.
- **¿Qué navegación?** Se cuentan destinos, no acciones: 2 o 3 → AppPequena (pestañas); 4 a 7 → BarraLateral plana; módulos con submódulos → BarraLateral por módulos. Nunca tres niveles.'''),
 'BarraLateral': ('Navegación', 470, preview('Navegación', 470, 'expediente', True,
     "setTimeout(()=>{const b=document.querySelector('button[data-g=\"4\"]');if(b){b.click();const f=document.querySelector('.sh-fly');if(f){f.style.left='80px';const z=parseFloat(document.getElementById('marco').style.zoom)||1,q=document.getElementById('sh').getBoundingClientRect(),r=b.getBoundingClientRect();f.style.top=Math.round((r.top-q.top)/z)+'px'}document.activeElement.blur()}},300);"),
 '''Barra lateral de módulos y submódulos. Aprobada 2026-11-05.

- **Medidas:** `sidebar-width` 264 px, fondo «surface», borde derecho «line», relleno 12 px. Módulo: fila de 44 px, icono Lucide de 20 px en «muted», texto 15 px.
- **Submódulos:** el módulo que los tiene es un `<button aria-expanded aria-controls>` con flecha (no un enlace); sus submódulos cuelgan de una línea guía de 1.5 px «line», sin icono, en filas de 40 px y texto «muted». Solo se abre el grupo de la página actual; los demás, cuando la persona los abre. Dos niveles como máximo.
- **Dónde estoy:** la página actual en «manik-soft», texto «manik» 600 y `aria-current="page"`; su módulo padre en 600 con el icono en «manik».
- **Pendientes:** contador en píldora «manik-soft» con texto «manik» y `aria-label` («3 pendientes»). Un grupo cerrado muestra la suma de sus submódulos.
- **Pie de la barra:** Ayuda y «Plegar menú».
- **Riel** (`rail-width`, 72 px): solo iconos; el nombre aparece en una etiqueta flotante al pasar o enfocar; los pendientes, como punto. Un módulo con submódulos abre un menú flotante (`shadow-pop`) con su título y sus submódulos; Esc lo cierra y devuelve el foco. La preferencia de riel se recuerda por persona.
- **Tableta y celular:** la misma barra, como cajón de 300 px (ver AppShell).'''),
 'AppPequena': ('Patrones', 470, preview('Patrones', 470, 'impulsa'),
 '''La alternativa para apps de 2 o 3 secciones (por ejemplo, Impulsa: Campañas y Resultados). Aprobada 2026-11-05.

- **Sin barra lateral:** 264 px para dos enlaces harían ver la app más grande de lo que es.
- **Pestañas bajo la barra superior,** a todo el ancho en «surface» con borde «line»: icono de 18 px y texto 15 px 600; la actual en «manik» con subrayado de 3 px. Son destinos: `<nav>` con enlaces y `aria-current="page"`, no `role="tab"`.
- **Las acciones no son pestañas:** «Nueva campaña» es el botón principal del encabezado de página.
- **Contenido centrado** a `content-narrow` (1120 px); mismo encabezado de página, área de trabajo y pie que AppShell.
- **Celular:** las pestañas se reparten el ancho; no hay cajón ni barra inferior.
- **Si la app crece** a 4 secciones o más, pasa a BarraLateral plana; no se suman pestañas.'''),
}
for name, (grp, h, html, md) in comps.items():
    os.makedirs(os.path.join(P, 'components', name), exist_ok=True)
    open(os.path.join(P, 'components', name, 'preview.html'), 'w').write(html)
    open(os.path.join(P, 'components', name, 'README.md'), 'w').write(f'# {name}\n\n{md}\n')

# EncabezadoApp: suma el botón de menú y el comportamiento por ancho
ep = os.path.join(P, 'components', 'EncabezadoApp', 'README.md'); E = open(ep).read()
NOTA = '\n- **Por ancho (2026-11-05):** por debajo de `bp-cajon` aparece a la izquierda el botón de menú que abre el cajón de la barra lateral (`aria-expanded`, `aria-controls`); por debajo de `bp-celular` la búsqueda pasa a botón con lupa y el sello va sin nombre. El nombre y el rol del usuario se ocultan por debajo de `bp-cajon`; el avatar queda.\n'
if 'Por ancho (2026-11-05)' not in E: E = E.rstrip('\n') + '\n' + NOTA
open(ep, 'w').write(E)

rp = os.path.join(P, 'README.md'); R = open(rp).read()
SEC = '''## App shell (aprobado 2026-11-05)

Un mismo esqueleto en las siete apps y dos formas de navegar según su tamaño. Ronda: `../../shell-r02/`.

- **Componentes:** EncabezadoApp, AppShell, BarraLateral y AppPequena.
- **¿Qué navegación?** Se cuentan destinos, no acciones: 2 o 3 → pestañas (AppPequena); 4 a 7 → barra lateral plana; módulos con submódulos → barra lateral por módulos. Dos niveles como máximo.
- **Barra lateral** de 264 px (riel de 72), submódulos desplegables sin icono colgando de una línea guía, la página actual en «manik-soft» con `aria-current`.
- **Pie** de 44 px dentro de la columna de contenido.
- **Tableta:** cajón con velo. **Celular:** búsqueda como icono, tablas en filas.
- **Apps pequeñas:** pestañas bajo la barra superior y contenido centrado a 1120 px.

'''
R = re.sub(r'## App shell \(aprobado.*?(?=\n## )\n', '', R, flags=re.S)
R = R.replace('## Iconografía', SEC + '## Iconografía', 1)
open(rp, 'w').write(R)

jp = os.path.join(P, 'design-system.json'); J = json.load(open(jp))
J['lastChange'] = {'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'by': 'Kevin', 'via': 'Claude Code',
                   'note': 'App shell aprobado: AppShell, BarraLateral (módulos y submódulos, riel) y AppPequena (pestañas para apps de 2 o 3 secciones); EncabezadoApp por ancho; tokens sidebar-width, rail-width, content-narrow, footer-height, bp-cajon y bp-celular.'}
json.dump(J, open(jp, 'w'), indent=2, ensure_ascii=False)
print('ok', sorted(comps))
