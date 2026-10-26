# Consulta v2 · prototipos uno por uno. Uso: python3 gen.py [carpeta-fuentes salida-local]
# Inserta los íconos de iconos/ ({{i:nombre}}) y el sello de Expediente en plantilla-<n>.html → p<n>-*.html.
import re, os, sys, glob
H = os.path.dirname(os.path.abspath(__file__))
SELLO = os.path.join(H, '..', 'final', 'svg', 'expediente.svg')
def ico(n):
    s = open(os.path.join(H, 'iconos', n + '.svg')).read()
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S).strip()
    s = re.sub(r'\s+', ' ', s).replace(' width="24" height="24"', '')
    return s.replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
def sello():
    s = open(SELLO).read()
    s = re.sub(r'<title>.*?</title>', '', s)
    s = re.sub(r'id="([\w-]+)"', r'id="ex-\1"', s); s = re.sub(r'url\(#([\w-]+)\)', r'url(#ex-\1)', s)
    return re.sub(r'role="img"[^>]*?aria-label="[^"]*"', 'aria-hidden="true" focusable="false"', s)
GOOGLE = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
  '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700&family=Atkinson+Hyperlegible+Next:wght@400;600;700&display=swap">')
def local(d):
    f = {'Sora': 'Sora[wght].ttf', 'Atkinson Hyperlegible Next': 'Atkinson.ttf'}
    return '<style>' + ''.join(f"@font-face{{font-family:'{k}';src:url('file://{d}/{v}');font-weight:100 900}}" for k, v in f.items()) + '</style>'
for src in sorted(glob.glob(os.path.join(H, 'plantilla-*.html'))):
    t = open(src).read()
    t = t.replace('{{FUENTES}}', local(sys.argv[1]) if len(sys.argv) > 1 else GOOGLE).replace('{{SELLO}}', sello())
    t = re.sub(r'\{\{i:([a-z0-9-]+)\}\}', lambda m: ico(m.group(1)), t)
    nombre = re.search(r'<!-- salida: ([\w.-]+) -->', t).group(1)
    out = os.path.join(sys.argv[2], nombre) if len(sys.argv) > 2 else os.path.join(H, nombre)
    open(out, 'w').write(t)
    print('ok', nombre)
