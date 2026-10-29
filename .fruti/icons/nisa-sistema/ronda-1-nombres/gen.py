# Nisa Nabani · sistema de laboratorio · ronda 1: nombres del sistema
# Uso: python3 gen.py [carpeta-fuentes] → nombres.html
import os, sys

H = os.path.dirname(os.path.abspath(__file__))
AZ, PE, TINTA = '#052A76', '#C2D225', '#141B33'
N = [  # territorio, nombre, por qué, riesgo
    ('Familia Nisa', 'NisaLab', 'Dice de quién es y qué es en una palabra. Los productos se leen solos: Recepción NisaLab, Calidad NisaLab. Es tu propuesta.', '«Lab» es un sufijo muy usado: aporta claridad, no personalidad.'),
    ('Familia Nisa', 'Nabi', 'Ya lo conoce el equipo y viene de NABanI, igual que la marca madre. Corto y propio.', 'No dice «laboratorio»: el significado lo pone Nisa Nabani al lado.'),
    ('El laboratorio', 'Alícuota', 'La porción exacta de muestra que se analiza. Todo analista la entiende y casi ningún software la usa como nombre.', 'Cuatro sílabas y con acento; un cliente del laboratorio no la conoce.'),
    ('El laboratorio', 'Matraz', 'El matraz ya está dibujado en el logo de Nisa Nabani: el nombre y el símbolo cuentan lo mismo.', 'Suena a objeto, no a sistema; la z final se escribe mal con frecuencia.'),
    ('El laboratorio', 'Ensaya', 'Del ensayo de laboratorio, en forma de verbo: invita a hacer. Se pronuncia igual en todo el continente.', 'Puede leerse como «ensayo y error», no como certeza.'),
    ('El resultado', 'Fiel', 'El fiel es la aguja que marca el equilibrio en la balanza, y un resultado fiel es uno confiable.', 'Palabra común: difícil de registrar sola; necesita «de Nisa Nabani».'),
    ('El resultado', 'Certa', 'De certeza y certificado, lo que entrega el laboratorio. Breve y con sonido firme.', 'Nombre usado en otros sectores (no verificado a fondo).'),
    ('El resultado', 'Traza', 'Las trazas que detecta un análisis y la trazabilidad de cada muestra.', 'Ya existe TRAZiT, un LIMS español con la misma idea.'),
]

F = sys.argv[1] if len(sys.argv) > 1 else None
fonts = (''.join(f"@font-face{{font-family:Poppins;src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 600, 700)) if F else '')
link = '' if F else '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap">'

cards = ''.join(
    f'<article{" class=rec" if n == "NisaLab" else ""}><span class="t">{t}</span><div class="w">{n}</div>'
    f'<div class="lk"><span>Nisa Nabani</span> · {n}</div><div class="pr">Recepción {n} · Calidad {n}</div>'
    f'<p>{p}</p><p class="r"><b>Riesgo:</b> {r}</p></article>' for t, n, p, r in N)

html = f'''<title>Nombres del sistema Nisa</title>
<meta name="claude:viewport-fit-sides" content="cover">
{link}
<style>
/* Lámina de nombres: blanco, tinta y azul real de Nisa Nabani; Poppins como en el manual. */
{fonts}
:root{{--az:{AZ};--pe:{PE};--fg:{TINTA};--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:16px/1.55 Poppins,system-ui,sans-serif;padding-block:0 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1120px;margin:0 auto}} header{{padding:40px 0 22px;display:grid;gap:10px}}
.ov{{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}} h1{{margin:0;font:700 clamp(28px,5vw,44px)/1.1 Poppins,sans-serif;letter-spacing:-.02em}} p{{margin:0;max-width:72ch}}
.crit{{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin:6px 0 22px}} .crit div{{background:var(--sunk);border-radius:14px;padding:12px 14px;font-size:14px;line-height:1.4}} .crit b{{display:block}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}}
article{{border:1px solid var(--line);border-radius:18px;padding:18px;display:grid;gap:8px;align-content:start}} article.rec{{border:2px solid var(--az);box-shadow:inset 0 4px 0 var(--pe)}}
.t{{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}} .w{{font:700 36px/1.05 Poppins,sans-serif;color:var(--az);letter-spacing:-.02em}}
.lk{{font-size:14px;color:var(--muted)}} .lk span{{font-weight:700;color:var(--fg)}} .pr{{font-size:14px;font-weight:600;background:var(--sunk);border-radius:10px;padding:6px 10px}}
article p{{font-size:14px;line-height:1.5}} .r{{color:#8A1A12}} .r b{{font-weight:600}}
.rec-box{{background:var(--sunk);border-radius:18px;padding:18px 20px;margin-top:22px;display:grid;gap:8px}}
</style>
<main>
<header><span class="ov">Nisa Nabani · sistema de laboratorio · ronda 1 de nombres</span>
<h1>¿Cómo se llama el sistema?</h1>
<p class="muted" style="color:var(--muted)">El nombre del sistema es la palabra que acompaña a cada producto, como «Manik» en «Agenda Manik». Ocho opciones en cuatro territorios; la marcada es la recomendación.</p></header>
<div class="crit"><div><b>Dice qué es</b>Se entiende que es de laboratorio, o lo dice la marca madre al lado.</div><div><b>Se dice sin dudar</b>Se pronuncia y se escribe igual al oírlo.</div><div><b>Funciona con productos</b>«Recepción ___» se lee natural.</div><div><b>No choca</b>Sin otro software de laboratorio con el mismo nombre (búsqueda rápida, no revisión legal).</div></div>
<div class="g">{cards}</div>
<div class="rec-box"><b>Recomendación: NisaLab</b><p>Cumple los cuatro criterios: dice de quién es y qué es, se pronuncia sin dudas, los productos se leen solos y en una búsqueda rápida no apareció otro software de laboratorio con ese nombre. Lo que no da es personalidad; esa la pondrán el sello y la identidad visual. Si prefieres un nombre con más carácter, la alternativa es <b>Fiel</b>, que necesita «de Nisa Nabani» al lado.</p><p style="font-size:14px;color:var(--muted)">Antes de decidir: revisar el registro de marca en el IMPI y la disponibilidad del dominio. Eso no está hecho.</p></div>
</main>'''
open(os.path.join(H, 'nombres.html'), 'w').write(html)
print('ok')
