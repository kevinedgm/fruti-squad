# Directorio Manik · dirección «bienestar» (referencia: Hims & Hers / Oura). Uso: python3 gen.py [carpeta-fuentes salida-local]
# Sin argumentos: Google Fonts → directorio.html. Con argumentos: @font-face locales para capturar sin red.
import re, os, sys
H = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(H, '..', 'manik-final', 'svg')
def svg(nombre, uid):
    s = open(os.path.join(B, nombre)).read()
    s = re.sub(r'<title>.*?</title>', '', s)
    for k in ('l', 'm'):
        s = s.replace(f'id="{k}"', f'id="{uid}"').replace(f'url(#{k})', f'url(#{uid})')
    return s.replace('role="img" aria-label="Manik"', 'aria-hidden="true" focusable="false"')
def ico(n):
    s = open(os.path.join(H, 'iconos', n + '.svg')).read()
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S).strip()
    s = re.sub(r'\s+', ' ', s).replace(' width="24" height="24"', '')
    return s.replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
GOOGLE = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
  '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Onest:wght@400..700&display=swap">')
def local(d):
    f = {'Urbanist': 'Urbanist.woff2', 'Onest': 'OnestVar.woff2'}
    return '<style>' + ''.join(f"@font-face{{font-family:'{k}';src:url('file://{d}/{v}');font-weight:100 900}}" for k, v in f.items()) + '</style>'
t = open(os.path.join(H, 'plantilla.html')).read()
t = t.replace('{{FUENTES}}', local(sys.argv[1]) if len(sys.argv) > 1 else GOOGLE)
t = t.replace('{{LOGO}}', svg('logotipo.svg', 'lg1')).replace('{{LOGO_B}}', svg('logotipo.svg', 'lg2'))
t = re.sub(r'\{\{i:([a-z0-9-]+)\}\}', lambda m: ico(m.group(1)), t)
open(sys.argv[2] if len(sys.argv) > 2 else os.path.join(H, 'directorio.html'), 'w').write(t)
print('ok')
