# GEMA · dirección visual de la interfaz, ronda 1 (2026-11-17). Marca fija: símbolo, degradado navy, Onest.
# Tres direcciones sobre la MISMA pantalla (lista de muestras + detalle) y los mismos datos ficticios.
import re
sym = open('../../final/gema-simbolo.svg').read(); sym = re.sub(r'<title>.*?</title>', '', sym)
SYM = sym[sym.index('>', sym.index('<svg')) + 1: sym.rindex('</svg>')]
n = [0]
def simb(z, tinta, a='#052A76', b='#3D67AE'):
    n[0] += 1; s = SYM.replace('gema-s', f'gs{n[0]}').replace('currentColor', tinta).replace('var(--gema-pico-a,#052A76)', a).replace('var(--gema-pico-b,#3D67AE)', b)
    return f'<svg viewBox="0 0 48 48" width="{z}" height="{z}" aria-hidden="true">{s}</svg>'
M = [('M-2026-1184', 'Agua residual · planta norte', 'Purificadora del Valle', 'Aguas', 'DBO₅ · SST · pH', 'en', 'En análisis', 'Hoy 18:00'),
     ('M-2026-1185', 'Mezcal joven · lote 0711', 'Destilería Las Lomas', 'Bebidas alcohólicas', 'Metanol · grado alcohólico', 'no', 'No cumple', '18 nov'),
     ('M-2026-1186', 'Suelo agrícola · parcela 3', 'Agroinsumos del Sur', 'Agrícolas', 'pH · materia orgánica', 'rec', 'Recibida', '20 nov'),
     ('M-2026-1187', 'Mole en pasta · lote 22', 'Cocina Tradicional MX', 'Alimentos', 'Humedad · aflatoxinas', 'si', 'Cumple', 'Entregado'),
     ('M-2026-1188', 'Agua potable · pozo 2', 'Municipio de San Pedro', 'Aguas', 'Coliformes · cloro residual', 'rev', 'En revisión', '19 nov')]
RES = [('DBO₅', '18.4 mg/L', '≤ 30 mg/L', 'si'), ('SST', '22.0 mg/L', '≤ 40 mg/L', 'si'), ('pH', '—', '6.5 – 8.5', 'en')]
def estado(k, t, d):
    return f'<span class="st st-{k}">{"✓ " if k=="si" else "✕ " if k=="no" else ""}{t}</span>'
def tabla(d):
    rows = ''.join(f'<tr class="{"sel" if i==0 else ""}"><td><span class="fol">{f}</span><b>{nom}</b><span class="cli">{cli}</span></td><td class="h-md">{tipo}</td><td class="h-lg">{par}</td><td>{estado(k,e,d)}</td><td class="n">{v}</td></tr>'
                   for i, (f, nom, cli, tipo, par, k, e, v) in enumerate(M))
    return f'<table class="tbl"><thead><tr><th>Muestra</th><th class="h-md">Tipo</th><th class="h-lg">Análisis</th><th>Estado</th><th class="n">Vence</th></tr></thead><tbody>{rows}</tbody></table>'
def detalle():
    r = ''.join(f'<tr><td>{p}</td><td class="n val">{v}</td><td class="lim">{l}</td><td>{estado(k, "Cumple" if k=="si" else "En análisis", 0)}</td></tr>' for p, v, l, k in RES)
    return (f'<aside class="det"><span class="fol">M-2026-1184</span><h3>Agua residual · planta norte</h3><p class="cli">Purificadora del Valle · recibida 12 nov, 09:40 · Oaxaca</p>'
            f'<table class="res"><thead><tr><th>Parámetro</th><th class="n">Valor</th><th>Límite</th><th>Dictamen</th></tr></thead><tbody>{r}</tbody></table>'
            f'<div class="acc"><button class="pri">Capturar resultado</button><button class="sec">Ver orden</button></div></aside>')
