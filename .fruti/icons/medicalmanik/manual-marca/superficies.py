# Sección «Superficies e interfaz» del manual MedicalManik (pedido 2026-11-05: superficies, acentos, semánticos y bordes
# de botones e inputs para todo el ecosistema, dentro del manual).
# Los valores NO se escriben aquí: se leen de los tokens de cada sistema de diseño, para que el manual no pueda
# contradecirlos. Manik IA no tiene tokens.json: sus valores vienen de su manual (../manik-ia/manual.html, :root).
import json, os, re
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')

def tokens(rel):
    t = json.load(open(os.path.join(M, rel)))
    out = {}
    for g in ('color', 'radius', 'shadow', 'layout'):
        for x in t[g]['tokens']: out[x['name']] = x['value']
    for k, v in out.items():  # alias {otro}
        if isinstance(v, str) and v.startswith('{'): out[k] = out[v.strip('{}')]
    return out

E = tokens('design-system/project/tokens.json')      # Ecosistema Manik (apps)
R = tokens('directorio-ds/project/tokens.json')      # Directorio Manik
ia_css = open(os.path.join(M, 'manik-ia/manual.html')).read()
I = {k: v for k, v in re.findall(r'--(ia(?:-[a-z]+)?):(#[0-9A-Fa-f]{6})', ia_css)}

def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + .05) / (lb + .05)
f = lambda a, b: f'{cr(a, b):.2f}'.rstrip('0').rstrip('.')

def c(fam, name, nota=''):
    v = fam[name]
    return f'<span class="dot" style="background:{v}"></span><span class="mono">{v}</span> <span class="sf-tok">{name}</span>' + (f'<br><span class="nota">{nota}</span>' if nota else '')
NO = '<span class="sf-falta">No definido</span>'
HER = '<span class="nota">Hereda de las apps</span>'

def fila(rol, apps, dirc, ia):
    return f'<tr><td>{rol}</td><td>{apps}</td><td>{dirc}</td><td>{ia}</td></tr>'

def grupo(t): return f'<tr class="sf-g"><th colspan="4" scope="colgroup">{t}</th></tr>'

