# Manik · ronda 4: propuesta B refinada. La línea R1 es idéntica; el contenedor dice el producto.
# Reglas: (1) el modificador vive en el borde del cuadro, nunca dentro; (2) la línea nunca se recorta por él;
# (3) dos clases de modificador: silueta (carpeta, ticket) o pieza sobre el borde separada por un corte de 5 (argollas, cruz, flecha);
# (4) todos comparten lienzo, así el cuadro mide lo mismo en los cinco.
import sys, os
S = sys.argv[1]; F = f'file://{S}/fuentes'
AZ, CI, PAPEL, TINTA = '#234899', '#00BDD0', '#F6F8FC', '#14213D'
LINEA = 'M-6 63 L13 63 L27 12 L49 86 L71 25 L84 64 L106 64'
VB = '-8 -18 124 126'
r = 21
CUADRO = f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z'
CORTE = 'stroke="var(--fondo,#fff)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"'  # 10 de pieza + 5 de aire por lado
def pieza(d, c, cap='round'):
    return (f'<path d="{d}" fill="none" {CORTE}/>'
            f'<path d="{d}" fill="none" stroke="{c}" stroke-width="10" stroke-linecap="{cap}" stroke-linejoin="round"/>')
PROD = {
 'MedicalManik': (CUADRO, ''),
 'Expediente': ('M0 -2 A10 10 0 0 1 10 -12 H38 C44 -12 46 -10 49 -6 L52 -2 C54 0 56 0 60 0 '
                f'H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} Z', ''),
 'Agenda': (CUADRO, 'M14 -10 V8 M86 -10 V8'),  # argollas fuera de las crestas de la línea
 'Compras': (f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V100 L87.5 90 L75 100 L62.5 90 L50 100 L37.5 90 L25 100 L12.5 90 L0 100 V{r} A{r} {r} 0 0 1 {r} 0 Z', ''),
 'Farmacia': (CUADRO, 'M96 -7 V15 M85 4 H107'),
 'Impulsa': (CUADRO, 'M88 12 L104 -4 M92 -4 H104 V8'),
}
COL = {'MedicalManik': AZ, 'Expediente': AZ, 'Agenda': '#007C8C', 'Compras': '#6B3FB8', 'Farmacia': '#1B7F52', 'Impulsa': '#C73A55'}
n = [0]
def sym(p, col=None, linea=PAPEL):
    n[0] += 1; u = f'k{n[0]}'; c = col or COL[p]; d, extra = PROD[p]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}"><defs><clipPath id="{u}"><path d="{d}"/></clipPath></defs>'
            f'<path d="{d}" fill="{c}"/><path clip-path="url(#{u})" d="{LINEA}" fill="none" stroke="{linea}" stroke-width="13" stroke-linejoin="round"/>'
            + (pieza(extra, c) if extra else '') + '</svg>')
os.makedirs('svg', exist_ok=True)
for p in PROD: open(f'svg/{p.lower()}.svg', 'w').write(sym(p).replace('var(--fondo,#fff)', '#FFFFFF'))

ORDEN = ['MedicalManik', 'Expediente', 'Agenda', 'Compras', 'Farmacia', 'Impulsa']
def s(p, z, **k): return f'<span class="s" style="width:{z}px;height:{z}px">{sym(p, **k)}</span>'
grande = ''.join(f'<figure>{s(p, 128)}<figcaption>{"<b>MedicalManik</b> · sello" if p == "MedicalManik" else f"<b>{p}</b> Manik"}</figcaption></figure>' for p in ORDEN)
tam = ''.join(f'<div class="col">{"".join(s(p, z) for z in (48, 32, 24, 16))}</div>' for p in ORDEN)
tinta = ''.join(s(p, 56, col=TINTA, linea='#FFFFFF') for p in ORDEN)
osc = ''.join(s(p, 56) for p in ORDEN)
lk = ''.join(f'<div class="lk">{s(p, 52)}<span class="nm"><b>{p}</b> <i>Manik</i></span></div>' for p in ORDEN[1:])
barra = ''.join(f'<div class="it{" on" if p == "Farmacia" else ""}">{s(p, 26)}{p}</div>' for p in ORDEN[1:])
open('lamina.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
:root{{--fondo:#fff}}body{{margin:0;background:{PAPEL};color:{TINTA};font:14px/1.45 Inst,sans-serif;padding:36px;width:1140px}}
h1{{font:600 26px Sora;color:{AZ};margin:0}}.i{{margin:2px 0 18px;color:#4A5674;max-width:1000px}}
section{{background:#fff;border:1px solid #E1E6F0;border-radius:16px;padding:20px 22px;margin-bottom:14px}}h2{{font:600 17px Sora;color:{AZ};margin:0 0 14px}}
.s{{display:inline-block;flex:none}}.s svg{{display:block;width:100%;height:100%}}
.row{{display:flex;gap:26px;align-items:end}}figure{{margin:0;display:grid;justify-items:center;gap:8px;font:14px Sora;color:#4A5674}}figure b{{color:{TINTA};font-weight:600}}
.tams{{display:flex;gap:30px;margin-top:22px}}.col{{display:flex;gap:12px;align-items:end;width:150px}}
.dos{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}.fila{{display:flex;gap:16px}}.dark{{background:#0F1C3F;--fondo:#0F1C3F}}.dark h2{{color:#fff}}
.lks{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px 10px}}.lk{{display:flex;gap:10px;align-items:center}}.nm{{font:23px Sora;letter-spacing:-.01em}}.nm b{{font-weight:600}}.nm i{{font-style:normal;color:#4A5674}}
.app{{display:grid;grid-template-columns:230px 1fr;border-radius:14px;overflow:hidden;border:1px solid #E1E6F0}}.side{{background:#0F1C3F;--fondo:#0F1C3F;padding:14px 10px;display:grid;gap:4px;align-content:start}}
.side .b{{display:flex;gap:10px;align-items:center;color:#fff;font:600 15px Sora;padding:4px 8px 14px}}.it{{display:flex;gap:10px;align-items:center;color:#C9D3EA;padding:7px 8px;border-radius:10px}}.it.on{{background:#1E2D5A;color:#fff}}
.main{{padding:22px;color:#4A5674;background:#fff}}.main b{{display:block;font:600 20px Sora;color:{TINTA};margin-bottom:6px}}
</style></head><body><h1>Manik · el contenedor cuenta el producto</h1>
<p class="i">Ronda 4 (B refinada). La línea de pulso es idéntica en los seis. El sello madre es el cuadro limpio; cada producto cambia solo el borde: silueta (carpeta, ticket) o una pieza separada por un corte (argollas, cruz, flecha). La línea nunca se recorta por el modificador.</p>
<section><h2>Sello madre y productos</h2><div class="row">{grande}</div><div class="tams">{tam}</div></section>
<div class="dos"><section><h2>A una tinta</h2><div class="fila">{tinta}</div></section><section class="dark"><h2>Sobre fondo oscuro</h2><div class="fila">{osc}</div></section></div>
<section><h2>Producto + Manik</h2><div class="lks">{lk}</div></section>
<section><h2>En el sistema: barra lateral a 26 px</h2><div class="app"><div class="side"><div class="b">{s("MedicalManik", 28)}MedicalManik</div>{barra}</div><div class="main"><b>Farmacia Manik</b>Inventario, recetas surtidas y existencias por sucursal.</div></div></section>
</body></html>""")
print('ok')
