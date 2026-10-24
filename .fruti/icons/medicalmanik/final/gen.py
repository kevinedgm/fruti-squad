# Manik · paquete final: sello madre, 6 productos y el identificador del ecosistema
# Uso: python3 gen.py <scratchpad>  → svg/ (color y una tinta, fondo transparente), tema.json, lamina.html
# Los cortes (separación de piezas, tarjeta de Grupos, línea a una tinta) son máscaras: el SVG sirve sobre cualquier fondo.
import sys, os, json, math
S = sys.argv[1]; F = f'file://{S}/fuentes'
AZ, CI, PAPEL, TINTA, NOCHE = '#234899', '#00BDD0', '#F6F8FC', '#14213D', '#0F1C3F'
LINEA = 'M-6 63 L13 63 L27 12 L49 86 L71 25 L84 64 L106 64'
VB = '-8 -18 126 126'; r = 21
CUADRO = f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z'
PROD = {
 'MedicalManik': (CUADRO, '', '#234899', 'sello madre'),
 'Expediente': ('M0 -2 A10 10 0 0 1 10 -12 H38 C44 -12 46 -10 49 -6 L52 -2 C54 0 56 0 60 0 '
                f'H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} Z', '', '#234899', 'médicos'),
 'Agenda': (CUADRO, 'M14 -10 V8 M86 -10 V8', '#007C8C', 'asistentes'),
 'Compras': (f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V100 L87.5 90 L75 100 L62.5 90 L50 100 L37.5 90 L25 100 L12.5 90 L0 100 V{r} A{r} {r} 0 0 1 {r} 0 Z', '', '#A15C07', 'compras y facturación'),
 'Farmacia': (CUADRO, 'M96 -7 V15 M85 4 H107', '#1B7F52', 'farmacia'),
 'Impulsa': (CUADRO, 'M88 12 L104 -4 M92 -4 H104 V8', '#6B3FB8', 'campañas de prevención y marketing'),
 'Grupos': (CUADRO, '', '#C73A55', 'administradores de clínicas y hospitales'),
}
def simbolo(p, mono=False):
    d, pieza, col, _ = PROD[p]; c = 'currentColor' if mono else col; k = p.lower()
    m = f'<mask id="m-{k}" maskUnits="userSpaceOnUse" x="-8" y="-18" width="126" height="126"><rect x="-8" y="-18" width="126" height="126" fill="#fff"/>'
    if pieza: m += f'<path d="{pieza}" fill="none" stroke="#000" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>'
    if mono: m += f'<path d="{LINEA}" fill="none" stroke="#000" stroke-width="13" stroke-linejoin="round"/>'
    m += '</mask>'
    defs = f'<defs><clipPath id="c-{k}"><path d="{d}"/></clipPath>{m}'
    cuerpo = ''
    if p == 'Grupos':
        defs += f'<mask id="g-{k}" maskUnits="userSpaceOnUse" x="-8" y="-18" width="126" height="126"><rect x="-8" y="-18" width="126" height="126" fill="#fff"/><path d="{d}" fill="#000" stroke="#000" stroke-width="10"/></mask>'
        cuerpo += f'<g mask="url(#g-{k})"><path transform="translate(12 -12)" d="{d}" fill="{c}"/></g>'  # la máscara en el grupo, fuera de la traslación
    defs += '</defs>'
    cuerpo += f'<g mask="url(#m-{k})"><path d="{d}" fill="{c}"/>'
    if not mono: cuerpo += f'<path clip-path="url(#c-{k})" d="{LINEA}" fill="none" stroke="{PAPEL}" stroke-width="13" stroke-linejoin="round"/>'
    cuerpo += '</g>'
    if pieza: cuerpo += f'<path d="{pieza}" fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
    titulo = 'MedicalManik' if p == 'MedicalManik' else f'{p} Manik'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" role="img" aria-label="{titulo}"><title>{titulo}</title>{defs}{cuerpo}</svg>'

ORDEN = [p for p in PROD if p != 'MedicalManik']
def ecosistema(mono=False):  # A · mosaico: emblema fijo de la familia (siempre seis cuadros, aunque haya más apps)
    c, g, x0 = 5.6, 1.6, 2.8; y0 = 12 - c - g / 2; out = ''
    for i, p in enumerate(ORDEN):
        x = x0 + (i % 3) * (c + g); y = y0 + (i // 3) * (c + g)
        out += f'<rect x="{x:.2f}" y="{y:.2f}" width="{c}" height="{c}" rx="1.6" fill="{"currentColor" if mono else PROD[p][2]}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true">{out}</svg>'

os.makedirs('svg', exist_ok=True)
for p in PROD:
    open(f'svg/{p.lower()}.svg', 'w').write(simbolo(p))
    open(f'svg/{p.lower()}-1tinta.svg', 'w').write(simbolo(p, True))
open('svg/ecosistema.svg', 'w').write(ecosistema())
open('svg/ecosistema-1tinta.svg', 'w').write(ecosistema(True))

def lum(h):
    c = [int(h[i:i+2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b): la, lb = sorted([lum(a), lum(b)], reverse=True); return round((la + .05) / (lb + .05), 2)
tema = {'ecosistema': 'Ecosistema Manik', 'empresa': 'MedicalManik', 'patron_nombre': '<Producto> Manik',
        'linea': PAPEL, 'acento_marca': {'hex': CI, 'uso': 'acento gráfico; no como fondo de texto ni de producto (2.29:1 con blanco)'},
        'tinta': TINTA, 'noche': NOCHE,
        'productos': {p: {'hex': PROD[p][2], 'para': PROD[p][3], 'contraste_blanco': cr(PROD[p][2], '#FFFFFF'), 'contraste_noche': cr(PROD[p][2], NOCHE)} for p in PROD}}
json.dump(tema, open('tema.json', 'w'), ensure_ascii=False, indent=2)

def img(f, z): return f'<img src="svg/{f}.svg" width="{z}" height="{z}">'
grande = ''.join(f'<figure>{img(p.lower(), 112)}<figcaption>{"<b>MedicalManik</b>" if p == "MedicalManik" else f"<b>{p}</b> Manik"}<small>{PROD[p][2]}</small></figcaption></figure>' for p in PROD)
tinta = ''.join(f'<span style="color:{TINTA}">{open(f"svg/{p.lower()}-1tinta.svg").read()}</span>' for p in PROD)
osc = ''.join(img(p.lower(), 60) for p in PROD)
eco = f'<div class="eco">{img("ecosistema", 64)}<span style="color:{TINTA}" class="m">{ecosistema(True)}</span><div class="ew"><b>Ecosistema</b> Manik</div></div>'
open('lamina.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
body{{margin:0;background:{PAPEL};color:{TINTA};font:14px/1.45 Inst,sans-serif;padding:36px;width:1140px}}h1{{font:600 28px Sora;color:{AZ};margin:0}}.i{{margin:2px 0 20px;color:#4A5674}}
section{{background:#fff;border:1px solid #E1E6F0;border-radius:16px;padding:20px 22px;margin-bottom:14px}}h2{{font:600 16px Sora;color:{AZ};margin:0 0 14px}}
.row{{display:flex;gap:16px;align-items:end}}figure{{margin:0;display:grid;justify-items:center;gap:6px;font:13px Sora;color:#4A5674;text-align:center}}figure b{{color:{TINTA};font-weight:600}}figure small{{display:block;font:11px Inst;color:#8A93A8}}
.dos{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}.f{{display:flex;gap:14px}}.f span svg,.f img{{width:56px;height:56px;display:block}}.dark{{background:{NOCHE}}}.dark h2{{color:#fff}}
.eco{{display:flex;gap:22px;align-items:center}}.m svg{{width:64px;height:64px;display:block}}.ew{{font:30px Sora;color:#4A5674}}.ew b{{color:{TINTA};font-weight:600}}
</style></head><body><h1>Ecosistema Manik · paquete final</h1><p class="i">Sello madre MedicalManik, seis productos «Producto + Manik» y el identificador del ecosistema. Fondos transparentes: los cortes son máscaras.</p>
<section><h2>Sello madre y productos</h2><div class="row">{grande}</div></section>
<div class="dos"><section><h2>A una tinta</h2><div class="f">{tinta}</div></section><section class="dark"><h2>Sobre fondo oscuro</h2><div class="f">{osc}</div></section></div>
<section><h2>Identificador del ecosistema · color y una tinta</h2>{eco}</section></body></html>""")
print('ok')
