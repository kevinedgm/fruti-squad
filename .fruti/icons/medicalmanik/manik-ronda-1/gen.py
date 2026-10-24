# Manik (directorio de pacientes) · ronda 1 de identidad: tres direcciones
import sys
S = sys.argv[1]; F = f'file://{S}/fuentes'
INK, JADE, MAIZ, AZ = '#14213D', '#0B7A68', '#F2B33D', '#234899'
# A · el pulso suelto: la misma línea del ecosistema, fuera del cuadro y con puntas redondas
def A(c=JADE, w=11): return f'<path d="M8 58 L21 58 L33 20 L50 80 L67 32 L78 58 L92 58" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
# B · la mano: el glifo de Manik' (mano semiempuñada) sostiene a la persona
def B(c=JADE, d=MAIZ, w=11): return (f'<path d="M22 34 C18 64 32 84 54 84 C74 84 87 70 86 50" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
    f'<path d="M22 34 C24 24 34 22 37 32" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/><circle cx="56" cy="48" r="13" fill="{d}"/>')
# C · el lugar: un pin con el pulso calado
def C(c=JADE, w=9): return (f'<path d="M50 94 C50 94 16 62 16 40 A34 34 0 0 1 84 40 C84 62 50 94 50 94Z" fill="{c}"/>'
    f'<path d="M27 42 L35 42 L42 24 L52 56 L61 30 L66 42 L73 42" fill="none" stroke="#fff" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
def svg(body, z, vb='0 0 100 100'): return f'<svg viewBox="{vb}" width="{z}" height="{z}" aria-hidden="true">{body}</svg>'
DIR = [
 ('A', 'Pulso suelto', A, 'La línea del ecosistema sale del cuadro y termina en puntas redondas: es la misma familia, pero abierta al público. La más conectada con MedicalManik.', 'Para el paciente sigue siendo un latido, el recurso más común en salud.'),
 ('B', 'A la mano', B, 'El glifo maya de Manik\' es una mano semiempuñada: aquí sostiene a la persona (el punto maíz). Cuenta el lema «Tu médico, a la mano» sin palabras.', 'Se aleja de la M de pulso: la relación con el ecosistema queda en el nombre y el respaldo.'),
 ('C', 'Cerca de ti', C, 'Un pin de ubicación con el pulso calado: dice «directorio, cerca de ti» al instante.', 'Los pines son comunes en apps de mapas y directorios; menos propio.'),
]
def ficha(fn, acc):
    return (f'<div class="fi"><div class="top"><span class="av">LH</span><div><b>Dra. Lucía Herrera</b><small>Pediatra · Puebla · a 1.2 km</small>'
            f'<span class="st"><i style="color:{MAIZ}">★★★★★</i> 4.9 <span>(124 opiniones)</span></span></div></div>'
            f'<div class="sl"><span>Hoy</span><button>11:30</button><button>12:00</button><button>16:30</button></div>'
            f'<button class="cta" style="background:{acc}">Agendar cita</button></div>')
rows = ''
for k, n, fn, pro, con in DIR:
    big = svg(fn(), 140)
    lock = f'<span class="lk">{svg(fn(), 56)}<span class="wm">manik</span></span>'
    lock2 = f'<span class="lk sm">{svg(fn(), 34)}<span class="wm s">manik</span><span class="end">de MedicalManik</span></span>'
    ic = f'<span class="ic" style="background:{JADE}">{svg(fn("#fff") if fn is not B else B("#fff", MAIZ), 52)}</span>' if fn is not C else f'<span class="ic" style="background:#fff;border:1px solid #C9D1DF">{svg(C(), 56)}</span>'
    rows += f'''<section><div class="hd"><h2>{k} · {n}</h2><p>{pro}</p><p class="r"><b>Riesgo:</b> {con}</p></div>
    <div class="row"><div class="big">{big}</div><div class="col">{lock}<p class="lema">Tu médico, a la mano.</p>{lock2}<div class="ics">{ic}<span class="fav">{svg(fn() if fn is not B else B(), 24)}</span><small>ícono de app · favicon</small></div></div>{ficha(fn, JADE)}</div></section>'''
pal = ''.join(f'<span class="sw"><i style="background:{c}"></i><b>{n}</b><small>{h}</small></span>' for n, c, h in [('Jade', JADE, 'marca, botones · 5.4:1 con blanco'), ('Tinta', INK, 'texto'), ('Maíz', MAIZ, 'calificaciones, acento; nunca texto'), ('Azul Manik', AZ, 'solo en «de MedicalManik»')])
open('lamina.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Atk';src:url('{F}/Atkinson.ttf')}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
body{{margin:0;background:#F6F8F7;color:{INK};font:15px/1.45 Inst,sans-serif;padding:36px;width:1180px}}
h1{{font:600 28px Sora;color:{INK};margin:0}}.i{{margin:4px 0 14px;color:#3E4A66;max-width:900px}}
.pal{{display:flex;gap:18px;margin-bottom:18px}}.sw{{display:flex;gap:8px;align-items:center}}.sw i{{width:26px;height:26px;border-radius:8px;display:inline-block}}.sw small{{color:#3E4A66}}
section{{background:#fff;border:1px solid #C9D1DF;border-radius:18px;padding:20px 22px;margin-bottom:14px}}.hd h2{{margin:0;font:600 19px Sora}}.hd p{{margin:2px 0 0;color:#3E4A66;max-width:980px}}.hd .r{{color:#7F4A08}}
.row{{display:grid;grid-template-columns:170px 1fr 360px;gap:24px;align-items:center;margin-top:14px}}.big{{display:grid;place-items:center;background:#F6F8F7;border-radius:16px;height:170px}}
.col{{display:grid;gap:10px}}.lk{{display:flex;align-items:center;gap:12px}}.wm{{font:600 52px/1 Sora;letter-spacing:-.04em;color:{INK}}}.wm.s{{font-size:30px}}.lk.sm{{gap:8px}}.end{{font:500 13px Inst;color:{AZ};border-left:1px solid #C9D1DF;padding-left:10px;margin-left:4px}}
.lema{{margin:0;font:500 18px Sora;color:{JADE}}}.ics{{display:flex;gap:12px;align-items:center}}.ic{{width:72px;height:72px;border-radius:18px;display:grid;place-items:center}}.fav{{display:grid;place-items:center;width:32px;height:32px;border:1px solid #C9D1DF;border-radius:8px}}.ics small{{color:#3E4A66}}
.fi{{border:1px solid #C9D1DF;border-radius:16px;padding:14px;display:grid;gap:10px;font-family:Atk,Inst,sans-serif}}.top{{display:flex;gap:12px}}.av{{width:48px;height:48px;border-radius:50%;background:#E3F1EE;color:{JADE};display:grid;place-items:center;font:600 16px Sora;flex:none}}
.fi b{{display:block;font:600 16px Sora}}.fi small{{display:block;color:#3E4A66;font-size:14px}}.st{{font-size:14px}}.st i{{font-style:normal;letter-spacing:1px}}.st span{{color:#3E4A66}}
.sl{{display:flex;gap:6px;align-items:center;font-size:14px;color:#3E4A66}}.sl button{{border:1px solid {JADE};color:{JADE};background:#fff;border-radius:10px;padding:6px 10px;font:600 14px Atk,sans-serif}}
.cta{{border:0;color:#fff;border-radius:12px;min-height:44px;font:600 16px Atk,sans-serif}}
</style></head><body><h1>Manik · identidad del directorio</h1><p class="i">Ronda 1: tres direcciones. El nombre es solo «Manik», en minúsculas para que se sienta cercano; «de MedicalManik» aparece como respaldo. Paleta propia para el paciente, más cálida que la de las herramientas de clínica: jade (piedra preciosa maya) y maíz.</p>
<div class="pal">{pal}</div>{rows}</body></html>""")
print('ok')
