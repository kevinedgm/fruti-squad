# Directorio Manik · nombre nuevo · r01 (familia del lema, con «Manik»).
# Pedido (2026-11-05): «Manik» solo no se puede registrar como marca; explorar la familia del lema («Tu médico, a la mano»),
# debe llevar «Manik»; se mencionó «Dr. Manik». Uso: python3 gen.py → nombres.html
# Logotipo: misma construcción que el vigente (Sora 600, −0.04 em, minúsculas, junto al pin). Colores del DS del directorio.
import os, base64, json, html
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
uri = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
PIN = uri('manik-final/svg/simbolo.svg'); ICONO = uri('manik-final/svg/app-icon.svg')
T = {x['name']: x['value'] for x in json.load(open(os.path.join(M, 'directorio-ds/project/tokens.json')))['color']['tokens']}

# (clave, piezas del logotipo [(texto, peso)], cómo se dice, frase de uso, del lema, distintivo, riesgos)
N = [
 ('manik-a-la-mano', [('manik', 600), (' a la mano', 300)], 'Manik a la Mano', 'Agenda con Manik a la Mano',
  'Literal: es el lema hecho nombre; conserva la mano de Manik\'.', 'Media-alta: la frase completa da una impresión distinta a «Manik».',
  'Largo (15 letras); la gente lo acortará a «Manik» al hablar.'),
 ('tu-manik', [('tu ', 300), ('manik', 600)], 'Tu Manik', 'Busca en Tu Manik',
  'Toma el «Tu» del lema: cercano y corto.', 'Baja-media: «tu» es una palabra común; el peso sigue en «Manik».',
  'Puede tener el mismo problema que «Manik» solo.'),
 ('manik-cerca', [('manik', 600), (' cerca', 300)], 'Manik Cerca', 'Encuéntralo en Manik Cerca',
  'Del «cerca de ti» de la leyenda del inicio.', 'Media: «cerca» describe una cualidad, no el servicio.',
  'Puede leerse como «hay un Manik cerca».'),
 ('manik-contigo', [('manik', 600), (' contigo', 300)], 'Manik Contigo', 'Agenda con Manik Contigo',
  'La cercanía del lema dicha como compañía.', 'Media: frase con sentido propio.',
  'Suena a programa de apoyo o aseguradora más que a buscador.'),
 ('manik-aqui', [('manik', 600), (' aquí', 300)], 'Manik Aquí', 'Tu médico está en Manik Aquí',
  'El pin del símbolo dice «aquí»: nombre y símbolo cuentan lo mismo.', 'Media.',
  'El acento de «aquí» se pierde en dominios y usuarios de redes.'),
 ('mi-manik', [('mi ', 300), ('manik', 600)], 'Mi Manik', 'Abre Mi Manik',
  'Eco del nombre anterior, «Mi Médico Manik».', 'Baja: «mi» es común y vuelve al nombre retirado.',
  'Contradice la decisión de dejar «Mi Médico Manik».'),
 ('dr-manik', [('dr. ', 300), ('manik', 600)], 'Dr. Manik', 'Busca en Dr. Manik',
  'No sale del lema; es la idea que mencionaron.', 'Media: «Dr.» más un nombre se lee como una persona.',
  'Hay médicos reales llamados «Dr. Manik» en directorios de India y Bangladesh. Sugiere que la app es un médico o da consultas, y un título profesional en una marca de salud puede tener reglas de publicidad (por verificar con el área legal).'),
 ('manik-doc', [('manik', 600), (' doc', 300)], 'Manik Doc', 'Busca en Manik Doc',
  'Variante de «Dr. Manik» sin título de persona.', 'Media.',
  '«Doc» es inglés coloquial; en Centroamérica se entiende, en algunos públicos suena informal.'),
]

def logo(piezas, tam=34):
    t = ''.join(f'<span style="font-weight:{w}">{html.escape(x)}</span>' for x, w in piezas)
    return f'<span class="lk" style="--t:{tam}px"><img src="{PIN}" alt=""><span class="wm">{t}</span></span>'

