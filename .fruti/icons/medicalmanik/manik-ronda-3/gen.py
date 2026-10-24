# Manik (directorio) · ronda 3: miembro de la familia. Misma línea R1, mismo cuadro, un rasgo en el borde.
import sys, re
S = sys.argv[1]; F = f'file://{S}/fuentes'
INK, AZ, CI, PAPEL = '#14213D', '#234899', '#00BDD0', '#F6F8FC'
LINEA = 'M-6 63 L13 63 L27 12 L49 86 L71 25 L84 64 L106 64'
r = 21
CUADRO = f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z'
PIN = f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H62 L50 114 L38 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z'
LUPA = 'M92 92 L108 108'
n = [0]
def sym(forma, fondo, linea=PAPEL, pieza=None, color_pieza=None):
    n[0] += 1; u = f'k{n[0]}'; d = PIN if forma == 'pin' else CUADRO
    body = f'<defs><clipPath id="{u}"><path d="{d}"/></clipPath><mask id="m{u}" maskUnits="userSpaceOnUse" x="-10" y="-10" width="130" height="130"><rect x="-10" y="-10" width="130" height="130" fill="#fff"/>'
    if pieza: body += f'<path d="{pieza}" stroke="#000" stroke-width="22" stroke-linecap="round"/>'
    body += f'</mask></defs><g mask="url(#m{u})"><path d="{d}" fill="{fondo}"/><path clip-path="url(#{u})" d="{LINEA}" fill="none" stroke="{linea}" stroke-width="13" stroke-linejoin="round"/></g>'
    if pieza: body += f'<path d="{pieza}" stroke="{color_pieza}" stroke-width="12" stroke-linecap="round"/>'
    return f'<svg viewBox="-8 -10 126 130" xmlns="http://www.w3.org/2000/svg">{body}</svg>'
V = [
 ('1', 'Lupa · azul + cian', lambda: sym('cuadro', AZ, PAPEL, LUPA, CI), 'El cuadro se vuelve lupa: el mango cian sale de la esquina. Dice «buscar» y es la misma pieza separada por un corte que usan Farmacia e Impulsa.'),
 ('2', 'Pin · azul', lambda: sym('pin', AZ), 'La base del cuadro se cierra en punta de ubicación: «cerca de ti». Es un cambio de silueta, como la carpeta de Expediente o el ticket de Compras.'),
 ('3', 'Pin · cian', lambda: sym('pin', CI, INK), 'La misma silueta en cian, el color que ninguna app interna usa: distingue la cara pública. La línea va en tinta porque blanco sobre cian no se lee (2.3:1).'),
 ('4', 'Lupa · cian + azul', lambda: sym('cuadro', CI, INK, LUPA, AZ), 'Cuadro cian con línea tinta y mango azul: el más vivo de los cuatro.'),
]
SV = '/home/user/fruti-squad/.fruti/icons/medicalmanik/final/svg/'
fam = ''.join(f'<span class="fm"><img src="file://{SV}{k}.svg" alt=""><small>{n}</small></span>' for k, n in [('expediente','Expediente'),('agenda','Agenda'),('compras','Compras'),('farmacia','Farmacia'),('impulsa','Impulsa'),('grupos','Grupos')])
rows = ''
for k, nom, f, txt in V:
    s = f()
    sz = ''.join(f'<span class="s" style="width:{z}px;height:{z}px">{s}</span>' for z in (128, 64, 40, 24))
    rows += f'''<section><div class="hd"><h2>{k} · {nom}</h2><p>{txt}</p></div><div class="row"><div class="sz">{sz}</div>
     <div class="lk"><span class="s" style="width:64px;height:64px">{s}</span><span class="wm">manik</span><span class="end">de MedicalManik</span></div></div>
     <div class="fam">{fam}<span class="fm me"><span class="s" style="width:56px;height:56px">{s}</span><small>Manik</small></span></div></section>'''
open('lamina.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
body{{margin:0;background:#F5F7FB;color:{INK};font:15px/1.45 Inst,sans-serif;padding:36px;width:1180px}}h1{{font:600 28px Sora;margin:0}}.i{{margin:4px 0 18px;color:#3E4A66;max-width:940px}}
section{{background:#fff;border:1px solid #C9D1DF;border-radius:18px;padding:20px 22px;margin-bottom:14px;display:grid;gap:14px}}.hd h2{{margin:0;font:600 19px Sora}}.hd p{{margin:2px 0 0;color:#3E4A66}}
.row{{display:flex;gap:40px;align-items:center}}.sz{{display:flex;gap:18px;align-items:end}}.s{{display:inline-block}}.s svg{{width:100%;height:100%;display:block}}
.lk{{display:flex;align-items:center;gap:12px}}.wm{{font:600 52px/1 Sora;letter-spacing:-.04em}}.end{{font:500 13px Inst;color:{AZ};border-left:1px solid #C9D1DF;padding-left:10px}}
.fam{{display:flex;gap:14px;align-items:end;border-top:1px solid #E1E6F0;padding-top:12px}}.fm{{display:grid;justify-items:center;gap:4px}}.fm img{{width:56px;height:56px}}.fm small{{font-size:12px;color:#3E4A66}}.fm.me small{{font-weight:700;color:{INK}}}
</style></head><body><h1>Manik · un miembro más de la familia</h1><p class="i">Ronda 3. Misma M de pulso, mismo cuadro y la misma regla del ecosistema: un solo rasgo en el borde dice qué es. Abajo de cada opción, junto a las seis apps.</p>{rows}</body></html>""")
print('ok')
