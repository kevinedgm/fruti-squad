# Directorio para pacientes · nombre nuevo · r02. Pedido (2026-11-05): «debe ser fácil de recordar, identificar y saber que es
# un directorio médico, como Doctoralia», y llevar «Manik». Molde Doctoralia: raíz que dice qué es + palabra nueva, en una sola palabra.
# Reutiliza el estilo de la r01 (se lee su HTML, no se modifica). Uso: python3 gen.py → nombres.html
import os, base64, html
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
uri = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
PIN = uri('manik-final/svg/simbolo.svg'); ICONO = uri('manik-final/svg/app-icon.svg')
CSS = open(os.path.join(M, 'directorio-nombre-r01/nombres.html')).read().split('<style>', 1)[1].split('</style>', 1)[0]
CSS += '.sc{display:flex;gap:6px;flex-wrap:wrap}.sc span{font:600 12px/16px "Onest";border-radius:999px;padding:3px 10px;background:var(--bruma);border:1px solid var(--linea)}.sc span.si{background:#E7F5EE;border-color:#E7F5EE;color:#157B4A}.sc span.me{background:#FFF4E0;border-color:#FFF4E0;color:#6B4A00}.sc span.no{background:#F9ECED;border-color:#F9ECED;color:#B23A48}\n.esp{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px}.esp div{background:var(--blanco);border:1px solid var(--linea);border-radius:14px;padding:12px;display:grid;gap:4px;font-size:14px;line-height:20px}.esp b{font:600 15px/20px "Urbanist"}.esp .on{border:2px solid var(--cian-ui)}@media(max-width:760px){.esp{grid-template-columns:1fr 1fr}}'
# (nombre, piezas, se dice, frase, ¿dice que es médico?, recordable, registrable, nota)
N = [
 ('MediManik', [('medi', 300), ('manik', 600)], 'me·di·ma·nik', 'Busca tu médico en MediManik',
  ('si', 'Dice «médico»'), ('si', 'Rima interna m–m'), ('me', 'Registro: medio'),
  '«Medi» se entiende en español e inglés; las dos emes lo hacen pegajoso. Hay muchas marcas con «medi-»: lo que distingue es «manik».'),
 ('DoctorManik', [('doctor', 300), ('manik', 600)], 'doc·tor·ma·nik', 'Encuentra doctor en DoctorManik',
  ('si', 'El más claro'), ('me', 'Largo: 11 letras'), ('me', 'Registro: medio'),
  'Es el molde Doctoralia casi literal. Fundido en una palabra ya no se lee como «Dr. Manik», una persona.'),
 ('DocManik', [('doc', 300), ('manik', 600)], 'doc·ma·nik', 'Agenda en DocManik',
  ('si', 'Dice «doctor»'), ('si', 'Corto: 8 letras'), ('me', 'Registro: medio'),
  'La versión corta de DoctorManik; «doc» es coloquial pero se entiende en toda la región.'),
 ('ManikMed', [('manik', 600), ('med', 300)], 'ma·nik·med', 'Busca en ManikMed',
  ('me', 'Dice «med», más técnico'), ('si', 'Corto'), ('me', 'Registro: medio'),
  'Suena a laboratorio o a farmacia más que a directorio; «med» al final pesa menos.'),
 ('CitaManik', [('cita', 300), ('manik', 600)], 'ci·ta·ma·nik', 'Haz tu cita en CitaManik',
  ('me', 'Dice «cita», no «médico»'), ('si', 'Muy fácil de decir'), ('me', 'Registro: medio'),
  'Nombra la acción principal (agendar), pero no dice que es médico: puede ser cualquier tipo de cita.'),
 ('Médico Manik', [('médico ', 300), ('manik', 600)], 'mé·di·co ma·nik', 'Encuéntralo en Médico Manik',
  ('si', 'Dice «médico»'), ('si', 'Conocido: era «Mi Médico Manik»'), ('no', 'Registro: bajo'),
  '«Médico» suelto es descriptivo: el registro lo trata casi como «Manik» solo. Lleva acento: complica dominio y redes.'),
]
cl = {'si': 'si', 'me': 'me', 'no': 'no'}
def logo(p, t=34):
    return f'<span class="lk" style="--t:{t}px"><img src="{PIN}" alt=""><span class="wm">' + ''.join(f'<span style="font-weight:{w}">{html.escape(x)}</span>' for x, w in p) + '</span></span>'
