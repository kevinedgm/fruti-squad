# Nisa Nabani · informe de resultados, rediseño r1. Un solo formato con bloques por norma de referencia.
# Datos de ejemplo (cliente y lote ficticios; estructura y métodos tomados de los informes NNMZ actuales).
# Uso: python3 gen.py → informe.html (para publicar como Artifact)
import os, re
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..')
NN = re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(NS, 'nabi-design-system', 'marca-nisa', 'nisa-nabani-logo.svg')).read().strip())
NN = re.sub(r'\s(width|height)="[^"]*"', '', NN.split('>', 1)[0]) + '>' + NN.split('>', 1)[1]
NN = NN.replace('<svg ', '<svg class="nn" aria-label="Nisa Nabani" role="img" ', 1)
# bloque = (norma, título, regla, [ensayos]); ensayo = (nombre, método, resultado, U, min, max, unidades, fecha, acreditado)
B = [
 ('NOM-070-SCFI-2016', 'Bebidas alcohólicas — Mezcal — Especificaciones', 'Certificación', [
  ('% Alc. Vol.', 'NMX-V-013-NORMEX-2019 · inc. 6 · Densímetro digital', 49.20, 0.02, 35.0, 55.0, '% Alc. Vol. a 20 °C', '07-09-2026', True),
  ('Extracto seco', 'NMX-V-017-NORMEX-2018 · inc. 5 · Gravimetría', '<0.10', None, 0.0, 10.0, 'g/L', '08-09-2026', True),
  ('Metanol', 'NMX-V-005-NORMEX-2018 · inc. 5 · Cromatografía de gases', 288.97, 2.40, 30.0, 300.0, 'mg/100 mL A.A.', '08-09-2026', True),
  ('Alcoholes superiores', 'NMX-V-005-NORMEX-2018 · inc. 5 · Cromatografía de gases', 542.63, 3.99, 100.0, 500.0, 'mg/100 mL A.A.', '08-09-2026', True),
  ('Aldehídos (acetaldehído)', 'NMX-V-005-NORMEX-2018 · inc. 5 · Cromatografía de gases', 11.54, 0.62, 0.0, 40.0, 'mg/100 mL A.A.', '08-09-2026', True),
  ('Furfural', 'NMX-V-004-NORMEX-2018 · inc. 7 · Cromatografía de gases', 3.35, 0.21, 0.0, 5.0, 'mg/100 mL A.A.', '08-09-2026', True),
  ('Plomo', 'NMX-V-050-NORMEX-2010 · inc. 4 · Absorción atómica', '<0.2', None, 0.0, 0.5, 'mg/L', '08-09-2026', True),
  ('Arsénico', 'NMX-V-050-NORMEX-2010 · inc. 4 · Absorción atómica', '<0.001', None, 0.0, 0.5, 'mg/L', '08-09-2026', True)]),
 ('Norma de referencia B (ejemplo)', 'Acidez solicitada por el cliente — norma por confirmar', 'Control de calidad', [
  ('Acidez total (como ácido acético)', 'Método por confirmar · Titulación volumétrica', 64.8, 1.10, None, None, 'mg/100 mL A.A.', '08-09-2026', False)]),
]
def num(v): return isinstance(v, (int, float))
def f(v, d=2): return '—' if v is None else (f'{v:.{d}f}' if num(v) else v)
def decl(r, u, lo, hi):
    if lo is None and hi is None: return 'na', 'No aplica'
    if not num(r): return 'ok', 'Cumple'  # «<LC» por debajo del máximo
    w = u or 0
    a, b = (lo + w if lo is not None else None), (hi - w if hi is not None else None)
    ok = (a is None or r >= a) and (b is None or r <= b)
    return ('ok', 'Cumple') if ok else ('no', 'No cumple')
IC = {'ok': '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M4.8 8.2 7 10.4 11.2 5.9" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>',
      'no': '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M8 4.2v5M8 11.6v.2" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>',
      'na': '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M5 8h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'}
