# Nisa Nabani · informe de resultados, rediseño r2: hoja membretada y paginación.
# Membrete: banda azul real con logo blanco y pestaña pera del folio, filo pera a la izquierda, marca de agua del logo y pie institucional.
# Paginación (en el navegador, midiendo el contenido real): encabezado en cada hoja, bloques que continúan con «(continuación)»
# y títulos de columna repetidos, sin título de bloque huérfano, firma solo en la última hoja, «Página X de N».
# Datos de ejemplo (clientes, lotes y límites ficticios o por confirmar). Uso: python3 gen.py → informe.html
import json, os, re
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..')
raw = re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(NS, 'nabi-design-system', 'marca-nisa', 'nisa-nabani-logo.svg')).read().strip())
raw = re.sub(r'\s(width|height)="[^"]*"', '', raw.split('>', 1)[0]) + '>' + raw.split('>', 1)[1]
AZRGB = 'rgb(1.998901%, 16.499329%, 46.299744%)'
LOGO_B = raw.replace(AZRGB, '#FFFFFF').replace('<svg ', '<svg class="nn" aria-label="Nisa Nabani" role="img" ', 1)
MARCA = raw.replace(AZRGB, '#052A76').replace('<svg ', '<svg class="wm" aria-hidden="true" ', 1)
PERGB = 'rgb(76.098633%, 82.398987%, 14.498901%)'
LOGO_A = raw.replace(PERGB, '#052A76').replace('<svg ', '<svg class="nn" aria-label="Nisa Nabani" role="img" ', 1)  # una tinta azul real, para bandas claras
# tema por tipo: oficial = institucional; preliminar = color del área (secundarios del manual de Nisa Nabani)
TEMAS = {'oficial': dict(band='#052A76', band2='#0A3487', tx='#FFFFFF', sub='#C9D3EA', tab='#C2D225', tabtx='#052A76', s1='#C2D225', s2='#052A76', logo='b'),
         'aguas': dict(band='#00B4D8', band2='#0098B8', tx='#052A76', sub='#08345F', tab='#FFFFFF', tabtx='#05597A', s1='#00B4D8', s2='#7FDDEE', logo='a'),
         'bebidas': dict(band='#3D67AE', band2='#2F5596', tx='#FFFFFF', sub='#DCE6F7', tab='#FFFFFF', tabtx='#2F5596', s1='#3D67AE', s2='#9DB4DD', logo='b'),
         'alimentos': dict(band='#F48C06', band2='#E07B00', tx='#052A76', sub='#3B2A0A', tab='#FFFFFF', tabtx='#9A4F00', s1='#F48C06', s2='#FAC27E', logo='a')}
def R(nombre, metodo, res, u, lo, hi, un, fecha='08-09-2026', acr=True): return dict(n=nombre, m=metodo, r=res, u=u, lo=lo, hi=hi, un=un, f=fecha, a=acr)
CORTO = dict(clave='bebidas', folio='NNMZ-56151', area='Bebidas alcohólicas', emision='08 de septiembre de 2026', cliente='MEZCALERA EJEMPLO S.A. DE C.V.', dir='Camino a la Presa s/n, Col. Centro, Santiago Matatlán, Oaxaca · C.P. 70440',
  muestra=[('Producto', 'Mezcal'), ('Categoría · clase', 'Mezcal artesanal · Blanco o joven'), ('Maguey', 'Tepeztate (Agave marmorata)'), ('Lote', 'LOTE-0001 · 544 L'), ('Folio de muestreo', '2700000LBOX'), ('Fecha de muestreo', '07-09-2026'), ('Muestreado por', 'Inspector autorizado (ejemplo)')],
  recepcion=[('Recepción', '07-09-2026 · 13:05'), ('Estudios solicitados', 'BAFQ-01 · BAFQ-ACID'), ('Presentación', 'Botella de plástico · 1 L'), ('Condiciones', 'Temperatura ambiente'), ('Certificación', 'Organismo certificador (ejemplo)'), ('Observaciones', 'Sellada por inspector autorizado')],
  bloques=[dict(norma='NOM-070-SCFI-2016', titulo='Bebidas alcohólicas — Mezcal — Especificaciones', uso='certificación', filas=[
    R('% Alc. Vol.', 'NMX-V-013-NORMEX-2019 · inc. 6 · Densímetro digital', 49.20, 0.02, 35.0, 55.0, '% Alc. Vol. a 20 °C', '07-09-2026'),
    R('Extracto seco', 'NMX-V-017-NORMEX-2018 · inc. 5 · Gravimetría', '<0.10', None, 0.0, 10.0, 'g/L'),
    R('Metanol', 'NMX-V-005-NORMEX-2018 · inc. 5 · Cromatografía de gases', 288.97, 2.40, 30.0, 300.0, 'mg/100 mL A.A.'),
    R('Alcoholes superiores', 'NMX-V-005-NORMEX-2018 · inc. 5 · Cromatografía de gases', 542.63, 3.99, 100.0, 500.0, 'mg/100 mL A.A.'),
    R('Aldehídos (acetaldehído)', 'NMX-V-005-NORMEX-2018 · inc. 5 · Cromatografía de gases', 11.54, 0.62, 0.0, 40.0, 'mg/100 mL A.A.'),
    R('Furfural', 'NMX-V-004-NORMEX-2018 · inc. 7 · Cromatografía de gases', 3.35, 0.21, 0.0, 5.0, 'mg/100 mL A.A.'),
    R('Plomo', 'NMX-V-050-NORMEX-2010 · inc. 4 · Absorción atómica', '<0.2', None, 0.0, 0.5, 'mg/L'),
    R('Arsénico', 'NMX-V-050-NORMEX-2010 · inc. 4 · Absorción atómica', '<0.001', None, 0.0, 0.5, 'mg/L')]),
   dict(norma='Norma de referencia B (ejemplo)', titulo='Acidez solicitada por el cliente — norma por confirmar', uso='control de calidad', filas=[
    R('Acidez total (como ácido acético)', 'Método por confirmar · Titulación volumétrica', 64.8, 1.10, None, None, 'mg/100 mL A.A.', acr=False)])],
  trazabilidad='Muestreo realizado por un inspector autorizado con procedimientos estandarizados; trazabilidad según los requisitos del organismo de certificación.')
