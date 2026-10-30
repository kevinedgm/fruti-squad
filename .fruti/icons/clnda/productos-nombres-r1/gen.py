# CLNDA Studio · productos · ronda 1 de nombres (patrón «CLNDA + palabra clara»).
# La marca del producto la ven el negocio (panel, sitio comercial, ventas); el huésped/comprador ve la marca del negocio y «hecho por CLNDA».
# Uso: python3 gen.py → nombres.html
import os
H = os.path.dirname(os.path.abspath(__file__))
IND = '#4338ca'; INK = '#0e0f1c'; BG = '#f5f6fb'
BR = 'M40 10 H36 a8 8 0 0 0 -8 8 V26 a6 6 0 0 1 -6 6 a6 6 0 0 1 6 6 V46 a8 8 0 0 0 8 8 H40'
SIM = f'<svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="{BR}" stroke="{IND}" stroke-width="7" transform="translate(-3 0)"/><circle cx="46" cy="32" r="6.5" fill="{INK}"/></svg>'
# familias: (clave, título, idea, a favor, riesgo, [reservas, tienda, restaurante])
F = [
 ('A', 'En inglés, corto', 'Una palabra de acción o de lugar, como las apps que ya usa el sector.',
  'Cortas, se leen igual en cualquier país; «Stay» y «Table» suenan a hotelería y restaurante.',
  'Dejan a CLNDA (raíz oaxaqueña) rodeado de inglés; «Shop» es muy común.', ['Stay', 'Shop', 'Table']),
 ('B', 'En español, directo', 'La palabra que el dueño del negocio ya usa al hablar.',
  'Cero explicación para hoteles y restaurantes de México; coherente con la calenda.',
  'Si venden fuera de México, hay que traducir; «Tienda» es genérica.', ['Reservas', 'Tienda', 'Mesa']),
 ('C', 'Mixto, la palabra del sector', 'El término que usa cada industria aunque sea en inglés.',
  '«Booking» es como el hotelero llama a esto; «Menú» se entiende igual en los dos idiomas.',
  'Mezcla idiomas dentro de la familia; «Booking» recuerda a Booking.com.', ['Booking', 'Shop', 'Menú']),
]
P = ['Reservas para hoteles', 'Tienda en línea', 'Restaurantes']
def lock(w):
    return f'<div class="lk">{SIM}<span class="wm">CLNDA</span><span class="pw">{w}</span></div>'
def fam(k, t, i, a, r, ws):
    filas = ''.join(f'<li><span class="pp">{p}</span>{lock(w)}</li>' for p, w in zip(P, ws))
    return (f'<section class="c"><header><span class="k">{k}</span><h2>{t}</h2></header><p class="id">{i}</p><ul>{filas}</ul>'
            f'<p class="pr"><b>A favor:</b> {a}</p><p class="pr"><b>Riesgo:</b> {r}</p></section>')
css = f'''*{{box-sizing:border-box}}body{{margin:0;background:{BG};color:{INK};font:400 15px/1.55 'Space Grotesk',system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1180px;margin:0 auto}}h1{{font:700 28px/1.2 'Space Grotesk';margin:0 0 6px}}.lead{{color:#4a4d63;max-width:820px;margin:0 0 24px}}
.g{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.c{{background:#fff;border:1px solid #dfe1ec;border-radius:16px;padding:20px;display:flex;flex-direction:column;gap:10px;min-width:0;box-shadow:0 1px 2px rgba(14,15,28,.04)}}
.c header{{display:flex;gap:10px;align-items:center}}.k{{width:28px;height:28px;border-radius:8px;background:{INK};color:#fff;display:grid;place-items:center;font-weight:700}}
h2{{font:600 18px/1.2 'Space Grotesk';margin:0}}.id{{margin:0;color:#4a4d63;font-size:14px}}
ul{{list-style:none;margin:4px 0;padding:0;display:grid;gap:12px}}li{{border-top:1px solid #eceef5;padding-top:10px}}
.pp{{display:block;font:500 11px/1 'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:.06em;color:#5b5e73;margin-bottom:6px}}
.lk{{display:flex;align-items:center;gap:6px;min-width:0}}.lk svg{{width:36px;height:36px;flex:none;margin-right:-2px}}
.wm{{font:700 26px/1 'Space Grotesk';letter-spacing:-.015em}}.pw{{font:400 26px/1 'Space Grotesk';color:{IND};overflow-wrap:anywhere}}
.pr{{margin:0;font-size:13.5px;color:#4a4d63}}.pr b{{color:{INK};font-weight:600}}
.nota{{margin-top:20px;background:#fff;border:1px solid #dfe1ec;border-radius:16px;padding:20px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:24px;align-items:center}}
.nota h3{{font:600 12px/1 'JetBrains Mono',monospace;letter-spacing:.06em;text-transform:uppercase;color:#5b5e73;margin:0 0 8px}}.nota p{{margin:0;color:#4a4d63}}
.demo{{border:1px solid #dfe1ec;border-radius:12px;padding:16px;display:grid;gap:8px}}.hotel{{font:600 18px 'Space Grotesk'}}.btn{{justify-self:start;background:#1f3b2d;color:#fff;border-radius:8px;padding:8px 14px;font-weight:500}}
.firma{{display:flex;align-items:center;gap:6px;font-size:12.5px;color:#5b5e73;border-top:1px solid #eceef5;padding-top:8px}}.firma svg{{width:18px;height:18px}}.firma b{{color:{INK}}}
@media (max-width:920px){{.g,.nota{{grid-template-columns:1fr}}}}'''
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="claude:viewport-fit-sides" content="true"><title>Nombres de productos CLNDA</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">'
        f'<style>{css}</style></head><body><main>'
        '<h1>Productos de CLNDA Studio · ronda 1 de nombres</h1>'
        '<p class="lead">Tres familias de nombres con el patrón «CLNDA + palabra clara». En cada familia los tres productos hablan el mismo idioma, para que se lean como hermanos. Ningún nombre está verificado ante el IMPI. Color y símbolo por producto vienen en la siguiente ronda: aquí todos usan el índigo de CLNDA.</p>'
        f'<div class="g">{"".join(fam(*f) for f in F)}</div>'
        '<div class="nota"><div><h3>Dónde vive el nombre</h3><p>El huésped o el comprador ve la marca del negocio, no la del producto. El nombre del producto aparece en el panel de administración, en el sitio comercial y en las ventas; frente al cliente final solo queda la firma «hecho por CLNDA». Por eso el nombre tiene que funcionar para el dueño del hotel o del restaurante.</p></div>'
        f'<div class="demo"><span class="hotel">Hotel Ejemplo · Oaxaca</span><span>Llegada 12 nov · Salida 14 nov · 2 huéspedes</span><span class="btn">Reservar</span><span class="firma">{SIM}<span>hecho por <b>CLNDA</b></span></span></div></div>'
        '</main></body></html>')
open(os.path.join(H, 'nombres.html'), 'w').write(html); print('ok')
