# Nexa Squad · guía de marca + kit de marketplace. Usa ../final (símbolos y tema).
# Uso: python3 gen.py <carpeta de fuentes> && node kit.cjs → kit/*.png, guia.html, textos.md
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); FIN = os.path.join(H, '..', 'final'); FD = sys.argv[1]
exec(open(os.path.join(H, 'textos.py')).read())
tema = json.load(open(os.path.join(FIN, 'tema.json'))); C = tema['color']
P = tema['productos']; ORDER = list(P)
def sv(k, n, uid=''):
    s = open(os.path.join(FIN, k, 'svg', n + '.svg')).read()
    return s.replace('id="', f'id="{uid}').replace('url(#', f'url(#{uid}') if uid else s
FONT = (f"@font-face{{font-family:'Bricolage Grotesque';src:url('file://{FD}/BricolageGrotesque-Bold.ttf');font-weight:700}}"
        f"@font-face{{font-family:'Bricolage Grotesque';src:url('file://{FD}/BricolageGrotesque-Regular.ttf');font-weight:400}}")
os.makedirs(os.path.join(H, 'kit', 'src'), exist_ok=True)
def portada(k, w, h):
    n, p = P[k]['nombre'], P[k]['producto']; tag = T[k]['en'][0]
    fam = '' if k != 'squad' else '<div class="fam">' + ''.join(sv(x, 'simbolo-oscuro', f'f{x}') for x in ORDER[1:]) + '</div>'
    sub = 'Nexa Squad · for Claude Code, Codex and Kiro' if k != 'squad' else 'for Claude Code, Codex and Kiro'
    return f'''<!doctype html><meta charset=utf-8><style>{FONT}*{{margin:0;box-sizing:border-box}}body{{width:{w}px;height:{h}px;background:{C["tinta"]};color:{C["claro"]};font-family:'Bricolage Grotesque';overflow:hidden;position:relative}}
.s{{position:absolute;left:{int(w*.07)}px;top:50%;transform:translateY(-50%);width:{int(h*.42)}px;height:{int(h*.42)}px}}.s svg{{width:100%;height:100%}}
.t{{position:absolute;left:{int(w*.07+h*.42+w*.05)}px;right:{int(w*.06)}px;top:50%;transform:translateY(-50%)}}
.e{{font-size:{int(h*.032)}px;letter-spacing:.12em;text-transform:uppercase;color:{C["cian"]};font-weight:700;margin-bottom:{int(h*.025)}px}}
h1{{font-weight:700;font-size:{int(h*.13)}px;line-height:1;letter-spacing:-.02em}}h2{{font-weight:400;font-size:{int(h*.055)}px;color:#c9c9c3;margin-top:{int(h*.02)}px}}
p{{font-weight:400;font-size:{int(h*.042)}px;margin-top:{int(h*.055)}px;max-width:{int(w*.52)}px;line-height:1.3}}
.k{{position:absolute;left:{int(w*.07)}px;bottom:{int(h*.07)}px;font-size:{int(h*.03)}px;color:#a1a19b}}
.fam{{position:absolute;right:{int(w*.06)}px;bottom:{int(h*.065)}px;display:flex;gap:{int(h*.02)}px}}.fam svg{{width:{int(h*.06)}px;height:{int(h*.06)}px}}</style>
<div class="s">{sv(k, "simbolo-oscuro")}</div><div class="t"><div class="e">{"Nexa Squad · agent" if k!="squad" else "8 agents · module composition"}</div><h1>{n}</h1><h2{' style="font-size:'+str(int(h*.042))+'px;white-space:nowrap"' if k=="squad" else ""}>{p if k!="squad" else "Orka · Inqa · Arko · Fluxa · Kompa · Kura · Forja · Vera"}</h2><p>{tag}</p></div><div class="k">{sub}</div>{fam}'''
jobs = []
for k in ORDER:
    for nm, w, h in (('og', 1200, 630), ('social', 1280, 640)):
        f = os.path.join(H, 'kit', 'src', f'{k}-{nm}.html'); open(f, 'w').write(portada(k, w, h))
        jobs.append([f, os.path.join(H, 'kit', f'{k}-{nm}-{w}x{h}.png'), w, h])
