# Manik (directorio) · ronda 4: el pin, separado del azul de Expediente (cian, degradado azul→cian)
import sys
S = sys.argv[1]; F = f'file://{S}/fuentes'
INK, AZ, CI, CIP, PAPEL = '#14213D', '#234899', '#00BDD0', '#009BB0', '#F6F8FC'
LINEA = 'M-6 63 L13 63 L27 12 L49 86 L71 25 L84 64 L106 64'
r = 21
# punta más larga y estrecha que en la ronda 3: a 24 px se lee como ubicación, no como globo de chat
PIN = f'M{r} 0 H{100-r} A{r} {r} 0 0 1 100 {r} V{100-r} A{r} {r} 0 0 1 {100-r} 100 H66 Q59 100 56 106 L50 119 L44 106 Q41 100 34 100 H{r} A{r} {r} 0 0 1 0 {100-r} V{r} A{r} {r} 0 0 1 {r} 0 Z'
n = [0]
def sym(fill, grad=None, linea=PAPEL, punta=None):
    n[0] += 1; u = f'k{n[0]}'
    defs = f'<clipPath id="c{u}"><path d="{PIN}"/></clipPath>'
    if grad: defs += f'<linearGradient id="g{u}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{grad[0]}"/><stop offset="1" stop-color="{grad[1]}"/></linearGradient>'
    f = f'url(#g{u})' if grad else fill
    body = f'<path d="{PIN}" fill="{f}"/>'
    if punta: body += f'<path clip-path="url(#c{u})" d="M30 100 H70 L50 120Z" fill="{punta}"/>'
    body += f'<path clip-path="url(#c{u})" d="{LINEA}" fill="none" stroke="{linea}" stroke-width="13" stroke-linejoin="round"/>'
    return f'<svg viewBox="-8 -8 116 132" xmlns="http://www.w3.org/2000/svg"><defs>{defs}</defs>{body}</svg>'
V = [
 ('A', 'Degradado azul → cian profundo', sym(None, (AZ, CIP)), 'Del azul MedicalManik arriba a la izquierda a un cian profundo abajo a la derecha. La línea blanca se lee en todo el recorrido (mínimo 3.3:1). Toma el degradado de tu logo original y lo vuelve propio del paciente.', True),
 ('B', 'Degradado azul → cian brillante', sym(None, (AZ, CI)), 'El degradado exacto del logo original. Más luminoso, pero en la esquina cian la línea blanca baja a 2.3:1 y se pierde a tamaño chico.', False),
 ('C', 'Cian profundo sólido', sym(CIP), 'Un solo color, sin degradado: más fácil de imprimir, bordar o poner en un sello de goma. Línea blanca a 3.3:1.', False),
 ('D', 'Azul con punta cian', sym(AZ, punta=CI), 'El cuerpo azul de la familia y la punta del pin en cian: el cian marca justo el «aquí».', False),
]
EXP = open('/home/user/fruti-squad/.fruti/icons/medicalmanik/final/svg/expediente.svg').read()
rows = ''
for k, nom, s, txt, rec in V:
    sz = ''.join(f'<span class="s" style="width:{z}px;height:{z}px">{s}</span>' for z in (120, 56, 32, 24))
    rows += f'''<section class="{"rec" if rec else ""}">{"<span class=r>Recomendado</span>" if rec else ""}<div class="hd"><h2>{k} · {nom}</h2><p>{txt}</p></div>
     <div class="row"><div class="sz">{sz}</div><div class="lk"><span class="s" style="width:60px;height:60px">{s}</span><span class="wm">manik</span><span class="end">de MedicalManik</span></div>
     <div class="vs"><span class="s" style="width:48px;height:48px">{EXP}</span><span class="s" style="width:48px;height:48px">{s}</span><small>junto a Expediente</small></div>
     <div class="dk"><span class="s" style="width:48px;height:48px">{s}</span><span class="wm s2">manik</span></div></div></section>'''
open('lamina.html', 'w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Sora';src:url('{F}/Sora[wght].ttf');font-weight:100 800}}@font-face{{font-family:'Inst';src:url('{F}/InstrumentSans[wdth,wght].ttf');font-weight:400 700}}
body{{margin:0;background:#F5F7FB;color:{INK};font:15px/1.45 Inst,sans-serif;padding:36px;width:1180px}}h1{{font:600 28px Sora;margin:0}}.i{{margin:4px 0 18px;color:#3E4A66;max-width:960px}}
section{{position:relative;background:#fff;border:1px solid #C9D1DF;border-radius:18px;padding:20px 22px;margin-bottom:16px;display:grid;gap:12px}}section.rec{{border:2px solid {AZ}}}.r{{position:absolute;top:-12px;left:18px;background:{AZ};color:#fff;font:600 12px Inst;padding:3px 10px;border-radius:99px}}
.hd h2{{margin:0;font:600 19px Sora}}.hd p{{margin:2px 0 0;color:#3E4A66}}
.row{{display:grid;grid-template-columns:auto auto auto 1fr;gap:30px;align-items:center}}.sz{{display:flex;gap:14px;align-items:end}}.s{{display:inline-block}}.s svg{{width:100%;height:100%;display:block}}
.lk{{display:flex;align-items:center;gap:10px}}.wm{{font:600 46px/1 Sora;letter-spacing:-.04em}}.end{{font:500 12.5px Inst;color:{AZ};border-left:1px solid #C9D1DF;padding-left:8px}}
.vs{{display:grid;grid-template-columns:auto auto;gap:4px 8px;justify-items:center}}.vs small{{grid-column:1/-1;color:#3E4A66;font-size:12px}}
.dk{{display:flex;align-items:center;gap:8px;background:#0F1C3F;border-radius:14px;padding:12px 16px;justify-self:start}}.dk .wm{{color:#fff;font-size:30px}}
</style></head><body><h1>Manik · el pin, con color propio</h1><p class="i">Ronda 4. El pin de la opción 2, separado del azul de Expediente. La punta es más larga que en la ronda anterior, para que se lea como ubicación y no como globo de chat. Cada opción aparece en tamaños, con el logotipo, junto a Expediente y sobre fondo oscuro.</p>{rows}</body></html>""")
print('ok')
