# Diálogos NisaLab · r02 · una dirección: encabezado con avatar de tono, superficies claras y sistema tipográfico. Uso: python3 gen.py → dialogos.html
# Todo valor sale de ../nabi-design-system/tokens.json (color, tipografía, radios, sombras). Datos de ejemplo.
import os, re, json
D = os.path.dirname(os.path.abspath(__file__))
TOK = json.load(open(os.path.join(D, '..', 'nabi-design-system', 'tokens.json')))
C = {t['name']: t['value'] for t in TOK['color']['tokens']}
V = [f"--{k}:{v}" for k, v in C.items()]
for g in ('spacing', 'radius', 'sizing', 'shadow', 'motion'): V += [f"--{t['name']}:{t['value']}" for t in TOK[g]['tokens']]
V += [f"--font-{k}:{v}" for k, v in TOK['type']['families'].items()]
TY = {s['name']: (g['family'], s) for g in TOK['type']['groups'] for s in g['styles']}
for n, (fam, s) in TY.items():
    V.append(f"--t-{n}:{s['fontWeight']} {s['fontSize']}/{s['lineHeight']} var(--font-{fam})")
ROOT = ':root{' + ';'.join(V) + ';color-scheme:light}'
L = '/root/.cache/fruti-uva/package/icons/'
def ico(n, s=18):
    inner = ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse|polygon)[^>]*/>', open(L + n + '.svg').read()))
    return f'<svg class="i" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{inner}</svg>'
exec(open(os.path.join(D, '..', 'nisalab-areas-color-r01', 'oklch.py')).read())
def c(a, b): return f'{cr(C[a], C[b]):.1f}:1'

# ---------- sistema tipográfico del diálogo (roles → estilos existentes del DS)
ROLES = [
 ('Contexto', 'overline', 'primary', 'Tipo de diálogo y código. Mayúsculas, +0.06 em. Ata el texto al color del avatar.', 'BITÁCORA · BIT-02-01'),
 ('Título', 'title-1', 'text', 'Lo que se hace o se decide. Una línea si cabe.', '% Alcohol por volumen'),
 ('Subtítulo', 'body', 'text-muted', 'Una frase de contexto: vigencia, norma, folio.', 'Vigente desde el 1 de octubre de 2021'),
 ('Sección', 'title-2', 'text', 'Agrupa campos dentro del cuerpo.', 'Lecturas'),
 ('Etiqueta', 'label', 'text', 'Nombre de cada campo.', 'Fecha de análisis'),
 ('Texto', 'body', 'text', 'Explicaciones y consecuencias.', 'El analista recibirá el motivo.'),
 ('Ayuda', 'caption', 'text-muted', 'Metadatos, límites, pistas.', 'Rango de referencia: 35–55'),
 ('Dato', 'valor', 'text', 'Valores medidos y códigos. Cifras de ancho fijo.', '40.12 % Alc. Vol.'),
 ('Resultado', 'valor-xl', 'text', 'El valor protagonista, uno por diálogo.', '40.11'),
 ('Botón', 'button', 'primary', 'Verbo + objeto.', 'Registrar lecturas'),
]
def fondo(col): return 'surface'
ROLES_H = ''.join(f'''<tr><td><b>{r}</b><small>{u}</small></td><td><span style="font:var(--t-{s});{'letter-spacing:.06em;text-transform:uppercase;' if s == 'overline' else ''}color:var(--{col})">{m}</span></td>
<td class="mono">{TY[s][1]['fontSize']} / {TY[s][1]['lineHeight']} · {TY[s][1]['fontWeight']}</td><td class="mono">{s}</td><td><span class="dot" style="background:var(--{col})"></span><span class="mono">{col}</span></td><td class="mono r">{c(col, 'surface')}</td></tr>''' for r, s, col, u, m in ROLES)

# ---------- piezas
TONOS = {'neutro': ('primary-soft', 'primary'), 'aviso': ('alerta-soft', 'alerta'), 'fuera': ('fuera-soft', 'fuera'), 'ok': ('conforme-soft', 'conforme')}
def header(tono, icono, ctx, titulo, sub, cerrar=True, hid=''):
    return (f'<header class="hd"><span class="av t-{tono}" data-n="1">{ico(icono, 24)}</span><div class="tx"><p class="ctx" data-n="2">{ctx}</p>'
            f'<h2 id="{hid}" data-n="3">{titulo}</h2><p class="sub" data-n="4">{sub}</p></div>'
            + (f'<button class="x" aria-label="Cerrar" data-n="5">{ico("x", 20)}</button>' if cerrar else '') + '</header>')