tabla = ''.join([
    grupo('Superficies'),
    fila('Fondo de página', c(E, 'canvas'), c(R, 'bruma'), HER),
    fila('Fondo de marca<br><span class="nota">portada, inicio de sesión, inicio</span>', c(E, 'bruma'), c(R, 'bruma'), '—'),
    fila('Superficie<br><span class="nota">tarjetas, tablas, barras, diálogos</span>', c(E, 'surface'), c(R, 'blanco'), HER),
    fila('Agrupación<br><span class="nota">encabezado de tabla, zona agrupada, solo lectura</span>', c(E, 'surface-soft'), c(R, 'lavado'), HER),
    fila('Presionado neutro', c(E, 'surface-pressed'), NO, HER),
    fila('Luz de marca<br><span class="nota">halos de fondo, círculo de icono</span>', c(E, 'luz-cian') + '<br>' + c(E, 'luz-calida'), c(R, 'luz-cian') + '<br>' + c(R, 'luz-calida'), '—'),
    grupo('Texto'),
    fila('Principal', c(E, 'ink', f'{f(E["ink"], E["surface"])}:1 sobre superficie'), c(R, 'tinta', f'{f(R["tinta"], R["blanco"])}:1'), HER),
    fila('Secundario', c(E, 'muted', f'{f(E["muted"], E["surface"])}:1'), c(R, 'muted', f'{f(R["muted"], R["blanco"])}:1'), HER),
    grupo('Bordes'),
    fila('Decorativo<br><span class="nota">tarjeta, divisor; nunca el único borde de un control</span>', c(E, 'line', f'{f(E["line"], E["surface"])}:1'), c(R, 'linea', f'{f(R["linea"], R["blanco"])}:1'), HER),
    fila('De control<br><span class="nota">campo, botón secundario; mínimo 3:1</span>', c(E, 'line-control', f'{f(E["line-control"], E["surface"])}:1 sobre superficie'), c(R, 'linea-control', f'{f(R["linea-control"], R["blanco"])}:1 sobre blanco'), HER),
    fila('Foco', c(E, 'focus', 'anillo de 2 px, 2 px de separación'), c(R, 'focus', 'anillo de 3 px, 2 px de separación'), HER),
    grupo('Acentos'),
    fila('Acción principal<br><span class="nota">un botón por vista</span>', c(E, 'manik', f'blanco encima {f("#FFFFFF", E["manik"])}:1'), c(R, 'cian-ui', f'blanco encima {f("#FFFFFF", R["cian-ui"])}:1'), c(I, 'ia', f'solo botones de IA · blanco {f("#FFFFFF", I["ia"])}:1')),
    fila('Hover y presionado', c(E, 'manik-hover'), c(R, 'cian-ui-hover'), c(I, 'ia-hover')),
    fila('Selección suave<br><span class="nota">activo, filtro, chip</span>', c(E, 'manik-soft', f'texto manik {f(E["manik"], E["manik-soft"])}:1'), '<span class="nota">Chip activo en</span> ' + c(R, 'tinta'), c(I, 'ia-suave', f'texto ia {f(I["ia"], I["ia-suave"])}:1')),
    fila('Acento gráfico<br><span class="nota">iconos y detalles; nunca texto pequeño ni botón</span>', c(E, 'cian', f'{f(E["cian"], "#FFFFFF")}:1 con blanco'), c(R, 'cian'), c(I, 'ia-destello')),
    fila('Identidad de producto<br><span class="nota">sello, tarjeta y app activa; nunca botón ni estado</span>', '<span class="nota">Siete colores <span class="mono">app-*</span> (ver Paleta)</span>', '—', '—'),
    grupo('Semánticos · siempre con icono y texto'),
])
for k, n in (('exito', 'Éxito'), ('aviso', 'Aviso'), ('error', 'Error'), ('info', 'Información')):
    apps = c(E, k, f'{f(E[k], E["surface"])}:1') + '<br>' + c(E, k + '-soft') + '<br>' + c(E, 'on-' + k + '-soft', f'{f(E["on-" + k + "-soft"], E[k + "-soft"])}:1 sobre su fondo')
    if k == 'exito':
        dirc = c(R, 'exito', f'{f(R["exito"], R["blanco"])}:1') + '<br>' + c(R, 'exito-suave') + '<br>' + c(R, 'on-exito-suave', f'{f(R["on-exito-suave"], R["exito-suave"])}:1')
    else:
        dirc = NO
    tabla += fila(n, apps, dirc, HER)
tabla += grupo('Forma')
tabla += fila('Botón y campo', f'Radio {E["radius-md"]} · alto {E["control-height"]}', f'Píldora · alto {R["boton-height"]} (Agendar), {R["control-height"]} (chips)', 'Píldora · alto 44px')
tabla += fila('Tarjeta', f'Radio {E["radius-2xl"]}; sin sombra o <span class="mono">shadow-card</span>', f'Radio {R["radius-ficha"]} (24px en celular)', HER)
tabla += fila('Lo que flota', '<span class="mono">shadow-pop</span>: menús, selector, diálogos', '<span class="mono">shadow-buscador</span>, <span class="mono">shadow-flotante</span>', HER)

# Muestras vivas: se pintan con los tokens leídos, no con valores escritos a mano.
def btn(bg, fg, txt, borde='transparent', rad='14px', h='44px'):
    return f'<span class="sf-btn" style="background:{bg};color:{fg};border-color:{borde};border-radius:{rad};min-height:{h}">{txt}</span>'
def campo(lbl, val, borde, fondo, msg='', ancho='1px', anillo=''):
    ring = f';box-shadow:0 0 0 2px {fondo},0 0 0 4px {anillo}' if anillo else ''
    return (f'<div class="sf-campo"><span class="sf-lbl">{lbl}</span><span class="sf-in" style="border:{ancho} solid {borde};background:{fondo}{ring}">{val}</span>'
            + (f'<span class="sf-msg" style="color:{E["error"]}"><b aria-hidden="true">⚠</b> {msg}</span>' if msg else '') + '</div>')
def estado(k):
    n = {'exito': 'Guardado', 'aviso': 'Vence en 3 días', 'error': 'Alergia: penicilina', 'info': 'En proceso'}[k]
    ic = {'exito': '✓', 'aviso': '!', 'error': '×', 'info': 'i'}[k]
    return f'<span class="sf-est" style="background:{E[k + "-soft"]};color:{E["on-" + k + "-soft"]}"><b aria-hidden="true">{ic}</b>{n}</span>'

