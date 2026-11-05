# Sellos con la M original · r01. Pedido (2026-11-05): «respetar la forma de la M: tomar del archivo AI la forma de la M para no
# redondear sus esquinas y forma». Fuente: «Logos editables MM.ai» del usuario (no se versiona), mesa de trabajo 5 (sello sólido):
# trazado relleno de la M, extraído con pdftocairo. Aquí solo queda la geometría normalizada (constante M_ORIGINAL).
# Sustituye en cada SVG la línea redibujada (trazo de 13 con uniones redondas) por la M original rellena, recortada al contenedor.
# Uso: python3 gen.py → svg/ (copias nuevas, no toca ../final ni ../manik-final) y comparacion.html
import os, re, base64
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
# Cuadro original en el AI: x 164.019531–675.792969, y 157.664062–669.441406 (radio de esquina 104.51 = 20.4 % → el «21» de la retícula).
X0, Y0, W, H = 164.019531, 157.664062, 675.792969 - 164.019531, 669.441406 - 157.664062
RAW = ('M 672.515625 479.230469 C 665.078125 479.230469 658.453125 474.523438 656.007812 467.5 L 598.5 272.746094 C 596.253906 266.292969 588.824219 261.011719 581.992188 261.011719 '
 'L 537.1875 261.011719 C 529.621094 261.011719 522.914062 265.878906 520.566406 273.074219 L 449.542969 490.875 C 438.332031 525.253906 423.152344 524.414062 415.804688 489.007812 '
 'L 355.78125 199.730469 C 354.097656 191.617188 346.949219 185.800781 338.664062 185.800781 L 296.449219 185.800781 C 288.507812 185.800781 281.566406 191.152344 279.542969 198.832031 '
 'L 216.925781 436.539062 C 214.90625 444.21875 207.960938 449.570312 200.019531 449.570312 L 157.453125 449.570312 C 147.796875 449.570312 139.96875 457.398438 139.96875 467.054688 '
 'L 139.96875 501.941406 C 139.96875 511.621094 147.832031 519.457031 157.515625 519.421875 L 201.464844 519.269531 L 201.449219 519.339844 L 239.601562 519.339844 '
 'C 247.652344 519.339844 254.664062 513.839844 256.582031 506.019531 L 299.535156 330.773438 C 309.65625 289.492188 325 289.765625 333.632812 331.386719 L 391.3125 609.367188 '
 'C 392.996094 617.480469 400.144531 623.296875 408.433594 623.296875 L 451.386719 623.296875 C 458.976562 623.296875 465.699219 618.402344 468.027344 611.179688 L 541.101562 384.570312 '
 'C 550.613281 355.066406 565.640625 355.234375 574.496094 384.945312 L 610.820312 506.847656 C 613.027344 514.261719 619.84375 519.339844 627.574219 519.339844 L 669.324219 519.339844 '
 'L 669.304688 519.269531 L 985.988281 519.472656 C 995.652344 519.480469 1003.488281 511.648438 1003.488281 501.988281 L 1003.488281 479.230469 Z')
def norm(d):
    t = d.split(); out = []; i = 0
    while i < len(t):
        if t[i] in 'MLCZ': out.append(t[i]); i += 1; continue
        x = (float(t[i]) - X0) * 100 / W; y = (float(t[i + 1]) - Y0) * 100 / H
        out.append(f'{x:.2f} {y:.2f}'); i += 2
    return ' '.join(out)
M_ORIGINAL = norm(RAW)
LINEA = 'M-6 63 L13 63 L27 12 L49 86 L71 25 L84 64 L106 64'
COLOR = re.compile(r'<path (clip-path="url\(#[^)]*\)") d="' + re.escape(LINEA) + r'" fill="none" stroke="(#[0-9A-Fa-f]{6})" stroke-width="13" stroke-linejoin="round"/>')
MASK = '<path d="' + LINEA + '" fill="none" stroke="#000" stroke-width="13" stroke-linejoin="round"/>'
def convertir(svg):
    n = len(COLOR.findall(svg)) + svg.count(MASK)
    svg = COLOR.sub(lambda m: f'<path {m.group(1)} d="{M_ORIGINAL}" fill="{m.group(2)}"/>', svg)
    svg = svg.replace(MASK, f'<path d="{M_ORIGINAL}" fill="#000"/>')
    return svg, n

