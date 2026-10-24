# Manik · ronda 2: la M de pulso refinada y el sistema «Producto + Manik»
# Uso: python3 gen.py <scratchpad>  → lamina.html (y svg/ con los símbolos)
import sys, os
S = sys.argv[1]; F = f'file://{S}/fuentes'
AZ, CI, PAPEL, TINTA = '#234899', '#00BDD0', '#F6F8FC', '#14213D'
os.makedirs('svg', exist_ok=True)

# Original, limpio del .ai (mismas trazas, sin perfil de color): cuadro + pulso recortado por el cuadro
ORIG_CUADRO = 'm 0,0 h -303.025 c -57.532,0 -104.604,47.072 -104.604,104.605 v 303.024 c 0,57.533 47.072,104.605 104.604,104.605 H 0 c 57.533,0 104.605,-47.072 104.605,-104.605 V 104.605 C 104.605,47.072 57.533,0 0,0'
ORIG_PULSO = 'm 0,0 c -7.446,0 -14.076,4.712 -16.525,11.743 l -57.556,194.928 c -2.25,6.459 -9.686,11.743 -16.525,11.743 h -44.843 c -7.574,0 -14.288,-4.873 -16.637,-12.074 l -71.085,-217.995 c -11.221,-34.41 -26.417,-33.568 -33.771,1.87 l -60.076,289.534 c -1.685,8.121 -8.84,13.944 -17.134,13.944 h -42.25 c -7.948,0 -14.897,-5.356 -16.922,-13.042 L -455.996,42.729 c -2.024,-7.686 -8.974,-13.042 -16.922,-13.042 h -42.607 c -9.664,0 -17.499,-7.834 -17.499,-17.498 v -34.918 c 0,-9.689 7.872,-17.533 17.561,-17.499 l 43.991,0.155 -0.018,-0.071 h 38.187 c 8.059,0 15.076,5.505 16.995,13.333 l 42.993,175.4 c 10.129,41.319 25.487,41.045 34.13,-0.611 l 57.731,-278.23 c 1.685,-8.121 8.84,-13.944 17.134,-13.944 h 42.993 c 7.595,0 14.323,4.9 16.654,12.129 l 73.139,226.811 c 9.523,29.531 24.564,29.363 33.425,-0.373 l 36.358,-122.014 c 2.21,-7.417 9.03,-12.501 16.77,-12.501 h 41.785 l -0.02,0.071 316.969,-0.203 c 9.67,-0.008 17.513,7.829 17.513,17.499 V 0 Z'
def original(bg, fg, uid):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="217.97 210 683.4 683.4"><defs><clipPath id="c{uid}">'
            f'<path transform="matrix(1.3333333,0,0,-1.3333333,761.952,893.3836)" d="{ORIG_CUADRO}"/></clipPath></defs>'
            f'<path transform="matrix(1.3333333,0,0,-1.3333333,761.952,893.3836)" d="{ORIG_CUADRO}" fill="{bg}"/>'
            f'<g clip-path="url(#c{uid})"><path transform="matrix(1.3333333,0,0,-1.3333333,897.051,639.54547)" d="{ORIG_PULSO}" fill="{fg}"/></g></svg>')

# Refinadas (retícula 100, radio 21 como el original): el pulso es un trazo de grosor constante que corta el cuadro de lado a lado
LINEAS = {
 'R1': ('(-6,63) (13,63) (27,12) (49,86) (71,25) (84,64) (106,64)', 13,
        'Fiel: la misma línea del original con grosor constante y más peso. Las salidas laterales miden lo mismo que el trazo.'),
 'R2': ('(-6,62) (17,62) (25,15) (50,80) (74,26) (82,62) (106,62)', 13,
        'M primero: astas casi verticales y la V al centro. Se lee antes la M que el latido genérico.'),
}
def pts(s): return [tuple(float(v) for v in p.strip('()').split(',')) for p in s.split()]
def refinada(k, bg, fg, uid):
    p, w, _ = LINEAS[k]
    d = 'M' + ' L'.join(f'{x:g} {y:g}' for x, y in pts(p))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><clipPath id="c{uid}"><rect width="100" height="100" rx="21"/></clipPath></defs>'
            f'<rect width="100" height="100" rx="21" fill="{bg}"/><path clip-path="url(#c{uid})" d="{d}" fill="none" stroke="{fg}" stroke-width="{w}" '
            f'stroke-linejoin="round" stroke-linecap="butt"/></svg>')

n = [0]
def uid(): n[0] += 1; return n[0]
def sym(k, bg, fg=PAPEL): return original(bg, fg, uid()) if k == 'O' else refinada(k, bg, fg, uid())
for k in ('O', 'R1', 'R2'):
    open(f'svg/simbolo-{k}.svg', 'w').write(sym(k, AZ))