cards = ''.join(f'''<article class="card" aria-labelledby="n{i}"><h3 id="n{i}">{n}</h3>
 <div class="lam">{logo(p)}<span class="end">de MedicalManik</span></div>
 <div class="sc">{"".join(f'<span class="{cl[a]}">{b}</span>' for a, b in (q1, q2, q3))}</div>
 <div class="usos"><span class="app"><img src="{ICONO}" alt=""><small>{html.escape(n)}</small></span><p class="fr">«{html.escape(fr)}»</p></div>
 <p class="nota">Se dice {se}. {nota}</p></article>''' for i, (n, p, se, fr, q1, q2, q3, nota) in enumerate(N))

ESP = ''.join(f'<div class="{c}"><b>{t}</b><span class="nota">{d}</span></div>' for t, d, c in [
 ('Genérico', '«Directorio médico». No se registra.', ''), ('Descriptivo', '«Médico Manik». Casi no se registra.', ''),
 ('Sugestivo', '«Doctoralia», «MediManik». Dice qué es y se registra.', 'on'), ('Arbitrario', 'Palabra real sin relación: «Manzana».', ''), ('Inventado', '«Kodak». Muy fuerte, no dice nada.', '')])

HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Nombre del directorio r02</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;600&family=Urbanist:wght@300..700&family=Onest:wght@400..700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><main class="wrap">
<header class="cab"><span class="eti">Directorio para pacientes · nombre · ronda 2</span>
<h1>Que se entienda que es <b>un directorio médico</b>, con Manik</h1>
<p>Criterio nuevo: fácil de recordar, de identificar y que diga qué es, como Doctoralia. Doctoralia funciona porque une una raíz que dice qué es («doctor») con un final que la vuelve una palabra nueva («-alia»): se entiende al verla y, como palabra completa, se puede registrar. Aquí, el mismo molde con Manik.</p></header>
<section aria-labelledby="s0"><h2 id="s0">Dónde cae cada nombre</h2><p class="nota">De menos a más registrable. Lo que sirve está en medio: dice qué es y no es una palabra común.</p><div class="esp">{ESP}</div></section>
<div class="aviso"><b>Sigue abierto</b><p>Todos llevan «Manik» completo. Si «Manik» solo se rechazó por una marca previa parecida, la parte que más se recuerda sigue siendo «Manik» y el riesgo no desaparece; fundirlo en una palabra con impresión propia lo reduce, no lo elimina. Lo confirma el área legal.</p></div>
<section aria-labelledby="s1"><h2 id="s1">Seis candidatos</h2><p class="nota">Logotipo con la construcción vigente: la raíz en Sora 300 y «manik» en 600, para que Manik se siga reconociendo. Registro, dominios y redes: sin verificar.</p><div class="grid">{cards}</div></section>
<section class="reco" aria-labelledby="s2"><h2 id="s2">Recomendación</h2>
<ol><li><b>MediManik</b> (confianza media): dice «médico» en español e inglés, las dos emes lo vuelven fácil de recordar, se escribe como se oye y conserva «manik» entero.</li>
<li><b>DocManik</b> si se quiere más corto y más cercano a «doctor».</li>
<li><b>DoctorManik</b> es el más claro y el más fiel al molde Doctoralia, pero el más largo.</li></ol>
<p class="nota">Búsqueda web preliminar (no sustituye la del registro): no aparecieron servicios con «MediManik», «DocManik», «DoctorManik», «CitaManik» ni «ManikMed»; sí médicos reales de apellido Manik en otros países, por ejemplo en <a href="https://www.docindia.org/doctors/hisar/dr-manik-arora-internal-medicine">DocIndia</a>. «Medi-» es un prefijo muy usado en salud (por ejemplo <a href="https://www.affarsvarlden.se/aktie/medimi">Medimi</a> en Suecia).</p></section>
</main></body></html>'''
open(os.path.join(D, 'nombres.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
