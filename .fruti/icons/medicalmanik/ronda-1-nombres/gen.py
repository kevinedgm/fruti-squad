# MedicalManik · expediente médico digital · ronda 1: nombres del producto
import sys
S = sys.argv[1]; F = f'file://{S}/fuentes'
AZ, CI = '#234899', '#00BDD0'
N = [  # territorio, nombre, por qué, riesgo
 ('Familia Manik', 'Anik', 'Sale de mANIK: se lee como hijo de la marca, igual que Nabi de Nabani. Corto y sin significado previo en español.', 'No dice «expediente»: el significado lo pone la marca madre.'),
 ('Familia Manik', 'Manik Folio', 'Folio es la hoja numerada del expediente clínico. Arquitectura clara: empresa + producto.', 'Largo; «Folio» lo usan muchos productos de documentos.'),
 ('El expediente', 'Anam', 'De anamnesis, la historia clínica que el médico levanta. Lo entiende cualquier médico.', 'El paciente no conoce la palabra.'),
 ('El expediente', 'Hilo', 'La historia del paciente como un hilo continuo de consultas, y la línea de la M de pulso.', 'Palabra común: difícil de registrar sola.'),
 ('El expediente', 'Kardi', 'Del kárdex, la tarjeta de registro de enfermería en Latinoamérica, y de kardia (corazón).', 'Puede leerse solo como «cardiología».'),
 ('El pulso', 'Lati', 'De latido. Breve, cálido, se pronuncia igual en todo el continente.', 'Suena informal para un registro legal.'),
 ('El pulso', 'Trazo', 'El trazo del electrocardiograma y el trazo de quien escribe la nota médica.', 'Puede sonar a herramienta de dibujo.'),
 ('El pulso', 'Ritma', 'Ritmo cardiaco + «a» final femenina que lo vuelve nombre propio.', 'Cercano a marcas de música o fitness.'),
]
cards = ''
for t, n, p, r in N:
    cards += f'<article><span class="t">{t}</span><div class="w">{n}</div><div class="lk"><b>MedicalManik</b> · {n}</div><p>{p}</p><p class="r">Riesgo: {r}</p></article>'
open('nombres.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
body{{margin:0;background:#F6F8FC;color:#14213D;font:14px/1.45 Inst,sans-serif;padding:36px;width:1140px}}
header{{display:flex;gap:18px;align-items:center;margin-bottom:22px}}header img{{height:54px}}h1{{font:600 26px Sora;color:{AZ};margin:0}}header p{{margin:2px 0 0;color:#4A5674}}
.g{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}article{{background:#fff;border:1px solid #E1E6F0;border-radius:16px;padding:18px;display:grid;gap:6px;align-content:start}}
.t{{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:{CI};font-weight:700}}.w{{font:600 40px/1.1 Sora;color:{AZ};letter-spacing:-.02em}}.lk{{font-size:12px;color:#4A5674}}.lk b{{color:{AZ}}}
article p{{margin:0;font-size:13px}}.r{{color:#8A5A00}}
</style></head><body><header><img src="../fuente/logo-MM-2.png" style="height:56px"><div><h1>Expediente médico digital · nombres</h1><p>Ronda 1: ocho nombres en tres territorios. La empresa sigue siendo MedicalManik; el producto lleva nombre propio.</p></div></header>
<div class="g">{cards}</div></body></html>""")
print('ok')
