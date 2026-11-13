# SAM · identidad, ronda 3: desarrollo de A · Corte (usuario, 2026-11-13: «me gusta la A, desarróllala»).
# Variantes del símbolo (ángulo, desplazamiento, inclinación, 16 px) y tres maneras de unirlo al nombre.
COLOR = 'var(--g-color-brand,#c6f432)'
S = 'M33.5 12.6C31.2 10.2 28 9 24 9C18 9 13.8 12 13.8 16.8C13.8 26.4 34.2 21.8 34.2 31.6C34.2 36.4 30 39.4 24 39.4C19.6 39.4 16.4 38 13.6 35.2'
def corte(k, y0, y1, dx, dy, w=8.4, skew=0, path=S):
    up, dn = f'M0 0H48V{y1}L0 {y0}Z', f'M0 {y0}L48 {y1}V48H0Z'
    g = f' transform="skewX({skew}) translate({-skew*0.42:.2f} 0)"' if skew else ''
    return (f'  <defs><clipPath id="sam-{k}-u"><path d="{up}"/></clipPath><clipPath id="sam-{k}-d"><path d="{dn}"/></clipPath></defs>\n'
            f'  <g fill="none" stroke-width="{w}"{g}>\n'
            f'    <path d="{path}" stroke="currentColor" clip-path="url(#sam-{k}-u)" transform="translate({dx} {dy})"/>\n'
            f'    <path d="{path}" stroke="{COLOR}" clip-path="url(#sam-{k}-d)"/>\n  </g>\n')
def svg(k, body, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="SAM" class="sam-{k}">\n'
            f'  <!-- SAM · {desc} -->\n{body}</svg>\n')
S16 = 'M33 13.4C30.9 10.8 27.8 9.6 24 9.6C18.4 9.6 14.6 12.4 14.6 16.8C14.6 26 33.4 21.8 33.4 31.4C33.4 36 29.6 38.8 24 38.8C19.8 38.8 16.8 37.4 14.4 34.8'
V = {
 'a1-depurada': (corte('a1', 30, 18, 3.2, -2.2), 'A1 · Depurada', 'La de la ronda 2 con el desplazamiento un poco mayor (3.2 en vez de 2.6) para que el corte se lea desde 24 px. Ángulo de 14°.'),
 'a2-profunda': (corte('a2', 35, 13, 4.2, -2.6), 'A2 · Corte profundo', 'Ángulo de 25° y desplazamiento mayor. Se ve más rápida y más rota. A 128 px la parte de arriba casi sale del cuadro.'),
 'a3-en-marcha': (corte('a3', 30, 18, 3.2, -2.2, skew=-9), 'A3 · En marcha', 'A1 inclinada 9° hacia delante. Suma velocidad, pero las cursivas cortadas son más comunes en marcas deportivas.'),
 'a4-16px': (corte('a4', 30, 18, 3.6, -2.6, w=10, path=S16), 'A4 · Para 16–24 px', 'Trazo más grueso (10) y curvas más abiertas. Es la versión de favicon y pestaña; no reemplaza a la grande.'),
}
for k, (b, t, d) in V.items(): open(f'{k}.svg', 'w').write(svg(k, b, t))
OSC, CLA, LIMA, OLIVA = '#0a0a0b', '#f2f2ee', '#c6f432', '#4d7c0f'
def at(s, z): return s.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
cards = ''
for k, (b, t, d) in V.items():
    s = open(f'{k}.svg').read()
    tam = ''.join(f'<figure><div class="z">{at(s, z)}</div><figcaption>{z} px</figcaption></figure>' for z in (16, 24, 32, 48, 128))
    apps = (f'<div class="app" style="background:{OSC};color:{CLA}">{at(s, 60)}</div>'
            f'<div class="app" style="background:{CLA};color:{OSC};--g-color-brand:{OLIVA}">{at(s, 60)}</div>'
            f'<span class="th" style="--g-color-brand:currentColor">{at(s, 32)}<small>una tinta</small></span>'
            f'<div class="tab">{at(s, 16)}<span>Mis pendientes · SAM</span></div>')
    cards += f'<section><header><h2>{t}</h2><p>{d}</p></header><div class="row tams">{tam}</div><div class="row">{apps}</div></section>'