cards = ''
for k, piezas, dicho, frase, lema, dist, riesgo in N:
    cards += f'''<article class="card" aria-labelledby="n-{k}"><h3 id="n-{k}">{dicho}</h3>
 <div class="lam">{logo(piezas)}<span class="end">de MedicalManik</span></div>
 <div class="usos"><span class="app"><img src="{ICONO}" alt=""><small>{html.escape(dicho)}</small></span><p class="fr">«{html.escape(frase)}»</p></div>
 <dl><dt>Del lema</dt><dd>{lema}</dd><dt>Distintivo <span class="inf">inferencia</span></dt><dd>{dist}</dd><dt>Riesgo</dt><dd>{riesgo}</dd></dl></article>'''

HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Nombre del directorio</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;600&family=Urbanist:wght@300..700&family=Onest:wght@400..700&display=swap" rel="stylesheet">
<style>
:root{{--bruma:{T["bruma"]};--blanco:{T["blanco"]};--tinta:{T["tinta"]};--muted:{T["muted"]};--linea:{T["linea"]};--cian-ui:{T["cian-ui"]};--luz-cian:{T["luz-cian"]};--luz-calida:{T["luz-calida"]};--azul:{T["azul-medicalmanik"]};--aviso:{T["texto-calido"]};color-scheme:light}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bruma);color:var(--tinta);font:400 16px/24px "Onest",system-ui,sans-serif;padding:0 16px}}
h1,h2,h3{{font-family:"Urbanist",sans-serif;margin:0}}h1{{font-weight:300;font-size:clamp(30px,5vw,44px);line-height:1.1;letter-spacing:-.02em}}h1 b{{font-weight:600}}h2{{font-size:24px;line-height:32px;font-weight:600}}h3{{font-size:18px;line-height:26px;font-weight:600}}p{{margin:0}}
.wrap{{max-width:1180px;margin:0 auto;padding:40px 0 80px;display:grid;gap:40px;grid-template-columns:minmax(0,1fr)}}
.cab{{display:grid;gap:12px;max-width:78ch;background:radial-gradient(ellipse 60% 90% at 0 0,var(--luz-cian),transparent 70%),radial-gradient(ellipse 50% 80% at 100% 0,var(--luz-calida),transparent 70%);border-radius:28px;padding:28px}}
.eti{{font:600 13px/18px "Onest";letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}}
.nota{{font-size:14px;line-height:20px;color:var(--muted)}}
.aviso{{background:var(--blanco);border:1px solid var(--linea);border-left:4px solid var(--aviso);border-radius:16px;padding:16px 20px;display:grid;gap:6px;max-width:86ch}}.aviso b{{color:var(--aviso)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:16px}}
.card{{background:var(--blanco);border:1px solid var(--linea);border-radius:24px;padding:20px;display:grid;gap:14px;align-content:start}}
.lam{{display:grid;place-items:center;gap:6px;padding:28px 12px;border-radius:18px;background:var(--bruma);min-height:150px}}
.lk{{display:inline-flex;align-items:center;gap:calc(var(--t)*.3)}}.lk img{{height:calc(var(--t)*1.35);width:auto}}
.wm{{font-family:"Sora",sans-serif;font-size:var(--t);line-height:1;letter-spacing:-.04em;color:var(--tinta);white-space:nowrap}}
.end{{font:600 12px/16px "Urbanist";color:var(--azul)}}
.usos{{display:flex;gap:14px;align-items:center}}.app{{display:grid;justify-items:center;gap:4px;width:72px;flex:none}}.app img{{width:52px;height:52px}}.app small{{font-size:11px;line-height:14px;text-align:center;color:var(--tinta)}}
.fr{{font:300 20px/26px "Urbanist";color:var(--tinta)}}
dl{{margin:0;display:grid;grid-template-columns:auto 1fr;gap:6px 12px;font-size:14px;line-height:20px}}dt{{font-weight:600}}dd{{margin:0;color:var(--tinta)}}.inf{{font-weight:400;color:var(--muted);font-size:12px}}
table{{border-collapse:collapse;width:100%;background:var(--blanco);border-radius:16px;overflow:hidden}}th,td{{text-align:left;padding:10px 14px;border-bottom:1px solid var(--linea);font-size:15px;line-height:22px;vertical-align:top}}th{{color:var(--muted);font-weight:600;font-size:14px}}
.tw{{overflow-x:auto;border:1px solid var(--linea);border-radius:16px}}
.reco{{background:var(--blanco);border:1px solid var(--linea);border-radius:24px;padding:24px;display:grid;gap:12px;max-width:86ch}}
ol{{margin:0;padding-left:24px;display:grid;gap:8px}}a{{color:var(--cian-ui)}}
</style></head><body><main class="wrap">
<header class="cab"><span class="eti">Directorio para pacientes · nombre · ronda 1</span>
<h1>Ocho nombres de la familia <b>del lema</b>, todos con Manik</h1>
<p>El lema es «Tu médico, a la mano.» y la leyenda del inicio, «Encuentra a tu médico cerca de ti.». Cada nombre toma una pieza de ahí y la une a Manik. Se conservan el pin con la línea de pulso, el lema y el respaldo «de MedicalManik»; solo cambia la palabra.</p></header>

