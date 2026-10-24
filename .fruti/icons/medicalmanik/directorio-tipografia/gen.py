# Directorio Manik · tres direcciones tipográficas. Uso: python3 gen.py [carpeta-de-fuentes]
# Sin argumento: fuentes desde Google Fonts (para publicar). Con carpeta: @font-face locales (para capturar sin red).
import re, os, sys
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'manik-final', 'svg')
def svg(nombre, uid):
    s = open(os.path.join(B, nombre)).read()
    s = re.sub(r'<title>.*?</title>', '', s)
    for k in ('l', 'm'):
        s = s.replace(f'id="{k}"', f'id="{uid}"').replace(f'url(#{k})', f'url(#{uid})')
    return s.replace('role="img" aria-label="Manik"', 'aria-hidden="true" focusable="false"')
GOOGLE = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
  '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800'
  '&family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..700,100;1,9..144,300..700,100&family=Instrument+Sans:wght@400..700'
  '&family=Manrope:wght@400..700&family=Onest:wght@400..700&family=Unbounded:wght@400..800&display=swap">')
PCT = '%'
def local(d):
    f = {'Bricolage Grotesque': 'BricolageGrotesque[opsz,wdth,wght].ttf', 'Fraunces': 'Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf',
         'Instrument Sans': 'InstrumentSans[wdth,wght].ttf', 'Manrope': 'Manrope[wght].ttf', 'Onest': 'Onest.ttf', 'Unbounded': 'Unbounded[wght].ttf'}
    return '<style>' + ''.join(f"@font-face{{font-family:'{k}';src:url('file://{d}/{v.replace(PCT, PCT + '25')}');font-weight:100 900;font-stretch:75% 100%}}" for k, v in f.items()) + '</style>'
t = open('plantilla.html').read()
t = t.replace('{{FUENTES}}', local(sys.argv[1]) if len(sys.argv) > 1 else GOOGLE)
D = [('a', 'A', 'Grotesca con carácter', 'Bricolage Grotesque + Onest',
      'Letra con trazos vivos y ancho ajustable. Se siente de app actual, cercana y con energía. Resalta palabras como marcador.'),
     ('b', 'B', 'Revista de salud', 'Fraunces + Instrument Sans',
      'Serif suave con cursivas expresivas. Se siente editorial y confiable, como una revista. Da voz a los artículos y a las respuestas de médicos.'),
     ('x', 'C', 'Pop ancho', 'Unbounded + Manrope',
      'Geométrica, ancha y redonda, familia de la letra del logotipo. Se siente joven y digital, sobre todo en fondo oscuro.')]
bloque = open('bloque.html').read()
html = ''
for i, (k, L, nom, fam, nota) in enumerate(D):
    b = bloque.replace('{{K}}', k).replace('{{L}}', L).replace('{{NOMBRE}}', nom).replace('{{FAMILIAS}}', fam).replace('{{NOTA}}', nota)
    html += b.replace('{{LOGO}}', svg('logotipo.svg', f'lg{k}'))
t = t.replace('{{DIRECCIONES}}', html)
open(sys.argv[2] if len(sys.argv) > 2 else 'tipografia.html', 'w').write(t)
print('ok')
