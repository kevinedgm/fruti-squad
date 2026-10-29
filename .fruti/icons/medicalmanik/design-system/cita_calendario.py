# CitaCalendario: cómo aparece una cita en los espacios del calendario (Expediente y Agenda).
# Lo importa build.py; escribe project/components/CitaCalendario/.
import json, os

LU = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lucide-cita.json')))
def li(n, cls='li'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{LU[n]}</svg>'

# estado: (clase, texto, sistema, icono, cuándo cambia)
EST = {
    'term': ('Terminada', 'exito', 'circle-check', 'El médico cerró la consulta.'),
    'conf': ('Confirmó', 'exito', 'calendar-check', 'El paciente respondió que sí al recordatorio, o la asistente lo marcó.'),
    'sala': ('En sala', 'info', 'armchair', 'La asistente registró su llegada.'),
    'sinr': ('Sin respuesta', 'info', 'clock', 'Se envió el recordatorio y aún no contesta.'),
    'noco': ('No confirmó', 'aviso', 'calendar-x', 'Pasó el plazo para confirmar sin respuesta.'),
    'canc': ('Cancelada', 'error', 'circle-x', 'La canceló el paciente o la clínica. El espacio queda libre.'),
}
ALERTA = ('Signos fuera de rango', 'error', 'triangle-alert', 'Se capturaron signos fuera del rango. Se suma al estado; no lo reemplaza.')
ROW = 24  # 15 min

def cita(k, ini, fin, pac, motivo, top, mins, alerta=False):
    txt, sis, icon, _ = EST[k]
    h = mins // 15 * ROW
    size = 's' if mins <= 15 else ('m' if mins <= 30 else 'l')
    label = f'{ini} a {fin}, {pac}, {motivo}. Estado: {txt}.' + (' Alerta: signos fuera de rango.' if alerta else '')
    al = f'<span class="al" title="Signos fuera de rango">{li("triangle-alert")}</span>' if alerta else ''
    if size == 's':
        inner = f'{li(icon)}<span class="h num">{ini}</span><span class="p">{pac}</span>'
    elif size == 'm':
        inner = f'<span class="p"><span class="h num">{ini}</span> {pac}</span><span class="e">{li(icon)}{txt}</span>'
    else:
        inner = f'<span class="h num">{ini} – {fin}</span><span class="p">{pac}</span><span class="mo">{motivo}</span><span class="e">{li(icon)}{txt}</span>'
    return (f'<button type="button" class="ci {size} k-{k}{" con-al" if alerta else ""}" style="top:{top * ROW // 15 + 1}px;height:{h - 3}px" '
            f'aria-label="{label}">{inner}{al}</button>')

DIA = [
    ('term', '8:00', '8:30', 'Ana Lucía Pérez', 'Control de presión', 0, 30, False),
    ('canc', '8:30', '8:45', 'Jorge Méndez', 'Receta', 30, 15, False),
    ('sala', '8:45', '9:15', 'Rosa Martínez', 'Revisión de glucosa', 45, 30, True),
    ('conf', '9:15', '9:30', 'Luis Hernández', 'Certificado médico', 75, 15, False),
    ('conf', '9:30', '10:30', 'Mariana Ruiz Ortega', 'Primera vez · dolor de cabeza', 90, 60, False),
    ('sinr', '10:30', '11:00', 'Pedro Sánchez', 'Seguimiento', 150, 30, False),
    ('noco', '11:00', '11:30', 'Elena Torres', 'Resultados de laboratorio', 180, 30, False),
]
HORAS = ['8:00', '9:00', '10:00', '11:00']
ALTO = 210 // 15 * ROW

CSS = '''body{padding:20px}.wrap{display:grid;grid-template-columns:minmax(0,380px) minmax(0,1fr);gap:28px;align-items:start}
.dh{display:flex;justify-content:space-between;align-items:baseline;margin:0 0 10px}.dh b{font:600 18px/24px var(--font-display,"Urbanist",sans-serif)}.dh span{font-size:14px;color:var(--muted,#4A5674)}
.dia{display:grid;grid-template-columns:48px 1fr}.gut{position:relative}.gut span{position:absolute;right:8px;transform:translateY(-8px);font:500 12px/16px var(--font-sans,sans-serif);color:var(--muted,#4A5674);font-variant-numeric:tabular-nums}
.col{position:relative;background:var(--surface,#fff);border:1px solid var(--line,#E1E6F0);border-radius:14px;background-image:repeating-linear-gradient(to bottom,transparent 0 23px,rgba(20,33,61,.06) 23px 24px)}
.ci{position:absolute;left:6px;right:6px;border-radius:10px;background:var(--surface,#fff);border:1px solid var(--line,#E1E6F0);border-left:4px solid var(--k);padding:3px 8px 3px 9px;display:grid;align-content:start;text-align:left;font:inherit;color:var(--ink,#14213D);overflow:hidden;cursor:pointer;box-shadow:var(--shadow-card,0 1px 2px rgba(20,33,61,.05))}
.ci:hover{box-shadow:var(--shadow-hover,0 8px 20px rgba(20,33,61,.08));z-index:2}.ci:focus-visible{outline:2px solid var(--focus,#234899);outline-offset:2px;z-index:2}
.ci .li{width:14px;height:14px;flex:none}.ci .h{font:600 12px/18px var(--font-sans,sans-serif);color:var(--muted,#4A5674)}
.ci .p{font:600 14px/20px var(--font-sans,sans-serif);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
.ci .mo{font:400 13px/18px var(--font-sans,sans-serif);color:var(--muted,#4A5674);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ci .e{display:flex;align-items:center;gap:4px;font:600 12px/18px var(--font-sans,sans-serif);color:var(--kt)}
.ci.s{border-radius:6px;grid-auto-flow:column;grid-template-columns:auto auto minmax(0,1fr);align-items:center;gap:6px;padding-block:0}.ci.s .li{color:var(--kt)}
.ci.con-al{padding-right:30px}.ci .al{position:absolute;top:2px;right:4px;width:20px;height:20px;border-radius:50%;background:var(--error-soft,#F9ECED);color:var(--error,#C33F4E);display:grid;place-items:center}.ci .al .li{width:13px;height:13px}
.k-term{--k:var(--exito,#15814B);--kt:var(--on-exito-soft,#157C4A);box-shadow:none}.k-term .p{color:var(--muted,#4A5674);font-weight:500}
.k-conf{--k:var(--exito,#15814B);--kt:var(--on-exito-soft,#157C4A)}
.k-sala{--k:var(--info,#3F7695);--kt:var(--on-info-soft,#3D7291);background:var(--info-soft,#ECF1F4)}
.k-sinr{--k:var(--info,#3F7695);--kt:var(--on-info-soft,#3D7291)}
.k-noco{--k:var(--aviso,#A75F00);--kt:var(--on-aviso-soft,#A05C03)}
.k-canc{--k:var(--error,#C33F4E);--kt:var(--on-error-soft,#BA3D4D);right:50%;background:var(--error-soft,#F9ECED);border-style:dashed;border-left-style:solid;box-shadow:none}.k-canc .p{text-decoration:line-through;color:var(--muted,#4A5674);font-weight:500}
.lg{display:grid;gap:14px}.lg table{border-collapse:collapse;width:100%;font-size:14px;line-height:20px}.lg th,.lg td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line,#E1E6F0);vertical-align:top}.lg th{font-weight:600;color:var(--muted,#4A5674);background:var(--surface-soft,#EEF1F7)}
.chip{display:inline-flex;align-items:center;gap:6px;font-weight:600;white-space:nowrap}.chip .li{width:16px;height:16px}.sis{font-family:ui-monospace,monospace;font-size:13px;color:var(--muted,#4A5674);white-space:nowrap}
.tm{display:flex;gap:12px;align-items:flex-start;flex-wrap:wrap}.tm .ci{position:relative;left:auto;right:auto;width:180px}.tm figure{margin:0;display:grid;gap:4px}.tm figcaption{font-size:12px;color:var(--muted,#4A5674)}
@media (max-width:760px){.wrap{grid-template-columns:1fr}}'''

def build(P, page_head):
    gut = ''.join(f'<span style="top:{i * 4 * ROW}px">{hh}</span>' for i, hh in enumerate(HORAS))
    col = ''.join(cita(*c) for c in DIA)
    rows = ''.join(f'<tr><td><span class="chip" style="color:var(--{"on-" + s + "-soft"})">{li(i)}{t}</span></td><td class="sis">{s}</td><td class="sis">{i}</td><td>{w}</td></tr>' for t, s, i, w in EST.values())
    t, s, i, w = ALERTA
    rows += f'<tr><td><span class="chip" style="color:var(--error)">{li(i)}{t}</span><br><small style="color:var(--muted)">alerta clínica</small></td><td class="sis">{s}</td><td class="sis">{i}</td><td>{w}</td></tr>'
    tam = (f'<figure>{cita("conf", "9:15", "9:30", "Luis Hernández", "Certificado médico", 0, 15).replace("style=", "data-s=")}<figcaption>15 min: icono, hora y paciente</figcaption></figure>'
           f'<figure style="height:auto">{cita("conf", "9:15", "9:45", "Luis Hernández", "Certificado médico", 0, 30).replace("style=", "data-s=")}<figcaption>30 min: + estado en texto</figcaption></figure>'
           f'<figure>{cita("conf", "9:15", "10:15", "Luis Hernández", "Certificado médico", 0, 60).replace("style=", "data-s=")}<figcaption>60 min: + horario y motivo</figcaption></figure>')
    tam = tam.replace('class="ci s ', 'style="height:21px" class="ci s ').replace('class="ci m ', 'style="height:45px" class="ci m ').replace('class="ci l ', 'style="height:93px" class="ci l ')
    body = (f'<div class="wrap"><div><div class="dh"><b>Martes 28</b><span>Dra. Ramírez · Consultorio 2</span></div>'
            f'<div class="dia"><div class="gut" aria-hidden="true">{gut}</div><div class="col" style="height:{ALTO}px">{col}</div></div></div>'
            f'<div class="lg"><table><thead><tr><th>Estado de la cita</th><th>Sistema</th><th>Lucide</th><th>Cuándo cambia</th></tr></thead><tbody>{rows}</tbody></table>'
            f'<div><p style="margin:0 0 8px;font-weight:600">Según la duración</p><div class="tm">{tam}</div></div></div></div>')
    os.makedirs(f'{P}/components/CitaCalendario', exist_ok=True)
    html = page_head('Datos', 720, body, CSS).replace('height=720 -->', 'height=720 width=1040 -->', 1)
    open(f'{P}/components/CitaCalendario/preview.html', 'w').write(html)
    open(f'{P}/components/CitaCalendario/README.md', 'w').write('''# CitaCalendario

Cómo aparece una cita en los espacios del calendario de Expediente y de Agenda.

- **Anatomía:** tarjeta blanca dentro del espacio, con una barra izquierda de 4 px en el color del estado (`exito`, `info`, `aviso` o `error`). El estado siempre lleva icono de Lucide y, si cabe, texto: nunca solo color.
- **Según la duración** (15 min = 24 px): 15 min muestra icono del estado, hora y paciente en una línea; 30 min agrega el estado en texto; 60 min o más agrega horario completo y motivo.
- **Estados** (uno a la vez): Terminada (`exito`, circle-check, sin sombra y nombre en «muted»: ya pasó), Confirmó (`exito`, calendar-check), En sala (`info`, armchair, fondo `info-soft` para que se note quién espera), Sin respuesta (`info`, clock), No confirmó (`aviso`, calendar-x), Cancelada (`error`, circle-x).
- **Cancelada** ocupa solo la mitad izquierda del espacio, con borde punteado y el nombre tachado: el resto del espacio se puede volver a agendar.
- **Signos fuera de rango** es una alerta clínica, no un estado: un círculo `error-soft` con triangle-alert en la esquina superior derecha. Se suma al estado (por ejemplo, En sala + alerta) y no cambia la barra.
- **Accesibilidad:** cada cita es un botón con `aria-label` completo («8:45 a 9:15, Rosa Martínez, Revisión de glucosa. Estado: En sala. Alerta: signos fuera de rango.»). En 15 min el texto del estado no cabe; está en el `aria-label` y en el detalle al abrir la cita.
- **Pendiente de definir:** el plazo de «No confirmó», el estado de una cita recién creada antes del recordatorio, y si «En consulta» y «No asistió» siguen existiendo.
- El consumidor provee: hora de inicio y fin, paciente, motivo, estado y alertas.
''')
