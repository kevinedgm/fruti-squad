# Sellos · opción B · r01: productos sin la M. Pedido (2026-11-05): «prepara una alternativa a los productos que no lleven la M,
# porque alguien comentó que estamos abusando de las M; preparemos una opción B».
# Concepto: solo el sello madre lleva la M. Cada producto usa el mismo cuadro (radio 21) en su color, con el rasgo que hoy vive
# en el borde convertido en pictograma blanco, de trazo 8 sobre la retícula de 100. Uso: python3 gen.py → svg/ y comparacion.html
import os, sys, json, math, base64
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
T = json.load(open(os.path.join(M, 'final/tema.json')))['productos']
PAPEL = '#F6F8FC'; r = 21
CUADRO = f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z'
def engrane(cx=50, cy=51, ro=27, ri=20, n=8):
    p = []
    for i in range(n * 2):
        a0 = math.pi * 2 * i / (n * 2) - math.pi / 2; rad = ro if i % 2 == 0 else ri
        for da in (-0.17, 0.17):
            a = a0 + da; p.append(f'{cx + rad * math.cos(a):.2f} {cy + rad * math.sin(a):.2f}')
    return 'M' + ' L'.join(p) + ' Z'
# pictograma: (trazos, relleno)  — trazos con stroke 8 redondeado; relleno para formas macizas
PICTO = {
 'Expediente': ('M24 36 A5 5 0 0 1 29 31 H42 L47 37 H71 A5 5 0 0 1 76 42 V69 A5 5 0 0 1 71 74 H29 A5 5 0 0 1 24 69 Z M36 53 H64 M36 63 H54', ''),
 'Agenda': ('M29 33 H71 A5 5 0 0 1 76 38 V70 A5 5 0 0 1 71 75 H29 A5 5 0 0 1 24 70 V38 A5 5 0 0 1 29 33 Z M38 25 V39 M62 25 V39 M39 58 L47 66 L62 51', ''),
 'Compras': ('M32 24 H68 V77 L62 72 L56 77 L50 72 L44 77 L38 72 L32 77 Z M41 39 H59 M41 50 H59 M41 61 H51', ''),
 'Farmacia': ('M50 29 V71 M29 50 H71', ''),
 'Impulsa': ('M25 71 L43 53 L54 62 L74 40 M60 39 H75 V54', ''),
 'Grupos': ('M37 25 H70 A5 5 0 0 1 75 30 V58 M30 37 H58 A5 5 0 0 1 63 42 V70 A5 5 0 0 1 58 75 H30 A5 5 0 0 1 25 70 V42 A5 5 0 0 1 30 37 Z', ''),
 'Administración': ('', engrane()),
}
GROSOR = {'Farmacia': 14}
def sello(p, mono=False):
    col = 'currentColor' if mono else T[p]['hex']; k = 'b-' + p.lower().replace('ó', 'o')
    tr, rel = PICTO[p]; sw = GROSOR.get(p, 8)
    if not mono:
        g = f'<path d="{CUADRO}" fill="{col}"/>'
        if tr: g += f'<path d="{tr}" fill="none" stroke="{PAPEL}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
        if rel: g += f'<path d="{rel}" fill="{PAPEL}"/><circle cx="50" cy="51" r="8" fill="{col}"/>'
        cuerpo = g
    else:
        m = f'<mask id="{k}" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><rect width="100" height="100" fill="#fff"/>'
        if tr: m += f'<path d="{tr}" fill="none" stroke="#000" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
        if rel: m += f'<path d="{rel}" fill="#000"/><circle cx="50" cy="51" r="8" fill="#fff"/>'
        m += '</mask>'
        cuerpo = f'<defs>{m}</defs><path d="{CUADRO}" fill="{col}" mask="url(#{k})"/>'
    t = f'{p} Manik'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="{t}"><title>{t}</title>{cuerpo}</svg>'

