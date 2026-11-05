# Grupos Manik · color nuevo · r01. Pedido (2026-11-05): «el color rojo de Grupos no era buena opción porque está asociado a error».
# Medido: Grupos #C73A55 contra error #C33F4E = ΔE 1.6 (OKLab ×100): casi el mismo color.
# Candidatos: búsqueda en OKLCH (L 0.48–0.54, C 0.10–0.16, todo el círculo) que maximiza la distancia mínima a los otros
# productos, los 4 estados y el cian de marca, con blanco encima ≥ 4.6:1. Uso: python3 gen.py → grupos.html
import os, math, base64, json
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
ACTUAL = '#C73A55'
OTROS = {'Expediente': '#234899', 'Agenda': '#007C8C', 'Compras': '#A15C07', 'Farmacia': '#1B7F52', 'Impulsa': '#504CA1', 'Administración': '#3A4558',
         'éxito': '#15814B', 'aviso': '#A75F00', 'error': '#C33F4E', 'info': '#3F7695'}
CAND = [('Orquídea', '#9D469E', 'Magenta violáceo. El tono libre más lejano de todos: no hay otro producto ni estado cerca.'),
        ('Oliva', '#666005', 'Verde amarillento oscuro. Lejos de los estados; sobrio, «institucional».'),
        ('Azul cobalto', '#346ACA', 'Azul medio, más claro que Expediente. Lejos de los estados, pero se acerca a los azules de la familia.')]
