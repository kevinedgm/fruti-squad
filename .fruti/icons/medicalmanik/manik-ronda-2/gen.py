# Manik · ronda 2: sin jade (se confundía con Doctoralia). Azul, cian o azul + cian, en las tres direcciones
import sys
S = sys.argv[1]; F = f'file://{S}/fuentes'
INK, AZ, CI, CIO = '#14213D', '#234899', '#00BDD0', '#00788A'
def A(c, d, w=11): return f'<path d="M8 58 L21 58 L33 20 L50 80 L67 32 L78 58 L92 58" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>' + (f'<circle cx="92" cy="58" r="8.5" fill="{d}"/>' if d != c else '')
def B(c, d, w=11): return (f'<path d="M22 34 C18 64 32 84 54 84 C74 84 87 70 86 50" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
    f'<path d="M22 34 C24 24 34 22 37 32" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/><circle cx="56" cy="48" r="13" fill="{d}"/>')
def C(c, d, w=9): return (f'<path d="M50 94 C50 94 16 62 16 40 A34 34 0 0 1 84 40 C84 62 50 94 50 94Z" fill="{c}"/>'
    f'<path d="M27 42 L35 42 L42 24 L52 56 L61 30 L66 42 L73 42" fill="none" stroke="{d}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
svg = lambda b, z: f'<svg viewBox="0 0 100 100" width="{z}" height="{z}" aria-hidden="true">{b}</svg>'
PAL = [  # nombre, símbolo, acento del símbolo, botón, texto del botón, nota
 ('Azul', AZ, AZ, AZ, '#fff', 'Todo en el azul de MedicalManik: máxima coherencia con la familia; el menos distinto para el paciente.'),
 ('Cian', CI, CI, CI, INK, 'El cian de la marca original como protagonista: fresco y propio. Con blanco solo da 2.3:1, así que el botón lleva texto tinta (7.0:1).'),
 ('Azul + cian', AZ, CI, AZ, '#fff', 'Azul para la estructura y los botones; cian solo para el punto que da vida al símbolo. Une las dos marcas originales.'),
]
DIRS = [('A · Pulso suelto', A), ('B · A la mano', B), ('C · Cerca de ti', C)]
head = ''.join(f'<div class="ph"><b>{n}</b><small>{nota}</small></div>' for n, *_, nota in PAL)
rows = ''
for dn, fn in DIRS:
    rows += f'<div class="dn">{dn}</div>'
    for n, c, d, b, bt, _ in PAL:
        sym = fn(c, d) if fn is not C else C(c, '#fff' if d == c else d)
        icon_sym = (fn('#fff', d if d != c else '#fff') if fn is not C else C('#fff', c))
        rows += (f'<div class="cell"><div class="lk">{svg(sym, 58)}<span class="wm">manik</span></div>'
                 f'<div class="mini"><span class="ic" style="background:{c}">{svg(icon_sym, 40)}</span>'
                 f'<button style="background:{b};color:{bt}">Agendar cita</button><span class="st">★ 4.9</span></div></div>')
open('lamina.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
body{{margin:0;background:#F5F7FB;color:{INK};font:15px/1.45 Inst,sans-serif;padding:36px;width:1180px}}
h1{{font:600 28px Sora;margin:0}}.i{{margin:4px 0 18px;color:#3E4A66;max-width:940px}}
.grid{{display:grid;grid-template-columns:150px repeat(3,1fr);gap:12px;align-items:stretch}}
.ph{{display:grid;gap:4px;padding:4px 4px 8px}}.ph b{{font:600 18px Sora}}.ph small{{color:#3E4A66;font-size:13.5px}}
.dn{{font:600 16px Sora;align-self:center}}.cell{{background:#fff;border:1px solid #C9D1DF;border-radius:16px;padding:16px;display:grid;gap:14px}}
.lk{{display:flex;align-items:center;gap:10px}}.wm{{font:600 40px/1 Sora;letter-spacing:-.04em}}
.mini{{display:flex;align-items:center;gap:10px}}.ic{{width:56px;height:56px;border-radius:15px;display:grid;place-items:center;flex:none}}
.mini button{{border:0;border-radius:12px;min-height:44px;padding:0 16px;font:600 15px Inst}}.st{{font:600 14px Inst;color:#8A5A00}}
</style></head><body><h1>Manik · color, ronda 2</h1><p class="i">Sin jade: se parecía a Doctoralia. Tres caminos de color, probados en las tres direcciones de símbolo. Las estrellas quedan en un ámbar oscuro solo como dato de calificación.</p>
<div class="grid"><div></div>{head}{rows}</div></body></html>""")
print('ok')
