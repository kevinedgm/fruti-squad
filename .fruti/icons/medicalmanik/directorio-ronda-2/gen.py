# Directorio de pacientes · ronda 2: nombres desde el significado de Manik'
import sys
S = sys.argv[1]; F = f'file://{S}/fuentes'
AZ = '#234899'
HECHOS = [('Qué es', "Manik' es el séptimo día del Tzolk'in, el calendario maya de 260 días."),
          ('Su glifo', 'Una mano derecha semiempuñada, en actitud de agarrar.'),
          ('Su asociación', 'El venado: en otras lenguas mesoamericanas ese día se llama «venado» (mázatl, kej).'),
          ('Lo que no se sabe', 'El significado exacto de la palabra se sigue discutiendo entre especialistas.')]
N = [
 ('Manik', 'manik.mx', 'Tu médico, a la mano.', 'La palabra raíz, sola, para el paciente. El glifo es una mano y «a la mano» en español es «cerca y fácil». MedicalManik queda como la empresa; Manik como lo que conoce la gente.', 'El paciente no sabe qué significa: el lema lo explica. Puede confundirse con la empresa.', True),
 ('Mano', 'mano.mx', 'Pídele una mano a tu médico.', 'El glifo de Manik\' traducido. Y en México «mano» es también «amigo»: cercano, de confianza.', 'Muy común: difícil de registrar y casi seguro el dominio está ocupado.', False),
 ('Kéej', 'keej.mx', 'Te guía hasta tu médico.', 'Venado en maya yucateco: el animal del día Manik\'. Nombre corto y propio.', 'Pronunciación y escritura poco claras fuera de la península; validar ortografía con hablantes.', False),
 ("Ts'aak", 'tsaak.mx', 'Encuentra quién te cure.', 'Remedio, curar, en maya yucateco: de ahí J-ts\'aak, el curandero.', 'El apóstrofo no cabe en un dominio y se escribe mal; es vocabulario de la medicina tradicional y conviene consultarlo con comunidades mayas.', False),
]
h = ''.join(f'<div class="h"><b>{a}</b><span>{b}</span></div>' for a, b in HECHOS)
c = ''
for n, u, lema, pro, con, rec in N:
    c += f'<article class="{"rec" if rec else ""}">{"<span class=r>Recomendado</span>" if rec else ""}<div class="w">{n}</div><p class="l">{lema}</p><p class="u">{u}</p><p>{pro}</p><p class="k"><b>Riesgo:</b> {con}</p></article>'
open('nombres.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
body{{margin:0;background:#F5F7FB;color:#14213D;font:15px/1.45 Inst,sans-serif;padding:36px;width:1180px}}
h1{{font:600 28px Sora;color:{AZ};margin:0}}.i{{margin:4px 0 18px;color:#3E4A66;max-width:900px}}
.hs{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:22px}}.h{{background:#fff;border:1px solid #C9D1DF;border-radius:14px;padding:12px 14px;display:grid;gap:2px}}.h b{{font:600 13px Inst;color:#3E4A66;text-transform:uppercase;letter-spacing:.06em}}
.g{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}article{{position:relative;background:#fff;border:1px solid #C9D1DF;border-radius:16px;padding:20px 18px;display:grid;gap:6px;align-content:start}}
article.rec{{border:2px solid {AZ}}}.r{{position:absolute;top:-12px;left:16px;background:{AZ};color:#fff;font:600 12px Inst;padding:3px 10px;border-radius:99px}}
.w{{font:600 40px/1.1 Sora;color:{AZ};letter-spacing:-.02em}}.l{{margin:0;font:600 16px Sora;color:#14213D}}.u{{margin:0;font:600 13px Inst;color:#007C8C}}article p{{margin:0;font-size:14px}}.k{{color:#7F4A08}}
</style></head><body><h1>Directorio de pacientes · nombres desde Manik'</h1><p class="i">Ronda 2. Lo que dicen las fuentes sobre la palabra, y cuatro nombres que salen de ella.</p><div class="hs">{h}</div><div class="g">{c}</div></body></html>""")
print('ok')