def lin(c): return ((c + .055) / 1.055) ** 2.4 if c > .04045 else c / 12.92
def rgb(h): return [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
def lab(h):
    r, g, b = map(lin, rgb(h))
    l = .4122214708*r + .5363325363*g + .0514459929*b; m = .2119034982*r + .6806995451*g + .1073969566*b; s = .0883024619*r + .2817188376*g + .6299787005*b
    l, m, s = [x ** (1/3) for x in (l, m, s)]
    return (.2104542553*l + .7936177850*m - .0040720468*s, 1.9779984951*l - 2.4285922050*m + .4505937099*s, .0259040371*l + .7827717662*m - .8086757660*s)
def dE(a, b): return 100 * math.dist(lab(a), lab(b))
def lum(h): r, g, b = map(lin, rgb(h)); return .2126*r + .7152*g + .0722*b
def cr(a, b): x, y = sorted((lum(a), lum(b)), reverse=True); return (x + .05) / (y + .05)
def mezcla(a, b, t): A, B = rgb(a), rgb(b); return '#' + ''.join(f'{round((x*(1-t)+y*t)*255):02X}' for x, y in zip(A, B))
def suave(h): return mezcla(h, '#FFFFFF', .91)
def tinta(h):  # oscurece hasta 4.5:1 sobre su suave
    t = 0; s = suave(h); c = h
    while cr(c, s) < 4.5 and t < 1: t += .02; c = mezcla(h, '#14213D', t)
    return c
u = lambda txt: 'data:image/svg+xml;base64,' + base64.b64encode(txt.encode()).decode()
SA = open(os.path.join(M, 'final/svg/grupos.svg')).read(); SB = open(os.path.join(M, 'sellos-b-r01/svg/grupos.svg')).read()
ECO = open(os.path.join(M, 'final/svg/ecosistema.svg')).read()
FAM = [(k, open(os.path.join(M, f'final/svg/{k}.svg')).read()) for k in ('expediente', 'agenda', 'compras', 'farmacia', 'impulsa')]

def bloque(nombre, hx, nota, actual=False):
    near = min(OTROS, key=lambda k: dE(hx, OTROS[k])); d = dE(hx, OTROS[near]); de_err = dE(hx, OTROS['error'])
    sa = u(SA.replace(ACTUAL, hx)); sb = u(SB.replace(ACTUAL, hx)); eco = u(ECO.replace(ACTUAL, hx)); sv, tn = suave(hx), tinta(hx)
    fila = ''.join(f'<img src="{u(s)}" alt="" width="40" height="40">' for _, s in FAM) + f'<img src="{sa}" alt="Grupos" width="40" height="40" class="yo">'
    return f'''<article class="card{' act' if actual else ''}" aria-labelledby="c-{hx[1:]}"><header><span class="mu" style="background:{hx}"></span><div><h3 id="c-{hx[1:]}">{nombre} <span class="hex">{hx}</span></h3><p class="nota">{nota}</p></div></header>
 <div class="sellos"><figure><img src="{sa}" alt="" width="84" height="84"><figcaption>A · con la M</figcaption></figure><figure><img src="{sb}" alt="" width="84" height="84"><figcaption>B · sin la M</figcaption></figure><figure><img src="{eco}" alt="" width="84" height="84"><figcaption>Mosaico</figcaption></figure></div>
 <div class="fam">{fila}</div>
 <div class="junto"><span class="est" style="background:#F9ECED;color:#BA3D4D">✕ Pago rechazado</span><span class="tile" style="background:{sv};color:{tn}"><img src="{sa}" alt="" width="24" height="24"><b>Grupos</b> Manik</span></div>
 <dl><dt>Distancia a error</dt><dd class="{'mal' if de_err < 8 else 'ok'}">{de_err:.1f}</dd><dt>Más cercano</dt><dd>{near} · {d:.1f}</dd><dt>Blanco encima</dt><dd>{cr(hx, '#FFFFFF'):.2f}:1</dd><dt>Tinta sobre suave</dt><dd>{tn} · {cr(tn, sv):.2f}:1</dd></dl></article>'''

cards = bloque('Actual', ACTUAL, 'El rojo de hoy: casi idéntico al color de error.', True) + ''.join(bloque(n, h, t) for n, h, t in CAND)
HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Color de Grupos Manik</title>
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;600;700&display=swap" rel="stylesheet">
<style>:root{{--tinta:#14213D;--muted:#4A5674;--linea:#E1E6F0;--papel:#F7F8FB;color-scheme:light}}*{{box-sizing:border-box}}
body{{margin:0;background:var(--papel);color:var(--tinta);font:400 16px/1.55 "Atkinson Hyperlegible Next",system-ui,sans-serif;padding:0 16px}}h1,h2,h3{{font-family:Urbanist,sans-serif;margin:0}}h1{{font-size:clamp(28px,4.4vw,42px);font-weight:300;line-height:1.1}}h1 b{{font-weight:600}}h2{{font-size:22px;font-weight:600}}h3{{font-size:19px;font-weight:600}}p{{margin:0}}
.wrap{{max-width:1180px;margin:0 auto;padding:36px 0 80px;display:grid;gap:28px;grid-template-columns:minmax(0,1fr)}}.nota{{font-size:14px;line-height:20px;color:var(--muted)}}.cab{{display:grid;gap:12px;max-width:84ch}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,520px),1fr));gap:16px}}
.card{{background:#fff;border:1px solid var(--linea);border-radius:20px;padding:18px;display:grid;gap:14px;min-width:0}}.card.act{{border-style:dashed}}
.card header{{display:flex;gap:12px;align-items:center}}.mu{{width:44px;height:44px;border-radius:12px;flex:none}}.hex{{font:400 14px ui-monospace,Menlo,monospace;color:var(--muted)}}
.sellos{{display:flex;gap:16px;flex-wrap:wrap}}.sellos figure{{margin:0;display:grid;gap:4px;justify-items:center;font-size:13px;color:var(--muted)}}
.fam{{display:flex;gap:8px;align-items:center;padding:10px;border:1px solid var(--linea);border-radius:14px;flex-wrap:wrap}}.fam .yo{{outline:2px dashed #9AA3B8;outline-offset:3px;border-radius:10px}}
.junto{{display:flex;gap:10px;flex-wrap:wrap;align-items:center}}.est{{border-radius:999px;padding:5px 12px;font:600 14px/20px "Atkinson Hyperlegible Next"}}.tile{{display:inline-flex;align-items:center;gap:8px;border-radius:12px;padding:6px 12px 6px 6px;font:400 15px Urbanist}}.tile b{{font-weight:600}}
dl{{margin:0;display:grid;grid-template-columns:auto 1fr auto 1fr;gap:4px 12px;font-size:14px}}dt{{color:var(--muted)}}dd{{margin:0;font-weight:600;font-variant-numeric:tabular-nums}}dd.mal{{color:#B23A48}}dd.ok{{color:#157B4A}}
.reco{{background:#fff;border:1px solid var(--linea);border-radius:20px;padding:20px;display:grid;gap:10px;max-width:86ch}}ol{{margin:0;padding-left:22px;display:grid;gap:6px}}
@media(max-width:560px){{dl{{grid-template-columns:auto 1fr}}}}</style></head><body><main class="wrap">
<header class="cab"><span class="nota">Grupos Manik · color · ronda 1 · propuesta</span><h1>Un color para Grupos que <b>no diga «error»</b></h1>
<p>Grupos usa #C73A55 y el color de error del sistema es #C33F4E: la distancia entre ellos es 1.6, donde menos de 2 casi no se distingue. En una lista con un aviso de error al lado, Grupos parece una alerta. Los candidatos salen de buscar en todo el círculo de color el tono más lejano a los otros productos y a los cuatro estados, con el blanco encima en 4.6:1 o más.</p>
<p class="nota">Distancia medida en OKLab (×100): menos de 2 casi igual, de 2 a 5 parecido, más de 10 claramente distinto. Cada tarjeta muestra el sello A, el B, el mosaico del ecosistema, la fila con los demás productos y Grupos junto a un aviso de error.</p></header>
<div class="grid">{cards}</div>
<section class="reco" aria-labelledby="s2"><h2 id="s2">Recomendación [inferencia]</h2>
<ol><li><b>Orquídea #9D469E</b>: es el único tono libre del círculo; queda a 13.7 del producto más cercano (Impulsa) y a 14.2 de error. Sigue siendo cálido y humano, sin leerse como alerta.</li>
<li><b>Oliva #666005</b> si se prefiere algo sobrio; su vecino es Compras (ámbar), con quien comparte calidez.</li>
<li><b>Azul cobalto</b> no lo recomiendo: ya hay dos azules (Expediente y el violeta de Impulsa) y un tercero obliga a leer el nombre.</li></ol>
<p class="nota">Al elegir se actualizan: el sello de Grupos (A y B), el mosaico del ecosistema, los tokens app-grupos del sistema de diseño, la tabla del manual y los PNG.</p></section>
</main></body></html>'''
open(os.path.join(D, 'grupos.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
