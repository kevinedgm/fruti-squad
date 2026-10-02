#!/usr/bin/env python3
"""Mango · separa una hoja de varias ilustraciones (p. ej. 2×2 de un generador) en fuentes sueltas con alfa.

Cada pieza conectada (mano, objeto, marca cinética) va a la celda que contiene su centro: un objeto que cruza la línea
media no se parte. Para cada celda calcula el recorte cuadrado anclado al corte del brazo (que toque el borde).

Uso: python parte-hoja.py hoja.png --rejilla 2x2 --nombres a,b,c,d [--quitar-cuadros] [--ancla br|lbr,...]
  ancla por celda: br = el brazo entra por abajo-derecha (por defecto); lbr = además por la izquierda.
Salida: fuente-<nombre>.png y cortes.json ({nombre: [x0,y0,x1,y1]}) para `vectoriza.py --recorte`.
"""
import argparse, json, os, sys
from collections import deque
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vectoriza import quita_cuadros

ap = argparse.ArgumentParser()
ap.add_argument('hoja'); ap.add_argument('--rejilla', default='2x2'); ap.add_argument('--nombres', required=True)
ap.add_argument('--quitar-cuadros', action='store_true'); ap.add_argument('--ancla', default=''); ap.add_argument('--margen', type=int, default=36)
a = ap.parse_args()
im = Image.open(a.hoja).convert('RGBA')
if a.quitar_cuadros: im = quita_cuadros(im)
A = np.asarray(im); op = A[..., 3] > 128; H, W = op.shape
cols, filas = (int(v) for v in a.rejilla.split('x')); cw, ch = W / cols, H / filas
nombres = a.nombres.split(','); anclas = (a.ancla.split(',') if a.ancla else []) + ['br'] * len(nombres)
eti = np.zeros(op.shape, int); n = 0; piezas = []
for y0, x0 in zip(*np.where(op)):
    if eti[y0, x0]: continue
    n += 1; q = deque([(y0, x0)]); eti[y0, x0] = n; sy = sx = c = 0
    while q:
        y, x = q.popleft(); sy += y; sx += x; c += 1
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                v, u = y + dy, x + dx
                if 0 <= v < H and 0 <= u < W and op[v, u] and not eti[v, u]: eti[v, u] = n; q.append((v, u))
    piezas.append((n, sy / c, sx / c))
cortes = {}
for k, nombre in enumerate(nombres):
    cx, cy = k % cols, k // cols
    m = np.isin(eti, [i for i, y, x in piezas if int(x // cw) == cx and int(y // ch) == cy])
    B = A.copy(); B[~m, 3] = 0; Image.fromarray(B, 'RGBA').save(f'fuente-{nombre}.png')
    ys, xs = np.where(m); bx0, by0, bx1, by1 = xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
    lado = max(bx1 - bx0, by1 - by0) + a.margen
    cortes[nombre] = [int(v) for v in ((bx0, by1 - lado, bx0 + lado, by1) if anclas[k] == 'lbr' else (bx1 - lado, by1 - lado, bx1, by1))]
json.dump(cortes, open('cortes.json', 'w'), indent=1); print(f'{n} piezas →', cortes)
