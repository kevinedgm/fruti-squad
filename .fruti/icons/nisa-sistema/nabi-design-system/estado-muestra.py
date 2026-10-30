# NisaLab · EstadoMuestra se reemplaza por el esquema aprobado en nisalab-estatus-r3:
# proceso (pastilla rellena, colores semánticos del laboratorio), pago (etiqueta con contorno + moneda) y urgente (ficha pera + rayo).
# Uso: python3 estado-muestra.py <project>   (después de areas-sin-color.py)
import json, os, sys
P = sys.argv[1]
def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)
PROC = [('no-ingresada', 'No ingresada', '#FEF3C7', '#713F12', 'Recibida en ventanilla, sin folio interno. Acción: ingresarla.'),
        ('en-proceso', 'En proceso', '#E0F2FE', '#075985', 'Con folio interno de laboratorio. Acción: capturar parámetros.'),
        ('generando-informe', 'Generando informe', '#EDE9FE', '#5B21B6', 'Parámetros requeridos capturados. Acción: generar el informe.'),
        ('terminada', 'Terminada', '#DCFCE7', '#166534', 'Informe generado y enviado.'),
        ('cancelada', 'Cancelada', '#FEE2E2', '#991B1B', 'Muestra cancelada, sola o con toda su orden. Etapa final.')]
PAGO = [('no-pagada', 'No pagada', '#B42318', 'Sin pagos registrados.'), ('parcial', 'Pago parcial', '#B54708', 'Pagó una parte; queda saldo.'),
        ('pagada', 'Pagada', '#166534', 'Saldo en cero.'), ('cortesia', 'Cortesía', '#052A76', 'Se procesa sin cobro, por decisión del laboratorio.')]
# ---------- tokens ----------
t = json.load(open(f'{P}/tokens.json')); toks = t['color']['tokens']
toks[:] = [c for c in toks if not c['name'].startswith(('muestra-', 'on-muestra-', 'pago-'))]
for k, n, bg, tx, u in PROC:
    toks.append({'name': f'muestra-{k}', 'value': bg, 'usage': f'Fondo de la pastilla de proceso «{n}». {u} Color semántico del laboratorio: el personal lo asocia a esta acción.'})
    toks.append({'name': f'on-muestra-{k}', 'value': tx, 'usage': f'Texto e ícono de «{n}» sobre `muestra-{k}`: {cr(tx, bg)}:1.'})
for k, n, c, u in PAGO:
    toks.append({'name': f'pago-{k}', 'value': c, 'usage': f'Texto, ícono y contorno de la etiqueta de pago «{n}» sobre blanco: {cr(c, "#FFFFFF")}:1. {u}'})
for c in toks:
    if c['name'] == 'pera':
        c['usage'] = 'La célula que creció del símbolo Colonia, lo que está en curso (el registro que se edita) y la marca Urgente (ficha pera con rayo y franja de fila). Nunca texto (1.7:1 sobre blanco); encima va `on-pera`.'
json.dump(t, open(f'{P}/tokens.json', 'w'), ensure_ascii=False, indent=1)
# ---------- preview ----------
def etapa(n):
    b = '<svg class="ico" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    if n == 0: return b + '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75" stroke-dasharray="2.6 2.1"/></svg>'
    if n == 3: return b + '<circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M4.8 8.2 7 10.4 11.2 5.9" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    arc = 'M8 8 V2.5 A5.5 5.5 0 0 1 8 13.5 Z' if n == 1 else 'M8 8 V2.5 A5.5 5.5 0 1 1 2.5 8 Z'
    return b + f'<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75"/><path d="{arc}" fill="currentColor"/></svg>'