bloques = ''; resumen = ''; n = 0
for i, (norma, tit, uso, ens) in enumerate(B, 1):
    filas = ''; cnt = {'ok': 0, 'no': 0, 'na': 0}
    for nom, met, r, u, lo, hi, un, fe, acr in ens:
        n += 1; c, t = decl(r, u, lo, hi); cnt[c] += 1
        lim = 'N/I' if lo is None and hi is None else f'{f(lo, 1)} – {f(hi, 1)}'
        acep = 'N/I' if lo is None and hi is None else f'{f(lo + (u or 0) if lo is not None else None)} – {f(hi - (u or 0) if hi is not None else None)}'
        filas += (f'<tr class="{c}"><td class="n">{n}</td><td><b>{nom}{"" if acr else "<sup title=Ensayo no acreditado>◊</sup>"}</b><span>{met}</span></td><td class="v">{f(r)}</td><td class="m">{f(u)}</td>'
                  f'<td class="m">{lim}{"" if acep == "N/I" else f"<span>acept. {acep}</span>"}</td><td class="u">{un}</td><td class="m">{fe}</td><td><span class="dc {c}">{IC[c]}{t}</span></td></tr>')
    partes = ', '.join(f'{v} {k}' for k, v in (('cumplen', cnt['ok']), ('no cumplen', cnt['no']), ('sin límite (no aplica)', cnt['na'])) if v)
    resumen += f'<li><span class="bn">{i}</span><div><b>{norma}</b><span>{tit}</span></div><em>{len(ens)} ensayo{"s" if len(ens) > 1 else ""} · {partes}</em></li>'
    bloques += (f'<section class="blq"><header><span class="bn">{i}</span><div><b>{norma}</b><span>{tit}</span></div><span class="cnt">{len(ens)} ensayo{"s" if len(ens) > 1 else ""} · {partes}</span><span class="uso">Para fines de {uso.lower()}</span></header>'
                f'<table><thead><tr><th>#</th><th>Ensayo · método</th><th>Resultado</th><th>Uexp</th><th>Límites mín – máx<br><span class=th2>intervalo de aceptación</span></th><th>Unidades</th><th>Fecha</th><th>Declaración</th></tr></thead><tbody>{filas}</tbody></table></section>')
