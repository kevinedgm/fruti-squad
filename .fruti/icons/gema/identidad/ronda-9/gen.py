# GEMA · ronda 9: tipografía con símbolo R1 y color N2 (degradado navy) congelados por el usuario el 2026-11-17.
# Criterio: la misma letra en marca e interfaz; legible a 13–15 px; números, decimales, unidades y subíndices claros (DBO₅, mg/L).
NAVY, AZUL, CLA, BL, OSC, SEC = '#052A76', '#3D67AE', '#f2f2ee', '#ffffff', '#0a0a0b', '#a3a3a8'
r1 = open('../ronda-5/r1-pantalla.svg').read(); inner = r1[r1.index('>', r1.index('<svg')) + 1: r1.rindex('</svg>')]
n = [0]
def simb(z, tinta, a=NAVY, b=AZUL):
    n[0] += 1; g = f'g{n[0]}'
    return (f'<svg viewBox="0 0 48 48" width="{z}" height="{z}" aria-hidden="true"><defs><linearGradient id="{g}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{b}"/><stop offset="1" stop-color="{a}"/></linearGradient></defs>'
            + inner.replace('currentColor', tinta).replace('var(--g-color-brand,#38bdf8)', f'url(#{g})') + '</svg>')
F = [
 ('A · Onest', 'Onest', 'JetBrains Mono', 'La de SAM. Las dos herramientas internas compartirían letra y se sentirían de la misma familia. Clara, con números bien diferenciados.'),
 ('B · IBM Plex Sans', 'IBM Plex Sans', 'IBM Plex Mono', 'Hecha para entornos técnicos e industriales: distingue I, l y 1, y O y 0; tiene subíndices y su propia monoespaciada para folios y valores. La más «instrumento».'),
 ('C · Instrument Sans', 'Instrument Sans', 'JetBrains Mono', 'La letra de Grana, la librería de la interfaz. Compacta: caben más filas de resultados por pantalla.'),
]
FIL = [('M-2026-1184', 'Agua residual · planta norte', 'DBO₅', '18.4 mg/L', 'Cumple'), ('M-2026-1185', 'Mezcal joven · lote 0711', 'Metanol', '196 mg/100 mL A.A.', 'Cumple'),
       ('M-2026-1186', 'Suelo agrícola · parcela 3', 'pH', '7.21', 'En análisis')]
def pantalla(fam, mono, fondo, sup, tinta, sec, linea, claro):
    rows = ''.join(f'<tr style="border-color:{linea}"><td><span class="fol" style="font-family:\'{mono}\';color:{sec}">{f}</span><br><b>{m}</b></td><td>{p}</td><td class="n" style="font-family:\'{mono}\'">{v}</td>'
                   f'<td><span class="chip" style="{("background:"+NAVY+";color:#fff") if claro else ("background:"+AZUL+";color:#fff")}">{e}</span></td></tr>' if e == 'En análisis' else
                   f'<tr style="border-color:{linea}"><td><span class="fol" style="font-family:\'{mono}\';color:{sec}">{f}</span><br><b>{m}</b></td><td>{p}</td><td class="n" style="font-family:\'{mono}\'">{v}</td><td><span class="ok" style="color:{tinta}">✓ {e}</span></td></tr>'
                   for f, m, p, v, e in FIL)
    return (f'<div class="pan" style="background:{fondo};color:{tinta};font-family:\'{fam}\';border-color:{linea}"><div class="bar" style="border-color:{linea}">{simb(26, tinta, *( (NAVY, AZUL) if claro else (AZUL, "#7aa2f0") ))}<b>GEMA</b></div>'
            f'<h3>Resultados del día</h3><p style="color:{sec};margin:0 0 10px">3 muestras · Oaxaca</p>'
            f'<table><thead><tr style="color:{sec}"><th>Muestra</th><th>Parámetro</th><th class="n">Valor</th><th>Estado</th></tr></thead><tbody>{rows}</tbody></table>'
            f'<button style="background:{NAVY if claro else AZUL};color:#fff">Registrar muestra</button></div>')
secs = ''
for t, fam, mono, nota in F:
    lk = (f'<div class="lock" style="background:{CLA};color:{OSC};font-family:\'{fam}\'">{simb(56, OSC)}<span><span class="wm">GEMA</span><span class="desc" style="color:#3a3a40">Gestión de Muestras y Análisis</span></span></div>'
          f'<div class="lock" style="background:{OSC};color:{CLA};font-family:\'{fam}\'">{simb(56, CLA, AZUL, "#7aa2f0")}<span><span class="wm">GEMA</span><span class="desc" style="color:{SEC}">Gestión de Muestras y Análisis</span></span></div>')
    prueba = f'<p class="pr" style="font-family:\'{fam}\'">Il1 · O0 · rn m · 0.05 mg/L · DBO₅ · 14:05 · ñ á</p>'
    secs += (f'<section><h2 style="font-family:\'{fam}\'">{t}</h2><p>{nota}</p><div class="row">{lk}</div>'
             f'<div class="row al">{pantalla(fam, mono, CLA, BL, OSC, "#55555c", "#d6d6d0", True)}{pantalla(fam, mono, OSC, "#16161a", CLA, SEC, "#2a2a30", False)}</div>{prueba}</section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GEMA · ronda 9</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 'Onest',system-ui,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:{SEC};max-width:82ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:24px}} section>p{{margin:4px 0 0;max-width:88ch}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:16px}} .row.al{{align-items:flex-start}}
.lock{{display:flex;align-items:center;gap:12px;padding:14px 24px 14px 14px;border:1px solid #26262b;border-radius:2px}}
.wm{{display:block;font-weight:700;font-size:40px;line-height:1}} .desc{{display:block;font-size:14px;font-weight:500;margin-top:4px}}
.pan{{width:520px;max-width:100%;border:1px solid;border-radius:10px;padding:0 0 16px}} .bar{{display:flex;gap:8px;align-items:center;padding:10px 14px;border-bottom:1px solid}} .bar b{{font-size:18px;font-weight:700}}
.pan h3{{margin:14px 14px 2px;font-size:22px;font-weight:700}} .pan>p{{padding:0 14px}}
table{{width:calc(100% - 28px);margin:0 14px;border-collapse:collapse;font-size:14px}} th{{text-align:left;font-weight:600;font-size:12px;padding:6px 6px 6px 0}} td{{padding:8px 6px 8px 0;vertical-align:top}}
tr{{border-bottom:1px solid}} thead tr{{border-bottom:0}} .n{{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}} td b{{font-weight:600}}
.fol{{font-size:12px}} .chip{{font-size:12px;font-weight:600;padding:2px 9px;border-radius:999px;white-space:nowrap}} .ok{{font-size:13px;font-weight:600;white-space:nowrap}}
.pan button{{margin:14px 14px 0;font:inherit;font-weight:600;font-size:15px;border:0;border-radius:6px;min-height:44px;padding:0 18px}}
.pr{{font-size:15px;margin-top:14px}}
</style></head><body><main><h1>GEMA · identidad, ronda 9 · tipografía</h1>
<p class="sub">Símbolo R1 y color N2 (degradado navy) elegidos. Tres letras probadas en el logotipo y en una pantalla de resultados, con folios, parámetros, unidades, decimales y subíndices. Datos ficticios.</p>
{secs}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