def campo(lbl, val, cls='', unit='', help_=''):
    u = f'<span class="u">{unit}</span>' if unit else ''
    return f'<div class="fld"><label>{lbl}</label><span class="in {cls}"><span>{val}</span>{u}</span>{f"<small>{help_}</small>" if help_ else ""}</div>'

TRABAJO = f'''<div class="dlg big" role="dialog" aria-labelledby="t1">{header('neutro', 'flask-conical', 'Bitácora · BIT-02-01 · Rev. 01', '% Alcohol por volumen', 'Vigente desde el 1 de octubre de 2021 · NOM-070-SCFI-2016', hid='t1')}
<div class="bd" data-n="6"><section class="sec"><div class="sh"><h3>Información general</h3></div><div class="g2">{campo('Fecha de análisis', '04/11/2026', 'mono')}<div class="fld"><label>Equipo</label><span class="dato">Densímetro digital Anton Paar <span class="mono mut">DD-01</span></span></div></div></section>
<section class="sec"><div class="sh"><h3>Lecturas</h3><small>3 corridas · temperatura en °C</small></div>
<div class="lect"><span class="n mono">1</span>{campo('<span class=vh>Alcohol 1</span>', '40.12', 'mono r', '% Alc. Vol.')}{campo('<span class=vh>Temperatura 1</span>', '20.1', 'mono r', '°C')}
<span class="n mono">2</span>{campo('<span class=vh>Alcohol 2</span>', '40.10', 'mono r', '% Alc. Vol.')}{campo('<span class=vh>Temperatura 2</span>', '20.0', 'mono r', '°C')}
<span class="n mono">3</span>{campo('<span class=vh>Alcohol 3</span>', '40.11', 'mono r', '% Alc. Vol.')}{campo('<span class=vh>Temperatura 3</span>', '20.1', 'mono r', '°C')}</div>
<div class="res"><div><small class="ov">Promedio</small><span class="vxl mono">40.11<small>% Alc. Vol.</small></span></div><div class="rep"><small class="ov">Repetibilidad</small><span class="mono dato">0.02</span><span class="st ok">{ico('circle-check', 14)}Conforme · criterio ±0.10</span></div></div></section></div>
<footer class="ft" data-n="7"><small>Al registrar, la bitácora pasa a visto bueno.</small><button class="btn s">Cerrar</button><button class="btn p">{ico('check', 16)}Registrar lecturas</button></footer></div>'''

def decision(tono, icono, ctx, titulo, sub, texto, extra, sec, prim, pcls, hid, anat=False):
    return f'''<div class="dlg small{' anat' if anat else ''}" role="alertdialog" aria-labelledby="{hid}">{header(tono, icono, ctx, titulo, sub, hid=hid)}
<div class="bd" data-n="6"><p class="txt">{texto}</p>{extra}</div><footer class="ft" data-n="7">{f'<button class="btn s">{sec}</button>' if sec else ''}<button class="btn {pcls}">{prim}</button></footer></div>'''
AVISO = decision('aviso', 'clock', 'Registro fuera de plazo', 'Justifica el registro tardío', 'BIT-02-01 · AG-2610-0147', 'La fecha de entrega venció el 3 de noviembre. La justificación queda en el historial de la bitácora.',
                 campo('Justificación <span class=opc>(obligatoria)</span>', 'Equipo en calibración del 1 al 3 de noviembre.', 'area', help_='Máximo 500 caracteres.'), 'Cancelar', 'Registrar con justificación', 'p', 'd-aviso')
RECHAZO = decision('fuera', 'circle-x', 'Rechazo', 'Rechazar la bitácora', 'BIT-02-01 · AG-2610-0147 · M. Ruiz', 'El analista recibirá el motivo y la bitácora volverá a captura. El rechazo queda registrado y no se deshace.',
                   campo('Motivo del rechazo <span class=opc>(obligatorio)</span>', 'La corrida 2 se capturó con la temperatura de la corrida 3.', 'area'), 'Cancelar', 'Rechazar bitácora', 'd', 'd-fuera')