BAN = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="10"/><path d="m4.9 4.9 14.2 14.2"/></svg>'
GIFT = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5A4.8 8 0 0 1 12 8a4.8 8 0 0 1 4.5-5 2.5 2.5 0 0 1 0 5"/></svg>'
ZAP = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/></svg>'
def moneda(n):
    b = '<svg class="ico" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'; s = '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.75"/>'
    if n == 1: return b + s + '<path d="M8 1.5 A6.5 6.5 0 0 0 8 14.5 Z" fill="currentColor"/></svg>'
    if n == 2: s = '<circle cx="8" cy="8" r="7.5" fill="currentColor"/>'
    return b + s + f'<path d="M10 5.6 H7.1 a1.3 1.3 0 0 0 0 2.6 h1.8 a1.3 1.3 0 0 1 0 2.6 H6 M8 4.2 v7.6" fill="none" stroke="{"#fff" if n == 2 else "currentColor"}" stroke-width="1.3" stroke-linecap="round"/></svg>'
IP = [etapa(0), etapa(1), etapa(2), etapa(3), BAN]; IG = [moneda(0), moneda(1), moneda(2), GIFT]
proc = ''.join(f'<span class="ps" style="background:var(--muestra-{k},{bg});color:var(--on-muestra-{k},{tx})">{IP[i]}{n}</span>' for i, (k, n, bg, tx, _) in enumerate(PROC))
pago = ''.join(f'<span class="et" style="color:var(--pago-{k},{c})">{IG[i]}{n}</span>' for i, (k, n, c, _) in enumerate(PAGO))
urg = f'<span class="ur">{ZAP}Urgente</span>'
h = ('<!-- @dsCard group="Feedback" height=180 width=900 -->\n'
     '<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap"><style>\n'
     'html,body{margin:0}body{background:var(--surface,#fff);color:var(--text,#141B33);font:15px/22px var(--font-sans,"Poppins",sans-serif);padding:var(--space-5,20px)}\n'
     '.g{display:grid;grid-template-columns:120px 1fr;gap:14px 16px;align-items:center}.lb{font:600 11px/14px var(--font-sans,"Poppins",sans-serif);letter-spacing:.06em;text-transform:uppercase;color:var(--text-subtle,#646B80)}\n'
     '.f{display:flex;flex-wrap:wrap;gap:8px;align-items:center}.ico{width:14px;height:14px;display:block;flex:none}\n'
     '.ps,.et,.ur{display:inline-flex;align-items:center;gap:6px;font:500 13px/18px var(--font-sans,"Poppins",sans-serif);white-space:nowrap}\n'
     '.ps{border-radius:var(--radius-pill,999px);padding:3px 10px 3px 7px}\n'
     '.et{border:1.5px solid currentColor;border-radius:var(--radius-sm,6px);padding:2px 8px 2px 6px;background:var(--surface,#fff)}\n'
     '.ur{font-weight:600;border-radius:var(--radius-sm,6px);padding:3px 8px 3px 6px;background:var(--pera,#C2D225);color:var(--on-pera,#052A76)}\n'
     '.nota{grid-column:1/-1;font-size:13px;line-height:18px;color:var(--text-muted,#535B70);margin:4px 0 0}\n'
     '@media (max-width:640px){.g{grid-template-columns:1fr;gap:6px}}\n'
     f'</style></head><body><div class="g"><span class="lb">Proceso</span><div class="f">{proc}</div><span class="lb">Pago</span><div class="f">{pago}</div>'
     f'<span class="lb">Prioridad</span><div class="f">{urg}</div><p class="nota">Pastilla rellena = proceso · etiqueta con contorno = pago · ficha pera = urgente. Siempre ícono + palabra.</p></div></body></html>\n')
