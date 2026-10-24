# Nabi · familia de iconos del laboratorio: búsqueda en Lucide (Uva E1) y lámina de candidatos
import subprocess, sys, json
S = sys.argv[1]
B = ['node', '../../../../agentes/uva/scripts/buscar-lucide.mjs', '--svg']
C = [  # concepto, [candidatos], recomendado, nota (riesgo o supuesto)
 ('Muestras de agua', ['droplet', 'test-tube', 'glass-water'], 'droplet', 'glass-water se lee como «bebida»: choca con bebidas alcohólicas.'),
 ('Bebidas alcohólicas', ['wine', 'bottle-wine', 'martini'], 'bottle-wine', 'La botella cubre vino, mezcal o cerveza mejor que una copa.'),
 ('Alimentos', ['apple', 'utensils', 'sandwich'], 'apple', 'utensils se lee como «restaurante».'),
 ('Cotizaciones', ['receipt-text', 'calculator', 'file-spreadsheet'], 'receipt-text', 'receipt puede leerse como «recibo pagado»: la etiqueta lo resuelve.'),
 ('Informes de resultados', ['file-check', 'file-chart-column', 'file-badge'], 'file-check', 'Informe liberado; file-badge si se emiten como certificado.'),
 ('Ficha de análisis', ['clipboard-list', 'file-text', 'form'], 'clipboard-list', 'Tabla de datos de captura: se distingue del informe (hoja con ✓).'),
 ('Bitácora', ['notebook-pen', 'notebook-text', 'list-clock'], 'notebook-pen', 'Libreta que se escribe; list-clock si es historial automático.'),
 ('Código de ensayo', ['flask-conical', 'hash', 'barcode'], 'flask-conical', 'Supuesto: es el método de ensayo. Si es el código de la muestra, barcode.'),
 ('Agenda', ['calendar-days', 'calendar-clock', 'calendar'], 'calendar-days', ''),
 ('Clientes', ['users', 'building-2', 'contact'], 'building-2', 'Si los clientes son empresas, el edificio; users ya significa «personas».'),
 ('Hojas de seguridad', ['file-exclamation-point', 'shield-alert', 'triangle-alert'], 'file-exclamation-point', 'Lucide no tiene pictograma SGA: candidato a icono propio de Uva.'),
]
def svg(n, z=32):
    s = subprocess.run(B + [n, '--stroke', '1.5'], capture_output=True, text=True).stdout.strip()
    open(f'svg/{n}.svg', 'w').write(s); return s.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
import os; os.makedirs('svg', exist_ok=True)
INK = '#052A76'
rows = ''
for con, cands, rec, nota in C:
    cells = ''.join(f'<div class="c{" r" if n == rec else ""}">{svg(n)}<span>{n}</span></div>' for n in cands)
    rows += f'<div class="f"><div class="k">{con}<small>{nota}</small></div>{cells}</div>'
fam = ''.join(f'<div class="t">{svg(rec, 24)}<span>{con}</span></div>' for con, _, rec, _ in C)
open('lamina.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo';src:url('file://{S}/fuentes/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}
body{{margin:0;background:#fff;color:#141B33;font:14px/1.4 Archivo,sans-serif;padding:32px;width:1040px}}h1{{font-size:24px;font-stretch:125%;color:{INK};margin:0 0 4px}}.i{{color:#535B70;margin:0 0 18px}}
.f{{display:grid;grid-template-columns:330px repeat(3,1fr);gap:10px;align-items:center;border-top:1px solid #E2E5EC;padding:10px 0}}.k{{font-weight:600;display:grid}}.k small{{font-weight:400;color:#535B70;font-size:12px}}
.c{{display:flex;gap:10px;align-items:center;padding:8px 10px;border-radius:10px;font-size:12px;color:#535B70}}.c svg{{color:#141B33}}.c.r{{background:#EEF2FB;outline:1.5px solid {INK};color:{INK};font-weight:600}}
h2{{font-size:16px;font-stretch:125%;color:{INK};margin:26px 0 10px}}.fam{{display:flex;gap:8px;flex-wrap:wrap}}.t{{display:grid;justify-items:center;gap:6px;width:86px;font-size:11px;text-align:center;color:#535B70}}.t svg{{color:#141B33}}
.osc{{background:{INK};padding:16px 4px;gap:4px;border-radius:12px;margin-top:10px}}.osc .t,.osc .t svg{{color:#fff}}
</style></head><body><h1>Nabi · iconos del laboratorio</h1><p class="i">Búsqueda en Lucide (trazo 1.5): tres candidatos por concepto; el recuadrado es el recomendado.</p>{rows}
<h2>La familia recomendada a 24px</h2><div class="fam">{fam}</div><div class="fam osc">{fam}</div></body></html>""")
json.dump({c: r for c, _, r, _ in C}, open('seleccion.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
