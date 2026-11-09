# Ecosistema Manik · exportación de lo aprobado (sin rondas de exploración, scripts ni material de terceros).
# Uso: python3 exportar.py <carpeta de salida>  ->  <salida>/ecosistema-manik-AAAA-MM-DD.zip
import os, sys, shutil, zipfile, datetime
H = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]
HOY = datetime.date.today().isoformat(); RAIZ = f'ecosistema-manik-{HOY}'
A = 'https://claude.ai/artifact/'
PIEZAS = [  # (carpeta en el zip, origen, archivos o carpetas a copiar, enlace publicado, descripción)
 ('01-manual-de-marca', 'manual-marca', ['manual.html', 'img'], A + '9CXk9mHzwGdy8bow3Q9VsV', 'Manual de identidad de MedicalManik y del Ecosistema Manik (versión 2026). Ábrelo en el navegador.'),
 ('02-design-system', 'design-system/project', ['README.md', 'tokens.json', 'design-system.json', 'components', 'assets'], A + '28z6yfie6L8btocL8QBZi9', 'Design System del Ecosistema Manik: tokens, 20 componentes con su README y vista previa (components/<nombre>/preview.html) y los sellos.'),
 ('03-sellos-de-producto', 'final', ['svg', 'png', 'tema.json', 'lamina.png'], None, 'Sellos con la M original: SVG a color y a una tinta, PNG de 16 a 512 px y tema.json con los colores de cada producto.'),
 ('04-sellos-alternativa-b', 'sellos-b-r01', ['svg', 'comparacion.html'], A + 'DGDKQeSEP5cWrBtZCqtNqL', 'Alternativa aprobada: sellos de producto sin la M.'),
 ('05-arquitectura-de-marca', 'arquitectura-marca', ['arquitectura.html'], A + '8TpQWGjCFJ5smnbiQFgSZm', 'Por qué MedicalManik es la marca madre y los productos se llaman «Producto Manik».'),
 ('06-guia-impulsa', 'impulsa-migracion', ['guia.html'], A + 'AjTnxzTXKHqqHon5C3jsig', 'Guía para alinear Impulsa Manik con el Design System.'),
 ('07-directorio', 'directorio-manual', ['manual.html'], A + 'PNtPN4fEMSdEyVKTKwxAM7', 'Manual de marca del directorio Manik.'),
 ('07-directorio/design-system', 'directorio-ds/project', ['README.md', 'tokens.json', 'design-system.json', 'components', 'assets'], A + 'MTg2EAZVsJKZJRFCWGvAuj', 'Design System del directorio.'),
 ('08-manik-ia', 'manik-ia', ['manual.html'], None, 'Manual de la capa de IA de Expediente (Manik IA).'),
]
dst = os.path.join(OUT, RAIZ); shutil.rmtree(dst, ignore_errors=True); os.makedirs(dst)
ign = shutil.ignore_patterns('__pycache__', '*.py', '*.pyc')
filas = []
for carpeta, origen, items, url, desc in PIEZAS:
    d = os.path.join(dst, carpeta); os.makedirs(d, exist_ok=True)
    for it in items:
        s = os.path.join(H, origen, it)
        if os.path.isdir(s): shutil.copytree(s, os.path.join(d, it), ignore=ign)
        elif os.path.exists(s): shutil.copy2(s, d)
        else: print('falta', s)
    filas.append(f'| `{carpeta}/` | {desc} | {"[en línea](" + url + ")" if url else "—"} |')
open(os.path.join(dst, 'LEEME.md'), 'w').write(f'''# Ecosistema Manik · exportación {HOY}

Todo lo aprobado del Ecosistema Manik de MedicalManik: manual, Design System, sellos y documentos de marca.
No incluye las rondas de exploración ni los scripts que generan los archivos (viven en el repositorio, `.fruti/icons/medicalmanik/`).
Los archivos `.html` se abren directo en el navegador; las fuentes se cargan de Google Fonts, así que necesitan internet.

| Carpeta | Qué es | Versión publicada |
|---|---|---|
{chr(10).join(filas)}

Datos de ejemplo: todos los pacientes, médicos, cédulas y teléfonos de las vistas previas son ficticios.
''')
zp = os.path.join(OUT, RAIZ + '.zip')
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for r, _, fs in os.walk(dst):
        for f in fs:
            p = os.path.join(r, f); z.write(p, os.path.relpath(p, OUT))
n = sum(len(fs) for _, _, fs in os.walk(dst)); print('ok', zp, n, 'archivos', round(os.path.getsize(zp)/1e6, 1), 'MB')