# 1 · comparación de tamaños
NOM = {'O': 'Original', 'R1': 'R1 · Fiel', 'R2': 'R2 · M primero'}
filas = ''
for k in ('O', 'R1', 'R2'):
    tam = ''.join(f'<span class="s" style="width:{z}px;height:{z}px">{sym(k, AZ)}</span>' for z in (16, 24, 32, 64, 120))
    inv = f'<span class="s" style="width:64px;height:64px">{sym(k, PAPEL, AZ)}</span><span class="s neg" style="width:64px;height:64px">{sym(k, "#FFFFFF", TINTA)}</span>'
    nota = LINEAS[k][2] if k in LINEAS else 'Grosor variable: las salidas laterales son más finas que las astas. A 16 px aguanta mejor de lo que esperaba; la diferencia con R1 es de peso, no de legibilidad.'
    filas += f'<div class="fila"><div class="k"><b>{NOM[k]}</b><small>{nota}</small></div><div class="tam">{tam}</div><div class="tam">{inv}</div></div>'

# 2 · productos: el sello es el mismo, cambian el color y el nombre
P = [('Expediente', AZ, 'médicos'), ('Agenda', '#007C8C', 'asistentes'), ('Compras', '#6B3FB8', 'administración'),
     ('Farmacia', '#1B7F52', 'farmacia'), ('Impulsa', '#C73A55', 'campañas de prevención')]
def lockup(prod, col, k='R1', z=44):
    return (f'<div class="lk"><span class="s" style="width:{z}px;height:{z}px">{sym(k, col)}</span>'
            f'<span class="nm"><b>{prod}</b> <i>Manik</i></span></div>')
lks = ''.join(f'<div class="pc">{lockup(p, c)}<small>{u} · <code>{c}</code></small></div>' for p, c, u in P)
barra = ''.join(f'<div class="it{" on" if i == 0 else ""}"><span class="s" style="width:24px;height:24px">{sym("R1", c)}</span>{p}</div>' for i, (p, c, _) in enumerate(P))

open('lamina.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
body{{margin:0;background:{PAPEL};color:{TINTA};font:14px/1.45 Inst,sans-serif;padding:36px;width:1140px}}
h1{{font:600 26px Sora;color:{AZ};margin:0}}.i{{margin:2px 0 22px;color:#4A5674}}h2{{font:600 17px Sora;color:{AZ};margin:26px 0 10px}}
.s{{display:inline-block;flex:none}}.s svg{{display:block;width:100%;height:100%}}
.fila{{display:grid;grid-template-columns:330px 1fr 170px;gap:20px;align-items:center;background:#fff;border:1px solid #E1E6F0;border-radius:16px;padding:16px 18px;margin-bottom:10px}}
.k{{display:grid;gap:4px}}.k small{{color:#4A5674;font-size:12.5px}}.tam{{display:flex;gap:18px;align-items:end}}.neg{{background:#fff;border-radius:22%}}
.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}.pc{{background:#fff;border:1px solid #E1E6F0;border-radius:16px;padding:18px;display:grid;gap:10px}}.pc small{{color:#4A5674}}
.lk{{display:flex;gap:12px;align-items:center}}.nm{{font:24px Sora;letter-spacing:-.01em}}.nm b{{font-weight:600}}.nm i{{font-style:normal;font-weight:400;color:#4A5674}}
.app{{display:grid;grid-template-columns:240px 1fr;background:#fff;border:1px solid #E1E6F0;border-radius:16px;overflow:hidden}}.side{{background:#0F1C3F;padding:14px 10px;display:grid;gap:4px;align-content:start}}
.side .brand{{color:#fff;font:600 15px Sora;padding:6px 8px 12px}}.it{{display:flex;gap:10px;align-items:center;color:#C9D3EA;padding:8px;border-radius:10px;font-size:14px}}.it.on{{background:#1E2D5A;color:#fff}}
.main{{padding:22px;color:#4A5674}}.main b{{color:{TINTA};font:600 20px Sora;display:block;margin-bottom:6px}}
</style></head><body><h1>Manik · el sello y sus productos</h1><p class="i">Ronda 2. Se conserva la M de pulso y se refina para tamaños chicos y una sola tinta. Cada producto se reconoce por su nombre y su color; el sello no cambia.</p>
<h2>1 · La M a 16, 24, 32, 64 y 120 px · en negativo y a una tinta</h2>{filas}
<h2>2 · «Producto + Manik» (con R1)</h2><div class="g">{lks}</div>
<h2>3 · Prueba: los cinco juntos en la barra lateral, a 24 px</h2><div class="app"><div class="side"><div class="brand">MedicalManik</div>{barra}</div><div class="main"><b>Expediente Manik</b>¿Te ubicas en qué producto estás sin leer los nombres? Si sí, el color está trabajando.</div></div>
</body></html>""")
print('ok')