EXITO = decision('ok', 'circle-check', 'Bitácora registrada', 'Lecturas registradas', 'BIT-02-01 · AG-2610-0147 · 4 nov 2026 12:40', 'La bitácora pasó a visto bueno. J. Orozco recibirá el aviso.',
                 f'<div class="res sm"><div><small class="ov">Promedio</small><span class="vxl mono">40.11<small>% Alc. Vol.</small></span></div><span class="st ok">{ico("circle-check", 14)}Conforme</span></div>', 'Ver historial', 'Listo', 'p', 'd-ok')
ANAT = decision('neutro', 'send', 'Visto bueno', 'Enviar a visto bueno', 'BIT-02-01 · AG-2610-0147', 'J. Orozco recibirá la bitácora para revisarla. Mientras tanto no podrás editarla.', '', 'Cancelar', 'Enviar a visto bueno', 'p', 'd-anat', anat=True)
LEYENDA = [('Avatar', '48 × 48, radio 12, fondo suave del tono e ícono de 24 en el color del tono. Neutro azul, aviso ámbar, destructivo rojo, éxito verde.'),
           ('Contexto', 'overline 11/16 · 600 · mayúsculas · azul. Dice qué tipo de diálogo es y el código.'),
           ('Título', 'title-1 22/30 · 600 · tinta. Alineado al borde superior del avatar más la línea de contexto.'),
           ('Subtítulo', 'body 14/22 · 400 · gris de texto. Una frase; datos en Google Sans Code si son códigos.'),
           ('Cerrar', '40 × 40, sin fondo; gris de texto. Esc también cierra. En diálogos destructivos sí aparece.'),
           ('Cuerpo', 'Blanco, márgenes de 24. Su borde izquierdo coincide con el del avatar.'),
           ('Pie', 'Blanco con filete superior. Ayuda a la izquierda; secundaria y una sola primaria a la derecha.')]
LEY_H = ''.join(f'<li><span><b>{a}.</b> {b}</span></li>' for a, b in LEYENDA)
MEDIDAS = [('Ancho', 'Trabajo 720 px · decisión 440 px · celular: hoja inferior a todo el ancho'), ('Márgenes', '24 px a los lados en encabezado, cuerpo y pie; 20 arriba y abajo del encabezado'),
           ('Separaciones', 'Avatar ↔ texto 16 · secciones 24 · campos 16 · etiqueta ↔ campo 6'), ('Superficies', f'Diálogo blanco; datos agrupados sobre el lienzo (bg); filetes «border» (decorativos)'),
           ('Sombra', 'shadow-overlay en el diálogo; shadow-inset en campos; shadow-primary en el botón principal'), ('Radios', 'Diálogo 12 · avatar 12 · campos 8 · botones 6')]
MED_H = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in MEDIDAS)

