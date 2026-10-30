# Convia · distintivo para negocios aprobados: calca circular de ventana (10 cm) y tarjeta de mostrador (A6).
# Uso: python3 distintivo.py <carpeta con Fraunces-Suave-500.ttf y Figtree-650.ttf>
# Reutiliza las funciones de sellos.py (texto en arco y en línea, convertido a trazos).
import sys, os, json, io
sys.argv = sys.argv[:2]
import sellos as S  # regenera los sellos (mismo resultado) y expone arc(), line(), star()
import qrcode, qrcode.image.svg
ANIO = '2027'  # vigencia anual por año calendario; quien entra después del 1 de octubre recibe la del año siguiente
D = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(D, 'tema.json'))); C = T['color']; CAT = T['categorias']

def calca(k):
    c = CAT[k]; bg, ink = c['texto'], C['papel']
    top = S.arc(S.FG, 'RECOMENDADO EN CONVIA', 15, 120, 120, 92, True, 2.4)
    bot = S.arc(S.FG, c['nombre'].upper() + ' · OAXACA', 13.5, 120, 120, 101, False, 2.2)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="100mm" height="100mm" viewBox="0 0 240 240" role="img" aria-label="Recomendado en Convia, {c["nombre"]}">'
            f'<circle cx="120" cy="120" r="119" fill="{bg}"/><circle cx="120" cy="120" r="111" fill="none" stroke="{ink}" stroke-width="1.4"/>'
            f'<circle cx="120" cy="120" r="76" fill="none" stroke="{ink}" stroke-width="1" stroke-dasharray="2 4"/>'
            f'<g fill="{ink}">{top}{bot}</g>' + S.star(ink, 84, 78, 64) + yr(ink) + '</svg>')
def yr(ink):
    p, w = S.line(S.FR, ANIO, 22, 0, 0)
    return f'<path transform="translate({120 - w / 2:.2f} 176)" d="{p}" fill="{ink}"/>'

def qr_paths(data, x, y, size, color):
    q = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(data); q.make(fit=True)
    m = q.get_matrix(); n = len(m); cell = size / n
    return ''.join(f'<rect x="{x + j * cell:.2f}" y="{y + i * cell:.2f}" width="{cell + .05:.2f}" height="{cell + .05:.2f}"/>'
                   for i, row in enumerate(m) for j, v in enumerate(row) if v), n

def tarjeta(k, negocio, slug):
    # A6 vertical 105×148 mm; unidades = mm
    c = CAT[k]
    lp, lw = S.line(S.FR, 'Convia', 11, 0, 0)
    h1, _ = S.line(S.FR, 'Este lugar está', 8.4, 0, 0)
    h2, _ = S.line(S.FR, 'en Convia.', 8.4, 0, 0)
    nb, _ = S.line(S.FG, negocio.upper(), 3.4, 0, 0, .5)
    ch, cw = S.line(S.FG, c['nombre'].upper(), 3.1, 0, 0, .4)
    t1, _ = S.line(S.FG, 'Escanea para ver horarios, fotos', 3.6, 0, 0)
    t2, _ = S.line(S.FG, 'y otros lugares recomendados.', 3.6, 0, 0)
    ej, _ = S.line(S.FG, 'QR DE EJEMPLO', 2.4, 0, 0, .4)
    vg, _ = S.line(S.FG, 'VIGENTE ' + ANIO, 2.4, 0, 0, .4)
    qr, n = qr_paths(f'https://convia.example/{slug}', 30.5, 82, 44, C['tinta'])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="105mm" height="148mm" viewBox="0 0 105 148" role="img" aria-label="Tarjeta de mostrador Convia, {negocio}">'
            f'<rect width="105" height="148" rx="4" fill="{C["papel"]}"/>'
            f'<g transform="translate(10 12)">{S.star(C["cantera"], 9.5, 0, 0)}<path transform="translate(11.5 8.2)" d="{lp}" fill="{C["tinta"]}"/></g>'
            f'<path transform="translate(10 40)" d="{h1}" fill="{C["tinta"]}"/><path transform="translate(10 50)" d="{h2}" fill="{C["tinta"]}"/>'
            f'<rect x="10" y="57" width="{cw + 7:.1f}" height="6.2" rx="3.1" fill="{c["fondo"]}"/><path transform="translate(13.5 61.3)" d="{ch}" fill="{c["texto"]}"/>'
            f'<path transform="translate(10 72)" d="{nb}" fill="{C["texto_sec"]}"/>'
            f'<path transform="translate(80 15.5)" d="{vg}" fill="{C["texto_sec"]}"/>'
            f'<rect x="26.5" y="78" width="52" height="52" rx="4" fill="#fff" stroke="{C["linea"]}" stroke-width=".3"/><g fill="{C["tinta"]}">{qr}</g>'
            f'<path transform="translate(10 138)" d="{t1}" fill="{C["texto_sec"]}"/><path transform="translate(10 143)" d="{t2}" fill="{C["texto_sec"]}"/>'
            f'<path transform="translate(80 137)" d="{ej}" fill="{C["texto_sec"]}" opacity=".7"/>'
            + '</svg>')

for k in CAT:
    open(os.path.join(D, 'distintivo', f'calca-{k}.svg'), 'w').write(calca(k))
open(os.path.join(D, 'distintivo', 'tarjeta-ejemplo-cafes.svg'), 'w').write(tarjeta('cafes', 'Café Tres Patios', 'cafe-tres-patios'))
open(os.path.join(D, 'distintivo', 'tarjeta-ejemplo-talleres.svg'), 'w').write(tarjeta('talleres', 'Barro bruñido · Taller Abierto', 'taller-abierto'))
print('ok')