json.dump(jobs, open(os.path.join(H, 'kit', 'src', 'jobs.json'), 'w'))
md = ['# Nexa Squad · textos de marketplace', '', 'Fuente: squad.json y README de kevinedgm/nexa-squad. Lema corto + descripción, en español e inglés.', '']
for k in ORDER:
    md += [f"## {P[k]['nombre']} · {P[k]['producto']}", '', f"**ES** · {T[k]['es'][0]}", '', T[k]['es'][1], '', f"**EN** · {T[k]['en'][0]}", '', T[k]['en'][1], '']
open(os.path.join(H, 'textos.md'), 'w').write('\n'.join(md))
def esc(s): return s.replace('&', '&amp;')
prods = ''.join(f'''<article class="pr" id="{k}"><div class="pv">{sv(k, "simbolo", "p"+k)}</div><div><h3>{esc(P[k]["nombre"])} <span>{esc(P[k]["producto"])}</span></h3>
<p class="tag">{esc(T[k]["es"][0])}</p><p>{esc(T[k]["es"][1])}</p><p class="meta"><b>Hueco:</b> {SIMB[k]}</p></div></article>''' for k in ORDER)
kitimgs = ''.join(f'<figure><img src="kit/{k}-og-1200x630.png" alt="Portada de {esc(P[k]["nombre"])}"><figcaption>{esc(P[k]["nombre"])} · 1200 × 630</figcaption></figure>' for k in ORDER)
mal = [('Pintar el bloque de cian', sv('arko', 'simbolo', 'm1').replace(f'fill="{C["tinta"]}"', f'fill="{C["cian"]}"').replace(f'fill="{C["cian"]}"/><rect', f'fill="{C["tinta"]}"/><rect', 1)),
       ('Cian claro sobre bloque claro', sv('kura', 'simbolo-oscuro', 'm2').replace(C['cian_oscuro'], C['cian'])),
       ('Deformar o girar el símbolo', sv('vera', 'simbolo', 'm3').replace('<svg ', '<svg style="transform:scaleX(1.4) rotate(10deg)" ')),
       ('Un color distinto por agente', sv('kompa', 'simbolo', 'm4').replace(C['cian'], '#E5484D'))]