ORDEN = ['Expediente', 'Agenda', 'Compras', 'Farmacia', 'Impulsa', 'Grupos', 'Administración']
ARCH = {p: p.lower().replace('ó', 'o') for p in ORDEN}
if __name__ == '__main__':
    os.makedirs(os.path.join(D, 'svg'), exist_ok=True)
    for p in ORDEN:
        open(os.path.join(D, 'svg', ARCH[p] + '.svg'), 'w').write(sello(p))
        open(os.path.join(D, 'svg', ARCH[p] + '-1tinta.svg'), 'w').write(sello(p, True))
    u = lambda path: 'data:image/svg+xml;base64,' + base64.b64encode(open(path, 'rb').read()).decode()
    A = lambda p: os.path.join(M, 'final/svg', ARCH[p] + '.svg'); B = lambda p: os.path.join(D, 'svg', ARCH[p] + '.svg')
    MADRE = u(os.path.join(M, 'final/svg/medicalmanik.svg'))
    tam = [96, 48, 32, 24, 16]
    def tira(path):
        d = u(path); return '<div class="t">' + ''.join(f'<img src="{d}" width="{z}" height="{z}" alt="">' for z in tam) + '</div>'
    filas = ''.join(f'<tr><th scope="row"><b>{p}</b> Manik</th><td>{tira(A(p))}</td><td>{tira(B(p))}</td></tr>' for p in ORDEN)
    def selector(f):
        return '<div class="sel">' + ''.join(f'<div class="ti"><img src="{u(f(p))}" alt=""><span>{p}</span></div>' for p in ORDEN[:6]) + '</div>'
    def barra(f):
        return '<div class="bar">' + f'<img src="{MADRE}" alt="" class="madre"><span class="sep"></span>' + ''.join(f'<img src="{u(f(p))}" alt="{p}" width="28" height="28">' for p in ORDEN[:6]) + '</div>'
    mono = '<div class="mono">' + ''.join(f'<img src="{u(os.path.join(D, "svg", ARCH[p] + "-1tinta.svg"))}" alt="" width="44" height="44">' for p in ORDEN) + '</div>'
    HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sellos opción B</title>
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;600;700&display=swap" rel="stylesheet">
<style>:root{{--tinta:#14213D;--muted:#4A5674;--linea:#E1E6F0;--papel:#F7F8FB;--suave:#EEF1F7;color-scheme:light}}*{{box-sizing:border-box}}
body{{margin:0;background:var(--papel);color:var(--tinta);font:400 16px/1.55 "Atkinson Hyperlegible Next",system-ui,sans-serif;padding:0 16px}}h1,h2,h3{{font-family:Urbanist,sans-serif;margin:0}}h1{{font-size:clamp(28px,4.4vw,42px);font-weight:300;line-height:1.1}}h1 b{{font-weight:600}}h2{{font-size:22px;font-weight:600}}h3{{font-size:17px;font-weight:600}}p{{margin:0}}
.wrap{{max-width:1180px;margin:0 auto;padding:36px 0 80px;display:grid;gap:32px;grid-template-columns:minmax(0,1fr)}}.nota{{font-size:14px;line-height:20px;color:var(--muted)}}.cab{{display:grid;gap:12px;max-width:82ch}}
.tw{{overflow-x:auto;border:1px solid var(--linea);border-radius:18px;background:#fff}}table{{border-collapse:collapse;width:100%;min-width:820px}}th,td{{padding:12px 14px;border-bottom:1px solid var(--linea);text-align:left;vertical-align:middle}}thead th{{font:700 12px/16px "Atkinson Hyperlegible Next";letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:var(--suave)}}tbody th{{font:400 16px Urbanist;color:var(--muted);white-space:nowrap}}tbody th b{{color:var(--tinta);font-weight:600}}
.t{{display:flex;align-items:flex-end;gap:14px}}
.dos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,460px),1fr));gap:16px}}.lam{{background:#fff;border:1px solid var(--linea);border-radius:18px;padding:18px;display:grid;gap:12px;min-width:0}}
.sel{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}}.ti{{display:grid;justify-items:center;gap:6px;padding:12px 6px;border-radius:14px;background:var(--papel);font:600 13px/18px "Atkinson Hyperlegible Next"}}.ti img{{width:44px;height:44px}}
.bar{{display:flex;align-items:center;gap:12px;padding:10px 12px;border:1px solid var(--linea);border-radius:14px;flex-wrap:wrap}}.bar .madre{{width:32px;height:32px}}.sep{{width:1px;height:24px;background:var(--linea)}}
.mono{{display:flex;gap:14px;flex-wrap:wrap;color:var(--tinta)}}
.madreb{{display:flex;gap:18px;align-items:center;background:#fff;border:1px solid var(--linea);border-radius:18px;padding:18px}}.madreb img{{width:72px;height:72px}}
ul{{margin:0;padding-left:22px;display:grid;gap:6px}}</style></head><body><main class="wrap">
<header class="cab"><span class="nota">Sellos · opción B · propuesta</span><h1>Productos <b>sin la M</b></h1>
<p>Comentario recibido: «estamos abusando de las M». En la opción B solo el sello madre de MedicalManik lleva la M. Cada producto conserva el mismo cuadro, el mismo radio y el blanco sobre su color, y el rasgo que hoy vive en el borde del sello (carpeta, argollas, ticket, cruz, flecha, tarjeta, engrane) pasa adentro como pictograma.</p>
<div class="madreb"><img src="{MADRE}" alt="Sello de MedicalManik"><p>La M queda como firma de la empresa: aparece una vez (en el sello madre, el respaldo «de MedicalManik» y el inicio del ecosistema) en vez de siete.</p></div></header>
<section aria-labelledby="s1"><h2 id="s1">A (aprobada, con M) contra B (sin M)</h2><p class="nota">A 96, 48, 32, 24 y 16 px.</p><div class="tw" tabindex="0" role="region" aria-label="Comparación A y B"><table><thead><tr><th scope="col">Producto</th><th scope="col">A · con la M</th><th scope="col">B · sin la M</th></tr></thead><tbody>{filas}</tbody></table></div></section>
<section aria-labelledby="s2"><h2 id="s2">Donde más se ven: el selector y la barra</h2><div class="dos"><div class="lam"><h3>A · con la M</h3>{selector(A)}{barra(A)}</div><div class="lam"><h3>B · sin la M</h3>{selector(B)}{barra(B)}</div></div></section>
<section aria-labelledby="s3"><h2 id="s3">B a una tinta</h2><div class="lam">{mono}<p class="nota">El pictograma queda calado: funciona impreso, bordado o en sello.</p></div></section>
<section aria-labelledby="s4"><h2 id="s4">Qué se gana y qué se pierde</h2><div class="dos"><div class="lam"><h3>Gana</h3><ul><li>Cada producto se reconoce por lo que hace, sin leer el nombre: el pictograma lo dice.</li><li>La M deja de repetirse siete veces y vuelve a ser la firma de la empresa.</li><li>A 16 px un pictograma simple se lee mejor que la M con un rasgo pequeño en el borde.</li></ul></div>
<div class="lam"><h3>Pierde</h3><ul><li>El parentesco: sin la línea de pulso, los sellos se parecen más a íconos de app genéricos; la familia la sostienen solo el cuadro, el radio y el color.</li><li>Se tienen que rehacer los activos y los PNG (sencillo, igual que hoy).</li><li>Farmacia queda como una cruz: verde, nunca roja (emblema protegido).</li></ul></div></div>
<p class="nota">Lectura [inferencia]: B resuelve el comentario y gana claridad; A conserva mejor la familia. Una opción intermedia sería B con un detalle de la línea de pulso dentro de cada pictograma, a costa de complejidad a 16 px.</p></section>
</main></body></html>'''
    open(os.path.join(D, 'comparacion.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