apps = (f'<div class="sf-lienzo" style="background:{E["canvas"]}"><p class="sf-cap">Apps del ecosistema · fondo <span class="mono">canvas</span></p>'
        f'<div class="sf-hoja" style="background:{E["surface"]};border-color:{E["line"]};border-radius:{E["radius-2xl"]}">'
        '<div class="sf-fila">' + btn(E['manik'], E['on-manik'], 'Guardar consulta') + btn(E['surface'], E['manik'], 'Vista previa', E['line-control'])
        + btn('transparent', E['manik'], 'Cancelar') + btn(E['surface'], E['error'], 'Eliminar receta', E['error']) + '</div>'
        '<div class="sf-campos">' + campo('Peso', '72.5 <i>kg</i>', E['line-control'], E['surface'])
        + campo('Glucosa en ayuno', '98 <i>mg/dL</i>', E['manik'], E['surface'], anillo=E['focus'])
        + campo('Dosis diaria', '140 <i>mg</i>', E['error'], E['surface'], 'Máximo 100 mg al día', '2px')
        + campo('Folio', 'EXP-0000-0001', E['line'], E['surface-soft']) + '</div>'
        '<div class="sf-fila">' + ''.join(estado(k) for k in ('exito', 'aviso', 'error', 'info')) + '</div></div></div>')
dirm = (f'<div class="sf-lienzo" style="background:{R["bruma"]}"><p class="sf-cap">Directorio · fondo <span class="mono">bruma</span></p>'
        f'<div class="sf-hoja" style="background:{R["blanco"]};border-color:{R["linea"]};border-radius:{R["radius-ficha"]}">'
        '<div class="sf-fila">' + btn(R['cian-ui'], '#FFFFFF', 'Agendar', rad='999px', h=R['boton-height'])
        + btn(R['blanco'], R['tinta'], 'Copiar número', R['linea-control'], '999px', R['control-height'])
        + btn(R['tinta'], '#FFFFFF', 'Buscar', rad='999px', h=R['control-height']) + '</div>'
        f'<div class="sf-fila"><span class="sf-est" style="background:{R["exito-suave"]};color:{R["on-exito-suave"]}"><b aria-hidden="true">✓</b>Cédula verificada</span>'
        f'<span class="sf-est" style="background:{R["bruma"]};color:{R["tinta"]};border:1px solid {R["linea"]}">1.8 km</span></div></div></div>')
iam = (f'<div class="sf-lienzo" style="background:{E["canvas"]}"><p class="sf-cap">Manik IA · dentro de Expediente</p>'
       f'<div class="sf-hoja" style="background:{E["surface"]};border-color:{E["line"]};border-radius:{E["radius-2xl"]}"><div class="sf-fila">'
       + btn(I['ia'], '#FFFFFF', f'<b style="color:{I["ia-destello"]}" aria-hidden="true">✦</b> Sugerir con IA', rad='999px')
       + f'<span class="sf-est" style="background:{I["ia-suave"]};color:{I["ia"]}"><b aria-hidden="true">✦</b>Sugerido por IA</span></div></div></div>')

