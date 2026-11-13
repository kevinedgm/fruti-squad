# SAM · identidad, ronda 5: tipografía del logotipo L3 y de la marca (color Voltaje, elegido 2026-11-13).
OSC, CLA, VO, VC, SEC = '#0a0a0b', '#f2f2ee', '#c6f432', '#3f6b0a', '#a3a3a8'
F = [
 ('A · Geist', "'Geist'", 800, 'normal', "'Geist'", 'Grotesca afilada y neutra, hecha para interfaces. Lo distintivo lo pone el corte, no la letra. Familia con monoespaciada propia (Geist Mono) para folios y datos.', "'Geist Mono'"),
 ('B · Unbounded', "'Unbounded'", 800, 'normal', "'Geist'", 'Ancha, de esquinas redondeadas, con aire futurista. La más llamativa; en textos largos cansa, así que solo va en el nombre y títulos grandes. El texto de la app queda en Geist.', "'Geist Mono'"),
 ('C · Archivo Expanded', "'Archivo'", 800, '125', "'Archivo'", 'Grotesca expandida y pesada, de cartel. Se siente industrial y contundente; el corte atraviesa más superficie de letra. El texto de la app usa la misma familia en ancho normal.', "'JetBrains Mono'"),
]
def cortado(fam, peso, ancho, fondo, tinta, acento, tam=96):
    up = 'polygon(0 0,100% 0,100% 38%,0 62%)'; dn = 'polygon(0 62%,100% 38%,100% 100%,0 100%)'
    st = f'font-family:{fam};font-weight:{peso};font-size:{tam}px;' + (f'font-stretch:{ancho}%;' if ancho != 'normal' else '')
    return (f'<div class="lock" style="background:{fondo}"><span class="cw" style="{st}"><span style="color:{acento};clip-path:{dn}">SAM</span>'
            f'<span style="color:{tinta};clip-path:{up};transform:translate(.055em,-.04em)">SAM</span></span></div>')
secs = ''
for t, fam, peso, ancho, tx, nota, mono in F:
    sw = f'font-stretch:{ancho}%;' if ancho != 'normal' else ''
    ej = (f'<div class="ej" style="font-family:{tx}"><p class="eti" style="font-family:{mono}">INC-2041 · ETAPA 2 DE 4</p>'
          f'<h3 style="font-family:{fam};font-weight:{peso};{sw}">Mis pendientes</h3>'
          f'<p>El reporte diario de atrasos no llegó a Discord. Revisé el webhook y la tarea programada; adjunto la evidencia del log.</p>'
          f'<p class="meta" style="font-family:{mono}">Asignado a Soporte técnico · vence 14 nov, 18:00</p></div>')
    secs += (f'<section><header><h2>{t}</h2><p>{nota}</p></header><div class="row">{cortado(fam, peso, ancho, OSC, CLA, VO)}{cortado(fam, peso, ancho, CLA, OSC, VC)}</div>'
             f'<div class="row">{ej}</div></section>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAM · ronda 5</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100,400;125,800&family=Geist:wght@400;800&family=Geist+Mono:wght@500&family=JetBrains+Mono:wght@500&family=Unbounded:wght@800&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.55 "Geist",system-ui,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:{SEC};max-width:74ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px}} header p{{margin:4px 0 0;max-width:84ch}}
.row{{display:flex;flex-wrap:wrap;gap:13px;align-items:center;margin-top:16px}}
.lock{{display:flex;align-items:center;padding:13px 34px;border:1px solid #26262b;border-radius:2px;height:130px;box-sizing:border-box}}
.cw{{display:inline-grid;line-height:1;letter-spacing:-.03em}} .cw>span{{grid-area:1/1}}
.ej{{max-width:560px;border:1px solid #26262b;border-radius:2px;padding:21px}} .ej h3{{font-size:34px;line-height:1.05;margin:4px 0 13px;letter-spacing:-.01em}}
.ej p{{margin:0 0 8px;font-size:16px}} .eti{{font-size:12px;letter-spacing:.06em;color:{VO}}} .meta{{font-size:13px;color:{SEC}}}
</style></head><body><main><h1>SAM · identidad, ronda 5 · tipografía</h1>
<p class="sub">Logotipo L3 (nombre cortado) en color Voltaje con tres tipografías. Abajo de cada una, cómo se vería un título y el texto de la app. Las tres son de Google Fonts, con licencia libre (OFL).</p>
{secs}</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