<div class="aviso"><b>Lo que decide si alguno sirve</b><p>Si «Manik» solo se rechazó porque <b>ya existe una marca parecida</b> registrada en la misma clase, agregarle una palabra común («tu», «mi», «cerca») casi nunca basta: el registro compara la parte que más se recuerda, y esa sigue siendo «Manik». Si se rechazó por <b>otra razón</b> (por ejemplo, que es una palabra que no distingue), un compuesto con impresión propia sí puede pasar. Hay que preguntarle al área legal cuál fue el motivo antes de elegir.</p></div>

<section aria-labelledby="s1"><h2 id="s1">Los ocho</h2><p class="nota">Logotipo con la misma construcción del vigente: pin cian, Sora 600 en «manik» y 300 en la parte nueva, minúsculas. Disponibilidad en el registro de marcas, dominios y redes: <b>sin verificar</b>.</p>
<div class="grid">{cards}</div></section>

<section aria-labelledby="s2" class="reco"><h2 id="s2">Recomendación</h2>
<ol><li><b>Manik a la Mano</b> (confianza media): es el único que convierte el lema completo en nombre, guarda la historia de la mano y, como frase, se separa más de «Manik» solo. Su costo es el largo: el logotipo funciona, pero en el ícono de la app va solo el pin.</li>
<li><b>Manik Cerca</b> como alternativa corta: dos palabras, se dice fácil y repite la promesa del inicio.</li>
<li><b>Dr. Manik</b> no lo recomiendo: no sale del lema, hay médicos reales con ese nombre en otros directorios y hace pensar que la app es un médico.</li></ol>
<p class="nota">«Tu Manik» y «Mi Manik» son los más cortos, pero son los que más probablemente repiten el problema del registro.</p></section>

<section aria-labelledby="s3"><h2 id="s3">Siguiente paso</h2>
<ol><li>Confirmar con el área legal por qué se rechazó «Manik» solo.</li><li>Elegir 2 o 3 de esta lista.</li><li>Búsqueda fonética en el registro de marcas de México (clases 9, 42 y 44) y en los de Centroamérica donde se vaya a operar, más dominios y redes.</li><li>Con el nombre elegido, actualizar logotipos, manual del directorio, sistema de diseño y manual de identidad.</li></ol>
<p class="nota">Búsqueda preliminar en la web (no sustituye la del registro): «Dr Manik» aparece como nombre de médicos en directorios de India y Bangladesh, por ejemplo en <a href="https://www.medibuddy.in/doctor-consultations/ahmedabad/cardiologist/dr-manik-chopra-46413">MediBuddy</a> y <a href="https://www.apolloclinic.com/find-a-doctor/best-nephrologist-in-kolkata-west-bengal/dr-manik-kataruka">Apollo Clinic</a>. No se encontraron servicios de salud en México con los otros siete nombres; esa búsqueda no es concluyente.</p></section>
</main></body></html>'''
open(os.path.join(D, 'nombres.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
