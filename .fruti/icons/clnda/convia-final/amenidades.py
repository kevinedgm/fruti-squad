# Convia · íconos de amenidades de hotel (las declara el negocio; no son rasgos revisados). Mismo trazo de plumón que iconos.py.
# Uso: python3 amenidades.py → amenidades/<clave>.svg + amenidades/vista.png (vía navegador aparte).
import os
from iconos import ln, circ, rr, arcpts, C, D
from rasgos import ell, dot
I = {
 'alberca': ln([(24, 132), (52, 120), (80, 132), (108, 120), (136, 132), (164, 120), (180, 126)], 60, w=12)
          + ln([(24, 166), (52, 154), (80, 166), (108, 154), (136, 166), (164, 154), (180, 160)], 61, w=12)
          + ln([(66, 112), (66, 52), (80, 36)], 62, w=12) + ln([(116, 112), (116, 52), (130, 36)], 63, w=12) + ln([(66, 80), (116, 80)], 64, w=11),
 'desayuno': ln([(54, 70), (140, 70), (136, 112), (118, 136), (76, 136), (58, 112)], 65, True) + ln([(138, 82), (160, 86), (160, 106), (134, 114)], 66, w=12)
          + ln(ell(98, 156, 80, 16, 16), 67, True, w=11) + ln([(82, 52), (78, 40), (84, 28)], 68, w=10) + ln([(110, 52), (106, 40), (112, 28)], 69, w=10),
 'wifi': ln(arcpts(100, 152, 104, 222, 318, 14), 70, w=13) + ln(arcpts(100, 152, 70, 225, 315, 12), 71, w=13) + ln(arcpts(100, 152, 36, 230, 310, 8), 72, w=13) + dot(100, 156, 13),
 'estacionamiento': ln(rr(34, 30, 166, 170, 26), 73, True) + ln([(80, 146), (80, 56), (114, 56), (132, 68), (134, 92), (116, 106), (80, 106)], 74, w=14),
 'recepcion': ln(arcpts(100, 140, 62, 180, 360, 18), 75) + ln([(24, 146), (176, 146)], 76) + ln([(36, 172), (164, 172)], 77, w=11) + dot(100, 66, 11),
 'terraza': ln(arcpts(100, 92, 76, 182, 358, 18) + [(24, 92)], 78, w=12) + ln([(100, 92), (100, 172)], 79, w=12) + ln([(62, 172), (138, 172)], 80, w=11) + ln([(100, 16), (100, 22)], 81, w=10),
 'traslado': ln([(22, 136), (24, 104), (52, 98), (70, 70), (130, 70), (152, 98), (176, 104), (178, 136)], 82)
          + ln(circ(58, 140, 16, 83, 12), 83, True, w=11) + ln(circ(142, 140, 16, 84, 12), 84, True, w=11) + ln([(76, 98), (148, 98)], 85, w=10),
 'aire': ln([(100, 26), (100, 174)], 86, w=12) + ln([(36, 63), (164, 137)], 87, w=12) + ln([(36, 137), (164, 63)], 88, w=12)
          + ln([(84, 40), (100, 54), (116, 40)], 89, w=10) + ln([(84, 160), (100, 146), (116, 160)], 90, w=10),
}
NOMBRES = {'alberca': 'Alberca', 'desayuno': 'Desayuno incluido', 'wifi': 'Wifi', 'estacionamiento': 'Estacionamiento',
           'recepcion': 'Recepción 24 h', 'terraza': 'Terraza', 'traslado': 'Traslado al aeropuerto', 'aire': 'Aire acondicionado'}
def svg(k, col='currentColor', size=None, cls=None):
    wh = f' width="{size}" height="{size}"' if size else ''
    c = f' class="{cls}" aria-hidden="true"' if cls else f' role="img" aria-label="{NOMBRES[k]}"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"{wh}{c}><g fill="none" stroke="{col}" stroke-linecap="round" stroke-linejoin="round">'
            + I[k].replace('currentFill', col) + '</g></svg>')
if __name__ == '__main__':
    for k in I: open(os.path.join(D, 'amenidades', f'{k}.svg'), 'w').write(svg(k))
    rows = ''.join(f'<div class="c"><div class="r">{svg(k, C["tinta"], 72)}{svg(k, C["tinta"], 24)}{svg(k, C["tinta"], 16)}</div><b>{n}</b></div>' for k, n in NOMBRES.items())
    open(os.path.join(D, 'amenidades', 'vista.html'), 'w').write(f'<!doctype html><meta charset="utf-8"><style>body{{margin:0;padding:28px;background:{C["papel"]};font:600 15px sans-serif;width:980px}}main{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}.c{{background:#fff;border:1px solid {C["linea"]};border-radius:16px;padding:18px;display:grid;gap:8px}}.r{{display:flex;gap:16px;align-items:center}}</style><main>{rows}</main>')
    print('ok')
