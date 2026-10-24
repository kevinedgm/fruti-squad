# Manik · ronda 3: la línea R1 no cambia; cada producto suma un modificador que dice qué es
# A · insignia en la esquina · B · el contenedor cuenta el producto
import sys
S = sys.argv[1]; F = f'file://{S}/fuentes'
AZ, PAPEL, TINTA = '#234899', '#F6F8FC', '#14213D'
LINEA = 'M-6 63 L13 63 L27 12 L49 86 L71 25 L84 64 L106 64'
P = [('Expediente', AZ), ('Agenda', '#007C8C'), ('Compras', '#6B3FB8'), ('Farmacia', '#1B7F52'), ('Impulsa', '#C73A55')]
n = [0]
def uid(): n[0] += 1; return f'u{n[0]}'

# Glifos de la insignia, dibujados en una caja de 24 centrada en (0,0), trazo 3
G = {
 'Expediente': '<path d="M-6 -9 H3 L7 -5 V9 H-6 Z M-2 -1 H3 M-2 4 H3"/>',
 'Agenda': '<rect x="-8" y="-6" width="16" height="14" rx="2"/><path d="M-8 -1 H8 M-4 -9 V-4 M4 -9 V-4"/>',
 'Compras': '<path d="M-6 -9 H6 V9 L3 7 L0 9 L-3 7 L-6 9 Z M-2 -3 H2 M-2 2 H2"/>',
 'Farmacia': '<path d="M0 -8 V8 M-8 0 H8"/>',
 'Impulsa': '<path d="M-6 6 L6 -6 M-2 -6 H6 V2"/>',
}
def A(prod, col):  # insignia: disco de papel con el glifo en el color del producto, montado sobre la esquina
    u = uid()
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -12 112 112"><defs><clipPath id="{u}"><rect width="100" height="100" rx="21"/></clipPath></defs>'
            f'<rect width="100" height="100" rx="21" fill="{col}"/><path clip-path="url(#{u})" d="{LINEA}" fill="none" stroke="{PAPEL}" stroke-width="13" stroke-linejoin="round"/>'
            f'<circle cx="94" cy="6" r="18" fill="var(--fondo,#fff)"/><circle cx="94" cy="6" r="14.5" fill="{PAPEL}" stroke="{col}" stroke-width="2.5"/>'
            f'<g transform="translate(94 6) scale(.8)" fill="none" stroke="{col}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">{G[prod]}</g></svg>')

# Contenedores: la silueta del cuadro cambia; la línea es la misma
r = 21
BASE = f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z'
SIL = {
 'Expediente': (f'M0 {r} A{r} {r} 0 0 1 {r} 0 H34 Q38 0 41 -4 L44 -9 Q46 -12 50 -12 H86 A14 14 0 0 1 100 2 V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} Z', ''),
 'Agenda': (BASE, '<rect x="22" y="-14" width="10" height="24" rx="5" fill="{c}" stroke="var(--fondo,#fff)" stroke-width="5" paint-order="stroke"/><rect x="68" y="-14" width="10" height="24" rx="5" fill="{c}" stroke="var(--fondo,#fff)" stroke-width="5" paint-order="stroke"/>'),
 'Compras': (f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V106 L87.5 96 L75 106 L62.5 96 L50 106 L37.5 96 L25 106 L12.5 96 L0 106 V{r} A{r} {r} 0 0 1 {r} 0 Z', ''),
 'Farmacia': (f'M{r} 0 H66 V12 Q66 16 70 16 H82 V28 Q82 32 86 32 H100 V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z',
              '<path d="M90 -6 V20 M77 7 H103" stroke="{c}" stroke-width="8" stroke-linecap="round"/>'),
 'Impulsa': (f'M{r} 0 H72 L100 0 V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z',
             '<path d="M84 -14 H114 V16" fill="none" stroke="{c}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'),
}
def B(prod, col):
    u = uid(); d, extra = SIL[prod]
    if prod == 'Impulsa':  # esquina cortada en diagonal y una flecha que sale de ella
        d = f'M{r} 0 H70 L100 30 V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z'
        extra = '<path d="M80 -2 L102 -2 L102 20 M100 0 L84 16" fill="none" stroke="{c}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-6 -16 120 128"><defs><clipPath id="{u}"><path d="{d}"/></clipPath></defs>'
            f'<path d="{d}" fill="{col}"/><path clip-path="url(#{u})" d="{LINEA}" fill="none" stroke="{PAPEL}" stroke-width="13" stroke-linejoin="round"/>'
            + extra.replace('{c}', col) + '</svg>')

def fila(fn, titulo, nota):
    big = ''.join(f'<figure><span class="s" style="width:110px;height:110px">{fn(p, c)}</span><figcaption><b>{p}</b> Manik</figcaption></figure>' for p, c in P)
    small = ''.join(f'<div class="col">{"".join(f"<span class=s style=width:{z}px;height:{z}px>{fn(p, c)}</span>" for z in (48, 32, 24))}</div>' for p, c in P)
    return f'<section><h2>{titulo}</h2><p>{nota}</p><div class="big">{big}</div><div class="small">{small}</div></section>'

open('lamina.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
:root{{--fondo:#fff}}body{{margin:0;background:{PAPEL};color:{TINTA};font:14px/1.45 Inst,sans-serif;padding:36px;width:1140px}}
h1{{font:600 26px Sora;color:{AZ};margin:0}}.i{{margin:2px 0 18px;color:#4A5674}}
section{{background:#fff;border:1px solid #E1E6F0;border-radius:16px;padding:20px 22px;margin-bottom:14px}}h2{{font:600 18px Sora;color:{AZ};margin:0}}section>p{{margin:2px 0 16px;color:#4A5674}}
.big{{display:flex;gap:30px}}figure{{margin:0;display:grid;justify-items:center;gap:8px;font:15px Sora}}figure b{{font-weight:600}}figcaption{{color:#4A5674}}figcaption b{{color:{TINTA}}}
.s{{display:inline-block}}.s svg{{display:block;width:100%;height:100%;overflow:visible}}.small{{display:flex;gap:42px;margin-top:20px;padding-left:14px}}.col{{display:flex;gap:14px;align-items:end;width:150px}}
</style></head><body><h1>Manik · un modificador por producto</h1><p class="i">Ronda 3. La línea de pulso (R1) es idéntica en los cinco; lo que cambia dice qué producto es. Abajo de cada fila, el mismo sello a 48, 32 y 24 px.</p>
{fila(A, 'A · Insignia en la esquina', 'Un disco con el pictograma del producto se monta sobre la esquina, como una insignia de app. Sistema rígido: misma posición y tamaño en los cinco.')}
{fila(B, 'B · El contenedor cuenta el producto', 'La silueta del cuadro cambia: pestaña de carpeta, argollas de agenda, borde de ticket, cruz de farmacia, esquina que se impulsa. Más integrado, menos regla fija.')}
</body></html>""")
print('ok')