NAV = ['Recepción', 'Análisis', 'Informes', 'Cotizaciones', 'Cobranza', 'Compras']
def pantalla(d, nav_lateral, tinta_logo, a, b):
    navh = ''.join(f'<a class="{"on" if x=="Recepción" else ""}">{x}</a>' for x in NAV)
    if nav_lateral:
        shell = (f'<div class="app lateral"><nav class="side"><div class="logo">{simb(26, tinta_logo, a, b)}<b>GEMA</b></div>{navh}<div class="suc">Sucursal<br><b>Oaxaca</b></div></nav>'
                 f'<main><header class="pg"><div><h2>Muestras</h2><p>128 abiertas · 9 vencen hoy</p></div><button class="pri">Registrar muestra</button></header>'
                 f'<div class="filtros"><span class="chip on">Todas</span><span class="chip">Aguas</span><span class="chip">Bebidas</span><span class="chip">Alimentos</span><span class="chip">Agrícolas</span><span class="buscar">Buscar folio o cliente</span></div>'
                 f'<div class="cuerpo">{tabla(d)}{detalle()}</div></main></div>')
    else:
        shell = (f'<div class="app"><header class="top"><div class="logo">{simb(26, tinta_logo, a, b)}<b>GEMA</b></div><nav>{navh}</nav><span class="suc">Oaxaca</span></header>'
                 f'<main><header class="pg"><div><h2>Muestras</h2><p>128 abiertas · 9 vencen hoy</p></div><button class="pri">Registrar muestra</button></header>'
                 f'<div class="filtros"><span class="chip on">Todas</span><span class="chip">Aguas</span><span class="chip">Bebidas</span><span class="chip">Alimentos</span><span class="chip">Agrícolas</span><span class="buscar">Buscar folio o cliente</span></div>'
                 f'<div class="cuerpo">{tabla(d)}{detalle()}</div></main></div>')
    return shell