HTML = f'''<section id="superficies" aria-labelledby="h4s"><div class="cab"><span class="eti">Interfaz</span><h2 id="h4s">Superficies e interfaz</h2></div>
 <p class="texto">Cómo se construye cualquier pantalla de la marca, en cuatro capas: <b>superficies</b> (de qué está hecho el fondo), <b>acentos</b> (qué se toca y de quién es), <b>semánticos</b> (qué pasó) y <b>bordes</b> (qué separa y qué es un control). Cada familia tiene su paleta, pero las capas y sus reglas son las mismas.</p>
 <div class="sf-muestras">{apps}{dirm}{iam}</div>
 <ol class="reglas">
  <li><b>Tres niveles de superficie, no más:</b> fondo de página → superficie → agrupación. La sombra es solo para lo que flota (menú, selector, diálogo, buscador).</li>
  <li><b>Una acción principal por vista</b>, en el color de acción de su familia. El color de producto nunca es botón ni estado: Farmacia, Compras y Grupos se parecen a éxito, aviso y error.</li>
  <li><b>Dos bordes con trabajos distintos:</b> el decorativo solo separa; un control (campo, botón secundario) lleva siempre el borde de control, de 3:1 o más.</li>
  <li><b>Campo:</b> reposo con borde de control; foco con borde de acción y anillo; error con borde de 2 px, icono y un mensaje que dice el límite; solo lectura sobre agrupación con borde decorativo.</li>
  <li><b>Estados siempre con icono y texto</b>, y el texto sobre su fondo suave en <span class="mono">on-*-soft</span> (4.5:1 o más).</li>
  <li><b>Tema claro único.</b> El azul noche no es fondo de navegación ni de portada.</li></ol>
 <h3>Roles por familia</h3>
 <p class="nota">Valores leídos de los tokens de cada sistema de diseño al generar esta página; contrastes calculados con WCAG 2.2. Para cambiar un valor se cambia el token, no este manual.</p>
 <div class="lam tabla" tabindex="0" role="region" aria-label="Roles por familia (se desplaza a los lados)"><table class="sf-t"><thead><tr><th scope="col">Rol</th><th scope="col">Apps del ecosistema</th><th scope="col">Directorio</th><th scope="col">Manik IA</th></tr></thead><tbody>{tabla}</tbody></table></div>
 <h3>Huecos y diferencias</h3>
 <ol class="reglas">
  <li><b>Hueco:</b> el directorio no define aviso, error ni información (solo éxito). Propuesta: hereda los de las apps, que ya cumplen 4.5:1.</li>
  <li><b>Hueco:</b> el directorio no tiene campo de texto fuera del buscador, y ninguna familia define el estado <b>deshabilitado</b>. Pendiente de diseño; no se inventa aquí.</li>
  <li><b>Mismo rol, valores distintos:</b> borde de control <span class="mono">{E["line-control"]}</span> ({f(E["line-control"], E["surface"])}:1) contra <span class="mono">{R["linea-control"]}</span> ({f(R["linea-control"], R["blanco"])}:1); foco de 2 px contra 3 px; éxito suave <span class="mono">{E["exito-soft"]}</span> contra <span class="mono">{R["exito-suave"]}</span>; borde decorativo <span class="mono">{E["line"]}</span> contra <span class="mono">{R["linea"]}</span>. Todos cumplen; la diferencia no se ve, pero son dos valores que mantener. Por decidir: unificar o dejarlos por familia.</li></ol>
</section>'''

CSS = '''
/* superficies e interfaz (prefijo sf- para no chocar con .muestra, .combo, .f, .d, .m, .t) */
.sf-muestras{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:14px}
.sf-muestras>.sf-lienzo:first-child{grid-column:1/-1}
.sf-lienzo{border-radius:var(--r-2xl);padding:16px;display:grid;gap:10px;border:1px solid var(--line);min-width:0}
.sf-cap{font-size:13px;line-height:18px;color:var(--muted)}
.sf-hoja{border:1px solid;padding:18px;display:grid;gap:16px;min-width:0}
.sf-fila{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.sf-btn{display:inline-flex;align-items:center;gap:6px;padding:0 18px;border:1.5px solid;font:600 15px/20px var(--sans);white-space:nowrap}
.sf-campos{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr));gap:14px}
.sf-campo{display:grid;gap:6px;align-content:start}.sf-lbl{font:600 14px/20px var(--sans);color:var(--ink)}
.sf-in{min-height:44px;border-radius:14px;padding:0 14px;display:flex;align-items:center;justify-content:space-between;font:400 16px/22px var(--sans);color:var(--ink);font-variant-numeric:tabular-nums}
.sf-in i{font-style:normal;color:var(--muted)}.sf-msg{font-size:14px;line-height:20px}
.sf-est{display:inline-flex;align-items:center;gap:6px;border-radius:999px;padding:4px 12px 4px 8px;font:600 14px/20px var(--sans)}
.sf-est b{width:18px;height:18px;border-radius:50%;display:grid;place-items:center;font-size:12px;line-height:1;border:1.5px solid currentColor}
.sf-t td{min-width:150px}.sf-t td:first-child{min-width:170px;font-weight:600}.sf-tok{color:var(--muted);font-size:13px}
.sf-g th{padding-top:20px;color:var(--azul);font:700 15px/20px var(--display);white-space:normal}
.sf-falta{display:inline-block;border-radius:999px;padding:1px 10px;background:var(--aviso-soft);color:var(--on-aviso);font-weight:600;font-size:13px}
'''