CSS = r'''
/* Página: especificación arriba (anatomía, tipografía, medidas) y los diálogos sobre su velo oscuro. Tema claro, como NisaLab. */
*{box-sizing:border-box}html,body{margin:0}[hidden]{display:none!important}
body{background:var(--bg);color:var(--text);font:var(--t-body)}
.i{flex:none}.mono{font-family:var(--font-datos);font-variant-numeric:tabular-nums}.mut{color:var(--text-muted)}.r{text-align:right}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.wrap{max-width:1240px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 56px;display:grid;gap:28px}
.pg h1{margin:0;font:var(--t-display);letter-spacing:-.01em}.pg p{margin:6px 0 0;color:var(--text-muted);max-width:80ch}
.blk{display:grid;gap:14px;min-width:0}.blk>h2{margin:0;font:var(--t-title-1)}.blk>p{margin:0;color:var(--text-muted);max-width:80ch}
.tw{overflow-x:auto;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);box-shadow:var(--shadow-1)}
table{border-collapse:collapse;width:100%;min-width:860px}th{font:var(--t-label);color:var(--text-muted);text-align:left;padding:10px 14px;background:var(--bg);white-space:nowrap}
td{padding:12px 14px;border-top:1px solid var(--border);vertical-align:middle;font-size:13px}td small{display:block;font:var(--t-caption);color:var(--text-muted);max-width:30ch}td.mono{font-size:12.5px;white-space:nowrap}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:-1px}
.anatl{display:grid;gap:20px;align-items:start}@media(min-width:960px){.anatl{grid-template-columns:440px minmax(0,1fr)}}
.ley{margin:0;padding:0;list-style:none;counter-reset:n;display:grid;gap:10px}.ley li{counter-increment:n;display:grid;grid-template-columns:24px 1fr;gap:10px;font-size:14px;line-height:21px}
.ley li::before{content:counter(n);width:22px;height:22px;border-radius:50%;background:var(--primary);color:var(--surface);font:600 12px/22px var(--font-sans);text-align:center}
.med{margin:0;display:grid;gap:0;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg)}.med div{display:grid;grid-template-columns:140px 1fr;gap:12px;padding:10px 16px;border-top:1px solid var(--border);font-size:14px}.med div:first-child{border-top:0}
.med dt{font:var(--t-label)}.med dd{margin:0;color:var(--text-muted)}
.velo{background:rgba(20,27,51,.55);border-radius:var(--radius-lg);padding:28px;display:grid;gap:24px;align-items:start}
@media(min-width:1100px){.velo.dos{grid-template-columns:720px minmax(0,1fr)}}
.col{display:grid;gap:24px;justify-items:start}
/* ===== diálogo */
.dlg{background:var(--surface);border-radius:var(--radius-lg);box-shadow:var(--shadow-overlay),0 0 0 1px rgba(20,27,51,.06);overflow:hidden;width:100%;position:relative}
.dlg.big{max-width:720px}.dlg.small{max-width:440px}
.hd{display:grid;grid-template-columns:48px minmax(0,1fr) auto;gap:16px;align-items:start;padding:20px 24px;border-bottom:1px solid var(--border)}
.av{width:48px;height:48px;border-radius:var(--radius-lg);display:grid;place-items:center}
.t-neutro{background:var(--primary-soft);color:var(--primary)}.t-aviso{background:var(--alerta-soft);color:var(--alerta)}.t-fuera{background:var(--fuera-soft);color:var(--fuera)}.t-ok{background:var(--conforme-soft);color:var(--conforme)}
.tx{min-width:0;display:grid}.ctx{margin:0;font:var(--t-overline);letter-spacing:.06em;text-transform:uppercase;color:var(--primary)}
.hd h2{margin:2px 0 0;font:var(--t-title-1);letter-spacing:-.005em;color:var(--text);text-wrap:balance}
.sub{margin:2px 0 0;font:var(--t-body);color:var(--text-muted)}
.x{width:40px;height:40px;margin:-6px -8px 0 0;display:grid;place-items:center;border:0;border-radius:var(--radius-sm);background:transparent;color:var(--text-muted);cursor:pointer}.x:hover{background:var(--bg);color:var(--text)}
:focus-visible{outline:2px solid var(--primary);outline-offset:2px}
.bd{padding:20px 24px 24px;display:grid;gap:24px}
.sec{display:grid;gap:12px}.sh{display:flex;justify-content:space-between;align-items:baseline;gap:12px}.sh h3{margin:0;font:var(--t-title-2)}.sh small{font:var(--t-caption);color:var(--text-muted)}
.g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.fld{display:grid;gap:6px;min-width:0}.fld label{font:var(--t-label)}.fld .opc{font-weight:400;color:var(--text-muted)}.fld small{font:var(--t-caption);color:var(--text-muted)}
.in{display:flex;align-items:center;gap:8px;min-height:40px;padding:0 12px;background:var(--surface);border:1px solid var(--border-control);border-radius:var(--radius-md);box-shadow:var(--shadow-inset);font:var(--t-body)}
.in.mono span:first-child{font:var(--t-valor)}.in.r span:first-child{flex:1;text-align:right}.in .u{font:var(--t-valor-sm);color:var(--text-muted);padding-left:8px;border-left:1px solid var(--border);align-self:stretch;display:flex;align-items:center}
.in.area{min-height:72px;align-items:flex-start;padding-top:9px}
.dato{font:var(--t-body);min-height:40px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}.dato.mono{font:var(--t-valor)}
.lect{display:grid;grid-template-columns:28px minmax(0,1fr) minmax(0,1fr);gap:8px 12px;align-items:center}.lect .fld{gap:0}
.n{width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:var(--bg);color:var(--text-muted);font:var(--t-valor-sm)}
.res{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:16px;padding:16px;background:var(--bg);border-radius:var(--radius-md)}
.res.sm{align-items:center}.ov{display:block;font:var(--t-overline);letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted)}
.vxl{font:var(--t-valor-xl);color:var(--text)}.vxl small{font:var(--t-valor-sm);color:var(--text-muted);margin-left:6px}
.rep{display:grid;gap:4px;justify-items:end}
.st{display:inline-flex;align-items:center;gap:6px;padding:3px 10px 3px 8px;border-radius:var(--radius-sm);font:500 13px/18px var(--font-sans)}.st.ok{background:var(--conforme-soft);color:var(--on-conforme-soft)}
.txt{margin:0;font:var(--t-body);max-width:60ch}
.ft{display:flex;flex-wrap:wrap;gap:8px;justify-content:flex-end;align-items:center;padding:16px 24px;border-top:1px solid var(--border)}.ft small{margin-right:auto;font:var(--t-caption);color:var(--text-muted)}
.btn{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:0 16px;border-radius:var(--radius-sm);font:var(--t-button);border:1px solid transparent;cursor:pointer}
.btn.p{background:var(--primary);color:var(--surface);box-shadow:var(--shadow-primary)}.btn.s{background:var(--surface);color:var(--primary);border-color:var(--border-control);box-shadow:var(--shadow-1)}.btn.d{background:var(--fuera);color:var(--surface)}
/* anatomía: números sobre las piezas */
.anat [data-n]{position:relative;outline:1px dashed var(--primary);outline-offset:2px}.anat .x[data-n]::after{right:auto;left:-10px}.anat .bd[data-n]::after,.anat .ft[data-n]::after{right:auto;left:8px;top:6px}
.anat [data-n]::after{content:attr(data-n);position:absolute;top:-10px;right:-10px;width:20px;height:20px;border-radius:50%;background:var(--primary);color:var(--surface);font:600 11px/20px var(--font-sans);text-align:center;z-index:2}
@media(max-width:640px){.velo{padding:12px}.g2{grid-template-columns:1fr}.hd{grid-template-columns:40px minmax(0,1fr) auto;gap:12px;padding:16px}.av{width:40px;height:40px}.bd{padding:16px}.ft{padding:12px 16px}.lect{grid-template-columns:24px minmax(0,1fr) minmax(0,1fr)}}
'''
out = f'''<title>Diálogos NisaLab</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Google+Sans+Code:wght@400;500;600&display=swap">
<style>{ROOT}{CSS}</style><script>document.documentElement.lang='es'</script>
<main class="wrap"><header class="pg"><h1>Diálogos NisaLab</h1><p>Ronda 2. Identidad por estructura: avatar con el color del tono, contexto, título y subtítulo; superficies blancas, sombra que separa capas y un sistema tipográfico con pesos y colores fijos. Todo sale del design system. Datos de ejemplo.</p></header>
<section class="blk" aria-labelledby="s-an"><h2 id="s-an">Anatomía del encabezado</h2><div class="anatl">{ANAT}<ol class="ley">{LEY_H}</ol></div></section>
<section class="blk" aria-labelledby="s-ty"><h2 id="s-ty">Sistema tipográfico</h2><p>Diez papeles, todos con estilos que ya existen en el sistema. El peso separa niveles (600 títulos, 500 etiquetas y datos, 400 texto); el color separa importancia (tinta para leer, gris para acompañar, azul para el contexto y la acción).</p>
<div class="tw"><table><thead><tr><th>Papel</th><th>Muestra</th><th>Tamaño · peso</th><th>Estilo</th><th>Color</th><th class="r">Sobre blanco</th></tr></thead><tbody>{ROLES_H}</tbody></table></div></section>
<section class="blk" aria-labelledby="s-me"><h2 id="s-me">Medidas y capas</h2><dl class="med">{MED_H}</dl></section>
<section class="blk" aria-labelledby="s-di"><h2 id="s-di">Los diálogos</h2><p>Un diálogo de trabajo y tres de decisión. El tono cambia el avatar y, si es destructivo, el botón; la estructura no cambia.</p>
<div class="velo dos">{TRABAJO}<div class="col">{AVISO}{RECHAZO}{EXITO}</div></div></section></main>'''
open(os.path.join(D, 'dialogos.html'), 'w').write(out)
print('ok', len(out) // 1024, 'KB')