if __name__ == '__main__':
    os.makedirs(os.path.join(D, 'svg'), exist_ok=True); tot = 0; hechos = []
    for carpeta in ('final/svg', 'manik-final/svg'):
        for f in sorted(os.listdir(os.path.join(M, carpeta))):
            s = open(os.path.join(M, carpeta, f)).read(); n2, n = convertir(s)
            if n:
                pre = 'manik-' if carpeta.startswith('manik') else ''
                open(os.path.join(D, 'svg', pre + f), 'w').write(n2); tot += n; hechos.append(pre + f)
    print('archivos', len(hechos), 'sustituciones', tot)
    u = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
    PARES = [('medicalmanik', 'MedicalManik'), ('expediente', 'Expediente'), ('agenda', 'Agenda'), ('compras', 'Compras'), ('farmacia', 'Farmacia'), ('impulsa', 'Impulsa'), ('grupos', 'Grupos'), ('administracion', 'Administración')]
    def fila(antes, despues, nombre, fondo='#FFFFFF'):
        tam = [120, 64, 32, 24, 16]
        cel = lambda p: ''.join(f'<img src="{u(p)}" width="{z}" height="{z}" alt="">' for z in tam)
        return f'<tr><th scope="row">{nombre}</th><td style="background:{fondo}"><div class="t">{cel(antes)}</div></td><td style="background:{fondo}"><div class="t">{cel(despues)}</div></td></tr>'
    filas = ''.join(fila(os.path.join(M, 'final/svg', f'{k}.svg'), os.path.join(D, 'svg', f'{k}.svg'), n) for k, n in PARES)
    filas += fila(os.path.join(M, 'manik-final/svg/simbolo.svg'), os.path.join(D, 'svg/manik-simbolo.svg'), 'Directorio (pin)')
    mono = ''.join(fila(os.path.join(M, 'final/svg', f'{k}-1tinta.svg'), os.path.join(D, 'svg', f'{k}-1tinta.svg'), n + ' · una tinta') for k, n in PARES[:3])
    osc = fila(os.path.join(M, 'manik-final/svg/simbolo-blanco.svg'), os.path.join(D, 'svg/manik-simbolo-blanco.svg'), 'Pin en blanco', '#14213D')
    logos = ''.join(f'<figure><img src="{u(os.path.join(M, a))}" alt=""><img src="{u(os.path.join(D, "svg", b))}" alt=""><figcaption>{c}: antes arriba, M original abajo</figcaption></figure>'
                    for a, b, c in [('final/svg/medicalmanik-logotipo.svg', 'medicalmanik-logotipo.svg', 'Logotipo MedicalManik'), ('manik-final/svg/logotipo.svg', 'manik-logotipo.svg', 'Logotipo del directorio')])
    HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sellos con la M original</title>
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;600;700&display=swap" rel="stylesheet">
<style>:root{{--tinta:#14213D;--muted:#4A5674;--linea:#E1E6F0;--papel:#F7F8FB;--azul:#234899;color-scheme:light}}*{{box-sizing:border-box}}
body{{margin:0;background:var(--papel);color:var(--tinta);font:400 16px/1.55 "Atkinson Hyperlegible Next",system-ui,sans-serif;padding:0 16px}}h1,h2{{font-family:Urbanist,sans-serif;margin:0}}h1{{font-size:clamp(28px,4.4vw,42px);font-weight:300;line-height:1.1}}h1 b{{font-weight:600}}h2{{font-size:22px;font-weight:600}}p{{margin:0}}
.wrap{{max-width:1180px;margin:0 auto;padding:36px 0 80px;display:grid;gap:32px;grid-template-columns:minmax(0,1fr)}}.nota{{font-size:14px;line-height:20px;color:var(--muted)}}.cab{{display:grid;gap:12px;max-width:80ch}}
.tw{{overflow-x:auto;border:1px solid var(--linea);border-radius:18px;background:#fff}}table{{border-collapse:collapse;width:100%;min-width:900px}}th,td{{padding:12px 14px;border-bottom:1px solid var(--linea);text-align:left;vertical-align:middle}}thead th{{font:700 12px/16px "Atkinson Hyperlegible Next";letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:#EEF1F7}}tbody th{{font-weight:600;white-space:nowrap}}
.t{{display:flex;align-items:flex-end;gap:14px}}
.logos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:16px}}.logos figure{{margin:0;background:#fff;border:1px solid var(--linea);border-radius:18px;padding:20px;display:grid;gap:18px}}.logos img{{width:100%;max-width:420px;height:auto}}.logos figcaption{{font-size:14px;color:var(--muted)}}
.zoom{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:16px}}.zoom figure{{margin:0;background:#fff;border:1px solid var(--linea);border-radius:18px;padding:16px;display:grid;gap:8px;justify-items:center}}.zoom img{{width:260px;height:260px}}
ul{{margin:0;padding-left:22px;display:grid;gap:6px;max-width:80ch}}</style></head><body><main class="wrap">
<header class="cab"><span class="nota">Sellos · ronda 1 · propuesta</span><h1>Los sellos con la <b>M original</b></h1>
<p>La M ya no es una línea de grosor fijo con uniones redondas: es el trazado original del archivo de MedicalManik, con su grosor variable, sus picos estrechos y sus esquinas. Se colocó en el mismo cuadro (el radio de esquina del original es 20.4 % del lado; el de los sellos, 21 %) y se recorta con el contenedor de cada producto, igual que antes.</p>
<p class="nota">Se sustituyó en {len(hechos)} archivos ({tot} trazos). Los contenedores, rasgos de producto y colores no cambian.</p></header>
<section class="zoom" aria-label="Detalle a gran tamaño"><figure><img src="{u(os.path.join(M, 'final/svg/medicalmanik.svg'))}" alt="Sello anterior"><figcaption class="nota">Antes: línea redibujada</figcaption></figure><figure><img src="{u(os.path.join(D, 'svg/medicalmanik.svg'))}" alt="Sello con la M original"><figcaption class="nota">Ahora: M original</figcaption></figure></section>
<section aria-labelledby="s1"><h2 id="s1">Todos los sellos, a 120, 64, 32, 24 y 16 px</h2><div class="tw" tabindex="0" role="region" aria-label="Comparación de sellos"><table><thead><tr><th scope="col">Sello</th><th scope="col">Antes</th><th scope="col">M original</th></tr></thead><tbody>{filas}{mono}{osc}</tbody></table></div></section>
<section aria-labelledby="s2"><h2 id="s2">Logotipos</h2><div class="logos">{logos}</div></section>
<section aria-labelledby="s3"><h2 id="s3">Qué revisar</h2><ul><li>A 16 y 24 px los picos de la M original son más finos que la línea redibujada: comprobar que se siga leyendo en el favicon y en la barra lateral.</li><li>En los sellos con rasgo arriba (carpeta de Expediente, argollas de Agenda) el pico alto de la M queda cerca del borde: revisar que no choque.</li><li>Al aprobar: se reemplazan los sellos en el paquete final, el pin del directorio, los PNG, los assets del sistema de diseño y la lámina de construcción del manual.</li></ul></section>
</main></body></html>'''
    open(os.path.join(D, 'comparacion.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
