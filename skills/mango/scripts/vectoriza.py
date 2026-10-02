#!/usr/bin/env python3
"""Mango · vectoriza una ilustración raster (PNG/WebP generado fuera, p. ej. con ChatGPT) a SVG por capas de color.

Capas (de abajo arriba): superficie (todo lo opaco), gris secundario, acento, tinta. Cada capa se traza con potrace
y se rellena con su token. Antes de trazar se aplican las correcciones de auditoría (paso 9) sobre el raster.

Uso:
  python vectoriza.py entrada.png salida.svg --titulo "Alt text" [--recorte x0,y0,x1,y1] [--correcciones fix.py] [--decorativa]
  fix.py define `corrige(im)` (PIL RGBA) → im: borrar un rasgo (alfa 0), cubrirlo con superficie o redibujar un trazo.
Dependencias: pip install potracer pillow numpy   (en un venv; no hay binario potrace en el entorno)
"""
import argparse, runpy
import numpy as np, potrace
from PIL import Image

TOKENS = {'surface': '#FFFDF5', 'secondary': '#CFC6B8', 'accent': '#F8BC32', 'ink': '#111111'}   # system/illustration-tokens.yaml


def abre(m, r=2):
    """Apertura morfológica: quita franjas de menos de 2r px (halos de antialias junto a la tinta)."""
    def paso(m, f):
        out = m.copy()
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                out = f(out, np.roll(np.roll(m, dy, 0), dx, 1))
        return out
    return paso(paso(m, np.logical_and), np.logical_or)


def capas(im):
    a = np.asarray(im).astype(int); r, g, b, al = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    opaco = al > 128; lum = 0.299 * r + 0.587 * g + 0.114 * b
    acento = opaco & (r > 190) & (g > 130) & (b < 120)
    return [('surface', opaco),
            ('secondary', abre(opaco & (lum > 140) & (lum < 222) & (abs(r - g) < 25) & (b < r) & ~acento)),
            ('accent', acento),
            ('ink', opaco & (lum < 100))]


def ruta(mascara):
    out = []
    for c in potrace.Bitmap(~mascara).trace(turdsize=6, alphamax=1.0, opticurve=True, opttolerance=0.3):   # potracer traza lo «apagado»: se invierte
        p = c.start_point; s = [f'M{p.x:.1f} {p.y:.1f}']
        for seg in c.segments:
            if seg.is_corner: s.append(f'L{seg.c.x:.1f} {seg.c.y:.1f}L{seg.end_point.x:.1f} {seg.end_point.y:.1f}')
            else: s.append(f'C{seg.c1.x:.1f} {seg.c1.y:.1f} {seg.c2.x:.1f} {seg.c2.y:.1f} {seg.end_point.x:.1f} {seg.end_point.y:.1f}')
        out.append(''.join(s) + 'Z')
    return ''.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('entrada'); ap.add_argument('salida')
    ap.add_argument('--titulo', default=''); ap.add_argument('--id', default='mango-ilustracion')
    ap.add_argument('--recorte'); ap.add_argument('--correcciones'); ap.add_argument('--decorativa', action='store_true')
    a = ap.parse_args()
    im = Image.open(a.entrada).convert('RGBA')
    if a.correcciones: im = runpy.run_path(a.correcciones)['corrige'](im)
    if a.recorte: im = im.crop(tuple(int(v) for v in a.recorte.split(',')))
    W, H = im.size
    paths = [f'  <path id="{n}" fill="{TOKENS[n]}" fill-rule="evenodd" d="{d}"/>' for n, m in capas(im) if m.any() and (d := ruta(m))]
    a11y = 'aria-hidden="true"' if a.decorativa else f'role="img" aria-labelledby="{a.id}-t"'
    tit = '' if a.decorativa else f'  <title id="{a.id}-t">{a.titulo}</title>\n'
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" {a11y}>\n{tit}' + '\n'.join(paths) + '\n</svg>\n'
    open(a.salida, 'w').write(svg)
    print(f'{a.salida}: {len(svg) // 1024} KB, {W}×{H}, capas: {", ".join(n for n, m in capas(im) if m.any())}')


if __name__ == '__main__':
    main()