AG = [  # agua: nombre, método, resultado, U, min, max, unidades (límites de ejemplo, por confirmar con la norma)
 ('Coliformes totales', 'NMX-AA-042-SCFI-2015 · NMP', '<1.1', None, None, 1.1, 'NMP/100 mL'), ('Escherichia coli', 'NMX-AA-042-SCFI-2015 · NMP', '<1.1', None, None, 1.1, 'NMP/100 mL'),
 ('Coliformes fecales', 'NMX-AA-042-SCFI-2015 · NMP', '<1.1', None, None, 1.1, 'NMP/100 mL'), ('pH', 'NMX-AA-008-SCFI-2016 · Potenciometría', 7.42, 0.05, 6.5, 8.5, 'Unidades de pH'),
 ('Conductividad eléctrica', 'NMX-AA-093-SCFI-2018 · Conductimetría', 612.0, 8.0, None, None, 'µS/cm'), ('Turbiedad', 'NMX-AA-038-SCFI-2001 · Nefelometría', 0.62, 0.05, None, 4.0, 'UTN'),
 ('Color verdadero', 'NMX-AA-045-SCFI-2001 · Comparación visual', '<5', None, None, 15, 'U Pt-Co'), ('Sólidos disueltos totales', 'NMX-AA-034-SCFI-2015 · Gravimetría', 398.0, 6.0, None, 1000.0, 'mg/L'),
 ('Dureza total (como CaCO₃)', 'NMX-AA-072-SCFI-2001 · Titulación', 268.0, 4.1, None, 500.0, 'mg/L'), ('Alcalinidad total', 'NMX-AA-036-SCFI-2001 · Titulación', 211.0, 3.2, None, None, 'mg/L'),
 ('Cloruros', 'NMX-AA-073-SCFI-2001 · Argentometría', 41.3, 1.2, None, 250.0, 'mg/L'), ('Sulfatos', 'NMX-AA-074-SCFI-2014 · Turbidimetría', 58.6, 2.1, None, 400.0, 'mg/L'),
 ('Nitratos (como N)', 'NMX-AA-079-SCFI-2001 · Espectrofotometría UV', 6.8, 0.3, None, 11.0, 'mg/L'), ('Nitritos (como N)', 'NMX-AA-099-SCFI-2006 · Espectrofotometría', '<0.01', None, None, 0.9, 'mg/L'),
 ('Nitrógeno amoniacal', 'NMX-AA-026-SCFI-2010 · Destilación y titulación', '<0.10', None, None, 0.5, 'mg/L'), ('Fluoruros', 'NMX-AA-077-SCFI-2001 · Electrodo selectivo', 0.84, 0.04, None, 1.5, 'mg/L'),
 ('Cloro residual libre', 'NMX-AA-108-SCFI-2001 · Colorimetría DPD', 0.6, 0.05, 0.2, 1.5, 'mg/L'), ('Cianuros totales', 'NMX-AA-058-SCFI-2001 · Espectrofotometría', '<0.01', None, None, 0.07, 'mg/L'),
 ('Aluminio', 'NMX-AA-051-SCFI-2016 · Absorción atómica', '<0.05', None, None, 0.2, 'mg/L'), ('Arsénico', 'NMX-AA-051-SCFI-2016 · Absorción atómica', 0.012, 0.001, None, 0.025, 'mg/L'),
 ('Bario', 'NMX-AA-051-SCFI-2016 · Absorción atómica', 0.08, 0.01, None, 1.3, 'mg/L'), ('Cadmio', 'NMX-AA-051-SCFI-2016 · Absorción atómica', '<0.002', None, None, 0.003, 'mg/L'),
 ('Cobre', 'NMX-AA-051-SCFI-2016 · Absorción atómica', '<0.02', None, None, 2.0, 'mg/L'), ('Cromo total', 'NMX-AA-051-SCFI-2016 · Absorción atómica', '<0.01', None, None, 0.05, 'mg/L'),
 ('Hierro', 'NMX-AA-051-SCFI-2016 · Absorción atómica', 0.34, 0.02, None, 0.3, 'mg/L'), ('Manganeso', 'NMX-AA-051-SCFI-2016 · Absorción atómica', 0.06, 0.01, None, 0.15, 'mg/L'),
 ('Mercurio', 'NMX-AA-051-SCFI-2016 · Vapor frío', '<0.0005', None, None, 0.006, 'mg/L'), ('Plomo', 'NMX-AA-051-SCFI-2016 · Absorción atómica', '<0.005', None, None, 0.01, 'mg/L'),
 ('Sodio', 'NMX-AA-051-SCFI-2016 · Absorción atómica', 38.0, 1.5, None, 200.0, 'mg/L'), ('Zinc', 'NMX-AA-051-SCFI-2016 · Absorción atómica', 0.11, 0.01, None, 5.0, 'mg/L'),
]
LARGO = dict(clave='aguas', folio='NNAG-61204', area='Aguas', emision='22 de octubre de 2026', cliente='HOTEL EJEMPLO DEL PACÍFICO S.A. DE C.V.', dir='Av. del Mar 100, Zona Hotelera, Mazatlán, Sinaloa · C.P. 82110',
  muestra=[('Producto', 'Agua para uso y consumo humano'), ('Punto de muestreo', 'Cisterna principal · llave de salida'), ('Lote', 'PM-03'), ('Folio de muestreo', 'AG-2610-0147'), ('Fecha de muestreo', '20-10-2026 · 08:40'), ('Muestreado por', 'Personal del laboratorio (ejemplo)')],
  recepcion=[('Recepción', '20-10-2026 · 14:10'), ('Estudios solicitados', 'AGFQ-01 · AGMB-01 · AGME-01'), ('Presentación', 'Frascos estériles y de plástico'), ('Condiciones', 'Refrigeración 4 °C'), ('Observaciones', 'Llegan dentro del tiempo de conservación')],
  bloques=[dict(norma='NOM-127-SSA1-2021', titulo='Agua para uso y consumo humano — Límites permisibles (límites de ejemplo, por confirmar)', uso='control sanitario', filas=[R(*a, fecha='21-10-2026') for a in AG[:26]]),
           dict(norma='NOM-201-SSA1-2015 (ejemplo)', titulo='Agua y hielo para consumo humano envasados — parámetros solicitados', uso='control de calidad', filas=[R(*a, fecha='21-10-2026') for a in AG[26:]])],
  trazabilidad='Muestreo realizado por personal del laboratorio conforme al plan de muestreo acordado con el cliente; la muestra se conservó y transportó en las condiciones del método.')
