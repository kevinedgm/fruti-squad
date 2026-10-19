# Xila · ronda 5: identidad con J (greca bordada): paleta Cobalto y dos pares tipográficos, en contexto de gráfica
import sys,glob,os
S=sys.argv[1]; F=lambda pat: glob.glob(S+'/fuentes/'+pat)[0].replace('%','%25')
MANTA,SURF,INK,INK2='#f6f1e8','#fffdf9','#15171f','#5b5f6e'; DBG,DSURF,DINK,DINK2='#15171f','#1e2130','#f6f1e8','#a9adbd'
COB,COBD='#1f4bd8','#7a9bff'; HILO,HILOD='#d14e0a','#ff8a3d'; HILO_T='#ad3f09'
CAT=[('cobalto','#1f4bd8','#7a9bff'),('hilo','#d14e0a','#ff8a3d'),('jade','#0b6f71','#3fc1c3'),('morado','#7b4fd1','#b49cff'),('ocre','#7d6300','#e3c23a'),('grana','#c2275d','#ff6b9a'),('piedra','#6b7280','#9aa0ad')]
GRECA={(0,8),(1,8),(2,8),(2,7),(2,6),(3,6),(4,6),(4,5),(4,4),(5,4),(6,4),(6,3),(6,2),(7,2),(8,2),(8,1),(8,0)}
def cruz(x,y,c,s=2.4,w=1.9): return f'<path d="M{x-s} {y-s} L{x+s} {y+s} M{x+s} {y-s} L{x-s} {y+s}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
def greca(dark=False):
    ink=DINK if dark else INK; cob=COBD if dark else COB
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">'+''.join(cruz(8+i*6,8+j*6,cob if (i,j)==(8,0) else ink) for (i,j) in GRECA)+'</svg>'
def chart(dark=False,disp='Fraunces',ui='ISans',mono='JBM'):
    bg=DSURF if dark else SURF; ink=DINK if dark else INK; ink2=DINK2 if dark else INK2; cob=COBD if dark else COB; cats=[c[2] if dark else c[1] for c in CAT]
    grid=''.join(f'<path d="M40 {y} H300" stroke="{ink2}" stroke-width="1" opacity=".35"/>' for y in (40,70,100,130))
    line=f'<path d="M40 118 C80 110 100 96 140 92 S200 70 240 62 S280 48 300 44" stroke="{cob}" stroke-width="2" fill="none"/><circle cx="300" cy="44" r="4" fill="{cob}" stroke="{bg}" stroke-width="2"/><text x="308" y="48" font-family="{mono}" font-size="11" font-weight="600" fill="{ink}">12.4</text><text x="308" y="62" font-family="{ui}" font-size="10" fill="{ink2}">rendimiento</text>'
    bars=''.join(f'<rect x="{40+i*22}" y="{130-h}" width="12" height="{h}" rx="6" fill="{cats[i]}"/>' for i,h in enumerate([34,52,28,60,44,38,50]))
    return f'''<div style="background:{bg};border-radius:14px;padding:20px 22px;color:{ink};width:420px">
<div style="font:600 19px/1.2 {disp};letter-spacing:-.01em;margin-bottom:4px">El rendimiento subió 12 % tras la poda</div>
<div style="font:400 12px {ui};color:{ink2};margin-bottom:10px">Brix por semana · 7 parcelas · 2026</div>
<svg viewBox="0 0 360 150" style="width:100%;display:block">{grid}{line}<text x="40" y="146" font-family="{ui}" font-size="10" fill="{ink2}">ene</text><text x="285" y="146" font-family="{ui}" font-size="10" fill="{ink2}">oct</text></svg>
<svg viewBox="0 0 360 140" style="width:100%;display:block;margin-top:8px">{bars}<text x="40" y="146" font-family="{ui}" font-size="10" fill="{ink2}"></text></svg></div>'''
def swatch(name,l,d,note):
    return f'<div style="display:grid;gap:6px"><div style="display:flex;border-radius:10px;overflow:hidden;height:56px"><div style="flex:1;background:{l}"></div><div style="flex:1;background:{d}"></div></div><b style="font:600 13px ISans">{name}</b><span style="font:400 11px JBM;color:{INK2}">{l} · {d}</span><span style="font:400 11px ISans;color:{INK2}">{note}</span></div>'
