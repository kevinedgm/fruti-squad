# NisaLab · EncabezadoModulo gana la variante «por área» (opción B aprobada en nisalab-encabezados-r1).
# Uso: python3 encabezado-area.py <project>   (después de marca-nisalab.py)
import os, re, sys
P = sys.argv[1]; H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..')
C = os.path.join(P, 'components', 'EncabezadoModulo')
h = open(os.path.join(C, 'preview.html')).read()
marca = open(os.path.join(NS, 'nisalab-areas-final', 'svg', 'aguas', 'marca.svg')).read().strip()
marca = re.sub(r'<title>.*?</title>', '', marca).replace('<svg ', '<svg class="am" aria-hidden="true" focusable="false" ', 1)
marca = re.sub(r' role="img"| aria-label="[^"]*"', '', marca)
ic = re.findall(r'<svg[^>]*class="i".*?</svg>', h, flags=re.S)
printer = ('<svg class="i" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 9V3h12v6"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8" rx="1"/></svg>')
plus = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 12h14"/><path d="M12 5v14"/></svg>'
css = '''
/* variante por área: marca del área + línea de su color */
.lbl{font:600 11px/14px var(--font-sans);letter-spacing:.06em;text-transform:uppercase;color:var(--text-subtle);margin:0 0 var(--space-3)}
.lbl+.mh{margin-bottom:var(--space-8)}
.mh.area{grid-template-columns:auto minmax(0,1fr) auto;column-gap:var(--space-4);border-bottom:3px solid var(--ac);padding-bottom:var(--space-4)}
.mh.area .crumb{grid-column:2/-1}
.mh.area .am{grid-row:2;width:52px;height:52px;align-self:center}
.t1 .an{font-weight:400;color:var(--text-muted)}
@media (max-width:640px){.mh.area{grid-template-columns:auto minmax(0,1fr)}.mh.area .am{width:40px;height:40px;align-self:start;margin-top:2px}.mh.area .acts{grid-column:1/-1}}
'''
if '.mh.area' not in h:
    h = h.replace('</style>', css + '</style>', 1)
    i = h.index('<header class="mh">')
    area = (f'<p class="lbl">Por área</p><header class="mh area" style="--ac:var(--area-aguas)"><nav class="crumb" aria-label="Ruta"><a href="#">Recepción</a><span aria-hidden="true">/</span><span aria-current="page">Aguas</span></nav>'
            f'{marca}<div><h1 class="t1">Recepción de muestras <span class="an">Aguas</span></h1><p class="cnt"><b>12</b> muestras hoy · <b>3</b> por etiquetar</p></div>'
            f'<div class="acts"><button class="btn btn-s">{printer}Imprimir etiquetas</button><button class="btn btn-p">{plus}Registrar muestra</button></div></header>')
    h = h[:i] + '<p class="lbl">Global</p>' + h[i:].replace('</header>', '</header>' + area, 1)
    h = h.replace('@dsCard group="Módulos" height=190', '@dsCard group="Módulos" height=420 width=1000', 1)
    open(os.path.join(C, 'preview.html'), 'w').write(h)

R = os.path.join(C, 'README.md'); r = open(R).read()
r = r.replace('- **Título** (`title-1` ampliado: Poppins 600, 24/32): el nombre del módulo en plural, sin icono. El icono del módulo vive en el menú lateral; repetirlo junto al título no agrega información.',
              '- **Título** (`title-1` ampliado: Poppins 600, 24/32): el nombre del módulo, sin icono. El icono del módulo vive en el menú lateral; repetirlo junto al título no agrega información. Excepción: la variante por área (abajo).')
if '## Variante por área' not in r:
    r += '''
## Variante por área

Para páginas que trabajan dentro de un área (Recepción, Bitácora y Resultados de Aguas, Alimentos, Bebidas…). Su trabajo es que nadie capture en el área equivocada: el área se reconoce de lejos, sin leer.

- **Marca del área** (Colonia con la célula del área, 52 px; 40 px bajo 640) a la izquierda del título. Es decorativa (`aria-hidden`): el nombre del área ya está en el título y en la ruta.
- **Título**: la tarea + el nombre del área en Poppins 400 «text-muted» («Recepción de muestras **Aguas**»). El color nunca es la única señal.
- **Línea del área**: borde inferior de 3 px en `area-*` (`--ac`). Es la única superficie que toma el color del área; el fondo, el texto y los botones no cambian.
- **Ruta**: sección / área («Recepción / Aguas»).
- Las acciones no cambian: una primaria, en azul real, nunca en el color del área (el color del área no es de acción).
- Páginas globales (Usuarios, catálogos de servicios y de normas) usan la variante global, sin marca ni línea.
- Supuesto vigente: «Bebidas alcohólicas» usa `area-bebidas` hasta confirmar si sustituye a «Bebidas de agave».
'''
open(R, 'w').write(r); print('ok')
