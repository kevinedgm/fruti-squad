# NisaLab · color de áreas · r01 (propuesta). Uso: python3 gen.py → comparacion.html
# Método: OKLCH con luminosidad igual para las 8 y la intensidad máxima que admite cada tono en pantalla (tope 0.17); mismo tono que hoy.
import os, json, math, itertools, base64
D = os.path.dirname(os.path.abspath(__file__)); N = os.path.join(D, '..')
exec(open(os.path.join(D, 'oklch.py')).read())
A = json.load(open(os.path.join(N, 'nisalab-areas-final/tema.json')))['paleta']['areas']
H = {k: lch(v['hex'])[2] for k, v in A.items()}
def pal(L, cap=.17): return {k: tohex(L, min(maxc(L, h), cap) - .002, h) for k, h in H.items()}
OPC = [('Hoy', 'L 0.54 · intensidad 0.10–0.12', {k: v['hex'] for k, v in A.items()}),
       ('A · más intensos', 'Misma luz (0.54); cada tono a su intensidad máxima (tope 0.17).', pal(.54)),
       ('B · vivos', 'Luz 0.60; cada tono a su intensidad máxima (tope 0.17).', pal(.60))]
EST = {'conforme': '#2E7D32', 'alerta': '#8A6100', 'fuera': '#B42318'}
def svg(area, f, color):
    s = open(os.path.join(N, 'nisalab-areas-final/svg', area, f + '.svg')).read().replace(A[area]['hex'], color)
    return 'data:image/svg+xml;base64,' + base64.b64encode(s.encode()).decode()
def bloque(t, d, p):
    w = [cr('#FFFFFF', v) for v in p.values()]
    pares = min((de(p[a], p[b]), a, b) for a, b in itertools.combinations(p, 2))
    est = {(a, e): de(p[a], EST[e]) for a, e in (('agricolas', 'alerta'), ('ambiental', 'conforme'), ('alimentos', 'fuera'))}
    est_h = ''.join(f'<li class="{"bad" if v < 5 else ""}">{A[a]["nombre"]} frente a {e}: <b>{v:.1f}</b>{" · casi el mismo color" if v < 5 else ""}</li>' for (a, e), v in est.items())
    marcas = ''.join(f'<figure><img src="{svg(k, "marca", v)}" alt="" width="56" height="56"><figcaption>{A[k]["nombre"]}<code>{v}</code></figcaption></figure>' for k, v in p.items())
    chips = ''.join(f'<span class="chip"><i style="background:{v}"></i>{A[k]["nombre"]}</span>' for k, v in p.items())
    return f'''<section class="op"><header><h2>{t}</h2><p>{d}</p></header><div class="marcas">{marcas}</div>
<div class="enc" style="--ac:{p['aguas']}"><img src="{svg('aguas', 'marca', p['aguas'])}" alt="" width="40" height="40"><div><small>Recepción / Aguas</small><b>Recepción de muestras <span>Aguas</span></b></div></div>
<div class="chips">{chips}</div>
<ul class="dat"><li>Blanco sobre el color: <b>{min(w):.1f}–{max(w):.1f}:1</b> (el ícono es gráfico: mínimo 3:1)</li><li>Par de áreas más parecido: <b>{pares[0]:.1f}</b> ({A[pares[1]]["nombre"]} / {A[pares[2]]["nombre"]})</li>{est_h}</ul></section>'''
CSS = '''
/* Comparación vertical de tres paletas con piezas reales: marca, encabezado de área y filtros. Tema claro, como NisaLab. */
:root{--bg:#F2F4F8;--surface:#fff;--text:#141B33;--muted:#535B70;--border:#DFE3EC;--primary:#052A76;--bad:#B42318;--sans:"Poppins",system-ui,sans-serif;--mono:"Google Sans Code",ui-monospace,monospace;color-scheme:light}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 var(--sans)}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:24px 48px;display:grid;gap:20px}
h1{margin:0;font:700 clamp(26px,4vw,36px)/1.15 var(--sans);letter-spacing:-.02em}h1 span{font-weight:400}.intro{color:var(--muted);max-width:72ch;margin:0}
.op{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px;display:grid;gap:16px;min-width:0}
.op h2{margin:0;font:600 18px/1.3 var(--sans)}.op header p{margin:2px 0 0;color:var(--muted);font-size:14px}
.marcas{display:grid;grid-template-columns:repeat(auto-fill,minmax(118px,1fr));gap:12px}.marcas figure{margin:0;display:grid;justify-items:center;gap:4px;text-align:center;font-size:12.5px;line-height:1.3}
.marcas code{display:block;font:500 11.5px var(--mono);color:var(--muted)}
.enc{display:flex;gap:12px;align-items:center;padding:0 0 12px;border-bottom:3px solid var(--ac)}.enc small{display:block;color:var(--muted);font-size:12.5px}.enc b{font:600 18px var(--sans)}.enc b span{font-weight:400;color:var(--muted)}
.chips{display:flex;flex-wrap:wrap;gap:6px}.chip{display:inline-flex;gap:6px;align-items:center;min-height:32px;padding:0 10px;border:1px solid var(--border);border-radius:6px;font-size:13px}.chip i{width:10px;height:10px;border-radius:50%}
.dat{margin:0;padding-left:18px;display:grid;gap:2px;font-size:14px;color:var(--muted)}.dat b{color:var(--text);font-family:var(--mono);font-weight:500}.dat .bad,.dat .bad b{color:var(--bad)}
.rec{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:18px 20px;display:grid;gap:6px}.rec h2{margin:0;font:600 18px var(--sans)}.rec p{margin:0;color:var(--muted)}
'''
out = f'''<title>Áreas NisaLab · color</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Google+Sans+Code:wght@500&display=swap">
<style>{CSS}</style><script>document.documentElement.lang='es'</script>
<main class="wrap"><h1>Color de las áreas: <span>más vivos</span></h1>
<p class="intro">Mismos ocho tonos de hoy. Lo que cambia es cuánta intensidad lleva cada uno. Hoy comparten una intensidad baja, porque el verde azulado de Agave no admite más, y eso los acerca al gris. «Distancia» es la diferencia de color en OKLab ×100: por debajo de 5 dos colores se confunden.</p>
<div class="rec"><h2>Aprobada y aplicada: B (5 de noviembre de 2026)</h2><p>Es la única que separa Agrícolas del ámbar de alerta y Ambiental del verde de conforme. Costo: el blanco del ícono baja a 3.7–4.3:1; cumple porque el color de área nunca lleva texto (el nombre va en azul).</p></div>
{"".join(bloque(*o) for o in OPC)}
</main>'''
open(os.path.join(D, 'comparacion.html'), 'w').write(out)
print('ok', len(out) // 1024, 'KB')