open(f'{P}/components/EstadoMuestra/preview.html', 'w').write(h)
filas_p = '\n'.join(f'| {n} | `muestra-{k}` / `on-muestra-{k}` | {u} |' for k, n, bg, tx, u in PROC)
filas_g = '\n'.join(f'| {n} | `pago-{k}` | {u} |' for k, n, c, u in PAGO)
open(f'{P}/components/EstadoMuestra/README.md', 'w').write(f'''# EstadoMuestra

Los tres datos de estado de una muestra, que cambian por separado. El personal de recepción se guía por el color: cada color de proceso ya está asociado a una acción, por eso se respeta. Lo que separa los grupos es la forma.

## Proceso · pastilla rellena
El círculo se llena por etapa (punteado, mitad, tres cuartos, lleno con palomita) como apoyo cuando no se distingue el color.

| Estado | Tokens | Cuándo |
|---|---|---|
{filas_p}

Cancelada aplica a una muestra o a toda la orden de análisis. Si se cancela la orden, la orden y todas sus muestras llevan Cancelada; si se cancela una muestra, la orden dice «1 de N muestras cancelada» y sigue su curso. En la lista, el folio de una muestra cancelada va tachado y su pago se apaga a gris.

## Pago · etiqueta con contorno
Sin relleno; la moneda se llena (vacía, media, llena). Cortesía lleva regalo.

| Estado | Token | Cuándo |
|---|---|---|
{filas_g}

## Prioridad · Urgente
Ficha `pera` con rayo junto al folio y franja `pera` de 4 px a la izquierda de la fila. No usa rojo (ya es Cancelada y No pagada). Texto `on-pera` 7.8:1.

## Reglas
1. Proceso, pago y urgencia nunca comparten forma: pastilla rellena, etiqueta con contorno, ficha sólida.
2. Un color de estado significa la misma acción en toda la aplicación.
3. Siempre ícono + palabra; el color nunca es la única señal.
4. Los colores de área (`area-*`) nunca aparecen en tablas.
5. El consumidor provee: estado de proceso, estado de pago, si es urgente y, si aplica, quién y cuándo cambió el estado.

## Incógnitas
- ¿Una orden cancelada se puede reabrir?
- ¿Qué pasa con lo ya pagado de una muestra cancelada?
''')
def rep(rel, a, b):
    f = os.path.join(P, rel); s = open(f).read()
    if a in s: open(f, 'w').write(s.replace(a, b))
    elif b not in s: print('NO ENCONTRADO', rel, a[:60])
rep('README.md', '- Los nombres de estado de muestra (Recibida, En análisis, En revisión, Liberada, Rechazada) son una propuesta: confirmar con el flujo real del laboratorio.',
    '- Estados de muestra (componente «EstadoMuestra»): proceso No ingresada, En proceso, Generando informe, Terminada y Cancelada (tokens `muestra-*`); pago No pagada, Pago parcial, Pagada y Cortesía (tokens `pago-*`); y la marca Urgente en `pera`. Son los colores con los que ya trabaja el laboratorio.')
rep('modulos.md', '| Está bien | `conforme-soft` / `on-conforme-soft` | Activo · Conforme · Liberada |', '| Está bien | `conforme-soft` / `on-conforme-soft` | Activo · Conforme |')
rep('modulos.md', '| Pendiente | `pendiente-soft` / `on-pendiente-soft` | Invitación enviada · En análisis |', '| Pendiente | `pendiente-soft` / `on-pendiente-soft` | Invitación enviada |')
rep('modulos.md', '| Requiere atención | `alerta-soft` / `on-alerta-soft` | Suspendido · En revisión |', '| Requiere atención | `alerta-soft` / `on-alerta-soft` | Suspendido |')
rep('modulos.md', '| Impedido | `fuera-soft` / `on-fuera-soft` | Bloqueado · Fuera · Rechazada |', '| Impedido | `fuera-soft` / `on-fuera-soft` | Bloqueado · Fuera de límite |')
rep('modulos.md', 'Dado de baja · Recibida |', 'Dado de baja |')
rep('modulos.md', 'Siempre icono + palabra. El pera no es un estado,', 'Los estados de la muestra (proceso, pago, urgente) tienen sus propios tokens y viven en «EstadoMuestra».\n\nSiempre icono + palabra. El pera no es un estado (Urgente es una marca de prioridad),')
print('ok')
