# Laranda · ronda 1 (fase 1 del brief): tres territorios en blanco y negro, a 16 y 512 px.
# A · la flor contenida (recomendado): 4–5 formas, un pétalo separado, punto negativo. B · la copa. C · la L que florece.
import sys,math
S=sys.argv[1]; INK='#1C1917'; CREMA='#FAF8F5'; VIOLETA='#6B4FA0'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
def petalo(cx,cy,ang,largo,ancho,k):
    # pétalo redondo: elipse con un extremo en el centro de la flor
    a=math.radians(ang); mx,my=cx+largo*.5*math.cos(a),cy+largo*.5*math.sin(a)
    return f'<ellipse cx="{mx:.1f}" cy="{my:.1f}" rx="{largo*.5:.1f}" ry="{ancho:.1f}" transform="rotate({ang} {mx:.1f} {my:.1f})" fill="{k}"/>'
# A1 · cuatro pétalos; el de arriba a la derecha se separa (gira 12° y se aleja 3 unidades); punto negativo al centro
def flor4(k=INK,fondo=CREMA,sep=True):
    b=''; cx,cy=32,34
    for i,ang in enumerate((-90,0,90,180)):
        if i==0 and sep:
            a=math.radians(-90+14); ox,oy=3.5*math.cos(a),3.5*math.sin(a)
            b+=petalo(cx+ox,cy+oy,-90+14,25,8.2,k)
        else: b+=petalo(cx,cy,ang,25,8.2,k)
    b+=f'<circle cx="{cx}" cy="{cy}" r="4.5" fill="{fondo}"/>'
    return svg(b)
# A2 · cinco pétalos (como la jacaranda), uno separado
def flor5(k=INK,fondo=CREMA,sep=True):
    b=''; cx,cy=32,34
    for i in range(5):
        ang=-90+i*72
        if i==0 and sep:
            a=math.radians(ang+14); b+=petalo(cx+3.5*math.cos(a),cy+3.5*math.sin(a),ang+14,25,7.2,k)
        else: b+=petalo(cx,cy,ang,25,7.2,k)
    b+=f'<circle cx="{cx}" cy="{cy}" r="5" fill="{fondo}"/>'
    return svg(b)
# A-16 · versión chica: tres pétalos gruesos + punto
def flor16(k=INK,fondo=CREMA):
    b=''; cx,cy=32,36
    for i,ang in enumerate((-90,30,150)):
        if i==0: a=math.radians(-90+18); b+=petalo(cx+4.5*math.cos(a),cy+4.5*math.sin(a),-90+18,27,11,k)
        else: b+=petalo(cx,cy,ang,27,11,k)
    b+=f'<circle cx="{cx}" cy="{cy}" r="6" fill="{fondo}"/>'
    return svg(b)
# B · la copa: semicírculo sobre tallo, con una muesca en L en negativo
def copa(k=INK,fondo=CREMA):
    return svg(f'<path d="M6 38 A26 26 0 0 1 58 38 Z" fill="{k}"/><rect x="29" y="38" width="6" height="16" rx="3" fill="{k}"/><path d="M24 24 V34 H34" stroke="{fondo}" stroke-width="4.5"/>')
# C · la L que florece: L con un brote (pétalo) en la punta del trazo vertical
def ele(k=INK,fondo=CREMA):
    return svg(f'<path d="M22 20 V52 H46" stroke="{k}" stroke-width="9"/>'+petalo(22,20,-55,20,7,k)+petalo(22,20,-125,16,5.5,k)+f'<circle cx="22" cy="20" r="3" fill="{fondo}"/>')
T={'A1 · flor de cuatro':flor4,'A2 · flor de cinco':flor5,'A · versión 16 px':flor16,'B · la copa':copa,'C · la L que florece':ele}
fr=S+'/fuentes/Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf'; mr=S+'/fuentes/Manrope[wght].ttf'
css=f'''@font-face{{font-family:FR;src:url("file://{fr}");font-weight:100 900}} @font-face{{font-family:MR;src:url("file://{mr}");font-weight:200 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 MR,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 17px MR;margin:0 0 8px}} .sub{{color:#57534E;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-bottom:22px}}
.celda{{background:{CREMA};padding:16px;border-radius:12px;border:1px solid #F0EBE3;display:grid;gap:10px;align-content:start}} svg{{display:block}}
.big svg{{width:150px;height:150px}} .s{{display:flex;gap:12px;align-items:flex-end}} .s span{{display:block}} .s svg{{width:100%;height:100%}}
.dark{{background:{INK};padding:10px;border-radius:8px;display:inline-flex;gap:10px;align-items:flex-end}}
.wm{{display:grid;grid-template-columns:1fr 1fr;gap:16px}} .wmc{{background:{CREMA};padding:18px;border-radius:12px;border:1px solid #F0EBE3;display:grid;gap:8px}}
.f1{{font:600 58px/1 FR;font-variation-settings:"opsz" 72,"SOFT" 60}} .f2{{font:600 54px/1 MR;letter-spacing:-.02em}} .tag{{font:400 12px MR;color:#57534E}}
.lock{{display:flex;align-items:center;gap:12px}} .lock svg{{width:48px;height:48px}} .lock .f1{{font-size:40px}} .lock .f2{{font-size:38px}}
.v{{display:grid;justify-items:center;gap:6px}} .v svg{{width:56px;height:56px}} .v .f1{{font-size:26px}} .v .f2{{font-size:24px}}'''
def inv(s): return s.replace(f'fill="{CREMA}"','fill="@F@"').replace(f'stroke="{CREMA}"','stroke="@S@"').replace(INK,CREMA).replace('@F@',INK).replace('@S@',INK)
cells=''
for name,fn in T.items():
    s=fn()
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big">{s}</div><div class="s"><span style="width:48px;height:48px">{s}</span><span style="width:32px;height:32px">{s}</span><span style="width:16px;height:16px">{s}</span><span class="dark"><span style="width:48px;height:48px">{inv(s)}</span><span style="width:16px;height:16px">{inv(s)}</span></span></div></div>'
wm=f'''<div class="wm"><div class="wmc"><h2>Wordmark · serif (Fraunces 600)</h2><div class="f1">laranda</div><div class="lock">{flor4()}<span class="f1">laranda</span></div><div class="v">{flor4()}<span class="f1">laranda</span></div><span class="tag">editorial, cálida; caja baja siempre</span></div>
<div class="wmc"><h2>Wordmark · sans humanista (Manrope 600)</h2><div class="f2">laranda</div><div class="lock">{flor4()}<span class="f2">laranda</span></div><div class="v">{flor4()}<span class="f2">laranda</span></div><span class="tag">más herramienta que editorial; decisión del cliente</span></div></div>'''
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Laranda · ronda 1 (fase 1 del brief) · tres territorios en blanco y negro: tinta #1C1917 sobre crema y en blanco sobre tinta, a 150, 48, 32 y 16 px. Abajo, las dos pruebas de wordmark con lockup horizontal y vertical.</p><div class="fila">{cells}</div>{wm}')
print('ok')