def txt(v): return v if (v is None or isinstance(v, str)) else repr(v)
for d in (CORTO, LARGO):
    for b in d['bloques']:
        for r in b['filas']:
            for k in ('r', 'u', 'lo', 'hi'): r[k] = txt(r[k])
CORTO['bloques'][0]['filas'][0]['r'] = '49.20'
ALIM = dict(clave='alimentos', folio='NNAL-61310', area='Alimentos', emision='24 de octubre de 2026', cliente='RESTAURANTE EJEMPLO S.A. DE C.V.', dir='Calle Macedonio Alcalá 200, Centro, Oaxaca de Juárez, Oaxaca · C.P. 68000',
  muestra=[('Producto', 'Superficie en contacto con alimentos'), ('Punto de muestreo', 'Tabla de corte · cocina principal'), ('Área muestreada', '100 cm²'), ('Fecha de muestreo', '23-10-2026 · 10:15'), ('Muestreado por', 'Personal del laboratorio (ejemplo)')],
  recepcion=[('Recepción', '23-10-2026 · 13:40'), ('Estudios solicitados', 'ALMB-05'), ('Presentación', 'Hisopo en medio de transporte'), ('Condiciones', 'Refrigeración 4 °C')],
  bloques=[dict(norma='NOM-251-SSA1-2009 (ejemplo)', titulo='Prácticas de higiene para el proceso de alimentos — límites por confirmar', uso='control de calidad', filas=[
    R('Mesófilos aerobios', 'NOM-092-SSA1-1994 · Cuenta en placa', '120', None, None, '400', 'UFC/cm²', '24-10-2026'),
    R('Coliformes totales', 'NOM-113-SSA1-1994 · Cuenta en placa', '<10', None, None, '200', 'UFC/cm²', '24-10-2026'),
    R('Mohos y levaduras', 'NOM-111-SSA1-1994 · Cuenta en placa', '<10', None, None, None, 'UFC/cm²', '24-10-2026'),
    R('Salmonella spp.', 'NOM-210-SSA1-2014 · Presencia/ausencia', 'Ausente', None, None, None, 'en 100 cm²', '24-10-2026')])],
  trazabilidad='Muestreo realizado por personal del laboratorio conforme al plan acordado con el cliente.')
