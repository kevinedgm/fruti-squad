# Apollo · derivados de exportación (icono de app y favicon) con los hex del design system.
import re
src = open('apollo.svg').read()
geo = [re.sub(r' class="[^"]*"', '', l.strip()) for l in src.splitlines() if l.strip().startswith(('<ellipse', '<path', '<circle'))]
orb = next(g for g in geo if g.startswith('<ellipse')); pr = next(g for g in geo if g.startswith('<path')); sat = next(g for g in geo if g.startswith('<circle'))
T = {'orbita': ('#070a14', '#e8edf7', '#22e4f5'), 'dia': ('#f4f6fb', '#0b1020', '#00707f')}
def tile(n, full=False):
    bg, ink, sig = T[n]
    r = '' if full else ' rx="112"'
    sat_c = sat.replace('/>', ' fill="%s" stroke="none"/>' % sig)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="Apollo">\n'
            '  <!-- Apollo · icono de app (tema %s). Derivado de exportación con los hex del design system; el icono de interfaz es apollo.svg -->\n'
            '  <rect width="512" height="512"%s fill="%s"/>\n'
            '  <g transform="translate(106 106) scale(12.5)" fill="none" stroke="%s" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">\n'
            '    %s\n    %s\n    %s\n  </g>\n</svg>\n') % (n, r, bg, ink, orb, pr, sat_c)
for n in T:
    open('app/apollo-app-%s.svg' % n, 'w').write(tile(n))
    open('app/apollo-app-%s-cuadrado.svg' % n, 'w').write(tile(n, True))   # sin esquinas: iOS, Android y PWA las recortan
fav = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">\n'
       '  <!-- Apollo · favicon: sigue el tema del sistema (Día / Órbita) -->\n'
       '  <style>.t{stroke:#0b1020}.s{fill:#00707f}@media (prefers-color-scheme:dark){.t{stroke:#e8edf7}.s{fill:#22e4f5}}</style>\n'
       '  %s\n  %s\n  %s\n</svg>\n') % (orb.replace('<ellipse', '<ellipse class="t"'), pr.replace('<path', '<path class="t"'), sat.replace('<circle', '<circle class="s"'))
open('app/favicon.svg', 'w').write(fav)
