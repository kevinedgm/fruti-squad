# Laranda · ronda 9 · superficie y botones: tres direcciones más pulcras y editoriales, en la misma pantalla (perfil público).
import sys
S=sys.argv[1]
F='/home/user/fruti-squad/.fruti/icons/laranda/final/svg/'
VIO='#5B3BB5'; NAR='#E0611A'; ORO='#D9A400'; VERDE='#0E8F5E'; ROJO='#A8202F'
lock=open(F+'lockup-h.svg').read(); sil=open(F+'silueta.svg').read()
O=[dict(n='A · Blanco editorial',bg='#FFFFFF',surf='#FFFFFF',sunk='#F3F3F1',ink='#111013',muted='#5C5A61',line='#E4E3E0',r='8px',rb='6px',prim='#111013',onprim='#FFFFFF',sec_border='#111013',
   nota='Fondo blanco, superficies separadas solo por líneas finas. Botón primario en tinta; el violeta queda para la marca, enlaces y foco. Reservar en oro con texto en tinta. Radios chicos. Etiquetas en versalitas.',caps=True),
 dict(n='B · Papel frío',bg='#F2F2F0',surf='#FFFFFF',sunk='#E9E9E6',ink='#15121C',muted='#55535C',line='#DCDCD8',r='10px',rb='8px',prim=VIO,onprim='#FFFFFF',sec_border='#15121C',
   nota='Fondo gris muy claro y tarjetas blancas: contraste de planos sin bordes gruesos. Primario en violeta. Radios medios. Sin versalitas.',caps=False),
 dict(n='C · Tinta y aire',bg='#FFFFFF',surf='#FFFFFF',sunk='#F6F6F4',ink='#111013',muted='#5C5A61',line='#111013',r='0px',rb='4px',prim='#111013',onprim='#FFFFFF',sec_border='#111013',
   nota='Casi sin radios, reglas de 1 px en tinta como en una revista, mucho aire. El más editorial y el más arriesgado en móvil.',caps=True)]
css=f'''@font-face{{font-family:BR;src:url("file://{S}/fuentes/BricolageGrotesque[opsz,wdth,wght].ttf");font-weight:200 800}} @font-face{{font-family:ON;src:url("file://{S}/fuentes/Onest.ttf");font-weight:100 900}} @font-face{{font-family:PM;src:url("file://{S}/fuentes/IBMPlexMono.ttf");font-weight:500}}
body{{margin:0;padding:28px;background:#ddd;color:#111;font:13px ON,system-ui;width:1200px;box-sizing:border-box}} .sub{{margin:0 0 14px;color:#333}}
.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}} .op{{display:grid;gap:10px}} .op h2{{font:700 15px ON;margin:0}} .op .nota{{font:400 12px ON;color:#333}}
.ph{{width:360px;height:720px;border-radius:28px;overflow:hidden;border:6px solid #222;display:grid;grid-template-rows:auto 1fr auto}}
.top{{display:flex;align-items:center;justify-content:space-between;padding:14px 16px}} .top svg{{height:26px;width:auto;display:block}}
.body{{padding:0 16px;display:grid;gap:16px;align-content:start;overflow:hidden}}
.hero{{display:grid;gap:10px}} .foto{{height:160px;border-radius:var(--r);background:linear-gradient(135deg,#c9c3b8,#9a948a)}}
h1{{font:700 26px/30px BR;margin:0;letter-spacing:-.01em}} .cap{{font:500 11px ON;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}} .cap.lo{{text-transform:none;letter-spacing:0;font-size:13px}}
.chips{{display:flex;gap:6px;flex-wrap:wrap}} .chip{{display:inline-flex;align-items:center;gap:6px;font:600 12px ON;padding:5px 10px;border-radius:var(--rb);border:1px solid var(--line);background:var(--surf);color:var(--ink)}} .chip svg{{width:14px;height:14px;display:block}} .chip.v{{color:{VIO};border-color:{VIO}}}
p{{margin:0;font:400 15px/22px ON;color:var(--muted)}}
.row{{display:grid;grid-template-columns:1fr 1fr;gap:10px}} .cardi{{border:1px solid var(--line);border-radius:var(--r);padding:12px;background:var(--surf);display:grid;gap:4px}} .cardi b{{font:700 15px ON}} .cardi span{{font:400 12px ON;color:var(--muted)}}
.btns{{display:grid;gap:10px}} .btn{{display:flex;align-items:center;justify-content:center;min-height:48px;border-radius:var(--rb);font:700 15px ON;border:1px solid transparent}}
.reserve{{background:{ORO};color:#15121C}} .prim{{background:var(--prim);color:var(--onprim)}} .sec{{background:transparent;color:var(--ink);border-color:var(--sec)}} .lnk{{color:{NAR};font:700 14px ON;text-align:center}}
.est{{display:flex;gap:8px;align-items:center;font:500 13px ON;color:{VIO}}} .est svg{{width:16px;height:16px}}
.nav{{display:flex;border-top:1px solid var(--line);padding:8px 0 12px;background:var(--surf)}} .nav a{{flex:1;text-align:center;font:500 11px ON;color:var(--muted)}} .nav a.on{{color:{VIO}}}
.folio{{border:1px solid var(--line);border-radius:var(--r);padding:10px 12px;font:500 12px/18px PM;background:var(--sunk)}}
'''
cells=''
for o in O:
    st=f"--r:{o['r']};--rb:{o['rb']};--surf:{o['surf']};--sunk:{o['sunk']};--line:{o['line']};--muted:{o['muted']};--ink:{o['ink']};--prim:{o['prim']};--onprim:{o['onprim']};--sec:{o['sec_border']};background:{o['bg']};color:{o['ink']}"
    cap='cap' if o['caps'] else 'cap lo'
    lk=lock.replace('#15121C',o['ink'])
    cells+=f'''<div class="op"><h2>{o['n']}</h2><span class="nota">{o['nota']}</span><div class="ph" style="{st}"><div class="top">{lk}<span class="{cap}">Perfil</span></div><div class="body">
<div class="hero"><div class="foto"></div><span class="{cap}">Barbería · Centro, Oaxaca</span><h1>Andrés Cortés</h1><div class="chips"><span class="chip v">{sil.replace('#5B3BB5',VIO)}Barbería</span><span class="chip">Afeitado clásico</span><span class="chip">Barba</span></div><p>Corte, barba y navaja. Lunes a sábado. Responde en 1 h.</p></div>
<div class="row"><div class="cardi"><span class="{cap}">Próximo espacio</span><b>vie 24 oct · 16:00</b></div><div class="cardi"><span class="{cap}">Desde</span><b>$350</b><span>★ 4.9 · 128 reseñas</span></div></div>
<div class="btns"><a class="btn reserve">Reservar</a><a class="btn sec">Ver agenda completa</a><span class="lnk">Compartir perfil</span></div>
<div class="folio">FOLIO LR-2026-00417 · 24 oct · 16:00 · $350.00</div>
<div class="est">{sil}<span>Perfil verificado</span></div>
</div><div class="nav"><a class="on">Hoy</a><a>Agenda</a><a>Perfil</a><a>Folios</a></div></div></div>'''
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Laranda · ronda 9 · superficie y botones. Misma pantalla (perfil público, 360 px) en tres direcciones. Marca, violeta, naranja y oro no cambian; cambian fondo, superficie, bordes, radios y el color del botón primario.</p><div class="g">{cells}</div>')
print('ok')