for d in (ALIM,):
    for b in d['bloques']:
        for r in b['filas']:
            for k in ('r', 'u', 'lo', 'hi'): r[k] = r[k] if (r[k] is None or isinstance(r[k], str)) else repr(r[k])
DOCS = {'corto': CORTO, 'largo': LARGO, 'alim': ALIM}
html = '''<title>Informe de resultados Nisa Nabani</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Oficial (certificación) = colores institucionales; preliminar = color del área (secundarios del manual). Hoja membretada carta (816 × 1056 px a 96 ppp). Banda azul real con logo blanco, pestaña pera del folio, filo pera a la izquierda, marca de agua del logo, pie institucional. Tema claro deliberado (documento). */
:root{--az:#052A76;--az2:#0A3487;--pe:#C2D225;--tx:#141B33;--mu:#535B70;--ln:#D9DEE8;--sk:#F2F4F8;--ok:#1E6B34;--ok-s:#E3F1E4;--no:#A11D1D;--no-s:#FCE4E4;--na:#475467;--na-s:#EEF1F6;
--sans:Poppins,system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:light}
*{box-sizing:border-box}body{margin:0;background:#DCE1EA;color:var(--tx);font:10px/1.42 var(--sans);padding-block:20px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.ctl{max-width:816px;margin:0 auto 14px;display:flex;gap:10px;align-items:center;flex-wrap:wrap;font-size:13px;color:#3A4257}.ctl .tabs{display:flex;background:#fff;border:1px solid var(--ln);border-radius:10px;padding:3px}
.ctl button{font:600 13px var(--sans);border:0;background:none;border-radius:8px;padding:8px 12px;min-height:38px;cursor:pointer;color:#3A4257}.ctl button[aria-pressed="true"]{background:var(--az);color:#fff}.ctl button:focus-visible{outline:3px solid var(--pe);outline-offset:2px}
.hojas{overflow-x:auto;display:grid;gap:22px;justify-content:center}
.hoja{width:816px;height:1056px;background:#fff;box-shadow:0 14px 34px -14px rgba(20,27,51,.35);position:relative;overflow:hidden;display:flex;flex-direction:column}
.hoja::before{content:"";position:absolute;left:0;top:0;bottom:0;width:6px;background:linear-gradient(180deg,var(--s1),var(--s1) 60%,var(--s2));z-index:2}
.wm{position:absolute;width:560px;left:128px;top:380px;opacity:.035;pointer-events:none}
.banda{background:linear-gradient(115deg,var(--band) 0%,var(--band) 62%,var(--band2) 100%);color:var(--btx);padding:22px 40px 18px 46px;display:grid;grid-template-columns:auto 1fr auto;gap:22px;align-items:center;position:relative}
.banda::after{content:"";position:absolute;right:0;bottom:-1px;width:42%;height:4px;background:var(--tabbg)}.hoja.prel .banda::after{background:var(--band2)}
.nn{height:38px;width:auto;display:block}.banda h1{margin:0;font:700 17px/1.1 var(--sans);letter-spacing:.02em;text-transform:uppercase}.banda h1 small{display:block;font:500 10.5px var(--sans);letter-spacing:.04em;text-transform:none;color:var(--bsub);margin-top:4px}
.tab{background:var(--tabbg);color:var(--tabtx);box-shadow:0 2px 8px rgba(20,27,51,.15);border-radius:10px;padding:8px 14px;text-align:right;line-height:1.25}.tab span{display:block;font:600 8px var(--sans);letter-spacing:.1em;text-transform:uppercase;opacity:.8}.tab b{display:block;font:600 15px var(--mono)}.tab em{font-style:normal;font-weight:600;font-size:10px}
.banda.cont{padding:12px 40px 10px 46px}.banda.cont .nn{height:26px}.banda.cont h1{font-size:12px}.banda.cont .tab{padding:5px 12px}.banda.cont .tab b{font-size:13px}
.cuerpo>*{flex-shrink:0}.cuerpo{flex:1;min-height:0;overflow:hidden;padding:16px 40px 6px 46px;display:flex;flex-direction:column;gap:9px;position:relative}
.pie{padding:8px 40px 12px 46px;border-top:1px solid var(--ln);display:grid;grid-template-columns:1fr auto;gap:2px 16px;align-items:end;font-size:7.4px;line-height:1.35;color:var(--mu);background:linear-gradient(180deg,#fff,#F7F8FB)}
.pie b{color:var(--tx);font-size:8px}.pie .pg{grid-row:1/span 4;grid-column:2;text-align:right;font:600 9px var(--sans);color:var(--az)}.pie .pg small{display:block;font:500 7.4px var(--mono);color:var(--mu)}
.cli{display:flex;justify-content:space-between;gap:16px;align-items:flex-end}.cli .ov{font:600 8px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--mu)}.cli b{display:block;font:700 13px var(--sans)}.cli p{margin:1px 0 0;color:var(--mu)}
.qr{display:flex;gap:8px;align-items:center;font-size:8.5px;color:var(--mu);text-align:right}.qr i{width:40px;height:40px;border:1.5px dashed #9AA1B1;border-radius:6px;display:grid;place-items:center;font:600 8px var(--sans);font-style:normal}
.cont-cli{display:flex;justify-content:space-between;color:var(--mu);font-size:9px;border-bottom:1px solid var(--ln);padding-bottom:6px}.cont-cli b{color:var(--tx)}
.dos{display:grid;grid-template-columns:1.1fr 1fr;gap:10px}.kv{border:1px solid var(--ln);border-radius:8px;overflow:hidden;background:rgba(255,255,255,.85)}.kv h2{margin:0;font:600 8.5px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--az);padding:5px 10px;border-bottom:2px solid var(--pe);background:var(--sk)}
.kv dl{margin:0;display:grid;grid-template-columns:auto minmax(0,1fr);gap:0 8px;padding:5px 10px;font-size:8.8px;line-height:1.35}.kv dt{color:var(--mu)}.kv dd{margin:0;font-weight:600}
.sec{display:flex;align-items:baseline;gap:10px;border-bottom:2px solid var(--az);padding-bottom:4px}.sec h2{margin:0;font:700 11.5px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--az)}.sec span{color:var(--mu);font-size:9px}
.blq{border:1px solid var(--ln);border-radius:8px;overflow:hidden;background:rgba(255,255,255,.9)}.bh{display:grid;grid-template-columns:auto 1fr auto auto;gap:10px;align-items:center;padding:5px 10px;background:var(--sk);border-bottom:1px solid var(--ln)}
.bn{width:22px;height:22px;border-radius:6px;background:var(--az);color:#fff;font:700 11px/22px var(--sans);text-align:center}.bh b{font:700 11px var(--sans);color:var(--az)}.bh b i{font-style:normal;font-weight:500;color:var(--mu);font-size:9px}.bh div span{display:block;color:var(--mu);font-size:8.8px}
.bh .c{font-size:8.5px;color:var(--mu);text-align:right}.uso{font:600 8px var(--sans);letter-spacing:.05em;text-transform:uppercase;color:var(--az);border:1px solid #C9D3EA;background:#fff;border-radius:999px;padding:2px 8px;white-space:nowrap}
table{width:100%;border-collapse:collapse}th{font:600 7.6px/1.2 var(--sans);letter-spacing:.03em;text-transform:uppercase;color:var(--mu);text-align:left;padding:4px 6px;border-bottom:1px solid var(--ln)}th .t2{font-weight:500;text-transform:none;letter-spacing:0}
td{padding:2px 6px;border-bottom:1px solid #EDF0F4;vertical-align:middle;height:29px}tr:last-child td{border-bottom:0}td b{font-weight:600;line-height:1.25}td span:not(.dc){display:block;color:var(--mu);font-size:7.6px;line-height:1.2}
.n{color:var(--mu);font:500 8.5px var(--mono);width:20px}.v{font:600 10.5px var(--mono);white-space:nowrap}.m{font:400 9px var(--mono);white-space:nowrap}.u{font-size:8.3px;color:var(--mu);white-space:nowrap}
tr.no .v{color:var(--no)}tr.no td{background:#FFF6F6}sup{color:var(--az);font-size:8px;margin-left:2px}
.dc{display:inline-flex;align-items:center;gap:4px;font:600 8.5px/1 var(--sans);border-radius:999px;padding:3px 7px 3px 4px;white-space:nowrap}.dc svg{width:10px;height:10px}.dc.ok{background:var(--ok-s);color:var(--ok)}.dc.no{background:var(--no-s);color:var(--no)}.dc.na{background:var(--na-s);color:var(--na)}
.obs{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3px 14px;font-size:7.9px;line-height:1.3;color:#3A4257}.obs h3{margin:0 0 2px;font:600 8.5px var(--sans);color:var(--tx)}.obs p{margin:0}.obs .w{grid-column:1/-1}
.firma{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;padding-top:6px}.fi{text-align:center;min-width:220px}.fi i{display:block;height:26px;border-bottom:1px solid var(--tx);margin-bottom:4px}.fi b{display:block}.fi span{color:var(--mu);font-size:8.5px}
.sello{width:70px;height:70px;border-radius:50%;border:1.5px solid var(--az);display:grid;place-items:center;text-align:center;font:600 6.5px/1.2 var(--sans);color:var(--az);letter-spacing:.05em;text-transform:uppercase;opacity:.8}
.prelim{position:absolute;left:50%;top:52%;transform:translate(-50%,-50%) rotate(-28deg);font:800 96px var(--sans);letter-spacing:.08em;color:var(--band);opacity:.07;pointer-events:none;white-space:nowrap}.tab .pt{display:inline-block;background:var(--band);color:var(--btx);border-radius:4px;padding:1px 6px;margin-bottom:3px;font:700 8px var(--sans);letter-spacing:.12em;opacity:1}
.sigue{position:absolute;right:40px;bottom:2px;margin:0;text-align:right;font:500 8.5px var(--sans);color:var(--mu)}
@media print{body{background:#fff;padding:0}.ctl{display:none}.hojas{display:block}.hoja{box-shadow:none;margin:0;break-after:page}@page{size:letter;margin:0}}
</style>
<div class="ctl"><div class="tabs" role="group" aria-label="Ejemplo"><button data-doc="corto" aria-pressed="true">Bebidas · 9 ensayos</button><button data-doc="largo" aria-pressed="false">Aguas · 30 ensayos</button><button data-doc="alim" aria-pressed="false">Alimentos · 4 ensayos</button></div><div class="tabs" role="group" aria-label="Tipo de informe"><button data-tipo="oficial" aria-pressed="true">Oficial</button><button data-tipo="preliminar" aria-pressed="false">Preliminar</button></div><span>Oficial (certificación): colores institucionales. Preliminar: color del área. Datos de ejemplo.</span></div>
<div class="hojas" id="hojas" aria-live="polite"></div>
<script>
const DOCS=__DOCS__,LOGOS={b:__LOGO__,a:__LOGOA__},MARCA=__MARCA__,TEMAS=__TEMAS__;let TIPO='oficial',DOC='corto';
const IC={ok:'<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M4.8 8.2 7 10.4 11.2 5.9" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>',
no:'<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M8 4.2v5M8 11.6v.2" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>',
na:'<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M5 8h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'};
const T={ok:'Cumple',no:'No cumple',na:'No aplica'};
const num=v=>v!=null&&!/^[<>]/.test(v)&&!isNaN(parseFloat(v)),P=v=>parseFloat(v),dec=v=>v&&v.includes('.')?v.split('.')[1].length:0;
function decl(r){if(r.lo==null&&r.hi==null)return'na';if(!num(r.r))return'ok';const w=r.u?P(r.u):0,a=r.lo!=null?P(r.lo)+w:null,b=r.hi!=null?P(r.hi)-w:null,x=P(r.r);return((a==null||x>=a)&&(b==null||x<=b))?'ok':'no';}
function rango(lo,hi){if(lo==null&&hi==null)return'N/I';if(lo==null)return`≤ ${hi}`;if(hi==null)return`≥ ${lo}`;return`${lo} – ${hi}`;}
function acepta(r){if(r.lo==null&&r.hi==null)return'';const w=r.u?P(r.u):0,d=Math.max(dec(r.lo||''),dec(r.hi||''),dec(r.u||''));const lo=r.lo!=null?(P(r.lo)+w).toFixed(d):null,hi=r.hi!=null?(P(r.hi)-w).toFixed(d):null;return`<span>acept. ${rango(lo,hi)}</span>`;}
const el=(h)=>{const t=document.createElement('template');t.innerHTML=h.trim();return t.content.firstElementChild;};
function hoja(d,primera){
 const pre=TIPO==='preliminar',t=TEMAS[pre?d.clave:'oficial'];
 const h=el(`<article class="hoja${pre?' prel':''}" style="--band:${t.band};--band2:${t.band2};--btx:${t.tx};--bsub:${t.sub};--tabbg:${t.tab};--tabtx:${t.tabtx};--s1:${t.s1};--s2:${t.s2}">${MARCA}${pre?'<span class="prelim" aria-hidden="true">PRELIMINAR</span>':''}<header class="banda${primera?'':' cont'}">${LOGOS[t.logo]}<h1>Informe ${pre?'preliminar':'de resultados'}<small>${d.area}${pre?' · no válido para certificación':' · para fines de certificación'}</small></h1><div class="tab">${pre?'<span class="pt">PRELIMINAR</span>':''}<span>Folio de análisis</span><b>${d.folio}</b><em>${d.emision}</em></div></header><div class="cuerpo"></div>
 <footer class="pie"><b>Consultoría e Investigación en Ciencias Químicas Nisa Nabani S.A.P.I. de C.V.</b><span>Ensayos acreditados por la Entidad Mexicana de Acreditación, A.C. · Acreditación A-0627-061/15 · NMX-EC-17025-IMNC-2018 · Aprobación DGN A-0627-061/15</span><span>Estos resultados no pueden ser reproducidos parcialmente, excepto en su totalidad, y avalan únicamente la muestra descrita.</span><span>Av. Fuerza Aérea Mexicana 607, Col. Reforma, 68050, Oaxaca de Juárez, Oax. · cac@nisanabani.com</span><span class="pg">Página <span class="pi"></span>&nbsp;de&nbsp;<span class="pn"></span><small>RP-06-21 · ${d.folio}</small></span></footer></article>`);
 return h;}
const lleno=c=>c.scrollHeight>c.clientHeight+0.5;
function render(k){
 const d=DOCS[k],cont=document.getElementById('hojas');cont.innerHTML='';
 let pag=hoja(d,true);cont.appendChild(pag);let cu=pag.querySelector('.cuerpo');
 const nueva=()=>{pag=hoja(d,false);cont.appendChild(pag);cu=pag.querySelector('.cuerpo');cu.appendChild(el(`<div class="cont-cli"><span><b>${d.cliente}</b></span><span>Continuación del informe ${d.folio}</span></div>`));};
 const poner=(nodo)=>{cu.appendChild(nodo);if(lleno(cu)){nodo.remove();nueva();cu.appendChild(nodo);}return nodo;};
 const kv=(t,arr)=>`<section class="kv"><h2>${t}</h2><dl>${arr.map(([a,b])=>`<dt>${a}</dt><dd>${b}</dd>`).join('')}</dl></section>`;
 poner(el(`<div class="cli"><div><span class="ov">Cliente</span><b>${d.cliente}</b><p>${d.dir}</p></div><div class="qr"><span>Verifica la autenticidad<br>de este informe</span><i>QR</i></div></div>`));
 poner(el(`<div class="dos">${kv('Datos de la muestra',d.muestra)}${kv('Datos de recepción',d.recepcion)}</div>`));
 poner(el(`<div class="sec"><h2>Resultados de ensayo</h2><span>${d.bloques.length} norma${d.bloques.length>1?'s':''} de referencia · cada bloque indica su norma, su propósito y sus límites</span></div>`));
 let n=0;const thead='<thead><tr><th>#</th><th>Ensayo · método</th><th>Resultado</th><th>Uexp</th><th>Límites mín – máx<br><span class="t2">intervalo de aceptación</span></th><th>Unidades</th><th>Fecha</th><th>Declaración</th></tr></thead>';
 d.bloques.forEach((b,i)=>{
  const cnt={ok:0,no:0,na:0};b.filas.forEach(r=>cnt[decl(r)]++);
  const resumen=[cnt.ok&&`${cnt.ok} cumplen`,cnt.no&&`${cnt.no} no cumple${cnt.no>1?'n':''}`,cnt.na&&`${cnt.na} no aplica${cnt.na>1?'n':''}`].filter(Boolean).join(' · ');
  const cab=(cont)=>el(`<section class="blq"><div class="bh"><span class="bn">${i+1}</span><div><b>${b.norma}${cont?' <i>(continuación)</i>':''}</b><span>${b.titulo}</span></div><span class="c">${b.filas.length} ensayo${b.filas.length===1?"":"s"} · ${resumen}</span><span class="uso">Para fines de ${b.uso}</span></div><table>${thead}<tbody></tbody></table></section>`);
  let blq=cab(false);cu.appendChild(blq);let tb=blq.querySelector('tbody');
  b.filas.forEach((r,j)=>{n++;const c=decl(r);const lim=rango(r.lo,r.hi);
   const acep=acepta(r);
   const tr=el(`<table><tbody><tr class="${c}"><td class="n">${n}</td><td><b>${r.n}${r.a?'':'<sup>◊</sup>'}</b><span>${r.m}</span></td><td class="v">${r.r}</td><td class="m">${r.u??'—'}</td><td class="m">${lim}${acep}</td><td class="u">${r.un}</td><td class="m">${r.f}</td><td><span class="dc ${c}">${IC[c]}${T[c]}</span></td></tr></tbody></table>`).querySelector('tr');
   tb.appendChild(tr);
   if(lleno(cu)){tr.remove();
    if(tb.children.length<2){blq.remove();nueva();blq=cab(j>0);cu.appendChild(blq);tb=blq.querySelector('tbody');if(j>0){}tb.appendChild(tr);}  // sin título huérfano
    else{pag.querySelector('.cuerpo').appendChild(el('<p class="sigue">Continúa en la página siguiente →</p>'));nueva();blq=cab(true);cu.appendChild(blq);tb=blq.querySelector('tbody');tb.appendChild(tr);}}
  });});
 const normas=d.bloques.map((b,i)=>`<b>${b.norma}</b> (${b.titulo}) para los ensayos del bloque ${i+1}`).join('; ');
 poner(el(`<section class="obs"><div><h3>Declaración de conformidad</h3><p>Procedimiento PP-01 y guía ILAC-G8:09/2019. Con límite: regla con zona de seguridad; «Cumple» si el resultado queda dentro del intervalo de aceptación (límites ajustados por Uexp, k = 2, 95 %). Sin límite: «No aplica».</p></div><div><h3>Abreviaturas</h3><p>N/A: no aplica · N/D: no detectable · N/I: no indica · A.A.: alcohol anhidro · &lt;X: menor que el límite de cuantificación · Uexp: incertidumbre expandida · ◊: ensayo no acreditado.</p></div><div><h3>Trazabilidad</h3><p>${d.trazabilidad}</p></div><div class="w"><h3>Descarga de responsabilidad</h3><p>${TIPO==='preliminar'?'<b>Informe preliminar:</b> no válido para fines de certificación; los resultados pueden cambiar en el informe oficial. ':''}Este informe es válido de acuerdo con: ${normas}. Los resultados corresponden únicamente a la muestra analizada, recibida en las condiciones especificadas.</p></div></section>`));
 poner(el(`<div class="firma"><div class="fi"><i></i><b>Q.F.B. Nombre del responsable</b><span>Director general</span></div><div class="sello">Nisa Nabani<br>laboratorio<br>acreditado</div><div class="fi"><i></i><b>Responsable técnico</b><span>Revisó</span></div></div>`));
 const hs=[...cont.querySelectorAll('.hoja')];hs.forEach((h,i)=>{h.querySelector('.pi').textContent=i+1;h.querySelector('.pn').textContent=hs.length;h.setAttribute('aria-label',`Página ${i+1} de ${hs.length}`);});
}
document.querySelectorAll('[data-doc]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('[data-doc]').forEach(x=>x.setAttribute('aria-pressed',x===b));DOC=b.dataset.doc;render(DOC);}));
document.querySelectorAll('[data-tipo]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('[data-tipo]').forEach(x=>x.setAttribute('aria-pressed',x===b));TIPO=b.dataset.tipo;render(DOC);}));
(document.fonts&&document.fonts.ready?document.fonts.ready:Promise.resolve()).then(()=>render('corto'));
</script>'''
html = html.replace('__DOCS__', json.dumps(DOCS, ensure_ascii=False)).replace('__LOGOA__', json.dumps(LOGO_A)).replace('__LOGO__', json.dumps(LOGO_B)).replace('__TEMAS__', json.dumps(TEMAS)).replace('__MARCA__', json.dumps(MARCA))
open(os.path.join(H, 'informe.html'), 'w').write(html); print('ok', len(AG))
