#!/usr/bin/env python3
"""Mango · vectoriza una ilustración raster (PNG/WebP generado fuera, p. ej. con ChatGPT) a SVG por capas de color.

Capas (de abajo arriba): superficie (todo lo opaco), gris secundario, acento, tinta. Cada capa se traza con potrace
y se rellena con su token. Antes de trazar se aplican las correcciones de auditoría (paso 9) sobre el raster.

Uso:
  python vectoriza.py entrada.png salida.svg --titulo "Alt text" [--recorte x0,y0,x1,y1] [--correcciones fix.py] [--decorativa] [--quitar-cuadros]
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


def quita_cuadros(im):
    """El generador a veces pinta el «fondo transparente» como cuadros grises (RGB sin alfa): se vuelve alfa real.
    Relleno por inundación desde cada zona amplia de gris neutro (también las encerradas entre líneas); se detiene en la
    tinta, y la piel y las superficies (blanco cálido) o los blancos puros (≥225) nunca son fondo."""
    a = np.asarray(im.convert('RGBA')).copy(); r, g, b = (a[..., i].astype(int) for i in range(3))
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    neutro = (abs(r - g) < 7) & (abs(r - b) < 8) & (lum > 85) & (lum < 225)   # cuadros ≈130 y ≈190
    claro = neutro & (lum > 150); fondo = claro.copy()
    for dy in range(-2, 3):
        for dx in range(-2, 3): fondo &= np.roll(np.roll(claro, dy, 0), dx, 1)
    while True:
        n = fondo.copy()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            n |= np.roll(np.roll(fondo, dy, 0), dx, 1)
        n &= neutro
        if (n == fondo).all(): break
        fondo = n
    a[fondo, 3] = 0
    return Image.fromarray(a, 'RGBA')


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
    ap.add_argument('--quitar-cuadros', action='store_true', help='el fondo «transparente» viene pintado como cuadros grises')
    a = ap.parse_args()
    im = Image.open(a.entrada).convert('RGBA')
    if a.quitar_cuadros: im = quita_cuadros(im)
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