malh = ''.join(f'<figure class="no"><span>{s}</span><figcaption>✕ {t}</figcaption></figure>' for t, s in mal)
reglas = ''.join(f'<li>{esc(r)}</li>' for r in tema['reglas'])
ct = tema['construccion']
GRID = ''.join(f'<line x1="{v}" y1="0" x2="{v}" y2="48" stroke="{C["cian"]}" stroke-width=".2"/><line x1="0" y1="{v}" x2="48" y2="{v}" stroke="{C["cian"]}" stroke-width=".2"/>' for v in range(4, 45, 4))
cons = sv('squad', 'simbolo', 'c').replace('</svg>', GRID + '</svg>')
fam_cl = ''.join(f'<figure>{sv(k,"simbolo","a"+k)}<figcaption>{P[k]["nombre"]}</figcaption></figure>' for k in ORDER)
fam_os = ''.join(f'<figure>{sv(k,"simbolo-oscuro","b"+k)}<figcaption>{P[k]["nombre"]}</figcaption></figure>' for k in ORDER)
lockups = ''.join(f'<div class="lk">{sv(k,"lockup","l"+k)}</div>' for k in ORDER)
css = f'''*{{box-sizing:border-box}}:root{{--papel:{C["papel"]};--tinta:{C["tinta"]};--sub:{C["sub_claro"]};--linea:#e2e2dc;--tarjeta:#fff;--oscuro:{C["oscuro"]};--claro:{C["claro"]};--cian:{C["cian"]};--cian-o:{C["cian_oscuro"]}}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--papel:#131317;--tinta:#ededea;--sub:#a8a8b0;--linea:#2b2b32;--tarjeta:#1a1a1f;color-scheme:dark}}}}
:root[data-theme="dark"]{{--papel:#131317;--tinta:#ededea;--sub:#a8a8b0;--linea:#2b2b32;--tarjeta:#1a1a1f;color-scheme:dark}}
body{{margin:0;background:var(--papel);color:var(--tinta);font:400 16px/1.6 'Bricolage Grotesque',ui-sans-serif,system-ui,sans-serif;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 56px}}
main{{max-width:1080px;margin:0 auto;display:grid;gap:36px}}
.hero{{background:{C["tinta"]};color:{C["claro"]};border-radius:0 0 24px 24px;padding:56px 40px;display:flex;gap:32px;align-items:center;flex-wrap:wrap}}.hero svg{{width:120px;height:120px}}
h1{{font-size:clamp(36px,6vw,56px);line-height:1;letter-spacing:-.02em;margin:0}}.hero p{{margin:12px 0 0;color:#c9c9c3;max-width:600px}}.hero .e{{margin:0;color:var(--cian);font-weight:700;letter-spacing:.1em;text-transform:uppercase;font-size:13px}}
h2{{font-size:30px;letter-spacing:-.01em;margin:0 0 10px;line-height:1.1}}section>p{{margin:0 0 14px;max-width:72ch;color:var(--sub)}}
.box{{background:var(--tarjeta);border:1px solid var(--linea);border-radius:18px;padding:22px}}
.fam{{display:flex;flex-wrap:wrap;gap:16px 20px;padding:22px;border-radius:16px}}.fam figure{{margin:0;display:grid;justify-items:center;gap:6px}}.fam svg{{width:64px;height:64px}}.fam figcaption{{font-size:13px;opacity:.75}}
.fam.cl{{background:#fff;color:{C["tinta"]};border:1px solid var(--linea)}}.fam.os{{background:{C["oscuro"]};color:{C["claro"]};margin-top:12px}}
.cons{{display:flex;gap:28px;align-items:center;flex-wrap:wrap}}.cons svg{{width:200px;height:200px;background:#fff;border-radius:12px;border:1px solid var(--linea)}}.cons ul{{margin:0;padding-left:20px}}
.pr{{display:grid;grid-template-columns:96px minmax(0,1fr);gap:20px;background:var(--tarjeta);border:1px solid var(--linea);border-radius:18px;padding:20px;margin-bottom:12px}}.pv svg{{width:96px;height:96px}}
h3{{margin:0;font-size:24px;line-height:1.15}}h3 span{{font-weight:400;color:var(--sub);font-size:18px}}.tag{{font-weight:700;margin:6px 0 4px}}.pr p{{margin:4px 0}}.meta{{font-size:14.5px;color:var(--sub)}}
.pal{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}}.sw{{border-radius:14px;padding:14px;min-height:110px;display:flex;flex-direction:column;justify-content:flex-end;font-size:14px;border:1px solid var(--linea)}}.sw b{{font-size:16px}}.sw code{{font-size:13px;opacity:.85}}
.lks{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px}}.lk{{background:#fff;border:1px solid var(--linea);border-radius:12px;padding:16px}}.lk svg{{height:44px;width:auto;max-width:100%}}
.type b{{font-size:clamp(36px,7vw,60px);letter-spacing:-.02em;line-height:1;display:block}}.type p{{margin:8px 0 0}}
ol{{margin:0;padding-left:22px}}li{{margin:4px 0}}
.nos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px}}.no{{margin:0;background:var(--tarjeta);border:1px solid var(--linea);border-radius:14px;padding:16px;display:grid;justify-items:center;gap:8px;text-align:center}}.no span{{display:grid;place-items:center;width:96px;height:96px;background:#fff;border-radius:12px}}.no svg{{width:72px;height:72px}}.no figcaption{{color:#C4321F;font-weight:700;font-size:14px}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}.grid figure{{margin:0}}.grid img{{width:100%;border-radius:14px;display:block}}.grid figcaption{{font-size:13px;color:var(--sub);margin-top:6px}}
code{{font-family:ui-monospace,monospace;font-size:.92em}}
@media (max-width:760px){{.grid{{grid-template-columns:1fr}}.pr{{grid-template-columns:1fr}}.hero{{padding:36px 20px}}}}'''
pal = (f'<div class="sw" style="background:{C["tinta"]};color:{C["claro"]}"><b>Tinta</b><code>{C["tinta"]}</code>bloque en claro</div>'
       f'<div class="sw" style="background:{C["claro"]};color:{C["tinta"]}"><b>Claro</b><code>{C["claro"]}</code>bloque en oscuro</div>'
       f'<div class="sw" style="background:{C["cian"]};color:{C["tinta"]}"><b>Cian</b><code>{C["cian"]}</code>hueco en claro · {tema["contraste"]["cian/tinta"]}:1 contra tinta</div>'
       f'<div class="sw" style="background:{C["cian_oscuro"]};color:#fff"><b>Cian oscuro</b><code>{C["cian_oscuro"]}</code>hueco en oscuro · {tema["contraste"]["cian_oscuro/claro"]}:1 contra claro</div>'
       f'<div class="sw" style="background:{C["oscuro"]};color:{C["claro"]}"><b>Oscuro</b><code>{C["oscuro"]}</code>fondo oscuro</div>')