BASE = '''
.dir{font-family:'Onest',system-ui,sans-serif;margin-top:16px;overflow:hidden}
.dir *{box-sizing:border-box} .dir b{font-weight:600}
.dir .app{min-height:640px} .dir .logo{display:flex;align-items:center;gap:8px} .dir .logo b{font-size:19px;font-weight:700}
.dir .fol{display:block;font:500 12px 'JetBrains Mono',monospace} .dir .cli{display:block;font-size:13px}
.dir .tbl,.dir .res{width:100%;border-collapse:collapse;font-size:14px} .dir th{text-align:left;font-weight:600;font-size:12px} .dir .n{text-align:right;white-space:nowrap}
.dir .tbl td b{display:block} .dir button{font:600 14px 'Onest';border:0;cursor:pointer;min-height:40px;padding:0 16px}
.dir .val{font-family:'JetBrains Mono',monospace;font-variant-numeric:tabular-nums}
.dir .st{font-size:12px;font-weight:600;padding:2px 9px;border-radius:999px;white-space:nowrap;display:inline-block}
.dir .filtros{display:flex;gap:8px;align-items:center;flex-wrap:wrap} .dir .chip{font-size:13px;padding:6px 12px;border-radius:999px}
.dir .buscar{margin-left:auto;font-size:13px;padding:8px 12px;min-width:220px}
.dir .cuerpo{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(0,1fr);gap:16px;align-items:start}
.dir .det h3{margin:2px 0 2px;font-size:20px} .dir .det .acc{display:flex;gap:8px;margin-top:16px}
.dir .pg{display:flex;justify-content:space-between;align-items:flex-end;gap:16px} .dir .pg h2{margin:0} .dir .pg p{margin:2px 0 0;font-size:14px}
'''
CSS = {
'a': '''
/* A · Bata de laboratorio: papel, líneas finas, aire; el navy solo en acciones. */
.dir-a{background:#f7f7f4;color:#0a0a0b;border:1px solid #d6d6d0}
.dir-a .top{display:flex;align-items:center;gap:32px;padding:14px 32px;background:#ffffff;border-bottom:1px solid #e3e3de}
.dir-a .top nav{display:flex;gap:4px} .dir-a .top nav a{font-size:14px;font-weight:500;color:#55555c;padding:8px 10px;border-bottom:2px solid transparent}
.dir-a .top nav a.on{color:#0a0a0b;border-bottom-color:#052A76} .dir-a .top .suc{margin-left:auto;font-size:13px;color:#55555c}
.dir-a main{padding:32px;display:grid;gap:20px} .dir-a .pg h2{font-size:30px;letter-spacing:-.01em} .dir-a .pg p{color:#55555c}
.dir-a .pri{background:#052A76;color:#fff;border-radius:6px} .dir-a .sec{background:#fff;color:#0a0a0b;border-radius:6px;box-shadow:inset 0 0 0 1.5px #7a7a82}
.dir-a .chip{color:#0a0a0b;box-shadow:inset 0 0 0 1px #d6d6d0;background:#fff} .dir-a .chip.on{background:#0a0a0b;color:#fff;box-shadow:none}
.dir-a .buscar{background:#fff;border-radius:6px;box-shadow:inset 0 0 0 1.5px #7a7a82;color:#55555c}
.dir-a .tbl{background:#fff;border:1px solid #e3e3de;border-radius:10px} .dir-a .tbl th{color:#55555c;padding:12px 14px;border-bottom:1px solid #e3e3de}
.dir-a .tbl td{padding:14px;border-bottom:1px solid #eeeeea;vertical-align:top} .dir-a .tbl tr.sel td{background:#f0f3fa} .dir-a .tbl tr.sel td:first-child{box-shadow:inset 3px 0 0 #052A76}
.dir-a .fol,.dir-a .cli{color:#55555c} .dir-a .det{background:#fff;border:1px solid #e3e3de;border-radius:10px;padding:20px}
.dir-a .res th{color:#55555c;padding:8px 6px 8px 0;border-bottom:1px solid #e3e3de} .dir-a .res td{padding:10px 6px 10px 0;border-bottom:1px solid #eeeeea} .dir-a .lim{color:#55555c}
.dir-a .st-en{background:#052A76;color:#fff} .dir-a .st-rec,.dir-a .st-rev{box-shadow:inset 0 0 0 1px #7a7a82;color:#0a0a0b} .dir-a .st-si{color:#0a0a0b;padding-left:0} .dir-a .st-no{color:#b42318;box-shadow:inset 0 0 0 1px #b42318}
''',
'b': '''
/* B · Instrumento: barra lateral navy, densidad alta, valores en mono protagonistas, retícula visible. */
.dir-b{background:#eef0f4;color:#0b1220;border:1px solid #cfd5e0}
.dir-b .lateral{display:grid;grid-template-columns:200px minmax(0,1fr)}
.dir-b .side{background:linear-gradient(180deg,#0a2a6e,#052A76);color:#dfe7f7;padding:16px 12px;display:flex;flex-direction:column;gap:2px}
.dir-b .side .logo{color:#fff;margin:0 6px 18px} .dir-b .side a{font-size:13px;font-weight:500;padding:8px 10px;border-radius:4px;color:#c3d0ea}
.dir-b .side a.on{background:rgba(255,255,255,.12);color:#fff;box-shadow:inset 3px 0 0 #7aa2f0} .dir-b .side .suc{margin-top:auto;font-size:12px;color:#a9b6d6;padding:10px}
.dir-b .side .suc b{color:#fff;font-size:14px}
.dir-b main{padding:16px 20px;display:grid;gap:12px} .dir-b .pg h2{font-size:20px} .dir-b .pg p{color:#4a5674}
.dir-b .pri{background:#052A76;color:#fff;border-radius:4px;min-height:36px} .dir-b .sec{background:#fff;color:#0b1220;border-radius:4px;box-shadow:inset 0 0 0 1px #8a94a8;min-height:36px}
.dir-b .chip{border-radius:4px;background:#fff;box-shadow:inset 0 0 0 1px #cfd5e0;color:#0b1220;padding:4px 10px} .dir-b .chip.on{background:#0b1220;color:#fff;box-shadow:none}
.dir-b .buscar{background:#fff;border-radius:4px;box-shadow:inset 0 0 0 1px #8a94a8;color:#4a5674;padding:6px 10px}
.dir-b .tbl{background:#fff;border:1px solid #cfd5e0} .dir-b .tbl th{background:#f5f7fa;color:#4a5674;padding:7px 10px;border-bottom:1px solid #cfd5e0;text-transform:uppercase;letter-spacing:.04em;font-size:11px}
.dir-b .tbl td{padding:7px 10px;border-bottom:1px solid #e3e7ee;border-right:1px solid #f0f2f6;font-size:13px} .dir-b .tbl tr.sel td{background:#e6edf9}
.dir-b .tbl td b{font-size:13px} .dir-b .cli{font-size:12px} .dir-b .fol,.dir-b .cli{color:#4a5674}
.dir-b .det{background:#fff;border:1px solid #cfd5e0;padding:14px} .dir-b .det h3{font-size:16px}
.dir-b .res th{background:#f5f7fa;color:#4a5674;padding:6px 8px;font-size:11px;text-transform:uppercase;letter-spacing:.04em} .dir-b .res td{padding:7px 8px;border-bottom:1px solid #e3e7ee;font-size:13px}
.dir-b .val{font-size:15px;font-weight:600;color:#052A76} .dir-b .lim{color:#4a5674;font-family:'JetBrains Mono',monospace;font-size:12px}
.dir-b .st{border-radius:3px} .dir-b .st::before{content:"";display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:6px;background:currentColor;vertical-align:1px}
.dir-b .st-en{color:#052A76;background:#e6edf9} .dir-b .st-rec,.dir-b .st-rev{color:#4a5674;background:#eef0f4} .dir-b .st-si{color:#0b1220;background:#eef0f4} .dir-b .st-no{color:#b42318;background:#fdecea}
.dir-b .st-si::before,.dir-b .st-no::before{display:none}
''',
'c': '''
/* C · Capas: banda de marca con el degradado, tarjetas que flotan con sombra suave, radios generosos, más cálida. */
.dir-c{background:#eef1f6;color:#0a0a0b;border:1px solid #d6dbe4}
.dir-c .top{display:flex;align-items:center;gap:28px;padding:14px 28px 64px;background:linear-gradient(120deg,#3D67AE,#052A76 70%);color:#fff}
.dir-c .top nav{display:flex;gap:4px} .dir-c .top nav a{font-size:14px;font-weight:500;color:#c9d5ef;padding:8px 12px;border-radius:999px} .dir-c .top nav a.on{background:rgba(255,255,255,.16);color:#fff}
.dir-c .top .suc{margin-left:auto;font-size:13px;background:rgba(255,255,255,.14);padding:6px 12px;border-radius:999px}
.dir-c main{padding:0 28px 28px;margin-top:-48px;display:grid;gap:16px}
.dir-c .pg{background:#fff;border-radius:16px;padding:20px 22px;box-shadow:0 1px 2px rgba(5,42,118,.06),0 8px 24px rgba(5,42,118,.08)} .dir-c .pg h2{font-size:26px} .dir-c .pg p{color:#55555c}
.dir-c .pri{background:#052A76;color:#fff;border-radius:10px;min-height:44px} .dir-c .sec{background:#eef1f6;color:#0a0a0b;border-radius:10px}
.dir-c .chip{background:#fff;color:#0a0a0b;box-shadow:0 1px 2px rgba(5,42,118,.08)} .dir-c .chip.on{background:#052A76;color:#fff}
.dir-c .buscar{background:#fff;border-radius:10px;color:#55555c;box-shadow:inset 0 0 0 1.5px #7a7a82}
.dir-c .tbl{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 1px 2px rgba(5,42,118,.06),0 8px 24px rgba(5,42,118,.08);border-collapse:separate;border-spacing:0}
.dir-c .tbl th{color:#55555c;padding:14px 16px;border-bottom:1px solid #eceff4} .dir-c .tbl td{padding:14px 16px;border-bottom:1px solid #f1f3f7} .dir-c .tbl tr.sel td{background:#eef3fc}
.dir-c .fol,.dir-c .cli{color:#55555c} .dir-c .det{background:#fff;border-radius:16px;padding:22px;box-shadow:0 1px 2px rgba(5,42,118,.06),0 8px 24px rgba(5,42,118,.08)}
.dir-c .res th{color:#55555c;padding:8px 6px 8px 0;border-bottom:1px solid #eceff4} .dir-c .res td{padding:10px 6px 10px 0;border-bottom:1px solid #f1f3f7} .dir-c .lim{color:#55555c}
.dir-c .st-en{background:#052A76;color:#fff} .dir-c .st-rec,.dir-c .st-rev{background:#eef1f6;color:#0a0a0b} .dir-c .st-si{color:#0a0a0b;padding-left:0} .dir-c .st-no{background:#fdecea;color:#b42318}
'''}
INFO = [('a', 'A · Bata de laboratorio', 'Claro, limpio y con aire, como una hoja de resultados bien impresa. Fondos papel, líneas finas en lugar de sombras, navegación arriba y el navy solo en la acción principal y en «En análisis».',
         'Sostiene: lectura tranquila, informe y calidad. Sacrifica: densidad; caben menos filas por pantalla.', False, '#0a0a0b'),
        ('b', 'B · Instrumento', 'Como el software de un equipo de laboratorio: barra lateral navy con el degradado, filas compactas, encabezados en mayúsculas, valores en mono como protagonistas y estados con indicador de luz.',
         'Sostiene: mucho dato a la vista, uso de todo el día en recepción y captura. Sacrifica: calidez; se siente más técnico y frío.', True, '#ffffff'),
        ('c', 'C · Capas', 'Una banda de marca con el degradado arriba y tarjetas blancas que flotan encima con sombra suave; radios más redondos y botones grandes. La más cercana y moderna.',
         'Sostiene: sensación de producto actual y amable. Sacrifica: espacio vertical (la banda) y sobriedad; las sombras suman peso visual.', False, '#ffffff')]
