# Xila · rediseño · ronda 6 · color (usuario: «los colores que me presentaste no me gustaron»). Cinco paletas de textiles y artesanías de Oaxaca.
# python3 gen.py -> banco.html
import os
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D,'..','rediseno-r5','gen.py')).read().split('PAL = [')[0]
ns = {'__file__': os.path.join(D,'..','rediseno-r5','gen.py')}; exec(src, ns)
niveles, palabra, sv, grafica, cr = ns['niveles'], ns['palabra'], ns['sv'], ns['grafica'], ns['cr']
PAL = [
 ('istmo', 'Terciopelo del Istmo', 'Las flores bordadas del traje de tehuana sobre terciopelo negro: rosa mexicano, amarillo y verde.',
  dict(fondo='#141414', x='#F7C531', rombo='#E5007E', centro='#22B07D', g_fondo='#FAF6EE', g_gris='#C2BDB3', g_dato='#C2006B', g_txt='#141414'),
  ['#141414', '#E5007E', '#F7C531', '#22B07D', '#FAF6EE'], [('#E5007E', '#141414'), ('#F7C531', '#141414'), ('#22B07D', '#141414')]),
 ('barro', 'Barro negro', 'El barro negro bruñido de San Bartolo Coyotepec: grafito con brillo de plata y un solo punto de color, turquesa.',
  dict(fondo='#1E1E20', x='#C9CCD1', rombo='#7C8088', centro='#2EC4C4', g_fondo='#F4F4F2', g_gris='#C7C9CC', g_dato='#0E8A8A', g_txt='#1E1E20'),
  ['#1E1E20', '#7C8088', '#C9CCD1', '#2EC4C4', '#F4F4F2'], [('#C9CCD1', '#1E1E20'), ('#7C8088', '#1E1E20'), ('#2EC4C4', '#1E1E20')]),
 ('tapete', 'Tapete de Teotitlán', 'Los tintes naturales de los tapetes de lana de Teotitlán del Valle: añil, musgo y cempasúchil sobre lana cruda.',
  dict(fondo='#EFE6D2', x='#2B3A67', rombo='#9C5E12', centro='#5E7A2E', borde='#D9CDB2', g_fondo='#EFE6D2', g_gris='#C3B89F', g_dato='#2B3A67', g_txt='#2B3A67'),
  ['#EFE6D2', '#2B3A67', '#5E7A2E', '#9C5E12', '#3A2E22'], [('#2B3A67', '#EFE6D2'), ('#9C5E12', '#EFE6D2'), ('#5E7A2E', '#EFE6D2')]),
 ('mazateco', 'Huipil mazateco', 'El huipil de Huautla: manta blanca con pájaros y flores bordados en rosa y verde loro.',
  dict(fondo='#FBF8F3', x='#2E8540', rombo='#D6336C', centro='#D6336C', borde='#E6DED1', g_fondo='#FBF8F3', g_gris='#CFC8BC', g_dato='#C4285C', g_txt='#1F2A22'),
  ['#FBF8F3', '#D6336C', '#2E8540', '#1F2A22', '#F3C7D6'], [('#D6336C', '#FBF8F3'), ('#2E8540', '#FBF8F3')]),
 ('anil', 'Añil', 'Un solo tinte, el añil, en tres intensidades sobre manta: sobrio, editorial y fácil de sostener en una librería de gráficas.',
  dict(fondo='#16255C', x='#F4F1EA', rombo='#7FA0E0', centro='#F4F1EA', g_fondo='#F4F1EA', g_gris='#C4C6CF', g_dato='#16255C', g_txt='#16255C'),
  ['#16255C', '#2F4FA8', '#7FA0E0', '#C9D6F2', '#F4F1EA'], [('#F4F1EA', '#16255C'), ('#7FA0E0', '#16255C')]),
]
def tarj(k, n, txt, P, sw, pares):
    lv = niveles(P); claro = P.get('borde') is not None
    oscuro = P['fondo'] if not claro else P['x']
    dot = P['centro']
    crs = ' · '.join(f'{a} sobre {b}: {cr(a, b):.1f}:1' for a, b in pares)
    return f'''<article class="c"><header><h3>{n}</h3><p>{txt}</p></header>
<div class="sws">{''.join(f'<i style="background:{c}" title="{c}"></i>' for c in sw)}</div>
<div class="fam">{''.join(f'<span>{sv(s, t)}<small>{t} px</small></span>' for s, t in zip(lv, [96, 48, 24, 16]))}</div>
<div class="port" style="background:{oscuro}">{sv(lv[0], 70)}{palabra(42, P['g_fondo'], P['rombo'] if not claro else P['rombo'])}</div>
<div class="port" style="background:{P['g_fondo']};border:1px solid var(--line)">{sv(lv[0], 56)}{palabra(34, P['g_txt'], P['rombo'])}</div>
{grafica(P)}<p class="cr">{crs}</p></article>'''
HTML = f'''<title>Xila · Rediseño r6</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600&family=Fraunces:opsz,wght@9..144,600&display=swap">
<style>
/* Cinco paletas lado a lado: muestras, los cuatro dibujos, portada oscura y clara con el nombre, y una gráfica con el dato en el color de marca */
:root{{--bg:#efebe3;--fg:#15171f;--muted:#5b5f6e;--line:#dcd6ca;--card:#fffdf9;--f:'Instrument Sans',ui-sans-serif,system-ui,sans-serif;--d:'Fraunces',Georgia,serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111218;--fg:#f0ece4;--muted:#a9adbd;--line:#2c2f3b;--card:#1b1d27;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1240px;margin:0 auto;display:grid;gap:28px}} h1{{font:600 clamp(32px,5vw,52px)/1.05 var(--d);margin:0;text-wrap:balance}}
.intro{{display:grid;gap:12px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}} .ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.tres{{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:16px}}
.c{{display:grid;gap:12px;padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;align-content:start;min-width:0}} .c header{{display:grid;gap:4px}} .c h3{{margin:0;font:600 23px var(--d)}} .c p{{margin:0;font-size:14.5px}}
.cr{{color:var(--muted);font-size:12.5px!important;font-variant-numeric:tabular-nums}}
.sws{{display:flex;gap:0;border-radius:10px;overflow:hidden;height:34px;border:1px solid var(--line)}} .sws i{{flex:1}}
.fam{{display:flex;gap:14px;align-items:flex-end;padding:14px;border-radius:12px;background:#ffffff;border:1px solid var(--line);flex-wrap:wrap}} .fam span{{display:grid;justify-items:center;gap:4px}} .fam small{{font-size:12px;color:#5b5f6e}}
.port{{display:flex;gap:14px;align-items:center;padding:16px;border-radius:12px;min-width:0;flex-wrap:wrap}}
</style>
<div class="w"><div class="intro"><p class="ojo">Rediseño · ronda 6 · color</p><h1>Xila: cinco hilos de Oaxaca</h1>
<p>Cada paleta sale de un textil o una artesanía concreta de Oaxaca, para que el color tenga historia propia y no sea solo «azul y naranja». Se prueban igual que antes: los cuatro dibujos, portada oscura y clara con el nombre bordado, y una gráfica con el dato en el color de marca. La letra se decide después.</p></div>
<div class="tres">{''.join(tarj(*p) for p in PAL)}</div></div>'''
open(os.path.join(D,'banco.html'),'w').write(HTML); print('ok')