html = (f'<title>Nexa Squad · Guía de marca</title><meta name="claude:viewport-fit-sides" content="cover">'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,700&display=swap">'
        f'<style>{css}</style><header class="hero">{sv("squad", "simbolo-oscuro", "h")}<div><p class="e">Guía de marca · kit de marketplace</p><h1>Nexa Squad</h1><p>Ocho agentes que diseñan y construyen módulos completos acomodando bien los componentes que ya tienes. Para Claude Code, Codex y Kiro.</p></div></header><main>'
        f'<section><h2>La idea</h2><p>Nexa no fabrica piezas: acomoda las que ya existen. Por eso todos los símbolos son el mismo bloque, y lo que cambia es el hueco: el lugar exacto donde algo encaja. Cada hueco sale de lo que su agente hace según su SKILL.md, y el cian vive solo ahí: lo que hace cada agente es lo que brilla.</p>'
        f'<div class="fam cl">{fam_cl}</div><div class="fam os">{fam_os}</div></section>'
        f'<section><h2>Construcción</h2><div class="box cons">{cons}<ul><li>Lienzo de {ct["lienzo"]}; bloque {ct["bloque"]}, radio {ct["radio"]}.</li><li>Retícula de {ct["reticula"]}: los cortes caen en ella o en su mitad.</li><li>Canales de {ct["canal_min"]}, huecos de {ct["hueco_min"]} y círculos de radio {ct["circulo_r_min"]} como mínimo: siguen visibles a 16 px.</li><li>Tres cortes como máximo. Excepción: {ct["excepcion"]}.</li><li>Margen de respeto: la mitad del símbolo alrededor.</li></ul></div></section>'
        f'<section><h2>Los productos</h2>{prods}</section>'
        f'<section><h2>Color</h2><p>Tinta y un acento. El bloque siempre es neutro y el cian vive solo dentro del hueco. Su contraste se mide contra el bloque, que es lo que tiene alrededor.</p><div class="pal">{pal}</div><div class="box" style="margin-top:14px"><ol>{reglas}</ol></div></section>'
        '<section><h2>Tipografía</h2><div class="box type"><b>Bricolage Grotesque</b><p>700 para el nombre y 400 para el producto y el texto, la misma familia de Fruti Squad: los dos squads se leen como hermanos y el símbolo y el color los separan. Licencia SIL Open Font (Google Fonts). En las firmas va convertida a trazos.</p></div>'
        f'<div class="lks" style="margin-top:14px">{lockups}</div></section>'
        f'<section><h2>Usos incorrectos</h2><div class="nos">{malh}</div></section>'
        f'<section><h2>Kit de marketplace</h2><p>Portadas de 1200 × 630 (Open Graph) y 1280 × 640 (vista previa social de GitHub) para los nueve, iconos de app de 512 y 192 px, y textos cortos en español e inglés en <code>textos.md</code>.</p><div class="grid">{kitimgs}</div></section>'
        '</main>')
open(os.path.join(H, 'guia.html'), 'w').write(html); print('ok', len(jobs))
