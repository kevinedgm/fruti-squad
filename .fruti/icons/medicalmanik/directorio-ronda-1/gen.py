# Directorio de pacientes · ronda 1: nombres (hoy «Mi Médico Manik»)
import sys
S = sys.argv[1]; F = f'file://{S}/fuentes'
AZ, CI = '#234899', '#00BDD0'
G = [
 ('Dentro de la familia', 'El patrón «Producto Manik» que ya usan las seis apps.', [
   ('Médicos Manik', 'Busca tu dermatólogo en Médicos Manik', 'medicosmanik.mx', 'Dice exactamente qué encuentras; suma a la marca que ya conocen los médicos.', 'El paciente no conoce «Manik»: la palabra no le ayuda a recordarlo.'),
   ('Directorio Manik', 'Encuéntralo en Directorio Manik', 'directoriomanik.mx', 'Coherente con el resto.', 'Nadie busca «directorio»: suena a guía telefónica.')]),
 ('Nombre propio, respaldado', 'Un nombre para el paciente; «de MedicalManik» abajo, como garantía.', [
   ('Kuro', 'Agenda con tu pediatra en Kuro', 'kuro.mx', 'Dos sílabas, se dice igual en todo el país; evoca «curar» sin ser literal.', 'Hay que construir su significado; revisar registro y dominio.'),
   ('Consultia', 'Reserva en Consultia', 'consultia.mx', 'Se entiende solo (consulta); fácil de escribir.', 'Cercano a nombres de consultoras.'),
   ('Cita Ya', 'Saca tu cita en Cita Ya', 'citaya.mx', 'Dice la acción y la urgencia; muy fácil de recordar.', 'Promete inmediatez que no siempre hay; probablemente ocupado.')]),
 ('Nombre de búsqueda', 'Lo que la gente escribe en Google, convertido en marca.', [
   ('Doctor Cerca', 'Doctor Cerca: especialistas cerca de ti', 'doctorcerca.mx', 'Es literalmente lo que se busca («doctor cerca de mí»): ayuda en buscadores.', 'Genérico y difícil de registrar como marca.'),
   ('Mi Médico', '¿Ya viste a tu médico en Mi Médico?', 'mimedico.mx', 'Conserva lo que ya funciona del nombre actual, sin «Manik».', 'Muy genérico; casi seguro ya tomado.')]),
]
cards = ''
for t, d, items in G:
    cards += f'<section><h2>{t}</h2><p class="d">{d}</p><div class="g">'
    for n, frase, url, pro, con in items:
        cards += f'<article><div class="w">{n}</div><p class="f">«{frase}»</p><p class="u">{url}</p><p><b>A favor:</b> {pro}</p><p class="r"><b>Riesgo:</b> {con}</p></article>'
    cards += '</div></section>'
open('nombres.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
body{{margin:0;background:#F5F7FB;color:#14213D;font:15px/1.45 Inst,sans-serif;padding:36px;width:1180px}}
h1{{font:600 28px Sora;color:{AZ};margin:0}}.i{{margin:4px 0 20px;color:#3E4A66;max-width:900px}}
section{{border-top:1px solid #C9D1DF;padding:16px 0 20px}}h2{{margin:0;font:600 18px Sora}}.d{{margin:2px 0 12px;color:#3E4A66}}
.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}article{{background:#fff;border:1px solid #C9D1DF;border-radius:16px;padding:18px;display:grid;gap:6px;align-content:start}}
.w{{font:600 34px/1.1 Sora;color:{AZ};letter-spacing:-.02em}}.f{{margin:0;font-size:14px;color:#14213D;font-style:italic}}.u{{margin:0;font:600 13px Inst;color:#007C8C}}
article p{{margin:0;font-size:14px}}.r{{color:#7F4A08}}
</style></head><body><h1>Directorio de pacientes · nombres</h1><p class="i">Ronda 1. Es el único producto que usa el paciente, no la clínica. Por eso la pregunta es otra: ¿qué nombre recuerda alguien que nunca ha oído «Manik» cuando necesita un especialista?</p>{cards}</body></html>""")
print('ok')
