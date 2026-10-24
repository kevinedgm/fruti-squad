# Directorio Manik · dirección B (revista de salud). Uso: python3 gen.py [carpeta-fuentes salida-local]
# Sin argumentos: fuentes de Google Fonts → directorio.html. Con argumentos: @font-face locales para capturar sin red.
import re, os, sys
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'manik-final', 'svg')
def svg(nombre, uid):
    s = open(os.path.join(B, nombre)).read()
    s = re.sub(r'<title>.*?</title>', '', s)
    for k in ('l', 'm'):
        s = s.replace(f'id="{k}"', f'id="{uid}"').replace(f'url(#{k})', f'url(#{uid})')
    return s.replace('role="img" aria-label="Manik"', 'aria-hidden="true" focusable="false"')
GOOGLE = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
  '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..700,0..100;1,9..144,300..700,0..100'
  '&family=Instrument+Sans:wght@400..700&display=swap">')
PCT = '%'
def local(d):
    f = {'Fraunces': 'Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf', 'Instrument Sans': 'InstrumentSans[wdth,wght].ttf'}
    return '<style>' + ''.join(f"@font-face{{font-family:'{k}';src:url('file://{d}/{v.replace(PCT, PCT + '25')}');font-weight:100 900}}" for k, v in f.items()) + '</style>'
t = open('plantilla.html').read()
t = t.replace('{{FUENTES}}', local(sys.argv[1]) if len(sys.argv) > 1 else GOOGLE)
t = t.replace('{{LOGO}}', svg('logotipo.svg', 'lg1')).replace('{{LOGO_PIE}}', svg('logotipo-blanco.svg', 'lg2'))
open(sys.argv[2] if len(sys.argv) > 2 else 'directorio.html', 'w').write(t)
print('ok')