normas_txt = '; '.join(f'<b>{b[0]}</b> ({b[1]}) para los ensayos del bloque {i}' for i, b in enumerate(B, 1))
html = f'''<title>Informe de resultados Nisa Nabani</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Informe en hoja carta: una sola plantilla con bloques por norma. Azul real y pera institucionales; valores en Plex Mono. Tema claro deliberado (documento). */
:root{{--az:#052A76;--pe:#C2D225;--tx:#141B33;--mu:#535B70;--ln:#D9DEE8;--sk:#F2F4F8;--ok:#1E6B34;--ok-s:#E3F1E4;--no:#A11D1D;--no-s:#FCE4E4;--na:#475467;--na-s:#EEF1F6;
--sans:Poppins,system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:light}}
*{{box-sizing:border-box}}body{{margin:0;background:#E3E7EE;color:var(--tx);font:10.5px/1.45 var(--sans);padding-block:24px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.nota-proto{{max-width:816px;margin:0 auto 14px;font-size:13px;color:#3A4257;background:#fff;border:1px solid var(--ln);border-radius:10px;padding:10px 14px}}
.hoja-w{{overflow-x:auto}}.hoja{{width:816px;min-height:1056px;margin:0 auto;background:#fff;box-shadow:0 10px 30px -12px rgba(20,27,51,.3);padding:26px 36px 18px;display:flex;flex-direction:column;gap:8px}}
.top{{display:grid;grid-template-columns:auto 1fr auto;gap:18px;align-items:end;border-bottom:3px solid var(--az);padding-bottom:8px}}.nn{{height:32px;width:auto}}
.top h1{{font:700 18px/1.1 var(--sans);color:var(--az);margin:0;letter-spacing:.01em}}.top h1 small{{display:block;font:500 10.5px var(--sans);color:var(--mu);margin-top:3px;letter-spacing:0}}
.fol{{text-align:right;display:grid;gap:0;line-height:1.25}}.fol span{{font:600 9px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--mu)}}.fol b{{font:600 15px var(--mono);color:var(--az)}}.fol em{{font-style:normal;font-weight:600}}
.cli{{display:flex;justify-content:space-between;gap:16px;align-items:flex-end}}.cli b{{font:700 13px var(--sans)}}.cli p{{margin:1px 0 0;color:var(--mu)}}.qr{{display:flex;gap:8px;align-items:center;font-size:9px;color:var(--mu);text-align:right}}.qr i{{width:40px;height:40px;border:1px dashed #9AA1B1;border-radius:6px;display:grid;place-items:center;font:600 8px var(--sans);font-style:normal}}
.dos{{display:grid;grid-template-columns:1.1fr 1fr;gap:10px}}.kv{{border:1px solid var(--ln);border-radius:8px;overflow:hidden}}.kv h2{{margin:0;background:var(--sk);font:600 9px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--az);padding:4px 10px}}
.kv dl{{margin:0;display:grid;grid-template-columns:auto minmax(0,1fr);gap:0 8px;padding:4px 10px;font-size:8.8px;line-height:1.32}}.kv dt{{color:var(--mu)}}.kv dd{{margin:0;font-weight:600}}
.rl{{font:400 9.5px var(--sans);color:var(--mu);letter-spacing:0;text-transform:none}}.res h2{{margin:0;font:700 12px var(--sans);color:var(--az);letter-spacing:.06em;text-transform:uppercase}}
.ref{{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:4px}}.ref li{{display:grid;grid-template-columns:auto 1fr auto;gap:10px;align-items:center;border:1px solid var(--ln);border-radius:8px;padding:6px 10px}}
.ref li span:not(.bn),.blq header div span{{display:block;color:var(--mu);font-size:9.5px}}.ref em{{font-style:normal;color:var(--mu);font-size:9.5px;text-align:right}}
.bn{{width:22px;height:22px;border-radius:6px;background:var(--az);color:#fff;font:700 11px/22px var(--sans);text-align:center}}
.blq{{border:1px solid var(--ln);border-radius:8px;overflow:hidden;break-inside:avoid}}.blq .cnt{{font-size:9px;color:var(--mu);text-align:right}}.blq header{{display:grid;grid-template-columns:auto 1fr auto auto;gap:10px;align-items:center;padding:5px 10px;background:var(--sk);border-bottom:1px solid var(--ln)}}.blq header b{{font:700 11.5px var(--sans);color:var(--az)}}
.uso{{font:600 9px var(--sans);letter-spacing:.04em;text-transform:uppercase;color:var(--mu);border:1px solid var(--ln);background:#fff;border-radius:999px;padding:2px 8px}}
table{{width:100%;border-collapse:collapse}}th .th2{{font-weight:500;text-transform:none;letter-spacing:0}}th{{font:600 8px/1.2 var(--sans);letter-spacing:.03em;text-transform:uppercase;color:var(--mu);text-align:left;padding:4px 6px;border-bottom:1px solid var(--ln)}}
td{{padding:2px 6px;border-bottom:1px solid #EDF0F4;vertical-align:middle}}tr:last-child td{{border-bottom:0}}td b{{font-weight:600}}td span:not(.dc){{display:block;color:var(--mu);font-size:7.8px;line-height:1.2}}td b{{line-height:1.25}}
.n{{color:var(--mu);font:500 9px var(--mono)}}.v{{font:600 11px var(--mono)}}.m{{font:400 9.5px var(--mono);white-space:nowrap}}.u{{font-size:8.5px;color:var(--mu);white-space:nowrap}}tr.no .v{{color:var(--no)}}tr.no td{{background:#FFF7F7}}
.dc{{display:inline-flex;align-items:center;gap:4px;font:600 9px/1 var(--sans);border-radius:999px;padding:3px 7px 3px 4px;white-space:nowrap}}.dc svg{{width:11px;height:11px}}.dc.ok{{background:var(--ok-s);color:var(--ok)}}.dc.no{{background:var(--no-s);color:var(--no)}}.dc.na{{background:var(--na-s);color:var(--na)}}
sup{{color:var(--az);font-size:8px;margin-left:2px}}
.obs{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3px 14px;font-size:8px;line-height:1.3;color:#3A4257}}.obs h3{{margin:0 0 2px;font:600 9px var(--sans);color:var(--tx)}}.obs p{{margin:0}}.obs .w{{grid-column:1/-1}}
.firma{{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;margin-top:auto;padding-top:4px}}.fi{{text-align:center;min-width:220px}}.fi i{{display:block;height:22px;border-bottom:1px solid var(--tx);margin-bottom:4px}}.fi b{{display:block}}.fi span{{color:var(--mu);font-size:9px}}
.pie{{border-top:1px solid var(--ln);padding-top:6px;text-align:center;font-size:7.5px;line-height:1.35;color:var(--mu);display:grid;gap:1px}}.pie b{{color:var(--tx)}}
@media print{{body{{background:#fff;padding:0}}.nota-proto{{display:none}}.hoja{{box-shadow:none;margin:0}}@page{{size:letter;margin:0}}}}
</style>
<p class="nota-proto">Prototipo de formato · datos de ejemplo (cliente y lote ficticios). Un solo informe con <b>bloques por norma de referencia</b>: el bloque 2 muestra el caso de un parámetro (acidez) que va bajo otra norma, sin emitir un segundo informe.</p>
<div class="hoja-w"><article class="hoja">
<header class="top">{NN}<h1>Informe de resultados<small>Bebidas alcohólicas</small></h1><div class="fol"><span>Folio de análisis</span><b>NNMZ-56151</b><span>Emisión</span><em>08 de septiembre de 2026</em><span>Versión 1 · Página 1 de 1</span></div></header>
<div class="cli"><div><b>MEZCALERA EJEMPLO S.A. DE C.V.</b><p>Camino a la Presa s/n, Col. Centro, Santiago Matatlán, Oaxaca · C.P. 70440</p></div><div class="qr"><span>Verifica la autenticidad<br>de este informe</span><i>QR</i></div></div>
<div class="dos"><section class="kv"><h2>Datos de la muestra</h2><dl><dt>Producto</dt><dd>Mezcal</dd><dt>Categoría · clase</dt><dd>Mezcal artesanal · Blanco o joven</dd><dt>Maguey</dt><dd>Tepeztate (Agave marmorata)</dd><dt>Lote</dt><dd>LOTE-0001 · 544 L</dd><dt>Folio de muestreo</dt><dd>2700000LBOX</dd><dt>Fecha de muestreo</dt><dd>07-09-2026</dd><dt>Muestreado por</dt><dd>Inspector autorizado (ejemplo)</dd><dt>Estado productor</dt><dd>Oaxaca</dd></dl></section>
<section class="kv"><h2>Datos de recepción</h2><dl><dt>Recepción</dt><dd>07-09-2026 · 13:05</dd><dt>Estudios solicitados</dt><dd>BAFQ-01 · BAFQ-ACID</dd><dt>Presentación</dt><dd>Botella de plástico · 1 L</dd><dt>Condiciones</dt><dd>Temperatura ambiente</dd><dt>Certificación</dt><dd>Organismo certificador (ejemplo)</dd><dt>Observaciones</dt><dd>Sellada por inspector autorizado</dd></dl></section></div>
<section class="res"><h2>Resultados de ensayo <span class="rl">· Este informe reporta ensayos bajo <b>{len(B)} normas de referencia</b>. Cada bloque indica su norma, su propósito y sus límites.</span></h2></section>
{bloques}
<section class="obs"><div><h3>Declaración de conformidad</h3><p>Procedimiento PP-01 y guía ILAC-G8:09/2019. Con límite: regla con zona de seguridad; «Cumple» si el resultado queda dentro del intervalo de aceptación (límites ajustados por Uexp, k = 2, 95 %). Sin límite: «No aplica», sin juicio de conformidad.</p></div>
<div><h3>Abreviaturas</h3><p>N/A: no aplica · N/D: no detectable · N/I: no indica · A.A.: alcohol anhidro · &lt;X: menor que el límite de cuantificación · Uexp: incertidumbre expandida · ◊: ensayo no acreditado.</p></div>
<div><h3>Trazabilidad</h3><p>Muestreo realizado por un inspector autorizado con procedimientos estandarizados; trazabilidad según los requisitos del organismo de certificación.</p></div>
<div class="w"><h3>Descarga de responsabilidad</h3><p>Este informe es válido de acuerdo con: {normas_txt}, siempre que se cumplan los requisitos del organismo de certificación. Los resultados corresponden únicamente a la muestra analizada, recibida en las condiciones especificadas.</p></div></section>
<div class="firma"><div class="fi"><i></i><b>Q.F.B. Nombre del responsable</b><span>Director general</span></div><div class="fi"><i></i><b>Responsable técnico</b><span>Revisó</span></div></div>
<footer class="pie"><b>Consultoría e Investigación en Ciencias Químicas Nisa Nabani S.A.P.I. de C.V.</b><span>Ensayos acreditados por la Entidad Mexicana de Acreditación, A.C. · Acreditación A-0627-061/15 · NMX-EC-17025-IMNC-2018 · Aprobación DGN A-0627-061/15</span><span>Estos resultados no pueden ser reproducidos parcialmente, excepto en su totalidad, y avalan únicamente la muestra descrita.</span><span>Av. Fuerza Aérea Mexicana 607, Col. Reforma, 68050, Oaxaca de Juárez, Oaxaca · cac@nisanabani.com · RP-06-21</span></footer>
</article></div>'''
open(os.path.join(H, 'informe.html'), 'w').write(html); print('ok', n)
