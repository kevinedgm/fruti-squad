# Directorio Manik · rediseño v1. Uso: python3 gen.py → rediseno.html
# Inserta el logotipo y el símbolo de manik-final/svg en plantilla.html (cambia los id de clipPath para que no choquen).
import re, os
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'manik-final', 'svg')
def svg(nombre, uid):
    s = open(os.path.join(B, nombre)).read()
    s = re.sub(r'<title>.*?</title>', '', s)
    s = s.replace('id="l"', f'id="{uid}"').replace('id="m"', f'id="{uid}"').replace('url(#l)', f'url(#{uid})').replace('url(#m)', f'url(#{uid})')
    return s.replace('role="img" aria-label="Manik"', 'aria-hidden="true" focusable="false"')
t = open('plantilla.html').read()
t = t.replace('{{LOGO}}', svg('logotipo.svg', 'lg1')).replace('{{LOGO_PIE}}', svg('logotipo.svg', 'lg2'))
t = t.replace('{{SIMBOLO}}', svg('simbolo.svg', 'sm1'))
open('rediseno.html', 'w').write(t)
print('ok')