secs = ''
for k, t, idea, trade, lat, tinta in INFO:
    a, b = ('#7aa2f0', '#8fb3ff') if tinta == '#ffffff' else ('#052A76', '#3D67AE')
    secs += f'<section><h2>{t}</h2><p>{idea}</p><p class="fn">{trade}</p><div class="dir dir-{k}">{pantalla(k, lat, tinta, a, b)}</div></section>'
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GEMA · dirección visual</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<style>body{{margin:0;background:#0a0a0b;color:#f2f2ee;font:15px/1.55 'Onest',system-ui,sans-serif}} main.w{{max-width:1240px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;margin:0 0 8px}} .sub{{margin:0 0 30px;color:#a3a3a8;max-width:86ch}} section{{margin-bottom:40px}} section>h2{{margin:0;font-size:24px}} section>p{{margin:4px 0 0;max-width:96ch}} .fn{{color:#a3a3a8;font-size:14px}}
{BASE}{"".join(CSS.values())}</style></head><body><main class="w"><h1>GEMA · dirección visual de la interfaz · ronda 1</h1>
<p class="sub">Marca fija (símbolo, degradado navy, Onest). Tres direcciones para la interfaz sobre la misma pantalla —lista de muestras con el detalle de una— y los mismos datos ficticios. Se compara cómo se siente y cuánto cabe, no el contenido.</p>
{secs}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
