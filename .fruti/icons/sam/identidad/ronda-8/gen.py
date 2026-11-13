# SAM · identidad, ronda 8: desarrollo de C · Tarjetas (usuario, 2026-11-13: «me gusta la C, desarróllala»).
# Regla de color (ronda 7): el lima es relleno y siempre toca tinta; la palomita va en tinta fija.
LIMA, TINTA = 'var(--g-color-brand,#c6f432)', 'var(--sam-tinta,#0a0a0b)'
def check(x, y, w, h, sw):
    # palomita centrada en la tarjeta (x, y, w, h)
    cx, cy = x + w/2, y + h/2
    return (f'  <path d="M{cx-6.4:g} {cy+0.4:g}L{cx-2:g} {cy+4.6:g}L{cx+6.6:g} {cy-4.4:g}" fill="none" stroke="{TINTA}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>\n')
def tarjetas(atras, front=(16, 17, 26, 22), r=5, sw=3, borde=2.6):
    b = ''
    for (x, y, w, h, estilo) in atras:
        b += (f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="currentColor"/>\n' if estilo == 'relleno'
              else f'  <rect x="{x+1.3}" y="{y+1.3}" width="{w-2.6}" height="{h-2.6}" rx="{r-1}" fill="none" stroke="currentColor" stroke-width="2.6"/>\n')
    x, y, w, h = front
    b += f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{LIMA}" stroke="currentColor" stroke-width="{borde}"/>\n'
    return b + check(x, y, w, h, sw)
def svg(k, body, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="SAM" class="sam-{k}">\n'
            f'  <!-- SAM · {desc} -->\n{body}</svg>\n')
V = {
 'c1-depurada': (tarjetas([(5, 9, 27, 21, 'relleno')], front=(16, 18, 27, 21), sw=3.4),
   'C1 · Depurada', 'La de la ronda 7 con tarjetas en proporción de tarjeta real (9:7) y palomita más firme. La de atrás, sólida.'),
 'c2-contorno': (tarjetas([(5, 9, 27, 21, 'contorno')], front=(16, 18, 27, 21), sw=3.4),
   'C2 · Atrás en contorno', 'La tarjeta anterior queda solo como contorno: ya pasó. Más ligera y «simple»; en claro pesa mucho menos que el bloque negro.'),
 'c3-pila': (tarjetas([(3, 5, 24, 19, 'contorno'), (9.5, 12, 24, 19, 'relleno')], front=(17, 20, 27, 21), sw=3.4),
   'C3 · Pila de etapas', 'Tres tarjetas: la actividad cruza etapas y llega completada. Cuenta más el flujo, pero es más cargada y se empasta a 16 px.'),
 'c4-16px': (tarjetas([(4, 8, 28, 22, 'relleno')], front=(15, 18, 29, 23), r=5.5, sw=4.4, borde=3),
   'C4 · Para 16–24 px', 'Más desplazamiento entre tarjetas y palomita y bordes más gruesos. Versión de favicon y pestaña; acompaña a la grande.'),
}
for k, (b, t, d) in V.items(): open(f'{k}.svg', 'w').write(svg(k, b, t))
OSC, SUP, CLA, BL, VO, SEC = '#0a0a0b', '#16161a', '#f2f2ee', '#ffffff', '#c6f432', '#a3a3a8'
def at(s, z): return s.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
cards = ''
for k, (b, t, d) in V.items():
    s = open(f'{k}.svg').read()
    tam = ''.join(f'<figure><div class="z">{at(s, z)}</div><figcaption>{z} px</figcaption></figure>' for z in (16, 24, 32, 48, 128))
    apps = (f'<div class="app" style="background:{OSC};color:{CLA}">{at(s, 60)}</div>'
            f'<div class="app" style="background:{CLA};color:{OSC}">{at(s, 60)}</div>'
            f'<span class="th" style="--g-color-brand:transparent">{at(s, 32)}<small>una tinta</small></span>'
            f'<div class="tab" style="background:#e4e4de;color:{OSC}">{at(s, 16)}<span>Mis actividades · SAM</span></div>'
            f'<div class="tab">{at(s, 16)}<span>Mis actividades · SAM</span></div>')
    cards += f'<section><header><h2>{t}</h2><p>{d}</p></header><div class="row tams">{tam}</div><div class="row">{apps}</div></section>'
c2 = open('c2-contorno.svg').read(); c1 = open('c1-depurada.svg').read()
def locks(s, nom):
    h = ''
    for f, c, dc in ((OSC, CLA, SEC), (CLA, OSC, '#3a3a40')):
        h += (f'<div class="lock" style="background:{f};color:{c}">{at(s, 60)}<span><span class="wm">SAM</span><span class="desc" style="color:{dc}">Simple Activity Manager</span></span></div>'
              f'<div class="lock v" style="background:{f};color:{c}">{at(s, 72)}<span class="wm">SAM</span><span class="desc" style="color:{dc}">Simple Activity Manager</span></div>'
              f'<div class="lock" style="background:{f};color:{c}">{at(s, 40)}<span class="wm s">SAM</span></div>')
    return f'<h3>{nom}</h3><div class="row">{h}</div>'
logos = (f'<section><header><h2>Logotipo · horizontal, vertical y compacto</h2><p>Con C1 y con C2. Horizontal para la barra de la app y documentos; vertical para portada y pantalla de inicio; compacto (sin descriptor) para espacios chicos.</p></header>'
         f'{locks(c1, "Con C1 · atrás sólida")}{locks(c2, "Con C2 · atrás en contorno")}</section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAM · ronda 8</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 'Instrument Sans',system-ui,sans-serif;--g-color-brand:{VO}}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:{SEC};max-width:76ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px}} h3{{margin:21px 0 0;font-size:16px}} header p{{margin:4px 0 0;max-width:86ch}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:16px}}
.tams{{align-items:flex-end}} figure{{margin:0;text-align:center}} .z{{display:flex;align-items:flex-end;justify-content:center;min-width:56px;height:128px}}
figcaption,small{{font-size:12px;color:{SEC}}}
.lock{{display:flex;align-items:center;gap:13px;padding:16px 26px 16px 16px;border:1px solid #26262b;border-radius:2px}}
.lock.v{{flex-direction:column;gap:8px;padding:21px 26px;text-align:center}}
.wm{{display:block;font-weight:700;font-size:44px;line-height:1;letter-spacing:-.01em}} .wm.s{{font-size:30px}} .desc{{display:block;font-size:14px;font-weight:500;margin-top:4px}}
.app{{width:88px;height:88px;border-radius:20px;display:flex;align-items:center;justify-content:center;border:1px solid #26262b}}
.tab{{display:flex;gap:8px;align-items:center;background:#1c1c20;border-radius:8px 8px 0 0;padding:8px 13px;font-size:13px}}
.th{{display:inline-flex;gap:6px;align-items:center;padding:6px 10px;border:1px solid #26262b;border-radius:2px;--sam-tinta:{CLA}}}
</style></head><body><main><h1>SAM · identidad, ronda 8 · desarrollo de Tarjetas</h1>
<p class="sub">Cuatro variantes del símbolo y tres arreglos de logotipo. Lima Voltaje con la regla de la ronda 7 (relleno que siempre toca tinta). Nombre en Instrument Sans 700, provisional.</p>
{cards}{logos}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