# Logotipos (con A1)
a1 = open('a1-depurada.svg').read()
def cortado(txt, fondo, tinta, acento, tam=88):
    # El mismo corte de 14° atraviesa la palabra; la parte superior se adelanta.
    up = 'polygon(0 0,100% 0,100% 38%,0 62%)'; dn = 'polygon(0 62%,100% 38%,100% 100%,0 100%)'
    return (f'<div class="lock" style="background:{fondo}"><span class="cw" style="font-size:{tam}px">'
            f'<span style="color:{acento};clip-path:{dn}">{txt}</span>'
            f'<span style="color:{tinta};clip-path:{up};transform:translate(.055em,-.04em)">{txt}</span></span></div>')
L1 = ''.join(f'<div class="lock" style="background:{f};color:{c};--g-color-brand:{a}">{at(a1, 64)}<span class="wm">SAM</span></div>' for f, c, a in ((OSC, CLA, LIMA), (CLA, OSC, OLIVA)))
L2 = ''.join(f'<div class="lock" style="background:{f};color:{c};--g-color-brand:{a}"><span class="wm l2">{at(a1, 92)}<span>AM</span></span></div>' for f, c, a in ((OSC, CLA, LIMA), (CLA, OSC, OLIVA)))
L3 = cortado('SAM', OSC, CLA, LIMA) + cortado('SAM', CLA, OSC, OLIVA)
logos = (f'<section><header><h2>Logotipo · tres maneras de unir símbolo y nombre</h2><p>Con A1. Resuelven la S repetida de las rondas anteriores.</p></header>'
         f'<h3>L1 · Símbolo + nombre</h3><p class="fn">Lo convencional: el símbolo a la izquierda. La S se repite.</p><div class="row">{L1}</div>'
         f'<h3>L2 · El símbolo es la S</h3><p class="fn">El símbolo toma el lugar de la primera letra. Una sola S; el nombre se lee igual.</p><div class="row">{L2}</div>'
         f'<h3>L3 · Nombre cortado</h3><p class="fn">El mismo corte atraviesa las tres letras y la parte de arriba se adelanta. El símbolo aparece solo en el icono.</p><div class="row">{L3}</div></section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAM · ronda 3</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;700;800&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 "Geist",system-ui,sans-serif;--g-color-brand:{LIMA}}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:#a3a3a8;max-width:72ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px;letter-spacing:-.01em}} h3{{margin:26px 0 0;font-size:16px}} header p{{margin:4px 0 0;max-width:80ch}} .fn{{color:#a3a3a8;font-size:13px;margin:2px 0 0}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:16px}}
.tams{{align-items:flex-end}} figure{{margin:0;text-align:center}} .z{{display:flex;align-items:flex-end;justify-content:center;min-width:56px;height:128px}}
figcaption,small{{font-size:12px;color:#a3a3a8}}
.lock{{display:flex;align-items:center;gap:8px;padding:16px 30px 16px 18px;border:1px solid #26262b;border-radius:2px;min-height:96px;box-sizing:border-box}}
.wm{{font-weight:800;font-size:52px;line-height:1;letter-spacing:-.035em}}
.l2{{display:inline-flex;align-items:center;font-size:66px}} .l2 svg{{margin:0 -.2em 0 -.17em}}
.cw{{display:inline-grid;font-weight:800;line-height:1;letter-spacing:-.035em}} .cw>span{{grid-area:1/1}}
.app{{width:88px;height:88px;border-radius:20px;display:flex;align-items:center;justify-content:center;border:1px solid #26262b}}
.tab{{display:flex;gap:8px;align-items:center;background:#1c1c20;border-radius:8px 8px 0 0;padding:8px 13px;font-size:13px}}
.th{{display:inline-flex;gap:6px;align-items:center;padding:6px 10px;border:1px solid #26262b;border-radius:2px}}
</style></head><body><main><h1>SAM · identidad, ronda 3 · desarrollo de Corte</h1>
<p class="sub">Cuatro variantes del símbolo y tres logotipos. El lima y el oliva siguen siendo provisionales; el color y la tipografía se deciden después.</p>
{cards}{logos}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
