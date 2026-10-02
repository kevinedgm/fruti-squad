# Uva · bruno: siluetas de perfil (como rabbit/turtle) generadas como Catmull-Rom con esquinas marcadas.
import math, sys
f = lambda v: f'{v:.2f}'.rstrip('0').rstrip('.')
def camino(pts, cerrado=True, tension=1.0):
    """pts: [(x, y, esquina?)] → path suave; en una esquina la curva llega y sale recta (tangente nula)."""
    P = [(p[0], p[1]) for p in pts]; E = [len(p) > 2 and p[2] for p in pts]; n = len(P)
    tang = []
    for i in range(n):
        if E[i]: tang.append((0, 0)); continue
        a, b = P[(i - 1) % n], P[(i + 1) % n]
        tang.append(((b[0] - a[0]) / 6 * tension, (b[1] - a[1]) / 6 * tension))
    d = f'M{f(P[0][0])} {f(P[0][1])}'
    for i in range(n if cerrado else n - 1):
        a, b = P[i], P[(i + 1) % n]; ta, tb = tang[i], tang[(i + 1) % n]
        d += f'C{f(a[0] + ta[0])} {f(a[1] + ta[1])} {f(b[0] - tb[0])} {f(b[1] - tb[1])} {f(b[0])} {f(b[1])}'
    return d + ('Z' if cerrado else '')
C = True
# A · de pie, cola alzada (alerta, típica del malinois en marcha)
A = [(4.6, 10.4), (8.5, 10.7), (12.2, 10.1), (13.6, 8.7), (14.1, 6.8), (14.5, 2.7, C), (16.5, 5.3), (17.4, 5.5),
     (19.5, 6.8), (19.9, 7.6, C), (19.1, 8.3), (16.9, 8.9), (15.3, 9.8), (15.0, 12.4), (14.7, 14.6),
     (14.9, 20.2, C), (13.4, 20.2, C), (13.2, 15.4), (11.5, 14.9), (8.4, 14.7), (7.8, 15.5),
     (8.1, 20.2, C), (6.6, 20.2, C), (6.0, 17.6), (4.2, 14.6), (3.9, 12.1)]
cola = [(4.5, 10.6), (3.2, 9.9), (2.7, 8.6), (2.8, 7.0)]
def svg(id_, nota, cuerpo, cola, ojo, linea, extra=''):
    R = 'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'
    return (f'<svg {R} class="uva-icon uva-{id_}">\n  <style>.uva-{id_}{{stroke-width:var(--uva-stroke,1.5)}}.uva-{id_}__ojo{{fill:currentColor;stroke:none}}</style>\n'
            f'  <!-- {nota} -->\n  <path class="uva-{id_}__cuerpo" d="{camino(cuerpo)}"/>\n  <path class="uva-{id_}__cola" d="{camino(cola, False)}"/>\n'
            f'  <path class="uva-{id_}__linea" d="{camino(linea, False)}"/>\n  <circle class="uva-{id_}__ojo" cx="{ojo[0]}" cy="{ojo[1]}" r="0.75"/>\n{extra}</svg>\n')
def margen(pts):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return round(min(min(xs) - .75, min(ys) - .75, 24 - max(xs) - .75, 24 - max(ys) - .75), 2)
if __name__ == '__main__':
    open('bruno-a.svg', 'w').write(svg('bruno-a', 'A · de pie, cola alzada', A, cola, (16.4, 6.9), [(7.8, 15.5), (7.5, 13.4), (6.3, 12.2), (4.9, 11.9)]))
    print('A margen (puntos de control)', margen(A + cola))