css=f'''@font-face{{font-family:Fraunces;src:url("file://{F('Fraunces*')}");font-weight:100 900}}@font-face{{font-family:Newsreader;src:url("file://{F('Newsreader*')}");font-weight:200 800}}
@font-face{{font-family:ISans;src:url("file://{F('InstrumentSans*')}");font-weight:400 700}}@font-face{{font-family:SG;src:url("file://{F('SpaceGrotesk*')}");font-weight:300 700}}@font-face{{font-family:JBM;src:url("file://{F('JetBrainsMono*')}");font-weight:100 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.45 ISans,system-ui;width:1200px;box-sizing:border-box;display:grid;gap:30px}}
h2{{font:700 17px ISans;margin:0 0 10px}} .sub{{color:#666;margin:0}}
.sw{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}} .cat{{display:grid;grid-template-columns:repeat(7,1fr);gap:10px}}
.par{{display:grid;grid-template-columns:1fr 1fr;gap:24px}} .lock{{display:flex;align-items:center;gap:14px}} .lock svg{{width:52px;height:52px}}
.tag{{font:400 12px ISans;color:#666}} .heat{{height:28px;border-radius:8px;background:linear-gradient(90deg,{MANTA},#9fb3e8 45%,#1f4bd8 75%,#0b1f5c)}}'''
H=f'''<!doctype html><meta charset="utf-8"><style>{css}</style>
<section><h2>Símbolo elegido: J · greca bordada</h2><div style="display:flex;gap:28px;align-items:center"><div class="lock" style="background:{MANTA};padding:16px 22px;border-radius:14px">{greca()}<b style="font:700 40px ISans;letter-spacing:-.02em">xila</b></div><div class="lock" style="background:{DBG};padding:16px 22px;border-radius:14px;color:{DINK}">{greca(True)}<b style="font:700 40px ISans;letter-spacing:-.02em">xila</b></div><div class="lock" style="background:{MANTA};padding:16px 22px;border-radius:14px">{greca()}<b style="font:600 44px Fraunces;letter-spacing:-.01em;font-variation-settings:'opsz' 72,'SOFT' 60">xila</b></div><div class="lock" style="background:{MANTA};padding:16px 22px;border-radius:14px">{greca()}<b style="font:500 44px Newsreader;letter-spacing:-.01em;font-variation-settings:'opsz' 48">xila</b></div></div><p class="tag" style="margin-top:8px">nombre en sans (Instrument Sans 700) · en Fraunces 600 · en Newsreader 500</p></section>
<section><h2>Paleta Cobalto · base</h2><div class="sw">{swatch('Manta',MANTA,DBG,'fondo: el algodón crudo del huipil · en oscuro, la tinta')}{swatch('Tinta',INK,DINK,'texto y puntadas · 15.9:1 sobre manta en los dos modos')}{swatch('Cobalto',COB,COBD,'principal: línea, selección, el dato · 6.1:1 · 6.8:1')}{swatch('Hilo',HILO,HILOD,'acento del bordado (naranja del huipil) · como gráfico 3.9:1; como texto en claro usar '+HILO_T+' (4.5:1)')}</div>
<h2 style="margin-top:18px">Categórica de siete (gráficos, ≥3:1 en los dos modos)</h2><div class="cat">{''.join(swatch(n,l,d,'') for n,l,d in CAT)}</div>
<h2 style="margin-top:18px">Heatmap · de manta a marino</h2><div class="heat"></div><p class="tag">{MANTA} → #9fb3e8 → {COB} → #0b1f5c (marino, 13.7:1 sobre manta)</p></section>
<section><h2>Par tipográfico 1 · «Editorial»: Fraunces (hallazgo) + Instrument Sans (interfaz) + JetBrains Mono (cifras)</h2><div class="par">{chart(False)}{chart(True)}</div></section>
<section><h2>Par tipográfico 2 · «Periódico»: Newsreader (hallazgo) + Space Grotesk (interfaz y cifras tabulares)</h2><div class="par">{chart(False,'Newsreader','SG','SG')}{chart(True,'Newsreader','SG','SG')}</div></section>'''
open('muestra.html','w').write(H); print('ok')
